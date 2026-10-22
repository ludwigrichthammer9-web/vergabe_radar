"""Stichprobe zur Prüfung des Parsings: vergleicht unsere Tabelle mit der Original-XML der Bekanntmachung.

Zieht zufällig 5 Notices mit Haupt-CPV 909 (Gebäudereinigung) und 10 aus dem Rest, lädt die Original-eForms-XML
unverändert nach data/raw/ted_xml/ und liest die Vergleichswerte mit eigenen XPaths aus (unabhängig von der Search API).
XPaths laut eForms SDK, fields/fields.json (BT-536, BT-537, BT-36, BT-58, BT-57, BT-54, BT-262, BT-161, BT-720, BT-27).

Ergebnis: data/processed/stichprobe_iteration1.csv und eine Markdown-Tabelle auf der Konsole.
Die Bewertung der Abweichungen steht in reports/stichprobe_iteration1.md.

Aufruf:
    .venv\\Scripts\\python src/stichprobe_parsing.py
"""

import time
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "processed" / "notices_DEU_20260722_20261021.csv"
XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml"
OUT_PATH = PROJECT_ROOT / "data" / "processed" / "stichprobe_iteration1.csv"
XML_URL = "https://ted.europa.eu/en/notice/{nr}/xml"

SEED = 20261022
N_CLEANING = 5  # Haupt-CPV 909…
N_OTHER = 10

NS = {
    "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
    "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
    "efac": "http://data.europa.eu/p27/eforms-ubl-extension-aggregate-components/1",
    "efbc": "http://data.europa.eu/p27/eforms-ubl-extension-basic-components/1",
    "efext": "http://data.europa.eu/p27/eforms-ubl-extensions/1",
    "ext": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
}
EFORMS = "ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/efext:EformsExtension"
UNIT_TO_MONTHS = {"DAY": 1 / 30.44, "WEEK": 7 / 30.44, "MONTH": 1, "YEAR": 12}


def draw_sample(df: pd.DataFrame) -> pd.DataFrame:
    cleaning = df[df["main_cpv"].str.startswith("909")].sample(N_CLEANING, random_state=SEED)
    other = df[~df["main_cpv"].str.startswith("909")].sample(N_OTHER, random_state=SEED)
    return pd.concat([cleaning, other])


def fetch_xml(nr: str) -> Path:
    path = XML_DIR / f"{nr}.xml"
    if not path.exists():
        resp = requests.get(XML_URL.format(nr=nr), timeout=60)
        resp.raise_for_status()
        path.write_bytes(resp.content)  # unverändert speichern
        time.sleep(0.5)
    return path


def text(el) -> str:
    return el.text.strip() if el is not None and el.text else ""


def parse_xml(path: Path) -> dict:
    root = ET.parse(path).getroot()
    lots = root.findall("cac:ProcurementProjectLot", NS)
    lots = [lot for lot in lots if lot.find("cbc:ID", NS).get("schemeName") == "Lot"]

    per_lot = []
    for lot in lots:
        proj = lot.find("cac:ProcurementProject", NS)
        period = proj.find("cac:PlannedPeriod", NS)
        ext = proj.find("cac:ContractExtension", NS)
        dur = period.find("cbc:DurationMeasure", NS) if period is not None else None
        per_lot.append({
            "start": text(period.find("cbc:StartDate", NS))[:10] if period is not None else "",
            "end": text(period.find("cbc:EndDate", NS))[:10] if period is not None else "",
            "duration": (float(dur.text) * UNIT_TO_MONTHS[dur.get("unitCode")]) if dur is not None else None,
            "renewal_max": text(ext.find("cbc:MaximumNumberNumeric", NS)) if ext is not None else "",
            "renewal_text": bool(text(ext.find("cac:Renewal/cac:Period/cbc:Description", NS))) if ext is not None else False,
            "options_text": bool(text(ext.find("cbc:OptionsDescription", NS))) if ext is not None else False,
        })

    # Auftraggeber: ID der ersten ContractingParty -> Name im Organizations-Block
    buyer_id = text(root.find("cac:ContractingParty/cac:Party/cac:PartyIdentification/cbc:ID", NS))
    buyer_name = ""
    for org in root.findall(f"{EFORMS}/efac:Organizations/efac:Organization/efac:Company", NS):
        if text(org.find("cac:PartyIdentification/cbc:ID", NS)) == buyer_id:
            buyer_name = text(org.find("cac:PartyName/cbc:Name", NS))
            break

    def amounts(xpath):
        return [float(e.text) for e in root.findall(xpath, NS) if e.text]

    renewal_values = [int(l["renewal_max"]) for l in per_lot if l["renewal_max"].isdigit()]
    return {
        "lots_xml": len(per_lot),
        "lot1": per_lot[0] if per_lot else {},
        "lots_differ_dates": len({(l["start"], l["end"], l["duration"]) for l in per_lot}) > 1,
        "renewal_max": max(renewal_values) if renewal_values else None,
        "renewal_text_any": any(l["renewal_text"] for l in per_lot),
        "options_text_any": any(l["options_text"] for l in per_lot),
        "buyer_name": buyer_name,
        "main_cpv": text(root.find("cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode", NS)),
        "total_value": amounts(f"{EFORMS}/efac:NoticeResult/cbc:TotalAmount"),
        "tender_value": amounts(f"{EFORMS}/efac:NoticeResult/efac:LotTender/cac:LegalMonetaryTotal/cbc:PayableAmount"),
        "estimated_value": amounts("cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount")
        + amounts("cac:ProcurementProjectLot/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount"),
    }


def is_empty(v) -> bool:
    return v is None or v == "" or (isinstance(v, float) and pd.isna(v))


def same(a, b, numeric=False) -> str:
    """✓ gleich, ✗ verschieden, – beide leer."""
    if is_empty(a) and is_empty(b):
        return "–"
    if is_empty(a) or is_empty(b):
        return "✗"
    if numeric:
        return "✓" if abs(float(a) - float(b)) < 0.01 else "✗"
    return "✓" if str(a).strip() == str(b).strip() else "✗"


def compare(row: pd.Series, x: dict) -> dict:
    lot1 = x["lot1"]
    # Unsere Tabelle nimmt den ersten Wert ungleich -1; die XML kann mehrere Werte (Lose/Angebote) haben
    first = lambda vals: next((v for v in vals if v != -1), None)
    renewal_csv = (row["renewal_max"], row["filled:renewal-description-lot"], row["filled:option-description-lot"])
    renewal_xml = (x["renewal_max"], x["renewal_text_any"], x["options_text_any"])
    renewal_ok = (same(renewal_csv[0], renewal_xml[0], numeric=True) in "✓–"
                  and renewal_csv[1] == renewal_xml[1] and renewal_csv[2] == renewal_xml[2])
    values = [
        same(row["total_value"], first(x["total_value"]), numeric=True),
        same(row["tender_value"], first(x["tender_value"]), numeric=True),
        same(row["estimated_value"], first(x["estimated_value"]), numeric=True),
    ]
    return {
        "nr": row["publication_number"],
        "cpv909": row["main_cpv"].startswith("909"),
        "lose_csv": int(row["lots"]),
        "lose_xml": x["lots_xml"],
        "lose_unterschiedlich": x["lots_differ_dates"],
        "beginn": same(row["start_date_lot1"], lot1.get("start")),
        "beginn_werte": f"{row['start_date_lot1']} | {lot1.get('start')}",
        "ende": same(row["end_date_lot1"], lot1.get("end")),
        "ende_werte": f"{row['end_date_lot1']} | {lot1.get('end')}",
        "dauer": same(row["duration_months_lot1"], lot1.get("duration"), numeric=True),
        "dauer_werte": f"{row['duration_months_lot1']} | {lot1.get('duration')}",
        "verlaengerung": "✓" if renewal_ok else "✗",
        "verlaengerung_werte": f"BT58/57/54 {renewal_csv} | {renewal_xml}",
        "auftraggeber": same(row["buyer_name"], x["buyer_name"]),
        "auftraggeber_werte": f"{row['buyer_name']} | {x['buyer_name']}",
        "cpv": same(row["main_cpv"], x["main_cpv"]),
        "cpv_werte": f"{row['main_cpv']} | {x['main_cpv']}",
        "wert": "✗" if "✗" in values else ("✓" if "✓" in values else "–"),
        "wert_werte": (f"total {row['total_value']}|{x['total_value']}; tender {row['tender_value']}|{x['tender_value']}; "
                       f"est {row['estimated_value']}|{x['estimated_value']}"),
    }


def main() -> None:
    df = pd.read_csv(CSV_PATH, dtype={"publication_number": str, "main_cpv": str, "start_date_lot1": str,
                                      "end_date_lot1": str, "buyer_name": str})
    df[["start_date_lot1", "end_date_lot1", "buyer_name"]] = df[["start_date_lot1", "end_date_lot1", "buyer_name"]].fillna("")
    sample = draw_sample(df)
    XML_DIR.mkdir(parents=True, exist_ok=True)

    rows = []
    for _, row in sample.iterrows():
        nr = row["publication_number"]
        print(f"  {nr} ...")
        rows.append(compare(row, parse_xml(fetch_xml(nr))))
    result = pd.DataFrame(rows)
    result.to_csv(OUT_PATH, index=False, encoding="utf-8-sig")

    cols = ["nr", "cpv909", "lose_xml", "beginn", "ende", "dauer", "verlaengerung", "auftraggeber", "cpv", "wert"]
    print(result[cols].to_markdown(index=False))
    print(f"\nGespeichert: {OUT_PATH}")


if __name__ == "__main__":
    main()
