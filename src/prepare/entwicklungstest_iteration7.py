"""Iteration 7, Schritt 1: Entwicklungstest der erweiterten Lese-Regel 1b (vertragsliste.kurze_festlaufzeit). Zählt nicht für Y1 bis Y2b.

1. Regressionstest an den 60 Losen der Iteration 6 (Eingaben aus der Vorlage `reports/liste_pruefung_iteration6.md`, Soll = Eintrag des Prüfers,
   für L60 korrigiert auf 30.06.2028 nach dem Befund des Evaluators; „unbekannt“ wird übersprungen). Erwartung: L1, L42, L43, L60 werden richtig,
   sonst ändert sich nichts. Die Auszüge der Vorlage sind auf 700 Zeichen gekürzt (BT-24), der Test ist also nur ein Näherungstest.
2. Wirkung auf die ganze Liste: Zahl der Lose, deren Ende der Grundlaufzeit sich gegenüber `data/processed/vertragsliste_909.csv` (Fassung der Iteration 6)
   ändert, nach Herkunft. Es werden keine einzelnen Lose ausgegeben.

Aufruf:  .venv\\Scripts\\python -I src/prepare/entwicklungstest_iteration7.py
"""

import csv
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "src" / "prepare"))

from analyze_completeness import RAW_SEARCH_DIR, load_notices  # noqa: E402
from auswertung_iteration6 import datum  # noqa: E402
from population_iteration4 import exclusion_reason  # noqa: E402
from vertragsliste import RUN, laufzeit, zeilen  # noqa: E402

VORLAGE = ROOT / "reports" / "liste_pruefung_iteration6.md"
URTEILE = ROOT / "reports" / "liste_pruefung_iteration6_urteile.csv"
KORREKTUR = {"L60": date(2028, 6, 30)}  # Evaluator, Abschluss Iteration 6 (Text „2+1+1“)
DEV = {"L1", "L42", "L43", "L60"}


def vorlage() -> dict[str, dict]:
    out = {}
    for block in re.split(r"\n### (?=L\d+:)", VORLAGE.read_text(encoding="utf-8").split("## Teil B")[0])[1:]:
        L = re.match(r"(L\d+):", block).group(1)
        f = re.search(r"- Felder: Beginn (\S+), Ende (\S+), Dauer (\S+?), Verlängerungen \(BT-58\) (\S+)", block)
        txt = " ".join(re.search(rf"- {k}: (.*)", block).group(1).strip() for k in ("BT-57", "BT-54", "BT-24"))
        beginn, ende, bt58 = (None if x == "–" else x for x in (f.group(1), f.group(2), f.group(4)))
        out[L] = {"beginn": date.fromisoformat(beginn) if beginn else None, "ende": date.fromisoformat(ende) if ende else None,
                  "bt58": int(bt58) if bt58 and bt58.isdigit() and int(bt58) < 100 else None, "text": txt}
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    with URTEILE.open(encoding="utf-8") as f:
        pruefer = {r["L"]: r["gl_pruefer"] for r in csv.DictReader(f, delimiter=";")}
    probleme, geaendert = [], []
    for L, v in vorlage().items():
        verl = None if v["bt58"] is None else v["bt58"] > 0
        gl, gl_h, h, h_h = laufzeit(v["beginn"], v["ende"], None, v["text"], v["bt58"] or None, verl)
        soll = KORREKTUR.get(L) or datum(pruefer[L])
        if soll is None:
            continue
        ok = bool(gl and abs((gl - soll).days) <= 1)
        if (L in DEV) != ok and not (L not in DEV and ok):
            probleme.append((L, gl, gl_h, soll))
        if gl_h.startswith("text_") and gl_h != "text_zunaechst":
            geaendert.append((L, gl, gl_h, ok))
    print("Regression (Vorlage Iteration 6): Änderungen durch Regel 1b:", geaendert)
    print("Abweichungen vom Soll (Dev-Lose müssen richtig sein, andere dürfen nicht falsch werden):", probleme or "keine")

    alt = {}
    with (ROOT / "data" / "processed" / "vertragsliste_909_iteration6.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            alt[(r["notice"], r["los"])] = r["gl_ende"]
    zaehl, n, ausser = Counter(), 0, 0
    for x in load_notices(RAW_SEARCH_DIR / RUN):
        if exclusion_reason(x):
            continue
        for r in zeilen(x):
            n += 1
            a = alt.get((r["notice"], str(r["los"])))
            if a is not None and str(r["gl_ende"]) != a:
                zaehl[r["gl_herkunft"]] += 1
    print(f"Wirkung auf die Liste: {sum(zaehl.values())} von {n} Losen ändern das Ende der Grundlaufzeit {dict(zaehl)}")


if __name__ == "__main__":
    main()
