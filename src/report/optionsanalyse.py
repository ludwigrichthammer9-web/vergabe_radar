"""Paket F (Nachtrag zu Iteration 10): Optionsanalyse an den 52 Paaren des Backtests der Iteration 5.

Frage: Kam die Neuausschreibung (a) vor dem Ende der Grundlaufzeit, (b) zwischen Ende der Grundlaufzeit und
Höchstende, (c) nach dem Höchstende? Getrennt nach "Höchstende bekannt/unbekannt" und "mit/ohne Option".
Dazu der Vorlauf (Veröffentlichung der Neuausschreibung relativ zum Vertragsende).

Eingaben (nur lesen):
  data/processed/backtest_paare_iteration5.csv   Spalten: pid, gl_ende, hoechstende, hoechstende_herkunft, testfall_datum, ...
  data/processed/x1_paare_iteration5.txt         Paar-Kennungen der 52 bestätigten Paare (dieselbe Auswahl wie src/model/baseline.py)
Ausgabe: reports/optionsanalyse.md

Aufruf:  .venv\\Scripts\\python.exe -I src/report/optionsanalyse.py

Definitionen (vorab im Code, keine Schätzung aus den Paaren):
  Monate = Tage / 30,4375 (wie src/model/baseline.py). pub = Veröffentlichung der Neuausschreibung (testfall_datum).
  d = pub - Ende der Grundlaufzeit (Monate). a: pub < GL-Ende; b: GL-Ende <= pub <= Höchstende; c: pub > Höchstende.
  Ist das Höchstende unbekannt, sind b und c nicht trennbar ("ab GL-Ende").
"""

import csv
import math
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PAARE = ROOT / "data" / "processed" / "backtest_paare_iteration5.csv"
X1 = ROOT / "data" / "processed" / "x1_paare_iteration5.txt"
OUT = ROOT / "reports" / "optionsanalyse.md"
MON = 30.4375

GRUPPEN = [
    ("G1 Höchstende bekannt, Option belegt (Höchstende > GL-Ende)", "bekannt, Option belegt"),
    ("G2 Höchstende = GL-Ende, ausdrücklich „keine Verlängerung“", "bekannt, ohne Option"),
    ("G3 Höchstende = GL-Ende, Herkunft „keine_angabe“ oder „enddatum_ist_hoechstende“ (Option unklar)", "bekannt, Option unklar"),
    ("G4 Höchstende unbestimmbar", "unbekannt"),
]


def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 0.0
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, c - h), min(1.0, c + h)


def pct(k, n):
    if not n:
        return "–"
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {100*k/n:.1f} % ({100*lo:.1f}–{100*hi:.1f})".replace(".", ",")


def fz(x, nd=1):
    return f"{x:.{nd}f}".replace(".", ",")


def median(xs):
    xs = sorted(xs)
    n = len(xs)
    if not n:
        return None
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def lade():
    x1 = set(X1.read_text(encoding="utf-8").split())
    rows = []
    with PAARE.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            if r["pid"] not in x1:
                continue
            gl = date.fromisoformat(r["gl_ende"])
            h = date.fromisoformat(r["hoechstende"]) if r["hoechstende"] else None
            pub = date.fromisoformat(r["testfall_datum"])
            if h is None:
                g = 3
            elif h > gl:
                g = 0
            elif r["hoechstende_herkunft"] == "keine_verlaengerung":
                g = 1
            else:
                g = 2
            d = (pub - gl).days / MON
            lage = "a" if pub < gl else ("b" if h is None or pub <= h else "c")
            if h is None and pub >= gl:
                lage = "bc"
            rows.append({**r, "gl": gl, "h": h, "pub": pub, "g": g, "d": d,
                         "dh": (pub - h).days / MON if h else None,
                         "v_gl": (gl - pub).days / MON, "v_h": (h - pub).days / MON if h else None, "lage": lage})
    return rows


BINS = [(-1e9, -24, "< −24"), (-24, -12, "−24 bis −12"), (-12, -6, "−12 bis −6"), (-6, 0, "−6 bis 0"),
        (0, 6, "0 bis 6"), (6, 12, "6 bis 12"), (12, 24, "12 bis 24"), (24, 48, "24 bis 48"), (48, 1e9, "≥ 48")]


def histo_tabelle(rows, key, bins=BINS):
    kopf = "| Gruppe | n | " + " | ".join(b[2] for b in bins) + " |"
    out = [kopf, "|---|---|" + "---|" * len(bins)]
    mengen = [("alle 52 Paare", rows)] + [(GRUPPEN[i][1], [r for r in rows if r["g"] == i]) for i in range(4)]
    mengen += [("Höchstende bekannt (G1–G3)", [r for r in rows if r["g"] < 3]),
               ("mit belegter Option (G1)", [r for r in rows if r["g"] == 0]),
               ("ohne belegte Option (G2+G3+G4)", [r for r in rows if r["g"] != 0])]
    for name, rs in mengen:
        cnt = [sum(1 for r in rs if r[key] is not None and lo <= r[key] < hi) for lo, hi, _ in bins]
        out.append(f"| {name} | {len(rs)} | " + " | ".join(map(str, cnt)) + " |")
    return out


def textbalken(rows, key, bins=BINS):
    out = ["```"]
    for lo, hi, name in bins:
        k = sum(1 for r in rows if r[key] is not None and lo <= r[key] < hi)
        out.append(f"{name:>12} | {'#' * k} {k}")
    out.append("```")
    return out


def lage_tabelle(rows):
    out = ["| Gruppe | n | (a) vor GL-Ende | (b) GL-Ende bis Höchstende | (c) nach Höchstende | ab GL-Ende (b und c nicht trennbar) |",
           "|---|---|---|---|---|---|"]
    mengen = [("alle 52 Paare", rows)] + [(GRUPPEN[i][1], [r for r in rows if r["g"] == i]) for i in range(4)]
    mengen += [("Höchstende bekannt (G1–G3)", [r for r in rows if r["g"] < 3])]
    for name, rs in mengen:
        n = len(rs)
        c = Counter(r["lage"] for r in rs)
        zell = [pct(c[x], n) if (x != "bc" or c[x] or name.startswith(("unbekannt", "alle"))) else "–" for x in ("a", "b", "c", "bc")]
        if name.startswith(("bekannt", "Höchstende bekannt")):
            zell[3] = "–"
        out.append(f"| {name} | {n} | " + " | ".join(zell) + " |")
    return out


def main():
    rows = lade()
    n = len(rows)
    g = [[r for r in rows if r["g"] == i] for i in range(4)]
    g1 = g[0]
    c_all = Counter(r["lage"] for r in rows)
    k_a_all = c_all["a"]
    hb = [r for r in rows if r["g"] < 3]
    ca = Counter(r["lage"] for r in g1)
    n_xml = sum(1 for r in rows if r["format"] == "xml")
    n_obj = sum(1 for r in rows if r["gt"].startswith("objektgleich"))

    L = []
    A = L.append
    A("# Optionsanalyse (Paket F, Nachtrag zu Iteration 10)")
    A("")
    A("_Erzeugt mit `src/report/optionsanalyse.py` (liest nur, ändert keine Daten). Eingaben: `data/processed/backtest_paare_iteration5.csv`, "
      "`data/processed/x1_paare_iteration5.txt` (die 52 Paare, dieselbe Auswahl wie `src/model/baseline.py`), `reports/backtest_iteration5.md`, "
      "`reports/backtest_analysen_iteration5.md`. Nachträgliche, explorative Auswertung; keine Schwelle, keine Änderung an den Iterationen 1 bis 10._")
    A("")
    A("**Ausdrücklich: 52 Paare, Hinweis, kein Beleg für die Aussage der Vergabestelle (gestützt auf ein einziges Gespräch, n = 1).**")
    A("")
    A("## 1. Frage und Aussage der Vergabestelle")
    A("")
    A("- Fakt (Gespräch, `docs/business.md` §8.9, n = 1): „Fast immer [verlängern wir], wenn eine Verlängerungsoption im Vertrag steht.“ Meist 2 Jahre fest plus 1 Jahr Option. "
      "Planung etwa 9 Monate vor Vertragsende, Veröffentlichung „meist 3 bis 4 Monate vor Start“.")
    A("- Fakt (Iteration 5, `reports/backtest_iteration5.md`): Die Veröffentlichung der Neuausschreibung streut zweigipflig um „Höchstende − 6 Monate“: "
      "20 Paare früher als −3 Monate, 17 später als +3, 15 im Fenster.")
    A("- Frage hier: Wo liegt die Veröffentlichung relativ zum Ende der Grundlaufzeit (GL) und zum Höchstende, und passt das zu „fast immer verlängert“?")
    A("")
    A("## 2. Daten und Definitionen")
    A("")
    A(f"- Fakt: {n} Paare (Vorgänger-Zuschlag → Neuausschreibung); je Paar sind bekannt: Ende der Grundlaufzeit (`gl_ende`), Höchstende (`hoechstende`, mit Herkunft), "
      "Veröffentlichungsdatum der Neuausschreibung (`testfall_datum`). Das Zuschlagsdatum des Vorgängers und der Beginn der Neuausschreibung stehen in dieser Datei nicht "
      "(die Spalte `beginn` ist der Beginn des Vorgängers). Es wird nur verwendet, was dort steht.")
    A("- Monate = Tage / 30,4375 (wie in `src/model/baseline.py`). d = Veröffentlichung − GL-Ende (positiv: nach dem GL-Ende).")
    A("- (a) Veröffentlichung < GL-Ende. (b) GL-Ende ≤ Veröffentlichung ≤ Höchstende. (c) Veröffentlichung > Höchstende. Ist das Höchstende unbestimmbar, lassen sich (b) und (c) nicht trennen.")
    A("- Gruppen nach Datenlage im Vorgänger (nicht nach tatsächlichem Vertragsverlauf):")
    for i, (lang, _) in enumerate(GRUPPEN):
        A(f"  - {lang}: n = {len(g[i])}.")
    A("- Wilson-Intervalle: 95 %, in Klammern in Prozent. Nenner steht immer dabei.")
    A("")
    A("## 3. Fakten: Lage der Neuausschreibung")
    A("")
    A("Anteile mit Nenner und Wilson-Intervall (95 %); Rechenweg: Zahl der Paare in der Lage / Zahl der Paare der Gruppe.")
    A("")
    L += lage_tabelle(rows)
    A("")
    A(f"- Fakt: Über alle {n} Paare lag die Veröffentlichung in {pct(k_a_all, n)} der Fälle vor dem GL-Ende (a) und in {pct(n - k_a_all, n)} ab dem GL-Ende.")
    A(f"- Fakt (G1, Option belegt, n = {len(g1)}): (a) {pct(ca['a'], len(g1))}; (b) {pct(ca['b'], len(g1))}; (c) {pct(ca['c'], len(g1))}.")
    A(f"- Fakt: Bei den {len(hb)} Paaren mit bekanntem Höchstende lag die Veröffentlichung in {pct(sum(1 for r in hb if r['pub'] < r['h']), len(hb))} vor dem Höchstende "
      f"(bei G2 und G3 ist Höchstende = GL-Ende, dort fällt das mit (a) zusammen).")
    A("")
    A("### Sensitivität: Wie viel Vorlauf wäre bei voll gezogener Option normal?")
    A("")
    A("Eine Veröffentlichung vor dem Höchstende ist noch kein Hinweis auf eine nicht gezogene Option, denn auch bei voll genutzter Option wird vorher ausgeschrieben "
      "(Vergabestelle: Planung etwa 9 Monate, Veröffentlichung 3 bis 4 Monate vor Start). Anteil der G1-Paare, die **mehr als V Monate vor dem Höchstende** veröffentlicht wurden "
      "(dann spricht mehr für „Option nicht voll genutzt“; V ist hier eine Setzung zur Sensitivität, nicht aus den Paaren geschätzt):")
    A("")
    A("| V (Monate vor Höchstende) | G1: Veröffentlichung früher als Höchstende − V |")
    A("|---|---|")
    for v in (0, 3, 6, 9, 12, 18):
        k = sum(1 for r in g1 if r["v_h"] > v)
        A(f"| {v} | {pct(k, len(g1))} |")
    A("")
    A("## 4. Fakten: Verteilung von d = Veröffentlichung − GL-Ende (Monate)")
    A("")
    A("Zahl der Paare je Klasse (Klasse unten ≤ d < oben):")
    A("")
    L += histo_tabelle(rows, "d")
    A("")
    A("Textbalken, alle 52 Paare (je # ein Paar):")
    A("")
    L += textbalken(rows, "d")
    A("")
    A("Textbalken, G1 (Option belegt):")
    A("")
    L += textbalken(g1, "d")
    A("")
    A("Textbalken, G2+G3+G4 (keine belegte Option):")
    A("")
    L += textbalken([r for r in rows if r["g"] != 0], "d")
    A("")
    med = lambda rs, k: median([r[k] for r in rs if r[k] is not None])
    A(f"- Fakt: Median d: alle {n} Paare {fz(med(rows, 'd'))} Monate; G1 {fz(med(g1, 'd'))}; G2 {fz(med(g[1], 'd'))}; G3 {fz(med(g[2], 'd'))}; G4 {fz(med(g[3], 'd'))}.")
    A(f"- Fakt: In G1 liegt d zwischen {fz(min(r['d'] for r in g1))} und {fz(max(r['d'] for r in g1))} Monaten; "
      f"in G4 (Höchstende unbestimmbar) zwischen {fz(min(r['d'] for r in g[3]))} und {fz(max(r['d'] for r in g[3]))}.")
    A("")
    A("Zum Vergleich: Abstand Veröffentlichung − **Höchstende** (dh, nur G1 bis G3, in Monaten):")
    A("")
    L += histo_tabelle([r for r in rows if r["dh"] is not None], "dh", [
        (-1e9, -24, "< −24"), (-24, -12, "−24 bis −12"), (-12, -6, "−12 bis −6"), (-6, -3, "−6 bis −3"), (-3, 0, "−3 bis 0"),
        (0, 12, "0 bis 12"), (12, 1e9, "≥ 12")])
    A("")
    A("(Die Zeilen G4 und „ohne belegte Option“ enthalten hier nur Paare mit bekanntem Höchstende; G4 ist leer.)")
    A("")
    A("## 5. Fakten: Vorlauf")
    A("")
    A("Vorlauf = Vertragsende − Veröffentlichung der Neuausschreibung (Monate; positiv: vor dem Ende veröffentlicht; negativ: nach dem Ende). "
      "Vertragsende = Höchstende, wenn bekannt, sonst GL-Ende. Der Beginn des Folgevertrags steht nicht in den Daten; „3 bis 4 Monate vor Start“ lässt sich deshalb nur "
      "näherungsweise (Start ≈ Vertragsende des Vorgängers) prüfen.")
    A("")
    vb = [(-1e9, 0, "< 0 (nach Ende)"), (0, 3, "0 bis 3"), (3, 6, "3 bis 6"), (6, 9, "6 bis 9"), (9, 12, "9 bis 12"), (12, 24, "12 bis 24"), (24, 1e9, "≥ 24")]
    for r in rows:
        r["v_end"] = r["v_h"] if r["h"] else r["v_gl"]
    mengen = [("alle 52 Paare (Vertragsende = Höchstende, sonst GL-Ende)", rows),
              ("G1 Option belegt, bezogen auf Höchstende", g1),
              ("G2 ohne Option", g[1]), ("G3 Option unklar", g[2]), ("G4 Höchstende unbekannt (GL-Ende)", g[3])]
    A("| Menge | n | " + " | ".join(b[2] for b in vb) + " | Median |")
    A("|---|---|" + "---|" * (len(vb) + 1))
    for name, rs in mengen:
        cnt = [sum(1 for r in rs if lo <= r["v_end"] < hi) for lo, hi, _ in vb]
        A(f"| {name} | {len(rs)} | " + " | ".join(map(str, cnt)) + f" | {fz(median([r['v_end'] for r in rs]))} |")
    A("")
    k34 = sum(1 for r in rows if 2.5 <= r["v_end"] <= 4.5)
    k_9 = sum(1 for r in rows if 0 <= r["v_end"] <= 12)
    k_neg = sum(1 for r in rows if r["v_end"] < 0)
    k_g1_012 = sum(1 for r in g1 if 0 <= r["v_h"] <= 12)
    A(f"- Fakt: Vorlauf zwischen 2,5 und 4,5 Monaten („3 bis 4 Monate“ der Vergabestelle, grob): {pct(k34, n)}. Vorlauf 0 bis 12 Monate: {pct(k_9, n)}. "
      f"Veröffentlichung erst nach dem Vertragsende (Vorlauf < 0): {pct(k_neg, n)}.")
    A(f"- Fakt (G1): Vorlauf zum Höchstende 0 bis 12 Monate bei {pct(k_g1_012, len(g1))}; Median {fz(median([r['v_h'] for r in g1]))} Monate.")
    A(f"- Fakt: Median des Vorlaufs zum Vertragsende (alle Paare) {fz(median([r['v_end'] for r in rows]))} Monate; "
      f"zum GL-Ende (alle Paare) {fz(median([r['v_gl'] for r in rows]))} Monate.")
    A("")
    A("## 6. Deutung (getrennt von den Fakten)")
    A("")
    n_early = ca["a"]
    A(f"1. **Zweigipfligkeit.** Ein Teil der Neuausschreibungen kommt vor dem GL-Ende, ein anderer deutlich danach (siehe Textbalken). Das passt zu zwei Fällen: "
      "Verträge ohne gezogene Option (kurzer Vorlauf vor dem GL-Ende) und Verträge mit gezogener Option (Veröffentlichung nach dem GL-Ende). "
      "Die Daten trennen diese Fälle nicht, weil die tatsächliche Ausübung der Option in keiner Bekanntmachung der Paare steht.")
    k6 = sum(1 for r in g1 if r["v_h"] > 6)
    A(f"2. **Option belegt (G1, n = {len(g1)}).** {ca['b']} von {len(g1)} Veröffentlichungen liegen zwischen GL-Ende und Höchstende, nur {ca['a']} vor dem GL-Ende und {ca['c']} nach dem Höchstende. "
      "Das ist mit „Option wird in der Regel gezogen, ausgeschrieben wird gegen Ende der Optionszeit“ vereinbar. Es ist aber auch mit anderen Vorgängen vereinbar "
      "(Übergangsverlängerung, vorzeitige Ausschreibung vor Ablauf der Option, eine Option, die nur teilweise genutzt wurde). Wie viel davon „Option gezogen“ ist, "
      "lässt sich aus den Daten nicht sagen.")
    A("3. **Vorlauf.** Der Vorlauf streut breit; der Wert „3 bis 4 Monate vor Start“ ist nur ein Teil der Fälle (siehe oben). Die Angabe „Planung 9 Monate vorher“ "
      "betrifft interne Arbeit und ist an einer Veröffentlichung nicht ablesbar. Ein Vorlauf von mehreren Monaten ist mit einer voll genutzten Option verträglich; "
      "wo die Veröffentlichung 12 Monate und mehr vor dem Höchstende liegt (Sensitivitätstabelle), spricht mehr für eine nicht voll genutzte Option oder eine Zuordnung, "
      "die nicht das gleiche Los trifft.")
    k6 = sum(1 for r in g1 if r["v_h"] > 6)
    A("4. **Zeitpunkt relativ zum Höchstende (G1).** Läge bei jedem Vertrag mit Option die Option voll bis zum Höchstende, wäre bei „Veröffentlichung 3 bis 4 Monate vor Start“ "
      f"ein Vorlauf zum Höchstende von etwa 3 bis 6 Monaten zu erwarten. Tatsächlich liegen {pct(k6, len(g1))} der G1-Veröffentlichungen mehr als 6 Monate vor dem Höchstende. "
      "Das ist ein Hinweis, dass bei den später doch neu ausgeschriebenen Verträgen mit Option die Option oft nicht bis zum Ende lief (oder nur teilweise gezogen wurde, "
      "z. B. 2 Jahre fest plus 1 Jahr Option, davon nur ein Teil); es ist kein Beleg, weil Höchstende und GL-Ende vor eForms teils aus Freitext stammen und die Auswahl nur Neuausschreibungen enthält.")
    A("5. **Lange Lücken nach dem Ende** (G2 und G4 mit d über 24 Monaten): Die Analysen der Iteration 5 (`reports/backtest_analysen_iteration5.md`, 12 Paare mit Lücke über 24 Monaten) "
      "belegen keinen Zwischenvertrag; es sind mehrere Erklärungen möglich (nicht in der Bekanntmachung stehende Verlängerung, Zwischenvertrag, falsche Zuordnung). "
      "Bei G4 fehlt das Höchstende, ein spätes d ist dort deshalb nicht auswertbar.")
    A("")
    A("## 7. Grenzen")
    A("")
    A(f"- **Nur Neuausschreibungen sind erfasst.** Die Paare entstanden durch Rückwärtssuche vom Testfall (Neuausschreibung 2026) zum auffindbaren Vorgänger. Verträge, die verlängert wurden "
      "und (noch) nicht neu ausgeschrieben sind, fehlen vollständig. Für „fast immer verlängert, wenn Option vorhanden“ wäre der Nenner alle Verträge mit Option am Ende der Grundlaufzeit; "
      "der steht in den Daten nicht (Überlebens- bzw. Auswahlverzerrung).")
    A(f"- **Kleine Zahlen.** {n} Paare, davon nur {len(g1)} mit belegter Option; die Wilson-Intervalle sind breit (oft über 30 Prozentpunkte).")
    A(f"- **Zeitfenster der Testfälle:** Neuausschreibungen aus Q1 und Q3 2026 (Iteration 4 und 3); Verträge, deren Option bis nach 2026 läuft, können nur vorzeitig ausgeschrieben worden sein "
      "(Rechtszensierung zugunsten von (a)/(b)).")
    A(f"- **Datenherkunft der Enden:** {n_xml} von {n} Vorgängern liegen vor eForms (XML), {n - n_xml} im eForms-Format; (in der Rohdatei mit 68 Vorgängern sind es 55 vor eForms, 13 eForms). "
      "Das Höchstende ist vor eForms nur teilweise und aus Freitext bestimmbar (Herkunft `datum_text`, `anzahl_x_laenge`, `hoechstlaufzeit_text`); "
      "bei `enddatum_ist_hoechstende` (n = 4) ist das GL-Ende selbst unsicher.")
    A(f"- **Zuordnung und Prüfung:** {n_obj} Paare „objektgleich“, {n - n_obj} „Teilmenge“ laut Handsuche; die Ground Truth ist nicht unabhängig bestätigt (A18); "
      "die Zweitprüfung war KI-gestützt (`docs/ki_irrwege.md`, `reports/gt_pruefung_iteration5_auswertung.md`).")
    A("- **Veröffentlichungsdatum ist nicht Vergabestart.** Der Beginn der Neuausschreibung steht nicht in den Daten; „Vorlauf zum Vertragsende“ ist eine Näherung für „Vorlauf zum Start“.")
    A("- **Eine Quelle für die Aussage** (n = 1, eine Vergabestelle). Gespräche sind Hinweise, keine Stichprobe.")
    A("- **Auftraggeber-Cluster:** 52 Paare, 40 Auftraggeber, 6 mit mehr als einem Paar (`reports/backtest_analysen_iteration5.md`); die Paare sind nicht unabhängig.")
    A("- **Nicht auswertbar:** Wie oft eine Option tatsächlich gezogen wurde; Verlängerung ohne Neuausschreibung; Dauer der Verlängerung.")
    A("")
    A("## 8. Urteil zur Aussage „fast immer verlängert“")
    A("")
    A("**Die Daten können die Aussage „fast immer verlängert“ nicht prüfen** (kein Beleg dafür und keiner dagegen). Begründung: "
      "Die 52 Paare sind per Konstruktion Verträge, die neu ausgeschrieben wurden; eine Quote „verlängert / nicht verlängert“ braucht auch die Verträge, die verlängert und (noch) nicht neu ausgeschrieben wurden. "
      f"Als schwache Nebenbeobachtung: Bei den {len(g1)} Paaren mit belegter Option wurde {pct(ca['b'] + ca['c'], len(g1))} ab dem GL-Ende veröffentlicht (mit Verlängerung vereinbar), "
      f"aber {pct(k6, len(g1))} mehr als 6 Monate vor dem Höchstende (spricht eher gegen „Option wird bis zum Höchstende ausgeschöpft“, ohne die Aussage zu widerlegen, "
      "denn eine Verlängerung um nur einen Teil der Option bleibt möglich). Belastbar prüfen ließe sich die Aussage nur mit einer Vorwärtsbetrachtung "
      "(alle Verträge mit Option, deren Grundlaufzeit endete, und was danach geschah) und mehr als einer Vergabestelle.")
    A("")
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("geschrieben:", OUT, "Paare:", n)


if __name__ == "__main__":
    main()
