"""Zieht die Testprobe für Iteration 3 (V1–V5): 60 Ausschreibungen aus Q3 2026, höchstens 2 je Auftraggeber.

Population wie in src/population_iteration3.py. Ablauf: Population nach Notice-Nummer sortieren, mit Seed 20261024 mischen und der Reihe
nach übernehmen, solange der Auftraggeber (erster normalisierter Name) noch keine 2 Fälle hat.

Ergebnis:
    reports/testfaelle_iteration3.txt   Notice-Nummern (Eingabe für zuordnung_objekt.py --test und den Rechercheur)
    reports/testfaelle_iteration3.md    Liste mit Auftraggeber, Titel, Link; Größe der Population (für V5)
"""

import collections
import random
import sys
from pathlib import Path

from analyze_completeness import RAW_SEARCH_DIR, load_notices
from objekt_merkmale import norm
from population_iteration3 import exclusion_reason, title
from zuordnung_objekt import TEST_RUN

SEED = 20261024
N = 60
MAX_PER_BUYER = 2
REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"
TED_URL = "https://ted.europa.eu/de/notice/-/detail/{}"


def buyer_key(n: dict) -> str:
    names = n.get("buyer-name") or {}
    vals = names.get("deu") if isinstance(names, dict) and names.get("deu") else [v for vs in names.values() for v in vs]
    return norm(vals[0]) if vals else ""


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    notices = load_notices(RAW_SEARCH_DIR / TEST_RUN)
    reasons = collections.Counter((exclusion_reason(n) or "in Population") for n in notices)
    pop = sorted((n for n in notices if exclusion_reason(n) is None), key=lambda n: n["publication-number"])
    rng = random.Random(SEED)
    rng.shuffle(pop)
    per_buyer, sample = collections.Counter(), []
    for n in pop:
        key = buyer_key(n)
        if per_buyer[key] < MAX_PER_BUYER:
            per_buyer[key] += 1
            sample.append(n)
        if len(sample) == N:
            break
    (REPORT_DIR / "testfaelle_iteration3.txt").write_text("\n".join(n["publication-number"] for n in sample) + "\n", encoding="utf-8")
    out = ["# Testfälle Iteration 3 (Q3 2026)", "",
           f"Erzeugt mit `src/testprobe_iteration3.py` (Seed {SEED}, höchstens {MAX_PER_BUYER} je Auftraggeber) aus "
           f"`data/raw/ted_search/{TEST_RUN}/`.", "",
           f"Notices im Download: {len(notices)}. Population (Original-Ausschreibungen, Haupt-CPV 90910/90911/90919, ohne "
           f"Ausschlussbegriffe): **{len(pop)}**.", "", "| Grund | Anzahl |", "|---|---|"]
    out += [f"| {r} | {c} |" for r, c in reasons.most_common()]
    out += ["", "| Nr | Notice | Datum | Auftraggeber | Titel |", "|---|---|---|---|---|"]
    for i, n in enumerate(sample, 1):
        names = n.get("buyer-name") or {}
        buyer = (names.get("deu") or [""])[0] if isinstance(names, dict) else ""
        out.append(f"| T{i} | [{n['publication-number']}]({TED_URL.format(n['publication-number'])}) | "
                   f"{str(n['publication-date'])[:10]} | {buyer[:60]} | {title(n)[:90].replace('|', '/')} |")
    (REPORT_DIR / "testfaelle_iteration3.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Population {len(pop)}, Stichprobe {len(sample)}, Auftraggeber in der Stichprobe {len(set(map(buyer_key, sample)))}")


if __name__ == "__main__":
    main()
