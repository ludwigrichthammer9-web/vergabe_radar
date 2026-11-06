"""Blatt für den Wizard-of-Oz-Test (Business Understanding, Ersatz für den LLM-Profilfilter als gebautes Produkt).

Idee: Ein Betrieb bekommt 5 echte, laufende Oberpfälzer Lose (Auftraggeber, Ort, Laufzeit, Wert falls vorhanden, Link zur Bekanntmachung) und sagt,
ob er bieten würde und warum. Die Begründungen zeigen, ob die Entscheidungsgründe aus den Gesprächen (Entfernung, Personal, Größe, Kapazität, Bürokratie)
mit den vorhandenen TED-Feldern abbildbar sind, und wofür ein Betrieb Informationen bräuchte (Auftragnehmer, Preis, Bieterzahl).

Auswahl (vorab festgelegt): aus reports/wettbewerbsbild_oberpfalz.csv Lose mit Status der Liste „Grundlaufzeit läuft“, höchstens 1 Los je Auftraggeber,
Seed 20261117, 5 Lose; Auftragnehmer, Wert und Angebote werden NICHT gezeigt (erst am Ende als Zusatzfrage), damit sie die Entscheidung nicht lenken.
Geänderte Auswahlregel (offen, nach der Gesamtprüfung am 2026-11-06): Bevorzugt werden Lose mit Ende der Grundlaufzeit frühestens 2027-01-01 und
spätestens 2029-12-31 (nah genug, dass die Neuausschreibung für einen Betrieb greifbar ist); reicht dieser Pool nicht für 5 verschiedene Auftraggeber,
wird mit den übrigen Losen (gleicher Seed) aufgefüllt. Seed und Mischung bleiben 20261117; die Auswahl kann sich dadurch gegenüber der ersten Fassung ändern.
Zusätzlich je Los: Text der Bekanntmachung (Beschreibung des Loses, cbc:Description im Los-Abschnitt des eForms-XML in data/raw/ted_xml/wettbewerbsbild_20261105),
auf höchstens drei Sätze gekürzt; keine Listenwerte. Randfälle (Autobahn, nur Fenster-/Glasreinigung, Vertretungsreinigung) werden gekennzeichnet.

Aufruf:  .venv\\Scripts\\python -I src/report/wizard_of_oz_blatt.py      Ausgabe: docs/wizard_of_oz_blatt.md
"""

import csv
import random
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from webseite import NUTS  # noqa: E402  (Namen der NUTS-3-Codes, geprüft in Paket Webseite)

ROOT = Path(__file__).resolve().parent.parent.parent
CSV = ROOT / "reports" / "wettbewerbsbild_oberpfalz.csv"
OUT = ROOT / "docs" / "wizard_of_oz_blatt.md"
XML_DIR = ROOT / "data" / "raw" / "ted_xml" / "wettbewerbsbild_20261105"
SEED, N = 20261117, 5
VON, BIS = "2027-01-01", "2029-12-31"
NS = {"cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2", "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"}
KEIN_TEXT = "keine Beschreibung in der Bekanntmachung"


def beschreibung(notice: str, lot: str, titel: str) -> str:
    """Beschreibung des Loses aus dem eForms-XML, auf höchstens drei Sätze gekürzt; sonst KEIN_TEXT."""
    pfad = XML_DIR / f"{notice}.xml"
    if not pfad.exists():
        return KEIN_TEXT
    root = ET.parse(pfad).getroot()
    text = ""
    for pl in root.findall("cac:ProcurementProjectLot", NS):
        if (pl.findtext("cbc:ID", "", NS) or "").strip() == lot:
            text = (pl.findtext("cac:ProcurementProject/cbc:Description", "", NS) or "").strip()
            break
    text = re.sub(r"\s+", " ", text)
    if not text or text.strip().lower() == (titel or "").strip().lower():
        return KEIN_TEXT
    saetze = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ„\"])", text)
    kurz = " ".join(saetze[:3])
    return kurz if len(kurz) <= 350 else kurz[:347].rsplit(" ", 1)[0] + " …"


def randfall(r: dict, text: str = "") -> str:
    t = f"{r['auftraggeber']} {r['los_titel_liste']}".lower()
    if "autobahn" in t:
        return "Reinigung entlang Autobahn, evtl. keine Gebäudereinigung"
    if re.search(r"fenster|glas", t) and not re.search(r"unterhalt|grund", t):
        return "nur Fenster-/Glasreinigung (Teilleistung), keine Unterhaltsreinigung"
    if "interim" in text.lower():
        return "Interimsvergabe (kurze Übergangsleistung), Beschreibung in der Bekanntmachung teils widersprüchlich"
    if "vertretung" in r["los_titel_liste"].lower():
        return "Vertretungsreinigung (Springerleistung für Reinigungskräfte des Auftraggebers)"
    return ""


def main() -> None:
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        zeilen = [r for r in csv.DictReader(f, delimiter=";") if r["status_liste"] == "Grundlaufzeit läuft" and r["vertragsende_gl"]]
    with (ROOT / "reports" / "beispiel_liste_oberpfalz.csv").open(encoding="utf-8-sig", newline="") as f:
        region = {(r["notice"], r["los"]): " / ".join(NUTS.get(c, c) for c in r["nuts"].split()) for r in csv.DictReader(f, delimiter=";")}
    random.Random(SEED).shuffle(zeilen)
    bevorzugt = [r for r in zeilen if VON <= r["vertragsende_gl"] <= BIS]
    gewaehlt, gesehen = [], set()
    for r in bevorzugt + [r for r in zeilen if r not in bevorzugt]:
        if r["auftraggeber"] not in gesehen:
            gesehen.add(r["auftraggeber"])
            gewaehlt.append(r)
        if len(gewaehlt) == N:
            break
    gewaehlt.sort(key=lambda r: r["vertragsende_gl"])

    out = ["# Blatt für das Gespräch: fünf Aufträge, würden Sie bieten?", "",
           "_Für ein kurzes Gespräch mit einem Reinigungsbetrieb (10 bis 15 Minuten). Keine Namen von Personen notieren, Betrieb nur beschreibend (Größe, Region). "
           "Die Aufträge sind echte, laufende Verträge aus der Oberpfalz-Liste (TED-Zuschlagsbekanntmachungen); gezeigt werden nur Auftraggeber, Los, Text der Bekanntmachung, Laufzeit und der Link zur Bekanntmachung. "
           f"Auswahl: Seed {SEED}, höchstens ein Los je Auftraggeber, bevorzugt Ende der Grundlaufzeit {VON} bis {BIS} (Skript `src/report/wizard_of_oz_blatt.py`)._", "",
           "**Stichprobe und Stand:** 3 bis 5 Betriebe, auch ein Betrieb ohne öffentliche Aufträge. Einwilligung vorher klären. Ergebnis nur als Hinweis. "
           "Bis zur Abgabe nur „vorbereitet, nicht durchgeführt“, falls keine Antworten vorliegen.", "",
           "**Vorab festgelegte Schwelle für die Auswertung:** Ein Textfilter lohnt sich, wenn bei mindestens 3 von 5 Aufträgen die Entscheidungsgründe aus dem gezeigten Text ablesbar waren; sonst reichen Entfernung und Laufzeit.", "",
           "**Einstieg (zum Ablesen):** „Ich zeige Ihnen fünf Aufträge, die in einigen Jahren wieder ausgeschrieben werden könnten. "
           "Sagen Sie mir bitte zu jedem, ob Sie dafür grundsätzlich bieten würden, und warum oder warum nicht. Es gibt keine falschen Antworten.“", ""]
    for i, r in enumerate(gewaehlt, 1):
        txt = beschreibung(r["notice"], r["los_zugeordnet"], r["los_titel_xml"])
        rf = randfall(r, txt)
        out += [f"## Auftrag {i}",
                f"- Auftraggeber: {r['auftraggeber']}",
                f"- Los: {r['los_titel_liste']}",
                f"- Text der Bekanntmachung: {txt}",
                *([f"- Randfall (Hinweis für die Gesprächsführung): {rf}"] if rf else []),
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
            "## Fragen zur Systemlandschaft (ein Betrieb, 5 Minuten)", "",
            "_Hintergrund: Die Idee ist, dass ein Betrieb seine Aufträge selbst filtert und das Ergebnis als Datei in sein Verwaltungssystem übernimmt; die Webseite stellt nur dar. "
            "Zeigen Sie `docs/prototyp/export/vertragsliste_v1_de.csv` in Excel (Schema: `docs/export_schema.md`). Antworten sind Aussagen, keine Zusagen._", "",
            "| Frage | Antwort (wörtlich) |", "|---|---|",
            "| Wer filtert heute bei Ihnen Ausschreibungen (Rolle, nicht Name)? | |",
            "| In welchem System landet das Ergebnis? (E-Mail, Excel, ERP/CRM, Kalkulationssoftware, nichts) | |",
            "| Wer pflegt das, und wie viel Zeit je Woche? | |",
            "| Könnten Sie eine CSV mit festem Schema in Ihr System laden? (Datei in Excel zeigen; Spalten, die Sie bräuchten oder nicht bräuchten) | |",
            "| Was fehlt Ihnen an kostenlosen Wegen? (TED-Suchprofil, Bekanntmachungsservice, Vergabeweiser) | |",
            "| Würden Sie so etwas selbst betreiben oder einkaufen, und wo liegt Ihre Schmerzgrenze beim Preis? (Aussage, keine Zusage) | |", "",
            "- Auswertung Systemlandschaft: H1/H2 (siehe docs/iterationen.md Paket D): bestätigt / nicht bestätigt, Begründung: ____", "",
            "## Auswertung (nach dem Gespräch, 5 Minuten)", "",
            "- Für wie viele der fünf Aufträge konnte der Betrieb **allein mit den gezeigten Angaben** entscheiden? ____ von 5",
            "- Welche Gründe kamen vor, die **nicht** aus Bekanntmachungsfeldern (Ort, Laufzeit, Auftraggeber) ablesbar sind? (z. B. Personal, Kapazität, Bürokratie, Fläche): ____",
            "- Gründe aus dem gezeigten Text ablesbar bei ____ von 5 Aufträgen (Schwelle: mindestens 3 von 5 → Textfilter lohnt sich; sonst reichen Entfernung und Laufzeit).",
            "- Was folgt daraus für einen Profilfilter? Nach der vorab festgelegten Schwelle: ____",
            "- Bezug zu den Annahmen: A1 / A15 (stützt, schwächt, neutral, kurz begründen): ____", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(len(gewaehlt), "Lose;", OUT)


if __name__ == "__main__":
    main()
