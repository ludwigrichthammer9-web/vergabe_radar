"""Auswertung Iteration 3, Schritt 5: eingefrorene Regel auf die Testfälle anwenden und mit der Handsuche vergleichen.

Eingaben:
- reports/testfaelle_iteration3.txt                 Testfälle (Reihenfolge = T1 … T60)
- reports/sichtbarkeit_iteration3_gt.csv            Handsuche (Ground Truth), aus den Protokollen Teil 1–4 übertragen:
      T;notice;kategorie;vorgaenger;belegstaerke    (vorgaenger: alle Notice-Nummern desselben Vorgängers, durch Leerzeichen getrennt)
- reports/zuordnung_iteration3_urteile.csv          Einzelurteile für Regelvorschläge, die nicht in der Handsuche stehen:
      T;vorschlag;urteil;begruendung                (urteil: korrekt | falsch; wird nach dem ersten Lauf ausgefüllt)

Ausgaben:
- reports/zuordnung_iteration3.md                   V1, V2, V3, V5 und Fallliste
- data/processed/zuordnung_iteration3.json          Rohausgabe der Regel

Zählweise (vorab festgelegt in docs/iterationen.md, Iteration 3):
- V1 = Anteil Testfälle mit Handsuche-Kategorie objektgleich oder teilmenge.
- V2 = korrekte Vorschläge / alle Vorschläge der Regel. Korrekt, wenn der Vorschlag in der Vorgängerliste der Handsuche steht oder laut
  Einzelurteil objektgleich bzw. Teilmenge ist.
- V3 = Testfälle mit Handsuche-Vorgänger, für die die Regel einen korrekten Vorschlag macht / Testfälle mit Handsuche-Vorgänger.
- V5 = Anteil der Testfälle mit korrektem Vorschlag und bestimmbarem Vorgänger-Ende × Population pro Jahr (Q3 2026 × 4).

Aufruf:
    .venv\\Scripts\\python src/auswertung_iteration3.py
"""

import csv
import json
import re
import sys
from pathlib import Path

from analyze_completeness import RAW_SEARCH_DIR, load_notices
from kennzahlen_iteration2 import wilson
from objekt_merkmale import load_xml
from zuordnung_objekt import TEST_RUN, Pool, match_all

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
POPULATION_Q3 = 492  # reports/testfaelle_iteration3.md


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def end_date(pool: Pool, pn: str) -> str:
    """Grundlaufzeit-Ende des Vorgängers: eForms aus den API-Feldern, sonst aus der XML bzw. über REF_NOTICE."""
    n = pool.notices.get(pn)
    if n and n.get("contract-duration-end-date-lot"):
        return str(n["contract-duration-end-date-lot"][0])[:10]
    root = load_xml(pn)
    for _ in range(2):  # eigener Zuschlag, dann referenzierte Ausschreibung
        if root is None:
            return ""
        end = next((e for e in root.iter() if local(e.tag) == "DATE_END"), None)
        if end is not None and (end.text or "").strip():
            return end.text.strip()[:10]
        ref = next((e for e in root.iter() if local(e.tag) in ("REF_NOTICE", "NOTICE_NUMBER_OJ")), None)
        m = re.search(r"(\d{4})/S \d+-(\d+)", " ".join(ref.itertext())) if ref is not None else None
        root = load_xml(f"{int(m.group(2))}-{m.group(1)}") if m else None
    return ""


def pct(k: int, n: int) -> str:
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {k / n * 100:.1f} % (Wilson {lo * 100:.1f}–{hi * 100:.1f} %)".replace(".", ",") if n else "–"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    tests = [l.strip() for l in (REPORTS / "testfaelle_iteration3.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    gt = {r["notice"]: r for r in read_csv(REPORTS / "sichtbarkeit_iteration3_gt.csv")}
    if len(gt) != len(tests):
        sys.exit(f"Handsuche unvollständig: {len(gt)} von {len(tests)} Fällen in sichtbarkeit_iteration3_gt.csv")
    urteile = {(r["T"], r["vorschlag"]): r for r in read_csv(REPORTS / "zuordnung_iteration3_urteile.csv")}

    comps = {n["publication-number"]: n for n in load_notices(RAW_SEARCH_DIR / TEST_RUN)}
    pool = Pool()
    results = match_all([comps[t] for t in tests], pool)
    (ROOT / "data" / "processed").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "processed" / "zuordnung_iteration3.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")

    rows, offen = [], []
    for i, (t, r) in enumerate(zip(tests, results), 1):
        g = gt[t]
        found = g["kategorie"] in ("objektgleich", "teilmenge")
        gt_preds = set(g["vorgaenger"].split())
        prop = r["best"]["pn"] if r["best"] else ""
        if not prop:
            status = "kein Vorschlag"
        elif prop in gt_preds:
            status = "korrekt (Handsuche)"
        elif (f"T{i}", prop) in urteile and urteile[(f"T{i}", prop)]["urteil"]:
            status = f"{urteile[(f'T{i}', prop)]['urteil']} (Einzelurteil)"
        else:
            status = "offen"
            offen.append((f"T{i}", t, prop))
        correct = status.startswith("korrekt")
        rows.append({"T": f"T{i}", "notice": t, "gt": g["kategorie"], "gt_preds": " ".join(sorted(gt_preds)), "prop": prop,
                     "level": r["best"]["level"] if r["best"] else "", "status": status, "found": found, "correct": correct,
                     "end": end_date(pool, prop) if correct else ""})

    n = len(rows)
    v1 = sum(r["found"] for r in rows)
    props = [r for r in rows if r["prop"]]
    v2 = sum(r["correct"] for r in props)
    v3 = sum(r["correct"] for r in rows if r["found"])
    v5_cases = sum(1 for r in rows if r["correct"] and r["end"])
    v5 = v5_cases / n * POPULATION_Q3 * 4

    out = ["# Zuordnung über das Objekt: Testergebnis (Iteration 3)", "",
           "Erzeugt mit `src/auswertung_iteration3.py`. Regel: Stand Commit 4497743 (eingefroren vor den Testdaten). Handsuche: "
           "`reports/sichtbarkeit_iteration3_teil1.md` bis `_teil4.md`, übertragen in `sichtbarkeit_iteration3_gt.csv`.", ""]
    if offen:
        out += ["**Noch nicht vollständig:** Für folgende Vorschläge fehlt ein Einzelurteil in `zuordnung_iteration3_urteile.csv`:", ""]
        out += [f"- {t} ({notice}) → {prop}" for t, notice, prop in offen]
        out.append("")
    out += ["| Kriterium | Ergebnis | Schwelle |", "|---|---|---|",
            f"| V1 Sichtbarkeit | {pct(v1, n)} | ≥ 50 % |",
            f"| V2 Präzision | {pct(v2, len(props))} | ≥ 80 % und Untergrenze ≥ 60 % |",
            f"| V3 Trefferquote | {pct(v3, v1)} | ≥ 60 % |",
            f"| V5 Backtest-Basis | {v5_cases}/{n} Fälle × {POPULATION_Q3} × 4 = {v5:.0f} pro Jahr | ≥ 100 pro Jahr |", "",
            "| T | Testfall | Handsuche | Vorgänger (Handsuche) | Vorschlag der Regel | Stufe | Status | Vorgänger-Ende |",
            "|---|---|---|---|---|---|---|---|"]
    out += [f"| {r['T']} | {r['notice']} | {r['gt']} | {r['gt_preds'] or '–'} | {r['prop'] or '–'} | {r['level']} | {r['status']} | "
            f"{r['end']} |" for r in rows]
    (REPORTS / "zuordnung_iteration3.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out[:16]))


if __name__ == "__main__":
    main()
