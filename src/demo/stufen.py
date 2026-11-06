"""Demo Profil-Match: harte Filter (Stufen a und b), regelbasiertes Vergleichsurteil, Eignungs-Block, Vorgänger-Hinweis."""

import csv
import difflib
import math
import re
from collections import Counter
from datetime import timedelta

from daten import PROJECT_ROOT, volltext

# NUTS-3 Oberpfalz (DE231-DE23A). Näherung: Koordinaten der jeweiligen Kreisstadt (Stadtkreise: Stadt), NICHT der
# geometrische Mittelpunkt des Kreises. Entfernung = Luftlinie (Haversine). Fehler bei großen Landkreisen: bis ca. 20 km.
NUTS3_PUNKTE = {
    "DE231": ("Amberg (Stadt)", 49.4430, 11.8620),
    "DE232": ("Regensburg (Stadt)", 49.0134, 12.1016),
    "DE233": ("Weiden i. d. OPf. (Stadt)", 49.6765, 12.1561),
    "DE234": ("Amberg-Sulzbach (Sulzbach-Rosenberg)", 49.5008, 11.7419),
    "DE235": ("Cham", 49.2194, 12.6618),
    "DE236": ("Neumarkt i. d. OPf.", 49.2803, 11.4631),
    "DE237": ("Neustadt a. d. Waldnaab", 49.7295, 12.1735),
    "DE238": ("Regensburg (Landkreis)", 49.0134, 12.1016),
    "DE239": ("Schwandorf", 49.3257, 12.1056),
    "DE23A": ("Tirschenreuth", 49.8800, 12.3400),
}

EIGNUNG_LABEL = {  # Beschriftung von uns aus dem Code abgeleitet; Codeliste nicht Eintrag für Eintrag geprüft
    "slc-abil-ref-services": "Referenzen (Dienstleistungen)",
    "slc-stand-ins": "Versicherung",
    "slc-suit-reg-prof": "Berufsregister",
    "slc-suit-reg-trade": "Handelsregister",
    "slc-abil-staff-yrly-avg-mp": "Beschäftigtenzahl",
    "slc-stand-to-avg": "Durchschnittsumsatz",
    "slc-stand-to-spec": "Umsatz im Tätigkeitsbereich",
    "slc-stand-to-gen": "Gesamtumsatz",
    "slc-abil-staff-qual": "Qualifikation des Personals",
    "slc-abil-mgmt-qual": "Qualitätsmanagement",
    "slc-abil-mgmt-env": "Umweltmanagement",
    "slc-stand-other": "sonstige wirtschaftliche Anforderungen",
}


def haversine_km(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2
    return 2 * 6371.0 * math.asin(math.sqrt(a))


def dedupe(bekanntmachungen):
    """Mehrfachveröffentlichungen (gleicher Auftraggeber + gleicher Titel): nur die jüngste behalten (Näherung)."""
    neu = {}
    for b in sorted(bekanntmachungen, key=lambda x: (x["veroeffentlicht"], x["nr"])):
        neu[(b["auftraggeber"].strip().lower(), b["titel"].strip().lower())] = b
    return sorted(neu.values(), key=lambda x: (x["veroeffentlicht"], x["nr"]))


def in_oberpfalz(b):
    """Gibt ('nuts'|'plz'|None) zurück."""
    if any(n.startswith("DE23") for n in b["nuts"]):
        return "nuts"
    if not b["nuts"] and any(p[:2] in ("92", "93") for p in b["plz"]):
        return "plz"
    return None


def entfernung_km(profil, b):
    """Kleinste Entfernung Sitz -> NUTS-3-Punkt der Leistungsorte; None, wenn nicht berechenbar."""
    werte = [haversine_km(profil["sitz"]["lat"], profil["sitz"]["lon"], NUTS3_PUNKTE[n][1], NUTS3_PUNKTE[n][2])
             for n in b["nuts"] if n in NUTS3_PUNKTE]
    return round(min(werte), 1) if werte else None


def trichter(profil, bekanntmachungen_dedupliziert, stichtag, ohne_frist=False, ohne_radius=False):
    """Wendet die harten Filter an. Rückgabe: (Stufenliste, Treffer). Unbekannte Angaben bleiben im Trichter (markiert)."""
    stufen, menge = [], bekanntmachungen_dedupliziert

    def stufe(name, neu, notiz=""):
        stufen.append({"name": name, "anzahl": len(neu), "notiz": notiz})
        return neu

    menge = stufe("Gebäudereinigungs-CPV (Profil)", [b for b in menge if any(c.startswith(tuple(profil["cpv_praefixe"])) for c in b["cpv"])])
    menge = stufe("Oberpfalz (NUTS DE231-DE23A)", [b for b in menge if in_oberpfalz(b)],
                  f"davon nur über PLZ 92/93 erkannt: {sum(1 for b in menge if in_oberpfalz(b) == 'plz')}")
    for b in menge:
        b["_entfernung"] = entfernung_km(profil, b)
    im_radius = [b for b in menge if ohne_radius or b["_entfernung"] is None or b["_entfernung"] <= profil["radius_km"]]
    menge = stufe(f"Radius {profil['radius_km']} km um {profil['sitz']['ort']}", im_radius,
                  f"davon Entfernung nicht berechenbar (nur NUTS-2/PLZ): {sum(1 for b in im_radius if b['_entfernung'] is None)}")
    if not ohne_frist:  # ohne_frist nur für die Vergleichsmenge (KI gegen Regel)
        offen = [b for b in menge if not b["fristen"] or max(b["fristen"]) >= stichtag]
        menge = stufe("Abgabefrist noch offen", offen, f"davon Frist nicht angegeben: {sum(1 for b in offen if not b['fristen'])}")
    lang = [b for b in menge if not b["laufzeit_monate"] or max(b["laufzeit_monate"]) >= profil["laufzeit_min_monate"]]
    menge = stufe(f"Laufzeit mindestens {profil['laufzeit_min_monate']} Monate", lang,
                  f"davon Laufzeit im Datenfeld nicht angegeben: {sum(1 for b in lang if not b['laufzeit_monate'])}")
    n_wert = sum(1 for b in menge if b["wert_lose"] or b["wert_verfahren"])
    stufen.append({"name": "Info: Wert angegeben (kein Filter)", "anzahl": n_wert,
                   "notiz": f"bei {len(menge) - n_wert} von {len(menge)} Treffern ist kein Wert angegeben"})
    return stufen, menge


# ---------------------------------------------------------------- regelbasiertes Urteil (Vergleichsmaßstab)
def regel_urteil(profil, b):
    """Stichwortregel ohne Sprachmodell. Gibt (urteil, begruendung) zurück."""
    t = volltext(b).lower()
    entf = entfernung_km(profil, b)
    if entf is not None and entf > profil["radius_km"]:
        return "passt nicht", f"Entfernung ca. {entf:.0f} km größer als Radius {profil['radius_km']} km"
    treffer_l = [s for s in profil["leistung_stichworte"] if s in t]
    treffer_o = [s.strip() for s in profil["objekt_stichworte"] if s in t]
    werte = b["wert_verfahren"] or b["wert_lose"]
    if werte and (max(werte) > profil["wert_max_eur"] or max(werte) < profil["wert_min_eur"]):
        return "passt nicht", f"Wert {max(werte):,.0f} EUR außerhalb {profil['wert_min_eur']:,}-{profil['wert_max_eur']:,} EUR".replace(",", ".")
    if not treffer_l:
        return "passt nicht", "kein Stichwort der Profil-Leistungen im Text"
    if not treffer_o:
        return "unklar", f"Leistungsstichwort ({treffer_l[0]}), aber keine Profil-Objektart im Text"
    return "passt", f"Leistungsstichwort ({treffer_l[0]}) und Objektart ({treffer_o[0]}) im Text"


# ---------------------------------------------------------------- Eignungs-Block
def eignung_block(b):
    """Fakten aus Bekanntmachung: welche Arten von Nachweisen verlangt werden."""
    arten = [EIGNUNG_LABEL.get(c, c) for c in b["eignung_codes"]]
    return {
        "arten": arten,
        "codes": b["eignung_codes"],
        "hat_freitext": bool(b["eignung_text"]),
        "hinweis": "Schwellen und Zertifikate: nur soweit im Freitext der Bekanntmachung genannt, sonst nicht ablesbar (Vergabeunterlagen).",
    }


# ---------------------------------------------------------------- Vorgänger-Hinweis (optional)
def _norm(s):
    return re.sub(r"[^a-zäöüß0-9 ]+", " ", s.lower()).split()


def lade_liste():
    pfad = PROJECT_ROOT / "docs" / "prototyp" / "export" / "vertragsliste_v1_ohne_auftragnehmer.csv"
    with open(pfad, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def vorgaenger_hinweis(b, liste):
    """Nur bei eindeutigem Treffer: gleicher Auftraggeber (normalisiert) und genau ein Los mit Titelähnlichkeit.
    Eindeutig = bester Titel-Score >= 0.6 und mindestens 0.15 vor dem zweitbesten Los desselben Auftraggebers;
    gleiche Bekanntmachung mit mehreren Losen zählt als nicht eindeutig. Sonst None."""
    ag = " ".join(_norm(b["auftraggeber"]))
    kandidaten = [z for z in liste if " ".join(_norm(z["auftraggeber"])) == ag and z["ende_grundlaufzeit"]]
    if not kandidaten:
        return None
    titel_neu = [b["titel"], *b["titel_lose"]]
    bewertet = []
    for z in kandidaten:
        s = max(difflib.SequenceMatcher(None, " ".join(_norm(t)), " ".join(_norm(z["los_titel"]))).ratio() for t in titel_neu)
        bewertet.append((s, z))
    bewertet.sort(key=lambda x: -x[0])
    if bewertet[0][0] < 0.6:
        return None
    if len(bewertet) > 1 and bewertet[0][0] - bewertet[1][0] < 0.15:
        return None
    z = bewertet[0][1]
    return {"bekanntmachung": z["bekanntmachung"], "los_titel": z["los_titel"], "ende_grundlaufzeit": z["ende_grundlaufzeit"],
            "ende_herkunft": z["ende_herkunft"], "score": round(bewertet[0][0], 2), "link": z["ted_link"]}
