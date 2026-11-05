"""Paket B, Robustheitsprüfung: Ist "0 von 84 Verfahren unterhalb der EU-Schwelle (Oberpfalz)" ein Artefakt des Filters?

Neues Skript, ändert keine bestehende Datei, ruft die Vergabeweiser-API nicht auf. Liest die OCDS-Jahresdateien
(data/raw/oeffentlichevergabe_20261105/2024|2025|2026.jsonl.gz) streamend und unverändert. Die Setzung "EU = Verfahrenskennung
steht auf TED" und die Feldnamen stammen aus src/oeffentlichevergabe_test.py.

Aufruf (Projektwurzel): .venv\\Scripts\\python.exe -I src\\oeffentlichevergabe_robustheit.py
Ausgabe: stdout (Zahlen mit Nennern). Der Bericht reports/oeffentlichevergabe_robustheit.md fasst sie zusammen.
Nur für die nationalen Treffer in Teil c wird bei TED einzeln nachgefragt (Antworten in data/raw/ted_nachpruefung_robustheit/).

Zuordnungsregeln (alle Näherungen, siehe Bericht):
 - Bundesland: 1. NUTS-Code des Lieferorts der betrachteten Position (DE1..DEG), 2. NUTS-Code des Auftraggebers,
   3. Postleitzahl des Auftraggebers, 4. Postleitzahl des Lieferorts. Postleitzahl -> Bundesland: die ersten zwei Ziffern werden
   ZUORDNUNG_PLZ2 aus dem Datensatz selbst gelernt (häufigstes Bundesland unter allen Auftraggebern mit NUTS-Code und PLZ).
 - Oberpfalz (Teil b/c): NUTS DE231 bis DE23A; sonst Auftraggeber-/Lieferort-PLZ 92xxx, 93xxx (ohne Landkreis Kelheim 93309-93359
   und 93077 Bad Abbach, die in Niederbayern liegen), 95xxx nur mit einem Ortsnamen des Landkreises Tirschenreuth; sonst Ortsname
   aus OP_ORTE im Ort/Straßenfeld des Lieferorts oder im Ort des Auftraggebers. Ein Ortsnamen-Treffer wird verworfen, wenn ein
   NUTS-Code außerhalb DE23 oder eine PLZ außerhalb der Oberpfalz-Regel dagegen spricht (z. B. Weiden bei Köln).
"""
import collections
import glob
import gzip
import json
import math
import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "oeffentlichevergabe_20261105"
NACH = ROOT / "data" / "raw" / "ted_nachpruefung_robustheit"
JAHRE = (2024, 2025, 2026)
GRENZE = "2026-09-01"  # lokale TED-Abfragen reichen nur bis etwa Ende September/Oktober 2026
OBERPFALZ = {"DE23" + c for c in "123456789A"}
BL = {"DE1": "Baden-Württemberg", "DE2": "Bayern", "DE3": "Berlin", "DE4": "Brandenburg", "DE5": "Bremen", "DE6": "Hamburg",
      "DE7": "Hessen", "DE8": "Mecklenburg-Vorpommern", "DE9": "Niedersachsen", "DEA": "Nordrhein-Westfalen",
      "DEB": "Rheinland-Pfalz", "DEC": "Saarland", "DED": "Sachsen", "DEE": "Sachsen-Anhalt", "DEF": "Schleswig-Holstein",
      "DEG": "Thüringen"}
BY_SUB = {"DE21": "Oberbayern", "DE22": "Niederbayern", "DE23": "Oberpfalz", "DE24": "Oberfranken", "DE25": "Mittelfranken",
          "DE26": "Unterfranken", "DE27": "Schwaben"}

# Orte der Oberpfalz (normalisiert: klein, ohne Umlaute, Satzzeichen als Leerzeichen). "Cham", "Weiden", "Neumarkt" sind mehrdeutig.
OP_ORTE = ["regensburg", "amberg", "weiden", "schwandorf", "cham", "neumarkt", "tirschenreuth", "neustadt a d waldnaab",
           "neustadt an der waldnaab", "neustadt a d w", "sulzbach rosenberg", "nabburg", "burglengenfeld", "roding", "parsberg",
           "regenstauf", "nittenau", "hemau", "kemnath", "waldsassen", "mitterteich", "eschenbach", "grafenwohr", "vilseck",
           "hirschau", "furth im wald", "bad kotzting", "kotzting", "waldmunchen", "neunburg vorm wald", "oberviechtach",
           "pfreimd", "wackersdorf", "maxhutte haidhof", "teublitz", "lappersdorf", "neutraubling", "wenzenbach", "pentling",
           "donaustauf", "barbing", "kallmunz", "beratzhausen", "dietfurt", "berching", "velburg", "freystadt", "pyrbaum",
           "plossberg", "baernau", "barnau", "wiesau", "waldershof", "konnersreuth", "immenreuth", "erbendorf", "pressath",
           "windischeschenbach", "vohenstrauss", "weiherhammer", "floss", "altenstadt a d waldnaab", "ensdorf", "schmidmuhlen",
           "kummersbruck", "ammerthal", "freihung", "hohenburg", "ursensollen", "nittendorf", "bernhardswald", "tegernheim",
           "wald", "oberpfalz", "landkreis cham", "landkreis schwandorf", "landkreis regensburg", "landkreis neumarkt",
           "landkreis tirschenreuth", "landkreis amberg sulzbach", "landkreis neustadt a d waldnaab"]
OP_ORTE = [o for o in OP_ORTE if o not in ("wald", "floss", "baernau")]  # zu mehrdeutig / Schreibvariante doppelt
AMBIG = {"cham", "weiden", "neumarkt", "amberg", "eschenbach", "regensburg", "oberpfalz"}  # nur mit stützender PLZ/NUTS oder ohne Gegenhinweis
TIR95 = ["tirschenreuth", "kemnath", "waldsassen", "mitterteich", "barnau", "wiesau", "waldershof", "falkenberg", "konnersreuth",
         "neualbenreuth", "neusorg", "pechbrunn", "plossberg", "fuchsmuhl", "friedenfels", "mahring", "ebnath", "immenreuth",
         "brand", "kulmain", "krummennaab", "erbendorf"]
ORT_RE = re.compile(r"(?:^| )(" + "|".join(sorted((re.escape(o) for o in OP_ORTE), key=len, reverse=True)) + r")(?: |$)")
TIR95_RE = re.compile(r"(?:^| )(" + "|".join(TIR95) + r")(?: |$)")


def norm(s):
    s = (s or "").lower()
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss")):
        s = s.replace(a, b)
    s = re.sub(r"[-./,()]", " ", s)
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r" +", " ", s).strip()


def wilson(k, n, z=1.96):
    if n == 0:
        return float("nan"), float("nan")
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (c - h), 100 * (c + h)


def pct(k, n):
    return f"{k}/{n} = {100 * k / n:.1f} %" if n else f"{k}/0"


def pctci(k, n):
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {100 * k / n:.1f} % [{lo:.1f}; {hi:.1f}]" if n else f"{k}/0"


# ---------------------------------------------------------------- TED-Index (wie in oeffentlichevergabe_test.py)
def ted_verfahren():
    idx = set()
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
                idx.add(p if isinstance(p, str) else p[0])
    for f in glob.glob(str(ROOT / "data" / "raw" / "ted_xml" / "*.xml")):
        try:
            for e in ET.parse(f).getroot().iter():
                if e.tag.rsplit("}", 1)[-1] == "ContractFolderID" and e.text:
                    idx.add(e.text.strip())
                    break
        except Exception:
            continue
    return idx


def ted_einzel(u):
    """Einzelabfrage bei TED (procedure-identifier), Antwort gespeichert. True = steht auf TED."""
    NACH.mkdir(parents=True, exist_ok=True)
    f = NACH / f"{u}.json"
    if not f.exists():
        for versuch in range(1, 5):
            try:
                body = json.dumps({"query": f"procedure-identifier={u}", "fields": ["publication-number"], "limit": 5}).encode()
                req = urllib.request.Request("https://api.ted.europa.eu/v3/notices/search", data=body,
                                             headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=60) as r:
                    f.write_bytes(r.read())
                break
            except Exception as e:
                print("TED-Einzelabfrage", u, "Versuch", versuch, e)
                time.sleep(3 * versuch)
        time.sleep(1)
    if not f.exists():
        return None
    return bool(json.loads(f.read_text(encoding="utf-8")).get("notices"))


# ---------------------------------------------------------------- Einlesen
def adr(a):
    a = a or {}
    return dict(region=str(a.get("region") or ""), plz=str(a.get("postalCode") or "").strip(), ort=a.get("locality") or "",
                strasse=a.get("streetAddress") or "")


def kompakt(y, r, ted):
    t = r.get("tender", {})
    uuid = r["ocid"][len("ocds-mnwr74-"):]
    items = []
    for i in t.get("items", []):
        main = str((i.get("classification") or {}).get("id", ""))
        zus = [str(c.get("id", "")) for c in (i.get("additionalClassifications") or [])]
        d = adr(i.get("deliveryAddress"))
        items.append(dict(main=main, zus=zus, **d))
    b = r.get("buyer", {})
    ba = adr(b.get("address"))
    if not (ba["region"] or ba["plz"]):  # Ersatz: Partei mit Rolle buyer
        for p in r.get("parties", []):
            if "buyer" in (p.get("roles") or []) and p.get("address"):
                ba = adr(p["address"])
                break
    text = " ".join([t.get("title") or "", t.get("description") or ""] + [(l.get("title") or "") + " " + (l.get("description") or "") for l in t.get("lots", [])]).lower()
    return dict(y=y, uuid=uuid, date=r.get("date", ""), titel=(t.get("title") or "")[:140], buyer=b.get("name", ""), b=ba, items=items,
                eu=uuid in ted, rein="reinigung" in text,
                m909=any(i["main"].startswith("909") for i in items),
                a909=any(i["main"].startswith("909") or any(z.startswith("909") for z in i["zus"]) for i in items),
                cpv_da=any(i["main"] for i in items), n_items=len(items))


def scan(ted):
    kand, monat, monat_start, jahr_n, dups = {}, collections.Counter(), collections.Counter(), collections.Counter(), 0
    for y in JAHRE:
        with gzip.open(RAW / f"{y}.jsonl.gz", "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                jahr_n[y] += 1
                m = re.search(r'"date": "(\d{4}-\d{2})', line[:600])
                monat[(y, m.group(1) if m else "ohne")] += 1
                if '"909' not in line and "einigung" not in line.lower():
                    continue
                r = json.loads(line)
                k = kompakt(y, r, ted)
                if not (k["a909"] or k["rein"]):
                    continue
                if k["uuid"] in kand:
                    dups += 1
                    if kand[k["uuid"]]["date"] >= k["date"]:
                        continue
                kand[k["uuid"]] = k
    return kand, monat, jahr_n, dups


# ---------------------------------------------------------------- Zuordnung
def plz2_lernen(kand):
    c = collections.defaultdict(collections.Counter)
    for k in kand.values():
        reg = k["b"]["region"][:3]
        if reg in BL and re.fullmatch(r"\d{5}", k["b"]["plz"]):
            c[k["b"]["plz"][:2]][BL[reg]] += 1
    m = {p: cnt.most_common(1)[0][0] for p, cnt in c.items()}
    rein = sum(cnt.most_common(1)[0][1] for cnt in c.values())
    ges = sum(sum(cnt.values()) for cnt in c.values())
    return m, rein, ges


def plz_op(p):
    if not re.fullmatch(r"\d{5}", p or ""):
        return None
    n = int(p)
    if p[:2] == "92":
        return True
    if p[:2] == "93":
        return not (93309 <= n <= 93359 or n == 93077)
    return False


def rel_items(k, gruppe):
    if gruppe == "m909":
        return [i for i in k["items"] if i["main"].startswith("909")]
    if gruppe == "a909":
        return [i for i in k["items"] if i["main"].startswith("909") or any(z.startswith("909") for z in i["zus"])]
    return k["items"]


def bundesland(k, gruppe, plzmap):
    for i in rel_items(k, gruppe):
        if i["region"][:3] in BL:
            return BL[i["region"][:3]], "NUTS Lieferort"
    if k["b"]["region"][:3] in BL:
        return BL[k["b"]["region"][:3]], "NUTS Auftraggeber"
    if k["b"]["plz"][:2] in plzmap and re.fullmatch(r"\d{5}", k["b"]["plz"]):
        return plzmap[k["b"]["plz"][:2]], "PLZ Auftraggeber"
    for i in rel_items(k, gruppe):
        if i["plz"][:2] in plzmap and re.fullmatch(r"\d{5}", i["plz"]):
            return plzmap[i["plz"][:2]], "PLZ Lieferort"
    return "unbekannt", "-"


def oberpfalz_eng(k, gruppe):
    """Enger Filter wie in Paket B: NUTS-Lieferort DE231 bis DE23A an der betrachteten Position."""
    return any(i["region"] in OBERPFALZ for i in rel_items(k, gruppe))


def oberpfalz_weit(k, gruppe):
    """Breiter Filter. Rückgabe (Treffer, Grund)."""
    its = rel_items(k, gruppe) if gruppe != "text" else k["items"]
    regs = [i["region"] for i in its] + [k["b"]["region"]]
    if any(r in OBERPFALZ for r in regs):
        return True, "NUTS"
    plzs = [k["b"]["plz"]] + [i["plz"] for i in its]
    nuts_dagegen = any(r.startswith("DE") and len(r) >= 4 and r[:4] != "DE23" for r in regs if r)
    if any(plz_op(p) for p in plzs if p) and not nuts_dagegen:
        return True, "PLZ 92/93"
    texte = [norm(i["ort"]) + " " + norm(i["strasse"]) for i in its] + [norm(k["b"]["ort"]), norm(k["buyer"])]
    plz_dagegen = any(plz_op(p) is False and re.fullmatch(r"\d{5}", p) for p in plzs if p) and not any(plz_op(p) for p in plzs if p)
    for tx in texte:
        m = ORT_RE.search(tx)
        if m and not nuts_dagegen and not plz_dagegen:
            return True, "Ortsname: " + m.group(1)
        if TIR95_RE.search(tx) and any(p[:2] == "95" for p in plzs if p) and not nuts_dagegen:
            return True, "PLZ 95 + Ort Tirschenreuth"
    return False, ""


# ---------------------------------------------------------------- Ausgabe
GRUPPEN = [("m909", "Haupt-CPV 909xxxxx (eine Position)"), ("a909", "CPV 909 als Haupt- oder Zusatz-CPV"),
           ("text", "ohne CPV-Filter: Titel/Beschreibung enthält 'Reinigung'"),
           ("text_ohne", "  davon ohne jede CPV-909-Angabe")]


def gehoert(k, g):
    return {"m909": k["m909"], "a909": k["a909"], "text": k["rein"], "text_ohne": k["rein"] and not k["a909"]}[g]


def betrachtete_items(k, g):
    return rel_items(k, "a909" if g in ("a909",) else g) if g in ("m909", "a909") else k["items"]


def teil_a(kand, jahr_n):
    print("=" * 100, "\nTEIL a) Bundesweit: Verfahren je Jahr (Datei), EU (auf TED) gegen national (nicht auf TED)")
    print("Datensätze je Jahresdatei:", dict(jahr_n), "gesamt", sum(jahr_n.values()))
    print(f"Hinweis: Datum >= {GRENZE} liegt hinter dem Ende der lokalen TED-Abfragen; national dort unsicher und in den Anteilen weggelassen.")
    for g, name in GRUPPEN:
        print(f"\n--- {name}")
        for y in JAHRE + ("alle",):
            ks = [k for k in kand.values() if gehoert(k, g) and (y == "alle" or k["y"] == y)]
            alt = [k for k in ks if k["date"] < GRENZE]
            nat = sum(1 for k in alt if not k["eu"])
            print(f"  {y}: Verfahren {len(ks)}, davon Datum vor {GRENZE}: {len(alt)}; national {pctci(nat, len(alt))}; "
                  f"Datum ab {GRENZE}: {len(ks) - len(alt)} (davon ohne lokalen TED-Treffer {sum(1 for k in ks if k['date'] >= GRENZE and not k['eu'])})")
        alt = [k for k in kand.values() if gehoert(k, g) and k["date"] < GRENZE]
        print("  Merkmale (Datum vor Grenze), Anteil mit Angabe; Position = betrachtete Positionen der Gruppe:")
        for grp, lab in (("national", False), ("EU", True)):
            ks = [k for k in alt if k["eu"] == lab]
            n = len(ks)

            def mit(f):
                return sum(1 for k in ks if f(k))
            its = lambda k: betrachtete_items(k, g)
            print(f"   {grp:8s} n={n}: (i) NUTS-Code im Lieferort {pct(mit(lambda k: any(i['region'].startswith('DE') for i in its(k))), n)}; "
                  f"(ii) PLZ oder Ort im Lieferort {pct(mit(lambda k: any(i['plz'] or i['ort'] for i in its(k))), n)} "
                  f"(nur PLZ {pct(mit(lambda k: any(i['plz'] for i in its(k))), n)}); "
                  f"(iii) Auftraggeber mit PLZ {pct(mit(lambda k: bool(k['b']['plz'])), n)}, mit NUTS {pct(mit(lambda k: k['b']['region'].startswith('DE')), n)}; "
                  f"(iv) irgendeine CPV-Angabe an einer Position {pct(mit(lambda k: k['cpv_da']), n)}"
                  f"{'; CPV 909 an einer Position ' + pct(mit(lambda k: k['a909']), n) if g.startswith('text') else ''}")
            ohne_ort = mit(lambda k: not any(i['region'].startswith('DE') or i['plz'] or i['ort'] for i in its(k)))
            print(f"            ohne jede Ortsangabe im Lieferort {pct(ohne_ort, n)}; davon mit Auftraggeber-Sitz (PLZ oder NUTS) "
                  f"{pct(mit(lambda k: not any(i['region'].startswith('DE') or i['plz'] or i['ort'] for i in its(k)) and (k['b']['plz'] or k['b']['region'])), ohne_ort)}")


def teil_b(kand, plzmap):
    print("=" * 100, "\nTEIL b) Anteil national je Bundesland (Datum vor Grenze)")
    for g, name in (("m909", "Haupt-CPV 909"), ("a909", "CPV 909 Haupt oder Zusatz")):
        print(f"\n--- {name}; Zuordnung Lieferort-NUTS, dann Auftraggeber-NUTS, dann PLZ")
        alt = [k for k in kand.values() if gehoert(k, g) and k["date"] < GRENZE]
        c = collections.Counter()
        quelle = collections.Counter()
        for k in alt:
            bl, q = bundesland(k, g, plzmap)
            quelle[q] += 1
            c[(bl, k["eu"])] += 1
        print("  Zuordnungsquelle:", dict(quelle))
        zeilen = sorted({bl for bl, _ in c}, key=lambda b: -(c[(b, True)] + c[(b, False)]))
        ges_n = sum(v for (b, e), v in c.items() if not e)
        for bl in zeilen:
            nat, eu = c[(bl, False)], c[(bl, True)]
            print(f"  {bl:24s} Verfahren {nat + eu:5d}  national {pctci(nat, nat + eu)}")
        print(f"  {'gesamt':24s} Verfahren {len(alt):5d}  national {pctci(ges_n, len(alt))}")
        # Bayern-Aufteilung
        by = collections.Counter()
        for k in alt:
            bl, q = bundesland(k, g, plzmap)
            if bl != "Bayern":
                continue
            sub = None
            for i in rel_items(k, g):
                if i["region"][:4] in BY_SUB:
                    sub = BY_SUB[i["region"][:4]]
                    break
            if not sub and k["b"]["region"][:4] in BY_SUB:
                sub = BY_SUB[k["b"]["region"][:4]]
            if not sub:
                hit, _ = oberpfalz_weit(k, g)
                sub = "Oberpfalz (nur PLZ/Ortsliste)" if hit else "Bayern, Regierungsbezirk unbekannt/andere"
            by[(sub, k["eu"])] += 1
        print("  Bayern nach Regierungsbezirk (NUTS; sonst PLZ/Ortsliste für Oberpfalz):")
        for sub in sorted({s for s, _ in by}):
            nat, eu = by[(sub, False)], by[(sub, True)]
            print(f"     {sub:42s} Verfahren {nat + eu:4d}  national {pctci(nat, nat + eu)}")
        # Auftraggeber national in Bayern (juristische Personen), häufigste
        namen = collections.Counter(k["buyer"] for k in alt if not k["eu"] and bundesland(k, g, plzmap)[0] == "Bayern")
        print("  Bayern: nationale Verfahren, häufigste Auftraggeber:", namen.most_common(8))
        namen_eu = collections.Counter(k["buyer"] for k in alt if k["eu"] and bundesland(k, g, plzmap)[0] == "Bayern")
        print("  Bayern: EU-Verfahren, häufigste Auftraggeber:", namen_eu.most_common(8))
    # Zuordnung ohne Lieferort: nur Auftraggeber-Sitz
    print("\n--- Kontrolle: nur Sitz des Auftraggebers (NUTS, sonst PLZ), Haupt-CPV 909")
    alt = [k for k in kand.values() if k["m909"] and k["date"] < GRENZE]
    c = collections.Counter()
    for k in alt:
        bl = BL.get(k["b"]["region"][:3]) or (plzmap.get(k["b"]["plz"][:2]) if re.fullmatch(r"\d{5}", k["b"]["plz"]) else None) or "unbekannt"
        c[(bl, k["eu"])] += 1
    for bl in sorted({b for b, _ in c}, key=lambda b: -(c[(b, True)] + c[(b, False)])):
        nat, eu = c[(bl, False)], c[(bl, True)]
        print(f"  {bl:24s} Verfahren {nat + eu:5d}  national {pctci(nat, nat + eu)}")


def teil_c(kand):
    print("=" * 100, "\nTEIL c) Oberpfalz, breiter Filter (Treffer: NUTS DE231-DE23A bei Position oder Auftraggeber, PLZ 92/93, Ortsliste)")
    zellen = {}
    for g, name in GRUPPEN[:3]:
        treffer = []
        for k in kand.values():
            if not gehoert(k, g):
                continue
            hit, grund = oberpfalz_weit(k, "text" if g == "text" else g)
            if hit:
                treffer.append((k, grund))
        zellen[g] = treffer
        eu = [t for t in treffer if t[0]["eu"]]
        nat = [t for t in treffer if not t[0]["eu"]]
        eng = [t for t in treffer if oberpfalz_eng(t[0], "m909" if g != "text" else "m909")]
        print(f"\n--- {name}: breiter Filter {len(treffer)} Verfahren (alle Jahre), EU {len(eu)}, ohne lokalen TED-Treffer {len(nat)}; "
              f"davon im engen Paket-B-Filter (Haupt-CPV 909 + NUTS Lieferort) {len(eng)}")
        print("    Gründe:", dict(collections.Counter(t[1].split(":")[0] for t in treffer)))
    # TED-Einzelabfrage für die nicht lokal gefundenen Treffer
    alle = {}
    for g in ("m909", "a909", "text"):
        for k, grund in zellen[g]:
            if not k["eu"]:
                alle[k["uuid"]] = (k, grund)
    print(f"\nNicht lokal auf TED gefundene Treffer aller drei Gruppen (verschiedene Verfahren): {len(alle)}; Einzelabfrage bei TED ...")
    for u, (k, _) in alle.items():
        k["ted_einzel"] = ted_einzel(u)
    echt_nat = {u: v for u, v in alle.items() if v[0].get("ted_einzel") is False}
    unklar = {u: v for u, v in alle.items() if v[0].get("ted_einzel") is None}
    print(f"  nach Einzelabfrage doch auf TED: {sum(1 for v in alle.values() if v[0].get('ted_einzel'))}; nicht auf TED: {len(echt_nat)}; Abfrage nicht gelungen: {len(unklar)}")
    for g, name in GRUPPEN[:3]:
        treffer = zellen[g]
        n = len(treffer)
        nn = sum(1 for k, _ in treffer if not k["eu"] and k.get("ted_einzel") is False)
        print(f"  {name}: breiter Filter {n} Verfahren, national (nach Einzelabfrage) {pctci(nn, n)}")
    # Beispiele
    print("\nBeispiele: alle nationalen Treffer (Jahr der Datei | Stand | Auftraggeber | Titel | Gruppen | Grund | CPV909 | PLZ Auftraggeber | Lieferort)")
    for u, (k, grund) in sorted(echt_nat.items(), key=lambda kv: (kv[1][0]["y"], kv[1][0]["buyer"])):
        gr = [g for g in ("m909", "a909", "text") if any(kk["uuid"] == u for kk, _ in zellen[g])]
        lo = "; ".join(sorted({(i["plz"] + " " + i["ort"]).strip() + (" [" + i["region"] + "]" if i["region"] else "") for i in k["items"]}))[:80]
        print(f"  {k['y']} | {k['date'][:10]} | {k['buyer'][:70]} | {k['titel'][:100]} | {','.join(gr)} | {grund} | 909={k['a909']} | {k['b']['plz']} | {lo}")
    # EU-Treffer zum Vergleich, die nur im breiten Filter stehen
    print("\nEU-Treffer des breiten Filters (Gruppe Reinigung-Text) außerhalb des engen Filters, Anzahl nach Grund:")
    c = collections.Counter()
    for k, grund in zellen["text"]:
        if k["eu"] and not oberpfalz_eng(k, "m909"):
            c[grund.split(":")[0]] += 1
    print("  ", dict(c))


def teil_d(monat):
    print("=" * 100, "\nTEIL d) Verfahren je Monat (Monat des Feldes 'date' = letzte Aktualisierung; Zeilen: Dateijahr)")
    for y in JAHRE:
        werte = {m: n for (yy, m), n in monat.items() if yy == y}
        print(f" Datei {y}: gesamt {sum(werte.values())}")
        for m in sorted(werte):
            print(f"    {m}: {werte[m]:6d} " + "#" * (werte[m] // 1000))
    alle = collections.Counter()
    for (y, m), n in monat.items():
        alle[m] += n
    print(" Monate über alle Dateien (Vorjahre in einer Datei = aktualisiert im Jahr der Datei):", len(alle))
    ms = sorted(m for m in alle if m != "ohne")
    print("  erster Monat", ms[0], "letzter Monat", ms[-1])
    erwartet = []
    y, mth = int(ms[0][:4]), int(ms[0][5:])
    while (y, mth) <= (int(ms[-1][:4]), int(ms[-1][5:])):
        erwartet.append(f"{y}-{mth:02d}")
        mth += 1
        if mth == 13:
            y, mth = y + 1, 1
    print("  Monate ohne jeden Datensatz zwischen erstem und letztem:", [m for m in erwartet if m not in alle])


def lieferort_op(its):
    """Streng: nur der Lieferort der Position zählt (kein Auftraggeber-Name, kein Auftraggeber-Sitz)."""
    for i in its:
        r, p = i["region"], i["plz"]
        if r in OBERPFALZ:
            return True
        if r.startswith("DE") and len(r) >= 4 and r[:4] != "DE23":
            continue
        if re.fullmatch(r"\d{5}", p or ""):
            if plz_op(p):
                return True
            if not (p[:2] == "95" and TIR95_RE.search(norm(i["ort"]))):
                continue
            return True
        if ORT_RE.search(norm(i["ort"]) + " " + norm(i["strasse"])):
            return True
    return False


def teil_e(kand):
    print("=" * 100, "\nTEIL e) Genauigkeit des Feldes Lieferort (Länge des NUTS-Codes) und strenger Oberpfalz-Filter nur über den Lieferort")
    for g, name in (("m909", "Haupt-CPV 909"), ("text", "Text 'Reinigung'")):
        alt = [k for k in kand.values() if gehoert(k, g) and k["date"] < GRENZE]
        print(f"\n--- {name}: Länge des NUTS-Codes im Lieferort der Position (Verfahren, Datum vor Grenze; ein Verfahren zählt mit seiner genauesten Position)")
        for grp, lab in (("national", False), ("EU", True)):
            ks = [k for k in alt if k["eu"] == lab]
            c = collections.Counter()
            for k in ks:
                lens = [len(i["region"]) for i in rel_items(k, g if g != "text" else "text") if i["region"].startswith("DE")]
                c[max(lens) if lens else 0] += 1
            n = len(ks)
            print(f"   {grp:8s} n={n}: kein DE-Code {pct(c[0], n)}; NUTS-1 (DEx, 3 Zeichen) {pct(c[3], n)}; NUTS-2 (4) {pct(c[4], n)}; NUTS-3 (5) {pct(c[5], n)}; sonst {n - c[0] - c[3] - c[4] - c[5]}")
    print("\n--- Strenger Oberpfalz-Filter (nur Lieferort der Position: NUTS DE231-DE23A, PLZ 92/93, Ortsliste), alle Jahre, nationale nach TED-Einzelabfrage")
    for g, name in (("m909", "Haupt-CPV 909"), ("a909", "CPV 909 Haupt/Zusatz"), ("text", "Text 'Reinigung'")):
        tr = [k for k in kand.values() if gehoert(k, g) and lieferort_op(rel_items(k, g))]
        for k in tr:
            if not k["eu"] and "ted_einzel" not in k:
                k["ted_einzel"] = ted_einzel(k["uuid"])
        nat = [k for k in tr if not k["eu"] and k.get("ted_einzel") is False]
        eng = [k for k in tr if oberpfalz_eng(k, "m909")]
        nat_nuts3 = [k for k in nat if any(i["region"] in OBERPFALZ for i in rel_items(k, g))]
        print(f"  {name}: {len(tr)} Verfahren, davon national {pctci(len(nat), len(tr))}; im engen NUTS-3-Filter (Haupt-CPV 909) {len(eng)}; "
              f"nationale mit NUTS-3-Code der Oberpfalz: {len(nat_nuts3)}")
        print("     Länge des Lieferort-NUTS bei den nationalen Treffern:", dict(collections.Counter(max([len(i['region']) for i in rel_items(k, g) if i['region'].startswith('DE')] or [0]) for k in nat)))
        for jahr in JAHRE:
            t2 = [k for k in tr if k["y"] == jahr]
            n2 = [k for k in t2 if not k["eu"] and k.get("ted_einzel") is False]
            print(f"       {jahr}: {pct(len(n2), len(t2))}")
        if g == "m909":
            print("     nationale Haupt-CPV-909-Treffer (Auftraggeber | Titel | Lieferort):")
            for k in sorted(nat, key=lambda k: (k["y"], k["buyer"])):
                lo = "; ".join(sorted({(i["plz"] + " " + i["ort"]).strip() for i in k["items"]}))[:60]
                print(f"       {k['y']} | {k['buyer'][:55]} | {k['titel'][:80]} | {lo}")


def main():
    t0 = time.time()
    ted = ted_verfahren()
    print(f"TED-Index: {len(ted)} Verfahrenskennungen")
    kand, monat, jahr_n, dups = scan(ted)
    print(f"Kandidaten (CPV 909 irgendwo oder 'Reinigung' im Text): {len(kand)} Verfahren; Doppelte ocid über Dateien: {dups}")
    plzmap, rein, ges = plz2_lernen(kand)
    print(f"Gelernte PLZ-Zuordnung (erste 2 Ziffern -> Bundesland): {len(plzmap)} Bereiche aus {ges} Auftraggebern; Übereinstimmung mit häufigstem Bundesland {pct(rein, ges)}")
    teil_a(kand, jahr_n)
    teil_b(kand, plzmap)
    teil_c(kand)
    teil_e(kand)
    teil_d(monat)
    print(f"\nDauer: {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
