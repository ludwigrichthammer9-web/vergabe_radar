"""Zuordnung Ausschreibung → objektgleicher Vorgänger über Merkmale je Los (Iteration 4, Schritt 3).

Ersetzt für Iteration 4 `zuordnung_objekt.py` (bleibt als eingefrorene Regel von Iteration 3 unverändert). Läuft ohne pandas.

Vorgänger-Quellen: Zuschläge und frühere Ausschreibungen mit CPV 909 seit Oktober 2016 (ohne Änderungsbekanntmachungen),
veröffentlicht vor der Ausschreibung und nicht aus demselben Verfahren. Merkmale aus `los_merkmale.py` (eForms über die API mit
Los-Texten, vor eForms über die XML).

Kandidaten je Ausschreibung:
- Auftraggeber ähnlich (wie Iteration 3: gleicher Name, Jaccard ≥ BUYER_MIN oder Überlappung ≥ BUYER_OVERLAP), oder
- gleiche PLZ des Leistungsorts (eForms), oder
- Treffer der Volltextsuche: eine Abfrage `FT~"<Name oder Adresse>"` (höchstens FT_TERMS Begriffe, ODER-verknüpft) mit CPV 909 und
  Datum vor der Ausschreibung. Antworten unverändert unter data/raw/ted_ft/<Ausschreibung>.json.
Vor eForms höchstens XML_CAP Kandidaten mit XML (zuerst Volltexttreffer, dann gleicher Ort, dann jüngste).

Vergleich (Logik der Urteilsregeln 1.1, ohne Zeitabstand):
- Widerspruch Leistungsart: Kernarten (Unterhalt, Glas, Treppenhaus, Bau) beider Seiten ohne Schnittmenge, oder Kandidat nur Bau.
- Identität = Objektnamen ∪ Adressen. Anteil gemeinsamer Merkmale an der kürzeren (r_kurz) und längeren Seite (r_lang).
- Fläche: gleiche Art, Abweichung ≤ 2 %.
- Kategorie: „objekt“ (r_kurz ≥ 0,5), „unklar“ (gemeinsam, r_kurz < 0,5, oder nur Fläche), „geschwister“ (Auftraggeber ähnlich,
  beide mit Objekten, keine Überschneidung über 20 %), „nein“ (Widerspruch oder nichts gemeinsam).
- Rangliste (W6): alle Kandidaten ohne Widerspruch und nicht „geschwister“, nach Punktzahl, dann jünger; höchstens TOP_N.
- Vorschlag (W2/W3): bester Kandidat der Kategorie „objekt“. Kein Zeitfenster.

Aufruf:
    .venv\\Scripts\\python src/zuordnung_los.py --dev-q3                 # Entwicklung: 60 Fälle Q3 2026 gegen die Handsuche
    .venv\\Scripts\\python src/zuordnung_los.py --dev-q2 40              # Entwicklung: Stichprobe Q2 2026 (ohne Maßstab)
    .venv\\Scripts\\python src/zuordnung_los.py --test FILE --out JSON    # eingefrorene Regel auf Testfälle (Lauf Q1 2026, --run)
"""

import argparse
import csv
import hashlib
import json
import random
import re
import sys
import time
from pathlib import Path

import requests

from los_merkmale import Bekanntmachung, bekanntmachung, has_text_fields, norm
from population_iteration4 import exclusion_reason, flatten

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW = PROJECT_ROOT / "data" / "raw" / "ted_search"
FT_DIR = PROJECT_ROOT / "data" / "raw" / "ted_ft"
API_URL = "https://api.ted.europa.eu/v3/notices/search"
Q1_SEEN = PROJECT_ROOT / "reports" / "dev_gesehene_q1_notices.txt"

POOL_RUNS = ("DEU_result_cpv909_20161001_20260930", "DEU_competition_cpv909_20161001_20260930")
TEXT_RUNS = ("DEU_result_cpv909_20231025_20260930_lostext", "DEU_competition_cpv909_20231025_20260930_lostext")
DEV_Q2 = "DEU_competition_cpv9091main_20260401_20260630_lostext"
DEV_Q3 = "DEU_competition_cpv9091main_20260701_20260930_lostext"

BUYER_MIN = 0.6
BUYER_OVERLAP = 0.8
XML_CAP = 40
FT_TERMS = 6
RARE_WORD = 50  # Namenswort in höchstens so vielen Pool-Notices: Kandidat auch ohne ähnlichen Auftraggeber
FT_LIMIT = 100
TOP_N = 3
AREA_TOL = 0.02
R_OBJEKT = 0.5
R_GESCHWISTER = 0.2
KERN = {"unterhalt", "glas", "treppenhaus", "bau"}
DEV_Q2_SEED = 20261025

BUYER_GENERIC = set("""
stadt gemeinde landkreis kreis amt aemter der die das des fuer und von land freistaat bundesrepublik deutschland vertreten durch
vertreten verwaltung stadtverwaltung kreisverwaltung buergermeister oberbuergermeister landrat landratsamt magistrat zentrale vergabestelle
vergabestelle zentraler einkauf beschaffung beschaffungsamt fachbereich abteilung referat dezernat eigenbetrieb gmbh mbh ag aoer ev e v
hansestadt kreisstadt grosse landeshauptstadt bundesanstalt anstalt oeffentlichen rechts koerperschaft
""".split())  # wie objekt_merkmale.BUYER_GENERIC (Iteration 3)
# Titelwörter ohne Aussage über das Objekt (Auszug aus objekt_merkmale.GENERIC, Iteration 3)
TITLE_GENERIC = set("""
reinigung reinigungen reinigungsleistung reinigungsleistungen reinigungsdienstleistung reinigungsdienstleistungen unterhaltsreinigung
unterhalts glasreinigung glas grundreinigung grund gebaeudereinigung gebaeudereinigungsleistungen fensterreinigung fenster rahmenreinigung
sonderreinigung innenglasreinigung aussenglasreinigung leistung leistungen dienstleistung dienstleistungen vergabe ausschreibung offenes
offene verfahren eu weit los lose losen rahmenvertrag rahmenvereinbarung vertrag durchfuehrung erbringung fuer und der die das des den
dem von im in am an zur zum mit sowie bzw ab bis inkl diverse verschiedene verschiedenen objekte objekten objekt gebaeude gebaeuden
liegenschaft liegenschaften standort standorte staedtische staedtischer einrichtungen stadt gemeinde landkreis
""".split())
# Merkmal bei mindestens 4 und 40 % der Kandidaten: vermutlich Anschrift des Auftraggebers. Nur bei Fällen mit vielen Kandidaten,
# weil bei Einzelstandorten (z. B. eine Hochschule) die Objektadresse zu Recht in jeder Bekanntmachung steht.
FREQ_MIN, FREQ_SHARE, FREQ_CANDIDATES = 4, 0.4, 15


def pub_date(n: dict) -> str:
    return str(n.get("publication-date", ""))[:10]


def texts(value) -> list[str]:
    if isinstance(value, dict):
        value = value.get("deu") or next(iter(value.values()), [])
    return [str(v) for v in flatten(value) if str(v).strip()]


def buyer_words(n: dict) -> tuple[set[str], set[str]]:
    names = {norm(x) for x in texts(n.get("buyer-name"))}
    words = {w for x in names for w in x.split() if len(w) > 2 and w not in BUYER_GENERIC and not w.isdigit()}
    return names, words


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def buyer_similar(a: tuple[set, set], b: tuple[set, set]) -> bool:
    if a[0] & b[0] or jaccard(a[1], b[1]) >= BUYER_MIN:
        return True
    small = min(len(a[1]), len(b[1]))
    return small >= 2 and len(a[1] & b[1]) / small >= BUYER_OVERLAP


def load_run(run: str) -> list[dict]:
    out = []
    for f in sorted((RAW / run).glob("page_*.json")):
        out += json.loads(f.read_bytes().decode("utf-8")).get("notices", [])
    return out


class Pool:
    def __init__(self) -> None:
        self.notices: dict[str, dict] = {}
        for run in POOL_RUNS + TEXT_RUNS:  # Läufe mit Los-Texten zuletzt, sie ersetzen die Fassung ohne Beschreibung
            for n in load_run(run):
                if not n.get("change-notice-version-identifier") and n.get("form-type") in ("result", "competition"):
                    self.notices[n["publication-number"]] = n
        self.buyer = {pn: buyer_words(n) for pn, n in self.notices.items()}
        self.by_word: dict[str, set[str]] = {}
        self.by_name: dict[str, set[str]] = {}
        self.by_plz: dict[str, set[str]] = {}
        for pn, (names, words) in self.buyer.items():
            for w in words:
                self.by_word.setdefault(w, set()).add(pn)
            for nm in names:
                self.by_name.setdefault(nm, set()).add(pn)
            for p in texts(self.notices[pn].get("place-of-performance-post-code-lot")):
                self.by_plz.setdefault(p, set()).add(pn)
        self.cache: dict[str, Bekanntmachung] = {}

    def features(self, pn: str) -> Bekanntmachung:
        if pn not in self.cache:
            self.cache[pn] = bekanntmachung(self.notices[pn])
        return self.cache[pn]


def ft_search(case: Bekanntmachung) -> list[str]:
    """Volltextsuche nach Namen und Adressen des Falls; Antwort unverändert gespeichert und wiederverwendet."""
    terms = sorted(case.alle("roh"), key=lambda t: (-len(t.split()), -len(t)))[:FT_TERMS]
    if not terms:
        return []
    FT_DIR.mkdir(parents=True, exist_ok=True)
    before = case.datum.replace("-", "")
    query = "(" + " OR ".join(f'FT~"{t}"' for t in terms) + f") AND classification-cpv=909* AND publication-date<{before}"
    # Dateiname je Abfrage, damit geänderte Suchbegriffe nicht eine ältere Antwort wiederverwenden
    path = FT_DIR / f"{case.nr}_{hashlib.sha1(query.encode('utf-8')).hexdigest()[:8]}.json"
    if not path.exists():
        body = {"query": query, "fields": ["publication-number", "publication-date", "form-type"], "limit": FT_LIMIT,
                "page": 1, "scope": "ALL", "paginationMode": "PAGE_NUMBER"}
        for attempt in range(4):
            resp = requests.post(API_URL, json=body, timeout=120)
            if resp.status_code == 200:
                break
            time.sleep(2 ** (attempt + 1))
        else:
            return []
        path.with_suffix(".request.json").write_text(json.dumps(body, ensure_ascii=False, indent=1), encoding="utf-8")
        path.write_bytes(resp.content)
        time.sleep(0.5)
    data = json.loads(path.read_bytes().decode("utf-8"))
    return [n["publication-number"] for n in data.get("notices", [])]


def candidates(notice: dict, case: Bekanntmachung, pool: Pool) -> list[dict]:
    c_date, c_proc = pub_date(notice), notice.get("procedure-identifier")
    cb = buyer_words(notice)
    by_buyer = set()
    for nm in cb[0]:
        by_buyer |= pool.by_name.get(nm, set())
    weak = set()  # gemeinsames seltenes Namenswort (z. B. Schreibvariante „Gemeinde Oststeinbek (Kreis Stormarn)“)
    for w in cb[1]:
        ids = pool.by_word.get(w, set())
        by_buyer |= ids
        if len(ids) <= RARE_WORD:
            weak |= ids
    by_plz = set()
    for p in case.alle("plz"):
        by_plz |= pool.by_plz.get(p, set())
    by_ft = set(ft_search(case))
    out, old = [], []
    for pn in by_buyer | by_plz | by_ft:
        n = pool.notices.get(pn)
        if n is None or pub_date(n) >= c_date or pn == case.nr or (c_proc and n.get("procedure-identifier") == c_proc):
            continue
        b_sim = buyer_similar(cb, pool.buyer[pn])
        if not (b_sim or pn in by_ft or pn in by_plz or pn in weak):
            continue
        cand = {"pn": pn, "buyer_similar": b_sim, "ft": pn in by_ft}
        if has_text_fields(n):
            out.append(cand)
        else:
            same_city = bool({norm(c) for c in texts(n.get("buyer-city"))} & (case.alle("orte") | {norm(c) for c in texts(notice.get("buyer-city"))}))
            old.append({**cand, "same_city": same_city})
    old.sort(key=lambda c: (c["ft"], c["same_city"], pub_date(pool.notices[c["pn"]])), reverse=True)
    return out + old[:XML_CAP]


def identity(b: Bekanntmachung) -> set[str]:
    return b.alle("namen") | b.alle("adressen")


def area_match(a: Bekanntmachung, b: Bekanntmachung) -> bool:
    fa, fb = a.alle("flaechen"), b.alle("flaechen")
    return any(x[0] == y[0] and abs(x[1] - y[1]) <= AREA_TOL * max(x[1], y[1]) for x in fa for y in fb)


def title_words(b: Bekanntmachung) -> set[str]:
    return {w for w in norm(b.titel).split() if len(w) > 2 and w not in TITLE_GENERIC and not w.isdigit()}


def compare(case: Bekanntmachung, cand: Bekanntmachung, info: dict, generic: set[str] = frozenset(),
            case_buyer: set[str] = frozenset()) -> dict:
    arten_k = cand.alle("arten")
    ac, ak = case.alle("arten") & KERN, arten_k & KERN
    pc, pk = case.alle("plz"), cand.alle("plz")
    gebiet = bool(pc and pk and not pc & pk and len(pc) <= 2 and len(pk) <= 2)  # Urteilsregeln Stufe B: anderes Gebiet
    conflict = (bool(ac and ak and not ac & ak) or (ak == {"bau"} and "bau" not in ac)
                or ("fremd" in arten_k and "fremd" not in case.alle("arten")) or gebiet)
    ic, ik = identity(case) - generic, identity(cand) - generic
    common = ic & ik
    r_short = len(common) / min(len(ic), len(ik)) if ic and ik else 0.0
    r_long = len(common) / max(len(ic), len(ik)) if ic and ik else 0.0
    area = area_match(case, cand)
    streets = bool(case.alle("strassen") & cand.alle("strassen"))
    # Ortsbezug: ähnlicher Auftraggeber, gemeinsame PLZ oder Orte, oder ein gemeinsamer Name, dessen Eigenname einen Ort des
    # Falls nennt (z. B. „polizeiinspektion stade“ bei Leistungsort oder Titel Stade). Allgemeine Namen („goetheschule“,
    # „foerderschule geistige entwicklung“) und Adressen allein reichen nicht.
    place_words = {w for o in case.alle("orte") | cand.alle("orte") for w in o.split()} | set(norm(case.titel).split())
    named = any(set(c.split()[1:]) & place_words for c in common & case.alle("namen") if " " in c)
    locality = info["buyer_similar"] or bool(pc & pk) or bool(case.alle("orte") & cand.alle("orte")) or named
    title = jaccard(title_words(case) - case_buyer, title_words(cand) - case_buyer)
    if conflict:
        cat = "nein"
    elif ic and ik and r_short >= R_OBJEKT and locality:
        cat = "objekt"
    elif ic and ik and info["buyer_similar"] and r_short < R_GESCHWISTER and r_long < R_GESCHWISTER and not area:
        cat = "geschwister"
    elif common or area or (streets and info["buyer_similar"]):
        cat = "unklar"
    elif info["buyer_similar"] and not (ic and ik):
        cat = "unklar"  # mindestens eine Seite ohne Objekte: nicht entscheidbar
    elif info["ft"]:
        cat = "unklar"  # Volltext enthält einen Namen oder eine Adresse des Falls (z. B. nach Namenswechsel des Auftraggebers)
    else:
        cat = "nein"
    points = 3 * r_short + r_long + 1.5 * area + 0.5 * streets + 0.7 * info["buyer_similar"] + 0.5 * title + 1.0 * info["ft"]
    if not locality and not info["ft"]:
        points -= 1.0  # ohne Ortsbezug (anderer Auftraggeber, andere PLZ und Orte) deutlich schwächer
    return {**info, "cat": cat, "points": round(points, 3), "r_short": round(r_short, 2), "r_long": round(r_long, 2),
            "area": area, "streets": streets, "title": round(title, 2), "common": sorted(common)[:6], "conflict": conflict,
            "gebiet": gebiet, "locality": locality}


BEST_MARGIN = 1.5  # unter starken Treffern („objekt“) gilt der jüngste, wenn seine Punktzahl höchstens so weit unter der besten liegt


def match(notice: dict, pool: Pool) -> dict:
    case = bekanntmachung(notice)
    cands = candidates(notice, case, pool)
    feats = {c["pn"]: pool.features(c["pn"]) for c in cands}
    counts: dict[str, int] = {}
    for b in feats.values():
        for item in identity(b):
            counts[item] = counts.get(item, 0) + 1
    generic = ({i for i, k in counts.items() if k >= FREQ_MIN and k >= FREQ_SHARE * len(cands)}
               if len(cands) >= FREQ_CANDIDATES else set())
    case_buyer = buyer_words(notice)[1]
    scored = [compare(case, feats[c["pn"]], c, generic, case_buyer) for c in cands]
    ranked = sorted((s for s in scored if s["cat"] in ("objekt", "unklar")),
                    key=lambda s: (s["points"], pub_date(pool.notices[s["pn"]])), reverse=True)
    objekt = [s for s in ranked if s["cat"] == "objekt"]
    best = None
    if objekt:
        top_points = max(s["points"] for s in objekt)
        best = max((s for s in objekt if s["points"] >= top_points - BEST_MARGIN), key=lambda s: pub_date(pool.notices[s["pn"]]))
    return {"case": case.nr, "n_candidates": len(scored), "proposal": best, "top": ranked[:TOP_N],
            "n_geschwister": sum(s["cat"] == "geschwister" for s in scored), "generic": sorted(generic), "scored": scored}


def log_q1(pns: set[str], pool: Pool) -> None:
    q1 = {pn for pn in pns if "2026-01-01" <= pub_date(pool.notices.get(pn, {})) <= "2026-03-31"}
    if not q1:
        return
    old = set(Q1_SEEN.read_text(encoding="utf-8").split()) if Q1_SEEN.exists() else set()
    Q1_SEEN.write_text("\n".join(sorted(old | q1, key=lambda s: int(s.split("-")[0]))) + "\n", encoding="utf-8")


def describe(pool: Pool, pn: str) -> str:
    n, b = pool.notices[pn], pool.features(pn)
    return f"{pn} ({pub_date(n)}, {n.get('form-type')}, {b.quelle}) „{b.titel[:80]}“"


def dev_q3(pool: Pool, verbose: bool) -> list[dict]:
    gt = {r["notice"]: r for r in csv.DictReader(open(PROJECT_ROOT / "reports" / "sichtbarkeit_iteration3_gt.csv", encoding="utf-8"),
                                                    delimiter=";")}
    notices = {n["publication-number"]: n for n in load_run(DEV_Q3)}
    results, stats = [], {"P": 0, "korrekt": 0, "falsch_bekannt": 0, "unbekannt": 0, "gefunden": 0, "top": 0}
    for t, (pn, g) in enumerate(gt.items(), 1):
        n = notices[pn]
        if exclusion_reason(n):
            print(f"T{t} {pn}: nicht mehr in der Population ({exclusion_reason(n)})")
            continue
        r = match(n, pool)
        results.append(r)
        found = g["kategorie"] in ("objektgleich", "teilmenge")
        preds = set(g["vorgaenger"].split())
        stats["gefunden"] += found
        stats["top"] += found and any(s["pn"] in preds for s in r["top"])
        status = "–"
        if r["proposal"]:
            stats["P"] += 1
            if found and r["proposal"]["pn"] in preds:
                status, key = "korrekt", "korrekt"
            elif g["kategorie"] == "kein_vorgaenger":
                status, key = "falsch (Handsuche: kein Vorgänger)", "falsch_bekannt"
            else:
                status, key = "unbekannt (nicht in der Handsuche)", "unbekannt"
            stats[key] += 1
        elif found:
            status = "verpasst"
        log_q1({s["pn"] for s in r["top"]} | ({r["proposal"]["pn"]} if r["proposal"] else set()), pool)
        top_hit = "Top3✓" if found and any(s["pn"] in preds for s in r["top"]) else ""
        print(f"T{t:<3}{pn} GT={g['kategorie']:<15} {status:<36} {top_hit} Kand={r['n_candidates']} Geschw={r['n_geschwister']}")
        if verbose or status.startswith(("unbekannt", "falsch")) or status == "verpasst":
            for s in ([r["proposal"]] if r["proposal"] else []) + [s for s in r["top"] if s is not r["proposal"]]:
                print(f"      {s['cat']:<8} p={s['points']:<5} r={s['r_short']}/{s['r_long']} fl={int(s['area'])} "
                      f"gem={s['common'][:3]} | {describe(pool, s['pn'])}")
            if status == "verpasst":
                seen = {s["pn"]: s for s in r.get("scored", [])}
                info = [f"{p}: " + (f"{seen[p]['cat']} p={seen[p]['points']} r={seen[p]['r_short']} gem={seen[p]['common'][:2]}"
                                    if p in seen else "kein Kandidat") for p in g["vorgaenger"].split()]
                print(f"      Handsuche: {' | '.join(info)}")
    P, k = stats["P"], stats["korrekt"]
    print(f"\nVorschläge {P}: korrekt {k}, falsch (bekannt) {stats['falsch_bekannt']}, unbekannt {stats['unbekannt']}")
    if P:
        print(f"Präzision: untere Grenze {k / P:.1%} (unbekannt = falsch), obere {(k + stats['unbekannt']) / P:.1%}")
    print(f"Trefferquote {k}/{stats['gefunden']} = {k / stats['gefunden']:.1%}; Top {TOP_N}: {stats['top']}/{stats['gefunden']} "
          f"= {stats['top'] / stats['gefunden']:.1%}")
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dev-q3", action="store_true")
    parser.add_argument("--dev-q2", type=int, default=0)
    parser.add_argument("--test", help="Datei mit Notice-Nummern der Testfälle (eine pro Zeile)")
    parser.add_argument("--run", default="DEU_competition_cpv9091main_20260101_20260331_lostext",
                        help="Lauf mit den Testfällen (Ordner unter data/raw/ted_search)")
    parser.add_argument("--out", help="JSON-Ausgabe der Zuordnungen")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    pool = Pool()
    print(f"Pool: {len(pool.notices)} Notices")
    if args.dev_q3:
        results = dev_q3(pool, args.verbose)
    elif args.dev_q2:
        comps = [n for n in load_run(DEV_Q2) if exclusion_reason(n) is None]
        results = []
        for n in random.Random(DEV_Q2_SEED).sample(comps, args.dev_q2):
            r = match(n, pool)
            results.append(r)
            log_q1({s["pn"] for s in r["top"]}, pool)
            print(f"\n## {n['publication-number']} „{texts(n.get('title-proc'))[:1]}“ Kand={r['n_candidates']}")
            for s in ([r["proposal"]] if r["proposal"] else []) + [s for s in r["top"] if s is not r["proposal"]]:
                print(f"   {s['cat']:<8} p={s['points']:<5} r={s['r_short']}/{s['r_long']} gem={s['common'][:3]} | {describe(pool, s['pn'])}")
    elif args.test:
        wanted = [x.strip() for x in Path(args.test).read_text(encoding="utf-8").splitlines() if x.strip()]
        notices = {n["publication-number"]: n for n in load_run(args.run)}
        missing = [w for w in wanted if w not in notices]
        if missing:
            sys.exit(f"Nicht im Lauf {args.run}: {', '.join(missing)}")
        results = []
        for w in wanted:
            r = match(notices[w], pool)
            r.pop("scored")  # nur Vorschlag, Rangliste und Zählungen ausgeben
            results.append(r)
            p = r["proposal"]
            print(f"{w}: Kand={r['n_candidates']} Vorschlag={p['pn'] if p else '–'} Top={[s['pn'] for s in r['top']]}")
    else:
        sys.exit("--dev-q3, --dev-q2 N oder --test angeben")
    if args.out:
        Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
