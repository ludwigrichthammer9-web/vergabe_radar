"""Iteration 7, Schritt 5 (Phase 6; Fassung der Iteration 6 neu erzeugt): Prototyp der Vertragsliste für eine Region (Oberpfalz, NUTS DE23) mit Quelle und Unsicherheit je Eintrag (Y4).

Eingaben (keine neue API-Abfrage):
- data/processed/vertragsliste_909.csv aus src/prepare/vertragsliste.py (Ende der Grundlaufzeit, Höchstende, Herkunft je Los)
- data/raw/ted_search/zielgruppe_oberpfalz_20261023/page_0001.json (unverändert gespeicherter Abruf mit Leistungsort
  place-of-performance-subdiv-lot = DE23*, Zuschläge 25.10.2023 bis 23.10.2026; deckt den Zeitraum der Liste ab)
- Prüfung der Stichprobe der Iteration 7 (src/prepare/auswertung_iteration7.bewertung, Typ Y, L1 bis L50) für die Fehlerquote je Unsicherheitsstufe

Regeln
1. Region je Los: NUTS-Codes der Bekanntmachung werden wie in vertragsliste.je_los den Losen zugeordnet. Ein Los gehört zur Liste,
   wenn sein Code mit DE23 beginnt. Ist die Liste nicht eindeutig (die Such-API liefert alle Leistungsorte als flache Liste, ein Los
   kann mehrere haben), werden die Codes je Los aus dem eForms-XML gelesen (ProcurementProjectLot/RealizedLocation/
   CountrySubentityCode; Adresse aus dem Feld `links` der API-Antwort, XML unverändert in data/raw/ted_xml/beispiel_liste_20261104/).
   Das Los gehört dazu, wenn mindestens einer seiner Codes mit DE23 beginnt. Zuordnung XML-Los zu Listen-Los über den Lostitel,
   sonst über die Reihenfolge. Scheitert das, bleiben alle Lose drin und werden markiert („Region je Los unklar“).
2. Unsicherheitsstufe je Eintrag nach der Herkunft (Einteilung für Iteration 7 vor dem Ziehen der Stichprobe festgelegt, 2026-11-04):
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

from auswertung_iteration6 import wilson  # noqa: E402
from auswertung_iteration7 import MAX_Y, bewertung  # noqa: E402
from vertragsliste import _liste, je_los  # noqa: E402

LISTE = ROOT / "data" / "processed" / "vertragsliste_909.csv"
REGION_RAW = ROOT / "data" / "raw" / "ted_search" / "zielgruppe_oberpfalz_20261023" / "page_0001.json"
XML_DIR = ROOT / "data" / "raw" / "ted_xml" / "beispiel_liste_20261104"
OUT_MD = ROOT / "reports" / "beispiel_liste.md"
OUT_CSV = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
REGION, REGION_NAME = "DE23", "Oberpfalz"
STICHTAG = date(2026, 11, 4)
TED = "https://ted.europa.eu/de/notice/-/detail/{}"
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


def xml_nuts(notice: dict, rows: list[dict], n_total: int | None) -> list[list[str]] | None:
    """NUTS-Codes aus dem eForms-XML für alle `n_total` Lose der Bekanntmachung (Index = Losnummer − 1); None, wenn die Zuordnung nicht gelingt.
    Iteration 9: `rows` enthält nur Lose mit Zuschlag; die Zahl der Lose im XML wird deshalb mit der Zahl aller Lose verglichen (`n_total`);
    fehlt diese in der Abfrage (kein Feld title-lot), gilt die Zahl der Lose im XML, sofern die höchste Losnummer der Liste hineinpasst."""
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
    if n_total is None:
        if not rows or max(int(r["los"]) for r in rows) > len(lose):
            return None
        n_total = len(lose)
    if len(lose) != n_total:
        return None
    ergebnis = [c for _, c in lose]
    nach_titel = {n[:120]: c for n, c in lose}
    if len(nach_titel) == len(lose):  # eindeutige Titel: Zuordnung über den Titel statt über die Reihenfolge
        for r in rows:
            t = " ".join(r["los_titel"].split())
            if t in nach_titel and 0 < int(r["los"]) <= n_total:
                ergebnis[int(r["los"]) - 1] = nach_titel[t]
    return ergebnis


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
        n_total = len(_liste(x.get("title-lot"))) or None  # Iteration 9: Lose ohne Zuschlag fehlen in `rows`, die Felder der API führen sie weiter
        codes_alle, eindeutig = je_los(x, "place-of-performance-subdiv-lot", n_total or len(rows))
        codes_alle = [[c] if c else [] for c in codes_alle]
        quelle = "api"
        if not eindeutig and (aus_xml := xml_nuts(x, rows, n_total)) is not None:
            codes_alle, eindeutig, quelle = aus_xml, True, "xml"
            info["aus_xml"] += 1
        codes = [codes_alle[int(r["los"]) - 1] if 0 < int(r["los"]) <= len(codes_alle) else [] for r in rows]
        for r, cs in zip(rows, codes):
            drin = [c for c in cs if c.startswith(REGION)]
            if eindeutig and not drin:
                continue
            out.append({**r, "nuts": " ".join(dict.fromkeys(cs)), "region_eindeutig": eindeutig, "nuts_quelle": quelle,
                        "auch_ausserhalb": eindeutig and len(drin) < len(cs)})
            info["unklar"] += not eindeutig
    return out, info


def stichprobe() -> list[dict]:
    """Zufallslose des Typs Y der Iteration 7 (L1 bis L50 nach der vorab festgelegten Kürzung); `stale`: Höchstende des Prüfers veraltet (siehe Auswertung)."""
    rows, _ = bewertung()
    y = [r for r in rows if r["typ"] == "Y" and int(r["L"][1:]) <= MAX_Y]
    return [{**r, "stale": r["nach"] == "ja" and r["h_p"].strip().lower() == "unbestimmbar" and r["nennt_h"]} for r in y]


def stufen_stichprobe(rows: list[dict]) -> dict[str, tuple[int, int, int, int]]:
    """Je Stufe: Lose der Stichprobe, davon Ende der Grundlaufzeit korrekt (Y1); Lose mit aktuellem Höchstende-Eintrag und davon korrekt (Y2)."""
    out = defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        s = out[stufe(r)]
        s[0] += 1
        s[1] += r["ok1"]
        if not r["stale"]:
            s[2] += 1
            s[3] += r["ok2"]
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
    quote_gl = f"{100 * k_gl / len(stich_rows):.1f}".replace(".", ",")

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

    kopf = ["| Ende Grundlaufzeit (laut Bekanntmachung) | Höchstende (nur Hinweis) | Status | Auftraggeber | Los | Stufe | Herkunft | Quelle |",
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
        n, k1, n2, k2 = stich.get(s, (0, 0, 0, 0))
        legende.append(f"| **{s}** | {STUFE_TEXT[s]} | {zaehl[s]} | {n or '–'} | {quote(k1, n) if n else 'ungeprüft'} | "
                       f"{quote(k2, n2) if n2 else 'ungeprüft'} |")

    md = [
        f"# Vertragsliste Gebäudereinigung {REGION_NAME} (Prototyp, Stand {STICHTAG.strftime('%d.%m.%Y')})",
        "",
        "_Erzeugt mit `src/report/beispiel_liste.py` (Iteration 9: Fassung der Lese-Regeln 1 bis 10, Lose ohne Zuschlag entfernt). Tabelle zum Weiterverarbeiten: "
        f"[{OUT_CSV.name}]({OUT_CSV.name})._",
        "",
        "Die Liste zeigt öffentliche Aufträge der Gebäudereinigung mit Leistungsort in der Oberpfalz, wann ihre feste Laufzeit endet "
        "und wie lange sie höchstens verlängert werden können. **Sie sagt nicht voraus, wann neu ausgeschrieben wird**; eine solche "
        "Prognose hat sich in Iteration 5 als nicht tragfähig erwiesen.",
        "",
        "**So ist die Liste zu lesen (Stand Iteration 9):** Das Ende der Grundlaufzeit steht so da, wie es die Bekanntmachung angibt (bzw. wie die Lese-Regeln es daraus ablesen). "
        "Auf einer neuen Stichprobe aus ganz Deutschland stimmt es zu 94,3 % mit dem Vergleichswert zweier KI-Leser überein; ein Mensch hat 15 Lose gegengelesen (14/15). "
        "Das Höchstende ist nur ein Hinweis (87,1 % der Zufallslose stimmen, Schwelle 90 % verfehlt). Vor einer Entscheidung immer die verlinkte Bekanntmachung lesen.",
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
        "- **Genauigkeit (Iteration 9, neue Stichprobe, Fassung der Regeln 1 bis 10)** ([zweitlesung_iteration9_auswertung.md](zweitlesung_iteration9_auswertung.md), "
        "[evaluation_iteration9.md](evaluation_iteration9.md)): Ende der Grundlaufzeit der Liste = Vergleichswert zweier KI-Leser bei 66/70 Zufallslosen (94,3 %, Wilson 86,2–97,8) und 28/30 "
        "geschichteten Losen; Kommilitone 14/15; Höchstende 61/70 = 87,1 % (Schwelle 90 % verfehlt). **Vorbehalte:** Leser und Regeln stammen aus derselben Modellfamilie, der Vergleichswert ist teilweise "
        "zirkulär (Feld als Standard), die alte Fassung kam auf 65/70, das bloße Feld auf 63/70; der Nutzen der neuen Regeln ist durch die Stichprobe nicht gesichert.",
        f"- Frühere Messung (Iteration 7, **alte Fassung der Regeln**; Prüfung einer Zufallsstichprobe von {alle_stich} Losen aus ganz Deutschland, "
        f"[liste_auswertung_iteration7.md](liste_auswertung_iteration7.md)): Ende der Grundlaufzeit {k_gl}/{alle_stich} = "
        f"{quote_gl} % übereinstimmend mit dem Prüfer (Wilson 62,8–86,4 %); bei Losen, deren Laufzeit im Text der Bekanntmachung "
        "steht, 12/12. **Vorbehalte:** Die Prüfung wurde gekürzt (L1 bis L50 statt 80 Lose), 4 Nachprüfungen blieben leer, und bei 5 von 38 Losen "
        "wich der abgeschriebene Feldwert von den Rohdaten ab ([abschreibecheck_iteration7.md](abschreibecheck_iteration7.md)); die Zahl ist deshalb "
        "eine Mischung aus Fehlern der Liste und Lesefehlern der Prüfung. Bei den 15 Losen, die Regel 1b ändert, stimmten nur 8 mit dem Prüfer überein "
        "(bei allen 7 Abweichungen hatte die Nachprüfung das Enddatum des Feldes übernommen, die Liste ein früheres Datum aus dem Text; wer recht hat, ist offen).",
        "",
        "### Unsicherheit je Eintrag (Spalte „Stufe“)",
        "",
        *legende,
        "",
        "_Die Einteilung in Stufen wurde vor dem Ziehen der Stichprobe festgelegt (2026-11-04). Die Quoten je Stufe beruhen auf wenigen Losen (Klammer: 95-%-Wilson-Intervall) und stammen "
        "nicht aus der Oberpfalz. „Ende GL korrekt“ zählt einen Eintrag „unbekannt“ des Prüfers (4 leer gebliebene Nachprüfungen) und Lesefehler beim Abschreiben der Felder als Abweichung. "
        "„Höchstende korrekt“ ist ohne die 15 Lose berechnet, bei denen das Höchstende des Prüfers vor der Nachprüfung eingetragen wurde (veraltet); bei Stufe D ist es per Definition 100 %, "
        "weil „unbestimmbar“ immer als korrekt zählt._",
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
        "- Die Spalte „Stufe“ sagt, woher ein Eintrag stammt, nicht, wie verlässlich er ist. Für Stufe A ist die Genauigkeit **nicht belegt**: Die Quote oben stammt nur aus Zufallslosen "
        "ohne Regel 1b; die Lose, deren Ende Regel 1b aus dem Text berichtigt (ebenfalls Stufe A), stimmten nur in 8 von 15 Fällen mit dem Prüfer überein. Bei allen Stufen lohnt ein Blick "
        "in die Bekanntmachung. Die Quoten je Stufe beruhen auf sehr wenigen Losen. _(Korrigiert beim Abschluss von Iteration 7, 2026-11-04; vorher hieß es, Stufe A sei „die sicherste“.)_",
        "- **Regel 1b, Typ „Festlaufzeit-Datum“** (z. B. Bekanntmachung 143100-2026, Autobahn GmbH) ist **nicht** durch die Stichprobe getestet; die Einträge "
        "stehen in der Liste mit Stufe A, ohne dass ihre Genauigkeit belegt ist. Ebenso ist der Typ „feste Dauer + Option“ nur an 15 Losen mit gemischtem Ergebnis geprüft.",
        "- Zwei Fehler der Liste fielen in der Prüfung auf: Höchstende bei Bekanntmachung 557125-2026 (Liste 31.08.2037, Text 31.08.2031) und 707425-2025 "
        "(Liste 31.10.2029, Text 31.10.2030); beide stehen noch so in der bundesweiten Vertragsliste (nicht in der Oberpfalz-Liste).",
        f"- Aus der Oberpfalz liegt {len(geprueft)} Los der Stichprobe vor ({', '.join(geprueft) or '–'}). "
        "Die Liste kommt ohne Kundentest aus (A1, A15 ungeprüft); ob diese Form für einen Mittelständler nützlich ist, bleibt offen.",
        "",
    ]
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"{len(lose)} Lose ({len(laufend)} laufend); Stufen {dict(sorted(zaehl.items()))}; Stichprobe {dict(sorted(stich.items()))}")
    print(f"{OUT_MD}\n{OUT_CSV}")


if __name__ == "__main__":
    main()
