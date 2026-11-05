"""Iteration 10b: Vergleich Liste gegen Vergabeweiser auf der größeren Stichprobe (160 Lose, Seed 20261112).

Kriterien, Begriffe und Schwellen sind vorab in docs/iterationen.md (Iteration 10b) festgelegt und werden hier nicht geändert:
- Zuordnung zu Vergabeweiser und Wert je Los wie in Iteration 10 (src/prepare/vergleich_iteration10.py: Wege 1, 2, 3; ends_on, sonst Beginn + Dauer − 1 Tag).
- Diskordantes Los: Vergabeweiser hat einen Eintrag und (Datum weicht um mehr als einen Tag von der Liste ab oder eine Seite hat kein Datum).
  Lose ohne Eintrag bei Vergabeweiser sind nicht diskordant (W10, Abdeckung), sie gehen in W8 nicht ein (wie die „gemeinsamen Lose“ in Iteration 10).
- Ursachenklassen (je diskordantem Los eine, in dieser Reihenfolge geprüft):
  (c) eine Seite ohne Datum; (a) Datum von Vergabeweiser = Ende (gl_ende, ± 1 Tag) eines anderen Loses derselben Bekanntmachung in der Liste (vertragsliste_909.csv);
  (b) Datum von Vergabeweiser = Höchstende der Liste (± 1 Tag), oder `renewals` ≥ 1 und Datum von Vergabeweiser später als das Ende der Liste + 5 Tage;
  (d) Abweichung 2 bis 5 Tage; (e) andere.
- W8a/W8b: erst nach dem Vergleichswert der Leser (Modus --ergebnis). Vergleichswert wie Iteration 9 (neutrale Definition aus src/prepare/auswertung_iteration9.py,
  deren Funktionen hier wiederverwendet werden): stimmen Leser A und B überein, gilt der Wert, sonst die Entscheidung des Evaluators, sonst „unklar“.
  Treffer (Liste und Vergabeweiser gleich): Datum = Vergleichswert ± 1 Tag, oder beide ohne Datum (wie Iteration 10). „nicht tagesgenau“ nimmt das Los aus der Zählung.
  W8a: (nur Liste richtig) − (nur Vergabeweiser richtig) ≥ 16 Lose und exakter zweiseitiger McNemar-Test p < 0,05.
  W8b: wie W8a, aber Vergabeweiser gilt auch bei Klasse (a) als richtig; ≥ 8 Lose und p < 0,05.
  Lose, in denen Liste und Vergabeweiser übereinstimmen („beide gleich“), gehen in die Differenz nicht ein.

Eingaben (Pfade relativ zu ROOT; für Tests mit der Umgebungsvariable VR10B_BASIS auf einen anderen Basisordner umstellbar, der data/ und reports/ enthält):
  data/processed/stichprobe_iteration10b_schluessel.csv   Schlüssel (Prüfgeheimnis, Listenwerte nie an Leser weitergeben)
  data/processed/vertragsliste_909.csv                    Liste (Fassung 9)
  data/raw/ted_xml/iteration10b_20261105/<Nr>.xml         TED-XML (--abruf lädt fehlende; vorhandene Dateien aus Iteration 9 und 10 werden mitgenutzt)
  data/raw/vergabeweiser_20261105/tender_<id>.json|.404   Rohantworten von Vergabeweiser (unverändert, gemeinsam mit Iteration 10)
  reports/vergleich_iteration10b_roh/leser_{a,b}_teil*.tsv  Antworten der Leser (nur --ergebnis)
  reports/vergleich_iteration10b_entscheide.csv           N;gl;… Entscheidung des Evaluators bei Uneinigkeit (nur --ergebnis)
  reports/vergleich_iteration10b_mensch.csv               optional, N;ende_gl (Kommilitone, beschreibend)

Aufruf:  .venv\\Scripts\\python -I src/prepare/vergleich_iteration10b.py --abruf      lädt fehlende Daten (höchstens 1 Vergabeweiser-Abfrage je 61 s), wertet dann aus
         .venv\\Scripts\\python -I src/prepare/vergleich_iteration10b.py              wertet nur aus den gespeicherten Rohdaten aus
         .venv\\Scripts\\python -I src/prepare/vergleich_iteration10b.py --status     zeigt, wie viele Abfragen noch fehlen (kein Netz)
         .venv\\Scripts\\python -I src/prepare/vergleich_iteration10b.py --ergebnis   W8a/W8b nach dem Vergleichswert der Leser
Ausgabe: reports/vergleich_iteration10b.md, reports/vergleich_iteration10b_diskordant.csv (N;notice;los, ohne Werte), data/processed/vergleich_iteration10b_voll.csv (lokal, mit Werten)
"""

import csv
import hashlib
import math
import os
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auswertung_iteration9 as a9  # noqa: E402  (Vergleichswert und Hilfsfunktionen unverändert wiederverwenden)
import vergleich_iteration10 as v10  # noqa: E402  (Zuordnung und Wert von Vergabeweiser unverändert wiederverwenden)

ROOT = Path(os.environ.get("VR10B_BASIS") or Path(__file__).resolve().parent.parent.parent)
PROC, R = ROOT / "data" / "processed", ROOT / "reports"
SCHLUESSEL = PROC / "stichprobe_iteration10b_schluessel.csv"
SHA_ERWARTET = "2cd0020634582a77e46155375cb655db9f0bc04f186bc5e6bbc6b446633a6e33"  # aus dem Commit 9d63c59
LISTE = PROC / "vertragsliste_909.csv"
XML10B = ROOT / "data" / "raw" / "ted_xml" / "iteration10b_20261105"
XML_LESEN = [XML10B, ROOT / "data" / "raw" / "ted_xml" / "iteration9_20261105", ROOT / "data" / "raw" / "ted_xml" / "vergleich_iteration10", ROOT / "data" / "raw" / "ted_xml"]
VW = ROOT / "data" / "raw" / "vergabeweiser_20261105"
ROH = R / "vergleich_iteration10b_roh"
ENTSCHEIDE = R / "vergleich_iteration10b_entscheide.csv"
MENSCH = R / "vergleich_iteration10b_mensch.csv"
REPORT = R / "vergleich_iteration10b.md"
DISKORDANT = R / "vergleich_iteration10b_diskordant.csv"
VOLL = PROC / "vergleich_iteration10b_voll.csv"
ROHSCHEMA = "leser_{}_teil*.tsv"
SCHWELLE_A, SCHWELLE_B, ALPHA = 16, 8, 0.05

# die Funktionen aus Iteration 10 greifen auf Modulvariablen zu; hier auf die Pfade dieses Laufs setzen (im echten Lauf identisch mit dem Repo)
v10.VW = VW
v10.ROOT = ROOT  # für verfahrensindex() (data/raw/ted_search)


def xml_pfad(nr: str) -> Path | None:
    for d in XML_LESEN:
        if (d / f"{nr}.xml").exists():
            return d / f"{nr}.xml"
    return None


def lade_xml(nr: str, abruf: bool) -> Path | None:
    """TED-XML der Bekanntmachung: lokal vorhanden oder (nur mit --abruf) unverändert nach XML10B geladen."""
    p = xml_pfad(nr)
    if p or not abruf:
        return p
    r = v10.hole(f"https://ted.europa.eu/en/notice/{nr}/xml")
    if r.status_code != 200:
        print(f"  TED {nr}: HTTP {r.status_code}")
        return None
    XML10B.mkdir(parents=True, exist_ok=True)
    (XML10B / f"{nr}.xml").write_bytes(r.content)  # unverändert
    time.sleep(1.0)
    return XML10B / f"{nr}.xml"


def referenzen_10b(pub: str, abruf: bool) -> tuple[list[str], str | None, str | None] | None:
    """Wie v10.referenzen, aber mit der TED-XML aus iteration10b_20261105 (oder einem anderen lokalen Ordner). None, wenn die XML fehlt."""
    p = lade_xml(pub, abruf)
    if not p:
        return None
    import re
    root = ET.fromstring(p.read_bytes())
    refs, folder, nid = [], None, None
    for e in root.iter():
        tag = v10._local(e.tag)
        if tag == "NoticeDocumentReference":
            for c in e:
                if v10._local(c.tag) == "ID" and re.fullmatch(r"\d+-\d{4}", (c.text or "").strip()):
                    refs.append(c.text.strip())
        elif tag == "ContractFolderID" and folder is None:
            folder = (e.text or "").strip()
        elif tag == "ID" and e.get("schemeName") == "notice-id" and nid is None:
            nid = (e.text or "").strip()
    return list(dict.fromkeys(refs)), folder, nid


def notice_id_10b(nr: str, abruf: bool) -> str | None:
    p = lade_xml(nr, abruf)
    if not p:
        return None
    for e in ET.fromstring(p.read_bytes()).iter():
        if v10._local(e.tag) == "ID" and e.get("schemeName") == "notice-id":
            return (e.text or "").strip()
    return None


class Vorlaeufig(Exception):
    """Abfrage ohne endgültige Antwort (Verbindungsfehler, 429, 5xx): nichts speichern, Zuordnung dieser Bekanntmachung beim nächsten Lauf neu versuchen."""


def tender(vid: str, abruf: bool) -> dict | None:
    t = None
    try:
        t = v10.vw_tender(vid, abruf)
    except requests.exceptions.RequestException as e:
        raise Vorlaeufig(str(e)) from e
    if t is None and abruf and not ((VW / f"tender_{vid}.json").exists() or (VW / f"tender_{vid}.404").exists()):
        raise Vorlaeufig(f"keine endgültige Antwort für {vid}")
    return t


def zuordnen(pubs: list[str], abruf: bool) -> dict[str, dict]:
    zuord, vidx = {}, v10.verfahrensindex()
    for pub in pubs:
        info = {"refs": [], "vid": None, "tender": None, "weg": None, "status": "ok"}
        try:
            rf = referenzen_10b(pub, abruf)
            if rf is None:
                info["status"] = "xml_fehlt"
                kandidaten = []
            else:
                refs, folder, eigen = rf
                kandidaten = [(1, ref, None) for ref in refs] + [(2, None, ni) for ni in vidx.get(folder, [])] + ([(3, None, eigen)] if eigen else [])
                for weg, ref, nid in kandidaten:
                    nid = nid or notice_id_10b(ref, abruf)
                    if nid and (t := tender(nid[:8], abruf)):
                        info.update(vid=nid[:8], tender=t, weg=weg)
                        break
        except Vorlaeufig as e:
            info["status"] = "vorlaeufig"
            print(f"  {pub}: vorläufig ({e}); beim nächsten Lauf mit --abruf erneut")
        zuord[pub] = info
        print(f"{pub}: {info['status']} → {info['vid'] or 'nicht gefunden'} (Weg {info['weg']})")
    return zuord


def status(pubs: list[str]) -> None:
    """Ohne Netz: wie viele TED-XML und Vergabeweiser-Abfragen fehlen mindestens noch."""
    vidx = v10.verfahrensindex()
    xml_fehlt, offen_ted, offen_vw, fertig_ok, fertig_nf = 0, 0, 0, 0, 0
    for pub in pubs:
        rf = referenzen_10b(pub, False)
        if rf is None:
            xml_fehlt += 1
            continue
        refs, folder, eigen = rf
        kand = [(1, ref, None) for ref in refs] + [(2, None, ni) for ni in vidx.get(folder, [])] + ([(3, None, eigen)] if eigen else [])
        gefunden, offen = False, False
        for weg, ref, nid in kand:
            if not nid:
                if not xml_pfad(ref):
                    offen_ted += 1
                    offen = True
                    break
                nid = notice_id_10b(ref, False)
            if not nid:
                continue
            if (VW / f"tender_{nid[:8]}.json").exists():
                gefunden = True
                break
            if not (VW / f"tender_{nid[:8]}.404").exists():
                offen = True
                offen_vw += 1
                break
        fertig_ok += gefunden
        fertig_nf += (not gefunden and not offen)
    print(f"Bekanntmachungen {len(pubs)}: TED-XML der Zuschlagsbekanntmachung fehlt bei {xml_fehlt}; fertig zugeordnet {fertig_ok}, fertig ohne Eintrag {fertig_nf}; "
          f"mit offener TED-XML eines Verweises {offen_ted}; mit offener Vergabeweiser-Abfrage {offen_vw} (mindestens je 1 Abfrage, je nach 404 mehr).")
    print(f"Untergrenze Vergabeweiser-Abfragen: {offen_vw} (≈ {offen_vw * 61 / 60:.0f} min); dazu {xml_fehlt + offen_ted} TED-XML (je ≥ 1 s) und die Abfragen nach 404-Antworten.")


def lies(p: Path, enc: str = "utf-8") -> list[dict]:
    with p.open(encoding=enc, newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def tage(a: date | None, b: date | None) -> int | None:
    return (a - b).days if a and b else None


def klasse(r: dict, andere_enden: list[date]) -> str:
    """Ursachenklasse eines diskordanten Loses (r: liste, vw, hoechstende, renewals)."""
    L, W = r["liste"][1], r["vw"][1]
    if not L or not W:
        return "c"
    if any(abs((W - e).days) <= 1 for e in andere_enden):
        return "a"
    if (r["hoechstende"] and abs((W - r["hoechstende"]).days) <= 1) or (r["renewals"] and r["renewals"] >= 1 and (W - L).days > 5):
        return "b"
    if 2 <= abs((W - L).days) <= 5:
        return "d"
    return "e"


def vergleichswerte_10b(schl: dict) -> tuple[dict, list[str]]:
    """Vergleichswert je Los aus den Antworten der Leser (Funktionen aus auswertung_iteration9). Rückgabe: Werte, Liste der noch offenen N."""
    ant = {}
    for l in "ab":
        ant[l] = {}
        for p in sorted(ROH.glob(ROHSCHEMA.format(l))):
            ant[l].update(a9.lese_tsv(p))
    ent = a9.lese_csv(ENTSCHEIDE)
    v, offen = {}, []
    for n in schl:
        if n not in ant["a"] or n not in ant["b"]:
            offen.append(n)
            continue
        ga, gb = a9.ende_gl(ant["a"][n]), a9.ende_gl(ant["b"][n])
        e = ent.get(n)
        ntg = "nicht_tagesgenau" in (ga[0], gb[0])
        einig = a9.gleich(ga, gb)
        v[n] = {"ntg": ntg, "einig": einig, "ga": ga, "gb": gb,
                "gl": ga if einig else (a9.kat_wert(e["gl"]) if e and e["gl"].strip() else ("unklar", None)),
                "kz": "ja" in (ant["a"][n]["kein_zuschlag"].lower(), ant["b"][n]["kein_zuschlag"].lower())}
        if not einig and not ntg and v[n]["gl"][0] == "unklar":
            offen.append(n)
    return v, offen


def mcnemar_exakt(b: int, c: int) -> float:
    """Exakter zweiseitiger McNemar-Test = zweiseitiger Binomialtest (p = 0,5) auf den b + c diskordanten Paaren (ohne scipy)."""
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    p = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * p)


def fmt(x: tuple[str, date | None]) -> str:
    return x[1].isoformat() if x[1] else x[0]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    abruf, ergebnis, nur_status = "--abruf" in sys.argv, "--ergebnis" in sys.argv, "--status" in sys.argv
    sha = hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()
    sha_ok = sha == SHA_ERWARTET
    if not sha_ok:
        print(f"WARNUNG: SHA-256 des Schlüssels weicht vom Commit ab ({sha[:8]}…{sha[-4:]}); Auswertung nur zu Testzwecken.")
    schl = {r["N"]: r for r in lies(SCHLUESSEL)}
    pubs = sorted({r["notice"] for r in schl.values()})
    if nur_status:
        status(pubs)
        return
    zuord = zuordnen(pubs, abruf)

    enden_je = defaultdict(dict)  # Bekanntmachung → Los → Ende der Liste
    with LISTE.open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f, delimiter=";"):
            d = a9.liste_gl(r)[1]
            if d:
                enden_je[r["notice"]][r["los"]] = d

    zeilen = []
    for n, s in schl.items():
        t = zuord[s["notice"]]["tender"]
        liste = a9.liste_gl(s)
        w = v10.vw_wert(t) if t else ("nicht_gefunden", None)
        hoe = a9.datum(".".join(reversed(s["hoechstende"].split("-")))) if s["hoechstende"] else None
        andere = [d for lo, d in enden_je[s["notice"]].items() if lo != s["los"]]
        rn = t.get("renewals") if t else None
        z = {"N": n, "notice": s["notice"], "los": s["los"], "weg": zuord[s["notice"]]["weg"], "vid": zuord[s["notice"]]["vid"], "status": zuord[s["notice"]]["status"],
             "gefunden": t is not None, "liste": liste, "vw": w, "hoechstende": hoe, "renewals": rn if isinstance(rn, int) else None, "gl_herkunft": s["gl_herkunft"]}
        z["diff"] = tage(w[1], liste[1])
        z["diskordant"] = z["gefunden"] and (liste[1] is None or w[1] is None or abs(z["diff"]) > 1)
        z["klasse"] = klasse(z, andere) if z["diskordant"] else ""
        zeilen.append(z)
    gem = [z for z in zeilen if z["gefunden"]]
    disk = [z for z in zeilen if z["diskordant"]]
    gleich_ = [z for z in gem if not z["diskordant"]]
    kl = Counter(z["klasse"] for z in disk)

    R.mkdir(parents=True, exist_ok=True)
    PROC.mkdir(parents=True, exist_ok=True)
    with DISKORDANT.open("w", encoding="utf-8", newline="") as f:
        w_ = csv.writer(f, delimiter=";")
        w_.writerow(["N", "notice", "los"])
        w_.writerows([z["N"], z["notice"], z["los"]] for z in disk)

    out = ["# Vergleich Liste gegen Vergabeweiser, größere Stichprobe (Iteration 10b)", "",
           "_Erzeugt mit `src/prepare/vergleich_iteration10b.py`. Kriterien vorab in `docs/iterationen.md` (Iteration 10b), Skript im Kopf mit den Definitionen. "
           f"Schlüssel-SHA-256 `{sha[:8]}…{sha[-4:]}` ({'stimmt mit dem Commit überein' if sha_ok else 'WEICHT AB'}). Daten von Vergabeweiser: CC BY 4.0, Quelle „Vergabeweiser“ (vergabeweiser.de), "
           "Abruf 2026-11-05 ff., Rohdaten unverändert in `data/raw/vergabeweiser_20261105/`. In diesem Bericht stehen keine Datumswerte je Los (Leser bleiben blind); sie stehen in "
           "`data/processed/vergleich_iteration10b_voll.csv` (lokal)._", "", "## Fakten", "",
           f"- Stichprobe: {len(schl)} Lose aus {len(pubs)} Bekanntmachungen.",
           f"- **W10 Abdeckung:** Vergabeweiser hat einen Eintrag für {len(gem)}/{len(schl)} Lose ({a9.pct(len(gem), len(schl))}); Bekanntmachungen zugeordnet "
           f"{sum(1 for i in zuord.values() if i['vid'])}/{len(pubs)} (Weg 1/2/3: {sum(i['weg'] == 1 for i in zuord.values())}/{sum(i['weg'] == 2 for i in zuord.values())}/"
           f"{sum(i['weg'] == 3 for i in zuord.values())}). Unvollständig (TED-XML fehlt oder Abfrage vorläufig): {sum(i['status'] != 'ok' for i in zuord.values())} Bekanntmachungen "
           f"({sum(1 for z in zeilen if z['status'] != 'ok')} Lose) – diese gelten bis zu einem erneuten Lauf als „kein Eintrag“.",
           f"- Von {len(gem)} Losen mit Eintrag: Liste und Vergabeweiser gleich (± 1 Tag) bei {len(gleich_)}; **diskordant {len(disk)}** (an die Leser: `reports/vergleich_iteration10b_diskordant.csv`).",
           f"- Art des Werts von Vergabeweiser bei Losen mit Eintrag: {dict(Counter(z['vw'][0] for z in gem))}.",
           f"- **W9 Ursachenverteilung der {len(disk)} diskordanten Lose:** " + (", ".join(f"({k}) {kl.get(k, 0)} = {100 * kl.get(k, 0) / len(disk):.1f} %".replace(".", ",") for k in "abcde") if disk else "–")
           + ". Klassen: (a) Losebene, (b) Höchstende bzw. `renewals`, (c) fehlendes Datum, (d) Abweichung 2 bis 5 Tage, (e) andere."]

    kopf = ["N", "notice", "los", "weg", "vid", "gefunden", "liste_ende", "liste_herkunft", "liste_hoechstende", "vw_art", "vw_datum", "vw_renewals", "diff_tage_vw_minus_liste", "diskordant", "klasse"]

    def zeile(z):
        return [z["N"], z["notice"], z["los"], z["weg"] or "", z["vid"] or "", int(z["gefunden"]), z["liste"][1] or "", z["gl_herkunft"], z["hoechstende"] or "", z["vw"][0],
                z["vw"][1] or "", "" if z["renewals"] is None else z["renewals"], "" if z["diff"] is None else z["diff"], int(z["diskordant"]), z["klasse"]]

    extra_kopf, extra = [], {}
    if ergebnis:
        v, offen = vergleichswerte_10b({z["N"]: schl[z["N"]] for z in disk})
        if offen:
            out += ["", f"**Noch offen:** Antworten der Leser oder Entscheidung des Evaluators fehlen für {', '.join(offen)}. W8a und W8b werden erst danach berechnet."]
            ergebnis = False
        else:
            ntg = [z for z in disk if v[z["N"]]["ntg"]]
            zaehl = [z for z in disk if not v[z["N"]]["ntg"]]
            for z in zaehl:
                ref = v[z["N"]]["gl"]
                z["ok_l"] = v10.korrekt(z["liste"], ref)
                z["ok_w"] = v10.korrekt(z["vw"], ref)
                z["ok_wb"] = z["ok_w"] or z["klasse"] == "a"
                extra[z["N"]] = [fmt(ref), int(z["ok_l"]), int(z["ok_w"]), int(z["ok_wb"])]
            extra_kopf = ["vergleichswert", "ok_liste", "ok_vw", "ok_vw_b"]

            def stat(ok_w_key: str) -> tuple[int, int, int, int, float]:
                nl = sum(1 for z in zaehl if z["ok_l"] and not z[ok_w_key])
                nw = sum(1 for z in zaehl if z[ok_w_key] and not z["ok_l"])
                beide = sum(1 for z in zaehl if z["ok_l"] and z[ok_w_key])
                keine = sum(1 for z in zaehl if not z["ok_l"] and not z[ok_w_key])
                return nl, nw, beide, keine, mcnemar_exakt(nl, nw)

            la, wa, ba, ka, pa = stat("ok_w")
            lb, wb, bb, kb, pb = stat("ok_wb")
            w8a = (la - wa) >= SCHWELLE_A and pa < ALPHA
            w8b = (lb - wb) >= SCHWELLE_B and pb < ALPHA
            p_ = lambda p: f"{p:.4f}".replace(".", ",")  # noqa: E731
            kz = [z["N"] for z in disk if v[z["N"]]["kz"]]
            einig = sum(v[z["N"]]["einig"] for z in disk)
            out += ["", "### Ergebnis nach dem Vergleichswert der Leser", "",
                    f"- Diskordante Lose {len(disk)}; davon „nicht tagesgenau“ (aus der Zählung genommen): {', '.join(z['N'] for z in ntg) or '–'}; gezählt {len(zaehl)}. "
                    f"Leser A = B beim Ende der Grundlaufzeit: {a9.pct(einig, len(disk))}; übrige Lose durch Evaluator entschieden. Lose mit „kein Zuschlag“ bei einem Leser: {', '.join(kz) or '–'}.",
                    "", "| | beide richtig | nur Liste richtig | nur Vergabeweiser richtig | beide falsch | Differenz (Liste − VW) | McNemar exakt p |", "|---|---|---|---|---|---|---|",
                    f"| W8a (Vergabeweiser wie gelesen) | {ba} | {la} | {wa} | {ka} | {la - wa:+d} | {p_(pa)} |",
                    f"| W8b (Klasse (a) zählt für Vergabeweiser als richtig) | {bb} | {lb} | {wb} | {kb} | {lb - wb:+d} | {p_(pb)} |", "",
                    f"- Treffer je Quelle gegen den Vergleichswert (diskordante Lose, n = {len(zaehl)}): Liste {sum(z['ok_l'] for z in zaehl)}, Vergabeweiser {sum(z['ok_w'] for z in zaehl)}, "
                    f"Vergabeweiser nach W8b {sum(z['ok_wb'] for z in zaehl)}.",
                    f"- **W8a:** Differenz {la - wa:+d} (Schwelle ≥ {SCHWELLE_A} = 10 % der Stichprobe), p = {p_(pa)} → **{'erfüllt' if w8a else 'verfehlt'}**.",
                    f"- **W8b:** Differenz {lb - wb:+d} (Schwelle ≥ {SCHWELLE_B} = 5 % der Stichprobe), p = {p_(pb)} → **{'erfüllt' if w8b else 'verfehlt'}**.",
                    f"- Ursachen der Fehltreffer von Vergabeweiser (diskordante, gezählte Lose): {dict(Counter(z['klasse'] for z in zaehl if not z['ok_w']))}; der Liste: "
                    f"{dict(Counter(z['klasse'] for z in zaehl if not z['ok_l']))}.",
                    f"- Nur Liste richtig: {', '.join(z['N'] for z in zaehl if z['ok_l'] and not z['ok_w']) or '–'}; nur Vergabeweiser richtig: {', '.join(z['N'] for z in zaehl if z['ok_w'] and not z['ok_l']) or '–'}."]
            if MENSCH.exists():
                m = a9.lese_csv(MENSCH)
                mn = [z["N"] for z in disk if z["N"] in m and not v[z["N"]]["ntg"]]
                out += [f"- Kommilitone (beschreibend): Eintrag = Vergleichswert bei {sum(a9.gleich(a9.kat_wert(m[n]['ende_gl']), v[n]['gl']) for n in mn)}/{len(mn)} Losen."]
            folge = ("W8a und W8b erfüllt: Vorsprung auf Losebene und über die Granularität hinaus belegt (zwei Stichproben)" if w8a and w8b else
                     "W8a erfüllt, W8b verfehlt: Vorsprung nur auf Losebene, nicht als Lesequalität belegt" if w8a else
                     "W8a verfehlt: kein belegter Vorteil, die Aussage „kein Vorteil gegenüber Vergabeweiser“ gilt weiter (mit Einschränkung der Stichprobengröße)")
            out += ["", "## Deutung (Interpretation, nicht Messung)", "", f"- Nach den vorab festgelegten Folgen: {folge}.",
                    "- Die Differenz stützt sich nur auf diskordante Lose und setzt voraus, dass bei übereinstimmenden Losen beide Quellen gleich liegen (vorab benannte Grenze). "
                    "Leser und Regeln stammen aus derselben Modellfamilie; die Wahl der Losebene in W8a ist nicht neutral, deshalb W8b.",
                    "- Lose ohne Eintrag bei Vergabeweiser (W10) gehen in W8 nicht ein; würde man sie als Fehltreffer von Vergabeweiser werten, wäre das ein anderes Maß (Abdeckung statt Genauigkeit)."]
    if not ergebnis:
        out += ["", "## Deutung (Interpretation, nicht Messung)", "",
                "- Erst nach dem Vergleichswert der Leser (Modus `--ergebnis`) lässt sich sagen, welche Quelle bei den diskordanten Losen richtig liegt. "
                "Die Ursachenverteilung zeigt nur, wie die Abweichungen zustande kommen, nicht wer recht hat (Klasse (a) und (b) sind Verdachtsfälle für Verfahrens- statt Losebene bzw. Höchstende)."]
    out += ["", "## Verfahren (W11, Hinweis)", "",
            "- Seed, Skript und Kriterien lagen vor dem Ziehen im Commit; Rohantworten von Vergabeweiser und TED-XML werden unverändert gespeichert. Abweichungen von der Vorab-Festlegung: keine; "
            "Festlegungen, die dort offen waren (Behandlung von Losen ohne Eintrag, Reihenfolge der Ursachenklassen, Schwelle „später als +5 Tage“ bei `renewals`), stehen im Kopf dieses Skripts."]

    with VOLL.open("w", encoding="utf-8", newline="") as f:
        w_ = csv.writer(f, delimiter=";")
        w_.writerow(kopf + extra_kopf)
        for z in zeilen:
            w_.writerow(zeile(z) + (extra.get(z["N"], [""] * len(extra_kopf)) if extra_kopf else []))
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Lose {len(schl)}, mit Eintrag {len(gem)}, diskordant {len(disk)} ({dict(kl)}); {REPORT}")


if __name__ == "__main__":
    main()
