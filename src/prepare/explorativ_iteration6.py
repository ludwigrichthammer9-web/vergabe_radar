"""Iteration 6: explorative Kennzahlen ohne Schwelle (vorab genannt in docs/iterationen.md, Iteration 6).

1. Lose, deren Grundlaufzeit in den nächsten 12 bzw. 24 Monaten endet (bundesweit, alle eForms-Zuschläge der Vertragsliste; Stichtag 2026-11-04).
2. Anteil der 52 Backtest-Paare (X1) im Beobachtungsfenster „Ende der Grundlaufzeit − 12 Monate bis Höchstende + 12 Monate“, nur beschreibend
   (die Paare sind bekannt). Bei unbestimmbarem Höchstende gilt als Obergrenze Ende der Grundlaufzeit + 12 Monate; diese Regel war NICHT vorab
   festgelegt, sondern kam beim Rechnen dazu.

Aufruf:  .venv\\Scripts\\python -I src/prepare/explorativ_iteration6.py     Ausgabe: reports/explorativ_iteration6.md
"""

import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "src" / "prepare"))
sys.path.insert(0, str(ROOT / "src" / "model"))

from baseline import lade  # noqa: E402
from vertragsliste import plus_monate  # noqa: E402

STICHTAG = date(2026, 11, 4)
REPORT = ROOT / "reports" / "explorativ_iteration6.md"


def main() -> None:
    with (ROOT / "data" / "processed" / "vertragsliste_909.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    mit_gl = [r for r in rows if r["gl_ende"]]
    zaehl = {m: sum(1 for r in mit_gl if STICHTAG <= date.fromisoformat(r["gl_ende"]) <= plus_monate(STICHTAG, m)) for m in (12, 24)}

    paare = lade()
    im = fruehe = spaete = unb = unb_im = 0
    for r in paare:
        lo, hi = plus_monate(r["gl"], -12), plus_monate(r["h"] or r["gl"], 12)
        t = lo <= r["pub"] <= hi
        im += t
        fruehe += r["pub"] < lo
        spaete += r["pub"] > hi
        if r["h"] is None:
            unb += 1
            unb_im += t
    out = [
        "# Explorative Kennzahlen Iteration 6 (ohne Schwelle)", "",
        "_Erzeugt mit `src/prepare/explorativ_iteration6.py`; Stichtag 04.11.2026._", "",
        "## Fakten", "",
        f"- Lose mit Ende der Grundlaufzeit in den nächsten 12 Monaten: **{zaehl[12]}**, in den nächsten 24 Monaten: **{zaehl[24]}** "
        f"(von {len(rows)} Losen, davon {len(mit_gl)} mit Ende der Grundlaufzeit; bundesweit, eForms-Zuschläge seit 10/2023, Haupt-CPV 909).",
        f"- Backtest-Paare (X1, n = {len(paare)}) mit Veröffentlichung der Neuausschreibung im Fenster „Ende GL − 12 Monate bis Höchstende + 12 Monate“: "
        f"**{im}/{len(paare)}**; davor {fruehe}, danach {spaete}. {unb} Paare mit unbestimmbarem Höchstende (Obergrenze GL + 12 Monate, nicht vorab "
        f"festgelegt), davon {unb_im} im Fenster.", "",
        "## Interpretation", "",
        "- Das Fenster ist oft vier Jahre und länger breit; ohne Referenz (z. B. zufällige Termine) sagt 32/52 wenig. Die Paare sind bekannt und "
        "durch die Rückwärtssuche ausgewählt, die Zahl ist nur beschreibend.",
        "- Die Zahlen zu 12 und 24 Monaten zählen Lose, nicht Verträge, und nehmen das Enddatum der Liste (auch dort, wo es das Höchstende sein könnte, "
        "siehe Abschluss Iteration 6).", "",
    ]
    REPORT.write_text("\n".join(out), encoding="utf-8")
    print(f"12 Monate {zaehl[12]}, 24 Monate {zaehl[24]}; Paare im Fenster {im}/{len(paare)}; Report {REPORT}")


if __name__ == "__main__":
    main()
