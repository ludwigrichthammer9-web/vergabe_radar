"""Zählt TED-Bekanntmachungen je Quartal für einen CPV-Bereich (nur Trefferzahlen, keine Notices).

Zweck: Rückreichweite und Basisrate klären (Iteration 2, Schritt 2). Pro Quartal und Zählung wird eine Suchanfrage
mit limit=1 gestellt und `totalNoticeCount` ausgewertet. Jede API-Antwort wird unverändert in
data/raw/ted_counts/<land>_<cpv>_<datum>/ gespeichert, die Auswertung als CSV in data/processed/.

Zählungen:
- result_cpv, competition_cpv, planning_cpv: CPV-Bereich in `classification-cpv` (Haupt- oder Zusatz-CPV).
  Funktioniert auch für Notices vor eForms.
- result_main, competition_main: CPV-Bereich in `main-classification-proc` (Haupt-CPV, BT-262).
  Nur für eForms-Notices befüllt (ab Ende Oktober 2023), davor 0.

Die Such-API enthält Notices ab Ende Oktober 2016 (Probeabfragen vom 23.10.2026, data/raw/ted_probes/20261023/).

Aufruf:
    .venv\\Scripts\\python src/ted_counts.py                       # CPV 909, DEU, Q4 2016 bis heute
    .venv\\Scripts\\python src/ted_counts.py --cpv 9062 --country DEU
"""

import argparse
import csv
import json
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

from ted_download import API_URL, PAUSE_SECONDS, post_with_retry

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw" / "ted_counts"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

FIRST_QUARTER = date(2016, 10, 1)  # Beginn der Such-API laut Probeabfragen

# Name der Zählung -> (form-type, CPV-Feld)
COUNTS = {
    "result_cpv": ("result", "classification-cpv"),
    "competition_cpv": ("competition", "classification-cpv"),
    "planning_cpv": ("planning", "classification-cpv"),
    "result_main": ("result", "main-classification-proc"),
    "competition_main": ("competition", "main-classification-proc"),
}


def quarters(first: date, last_day: date) -> list[tuple[str, date, date]]:
    """Quartale von `first` bis einschließlich `last_day`; das letzte Quartal endet ggf. vorzeitig."""
    result = []
    start = first
    while start <= last_day:
        q = (start.month - 1) // 3 + 1
        next_start = date(start.year + (q == 4), 1 if q == 4 else start.month + 3, 1)
        end = min(next_start - timedelta(days=1), last_day)
        result.append((f"{start.year}-Q{q}", start, end))
        start = next_start
    return result


def build_query(country: str, form_type: str, cpv_field: str, cpv: str, start: date, end: date) -> str:
    return (
        f"buyer-country={country} AND form-type={form_type} AND {cpv_field}={cpv}* "
        f"AND publication-date>={start:%Y%m%d} AND publication-date<={end:%Y%m%d}"
    )


def main() -> None:
    yesterday = date.today() - timedelta(days=1)
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cpv", default="909", help="CPV-Präfix, z. B. 909 für Gebäudereinigung")
    parser.add_argument("--country", default="DEU", help="dreistelliger Ländercode des Auftraggebers")
    parser.add_argument("--to", dest="date_to", default=yesterday.strftime("%Y%m%d"), help="letzter Tag (JJJJMMTT)")
    args = parser.parse_args()

    last_day = datetime.strptime(args.date_to, "%Y%m%d").date()
    out_dir = RAW_DIR / f"{args.country}_{args.cpv}_{date.today():%Y%m%d}"
    if out_dir.exists() and any(out_dir.iterdir()):
        sys.exit(f"{out_dir} existiert bereits und ist nicht leer. Bitte löschen oder an einem anderen Tag laufen lassen.")
    out_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    rows = []
    for label, start, end in quarters(FIRST_QUARTER, last_day):
        row = {"quartal": label, "von": start.isoformat(), "bis": end.isoformat()}
        for name, (form_type, cpv_field) in COUNTS.items():
            query = build_query(args.country, form_type, cpv_field, args.cpv, start, end)
            resp = post_with_retry(session, {"query": query, "fields": ["publication-number"], "limit": 1, "page": 1})
            # Rohdaten unverändert speichern, bevor wir etwas daran auswerten
            (out_dir / f"{label}_{name}.json").write_bytes(resp.content)
            data = resp.json()
            if data.get("timedOut"):
                print(f"  WARNUNG: {label} {name} meldet timedOut=true")
            row[name] = data.get("totalNoticeCount")
            time.sleep(PAUSE_SECONDS)
        rows.append(row)
        print("  " + "  ".join(f"{k}={v}" for k, v in row.items() if k not in ("von", "bis")))

    meta = {
        "api_url": API_URL,
        "queries": {
            name: f"buyer-country={args.country} AND form-type={ft} AND {field}={args.cpv}* "
            "AND publication-date>=<von> AND publication-date<=<bis>"
            for name, (ft, field) in COUNTS.items()
        },
        "cpv": args.cpv,
        "country": args.country,
        "first_quarter": FIRST_QUARTER.isoformat(),
        "date_to": last_day.isoformat(),
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
        "quarters": len(rows),
    }
    (out_dir / "request_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = PROCESSED_DIR / f"counts_{args.country}_{args.cpv}_quartale.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nFertig: {len(rows)} Quartale. Rohdaten: {out_dir}  Tabelle: {csv_path}")


if __name__ == "__main__":
    main()
