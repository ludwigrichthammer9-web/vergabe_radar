"""Iteration 5, Schritt 3: Zuschlagstabelle je Los mit Ende der Grundlaufzeit, Höchstende und Herkunft (Phase 3).

Regeln: docs/business.md §7.1 (Prognoseziel, R0/R1) und die Lese-Regeln unten (festgelegt 2026-10-30, Schritt 3).
Grundlage der Lese-Regeln: reports/verlaengerung_praxis_iteration5.md (BT-537/DATE_END = Ende der Grundlaufzeit; Höchstende nur
aus BT-58 und Freitext).

Lese-Regeln
1. Ende der Grundlaufzeit (GL): Enddatum (BT-537, vor eForms DATE_END), sonst Beginn + Dauer (BT-536 + BT-36, vor eForms
   DATE_START + DURATION). Unplausibel und verworfen: Laufzeit <= 0 oder > 240 Monate (wie seit Iteration 1).
1a. Ausnahme (ergänzt nach der Prüfstichprobe, Entwicklungsteil): Nennt der Text das Enddatum ausdrücklich als spätestes Ende
   („endet spätestens am …“, „längstens bis zum …“, „inkl. Verlängerungen …“), ist das Enddatum das Höchstende (Herkunft
   „enddatum_ist_hoechstende“). Als GL gilt dann ein früheres Datum nach „zunächst … bis zum / am“ (Herkunft „text_zunaechst“),
   sonst bleibt GL = Enddatum (R0 und R1 fallen dann zusammen).
   _Nach dem Testdurchgang ergänzt (e2ecbe6):_ „zunächst“ im Satzfilter und „endet (der Vertrag) am …“ als früheres Ende. Betrifft
   nur GL in diesem Fall, nicht das getestete Höchstende.

1b. Ausnahme (Iteration 7, nach der Prüfung der Iteration 6; Fehlertyp „Enddatum der Bekanntmachung ist schon das Höchstende“, L1, L42, L43, L60):
   Nennt der Text eine kürzere feste Laufzeit, gilt diese als Ende der Grundlaufzeit (`kurze_festlaufzeit`). (a) Herkunft „text_festlaufzeit“: ein Datum nach
   „Festlaufzeit“, „feste Laufzeit“, „Grundlaufzeit“, „zunächst … bis“ liegt mehr als 20 Tage vor dem Enddatum; das Höchstende kommt wie sonst aus dem Text,
   sonst gilt das Enddatum. (b) Herkunft „text_laufzeit_option“: eine feste Dauer („Vertragsdauer beträgt zwei Jahre“, „Laufzeit von 2 Jahren“, „(2+1+1)“) ergibt mit dem Beginn
   ein Ende mehr als 31 Tage vor dem Enddatum (Dauer mindestens 12 Monate, keine Fristen), und das Enddatum passt (± 31 Tage) zum Höchstende aus Anzahl × Länge,
   Höchstlaufzeit, BT-36 oder der Summe (ein Datum im Text zählt nicht, es wäre meist das Enddatum selbst); Höchstende = Enddatum. Beide nur, wenn der Text von Verlängerung oder Option spricht. Regel 1a hat Vorrang. Vor dem Ziehen der Stichprobe der Iteration 7 festgelegt.

Genauigkeit des Höchstendes (Teststichprobe, Fassung a0aa419): 53/60 richtig, gewichtet etwa 91 %; Fehler fast nur bei
„unbestimmbar“ (reports/hoechstende_pruefung_iteration5_test.md).
2. Text = BT-57 + BT-54 + BT-24 des Loses (vor eForms RENEWAL_DESCR; die Funktion `hoechstende` nimmt jeden Text).
3. Kandidaten für das Höchstende (alle, die gefunden werden):
   a) Datum im Text, das nach GL liegt (z. B. „spätestens zum 31.12.2027“),
   b) Höchstlaufzeit im Text („maximale Vertragslaufzeit 4 Jahre“) ab Beginn,
   c) BT-36 länger als die Spanne Beginn–GL (BT-36 schließt laut Definition Verlängerungen ein),
   d) Anzahl × Länge: Anzahl aus BT-58 (> 0), sonst aus dem Text („zweimal“, „2 x“, „3-malig“); Länge aus dem Text
      („um jeweils ein Jahr“, „12 Monate“, „Schuljahr“ = 12 Monate); Höchstende = GL + Anzahl × Länge.
   Datum und Höchstlaufzeit werden nur in Sätzen gesucht, die von Verlängerung, Option, Laufzeit oder Ende sprechen; Anzahl und
   Länge nur in Sätzen mit „verläng…“ oder „Option“ (Beschreibungen enthalten z. B. „3 x wöchentlich“).
   Plausibel ist ein Kandidat, wenn er nach GL und höchstens 10 Jahre nach GL liegt. **Gewählt wird der späteste plausible
   Kandidat.** Grund: Im Text stehen auch Kündigungstermine nach GL, die vor dem Höchstende liegen.
4. Kein Kandidat:
   - ausdrücklich keine Verlängerung (BT-58 = 0, vor eForms NO_RENEWAL, oder „keine Verlängerung“ im Text) → Höchstende = GL,
     Herkunft „keine_verlaengerung“;
   - keine Angabe (BT-58 fehlt und kein „verläng…“ im Text) → Höchstende = GL, Herkunft „keine_angabe“
     (§7.1: „Fehlt eine Verlängerungsangabe, gilt das Ende der Grundlaufzeit“);
   - sonst (Verlängerung erwähnt, aber nicht bezifferbar, z. B. rollierend ohne Höchstzahl) → Höchstende unbestimmbar.
5. R0 = GL − 6 Monate; R1 = Höchstende − 6 Monate, bei unbestimmbarem Höchstende GL − 6 Monate (§7.1, Festlegung 4).
6. Lose: Die API liefert je Feld eine Liste. Ist sie so lang wie die Liste der Lostitel, wird sie Los für Los zugeordnet. Ist sie
   kürzer und alle Werte gleich, gilt der Wert für alle Lose; sonst bleibt das Feld leer (Herkunft „liste_unvollstaendig“).

Aufruf:  python src/prepare/vertragsliste.py [Berichtspfad]
Ausgabe: data/processed/vertragsliste_909.csv, reports/vertragsliste_iteration5.md (Kennzahl X4) bzw. der angegebene Berichtspfad
         (Iteration 7: reports/vertragsliste_iteration7.md; die Fassung der Iteration 6 liegt als vertragsliste_909_iteration6.csv)
"""

import calendar
import csv
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analyze_completeness import PROJECT_ROOT, RAW_SEARCH_DIR, load_notices  # noqa: E402
from kennzahlen_iteration2 import wilson  # noqa: E402
from population_iteration4 import exclusion_reason  # noqa: E402

RUN = "DEU_result_cpv909_20231025_20260930_lostext"
OUT_CSV = PROJECT_ROOT / "data" / "processed" / "vertragsliste_909.csv"
REPORT = PROJECT_ROOT / "reports" / "vertragsliste_iteration5.md"
X4_VON, X4_BIS = "2025-10-01", "2026-09-30"
MAX_MONATE = 240
MAX_NACH_GL = 120  # Monate

ZAHL = {"ein": 1, "eine": 1, "einen": 1, "einem": 1, "einer": 1, "eines": 1, "zwei": 2, "drei": 3, "vier": 4, "fünf": 5,
        "sechs": 6, "sieben": 7, "acht": 8, "neun": 9, "zehn": 10, "zwölf": 12, "einmal": 1, "zweimal": 2, "dreimal": 3,
        "viermal": 4, "fünfmal": 5}
Z = r"(\d+|ein(?:e[mnrs]?)?|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|zwölf)"
EINHEIT = r"(schul|vertrags|leistungs)?(jahre?n?|monate?n?)"
RE_DATUM = re.compile(r"\b(\d{1,2})\.\s?(\d{1,2})\.\s?(20\d{2})\b")
RE_MAX = re.compile(rf"(?i)(maximale?n?\s*(?:gesamt)?(?:vertrags|leistungs)?(?:laufzeit|dauer)|gesamtlaufzeit|insgesamt\s+(?:maximal|höchstens)"
                    rf"|längstens|höchstlaufzeit|maximal\s+bis\s+zu\s+einer\s+(?:gesamt)?laufzeit\s+von|\bauf\s+max(?:imal|\.)"
                    rf"|verlängerung\s+(?:auf\s+)?max(?:imal|\.))\D{{0,30}}?\b{Z}\b\s*(?:\(\d+\)\s*)?{EINHEIT}")
# Enddatum ist selbst das Höchstende, wenn der Text genau dieses Datum als spätestes Ende nennt („endet spätestens am …“)
RE_SPAETESTENS = re.compile(r"(?i)(spätestens|längstens|maximal|höchstens|inkl\.?|einschließlich|inklusive)[^.]{0,80}?"
                            r"\b(\d{1,2})\.\s?(\d{1,2})\.\s?(20\d{2})\b")
RE_ZUNAECHST = re.compile(r"(?i)(?:zunächst[^.]{0,60}?(?:bis\s+(?:zum\s+)?|am\s+)|endet\s+(?:der\s+vertrag\s+)?am\s+)"
                          r"(\d{1,2})\.\s?(\d{1,2})\.\s?(20\d{2})\b")
RE_LAENGE = re.compile(rf"(?i)\b(?:je(?:weils)?|um|x|×)\s+(?:weitere[nrs]?\s+)?{Z}\s*(?:\(\d+\)\s*)?(?:weitere[nrs]?\s+)?{EINHEIT}"
                       rf"|\b(ein|zwei|drei)jährige")
RE_ANZAHL = re.compile(rf"(?i)\b{Z}\s*(?:-\s*)?(?:mal(?:ig\w*)?|fach\w*|x|×)(?!\w)|\b(einmal|zweimal|dreimal|viermal|fünfmal)(?:ig\w*)?\b"
                       rf"|bis\s+zu\s+{Z}\s*mal")
RE_KEINE = re.compile(r"(?i)keine\s+(weiteren?\s+)?verlängerung|nicht\s+verlängert|verlängerung(soption)?\s+(ist\s+)?ausgeschlossen")
RE_VERL = re.compile(r"(?i)verläng")
# Nur in passenden Sätzen suchen: Beschreibungen enthalten z. B. „3 x wöchentlich“ oder Termine anderer Art.
RE_SATZ_VERL = re.compile(r"(?i)verläng|option")
RE_SATZ_ENDE = re.compile(r"(?i)verläng|option|spätestens|längstens|maximal|höchst|laufzeit|vertragsdauer|vertragsende|endet"
                          r"|zunächst")
RE_SATZGRENZE = re.compile(r"(?<=[.!?;])\s+(?=[A-ZÄÖÜ])|\n")
# Regel 1b (Iteration 7): kurze feste Laufzeit im Text. Datum: „Festlaufzeit von 01.01.2026-31.03.2030“, „erste feste Laufzeit bis zum 14.07.2028“.
_D = r"(\d{1,2})\.\s?(\d{1,2})\.\s?(20\d{2})"
RE_FEST_DATUM = re.compile(rf"(?i)(?:fest\s*laufzeit|feste\s+laufzeit|grundlaufzeit|mindestlaufzeit|erstlaufzeit)\s*(?:des\s+vertrage?s\s+)?"
                           rf"(?:von|bis(?:\s+zum)?|ist|beträgt|:)?\s*(?:{_D}\s*(?:-|–|bis(?:\s+zum)?)\s*)?{_D}")
# Dauer: „Die Vertragsdauer beträgt zwei Jahre …“, „Laufzeit von 2 Jahren“, „für die Dauer von 4 Jahren“ (nicht „maximale/gesamte/längstens …“).
RE_BASIS_DAUER = re.compile(rf"(?i)(?:(?:vertrags)?laufzeit|vertragsdauer|beauftragung|vertragsverhältnis|vertrag)[^.]{{0,60}}?"
                            rf"\b(?:von|beträgt|dauer\s+von)\s+{Z}\s*(?:\(\d+\)\s*)?{EINHEIT}")
RE_BASIS_AUSSCHLUSS = re.compile(r"(?i)(maximal|gesamt|insgesamt|längstens|höchstens|spätestens|bis\s+zu)\w*\s*\w*\s*$")
RE_SUMME = re.compile(r"\(\s*(\d{1,2}(?:\s*\+\s*\d{1,2})+)\s*\)")  # „(2+1+1)“ = 2 Jahre fest, dann 1 + 1 Jahr Option


def saetze(text: str, muster: re.Pattern) -> str:
    return " ".join(s for s in RE_SATZGRENZE.split(text) if muster.search(s))


def zahl(s: str) -> int | None:
    s = s.lower()
    return int(s) if s.isdigit() else ZAHL.get(s)


def plus_monate(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    y, mo = d.year + y, mo + 1
    return date(y, mo, min(d.day, calendar.monthrange(y, mo)[1]))


def ende_nach_monaten(beginn: date, m: int) -> date:
    """Letzter Tag einer Laufzeit von m Monaten ab Beginn (01.01.2026 + 24 Monate = 31.12.2027)."""
    return plus_monate(beginn, m) - timedelta(days=1)


def monate(beginn: date, ende: date) -> int:
    return round(((ende - beginn).days + 1) / 30.4375)


def iso(s) -> date | None:
    try:
        return date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


def grundlaufzeit(beginn: date | None, ende: date | None, dauer_monate: int | None) -> tuple[date | None, str]:
    if ende:
        if beginn and not 0 < monate(beginn, ende) <= MAX_MONATE:
            return None, "unplausibel"
        return ende, "enddatum"
    if beginn and dauer_monate:
        if not 0 < dauer_monate <= MAX_MONATE:
            return None, "unplausibel"
        return ende_nach_monaten(beginn, dauer_monate), "beginn_plus_dauer"
    return None, "unbekannt"


def _in_monate(n: int, einheit: str) -> int:
    return n * 12 if einheit.lower().startswith("jahr") else n


def _datum(t: str, m: str, j: str) -> date | None:
    try:
        return date(int(j), int(m), int(t))
    except ValueError:
        return None


def kandidaten(gl: date, beginn: date | None, text: str, anzahl: int | None, dauer_monate: int | None) -> list[tuple[date, str]]:
    out = []
    text_ende, text_verl = saetze(text, RE_SATZ_ENDE), saetze(text, RE_SATZ_VERL)
    for t, mo, j in RE_DATUM.findall(text_ende):
        if d := _datum(t, mo, j):
            out.append((d, "datum_text"))
    if beginn:
        for m in RE_MAX.finditer(text_ende):
            n = zahl(m.group(2))
            if n and 0 < _in_monate(n, m.group(4)) <= MAX_MONATE:
                out.append((ende_nach_monaten(beginn, _in_monate(n, m.group(4))), "hoechstlaufzeit_text"))
        if dauer_monate and monate(beginn, gl) + 1 < dauer_monate <= MAX_MONATE:
            out.append((ende_nach_monaten(beginn, dauer_monate), "bt36_laenger"))
    laengen = []
    for m in RE_LAENGE.finditer(text_verl):
        if m.group(4):
            laengen.append(12 * zahl(m.group(4)))
        elif (n := zahl(m.group(1))):
            laengen.append(_in_monate(n, m.group(3)))
    if not anzahl:
        for m in RE_ANZAHL.finditer(text_verl):
            n = zahl(next(g for g in m.groups() if g))
            if n and n <= 10:
                anzahl = max(anzahl or 0, n)
    laengen = [m for m in laengen if 0 < m <= MAX_NACH_GL]
    if anzahl and anzahl <= 10 and laengen:
        out.append((plus_monate(gl, anzahl * max(laengen)), "anzahl_x_laenge"))
    return out


def hoechstende(gl: date | None, beginn: date | None, text: str, anzahl: int | None, dauer_monate: int | None,
                verlaengerbar: bool | None) -> tuple[date | None, str]:
    """Höchstende und Herkunft nach den Lese-Regeln 3 und 4. `anzahl` = BT-58 (> 0) oder None; `verlaengerbar` = False bei
    BT-58 = 0 bzw. NO_RENEWAL, True bei BT-58 > 0 bzw. RENEWAL, None ohne Angabe."""
    if gl is None:
        return None, "keine_grundlaufzeit"
    grenze = plus_monate(gl, MAX_NACH_GL)
    plausibel = [(d, h) for d, h in kandidaten(gl, beginn, text, anzahl, dauer_monate) if gl < d <= grenze]
    if plausibel:
        return max(plausibel)
    if verlaengerbar is False or (verlaengerbar is None and RE_KEINE.search(text)):
        return gl, "keine_verlaengerung"
    if verlaengerbar is None and not RE_VERL.search(text):
        return gl, "keine_angabe"
    return None, "unbestimmbar"


def kurze_festlaufzeit(beginn: date | None, gl: date, text: str, anzahl: int | None,
                       dauer_monate: int | None) -> tuple[date, str] | None:
    """Regel 1b: Das Enddatum ist laut Text schon das Höchstende; liefert das frühere Ende der festen Laufzeit und die Herkunft.
    (a) „text_festlaufzeit“: Der Text nennt ein Datum der festen Laufzeit, das mehr als 20 Tage vor dem Enddatum liegt.
    (b) „text_laufzeit_option“: Der Text nennt eine feste Dauer (oder „2+1+1“), Beginn + Dauer liegt mehr als 31 Tage vor dem Enddatum, und das
        Enddatum passt (± 31 Tage) zu einem Höchstende, das sich aus Anzahl × Länge, Höchstlaufzeit, Datum im Text oder der Summe ergibt.
    Beide nur, wenn der Text von Verlängerung oder Option spricht."""
    if not saetze(text, RE_SATZ_VERL):
        return None
    dauern, summen = [], []
    if beginn is not None:
        for m in RE_BASIS_DAUER.finditer(text):
            if (RE_BASIS_AUSSCHLUSS.search(text[max(0, m.start() - 25):m.start()])
                    or re.search(r"(?i)frist|kündig|widerspr|maximal|gesamt|längstens|höchstens|spätestens|bis\s+zu", m.group(0))):
                continue
            n = zahl(m.group(1))
            if n and 12 <= (mo := _in_monate(n, m.group(3))) <= MAX_MONATE:  # unter 12 Monaten meist Fristen, keine feste Laufzeit
                dauern.append(mo)
        if "jahr" in text.lower():
            for m in RE_SUMME.finditer(text):
                teile = [int(t) for t in re.split(r"\s*\+\s*", m.group(1))]
                if all(0 < t <= 10 for t in teile) and sum(teile) <= 20:
                    dauern.append(12 * teile[0])
                    summen.append(ende_nach_monaten(beginn, 12 * sum(teile)))
        # Erklärt eine genannte Dauer das Enddatum schon (Beginn + Dauer ≈ Enddatum), ist es die Grundlaufzeit; ein anderes Datum im Text
        # gehört dann meist zu einem anderen Los oder Objekt.
        if any(abs((ende_nach_monaten(beginn, mo) - gl).days) <= 31 for mo in dauern):
            return None
    daten = [_datum(*m.groups()[3:]) for m in RE_FEST_DATUM.finditer(text)] + [_datum(*m.groups()) for m in RE_ZUNAECHST.finditer(text)]
    fruehere = [d for d in daten if d and (beginn is None or d > beginn) and d < gl - timedelta(days=20)]
    if fruehere:
        return max(fruehere), "text_festlaufzeit"
    if beginn is None:
        return None
    for mo in sorted(set(dauern)):
        gl_neu = ende_nach_monaten(beginn, mo)
        if gl_neu >= gl - timedelta(days=31):
            continue
        # Datum im Text zählt nicht: Das Enddatum steht meist selbst im Text und würde die Prüfung trivial erfüllen.
        hoechst = [d for d, q in kandidaten(gl_neu, beginn, text, anzahl, dauer_monate) if q != "datum_text"] + summen
        if any(abs((d - gl).days) <= 31 for d in hoechst):
            return gl_neu, "text_laufzeit_option"
    return None


def laufzeit(beginn: date | None, ende: date | None, dauer_monate: int | None, text: str, anzahl: int | None,
             verlaengerbar: bool | None) -> tuple[date | None, str, date | None, str]:
    """Ende der Grundlaufzeit und Höchstende mit Herkunft (Lese-Regeln 1, 3, 4, 1a und 1b)."""
    gl, gl_h = grundlaufzeit(beginn, ende, dauer_monate)
    if gl:
        text_ende = saetze(text, RE_SATZ_ENDE)
        if any(_datum(*m.groups()[1:]) == gl for m in RE_SPAETESTENS.finditer(text_ende)):
            frueher = [d for m in RE_ZUNAECHST.finditer(text_ende) if (d := _datum(*m.groups()))
                       and (beginn is None or d > beginn) and d < gl]
            if frueher:
                return max(frueher), "text_zunaechst", gl, "enddatum_ist_hoechstende"
            return gl, gl_h, gl, "enddatum_ist_hoechstende"
        if gl_h == "enddatum" and (neu := kurze_festlaufzeit(beginn, gl, text, anzahl, dauer_monate)):
            gl_neu, gl_neu_h = neu
            if gl_neu_h == "text_laufzeit_option":
                return gl_neu, gl_neu_h, gl, "enddatum_ist_hoechstende"
            h, h_h = hoechstende(gl_neu, beginn, text, anzahl, dauer_monate, verlaengerbar)
            if h is None or h <= gl_neu:  # keine Angabe zum Höchstende: das spätere Enddatum der Bekanntmachung gilt als Höchstende
                return gl_neu, gl_neu_h, gl, "enddatum_ist_hoechstende"
            return gl_neu, gl_neu_h, h, h_h
    h, h_h = hoechstende(gl, beginn, text, anzahl, dauer_monate, verlaengerbar)
    return gl, gl_h, h, h_h


def prognosen(gl: date | None, hoechst: date | None) -> tuple[date | None, date | None]:
    r0 = plus_monate(gl, -6) if gl else None
    r1 = plus_monate(hoechst or gl, -6) if (hoechst or gl) else None
    return r0, r1


# ---------------------------------------------------------------------------------------------------------------------
# eForms-Zuschläge aus der API

def _liste(value) -> list:
    if value is None:
        return []
    if isinstance(value, dict):
        value = value.get("deu") or next(iter(value.values()), [])
    return value if isinstance(value, list) else [value]


def je_los(notice: dict, feld: str, n_lose: int) -> tuple[list, bool]:
    """Werte eines Feldes je Los; zweiter Wert False, wenn die Liste nicht eindeutig zuzuordnen war."""
    werte = _liste(notice.get(feld))
    if len(werte) == n_lose or not werte:
        return (werte or [None] * n_lose), True
    if len(set(map(str, werte))) == 1:
        return [werte[0]] * n_lose, True
    return [None] * n_lose, False


def _dauer(p) -> int | None:
    if not isinstance(p, dict) or not str(p.get("value", "")).isdigit():
        return None
    return int(p["value"]) * {"YEAR": 12, "MONTH": 1}.get(p.get("unit"), 0) or None


def zeilen(notice: dict) -> list[dict]:
    titel = [str(t) for t in _liste(notice.get("title-lot"))] or [""]
    n = len(titel)
    felder = {}
    eindeutig = True
    for key, feld in (("beginn", "contract-duration-start-date-lot"), ("ende", "contract-duration-end-date-lot"),
                      ("dauer", "contract-duration-period-lot"), ("bt58", "renewal-maximum-lot"),
                      ("bt57", "renewal-description-lot"), ("bt54", "option-description-lot"), ("bt24", "description-lot")):
        felder[key], ok = je_los(notice, feld, n)
        eindeutig &= ok
    out = []
    for i in range(n):
        beginn, ende, dauer = iso(felder["beginn"][i]) if felder["beginn"][i] else None, \
            iso(felder["ende"][i]) if felder["ende"][i] else None, _dauer(felder["dauer"][i])
        bt58 = int(felder["bt58"][i]) if str(felder["bt58"][i] or "").isdigit() else None
        text = " ".join(str(felder[k][i] or "") for k in ("bt57", "bt54", "bt24"))
        verl = None if bt58 is None else bt58 > 0
        gl, gl_h, h, h_h = laufzeit(beginn, ende, dauer, text, bt58 if bt58 else None, verl)
        r0, r1 = prognosen(gl, h)
        # Iteration 6: Ende nur geschätzt (Veröffentlichung + Dauer), wenn kein Beginn und kein Enddatum, aber eine Dauer vorliegt.
        # Zählt weder für die Abdeckung Y3 noch für die Genauigkeit Y1; Spalte nur für den Prototyp (als „geschätzt“ zu kennzeichnen).
        pub = iso(notice.get("publication-date", ""))
        geschaetzt = ende_nach_monaten(pub, dauer) if (gl is None and dauer and 0 < dauer <= MAX_MONATE and pub) else ""
        out.append({
            "notice": notice["publication-number"], "veroeffentlicht": str(notice.get("publication-date", ""))[:10],
            "auftraggeber": (_liste(notice.get("buyer-name")) or [""])[0], "los": i + 1, "los_titel": titel[i][:120],
            "beginn": beginn or "", "gl_ende": gl or "", "gl_herkunft": gl_h, "bt58": "" if bt58 is None else bt58,
            "hoechstende": h or "", "hoechstende_herkunft": h_h, "r0": r0 or "", "r1": r1 or "",
            "liste_eindeutig": eindeutig, "gl_geschaetzt": geschaetzt,
        })
    return out


def pct(k: int, n: int, ki: bool = False) -> str:
    if not n:
        return "–"
    s = f"{k}/{n} = {100 * k / n:.1f} %"
    if ki:
        lo, hi = wilson(k, n)
        s += f" (Wilson {100 * lo:.1f}–{100 * hi:.1f})"
    return s.replace(".", ",")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rows, ausgeschlossen = [], 0
    for x in load_notices(RAW_SEARCH_DIR / RUN):
        if exclusion_reason(x):
            ausgeschlossen += 1
            continue
        rows.extend(zeilen(x))
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=";")
        w.writeheader()
        w.writerows(rows)

    x4 = [r for r in rows if X4_VON <= r["veroeffentlicht"] <= X4_BIS]
    mit_r1 = sum(1 for r in x4 if r["r1"])
    mit_geschaetzt = sum(1 for r in x4 if r["r1"] or r["gl_geschaetzt"])
    def zaehle(rs, key):
        out = {}
        for r in rs:
            out[r[key]] = out.get(r[key], 0) + 1
        return sorted(out.items(), key=lambda t: -t[1])
    mit_gl = [r for r in rows if r["gl_ende"]]
    lines = [
        "# Vertragsliste aus Zuschlägen (Iteration 5, Schritt 3)",
        "",
        "_Erzeugt mit `src/prepare/vertragsliste.py`; Regeln im Kopf des Skripts und in `docs/business.md` §7.1._",
        "",
        "## Fakten",
        "",
        f"- Datenbasis: eForms-Zuschläge `{RUN}`; Population wie Iteration 4 (`population_iteration4.exclusion_reason`), "
        f"{ausgeschlossen} Notices ausgeschlossen.",
        f"- Tabelle: {len(rows)} Lose aus {len({r['notice'] for r in rows})} Zuschlägen (`{OUT_CSV.relative_to(PROJECT_ROOT).as_posix()}`, nicht im Git).",
        f"- Lose mit nicht eindeutig zuordenbarer Feldliste: {sum(1 for r in rows if not r['liste_eindeutig'])}.",
        "",
        f"### X4 Abdeckung (Lose aus Zuschlägen, veröffentlicht {X4_VON} bis {X4_BIS})",
        "",
        f"**R1 liefert ein Datum: {pct(mit_r1, len(x4), True)}** (Schwelle ≥ 80 %, vorab festgelegt).",
        "",
        f"Zusätzlich (Iteration 6, nur Hinweis, zählt nicht für X4/Y3): mit **geschätztem** Ende (Veröffentlichung + Dauer, wenn nur die Dauer vorliegt) "
        f"{pct(mit_geschaetzt, len(x4), True)}.",
        "",
        "| Herkunft Ende der Grundlaufzeit | Lose |",
        "|---|---|",
        *[f"| {k} | {pct(v, len(x4))} |" for k, v in zaehle(x4, "gl_herkunft")],
        "",
        "### Herkunft des Höchstendes (alle Lose mit Ende der Grundlaufzeit)",
        "",
        "| Herkunft | Lose |",
        "|---|---|",
        *[f"| {k} | {pct(v, len(mit_gl))} |" for k, v in zaehle(mit_gl, "hoechstende_herkunft")],
        "",
        "### Genauigkeit der Lese-Regeln",
        "",
        "- Entwicklungsstichprobe (40 Lose, vor Regel 1a): 30 richtig; Fehler führten zu Regel 1a und weiteren Mustern",
        "  ([hoechstende_pruefung_iteration5_entwicklung.md](hoechstende_pruefung_iteration5_entwicklung.md)).",
        "- Teststichprobe (60 Lose, nach dem Einfrieren gezogen, Fassung a0aa419): Höchstende 53/60 richtig, gewichtet etwa 91 %;",
        "  Fehler fast nur bei „unbestimmbar“ ([hoechstende_pruefung_iteration5_test.md](hoechstende_pruefung_iteration5_test.md)).",
        "  Urteile von Claude allein.",
        "",
        "## Interpretation",
        "",
        "- X4 liegt knapp unter der Schwelle von 80 %. Ursache ist fast nur, dass bei etwa 20 % der Lose gar keine Laufzeit angegeben ist;",
        "  das Höchstende spielt für X4 keine Rolle (R1 fällt auf die Grundlaufzeit zurück). Laut Vorab-Regel kein Abbruch, die",
        "  Abdeckung wird im Prototyp genannt.",
        "- Wo eine Laufzeit vorliegt, ist das Höchstende meist lesbar. Bleibt es unbestimmbar, liegt R1 eher zu früh.",
        "",
    ]
    ziel = Path(sys.argv[1]) if len(sys.argv) > 1 else REPORT  # optional: anderer Berichtspfad, damit der Bericht der Iteration 5 bleibt
    ziel.write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(rows)} Lose; X4 = {pct(mit_r1, len(x4), True)}; Report: {ziel}")


if __name__ == "__main__":
    main()
