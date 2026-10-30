"""Auswertung Iteration 4, Schritt 5: eingefrorene Regel (Commit 1d0e060) gegen die Handsuche (Commit d43c547).

Eingaben:
- reports/sichtbarkeit_iteration4_gt.csv      Handsuche nach Urteilsregeln 1.1 (src/gt_iteration4.py)
- reports/zuordnung_iteration4_lauf.json      Lauf der Regel: zuordnung_los.py --test reports/testfaelle_iteration4.txt
- reports/paarbeurteilung_iteration4.md       Urteil des Rechercheurs zu Vorschlägen, die die Handsuche nicht nennt (blind)

Kriterien (docs/iterationen.md, Iteration 4, vorab festgelegt):
- W1 = Fälle mit objektgleichem Vorgänger oder Teilmenge / 70
- W2 = korrekte Vorschläge / alle Vorschläge (korrekt: in den Vorgänger-Notices der Handsuche oder Paarurteil objektgleich/teilmenge);
       Schwelle ≥ 80 % und Wilson-Untergrenze ≥ 60 % bei mindestens 25 Vorschlägen
- W3 = Fälle aus W1 mit korrektem Vorschlag / Fälle aus W1
- W5 = korrekte Vorschläge mit bestimmbarem Ende der Grundlaufzeit / 70 × Population der letzten 4 Quartale
- W6 = Fälle aus W1, deren Vorgänger (Notices der Handsuche) unter den höchstens 3 Kandidaten der Regel ist / Fälle aus W1
Explorativ: Vorlaufzeit (Veröffentlichung des Testfalls bis Vorgänger-Ende) und vorzeitige Neuvergaben laut Handsuche.

Aufruf:
    python -I src/auswertung_iteration4.py      # schreibt reports/zuordnung_iteration4.md
    python -I src/auswertung_iteration4.py zuordnung_iteration4_korrektur.md   # korrigierte Fassung (2026-10-30)
"""

import csv
import json
import re
import sys
from datetime import date
from math import sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
POPULATION_JAHR = {"Q4 2025": 381, "Q1 2026": 538, "Q2 2026": 488, "Q3 2026": 486}  # population_iteration4.py auf den _lostext-Läufen
FOUND = ("objektgleich_hoch", "objektgleich_mittel", "teilmenge")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return 0.0, 0.0
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return c - h, c + h


def fmt(k: int, n: int) -> str:
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {k / n:.1%} (Wilson {lo:.1%}–{hi:.1%})".replace(".", ",") if n else f"{k}/0"


def pair_judgments() -> dict[tuple[str, str], dict]:
    path = REPORTS / "paarbeurteilung_iteration4.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    out = {}
    for line in text.splitlines():
        cells = [c.strip().strip("*") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and re.fullmatch(r"Q\d+", cells[0]):
            alt, neu = (re.search(r"\d{1,6}-20\d\d", c).group(0) for c in cells[1:3])
            urteil = next((k for k in FOUND + ("nicht_objektgleich", "unklar") if k in cells[3].replace(" ", "_")), cells[3])
            out[(alt, neu)] = {"urteil": urteil, "ende": cells[5] if len(cells) > 5 else "", "herkunft": cells[6] if len(cells) > 6 else ""}
    return out


def months(a: str, b: str) -> float:
    d1, d2 = date.fromisoformat(a), date.fromisoformat(b)
    return round((d2 - d1).days / 30.44, 1)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    gt = {r["notice"]: r for r in csv.DictReader(open(REPORTS / "sichtbarkeit_iteration4_gt.csv", encoding="utf-8"), delimiter=";")}
    runs = json.loads((REPORTS / "zuordnung_iteration4_lauf.json").read_text(encoding="utf-8"))
    pairs = pair_judgments()
    tests = {n["publication-number"]: n for f in sorted((ROOT / "data/raw/ted_search/DEU_competition_cpv9091main_20260101_20260331_lostext")
                                                        .glob("page_*.json"))
             for n in json.loads(f.read_bytes().decode("utf-8"))["notices"]}
    n_cases, pop_year = len(gt), sum(POPULATION_JAHR.values())
    found = [g for g in gt.values() if g["kategorie"] in FOUND]
    rows, missing_pairs = [], []
    stats = {"P": 0, "korrekt": 0, "w3": 0, "w6": 0, "w5": 0}
    lead = []
    for r in runs:
        g = gt[r["case"]]
        preds = set(g["vorgaenger"].split())
        is_found = g["kategorie"] in FOUND
        top_hit = is_found and any(s["pn"] in preds for s in r["top"])
        stats["w6"] += top_hit
        p = r["proposal"]
        status, ende, herkunft = "–", "", ""
        if p:
            stats["P"] += 1
            if p["pn"] in preds:
                status, ok = "korrekt (Handsuche)", True
                ende, herkunft = g["ende"], g["herkunft"]
            elif (p["pn"], r["case"]) in pairs:
                j = pairs[(p["pn"], r["case"])]
                ok = j["urteil"] in FOUND
                status = f"{'korrekt' if ok else 'falsch'} (Paarurteil: {j['urteil']})"
                ende, herkunft = j["ende"], j["herkunft"]
            else:
                ok, status = False, "offen (kein Paarurteil)"
                missing_pairs.append((p["pn"], r["case"]))
            if ok:
                stats["korrekt"] += 1
                stats["w3"] += is_found
                d = DATE.search(ende or "")
                # Korrektur 2026-10-30 (Evaluation Iteration 4): auch „grundlaufzeit, hoechstende“ zählt; nur geplante Daten aus
                # einer Ausschreibung ohne Zuschlag („aus Ausschreibung“) zählen nicht.
                h = herkunft.strip().lower()
                if h.startswith("grundlaufzeit") and "aus ausschreibung" not in h and d:
                    stats["w5"] += 1
                    lead.append((g["U"], months(str(tests[r["case"]]["publication-date"])[:10], d.group(0))))
        elif is_found:
            status = "verpasst"
        rows.append((g, r, status, top_hit, ende, herkunft))
    P, k = stats["P"], stats["korrekt"]
    w2_lo = wilson(k, P)[0] if P else 0
    w5 = stats["w5"] / n_cases * pop_year
    # Korrektur 2026-10-30: nur Fälle mit Vorgänger (W1), nicht „unklar“
    early = [g["U"] for g in found if g["vorzeitig"].strip().lower().startswith("ja")]

    out = ["# Zuordnung über Merkmale je Los: Testergebnis (Iteration 4)", "",
           "Erzeugt mit `src/auswertung_iteration4.py`. Regel: `src/zuordnung_los.py`, Stand Commit 1d0e060 (eingefroren vor den Testdaten). "
           "Handsuche: `reports/sichtbarkeit_iteration4_teil1.md` bis `_teil5.md`, übertragen in `sichtbarkeit_iteration4_gt.csv` "
           "(Commit d43c547, vor dem Regel-Lauf). Vorschläge außerhalb der Handsuche: blind beurteilt in `paarbeurteilung_iteration4.md`.", "",
           "| Kriterium | Ergebnis | Schwelle |", "|---|---|---|",
           f"| W1 Sichtbarkeit | {fmt(len(found), n_cases)}; nur objektgleich "
           f"{fmt(sum(g['kategorie'].startswith('objektgleich') for g in gt.values()), n_cases)} | ≥ 50 % |",
           f"| W2 Präzision | {fmt(k, P)} | ≥ 80 % und Untergrenze ≥ 60 %, mindestens 25 Vorschläge |",
           f"| W3 Trefferquote | {fmt(stats['w3'], len(found))} | ≥ 60 % |",
           f"| W5 Backtest-Basis | {stats['w5']}/{n_cases} × {pop_year} = {w5:.0f} pro Jahr | ≥ 100 pro Jahr |",
           f"| W6 Kandidatenliste | {fmt(stats['w6'], len(found))} | ≥ 70 % |", "",
           f"Population der letzten 4 Quartale: {', '.join(f'{q} {v}' for q, v in POPULATION_JAHR.items())} = {pop_year}.",
           f"Wilson-Untergrenze W2: {w2_lo:.1%}.".replace(".", ","), ""]
    if missing_pairs:
        out += [f"**Noch offen:** Paarurteil fehlt für {', '.join(f'{a} → {b}' for a, b in missing_pairs)}.", ""]
    out += ["**Explorativ**", "",
            f"- Vorlaufzeit (Veröffentlichung Testfall bis Ende der Grundlaufzeit des Vorgängers), korrekte Paare: "
            f"{', '.join(f'{u} {m} Monate' for u, m in lead) or '–'}",
            f"- Vorzeitige Neuvergabe laut Handsuche: {', '.join(early) or 'keine'} (von {len(found)} Fällen mit Vorgänger)", "",
            "| U | Testfall | Handsuche | Vorgänger (Handsuche) | Vorschlag | Status | Top 3 | Vorgänger-Ende | Herkunft |",
            "|---|---|---|---|---|---|---|---|---|"]
    for g, r, status, top_hit, ende, herkunft in rows:
        p = r["proposal"]
        out.append(f"| {g['U']} | {r['case']} | {g['kategorie']} | {g['vorgaenger'] or '–'} | {p['pn'] if p else '–'} | {status} | "
                   f"{'✓' if top_hit else ''} | {ende or ''} | {herkunft or ''} |")
    target = REPORTS / (sys.argv[1] if len(sys.argv) > 1 else "zuordnung_iteration4.md")
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out[5:13]))
    if missing_pairs:
        print("Offen:", missing_pairs)


if __name__ == "__main__":
    main()
