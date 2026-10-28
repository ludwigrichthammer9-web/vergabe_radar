"""Blindprüfung W4 (Iteration 4): 20 Paare, vom Nutzer nach Urteilsregeln 1.1 beurteilt, gegen die Ground Truth.

Zusammensetzung (vorab festgelegt, je Testfall höchstens ein Paar, Seed SEED):
- A: 6 Vorschläge der Regel (reports/zuordnung_iteration4_lauf.json); Schlüssel aus Handsuche bzw. Paarurteil
- B: 6 weitere Fälle mit Vorgänger laut Handsuche, Paar mit dem jüngsten Vorgänger; Schlüssel „gefunden“
- C: 4 Fälle „unklar“ der Handsuche, Paar mit deren bestem Kandidaten; Schlüssel „nicht“
- D: 4 Fälle „kein Vorgänger“, Paar mit dem ersten Kandidaten der Regel; Schlüssel „nicht“
Gemischt mit SEED, nummeriert P1–P20. Schlüssel nur lokal in data/processed/ (Hash wird ausgegeben und committet).

Zählweise W4 (wie Iteration 3): binär, „gefunden“ = objektgleich (hoch/mittel) oder teilmenge, „nicht“ = nicht objektgleich oder unklar.
Zusätzlich: Median der Prüfzeit in Minuten (Folge laut iterationen.md: ≤ 5 Minuten je Paar).

Aufruf:
    python -I src/blindpruefung_iteration4.py               # Liste und Schlüssel erzeugen (einmalig)
    python -I src/blindpruefung_iteration4.py --auswerten   # Urteile in reports/blindpruefung_iteration4.md auswerten
"""

import argparse
import csv
import hashlib
import json
import random
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
LIST = REPORTS / "blindpruefung_iteration4.md"
KEY = ROOT / "data" / "processed" / "blindpruefung_iteration4_schluessel.csv"
SEED = 20261027
FOUND = ("objektgleich_hoch", "objektgleich_mittel", "teilmenge")
URL = "https://ted.europa.eu/de/notice/-/detail/{}"


def load() -> tuple[dict, list, dict]:
    gt = {r["notice"]: r for r in csv.DictReader(open(REPORTS / "sichtbarkeit_iteration4_gt.csv", encoding="utf-8"), delimiter=";")}
    runs = json.loads((REPORTS / "zuordnung_iteration4_lauf.json").read_text(encoding="utf-8"))
    pairs = {}
    for line in (REPORTS / "paarbeurteilung_iteration4.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip().strip("*") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and re.fullmatch(r"Q\d+", cells[0]):
            alt, neu = (re.search(r"\d{1,6}-20\d\d", c).group(0) for c in cells[1:3])
            pairs[(alt, neu)] = cells[3]
    return gt, runs, pairs


def build() -> None:
    if LIST.exists() or KEY.exists():
        sys.exit("Blindprüfung existiert bereits und wird nicht neu erzeugt.")
    gt, runs, pairs = load()
    rng = random.Random(SEED)
    used, items = set(), []

    def take(pool: list, n: int, gruppe: str) -> None:
        pool = [x for x in pool if x[0] not in used]
        for case, alt, key in rng.sample(pool, n):
            used.add(case)
            items.append({"case": case, "alt": alt, "gruppe": gruppe, "schluessel": key})

    by_case = {r["case"]: r for r in runs}
    a = []
    for r in runs:
        p = r["proposal"]
        if p:
            g = gt[r["case"]]
            ok = p["pn"] in g["vorgaenger"].split() or any(k in pairs.get((p["pn"], r["case"]), "") for k in FOUND)
            a.append((r["case"], p["pn"], "gefunden" if ok else "nicht"))
    take(sorted(a), 6, "A")
    take(sorted((n, g["vorgaenger"].split()[0], "gefunden") for n, g in gt.items() if g["kategorie"] in FOUND), 6, "B")
    take(sorted((n, g["kandidat_unklar"].split()[0], "nicht") for n, g in gt.items()
                if g["kategorie"] == "unklar" and g["kandidat_unklar"]), 4, "C")
    take(sorted((n, by_case[n]["top"][0]["pn"], "nicht") for n, g in gt.items()
                if g["kategorie"] == "kein_vorgaenger" and by_case[n]["top"]), 4, "D")
    rng.shuffle(items)

    KEY.parent.mkdir(parents=True, exist_ok=True)
    with open(KEY, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["P", "U", "neu", "alt", "gruppe", "schluessel"])
        for i, it in enumerate(items, 1):
            w.writerow([f"P{i}", gt[it["case"]]["U"], it["case"], it["alt"], it["gruppe"], it["schluessel"]])
    digest = hashlib.sha256(KEY.read_bytes()).hexdigest()

    out = ["# Blindprüfung Iteration 4 (Kriterium W4)", "",
           "**Bitte erst ausfüllen, bevor du Reports von Iteration 4 öffnest** (`sichtbarkeit_iteration4_*`, `zuordnung_iteration4*`, "
           "`paarbeurteilung_iteration4*`).", "",
           "Beurteile jedes Paar nach [Urteilsregeln Version 1.1](urteilsregeln_blindpruefung.md). Öffne nur die beiden Bekanntmachungen "
           "eines Paares. Zeitabstand, Vertragsende, Laufzeit und Auftragswert spielen keine Rolle.", "",
           "Je Paar eintragen:",
           "- **Urteil:** objektgleich | teilmenge | nicht objektgleich | unklar",
           "- **Sicherheit** (nur bei objektgleich): hoch | mittel",
           "- **Tendenz** (nur bei unklar): eher dafür | eher dagegen | keine",
           "- **Minuten:** wie lange du für das Paar gebraucht hast (ganze Minuten)",
           "- **Begründung:** ein Satz mit Feld und Wert", ""]
    for i, it in enumerate(items, 1):
        out += [f"### P{i}", f"- Alt: [{it['alt']}]({URL.format(it['alt'])})", f"- Neu: [{it['case']}]({URL.format(it['case'])})",
                "- Urteil: ", "- Sicherheit: ", "- Tendenz: ", "- Minuten: ", "- Begründung: ", ""]
    LIST.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(items)} Paare nach {LIST.relative_to(ROOT)}; Schlüssel {KEY.relative_to(ROOT)}, SHA-256 {digest}")


def evaluate() -> None:
    key = {r["P"]: r for r in csv.DictReader(open(KEY, encoding="utf-8"), delimiter=";")}
    text = LIST.read_text(encoding="utf-8")
    blocks = dict(re.findall(r"###\s*(P\d+)\b(.*?)(?=\n###\s*P\d+\b|\Z)", text, re.S))
    agree, minutes, rows, missing = 0, [], [], []
    for p, r in key.items():
        b = blocks.get(p, "")
        m = re.search(r"Urteil:\s*\**\s*([^\n]*)", b)
        line = (m.group(1) if m else "").lower()
        cat = ("nicht objektgleich" if "nicht" in line else "teilmenge" if "teilmenge" in line
               else "objektgleich" if "objektgleich" in line else "unklar" if "unklar" in line else "")
        if not cat:
            missing.append(p)
            continue
        user = "gefunden" if cat in ("objektgleich", "teilmenge") else "nicht"
        agree += user == r["schluessel"]
        t = re.search(r"Minuten:\s*\**\s*(\d+(?:[.,]\d+)?)", b)
        if t:
            minutes.append(float(t.group(1).replace(",", ".")))
        rows.append(f"{p:4} {r['U']:4} Gruppe {r['gruppe']}  Nutzer: {cat:19} → {user:9} | Schlüssel: {r['schluessel']:9} "
                    f"{'✓' if user == r['schluessel'] else '✗'}")
    if missing:
        sys.exit(f"Noch nicht beurteilt: {', '.join(missing)}")
    print("\n".join(rows))
    n = len(key)
    print(f"\nW4 (binär): Übereinstimmung {agree}/{n} = {agree / n:.0%} (Schwelle ≥ 85 %)")
    if minutes:
        print(f"Prüfzeit: Median {statistics.median(minutes):g} Minuten je Paar (n = {len(minutes)}; Folge bei ≤ 5)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--auswerten", action="store_true")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    evaluate() if args.auswerten else build()


if __name__ == "__main__":
    main()
