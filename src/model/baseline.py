"""Iteration 5, Schritt 6: Baseline-Regeln R0 und R1 und Backtest (Phasen 4 und 5).

Regeln (festgelegt in docs/business.md §7.1, vor jeder Berechnung; hier eingefroren und vor dem ersten Lauf committet):
- R0 (naive Referenz):  Prognose = Ende der Grundlaufzeit des Vorgängers − 6 Kalendermonate
- R1 (Hauptregel):      Prognose = Höchstende des Vorgängers − 6 Kalendermonate; ist das Höchstende unbestimmbar: wie R0
- Treffer: Veröffentlichung der neuen Ausschreibung (Testfall) liegt zwischen Prognose − 3 und Prognose + 3 Kalendermonaten (inklusive).
  Zusätzlich ohne Schwelle: ±6 Monate und die Abweichung in Monaten.
Es werden keine Parameter aus den Paaren geschätzt. Die Parameter stehen unten (VORLAUF_MONATE, FENSTER_MONATE).

Daten: data/processed/backtest_paare_iteration5.csv (aus src/prepare/backtest_paare.py: Vorgänger-Ende nur aus den Bekanntmachungen des
Vorgängers) und die Liste der von Rechercheur und Prüfer bestätigten Paare (X1) in data/processed/x1_paare_iteration5.txt.

Kriterium X3: R1-Trefferquote ≥ 60 % und ≥ 10 Prozentpunkte über R0 auf denselben Paaren.

Aufruf:  python src/model/baseline.py      Ausgabe: reports/backtest_iteration5.md
"""

import calendar
import csv
import math
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PAARE = ROOT / "data" / "processed" / "backtest_paare_iteration5.csv"
X1_LISTE = ROOT / "data" / "processed" / "x1_paare_iteration5.txt"
REPORT = ROOT / "reports" / "backtest_iteration5.md"

VORLAUF_MONATE = 6    # Parameter der Regeln R0 und R1
FENSTER_MONATE = 3    # Treffer-Fenster ±3 Monate (Setzung, docs/business.md §7.1)
FENSTER_WEIT = 6      # nur zusätzlich ausgewiesen


def plus_monate(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    y, mo = d.year + y, mo + 1
    return date(y, mo, min(d.day, calendar.monthrange(y, mo)[1]))


def monate_zwischen(a: date, b: date) -> float:
    """Abweichung b − a in Monaten (positiv: b später)."""
    return (b - a).days / 30.4375


def r0(gl: date) -> date:
    return plus_monate(gl, -VORLAUF_MONATE)


def r1(gl: date, hoechstende: date | None) -> date:
    return plus_monate(hoechstende or gl, -VORLAUF_MONATE)


def treffer(prognose: date, veroeffentlicht: date, fenster: int) -> bool:
    return plus_monate(prognose, -fenster) <= veroeffentlicht <= plus_monate(prognose, fenster)


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return 0.0, 0.0
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return c - h, c + h


def pct(k: int, n: int) -> str:
    if not n:
        return "–"
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {100 * k / n:.1f} % (Wilson {100 * lo:.1f}–{100 * hi:.1f})".replace(".", ",")


def median(xs: list[float]) -> float:
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def lade() -> list[dict]:
    x1 = set(X1_LISTE.read_text(encoding="utf-8").split())
    rows = []
    with PAARE.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            if r["pid"] not in x1:
                continue
            gl = date.fromisoformat(r["gl_ende"])
            h = date.fromisoformat(r["hoechstende"]) if r["hoechstende"] else None
            pub = date.fromisoformat(r["testfall_datum"])
            p0, p1 = r0(gl), r1(gl, h)
            rows.append({**r, "gl": gl, "h": h, "pub": pub, "p0": p0, "p1": p1,
                         "t0": treffer(p0, pub, FENSTER_MONATE), "t1": treffer(p1, pub, FENSTER_MONATE),
                         "t0w": treffer(p0, pub, FENSTER_WEIT), "t1w": treffer(p1, pub, FENSTER_WEIT),
                         "d0": monate_zwischen(p0, pub), "d1": monate_zwischen(p1, pub)})
    return rows


def zeile(name: str, rs: list[dict]) -> str:
    n = len(rs)
    if not n:
        return f"| {name} | 0 | – | – | – |"
    return (f"| {name} | {n} | {pct(sum(r['t0'] for r in rs), n)} | {pct(sum(r['t1'] for r in rs), n)} | "
            f"{sum(r['t1'] for r in rs) / n * 100 - sum(r['t0'] for r in rs) / n * 100:+.1f} |".replace(".", ",", 1))


def main() -> None:
    rows = lade()
    n = len(rows)
    k0, k1 = sum(r["t0"] for r in rows), sum(r["t1"] for r in rows)
    q0, q1 = 100 * k0 / n, 100 * k1 / n
    x3 = q1 >= 60 and q1 - q0 >= 10
    out = [
        "# Backtest Iteration 5 (Schritt 6, Kriterium X3)", "",
        "_Erzeugt mit `src/model/baseline.py` (eingefroren und vor dem Lauf committet). Regeln und Treffer-Definition in `docs/business.md` §7.1; "
        "fachliches Kriterium dort vor dem Lauf festgelegt._", "",
        "## Fakten", "",
        f"- Paare: **{n}** (von Rechercheur und Prüfer bestätigt, Ende der Grundlaufzeit bestimmbar; Zweitprüfung "
        "[gt_pruefung_iteration5_auswertung.md](gt_pruefung_iteration5_auswertung.md)).",
        f"- Parameter: Vorlauf {VORLAUF_MONATE} Monate, Fenster ±{FENSTER_MONATE} Monate; keine Schätzung aus den Paaren.", "",
        "| | Treffer ±3 Monate | ±6 Monate (ohne Schwelle) | Median Abweichung (Monate, Veröffentlichung − Prognose) |", "|---|---|---|---|",
        f"| **R0** Grundlaufzeit − 6 | {pct(k0, n)} | {pct(sum(r['t0w'] for r in rows), n)} | {median([r['d0'] for r in rows]):+.1f} |".replace(".", ",", 0),
        f"| **R1** Höchstende − 6 | {pct(k1, n)} | {pct(sum(r['t1w'] for r in rows), n)} | {median([r['d1'] for r in rows]):+.1f} |", "",
        f"**X3:** R1 {q1:.1f} % (Schwelle ≥ 60 %), Abstand zu R0 {q1 - q0:+.1f} Prozentpunkte (Schwelle ≥ +10) → "
        f"**{'erfüllt' if x3 else 'nicht erfüllt'}**.".replace(".", ","), "",
        "### Aufschlüsselung (explorativ, ohne Schwelle)", "",
        "| Gruppe | n | R0 Treffer | R1 Treffer | Differenz (Prozentpunkte) |", "|---|---|---|---|---|",
    ]
    out.append(zeile("Iteration 3 (Testfälle Q3 2026)", [r for r in rows if r["iteration"] == "3"]))
    out.append(zeile("Iteration 4 (Testfälle Q1 2026)", [r for r in rows if r["iteration"] == "4"]))
    out.append(zeile("Vorgänger vor eForms (XML)", [r for r in rows if r["format"] == "xml"]))
    out.append(zeile("Vorgänger eForms (API)", [r for r in rows if r["format"] == "eforms"]))
    for h in sorted({r["hoechstende_herkunft"] for r in rows}):
        out.append(zeile(f"Höchstende: {h}", [r for r in rows if r["hoechstende_herkunft"] == h]))
    out.append(zeile("Höchstende ≠ Grundlaufzeit (Verlängerung belegt)", [r for r in rows if r["h"] and r["h"] != r["gl"]]))
    out.append(zeile("Höchstende = Grundlaufzeit oder unbekannt", [r for r in rows if not r["h"] or r["h"] == r["gl"]]))
    out.append(zeile("Objektgleich laut Handsuche", [r for r in rows if r["gt"].startswith("objektgleich")]))
    out.append(zeile("Teilmenge laut Handsuche", [r for r in rows if r["gt"] == "teilmenge"]))
    out += ["", "### Lage der Veröffentlichung relativ zur R1-Prognose", ""]
    dc = Counter("früher als −3" if r["d1"] < -3 else ("im Fenster" if r["d1"] <= 3 else "später als +3") for r in rows)
    out += ["| Lage | Paare |", "|---|---|", *[f"| {k} | {v} |" for k, v in dc.most_common()], "",
            "### Alle Paare (Prognose und Veröffentlichung)", "",
            "| Paar | Testfall | Veröffentlicht | Ende GL | Höchstende (Herkunft) | R0 | R1 | Abw. R1 (Mon.) | R0 | R1 |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["d1"]):
        out.append(f"| {r['pid']} | {r['testfall']} | {r['pub']} | {r['gl']} | {r['h'] or '–'} ({r['hoechstende_herkunft'] or '–'}) | "
                   f"{r['p0']} | {r['p1']} | {r['d1']:+.1f} | {'✓' if r['t0'] else '✗'} | {'✓' if r['t1'] else '✗'} |")
    out += ["", "## Grenzen", "",
            "- Nur Neuausschreibungen, die auf TED erscheinen (Trefferquote, nicht Präzision der Prognosen ohne Nachfolger).",
            "- Paare stammen aus der Handsuche (Rückwärtssuche); ob sie für alle Verträge typisch sind, ist offen.",
            "- Die Vorlaufzeiten dieser Paare wurden in Iteration 3 und 4 explorativ gesehen; das hat das Prognoseziel mitbestimmt.",
            "- 5 Paare ohne Bestätigung beider Prüfer und die Paare ohne bestimmbares Ende fehlen.",
            "- Höchstende vor eForms nur an eForms-Texten getestet (`reports/hoechstende_pruefung_iteration5_test.md`).",
            "- Unabhängigkeit der Zweitprüfung für P14–P71 offen (A18)."]
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"n={n}  R0 {k0}/{n}={q0:.1f}%  R1 {k1}/{n}={q1:.1f}%  X3 {'erfüllt' if x3 else 'nicht erfüllt'}")


if __name__ == "__main__":
    main()
