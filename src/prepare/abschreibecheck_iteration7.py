"""Iteration 7, Schritt 4b: Abschreibe-Check der Nachprüfung. Vergleicht die vom Prüfer abgeschriebenen Felder Beginn/Ende (Feld) mit den Rohdaten der Bekanntmachung
(contract-duration-start-date-lot / contract-duration-end-date-lot des jeweiligen Loses). Das ist kein Urteil über die Grundlaufzeit, sondern prüft nur, ob richtig abgeschrieben wurde.

Aufruf:  .venv\Scripts\python -I src/prepare/abschreibecheck_iteration7.py      Ausgabe: reports/abschreibecheck_iteration7.md
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "src" / "prepare"))

from analyze_completeness import RAW_SEARCH_DIR, load_notices  # noqa: E402
from auswertung_iteration6 import datum  # noqa: E402
from vertragsliste import RUN, _liste, je_los  # noqa: E402


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    with (ROOT / "data" / "processed" / "liste_pruefung_iteration7_schluessel.csv").open(encoding="utf-8") as f:
        key = {r["L"]: r for r in csv.DictReader(f, delimiter=";")}
    with (ROOT / "reports" / "liste_nachpruefung_iteration7_urteile.csv").open(encoding="utf-8") as f:
        nach = {r["L"]: r for r in csv.DictReader(f, delimiter=";")}
    noti = {x["publication-number"]: x for x in load_notices(RAW_SEARCH_DIR / RUN) if x["publication-number"] in {key[L]["notice"] for L in nach}}
    gleich, abw = 0, []
    for L, n in nach.items():
        if not n["beginn_feld"] and not n["ende_feld"]:
            continue
        k = key[L]
        x = noti[k["notice"]]
        kk = len(_liste(x.get("title-lot"))) or 1
        i = int(k["los"]) - 1
        b, e = (je_los(x, f, kk)[0][i] for f in ("contract-duration-start-date-lot", "contract-duration-end-date-lot"))
        rb, re = (datum(str(v)[:10]) if v else None for v in (b, e))
        if datum(n["beginn_feld"]) == rb and datum(n["ende_feld"]) == re:
            gleich += 1
        else:
            abw.append((L, k["notice"], k["los"], n["beginn_feld"], n["ende_feld"], rb, re))
    out = ["# Abschreibe-Check der Nachprüfung (Iteration 7)", "",
           "_Erzeugt mit `src/prepare/abschreibecheck_iteration7.py`. Vergleich der abgeschriebenen Felder Beginn und Ende mit den Rohdaten (`contract-duration-start-date-lot`, `contract-duration-end-date-lot`) des Loses. "
           "Kein Urteil über die Grundlaufzeit._", "",
           f"- Mit Feldwerten abgeschrieben: {gleich + len(abw)} Lose; Beginn und Ende stimmen mit den Rohdaten überein: **{gleich}**, weichen ab: **{len(abw)}**.", "",
           "| L | Notice, Los | Prüfer: Beginn | Prüfer: Ende | Rohdaten: Beginn | Rohdaten: Ende |", "|---|---|---|---|---|---|"]
    for L, nn, los, pb, pe, rb, re in abw:
        out.append(f"| {L} | {nn}, {los} | {pb} | {pe} | {rb} | {re} |")
    (ROOT / "reports" / "abschreibecheck_iteration7.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"gleich {gleich}, abweichend {len(abw)}")


if __name__ == "__main__":
    main()
