"""Demo Profil-Match: Daten laden (Schnappschuss der TED Search API v3) und Bekanntmachungen vereinheitlichen.

Doku: https://docs.ted.europa.eu/api/latest/search.html (Endpunkt POST https://api.ted.europa.eu/v3/notices/search, anonym).
Feldnamen aus der eForms-Feldliste und durch Abfrage am 2026-11-06 bestätigt (deadline-receipt-tender-date-lot,
place-of-performance-subdiv-lot, selection-criterion-lot, selection-criterion-description-lot).

Die API-Antworten werden unverändert (Byte für Byte) in data/raw/demo_push_<Datum>/ abgelegt.
"""

import json
import re
import time
from datetime import date, datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
API_URL = "https://api.ted.europa.eu/v3/notices/search"

FIELDS = [
    "publication-number", "publication-date", "notice-type", "form-type", "procedure-type", "notice-version",
    "title-proc", "title-lot", "description-proc", "description-lot",
    "buyer-name", "buyer-city", "buyer-post-code",
    "classification-cpv", "main-classification-proc", "main-classification-lot",
    "deadline-receipt-tender-date-lot",
    "place-of-performance-subdiv-lot", "place-of-performance-city-lot", "place-of-performance-post-code-lot",
    "contract-duration-period-lot", "contract-duration-start-date-lot", "contract-duration-end-date-lot",
    "renewal-maximum-lot", "renewal-description-lot", "option-description-lot",
    "estimated-value-lot", "estimated-value-proc", "total-value",
    "selection-criterion-lot", "selection-criterion-description-lot",
]
PAGE_SIZE = 250  # API-Grenze: Felder * Seitengröße <= 10.000 (hier 31 * 250 = 7.750)


def live_abruf(ab_datum: str, ziel_ordner: Path, pause: float = 1.5, max_versuche: int = 6) -> Path:
    """Lädt deutsche Auftragsbekanntmachungen (form-type=competition) mit CPV 909* ab ab_datum (JJJJMMTT)."""
    import requests  # nur im Live-Modus nötig

    ziel_ordner.mkdir(parents=True, exist_ok=False)
    query = (f"buyer-country=DEU AND form-type=competition AND classification-cpv=909* "
             f"AND publication-date>={ab_datum}")
    seite, gesamt, geladen = 1, None, 0
    while True:
        body = {"query": query, "fields": FIELDS, "limit": PAGE_SIZE, "page": seite,
                "scope": "ALL", "paginationMode": "PAGE_NUMBER"}
        for versuch in range(max_versuche):
            r = requests.post(API_URL, json=body, timeout=120)
            if r.status_code == 200:
                break
            if r.status_code in (429, 500, 502, 503, 504):
                warte = min(60, 5 * 2 ** versuch)
                print(f"HTTP {r.status_code}, warte {warte} s (Versuch {versuch + 1})")
                time.sleep(warte)
                continue
            raise RuntimeError(f"HTTP {r.status_code}: {r.text[:500]}")
        else:
            raise RuntimeError("Zu viele Fehlversuche")
        (ziel_ordner / f"page_{seite:04d}.json").write_bytes(r.content)  # unverändert
        j = r.json()
        gesamt = j.get("totalNoticeCount")
        geladen += len(j.get("notices", []))
        print(f"Seite {seite}: {len(j.get('notices', []))} Bekanntmachungen (gesamt laut API {gesamt})")
        if geladen >= (gesamt or 0) or not j.get("notices"):
            break
        seite += 1
        time.sleep(pause)
    meta = {"api_url": API_URL, "query": query, "fields": FIELDS, "page_size": PAGE_SIZE,
            "downloaded_at": datetime.now(timezone.utc).isoformat(), "total_notice_count_api": gesamt,
            "notices_downloaded": geladen}
    (ziel_ordner / "request_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    return ziel_ordner


def neuester_schnappschuss() -> Path:
    ordner = sorted(p for p in RAW_DIR.glob("demo_push_*") if p.is_dir())
    if not ordner:
        raise FileNotFoundError("Kein Schnappschuss data/raw/demo_push_<Datum>/ vorhanden (Live-Abruf nötig).")
    return ordner[-1]


# ---------------------------------------------------------------- Normalisierung
def _liste(x):
    if x is None:
        return []
    if isinstance(x, list):
        out = []
        for e in x:
            out.extend(_liste(e))
        return out
    return [x]


def _text(feld):
    """Sprachfelder ({'deu': [...]} oder {'deu': '...'}) -> Liste von Texten (deutsch bevorzugt)."""
    if feld is None:
        return []
    if isinstance(feld, dict):
        for sprache in ("deu", "eng"):
            if sprache in feld:
                return [t for t in _liste(feld[sprache]) if isinstance(t, str)]
        erste = next(iter(feld.values()), [])
        return [t for t in _liste(erste) if isinstance(t, str)]
    return [t for t in _liste(feld) if isinstance(t, str)]


def _datum(s):
    if not s:
        return None
    try:
        return date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


def _eindeutig(seq):
    gesehen, out = set(), []
    for x in seq:
        if x not in gesehen:
            gesehen.add(x)
            out.append(x)
    return out


def _monate(perioden):
    """contract-duration-period-lot -> Liste (Monate) je Los; Einheiten YEAR/MONTH/DAY/WEEK."""
    faktor = {"YEAR": 12, "MONTH": 1, "WEEK": 12 / 52, "DAY": 12 / 365}
    out = []
    for p in _liste(perioden):
        if isinstance(p, dict) and p.get("unit") in faktor:
            try:
                out.append(round(float(p["value"]) * faktor[p["unit"]], 1))
            except (KeyError, ValueError):
                pass
    return out


def _zahlen(x):
    out = []
    for v in _liste(x):
        try:
            out.append(float(v))
        except (TypeError, ValueError):
            pass
    return out


def normalisieren(n: dict) -> dict:
    nr = n["publication-number"]
    links = n.get("links", {}).get("html", {})
    link = links.get("DEU") or links.get("ENG") or f"https://ted.europa.eu/de/notice/-/detail/{nr}"
    fristen = _eindeutig(d for d in map(_datum, _liste(n.get("deadline-receipt-tender-date-lot"))) if d)
    cpv = _eindeutig(str(c) for c in _liste(n.get("classification-cpv")) + _liste(n.get("main-classification-proc"))
                     + _liste(n.get("main-classification-lot")))
    nuts = _eindeutig(str(c) for c in _liste(n.get("place-of-performance-subdiv-lot")))
    wert_lot = _zahlen(n.get("estimated-value-lot"))
    wert_verf = _zahlen(n.get("estimated-value-proc")) + _zahlen(n.get("total-value"))
    return {
        "nr": nr,
        "veroeffentlicht": _datum(n.get("publication-date")),
        "verfahrensart": n.get("procedure-type"),
        "version": n.get("notice-version"),
        "titel": (_text(n.get("title-proc")) or [""])[0],
        "titel_lose": _text(n.get("title-lot")),
        "beschreibung_verfahren": " ".join(_text(n.get("description-proc"))),
        "beschreibung_lose": _text(n.get("description-lot")),
        "auftraggeber": (_text(n.get("buyer-name")) or ["(nicht angegeben)"])[0],
        "auftraggeber_ort": (_text(n.get("buyer-city")) or [""])[0],
        "cpv": cpv,
        "nuts": nuts,
        "orte": _eindeutig(_text(n.get("place-of-performance-city-lot"))),
        "plz": _eindeutig(_text(n.get("place-of-performance-post-code-lot"))),
        "fristen": fristen,
        "laufzeit_monate": _monate(n.get("contract-duration-period-lot")),
        "laufzeit_beginn": _eindeutig(str(_datum(d)) for d in _liste(n.get("contract-duration-start-date-lot")) if _datum(d)),
        "laufzeit_ende": _eindeutig(str(_datum(d)) for d in _liste(n.get("contract-duration-end-date-lot")) if _datum(d)),
        "verlaengerung": _text(n.get("renewal-description-lot")),
        "option": _text(n.get("option-description-lot")),
        "wert_lose": wert_lot,
        "wert_verfahren": wert_verf,
        "eignung_codes": _eindeutig(str(c) for c in _liste(n.get("selection-criterion-lot"))),
        "eignung_text": _eindeutig(_text(n.get("selection-criterion-description-lot"))),
        "link": link,
    }


def lade_schnappschuss(ordner: Path):
    """Liest alle Seiten; gibt (Meta, Liste normalisierter Bekanntmachungen ohne Duplikate) zurück."""
    meta = json.loads((ordner / "request_meta.json").read_text(encoding="utf-8"))
    gesehen, out = set(), []
    for f in sorted(ordner.glob("page_*.json")):
        for n in json.loads(f.read_text(encoding="utf-8")).get("notices", []):
            if n["publication-number"] in gesehen:
                continue
            gesehen.add(n["publication-number"])
            out.append(normalisieren(n))
    return meta, out


def volltext(b: dict) -> str:
    """Alle Texte einer Bekanntmachung, als Grundlage für Zitate (KI-Stufe) und Stichwortregeln."""
    teile = [b["titel"], *b["titel_lose"], b["beschreibung_verfahren"], *b["beschreibung_lose"],
             *b["verlaengerung"], *b["option"], *b["eignung_text"]]
    return "\n".join(_eindeutig(t for t in teile if t))[:30000]


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()
