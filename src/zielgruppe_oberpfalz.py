"""Mögliche Gesprächspartner für Phase 1 (Strang G): Firmen, die Gebäudereinigungsaufträge in der Oberpfalz gewonnen haben.

Quelle: TED-Zuschläge (eForms, ab 25.10.2023), Haupt-CPV 9091…, Leistungsort NUTS DE23 (Oberpfalz). Jede API-Antwort wird unverändert
in data/raw/ted_search/zielgruppe_oberpfalz_<datum>/ gespeichert.

Ergebnis:
    data/processed/zielgruppe_oberpfalz.csv   eine Zeile pro Firma (nicht in Git: Firmennamen können Personennamen enthalten)
    Konsolenausgabe mit Kennzahlen für docs/business.md

Aufruf:
    .venv\\Scripts\\python src/zielgruppe_oberpfalz.py
"""

import csv
import json
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

import requests

from analyze_completeness import flatten

API_URL = "https://api.ted.europa.eu/v3/notices/search"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
QUERY = ("buyer-country=DEU AND form-type=result AND main-classification-proc=9091* AND place-of-performance-subdiv-lot=DE23* "
         "AND publication-date>=20231025 AND publication-date<={to}")
FIELDS = ["publication-number", "publication-date", "buyer-name", "title-proc", "winner-name", "winner-city", "winner-post-code",
          "winner-size", "place-of-performance-subdiv-lot", "contract-duration-end-date-lot"]


def texts(value) -> list[str]:
    if isinstance(value, dict) and value.get("deu"):
        value = value["deu"]
    return [str(v) for v in flatten(value) if str(v).strip()]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    to = (date.today()).strftime("%Y%m%d")
    out_dir = PROJECT_ROOT / "data" / "raw" / "ted_search" / f"zielgruppe_oberpfalz_{to}"
    out_dir.mkdir(parents=True, exist_ok=True)
    body = {"query": QUERY.format(to=to), "fields": FIELDS, "limit": 250, "page": 1}
    resp = requests.post(API_URL, json=body, timeout=120)
    resp.raise_for_status()
    (out_dir / "page_0001.json").write_bytes(resp.content)  # unverändert speichern
    (out_dir / "request_meta.json").write_text(json.dumps({**body, "downloaded_at": datetime.now(timezone.utc).isoformat()},
                                                          ensure_ascii=False, indent=2), encoding="utf-8")
    data = resp.json()
    notices = data["notices"]
    if data["totalNoticeCount"] > len(notices):
        sys.exit(f"Mehr als {len(notices)} Treffer, Paginierung nötig.")

    firms = defaultdict(lambda: {"awards": set(), "cities": set(), "sizes": set(), "buyers": set(), "last": "", "ends": set()})
    without_winner = 0
    for n in notices:
        names = texts(n.get("winner-name"))
        if not names:
            without_winner += 1
            continue
        distinct = list(dict.fromkeys(name.strip() for name in names))
        for name in distinct:
            f = firms[name]
            f["awards"].add(n["publication-number"])
            # Ort und Größe nur zuordnen, wenn der Zuschlag genau einen Gewinner hat (sonst ist die Zuordnung unklar)
            if len(distinct) == 1:
                f["cities"] |= set(texts(n.get("winner-city")))
                f["sizes"] |= set(texts(n.get("winner-size")))
            f["buyers"] |= set(texts(n.get("buyer-name"))[:1])
            f["last"] = max(f["last"], str(n["publication-date"])[:10])
            f["ends"] |= {e[:10] for e in texts(n.get("contract-duration-end-date-lot"))}

    rows = sorted(firms.items(), key=lambda kv: (-len(kv[1]["awards"]), kv[0]))
    csv_path = PROJECT_ROOT / "data" / "processed" / "zielgruppe_oberpfalz.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["Firma", "Zuschläge", "Ort", "Größe", "Auftraggeber (Auswahl)", "letzter Zuschlag", "Vertragsenden", "Notices"])
        for name, f in rows:
            w.writerow([name, len(f["awards"]), ", ".join(sorted(f["cities"])), ", ".join(sorted(f["sizes"])),
                        " | ".join(sorted(f["buyers"])[:3]), f["last"], ", ".join(sorted(f["ends"])[:4]), ", ".join(sorted(f["awards"]))])

    sizes = defaultdict(int)
    for _, f in rows:
        for s in f["sizes"] or {"(keine Angabe)"}:
            sizes[s] += 1
    print(f"Zuschläge: {len(notices)}, davon ohne Firmenname: {without_winner}")
    print(f"Firmen: {len(rows)}, mit mehr als einem Zuschlag: {sum(len(f['awards']) > 1 for _, f in rows)}")
    print("Größe (Firmen):", dict(sizes))
    print(f"CSV: {csv_path}")


if __name__ == "__main__":
    main()
