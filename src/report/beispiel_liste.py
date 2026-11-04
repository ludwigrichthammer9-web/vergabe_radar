"""Iteration 6, Schritt 5 (Phase 6): Prototyp der Vertragsliste für eine Region (Oberpfalz, NUTS DE23) mit Quelle und Unsicherheit je Eintrag (Y4).

Eingaben (keine neue API-Abfrage):
- data/processed/vertragsliste_909.csv aus src/prepare/vertragsliste.py (Ende der Grundlaufzeit, Höchstende, Herkunft je Los)
- data/raw/ted_search/zielgruppe_oberpfalz_20261023/page_0001.json (unverändert gespeicherter Abruf mit Leistungsort
  place-of-performance-subdiv-lot = DE23*, Zuschläge 25.10.2023 bis 23.10.2026; deckt den Zeitraum der Liste ab)
- Prüfung der Stichprobe (src/prepare/auswertung_iteration6.bewertung) für die Fehlerquote je Unsicherheitsstufe

Regeln
1. Region je Los: NUTS-Codes der Bekanntmachung werden wie in vertragsliste.je_los den Losen zugeordnet. Ein Los gehört zur Liste,
   wenn sein Code mit DE23 beginnt. Ist die Liste nicht eindeutig (die Such-API liefert alle Leistungsorte als flache Liste, ein Los
   kann mehrere haben), werden die Codes je Los aus dem eForms-XML gelesen (ProcurementProjectLot/RealizedLocation/
   CountrySubentityCode; Adresse aus dem Feld `links` der API-Antwort, XML unverändert in data/raw/ted_xml/beispiel_liste_20261104/).
   Das Los gehört dazu, wenn mindestens einer seiner Codes mit DE23 beginnt. Zuordnung XML-Los zu Listen-Los über den Lostitel,
   sonst über die Reihenfolge. Scheitert das, bleiben alle Lose drin und werden markiert („Region je Los unklar“).
2. Unsicherheitsstufe je Eintrag nach der Herkunft (Einteilung nach Kenntnis der Prüfergebnisse, also nachträglich):
   A Höchstende steht ausdrücklich im Text oder Feld; B Höchstende = Anzahl × Länge der Verlängerungen; C keine Angabe zur
   Verlängerung (Höchstende = Grundlaufzeit angenommen); D Verlängerung erwähnt, Länge offen; E Ende nur geschätzt
   (Veröffentlichung + Dauer, ungeprüft); F kein Ende bekannt.
3. Status zum Stichtag: Grundlaufzeit läuft; Verlängerungszeit möglich (Grundlaufzeit vorbei, Höchstende nicht); Verlängerung offen
   (Grundlaufzeit vorbei, Höchstende unbestimmbar); abgelaufen. Keine Terminprognose (Entscheidung Iteration 5).

Aufruf:  .venv\\Scripts\\python -I src/report/beispiel_liste.py
Ausgabe: reports/beispiel_liste.md, reports/beispiel_liste_oberpfalz.csv
"""

import csv
import json
import sys
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "src" / "prepare"))

from auswertung_iteration6 import bewertung, wilson  # noqa: E402
from vertragsliste import je_los  # noqa: E402

LISTE = ROOT / "data" / "processed" / "vertragsliste_909.csv"
REGION_RAW = ROOT / "data" / "raw" / "ted_search" / "zielgruppe_oberpfalz_20261023" / "page_0001.json"
XML_DIR = ROOT / "data" / "raw" / "ted_xml" / "beispiel_liste_20261104"
OUT_MD = ROOT / "reports" / "beispiel_liste.md"
OUT_CSV = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
REGION, REGION_NAME = "DE23", "Oberpfalz"
STICHTAG = date(2026, 11, 4)
TED = "https://ted.europa.eu/de/notice/-/detail/{}"
# Fehler, die erst nach der Auswertung auffielen (Evaluator, Abschluss Iteration 6; Prüfer und Liste nannten beide 30.06.2030, der Text
# sagt „2+1+1“, also Grundlaufzeit bis 30.06.2028). Die Auswertung (auswertung_iteration6.py) bleibt unverändert, hier wird nur korrigiert.
KORREKTUREN = {"L60": {"ok1": False}}

GL_TEXT = {"enddatum": "Enddatum (BT-537)", "beginn_plus_dauer": "Beginn + Dauer (BT-536 + BT-36)",
           "text_zunaechst": "Text „zunächst bis …“", "text_festlaufzeit": "Text „Festlaufzeit bis …“",
           "text_laufzeit_option": "Text: feste Dauer + Option", "unbekannt": "–", "unplausibel": "Felder unplausibel"}
H_TEXT = {"datum_text": "Datum im Text", "hoechstlaufzeit_text": "Höchstlaufzeit im Text", "bt36_laenger": "Dauer BT-36",
          "anzahl_x_laenge": "Anzahl × Länge der Verlängerungen", "keine_verlaengerung": "keine Verlängerung laut Text/BT-58",
          "keine_angabe": "keine Angabe zur Verlängerung", "unbestimmbar": "Verlängerung erwähnt, Länge offen",
          "enddatum_ist_hoechstende": "Enddatum ist laut Text das späteste Ende", "keine_grundlaufzeit": "–"}
STUFE_TEXT = {
    "A": "Höchstende steht ausdrücklich im Text oder Feld, oder das Ende der Grundlaufzeit wurde aus dem Text berichtigt",
    "B": "Höchstende berechnet aus Anzahl × Länge der Verlängerungen; das Enddatum kann schon das Höchstende sein",
    "C": "keine Angabe zur Verlängerung; Höchstende = Grundlaufzeit angenommen, Verlängerung im Volltext möglich",
    "D": "Verlängerung erwähnt, aber Länge oder Anzahl fehlt; Höchstende unbestimmbar",
    "E": "Ende nur geschätzt (Veröffentlichung + Dauer), ungeprüft",
    "F": "kein Ende in der Bekanntmachung",
}


TEXT_GL = {"text_zunaechst", "text_festlaufzeit", "text_laufzeit_option"}  # Ende der Grundlaufzeit aus dem Text berichtigt (Regeln 1a, 1b)


def stufe(r: dict) -> str:
    """Stufen A–F, für Iteration 7 vor dem Ziehen der Stichprobe festgelegt (2026-11-04): Ende der Grundlaufzeit aus dem Text → A; sonst nach
    Herkunft des Höchstendes (Anzahl × Länge → B, keine Angabe → C, unbestimmbar → D, alles andere → A); ohne Ende E (nur geschätzt) oder F."""
    if not r["gl_ende"]:
        return "E" if r.get("gl_geschaetzt") else "F"
    if r["gl_herkunft"] in TEXT_GL:
        return "A"
    return {"anzahl_x_laenge": "B", "keine_angabe": "C", "unbestimmbar": "D"}.get(r["hoechstende_herkunft"], "A")


def iso(s: str) -> date | None:
    return date.fromisoformat(s[:10]) if s else None


def status(r: dict) -> str:
    gl, h, g = iso(r["gl_ende"]), iso(r["hoechstende"]), iso(r["gl_geschaetzt"])
    ende = gl or g
    if not ende:
        return "kein Ende bekannt"
    if ende >= STICHTAG:
        return "Grundlaufzeit läuft (geschätzt)" if not gl else "Grundlaufzeit läuft"
    if h and h >= STICHTAG:
        return "Verlängerungszeit möglich"
    if gl and r["hoechstende_herkunft"] == "unbestimmbar":
        return "Verlängerung offen"
    return "abgelaufen"


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _kind(el: ET.Element, name: str) -> ET.Element | None:
    return next((c for c in el if _local(c.tag) == name), None)


def xml_nuts(notice: dict, rows: list[dict]) -> list[list[str]] | None:
    """NUTS-Codes je Los aus dem eForms-XML, in der Reihenfolge von `rows`; None, wenn die Zuordnung nicht gelingt."""
    pub = notice["publication-number"]
    path = XML_DIR / f"{pub}.xml"
    if not path.exists():
        url = (notice.get("links") or {}).get("xml", {}).get("MUL")
        if not url:
            return None
        resp = requests.get(url, timeout=60)
        if resp.status_code != 200:
            print(f"  {pub}: HTTP {resp.status_code}")
            return None
        XML_DIR.mkdir(parents=True, exist_ok=True)
        path.write_bytes(resp.content)  # unverändert speichern
        time.sleep(0.5)
    lose = []
    for lot in (c for c in ET.fromstring(path.read_bytes()) if _local(c.tag) == "ProcurementProjectLot"):
        pp = _kind(lot, "ProcurementProject")
        if pp is None:
            continue
        name = " ".join("".join(_kind(pp, "Name").itertext()).split()) if _kind(pp, "Name") is not None else ""
        codes = [" ".join(e.itertext()).strip() for e in pp.iter() if _local(e.tag) == "CountrySubentityCode"]
        lose.append((name, codes))
    if len(lose) != len(rows):
        return None
    titel = [" ".join(r["los_titel"].split()) for r in rows]
    nach_titel = {n[:120]: c for n, c in lose}
    if len(nach_titel) == len(lose) and all(t in nach_titel for t in titel):
        return [nach_titel[t] for t in titel]
    return [c for _, c in lose]


def region_lose(liste: list[dict]) -> tuple[list[dict], dict]:
    """Lose der Liste mit Leistungsort DE23* (Regel 1) und Kennzahlen zur Zuordnung."""
    notices = json.loads(REGION_RAW.read_text(encoding="utf-8"))["notices"]
    lose_je_notice = defaultdict(list)
    for r in liste:
        lose_je_notice[r["notice"]].append(r)
    out, info = [], {"bekanntmachungen": len(notices), "nicht_in_liste": [], "unklar": 0, "aus_xml": 0}
    for x in notices:
        rows = sorted(lose_je_notice.get(x["publication-number"], []), key=lambda r: int(r["los"]))
        if not rows:
            info["nicht_in_liste"].append(x["publication-number"])
            continue
        codes, eindeutig = je_los(x, "place-of-performance-subdiv-lot", len(rows))
        codes = [[c] if c else [] for c in codes]
        quelle = "api"
        if not eindeutig and (aus_xml := xml_nuts(x, rows)) is not None:
            codes, eindeutig, quelle = aus_xml, True, "xml"
            info["aus_xml"] += 1
        for r, cs in zip(rows, codes):
            drin = [c for c in cs if c.startswith(REGION)]
            if eindeutig and not drin:
                continue
            out.append({**r, "nuts": " ".join(dict.fromkeys(cs)), "region_eindeutig": eindeutig, "nuts_quelle": quelle,
                        "auch_ausserhalb": eindeutig and len(drin) < len(cs)})
            info["unklar"] += not eindeutig
    return out, info


def stichprobe() -> list[dict]:
    rows, _ = bewertung()
    return [{**r, **KORREKTUREN.get(r["L"], {})} for r in rows]


def stufen_stichprobe(rows: list[dict]) -> dict[str, tuple[int, int, int]]:
    """Je Stufe: Lose der Stichprobe, davon Ende der Grundlaufzeit korrekt (Y1), Höchstende korrekt (Y2)."""
    out = defaultdict(lambda: [0, 0, 0])
    for r in rows:
        s = out[stufe(r)]
        s[0] += 1
        s[1] += r["ok1"]
        s[2] += r["ok2"]
    return {k: tuple(v) for k, v in out.items()}


def zelle(s: str, n: int = 60) -> str:
    s = " ".join(str(s).split()).replace("|", "/")
    return s if len(s) <= n else s[: n - 1] + "…"


def de(d: str) -> str:
    return f"{d[8:10]}.{d[5:7]}.{d[:4]}" if d else "–"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    with LISTE.open(encoding="utf-8") as f:
        liste = list(csv.DictReader(f, delimiter=";"))
    lose, info = region_lose(liste)
    for r in lose:
        r["stufe"], r["status"] = stufe(r), status(r)
    lose.sort(key=lambda r: (r["gl_ende"] or r["gl_geschaetzt"] or "9999", r["notice"], int(r["los"])))
    stich_rows = stichprobe()
    stich = stufen_stichprobe(stich_rows)
    in_region = {(r["notice"], str(r["los"])) for r in lose}
    geprueft = [r["L"] for r in stich_rows if (r["notice"], str(r["los"])) in in_region]
    k_gl = sum(r["ok1"] for r in stich_rows)

    felder = ["notice", "ted_link", "veroeffentlicht", "auftraggeber", "los", "los_titel", "nuts", "nuts_quelle", "region_eindeutig", "auch_ausserhalb", "beginn",
              "gl_ende", "gl_herkunft", "hoechstende", "hoechstende_herkunft", "gl_geschaetzt", "stufe", "status", "liste_eindeutig"]
    with OUT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=felder, delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows({**r, "ted_link": TED.format(r["notice"])} for r in lose)

    def zeile(r: dict) -> str:
        gl = de(r["gl_ende"]) if r["gl_ende"] else (f"ca. {de(r['gl_geschaetzt'])} (geschätzt)" if r["gl_geschaetzt"] else "–")
        h = de(r["hoechstende"]) if r["hoechstende"] else ("unbestimmbar" if r["hoechstende_herkunft"] == "unbestimmbar" else "–")
        hinweise = []
        if not r["region_eindeutig"]:
            hinweise.append("Region je Los unklar")
        if r["auch_ausserhalb"]:
            hinweise.append("Leistungsorte auch außerhalb der Oberpfalz")
        if r["liste_eindeutig"] != "True":
            hinweise.append("Felder je Los unklar")
        herkunft = GL_TEXT.get(r["gl_herkunft"], r["gl_herkunft"]) if r["gl_ende"] else "–"
        if r["gl_ende"]:
            herkunft += " / " + H_TEXT.get(r["hoechstende_herkunft"], r["hoechstende_herkunft"])
        return (f"| {gl} | {h} | {r['status']} | {zelle(r['auftraggeber'], 45)} | {r['los']}: {zelle(r['los_titel'], 50)} | "
                f"**{r['stufe']}** | {herkunft}{' · ' + ', '.join(hinweise) if hinweise else ''} | [{r['notice']}]({TED.format(r['notice'])}) |")

    kopf = ["| Ende Grundlaufzeit | Höchstende | Status | Auftraggeber | Los | Stufe | Herkunft | Quelle |",
            "|---|---|---|---|---|---|---|---|"]
    laufend = [r for r in lose if r["status"] not in ("abgelaufen", "kein Ende bekannt")]
    rest = [r for r in lose if r not in laufend]
    zaehl = defaultdict(int)
    for r in lose:
        zaehl[r["stufe"]] += 1
    mit_ende = sum(1 for r in lose if r["gl_ende"])
    alle_stich = sum(v[0] for v in stich.values())

    def quote(k: int, n: int) -> str:
        if not n:
            return "–"
        lo, hi = wilson(k, n)
        return f"{k}/{n} ({100 * lo:.0f}–{100 * hi:.0f} %)".replace(".", ",")

    legende = ["| Stufe | Bedeutung | Einträge hier | Stichprobe: Lose | Ende GL korrekt | Höchstende korrekt |", "|---|---|---|---|---|---|"]
    for s in "ABCDEF":
        n, k1, k2 = stich.get(s, (0, 0, 0))
        legende.append(f"| **{s}** | {STUFE_TEXT[s]} | {zaehl[s]} | {n or '–'} | {quote(k1, n) if n else 'ungeprüft'} | "
                       f"{quote(k2, n) if n else 'ungeprüft'} |")

    md = [
        f"# Vertragsliste Gebäudereinigung {REGION_NAME} (Prototyp, Stand {STICHTAG.strftime('%d.%m.%Y')})",
        "",
        "_Erzeugt mit `src/report/beispiel_liste.py` (Iteration 6, Schritt 5). Tabelle zum Weiterverarbeiten: "
        f"[{OUT_CSV.name}]({OUT_CSV.name})._",
        "",
        "Die Liste zeigt öffentliche Aufträge der Gebäudereinigung mit Leistungsort in der Oberpfalz, wann ihre feste Laufzeit endet "
        "und wie lange sie höchstens verlängert werden können. **Sie sagt nicht voraus, wann neu ausgeschrieben wird**; eine solche "
        "Prognose hat sich in Iteration 5 als nicht tragfähig erwiesen.",
        "",
        "## Fakten",
        "",
        f"- Quelle: TED-Zuschlagsbekanntmachungen (eForms) ab 25.10.2023, Haupt-CPV 90910/90911/90919, Leistungsort NUTS {REGION}* "
        f"(Abruf vom 23.10.2026, `{REGION_RAW.relative_to(ROOT).as_posix()}`), Lese-Regeln aus `src/prepare/vertragsliste.py`.",
        f"- {info['bekanntmachungen']} Bekanntmachungen im Abruf, davon {len(info['nicht_in_liste'])} nicht in der Vertragsliste "
        f"(durch die Population von Iteration 4 ausgeschlossen: {', '.join(info['nicht_in_liste']) or '–'}).",
        f"- **{len(lose)} Lose** in der Region, davon {mit_ende} mit Ende der Grundlaufzeit aus den Feldern "
        f"({100 * mit_ende / len(lose):.1f} %)".replace(".", ",") + f"; {info['unklar']} Lose mit unklarer Region je Los. "
        f"Bei {info['aus_xml']} Bekanntmachungen ließ sich der Leistungsort nur über das eForms-XML einem Los zuordnen; "
        f"{sum(1 for r in lose if r['auch_ausserhalb'])} Lose haben Leistungsorte auch außerhalb der Oberpfalz.",
        f"- Status zum {STICHTAG.strftime('%d.%m.%Y')}: " + ", ".join(
            f"{s} {sum(1 for r in lose if r['status'] == s)}" for s in
            ("Grundlaufzeit läuft", "Grundlaufzeit läuft (geschätzt)", "Verlängerungszeit möglich", "Verlängerung offen", "abgelaufen", "kein Ende bekannt")) + ".",
        f"- Genauigkeit insgesamt (Prüfung einer Zufallsstichprobe von {alle_stich} Losen aus ganz Deutschland, Iteration 6): Ende der "
        f"Grundlaufzeit laut Auswertung 54/60 = 90,0 % korrekt, nach einem später gefundenen Fehler (L60) {k_gl}/{alle_stich} = "
        f"{100 * k_gl / alle_stich:.1f}".replace(".", ",") + " %; Höchstende 91,7 % korrekt oder als unbestimmbar gekennzeichnet "
        "([liste_auswertung_iteration6.md](liste_auswertung_iteration6.md)). **Vorbehalt:** Das Feld „Hilfsmittel“ blieb leer "
        "(der Prüfer gibt mündlich an, ohne KI-Hilfe geprüft zu haben), und die Vorlage zeigte das Enddatum der Liste an; die Zahl ist "
        "eher eine Untergrenze der Fehler als eine Genauigkeit.",
        "",
        "### Unsicherheit je Eintrag (Spalte „Stufe“)",
        "",
        *legende,
        "",
        "_Die Einteilung in Stufen ist nach Kenntnis der Prüfergebnisse entstanden. Die Quoten je Stufe beruhen auf wenigen Losen (Klammer: "
        "95-%-Wilson-Intervall) und stammen überwiegend nicht aus der Oberpfalz. „Ende GL korrekt“ zählt einen Eintrag „unbekannt“ des "
        "Prüfers als Abweichung (L8, L48, L49, alle Stufe C) und enthält die Korrektur zu L60 (Stufe D). „Höchstende korrekt“ ist bei Stufe D "
        "per Definition 100 %, weil „unbestimmbar“ immer als korrekt zählt._",
        "",
        "## Laufende Verträge",
        "",
        "Sortiert nach dem Ende der Grundlaufzeit. „Verlängerungszeit möglich“: Die feste Laufzeit ist vorbei, der Vertrag kann aber "
        "noch bis zum Höchstende laufen. Ob verlängert wurde, steht nicht in TED.",
        "",
        *kopf,
        *[zeile(r) for r in laufend],
        "",
        "## Abgelaufen oder ohne Ende",
        "",
        "Bei „abgelaufen“ ist auch das Höchstende vorbei (bzw. bei Stufe C die Grundlaufzeit); eine Neuausschreibung kann schon "
        "veröffentlicht sein oder der Auftrag wurde anders weitergeführt.",
        "",
        *kopf,
        *[zeile(r) for r in rest],
        "",
        "## Interpretation",
        "",
        "- Die Spalte „Stufe“ macht sichtbar, wie verlässlich ein Eintrag ist. Fehler beim Ende der Grundlaufzeit traten in der "
        "Stichprobe vor allem auf, wenn das Enddatum der Bekanntmachung schon das Höchstende war (Stufe B, ein Fall in Stufe D); in "
        "Stufe C gab es drei Auslegungsfälle („unbekannt“ des Prüfers). Bei Stufe B, C und D lohnt ein Blick in die Bekanntmachung. "
        "Bekannte Fehler stehen weiter in der Liste, z. B. Bekanntmachung 143100-2026 (Autobahn GmbH): Dort steht die Festlaufzeit nur im "
        "Text, das Enddatum ist ein Jahr später.",
        "- Die Prüfung der Stichprobe ist durch den Prüfer mündlich als ohne KI-Hilfe angegeben, aber nicht in der Vorlage vermerkt; Teil B "
        "(Paare) stammte aus schon bekannten Paaren und zählt nicht. Die Zahlen sind deshalb vorläufig.",
        f"- Aus der Oberpfalz liegt {len(geprueft)} Los der Stichprobe vor ({', '.join(geprueft) or '–'}); mehr wurde dort nicht geprüft. "
        "Die Liste kommt ohne Kundentest aus (A1, A15 ungeprüft); ob diese Form für einen Mittelständler nützlich ist, bleibt offen.",
        "",
    ]
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"{len(lose)} Lose ({len(laufend)} laufend); Stufen {dict(sorted(zaehl.items()))}; Stichprobe {dict(sorted(stich.items()))}")
    print(f"{OUT_MD}\n{OUT_CSV}")


if __name__ == "__main__":
    main()
