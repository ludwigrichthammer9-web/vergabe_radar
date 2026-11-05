"""Paket A (Nachtrag zu Iteration 10): Wettbewerbsbild der 130 Lose der Oberpfalz-Liste aus TED-Daten.

Frage: Welche der Felder, für die die Gespräche (docs/business.md §8.9) Zahlungsbereitschaft zeigten (aktueller Auftragnehmer,
alte Preise, Bieterzahl), lassen sich für die 130 Lose von reports/beispiel_liste_oberpfalz.csv (64 Bekanntmachungen) aus TED
ergänzen, wie vollständig und wie plausibel?

Aufruf (Projektordner, Windows):
    .venv\\Scripts\\python.exe -I src/prepare/wettbewerbsbild_oberpfalz.py            # lädt fehlende XML nach, rechnet, schreibt Berichte
    .venv\\Scripts\\python.exe -I src/prepare/wettbewerbsbild_oberpfalz.py --offline  # lädt nichts nach (alle XML müssen lokal liegen)

Eingaben
- reports/beispiel_liste_oberpfalz.csv (130 Lose, 64 Bekanntmachungen; Nenner aller Anteile fest 130)
- TED-XML (eForms): lokal unter data/raw/ted_xml/** (9 + 1 Dateien); fehlende werden nach
  data/raw/ted_xml/wettbewerbsbild_20261105/ geladen (https://ted.europa.eu/en/notice/<Nr>/xml, Pause 1,2 s, 4 Versuche).
  Rohdaten werden nie überschrieben.
- Gegenprobe (nicht Quelle): data/raw/ted_search/zielgruppe_oberpfalz_20261023/page_0001.json (winner-name)
  und data/raw/ted_search/DEU_result_cpv909_20231025_20260930_lostext (tender-value, total-value).

Felder in eForms-XML (Struktur an echten Dateien geprüft, siehe Bericht):
- Los:        cac:ProcurementProjectLot / cbc:ID[@schemeName='Lot'] (Los n der Liste = n-tes Los nach sortierter Kennung,
              wie in src/prepare/vertragsliste.py, Regel 7; Titelvergleich als Kontrolle)
- Ergebnis:   efac:NoticeResult / efac:LotResult (TenderResultCode, ReceivedSubmissionsStatistics, TenderLot/ID, LotTender/ID,
              HigherTenderAmount, LowerTenderAmount)
- Gebot:      efac:NoticeResult / efac:LotTender (LegalMonetaryTotal/PayableAmount = Wert des Zuschlagsangebots, TenderingParty/ID,
              TenderLot/ID, FieldsPrivacy)
- Bieter:     efac:TenderingParty / efac:Tenderer / cbc:ID -> efac:Organization / efac:Company (PartyName, CompanySizeCode)
- Zahl der Angebote: efbc:StatisticsCode 'tenders' (Liste received-submission-type), efbc:StatisticsNumeric
- Gesamtwert der Bekanntmachung: efac:NoticeResult / cbc:TotalAmount (wird NICHT auf Lose verteilt)

Ausgabe: reports/wettbewerbsbild_oberpfalz.csv und reports/wettbewerbsbild_oberpfalz.md
"""

import csv
import glob
import json
import os
import random
import re
import statistics
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LISTE = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
XML_ROOT = ROOT / "data" / "raw" / "ted_xml"
XML_NEU = XML_ROOT / "wettbewerbsbild_20261105"
SEARCH_ZIEL = ROOT / "data" / "raw" / "ted_search" / "zielgruppe_oberpfalz_20261023"
SEARCH_LOSTEXT = ROOT / "data" / "raw" / "ted_search" / "DEU_result_cpv909_20231025_20260930_lostext"
OUT_CSV = ROOT / "reports" / "wettbewerbsbild_oberpfalz.csv"
OUT_MD = ROOT / "reports" / "wettbewerbsbild_oberpfalz.md"

SEED_HAND = 20261113      # vorab festgelegt: random.Random(20261113).sample(sorted(Lose-Schlüssel), 5)
N_HAND = 5
SEED_BLATT = 20261114     # Auswahl der 3 Beispiel-Lose fürs Wettbewerbsblatt (nur beschreibend), s. u.
NENNER = 130
PLATZHALTER_MAX = 1.0     # Werte <= 1 EUR gelten als Platzhalter (wie src/auftragswerte.py)

NS = {
    "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
    "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
    "efac": "http://data.europa.eu/p27/eforms-ubl-extension-aggregate-components/1",
    "efbc": "http://data.europa.eu/p27/eforms-ubl-extension-basic-components/1",
    "efext": "http://data.europa.eu/p27/eforms-ubl-extensions/1",
    "ext": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
}

# Ergebnis des Handabgleichs (nach dem Ziehen der 5 Lose von Hand in der Bekanntmachung gelesen und hier eingetragen).
# Schlüssel = "<Bekanntmachung>|<Los>"; Wert = (Ergebnis, Begründung). Das Skript prüft, dass genau die per Seed gezogenen Lose stehen.
HANDABGLEICH: dict[str, tuple[str, str]] = {
    "446124-2025|001": ("stimmt", "LOT-0001, Titel gleich; Gewinner Wackler Service Group GmbH & Co. KG; PayableAmount = 1 (Platzhalter, als solcher ausgewiesen); tenders = 5."),
    "143100-2026|014": ("stimmt", "LOT-0014; Gewinner Krätschmer Gebäudereinigung + Dienstleistungs-GmbH; PayableAmount = -1 mit FieldsPrivacy win-ten-val (Wert nicht veröffentlicht); tenders = 1. "
                                  "Einschränkung: Lostitel „Nordbayern“ kommt mehrfach vor, die Zuordnung Los 14 = LOT-0014 beruht nur auf der Nummer."),
    "354636-2026|001": ("stimmt", "LOT-0001, Titel gleich; Gewinner Götz-Gebäudemanagement RSL GmbH; PayableAmount = -1 mit win-ten-val; tenders = 8, davon t-esubm nur 2 (t-esubm ist also nicht die Gesamtzahl)."),
    "687086-2025|004": ("stimmt", "LOT-0004, Titel gleich; Gewinner Albert Gebäudereinigung (Name am TenderingParty); PayableAmount = 811.772,64 €; tenders = 6."),
    "143100-2026|008": ("stimmt", "LOT-0008; Gewinner Krätschmer Gebäudereinigung + Dienstleistungs-GmbH; PayableAmount = -1 mit win-ten-val; tenders = 2. Lostitel „Nordbayern“ nicht eindeutig (wie Los 14)."),
}
HANDABGLEICH_QUELLE = ("Verglichen wurde mit dem Rohtext der Bekanntmachung (eForms-XML von ted.europa.eu/en/notice/<Nr>/xml, von Hand mit Textsuche gelesen, nicht mit dem Parser des Skripts). "
                       "Die verlinkte HTML-Seite (ted.europa.eu/de/notice/-/detail/<Nr>) liefert beim Abruf ohne Browser keinen Inhalt (Seite wird per JavaScript aufgebaut); "
                       "der Abgleich gegen die Browseransicht steht deshalb aus.")


# ----------------------------------------------------------------------------------------------------------------- Laden

def key_of(notice: str, los: str) -> str:
    return f"{notice}|{int(los):03d}"


def lade_liste() -> list[dict]:
    with open(LISTE, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def xml_pfade(notices: list[str]) -> dict[str, Path]:
    pfade: dict[str, Path] = {}
    for p in glob.glob(str(XML_ROOT / "**" / "*.xml"), recursive=True):
        n = os.path.basename(p)[:-4]
        if n in notices and n not in pfade:
            pfade[n] = Path(p)
    return pfade


def lade_nach(fehlend: list[str]) -> None:
    XML_NEU.mkdir(parents=True, exist_ok=True)
    for n in fehlend:
        for versuch in range(4):
            try:
                req = urllib.request.Request(f"https://ted.europa.eu/en/notice/{n}/xml",
                                             headers={"User-Agent": "vergabe-radar-student-project"})
                daten = urllib.request.urlopen(req, timeout=60).read()
                (XML_NEU / f"{n}.xml").write_bytes(daten)
                print(f"geladen {n} ({len(daten)} Byte)")
                break
            except Exception as e:  # Verbindungsfehler: Pause und Wiederholung
                print(f"Fehler {n} (Versuch {versuch + 1}): {e}")
                time.sleep(3)
        time.sleep(1.2)


# ----------------------------------------------------------------------------------------------------------------- Parsen

def txt(e, pfad):
    x = e.find(pfad, NS)
    return x.text.strip() if x is not None and x.text else None


def zahl(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def parse_notice(pfad: Path) -> dict:
    root = ET.parse(pfad).getroot()
    # Organisationen
    orgs = {}
    for o in root.iter(f"{{{NS['efac']}}}Organization"):
        c = o.find("efac:Company", NS)
        if c is None:
            continue
        oid = txt(c, "cac:PartyIdentification/cbc:ID")
        orgs[oid] = {"name": txt(c, "cac:PartyName/cbc:Name"), "groesse": txt(c, "efbc:CompanySizeCode"),
                     "stadt": txt(c, "cac:PostalAddress/cbc:CityName")}
    # Lose (Dokumentreihenfolge, danach sortiert nach Kennung)
    lose = {}
    for pl in root.findall("cac:ProcurementProjectLot", NS):
        lid = txt(pl, "cbc:ID")
        if lid and lid.startswith("LOT"):
            lose[lid] = txt(pl, "cac:ProcurementProject/cbc:Name") or ""
    nr = root.find(".//efac:NoticeResult", NS)
    res = {"lose": lose, "orgs": orgs, "gesamt": None, "lot_results": [], "tenders": {}, "parties": {}, "contracts": {}}
    if nr is None:
        return res
    ta = nr.find("cbc:TotalAmount", NS)
    res["gesamt"] = zahl(ta.text) if ta is not None else None
    # Gebote (Top-Ebene)
    for lt in nr.findall("efac:LotTender", NS):
        tid = txt(lt, "cbc:ID")
        priv = [txt(p, "efbc:FieldIdentifierCode") for p in lt.findall("efac:FieldsPrivacy", NS)]
        res["tenders"][tid] = {
            "wert": zahl(txt(lt, "cac:LegalMonetaryTotal/cbc:PayableAmount")),
            "wert_roh": txt(lt, "cac:LegalMonetaryTotal/cbc:PayableAmount"),
            "party": txt(lt, "efac:TenderingParty/cbc:ID"),
            "lose": [x.text.strip() for x in lt.findall("efac:TenderLot/cbc:ID", NS)],
            "privacy": priv,
        }
    for tp in nr.findall("efac:TenderingParty", NS):
        pid = txt(tp, "cbc:ID")
        res["parties"][pid] = {"tenderer": [(txt(t, "cbc:ID"), txt(t, "efbc:GroupLeadIndicator")) for t in tp.findall("efac:Tenderer", NS)],
                               "name": txt(tp, "cbc:Name")}
    for sc in nr.findall("efac:SettledContract", NS):
        res["contracts"][txt(sc, "cbc:ID")] = [txt(x, "cbc:ID") for x in sc.findall("efac:LotTender", NS)]
    # Ergebnisse je Los
    for lr in nr.findall("efac:LotResult", NS):
        stat = {}
        for s in lr.findall("efac:ReceivedSubmissionsStatistics", NS):
            stat[txt(s, "efbc:StatisticsCode")] = txt(s, "efbc:StatisticsNumeric")
        res["lot_results"].append({
            "lot": txt(lr, "efac:TenderLot/cbc:ID"),
            "status": txt(lr, "cbc:TenderResultCode"),
            "tenders": [txt(x, "cbc:ID") for x in lr.findall("efac:LotTender", NS)],
            "stat": stat,
            "hoechst": zahl(txt(lr, "cbc:HigherTenderAmount")),
            "niedrig": zahl(txt(lr, "cbc:LowerTenderAmount")),
            "rahmen": txt(lr, "efac:FrameworkAgreementValues/efbc:MaximumValueAmount") or txt(lr, "efac:FrameworkAgreementValues/efbc:ReestimatedValueAmount"),
            "grund": txt(lr, "efac:DecisionReason/efbc:DecisionReasonCode"),
        })
    return res


def norm(s: str) -> str:
    return re.sub(r"\W+", " ", (s or "").lower()).strip()


def name_von_party(n: dict, pid: str) -> tuple[list[str], list[str]]:
    namen, groessen = [], []
    party = n["parties"].get(pid, {"tenderer": [], "name": None})
    for oid, _lead in party["tenderer"]:
        o = n["orgs"].get(oid, {})
        namen.append(o.get("name") or f"({oid} ohne Namen)")
        groessen.append(o.get("groesse") or "")
    if not namen and party["name"]:       # Rückfall: Name am TenderingParty (kommt in einzelnen Bekanntmachungen vor)
        namen.append(party["name"])
        groessen.append("")
    return namen, groessen


# ----------------------------------------------------------------------------------------------------------------- Zeile bauen

def baue_zeile(r: dict, n: dict | None) -> dict:
    z = {
        "schluessel": key_of(r["notice"], r["los"]), "notice": r["notice"], "ted_link": r["ted_link"],
        "veroeffentlicht": r["veroeffentlicht"], "auftraggeber": r["auftraggeber"], "los": int(r["los"]), "los_titel_liste": r["los_titel"],
        "beginn": r["beginn"], "vertragsende_gl": r["gl_ende"], "vertragsende_herkunft": r["gl_herkunft"],
        "hoechstende": r["hoechstende"], "status_liste": r["status"], "stufe": r["stufe"],
    }
    leer = dict(xml_vorhanden=False, los_zugeordnet="", los_titel_xml="", titel_stimmt="", titel_eindeutig="", ergebnis_status="", gewinner="", gewinner_zahl=0,
                bietergemeinschaft="", mehrfachgewinner="", gewinner_groesse="", wert_eur="", wert_status="", wert_gemeinsam_mehrere_lose="",
                wert_zurueckgehalten="", gesamtwert_bekanntmachung="", angebote="", angebote_status="", angebote_elektronisch="", angebote_kmu="", spanne_status="",
                niedrigstes_angebot="", hoechstes_angebot="", vertrag_mehrere_gebote="", bemerkung="")
    z.update(leer)
    if n is None:
        z["bemerkung"] = "keine XML-Datei"
        return z
    z["xml_vorhanden"] = True
    kennungen = sorted(n["lose"])
    idx = int(r["los"]) - 1
    if idx >= len(kennungen):
        z["bemerkung"] = f"Los {r['los']} nicht in XML ({len(kennungen)} Lose)"
        return z
    lid = kennungen[idx]
    z["los_zugeordnet"] = lid
    z["los_titel_xml"] = n["lose"][lid]
    a, b = norm(r["los_titel"])[:40], norm(n["lose"][lid])[:40]
    z["titel_stimmt"] = bool(a) and (a == b or a in norm(n["lose"][lid]) or b in norm(r["los_titel"]))
    z["titel_eindeutig"] = sum(1 for t in n["lose"].values() if norm(t)[:40] == b) == 1
    lrs = [x for x in n["lot_results"] if x["lot"] == lid]
    if n["gesamt"] is not None:
        z["gesamtwert_bekanntmachung"] = n["gesamt"]
    if not lrs:
        z["bemerkung"] = "kein LotResult zum Los"
        z["wert_status"] = "fehlt"
        z["angebote_status"] = "fehlt"
        return z
    lr = lrs[0]
    z["ergebnis_status"] = lr["status"] or ""
    # Angebote
    st = lr["stat"].get("tenders")
    es = zahl(lr["stat"].get("t-esubm"))
    if es is not None and es >= 0:
        z["angebote_elektronisch"] = int(es)
    if st is None and es is not None and es >= 0:
        z["angebote_status"] = "nur_elektronisch"   # nur t-esubm angegeben: Untergrenze, nicht die Gesamtzahl
    elif st is None:
        z["angebote_status"] = "fehlt"
    else:
        v = zahl(st)
        if v is None or v < 0:
            z["angebote_status"] = "platzhalter"   # z. B. -1 = keine Angabe
            z["angebote"] = st
        else:
            z["angebote_status"] = "angegeben" if v >= 1 else "null"
            z["angebote"] = int(v)
    km = zahl(lr["stat"].get("t-sme"))
    if km is not None and km >= 0:
        z["angebote_kmu"] = int(km)
    if lr["niedrig"] is None and lr["hoechst"] is None:
        z["spanne_status"] = "fehlt"
    elif (lr["niedrig"] or 0) > PLATZHALTER_MAX and (lr["hoechst"] or 0) > PLATZHALTER_MAX:
        z["spanne_status"] = "angegeben"
        z["niedrigstes_angebot"] = lr["niedrig"]
        z["hoechstes_angebot"] = lr["hoechst"]
    else:
        z["spanne_status"] = "platzhalter"
    # Gewinner und Wert je Gebot
    tids = lr["tenders"]
    z["gewinner_zahl"] = len(tids)
    namen_alle, groessen, werte, priv, gemeinsam, vertr_mehr = [], [], [], False, False, False
    bg = False
    for tid in tids:
        t = n["tenders"].get(tid)
        if not t:
            continue
        nm, gr = name_von_party(n, t["party"])
        if len(nm) > 1:
            bg = True
        namen_alle.append(" // ".join(nm))
        groessen.append("/".join(sorted(set(x for x in gr if x))))
        werte.append((t["wert"], t["wert_roh"]))
        if t["privacy"] and any(p in ("win-ten-val", "tender-value") for p in t["privacy"]):
            priv = True
        if len(t["lose"]) > 1:
            gemeinsam = True
        for ids in n["contracts"].values():
            if tid in ids and len(ids) > 1:
                vertr_mehr = True
    z["gewinner"] = " | ".join(namen_alle)
    z["gewinner_groesse"] = " | ".join(groessen)
    z["bietergemeinschaft"] = bg if tids else ""
    z["mehrfachgewinner"] = len(tids) > 1 if tids else ""
    z["wert_gemeinsam_mehrere_lose"] = gemeinsam if tids else ""
    z["wert_zurueckgehalten"] = priv if tids else ""
    z["vertrag_mehrere_gebote"] = vertr_mehr if tids else ""
    # Wert: nur wenn genau ein Gewinnergebot, sonst Summe nicht zulässig -> je Gebot ausweisen
    echte = [w for w, _ in werte if w is not None and w > PLATZHALTER_MAX]
    plat = [w for w, roh in werte if w is not None and w <= PLATZHALTER_MAX]
    if not tids:
        z["wert_status"] = "kein_gewinnergebot"
    elif gemeinsam:
        z["wert_status"] = "gemeinsam_mehrere_lose"
        z["wert_eur"] = ""
    elif len(werte) > 1 and echte:
        z["wert_status"] = "angegeben_mehrere_gewinner"
        z["wert_eur"] = " | ".join(f"{w:.2f}" for w, _ in werte if w is not None)
    elif echte:
        z["wert_status"] = "angegeben"
        z["wert_eur"] = echte[0]
    elif plat:
        z["wert_status"] = "platzhalter"
        z["wert_eur"] = plat[0]
    else:
        z["wert_status"] = "fehlt"
    return z


# ----------------------------------------------------------------------------------------------------------------- Gegenproben

def lade_gegenproben(notices: set[str]) -> tuple[dict, dict]:
    winner = {}
    if SEARCH_ZIEL.exists():
        for f in sorted(SEARCH_ZIEL.glob("page_*.json")):
            for x in json.load(open(f, encoding="utf-8"))["notices"]:
                pn = x["publication-number"]
                if pn in notices:
                    w = x.get("winner-name") or {}
                    winner[pn] = sorted({norm(s) for v in w.values() for s in (v if isinstance(v, list) else [v])})
    werte = {}
    if SEARCH_LOSTEXT.exists():
        for f in sorted(SEARCH_LOSTEXT.glob("page_*.json")):
            for x in json.load(open(f, encoding="utf-8"))["notices"]:
                pn = x["publication-number"]
                if pn in notices:
                    def liste(v):
                        v = v if isinstance(v, list) else ([] if v is None else [v])
                        return [zahl(str(i)) for i in v]
                    werte[pn] = {"tender": liste(x.get("tender-value")), "total": liste(x.get("total-value"))}
    return winner, werte


# ----------------------------------------------------------------------------------------------------------------- Auswertung

def anteil(k: int) -> str:
    return f"{k} von {NENNER} ({100 * k / NENNER:.1f} %)".replace(".", ",")


def eur(x) -> str:
    return f"{x:,.0f} €".replace(",", ".")


def hauptlauf(offline: bool) -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    liste = lade_liste()
    assert len(liste) == NENNER, len(liste)
    notices = sorted({r["notice"] for r in liste})
    pfade = xml_pfade(notices)
    fehlend = [n for n in notices if n not in pfade]
    if fehlend and not offline:
        lade_nach(fehlend)
        pfade = xml_pfade(notices)
    parsed = {n: parse_notice(p) for n, p in pfade.items()}
    zeilen = [baue_zeile(r, parsed.get(r["notice"])) for r in liste]
    zeilen.sort(key=lambda z: z["schluessel"])
    # Handabgleich: Ziehung vorab festgelegt
    schluessel = sorted(z["schluessel"] for z in zeilen)
    hand = random.Random(SEED_HAND).sample(schluessel, N_HAND)
    for z in zeilen:
        z["handabgleich"] = "ja" if z["schluessel"] in hand else ""
    if HANDABGLEICH:
        assert set(HANDABGLEICH) == set(hand), (sorted(HANDABGLEICH), sorted(hand))
    for z in zeilen:
        if z["schluessel"] in HANDABGLEICH:
            z["handabgleich"] = HANDABGLEICH[z["schluessel"]][0]
    # CSV
    felder = ["schluessel", "notice", "ted_link", "veroeffentlicht", "auftraggeber", "los", "los_titel_liste", "los_zugeordnet", "los_titel_xml",
              "titel_stimmt", "titel_eindeutig", "ergebnis_status", "gewinner", "gewinner_zahl", "bietergemeinschaft", "mehrfachgewinner", "gewinner_groesse",
              "wert_eur", "wert_status", "wert_gemeinsam_mehrere_lose", "wert_zurueckgehalten", "gesamtwert_bekanntmachung",
              "vertrag_mehrere_gebote", "angebote", "angebote_status", "angebote_elektronisch", "angebote_kmu", "spanne_status", "niedrigstes_angebot", "hoechstes_angebot",
              "beginn", "vertragsende_gl", "vertragsende_herkunft", "hoechstende", "status_liste", "stufe", "xml_vorhanden", "handabgleich",
              "bemerkung"]
    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=felder, delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(zeilen)
    gp_winner, gp_werte = lade_gegenproben(set(notices))
    schreibe_bericht(zeilen, parsed, hand, gp_winner, gp_werte, fehlend, pfade)
    print(f"geschrieben: {OUT_CSV.name}, {OUT_MD.name}; Handabgleich-Lose: {hand}")


def schreibe_bericht(zeilen, parsed, hand, gp_winner, gp_werte, fehlend, pfade) -> None:
    L = lambda f: sum(1 for z in zeilen if f(z))  # noqa: E731
    mit_xml = L(lambda z: z["xml_vorhanden"])
    zugeordnet = L(lambda z: z["los_zugeordnet"] != "")
    titel_ok = L(lambda z: z["titel_stimmt"] is True)
    zuschlag = L(lambda z: z["ergebnis_status"] == "selec-w")
    status_cnt = Counter(z["ergebnis_status"] or "(kein LotResult/keine XML)" for z in zeilen)
    mit_name = L(lambda z: z["gewinner"] != "" and z["gewinner_zahl"] >= 1)
    ein_gew = L(lambda z: z["gewinner_zahl"] == 1 and z["gewinner"] != "")
    mehr_gew = L(lambda z: z["gewinner_zahl"] > 1)
    bg = L(lambda z: z["bietergemeinschaft"] is True)
    ws = Counter(z["wert_status"] or "(keine XML)" for z in zeilen)
    zur = L(lambda z: z["wert_zurueckgehalten"] is True)
    wert_ok = ws["angegeben"]
    ang = Counter(z["angebote_status"] or "(keine XML)" for z in zeilen)
    spanne = L(lambda z: z["spanne_status"] == "angegeben")
    spanne_pl = L(lambda z: z["spanne_status"] == "platzhalter")
    nur_el = L(lambda z: z["angebote_status"] == "nur_elektronisch")
    ang_untergrenze = L(lambda z: z["angebote_status"] in ("angegeben", "nur_elektronisch"))
    vollstaendig = L(lambda z: z["gewinner_zahl"] == 1 and z["gewinner"] and z["wert_status"] == "angegeben" and z["angebote_status"] == "angegeben")
    gl = L(lambda z: z["vertragsende_gl"] != "")
    nur_gesamt = L(lambda z: z["wert_status"] in ("fehlt", "platzhalter", "gemeinsam_mehrere_lose") and z["gesamtwert_bekanntmachung"] not in ("", None)
                   and z["gesamtwert_bekanntmachung"] > PLATZHALTER_MAX)
    # Plausibilität
    jahres = []
    for z in zeilen:
        if z["wert_status"] == "angegeben" and z["beginn"] and z["vertragsende_gl"]:
            try:
                b, e = date.fromisoformat(z["beginn"]), date.fromisoformat(z["vertragsende_gl"])
                mon = (e - b).days / 30.4375
                if mon >= 1:
                    jahres.append((z["wert_eur"] / mon * 12, z["schluessel"], mon))
            except ValueError:
                pass
    wert_vals = sorted(z["wert_eur"] for z in zeilen if z["wert_status"] == "angegeben")
    # Gleicher Wert in mehreren Losen derselben Bekanntmachung
    je_notice = defaultdict(list)
    for z in zeilen:
        if z["wert_status"] == "angegeben":
            je_notice[z["notice"]].append(z["wert_eur"])
    gleich = sorted(n for n, v in je_notice.items() if len(v) > 1 and len(set(v)) < len(v))
    # Wert = Gesamtwert der Bekanntmachung bei mehreren Losen
    gleich_gesamt = sorted(z["schluessel"] for z in zeilen if z["wert_status"] == "angegeben" and z["gesamtwert_bekanntmachung"] not in ("", None)
                           and abs(z["wert_eur"] - z["gesamtwert_bekanntmachung"]) < 0.5 and sum(1 for y in zeilen if y["notice"] == z["notice"]) > 1)
    # Angebot-Spanne: Gewinnerwert innerhalb [niedrig, hoch]?
    in_span = out_span = 0
    for z in zeilen:
        if z["wert_status"] == "angegeben" and z["niedrigstes_angebot"] != "" and z["hoechstes_angebot"] != "":
            if z["niedrigstes_angebot"] - 0.5 <= z["wert_eur"] <= z["hoechstes_angebot"] + 0.5:
                in_span += 1
            else:
                out_span += 1
    # Gegenprobe Gewinnernamen (Suche vs. XML) je Bekanntmachung
    gp_ok = gp_ab = gp_fehlt = 0
    gp_abw = []
    for n in sorted(parsed):
        d = parsed[n]
        xml_namen = set()           # alle Gewinner der ganzen Bekanntmachung (die Suche liefert alle Lose, nicht nur die der Liste)
        for lr in d["lot_results"]:
            for tid in lr["tenders"]:
                t = d["tenders"].get(tid)
                if t:
                    nm, _ = name_von_party(d, t["party"])
                    xml_namen.update(norm(x) for x in nm)
        sn = set(gp_winner.get(n, []))
        if not sn:
            gp_fehlt += 1
        elif sn == xml_namen:
            gp_ok += 1
        else:
            gp_ab += 1
            gp_abw.append(n)
    # Gegenprobe Werte (nur Gebotswerte > 1 €)
    gw_ok = gw_ab = gw_nodata = 0
    gw_abw = []
    for n in sorted(parsed):
        xml_w = sorted(round(parsed[n]["tenders"][tid]["wert"], 2) for lr in parsed[n]["lot_results"] for tid in lr["tenders"]
                       if tid in parsed[n]["tenders"] and (parsed[n]["tenders"][tid]["wert"] or 0) > PLATZHALTER_MAX)   # ganze Bekanntmachung
        s = gp_werte.get(n, {})
        sw = sorted(round(v, 2) for v in s.get("tender", []) if v is not None and v > PLATZHALTER_MAX)
        if not xml_w and not sw:
            gw_nodata += 1
        elif all(v in sw for v in xml_w) and all(v in xml_w for v in sw):
            gw_ok += 1
        else:
            gw_ab += 1
            gw_abw.append(f"{n} (XML {xml_w[:4]} / Suche {sw[:4]})")
    # nach Jahr
    jahr = defaultdict(lambda: Counter())
    for z in zeilen:
        y = z["veroeffentlicht"][:4]
        jahr[y]["lose"] += 1
        jahr[y]["gew"] += 1 if (z["gewinner_zahl"] == 1 and z["gewinner"]) else 0
        jahr[y]["wert"] += 1 if z["wert_status"] == "angegeben" else 0
        jahr[y]["ang"] += 1 if z["angebote_status"] == "angegeben" else 0
        jahr[y]["esub"] += 1 if z["angebote_status"] == "nur_elektronisch" else 0
    # Beispielblatt: 3 Lose mit allen drei Feldern, per Seed gezogen
    voll = sorted(z["schluessel"] for z in zeilen if z["gewinner_zahl"] == 1 and z["gewinner"] and z["wert_status"] == "angegeben" and z["angebote_status"] == "angegeben")
    blatt = random.Random(SEED_BLATT).sample(voll, 3) if len(voll) >= 3 else voll
    byk = {z["schluessel"]: z for z in zeilen}
    # Wiederholte Gewinner
    gewinner_ct = Counter()
    for z in zeilen:
        if z["gewinner_zahl"] == 1 and z["gewinner"]:
            gewinner_ct[z["gewinner"]] += 1

    o = []
    P = o.append
    P("# Wettbewerbsbild der 130 Oberpfalz-Lose aus TED (Paket A)\n")
    P("_Erzeugt von `src/prepare/wettbewerbsbild_oberpfalz.py` (Aufruf im Kopf des Skripts). Zahlen stammen aus der zugehörigen CSV `reports/wettbewerbsbild_oberpfalz.csv`. "
      "Nachtrag zu Iteration 10; Fakten (mit Quelle) und Deutung sind getrennt. Nenner aller Anteile fest 130 Lose._\n")
    P("## 1. Frage und Vorgehen\n")
    P("**Frage (Fakt, Quelle `docs/business.md` §8.9):** In den drei Gesprächen zeigte sich Zahlungsbereitschaft nur für Wettbewerbsdaten (aktueller Auftragnehmer, alte Preise, Bieterzahl), "
      "nicht für Enddaten. Welche dieser Felder lassen sich für die 130 Lose der Liste `reports/beispiel_liste_oberpfalz.csv` (64 Bekanntmachungen) aus TED ergänzen, wie vollständig und wie plausibel?\n")
    P("**Vorgehen (Fakt):**\n")
    P(f"- Quelle ist das eForms-XML der Zuschlagsbekanntmachung. {len(pfade) - len(fehlend) if fehlend else len(pfade)} der 64 Dateien lagen lokal bzw. wurden in diesem Lauf vorgefunden; "
      f"{len(fehlend)} wurden in diesem Lauf nach `data/raw/ted_xml/wettbewerbsbild_20261105/` nachgeladen (Pause 1,2 s). Rohdaten blieben unverändert.")
    P("- Zuordnung Los der Liste zum Los der Bekanntmachung: n-tes Los nach sortierter Kennung (wie `src/prepare/vertragsliste.py`, Regel 7), Kontrolle über den Lostitel.")
    P("- Felder: Gewinner = `efac:LotResult/efac:LotTender` → `efac:TenderingParty` → `efac:Tenderer` → `efac:Organization` (Name, Größe). "
      "Wert = `efac:LotTender/cac:LegalMonetaryTotal/cbc:PayableAmount` (Wert des Gewinnerangebots, BT-720). "
      "Zahl der Angebote = `efac:ReceivedSubmissionsStatistics` mit Code `tenders` (BT-759). Zusätzlich `cbc:HigherTenderAmount`/`cbc:LowerTenderAmount` (teuerstes/billigstes Angebot) und `cbc:TotalAmount` (Gesamtwert der Bekanntmachung, wird nicht auf Lose verteilt).")
    P("- Werte ≤ 1 € gelten als Platzhalter und werden getrennt ausgewiesen (wie `src/auftragswerte.py`). Hat ein Gewinnerangebot mehrere Lose (`TenderLot`), wird der Wert nicht einem Los zugeteilt.")
    P("- Gegenproben (nicht Quelle): Gewinnernamen und Gebotswerte der Suchabfragen `zielgruppe_oberpfalz_20261023` und `DEU_result_cpv909_20231025_20260930_lostext`.\n")

    P("## 2. Ergebnis: Anteil der 130 Lose je Feld (Fakten)\n")
    P("Quelle: `reports/wettbewerbsbild_oberpfalz.csv`, Spalten in Klammern. Nenner fest 130.\n")
    P("| Feld | Anteil der 130 Lose | Anmerkung |")
    P("|---|---|---|")
    P(f"| Bekanntmachung als XML vorhanden (`xml_vorhanden`) | {anteil(mit_xml)} | |")
    P(f"| Los der Liste einem Los im XML zugeordnet (`los_zugeordnet`) | {anteil(zugeordnet)} | |")
    P(f"| … Lostitel stimmt überein (`titel_stimmt`, Kontrolle) | {anteil(titel_ok)} | Vergleich der ersten 40 Zeichen, normalisiert |")
    P(f"| … davon Lostitel im XML eindeutig (`titel_eindeutig`) | {anteil(L(lambda z: z['titel_eindeutig'] is True))} | Bei den übrigen kommt derselbe Titel in mehreren Losen vor; dort trägt nur die Nummer die Zuordnung |")
    P(f"| Zuschlag erteilt (`ergebnis_status` = selec-w) | {anteil(zuschlag)} | Status: " + ", ".join(f"{k}: {v}" for k, v in status_cnt.most_common()) + " |")
    P(f"| **Auftragnehmer genannt** (`gewinner`) | {anteil(mit_name)} | |")
    P(f"| … davon genau ein Gewinnerangebot je Los | {anteil(ein_gew)} | |")
    P(f"| … davon mehrere Gewinner je Los (Mehrfachgewinner, `mehrfachgewinner`) | {anteil(mehr_gew)} | Rahmenvereinbarung mit mehreren Partnern o. ä.; Werte werden je Gebot ausgewiesen |")
    P(f"| … davon Bietergemeinschaft als Gewinner (`bietergemeinschaft`) | {anteil(bg)} | Mitglieder mit „ // “ verbunden |")
    P(f"| **Zuschlagswert je Los > 1 €** (`wert_status` = angegeben) | {anteil(wert_ok)} | |")
    P(f"| … nur Platzhalter ≤ 1 € (`platzhalter`) | {anteil(ws['platzhalter'])} | getrennt, nicht als Wert gezählt |")
    P(f"| … Wert fehlt im Gewinnerangebot (`fehlt`) | {anteil(ws['fehlt'])} | |")
    P(f"| … Wert gilt für mehrere Lose zusammen (`gemeinsam_mehrere_lose`) | {anteil(ws['gemeinsam_mehrere_lose'])} | nicht je Los zugeteilt |")
    P(f"| … mehrere Gewinner mit Werten (`angegeben_mehrere_gewinner`) | {anteil(ws['angegeben_mehrere_gewinner'])} | Werte je Gebot in der CSV, nicht summiert |")
    P(f"| … ohne Gewinnerangebot (`kein_gewinnergebot`) / ohne XML | {anteil(ws['kein_gewinnergebot'] + ws['(keine XML)'])} | |")
    P(f"| Wert als „nicht veröffentlicht“ gekennzeichnet (`wert_zurueckgehalten`, FieldsPrivacy `win-ten-val`) | {anteil(zur)} | Auftraggeber hat die Veröffentlichung des Zuschlagswerts ausdrücklich ausgesetzt; kann zusätzlich zu einem Platzhalter auftreten |")
    P(f"| Nur Gesamtwert der Bekanntmachung bekannt, Los-Wert fehlt (`gesamtwert_bekanntmachung` > 1 €) | {anteil(nur_gesamt)} | Gesamtwert wird nicht auf Lose verteilt |")
    P(f"| **Zahl der Angebote angegeben, ≥ 1** (`angebote_status` = angegeben) | {anteil(ang['angegeben'])} | |")
    P(f"| … Angabe 0 (`null`) | {anteil(ang['null'])} | |")
    P(f"| … Platzhalter/negativ (`platzhalter`) | {anteil(ang['platzhalter'])} | |")
    P(f"| … nur „elektronisch eingegangene Angebote“ angegeben (Code `t-esubm`, `nur_elektronisch`) | {anteil(nur_el)} | Gesamtzahl fehlt; Zahl ist Untergrenze, nicht in der Zeile darüber gezählt |")
    P(f"| … Zahl der Angebote nach Gesamtzahl oder Untergrenze (Summe der beiden Zeilen) | {anteil(ang_untergrenze)} | |")
    P(f"| … gar keine Angabe | {anteil(ang['fehlt'])} | |")
    P(f"| Preisspanne der Angebote (billigstes/teuerstes, > 1 €; `spanne_status` = angegeben) | {anteil(spanne)} | Zusatzfeld (BT-710/711); Platzhalter (0 u. ä.) in {spanne_pl} Losen |")
    P(f"| **Alle drei Felder je Los vorhanden** (genau ein Gewinner, Wert > 1 €, Angebote ≥ 1) | {anteil(vollstaendig)} | |")
    vollst2 = L(lambda z: z["gewinner_zahl"] == 1 and z["gewinner"] and z["wert_status"] == "angegeben" and z["angebote_status"] in ("angegeben", "nur_elektronisch"))
    P(f"| … dasselbe, wenn die Untergrenze (nur elektronische Angebote) als Bieterzahl genügt | {anteil(vollst2)} | |")
    P(f"| Vertragsende aus der Liste (`vertragsende_gl`) | {anteil(gl)} | Stufe F = ohne Ende; Herkunft in `vertragsende_herkunft` |")
    P("")
    P("Aufteilung nach Veröffentlichungsjahr (Fakt; Lose / genau ein Gewinner / Wert > 1 € / Gesamtzahl der Angebote / nur elektronische Angebote):\n")
    P("| Jahr | Lose | Auftragnehmer | Wert | Angebote (Gesamt) | nur elektronisch |")
    P("|---|---|---|---|---|---|")
    for y in sorted(jahr):
        c = jahr[y]
        P(f"| {y} | {c['lose']} | {c['gew']} | {c['wert']} | {c['ang']} | {c['esub']} |")
    P("")

    P("## 3. Plausibilität (Fakten)\n")
    P(f"- **Gewinnernamen gegen die Suchabfrage** (`winner-name` in `zielgruppe_oberpfalz_20261023`), je Bekanntmachung: identische Namensmenge (alle Gewinner der Bekanntmachung) in {gp_ok}, abweichend in {gp_ab}, in der Suche ohne Namen in {gp_fehlt} von {len(parsed)} Bekanntmachungen."
      + (f" Abweichungen: {', '.join(gp_abw)}." if gp_abw else ""))
    P(f"- **Gebotswerte gegen die Suchabfrage** (`tender-value` in `DEU_result_cpv909_…_lostext`), je Bekanntmachung (alle Lose der Bekanntmachung), nur Werte > 1 €: gleich in {gw_ok}, abweichend in {gw_ab}, beide ohne Wert in {gw_nodata} von {len(parsed)}."
      + (f" Abweichungen: {'; '.join(gw_abw[:8])}." if gw_abw else ""))
    if wert_vals:
        P(f"- **Verteilung der angegebenen Zuschlagswerte (je Los, n = {len(wert_vals)}):** kleinster {eur(wert_vals[0])}, Median {eur(statistics.median(wert_vals))}, größter {eur(wert_vals[-1])}.")
    if jahres:
        js = sorted(j[0] for j in jahres)
        P(f"- **Jahreswert** (Zuschlagswert geteilt durch Dauer von Beginn bis Ende der Grundlaufzeit aus der Liste, mal 12; n = {len(js)}): "
          f"kleinster {eur(js[0])}, Median {eur(statistics.median(js))}, größter {eur(js[-1])}. Nur eine Größenordnungsprüfung: "
          "der Zuschlagswert kann die Option mit enthalten (dann ist der Jahreswert zu klein), die Dauer stammt aus der Liste (Stufe C/F möglich).")
    P(f"- **Wert innerhalb der Preisspanne der Angebote** (billigstes bis teuerstes Angebot, soweit beide angegeben): {in_span} Lose innerhalb, {out_span} außerhalb.")
    P(f"- **Gleicher Wert in mehreren Losen derselben Bekanntmachung** (Verdacht auf eingetragenen Gesamtwert): Bekanntmachungen {', '.join(gleich) if gleich else 'keine'}.")
    P(f"- **Los-Wert gleich dem Gesamtwert der Bekanntmachung bei mehreren Losen der Liste:** {len(gleich_gesamt)} Lose" + (f" ({', '.join(gleich_gesamt[:6])})." if gleich_gesamt else "."))
    P(f"- **Gleicher Auftragnehmer in mehreren Losen** (genau ein Gewinner): {sum(1 for v in gewinner_ct.values() if v > 1)} Namen kommen mehrfach vor, häufigster {gewinner_ct.most_common(1)[0][1] if gewinner_ct else 0} Lose.")
    P("")

    P("## 4. Handabgleich von 5 Losen mit der verlinkten Bekanntmachung\n")
    P(f"**Ziehung (vorab im Skript festgelegt):** `random.Random({SEED_HAND}).sample(sorted(Lose-Schlüssel), {N_HAND})`, Schlüssel = `<Bekanntmachung>|<Los dreistellig>` (Spalte `schluessel` der CSV), sortiert als Zeichenkette über alle {NENNER} Lose.\n")
    P("| Schlüssel | Auftragnehmer (Skript) | Wert (Skript) | Angebote (Skript) | Ergebnis Handabgleich | Grund |")
    P("|---|---|---|---|---|---|")
    for k in hand:
        z = byk[k]
        res, grund = HANDABGLEICH.get(k, ("(noch nicht eingetragen)", ""))
        wert = z["wert_eur"] if z["wert_eur"] != "" else f"({z['wert_status']})"
        P(f"| [{z['notice']} Los {z['los']}]({z['ted_link']}) | {z['gewinner'] or '(keiner)'} | {wert} | {z['angebote'] if z['angebote'] != '' else '(' + z['angebote_status'] + ')'} | {res} | {grund} |")
    P("")
    P("**Quelle des Vergleichs und Grenze:** " + HANDABGLEICH_QUELLE)
    P("")
    P("**Ergebnis:** " + f"{sum(1 for v in HANDABGLEICH.values() if v[0] == 'stimmt')} von {N_HAND} Losen stimmen (Auslesen und Zuordnung); die Platzhalter und die Zurückhaltung des Werts wurden am Rohtext ebenfalls so gefunden.")
    P("")

    P("## 5. Beispiel-Wettbewerbsblatt für 3 Lose (beschreibend)\n")
    P(f"Auswahl: drei Lose mit allen drei Feldern, per `random.Random({SEED_BLATT}).sample` aus den {len(voll)} vollständigen Losen gezogen (nicht handverlesen). "
      "So könnte ein Eintrag aussehen; die Angaben stammen aus den verlinkten Bekanntmachungen.\n")
    for k in blatt:
        z = byk[k]
        P(f"**{z['auftraggeber']}, {z['los_titel_liste']}** ([{z['notice']}, Los {z['los']}]({z['ted_link']}))\n")
        P(f"- Aktueller Auftragnehmer: {z['gewinner']} (Größe laut Bekanntmachung: {z['gewinner_groesse'] or 'keine Angabe'})")
        P(f"- Zuschlagswert: {eur(z['wert_eur'])}" + (f" (Spanne der Angebote {eur(z['niedrigstes_angebot'])} bis {eur(z['hoechstes_angebot'])})" if z['niedrigstes_angebot'] != '' and z['hoechstes_angebot'] != '' else ""))
        P(f"- Zahl der Angebote: {z['angebote']}" + (f", davon von KMU {z['angebote_kmu']}" if z['angebote_kmu'] != '' else ""))
        P(f"- Vertragsende (Grundlaufzeit): {z['vertragsende_gl'] or 'keine Angabe'} (Herkunft: {z['vertragsende_herkunft'] or '–'}); Höchstende nur Hinweis: {z['hoechstende'] or '–'}\n")

    P("## 6. Was Vergabeweiser schon zeigt und welche Lücken bleiben\n")
    P("**Fakten (Quelle `docs/business.md` §8.2, Tabelle, dort als „geprüft“ markiert, die API von Vergabeweiser wurde für diesen Bericht nicht aufgerufen):** "
      "Vergabeweiser zeigt je auslaufendem Vertrag Zuschlagsempfänger, Zahl der Angebote und Verlängerungsoptionen, dazu Erinnerung per E-Mail, ober- und unterschwellig, kostenlos; "
      "für Gebäudereinigung 1.005 von 10.265 Verträgen mit Ende in 12 Monaten. Nach §8.9 (Interpretation des Nutzers) zeigt Vergabeweiser auch Zuschlagssummen; das ist in §8.2 nicht belegt. "
      "AusschreibungsRadar nennt Zuschlagsempfänger und Wettbewerber-Tracking (§8.9). Einordnung in §8.4 Punkt 1.\n")
    P("**Deutung (nicht belegt, aus dem Vergleich):**\n")
    P("- Auftragnehmer und Bieterzahl sind damit **kein Alleinstellungsmerkmal**: Was TED hier liefert, bietet Vergabeweiser nach eigener Darstellung ohnehin kostenlos.")
    P("- Ein Vorsprung bliebe nur bei Feldern, die dort nicht stehen oder nicht je Los/Jahr aufbereitet sind: Zuschlagswert je Los und Jahreswert, Preisspanne der Angebote (billigstes/teuerstes), Größe/KMU-Anteil der Bieter, Mehrfachgewinner und Bietergemeinschaften. "
      "Ob Vergabeweiser diese Felder zeigt, wurde hier nicht geprüft (API nicht aufgerufen, Seite nicht ausgewertet).")
    P("- Bleibende Lücken unseres Wettbewerbsbildes: nur TED (oberhalb der EU-Schwelle), nur eForms-Zuschläge ab Oktober 2023, daher fehlen die Vorgänger der Neuausschreibungen der nächsten Jahre (`docs/business.md` §8.4 Punkt 3); "
      "Werte teils zurückgehalten oder Platzhalter (siehe Abschnitt 2); der Zuschlagswert kann Optionen einschließen; Bieterzahl ist die Zahl der eingegangenen Angebote, nicht der Bieter mit gültigem Angebot.\n")

    P("## 7. Grenzen\n")
    P("- Stichprobe ist die Oberpfalz-Liste (130 Lose, Region-Auswahl, Nische Gebäudereinigung), nicht der Markt; die Anteile gelten für diese Liste, nicht für Deutschland.")
    P("- Die Liste enthält nur Lose mit eForms-Zuschlag; ältere Bekanntmachungen haben ein anderes Format und sind nicht enthalten.")
    P("- Die Zuordnung Los der Liste zu Los im XML beruht auf Reihenfolge und Titelkontrolle (siehe `titel_stimmt`); bei abweichendem Titel ist die Zuordnung unsicher.")
    P("- Der Handabgleich (5 Lose) ist ein Stichprobenbeleg, kein Beleg für alle 130 Lose. Er prüft Auslesen und Zuordnung gegen die Bekanntmachung, nicht, ob die Angaben der Vergabestelle selbst stimmen.")
    P("- Keine Aussage über Zahlungsbereitschaft: Dass die Felder vorhanden sind, belegt keine Nachfrage (A15 bleibt ungeprüft; n = 3 Gespräche sind Hinweise).")
    OUT_MD.write_text("\n".join(o) + "\n", encoding="utf-8")


if __name__ == "__main__":
    hauptlauf("--offline" in sys.argv)
