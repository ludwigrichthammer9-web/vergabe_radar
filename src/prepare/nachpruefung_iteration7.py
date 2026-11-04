"""Iteration 7, Schritt 3b: verkürzte Vorlage für die Nachprüfung der Lose, bei denen der Prüfer „unbekannt“ als Ende der Grundlaufzeit eintrug.

Grund: Die erste Prüfung nutzte nur die Auszüge der Vorlage; Beginn, Ende und Dauer stehen absichtlich nur im TED-Original (docs/iterationen.md, Nachtrag).
Die Nachprüfung enthält nur Lose-Nummer, TED-Link und Los-Titel (aus `reports/liste_pruefung_iteration7.md`), **keine Listenwerte**. Der Prüfer trägt die Felder des Originals ab, den Wert
„Ende der Grundlaufzeit“ und die Quelle ein. Die vorab festgelegten Kriterien (Y1, Y1r, Y2, Y2b) bleiben; gewertet wird die Nachprüfung, wo sie einen Eintrag liefert.

Aufruf:  .venv\\Scripts\\python -I src/prepare/nachpruefung_iteration7.py      Ausgabe: reports/liste_nachpruefung_iteration7.md
"""

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
VORLAGE = ROOT / "reports" / "liste_pruefung_iteration7.md"
URTEILE = ROOT / "reports" / "liste_pruefung_iteration7_urteile.csv"
OUT = ROOT / "reports" / "liste_nachpruefung_iteration7.md"


def main() -> None:
    with URTEILE.open(encoding="utf-8") as f:
        offen = [r["L"] for r in csv.DictReader(f, delimiter=";") if r["gl_pruefer"].strip().lower() == "unbekannt"]
    bloecke = {m.group(1): m for m in re.finditer(r"### (L\d+): \[(\S+?)\]\((\S+?)\), Los (\d+)\n\n- Los-Titel: (.*)", VORLAGE.read_text(encoding="utf-8"))}
    out = [f"# Nachprüfung der Vertragsliste (Iteration 7): {len(offen)} Lose", "",
           "**Bitte ohne KI-Hilfe ausfüllen.** Nicht öffnen: `data/processed/`, `reports/vertragsliste_*.md`, `reports/beispiel_liste*`, `reports/liste_auswertung_*`, `reports/evaluation_*`.", "",
           f"Bei diesen {len(offen)} Losen trugst du in der ersten Prüfung „unbekannt“ ein. Die Texte der Vorlage sind nur Auszüge. **Öffne jetzt das Original auf TED** (Link) und suche beim angegebenen Los den Abschnitt zur Laufzeit "
           "(Beginn, Dauer, Enddatum, Verlängerungen, dazu Text der Beschreibung).", "",
           "Je Los eintragen:",
           "- **Felder des Originals:** Beginn, Ende, Dauer so, wie sie beim Los stehen (`-`, wenn leer). Nichts ausrechnen.",
           "- **Ende der Grundlaufzeit:** Datum (TT.MM.JJJJ) oder `unbekannt`. Gemeint ist das Ende der ersten festen Laufzeit **ohne** Verlängerungsoptionen. Wenn nur Beginn und Dauer stehen, selbst ausrechnen.",
           "- **Quelle:** `Text` (steht in der Beschreibung), `Feld` (nur Beginn/Ende/Dauer-Felder), `unbekannt`.",
           "- **Höchstende:** nur eintragen, wenn es sich gegenüber der ersten Prüfung ändert, sonst leer lassen.",
           "- **Hilfsmittel:** Pflicht, `keine` oder welche. **Minuten** je Los. Sitzungen (Start und Ende) unten ausfüllen.", "",
           "| Sitzung | Start | Ende | Lose |", "|---|---|---|---|", "| 1 | | | |", "| 2 | | | |", ""]
    for L in offen:
        m = bloecke[L]
        out += [f"### {L}: [{m.group(2)}]({m.group(3)}), Los {m.group(4)}", "", f"- Los-Titel: {m.group(5)}",
                "- Beginn (Feld): ", "- Ende (Feld): ", "- Dauer (Feld): ", "- Ende der Grundlaufzeit: ", "- Quelle: ", "- Höchstende (nur bei Änderung): ", "- Hilfsmittel: ", "- Minuten: ", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(offen)} Lose; SHA-256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
