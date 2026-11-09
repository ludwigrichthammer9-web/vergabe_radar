"""Referenz-Export der Vertragsliste (Oberpfalz) nach festem Schema, Version 1.1 (Schema: docs/export_schema.md).

Zweck: Datenübergabe in ein Verwaltungssystem (Excel, ERP, CRM, Kalkulationssoftware). Die Webseite stellt dieselben Daten nur dar.
Eingaben: reports/beispiel_liste_oberpfalz.csv (Liste, Fassung der Iteration 9), reports/wettbewerbsbild_oberpfalz.csv (Paket A),
          reports/beispiel_liste.md (nur für den Stand der Daten), reports/wettbewerbsbild_oberpfalz.md (Kontrollzählungen).
Ausgabe:  docs/prototyp/export/vertragsliste_v1.csv      (Komma, RFC 4180, UTF-8 ohne BOM, Zeilenende CRLF)
          docs/prototyp/export/vertragsliste_v1_de.csv   (Semikolon, UTF-8 mit BOM, für deutsches Excel)
          docs/prototyp/export/vertragsliste_v1.json     (Objekt mit meta und eintraege; region_nuts3 und region_name als Arrays)
Option:   --ohne-auftragnehmer erzeugt zusätzlich denselben Dateisatz ohne die Spalte auftragnehmer
          (vertragsliste_v1_ohne_auftragnehmer.csv, ..._de.csv, ....json), ebenfalls validiert.
Aufruf:   .venv\\Scripts\\python.exe -I src/report/export_vertragsliste.py [--ohne-auftragnehmer]
Danach läuft eine Validierung gegen das Schema; bei Fehlern bricht das Skript mit Exit-Code 1 ab.
Keine Terminprognose: ende_grundlaufzeit ist das Ende laut Bekanntmachung, kein Termin der Neuausschreibung.
"""

import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from webseite import NUTS, SONDER  # noqa: E402  (Regionsnamen und Sonderhinweise, eine Quelle für Seite und Export)

ROOT = Path(__file__).resolve().parent.parent.parent
LISTE = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
WETTB = ROOT / "reports" / "wettbewerbsbild_oberpfalz.csv"
WETTB_MD = ROOT / "reports" / "wettbewerbsbild_oberpfalz.md"
LISTE_MD = ROOT / "reports" / "beispiel_liste.md"
OUT = ROOT / "docs" / "prototyp" / "export"

SCHEMA_VERSION = "1.1"
QUELLE = "TED (Tenders Electronic Daily), Zuschlagsbekanntmachung; Ende und Herkunft aus der Vertragsliste, Auftragnehmer/Wert/Angebote aus dem eForms-XML"
HINWEIS_META = ("Keine Prognose: ende_grundlaufzeit ist das Ende der Grundlaufzeit laut Bekanntmachung, kein Termin der Neuausschreibung; "
                "hoechstende_hinweis ist nur ein Hinweis (bei hoechstende_herkunft keine_angabe oder keine_verlaengerung steht dort ersatzweise das Ende der Grundlaufzeit). "
                "Nur TED-Lose oberhalb der EU-Schwelle. Vor einer Entscheidung die Bekanntmachung (ted_link) lesen. "
                "TED als Quelle angeben; Lizenz laut TED-Rechtshinweis, Wortlaut am 06.11.2026 gelesen (docs/quellen.md).")

# Reihenfolge = Spaltenreihenfolge in CSV und JSON (Tabelle in docs/export_schema.md). Typ: s = Text, d = Datum, i = ganze Zahl, n = Dezimalzahl, b = true/false
# los_kennung (seit 1.1) steht als neues optionales Feld am Ende (Änderungsregel für Nebenversionen: nur neue Felder am Ende).
SPALTEN = [("schema_version", "s", True), ("stand_daten", "d", True), ("bekanntmachung", "s", True), ("ted_link", "s", True), ("veroeffentlicht", "d", True),
           ("los", "i", True), ("los_titel", "s", True), ("auftraggeber", "s", True), ("region_nuts3", "s", True), ("region_name", "s", True),
           ("leistungsort_auch_ausserhalb", "b", True), ("beginn", "d", False), ("ende_grundlaufzeit", "d", False), ("ende_herkunft", "s", True),
           ("hoechstende_hinweis", "d", False), ("hoechstende_herkunft", "s", True), ("stufe", "s", True), ("status_stand", "s", True),
           ("auftragnehmer", "s", False), ("wert_eur", "n", False), ("wert_status", "s", True), ("angebote_gesamt", "i", False),
           ("angebote_untergrenze", "i", False), ("hinweis", "s", False), ("quelle", "s", True), ("los_kennung", "s", False)]
NAMEN = [s[0] for s in SPALTEN]
NAMEN_OHNE_AN = [k for k in NAMEN if k != "auftragnehmer"]
TYP = {s[0]: s[1] for s in SPALTEN}
PFLICHT = [s[0] for s in SPALTEN if s[2]]
LISTENFELDER = ("region_nuts3", "region_name")  # im JSON Arrays, in der CSV mit | getrennter Text
SCHLUESSEL = ["bekanntmachung", "los_kennung"]

ENDE_HERKUNFT = {"enddatum", "text_zunaechst", "text_festlaufzeit", "beginn_plus_dauer", "geschaetzt", "unbekannt"}
HOECHSTENDE_HERKUNFT = {"datum_text", "enddatum_ist_hoechstende", "anzahl_x_laenge", "hoechstlaufzeit_text", "keine_verlaengerung",
                        "keine_angabe", "unbestimmbar", "keine_grundlaufzeit"}
STUFEN = set("ABCDEF")
WERT_STATUS = {"angegeben", "platzhalter", "fehlt", "zurueckgehalten", "kein_gewinnergebot", "gemeinsam_mehrere_lose", "angegeben_mehrere_gewinner"}
# Hinweise je Bekanntmachung: SONDER aus webseite.py (Fehlertyp „Dauerfeld enthält die Option“, reports/stufe_f_fehlertyp.csv, Paket C;
# in den 130 Losen: 527230-2026 und 533946-2026), damit Seite und Export dieselben Hinweise zeigen
HINWEISE = dict(SONDER)


def lies(pfad: Path) -> list[dict]:
    with pfad.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def stand_daten() -> str:
    m = re.search(r"Stand (\d{2})\.(\d{2})\.(\d{4})", LISTE_MD.read_text(encoding="utf-8"))
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"


def zahl(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def baue_zeilen() -> list[dict]:
    """Je Los der Liste eine Zeile nach Schema (Werte als Text oder None; leer = None). Verknüpfung mit dem Wettbewerbsbild über (Bekanntmachung, Los)."""
    stand = stand_daten()
    wb = {(r["notice"], int(r["los"])): r for r in lies(WETTB)}
    zeilen = []
    for r in lies(LISTE):
        w = wb.get((r["notice"], int(r["los"])))
        if w is None:
            raise SystemExit(f"Kein Wettbewerbsbild für {r['notice']} Los {r['los']}")
        codes = r["nuts"].split()
        # Ende: bekanntes Ende, sonst die Schätzung (Veröffentlichung + Dauer, Stufe E), sonst leer
        if r["gl_ende"]:
            ende, herk = r["gl_ende"], r["gl_herkunft"]
        elif r["gl_geschaetzt"]:
            ende, herk = r["gl_geschaetzt"], "geschaetzt"
        else:
            ende, herk = "", "unbekannt"
        # Wert: nur echte Werte über 1 EUR; Platzhalter nie als Wert
        wert, ws = None, w["wert_status"]
        if ws == "angegeben":
            v = zahl(w["wert_eur"])
            if v is not None and v > 1:
                wert = f"{v:.2f}"
            else:
                ws = "platzhalter"
        elif w["wert_zurueckgehalten"] == "True":
            ws = "zurueckgehalten"
        gewinner = w["gewinner"] if w["gewinner"] and w["mehrfachgewinner"] != "True" else ""
        gesamt = untergrenze = None
        if w["angebote_status"] == "angegeben":
            gesamt = str(int(float(w["angebote"])))
        elif w["angebote_status"] == "nur_elektronisch":
            untergrenze = str(int(float(w["angebote_elektronisch"])))
        z = {"schema_version": SCHEMA_VERSION, "stand_daten": stand, "bekanntmachung": r["notice"], "ted_link": r["ted_link"],
             "veroeffentlicht": r["veroeffentlicht"], "los": str(int(r["los"])), "los_titel": r["los_titel"], "auftraggeber": r["auftraggeber"],
             "region_nuts3": "|".join(codes), "region_name": "|".join(NUTS.get(c, c) for c in codes),
             "leistungsort_auch_ausserhalb": "true" if r["auch_ausserhalb"] == "True" else "false",
             "beginn": r["beginn"], "ende_grundlaufzeit": ende, "ende_herkunft": herk,
             "hoechstende_hinweis": r["hoechstende"], "hoechstende_herkunft": r["hoechstende_herkunft"], "stufe": r["stufe"], "status_stand": r["status"],
             "auftragnehmer": gewinner, "wert_eur": wert, "wert_status": ws, "angebote_gesamt": gesamt, "angebote_untergrenze": untergrenze,
             "hinweis": HINWEISE.get(r["notice"], ""), "quelle": QUELLE, "los_kennung": w["los_zugeordnet"]}
        zeilen.append({k: (None if z[k] in ("", None) else z[k]) for k in NAMEN})
    return zeilen


def csv_text(zeilen: list[dict], sep: str, namen: list = None) -> str:
    """CSV nach RFC 4180: Felder mit Trennzeichen, Anführungszeichen oder Zeilenumbruch in Anführungszeichen, Zeilenende CRLF, leer = leeres Feld."""
    namen = namen or NAMEN

    def q(v):
        s = "" if v is None else str(v)
        return '"' + s.replace('"', '""') + '"' if re.search(r'[%s"\r\n]' % re.escape(sep), s) else s
    return "\r\n".join(sep.join(q(v) for v in row) for row in [namen] + [[z[k] for k in namen] for z in zeilen]) + "\r\n"


def typisiert(z: dict, namen: list = None) -> dict:
    o = {}
    for k in namen or NAMEN:
        v = z[k]
        if k in LISTENFELDER:
            o[k] = None if v is None else v.split("|")
        else:
            o[k] = None if v is None else int(v) if TYP[k] == "i" else float(v) if TYP[k] == "n" else (v == "true") if TYP[k] == "b" else v
    return o


def schreibe(zeilen: list[dict], namen: list = None, suffix: str = "", variante: str = "") -> None:
    namen = namen or NAMEN
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"vertragsliste_v1{suffix}.csv").write_bytes(csv_text(zeilen, ",", namen).encode("utf-8"))
    (OUT / f"vertragsliste_v1{suffix}_de.csv").write_bytes(b"\xef\xbb\xbf" + csv_text(zeilen, ";", namen).encode("utf-8"))
    meta = {"schema_version": SCHEMA_VERSION, "stand_daten": zeilen[0]["stand_daten"], "erzeugt": date.today().isoformat(), "quelle": QUELLE,
            "hinweis": HINWEIS_META, "schema": "docs/export_schema.md", "schluessel": SCHLUESSEL, "zeilen": len(zeilen), "felder": len(namen)}
    if variante:
        meta["variante"] = variante
    (OUT / f"vertragsliste_v1{suffix}.json").write_text(
        json.dumps({"meta": meta, "eintraege": [typisiert(z, namen) for z in zeilen]}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def kontrollzahl(md: str, label: str) -> int:
    m = re.search(r"\*\*" + re.escape(label) + r"[^|]*\|\s*(\d+) von 130", md)
    if not m:
        raise SystemExit(f"Kontrollzahl '{label}' nicht in {WETTB_MD.name} gefunden")
    return int(m.group(1))


def validiere(zeilen: list[dict]) -> list[str]:
    fehler = []

    def f(msg):
        fehler.append(msg)
    iso = lambda s: bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", s)) and bool(datetime.strptime(s, "%Y-%m-%d"))
    for i, z in enumerate(zeilen, 1):
        tag = f"Zeile {i} ({z['bekanntmachung']}/{z['los_kennung']})"
        for k in PFLICHT:
            if z[k] is None:
                f(f"{tag}: Pflichtfeld {k} leer")
        for k in NAMEN:
            v = z[k]
            if v is None:
                continue
            try:
                if TYP[k] == "d" and not iso(v):
                    f(f"{tag}: {k} kein ISO-Datum: {v}")
                elif TYP[k] == "i" and (not re.fullmatch(r"\d+", v) or int(v) < 0):
                    f(f"{tag}: {k} keine ganze Zahl: {v}")
                elif TYP[k] == "n" and not re.fullmatch(r"\d+(\.\d{1,2})?", v):
                    f(f"{tag}: {k} kein Dezimalpunkt-Format: {v}")
                elif TYP[k] == "b" and v not in ("true", "false"):
                    f(f"{tag}: {k} nicht true/false: {v}")
            except ValueError:
                f(f"{tag}: {k} ungültiges Datum: {v}")
            if v in ("–", "-", "n/a", "NA", "null", "None", "nan"):
                f(f"{tag}: {k} Platzhaltertext statt leer: {v}")
        if z["wert_eur"] is not None and float(z["wert_eur"]) <= 1:
            f(f"{tag}: wert_eur ist Platzhalter (<= 1 EUR)")
        if (z["wert_eur"] is not None) != (z["wert_status"] == "angegeben"):
            f(f"{tag}: wert_eur und wert_status passen nicht zusammen")
        if z["angebote_gesamt"] is not None and z["angebote_untergrenze"] is not None:
            f(f"{tag}: angebote_gesamt und angebote_untergrenze zugleich gefüllt")
        if z["schema_version"] != SCHEMA_VERSION:
            f(f"{tag}: schema_version {z['schema_version']}")
        for k, erlaubt in (("ende_herkunft", ENDE_HERKUNFT), ("hoechstende_herkunft", HOECHSTENDE_HERKUNFT), ("stufe", STUFEN), ("wert_status", WERT_STATUS)):
            if z[k] is not None and z[k] not in erlaubt:
                f(f"{tag}: {k} = {z[k]!r} nicht erlaubt")
        if z["ende_grundlaufzeit"] is None and z["stufe"] != "F":
            f(f"{tag}: ende_grundlaufzeit leer, aber Stufe {z['stufe']} (nur Stufe F ohne Ende)")
        if z["ende_grundlaufzeit"] is not None and z["stufe"] == "F":
            f(f"{tag}: Stufe F, aber ende_grundlaufzeit gefüllt")
        if z["region_nuts3"] and len(z["region_nuts3"].split("|")) != len(z["region_name"].split("|")):
            f(f"{tag}: Zahl der Regionscodes und Regionsnamen verschieden")
        if z["los_kennung"] is not None and not re.fullmatch(r"LOT-\d{4}", z["los_kennung"]):
            f(f"{tag}: los_kennung {z['los_kennung']!r} nicht im Format LOT-0000")
        if z["los_kennung"] is None:
            f(f"{tag}: los_kennung leer (in den 130 Losen erwartet gefüllt)")
        # Regel zu hoechstende_hinweis: bei keine_angabe/keine_verlaengerung ersatzweise das Ende der Grundlaufzeit
        if z["hoechstende_herkunft"] in ("keine_angabe", "keine_verlaengerung") and z["hoechstende_hinweis"] != z["ende_grundlaufzeit"]:
            f(f"{tag}: hoechstende_herkunft {z['hoechstende_herkunft']}, aber hoechstende_hinweis weicht vom Ende der Grundlaufzeit ab")
    for name in (("bekanntmachung", "los"), ("bekanntmachung", "los_kennung")):
        schluessel = [tuple(z[k] for k in name) for z in zeilen]
        if len(set(schluessel)) != len(schluessel):
            f(f"Schlüssel {name} nicht eindeutig")
    if len(zeilen) != 130:
        f(f"Zeilenzahl {len(zeilen)} statt 130")
    md = WETTB_MD.read_text(encoding="utf-8")
    ist = {"Auftragnehmer genannt": sum(z["auftragnehmer"] is not None for z in zeilen),
           "Zuschlagswert je Los > 1": sum(z["wert_eur"] is not None for z in zeilen),
           "Zahl der Angebote angegeben": sum(z["angebote_gesamt"] is not None for z in zeilen)}
    soll = {k: kontrollzahl(md, k) for k in ist}
    for k in ist:
        if ist[k] != soll[k]:
            f(f"Zählung '{k}': Export {ist[k]}, {WETTB_MD.name} {soll[k]}")
    print(f"Zeilen: {len(zeilen)} (Soll 130); eindeutige Schlüssel (bekanntmachung, los_kennung): {len({(z['bekanntmachung'], z['los_kennung']) for z in zeilen})}; "
          f"Bekanntmachungen: {len({z['bekanntmachung'] for z in zeilen})}")
    for k in ist:
        print(f"Zählung {k}: Export {ist[k]}, Bericht {soll[k]}")
    print("Zusatz: Endedatum gefüllt", sum(z["ende_grundlaufzeit"] is not None for z in zeilen),
          "| Hinweis gefüllt", sum(z["hinweis"] is not None for z in zeilen),
          "| Gesamtzahl Angebote", sum(z["angebote_gesamt"] is not None for z in zeilen),
          "| nur Untergrenze", sum(z["angebote_untergrenze"] is not None for z in zeilen),
          "| los_kennung gefüllt", sum(z["los_kennung"] is not None for z in zeilen))
    return fehler


def pruefe_dateien(zeilen: list[dict], namen: list = None, suffix: str = "") -> list[str]:
    """Lädt die erzeugten Dateien mit csv, pandas und json und vergleicht sie mit den Zeilen."""
    import pandas as pd
    namen = namen or NAMEN
    fehler = []
    soll = [[("" if z[k] is None else z[k]) for k in namen] for z in zeilen]
    roh = (OUT / f"vertragsliste_v1{suffix}.csv").read_bytes()
    rohde = (OUT / f"vertragsliste_v1{suffix}_de.csv").read_bytes()
    if roh.startswith(b"\xef\xbb\xbf") or not rohde.startswith(b"\xef\xbb\xbf"):
        fehler.append("BOM falsch: Komma-Datei muss ohne, deutsche Datei mit BOM sein")
    for name, enc, sep in ((f"vertragsliste_v1{suffix}.csv", "utf-8", ","), (f"vertragsliste_v1{suffix}_de.csv", "utf-8-sig", ";")):
        p = OUT / name
        with p.open(encoding=enc, newline="") as fh:
            rows = list(csv.reader(fh, delimiter=sep))
        if rows[0] != namen or rows[1:] != soll:
            fehler.append(f"{name}: csv-Modul liest andere Werte als geschrieben")
        df = pd.read_csv(p, sep=sep, encoding=enc, dtype=str, keep_default_na=False)
        if list(df.columns) != namen or df.shape != (len(zeilen), len(namen)) or df.values.tolist() != soll:
            fehler.append(f"{name}: pandas liest andere Werte als geschrieben")
        dt = pd.read_csv(p, sep=sep, encoding=enc)
        if dt["los"].dtype.kind != "i" or dt["wert_eur"].dtype.kind != "f" or dt["wert_eur"].notna().sum() != sum(z["wert_eur"] is not None for z in zeilen):
            fehler.append(f"{name}: pandas-Typen (los ganzzahlig, wert_eur Dezimalzahl) stimmen nicht")
        if "auftragnehmer" in namen and "auftragnehmer" not in df.columns or "auftragnehmer" not in namen and "auftragnehmer" in df.columns:
            fehler.append(f"{name}: Spalte auftragnehmer passt nicht zur Variante")
        print(f"Laden {name}: csv-Modul {len(rows) - 1} Zeilen x {len(rows[0])} Spalten; pandas {df.shape}; wert_eur befüllt {int(dt['wert_eur'].notna().sum())}; "
              f"Umlaut-Probe: {'Universität' in ' '.join(df['auftraggeber'])}")
    j = json.loads((OUT / f"vertragsliste_v1{suffix}.json").read_text(encoding="utf-8"))
    if j["meta"]["zeilen"] != len(zeilen) or len(j["eintraege"]) != len(zeilen) or [list(e) for e in j["eintraege"]][0] != namen:
        fehler.append("JSON: Zeilenzahl oder Feldnamen stimmen nicht")
    if j["meta"]["schluessel"] != SCHLUESSEL or j["meta"]["felder"] != len(namen):
        fehler.append("JSON: meta (Schlüssel, Zahl der Felder) stimmt nicht")
    if [typisiert(z, namen) for z in zeilen] != j["eintraege"]:
        fehler.append("JSON: Einträge weichen von den Zeilen ab")
    if not all(isinstance(e["region_nuts3"], list) and isinstance(e["region_name"], list) and len(e["region_nuts3"]) == len(e["region_name"])
               for e in j["eintraege"]):
        fehler.append("JSON: region_nuts3/region_name keine Arrays gleicher Länge")
    if "auftragnehmer" not in namen and any("auftragnehmer" in e for e in j["eintraege"]):
        fehler.append("JSON (ohne Auftragnehmer): Feld auftragnehmer vorhanden")
    print(f"Laden vertragsliste_v1{suffix}.json: meta + {len(j['eintraege'])} Einträge; Schlüssel meta: {', '.join(j['meta'])}; "
          f"Arrays mit mehreren Regionen: {sum(len(e['region_nuts3']) > 1 for e in j['eintraege'])}")
    return fehler


RECHTSFORM = re.compile(r"(\bGmbH\b|\bmbH\b|\bAG\b|\bKG\b|\bOHG\b|\bGbR\b|\bUG\b|\bSE\b|\be\.\s?V\.|\beG\b|&\s*Co\b|\bAnstalt\b|\bK.rperschaft\b|\bKGaA\b|\be\.\s?K\.)", re.I)


def namenpruefung(zeilen: list[dict]) -> None:
    """Datenschutz-Vorprüfung (docs/export_schema.md, Abschnitt 8): nur Zahlen, keine Namen. Textmuster für Rechtsformen, nicht abschließend."""
    namen = [z["auftragnehmer"] for z in zeilen if z["auftragnehmer"]]
    ohne = {n for n in set(namen) if not RECHTSFORM.search(n)}
    ek = {n for n in set(namen) if re.search(r"\be\.\s?K\.", n, re.I)}
    print(f"Namenprüfung: {len(namen)} Lose mit Namen, {len(set(namen))} verschiedene Namen, {len(set(namen)) - len(ohne)} mit erkennbarer Rechtsform "
          f"(davon {len(ek)} e. K.), {len(ohne)} ohne (zusammen {sum(n in ohne for n in namen)} Lose); nicht abschließend, keine Namen ausgegeben")


def main() -> None:
    zeilen = baue_zeilen()
    namenpruefung(zeilen)
    fehler = validiere(zeilen)
    if fehler:
        print("VALIDIERUNG FEHLGESCHLAGEN:", *fehler[:30], sep="\n  ")
        sys.exit(1)
    schreibe(zeilen)
    fehler = pruefe_dateien(zeilen)
    if "--ohne-auftragnehmer" in sys.argv[1:]:
        schreibe(zeilen, NAMEN_OHNE_AN, "_ohne_auftragnehmer", "ohne_auftragnehmer")
        fehler += pruefe_dateien(zeilen, NAMEN_OHNE_AN, "_ohne_auftragnehmer")
        print(f"Variante ohne Auftragnehmer: {len(NAMEN_OHNE_AN)} Felder (Spalte auftragnehmer entfernt)")
    if fehler:
        print("DATEIPRÜFUNG FEHLGESCHLAGEN:", *fehler, sep="\n  ")
        sys.exit(1)
    print(f"Validierung gegen Schema {SCHEMA_VERSION} bestanden;", OUT)


if __name__ == "__main__":
    main()
