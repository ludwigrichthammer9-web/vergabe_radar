"""Lädt die Original-XML der Notices aus reports/k2_pruefliste.md und erstellt kompakte Auszüge für die manuelle Prüfung.

- Jede XML wird unverändert in data/raw/ted_xml/k2_<datum>/<publication-number>.xml gespeichert (vorhandene werden nicht neu geladen).
- Bei Zuschlägen vor eForms (Formular F03) wird zusätzlich die referenzierte alte Ausschreibung (REF_NOTICE, meist F02) geladen,
  denn nur dort steht die Laufzeit (Befund Iteration 2, Schritt 1). Damit wird A11 an der Stichprobe geprüft.
- Auszug: Titel, Kurzbeschreibung, Lose, Ort (Stadt, PLZ, Straße bzw. MAIN_SITE), Laufzeit, Verlängerung.

Ergebnis: reports/k2_auszuege.md (wird bei jedem Lauf neu erzeugt)

Aufruf:
    .venv\\Scripts\\python src/k2_xml_auszug.py
"""

import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHECKLIST = PROJECT_ROOT / "reports" / "k2_pruefliste.md"
XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml" / "k2_20261023"
OUT = PROJECT_ROOT / "reports" / "k2_auszuege.md"
XML_URL = "https://ted.europa.eu/en/notice/{}/xml"
PAUSE_SECONDS = 0.5
MAX_TEXT = 350


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def fetch(pub: str) -> ET.Element | None:
    path = XML_DIR / f"{pub}.xml"
    if not path.exists():
        resp = requests.get(XML_URL.format(pub), timeout=60)
        if resp.status_code != 200:
            print(f"  {pub}: HTTP {resp.status_code}")
            return None
        path.write_bytes(resp.content)  # unverändert speichern
        time.sleep(PAUSE_SECONDS)
    try:
        return ET.fromstring(path.read_bytes())
    except ET.ParseError as exc:
        print(f"  {pub}: XML-Fehler {exc}")
        return None


def text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    return re.sub(r"\s+", " ", " ".join(el.itertext())).strip()


def short(s: str) -> str:
    return s if len(s) <= MAX_TEXT else s[:MAX_TEXT] + " …"


def child(el: ET.Element, name: str) -> ET.Element | None:
    return next((c for c in el if local(c.tag) == name), None)


def children(el: ET.Element, name: str) -> list[ET.Element]:
    return [c for c in el if local(c.tag) == name]


def first_desc(el: ET.Element, name: str) -> ET.Element | None:
    return next((d for d in el.iter() if local(d.tag) == name), None)


def summarize_eforms(root: ET.Element) -> list[str]:
    lines = []
    proj = child(root, "ProcurementProject")
    if proj is not None:
        lines.append(f"Titel: {text(child(proj, 'Name'))}")
        lines.append(f"Beschreibung: {short(text(child(proj, 'Description')))}")
    for lot in children(root, "ProcurementProjectLot"):
        lp = child(lot, "ProcurementProject")
        if lp is None:
            continue
        lot_id = text(child(lot, "ID"))
        addr = first_desc(lp, "RealizedLocation")
        place = ""
        if addr is not None:
            parts = [text(first_desc(addr, n)) for n in ("StreetName", "PostalZone", "CityName")]
            place = ", ".join(p for p in parts if p) or short(text(first_desc(addr, "Description")))
        period = first_desc(lp, "PlannedPeriod")
        dur = ""
        if period is not None:
            start, end = text(first_desc(period, "StartDate")), text(first_desc(period, "EndDate"))
            measure = first_desc(period, "DurationMeasure")
            dur = f"{start[:10]} bis {end[:10]}" if end else (
                f"{text(measure)} {measure.get('unitCode', '')}" if measure is not None else "")
        renewal = text(first_desc(lp, "ContractExtension"))
        lines.append(f"Los {lot_id}: {text(child(lp, 'Name'))} | Ort: {place or '-'} | Laufzeit: {dur or '-'}"
                     + (f" | Verlängerung: {short(renewal)}" if renewal else ""))
    return lines


def summarize_ted2014(root: ET.Element) -> tuple[list[str], str | None]:
    form = next((e for e in root.iter() if re.fullmatch(r"F\d\d_2014", local(e.tag))), None)
    if form is None:
        return ["(altes Format nicht erkannt)"], None
    lines = [f"Formular: {local(form.tag)}"]
    obj = first_desc(form, "OBJECT_CONTRACT")
    if obj is not None:
        lines.append(f"Titel: {text(child(obj, 'TITLE'))}")
        lines.append(f"Beschreibung: {short(text(child(obj, 'SHORT_DESCR')))}")
        for d in children(obj, "OBJECT_DESCR"):
            dur = []
            for n in ("DATE_START", "DATE_END", "DURATION"):
                e = child(d, n)
                if e is not None:
                    dur.append(f"{n}={text(e)}{(' ' + e.get('TYPE', '')) if n == 'DURATION' else ''}")
            renewal = "ja" if child(d, "RENEWAL") is not None else ("nein" if child(d, "NO_RENEWAL") is not None else "-")
            lines.append(f"Los {text(child(d, 'LOT_NO')) or '-'}: {text(child(d, 'TITLE'))} | Ort: "
                         f"{short(text(child(d, 'MAIN_SITE'))) or '-'} | Laufzeit: {', '.join(dur) or '-'} | Verlängerung: {renewal}")
    # REF_NOTICE steht im Kopfteil (CODED_DATA_SECTION), nicht im Formular; NOTICE_NUMBER_OJ im Formularteil als Ersatz
    ref = first_desc(root, "REF_NOTICE")
    if ref is None:
        ref = first_desc(form, "NOTICE_NUMBER_OJ")
    ref_pub = None
    m = re.search(r"(\d{4})/S \d+-(\d+)", text(ref)) if ref is not None else None
    if m:
        ref_pub = f"{int(m.group(2))}-{m.group(1)}"
        lines.append(f"Verweis auf frühere Bekanntmachung: {text(ref)} → {ref_pub}")
    return lines, ref_pub


def summarize(pub: str) -> tuple[list[str], str | None]:
    root = fetch(pub)
    if root is None:
        return ["(nicht geladen)"], None
    if local(root.tag) in ("ContractNotice", "ContractAwardNotice", "PriorInformationNotice"):
        return summarize_eforms(root), None
    return summarize_ted2014(root)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    XML_DIR.mkdir(parents=True, exist_ok=True)
    lines = CHECKLIST.read_text(encoding="utf-8").splitlines()
    out = ["# Auszüge aus der Original-XML für die K2-Prüfung", "",
           f"Erzeugt mit `src/k2_xml_auszug.py` aus [k2_pruefliste.md](k2_pruefliste.md). XML unverändert in "
           f"`{XML_DIR.relative_to(PROJECT_ROOT).as_posix()}/`. Texte gekürzt auf {MAX_TEXT} Zeichen.", ""]
    case = None
    for line in lines:
        if line.startswith("### "):
            case = line[4:]
            out.append(f"## {case}")
        m = re.match(r"- (Ausschreibung|Vorgänger): \[(\d+-\d{4})\]", line)
        if case and m:
            role, pub = m.groups()
            print(f"{case} {role} {pub}")
            summary, ref_pub = summarize(pub)
            out.append(f"**{role} {pub}**")
            out += [f"- {s}" for s in summary]
            if ref_pub:
                ref_summary, _ = summarize(ref_pub)
                out.append(f"- *Referenzierte Bekanntmachung {ref_pub}:*")
                out += [f"  - {s}" for s in ref_summary]
            out.append("")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Auszüge: {OUT}")


if __name__ == "__main__":
    main()
