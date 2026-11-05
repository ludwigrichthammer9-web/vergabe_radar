"""Iteration 10: Vergabeweiser gegen die eigene Liste (Fassung 9) am Vergleichswert der Iteration 9 (W1 bis W4).

Vorab festgelegt in docs/iterationen.md (Iteration 10); dieses Skript wird vor dem Abruf der Stichprobe committet.
- Stichprobe: die Z-Lose der Iteration 9 ohne „nicht tagesgenau“ (wie V1). Vergleichswert unverändert aus src/prepare/auswertung_iteration9.py.
- Zuordnung ohne Handentscheid, Kandidaten in dieser Reihenfolge: (1) alle cac:NoticeDocumentReference/cbc:ID der Zuschlagsbekanntmachung (XML aus
  Iteration 9) → TED-XML dieser Bekanntmachungen (unverändert nach data/raw/ted_xml/vergleich_iteration10/) → cbc:ID[@schemeName="notice-id"];
  (2) Auftragsbekanntmachungen mit derselben ContractFolderID (= procedure-identifier, BT-04) aus data/raw/ted_search/*competition*, früheste zuerst
  → notice-identifier (BT-701); (3) notice-id der Zuschlagsbekanntmachung selbst. Je Kandidat GET /api/v1/tenders/{erste 8 Zeichen} (Antwort
  unverändert nach data/raw/vergabeweiser_20261105/tender_<id>.json, bei 404 Datei tender_<id>.404). Der erste Treffer mit Status 200 gilt.
- Wert von Vergabeweiser je Los: ends_on des Verfahrens; sonst starts_on + duration_months − 1 Tag; sonst „kein Wert“.
- Korrekt (für Liste und Vergabeweiser gleich): Datum = Vergleichswert ± 1 Tag, oder beide ohne Datum. Zusätzlich Zählung wie V1 (ohne Datum nie Treffer).
- W1: Treffer Liste − Treffer Vergabeweiser auf den gemeinsamen Losen (Vergabeweiser hat einen Eintrag); ≥ 5 Vorteil, 1 bis 4 kein gesicherter, ≤ 0 keiner;
  beurteilbar ab 40 gemeinsamen Losen. W2 Abdeckung und W1 auf allen Losen. W3 Fehltreffer aus Bekanntmachungen mit unterschiedlichen Enden je Los
  (eigene Liste). W4 Anteil eu = false bei /expiring (Gebäudereinigung, 36 Monate; Bayern und Deutschland).

Aufruf:  .venv\\Scripts\\python -I src/prepare/vergleich_iteration10.py --abruf   (lädt, höchstens 1 Vergabeweiser-Abfrage pro 61 s)
         .venv\\Scripts\\python -I src/prepare/vergleich_iteration10.py           (wertet nur aus)      Ausgabe: reports/vergleich_iteration10.md
"""

import csv
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auswertung_iteration9 as a9  # noqa: E402  (Vergleichswert und Hilfsfunktionen unverändert wiederverwenden)

ROOT = Path(__file__).resolve().parent.parent.parent
XML9 = ROOT / "data" / "raw" / "ted_xml" / "iteration9_20261105"
XML10 = ROOT / "data" / "raw" / "ted_xml" / "vergleich_iteration10"
VW = ROOT / "data" / "raw" / "vergabeweiser_20261105"
LISTE = ROOT / "data" / "processed" / "vertragsliste_909.csv"
REPORT = ROOT / "reports" / "vergleich_iteration10.md"
API = "https://vergabeweiser.de/api/v1"
HEADERS = {"User-Agent": "vergabe-radar-studienprojekt"}
PAUSE_VW = 61
_letzte_vw = [0.0]


def hole(url: str, **kw) -> requests.Response:
    """GET mit Wiederholung bei Verbindungsfehlern (z. B. kurzer DNS-Ausfall); ändert nichts an Zuordnung oder Auswertung."""
    for versuch in range(6):
        try:
            return requests.get(url, timeout=60, **kw)
        except requests.exceptions.ConnectionError as e:
            print(f"  Verbindungsfehler ({versuch + 1}/6), neuer Versuch in 120 s: {url}")
            time.sleep(120)
    return requests.get(url, timeout=60, **kw)


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def referenzen(pub: str) -> tuple[list[str], str | None, str | None]:
    """Verweise auf frühere Bekanntmachungen, ContractFolderID und eigene notice-id der Zuschlagsbekanntmachung."""
    root = ET.fromstring((XML9 / f"{pub}.xml").read_bytes())
    refs, folder, nid = [], None, None
    for e in root.iter():
        tag = _local(e.tag)
        if tag == "NoticeDocumentReference":
            for c in e:
                if _local(c.tag) == "ID" and re.fullmatch(r"\d+-\d{4}", (c.text or "").strip()):
                    refs.append(c.text.strip())
        elif tag == "ContractFolderID" and folder is None:
            folder = (e.text or "").strip()
        elif tag == "ID" and e.get("schemeName") == "notice-id" and nid is None:
            nid = (e.text or "").strip()
    return list(dict.fromkeys(refs)), folder, nid


def verfahrensindex() -> dict[str, list[str]]:
    """procedure-identifier → notice-identifier der Auftragsbekanntmachungen (früheste zuerst) aus den gespeicherten TED-Abfragen."""
    idx = defaultdict(set)
    for f in sorted((ROOT / "data" / "raw" / "ted_search").glob("*competition*/*.json")):
        for n in json.loads(f.read_text(encoding="utf-8")).get("notices", []):
            p, ni = n.get("procedure-identifier"), n.get("notice-identifier")
            if p and ni:
                p, ni = (p if isinstance(p, str) else p[0]), (ni if isinstance(ni, str) else ni[0])
                idx[p].add((n.get("publication-date") or "", ni))
    return {p: [ni for _, ni in sorted(s)] for p, s in idx.items()}


def notice_id(pub: str, abruf: bool) -> str | None:
    p = XML10 / f"{pub}.xml"
    if not p.exists():
        if not abruf:
            return None
        r = hole(f"https://ted.europa.eu/en/notice/{pub}/xml")
        if r.status_code != 200:
            print(f"  TED {pub}: HTTP {r.status_code}")
            return None
        XML10.mkdir(parents=True, exist_ok=True)
        p.write_bytes(r.content)  # unverändert
        time.sleep(0.5)
    for e in ET.fromstring(p.read_bytes()).iter():
        if _local(e.tag) == "ID" and e.get("schemeName") == "notice-id":
            return (e.text or "").strip()
    return None


def vw_tender(vid: str, abruf: bool) -> dict | None:
    ok, nf = VW / f"tender_{vid}.json", VW / f"tender_{vid}.404"
    if ok.exists():
        return json.loads(ok.read_text(encoding="utf-8"))
    if nf.exists() or not abruf:
        return None
    warte = PAUSE_VW - (time.time() - _letzte_vw[0])
    if warte > 0:
        time.sleep(warte)
    for _ in range(3):
        r = hole(f"{API}/tenders/{vid}", headers=HEADERS)
        _letzte_vw[0] = time.time()
        if r.status_code == 429:
            time.sleep(int(r.headers.get("Retry-After", "300")) + 5)
            continue
        break
    if r.status_code == 200:
        ok.write_bytes(r.content)  # unverändert
        return r.json()
    if r.status_code == 404:
        nf.write_text("404\n", encoding="utf-8")
    else:
        print(f"  Vergabeweiser {vid}: HTTP {r.status_code}")
    return None


def vw_wert(t: dict) -> tuple[str, date | None]:
    if t.get("ends_on"):
        return "datum", date.fromisoformat(t["ends_on"][:10])
    if t.get("starts_on") and t.get("duration_months"):
        return "datum", a9.ende_nach(date.fromisoformat(t["starts_on"][:10]), int(t["duration_months"]))
    return "kein_wert", None


def korrekt(x: tuple[str, date | None], ref: tuple[str, date | None]) -> bool:
    if x[1] and ref[1]:
        return abs((x[1] - ref[1]).days) <= 1
    return not x[1] and not ref[1]


def vergleichswerte() -> tuple[dict, dict]:
    """Schlüssel und Vergleichswert je Los wie in auswertung_iteration9.main (ohne deren Bericht zu schreiben)."""
    with a9.SCHLUESSEL.open(encoding="utf-8") as f:
        schl = {r["N"]: r for r in csv.DictReader(f, delimiter=";")}
    ant = {l: {} for l in "ab"}
    for l in "ab":
        for k in range(1, a9.N_TEILE + 1):
            ant[l].update(a9.lese_tsv(a9.ROH / f"leser_{l}_teil{k}.tsv"))
    ent = a9.lese_csv(a9.ENTSCHEIDE)
    v = {}
    for n in schl:
        ga, gb = a9.ende_gl(ant["a"][n]), a9.ende_gl(ant["b"][n])
        e = ent.get(n)
        v[n] = {"ntg": "nicht_tagesgenau" in (ga[0], gb[0]),
                "gl": ga if a9.gleich(ga, gb) else (a9.kat_wert(e["gl"]) if e and e["gl"].strip() else ("unklar", None))}
    return schl, v


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    abruf = "--abruf" in sys.argv
    schl, v = vergleichswerte()
    z = [n for n in schl if schl[n]["gruppe"] == "Z" and not v[n]["ntg"]]

    zuord, vidx = {}, verfahrensindex()
    for pub in sorted({schl[n]["notice"] for n in z}):
        refs, folder, eigen = referenzen(pub)
        info = {"refs": refs, "vid": None, "tender": None, "weg": None}
        kandidaten = [(1, ref, None) for ref in refs] + [(2, None, ni) for ni in vidx.get(folder, [])] + ([(3, None, eigen)] if eigen else [])
        for weg, ref, nid in kandidaten:
            nid = nid or notice_id(ref, abruf)
            if nid and (t := vw_tender(nid[:8], abruf)):
                info.update(vid=nid[:8], tender=t, weg=weg)
                break
        zuord[pub] = info
        print(f"{pub}: Wege {[k[0] for k in kandidaten]} → {info['vid'] or 'nicht gefunden'} (Weg {info['weg']})")

    if abruf:
        for name, q in (("bayern", "branche=gebaeudereinigung&land=bayern&monate=36"), ("deutschland", "branche=gebaeudereinigung&monate=36")):
            p = VW / f"expiring_gebaeudereinigung_{name}_36.json"
            if not p.exists():
                time.sleep(max(0, PAUSE_VW - (time.time() - _letzte_vw[0])))
                r = hole(f"{API}/expiring?{q}", headers=HEADERS)
                _letzte_vw[0] = time.time()
                if r.status_code == 200:
                    p.write_bytes(r.content)

    # Enden je Los in der eigenen Liste (W3)
    enden = defaultdict(set)
    with LISTE.open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f, delimiter=";"):
            enden[r["notice"]].add(r["gl_ende"] or "–")

    zeilen, gem = [], []
    for n in z:
        pub, ref = schl[n]["notice"], v[n]["gl"]
        liste = a9.liste_gl(schl[n])
        t = zuord[pub]["tender"]
        w = vw_wert(t) if t else ("nicht_gefunden", None)
        zeilen.append({"N": n, "notice": pub, "ref": ref, "liste": liste, "vw": w, "gefunden": t is not None,
                       "ok_l": korrekt(liste, ref), "ok_w": t is not None and korrekt(w, ref),
                       "v1_l": a9.ok_gl(liste, ref), "v1_w": t is not None and a9.ok_gl(w, ref),
                       "lose_versch": len(enden[pub]) > 1, "vid": zuord[pub]["vid"]})
    gem = [r for r in zeilen if r["gefunden"]]
    kl, kw = sum(r["ok_l"] for r in gem), sum(r["ok_w"] for r in gem)
    d = kl - kw
    if len(gem) < 40:
        urteil = "nicht beurteilbar (weniger als 40 gemeinsame Lose)"
    else:
        urteil = "Vorteil" if d >= 5 else ("kein gesicherter Vorteil" if d >= 1 else "kein Vorteil")
    fehl_w = [r for r in gem if not r["ok_w"]]

    def fmt(x):
        return x[1].strftime("%d.%m.%Y") if x[1] else x[0]

    out = ["# Vergleich mit Vergabeweiser (Iteration 10, W1 bis W4)", "",
           "_Erzeugt mit `src/prepare/vergleich_iteration10.py`. Kriterien vorab in `docs/iterationen.md` (Iteration 10). Vergleichswert unverändert aus Iteration 9. "
           "Daten von Vergabeweiser: CC BY 4.0, Quelle „Vergabeweiser“ (vergabeweiser.de), Abruf 2026-11-05, Rohdaten unverändert in `data/raw/vergabeweiser_20261105/`._", "",
           "## Fakten", "",
           f"- Z-Lose (ohne „nicht tagesgenau“): {len(z)} aus {len(zuord)} Bekanntmachungen.",
           f"- **W2 Abdeckung:** Vergabeweiser hat einen Eintrag für {len(gem)}/{len(z)} Lose ({a9.pct(len(gem), len(z))}); Bekanntmachungen gefunden "
           f"{sum(1 for i in zuord.values() if i['vid'])}/{len(zuord)} (über Weg 1/2/3: {sum(i['weg'] == 1 for i in zuord.values())}/"
           f"{sum(i['weg'] == 2 for i in zuord.values())}/{sum(i['weg'] == 3 for i in zuord.values())}).",
           f"- **W1 (gemeinsame Lose, {len(gem)}):** Liste {kl}/{len(gem)}, Vergabeweiser {kw}/{len(gem)}, **Vorsprung der Liste {d:+d} Lose → {urteil}.**",
           f"  Zählung wie V1: Liste {sum(r['v1_l'] for r in gem)}/{len(gem)}, Vergabeweiser {sum(r['v1_w'] for r in gem)}/{len(gem)}.",
           f"- W1 auf allen {len(z)} Losen („nicht gefunden“ = Fehltreffer): Liste {sum(r['ok_l'] for r in zeilen)}/{len(z)}, Vergabeweiser {sum(r['ok_w'] for r in zeilen)}/{len(z)}.",
           f"- Nur Vergabeweiser richtig: {', '.join(r['N'] for r in gem if r['ok_w'] and not r['ok_l']) or '–'}; nur Liste richtig: {', '.join(r['N'] for r in gem if r['ok_l'] and not r['ok_w']) or '–'}.",
           f"- **W3:** Von {len(fehl_w)} Fehltreffern von Vergabeweiser stammen {sum(r['lose_versch'] for r in fehl_w)} aus Bekanntmachungen, deren Lose in der eigenen Liste unterschiedliche Enden haben."]
    for name in ("bayern", "deutschland"):
        p = VW / f"expiring_gebaeudereinigung_{name}_36.json"
        if p.exists():
            e = json.loads(p.read_text(encoding="utf-8"))
            res = e.get("results") or []
            res = res if isinstance(res, list) else []
            out.append(f"- **W4 ({name.capitalize()}):** total {e.get('total')} auslaufende Verträge in 36 Monaten; von den gelieferten {len(res)} (früheste zuerst) "
                       f"sind {sum(1 for x in res if not x.get('eu'))} nicht EU-weit; Enden {res[0]['expected_end'] if res else '–'} bis {res[-1]['expected_end'] if res else '–'}.")
    out += ["", "## Je Los", "", "| N | Bekanntmachung | Vergleichswert | Liste | Vergabeweiser | Liste ok | VW ok | Lose mit versch. Enden | VW-ID |", "|---|---|---|---|---|---|---|---|---|"]
    out += [f"| {r['N']} | {r['notice']} | {fmt(r['ref'])} | {fmt(r['liste'])} | {fmt(r['vw'])} | {'ja' if r['ok_l'] else 'nein'} | {'ja' if r['ok_w'] else 'nein'} | "
            f"{'ja' if r['lose_versch'] else 'nein'} | {r['vid'] or '–'} |" for r in zeilen]
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"gemeinsam {len(gem)}/{len(z)}; Liste {kl}, VW {kw}, Vorsprung {d:+d} → {urteil}; {REPORT}")


if __name__ == "__main__":
    main()
