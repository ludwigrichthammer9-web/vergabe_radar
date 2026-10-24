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
    # pandas-abhängige Module nur hier laden, damit die Auswertung ohne pandas läuft
    from analyze_completeness import RAW_SEARCH_DIR, load_notices
    from zuordnung_objekt import TEST_RUN, Pool

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


def parse_judgments(text: str) -> dict[str, tuple[str, str]]:
    """Urteil je Paar aus einer Prüfdatei: (Kategorie, Sicherheit). Erkennt z. B. „objektgleich (mittel)“, „nicht objektgleich“."""
    out = {}
    for p, block in re.findall(r"(?:###\s*|Paar:\s*)(P?\d+)\b(.*?)(?=\n(?:###\s*|Paar:\s*)P?\d+\b|\Z)", text, re.S):
        p = p if p.startswith("P") else f"P{p}"
        m = re.search(r"Urteil:\s*\**\s*([^\n]*)", block)
        if not m:
            continue
        line = m.group(1).lower()
        if "nicht objektgleich" in line:
            cat = "nicht objektgleich"
        elif "teilmenge" in line:
            cat = "teilmenge"
        elif "objektgleich" in line:
            cat = "objektgleich"
        elif "unklar" in line:
            cat = "unklar"
        else:
            continue
        sicher = "hoch" if "hoch" in line else ("mittel" if "mittel" in line else "")
        if cat == "objektgleich" and not sicher:
            s = re.search(r"Sicherheit:\s*\**\s*(hoch|mittel)", block, re.I)
            sicher = s.group(1).lower() if s else ""
        out[p] = (cat, sicher)
    return out


def evaluate(path: Path = LIST, label: str = "Nutzer") -> None:
    key = {r["P"]: r for r in read_csv(KEY)}
    user = parse_judgments(path.read_text(encoding="utf-8"))
    missing = [p for p in key if p not in user]
    if missing:
        sys.exit(f"Noch nicht beurteilt ({label}): {', '.join(missing)}")
    agree = 0
    for p, r in key.items():
        cat, sicher = user[p]
        u_bin = "gefunden" if cat in ("objektgleich", "teilmenge") else "nicht"
        agree += u_bin == r["claude"]
        shown = f"{cat} ({sicher})" if sicher else cat
        print(f"{p:4} {r['T']:4} {label}: {shown:22} → {u_bin:9} | Claude: {r['claude']:9} ({r['quelle']}) "
              f"{'✓' if u_bin == r['claude'] else '✗'}")
    n = len(key)
    print(f"\nV4-Zählweise (binär, vorab festgelegt): Übereinstimmung {agree}/{n} = {agree / n * 100:.0f} % (Schwelle ≥ 85 %)")
    # Spanne laut urteilsregeln_blindpruefung.md, Schritt 4: Anteil „gefunden“ aus Sicht dieses Prüfers
    strict = sum(1 for c, s in user.values() if c == "objektgleich" and s == "hoch")
    broad_hits = sum(1 for c, _ in user.values() if c in ("objektgleich", "teilmenge"))
    broad_base = sum(1 for c, _ in user.values() if c != "unklar")
    print(f"Regeln Schritt 4 – streng: {strict}/{n} objektgleich (hoch); breit: {broad_hits}/{broad_base} (ohne {n - broad_base} unklar)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--auswerten", action="store_true")
    parser.add_argument("--datei", help="andere Prüfdatei auswerten, z. B. reports/blindpruefung_iteration3_agent.md")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if args.auswerten:
        evaluate(ROOT / args.datei, "Agent") if args.datei else evaluate()
    else:
        build()


if __name__ == "__main__":
    main()
