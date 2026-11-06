"""Live-Demo, großer Datensatz: Abruf (einmalig) und Auszug für die Einbettung in docs/demo/live_demo.html.

Schritt 1 (nur mit --abruf, Netz nötig): TED Search API v3 (POST https://api.ted.europa.eu/v3/notices/search,
anonym, Doku https://docs.ted.europa.eu/api/latest/search.html). Gleiche Felder, Seitengröße und Wartelogik wie der
Demo-Abruf (daten.live_abruf), nur eine andere Abfrage:
  Auftragsbekanntmachungen (form-type=competition), Auftraggeber Deutschland, CPV 909*, Leistungsort Bayern
  (NUTS DE2*, ersatzweise PLZ 92*/93*), veröffentlicht 16.10.2025 bis 06.11.2026.
Die Antworten liegen unverändert in data/raw/demo_live_20261106/.

Schritt 2: Auszug docs/demo/daten/datensatz_bayern.json mit den Feldern, die normalisieren() braucht
(daten.GEBRAUCHTE_FELDER). Bekanntmachungen mit Leistungsort Oberpfalz bleiben ungekürzt (nur sie erreichen in der Demo
die Textstufen); bei allen übrigen werden lange Texte gekürzt (TEXT_MAX Zeichen je Textfeld), damit die Repo-Kopie klein
bleibt; wortgleiche Wiederholungen im Eignungs-Freitext stehen nur einmal. Beides ist im Kopf vermerkt. Rohdaten unverändert.

Aufruf (im Projektordner):
  .venv\\Scripts\\python.exe -I src\\demo\\live_daten.py            # Auszug aus vorhandenem Ordner (oder Abruf, falls fehlt)
"""

import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # nötig wegen python -I

import daten as D  # noqa: E402

ORDNER = D.RAW_DIR / "demo_live_20261106"
AUSZUG = D.PROJECT_ROOT / "docs" / "demo" / "daten" / "datensatz_bayern.json"
VON, BIS = "20251016", "20261106"
QUERY = ("buyer-country=DEU AND form-type=competition AND classification-cpv=909* AND "
         "(place-of-performance-subdiv-lot=DE2* OR place-of-performance-post-code-lot=92* OR place-of-performance-post-code-lot=93*) "
         f"AND publication-date>={VON} AND publication-date<={BIS}")
TEXT_MAX = 1500  # Zeichen je Textfeld-Eintrag im Auszug (Rohdaten ungekürzt)
TEXTFELDER = {"description-proc", "description-lot", "selection-criterion-description-lot", "renewal-description-lot",
              "option-description-lot"}


def _kuerze(wert, zaehler):
    """Kürzt Zeichenketten in verschachtelten Sprachfeldern auf TEXT_MAX Zeichen (mit Marke)."""
    if isinstance(wert, str):
        if len(wert) > TEXT_MAX:
            zaehler[0] += 1
            return wert[:TEXT_MAX].rstrip() + " […gekürzt]"
        return wert
    if isinstance(wert, list):
        return [_kuerze(w, zaehler) for w in wert]
    if isinstance(wert, dict):
        return {k: _kuerze(v, zaehler) for k, v in wert.items()}
    return wert


def _ohne_wiederholung(wert):
    """Wortgleiche Wiederholungen in Listen entfernen (nur für selection-criterion-description-lot; normalisieren()
    entfernt sie ohnehin mit _eindeutig, das Ergebnis der Demo ändert sich dadurch nicht)."""
    if isinstance(wert, list):
        return D._eindeutig(_ohne_wiederholung(w) for w in wert) if all(isinstance(w, str) for w in wert) else [
            _ohne_wiederholung(w) for w in wert]
    if isinstance(wert, dict):
        return {k: _ohne_wiederholung(v) for k, v in wert.items()}
    return wert


def main():
    import stufen as S  # noqa: E402  (nur hier gebraucht)

    if "--abruf" in sys.argv:  # Netzabruf nur mit ausdrücklichem Schalter; Ordnername trägt das Abrufdatum
        neu = D.RAW_DIR / f"demo_live_{date.today():%Y%m%d}"
        print(f"Abruf nach {neu} ...")
        D.live_abruf(VON, neu, pause=2.0, query=QUERY)
        print("Neuer Abruf liegt vor. Für den Auszug ORDNER in live_daten.py auf diesen Ordner setzen (Zahlen ändern sich).")
        return
    if not ORDNER.exists():
        sys.exit(f"{ORDNER} fehlt. Neuer Abruf nur mit --abruf (Netz nötig).")
    meta = json.loads((ORDNER / "request_meta.json").read_text(encoding="utf-8"))
    notices, gesehen, gekuerzt = [], set(), [0]
    for f in sorted(ORDNER.glob("page_*.json")):
        for n in json.loads(f.read_text(encoding="utf-8")).get("notices", []):
            nr = n["publication-number"]
            if nr in gesehen:
                continue
            gesehen.add(nr)
            # Oberpfalz (nur diese erreichen in der Demo die Textstufen): Texte ungekürzt; übrige gekürzt
            voll = bool(S.in_oberpfalz(D.normalisieren(n)))
            kurz = {}
            for k in D.GEBRAUCHTE_FELDER:
                if k not in n:
                    continue
                v = _ohne_wiederholung(n[k]) if k == "selection-criterion-description-lot" else n[k]
                kurz[k] = v if (voll or k not in TEXTFELDER) else _kuerze(v, gekuerzt)
            html = n.get("links", {}).get("html", {})
            kurz["links"] = {"html": {k: v for k, v in html.items() if k in ("DEU", "ENG")}}
            notices.append(kurz)
    out = {
        "meta": {
            "quelle": "TED (Tenders Electronic Daily), Search API v3, POST https://api.ted.europa.eu/v3/notices/search, anonym. "
                      "Öffentliche Auftragsbekanntmachungen; Quellenangabe: © Europäische Union, https://ted.europa.eu "
                      "(Amt für Veröffentlichungen der Europäischen Union)",
            "hinweis": f"Auszug (nur gebrauchte Felder; Bekanntmachungen mit Leistungsort Oberpfalz ungekürzt, bei allen übrigen "
                       f"Textfelder auf {TEXT_MAX} Zeichen gekürzt, Marke '[…gekürzt]'; wortgleiche Wiederholungen im Eignungs-"
                       f"Freitext je Bekanntmachung nur einmal) aus dem unveränderten Abruf data/raw/{ORDNER.name}/ (liegt nicht im Repo). Enthält Auftraggeber, keine "
                       "Personendaten außer evtl. Ansprechpartnern im Freitext. Siehe docs/demo_push.md, Abschnitt 11.",
            "schnappschuss_ordner": ORDNER.name,
            "query": meta["query"],
            "downloaded_at": meta["downloaded_at"],
            "total_notice_count_api": meta.get("total_notice_count_api"),
            "notices_downloaded": meta["notices_downloaded"],
            "anzahl_gesamt": len(notices),
            "anzahl_in_kopie": len(notices),
            "fenster": f"{VON[:4]}-{VON[4:6]}-{VON[6:]} bis {BIS[:4]}-{BIS[4:6]}-{BIS[6:]}",
            "text_max": TEXT_MAX,
            "texte_gekuerzt": gekuerzt[0],
            "felder": D.GEBRAUCHTE_FELDER,
        },
        "notices": notices,
    }
    AUSZUG.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{len(notices)} Bekanntmachungen, {gekuerzt[0]} Texte gekürzt -> {AUSZUG} ({AUSZUG.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
