"""Iteration 7, Schritt 2: Stichprobe zur Prüfung der Vertragsliste nach der Regel 1b (Y1, Y2, Y2b) und Regelwirkungs-Lose.

Vorab festgelegt (docs/iterationen.md, Iteration 7; Seed und Skript werden **vor dem Ziehen** committet):
- 80 zufällige Lose aus `data/processed/vertragsliste_909.csv` (Fassung mit Regel 1b; Veröffentlichung Q4 2025 bis Q3 2026, Ende der Grundlaufzeit vorhanden),
  höchstens 2 Lose je Zuschlag. Ausgeschlossen: Lose der Prüfung der Iteration 6 und ihre Bekanntmachungen, Lose der Stichproben aus Iteration 5, Notices der Handsuche,
  Notices aus `reports/entwicklung_iteration7_notices.txt` (beim Entwickeln der Regel angesehen).
- Regelwirkung: bis zu 15 weitere Lose (gleiche Ausschlüsse, aber beliebiges Veröffentlichungsdatum, höchstens 2 je Zuschlag, nicht aus Zuschlägen der 80), bei denen Regel 1b das Ende der Grundlaufzeit gegenüber der
  Fassung der Iteration 6 (`vertragsliste_909_iteration6.csv`) ändert. Beide Gruppen werden gemischt und fortlaufend nummeriert; der Prüfer sieht nicht, welches Los zu welcher gehört.
- Die Vorlage zeigt Los-Titel, TED-Link und die Originaltexte BT-57, BT-54, BT-24, **nicht** Beginn, Ende, Dauer, BT-58 und nicht die Werte der Liste.

Aufruf:  .venv\\Scripts\\python -I src/prepare/stichprobe_iteration7.py [--trockenlauf]   (Trockenlauf: anderer Seed, schreibt nichts)
Ausgabe: reports/liste_pruefung_iteration7.md (Vorlage), data/processed/liste_pruefung_iteration7_schluessel.csv (lokal)
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

SEED = 20261106
N_LOSE = 80
N_REGEL = 15
MAX_JE_NOTICE = 2
REPORTS = PROJECT_ROOT / "reports"
VORLAGE = REPORTS / "liste_pruefung_iteration7.md"
SCHLUESSEL = PROJECT_ROOT / "data" / "processed" / "liste_pruefung_iteration7_schluessel.csv"
ALT_CSV = PROJECT_ROOT / "data" / "processed" / "vertragsliste_909_iteration6.csv"
TED_LINK = "https://ted.europa.eu/de/notice/-/detail/{}"
REGEL_HERKUNFT = {"text_festlaufzeit", "text_laufzeit_option"}


def kurz(t, n=700) -> str:
    t = " ".join(str(t or "").split()).replace("|", "/")
    return t[:n] + (" …" if len(t) > n else "")


def ziehen(pool: list[dict], rng: random.Random, n: int) -> list[dict]:
    pool = sorted(pool, key=lambda r: (r["notice"], int(r["los"])))
    rng.shuffle(pool)
    auswahl, je_notice = [], {}
    for r in pool:
        if je_notice.get(r["notice"], 0) >= MAX_JE_NOTICE:
            continue
        auswahl.append(r)
        je_notice[r["notice"]] = je_notice.get(r["notice"], 0) + 1
        if len(auswahl) == n:
            break
    return auswahl


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    trocken = "--trockenlauf" in sys.argv
    seed = 1 if trocken else SEED
    handsuche = set()
    for f in ("sichtbarkeit_iteration3_gt.csv", "sichtbarkeit_iteration4_gt.csv"):
        handsuche |= set(re.findall(r"\d{1,6}-20\d{2}", (REPORTS / f).read_text(encoding="utf-8")))
    gesehen = set()
    for f in REPORTS.glob("hoechstende_pruefung_iteration5_*.md"):
        gesehen |= set(re.findall(r"## H\d+: (\S+) Los (\d+)", f.read_text(encoding="utf-8")))
    with (PROJECT_ROOT / "data" / "processed" / "liste_pruefung_iteration6_schluessel.csv").open(encoding="utf-8") as f:
        it6 = [r for r in csv.DictReader(f, delimiter=";") if r["L"].startswith("L")]
    it6_notices = {r["notice"] for r in it6}
    entwicklung = {z.strip() for z in (REPORTS / "entwicklung_iteration7_notices.txt").read_text(encoding="utf-8").splitlines()
                   if z.strip() and not z.startswith("#")}
    ausgeschlossen = handsuche | it6_notices | entwicklung

    with OUT_CSV.open(encoding="utf-8") as f:
        liste = list(csv.DictReader(f, delimiter=";"))
    with ALT_CSV.open(encoding="utf-8") as f:
        alt = {(r["notice"], r["los"]): r["gl_ende"] for r in csv.DictReader(f, delimiter=";")}
    pool = [r for r in liste if X4_VON <= r["veroeffentlicht"] <= X4_BIS and r["gl_ende"] and r["notice"] not in ausgeschlossen
            and (r["notice"], r["los"]) not in gesehen]
    rng = random.Random(seed)
    haupt = ziehen(pool, rng, N_LOSE)
    haupt_notices = {r["notice"] for r in haupt}
    # Regelwirkung ohne Veröffentlichungsfenster: Die Regel ändert nur wenige Lose, im Fenster Q4 2025 bis Q3 2026 blieben nach den Ausschlüssen kaum welche übrig.
    regel_pool = [r for r in liste if r["gl_ende"] and r["gl_herkunft"] in REGEL_HERKUNFT and alt.get((r["notice"], r["los"])) != r["gl_ende"]
                  and r["notice"] not in ausgeschlossen and (r["notice"], r["los"]) not in gesehen and r["notice"] not in haupt_notices]
    regel = ziehen(regel_pool, rng, N_REGEL)
    alle = [dict(r, typ="Y") for r in haupt] + [dict(r, typ="R") for r in regel]
    random.Random(seed + 2).shuffle(alle)
    print(f"Pool {len(pool)} Lose aus {len({r['notice'] for r in pool})} Zuschlägen; Hauptstichprobe {len(haupt)} ({len({r['notice'] for r in haupt})} Zuschläge); "
          f"Regelwirkung {len(regel)} (Pool {len(regel_pool)}); davon in der Hauptstichprobe mit Regel 1b: "
          f"{sum(1 for r in haupt if r['gl_herkunft'] in REGEL_HERKUNFT)}")
    if trocken:
        print("Trockenlauf: nichts geschrieben.")
        return

    notices = {x["publication-number"]: x for x in load_notices(RAW_SEARCH_DIR / RUN) if x["publication-number"] in {r["notice"] for r in alle}}
    with SCHLUESSEL.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["L", "typ", "notice", "los", "gl_ende", "gl_herkunft", "hoechstende", "hoechstende_herkunft", "beginn", "gl_ende_iteration6"])
        for i, r in enumerate(alle, 1):
            w.writerow([f"L{i}", r["typ"], r["notice"], r["los"], r["gl_ende"], r["gl_herkunft"], r["hoechstende"], r["hoechstende_herkunft"], r["beginn"],
                        alt.get((r["notice"], r["los"]), "")])
    sha = hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()

    out = [f"# Prüfung der Vertragsliste (Iteration 7, Kriterien Y1, Y2, Y2b): {len(alle)} Lose", "",
           "**Bitte ohne KI-Hilfe ausfüllen.** Nicht öffnen vor dem Ausfüllen: `data/processed/`, `reports/vertragsliste_*.md`, `reports/beispiel_liste*`, `reports/liste_auswertung_*`, `reports/evaluation_*`.", "",
           "Quelle ist die **Original-Bekanntmachung** über den TED-Link; die Texte unten (BT-57, BT-54, BT-24) sind nur Auszüge. Die Felder zu Beginn, Ende und Dauer der Liste sind hier absichtlich nicht angegeben.", "",
           "Je Los eintragen:",
           "- **Ende der Grundlaufzeit:** Datum (TT.MM.JJJJ). Gemeint ist das Ende der ersten festen Laufzeit **ohne** Verlängerungsoptionen.",
           "- **Quelle:** `Text` (die Laufzeit steht im Text der Bekanntmachung), `Feld` (nur das Laufzeitfeld der Bekanntmachung nennt ein Ende, der Text nichts), `unbekannt` (weder Text noch Feld nennen ein Ende; dann Ende der Grundlaufzeit `unbekannt`).",
           "- **Höchstende:** Datum, wenn Optionen/Verlängerungen mit Ende oder Länge genannt sind (Ende mit allen Verlängerungen); `keine Verlängerung`, wenn der Text keine nennt; `unbestimmbar`, wenn Verlängerung erwähnt, aber Länge oder Anzahl fehlt.",
           "- **Hilfsmittel:** Pflichtfeld, `keine` oder welche. **Minuten:** ganze Minuten je Los.", "",
           "Sitzungen (Start und Ende, Datum und Uhrzeit):", "", "| Sitzung | Start | Ende | Lose |", "|---|---|---|---|",
           "| 1 | | | |", "| 2 | | | |", "| 3 | | | |", "| 4 | | | |", "",
           f"_Erzeugt mit `src/prepare/stichprobe_iteration7.py`, Seed {SEED}. Schlüssel lokal, SHA-256 `{sha}`._", ""]
    for i, r in enumerate(alle, 1):
        n = notices[r["notice"]]
        k = len(_liste(n.get("title-lot"))) or 1
        idx = int(r["los"]) - 1
        g = lambda feld: je_los(n, feld, k)[0][idx]  # noqa: E731
        out += [f"### L{i}: [{r['notice']}]({TED_LINK.format(r['notice'])}), Los {r['los']}", "",
                f"- Los-Titel: {kurz(g('title-lot'), 200)}",
                f"- BT-57: {kurz(g('renewal-description-lot'), 900)}",
                f"- BT-54: {kurz(g('option-description-lot'), 900)}",
                f"- BT-24: {kurz(g('description-lot'), 600)}",
                "- Ende der Grundlaufzeit: ", "- Quelle: ", "- Höchstende: ", "- Hilfsmittel: ", "- Minuten: ", ""]
    VORLAGE.write_text("\n".join(out), encoding="utf-8")
    print(f"Schlüssel SHA-256: {sha}")
    print(f"Vorlage SHA-256: {hashlib.sha256(VORLAGE.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
