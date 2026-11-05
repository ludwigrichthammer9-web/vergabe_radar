"""Iteration 9, Schritt 3/4: Auswertung der KI-Lesung (V1 bis V8) mit **neutraler Definition** des Vergleichswerts.

Vorab festgelegt (docs/iterationen.md, Iteration 9; dieses Skript wird vor dem Eintreffen der Antworten committet):
- Die Leser tragen nur Fakten ein (`beginn`, `feld_enddatum`, `feste_dauer_monate`, `feste_ende`, `verl_status`, `verl_anzahl`, `verl_monate`, `spaetestes_ende`,
  `gesamtdauer_monate`, `nicht_tagesgenau`, `kein_zuschlag`, …). Der Wert je Leser wird hier mit der Definition unten berechnet; die Projektregeln werden nicht benutzt.
- Ende der Grundlaufzeit (Definition): (1) `nicht_tagesgenau` = ja → ausgenommen; (2) ausdrückliches Ende der festen Laufzeit (`feste_ende`);
  (3) sonst Beginn + `feste_dauer_monate` − 1 Tag; (4) sonst das Feld-Enddatum, wenn für das Los keine Verlängerung genannt ist (`keine`, `nichts_genannt`) oder wenn bei genannter Verlängerung
  das Feld nicht selbst das späteste Ende ist (es ist es, wenn es dem `spaetestes_ende` entspricht oder Beginn + `gesamtdauer_monate` − 1 Tag um höchstens 31 Tage trifft);
  (5) sonst `unbekannt`.
- Höchstende (Definition): `spaetestes_ende`; sonst Beginn + `gesamtdauer_monate` − 1 Tag; sonst bei `keine` / `nichts_genannt` das Ende der Grundlaufzeit (Kategorie „keine“ bzw. „keine Angabe“);
  bei `genannt` mit Anzahl und Länge Ende der Grundlaufzeit + Anzahl × Länge; sonst `unbestimmbar`. Ist das Feld selbst das späteste Ende und gibt es keine Grundlaufzeit, gilt das Feld als Höchstende.
- Vergleichswert: Stimmen Leser A und B überein (Datum ± 1 Tag oder gleiche Kategorie), gilt der Wert; sonst gilt die Entscheidung des Evaluators (`reports/zweitlesung_iteration9_entscheide.csv`),
  ersatzweise `unklar` (zählt als Abweichung der Liste). `nicht_tagesgenau` (bei mindestens einem Leser) nimmt das Los aus Zähler und Nenner und wird einzeln ausgewiesen.
- V1 Z-Lose (70), Schwelle ≥ 90 %; V2 R- und M-Lose (30), ≥ 80 %; V3 neue Fassung auf Z nicht schlechter als die alte (`gl_ende_alt`); V4 Höchstende auf Z (≥ 90 % bzw. ≥ 85 % bei behauptetem Höchstende,
  streng ohne „unbestimmbar = korrekt“ beschreibend); V5 Übereinstimmung A/B beim Ende der Grundlaufzeit über alle 110 Lose (≥ 90 %); V6 Kommilitone: Vergleichswert = Eintrag bei 15 Losen (≥ 13/15);
  V7 kein V-Los (Z, R, M), für das ein Leser `kein_zuschlag` = ja meldet; V8 Verfahren (Commit-Reihenfolge, Sitzung ohne CLAUDE.md, Rohtexte unverändert) wird im Bericht des Evaluators geprüft.
- Beschreibend: S-Lose (Regel 6), gebaeudereinigung = nein (A12), `zuordnung_sicher` = nein, Kontrolle durch den Evaluator (10 Z-/R-/M-Lose, Seed 20261110, `reports/zweitlesung_iteration9_evaluator.tsv`).

Eingaben: `reports/zweitlesung_iteration9_roh/leser_{a,b}_teil{1-5}.tsv` (Antworten unverändert), `data/processed/stichprobe_iteration9_schluessel.csv` (SHA-256 im Commit),
`reports/zweitlesung_iteration9_mensch.csv` (Spalten N;ende_gl;hoechstende;kein_zuschlag;hilfsmittel;minuten; aus dem Blatt übertragen).

Aufruf:  .venv\\Scripts\\python -I src/prepare/auswertung_iteration9.py      Ausgabe: reports/zweitlesung_iteration9_auswertung.md
"""

import calendar
import csv
import hashlib
import math
import random
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PROC = ROOT / "data" / "processed"
R = ROOT / "reports"
SCHLUESSEL = PROC / "stichprobe_iteration9_schluessel.csv"
ROH = R / "zweitlesung_iteration9_roh"
ENTSCHEIDE = R / "zweitlesung_iteration9_entscheide.csv"      # N;gl;hoechstende;begruendung (gl/hoechstende: Datum, unbekannt, unbestimmbar, keine, keine_angabe oder unklar)
MENSCH = R / "zweitlesung_iteration9_mensch.csv"
EVALUATOR = R / "zweitlesung_iteration9_evaluator.tsv"
REPORT = R / "zweitlesung_iteration9_auswertung.md"
SEED_EVALUATOR, N_EVALUATOR = 20261110, 10
N_TEILE = 5


def datum(s: str) -> date | None:
    s = (s or "").strip()
    try:
        t, m, j = s.split(".")
        return date(int(j), int(m), int(t))
    except ValueError:
        return None


def plus_monate(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    y, mo = d.year + y, mo + 1
    return date(y, mo, min(d.day, calendar.monthrange(y, mo)[1]))


def ende_nach(d: date, m: int) -> date:
    return plus_monate(d, m) - timedelta(days=1)


def zahl(s: str) -> int | None:
    s = (s or "").strip()
    return int(s) if s.isdigit() else None


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return c - h, c + h


def pct(k: int, n: int) -> str:
    if not n:
        return "–"
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {100 * k / n:.1f} % (Wilson {100 * lo:.1f}–{100 * hi:.1f})".replace(".", ",")


def feld_ist_hoechstende(f: dict) -> bool:
    feld, spaet, beginn, gd = datum(f["feld_enddatum"]), datum(f["spaetestes_ende"]), datum(f["beginn"]), zahl(f["gesamtdauer_monate"])
    if not feld:
        return False
    return bool((spaet and abs((spaet - feld).days) <= 1) or (beginn and gd and abs((ende_nach(beginn, gd) - feld).days) <= 31))


def ende_gl(f: dict) -> tuple[str, date | None]:
    """Definition des Endes der Grundlaufzeit aus den Fakten eines Lesers (Kategorie, Datum)."""
    if f["nicht_tagesgenau"].strip().lower() == "ja":
        return "nicht_tagesgenau", None
    if d := datum(f["feste_ende"]):
        return "datum", d
    beginn, dm = datum(f["beginn"]), zahl(f["feste_dauer_monate"])
    if beginn and dm:
        return "datum", ende_nach(beginn, dm)
    feld = datum(f["feld_enddatum"])
    if not feld:
        return "unbekannt", None
    if f["verl_status"].strip() in ("keine", "nichts_genannt") or not feld_ist_hoechstende(f):
        return "datum", feld
    return "unbekannt", None


def hoechstende(f: dict, gl: tuple[str, date | None]) -> tuple[str, date | None]:
    """Definition des Höchstendes (Kategorie datum / keine / keine_angabe / unbestimmbar, Datum)."""
    if d := datum(f["spaetestes_ende"]):
        return "datum", d
    beginn, gd = datum(f["beginn"]), zahl(f["gesamtdauer_monate"])
    if beginn and gd:
        return "datum", ende_nach(beginn, gd)
    kat, g = gl
    vs = f["verl_status"].strip()
    if kat == "datum":
        if vs == "keine":
            return "keine", g
        if vs == "nichts_genannt":
            return "keine_angabe", g
        n, m = zahl(f["verl_anzahl"]), zahl(f["verl_monate"])
        if n and m:
            return "datum", plus_monate(g, n * m)
        return "unbestimmbar", None
    if kat == "unbekannt" and feld_ist_hoechstende(f):
        return "datum", datum(f["feld_enddatum"])
    return "unbestimmbar", None


def gleich(a: tuple[str, date | None], b: tuple[str, date | None]) -> bool:
    if a[1] and b[1]:
        return abs((a[1] - b[1]).days) <= 1
    return a[0] == b[0] and not a[1] and not b[1]


def kat_wert(s: str) -> tuple[str, date | None]:
    """Eintrag aus der Entscheidungs- oder Mensch-Datei: Datum oder Kategorie."""
    s = (s or "").strip().lower().replace(" ", "_")
    d = datum(s)
    return ("datum", d) if d else (s or "unklar", None)


def lese_tsv(p: Path) -> dict[str, dict]:
    with p.open(encoding="utf-8", newline="") as f:
        return {r["N"].strip(): {k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f, delimiter="\t")}


def lese_csv(p: Path) -> dict[str, dict]:
    if not p.exists():
        return {}
    with p.open(encoding="utf-8") as f:
        return {r["N"].strip(): r for r in csv.DictReader(f, delimiter=";")}


def liste_gl(r: dict) -> tuple[str, date | None]:
    d = datum(".".join(reversed(r["gl_ende"].split("-")))) if r["gl_ende"] else None
    return ("datum", d) if d else ("unbekannt", None)


def liste_h(r: dict) -> tuple[str, date | None]:
    if r["hoechstende_herkunft"] == "unbestimmbar":
        return "unbestimmbar", None
    d = datum(".".join(reversed(r["hoechstende"].split("-")))) if r["hoechstende"] else None
    return ("datum", d) if d else ("unbestimmbar", None)


def ok_gl(liste: tuple[str, date | None], ref: tuple[str, date | None]) -> bool:
    return bool(liste[1] and ref[1] and abs((liste[1] - ref[1]).days) <= 1)


def ok_h(r: dict, ref: tuple[str, date | None], streng: bool = False) -> bool:
    kat, d = liste_h(r)
    if kat == "unbestimmbar":
        return not streng
    if ref[1] and d:
        return abs((d - ref[1]).days) <= 1
    if ref[0] in ("keine", "keine_angabe") and d and r["gl_ende"]:
        return str(d) == r["gl_ende"]
    return False


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sha = hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()
    schl = {}
    with SCHLUESSEL.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            schl[r["N"]] = r
    antworten = {}
    for leser in "ab":
        antworten[leser] = {}
        for k in range(1, N_TEILE + 1):
            antworten[leser].update(lese_tsv(ROH / f"leser_{leser}_teil{k}.tsv"))
    fehlt = [n for n in schl if any(n not in antworten[l] for l in "ab")]
    assert not fehlt, f"Antworten fehlen: {fehlt}"
    ent, mensch, evaluator = lese_csv(ENTSCHEIDE), lese_csv(MENSCH), (lese_tsv(EVALUATOR) if EVALUATOR.exists() else {})

    v = {}
    for n in schl:
        fa, fb = antworten["a"][n], antworten["b"][n]
        ga, gb = ende_gl(fa), ende_gl(fb)
        ha, hb = hoechstende(fa, ga), hoechstende(fb, gb)
        ntg = "nicht_tagesgenau" in (ga[0], gb[0])
        einig_g, einig_h = gleich(ga, gb), gleich(ha, hb)
        e = ent.get(n)
        v[n] = {"ga": ga, "gb": gb, "ha": ha, "hb": hb, "ntg": ntg, "einig_g": einig_g, "einig_h": einig_h,
                "gl": ga if einig_g else (kat_wert(e["gl"]) if e and e["gl"].strip() else ("unklar", None)),
                "h": ha if einig_h else (kat_wert(e["hoechstende"]) if e and e["hoechstende"].strip() else ("unklar", None)),
                "kz": "ja" in (fa["kein_zuschlag"].lower(), fb["kein_zuschlag"].lower()),
                "rein": "nein" in (fa["gebaeudereinigung"].lower(), fb["gebaeudereinigung"].lower()),
                "unsicher": "nein" in (fa["zuordnung_sicher"].lower(), fb["zuordnung_sicher"].lower())}
    offen = [n for n in schl if (not v[n]["einig_g"] and v[n]["gl"][0] == "unklar" and not v[n]["ntg"]) or (not v[n]["einig_h"] and v[n]["h"][0] == "unklar")]
    gruppen = {g: [n for n in schl if schl[n]["gruppe"] == g] for g in "ZRMS"}
    vlose = gruppen["Z"] + gruppen["R"] + gruppen["M"]
    out = ["# Auswertung der KI-Lesung (Iteration 9, V1 bis V8)", "",
           f"_Erzeugt mit `src/prepare/auswertung_iteration9.py`. Schlüssel-SHA-256 `{sha[:8]}…{sha[-4:]}`. Vergleichswert nach der neutralen Definition im Kopf des Skripts. "
           "Leser A = Opus, Leser B = Sonnet, je 5 Teile in eigenen Sitzungen ohne Projektkontext._", "", "## Fakten", ""]
    einig = sum(v[n]["einig_g"] for n in schl)
    out += [f"- **V5 (Leser A = B beim Ende der Grundlaufzeit, {len(schl)} Lose): {pct(einig, len(schl))}** (Schwelle ≥ 90 %). Höchstende einig: {sum(v[n]['einig_h'] for n in schl)}/{len(schl)}."]
    ev_lose = sorted(random.Random(SEED_EVALUATOR).sample(sorted(vlose, key=lambda x: int(x[1:])), N_EVALUATOR), key=lambda x: int(x[1:]))
    out += [f"- Kontrolle des Evaluators (Seed {SEED_EVALUATOR}): {', '.join(ev_lose)}."]
    if offen:
        out += ["", f"**Noch offen:** Entscheidung des Evaluators für {', '.join(offen)}. V1 bis V4 und V6 werden erst danach berechnet."]
        REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"V5 {einig}/{len(schl)}; offen: {offen}")
        return

    def zaehlbar(ns: list[str]) -> list[str]:
        return [n for n in ns if not v[n]["ntg"]]

    z, rm = zaehlbar(gruppen["Z"]), zaehlbar(gruppen["R"] + gruppen["M"])
    ok_neu = {n: ok_gl(liste_gl(schl[n]), v[n]["gl"]) for n in schl}
    ok_alt = {n: ok_gl(liste_gl({"gl_ende": schl[n]["gl_ende_alt"]}), v[n]["gl"]) for n in schl}
    k1, k2 = sum(ok_neu[n] for n in z), sum(ok_neu[n] for n in rm)
    h_ok = {n: ok_h(schl[n], v[n]["h"]) for n in schl}
    h_streng = {n: ok_h(schl[n], v[n]["h"], True) for n in schl}
    behauptet = [n for n in z if schl[n]["hoechstende_herkunft"] != "unbestimmbar"]
    kz = [n for n in vlose if v[n]["kz"]]
    out += [f"- **V1 (Liste = Vergleichswert, Z-Lose, ohne „nicht tagesgenau“): {pct(k1, len(z))}** (Schwelle ≥ 63/70 = 90 %).",
            f"- **V2 (R- und M-Lose): {pct(k2, len(rm))}** (Schwelle ≥ 24/30 = 80 %).",
            f"- **V3 (neue Fassung nicht schlechter als die alte, Z-Lose):** neu {sum(ok_neu[n] for n in z)}/{len(z)}, alt {sum(ok_alt[n] for n in z)}/{len(z)} → "
            f"{'erfüllt' if sum(ok_neu[n] for n in z) >= sum(ok_alt[n] for n in z) else 'verfehlt'}.",
            f"- **V4 (Höchstende, Z-Lose): {pct(sum(h_ok[n] for n in z), len(z))}** (Schwelle ≥ 90 %); **nur behauptetes Höchstende: {pct(sum(h_ok[n] for n in behauptet), len(behauptet))}** "
            f"(Schwelle ≥ 85 %); streng ohne „unbestimmbar = korrekt“: {pct(sum(h_streng[n] for n in z), len(z))}.",
            f"- **V7 (V-Lose, für die ein Leser „kein Zuschlag“ meldet): {len(kz)} von {len(vlose)}** (Schwelle 0): {', '.join(kz) or '–'}.",
            f"- Lose mit „nicht tagesgenau“ (aus Zähler und Nenner genommen): {', '.join(n for n in schl if v[n]['ntg']) or '–'}."]
    if mensch:
        mn = [n for n in schl if schl[n]["mensch"] == "ja"]
        mok = {n: (kat_wert(mensch[n]["ende_gl"]) if n in mensch else ("fehlt", None)) for n in mn}
        treffer = {n: gleich(mok[n], v[n]["gl"]) for n in mn}
        out += [f"- **V6 (Kommilitone = Vergleichswert, {len(mn)} Lose): {sum(treffer.values())}/{len(mn)}** (Schwelle ≥ 13/15). Abweichend: "
                f"{', '.join(f'{n} (Mensch {mensch[n]['ende_gl']}, Vergleichswert {v[n]['gl'][1] or v[n]['gl'][0]})' for n in mn if not treffer[n]) or '–'}."]
    else:
        out += ["- V6: Eintrag des Kommilitonen liegt noch nicht vor."]
    if evaluator:
        evn = [n for n in ev_lose if n in evaluator]
        eok = sum(gleich(ende_gl(evaluator[n]), v[n]["gl"]) for n in evn)
        out += [f"- Kontrolle durch den Evaluator (beschreibend): Ende der Grundlaufzeit stimmt mit dem Vergleichswert bei {eok}/{len(evn)} Losen."]
    s_ok = [n for n in gruppen["S"] if v[n]["gl"][1]]
    out += ["", "### Beschreibend (ohne Schwelle)", "",
            f"- Regel-6-Lose (S, {len(gruppen['S'])}): Der Vergleichswert ist bestimmbar bei {len(s_ok)}; die Liste nennt bei allen kein Ende (Abdeckungsverlust: {len(s_ok)}/{len(gruppen['S'])}).",
            f"- Von mindestens einem Leser als „keine Gebäudereinigung“ eingestuft: {', '.join(n for n in schl if v[n]['rein']) or '–'}.",
            f"- Zuordnung des Loses von mindestens einem Leser als unsicher gemeldet: {', '.join(n for n in schl if v[n]['unsicher']) or '–'}.",
            f"- Herkunft des Endes in der Liste (V-Lose): {dict(Counter(schl[n]['gl_herkunft'] for n in vlose))}.", "",
            "### Abweichungen der Liste vom Vergleichswert (V-Lose)", "",
            "| N | Gruppe | Herkunft | Liste GL | Vergleichswert GL | Leser A | Leser B | Liste Höchstende | Vergleichswert Höchstende |", "|---|---|---|---|---|---|---|---|---|"]
    # Nachtrag (nach der Auswertung ergänzt, nicht vorab festgelegt): einfache Basisregel „Ende der Grundlaufzeit = Feld EndDate des Loses“ (Wert aus der Lesung von Leser A),
    # gemessen am selben Vergleichswert, um den Nutzen der Regeln einzuordnen.
    basis = {n: (lambda d: ("datum", d) if d else ("unbekannt", None))(datum(antworten["a"][n]["feld_enddatum"])) for n in schl}
    ok_basis = {n: ok_gl(basis[n], v[n]["gl"]) for n in schl}
    only_regeln = [n for n in z if ok_neu[n] and not ok_basis[n]]
    only_basis = [n for n in z if ok_basis[n] and not ok_neu[n]]
    nachtrag = ["", "### Nachtrag: Basisregel „Ende = Feld EndDate“ (nach der Auswertung ergänzt, nicht vorab festgelegt)", "",
            f"- Z-Lose: Basisregel {pct(sum(ok_basis[n] for n in z), len(z))}; neue Fassung {pct(k1, len(z))}; alte Fassung {pct(sum(ok_alt[n] for n in z), len(z))}.",
            f"- R- und M-Lose: Basisregel {pct(sum(ok_basis[n] for n in rm), len(rm))}; neue Fassung {pct(k2, len(rm))}; alte Fassung {pct(sum(ok_alt[n] for n in rm), len(rm))}.",
            f"- Z-Lose, bei denen nur die neue Fassung trifft, nicht die Basisregel: {', '.join(only_regeln) or '–'}; nur die Basisregel trifft: {', '.join(only_basis) or '–'}.",
            "- Lesehinweis: Der Feldwert stammt aus der Lesung von Leser A und ist auch Teil des Vergleichswerts (Schritt 4 der Definition); die Basisregel ist damit nahe am Vergleichswert. Sie zeigt, wie viel die Textregeln über das Feld hinaus leisten."]
    wert = lambda t: str(t[1]) if t[1] else t[0]  # noqa: E731
    for n in vlose:
        if not v[n]["ntg"] and (not ok_neu[n] or not h_ok[n]):
            s = schl[n]
            out.append(f"| {n} | {s['gruppe']} | {s['gl_herkunft']} | {s['gl_ende'] or '–'}{'' if ok_neu[n] else ' ✗'} | {wert(v[n]['gl'])} | {wert(v[n]['ga'])} | {wert(v[n]['gb'])} | "
                       f"{s['hoechstende'] or s['hoechstende_herkunft']}{'' if h_ok[n] else ' ✗'} | {wert(v[n]['h'])} |")
    out += nachtrag
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"V1 {k1}/{len(z)}, V2 {k2}/{len(rm)}, V5 {einig}/{len(schl)}, V7 {len(kz)}")


if __name__ == "__main__":
    main()
