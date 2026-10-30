"""Iteration 5, Schritt 2: Wie werden Laufzeit und Verlängerungen in der Praxis angegeben?

Frage: Ist das Enddatum (BT-537) bzw. die Dauer (BT-36) das Ende der Grundlaufzeit oder das Höchstende? Laut eForms-Definition
umfasst BT-36 „etwaige Optionen und Verlängerungen“, für BT-537 gibt es keine Aussage. Wie oft lässt sich die Länge der
Verlängerungen aus dem Freitext (BT-57, BT-54) ablesen?

Daten:
- eForms-Zuschläge Gebäudereinigung (Haupt-CPV 90910/90911/90919, nur Originale), veröffentlicht 25.10.2023–30.09.2026
  (`data/raw/ted_search/DEU_result_cpv909_20231025_20260930_lostext/`).
- Vor eForms: die über `REF_NOTICE` verknüpften Ausschreibungen (F02/F05) der A11-Zufallsstichprobe (`data/raw/ted_xml/a11_20261023/`).

Die Textmuster sind grob (reguläre Ausdrücke). Sie zeigen Größenordnungen, keine exakte Extraktion; Beispiele stehen im Report.

Ergebnis: reports/verlaengerung_praxis_iteration5.md
"""

import re
import xml.etree.ElementTree as ET
from datetime import date

from analyze_completeness import PROJECT_ROOT, RAW_SEARCH_DIR, load_notices
from kennzahlen_iteration2 import wilson

RUN = "DEU_result_cpv909_20231025_20260930_lostext"
XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml" / "a11_20261023"
REPORT = PROJECT_ROOT / "reports" / "verlaengerung_praxis_iteration5.md"
CPV_NISCHE = ("90910", "90911", "90919")

ZAHLWORT = {"ein": 1, "eine": 1, "einen": 1, "einmal": 1, "zwei": 2, "drei": 3, "vier": 4, "fünf": 5, "sechs": 6,
            "sieben": 7, "acht": 8, "zehn": 10}
# Länge einer einzelnen Verlängerung, z. B. „um jeweils ein Jahr“, „2 x 12 Monate“
RE_JE = re.compile(r"(?i)\b(je(weils)?|um|x)\s+(\d+|ein(e|en)?|zwei|drei|vier|sechs|zwölf)\s*(\(\d+\)\s*)?(weitere[nrs]?\s*)?"
                   r"(schul)?(jahr|monat)")
# Höchstlaufzeit, z. B. „maximale Vertragslaufzeit beträgt 4 Jahre“, „längstens 48 Monate“
RE_MAX = re.compile(r"(?i)(maximale?\s*(vertrags)?(laufzeit|dauer)|gesamtlaufzeit|insgesamt\s+maximal|längstens)"
                    r"\D{0,30}?\b(\d+|ein|zwei|drei|vier|fünf|sechs|sieben|acht|zehn)\b\s*(\(\d+\)\s*)?(schul)?(jahre?|monate?)")
RE_DATUM = re.compile(r"\b\d{1,2}\.\s?\d{1,2}\.\s?20\d{2}\b")
RE_VERL = re.compile(r"(?i)verläng")


def text(value) -> str:
    """Mehrsprachige API-Felder ({"deu": [...]}) oder Listen zu einem Text zusammenfassen, Deutsch bevorzugt."""
    if not value:
        return ""
    if isinstance(value, dict):
        parts = value.get("deu") or next(iter(value.values()), [])
        return " ".join(parts) if isinstance(parts, list) else str(parts)
    if isinstance(value, list):
        return " ".join(text(v) for v in value)
    return str(value)


def max_months(t: str) -> int | None:
    m = RE_MAX.search(t)
    if not m:
        return None
    n = m.group(4).lower()
    n = int(n) if n.isdigit() else ZAHLWORT.get(n)
    return n * 12 if m.group(7).lower().startswith("jahr") else n


def span_months(start: str, end: str) -> int:
    """Laufzeit in ganzen Monaten, Endtag eingeschlossen (01.01.2026–31.12.2027 = 24)."""
    s, e = date.fromisoformat(start[:10]), date.fromisoformat(end[:10])
    return round(((e - s).days + 1) / 30.4375)


def bt36_months(period) -> int | None:
    if not period:
        return None
    p = period[0]
    v = str(p.get("value", ""))
    if not v.isdigit():
        return None
    return int(v) * (12 if p.get("unit") == "YEAR" else 1) if p.get("unit") in ("YEAR", "MONTH") else None


def vergleich(paare: list[tuple[int, int]]) -> dict:
    """Paare (Laufzeit laut Feld, Höchstlaufzeit laut Text) → kürzer / gleich (±1 Monat) / länger."""
    return {"n": len(paare),
            "kuerzer": sum(1 for a, b in paare if a < b - 1),
            "gleich": sum(1 for a, b in paare if abs(a - b) <= 1),
            "laenger": sum(1 for a, b in paare if a > b + 1)}


def pct(k: int, n: int, ki: bool = False) -> str:
    if not n:
        return "–"
    s = f"{k}/{n} = {100 * k / n:.1f} %".replace(".", ",")
    if ki:
        lo, hi = wilson(k, n)
        s += f" (Wilson {100 * lo:.1f}–{100 * hi:.1f})".replace(".", ",")
    return s


def eforms() -> dict:
    r = {"tot": 0, "ende": 0, "start_dauer": 0, "oth": 0, "keins": 0, "rm_gt0": 0, "rm_0": 0, "rm_fehlt": 0,
         "rm_gt0_57": 0, "je": 0, "max": 0, "datum": 0, "irgend": 0, "ohne_rm_verl": 0,
         "v537": [], "v36": [], "v36span": [], "bsp": []}
    for x in load_notices(RAW_SEARCH_DIR / RUN):
        mc = x.get("main-classification-proc") or []
        if not any(str(c)[:5] in CPV_NISCHE for c in mc) or x.get("change-notice-version-identifier"):
            continue
        r["tot"] += 1
        start = (x.get("contract-duration-start-date-lot") or [""])[0]
        ende = (x.get("contract-duration-end-date-lot") or [""])[0]
        dauer = bt36_months(x.get("contract-duration-period-lot"))
        if ende:
            r["ende"] += 1
        elif start and dauer:
            r["start_dauer"] += 1
        elif x.get("contract-duration-period-oth-lot"):
            r["oth"] += 1
            continue
        else:
            r["keins"] += 1
            continue
        if dauer and start and ende:
            r["v36span"].append((span_months(start, ende), dauer))
        t57 = text(x.get("renewal-description-lot"))
        t = t57 + " " + text(x.get("option-description-lot"))
        mm = max_months(t)
        if mm:
            if start and ende:
                r["v537"].append((span_months(start, ende), mm))
            if dauer:
                r["v36"].append((dauer, mm))
        rm = [int(v) for v in (x.get("renewal-maximum-lot") or []) if str(v).isdigit()]
        if not rm:
            r["rm_fehlt"] += 1
        elif max(rm) == 0:
            r["rm_0"] += 1
        if not rm or max(rm) == 0:
            r["ohne_rm_verl"] += bool(RE_VERL.search(t))
            continue
        r["rm_gt0"] += 1
        r["rm_gt0_57"] += bool(t57.strip())
        je, mx, dt = bool(RE_JE.search(t)), bool(mm), bool(RE_DATUM.search(t))
        r["je"] += je
        r["max"] += mx
        r["datum"] += dt
        r["irgend"] += je or mx or dt
        if len(r["bsp"]) < 8 and t57.strip():
            r["bsp"].append((x["publication-number"], start[:10], ende[:10], dauer, max(rm), " ".join(t57.split())[:200]))
    return r


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def vor_eforms() -> dict:
    r = {"dateien": 0, "renewal": 0, "no_renewal": 0, "keine_angabe": 0, "descr": 0, "irgend": 0, "v": [], "bsp": []}
    for f in sorted(XML_DIR.glob("*.xml")):
        root = ET.parse(f).getroot()
        form = next((e for e in root.iter() if local(e.tag) in ("F02_2014", "F05_2014")), None)
        if form is None:
            continue
        od = next((e for e in form.iter() if local(e.tag) == "OBJECT_DESCR"), None)
        if od is None:
            continue
        r["dateien"] += 1
        kinder = {local(e.tag): e for e in od}
        if "RENEWAL" not in kinder:
            r["no_renewal" if "NO_RENEWAL" in kinder else "keine_angabe"] += 1
            continue
        r["renewal"] += 1
        d = kinder.get("RENEWAL_DESCR")
        t = " ".join("".join(d.itertext()).split()) if d is not None else ""
        r["descr"] += bool(t)
        mm = max_months(t)
        r["irgend"] += bool(RE_JE.search(t) or mm or RE_DATUM.search(t))
        s = next((e.text for e in od.iter() if local(e.tag) == "DATE_START"), None)
        e_ = next((e.text for e in od.iter() if local(e.tag) == "DATE_END"), None)
        if mm and s and e_:
            r["v"].append((span_months(s, e_), mm))
        if len(r["bsp"]) < 6:
            r["bsp"].append((f.stem, s or "", e_ or "", t[:200]))
    return r


def main() -> None:
    e, v = eforms(), vor_eforms()
    basis = e["ende"] + e["start_dauer"]
    v537, v36, vv = vergleich(e["v537"]), vergleich(e["v36"]), vergleich(v["v"])
    sp = vergleich(e["v36span"])  # (Datumsspanne, BT-36): „kürzer“ heißt BT-36 länger als die Spanne
    out = [
        "# Laufzeit und Verlängerungen in der Praxis (Iteration 5, Schritt 2)",
        "",
        "_Erzeugt mit `src/verlaengerung_praxis.py`. Grobe Textmuster, Größenordnungen; Fakten und Interpretation getrennt._",
        "",
        "## Definition laut eForms SDK",
        "",
        "Quelle: `translations/business-term_de.xml` im [eForms SDK](https://github.com/OP-TED/eForms-SDK) (Branch develop, abgerufen 2026-10-30).",
        "",
        "- **BT-36 Laufzeit:** „… vom Beginn bis zum Ende. Dies umfasst etwaige Optionen und Verlängerungen.“",
        "- **BT-537 Ende der Laufzeit:** „Angaben zum (voraussichtlichen) Ende der Laufzeit …“, ohne Aussage zu Verlängerungen.",
        "- **BT-538:** „Laufzeit unbekannt, unbegrenzt, usw.“",
        "- **BT-58 Höchstzahl der Verlängerungen:** „Die maximale Zahl der Vertragsverlängerungen …“, ohne Länge je Verlängerung.",
        "- **BT-57:** „Sonstige Informationen über die Verlängerung(en).“ (Freitext); **BT-54:** „Die Beschreibung der Optionen.“",
        "- Vor eForms (Formular F02/F05, Abschnitt II.2.7): Beginn/Ende oder Dauer, „verlängerbar ja/nein“ (`RENEWAL`/`NO_RENEWAL`) und",
        "  Freitext `RENEWAL_DESCR`. Eine Definition, ob die Laufzeit Verlängerungen einschließt, wurde im Schema nicht gefunden.",
        "",
        "## Fakten: eForms-Zuschläge",
        "",
        f"Population: eForms-Zuschläge, Haupt-CPV 90910/90911/90919, nur Originale, veröffentlicht 25.10.2023–30.09.2026: **{e['tot']}**.",
        "",
        "| | Anzahl |",
        "|---|---|",
        f"| Enddatum BT-537 vorhanden | {pct(e['ende'], e['tot'])} |",
        f"| kein Enddatum, aber Beginn + Dauer (BT-536 + BT-36) | {pct(e['start_dauer'], e['tot'])} |",
        f"| nur BT-538 (unbekannt/unbegrenzt) | {pct(e['oth'], e['tot'])} |",
        f"| keine verwertbare Laufzeit | {pct(e['keins'], e['tot'])} |",
        "",
        f"Unter den {basis} Zuschlägen mit bestimmbarem Ende:",
        "",
        "| | Anzahl |",
        "|---|---|",
        f"| BT-58 > 0 (Verlängerung möglich) | {pct(e['rm_gt0'], basis, True)} |",
        f"| BT-58 = 0 | {pct(e['rm_0'], basis)} |",
        f"| BT-58 fehlt | {pct(e['rm_fehlt'], basis)} |",
        f"| BT-58 = 0 oder fehlt, aber „verläng…“ im Text BT-57/BT-54 | {pct(e['ohne_rm_verl'], e['rm_0'] + e['rm_fehlt'])} |",
        "",
        f"Unter den {e['rm_gt0']} Zuschlägen mit BT-58 > 0 (Text = BT-57 und BT-54 zusammen):",
        "",
        "| | Anzahl |",
        "|---|---|",
        f"| BT-57 nicht leer | {pct(e['rm_gt0_57'], e['rm_gt0'])} |",
        f"| Text nennt Länge je Verlängerung („um jeweils ein Jahr“) | {pct(e['je'], e['rm_gt0'])} |",
        f"| Text nennt Höchstlaufzeit („maximale Laufzeit 4 Jahre“) | {pct(e['max'], e['rm_gt0'])} |",
        f"| Text nennt ein Datum | {pct(e['datum'], e['rm_gt0'])} |",
        f"| mindestens eine dieser Angaben | {pct(e['irgend'], e['rm_gt0'], True)} |",
        "",
        "**Bedeutet das Feld die Grundlaufzeit oder das Höchstende?** Vergleich mit der im Text genannten Höchstlaufzeit (±1 Monat = gleich):",
        "",
        "| Feld | n | Feld kürzer als Höchstlaufzeit | gleich | länger |",
        "|---|---|---|---|---|",
        f"| Beginn bis BT-537 | {v537['n']} | {pct(v537['kuerzer'], v537['n'], True)} | {v537['gleich']} | {v537['laenger']} |",
        f"| BT-36 | {v36['n']} | {pct(v36['kuerzer'], v36['n'], True)} | {v36['gleich']} | {v36['laenger']} |",
        "",
        "„Länger“ entsteht vor allem, wenn das Muster eine Höchstdauer **je Verlängerung** greift („maximal 12 Monate“).",
        "",
        f"**BT-36 neben Beginn und Ende** (beide angegeben, n = {sp['n']}): BT-36 gleich der Datumsspanne (±1 Monat) {pct(sp['gleich'], sp['n'], True)}, "
        f"BT-36 länger {pct(sp['kuerzer'], sp['n'], True)}, BT-36 kürzer {pct(sp['laenger'], sp['n'])}.",
        "",
        "Beispiele (BT-58 > 0, erste 8 in Dateireihenfolge):",
        "",
        "| Notice | Beginn | Ende | BT-36 (Mon.) | BT-58 | BT-57 (Auszug) |",
        "|---|---|---|---|---|---|",
        *[f"| {a} | {b} | {c} | {d or '–'} | {m} | {t.replace('|', '/')} |" for a, b, c, d, m, t in e["bsp"]],
        "",
        "## Fakten: vor eForms (A11-Zufallsstichprobe)",
        "",
        f"Referenzierte Ausschreibungen F02/F05 der 30 zufälligen Zuschläge 2018–2023 aus Iteration 3: **{v['dateien']}** Dateien.",
        "",
        "| | Anzahl |",
        "|---|---|",
        f"| `RENEWAL` (verlängerbar) | {pct(v['renewal'], v['dateien'])} |",
        f"| `NO_RENEWAL` | {pct(v['no_renewal'], v['dateien'])} |",
        f"| keine Angabe | {pct(v['keine_angabe'], v['dateien'])} |",
        f"| bei `RENEWAL`: `RENEWAL_DESCR` vorhanden | {pct(v['descr'], v['renewal'])} |",
        f"| bei `RENEWAL`: Text nennt Länge, Höchstlaufzeit oder Datum | {pct(v['irgend'], v['renewal'])} |",
        f"| Beginn bis DATE_END kürzer als genannte Höchstlaufzeit | {pct(vv['kuerzer'], vv['n'])} (gleich {vv['gleich']}, länger {vv['laenger']}) |",
        "",
        "Beispiele:",
        "",
        "| Notice | DATE_START | DATE_END | RENEWAL_DESCR (Auszug) |",
        "|---|---|---|---|",
        *[f"| {a} | {b} | {c} | {t.replace('|', '/')} |" for a, b, c, t in v["bsp"]],
        "",
        "## Interpretation",
        "",
        "- In der Praxis bezeichnet BT-537 das **Ende der Grundlaufzeit**; das gilt auch für `DATE_END` vor eForms. Für die Regeln in",
        "  `docs/business.md` §7.1 heißt das: „Ende der Grundlaufzeit“ = BT-537; das Höchstende muss aus BT-58 und dem Freitext",
        "  (BT-57, BT-54; vor eForms `RENEWAL_DESCR`) gewonnen werden.",
        "- BT-36 ist uneinheitlich (siehe Vergleich mit der Datumsspanne): teils Grundlaufzeit, teils Laufzeit mit Verlängerungen wie in",
        "  der Definition. Ist BT-36 länger als die Datumsspanne, ist das ein Hinweis auf das Höchstende. „Beginn + BT-36“ als Ende der",
        "  Grundlaufzeit betrifft nur wenige Zuschläge ohne Enddatum, ist aber unsicher.",
        "- BT-58 allein reicht nicht: Es nennt nur die Zahl der Verlängerungen, nicht ihre Länge. Die Länge steht meist im Freitext.",
        "- Verlängerungen kommen auch ohne BT-58 > 0 vor (Text erwähnt „verläng…“; Obergrenze, weil auch „keine Verlängerung“ mitzählt).",
        "  Die Regel muss den Text daher auch dort lesen.",
        "- Die Zahlen beruhen auf groben Mustern. Wie gut eine Extraktion des Höchstendes wirklich ist, misst erst Schritt 3 an Beispielen.",
        "",
    ]
    REPORT.write_text("\n".join(out), encoding="utf-8")
    print(f"Report geschrieben: {REPORT}")


if __name__ == "__main__":
    main()
