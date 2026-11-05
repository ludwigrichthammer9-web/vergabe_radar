"""Iteration 9, Schritt 2: Stichprobe für die KI-Lesung der verbesserten Vertragsliste (V1 bis V8).

Vorab festgelegt (docs/iterationen.md, Iteration 9 samt Präzisierungen; Seed und Skript werden **vor dem Ziehen** committet):
- Quelle: `data/processed/vertragsliste_909.csv` (Fassung der Iteration 9, ohne Lose ohne Zuschlag). Alte Fassung als Referenz: `vertragsliste_909_iteration8.csv`.
- Ausgeschlossen werden alle **Bekanntmachungen** der 95 Lose aus Iteration 7 und 8 (Schlüssel der Iteration 7), der Handsuche (Iteration 3 und 4),
  der Entwicklung der Regeln 1b (`reports/entwicklung_iteration7_notices.txt`) und der Regeln der Iteration 9 (`reports/entwicklung_iteration9_notices.txt`).
- Z (Zufall, V1/V3/V4): 70 Lose, Veröffentlichung Q4 2025 bis Q3 2026, Ende der Grundlaufzeit vorhanden, höchstens 2 Lose je Bekanntmachung.
- R (Regelwirkung, V2): **alle** Lose, deren Ende sich gegenüber der alten Fassung ändert und in der neuen Fassung vorhanden ist (bis zu 10, höchstens 2 je Bekanntmachung).
- M (Mehrfach-Lose, V2): Rest bis 30 Lose aus Bekanntmachungen mit mindestens 3 Losen (Fenster wie Z, nicht aus Bekanntmachungen von Z oder R, höchstens 2 je Bekanntmachung).
- S (Regel 6, beschreibend, nicht V1/V2): bis zu 10 Lose, bei denen das Ende durch Regel 6 entfällt (alte Fassung hatte ein Ende, die neue nicht).
- Menschliche Kontrolle (V6): 15 zufällige Lose aus Z, R und M (nicht S), Seed + 3.
- Alle Gruppen werden gemischt und mit N1, N2, … nummeriert; Leser und Kommilitone sehen weder Gruppe noch Listenwerte.

Aufruf:  .venv\\Scripts\\python -I src/prepare/stichprobe_iteration9.py [--trockenlauf]   (Trockenlauf: anderer Seed, schreibt nichts)
Ausgabe: reports/stichprobe_iteration9_lose.csv (Nummer, Bekanntmachung, Los, Los-Titel; ohne Listenwerte),
         data/processed/stichprobe_iteration9_schluessel.csv (lokal, mit Gruppe und Listenwerten)
"""

import csv
import hashlib
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyze_completeness import PROJECT_ROOT  # noqa: E402
from vertragsliste import OUT_CSV, X4_BIS, X4_VON  # noqa: E402

SEED = 20261109
N_Z, N_GESCHICHTET, N_R_MAX, N_S, N_MENSCH, MAX_JE_NOTICE = 70, 30, 10, 10, 15, 2
REPORTS = PROJECT_ROOT / "reports"
PROC = PROJECT_ROOT / "data" / "processed"
ALT_CSV = PROC / "vertragsliste_909_iteration8.csv"
SCHLUESSEL = PROC / "stichprobe_iteration9_schluessel.csv"
LOSE = REPORTS / "stichprobe_iteration9_lose.csv"


def ziehen(pool: list[dict], rng: random.Random, n: int, ausser: set[str]) -> list[dict]:
    pool = sorted((r for r in pool if r["notice"] not in ausser), key=lambda r: (r["notice"], int(r["los"])))
    rng.shuffle(pool)
    auswahl, je = [], Counter()
    for r in pool:
        if je[r["notice"]] >= MAX_JE_NOTICE:
            continue
        auswahl.append(r)
        je[r["notice"]] += 1
        if len(auswahl) == n:
            break
    return auswahl


def lese(p: Path) -> list[dict]:
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def liste_aus(p: Path) -> set[str]:
    return {z.strip() for z in p.read_text(encoding="utf-8").splitlines() if z.strip() and not z.startswith("#")}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    trocken = "--trockenlauf" in sys.argv
    seed = 1 if trocken else SEED
    handsuche = set()
    for f in ("sichtbarkeit_iteration3_gt.csv", "sichtbarkeit_iteration4_gt.csv"):
        handsuche |= set(re.findall(r"\d{1,6}-20\d{2}", (REPORTS / f).read_text(encoding="utf-8")))
    it7 = {r["notice"] for r in lese(PROC / "liste_pruefung_iteration7_schluessel.csv") if r["L"].startswith("L")}
    ausgeschlossen = handsuche | it7 | liste_aus(REPORTS / "entwicklung_iteration7_notices.txt") | liste_aus(REPORTS / "entwicklung_iteration9_notices.txt")

    neu = lese(OUT_CSV)
    alt = {(r["notice"], r["los"]): r for r in lese(ALT_CSV)}
    je_notice = Counter(r["notice"] for r in neu)
    im_fenster = [r for r in neu if X4_VON <= r["veroeffentlicht"] <= X4_BIS and r["gl_ende"] and r["notice"] not in ausgeschlossen]
    rng = random.Random(seed)
    z = ziehen(im_fenster, rng, N_Z, set())
    z_notices = {r["notice"] for r in z}
    r_pool = [r for r in neu if r["gl_ende"] and (r["notice"], r["los"]) in alt and alt[(r["notice"], r["los"])]["gl_ende"] != r["gl_ende"]
              and r["notice"] not in ausgeschlossen]
    r_lose = ziehen(r_pool, rng, N_R_MAX, z_notices)
    m_pool = [r for r in im_fenster if je_notice[r["notice"]] >= 3]
    m_lose = ziehen(m_pool, rng, N_GESCHICHTET - len(r_lose), z_notices | {r["notice"] for r in r_lose})
    s_pool = [r for r in neu if not r["gl_ende"] and (r["notice"], r["los"]) in alt and alt[(r["notice"], r["los"])]["gl_ende"]
              and r["notice"] not in ausgeschlossen]
    s_lose = ziehen(s_pool, rng, N_S, z_notices | {r["notice"] for r in r_lose} | {r["notice"] for r in m_lose})
    alle = [dict(r, gruppe="Z") for r in z] + [dict(r, gruppe="R") for r in r_lose] + [dict(r, gruppe="M") for r in m_lose] + [dict(r, gruppe="S") for r in s_lose]
    random.Random(seed + 2).shuffle(alle)
    v_lose = [r for r in alle if r["gruppe"] != "S"]
    mensch = {(r["notice"], r["los"]) for r in random.Random(seed + 3).sample(sorted(v_lose, key=lambda r: (r["notice"], int(r["los"]))), N_MENSCH)}
    print(f"Pool Fenster {len(im_fenster)} Lose aus {len({r['notice'] for r in im_fenster})} Bekanntmachungen; ausgeschlossene Bekanntmachungen {len(ausgeschlossen)}")
    print(f"Z {len(z)} | R {len(r_lose)} (Pool {len(r_pool)}) | M {len(m_lose)} (Pool {len(m_pool)}) | S {len(s_lose)} (Pool {len(s_pool)}) | Mensch {len(mensch)}")
    if trocken:
        print("Trockenlauf: nichts geschrieben.")
        return

    with SCHLUESSEL.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["N", "gruppe", "notice", "los", "gl_ende", "gl_herkunft", "hoechstende", "hoechstende_herkunft", "beginn", "gl_ende_alt", "gl_herkunft_alt",
                    "hoechstende_alt", "zuschlag", "mensch"])
        for i, r in enumerate(alle, 1):
            a = alt[(r["notice"], r["los"])]
            w.writerow([f"N{i}", r["gruppe"], r["notice"], r["los"], r["gl_ende"], r["gl_herkunft"], r["hoechstende"], r["hoechstende_herkunft"], r["beginn"],
                        a["gl_ende"], a["gl_herkunft"], a["hoechstende"], r["zuschlag"], "ja" if (r["notice"], r["los"]) in mensch else ""])
    with LOSE.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["N", "notice", "los", "los_titel"])
        for i, r in enumerate(alle, 1):
            w.writerow([f"N{i}", r["notice"], r["los"], r["los_titel"]])
    print(f"Schlüssel SHA-256: {hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()}")
    print(f"Lose-Liste SHA-256: {hashlib.sha256(LOSE.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
