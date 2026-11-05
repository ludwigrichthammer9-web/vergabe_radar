"""Iteration 9, Schritt 3: Rohtext je Bekanntmachung, Aufgaben-Pakete für die KI-Leser und Blatt für die menschliche Kontrolle.

Eingaben: `reports/stichprobe_iteration9_lose.csv` (ohne Listenwerte), TED-XML unverändert in `data/raw/ted_xml/iteration9_20261105/`.
Ausgaben:
- `reports/zweitlesung_iteration9/rohtext/<Nr>.txt`: je Bekanntmachung der Text des Verfahrens und der Lose (Felder und Texte unverändert, mit Feldnamen);
  bei Bekanntmachungen mit mehr als 8 Losen nur die Lose der Stichprobe vollständig, die übrigen mit Kennung, Titel und Datumsfeldern.
- `reports/zweitlesung_iteration9/pakete/teil_<k>/`: Aufgabe (`aufgabe.md`) und die zugehörigen Rohtexte; ein Paket je Sitzung der Leser (Leser A und B bekommen dieselben Pakete).
- `reports/zweitlesung_iteration9/blatt_mensch.md`: 15 Lose für den Kommilitonen (TED-Link, Titel, leere Felder), ohne Listenwerte.
- `reports/zweitlesung_iteration9/pruefung_rohtext.md`: Prüfung des Skripts gegen die API-Daten (Titel, Beginn, Enddatum je Los).
Die Anweisung nennt weder Projekt noch Regeln noch Fehlerarten.

Aufruf:  .venv\\Scripts\\python -I src/prepare/rohtext_iteration9.py
"""

import csv
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analyze_completeness import PROJECT_ROOT  # noqa: E402

XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml" / "iteration9_20261105"
OUT = PROJECT_ROOT / "reports" / "zweitlesung_iteration9"
LOSE = PROJECT_ROOT / "reports" / "stichprobe_iteration9_lose.csv"
SCHLUESSEL = PROJECT_ROOT / "data" / "processed" / "stichprobe_iteration9_schluessel.csv"
LISTE = PROJECT_ROOT / "data" / "processed" / "vertragsliste_909.csv"
N_TEILE = 5
MAX_LOSE_VOLL = 8
TED_LINK = "https://ted.europa.eu/de/notice/-/detail/{}"

AUFGABE = """# Aufgabe: Laufzeiten aus Bekanntmachungen ablesen

Du liest Auszüge aus EU-Bekanntmachungen über vergebene Aufträge (Reinigungsleistungen) und trägst je Los **Fakten** zur Vertragslaufzeit ein.
In diesem Ordner liegen die Auszüge (`rohtext_<Nummer>.txt`, eine Datei je Bekanntmachung) und diese Aufgabe. Öffne **keine** anderen Dateien, nutze kein Internet und
starte keine weiteren Agenten. Es gibt keine „richtigen“ Werte, die du erraten sollst: Lies sorgfältig und trage nur ein, was im Text oder in den Feldern steht.

## Vorgehen je Los
Die Tabelle unten nennt je Zeile eine Nummer (N…), die Bekanntmachung, die Nummer des Loses und den Titel. Suche das Los in der Datei der Bekanntmachung (über Titel und Nummer;
Kennungen wie LOT-0001 zählen oft ab 1, manchmal ab 0) und lies **alle** Angaben dieses Loses und die allgemeine Beschreibung des Verfahrens. Trage dann die Spalten ein.

## Spalten (Tab als Trenner, eine Zeile je Los, Reihenfolge wie in der Tabelle)
`N`, `zuordnung_sicher`, `beginn`, `feld_enddatum`, `feste_dauer_monate`, `feste_ende`, `verl_status`, `verl_anzahl`, `verl_monate`, `spaetestes_ende`, `gesamtdauer_monate`,
`nicht_tagesgenau`, `kein_zuschlag`, `gebaeudereinigung`, `widerspruch`, `zitat`

- **zuordnung_sicher:** `ja` oder `nein` (nein, wenn Titel und Nummer nicht eindeutig zu einem Los passen).
- **beginn:** Beginn der Laufzeit des Loses als TT.MM.JJJJ (Feld StartDate oder Text); leer, wenn keine Angabe.
- **feld_enddatum:** Wert des Felds EndDate des Loses als TT.MM.JJJJ; leer, wenn das Feld fehlt.
- **feste_dauer_monate:** Wenn Text oder Feld ausdrücklich eine Dauer der **ersten festen Laufzeit ohne Verlängerungsoptionen** nennen: Anzahl Monate (3 Jahre = 36). Sonst leer.
- **feste_ende:** Wenn Text oder Feld ausdrücklich ein **Ende der ersten festen Laufzeit** nennen: TT.MM.JJJJ. Sonst leer.
- **verl_status:** `keine` (Verlängerung ausgeschlossen oder ausdrücklich nicht vorgesehen), `nichts_genannt` (kein Wort zu Verlängerung oder Option für dieses Los) oder `genannt`.
- **verl_anzahl:** Höchstzahl der Verlängerungen als Zahl, wenn genannt; sonst leer. **verl_monate:** Länge je Verlängerung in Monaten, wenn genannt; sonst leer.
- **spaetestes_ende:** Wenn Text oder Feld ausdrücklich ein **spätestes Ende des Vertrags einschließlich aller Verlängerungen** nennen (z. B. „endet spätestens am“, „längstens bis“): TT.MM.JJJJ. Sonst leer.
- **gesamtdauer_monate:** Wenn ausdrücklich eine **maximale Gesamtlaufzeit** genannt ist (z. B. „maximale Vertragslaufzeit vier Jahre“): Anzahl Monate. Sonst leer.
- **nicht_tagesgenau:** `ja`, wenn die erste feste Laufzeit nur über ein Ereignis ohne Datum beschrieben ist (z. B. „bis zum Schuljahresende“) und du daraus kein Datum ablesen kannst. Sonst `nein`.
- **kein_zuschlag:** `ja`, wenn die Bekanntmachung für **dieses Los** keinen Zuschlag nennt (z. B. „kein Gewinner gewählt“, „keine Angebote“). Sonst `nein`.
- **gebaeudereinigung:** `ja`, wenn das Los im Kern Gebäudereinigung ist (auch Glas- und Unterhaltsreinigung); `nein` bei anderen Leistungen (z. B. Schädlingsbekämpfung, Kanalreinigung, Mietkleidung).
- **widerspruch:** Ein kurzer Satz, wenn sich Angaben widersprechen (z. B. Feld und Text), sonst leer.
- **zitat:** Die tragenden Stellen **wörtlich** mit Feldname (höchstens etwa 400 Zeichen, ohne Tabs und Zeilenumbrüche).

Rechne **nichts** aus und schätze nichts: Trage nur ein, was ausdrücklich dasteht. Datumsangaben immer als TT.MM.JJJJ.

## Ergebnis
Schreibe die Tabelle (mit Kopfzeile) in die Datei `ergebnis.tsv` in diesem Ordner und gib sie am Ende zusätzlich im Chat aus. Danach nichts weiter erklären.

## Lose
"""


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def kinder(e: ET.Element, name: str) -> list[ET.Element]:
    return [c for c in e if local(c.tag) == name]


def erstes(e: ET.Element | None, *pfad: str) -> ET.Element | None:
    for n in pfad:
        if e is None:
            return None
        k = kinder(e, n)
        e = k[0] if k else None
    return e


def txt(e: ET.Element | None) -> str:
    return " ".join("".join(e.itertext()).split()) if e is not None else ""


def datum(s: str) -> str:
    return s[:10]


def projekt_zeilen(pp: ET.Element | None) -> list[str]:
    """Felder und Texte eines ProcurementProject (Verfahren oder Los) unverändert, mit Feldnamen."""
    if pp is None:
        return []
    out = []
    for name, label in (("Name", "Titel (Name)"), ("Description", "Beschreibung (Description)"), ("Note", "Hinweis (Note)")):
        for e in kinder(pp, name):
            out.append(f"{label}: {txt(e)}")
    pl = erstes(pp, "PlannedPeriod")
    if pl is not None:
        for name, label in (("StartDate", "Beginn (StartDate)"), ("EndDate", "Enddatum (EndDate)")):
            for e in kinder(pl, name):
                out.append(f"{label}: {datum(txt(e))}")
        for e in kinder(pl, "DurationMeasure"):
            out.append(f"Dauer (DurationMeasure): {txt(e)} {e.attrib.get('unitCode', '')}")
        for e in kinder(pl, "Description"):
            out.append(f"Beschreibung der Laufzeit (PlannedPeriod/Description): {txt(e)}")
    ce = erstes(pp, "ContractExtension")
    if ce is not None:
        for e in kinder(ce, "MaximumNumberNumeric"):
            out.append(f"Höchstzahl der Verlängerungen (MaximumNumberNumeric): {txt(e)}")
        for e in kinder(ce, "OptionsDescription"):
            out.append(f"Beschreibung der Optionen (OptionsDescription): {txt(e)}")
        for r in kinder(ce, "Renewal"):
            for per in kinder(r, "Period"):
                for e in kinder(per, "Description"):
                    out.append(f"Beschreibung der Verlängerung (Renewal): {txt(e)}")
                for e in kinder(per, "DurationMeasure"):
                    out.append(f"Dauer der Verlängerung (Renewal/DurationMeasure): {txt(e)} {e.attrib.get('unitCode', '')}")
    return out


def lose_und_ergebnisse(root: ET.Element) -> tuple[ET.Element | None, list[ET.Element], dict[str, str]]:
    verfahren = None
    lose = []
    for e in root:
        n = local(e.tag)
        if n == "ProcurementProject":
            verfahren = e
        elif n == "ProcurementProjectLot":
            lose.append(e)
    status = {}
    for lr in root.iter():
        if local(lr.tag) == "LotResult":
            kennung = txt(erstes(lr, "TenderLot", "ID"))
            code = txt(erstes(lr, "TenderResultCode"))
            n = [txt(s.find("*[2]")) for s in kinder(lr, "ReceivedSubmissionsStatistics")]
            status[kennung] = f"Ergebnis des Loses (TenderResultCode): {code}" + (f"; Angebote (ReceivedSubmissionsStatistics): {', '.join(n)}" if n else "")
    return verfahren, lose, status


def rohtext(pub: str, stich_lose: set[int]) -> tuple[str, list[dict]]:
    root = ET.fromstring((XML_DIR / f"{pub}.xml").read_bytes())
    verfahren, lose, status = lose_und_ergebnisse(root)
    out = [f"Bekanntmachung {pub} (Auszug aus der TED-XML-Datei, Texte und Felder unverändert)", "", "## Verfahren (gilt für alle Lose)", *projekt_zeilen(verfahren), ""]
    info = []
    for i, lot in enumerate(lose, 1):
        kennung = txt(erstes(lot, "ID"))
        pp = erstes(lot, "ProcurementProject")
        titel = txt(erstes(pp, "Name"))
        zeilen = projekt_zeilen(pp)
        info.append({"los": i, "kennung": kennung, "titel": titel, "beginn": datum(txt(erstes(pp, "PlannedPeriod", "StartDate"))),
                     "ende": datum(txt(erstes(pp, "PlannedPeriod", "EndDate")))})
        voll = len(lose) <= MAX_LOSE_VOLL or i in stich_lose
        out += [f"## Los {i} der Liste: {kennung}" + ("" if voll else " (gekürzt: nur Titel und Datumsfelder)")]
        if voll:
            out += zeilen
        else:
            out += [z for z in zeilen if z.startswith(("Titel", "Beginn", "Enddatum", "Dauer"))]
        if kennung in status:
            out.append(status[kennung])
        out.append("")
    return "\n".join(out), info


def lese(p: Path) -> list[dict]:
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    lose = lese(LOSE)
    schluessel = {r["N"]: r for r in lese(SCHLUESSEL)}
    liste = {(r["notice"], r["los"]): r for r in lese(LISTE)}
    je_notice: dict[str, set[int]] = {}
    for r in lose:
        je_notice.setdefault(r["notice"], set()).add(int(r["los"]))
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "rohtext").mkdir(parents=True)
    infos = {}
    for pub, nummern in sorted(je_notice.items()):
        text, info = rohtext(pub, nummern)
        (OUT / "rohtext" / f"{pub}.txt").write_text(text, encoding="utf-8")
        infos[pub] = info

    # Prüfung gegen die API-Daten der Liste: Titel (die Liste kürzt auf 120 Zeichen), Beginn, Enddatum je Los
    pruef = ["# Prüfung des Rohtext-Skripts gegen die API-Daten (Iteration 9)", "",
             "Je Los der Stichprobe: Titel des XML-Loses = Titel der Liste (Beginn der Titel), Beginn und Enddatum des XML = Beginn und Enddatum aus der API (Liste). Abweichungen sind aufgeführt.", "",
             "| N | Bekanntmachung | Los | Titel gleich | Beginn gleich | Ende gleich | Hinweis |", "|---|---|---|---|---|---|---|"]
    ok = abw = 0
    for r in lose:
        i = int(r["los"])
        x = infos[r["notice"]][i - 1] if i <= len(infos[r["notice"]]) else None
        l = liste[(r["notice"], r["los"])]
        if x is None:
            pruef.append(f"| {r['N']} | {r['notice']} | {i} | – | – | – | Los fehlt im XML |")
            abw += 1
            continue
        t_ok = " ".join(x["titel"].split())[:100] == " ".join(l["los_titel"].split())[:100]
        b_ok = (x["beginn"] == l["beginn"]) or (not x["beginn"] and not l["beginn"])
        e_ok = True  # Enddatum der API steckt in gl_ende nur, wenn Herkunft „enddatum“
        if l["gl_herkunft"] == "enddatum" and l["gl_ende"]:
            e_ok = x["ende"] == l["gl_ende"]
        elif l["gl_herkunft"] == "beginn_plus_dauer":
            e_ok = not x["ende"]
        if t_ok and b_ok and e_ok:
            ok += 1
        else:
            abw += 1
            pruef.append(f"| {r['N']} | {r['notice']} | {i} | {'ja' if t_ok else 'nein'} | {'ja' if b_ok else 'nein'} | {'ja' if e_ok else 'nein'} | {x['kennung']}: {x['titel'][:50]} |")
    pruef += ["", f"**{ok} von {len(lose)} Losen stimmen in Titel, Beginn und Enddatum überein, {abw} weichen ab.**"]
    (OUT / "pruefung_rohtext.md").write_text("\n".join(pruef) + "\n", encoding="utf-8")

    # Pakete
    n = len(lose)
    gr = -(-n // N_TEILE)
    for k in range(N_TEILE):
        teil = lose[k * gr:(k + 1) * gr]
        if not teil:
            continue
        d = OUT / "pakete" / f"teil_{k + 1}"
        d.mkdir(parents=True)
        tab = ["| N | Bekanntmachung | Los | Titel |", "|---|---|---|---|"]
        for r in teil:
            tab.append(f"| {r['N']} | {r['notice']} | {r['los']} | {r['los_titel'].replace('|', '/')} |")
            shutil.copy(OUT / "rohtext" / f"{r['notice']}.txt", d / f"rohtext_{r['notice']}.txt")
        (d / "aufgabe.md").write_text(AUFGABE + "\n".join(tab) + "\n", encoding="utf-8")

    # Blatt für die menschliche Kontrolle (15 Lose)
    mensch = [r for r in lose if schluessel[r["N"]]["mensch"] == "ja"]
    blatt = ["# Kontrolle: Laufzeiten aus Bekanntmachungen ablesen (15 Lose)", "",
             "Bitte **ohne KI-Hilfe** ausfüllen und vorher nichts im Projektordner öffnen (`data/`, `reports/`). Öffne je Los die Bekanntmachung über den Link (TED, deutsche Fassung) und suche das Los über Titel und Nummer.",
             "Trage ein, was im Text und in den Feldern des Loses steht.", "",
             "- **Ende der ersten festen Laufzeit (ohne Verlängerungsoptionen):** TT.MM.JJJJ, `nicht tagesgenau` (Ereignis ohne Datum, z. B. „zum Schuljahresende“) oder `unbekannt`.",
             "- **Spätestes Ende (mit allen Verlängerungen):** TT.MM.JJJJ, `keine Verlängerung`, `keine Angabe` (nichts zu Verlängerungen gesagt) oder `unbestimmbar`.",
             "- **Kein Zuschlag:** `ja`, wenn für das Los kein Zuschlag erteilt wurde.", "- **Minuten:** ganze Minuten je Los. **Hilfsmittel:** `keine` oder welche.", "",
             "Sitzung: Start ______ Ende ______", ""]
    for r in sorted(mensch, key=lambda r: int(r["N"][1:])):
        blatt += [f"### {r['N']}: [{r['notice']}]({TED_LINK.format(r['notice'])}), Los {r['los']}", "", f"- Titel: {r['los_titel']}",
                  "- Ende der ersten festen Laufzeit: ", "- Spätestes Ende: ", "- Kein Zuschlag: ", "- Hilfsmittel: ", "- Minuten: ", ""]
    (OUT / "blatt_mensch.md").write_text("\n".join(blatt), encoding="utf-8")
    print(f"{len(je_notice)} Bekanntmachungen, {len(lose)} Lose, {N_TEILE} Pakete; Prüfung: {ok} von {len(lose)} stimmen, {abw} weichen ab; Blatt mit {len(mensch)} Losen")


if __name__ == "__main__":
    main()
