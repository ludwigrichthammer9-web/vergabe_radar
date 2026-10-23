"""Zuordnung Ausschreibung → objektgleicher Vorgänger über Objektmerkmale (Iteration 3, Schritt 3).

Vorgänger-Quellen: Zuschläge und frühere Ausschreibungen (ohne Änderungsbekanntmachungen) mit CPV 909 seit Oktober 2016,
veröffentlicht vor der Ausschreibung und nicht aus demselben Verfahren.

Kandidaten:
- Auftraggeber ähnlich: gleicher normalisierter Name, Jaccard der kennzeichnenden Namenswörter >= BUYER_MIN oder Überlappung
  (gemeinsame / kleinere Wortmenge, mindestens 2 Wörter) >= BUYER_OVERLAP, oder
- (nur eForms) gleiche PLZ des Leistungsorts und mindestens eine gemeinsame Straße oder ein gemeinsames kennzeichnendes Titelwort.
Für Kandidaten vor eForms wird die Original-XML gelesen, höchstens XML_CAP je Ausschreibung (bevorzugt gleicher Ort, dann die jüngsten).

Objektwörter = kennzeichnende Titel-/Ortswörter ohne Namen und Sitz des Auftraggebers (`object_words`).
Treffer (ohne Zeitfenster):
- Stufe T: Auftraggeber ähnlich und wortgleicher Titel, der mindestens ein kennzeichnendes Wort enthält
- Stufe A: gemeinsame Straße und gleiche PLZ und mindestens ein gemeinsames Objektwort
- Stufe B: Auftraggeber ähnlich und (mindestens 2 gemeinsame Objektwörter oder Jaccard der Objektwörter >= WORDS_MIN)
Bester Kandidat: T vor A vor B, dann höhere Wortähnlichkeit, dann jüngere Veröffentlichung. 1:1: Jeder Vorgänger höchstens einmal.

Aufruf:
    .venv\\Scripts\\python src/zuordnung_objekt.py --dev        # Entwicklungsdaten Q2 2026 (Stichprobe), Kandidatenliste zum Abstimmen
    .venv\\Scripts\\python src/zuordnung_objekt.py --test FILE  # eingefrorene Regel auf Testfälle (Liste von Notice-Nummern)
"""

import argparse
import json
import random
import sys
from pathlib import Path

from analyze_completeness import RAW_SEARCH_DIR, load_notices
from objekt_merkmale import Merkmale, from_api, from_xml, has_object_fields, norm, object_words
from population_iteration3 import exclusion_reason, title

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEV_RUN = "DEU_competition_cpv9091main_20260401_20260630"
TEST_RUN = "DEU_competition_cpv9091main_20260701_20260930"
POOL_RUNS = ("DEU_result_cpv909_20161001_20260930", "DEU_competition_cpv909_20161001_20260930")

BUYER_MIN = 0.6
BUYER_OVERLAP = 0.8
WORDS_MIN = 0.67
XML_CAP = 25
DEV_SEED = 20261023
DEV_SAMPLE = 40


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def pub_date(n: dict) -> str:
    return str(n.get("publication-date", ""))[:10]


class Pool:
    def __init__(self) -> None:
        notices = {}
        for run in POOL_RUNS:
            for n in load_notices(RAW_SEARCH_DIR / run):
                if not n.get("change-notice-version-identifier"):
                    notices[n["publication-number"]] = n
        self.notices = notices
        self.api = {pn: from_api(n) for pn, n in notices.items()}
        self.by_buyer_word: dict[str, set[str]] = {}
        self.by_buyer_name: dict[str, set[str]] = {}
        self.by_plz: dict[str, set[str]] = {}
        for pn, m in self.api.items():
            for w in m.buyer_words:
                self.by_buyer_word.setdefault(w, set()).add(pn)
            for nm in m.buyer_names:
                self.by_buyer_name.setdefault(nm, set()).add(pn)
            for p in m.plz:
                self.by_plz.setdefault(p, set()).add(pn)
        self.xml_cache: dict[str, Merkmale] = {}

    def features(self, pn: str) -> Merkmale:
        n = self.notices[pn]
        if has_object_fields(n):
            return self.api[pn]
        if pn not in self.xml_cache:
            self.xml_cache[pn] = from_xml(n)
        return self.xml_cache[pn]


def buyer_similar(a: Merkmale, b: Merkmale) -> bool:
    if a.buyer_names & b.buyer_names or jaccard(a.buyer_words, b.buyer_words) >= BUYER_MIN:
        return True
    small = min(len(a.buyer_words), len(b.buyer_words))
    return small >= 2 and len(a.buyer_words & b.buyer_words) / small >= BUYER_OVERLAP


def candidates(comp: dict, fc: Merkmale, pool: Pool) -> list[dict]:
    c_date, c_proc = pub_date(comp), comp.get("procedure-identifier")
    ids = set()
    for nm in fc.buyer_names:
        ids |= pool.by_buyer_name.get(nm, set())
    for w in fc.buyer_words:
        ids |= pool.by_buyer_word.get(w, set())
    by_place = set()
    for p in fc.plz:
        by_place |= pool.by_plz.get(p, set())
    out, old = [], []
    for pn in ids | by_place:
        n = pool.notices[pn]
        if pub_date(n) >= c_date or (c_proc and n.get("procedure-identifier") == c_proc):
            continue
        fa = pool.api[pn]
        b_sim = buyer_similar(fc, fa)
        if has_object_fields(n):
            place = bool(fc.plz & fa.plz) and bool((fc.streets & fa.streets) or (fc.words & fa.words))
            if b_sim or place:
                out.append({"pn": pn, "buyer_similar": b_sim})
        elif b_sim:
            old.append({"pn": pn, "buyer_similar": True, "same_city": bool(fc.cities & fa.cities)})
    old.sort(key=lambda c: (c["same_city"], pub_date(pool.notices[c["pn"]])), reverse=True)
    return out + old[:XML_CAP]


def score(fc: Merkmale, fk: Merkmale, cand: dict) -> dict:
    street = bool(fc.streets & fk.streets)
    plz = bool(fc.plz & fk.plz)
    oc, ok = object_words(fc), object_words(fk)
    common = oc & ok
    words = jaccard(oc, ok)
    same_title = bool(fc.title) and norm(fc.title) == norm(fk.title) and bool(fc.words)
    if cand["buyer_similar"] and same_title:
        level = "T"
    elif street and plz and common:
        level = "A"
    elif cand["buyer_similar"] and (len(common) >= 2 or words >= WORDS_MIN):
        level = "B"
    else:
        level = ""
    return {**cand, "street": street, "plz": plz, "words": round(words, 3), "level": level,
            "common_words": sorted(common)[:8], "common_streets": sorted(fc.streets & fk.streets)}


LEVEL_ORDER = {"T": 3, "A": 2, "B": 1, "": 0}


def rank(scored: list[dict], pool: Pool) -> list[dict]:
    return sorted(scored, key=lambda s: (LEVEL_ORDER[s["level"]], s["words"], pub_date(pool.notices[s["pn"]])), reverse=True)


def match_all(comps: list[dict], pool: Pool) -> list[dict]:
    """Beste Zuordnung je Ausschreibung mit 1:1-Bedingung (stärkste Treffer zuerst vergeben)."""
    ranked = {}
    for c in comps:
        fc = from_api(c)
        scored = [score(fc, pool.features(k["pn"]), k) for k in candidates(c, fc, pool)]
        ranked[c["publication-number"]] = (fc, [s for s in rank(scored, pool) if s["level"]], len(scored))
    def strength(pn: str) -> tuple:
        hits = ranked[pn][1]
        return (LEVEL_ORDER[hits[0]["level"]], hits[0]["words"]) if hits else (0, -1)

    order = sorted(ranked, key=strength, reverse=True)
    used, result = set(), {}
    for pn in order:
        fc, hits, n_cand = ranked[pn]
        best = next((h for h in hits if h["pn"] not in used), None)
        if best:
            used.add(best["pn"])
        result[pn] = {"comp": pn, "n_candidates": n_cand, "n_hits": len(hits), "best": best, "comp_title": fc.title}
    return [result[c["publication-number"]] for c in comps]


def describe(pool: Pool, pn: str) -> str:
    n, f = pool.notices[pn], pool.features(pn)
    era = "eForms" if has_object_fields(n) else "vor eForms"
    return (f"{pn} ({pub_date(n)}, {n.get('form-type')}, {era}) – {next(iter(f.buyer_names), '')[:60]} – „{f.title[:90]}“ "
            f"| PLZ {sorted(f.plz)[:4]} | Straßen {sorted(f.streets)[:4]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dev", action="store_true")
    parser.add_argument("--test", help="Datei mit Notice-Nummern der Testfälle (eine pro Zeile)")
    parser.add_argument("--out", help="JSON-Ausgabe der Zuordnungen")
    parser.add_argument("--extra", default="", help="zusätzliche Dev-Fälle, kommagetrennt")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    pool = Pool()
    if args.dev:
        comps = [n for n in load_notices(RAW_SEARCH_DIR / DEV_RUN) if exclusion_reason(n) is None]
        rng = random.Random(DEV_SEED)
        sample = rng.sample(comps, DEV_SAMPLE)
        extra = {x for x in args.extra.split(",") if x}
        sample += [c for c in comps if c["publication-number"] in extra and c not in sample]
    elif args.test:
        wanted = [line.strip() for line in Path(args.test).read_text(encoding="utf-8").splitlines() if line.strip()]
        comps_by = {n["publication-number"]: n for n in load_notices(RAW_SEARCH_DIR / TEST_RUN)}
        sample = [comps_by[w] for w in wanted]
    else:
        sys.exit("--dev oder --test angeben")

    results = match_all(sample, pool)
    for c, r in zip(sample, results):
        fc = from_api(c)
        print(f"\n## {c['publication-number']} ({pub_date(c)}) – {next(iter(fc.buyer_names), '')[:60]} – „{title(c)[:90]}“")
        print(f"   PLZ {sorted(fc.plz)[:4]} | Straßen {sorted(fc.streets)[:4]} | Objektwörter {sorted(object_words(fc))[:8]}")
        print(f"   Kandidaten {r['n_candidates']}, Treffer {r['n_hits']}")
        if r["best"]:
            b = r["best"]
            print(f"   → Stufe {b['level']} words={b['words']} street={b['street']} plz={b['plz']} gemeinsam={b['common_words']} "
                  f"{b['common_streets']}")
            print(f"     {describe(pool, b['pn'])}")
        else:
            print("   → kein Vorgänger")
    if args.out:
        Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
