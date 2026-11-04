"""Iteration 8, Schritt 1: Vorlage für die KI-Zweitlesung (zwei Leser, getrennte Läufe) und Seed für die Kontrolle Z4.

Die Vorlage enthält je Los nur Nummer, Bekanntmachung, TED-Link, Los-Nummer und Los-Titel: keine Listenwerte, keine Einträge des Prüfers, keinen Hinweis auf Typ Y/R.
Lose: L1 bis L95 der Iteration 7 (aus `reports/liste_pruefung_iteration7.md`, dort ebenfalls ohne Listenwerte) und als beschreibende Kontrolle K1 bis K3
(143100-2026 Lose 8, 9, 14 des Oberpfalz-Prototyps; Entwicklungsdaten, zählen nicht). Kriterien: `docs/iterationen.md`, Iteration 8.

Z4: Nach dem Lauf zieht `auswertung_iteration8.py` mit SEED_Z4 10 Lose aus den Übereinstimmungen der Leser A und B (sortiert nach Nummer); der Evaluator prüft sie am TED-Original.

Aufruf:  .venv\\Scripts\\python -I src/prepare/zweitlesung_iteration8.py      Ausgabe: reports/zweitlesung_iteration8_vorlage.md
"""

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
QUELLE = ROOT / "reports" / "liste_pruefung_iteration7.md"
OUT = ROOT / "reports" / "zweitlesung_iteration8_vorlage.md"
SEED_Z4 = 20261108
N_Z4 = 10
TED = "https://ted.europa.eu/de/notice/{}/html"  # die Detailseite lädt per JavaScript und ist für WebFetch leer (Test 2026-11-04 an 143100-2026)
KONTROLLE = [("K1", "143100-2026", "8", "Nordbayern"), ("K2", "143100-2026", "9", "Nordbayern"), ("K3", "143100-2026", "14", "Nordbayern")]

AUFTRAG = """# Vorlage KI-Zweitlesung (Iteration 8)

Lies für jedes Los die Bekanntmachung auf TED (Link, HTML-Fassung; lange Seiten mit `offset` weiterlesen, bis der Abschnitt des Loses gefunden ist) und dort den Abschnitt **zu genau diesem Los**
(Los n der Vorlage entspricht meist „LOT-000n“ der Bekanntmachung; der Los-Titel hilft bei der Zuordnung, sein Wortlaut kann eine andere Nummer nennen): Beginn, Ende, Dauer, Verlängerung/Optionen und die Beschreibung des Loses
(bei Bedarf auch die allgemeine Beschreibung des Verfahrens). Lies wie ein Mensch den ganzen Text, nicht nur einzelne Felder.

Je Los eine Zeile im Format (Semikolon, keine Semikolons im Zitat):
`Nr;ende_grundlaufzeit;hoechstende;zitat;gebaeudereinigung`

- **ende_grundlaufzeit:** Ende der ersten festen Laufzeit **ohne** Verlängerungsoptionen, als TT.MM.JJJJ, oder `unbekannt`. Stehen nur Beginn und Dauer da, selbst ausrechnen (Ende = Beginn + Dauer − 1 Tag).
  Nennt der Text eine kürzere feste Laufzeit als das Enddatum-Feld (z. B. „zwei Jahre mit Option auf …“, „Festlaufzeit bis …“), gilt die kürzere.
- **hoechstende:** Ende, wenn alle Verlängerungen gezogen werden (TT.MM.JJJJ), oder `keine Verlängerung`, `keine Angabe` (nichts zu Verlängerungen gesagt) oder `unbestimmbar` (Verlängerung genannt, Ende nicht berechenbar).
- **zitat:** die tragende Stelle wörtlich (höchstens etwa 300 Zeichen), mit Feldname, falls es ein Feld ist (z. B. „Enddatum der Laufzeit: 31/12/2028“).
- **gebaeudereinigung:** `ja` oder `nein` (nein z. B. bei Schädlingsbekämpfung, Kanal-, Fahrzeug- oder Industriereinigung, Mietkleidung).

## Lose
"""


def main() -> None:
    bloecke = re.findall(r"### (L\d+): \[(\S+?)\]\((\S+?)\), Los (\S+)\n\n- Los-Titel: (.*)", QUELLE.read_text(encoding="utf-8"))
    assert [b[0] for b in bloecke] == [f"L{i}" for i in range(1, 96)], "L1 bis L95 erwartet"
    zeilen = [f"| {nr} | {notice} | {los} | {titel.strip()} | {TED.format(notice)} |" for nr, notice, _link, los, titel in bloecke]
    zeilen += [f"| {nr} | {notice} | {los} | {titel} | {TED.format(notice)} |" for nr, notice, los, titel in KONTROLLE]
    OUT.write_text(AUFTRAG + "\n| Nr | Bekanntmachung | Los | Los-Titel | TED-Link |\n|---|---|---|---|---|\n" + "\n".join(zeilen) + "\n", encoding="utf-8")
    print(f"{len(zeilen)} Lose; SHA-256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
