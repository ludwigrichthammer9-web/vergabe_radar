"""Paket C (Nachtrag zu Iteration 10, 2026-11-05): Ursachen der 33 Lose ohne Ende (Stufe F) und Suche nach dem Fehlertyp
„Dauerfeld enthält die Gesamtdauer einschließlich Option“ (Fall 527230-2026).

Teil 1  Die 33 Lose der Stufe F in reports/beispiel_liste_oberpfalz.csv (Definition: src/report/beispiel_liste.py, Regel 2: F = kein Ende
        der Grundlaufzeit und keine Schätzung). Je Bekanntmachung werden die Rohfelder aus data/raw/ted_search/DEU_result_cpv909_20231025_20260930_lostext
        gelesen und das TED-XML (neu geladen nach data/raw/ted_xml/stufe_f_20261105/, Pause 1,2 s) auf Laufzeitelemente geprüft.
        Jedes Los bekommt GENAU EINE Ursache (Zuordnung von Hand beim Lesen der Rohtexte, unten in URSACHE; Vorrang bei mehreren Gründen:
        5 vor 3 vor 4 vor 2 vor 1). Eine einfache Zusatzregel („Datum/Dauer aus dem Freitext lesen“) wird als Schätzung probiert; die Liste
        wird NICHT geändert.
Teil 2  Alle Lose in data/processed/vertragsliste_909.csv mit gl_herkunft in {beginn_plus_dauer, text_laufzeit_option, text_zunaechst,
        text_festlaufzeit}: Rohtext lesen und prüfen, ob das Dauerfeld die Option schon enthält oder dem Text widerspricht.
        Hand- bzw. KI-Prüfung nur an diesen Rohtexten (Urteile unten in URTEIL_BPD, URTEIL_SONDER); beginn_plus_dauer, text_laufzeit_option und
        text_festlaufzeit wurden Satz für Satz gelesen, bei text_zunaechst (116 Bekanntmachungen) der Satz mit dem Datum des Listenwerts.

Aufruf:  .venv\\Scripts\\python.exe -I src/report/stufe_f_ursachen.py [Fragment-Ordner]
Ausgabe: reports/stufe_f_ursachen.csv (Teil 1, je Los), reports/stufe_f_fehlertyp.csv (Teil 2, je Bekanntmachung und Urteil);
         optional (mit Ordner-Argument) Markdown-Tabellen als Fragmente. Der Bericht reports/stufe_f_ursachen.md ist von Hand geschrieben.
Netz:    nur TED-XML https://ted.europa.eu/en/notice/<Nr>/xml, nur wenn die Datei in data/raw/ted_xml/stufe_f_20261105/ fehlt.
"""

import csv
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "src" / "prepare"))

from vertragsliste import _liste, ende_nach_monaten, je_los, normalisiere, plus_monate  # noqa: E402

BEISPIEL = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
LISTE = ROOT / "data" / "processed" / "vertragsliste_909.csv"
RAW = ROOT / "data" / "raw" / "ted_search" / "DEU_result_cpv909_20231025_20260930_lostext"
XML_DIR = ROOT / "data" / "raw" / "ted_xml" / "stufe_f_20261105"
OUT1 = ROOT / "reports" / "stufe_f_ursachen.csv"
OUT2 = ROOT / "reports" / "stufe_f_fehlertyp.csv"

KLASSEN = {
    "1a": "kein Dauer-/Beginn-/Endfeld und kein Satz zur Grundlaufzeit; nur eine Verlängerung wird genannt",
    "1b": "kein Dauer-/Beginn-/Endfeld und weder Laufzeit noch Verlängerung im Text",
    "2": "Dauer oder Datum nur im Freitext, von der Regel nicht gelesen",
    "3": "Rahmenvereinbarung/Abrufvertrag ohne feste Laufzeit",
    "4": "Dauer „unbestimmt“/„bis auf Weiteres“",
    "5": "keine Gebäudereinigung (Titel/CPV)",
    "6": "Zuordnung Los zu Feld nicht eindeutig",
    "7": "andere",
}

# ---- Teil 1: Zuordnung je Bekanntmachung (Ursache, wörtlicher Beleg aus den Rohdaten mit Feldname) ----------------------------------------
URSACHE: dict[str, tuple[str, str]] = {
    "788951-2023": ("1b", "description-lot: „Los 1 Unterhaltsreinigung: Jahresreinigungsfläche ca. 657.313.,25m² Sonderreinigungen Los 1 (z.B. Gästeapartments, …)“ – keine Laufzeitangabe"),
    "266771-2024": ("1a", "renewal-description-lot: „Verlängerung des Vertrages von 2 x 1 Jahr möglich“ – Grundlaufzeit fehlt"),
    "267158-2024": ("1a", "renewal-description-lot: „Verlängerung des Vertrages von 2 x 1 Jahr möglich“ – Grundlaufzeit fehlt"),
    "437343-2024": ("1b", "description-proc: „… Vergütet werden lediglich erbrachte Reinigungsstunden. … Insbes. bei Verzögerungen der Vergabe kann die Leistungszeit auf einen späteren Zeitraum verschoben … werden“ – keine Dauer; XML: framework-agreement = none"),
    "555698-2024": ("1b", "description-lot: „… 4.410,00 zu erbringende Mindestjahresreinigungsstunden für die Unterhaltsreinigung pro Jahr.“ – keine Dauer; XML: framework-agreement = none"),
    "446124-2025": ("1a", "renewal-description-lot: „Verlängerungsoption 1 Jahr“ (renewal-maximum-lot: 1) – Grundlaufzeit fehlt"),
    "685373-2025": ("1b", "description-lot: „Folgende Reinigungs- bzw. Raumgruppen sind für die Leistungserbringung vorgesehen: …“ – keine Laufzeitangabe"),
    "420148-2026": ("1b", "description-lot: „Für 22 verschiedene Objekte der Stadt Regensburg wird die Glasreinigung ausgeschrieben.“ – keine Laufzeitangabe"),
    "420740-2026": ("1a", "renewal-description-lot: „Der Vertrag kann dreimal jeweils um ein weiteres Jahr verlängert werden.“ – Grundlaufzeit fehlt"),
    "480569-2026": ("1a", "renewal-description-lot: „Wird der Vertrag nicht fristgemäß gekündigt, verlängert er sich jeweils um ein weiteres Jahr (siehe Punkt 1.28 der Vorbemerkungen/Vorgaben).“ – Grundlaufzeit nur in den Vergabeunterlagen"),
    "33610-2024": ("2", "renewal-description-lot: „Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von 6 Monaten vor Vertragsende (31.03. des jeweiligen Jahres) gekündigt wird und endet spätestens mit Ablauf des 31.03.2030.“"),
    "683177-2024": ("2", "option-description-lot: „Als vertragliche Fristen gelten: Beginn der Leistung: 01.01.2025 Der Vertrag wird auf die Dauer von 1 Jahr geschlossen Er verlängert sich um jeweils ein Jahr, wenn er nicht spätestens 3 Monate vor Ablauf schriftlich gekündigt wird. Der Vertrag endet spätestens am 31.12.2028“"),
    "226358-2025": ("2", "description-lot: „Der Vertrag wird auf 5 Jahre befristet und beinhaltet eine Probezeit von 6 Monaten.“ (kein Beginn)"),
    "503542-2025": ("2", "renewal-description-lot: „… verlängert sich die Laufzeit um zwölf Monate. Eine solche stillschweigende Verlängerung um jeweils zwölf Monate ist höchstens zweimal möglich. Der Vertrag endet spätestens mit Ablauf des 31.08.2029.“ (renewal-maximum-lot: 2)"),
    "722107-2025": ("2", "renewal-description-lot: „Der Vertrag beginnt am 01.01.2026 und endet am 31.12.2028.“"),
    "722423-2025": ("2", "renewal-description-lot: „Der Vertrag beginnt am 01.01.2026 und endet am 31.12.2029.“"),
    "215440-2026": ("2", "renewal-description-lot: „Der Vertrag beginnt am 01.10.2026 und endet am 30.09.2030.“"),
    "454420-2026": ("2", "renewal-description-lot: „Der Vertag hat eine Laufzeit von 4 Jahren und gilt vom 01.01.2027 bis 31.12.2030 mit der Option auf zweimalige Verlängerungen um jeweils ein Jahr.“"),
    "579178-2026": ("2", "description-lot: „… ab. dem 01.08.2026 neu. Der Vertrag wird auf 4 Jahre befristet, kann jedoch zweimalig um jeweils ein Jahr ver-längert werden.“; renewal-description-lot: „Der Vertrag verlängert sich bis zum 31.07.2031, …“"),
    "580747-2026": ("2", "description-lot: „… ab. dem 01.08.2026 neu. Der Vertrag wird auf 3 Jahre befristet, kann jedoch zweimalig um jeweils ein Jahr ver-längert werden“; renewal-description-lot: „Der Vertrag verlängert sich bis zum 31.07.2030, …“"),
    "556275-2026": ("5", "title-lot: „Kesselreinigungsarbeiten an der Ofenlinie 1 und 4 inkl. Strahlentrostungsarbeiten“; main-classification-lot: 90910000; description-lot: „Rahmenvereinbarung zur Durchführung von Kesselreinigungsarbeiten …“ (Text nennt zusätzlich: „… Vertragsende (31.12.2027) … endet spätestens mit Ablauf des 31.12.2029“)"),
}

# Hand-Schätzung, welches Ende ein Zusatzregel-Leser aus dem Text ableiten könnte: (Art, Datum Ende GL, Höchstende)
#   A exakt (Enddatum steht im Text) · B Beginn + Dauer · C Rückrechnung (Höchstende minus Verlängerungen) · E nur geschätzt (Veröffentlichung + Dauer)
#   H nur Höchstende lesbar · – nichts
HAND_ENDE: dict[str, tuple[str, str, str]] = {
    "722107-2025": ("A", "2028-12-31", "2030-12-31"),
    "722423-2025": ("A", "2029-12-31", "2031-12-31"),
    "215440-2026": ("A", "2030-09-30", "2032-09-30"),
    "454420-2026": ("A", "2030-12-31", "2032-12-31"),
    "579178-2026": ("B", "2030-07-31", "2032-07-31"),
    "580747-2026": ("B", "2029-07-31", "2031-07-31"),
    "683177-2024": ("B", "2025-12-31", "2028-12-31"),
    "503542-2025": ("C", "2027-08-31", "2029-08-31"),
    "226358-2025": ("E", "", ""),
    "33610-2024": ("H", "", "2030-03-31"),
}

D = r"(\d{1,2})\.\s?(\d{1,2})\.\s?(20\d{2})"
RE_A = re.compile(rf"(?i)beginnt\s+am\s+{D}\s+und\s+endet\s+am\s+{D}")
RE_A2 = re.compile(rf"(?i)(?:gilt\s+)?vom\s+{D}\s+bis\s+(?:zum\s+)?{D}")
RE_B = re.compile(rf"(?i)beginn\s+der\s+leistung:?\s*{D}.{{0,80}}?dauer\s+von\s+(\d+)\s+jahr")
RE_C = re.compile(rf"(?i)ab\.?\s*dem\s+{D}.{{0,60}}?auf\s+(\d+)\s+jahre?\s+befristet")
RE_D = re.compile(r"(?i)auf\s+(\d+)\s+jahre?\s+befristet")
RE_H = re.compile(rf"(?i)endet\s+(?:jedoch\s+)?spätestens\s+(?:mit\s+ablauf\s+des\s+|am\s+|zum\s+)?{D}")
RE_VLAENGE = re.compile(r"(?i)um\s+(?:jeweils\s+)?(zwölf|12)\s+monate")


def dat(t: str, m: str, j: str) -> date | None:
    try:
        return date(int(j), int(m), int(t))
    except ValueError:
        return None


def zusatzregel(text: str, bt58: int | None, pub: date | None) -> tuple[str, date | None, date | None]:
    """Einfache Zusatzregel (Schätzung, nicht Teil der Liste). Rückgabe: (Art, Ende GL, Höchstende)."""
    t = normalisiere(text)
    gl = hoechst = None
    if m := RE_A.search(t):
        gl = dat(*m.groups()[3:6])
        art = "A"
    elif m := RE_A2.search(t):
        gl = dat(*m.groups()[3:6])
        art = "A"
    elif m := RE_B.search(t):
        b = dat(*m.groups()[:3])
        gl, art = (ende_nach_monaten(b, 12 * int(m.group(4))), "B") if b else (None, "–")
    elif m := RE_C.search(t):
        b = dat(*m.groups()[:3])
        gl, art = (ende_nach_monaten(b, 12 * int(m.group(4))), "B") if b else (None, "–")
    else:
        art = "–"
    if m := RE_H.search(t):
        hoechst = dat(*m.groups())
        if art == "–" and bt58 and RE_VLAENGE.search(t) and hoechst:
            gl, art = plus_monate(hoechst, -12 * bt58), "C"
    if art == "–" and (m := RE_D.search(t)) and pub:
        gl, art = ende_nach_monaten(pub, 12 * int(m.group(1))), "E"
    if art == "–" and hoechst:
        art = "H"
    return art, gl, hoechst


def fl(v):
    if isinstance(v, dict):
        v = v.get("deu") or next(iter(v.values()), None)
    return v


def lade_roh(nummern: set[str]) -> dict[str, dict]:
    out = {}
    for f in sorted(RAW.glob("page_*.json")):
        for n in json.loads(f.read_text(encoding="utf-8")).get("notices", []):
            if n["publication-number"] in nummern:
                out[n["publication-number"]] = n
    return out


def lade_xml(pub: str) -> ET.Element:
    XML_DIR.mkdir(parents=True, exist_ok=True)
    p = XML_DIR / f"{pub}.xml"
    if not p.exists():
        r = requests.get(f"https://ted.europa.eu/en/notice/{pub}/xml", timeout=60)
        r.raise_for_status()
        p.write_bytes(r.content)
        time.sleep(1.2)
    return ET.parse(p).getroot()


def xml_laufzeit_elemente(root: ET.Element) -> list[str]:
    names = {"PlannedPeriod", "DurationMeasure", "StartDate", "EndDate", "DurationPeriod"}
    return sorted({el.tag.rsplit("}", 1)[-1] for el in root.iter() if el.tag.rsplit("}", 1)[-1] in names})


def lot_text(n: dict, i: int, nl: int) -> str:
    teile = []
    for f in ("renewal-description-lot", "option-description-lot", "description-lot"):
        werte, _ = je_los(n, f, nl)
        teile.append(str(werte[i] or ""))
    return " ".join(teile)


def teil1() -> list[dict]:
    rows = [r for r in csv.DictReader(BEISPIEL.open(encoding="utf-8-sig"), delimiter=";") if r["stufe"] == "F"]
    assert len(rows) == 33, len(rows)
    nummern = {r["notice"] for r in rows}
    assert nummern == set(URSACHE), nummern ^ set(URSACHE)
    roh = lade_roh(nummern)
    assert set(roh) == nummern
    out = []
    for r in rows:
        k = r["notice"]
        n = roh[k]
        nl = len(_liste(n.get("title-lot"))) or 1
        i = int(r["los"]) - 1
        xml = xml_laufzeit_elemente(lade_xml(k))
        felder = {f: fl(n.get(f)) for f in ("contract-duration-start-date-lot", "contract-duration-end-date-lot", "contract-duration-period-lot",
                                             "contract-duration-period-oth-lot")}
        assert not any(felder.values()), (k, felder)
        assert not xml, (k, xml)  # kein PlannedPeriod/Duration/StartDate/EndDate im XML
        bt58 = _liste(n.get("renewal-maximum-lot"))
        bt58 = int(bt58[i]) if len(bt58) > i and str(bt58[i]).isdigit() else (int(bt58[0]) if bt58 and str(bt58[0]).isdigit() else None)
        pub = date.fromisoformat(str(n["publication-date"])[:10])
        art, gl, h = zusatzregel(lot_text(n, i, nl), bt58, pub)
        klasse, beleg = URSACHE[k]
        out.append({
            "notice": k, "los": r["los"], "auftraggeber": r["auftraggeber"], "los_titel": r["los_titel"],
            "main_cpv": (_liste(n.get("main-classification-lot")) or [""])[min(i, max(len(_liste(n.get("main-classification-lot"))) - 1, 0))],
            "ursache": klasse, "ursache_text": KLASSEN[klasse], "beleg_wörtlich": beleg,
            "felder_leer": "ja", "xml_laufzeitelement": "keines",
            "zusatzregel_art": art, "zusatzregel_gl_ende": gl.isoformat() if gl else "", "zusatzregel_hoechstende": h.isoformat() if h else "",
        })
        hand = HAND_ENDE.get(k, ("–", "", ""))
        if k != "556275-2026":
            assert (art, gl.isoformat() if gl else "") == (hand[0], hand[1]) or (hand[0] == "E" and art == "E"), (k, art, gl, hand)
    return out


# ---- Teil 2 ---------------------------------------------------------------------------------------------------------------------------------
# beginn_plus_dauer: Urteil je Bekanntmachung (von Hand beim Lesen der Rohtexte). (Urteil, Text-Befund, richtiger GL laut Text, wörtlicher Beleg)
URTEIL_BPD: dict[str, tuple[str, str, str, str]] = {
    "108946-2025": ("kein Fehler", "bestätigt", "", "option-description-lot: „Der Vertrag endet spätestens am 31.05.2031“ = Dauer 2 Jahre (Feld) + 4 Verlängerungen (renewal-maximum-lot: 4)"),
    "109604-2026": ("kein Fehler", "kein Widerspruch", "", "option-description-lot: „dreimalige Verlängerung um jeweils ein Jahr“; Dauerfeld 2 Jahre"),
    "119677-2025": ("Fehler", "Dauerfeld = Gesamtdauer", "2026-12-31", "option-description-lot: „1. Januar 2025 bis 31. Dezember 2026 mit Verlängerungsoption (bei unterlassener Kündigung) bis maximal 31. Dezember 2029“; Dauerfeld 5 Jahre"),
    "122700-2025": ("Fehler", "Dauerfeld = Gesamtdauer", "Los 4-7: 2026-12-31; Los 1-3: 2027-08-31", "option-description-lot: „1. Januar 2025 bis 31.Dezember 2026 mit Verlängerungsoption (bei unterlassener Kündigung) bis maximal 31. Dezember 2029“ und „… optionale Verschiebung … auf 1. September 2025 bis 31. August 2027 …, jeweils mit Verlängerungsoption … bis maximal 31. Dezember 2029“; Dauerfeld 5 Jahre bzw. 52 Monate. Zwei Textblöcke für sieben Lose, Zuordnung über den Beginn"),
    "159782-2025": ("kein Fehler", "bestätigt", "", "description-lot: „Die Vertragslaufzeit beträgt 48 Monate.“ (keine Option im Text)"),
    "199184-2026": ("kein Fehler", "bestätigt", "", "option-description-lot: „Der Vertrag kann zwei Mal um jeweils 12 Monate, bis max. zum 30.03.2030, verlängert werden“; Dauerfeld 24 Monate ab 31.03.2026"),
    "325419-2024": ("kein Fehler", "kein Widerspruch", "", "option-description-lot: „Options to extend the term by 24 months * 2“; Dauerfeld 48 Monate (Rahmenvereinbarung Soft Services, keine reine Gebäudereinigung)"),
    "409547-2026": ("kein Fehler", "kein Widerspruch", "", "option-description-lot: „dreimalige Verlängerung um jeweils ein Jahr“; Dauerfeld 2 Jahre"),
    "495440-2026": ("Fehler", "Dauerfeld = Gesamtdauer", "2027-07-31", "renewal-description-lot: „Der Vertrag wird für einen Anfangszeitraum von 12 (zwölf) Monate, verlängerbar 3 (drei) geschlossen.“; Dauerfeld 48 Monate = 12 + 3 × 12 (Länge der Verlängerung im Text nicht genannt)"),
    "495951-2025": ("unklar", "Widerspruch (unbefristet)", "", "option-description-lot: „Der Vertrag beginnt am 01.11.2025 und läuft auf unbestimmte Zeit. Aus vergaberechtlichen Gründen ist der Auftraggeber grundsätzlich gehalten, die Vertragsleistung nach 6 Jahren neu zu vergeben.“; Dauerfeld 72 Monate. Anderer Fehlertyp: keine Option, aber ebenfalls keine feste Grundlaufzeit"),
    "496173-2025": ("unklar", "Widerspruch (unbefristet)", "", "option-description-lot: „Der Vertrag beginnt am 01.11.2025 und läuft auf unbestimmte Zeit. Aus vergaberechtlichen Gründen ist der Auftraggeber grundsätzlich gehalten, die Vertragsleistung nach 6 Jahren neu zu vergeben.“; Dauerfeld 72 Monate"),
    "510553-2026": ("kein Fehler", "bestätigt", "", "description-lot: „Jahresvertrag mit der Option der Verlängerung“; option-description-lot: „Option der Verlängerung, den Vetrag jeweils dreimal um ein weiteres Jahr zu verlängern.“; Dauerfeld 1 Jahr"),
    "527230-2026": ("Fehler", "Dauerfeld = Gesamtdauer", "2027-01-31", "description-proc: „Interimsvergabe aufgrund Dringlichkeit 01.10.26 - 31.01.27 mit 6 Monaten Option“; option-description-lot: „6 Monate Verlängerung falls Rechtsverfahren länger dauert“; Dauerfeld 10 Monate = 4 + 6 (bekannter Fall, Nachtrag in docs/iterationen.md)"),
    "529782-2025": ("kein Fehler", "bestätigt", "", "description-lot: „Jahresvertrag Unterhalts- und Grundreinigung ca. 6.200 m²“; option-description-lot: „Der Vertrag verlängert sich jeweils um ein weiteres Jahr, …“; Dauerfeld 1 Jahr"),
    "533946-2026": ("Fehler", "Dauerfeld = Gesamtdauer", "2028-09-30", "option-description-lot: „2 Jahre Festlaufzeit + 3x1 Jahr Option“; description-lot: „… für 2 Jahre + 3 Jahre Option“; Dauerfeld 5 Jahre"),
    "600919-2025": ("kein Fehler", "bestätigt", "", "renewal-description-lot: „Der Vertrag hat ab Leistungsbeginn eine Laufzeit von zwei (2) Jahren. Der AG hat dann zwei Mal die Möglichkeit den Vertrag … um ein weiteres Jahr zu verlängern. Die Verträge in beiden Losen enden aber spätestens am 30.09.2029“"),
    "620628-2025": ("kein Fehler", "bestätigt", "", "renewal-description-lot: „Der Vertrag verlängert sich automatisch jeweils um bis zu 15 Monaten, … Der Vertrag endet jedoch spätestens mit Ablauf des 31. Dezember 2028.“; Dauerfeld 24 Monate ab 01.10.2025 (+ 15 Monate = 31.12.2028)"),
    "697344-2025": ("kein Fehler", "bestätigt", "", "description-lot: „… für den Zeitraum vom 1.1.2026 bis 31.12.2027 mit zweimaliger Verlängerungsoption für den Auftraggeber um jeweils ein Kalenderjahr.“"),
    "707425-2025": ("kein Fehler", "bestätigt (rechnerisch)", "", "renewal-description-lot: „Der Vertrag verlängert sich automatisch jeweils um ein weiteres Jahr, … Der Vertrag endet jedoch spätestens mit Ablauf des 31. Oktober 2030.“; Dauerfeld 36 Monate ab 01.11.2025 (+ 2 Jahre = 31.10.2030); renewal-maximum-lot nennt 1, das passt nicht dazu"),
    "712919-2025": ("kein Fehler", "bestätigt (rechnerisch)", "", "renewal-description-lot: „Der Vertrag verlängert sich automatisch jeweils um ein weiteres Jahr, … Der Vertrag endet jedoch spätestens mit Ablauf des 31. Dezember 2029.“; Dauerfeld 15 Monate ab 01.10.2025 (+ 3 Jahre = 31.12.2029)"),
    "755291-2023": ("kein Fehler", "kein Text", "", "Kein Satz zur Laufzeit in description-lot/-proc; renewal-maximum-lot: 5, ohne Beschreibung; Dauerfeld 3 Jahre – nicht prüfbar"),
    "779220-2024": ("kein Fehler", "kein Text", "", "Kein Satz zur Laufzeit in description-lot/-proc; Dauerfeld 4 Jahre – nicht prüfbar"),
    "91389-2026": ("kein Fehler", "bestätigt", "", "option-description-lot: „Verlängerung - Maximale Anzahl: 3 … verlängert sich automatisch jeweils um ein weiteres Jahr, … Der Vertrag endet jedoch spätestens mit Ablauf des 31. März 2031.“; Dauerfeld 24 Monate ab 01.04.2026"),
    "9955-2026": ("kein Fehler", "kein Widerspruch", "", "option-description-lot: „dreimalige Verlängerung um jeweils ein Jahr“; Dauerfeld 2 Jahre"),
}

# Abweichungen bei den Textherkünften: (Bekanntmachung, Los oder None für alle) -> (Urteil, Befund, Beleg)
URTEIL_SONDER: dict[tuple[str, str | None], tuple[str, str, str]] = {
    ("612313-2026", None): ("unklar", "Textdatum widerspricht Feldbeginn",
                           "description-lot: „… für die Vertragsdauer von 3 Jahren (01.09.2025 bis 31.08.2028) zzgl. optionaler zweimaliger Verlängerung um jeweils weitere 12 Monate.“, aber contract-duration-start-date-lot: 2026-09-01 und -end-date-lot: 2031-08-31 (3 + 2 Jahre); Liste: 31.08.2029 = Feldbeginn + 3 Jahre. Das Jahr im Text ist wahrscheinlich ein Übernahmefehler; die Option ist nicht in der Dauer enthalten."),
    ("267775-2025", None): ("kein Fehler", "bestätigt (von Hand gelesen)", "option-description-lot: „Die Laufzeit des Vertrages beträgt ein Jahr zum Schuljahresende mit Verlängerungsoption. Die maximale Vertragslaufzeit beträgt vier Jahre. Vertragsbeginn ist der 30.06.2025, spätestes Vertragsende ist der 20.07.2029“ (Hinweis: Feld-Enddatum 22.07.2029, nur das Höchstende weicht um 2 Tage ab)"),
    ("340183-2026", None): ("kein Fehler", "bestätigt (von Hand gelesen)", "option-description-lot: „Die Laufzeit des Vertrages beträgt ein Jahr zum Schuljahresende mit Verlängerungsoption. Die maximale Vertragslaufzeit beträgt vier Jahre.“"),
    ("360180-2025", None): ("kein Fehler", "bestätigt (von Hand gelesen)", "option-description-lot: „Die Laufzeit des Vertrages beträgt ein Jahr mit Verlängerungsoption. Die maximale Vertragslaufzeit beträgt vier Jahre . Fristbeginn ist der 30.06.2025; spätestes Vertragsende der 22.07.2029“"),
    ("392720-2026", None): ("kein Fehler", "bestätigt (von Hand gelesen)", "option-description-lot: „Die Vertragsdauer beträgt zwei Jahre mit einer zusätzlichen Option einer Verlängerung von zweimal ein Jahr. (2+1+1)“"),
    ("412612-2025", None): ("kein Fehler", "bestätigt (von Hand gelesen)", "option-description-lot: „Optionale Vertragsverlängerung von zwei Jahren auf maximal vier Jahre.“ (GL = Beginn + 2 Jahre)"),
    ("758702-2025", "2"): ("unklar", "Beginn des Loses weicht vom Text ab",
                           "option-description-lot (für alle Lose gleich): „Die Laufzeit des Vertrages beträgt zwei Jahre, beginnend am 01.10.2025 und endet am 30.09.2027. Es besteht eine Option den Vertrag um zwei weitere Jahre zu verlängern.“; contract-duration-start-date-lot dieses Loses (Kurhaus Wiesbaden): 2025-12-01; Liste: Ende GL 30.09.2027, Höchstende 30.11.2029 (passen nicht zusammen)"),
}


def beleg_aus_text(text: str, x: dict) -> tuple[str, str]:
    """Textherkünfte: Satz mit dem Datum des Listenwerts (zunächst/Festlaufzeit) bzw. mit der festen Dauer (laufzeit_option)."""
    t = normalisiere(text)
    sätze = re.split(r"(?<=[.!?;])\s+|\n", t)
    y, m, d = x["gl_ende"].split("-")
    for s in sätze:
        if f"{int(d)}.{int(m)}.{y}" in s or f"{d}.{m}.{y}" in s:
            return "Datum des Listenwerts im Satz", s.strip()[:300]
    for s in sätze:
        if re.search(r"(?i)(laufzeit|vertragsdauer|auftragszeitraum|befristet|jahre?\b|monate)", s) and re.search(r"\d", s):
            return "feste Dauer im Satz", s.strip()[:300]
    return "kein Satz gefunden", ""


def teil2() -> list[dict]:
    rows = [r for r in csv.DictReader(LISTE.open(encoding="utf-8-sig"), delimiter=";")
            if r["gl_herkunft"] in ("beginn_plus_dauer", "text_laufzeit_option", "text_zunaechst", "text_festlaufzeit")]
    by = defaultdict(list)
    for r in rows:
        by[r["notice"]].append(r)
    roh = lade_roh(set(by))
    assert set(roh) == set(by)
    out = []
    for k, xs in sorted(by.items()):
        herkunft = xs[0]["gl_herkunft"]
        n = roh[k]
        nl = len(_liste(n.get("title-lot"))) or 1
        gruppen = defaultdict(list)
        for x in xs:
            if herkunft == "beginn_plus_dauer":
                u = URTEIL_BPD[k]
                key = (u[0], u[1], u[3], u[2])
            elif (k, x["los"]) in URTEIL_SONDER or (k, None) in URTEIL_SONDER:
                u = URTEIL_SONDER.get((k, x["los"])) or URTEIL_SONDER[(k, None)]
                key = (u[0], u[1], u[2], "")
            else:
                art, satz = beleg_aus_text(lot_text(n, int(x["los"]) - 1, nl), x)
                key = ("kein Fehler", "bestätigt (" + art + ")", satz, "")
            gruppen[key].append(x)
        for (urteil, befund, beleg, richtig), lose in gruppen.items():
            out.append({
                "notice": k, "herkunft": herkunft, "auftraggeber": xs[0]["auftraggeber"][:60], "lose_in_liste": len(xs),
                "los_nummern": ",".join(x["los"] for x in lose), "n_lose_urteil": len(lose),
                "listenwert_gl": ";".join(sorted({x["gl_ende"] for x in lose})), "listenwert_hoechstende": ";".join(sorted({x["hoechstende"] or "unbestimmbar" for x in lose})),
                "gl_laut_text": richtig, "urteil": urteil, "textbefund": befund, "beleg_wörtlich": beleg,
            })
    return out


def schreibe_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=";")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    frag = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    t1 = teil1()
    schreibe_csv(OUT1, t1)
    zaehl = Counter(r["ursache"] for r in t1)
    print("Teil 1: Lose", len(t1), "Bekanntmachungen", len({r['notice'] for r in t1}))
    for k in KLASSEN:
        print(f"  Ursache {k}: {zaehl.get(k, 0)} Lose; Bek.: {sorted({r['notice'] for r in t1 if r['ursache'] == k})}")
    zr = Counter(r["zusatzregel_art"] for r in t1 if r["ursache"] != "5")
    print("  Zusatzregel (ohne Ursache 5):", dict(zr))
    t2 = teil2()
    schreibe_csv(OUT2, t2)
    lose = sum(r["n_lose_urteil"] for r in t2)
    bek = len({r["notice"] for r in t2})
    print("Teil 2: Lose", lose, "Bekanntmachungen", bek)
    for h in ("beginn_plus_dauer", "text_laufzeit_option", "text_festlaufzeit", "text_zunaechst"):
        sub = [r for r in t2 if r["herkunft"] == h]
        print(f"  {h}: Bek. {len({r['notice'] for r in sub})}, Lose {sum(r['n_lose_urteil'] for r in sub)}; "
              + ", ".join(f"{u}: {sum(r['n_lose_urteil'] for r in sub if r['urteil'] == u)} Lose/{len({r['notice'] for r in sub if r['urteil'] == u})} Bek."
                          for u in ("Fehler", "unklar", "kein Fehler")))
    if frag:
        frag.mkdir(parents=True, exist_ok=True)
        (frag / "t1.json").write_text(json.dumps(t1, ensure_ascii=False, indent=1), encoding="utf-8")
        (frag / "t2.json").write_text(json.dumps(t2, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
