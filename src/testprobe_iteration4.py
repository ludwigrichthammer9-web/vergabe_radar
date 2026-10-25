"""Zieht die Testprobe für Iteration 4 (W1–W6): 70 Ausschreibungen aus Q1 2026, höchstens 2 je Auftraggeber.

Population wie in src/population_iteration4.py (festgelegt vor dem Laden der Testdaten, Commit 71e5d57). Ausgeschlossen sind zusätzlich
Notices aus reports/bekannte_notices_iteration4.txt (in Reports von Iteration 2/3 genannt) und reports/dev_gesehene_q1_notices.txt
(bei der Regelentwicklung als Kandidat gesehen). Ablauf wie Iteration 3: Population nach Notice-Nummer sortieren, mit dem Seed mischen und
der Reihe nach übernehmen, solange der Auftraggeber (erster normalisierter Name) noch keine 2 Fälle hat.

Ergebnis:
    reports/testfaelle_iteration4.txt   Notice-Nummern (Eingabe für zuordnung_los.py --test und den Rechercheur)
    reports/testfaelle_iteration4.md    Liste mit Auftraggeber, Titel, Link; Größe der Population (für W5)

Aufruf (einmalig; vorhandene Ergebnisdateien werden nicht überschrieben):
    .venv\\Scripts\\python src/testprobe_iteration4.py
"""

import collections
import json
import random
import sys
from pathlib import Path

from los_merkmale import norm
from population_iteration4 import KNOWN_FILE, MAX_PER_BUYER, TEST_SEED, TEST_SIZE, exclusion_reason, title

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORT_DIR = PROJECT_ROOT / "reports"
TEST_RUN = "DEU_competition_cpv9091main_20260101_20260331_lostext"
SEEN_FILE = REPORT_DIR / "dev_gesehene_q1_notices.txt"
TED_URL = "https://ted.europa.eu/de/notice/-/detail/{}"


def buyer_key(n: dict) -> str:
    names = n.get("buyer-name") or {}
    vals = names.get("deu") if isinstance(names, dict) and names.get("deu") else [v for vs in names.values() for v in vs]
    return norm(vals[0]) if vals else ""


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    txt, md = REPORT_DIR / "testfaelle_iteration4.txt", REPORT_DIR / "testfaelle_iteration4.md"
    if txt.exists() or md.exists():
        sys.exit("Testprobe existiert bereits und wird nicht neu gezogen.")
    notices = []
    for f in sorted((PROJECT_ROOT / "data" / "raw" / "ted_search" / TEST_RUN).glob("page_*.json")):
        notices += json.loads(f.read_bytes().decode("utf-8")).get("notices", [])
    excluded = set(KNOWN_FILE.read_text(encoding="utf-8").split()) | set(SEEN_FILE.read_text(encoding="utf-8").split())
    reasons = collections.Counter((exclusion_reason(n) or "in Population") for n in notices)
    pop = sorted((n for n in notices if exclusion_reason(n) is None), key=lambda n: n["publication-number"])
    eligible = [n for n in pop if n["publication-number"] not in excluded]
    rng = random.Random(TEST_SEED)
    rng.shuffle(eligible)
    per_buyer, sample = collections.Counter(), []
    for n in eligible:
        key = buyer_key(n)
        if per_buyer[key] < MAX_PER_BUYER:
            per_buyer[key] += 1
            sample.append(n)
        if len(sample) == TEST_SIZE:
            break
    txt.write_text("\n".join(n["publication-number"] for n in sample) + "\n", encoding="utf-8")
    out = ["# Testfälle Iteration 4 (Q1 2026)", "",
           f"Erzeugt mit `src/testprobe_iteration4.py` (Seed {TEST_SEED}, höchstens {MAX_PER_BUYER} je Auftraggeber) aus "
           f"`data/raw/ted_search/{TEST_RUN}/`.", "",
           f"Notices im Download: {len(notices)}. Population nach `src/population_iteration4.py`: **{len(pop)}**. Davon ausgeschlossen, "
           f"weil bereits bekannt oder bei der Entwicklung gesehen: {len(pop) - len(eligible)}. Ziehbar: {len(eligible)}.", "",
           "| Grund | Anzahl |", "|---|---|"]
    out += [f"| {r} | {c} |" for r, c in reasons.most_common()]
    out += ["", "| Nr | Notice | Datum | Auftraggeber | Titel |", "|---|---|---|---|---|"]
    for i, n in enumerate(sample, 1):
        names = n.get("buyer-name") or {}
        buyer = (names.get("deu") or [""])[0] if isinstance(names, dict) else ""
        out.append(f"| U{i} | [{n['publication-number']}]({TED_URL.format(n['publication-number'])}) | "
                   f"{str(n['publication-date'])[:10]} | {buyer[:60]} | {title(n)[:90].replace('|', '/')} |")
    md.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Population {len(pop)}, ziehbar {len(eligible)}, Stichprobe {len(sample)}, "
          f"Auftraggeber in der Stichprobe {len(set(map(buyer_key, sample)))}")


if __name__ == "__main__":
    main()
