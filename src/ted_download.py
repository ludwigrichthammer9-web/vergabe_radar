"""Lädt Bekanntmachungen aus der TED Search API v3 (Standard: Zuschläge, form-type=result).

Jede API-Antwort wird unverändert (Byte für Byte) in data/raw/ted_search/<lauf>/ gespeichert.
Auswertungen passieren getrennt in analyze_completeness.py.

Doku: https://docs.ted.europa.eu/api/latest/search.html
OpenAPI-Spezifikation: https://ted.europa.eu/docs/v3
Feldliste: https://docs.ted.europa.eu/ODS/latest/reuse/field-list.html

Hinweis: Notices vor eForms (vor dem 25.10.2023) liefern nur einen Teil der Felder (u. a. keine Haupt-CPV, keine Laufzeit).
Für sie filtert man den CPV-Bereich über --cpv-field classification-cpv. Die API reicht bis Ende Oktober 2016 zurück.

Aufruf:
    .venv\\Scripts\\python src/ted_download.py                       # Zuschläge der letzten 3 Monate bis gestern
    .venv\\Scripts\\python src/ted_download.py --from 20260722 --to 20261021
    .venv\\Scripts\\python src/ted_download.py --form-type competition --cpv 909 --cpv-field main-classification-proc \\
        --from 20260401 --to 20260630
"""

import argparse
import json
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

API_URL = "https://api.ted.europa.eu/v3/notices/search"
PAGE_SIZE = 250  # Maximum laut API
PAUSE_SECONDS = 0.5  # höflicher Abstand zwischen zwei Requests
MAX_RETRIES = 5

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw" / "ted_search"

# Felder, die wir pro Bekanntmachung abfragen. Grenze der API: len(FIELDS) * PAGE_SIZE <= 10.000.
FIELDS = [
    # Meta
    "publication-number",
    "publication-date",
    "notice-type",
    "procedure-type",
    "contract-nature-main-proc",
    "form-type",
    "title-proc",
    # Kennungen für Zuordnung und Deduplizierung (seit Iteration 2)
    "procedure-identifier",  # BT-04
    "notice-identifier",  # BT-701
    "notice-version",  # BT-757
    "change-notice-version-identifier",  # BT-758: gesetzt bei Änderungsbekanntmachungen
    "change-reason-code",  # BT-140
    # Vertragslaufzeit
    "contract-duration-period-lot",  # BT-36: Dauer (Wert + Einheit)
    "contract-duration-start-date-lot",  # BT-536
    "contract-duration-end-date-lot",  # BT-537
    "contract-duration-period-oth-lot",  # BT-538: z. B. UNLIMITED / UNKNOWN
    # Verlängerungen und Optionen
    "renewal-maximum-lot",  # BT-58: max. Anzahl Verlängerungen
    "renewal-description-lot",  # BT-57
    "option-description-lot",  # BT-54
    # CPV
    "main-classification-proc",
    "main-classification-lot",
    "classification-cpv",
    # Auftraggeber
    "buyer-name",
    "buyer-country",
    "buyer-identifier",  # BT-501, uneinheitlich befüllt (Leitweg-ID, UUID, teils Telefonnummer)
    "buyer-city",
    "buyer-post-code",
    # Auftragswert
    "total-value",  # BT-161: Gesamtwert der Bekanntmachung
    "result-value-lot",  # BT-709: Höchstwert Rahmenvereinbarung je Los-Ergebnis
    "tender-value",  # BT-720: Wert des erfolgreichen Angebots
    "estimated-value-proc",  # BT-27 (Verfahren)
    "estimated-value-lot",  # BT-27 (Los)
    "framework-maximum-value-lot",
]


def default_period(today: date) -> tuple[date, date]:
    """Letzte 3 Monate: vom gleichen Tag vor 3 Monaten bis gestern."""
    month = today.month - 3
    year = today.year
    if month < 1:
        month += 12
        year -= 1
    day = min(today.day, 28)  # einfache Absicherung gegen z. B. 31. Februar
    return date(year, month, day), today - timedelta(days=1)


def build_query(
    country: str, date_from: str, date_to: str, form_type: str = "result", cpv: str | None = None,
    cpv_field: str = "classification-cpv",
) -> str:
    cpv_clause = f"AND {cpv_field}={cpv}* " if cpv else ""
    return (
        f"buyer-country={country} AND form-type={form_type} {cpv_clause}"
        f"AND publication-date>={date_from} AND publication-date<={date_to}"
    )


def run_name(country: str, date_from: str, date_to: str, form_type: str, cpv: str | None, cpv_field: str) -> str:
    """Ordnername des Laufs. Ohne Zusatzfilter wie in Iteration 1: <land>_<von>_<bis>."""
    parts = [country]
    if form_type != "result" or cpv:
        parts.append(form_type)
    if cpv:
        parts.append(f"cpv{cpv}" + ("main" if cpv_field == "main-classification-proc" else ""))
    return "_".join(parts + [date_from, date_to])


def post_with_retry(session: requests.Session, body: dict) -> requests.Response:
    """POST mit exponentiellem Backoff bei Rate-Limit (429), Serverfehlern (5xx) und Timeouts."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.post(API_URL, json=body, timeout=120)
        except requests.RequestException as exc:
            error = f"{type(exc).__name__}: {exc}"
        else:
            if resp.status_code == 200:
                return resp
            if resp.status_code != 429 and resp.status_code < 500:
                # 4xx (außer 429) = Fehler in unserer Anfrage, Wiederholen hilft nicht
                sys.exit(f"API-Fehler {resp.status_code}: {resp.text[:1000]}")
            error = f"HTTP {resp.status_code}"
        wait = 2**attempt
        print(f"  Versuch {attempt}/{MAX_RETRIES} fehlgeschlagen ({error}), warte {wait}s ...")
        time.sleep(wait)
    sys.exit("Abbruch: zu viele fehlgeschlagene Versuche.")


def main() -> None:
    default_from, default_to = default_period(date.today())
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--from", dest="date_from", default=default_from.strftime("%Y%m%d"))
    parser.add_argument("--to", dest="date_to", default=default_to.strftime("%Y%m%d"))
    parser.add_argument("--country", default="DEU", help="dreistelliger Ländercode des Auftraggebers")
    parser.add_argument("--form-type", default="result", help="z. B. result, competition, planning")
    parser.add_argument("--cpv", help="CPV-Präfix, z. B. 909 (ohne Angabe: alle CPV)")
    parser.add_argument(
        "--cpv-field", default="classification-cpv", choices=["classification-cpv", "main-classification-proc"],
        help="classification-cpv = Haupt- oder Zusatz-CPV (auch vor eForms); main-classification-proc = Haupt-CPV (nur eForms)",
    )
    args = parser.parse_args()

    out_dir = RAW_DIR / run_name(args.country, args.date_from, args.date_to, args.form_type, args.cpv, args.cpv_field)
    if out_dir.exists() and any(out_dir.iterdir()):
        sys.exit(f"{out_dir} existiert bereits und ist nicht leer. Bitte löschen oder anderen Zeitraum wählen.")
    out_dir.mkdir(parents=True, exist_ok=True)

    query = build_query(args.country, args.date_from, args.date_to, args.form_type, args.cpv, args.cpv_field)
    body = {
        "query": query,
        "fields": FIELDS,
        "limit": PAGE_SIZE,
        "paginationMode": "ITERATION",
    }
    print(f"Query: {query}")
    print(f"Ziel:  {out_dir}")

    session = requests.Session()
    page = 0
    total_notices = 0
    total_expected = None
    seen = set()
    duplicates = 0

    while True:
        page += 1
        resp = post_with_retry(session, body)
        # Rohdaten unverändert speichern, bevor wir irgendetwas daran parsen
        (out_dir / f"page_{page:04d}.json").write_bytes(resp.content)

        data = resp.json()
        notices = data.get("notices", [])
        if total_expected is None:
            total_expected = data.get("totalNoticeCount")
        if data.get("timedOut"):
            print(f"  WARNUNG: Seite {page} meldet timedOut=true, Ergebnis evtl. unvollständig")

        for n in notices:
            pub = n.get("publication-number")
            if pub in seen:
                duplicates += 1
            seen.add(pub)
        total_notices += len(notices)
        print(f"  Seite {page:3d}: {len(notices):3d} Notices (gesamt {total_notices}/{total_expected})")

        token = data.get("iterationNextToken")
        if not notices or not token:
            break
        body["iterationNextToken"] = token
        time.sleep(PAUSE_SECONDS)

    meta = {
        "api_url": API_URL,
        "query": query,
        "fields": FIELDS,
        "page_size": PAGE_SIZE,
        "pagination_mode": "ITERATION",
        "date_from": args.date_from,
        "date_to": args.date_to,
        "country": args.country,
        "form_type": args.form_type,
        "cpv": args.cpv,
        "cpv_field": args.cpv_field if args.cpv else None,
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
        "total_notice_count_api": total_expected,
        "notices_downloaded": total_notices,
        "unique_publication_numbers": len(seen),
        "pages": page,
    }
    (out_dir / "request_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nFertig: {total_notices} Notices in {page} Dateien.")
    if total_notices != total_expected:
        print(f"WARNUNG: API meldete {total_expected} Treffer, geladen wurden {total_notices}.")
    if duplicates:
        print(f"WARNUNG: {duplicates} doppelte publication-numbers.")


if __name__ == "__main__":
    main()
