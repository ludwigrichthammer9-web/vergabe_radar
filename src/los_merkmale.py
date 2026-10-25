"""Objektmerkmale je Los für die Zuordnung über das Objekt (Iteration 4, Schritt 2).

Ersetzt für Iteration 4 `objekt_merkmale.py` (das bleibt unverändert, weil die eingefrorene Regel aus Iteration 3 davon abhängt).
Läuft ohne pandas.

Merkmale je Los (Begriffe nach reports/urteilsregeln_blindpruefung.md, Stufen A und B):
- arten:     Leistungsarten (unterhalt, glas, grund, treppenhaus, bau, sonder); „ohne Glasreinigung“ u. Ä. wird beachtet
- flaechen:  Flächen in m² mit Art (boden oder glas), aus „m²“, „m2“, „qm“, „Quadratmeter“
- adressen:  Straße + Hausnummer, normalisiert (z. B. „kanalstr 20“)
- strassen:  Straßennamen ohne Hausnummer
- namen:     Objektnamen aus Typwort + Name (z. B. „gesamtschule hoehscheid“, „amtsgericht amberg“) und zusammengesetzte
             Namen (z. B. „goetheschule“)
- plz, orte: Leistungsort

Quellen: eForms über die Such-API (`title-lot`, `description-lot`, `description-proc`, `place-*`, `main-classification-lot`;
Download mit `ted_download.py --los-texte`). Vor eForms aus der Original-XML (je OBJECT_DESCR: TITLE, MAIN_SITE, SHORT_DESCR),
zwischengespeichert unverändert unter data/raw/ted_xml/objekt/ (derselbe Speicher wie in Iteration 3).

Aufruf zum Ansehen einzelner Notices (nur Entwicklungsdaten):
    .venv\\Scripts\\python -I src/los_merkmale.py 496932-2026 683345-2024 107618-2021
"""

import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

import requests

from population_iteration4 import flatten

PROJECT_ROOT = Path(__file__).resolve().parent.parent
XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml" / "objekt"
XML_URL = "https://ted.europa.eu/en/notice/{}/xml"
PAUSE_SECONDS = 0.5

UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "Ä": "ae", "Ö": "oe", "Ü": "ue"})

# Leistungsarten: Muster auf normalisiertem Text (Kleinbuchstaben, Umlaute ersetzt)
ARTEN = {
    "unterhalt": r"unterhalt\w*|\buhr\b|laufende\w* (?:gebaeude)?reinigung|taegliche\w* reinigung|bueroreinigung|schulreinigung|"
                 r"gebaeude\w*reinigung\w*|gebaeude und glas\w*|innenreinigung\w*",
    "glas": r"glas\w*|fenster\w*|rahmenreinigung",
    "grund": r"grundreinigung\w*|grundpflege",
    "treppenhaus": r"treppenhaus\w*|hausflur\w*",
    "bau": r"bau(?:end|fein|grob|zwischen|schluss)?reinigung\w*",
    "sonder": r"sonderreinigung\w*",
    # keine Gebäudereinigung: Kandidaten nur mit dieser Art widersprechen jeder Gebäudereinigung
    "fremd": r"schaedling\w*|\w*fahrzeug(?:e|en|reinigung|pflege|waesche|waschanlage)\b|waesche\w*|bettwaesche\w*|textil\w*|"
             r"winterdienst\w*|reinigung von (?:\w+ )?(?:bussen|zuegen|bahnen)",
}
NEGATION = r"(?:ohne|nicht|ausgenommen|exklusive|ausser)\s+(?:\w+\s+){0,2}?"
# CPV je Los als Stütze für die Leistungsart, wenn der Text keine nennt
CPV_ART = {"90911300": "glas", "90911200": "unterhalt", "90919200": "unterhalt", "90919300": "unterhalt", "90911100": "treppenhaus"}

TYPWORT = (
    r"(?:grund|haupt|real|ober|mittel|gesamt|gemeinschafts|förder|foerder|berufs|sekundar|regional|fach|volks)?schule|gymnasium|"
    r"kita|kindertagesstätte|kindertagesstaette|kindergarten|kinderkrippe|hort|sporthalle|turnhalle|mehrzweckhalle|stadthalle|"
    r"rathaus|bürgerhaus|buergerhaus|gewandhaus|amtsgericht|landgericht|oberlandesgericht|arbeitsgericht|sozialgericht|"
    r"verwaltungsgericht|finanzamt|hauptzollamt|polizeiinspektion|polizeirevier|polizeipräsidium|polizeidirektion|polizeiposten|"
    r"feuerwache|feuerwehr|feuerwehrgerätehaus|museum|bibliothek|bücherei|hallenbad|freibad|schwimmbad|kaserne|mensa|wohnheim|"
    r"hochschule|universität|universitaet|klinikum|klinik|krankenhaus|jobcenter|kundenzentrum|bezirksamt|dienststelle|"
    r"verwaltungsgebäude|verwaltungsgebaeude|landratsamt|bildungshaus|jugendzentrum|bauhof|friedhof|zentrum|"
    r"justizgebäude|justizgebaeude|justizzentrum|behördenzentrum|behoerdenzentrum|dienstgebäude|dienstgebaeude"
)
# Vorsilben, mit denen ein zusammengesetztes Typwort nur eine Gebäudeart bezeichnet, keinen Eigennamen (z. B. „Berufsschulzentrum“)
GENERIC_PREFIX = set("""
berufsschul berufsbildungs rechen bildungs schul verwaltungs sport familien jugend gemeinde stadt kreis kinder senioren alten
einfeld zweifeld dreifeld vierfeld ganztags dienstleistungs kompetenz service behoerden haupt grund ober real gesamt foerder gemeinschafts mehrzweck stadtteil
buerger begegnungs gesundheits ausbildungs fortbildungs schulungs studien sozial kultur freizeit wohn betriebs einsatz
""".split())
# Typwort ohne Rücksicht auf Groß-/Kleinschreibung, der Name danach muss großgeschrieben sein
NAME_AFTER = re.compile(
    rf"\b((?i:{TYPWORT}))\s+(?:(?:der|des|am|an der|in|im|zu|auf dem)\s+)?"
    r"((?:[A-ZÄÖÜ][\wäöüß\.\-]+)(?:\s+[A-ZÄÖÜ][\wäöüß\.\-]+){0,2})",
    re.UNICODE,
)
COMPOUND = re.compile(rf"\b([A-ZÄÖÜ][\wäöüß\-]{{2,}}?-?(?i:{TYPWORT}))\b", re.UNICODE)
# Typwörter, die bei einem Auftraggeber meist nur ein Objekt bezeichnen; sie zählen auch ohne Namen
EINZELOBJEKT = re.compile(r"\b(rathaus|gewandhaus|stadthalle|bürgerhaus|amtsgericht|landgericht|oberlandesgericht|finanzamt|"
                          r"hauptzollamt|landratsamt|museum|kaserne|mensa|hallenbad|freibad)\b", re.IGNORECASE)
STOP_NAMES = {"und", "sowie", "mit", "fuer", "los", "nr", "gmbh", "der", "die", "das", "stadt", "gemeinde", "landkreis",
              "kreis", "verbandsgemeinde", "landeshauptstadt", "hansestadt", "gebaeude", "auftragnehmer", "objekte",
              "liegenschaften", "einrichtungen", "standort", "standorte", "unterhalts", "glas", "grund", "fenster", "ca",
              "quadratmeter", "in", "im", "am", "objektgruppe", "gebiet", "bereich", "teil", "uhr", "gr", "glasr", "ur"}
PLACEHOLDERS = {"anyw", "anywhere", "beliebiger ort", "deutschland"}

STREET = (r"[A-ZÄÖÜ][\wäöüß\.\-]*?(?:straße|strasse|str\.|weg|platz|allee|ring|gasse|damm|ufer|chaussee|steig|pfad|markt|hof|"
          r"wall|graben|berg|garten|park|feld|aue|kamp)")
ADDRESS_RE = re.compile(rf"({STREET}|(?:[A-ZÄÖÜ][\wäöüß\-]+\s)(?:Straße|Strasse|Str\.|Weg|Platz|Allee|Ring|Gasse|Damm|Ufer))"
                        r"\s*(\d{1,4}\s?[a-zA-Z]?(?:\s?[-–/]\s?\d{1,4}\s?[a-zA-Z]?)?)\b", re.UNICODE)
PLZ_RE = re.compile(r"\b(\d{5})\b")
AREA_RE = re.compile(r"(\d{1,3}(?:[\.\s ]\d{3})+|\d+)(?:,(\d{1,2}))?\s*(?:m²|m2\b|m 2\b|qm\b|quadratmeter)", re.IGNORECASE)


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower().translate(UMLAUTS)).strip()


def norm_street(street: str) -> str:
    s = norm(street)
    s = re.sub(r"(strasse|str)$", "str", s)
    s = re.sub(r"\b(strasse|str)\b", "str", s)
    return s.replace(" str", "str") if s.endswith(" str") else s


def norm_number(num: str) -> str:
    return re.sub(r"\s+", "", num.lower()).replace("–", "-")


@dataclass
class Los:
    nr: str = ""
    titel: str = ""
    text: str = ""  # Titel + Beschreibung + Ort, für die Suche
    arten: set[str] = field(default_factory=set)
    flaechen: list[tuple[str, float]] = field(default_factory=list)  # (art, m²)
    adressen: set[str] = field(default_factory=set)
    strassen: set[str] = field(default_factory=set)
    namen: set[str] = field(default_factory=set)
    plz: set[str] = field(default_factory=set)
    orte: set[str] = field(default_factory=set)
    roh: set[str] = field(default_factory=set)  # Namen und Adressen in Originalschreibweise, für die Volltextsuche


@dataclass
class Bekanntmachung:
    nr: str
    datum: str
    form: str
    auftraggeber: list[str]
    titel: str
    lose: list[Los]
    quelle: str  # "api" oder "xml" oder "leer"

    def alle(self, attr: str) -> set:
        out = set()
        for los in self.lose:
            out |= set(getattr(los, attr))
        return out


def _texts(value) -> list[str]:
    if isinstance(value, dict):
        value = value.get("deu") or next(iter(value.values()), [])
    return [str(v) for v in flatten(value) if str(v).strip()]


def leistungsarten(text: str) -> set[str]:
    low = norm(text)
    arten = set()
    for art, pat in ARTEN.items():
        hits = [m for m in re.finditer(pat, low)]
        negated = [m for m in re.finditer(NEGATION + f"(?:{pat})", low)]
        if len(hits) > len(negated):
            arten.add(art)
    return arten


def flaechen(text: str) -> list[tuple[str, float]]:
    out = []
    for m in AREA_RE.finditer(text):
        whole = re.sub(r"[\.\s ]", "", m.group(1))
        value = float(whole + "." + (m.group(2) or "0"))
        if value < 10:
            continue
        before = norm(text[max(0, m.start() - 60):m.start()])
        art = "glas" if re.search(r"glas|fenster", before) else "boden"
        out.append((art, value))
    return out


def objektnamen(text: str) -> set[str]:
    names = set()
    for typ, name in NAME_AFTER.findall(text):
        words = []
        for w in norm(name).split():
            if w in STOP_NAMES or "reinigung" in w or w.isdigit():
                break  # der Name endet vor Leistungs- oder Füllwörtern
            words.append(w)
        if words:
            names.add(norm(typ) + " " + " ".join(words[:2]))
    typ_re = TYPWORT.replace("ö", "oe").replace("ä", "ae").replace("ü", "ue")
    for comp in COMPOUND.findall(text):
        n = norm(comp).replace(" ", "")
        if re.fullmatch(typ_re, n):
            continue
        prefix = re.sub(rf"(?:{typ_re})$", "", n)
        if len(prefix) >= 3 and prefix not in GENERIC_PREFIX:
            names.add(n)
    covered = {n.split()[0] for n in names}
    names |= {norm(t) for t in EINZELOBJEKT.findall(text) if norm(t) not in covered}
    return names


def suchbegriffe(text: str) -> set[str]:
    """Objektnamen (mindestens zwei Wörter oder zusammengesetzt) und Adressen in Originalschreibweise."""
    out = set()
    for typ, name in NAME_AFTER.findall(text):
        words = []
        for w in name.split():
            if norm(w) in STOP_NAMES or "reinigung" in norm(w) or norm(w).isdigit():
                break
            words.append(w.strip(".,;:"))
        if words:
            out.add(f"{typ} {' '.join(words[:2])}")
    out |= {c for c in COMPOUND.findall(text) if len(c) > 8}
    out |= {f"{s} {n}".strip() for s, n in ADDRESS_RE.findall(text) if len(norm_street(s)) >= 4}
    return {re.sub(r"[\"()\[\]]", "", o) for o in out}


def adressen(text: str) -> tuple[set[str], set[str]]:
    adr, streets = set(), set()
    for street, num in ADDRESS_RE.findall(text):
        s = norm_street(street)
        if len(s) < 4:
            continue
        streets.add(s)
        adr.add(f"{s} {norm_number(num)}")
    return adr, streets


def build_los(nr: str, titel: str, beschreibung: str, ort_text: str, plz: set[str], orte: set[str], cpv: str = "",
              verfahrenstitel: str = "") -> Los:
    """Leistungsart aus Lostitel, sonst Beschreibung, sonst CPV; Namen, Adressen, Flächen aus allen Texten des Loses
    (der Verfahrenstitel wird ergänzt, wenn er vom Lostitel abweicht, z. B. „… Altmarkt 1 und Altmarkt 16“)."""
    extra = verfahrenstitel if verfahrenstitel and norm(verfahrenstitel) not in norm(titel) else ""
    text = " ".join(t for t in (titel, extra, beschreibung, ort_text) if t)
    los = Los(nr=nr, titel=titel, text=text, plz=set(plz) | set(PLZ_RE.findall(ort_text + " " + titel)), orte=set(orte))
    # „fremd“ (z. B. Winterdienst als Nebenleistung) zählt nur aus Titeln, nicht aus der Beschreibung
    los.arten = leistungsarten(titel) or leistungsarten(extra) or (leistungsarten(beschreibung) - {"fremd"})
    if not los.arten and cpv in CPV_ART:
        los.arten = {CPV_ART[cpv]}
    los.flaechen = flaechen(text)
    if los.arten == {"glas"}:
        los.flaechen = [("glas", v) for _, v in los.flaechen]  # reines Glaslos: Flächen sind Glasflächen
    los.adressen, los.strassen = adressen(text)
    los.namen = objektnamen(text)
    los.roh = suchbegriffe(text)
    return los


def from_api(notice: dict) -> Bekanntmachung:
    titles = _texts(notice.get("title-lot"))
    descs = _texts(notice.get("description-lot"))
    proc_title = (_texts(notice.get("title-proc")) or [""])[0]
    proc_desc = (_texts(notice.get("description-proc")) or [""])[0]
    plz = [p for p in _texts(notice.get("place-of-performance-post-code-lot")) if PLZ_RE.fullmatch(p)]
    cities = [norm(c) for c in _texts(notice.get("place-of-performance-city-lot"))]
    streets = _texts(notice.get("place-performance-street-lot")) + _texts(notice.get("place-performance-streetline1-lot"))
    other = [o for o in _texts(notice.get("place-of-performance-other-lot")) if norm(o) not in PLACEHOLDERS]
    extra_info = [o for o in _texts(notice.get("place-of-performance-addtional-lot")) if norm(o) not in PLACEHOLDERS]
    cpvs = [str(c) for c in flatten(notice.get("main-classification-lot"))]
    n = max(len(titles), len(descs), 1)
    # Die API liefert Listen je Feld ohne Loszuordnung; bei gleicher Länge wird über den Index zugeordnet, sonst gemeinsam.
    lose = []
    for i in range(n):
        titel = titles[i] if len(titles) == n else (titles[0] if titles else proc_title)
        desc = descs[i] if len(descs) == n else " ".join(descs)
        ort = " ".join(([streets[i]] if len(streets) == n else streets) + ([other[i]] if len(other) == n else other)
                       + ([extra_info[i]] if len(extra_info) == n else extra_info))
        lp = {plz[i]} if len(plz) == n else set(plz)
        lo = {cities[i]} if len(cities) == n else set(cities)
        cpv = cpvs[i] if len(cpvs) == n else (cpvs[0] if cpvs else "")
        lose.append(build_los(str(i + 1), titel, desc, ort, lp, lo, cpv, proc_title))
    # Verfahrensbeschreibung ergänzt Namen und Adressen, wenn die Lose selbst keine nennen
    if proc_desc and not any(los.namen or los.adressen for los in lose):
        extra = build_los("V", proc_title, proc_desc, "", set(), set())
        for los in lose:
            los.namen |= extra.namen
            los.adressen |= extra.adressen
            los.strassen |= extra.strassen
            los.roh |= extra.roh
    return Bekanntmachung(
        nr=notice["publication-number"], datum=str(notice.get("publication-date", ""))[:10], form=str(notice.get("form-type", "")),
        auftraggeber=_texts(notice.get("buyer-name")), titel=proc_title, lose=lose, quelle="api",
    )


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def load_xml(pub: str) -> ET.Element | None:
    XML_DIR.mkdir(parents=True, exist_ok=True)
    path = XML_DIR / f"{pub}.xml"
    if not path.exists():
        for attempt in range(4):
            resp = requests.get(XML_URL.format(pub), timeout=60)
            if resp.status_code == 200:
                path.write_bytes(resp.content)  # unverändert speichern
                break
            time.sleep(2 ** (attempt + 1))
        else:
            return None
        time.sleep(PAUSE_SECONDS)
    try:
        return ET.fromstring(path.read_bytes())
    except ET.ParseError:
        return None


def _text(el: ET.Element | None) -> str:
    return re.sub(r"\s+", " ", " ".join(el.itertext())).strip() if el is not None else ""


def _child(el: ET.Element, name: str) -> ET.Element | None:
    return next((c for c in el if _local(c.tag) == name), None)


def from_xml(notice: dict) -> Bekanntmachung:
    """Lose aus der Original-XML vor eForms (Formulare F02, F03, F05, F06 …). Auftraggeber aus den API-Feldern."""
    nr = notice["publication-number"]
    base = dict(nr=nr, datum=str(notice.get("publication-date", ""))[:10], form=str(notice.get("form-type", "")),
                auftraggeber=_texts(notice.get("buyer-name")))
    root = load_xml(nr)
    if root is None:
        return Bekanntmachung(**base, titel="", lose=[], quelle="leer")
    forms = [e for e in root.iter() if re.fullmatch(r"F\d\d_2014", _local(e.tag))]
    form = next((f for f in forms if f.get("CATEGORY") == "ORIGINAL"), forms[0] if forms else root)
    oc = next((e for e in form.iter() if _local(e.tag) == "OBJECT_CONTRACT"), form)
    titel = _text(_child(oc, "TITLE"))
    proc_desc = _text(_child(oc, "SHORT_DESCR"))
    lose = []
    for i, od in enumerate(e for e in oc.iter() if _local(e.tag) == "OBJECT_DESCR"):
        lot_title = _text(_child(od, "TITLE")) or titel
        lot_no = _text(_child(od, "LOT_NO")) or str(i + 1)
        site = _text(_child(od, "MAIN_SITE"))
        desc = _text(_child(od, "SHORT_DESCR"))
        cpv_el = next((e for e in od.iter() if _local(e.tag) == "CPV_CODE"), None)
        cpv = cpv_el.get("CODE", "") if cpv_el is not None else ""
        lose.append(build_los(lot_no, lot_title, desc, site, set(), set(), cpv, titel))
    if not lose:
        lose = [build_los("1", titel, proc_desc, "", set(), set())]
    elif proc_desc and not any(los.namen or los.adressen for los in lose):
        extra = build_los("V", titel, proc_desc, "", set(), set())
        for los in lose:
            los.namen |= extra.namen
            los.adressen |= extra.adressen
            los.strassen |= extra.strassen
            los.roh |= extra.roh
    return Bekanntmachung(**base, titel=titel, lose=lose, quelle="xml")


def has_text_fields(notice: dict) -> bool:
    return bool(notice.get("description-lot") or notice.get("title-lot"))


def bekanntmachung(notice: dict) -> Bekanntmachung:
    return from_api(notice) if has_text_fields(notice) else from_xml(notice)


def _show(b: Bekanntmachung) -> None:
    print(f"== {b.nr} {b.datum} {b.form} ({b.quelle}) | {'; '.join(b.auftraggeber)[:60]}\n   {b.titel[:110]}")
    for los in b.lose:
        print(f"   Los {los.nr}: arten={sorted(los.arten)} plz={sorted(los.plz)} orte={sorted(los.orte)}")
        print(f"      namen={sorted(los.namen)}")
        print(f"      adressen={sorted(los.adressen)}  flaechen={los.flaechen[:4]}")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    pool = {}
    for run in sorted((PROJECT_ROOT / "data" / "raw" / "ted_search").glob("DEU_*")):
        if "_2026" not in run.name and "20161001" not in run.name:
            continue
        for f in sorted(run.glob("page_*.json")):
            for n in json.loads(f.read_bytes().decode("utf-8")).get("notices", []):
                pub = n["publication-number"]
                if pub not in pool or (n.get("description-lot") and not pool[pub].get("description-lot")):
                    pool[pub] = n  # die Fassung mit Beschreibungen (Lauf _lostext) hat Vorrang
    for pub in sys.argv[1:]:
        if pub not in pool:
            print(f"== {pub}: nicht in den Rohdaten")
            continue
        _show(bekanntmachung(pool[pub]))


if __name__ == "__main__":
    main()
