"""Iteration 10b: Ziehung der Stichprobe (160 Lose) für den Vergleich Liste gegen Vergabeweiser (docs/iterationen.md, Iteration 10b).

Vorab festgelegt: Seed 20261112; Population = Lose der Liste (Fassung 9, data/processed/vertragsliste_909.csv) mit Zuschlag (zuschlag == "ja") und mit Ende der
Grundlaufzeit; höchstens 2 Lose je Bekanntmachung; ausgeschlossen alle Bekanntmachungen der Iterationen 6, 7 und 9 (Schlüsseldateien), die Entwicklungslisten
der Iterationen 7 und 9 sowie 527230-2026 und 105754-2026. Skript und Seed werden vor dem Ziehen committet.

Aufruf:  .venv\\Scripts\\python -I src/prepare/stichprobe_iteration10b.py
Ausgabe: data/processed/stichprobe_iteration10b_schluessel.csv (lokal, nicht im Git; SHA-256 im Commit), reports/stichprobe_iteration10b_lose.csv (nur N, Bekanntmachung, Los)
"""

import csv
import hashlib
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PROC, R = ROOT / "data" / "processed", ROOT / "reports"
SEED, N, MAX_JE_BEKANNTMACHUNG = 20261112, 160, 2
SCHLUESSEL = [PROC / "liste_pruefung_iteration6_schluessel.csv", PROC / "liste_pruefung_iteration7_schluessel.csv", PROC / "stichprobe_iteration9_schluessel.csv"]
ENTWICKLUNG = [R / "entwicklung_iteration7_notices.txt", R / "entwicklung_iteration9_notices.txt"]
SONST = {"527230-2026", "105754-2026"}


def main() -> None:
    ausgeschlossen = set(SONST)
    for p in SCHLUESSEL:
        with p.open(encoding="utf-8") as f:
            ausgeschlossen |= {r["notice"] for r in csv.DictReader(f, delimiter=";")}
    for p in ENTWICKLUNG:
        ausgeschlossen |= set(re.findall(r"\b\d{1,6}-\d{4}\b", p.read_text(encoding="utf-8")))
    with (PROC / "vertragsliste_909.csv").open(encoding="utf-8-sig") as f:
        liste = [r for r in csv.DictReader(f, delimiter=";") if r["zuschlag"] == "ja" and r["gl_ende"] and r["notice"] not in ausgeschlossen]
    rng = random.Random(SEED)
    rng.shuffle(liste)
    je, ziehung = {}, []
    for r in liste:
        if je.get(r["notice"], 0) < MAX_JE_BEKANNTMACHUNG:
            je[r["notice"]] = je.get(r["notice"], 0) + 1
            ziehung.append(r)
        if len(ziehung) == N:
            break
    ziehung.sort(key=lambda r: (r["notice"], int(r["los"])))
    schl = PROC / "stichprobe_iteration10b_schluessel.csv"
    with schl.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["N", "notice", "los", "los_titel", "auftraggeber", "gl_ende", "gl_herkunft", "hoechstende", "hoechstende_herkunft", "beginn"])
        for i, r in enumerate(ziehung, 1):
            w.writerow([f"M{i}", r["notice"], r["los"], r["los_titel"], r["auftraggeber"], r["gl_ende"], r["gl_herkunft"], r["hoechstende"], r["hoechstende_herkunft"], r["beginn"]])
    with (R / "stichprobe_iteration10b_lose.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["N", "notice", "los"])
        for i, r in enumerate(ziehung, 1):
            w.writerow([f"M{i}", r["notice"], r["los"]])
    print(f"Population {len(liste)} Lose, ausgeschlossene Bekanntmachungen {len(ausgeschlossen)}, gezogen {len(ziehung)} aus {len({r['notice'] for r in ziehung})} Bekanntmachungen")
    print("SHA-256 Schlüssel:", hashlib.sha256(schl.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
