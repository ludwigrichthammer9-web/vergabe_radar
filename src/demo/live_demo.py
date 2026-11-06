"""Live-Demo: erzeugt docs/demo/live_demo.html, eine einzelne, offline lauffähige HTML-Datei.

Die Datei enthält zwei Datensätze (Beispiel-Schnappschuss docs/demo/daten/schnappschuss_demo.json und großer Datensatz
docs/demo/daten/datensatz_bayern.json, beide im Python-Code vereinheitlicht), die
gespeicherten KI-Urteile (docs/demo/ki_urteile.json, nach der Zitatprüfung von ki_stufe._pruefe) und die Logik der Demo
(Filterstufen, Regelurteil, Nachrichten) in JavaScript. Die Vorlage steht in src/demo/live_demo_vorlage.html.
Kein Netz, keine KI-Aufrufe, nichts wird gesendet. Siehe docs/demo_push.md, Abschnitt "Live-Demo".

Aufruf (im Projektordner):
  .venv\\Scripts\\python.exe -I src\\demo\\live_demo.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # nötig wegen python -I

import daten as D  # noqa: E402
import ki_stufe as K  # noqa: E402
import nachrichten as N  # noqa: E402
import stufen as S  # noqa: E402

AUSGABE = D.PROJECT_ROOT / "docs" / "demo"
VORLAGE = Path(__file__).resolve().parent / "live_demo_vorlage.html"

# Kurznamen der Sitz-Auswahl (Bezugspunkte der NUTS-3-Regionen, dieselben Koordinaten wie stufen.NUTS3_PUNKTE)
SITZ_NAMEN = {"DE231": "Amberg", "DE232": "Regensburg", "DE233": "Weiden i. d. OPf.", "DE234": "Sulzbach-Rosenberg",
              "DE235": "Cham", "DE236": "Neumarkt i. d. OPf.", "DE237": "Neustadt a. d. Waldnaab", "DE239": "Schwandorf",
              "DE23A": "Tirschenreuth"}


# Großer Datensatz (Bayern, 12 Monate), erzeugt von src/demo/live_daten.py
BAYERN = D.PROJECT_ROOT / "docs" / "demo" / "daten" / "datensatz_bayern.json"
# NUTS-2-Namen (Regierungsbezirke Bayerns), nur für die Begründung "ausgeschieden wegen Ort" in der Animation
NUTS2_NAMEN = {"DE21": "Oberbayern", "DE22": "Niederbayern", "DE23": "Oberpfalz", "DE24": "Oberfranken",
               "DE25": "Mittelfranken", "DE26": "Unterfranken", "DE27": "Schwaben"}


def kompakt(alle, liste):
    """Bekanntmachungen für die Einbettung: Grundfelder für alle, ausführliche Felder nur für die Oberpfalz
    (nur diese erreichen die späteren Stufen)."""
    notices = []
    for b in alle:
        op = S.in_oberpfalz(b)
        n = {"nr": b["nr"], "d": b["veroeffentlicht"].isoformat(), "ag": b["auftraggeber"], "t": b["titel"],
             "cpv": b["cpv"], "nuts": b["nuts"], "op": op}
        if op:
            text = D.volltext(b)
            wert = b["wert_verfahren"] or b["wert_lose"]
            e = S.eignung_block(b)
            n.update({
                "orte": b["orte"], "fristen": [d.isoformat() for d in b["fristen"]], "lm": b["laufzeit_monate"],
                "lb": b["laufzeit_beginn"], "le": b["laufzeit_ende"], "wert": wert,
                "arten": e["arten"], "codes": e["codes"], "eignung_hinweis": e["hinweis"],
                "text_orte": S.orte_im_text(b), "lz_text": N.laufzeit_im_text(b),
                "n_lose": max(len(b["titel_lose"]), len(b["beschreibung_lose"]), 1),
                "link": b["link"], "text": text, "zeilen": K.kiquelle(b)[len(text) + 2:],
                "vorg": S.vorgaenger_hinweis(b, liste) if liste else None,
            })
        notices.append(n)
    return notices


def set_meta(meta, alle):
    return {"anzahl_gesamt": meta["anzahl_gesamt"], "anzahl_in_kopie": meta.get("anzahl_in_kopie", len(alle)),
            "schnappschuss": meta["schnappschuss_ordner"], "fenster": meta.get("fenster", ""),
            "downloaded_at": meta.get("downloaded_at", ""), "query": meta.get("query", "")}


def baue_daten():
    meta, alle = D.lade_schnappschuss(D.REPO_KOPIE)
    profile = json.loads((AUSGABE / "profil_beispiel.json").read_text(encoding="utf-8"))["profile"]
    cache = json.loads(D.PROJECT_ROOT.joinpath("docs", "demo", "ki_urteile.json").read_text(encoding="utf-8"))
    try:
        liste = S.lade_liste()
    except OSError:
        liste = []
    notices, ki = kompakt(alle, liste), {}
    for b in alle:
        if S.in_oberpfalz(b) and b["nr"] in cache and cache[b["nr"]].get("roh"):
            geprueft = K._pruefe(cache[b["nr"]]["roh"], b, profile)
            ki[b["nr"]] = {pid: {**u, "quelle": f"KI ({cache[b['nr']]['modell']})"} for pid, u in geprueft.items()}
    sets = {"beispiel": {"meta": set_meta(meta, alle), "notices": notices}}
    if BAYERN.exists():
        meta_b, alle_b = D.lade_schnappschuss(BAYERN)
        # Vorgänger-Hinweis im großen Datensatz abgeschaltet. Bezugsmenge: 52 Oberpfälzer Bekanntmachungen. Alte Fassung: 2 Auslösungen
        # (jeweils die spätere Zuschlagsbekanntmachung desselben Verfahrens), neue Fassung (Datumsbedingung in stufen.py): 1 Auslösung
        # (anderes Objekt, 118451-2026 "Gebäudereinigung Pfreimd" -> Los "Gebäudereinigung Standort Weiden"); alle falsch. docs/demo_push.md, Abschnitt 11.
        nb = kompakt(alle_b, [])
        # Gespeicherte KI-Urteile nur dort wiederverwenden, wo der Text der KI-Quelle wortgleich ist (gleiche Bekanntmachung)
        quelle_alt = {b["nr"]: K.kiquelle(b) for b in alle if b["nr"] in ki}
        for b, n in zip(alle_b, nb):
            if n["op"] and b["nr"] in quelle_alt:
                n["ki_gleich"] = K.kiquelle(b) == quelle_alt[b["nr"]]
        sets["bayern"] = {"meta": set_meta(meta_b, alle_b), "notices": nb}
    sitze = {c: {"name": SITZ_NAMEN[c], "lat": S.NUTS3_PUNKTE[c][1], "lon": S.NUTS3_PUNKTE[c][2]} for c in SITZ_NAMEN}
    return {
        "sets": sets,
        "nuts3": {c: list(v) for c, v in S.NUTS3_PUNKTE.items()}, "nuts2": NUTS2_NAMEN,
        "sitze": sitze, "profile": profile, "ki": ki,
        "texte": {"HINWEIS": N.HINWEIS, "QUELLE": N.QUELLE, "KI_HINWEIS": N.KI_HINWEIS, "KI_MODELL": K.MODELL},
    }


def main():
    daten = baue_daten()
    js = json.dumps(daten, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = VORLAGE.read_text(encoding="utf-8").replace("/*__DATEN__*/null", js)
    ziel = AUSGABE / "live_demo.html"
    ziel.write_text(html, encoding="utf-8")
    for name, s in daten["sets"].items():
        print(f"Datensatz {name}: {len(s['notices'])} Bekanntmachungen, {sum(1 for n in s['notices'] if n['op'])} in der Oberpfalz")
    print(f"{ziel} geschrieben: {len(html.encode('utf-8')) / 1e6:.2f} MB, {len(daten['ki'])} gespeicherte KI-Urteile (Bekanntmachungen).")


if __name__ == "__main__":
    main()
