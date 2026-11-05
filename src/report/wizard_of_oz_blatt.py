"""Blatt für den Wizard-of-Oz-Test (Business Understanding, Ersatz für den LLM-Profilfilter als gebautes Produkt).

Idee: Ein Betrieb bekommt 5 echte, laufende Oberpfälzer Lose (Auftraggeber, Ort, Laufzeit, Wert falls vorhanden, Link zur Bekanntmachung) und sagt,
ob er bieten würde und warum. Die Begründungen zeigen, ob die Entscheidungsgründe aus den Gesprächen (Entfernung, Personal, Größe, Kapazität, Bürokratie)
mit den vorhandenen TED-Feldern abbildbar sind, und wofür ein Betrieb Informationen bräuchte (Auftragnehmer, Preis, Bieterzahl).

Auswahl (vorab festgelegt): aus reports/wettbewerbsbild_oberpfalz.csv Lose mit Status der Liste „Grundlaufzeit läuft“, höchstens 1 Los je Auftraggeber,
Seed 20261117, 5 Lose; Auftragnehmer, Wert und Angebote werden NICHT gezeigt (erst am Ende als Zusatzfrage), damit sie die Entscheidung nicht lenken.

Aufruf:  .venv\\Scripts\\python -I src/report/wizard_of_oz_blatt.py      Ausgabe: docs/wizard_of_oz_blatt.md
"""

import csv
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from webseite import NUTS  # noqa: E402  (Namen der NUTS-3-Codes, geprüft in Paket Webseite)

ROOT = Path(__file__).resolve().parent.parent.parent
CSV = ROOT / "reports" / "wettbewerbsbild_oberpfalz.csv"
OUT = ROOT / "docs" / "wizard_of_oz_blatt.md"
SEED, N = 20261117, 5


def main() -> None:
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        zeilen = [r for r in csv.DictReader(f, delimiter=";") if r["status_liste"] == "Grundlaufzeit läuft" and r["vertragsende_gl"]]
    with (ROOT / "reports" / "beispiel_liste_oberpfalz.csv").open(encoding="utf-8-sig", newline="") as f:
        region = {(r["notice"], r["los"]): " / ".join(NUTS.get(c, c) for c in r["nuts"].split()) for r in csv.DictReader(f, delimiter=";")}
    random.Random(SEED).shuffle(zeilen)
    gewaehlt, gesehen = [], set()
    for r in zeilen:
        if r["auftraggeber"] not in gesehen:
            gesehen.add(r["auftraggeber"])
            gewaehlt.append(r)
        if len(gewaehlt) == N:
            break
    gewaehlt.sort(key=lambda r: r["vertragsende_gl"])

    out = ["# Blatt für das Gespräch: fünf Aufträge, würden Sie bieten?", "",
           "_Für ein kurzes Gespräch mit einem Reinigungsbetrieb (10 bis 15 Minuten). Keine Namen von Personen notieren, Betrieb nur beschreibend (Größe, Region). "
           "Die Aufträge sind echte, laufende Verträge aus der Oberpfalz-Liste (TED-Zuschlagsbekanntmachungen); gezeigt werden nur Auftraggeber, Los, Laufzeit und der Link zur Bekanntmachung. "
           f"Auswahl: Seed {SEED}, höchstens ein Los je Auftraggeber (Skript `src/report/wizard_of_oz_blatt.py`)._", "",
           "**Einstieg (zum Ablesen):** „Ich zeige Ihnen fünf Aufträge, die in einigen Jahren wieder ausgeschrieben werden könnten. "
           "Sagen Sie mir bitte zu jedem, ob Sie dafür grundsätzlich bieten würden, und warum oder warum nicht. Es gibt keine falschen Antworten.“", ""]
    for i, r in enumerate(gewaehlt, 1):
        out += [f"## Auftrag {i}",
                f"- Auftraggeber: {r['auftraggeber']}",
                f"- Los: {r['los_titel_liste']}",
                f"- Region: {region.get((r['notice'], r['los']), 'nicht angegeben')}",
                f"- Laufzeit: {r['beginn'] or 'Beginn nicht angegeben'} bis {r['vertragsende_gl']} (Ende der Grundlaufzeit laut Bekanntmachung; Höchstende: {r['hoechstende'] or 'nicht bekannt'})",
                f"- Bekanntmachung: {r['ted_link']}", "",
                "| Frage | Antwort (wörtlich) |", "|---|---|",
                "| Würden Sie bieten? (ja / nein / vielleicht) | |",
                "| Warum? (Entfernung, Personal, Größe, Kapazität, Bürokratie, Preis, anderes) | |",
                "| Was müssten Sie noch wissen, um zu entscheiden? | |", ""]
    out += ["## Zum Schluss (nach den fünf Aufträgen)", "",
            "| Frage | Antwort (wörtlich) |", "|---|---|",
            "| Welche Angabe hätte Ihnen bei der Entscheidung am meisten geholfen? (Vertragsende, aktueller Auftragnehmer, Preis der letzten Vergabe, Zahl der Bieter, Reinigungsfläche, Turnus, Nachweise) | |",
            "| Würden Sie für eine solche Auswahl zahlen? Wenn ja, wofür und in welcher Größenordnung? (Aussage, keine Zusage) | |",
            "| Kennen Sie Vergabeweiser oder AusschreibungsRadar? Was fehlt dort? | |", "",
            "## Auswertung (nach dem Gespräch, 5 Minuten)", "",
            "- Für wie viele der fünf Aufträge konnte der Betrieb **allein mit den gezeigten Angaben** entscheiden? ____ von 5",
            "- Welche Gründe kamen vor, die **nicht** aus Bekanntmachungsfeldern (Ort, Laufzeit, Auftraggeber) ablesbar sind? (z. B. Personal, Kapazität, Bürokratie, Fläche): ____",
            "- Was folgt daraus für einen Profilfilter? Wenn die meisten Gründe nicht aus den Feldern ablesbar sind, kann ein Filter nur Entfernung und Laufzeit abbilden und braucht keine KI; wenn sie aus dem Text der Bekanntmachung ablesbar sind, wäre ein Textfilter sinnvoll: ____",
            "- Bezug zu den Annahmen: A1 / A15 (stützt, schwächt, neutral, kurz begründen): ____", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(len(gewaehlt), "Lose;", OUT)


if __name__ == "__main__":
    main()
