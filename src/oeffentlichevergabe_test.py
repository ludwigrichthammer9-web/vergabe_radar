"""Paket B: Abdeckungstest unterhalb der EU-Schwelle (A3), Oberpfalz.

Kriterien B1 bis B5 stehen vorab in docs/iterationen.md (Abschnitt "Paket B ...").
Dieses Skript ändert keine bestehenden Dateien und ruft die Vergabeweiser-API nicht auf.

Aufruf (Projektwurzel, Windows):
    .venv\\Scripts\\python.exe -I src\\oeffentlichevergabe_test.py --download   # Jahresdateien 2024 bis 2026 laden (nur wenn nicht vorhanden)
    .venv\\Scripts\\python.exe -I src\\oeffentlichevergabe_test.py              # auswerten (liest die Dateien streamend, ca. 3 Minuten)

Quelle: OCDS-Jahresdateien des Bekanntmachungsservice (oeffentlichevergabe.de) bei der Open Contracting
Partnership, Veröffentlichung 136, Lizenz CC0 1.0: https://data.open-contracting.org/en/publication/136
Dateien: https://data.open-contracting.org/en/publication/136/download?name=<JAHR>.jsonl.gz
Rohdaten: data/raw/oeffentlichevergabe_20261105/<JAHR>.jsonl.gz (unverändert).

Ausgaben: reports/oeffentlichevergabe_test_los.csv (ein Los je Zeile) und Kennzahlen auf stdout.

EU/national-Regel (Setzung, Unsicherheit im Bericht): Der OCDS-Datensatz enthält kein Kennzeichen "oberhalb/unterhalb der
EU-Schwelle". Ein Verfahren gilt als EU (oberschwellig), wenn seine Verfahrenskennung (OCDS tender.id = UUID im ocid
= TED-Feld procedure-identifier, BT-04) in den gespeicherten TED-Abfragen (data/raw/ted_search) oder TED-XML
(data/raw/ted_xml, ContractFolderID) vorkommt, d. h. wenn es auf TED veröffentlicht wurde. Sonst gilt es als "national"
(nicht auf TED gefunden). Zusatzprüfung nur beschreibend: Auftragswert gegen die EU-Schwellenwerte.
"""
import argparse
import collections
import csv
import glob
import gzip
import json
import math
import random
import re
import shutil
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "oeffentlichevergabe_20261105"
JAHRE = (2024, 2025, 2026)
URL = "https://data.open-contracting.org/en/publication/136/download?name={y}.jsonl.gz"
OBERPFALZ = {"DE23" + c for c in "123456789A"}  # DE231 bis DE23A
CPV_PRAEFIX = ("90910", "90911", "90919")
SEED_B4 = 20261116
LISTE = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
OUT_CSV = ROOT / "reports" / "oeffentlichevergabe_test_los.csv"


# ---------------------------------------------------------------- Download
def download():
    frei = shutil.disk_usage(ROOT).free
    if frei < 3 * 1024**3:
        sys.exit(f"Abbruch: nur {frei / 1024**3:.1f} GB frei (weniger als 3 GB).")
    RAW.mkdir(parents=True, exist_ok=True)
    for y in JAHRE:
        ziel = RAW / f"{y}.jsonl.gz"
        if ziel.exists() and ziel.stat().st_size > 0:
            print(f"{y}: vorhanden ({ziel.stat().st_size / 1e6:.0f} MB), nicht überschrieben")
            continue
        for versuch in range(1, 6):
            try:
                req = urllib.request.Request(URL.format(y=y), headers={"User-Agent": "vergabe-radar-student-projekt"})
                tmp = ziel.with_suffix(".part")
                with urllib.request.urlopen(req, timeout=120) as r, open(tmp, "wb") as f:
                    shutil.copyfileobj(r, f, 1 << 20)  # streamend
                tmp.rename(ziel)
                print(f"{y}: geladen, {ziel.stat().st_size / 1e6:.0f} MB")
                break
            except Exception as e:  # Verbindungsfehler: warten und wiederholen
                print(f"{y}: Versuch {versuch} fehlgeschlagen: {e}")
                time.sleep(5 * versuch)
        else:
            sys.exit(f"nicht gelungen: {URL.format(y=y)}")
        time.sleep(1)


# ---------------------------------------------------------------- TED-Index
def ted_verfahren():
    """Verfahrenskennungen (procedure-identifier) aus den gespeicherten TED-Abfragen und TED-XML."""
    idx = {}
    for f in glob.glob(str(ROOT / "data" / "raw" / "ted_search" / "**" / "*.json"), recursive=True):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        for n in d.get("notices", []):
            p = n.get("procedure-identifier")
            if p:
                p = p if isinstance(p, str) else p[0]
                idx.setdefault(p, set()).add(n.get("publication-number"))
    for f in glob.glob(str(ROOT / "data" / "raw" / "ted_xml" / "*.xml")):
        try:
            for e in ET.parse(f).getroot().iter():
                if e.tag.rsplit("}", 1)[-1] == "ContractFolderID" and e.text:
                    idx.setdefault(e.text.strip(), set()).add(Path(f).stem)
                    break
        except Exception:
            continue
    return idx


def liste_kennungen(ted):
    """Die 64 Bekanntmachungen der Liste -> Verfahrenskennung (aus den gespeicherten TED-Abfragen)."""
    nums = {r["notice"] for r in csv.DictReader(open(LISTE, encoding="utf-8-sig"), delimiter=";")}
    m = {}
    for f in glob.glob(str(ROOT / "data" / "raw" / "ted_search" / "**" / "*.json"), recursive=True):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        for n in d.get("notices", []):
            if n.get("publication-number") in nums and n.get("procedure-identifier"):
                p = n["procedure-identifier"]
                m[n["publication-number"]] = p if isinstance(p, str) else p[0]
    return nums, m


# ---------------------------------------------------------------- Hilfsfunktionen
def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"),) * 2
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def pct(k, n):
    return f"{k}/{n} = {100 * k / n:.1f} %" if n else f"{k}/0"


def gueltig_betrag(x):
    return isinstance(x, (int, float)) and x > 1


def ende_vorhanden(lot):
    cp = (lot or {}).get("contractPeriod") or {}
    return bool(cp.get("endDate")), bool(cp.get("durationInDays")), bool(cp.get("endDate") or cp.get("durationInDays"))


def verfahrenswert(r):
    t = r.get("tender", {})
    v = (t.get("value") or {}).get("amount")
    if gueltig_betrag(v):
        return v, "tender.value"
    s = [(l.get("value") or {}).get("amount") for l in t.get("lots", [])]
    s = [x for x in s if gueltig_betrag(x)]
    if s:
        return sum(s), "Summe lots.value"
    s = [(a.get("value") or {}).get("amount") for a in r.get("awards", [])]
    s = [x for x in s if gueltig_betrag(x)]
    if s:
        return sum(s), "Summe awards.value"
    s = [(c.get("value") or {}).get("amount") for c in r.get("contracts", [])]
    s = [x for x in s if gueltig_betrag(x)]
    if s:
        return sum(s), "Summe contracts.value"
    return None, "kein Wert"


def treffer_items(r):
    """Positionen mit Haupt-CPV-Präfix 90910/90911/90919 und NUTS-3-Code der Oberpfalz (Lieferort der Position)."""
    out = []
    for i in r.get("tender", {}).get("items", []):
        cpv = str((i.get("classification") or {}).get("id", ""))
        reg = (i.get("deliveryAddress") or {}).get("region")
        if cpv.startswith(CPV_PRAEFIX) and reg in OBERPFALZ:
            out.append(i)
    return out


def verfahren_bauen(treffer, ted):
    verf = {}
    for y, r, its in treffer:
        uuid = r["ocid"][len("ocds-mnwr74-"):]
        eu = uuid in ted
        phase = "Zuschlag" if r.get("awards") else "Auftragsbekanntmachung"
        w, wq = verfahrenswert(r)
        verf[uuid] = dict(jahr=y, r=r, items=its, eu=eu, gruppe="EU" if eu else "national", phase=phase, wert=w, wertquelle=wq)
    return verf


def ted_nachpruefung(verf):
    """Verfahren ohne TED-Treffer im lokalen Index einzeln bei TED nachschlagen (Suche nach procedure-identifier, Pause 1 s).
    Grund: Die lokalen TED-Abfragen enden im Oktober 2026; jüngere Verfahren würden sonst fälschlich als national gelten."""
    ordner = RAW / "ted_nachpruefung"
    ordner.mkdir(exist_ok=True)
    for u, v in verf.items():
        if v["eu"]:
            continue
        f = ordner / f"{u}.json"
        if not f.exists():
            for versuch in range(1, 5):
                try:
                    body = json.dumps({"query": f"procedure-identifier={u}", "fields": ["publication-number", "publication-date", "notice-type"], "limit": 10}).encode()
                    req = urllib.request.Request("https://api.ted.europa.eu/v3/notices/search", data=body, headers={"Content-Type": "application/json"})
                    with urllib.request.urlopen(req, timeout=60) as r:
                        f.write_bytes(r.read())
                    break
                except Exception as e:
                    print("TED-Nachprüfung", u, "Versuch", versuch, e)
                    time.sleep(3 * versuch)
            time.sleep(1)
        if f.exists():
            nots = json.loads(f.read_text(encoding="utf-8")).get("notices", [])
            if nots:
                v["eu"] = True
                v["gruppe"] = "EU"
                v["ted_nachpruefung"] = [x.get("publication-number") for x in nots]
    print("TED-Nachprüfung: Verfahren ohne lokalen Treffer, nach Einzelabfrage bei TED doch auf TED:", sum(1 for v in verf.values() if v.get("ted_nachpruefung")))


# ---------------------------------------------------------------- Auswertung
def scan(ted, liste_proc):
    treffer, liste_gefunden, erweitert = [], {}, []
    zaehl = collections.Counter()
    weit = collections.Counter()  # Kontext: ganz Deutschland, ganzer Datensatz
    liste_set = set(liste_proc.values())
    for y in JAHRE:
        p = RAW / f"{y}.jsonl.gz"
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                zaehl[y] += 1
                m = re.match(r'\{"id": "ocds-mnwr74-([0-9a-f-]{36})', line)
                uuid = m.group(1) if m else None
                if uuid in liste_set:
                    liste_gefunden[uuid] = y
                if '"909' not in line:
                    continue
                r = json.loads(line)
                # Kontext: Haupt-CPV 909x0/1/9 bundesweit, Anteil ohne TED-Verfahrenskennung
                if any(str((i.get("classification") or {}).get("id", "")).startswith(CPV_PRAEFIX) for i in r.get("tender", {}).get("items", [])):
                    weit[("bundesweit", y, uuid in ted)] += 1
                    if r.get("date", "") < "2026-09-01":  # TED-Abfragen reichen bis Ende September/Oktober 2026
                        regs = {str((i.get("deliveryAddress") or {}).get("region", ""))[:3] for i in r["tender"]["items"]}
                        for reg in regs or {"ohne Ort"}:
                            weit[("nuts1", reg or "ohne Ort", uuid in ted)] += 1
                its = treffer_items(r)
                if not its:
                    # Erweiterung (nur Sensitivität): Position ohne Ortsangabe, aber Auftraggeber in der Oberpfalz
                    ohne = [i for i in r.get("tender", {}).get("items", [])
                            if str((i.get("classification") or {}).get("id", "")).startswith(CPV_PRAEFIX) and not (i.get("deliveryAddress") or {}).get("region")]
                    if ohne and (r.get("buyer", {}).get("address") or {}).get("region") in OBERPFALZ:
                        erweitert.append((y, r, ohne))
                    continue
                treffer.append((y, r, its))
    return treffer, liste_gefunden, zaehl, weit, erweitert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--download", action="store_true")
    a = ap.parse_args()
    if a.download:
        download()
        return
    t0 = time.time()
    groesse = {y: (RAW / f"{y}.jsonl.gz").stat().st_size for y in JAHRE}
    ted = ted_verfahren()
    nums, nummer2proc = liste_kennungen(ted)
    treffer, liste_gefunden, zaehl, weit, erweitert = scan(ted, nummer2proc)
    print(f"Dateien: " + ", ".join(f"{y}: {groesse[y] / 1e6:.0f} MB" for y in JAHRE) + f" (zusammen {sum(groesse.values()) / 1e6:.0f} MB)")
    print("Datensätze je Jahresdatei:", dict(zaehl), "gesamt", sum(zaehl.values()))
    print(f"TED-Index: {len(ted)} Verfahrenskennungen")
    for y in JAHRE:
        e, nn = weit[("bundesweit", y, True)], weit[("bundesweit", y, False)]
        print(f"Kontext bundesweit, Haupt-CPV 90910/90911/90919, Datei {y}: auf TED gefunden {e}, nicht gefunden {nn}")
    print("Kontext bundesweit (Stand vor 2026-09-01), Anteil ohne TED-Verfahrenskennung je NUTS-1-Gebiet (Lieferort; DE2 = Bayern):")
    for reg in sorted({k[1] for k in weit if k[0] == "nuts1"}):
        e, nn = weit[("nuts1", reg, True)], weit[("nuts1", reg, False)]
        print(f"   {reg}: nicht auf TED {pct(nn, e + nn)}")

    # ---- Verfahren
    verf = verfahren_bauen(treffer, ted)
    ted_nachpruefung(verf)
    erw = verfahren_bauen(erweitert, ted)
    ted_nachpruefung(erw)
    erw_g = collections.Counter((v["gruppe"], v["phase"]) for v in erw.values())
    print(f"\nSensitivität Erweiterung (nicht Teil des Filters): Position ohne Ortsangabe, Sitz des Auftraggebers in DE231 bis DE23A: {len(erw)} Verfahren, davon {dict(erw_g)}")
    n = len(verf)
    print(f"\nVerfahren im Filter (Haupt-CPV 90910/90911/90919, NUTS-3 DE231 bis DE23A, Lieferort der Position), 2024 bis 2026: {n}")
    tab = collections.Counter((v["gruppe"], v["phase"]) for v in verf.values())
    for g in ("EU", "national"):
        for ph in ("Auftragsbekanntmachung", "Zuschlag"):
            print(f"  {g:9s} {ph:24s} {tab[(g, ph)]}")
    print("  je Jahr (Datei) und Gruppe:", {y: dict(collections.Counter(v['gruppe'] for v in verf.values() if v['jahr'] == y)) for y in JAHRE})
    kn = sum(1 for v in verf.values() if v["gruppe"] == "national")
    lo, hi = wilson(kn, n)
    print(f"B1: unterhalb der EU-Schwelle (national, nicht auf TED): {pct(kn, n)}, Wilson 95 %: {100 * lo:.1f} bis {100 * hi:.1f} % (Schwelle >= 33 %)")
    for ph in ("Auftragsbekanntmachung", "Zuschlag"):
        nn = sum(1 for v in verf.values() if v["phase"] == ph)
        kk = sum(1 for v in verf.values() if v["phase"] == ph and v["gruppe"] == "national")
        l2, h2 = wilson(kk, nn)
        print(f"   nur {ph}: {pct(kk, nn)}, Wilson {100 * l2:.1f} bis {100 * h2:.1f} %")

    # ---- Sensitivität: Wert gegen EU-Schwelle (Dienstleistungen: 221.000 EUR sub-zentral, 143.000 EUR zentral; ab 2026 216.000/140.000)
    print("\nSensitivität (nur beschreibend): Auftragswert < EU-Schwelle (obere Grenze 221.000 EUR bis 2025, 216.000 EUR 2026)")
    for g in ("EU", "national"):
        vs = [v for v in verf.values() if v["gruppe"] == g]
        mitw = [v for v in vs if v["wert"] is not None]
        unter = [v for v in mitw if v["wert"] < (216000 if v["jahr"] == 2026 else 221000)]
        print(f"  {g}: mit Wert {pct(len(mitw), len(vs))}; davon Wert unter Schwelle {pct(len(unter), len(mitw))}")
    wertunter = sum(1 for v in verf.values() if v["wert"] is not None and v["wert"] < (216000 if v["jahr"] == 2026 else 221000))
    mitw = sum(1 for v in verf.values() if v["wert"] is not None)
    kn_w = sum(1 for v in verf.values() if v["wert"] is not None and v["wert"] < (216000 if v["jahr"] == 2026 else 221000))
    print(f"  Alternativmaß unter Schwelle nach Wert (nur Verfahren mit Wert): {pct(wertunter, mitw)}")
    print("  Wertquellen:", dict(collections.Counter(v["wertquelle"] for v in verf.values())))
    print("  Verfahrensart (procurementMethodDetails) je Gruppe:")
    for g in ("EU", "national"):
        print("   ", g, dict(collections.Counter((v["r"]["tender"].get("procurementMethodDetails")) for v in verf.values() if v["gruppe"] == g)))

    # ---- Lose (B2)
    lose = []
    for u, v in verf.items():
        r = v["r"]
        t = r["tender"]
        lotmap = {l["id"]: l for l in t.get("lots", [])}
        awards = r.get("awards", [])
        contracts = r.get("contracts", [])
        lot_ids = sorted({i.get("relatedLot") for i in v["items"] if i.get("relatedLot")})
        for lid in lot_ids:
            lot = lotmap.get(lid)
            aw = [x for x in awards if lid in (x.get("relatedLots") or []) or x.get("id") == lid]
            aw_aktiv = [x for x in aw if x.get("status") == "active"]
            ende, dauer, ende_oder = ende_vorhanden(lot)
            ct = [c for c in contracts if any(i.get("relatedLot") == lid for i in c.get("items", []))]
            lose.append(dict(
                ocid=r["ocid"], verfahren=u, jahr=v["jahr"], gruppe=v["gruppe"], phase=v["phase"], los=lid,
                titel=(lot or {}).get("title", "")[:120], auftraggeber=r["buyer"].get("name", "")[:100],
                nuts=next((i["deliveryAddress"]["region"] for i in v["items"] if i.get("relatedLot") == lid), ""),
                cpv=next((i["classification"]["id"] for i in v["items"] if i.get("relatedLot") == lid), ""),
                verfahrensart=t.get("procurementMethodDetails", ""),
                beginn=((lot or {}).get("contractPeriod") or {}).get("startDate", "")[:10],
                ende=((lot or {}).get("contractPeriod") or {}).get("endDate", "")[:10],
                dauer_tage=((lot or {}).get("contractPeriod") or {}).get("durationInDays", ""),
                f_ende=ende, f_dauer=dauer, f_ende_oder_dauer=ende_oder,
                zuschlag_los=bool(aw_aktiv),
                f_empfaenger=any(x.get("suppliers") for x in aw_aktiv),
                f_empfaenger_oder_partei=any(x.get("suppliers") for x in aw_aktiv)
                or any("supplier" in (p.get("roles") or []) for p in r.get("parties", [])),
                f_wert_award=any(gueltig_betrag((x.get("value") or {}).get("amount")) for x in aw_aktiv),
                f_wert_award_oder_vertrag=any(gueltig_betrag((x.get("value") or {}).get("amount")) for x in aw_aktiv)
                or any(gueltig_betrag((c.get("value") or {}).get("amount")) for c in ct),
                f_datum=any(x.get("date") for x in aw_aktiv) or any(c.get("dateSigned") for c in ct),
                f_angebote=(t.get("numberOfTenderers") or 0) > 0,
                wert_verfahren=v["wert"] if v["wert"] is not None else "",
                url=(t.get("documents") or [{}])[0].get("url", ""),
            ))
    with open(OUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(lose[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(lose)
    print(f"\nB2: {len(lose)} Lose (Positionen im Filter), Datei {OUT_CSV.relative_to(ROOT)}")
    felder = [("f_ende_oder_dauer", "Ende oder Dauer (Los)", "alle"), ("f_ende", "  davon Enddatum", "alle"),
              ("f_empfaenger", "Zuschlagsempfänger (awards.suppliers)", "zuschlag"),
              ("f_empfaenger_oder_partei", "Zuschlagsempfänger (awards.suppliers oder parties mit Rolle supplier)", "zuschlag"), ("f_wert_award", "Zuschlagswert > 1 EUR (awards.value)", "zuschlag"),
              ("f_wert_award_oder_vertrag", "Zuschlagswert > 1 EUR (awards oder contracts)", "zuschlag"),
              ("f_datum", "Zuschlagsdatum (awards.date oder contracts.dateSigned)", "zuschlag"), ("f_angebote", "Zahl der Angebote > 0 (Verfahrensebene)", "zuschlag")]
    for g in ("national", "EU"):
        ls = [l for l in lose if l["gruppe"] == g]
        lz = [l for l in ls if l["zuschlag_los"]]
        print(f"  Gruppe {g}: Lose {len(ls)}, davon mit aktivem Zuschlag {len(lz)}")
        for key, name, nenner in felder:
            base = ls if nenner == "alle" else lz
            print(f"    {name:60s} {pct(sum(1 for l in base if l[key]), len(base))} (Nenner: {'alle Lose' if nenner == 'alle' else 'Lose mit Zuschlag'})")

    zz = [v["r"]["tender"] for v in verf.values() if v["phase"] == "Zuschlag" and (v["r"]["tender"].get("numberOfTenderers") or 0) > 0]
    gl = sum(1 for t in zz if t["numberOfTenderers"] == len(t.get("tenderers", [])))
    print(f"\nnumberOfTenderers == Zahl der unter tender.tenderers genannten Bieter: {pct(gl, len(zz))} (Zuschlag-Verfahren mit Wert > 0); Hinweis: B4-Ersatz zeigt, dass das Feld nicht die Zahl der eingegangenen Angebote (TED: StatisticsCode 'tenders') ist")
    # ---- beschreibend: unterschwellige Verfahren mit Zuschlag je Jahr und Laufzeitende
    print("\nUnterschwellige (nationale) Verfahren mit Zuschlag je Jahr der Datei:")
    for y in JAHRE:
        print("  ", y, sum(1 for v in verf.values() if v["gruppe"] == "national" and v["phase"] == "Zuschlag" and v["jahr"] == y))
    zj = collections.Counter()
    for v in verf.values():
        if v["gruppe"] == "national" and v["phase"] == "Zuschlag":
            ds = [a.get("date", "")[:4] for a in v["r"].get("awards", []) if a.get("date")]
            zj[min(ds) if ds else "ohne Datum"] += 1
    print("   nach Jahr des Zuschlagsdatums:", dict(zj))
    ln = [l for l in lose if l["gruppe"] == "national" and l["zuschlag_los"]]
    print(f"   Lose mit Zuschlag, national: Ende lesbar (Enddatum oder Dauer) {pct(sum(1 for l in ln if l['f_ende_oder_dauer']), len(ln))}")

    # ---- B3
    print(f"\nB3: Liste {len(nums)} Bekanntmachungen, davon mit Verfahrenskennung aus gespeicherten TED-Abfragen: {len(nummer2proc)}")
    procs = set(nummer2proc.values())
    gef = {p for p in procs if p in liste_gefunden}
    print(f"   verschiedene Verfahren: {len(procs)}; im OCDS-Datensatz 2024 bis 2026 gefunden (ocid-Kennung): {len(gef)}")
    nm = [k for k, p in nummer2proc.items() if p in gef]
    print(f"   Bekanntmachungen (Nummern) mit gefundenem Verfahren: {len(nm)} von {len(nums)}")
    imfilter = {p for p in procs if p in verf}
    print(f"   davon im Filter dieses Tests (Lieferort-NUTS/CPV an der Position): {len(imfilter)} Verfahren")
    print("   nicht gefundene Bekanntmachungen (Nummer, TED-Jahr):", sorted(k for k in nums if nummer2proc.get(k) not in gef))
    print("   Überhang: Verfahren im Filter mit EU-Kennzeichen, die nicht in der Liste stehen:", sum(1 for u, v in verf.items() if v["eu"] and u not in procs), "; national:", kn)

    # ---- B4: Zufallsstichprobe unterschwelliger Verfahren
    nat = sorted(u for u, v in verf.items() if v["gruppe"] == "national")
    rnd = random.Random(SEED_B4)
    stich = rnd.sample(nat, min(5, len(nat)))
    print(f"\nB4: unterschwellige Verfahren insgesamt {len(nat)}; Stichprobe (Seed {SEED_B4}): {len(stich)}")
    if len(nat) < 5:
        # Ersatz (offene Abweichung von B4): 5 EU-Verfahren mit Zuschlag, gleicher Seed, Abgleich gegen die TED-Bekanntmachung
        eu_z = sorted(u for u, v in verf.items() if v["gruppe"] == "EU" and v["phase"] == "Zuschlag")
        stich = random.Random(SEED_B4).sample(eu_z, 5)
        print("  B4-Ersatz: Stichprobe aus EU-Verfahren mit Zuschlag (Zahl:", len(eu_z), "); TED-Nummern:", {u: sorted(ted.get(u, [])) for u in stich})
    for u in stich:
        v = verf[u]
        r = v["r"]
        t = r["tender"]
        print("  ---", u, v["jahr"], "Stand des Datensatzes:", r["date"], v["phase"], "|", r["buyer"].get("name"), "|", t.get("title"))
        for l in [x for x in lose if x["verfahren"] == u]:
            print("     Los", l["los"], "Ende", l["ende"], "Dauer", l["dauer_tage"], "Beginn", l["beginn"])
        for a in r.get("awards", []):
            sup = [s.get("name") for s in a.get("suppliers", [])]
            print("     Award", a.get("relatedLots"), a.get("status"), a.get("date"), (a.get("value") or {}).get("amount"), sup)
        for c in r.get("contracts", []):
            print("     Vertrag", c.get("status"), c.get("dateSigned"), (c.get("value") or {}).get("amount"))
        print("     Bieter", t.get("numberOfTenderers"), "Quelle", [d.get("url") for d in t.get("documents", [])][:2])
    print(f"\nDauer der Auswertung: {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
