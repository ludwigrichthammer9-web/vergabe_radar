"""Erstellt die Blindprüfung für Iteration 3 (Kriterium V4) und wertet sie aus.

Auswahl (20 Paare, festgelegt am 2026-10-24 vor dem Urteil des Nutzers):
- 3 schwach belegte Treffer der Handsuche (T4, T10, T11), vom Rechercheur zur Prüfung empfohlen
- 7 weitere Treffer der Handsuche, zufällig (Seed 20261024)
- 8 Einzelurteile von Claude zu Regelvorschlägen (T33 korrekt; T1, T8, T21, T31, T54, T58 falsch; T36 unklar)
- 2 „unklare“ Kandidaten der Handsuche (T27, T50)

Übereinstimmung (V4): Claude-Seite = Handsuche bzw. Einzelurteil. Verglichen wird binär „Vorgänger gefunden“
(objektgleich oder teilmenge) gegen „nicht gefunden“ (nicht objektgleich oder unklar). Schwelle laut iterationen.md: ≥ 85 %.

Aufruf:
    .venv\\Scripts\\python src/blindpruefung_iteration3.py            # Prüfliste erzeugen (nur einmal)
    .venv\\Scripts\\python src/blindpruefung_iteration3.py --auswerten # nach dem Ausfüllen
"""

import argparse
import csv
import hashlib
import random
import re
import sys
from pathlib import Path

from analyze_completeness import RAW_SEARCH_DIR, load_notices
from zuordnung_objekt import TEST_RUN, Pool

ROOT = Path(__file__).resolve().parent.parent
LIST = ROOT / "reports" / "blindpruefung_iteration3.md"
KEY = ROOT / "data" / "processed" / "blindpruefung_iteration3_schluessel.csv"
SEED = 20261024
TED = "https://ted.europa.eu/de/notice/-/detail/{}"

CLAUDE_PAIRS = {"T33": ("582425-2019", "gefunden"), "T1": ("442059-2026", "nicht"), "T8": ("306431-2026", "nicht"),
                "T21": ("165984-2026", "nicht"), "T31": ("467991-2026", "nicht"), "T54": ("563086-2025", "nicht"),
                "T58": ("410442-2026", "nicht"), "T36": ("436672-2026", "nicht")}
UNCLEAR_PAIRS = {"T27": "390156-2023", "T50": "216353-2021"}
WEAK = ["T4", "T10", "T11"]


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def build() -> None:
    if LIST.exists() or KEY.exists():
        sys.exit("Prüfliste existiert bereits und wird nicht neu erzeugt.")
    gt = {r["T"]: r for r in read_csv(ROOT / "reports" / "sichtbarkeit_iteration3_gt.csv")}
    rng = random.Random(SEED)
    found = sorted((t for t, r in gt.items() if r["vorgaenger"] and t not in WEAK and t not in CLAUDE_PAIRS),
                   key=lambda t: int(t[1:]))
    pairs = [(t, gt[t]["vorgaenger"].split()[0], "gefunden", "Handsuche") for t in WEAK + rng.sample(found, 7)]
    pairs += [(t, pn, key, "Einzelurteil") for t, (pn, key) in CLAUDE_PAIRS.items()]
    pairs += [(t, pn, "nicht", "Handsuche unklar") for t, pn in UNCLEAR_PAIRS.items()]
    rng.shuffle(pairs)

    tests = {n["publication-number"]: n for n in load_notices(RAW_SEARCH_DIR / TEST_RUN)}
    pool = Pool()
    out = ["# Blindprüfung Iteration 3 (Kriterium V4)", "",
           "**Bitte erst ausfüllen, bevor du andere Reports von Iteration 3 öffnest** (`sichtbarkeit_*`, `zuordnung_*`).", "",
           "Je Paar: Öffne beide Links und vergleiche Objekte (Adressen, Gebäude- bzw. Liegenschaftsnamen) und Leistungsart.",
           "Bei alten Bekanntmachungen stehen die Objekte oft unter „Ort der Ausführung“ oder in der Beschreibung.", "",
           "**Kategorien** (Definition aus `docs/iterationen.md`):",
           "- **objektgleich**: gleiche Adresse oder gleicher Liegenschaftsname **und** überlappende Leistungsart "
           "(Unterhalts-, Grund-, Glasreinigung)",
           "- **teilmenge**: mindestens ein gemeinsames Objekt (Neuzuschnitt)",
           "- **nicht objektgleich**: andere Objekte oder keine überlappende Leistungsart (z. B. Baureinigung vs. Unterhaltsreinigung)",
           "- **unklar**: nicht entscheidbar, z. B. weil keine Objekte genannt werden", "",
           "Der Zeitpunkt spielt keine Rolle. Rechne mit etwa 3 Minuten je Paar.", ""]
    keyrows = []
    for i, (t, pn, key, source) in enumerate(pairs, 1):
        test = tests[gt[t]["notice"]] if t in gt else None
        tn = gt[t]["notice"]
        ttitle = (test.get("title-proc") or {}).get("deu", "") if test else ""
        ktitle = pool.features(pn).title if pn in pool.notices else ""
        out += [f"### P{i}",
                f"- Ausschreibung (neu): [{tn}]({TED.format(tn)}) – „{ttitle[:120]}“",
                f"- Möglicher Vorgänger: [{pn}]({TED.format(pn)}) – „{ktitle[:120] or '(Titel siehe Link)'}“",
                "- Urteil: ", "- Begründung: ", ""]
        keyrows.append([f"P{i}", t, tn, pn, key, source])
    LIST.write_text("\n".join(out) + "\n", encoding="utf-8")
    KEY.parent.mkdir(parents=True, exist_ok=True)
    with KEY.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh, delimiter=";").writerows([["P", "T", "notice", "kandidat", "claude", "quelle"]] + keyrows)
    digest = hashlib.sha256(KEY.read_bytes()).hexdigest()
    print(f"Prüfliste: {LIST}\nSchlüssel: {KEY}\nSHA-256 Schlüssel: {digest}")


def evaluate() -> None:
    key = {r["P"]: r for r in read_csv(KEY)}
    text = LIST.read_text(encoding="utf-8")
    user = dict(re.findall(r"### (P\d+)\n(?:.*\n){2}- Urteil: *\**([a-zA-ZäöüÄÖÜ ]+?)\**\s*\n", text))
    missing = [p for p in key if not user.get(p, "").strip()]
    if missing:
        sys.exit(f"Noch nicht beurteilt: {', '.join(missing)}")
    agree = 0
    for p, r in key.items():
        u = user[p].strip().lower()
        u_bin = "gefunden" if u in ("objektgleich", "teilmenge") else "nicht"
        agree += u_bin == r["claude"]
        print(f"{p} {r['T']:4} Nutzer: {u:20} → {u_bin:9} | Claude: {r['claude']:9} ({r['quelle']}) {'✓' if u_bin == r['claude'] else '✗'}")
    print(f"\nV4 Übereinstimmung: {agree}/{len(key)} = {agree / len(key) * 100:.0f} % (Schwelle ≥ 85 %)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--auswerten", action="store_true")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    evaluate() if args.auswerten else build()


if __name__ == "__main__":
    main()
