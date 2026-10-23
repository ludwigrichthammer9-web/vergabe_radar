"""Objektmerkmale einer Bekanntmachung für die Zuordnung über das Objekt (Iteration 3, Schritt 2).

Merkmale je Notice:
- buyer:   normalisierte Auftraggebernamen und deren kennzeichnende Wörter (ohne Allerweltswörter wie „Stadt“, „Amt“)
- words:   kennzeichnende Wörter aus Verfahrens- und Lostiteln (ohne Reinigungs- und Verfahrensvokabular)
- plz:     Postleitzahlen der Leistungsorte
- streets: Straßennamen der Leistungsorte (ohne Hausnummer)
- cities:  Orte der Leistungsorte bzw. des Auftraggebers

eForms-Notices: aus den API-Feldern (`title-proc`, `title-lot`, `place-of-performance-*`, `place-performance-street-lot`).
Notices vor eForms: Die API liefert keine Titel und Orte. Dann wird die Original-XML gelesen (TITLE, SHORT_DESCR, MAIN_SITE der Lose)
und unverändert unter data/raw/ted_xml/objekt/ zwischengespeichert. Nur für Kandidaten aufrufen, nicht für den ganzen Pool.
"""

import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

import requests

from analyze_completeness import flatten

PROJECT_ROOT = Path(__file__).resolve().parent.parent
XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml" / "objekt"
XML_URL = "https://ted.europa.eu/en/notice/{}/xml"
PAUSE_SECONDS = 0.5

UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})

# Wörter, die in fast jeder Reinigungsausschreibung oder in vielen Behördennamen vorkommen und daher nichts über das Objekt sagen
GENERIC = set("""
reinigung reinigungen reinigungsleistung reinigungsleistungen reinigungsdienstleistung reinigungsdienstleistungen
unterhaltsreinigung unterhaltsreinigungen unterhalts glasreinigung glas grundreinigung grund gebaeudereinigung gebaeudereinigungsleistungen
gebaeudeinnenreinigung gebaeudeinnen fensterreinigung fenster rahmenreinigung rahmen sonderreinigung sonderreinigungen
glasreinigungsleistungen unterhaltsreinigungsleistungen reinigungsarbeiten unterhaltsreinigungsarbeiten objektreinigung objektreinigungen
leistung leistungen dienstleistung dienstleistungen dienstleistungsvertrag dienstleistungsvertraege vergabe ausschreibung offenes offene
verfahren eu weit nach vgv uvgo vol los lose losen teil teillos rahmenvertrag rahmenvertraege rahmenvereinbarung vertrag vertraege
durchfuehrung erbringung beschaffung abschluss fuer und der die das des den dem von im in am an zur zum mit sowie bzw ab bis sowie
inkl einschl einschliesslich diverse diverser verschiedene verschiedenen objekte objekten objekt gebaeude gebaeuden liegenschaft
liegenschaften standort standorte standorten dienstgebaeude bereich bereiche bereichen laufende jahr jahre monate
uhr schule schulen grundschule grundschulen gymnasium realschule oberschule gesamtschule mittelschule igs kita kitas
kindertagesstaette kindertagesstaetten kindergarten sporthalle sporthallen turnhalle rathaus verwaltungsgebaeude
innen kehrreinigung zwischenreinigung jahresvertrag alle aller bedarf ueber sonder dienstleistungsvertraegen gmbh ggmbh
stadt gemeinde landkreis staedtische einrichtungen flaechen fensterflaechen fensterbaenke bueros besprechungs aufenthaltsraeumen
inklusive verbrauchsmaterial deutschland justiz dienst sozialen sozialer arbeitsplaetze
""".split())
BUYER_GENERIC = set("""
stadt gemeinde landkreis kreis amt aemter der die das des fuer und von land freistaat bundesrepublik deutschland vertreten durch
vertreten verwaltung stadtverwaltung kreisverwaltung buergermeister oberbuergermeister landrat landratsamt magistrat zentrale vergabestelle
vergabestelle zentraler einkauf beschaffung beschaffungsamt fachbereich abteilung referat dezernat eigenbetrieb gmbh mbh ag aoer ev e v
hansestadt kreisstadt grosse landeshauptstadt bundesanstalt anstalt oeffentlichen rechts koerperschaft
""".split())

STREET_RE = re.compile(
    r"([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\.\-]*(?:straße|strasse|str\.|weg|platz|allee|ring|gasse|damm|ufer|chaussee|steig|pfad|markt|hof))"
    r"\s*\d", re.UNICODE)
PLZ_RE = re.compile(r"\b(\d{5})\b")


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower().translate(UMLAUTS)).strip()


def tokens(text: str, generic: set[str]) -> set[str]:
    """Kennzeichnende Wörter; Zusammensetzungen mit „reinigung“ (z. B. Gebäudeunterhaltsreinigung) gelten immer als allgemein."""
    return {t for t in norm(text).split() if len(t) > 2 and t not in generic and not t.isdigit() and "reinigung" not in t}


def norm_street(street: str) -> str:
    s = norm(street)
    s = re.sub(r"\b(strasse|str)\b", "str", s)
    s = re.sub(r"str$|strasse$", "str", s)
    return re.sub(r"\s*\d.*$", "", s).strip()


@dataclass
class Merkmale:
    buyer_names: set[str] = field(default_factory=set)
    buyer_words: set[str] = field(default_factory=set)
    words: set[str] = field(default_factory=set)
    plz: set[str] = field(default_factory=set)
    streets: set[str] = field(default_factory=set)
    cities: set[str] = field(default_factory=set)
    buyer_city_words: set[str] = field(default_factory=set)
    title: str = ""
    source: str = ""  # "api" oder "xml"


def _texts(value) -> list[str]:
    if isinstance(value, dict) and value.get("deu"):
        value = value["deu"]
    return [str(v) for v in flatten(value) if str(v).strip()]


def _buyer(notice: dict, m: Merkmale) -> None:
    for name in _texts(notice.get("buyer-name")):
        m.buyer_names.add(norm(name))
        m.buyer_words |= tokens(name, BUYER_GENERIC)
    for c in _texts(notice.get("buyer-city")):
        m.cities.add(norm(c))
        m.buyer_city_words |= set(norm(c).split())


def object_words(m: Merkmale) -> set[str]:
    """Kennzeichnende Wörter ohne Namen und Sitz des Auftraggebers (der Leistungsort bleibt erhalten)."""
    return m.words - m.buyer_words - m.buyer_city_words


def from_api(notice: dict) -> Merkmale:
    """Merkmale aus den Feldern der Such-API (vollständig nur bei eForms)."""
    m = Merkmale(source="api")
    _buyer(notice, m)
    titles = _texts(notice.get("title-proc")) + _texts(notice.get("title-lot"))
    m.title = titles[0] if titles else ""
    for t in titles:
        m.words |= tokens(t, GENERIC)
        m.plz |= set(PLZ_RE.findall(t))
        m.streets |= {norm_street(s) for s in STREET_RE.findall(t)}
    m.plz |= {p for p in _texts(notice.get("place-of-performance-post-code-lot")) if PLZ_RE.fullmatch(p)}
    m.streets |= {norm_street(s) for s in _texts(notice.get("place-performance-street-lot")) if norm_street(s)}
    m.cities |= {norm(c) for c in _texts(notice.get("place-of-performance-city-lot"))}
    for other in _texts(notice.get("place-of-performance-other-lot")):
        m.plz |= set(PLZ_RE.findall(other))
        m.streets |= {norm_street(s) for s in STREET_RE.findall(other)}
    return m


def has_object_fields(notice: dict) -> bool:
    return bool(notice.get("title-proc") or notice.get("title-lot"))


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


def from_xml(notice: dict) -> Merkmale:
    """Merkmale aus der Original-XML (für Notices vor eForms). Auftraggeber aus den API-Feldern."""
    m = Merkmale(source="xml")
    _buyer(notice, m)
    root = load_xml(notice["publication-number"])
    if root is None:
        return m
    form = next((e for e in root.iter() if re.fullmatch(r"F\d\d_2014", _local(e.tag))), root)
    texts = []
    for el in form.iter():
        name = _local(el.tag)
        if name in ("TITLE", "SHORT_DESCR", "MAIN_SITE"):
            txt = re.sub(r"\s+", " ", " ".join(el.itertext())).strip()
            if txt:
                texts.append((name, txt))
    titles = [t for n, t in texts if n == "TITLE"]
    m.title = titles[0] if titles else ""
    for name, txt in texts:
        if name == "TITLE":
            m.words |= tokens(txt, GENERIC)
        m.plz |= set(PLZ_RE.findall(txt))
        m.streets |= {norm_street(s) for s in STREET_RE.findall(txt)}
        if name == "MAIN_SITE":
            m.words |= tokens(txt, GENERIC) - {"deutschland"}
    return m


def merkmale(notice: dict) -> Merkmale:
    return from_api(notice) if has_object_fields(notice) else from_xml(notice)
