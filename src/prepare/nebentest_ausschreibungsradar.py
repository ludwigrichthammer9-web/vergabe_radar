"""Iteration 10, W7: Ziehung der 15 Z-Lose für den Nebentest AusschreibungsRadar (docs/iterationen.md).

Seed 20261111, gezogen aus den Z-Losen der Iteration 9 ohne „nicht tagesgenau“ (wie V1). Es wird nur die Liste der Lose geschrieben (ohne Listen- und Vergleichswerte);
die Suche auf ausschreibungsradar.com erfolgt danach von Hand bzw. mit einzelnen Seitenabrufen, nicht per Massenabruf.

Aufruf:  .venv\\Scripts\\python -I src/prepare/nebentest_ausschreibungsradar.py      Ausgabe: reports/nebentest_ausschreibungsradar_lose.csv
"""

import csv
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vergleich_iteration10 as v10  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "reports" / "nebentest_ausschreibungsradar_lose.csv"
SEED, N = 20261111, 15


def main() -> None:
    schl, v = v10.vergleichswerte()
    z = sorted((n for n in schl if schl[n]["gruppe"] == "Z" and not v[n]["ntg"]), key=lambda x: int(x[1:]))
    ziehung = sorted(random.Random(SEED).sample(z, N), key=lambda x: int(x[1:]))
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["N", "notice", "los"])
        for n in ziehung:
            w.writerow([n, schl[n]["notice"], schl[n]["los"]])
    print(len(z), "Z-Lose;", ", ".join(ziehung))


if __name__ == "__main__":
    main()
