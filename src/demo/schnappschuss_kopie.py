"""Demo Profil-Match: erzeugt die Repo-Kopie docs/demo/daten/schnappschuss_demo.json aus data/raw/demo_push_<Datum>/.

Die Kopie enthält nur die Felder, die die Demo braucht (daten.GEBRAUCHTE_FELDER), und nur die Bekanntmachungen, die für die
Wiedergabe nötig sind: alle des 14-Tage-Fensters (Standard 02.10.-16.10.2026) sowie alle mit Leistungsort in der Oberpfalz
(Vergleichsmenge KI/Regel) und alle, die mit diesen Auftraggeber und Titel teilen (damit die Mehrfachprüfung gleich ausfällt).
Die übrigen Bekanntmachungen des Schnappschusses werden nur gezählt (meta.anzahl_gesamt). Die Rohdaten in data/raw bleiben unverändert.

Aufruf: .venv\\Scripts\\python.exe -I src\\demo\\schnappschuss_kopie.py
"""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # nötig wegen python -I

import daten as D  # noqa: E402
import stufen as S  # noqa: E402


def main(stichtag=date(2026, 10, 16), fenster_tage=14):
    ordner = D.neuester_schnappschuss()
    meta, alle = D.lade_schnappschuss(ordner)
    von = stichtag - timedelta(days=fenster_tage)
    schluessel = lambda b: (b["auftraggeber"].strip().lower(), b["titel"].strip().lower())  # wie S.dedupe
    wichtig = {schluessel(b) for b in alle if S.in_oberpfalz(b)}
    behalten = {b["nr"] for b in alle if von <= b["veroeffentlicht"] <= stichtag or S.in_oberpfalz(b) or schluessel(b) in wichtig}
    notices, gesehen = [], set()
    for f in sorted(ordner.glob("page_*.json")):
        for n in json.loads(f.read_text(encoding="utf-8")).get("notices", []):
            nr = n["publication-number"]
            if nr in behalten and nr not in gesehen:
                gesehen.add(nr)
                kurz = {k: n[k] for k in D.GEBRAUCHTE_FELDER if k in n}
                html = n.get("links", {}).get("html", {})
                kurz["links"] = {"html": {k: v for k, v in html.items() if k in ("DEU", "ENG")}}
                notices.append(kurz)
    ziel = D.REPO_KOPIE
    ziel.parent.mkdir(parents=True, exist_ok=True)
    out = {
        "meta": {
            "quelle": "TED (Tenders Electronic Daily), Search API v3, POST https://api.ted.europa.eu/v3/notices/search, anonym. "
                      "Öffentliche Auftragsbekanntmachungen; Quellenangabe: © Europäische Union, https://ted.europa.eu",
            "hinweis": "Auszug (nur gebrauchte Felder, nur Bekanntmachungen für die Wiedergabe) aus dem unveränderten Schnappschuss "
                       "data/raw/demo_push_20261106/ (liegt nicht im Repo). Enthält Auftraggeber, keine Personendaten außer evtl. "
                       "Ansprechpartnern im Freitext der Bekanntmachungen. Siehe docs/demo_push.md.",
            "schnappschuss_ordner": ordner.name,
            "query": meta["query"],
            "downloaded_at": meta["downloaded_at"],
            "notices_downloaded": meta["notices_downloaded"],
            "anzahl_gesamt": len(alle),
            "anzahl_in_kopie": len(notices),
            "fenster": f"{von} bis {stichtag}",
            "felder": D.GEBRAUCHTE_FELDER,
        },
        "notices": notices,
    }
    ziel.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(notices)} von {len(alle)} Bekanntmachungen -> {ziel} ({ziel.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
