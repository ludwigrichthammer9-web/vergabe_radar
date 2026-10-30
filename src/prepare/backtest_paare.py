"""Iteration 5, Schritt 4: Backtest-Paare aus der Handsuche (Iteration 3 und 4) und Vorlage für die Zweitprüfung (Schritt 5).

Paare (vorab festgelegt in docs/iterationen.md, Iteration 5):
- Iteration 3 (sichtbarkeit_iteration3_gt.csv): Kategorie objektgleich oder teilmenge; Vorgänger = erste Notice der Spalte
  „vorgaenger“ (laut Protokoll der jüngste Vorgänger). T26: 95743-2021 laut vorgaenger_ende_iteration3_korrektur.csv
  (462151-2026 war ein aufgehobenes Verfahren).
- Iteration 4 (sichtbarkeit_iteration4_gt.csv): Kategorie objektgleich_* oder teilmenge; Vorgänger = Spalte „vertrag“, bei „–“ die
  erste Notice der Spalte „vorgaenger“.
- Bekannte Lücke: Formulare der Verteidigungsvergabe (F17/F18, altes Schema) werden nicht gelesen (U37).

Vorgänger-Ende nur aus den Bekanntmachungen des Vorgängers (docs/business.md §7.1, Festlegung 1), mit den Lese-Regeln aus
src/prepare/vertragsliste.py (`laufzeit`):
- eForms: API-Felder der Notice (lostext-Downloads). Fehlt bei einem Zuschlag die Laufzeit, die Ausschreibung desselben Verfahrens.
- vor eForms: Original-XML; bei Zuschlag (F03/F06) die über REF_NOTICE verknüpfte Ausschreibung (F02/F05). Text = RENEWAL_DESCR +
  OPTIONS_DESCR + SHORT_DESCR des Loses; NO_RENEWAL = keine Verlängerung. XML unverändert in data/raw/ted_xml/backtest_20261030/.
- Mehrere Lose: Die GT nennt die Lose nicht strukturiert, daher gilt je Paar das früheste Ende aller Lose (Festlegung 6, Rückfall),
  gekennzeichnet in „lose_unterschiedlich“.

Zweitprüfung (Schritt 5): alle Paare mit bestimmbarem Ende der Grundlaufzeit (X1-Kandidaten) plus 10 Köder-Paare aus Iteration 4,
Kategorie „unklar“ (bester Kandidat der Handsuche), ohne Testfälle, die der Nutzer in W4 gesehen hat. Köder zählen wie in W4 als
„nicht gefunden“, damit „alles bestätigen“ nicht zu 100 % Übereinstimmung führt. Gemischt mit Seed 20261101.

Ausgabe:
- data/processed/backtest_paare_iteration5.csv  (Vorgänger-Enden; vor der Zweitprüfung nicht öffnen)
- data/processed/gt_pruefung_iteration5_schluessel.csv  (P-Nummer → Paar und Urteil der Handsuche; SHA-256 wird ausgegeben)
- reports/gt_pruefung_iteration5.md  (Vorlage) und reports/gt_pruefung_iteration5_lesehilfe.md (Auszüge mit Feldnamen)

Aufruf: python src/prepare/backtest_paare.py
"""

import csv
import hashlib
import random
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyze_completeness import PROJECT_ROOT, RAW_SEARCH_DIR, load_notices  # noqa: E402
from vertragsliste import _liste, iso, laufzeit, monate, zeilen  # noqa: E402

GT3 = PROJECT_ROOT / "reports" / "sichtbarkeit_iteration3_gt.csv"
GT4 = PROJECT_ROOT / "reports" / "sichtbarkeit_iteration4_gt.csv"
W4 = PROJECT_ROOT / "reports" / "blindpruefung_iteration4.md"
KORREKTUR = {"T26": "95743-2021"}  # reports/vorgaenger_ende_iteration3_korrektur.csv
POOLS = ("DEU_result_cpv909_20231025_20260930_lostext", "DEU_competition_cpv909_20231025_20260930_lostext",
         "DEU_competition_cpv9091main_20251001_20251231_lostext", "DEU_competition_cpv9091main_20260101_20260331_lostext",
         "DEU_competition_cpv9091main_20260401_20260630_lostext", "DEU_competition_cpv9091main_20260701_20260930_lostext")
XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml" / "backtest_20261030"
XML_URL = "https://ted.europa.eu/en/notice/{}/xml"
OUT_CSV = PROJECT_ROOT / "data" / "processed" / "backtest_paare_iteration5.csv"
SCHLUESSEL = PROJECT_ROOT / "data" / "processed" / "gt_pruefung_iteration5_schluessel.csv"
VORLAGE = PROJECT_ROOT / "reports" / "gt_pruefung_iteration5.md"
LESEHILFE = PROJECT_ROOT / "reports" / "gt_pruefung_iteration5_lesehilfe.md"
SEED = 20261101
N_KOEDER = 10
MAX_TEXT = 900
TED_LINK = "https://ted.europa.eu/de/notice/-/detail/{}"


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def fetch(pub: str) -> ET.Element | None:
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
        time.sleep(0.5)
    try:
        return ET.fromstring(path.read_bytes())
    except ET.ParseError:
        return None


def first(el: ET.Element, name: str) -> ET.Element | None:
    return next((e for e in el.iter() if local(e.tag) == name), None)


def child(el: ET.Element, name: str) -> ET.Element | None:
    return next((c for c in el if local(c.tag) == name), None)


def text(el: ET.Element | None) -> str:
    return re.sub(r"\s+", " ", " ".join(el.itertext())).strip() if el is not None else ""


def form_el(root: ET.Element) -> ET.Element | None:
    forms = [e for e in root.iter() if re.fullmatch(r"F\d\d_2014", local(e.tag))]
    return next((f for f in forms if f.get("CATEGORY") == "ORIGINAL"), forms[0] if forms else None)


def ref_pub(root: ET.Element) -> str | None:
    ref = first(root, "REF_NOTICE")
    if ref is None:
        ref = first(root, "NOTICE_NUMBER_OJ")
    m = re.search(r"(\d{4})/S \d+-(\d+)", text(ref)) if ref is not None else None
    return f"{int(m.group(2))}-{m.group(1)}" if m else None


def xml_lose(form: ET.Element) -> list[tuple]:
    """(gl, gl_h, h, h_h, beginn) je Los einer Ausschreibung vor eForms."""
    out = []
    for od in (e for e in form.iter() if local(e.tag) == "OBJECT_DESCR"):
        beginn, ende = iso(text(first(od, "DATE_START"))), iso(text(first(od, "DATE_END")))
        dur = first(od, "DURATION")
        dauer = None
        if dur is not None and text(dur).isdigit():
            n = int(text(dur))
            dauer = {"MONTH": n, "YEAR": 12 * n, "DAY": round(n / 30.4375)}.get(dur.get("TYPE", "MONTH"))
        verl = True if child(od, "RENEWAL") is not None else (False if child(od, "NO_RENEWAL") is not None else None)
        t = " ".join(text(child(od, k)) for k in ("RENEWAL_DESCR", "OPTIONS_DESCR", "SHORT_DESCR"))
        out.append((*laufzeit(beginn, ende, dauer, t, None, verl), beginn))
    return out


def api_lose(notice: dict) -> list[tuple]:
    return [(iso(r["gl_ende"]) if r["gl_ende"] else None, r["gl_herkunft"],
             iso(r["hoechstende"]) if r["hoechstende"] else None, r["hoechstende_herkunft"],
             r["beginn"] or None) for r in zeilen(notice)]


def ist_eforms(notice: dict | None) -> bool:
    return bool(notice and notice.get("notice-identifier"))


def vorgaenger_ende(pub: str, api: dict, by_proc: dict) -> dict:
    """Laufzeitangaben des Vorgängers; bevorzugt eForms-API, sonst XML (mit REF_NOTICE)."""
    n = api.get(pub)
    if ist_eforms(n):
        lose, quelle = api_lose(n), pub
        if not any(lo[0] for lo in lose) and "result" in str(n.get("form-type", "")):
            for c in by_proc.get((n.get("procedure-identifier") or [None])[0] if isinstance(n.get("procedure-identifier"), list)
                                 else n.get("procedure-identifier"), []):
                if c is not n and "competition" in str(c.get("form-type", "")):
                    lose, quelle = api_lose(c), c["publication-number"]
                    break
        return {"format": "eforms", "laufzeit_aus": quelle, "lose": lose}
    root = fetch(pub)
    if root is None:
        return {"format": "xml", "laufzeit_aus": "", "lose": [], "fehler": "XML nicht ladbar"}
    form = form_el(root)
    fname = local(form.tag) if form is not None else local(root.tag)
    quelle = pub
    if fname in ("F03_2014", "F06_2014", "F15_2014", "F20_2014") or (form is not None and first(form, "OBJECT_DESCR") is not None
                                                                     and first(form, "DATE_END") is None and first(form, "DURATION") is None):
        ref = ref_pub(root)
        ref_root = fetch(ref) if ref else None
        if ref_root is not None and form_el(ref_root) is not None:
            form, quelle = form_el(ref_root), ref
    lose = xml_lose(form) if form is not None else []
    return {"format": "xml", "laufzeit_aus": quelle if lose else "", "lose": lose, "form": fname}


def zusammenfassen(lose: list[tuple]) -> dict:
    """Frühestes Ende aller Lose (Festlegung 6, Rückfall)."""
    mit_gl = [lo for lo in lose if lo[0]]
    if not mit_gl:
        return {"gl_ende": "", "gl_herkunft": lose[0][1] if lose else "keine_daten", "hoechstende": "",
                "hoechstende_herkunft": "", "beginn": "", "n_lose": len(lose), "lose_unterschiedlich": False}
    gl = min(mit_gl, key=lambda lo: lo[0])
    hs = min(mit_gl, key=lambda lo: lo[2] or lo[0])
    return {"gl_ende": gl[0], "gl_herkunft": gl[1], "hoechstende": hs[2] or "", "hoechstende_herkunft": hs[3],
            "beginn": gl[4] or "", "n_lose": len(lose),
            "lose_unterschiedlich": len({(lo[0], lo[2]) for lo in mit_gl}) > 1}


# ---------------------------------------------------------------------------------------------------------------------
# Lesehilfe: Auszüge mit Feldnamen, ohne Laufzeitfelder

def kurz(t: str, n: int = MAX_TEXT) -> str:
    t = " ".join(str(t or "").split()).replace("|", "/")
    return t[:n] + (" …" if len(t) > n else "")


def auszug_api(n: dict) -> list[str]:
    titel = [str(t) for t in _liste(n.get("title-lot"))]
    beschr = [str(t) for t in _liste(n.get("description-lot"))]
    orte = lambda f: [str(t) for t in _liste(n.get(f))]  # noqa: E731
    strasse, plz, ort = orte("place-performance-street-lot"), orte("place-of-performance-post-code-lot"), orte("place-of-performance-city-lot")
    out = [f"- Auftraggeber: {kurz(' / '.join(map(str, _liste(n.get('buyer-name')))), 200)} ({kurz(' '.join(map(str, _liste(n.get('buyer-city')))), 80)})",
           f"- Titel (Verfahren): {kurz((_liste(n.get('title-proc')) or [''])[0], 300)}",
           f"- Beschreibung (Verfahren): {kurz((_liste(n.get('description-proc')) or [''])[0])}"]
    for i, t in enumerate(titel[:12]):
        ortsangabe = ", ".join(x for x in (strasse[i] if i < len(strasse) else "", plz[i] if i < len(plz) else "",
                                           ort[i] if i < len(ort) else "") if x)
        out.append(f"- Los {i + 1}: Titel: {kurz(t, 300)} | Erfüllungsort: {ortsangabe or '–'} | Beschreibung: "
                   f"{kurz(beschr[i] if i < len(beschr) else '')}")
    if len(titel) > 12:
        out.append(f"- … weitere {len(titel) - 12} Lose (siehe TED-Link)")
    return out


def auszug_xml(pub: str) -> list[str]:
    root = fetch(pub)
    form = form_el(root) if root is not None else None
    if form is None:
        return ["- (XML nicht lesbar, bitte TED-Link öffnen)"]
    cb = first(form, "CONTRACTING_BODY")
    oc = first(form, "OBJECT_CONTRACT")
    out = [f"- Formular: {local(form.tag)}",
           f"- Auftraggeber: {kurz(text(first(cb, 'OFFICIALNAME')) if cb is not None else '', 200)} "
           f"({kurz(text(first(cb, 'TOWN')) if cb is not None else '', 80)})",
           f"- Titel: {kurz(text(child(oc, 'TITLE')) if oc is not None else '', 300)}",
           f"- Kurzbeschreibung: {kurz(text(child(oc, 'SHORT_DESCR')) if oc is not None else '')}"]
    for i, od in enumerate(e for e in form.iter() if local(e.tag) == "OBJECT_DESCR"):
        if i == 12:
            out.append("- … weitere Lose (siehe TED-Link)")
            break
        out.append(f"- Los {text(child(od, 'LOT_NO')) or i + 1}: Titel: {kurz(text(child(od, 'TITLE')), 300)} | Erfüllungsort: "
                   f"{kurz(text(child(od, 'MAIN_SITE')), 200) or '–'} | Beschreibung: {kurz(text(child(od, 'SHORT_DESCR')))}")
    for i, aw in enumerate(e for e in form.iter() if local(e.tag) == "AWARD_CONTRACT"):
        if i == 12:
            break
        out.append(f"- Zuschlag Los {text(child(aw, 'LOT_NO')) or i + 1}: {kurz(text(child(aw, 'TITLE')), 300)}")
    return out


def auszug(pub: str, api: dict) -> list[str]:
    n = api.get(pub)
    return auszug_api(n) if ist_eforms(n) else auszug_xml(pub)


# ---------------------------------------------------------------------------------------------------------------------

def erste_notice(*felder: str) -> str:
    """Erste Notice-Nummer aus den Feldern („–“ heißt leer)."""
    for f in felder:
        if m := re.search(r"\d{1,6}-\d{4}", f or ""):
            return m.group(0)
    return ""


def gt_paare() -> tuple[list[dict], list[dict]]:
    paare, koeder = [], []
    with GT3.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            if r["kategorie"] in ("objektgleich", "teilmenge") and r["vorgaenger"].strip():
                v = KORREKTUR.get(r["T"], erste_notice(r["vorgaenger"]))
                paare.append({"pid": r["T"], "iteration": 3, "gt": r["kategorie"], "testfall": r["notice"], "vorgaenger": v})
    with GT4.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            if r["kategorie"].startswith("objektgleich") or r["kategorie"] == "teilmenge":
                v = erste_notice(r["vertrag"], r["vorgaenger"])
                paare.append({"pid": r["U"], "iteration": 4, "gt": r["kategorie"], "testfall": r["notice"], "vorgaenger": v})
            elif r["kategorie"] == "unklar" and r["kandidat_unklar"].strip():
                koeder.append({"pid": r["U"], "iteration": 4, "gt": "unklar", "testfall": r["notice"],
                               "vorgaenger": erste_notice(r["kandidat_unklar"])})
    return paare, koeder


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    api, by_proc = {}, {}
    for pool in POOLS:
        for n in load_notices(RAW_SEARCH_DIR / pool):
            api.setdefault(n["publication-number"], n)
            p = n.get("procedure-identifier")
            p = p[0] if isinstance(p, list) and p else p
            if p:
                by_proc.setdefault(p, []).append(n)
    paare, koeder = gt_paare()

    rows = []
    for p in paare:
        t = api.get(p["testfall"])
        v = vorgaenger_ende(p["vorgaenger"], api, by_proc)
        z = zusammenfassen(v["lose"])
        rows.append({**p, "testfall_datum": str(t.get("publication-date", ""))[:10] if t else "",
                     "format": v["format"], "laufzeit_aus": v["laufzeit_aus"], **z,
                     "gl_monate": monate(iso(z["beginn"]), z["gl_ende"]) if z["beginn"] and z["gl_ende"] else "",
                     "fehler": v.get("fehler", "")})
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=";")
        w.writeheader()
        w.writerows(rows)

    # Zweitprüfung: X1-Kandidaten + Köder
    gesehen_w4 = set(re.findall(r"- Neu: \[(\S+?)\]", W4.read_text(encoding="utf-8")))
    alt_w4 = set(re.findall(r"- Alt: \[(\S+?)\]", W4.read_text(encoding="utf-8")))
    rng = random.Random(SEED)
    kandidaten = [r for r in rows if r["gl_ende"]]
    koeder_pool = [k for k in koeder if k["testfall"] not in gesehen_w4]
    items = [{**r, "rolle": "paar"} for r in kandidaten] + [{**k, "rolle": "koeder"} for k in
                                                              rng.sample(koeder_pool, min(N_KOEDER, len(koeder_pool)))]
    rng.shuffle(items)
    for i, it in enumerate(items, 1):
        it["P"] = f"P{i}"
        it["in_w4_gesehen"] = it["testfall"] in gesehen_w4 or it["vorgaenger"] in alt_w4
    with SCHLUESSEL.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["P", "pid", "rolle", "gt", "testfall", "vorgaenger", "in_w4_gesehen"])
        for it in items:
            w.writerow([it["P"], it["pid"], it["rolle"], it["gt"], it["testfall"], it["vorgaenger"], it["in_w4_gesehen"]])
    sha = hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()

    vorlage = [
        "# Zweitprüfung der Backtest-Paare (Iteration 5, Schritt 5, Kriterien X1 und X2)", "",
        "**Bitte erst ausfüllen, bevor du `data/processed/backtest_paare_iteration5.csv`, den Schlüssel oder Reports zum Backtest "
        "öffnest.** Die Handsuche-Dateien (`sichtbarkeit_iteration3_*`, `sichtbarkeit_iteration4_*`) bitte ebenfalls nicht öffnen.", "",
        f"Beurteile jedes Paar nach [Urteilsregeln Version 1.1](urteilsregeln_blindpruefung.md). Lesehilfe mit Feldnamen: "
        f"[gt_pruefung_iteration5_lesehilfe.md](gt_pruefung_iteration5_lesehilfe.md); im Zweifel den TED-Link öffnen. "
        "Zeitabstand, Vertragsende, Laufzeit und Auftragswert spielen keine Rolle. Keine Zeitgrenze; du kannst in mehreren "
        "Sitzungen arbeiten. Unter den Paaren sind auch solche, bei denen der Vorgänger nicht passt.", "",
        "Je Paar eintragen:",
        "- **Urteil:** objektgleich | teilmenge | nicht objektgleich | unklar",
        "- **Sicherheit** (nur bei objektgleich): hoch | mittel",
        "- **Tendenz** (nur bei unklar): eher dafür | eher dagegen | keine",
        "- **Minuten:** ungefähr, ganze Minuten",
        "- **Begründung:** ein Satz mit Feld und Wert (z. B. „Los 2 Erfüllungsort Hauptstr. 5 in beiden“)", "",
        f"_Erzeugt mit `src/prepare/backtest_paare.py`, Seed {SEED}, {len(items)} Paare. Schlüssel lokal, SHA-256 `{sha}`._", "",
    ]
    lesehilfe = ["# Lesehilfe zur Zweitprüfung (Iteration 5)", "",
                 "Auszüge mit Feldnamen, ohne Laufzeit- und Wertfelder. Texte gekürzt; vollständig über die TED-Links.", ""]
    for it in items:
        if it["rolle"] == "koeder":
            it["laufzeit_aus"] = vorgaenger_ende(it["vorgaenger"], api, by_proc)["laufzeit_aus"]
        alt = [it["vorgaenger"]]
        if it.get("laufzeit_aus") and it["laufzeit_aus"] != it["vorgaenger"]:
            alt.append(it["laufzeit_aus"])
        vorlage += [f"### {it['P']}",
                    "- Alt: " + ", ".join(f"[{a}]({TED_LINK.format(a)})" for a in alt),
                    f"- Neu: [{it['testfall']}]({TED_LINK.format(it['testfall'])})",
                    "- Urteil: ", "- Sicherheit: ", "- Tendenz: ", "- Minuten: ", "- Begründung: ", ""]
        lesehilfe += [f"## {it['P']}", ""]
        for a in alt:
            lesehilfe += [f"### Alt: {a}", *auszug(a, api), ""]
        lesehilfe += [f"### Neu: {it['testfall']}", *auszug(it["testfall"], api), ""]
    VORLAGE.write_text("\n".join(vorlage), encoding="utf-8")
    LESEHILFE.write_text("\n".join(lesehilfe), encoding="utf-8")

    n_gl = len(kandidaten)
    print(f"Paare: {len(rows)} (Iteration 3: {sum(r['iteration'] == 3 for r in rows)}, Iteration 4: {sum(r['iteration'] == 4 for r in rows)})")
    print(f"mit bestimmbarem Ende der Grundlaufzeit: {n_gl}; ohne: {len(rows) - n_gl}; davon Fehler: {sum(bool(r['fehler']) for r in rows)}")
    print(f"Zweitprüfung: {len(items)} Paare ({n_gl} + {len(items) - n_gl} Köder), davon in W4 gesehen: "
          f"{sum(it['in_w4_gesehen'] for it in items)}")
    print(f"Schlüssel SHA-256: {sha}")


if __name__ == "__main__":
    main()
