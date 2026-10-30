"""Iteration 5, Schritt 3: Stichprobe zur Prüfung der Lese-Regeln für das Höchstende (vertragsliste.py).

Je Herkunft (datum_text, anzahl_x_laenge, hoechstlaufzeit_text, unbestimmbar) 10 zufällige Lose (Seed 20261030) aus der
Zuschlagstabelle. Ausgenommen sind alle Notices, die in der Handsuche von Iteration 3 oder 4 vorkommen (Backtest-Paare bleiben
ungesehen). Der Report zeigt je Los die Texte BT-57, BT-54 und die Verlängerungssätze aus BT-24 sowie das extrahierte Höchstende;
das Urteil wird von Hand in die Spalte „Urteil“ eingetragen.

Zwei Durchgänge:
- Entwicklung (Seed 20261030): Fehler daraus führten zu Regel 1a und weiteren Mustern in vertragsliste.py.
- Test (Seed 20261031): erst nach der Korrektur gezogen, ohne die Lose der Entwicklung; misst die Genauigkeit der Lese-Regeln.

Aufruf:  python src/prepare/pruefung_hoechstende.py entwicklung|test
Ausgabe: reports/hoechstende_pruefung_iteration5_<durchgang>.md
"""

import argparse
import csv
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyze_completeness import PROJECT_ROOT, RAW_SEARCH_DIR, load_notices  # noqa: E402
from vertragsliste import OUT_CSV, RE_SATZ_ENDE, RUN, _liste, je_los, saetze  # noqa: E402

SEEDS = {"entwicklung": 20261030, "test": 20261031}
JE_HERKUNFT = 10
HERKUNFT = {"entwicklung": ("datum_text", "anzahl_x_laenge", "hoechstlaufzeit_text", "unbestimmbar"),
            "test": ("datum_text", "anzahl_x_laenge", "hoechstlaufzeit_text", "unbestimmbar", "enddatum_ist_hoechstende",
                     "keine_angabe")}
GT_FILES = ("reports/sichtbarkeit_iteration3_gt.csv", "reports/sichtbarkeit_iteration4_gt.csv")
REPORTS = PROJECT_ROOT / "reports"


def kurz(t: str, n: int = 400) -> str:
    t = " ".join(str(t or "").split()).replace("|", "/")
    return t[:n] + (" …" if len(t) > n else "")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("durchgang", choices=list(SEEDS))
    durchgang = parser.parse_args().durchgang
    SEED = SEEDS[durchgang]
    REPORT = REPORTS / f"hoechstende_pruefung_iteration5_{durchgang}.md"
    gt = set()
    for f in GT_FILES:
        gt |= set(re.findall(r"\d{1,6}-20\d{2}", (PROJECT_ROOT / f).read_text(encoding="utf-8")))
    gesehen = set()
    if durchgang == "test":
        gesehen = set(re.findall(r"## H\d+: (\S+) Los (\d+)",
                                 (REPORTS / "hoechstende_pruefung_iteration5_entwicklung.md").read_text(encoding="utf-8")))
    with OUT_CSV.open(encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f, delimiter=";") if r["notice"] not in gt and (r["notice"], r["los"]) not in gesehen]
    rng = random.Random(SEED)
    auswahl = []
    for h in HERKUNFT[durchgang]:
        pool = [r for r in rows if r["hoechstende_herkunft"] == h]
        auswahl += rng.sample(pool, min(JE_HERKUNFT, len(pool)))
    notices = {x["publication-number"]: x for x in load_notices(RAW_SEARCH_DIR / RUN)
               if x["publication-number"] in {r["notice"] for r in auswahl}}
    out = [f"# Prüfung der Lese-Regeln für das Höchstende (Iteration 5, Schritt 3, {durchgang})", "",
           f"_Erzeugt mit `src/prepare/pruefung_hoechstende.py {durchgang}`, Seed {SEED}, je Herkunft {JE_HERKUNFT} Lose, ohne "
           "Notices der Handsuche. Urteil von Hand: **richtig**, **falsch** (mit richtigem Wert) oder **unklar**._", ""]
    for i, r in enumerate(auswahl, 1):
        x = notices[r["notice"]]
        n = len(_liste(x.get("title-lot"))) or 1
        idx = int(r["los"]) - 1
        txt = {k: je_los(x, f, n)[0][idx] for k, f in
               (("BT-57", "renewal-description-lot"), ("BT-54", "option-description-lot"), ("BT-24", "description-lot"))}
        out += [f"## H{i}: {r['notice']} Los {r['los']} ({r['hoechstende_herkunft']})", "",
                f"- Beginn {r['beginn'] or '–'}, Ende Grundlaufzeit {r['gl_ende']} ({r['gl_herkunft']}), BT-58 {r['bt58'] or '–'}",
                f"- **Extrahiert: Höchstende {r['hoechstende'] or 'unbestimmbar'}**",
                f"- BT-57: {kurz(txt['BT-57'])}", f"- BT-54: {kurz(txt['BT-54'])}",
                f"- BT-24 (nur Sätze zu Laufzeit/Verlängerung): {kurz(saetze(str(txt['BT-24'] or ''), RE_SATZ_ENDE))}",
                "- Urteil: ", ""]
    REPORT.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(auswahl)} Lose; Report: {REPORT}")


if __name__ == "__main__":
    main()
