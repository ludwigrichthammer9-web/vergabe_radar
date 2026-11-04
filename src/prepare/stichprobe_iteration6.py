"""Iteration 6, Schritt 2: Stichprobe zur Prüfung der Vertragsliste (Y1, Y2) und 10 Paare der Handsuche ohne Hilfsmittel (A18).

Vorab festgelegt (docs/iterationen.md, Iteration 6):
- 60 zufällige Lose aus `data/processed/vertragsliste_909.csv` (Veröffentlichung Q4 2025 bis Q3 2026, Ende der Grundlaufzeit vorhanden), höchstens 2 Lose je Zuschlag,
  ohne Lose aus `reports/hoechstende_pruefung_iteration5_*.md` und ohne Notices der Handsuche (Iteration 3 und 4). Seed 20261105.
- Der Prüfer sieht die Originaltexte (BT-57, BT-54, BT-24, Beginn, Laufzeitfelder) und trägt **selbst** Ende der Grundlaufzeit und Höchstende ein. Die Werte der Liste
  stehen nur im lokalen Schlüssel (SHA-256 wird ausgegeben und in docs/iterationen.md festgehalten, bevor der Prüfer abgibt).
- 10 Paare der Handsuche (aus den 57 gewerteten Paaren der Zweitprüfung Iteration 5, ohne die Kalibrierungsbeispiele), die der Prüfer ohne Hilfsmittel nach Urteilsregeln 1.1 beurteilt.

Aufruf:  python src/prepare/stichprobe_iteration6.py
Ausgabe: reports/liste_pruefung_iteration6.md (Vorlage), data/processed/liste_pruefung_iteration6_schluessel.csv (lokal)
"""

import csv
import hashlib
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyze_completeness import PROJECT_ROOT, RAW_SEARCH_DIR, load_notices  # noqa: E402
from vertragsliste import OUT_CSV, RUN, X4_BIS, X4_VON, _liste, je_los  # noqa: E402

SEED = 20261105
N_LOSE = 60
N_PAARE = 10
REPORTS = PROJECT_ROOT / "reports"
VORLAGE = REPORTS / "liste_pruefung_iteration6.md"
SCHLUESSEL = PROJECT_ROOT / "data" / "processed" / "liste_pruefung_iteration6_schluessel.csv"
TED_LINK = "https://ted.europa.eu/de/notice/-/detail/{}"


def kurz(t, n=700) -> str:
    t = " ".join(str(t or "").split()).replace("|", "/")
    return t[:n] + (" …" if len(t) > n else "")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    handsuche = set()
    for f in ("sichtbarkeit_iteration3_gt.csv", "sichtbarkeit_iteration4_gt.csv"):
        handsuche |= set(re.findall(r"\d{1,6}-20\d{2}", (REPORTS / f).read_text(encoding="utf-8")))
    gesehen = set()
    for f in REPORTS.glob("hoechstende_pruefung_iteration5_*.md"):
        gesehen |= set(re.findall(r"## H\d+: (\S+) Los (\d+)", f.read_text(encoding="utf-8")))
    with OUT_CSV.open(encoding="utf-8") as f:
        pool = [r for r in csv.DictReader(f, delimiter=";")
                if X4_VON <= r["veroeffentlicht"] <= X4_BIS and r["gl_ende"] and r["notice"] not in handsuche
                and (r["notice"], r["los"]) not in gesehen]
    pool.sort(key=lambda r: (r["notice"], int(r["los"])))
    rng = random.Random(SEED)
    rng.shuffle(pool)
    auswahl, je_notice = [], {}
    for r in pool:
        if je_notice.get(r["notice"], 0) >= 2:
            continue
        auswahl.append(r)
        je_notice[r["notice"]] = je_notice.get(r["notice"], 0) + 1
        if len(auswahl) == N_LOSE:
            break
    notices = {x["publication-number"]: x for x in load_notices(RAW_SEARCH_DIR / RUN) if x["publication-number"] in {r["notice"] for r in auswahl}}

    # Paare der Handsuche (Zweitprüfung Iteration 5), ohne Kalibrierungsbeispiele
    with (PROJECT_ROOT / "data" / "processed" / "gt_pruefung_iteration5_schluessel.csv").open(encoding="utf-8") as f:
        schl = {r["P"]: r for r in csv.DictReader(f, delimiter=";")}
    with (REPORTS / "gt_pruefung_iteration5_urteile.csv").open(encoding="utf-8") as f:
        gewertet = [r["P"] for r in csv.DictReader(f, delimiter=";") if r["urteil"] != "nicht_beurteilt"]
    kandidaten = sorted(p for p in gewertet if schl[p]["rolle"] == "paar")
    paare = random.Random(SEED + 1).sample(kandidaten, N_PAARE)

    with SCHLUESSEL.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["L", "notice", "los", "gl_ende", "gl_herkunft", "hoechstende", "hoechstende_herkunft", "beginn"])
        for i, r in enumerate(auswahl, 1):
            w.writerow([f"L{i}", r["notice"], r["los"], r["gl_ende"], r["gl_herkunft"], r["hoechstende"], r["hoechstende_herkunft"], r["beginn"]])
        for j, p in enumerate(paare, 1):
            w.writerow([f"Q{j}", schl[p]["testfall"], "", "", "", "", "", f"Paar {p} der Zweitprüfung Iteration 5 (Handsuche: {schl[p]['gt']}; vorheriges Urteil KI-unterstützt)"])
    sha = hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()

    out = ["# Prüfung der Vertragsliste (Iteration 6, Kriterien Y1 und Y2) und 10 Paare ohne Hilfsmittel (A18)", "",
           "**Bitte ohne KI-Hilfe ausfüllen** (Hilfsmittel je Eintrag unten vermerken). Nicht öffnen vor dem Ausfüllen: `data/processed/`, `reports/vertragsliste_iteration5.md`, "
           "`reports/hoechstende_pruefung_iteration5_*.md`.", "",
           "## Teil A: 60 Lose, Ende der Grundlaufzeit und Höchstende aus dem Originaltext", "",
           "Je Los eintragen (Quelle: Original-Bekanntmachung über den TED-Link; die Auszüge unten dienen nur dem schnelleren Lesen):",
           "- **Ende der Grundlaufzeit:** Datum (TT.MM.JJJJ) oder `unbekannt`. Gemeint ist das Ende der ersten festen Laufzeit **ohne** Verlängerungsoptionen.",
           "- **Höchstende:** Datum, wenn Optionen/Verlängerungen mit Ende oder Länge genannt sind (Ende mit allen Verlängerungen); `keine Verlängerung`, wenn der Text keine nennt; `unbestimmbar`, wenn Verlängerung erwähnt, aber Länge oder Anzahl fehlt.",
           "- **Hilfsmittel:** `keine` oder welche. **Minuten:** ganze Minuten.", "",
           f"_Erzeugt mit `src/prepare/stichprobe_iteration6.py`, Seed {SEED}. Schlüssel lokal, SHA-256 `{sha}`._", ""]
    for i, r in enumerate(auswahl, 1):
        n = notices[r["notice"]]
        k = len(_liste(n.get("title-lot"))) or 1
        idx = int(r["los"]) - 1
        g = lambda feld: je_los(n, feld, k)[0][idx]  # noqa: E731
        titel = g("title-lot")
        out += [f"### L{i}: [{r['notice']}]({TED_LINK.format(r['notice'])}), Los {r['los']}", "",
                f"- Los-Titel: {kurz(titel, 200)}",
                f"- Felder: Beginn {str(g('contract-duration-start-date-lot') or '–')[:10]}, Ende {str(g('contract-duration-end-date-lot') or '–')[:10]}, "
                f"Dauer {g('contract-duration-period-lot') or '–'}, Verlängerungen (BT-58) {g('renewal-maximum-lot') or '–'}",
                f"- BT-57: {kurz(g('renewal-description-lot'))}",
                f"- BT-54: {kurz(g('option-description-lot'))}",
                f"- BT-24: {kurz(g('description-lot'), 500)}",
                "- Ende der Grundlaufzeit: ", "- Höchstende: ", "- Hilfsmittel: ", "- Minuten: ", ""]
    out += ["## Teil B: 10 Paare der Handsuche, nach Urteilsregeln 1.1 ohne Hilfsmittel beurteilen", "",
            "Je Paar Urteil (objektgleich | teilmenge | nicht objektgleich | unklar), Sicherheit/Tendenz, Hilfsmittel, Minuten und eine Begründung wie in der Zweitprüfung Iteration 5.", ""]
    for j, p in enumerate(paare, 1):
        t, v = schl[p]["testfall"], schl[p]["vorgaenger"]
        out += [f"### Q{j}", f"- Alt: [{v}]({TED_LINK.format(v)})", f"- Neu: [{t}]({TED_LINK.format(t)})",
                "- Urteil: ", "- Sicherheit: ", "- Tendenz: ", "- Hilfsmittel: ", "- Minuten: ", "- Begründung: ", ""]
    VORLAGE.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(auswahl)} Lose aus {len(je_notice)} Zuschlägen, {len(paare)} Paare; Pool {len(pool)}")
    print(f"Schlüssel SHA-256: {sha}")


if __name__ == "__main__":
    main()
