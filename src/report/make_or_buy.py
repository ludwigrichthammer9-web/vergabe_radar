"""Make-or-Buy-Modell: Aufträge selbst filtern (Eigenbau) gegen Abo kaufen.

Aufruf (aus dem Repo-Wurzelordner):
    .venv\\Scripts\\python.exe -I src\\report\\make_or_buy.py

Reine Standardbibliothek. Schreibt reports/make_or_buy.md und reports/make_or_buy.csv.
Alle Eingaben stehen als Konstanten am Anfang; jede trägt eine Quelle oder das Etikett "Annahme".
Das Modell rechnet Kosten, keine Umsätze des Projekts und keine Nachfrage.
Zwei Varianten: Basismodell (Abo und kostenlose Dienste ohne Eigenaufwand) und symmetrische Variante (auch dort fallen Nutzungsstunden an).
Beide sind Modellkonstruktionen mit Annahmen; "Eigenbau nie günstiger gegen kostenlos" folgt im Basismodell aus der Konstruktion, keine Messung.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REPORT_MD = ROOT / "reports" / "make_or_buy.md"
REPORT_CSV = ROOT / "reports" / "make_or_buy.csv"

# ---------------------------------------------------------------- Annahmen (Eigenbau)
# Stundensatz, extern. Annahme. Spanne 60-110 EUR/h; Quelle: freelancermap Freelancer-Kompass 2025, Durchschnitt etwa
# 104 EUR/h, sekundär über Websuche gelesen, nicht im Original geprüft.
STUNDENSATZ = 100.0
STUNDENSATZ_SPANNE = (60.0, 100.0, 110.0)
# Aufwand je Szenario in Stunden. Annahme (keine Messung).
SZENARIEN = {
    "Niedrig": {"einmal_h": 20, "laufend_h": 5,
                "beschreibung": "fertige JSON/CSV-Quelle in Excel laden"},
    "Mittel": {"einmal_h": 60, "laufend_h": 20,
               "beschreibung": "eigener Filter plus Import ins Verwaltungssystem"},
    "Hoch": {"einmal_h": 120, "laufend_h": 50,
             "beschreibung": "TED-API plus eigene Leseregeln plus Fehlerbehandlung"},
}
# ---------------------------------------------------------------- Symmetrische Variante (Annahmen, keine Messung)
# Auch bei Abo und kostenlosen Diensten fallen Nutzungsstunden an: Alerts lesen, Treffer ins eigene System übertragen.
NUTZUNG_H = {"Niedrig": 10, "Mittel": 30, "Hoch": 60}   # Stunden je Jahr, je Szenario (Annahme)
# Kostenlosen Dienst nutzen und selbst importieren: derselbe Importaufwand wie im Eigenbau-Niedrig-Szenario (Annahme);
# die Nutzung (Alerts lesen, Treffer übernehmen) ist in den 10 h je Jahr enthalten und wird nicht noch einmal addiert.
IMPORT_EINMAL_H = 20
IMPORT_LAUFEND_H = 10
# Der Eigenbau bleibt wie im Basismodell: Seine laufenden Stunden (5 / 20 / 50 h) enthalten Pflege und Nutzung.
NAME_HAND = "Kostenloser Dienst (Vergabeweiser, AusschreibungsRadar Free), Treffer von Hand übernehmen"
NAME_IMPORT = "Kostenloser Dienst, Treffer selbst importieren"

# Wert eines Auftrags
JAHRESUMSATZ_MEDIAN = 167_404.0   # Fakt: reports/auftragswerte_909.md, Median Jahreswert, n = 957, TED 2024-2025
JAHRESUMSATZ_QUARTILE = (80_367.0, 422_744.0)  # ebd.
MARGE = 0.05                      # Annahme (Sensitivität unten)
MARGEN = (0.03, 0.05, 0.08)       # Annahme
LAUFZEIT_JAHRE = 3                # Fakt (Gespräch mit der Vergabestelle, n = 1): meist 2 Jahre fest plus 1 Jahr Option
HORIZONT_JAHRE = 3                # Annahme: Kosten der ersten drei Jahre

# ---------------------------------------------------------------- Kaufen (Preise je Jahr, netto, Quellen in business.md §6, §8)
# (Name, Preis je Jahr in EUR, Quelle/Hinweis)
ABOS = [
    ("DTAD", 1_500.0, "Gespräch 2026-11-05 (Betrieb mittlerer Größe): 'knapp 1.500 €' im Jahr; n = 1"),
    ("subreport (unterer Preis)", 84 * 12.0, "84 €/Monat, Wettbewerber-Vergleich (jorpex.com), nicht beim Anbieter geprüft; zzgl. USt."),
    ("subreport (oberer Preis)", 198 * 12.0, "198 €/Monat, ebd."),
    ("AusschreibungsRadar Starter", 290.0, "29 €/Monat laut Preisseite (gelesen 2026-11-05); 290 €/Jahr wie vom Auftrag vorgegeben, "
                                          "12 x 29 = 348 € wäre der Monatspreis; Rechnung gilt für beide Werte"),
    ("AusschreibungsRadar Business", 79 * 12.0, "79 €/Monat laut Preisseite; hier 12 x Monatspreis"),
    ("AusschreibungsRadar Professional", 1_490.0, "149 €/Monat laut Preisseite, mit CSV-Export; 1.490 €/Jahr wie vom Auftrag vorgegeben "
                                                  "(12 x 149 = 1.788 €)"),
    ("Vergabeweiser", 0.0, "kostenlos (API/MCP, Limits siehe business.md §9)"),
]


def eur(x: float, nachkomma: int = 0) -> str:
    s = f"{x:,.{nachkomma}f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return s + " €"


def zahl(x: float, nachkomma: int = 2) -> str:
    return f"{x:.{nachkomma}f}".replace(".", ",")


def kosten(sz: dict, satz: float = STUNDENSATZ) -> dict:
    einmal = sz["einmal_h"] * satz
    laufend = sz["laufend_h"] * satz
    summe = einmal + laufend * HORIZONT_JAHRE
    return {"einmal": einmal, "laufend": laufend, "summe": summe}


def break_even(einmal: float, laufend: float, abo: float):
    """Jahre bis Eigenbau (einmal + laufend*t) billiger ist als Abo (abo*t). None = nie."""
    if laufend >= abo:
        return None
    return einmal / (abo - laufend)


def break_even_allg(e_einmal: float, e_lauf: float, x_einmal: float, x_lauf: float):
    """Jahre, bis der Eigenbau (E) billiger ist als die Alternative (X): e_einmal + e_lauf*t < x_einmal + x_lauf*t.
    0.0 = von Beginn an nicht teurer (e_einmal <= x_einmal und e_lauf <= x_lauf); None = nie."""
    if e_einmal <= x_einmal and e_lauf <= x_lauf:
        return 0.0
    if x_lauf <= e_lauf:
        return None
    return (e_einmal - x_einmal) / (x_lauf - e_lauf)


def alternativen(szenario: str) -> list:
    """Alternativen zum Eigenbau in der symmetrischen Variante: (Name, einmalig, laufend je Jahr) in EUR."""
    nutz = NUTZUNG_H[szenario] * STUNDENSATZ
    alt = [(name, 0.0, preis + nutz) for name, preis, _ in ABOS if name != "Vergabeweiser"]
    alt.append((NAME_HAND, 0.0, nutz))
    alt.append((NAME_IMPORT, IMPORT_EINMAL_H * STUNDENSATZ, IMPORT_LAUFEND_H * STUNDENSATZ))
    return alt


def be_zelle(t) -> str:
    if t is None:
        return "nie"
    if t == 0.0:
        return "von Beginn an"
    return zahl(t, 1) + (" (> 3)" if t > HORIZONT_JAHRE else "")


def be_text(t) -> str:
    if t is None:
        return "nie"
    s = zahl(t, 1) + " Jahre"
    if t > HORIZONT_JAHRE:
        s += " (jenseits von 3 Jahren)"
    return s


def deckungsbeitrag(umsatz: float = JAHRESUMSATZ_MEDIAN, marge: float = MARGE) -> float:
    return umsatz * marge * LAUFZEIT_JAHRE


def main() -> None:
    k = {n: kosten(sz) for n, sz in SZENARIEN.items()}
    db = deckungsbeitrag()

    # ---- Kontrollwerte (aus dem Auftrag)
    kontrolle = {
        ("Niedrig", "einmal"): 2000, ("Niedrig", "laufend"): 500, ("Niedrig", "summe"): 3500,
        ("Mittel", "einmal"): 6000, ("Mittel", "laufend"): 2000, ("Mittel", "summe"): 12000,
        ("Hoch", "einmal"): 12000, ("Hoch", "laufend"): 5000, ("Hoch", "summe"): 27000,
    }
    ok = all(abs(k[s][f] - v) < 0.5 for (s, f), v in kontrolle.items())
    be_dtad = {n: break_even(k[n]["einmal"], k[n]["laufend"], 1500.0) for n in k}
    ok &= abs(be_dtad["Niedrig"] - 2.0) < 1e-9 and be_dtad["Mittel"] is None and be_dtad["Hoch"] is None
    ok &= break_even(k["Niedrig"]["einmal"], k["Niedrig"]["laufend"], 290.0) is None
    zusatz = {n: k[n]["summe"] / db for n in k}
    ok &= [round(zusatz[n], 2) for n in ("Niedrig", "Mittel", "Hoch")] == [0.14, 0.48, 1.08]
    ok &= round(db) == 25111  # Auftrag nennt 25.110 (abgerundet); exakt 25.110,6
    # symmetrische Variante, Handrechnung: z. B. DTAD Niedrig 2.000 + 500 t = (1.500 + 1.000) t, also t = 1,0
    sym = {n: {a[0]: break_even_allg(k[n]["einmal"], k[n]["laufend"], a[1], a[2]) for a in alternativen(n)} for n in k}
    ok &= [round(sym[n]["DTAD"], 6) for n in k] == [1.0, 2.4, 4.8]
    ok &= [round(sym[n][NAME_HAND], 6) for n in k] == [4.0, 6.0, 12.0]
    ok &= sym["Niedrig"][NAME_IMPORT] == 0.0 and sym["Mittel"][NAME_IMPORT] is None and sym["Hoch"][NAME_IMPORT] is None
    print("Kontrollwerte stimmen:", ok)
    assert ok, "Kontrollwerte weichen ab"

    # ---- CSV
    rows = []
    for n, sz in SZENARIEN.items():
        c = k[n]
        rows.append({"typ": "szenario", "szenario": n, "einmal_h": sz["einmal_h"], "laufend_h_je_jahr": sz["laufend_h"],
                     "einmalig_eur": c["einmal"], "laufend_eur_je_jahr": c["laufend"],
                     "summe_3_jahre_eur": c["summe"], "abo": "", "abo_preis_eur_je_jahr": "", "break_even_jahre": "",
                     "zusaetzliche_auftraege_marge_5": round(zusatz[n], 3)})
        for name, preis, _ in ABOS:
            be = break_even(c["einmal"], c["laufend"], preis)
            rows.append({"typ": "break_even", "szenario": n, "einmal_h": "", "laufend_h_je_jahr": "",
                         "einmalig_eur": "", "laufend_eur_je_jahr": "", "summe_3_jahre_eur": "", "abo": name,
                         "abo_preis_eur_je_jahr": preis, "break_even_jahre": "nie" if be is None else round(be, 2),
                         "zusaetzliche_auftraege_marge_5": ""})
        for m in MARGEN:
            rows.append({"typ": "sensitivitaet_marge", "szenario": n, "einmal_h": "", "laufend_h_je_jahr": "",
                         "einmalig_eur": "", "laufend_eur_je_jahr": "", "summe_3_jahre_eur": c["summe"],
                         "abo": f"marge_{int(m * 100)}_prozent", "abo_preis_eur_je_jahr": "",
                         "break_even_jahre": "", "zusaetzliche_auftraege_marge_5": round(c["summe"] / deckungsbeitrag(marge=m), 3)})
    for n in SZENARIEN:
        c = k[n]
        for name, ein, lauf in alternativen(n):
            be = break_even_allg(c["einmal"], c["laufend"], ein, lauf)
            rows.append({"typ": "symmetrisch", "szenario": n, "einmal_h": "", "laufend_h_je_jahr": "",
                         "einmalig_eur": ein, "laufend_eur_je_jahr": lauf, "summe_3_jahre_eur": ein + HORIZONT_JAHRE * lauf, "abo": name,
                         "abo_preis_eur_je_jahr": "", "break_even_jahre": "nie" if be is None else round(be, 2),
                         "zusaetzliche_auftraege_marge_5": ""})
    with REPORT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ---- Markdown
    L = []
    a = L.append
    a("# Make or Buy: Aufträge selbst filtern oder ein Abo kaufen")
    a("")
    a("Erzeugt mit `src/report/make_or_buy.py` (reine Standardbibliothek, `.venv\\Scripts\\python.exe -I src\\report\\make_or_buy.py`). "
      "CSV mit denselben Zahlen: `reports/make_or_buy.csv`. Das Modell rechnet **Kosten eines Betriebs**. Es sagt nichts über Nachfrage, "
      "Umsatz des Projekts oder die Qualität der Daten. Kontrollrechnung im Skript: bestanden.")
    a("")
    a("## 1. Fakten (mit Quelle)")
    a("")
    a("| Größe | Wert | Quelle |")
    a("|---|---|---|")
    a("| Jahresumsatz je Auftrag, Median | 167.404 € (Quartile 80.367 € / 422.744 €; n = 957) | `reports/auftragswerte_909.md`, TED-Zuschläge 2024 bis 2025, Haupt-CPV 909; nur 45 % der Zuschläge haben einen plausiblen Wert |")
    a("| Laufzeit | meist 2 Jahre fest plus 1 Jahr Option, also 3 Jahre | Gespräch mit einer Vergabestelle, n = 1 (`docs/business.md` §8.9) |")
    a("| Abo-Preise | siehe Tabelle 1 | `docs/business.md` §6, §8.1, §8.2, §8.9 |")
    a("")
    a("**Tabelle 1: Kaufen (Preise je Jahr, netto)**")
    a("")
    a("| Angebot | Preis je Jahr | Quelle / Hinweis |")
    a("|---|---|---|")
    for name, preis, q in ABOS:
        a(f"| {name} | {eur(preis)} | {q} |")
    a("")
    a("## 2. Annahmen (nicht gemessen)")
    a("")
    a("| Annahme | Wert | Herkunft |")
    a("|---|---|---|")
    a(f"| Stundensatz (extern) | {eur(STUNDENSATZ)}/h, Spanne 60 bis 110 €/h | Annahme; freelancermap Freelancer-Kompass 2025, Durchschnitt etwa 104 €/h, sekundär über Websuche gelesen, nicht im Original geprüft |")
    for n, sz in SZENARIEN.items():
        a(f"| Aufwand {n} | einmalig {sz['einmal_h']} h, laufend {sz['laufend_h']} h je Jahr ({sz['beschreibung']}) | Annahme, keine Messung |")
    a(f"| Marge | {int(MARGE * 100)} % (Sensitivität 3 / 5 / 8 %) | Annahme |")
    a(f"| Kostenhorizont | {HORIZONT_JAHRE} Jahre | Annahme (entspricht einer Vertragslaufzeit) |")
    a("| Eigene Arbeitszeit | wird mit dem Stundensatz bewertet | Annahme; ein Betrieb, der selbst baut, setzt vielleicht einen anderen Satz an |")
    a("")
    a("## 3. Rechnung")
    a("")
    a("**Kosten des Eigenbaus.** einmalig = Stunden einmalig × Stundensatz; laufend = Stunden je Jahr × Stundensatz; Summe über 3 Jahre = einmalig + 3 × laufend.")
    a("")
    a("| Szenario | Rechenweg | einmalig | laufend je Jahr | Summe 3 Jahre |")
    a("|---|---|---|---|---|")
    for n, sz in SZENARIEN.items():
        c = k[n]
        a(f"| {n} | {sz['einmal_h']} h × {int(STUNDENSATZ)} € = {eur(c['einmal'])}; {sz['laufend_h']} h × {int(STUNDENSATZ)} € = {eur(c['laufend'])}; "
          f"{eur(c['einmal'])} + 3 × {eur(c['laufend'])} | {eur(c['einmal'])} | {eur(c['laufend'])} | {eur(c['summe'])} |")
    a("")
    a("**Break-even gegen ein Abo.** Eigenbau kostet nach t Jahren einmalig + laufend × t, das Abo Preis × t. Gleichstand bei t = einmalig / (Abopreis − laufend). "
      "Ist laufend ≥ Abopreis, wird der Eigenbau nie günstiger („nie“). Gegen Vergabeweiser (0 €) ist das immer so.")
    a("")
    a("| Abo (Preis je Jahr) | " + " | ".join(SZENARIEN) + " |")
    a("|---|" + "---|" * len(SZENARIEN))
    for name, preis, _ in ABOS:
        cells = []
        for n in SZENARIEN:
            c = k[n]
            be = break_even(c["einmal"], c["laufend"], preis)
            if be is None:
                cells.append("nie")
            else:
                cells.append(f"{zahl(be, 1)} Jahre" + (" (> 3)" if be > HORIZONT_JAHRE else "") +
                             f" = {eur(c['einmal'])} / ({eur(preis)} − {eur(c['laufend'])})")
        a(f"| {name} ({eur(preis)}) | " + " | ".join(cells) + " |")
    a("")
    a("**Zusätzliche Aufträge, die der frühe Hinweis erbringen müsste.** Deckungsbeitrag je Auftrag = Jahresumsatz × Marge × Laufzeit = "
      f"{eur(JAHRESUMSATZ_MEDIAN)} × {zahl(MARGE, 2)} × {LAUFZEIT_JAHRE} = {eur(db, 0)} (exakt {eur(db, 2)}). "
      "Zusätzliche Aufträge = Kosten der ersten drei Jahre / Deckungsbeitrag je Auftrag. Gemeint sind Aufträge, die der Betrieb **ohne** den Hinweis nicht gewonnen hätte.")
    a("")
    a("| Szenario | Kosten 3 Jahre | Marge 3 % (" + eur(deckungsbeitrag(marge=0.03)) + ") | Marge 5 % (" + eur(deckungsbeitrag(marge=0.05)) +
      ") | Marge 8 % (" + eur(deckungsbeitrag(marge=0.08)) + ") |")
    a("|---|---|---|---|---|")
    for n in SZENARIEN:
        c = k[n]["summe"]
        a(f"| {n} | {eur(c)} | " + " | ".join(zahl(c / deckungsbeitrag(marge=m), 2) for m in MARGEN) + " |")
    a("")
    a("Dasselbe mit den Quartilen des Jahresumsatzes (Marge 5 %, Laufzeit 3 Jahre):")
    a("")
    a("| Szenario | unteres Quartil (" + eur(JAHRESUMSATZ_QUARTILE[0]) + ") | Median | oberes Quartil (" + eur(JAHRESUMSATZ_QUARTILE[1]) + ") |")
    a("|---|---|---|---|")
    for n in SZENARIEN:
        c = k[n]["summe"]
        a(f"| {n} | " + " | ".join(zahl(c / deckungsbeitrag(umsatz=u), 2) for u in (JAHRESUMSATZ_QUARTILE[0], JAHRESUMSATZ_MEDIAN, JAHRESUMSATZ_QUARTILE[1])) + " |")
    a("")
    a("Sensitivität Stundensatz (Summe 3 Jahre):")
    a("")
    a("| Szenario | " + " | ".join(f"{int(s)} €/h" for s in STUNDENSATZ_SPANNE) + " |")
    a("|---|" + "---|" * len(STUNDENSATZ_SPANNE))
    for n, sz in SZENARIEN.items():
        a(f"| {n} | " + " | ".join(eur(kosten(sz, s)["summe"]) for s in STUNDENSATZ_SPANNE) + " |")
    a("")
    a("Kontrolle: Niedrig 2.000 € / 500 € / 3.500 €, Break-even gegen DTAD 2,0 Jahre; Mittel 6.000 € / 2.000 € / 12.000 €; Hoch 12.000 € / 5.000 € / 27.000 €; "
      "zusätzliche Aufträge 0,14 / 0,48 / 1,08 (Marge 5 %). Alle Werte oben stimmen (im Skript als Assertion geprüft).")
    a("")
    a("## 3a. Symmetrische Variante: auch bei Abo und kostenlosen Diensten fallen Stunden an")
    a("")
    a("Das Basismodell (Abschnitt 3) rechnet Abos und kostenlose Dienste **ohne Eigenaufwand** und den Eigenbau **mit** Stunden. Daraus folgt „gegen kostenlose Dienste ist Eigenbau nie günstiger“ "
      "**aus der Konstruktion des Modells**, nicht aus einer Messung. Die symmetrische Variante gibt auch den Alternativen Stunden (alles Annahmen, keine Messung). "
      "Das Basismodell bleibt unverändert (Abschnitt 3).")
    a("")
    a("| Annahme | Wert |")
    a("|---|---|")
    a("| Nutzung bei Abo und bei kostenlosem Dienst mit Übernahme von Hand (Alerts lesen, Treffer ins eigene System übertragen) | " +
      ", ".join(f"{NUTZUNG_H[n]} h je Jahr ({n})" for n in SZENARIEN) + ", je Szenario |")
    a(f"| Kostenlosen Dienst nutzen und selbst importieren | {IMPORT_EINMAL_H} h einmalig plus {IMPORT_LAUFEND_H} h je Jahr (derselbe Importaufwand wie Eigenbau Niedrig; die Nutzung ist darin enthalten, nicht doppelt gezählt) |")
    a("| Eigenbau | unverändert wie im Basismodell (laufende Stunden enthalten Pflege und Nutzung) |")
    a("| Alternative je Jahr | Abopreis + Nutzungsstunden × 100 € |")
    a("")
    a("**Break-even, Basismodell / symmetrische Variante** (Jahre bis der Eigenbau günstiger ist; „von Beginn an“ = nie teurer, „nie“ = nie günstiger, „(> 3)“ = jenseits des Horizonts):")
    a("")
    a("| Alternative | " + " | ".join(f"{n}: Basis / symmetrisch" for n in SZENARIEN) + " |")
    a("|---|" + "---|" * len(SZENARIEN))
    for name, preis, _ in ABOS:
        cells = []
        for n in SZENARIEN:
            c = k[n]
            b = be_zelle(break_even(c["einmal"], c["laufend"], preis))
            if name == "Vergabeweiser":
                sy = " / ".join(be_zelle(break_even_allg(c["einmal"], c["laufend"], ein, lauf)) for nm, ein, lauf in alternativen(n)[-2:])
                cells.append(f"{b} / {sy} (Hand / Import)")
            else:
                alt = [x for x in alternativen(n) if x[0] == name][0]
                cells.append(f"{b} / {be_zelle(break_even_allg(c['einmal'], c['laufend'], alt[1], alt[2]))}")
        a(f"| {name} ({eur(preis)}) | " + " | ".join(cells) + " |")
    a("")
    a("**Kosten in 3 Jahren, symmetrische Variante** (einmalig + 3 × laufend; Eigenbau zum Vergleich):")
    a("")
    a("| Weg | " + " | ".join(SZENARIEN) + " |")
    a("|---|" + "---|" * len(SZENARIEN))
    a("| Eigenbau | " + " | ".join(eur(k[n]["summe"]) for n in SZENARIEN) + " |")
    for i, (nm, _, _) in enumerate(alternativen("Niedrig")):
        a(f"| {nm} | " + " | ".join(eur(alternativen(n)[i][1] + HORIZONT_JAHRE * alternativen(n)[i][2]) for n in SZENARIEN) + " |")
    a("")
    a("Kontrolle der symmetrischen Variante (im Skript als Assertion): DTAD 1,0 / 2,4 / 4,8 Jahre; kostenloser Dienst von Hand 4,0 / 6,0 / 12,0 Jahre; kostenloser Dienst mit Import: Niedrig von Beginn an, Mittel und Hoch nie.")
    a("")
    a("## 4. Deutung (Interpretation, keine Fakten)")
    a("")
    a("- **Im Basismodell ist Eigenbau gegen kostenlose Dienste nie günstiger (Modellkonstruktion, Annahmen, keine Messung).** Vergabeweiser (API/MCP) kostet 0 € und wird im Basismodell ohne Eigenaufwand gerechnet, der Eigenbau mit Stunden; das Ergebnis folgt aus dieser Konstruktion. "
      "Dasselbe gilt für AusschreibungsRadar Starter (laufende Eigenkosten von 500 € und mehr liegen über 290 € bzw. 348 € im Jahr).")
    a("- **Symmetrische Variante (Abschnitt 3a):** Gibt man auch Abo und kostenlosen Diensten Nutzungsstunden, wird der Eigenbau gegen DTAD schon im Niedrig-Szenario nach 1,0 Jahren und im Mittel-Szenario nach 2,4 Jahren günstiger; "
      "gegen einen kostenlosen Dienst mit Übernahme von Hand erst nach 4,0 / 6,0 / 12,0 Jahren. Gegen einen kostenlosen Dienst mit eigenem Import ist der Eigenbau Niedrig von Beginn an nicht teurer, weil der Importaufwand dort dem Eigenbau Niedrig gleich angesetzt ist und nur die laufenden Stunden höher (10 h gegen 5 h); diese Annahme trägt das Ergebnis. "
      "Die Ergebnisse hängen an den angenommenen Stunden. **Die Aussage, die beide Varianten tragen: Der Preis ist kein Vorteil des Eigenbaus.** Sie sagt nicht, dass der Eigenbau teuer wäre.")
    a("- **Im Basismodell rechnet sich Eigenbau gegen ein Abo wie DTAD nur im Niedrig-Szenario** und erst nach 2,0 Jahren. Im Mittel- und Hoch-Szenario übersteigen die laufenden Eigenkosten (2.000 € bzw. 5.000 €) den Abopreis von 1.500 € im Jahr. "
      "Gegen den oberen subreport-Preis (2.376 € im Jahr) wäre der Eigenbau im Niedrig-Szenario nach 1,1 Jahren günstiger; im Mittel-Szenario erst nach rund 16 Jahren, im Hoch-Szenario nie.")
    a("- Gegen AusschreibungsRadar Professional (1.490 € im Jahr, einzige Stufe mit CSV-Export) gilt dasselbe wie gegen DTAD: nur im Niedrig-Szenario, nach 2,0 Jahren; gegen Business (948 €) erst nach 4,5 Jahren.")
    a("- **Ein Abo kauft nicht nur Daten**, sondern auch Pflege, Suchprofile und Alarme. Der Eigenbau muss diese Arbeit selbst leisten; das Modell bewertet sie nur über den Stundensatz.")
    a("- **Die Rechnung „zusätzliche Aufträge“ ist eine Größenordnung, kein Nutzenbeleg.** Selbst im Hoch-Szenario genügt rechnerisch etwa ein zusätzlicher Auftrag in drei Jahren, im Niedrig-Szenario ein siebtel. "
      "Ob ein früher Hinweis auch nur einen Auftrag zusätzlich bringt, ist nicht belegt (A1, A15; Gespräche n = 3, gespalten). Die Marge von 5 % ist eine Annahme; bei 3 % steigt die Zahl im Hoch-Szenario auf 1,79.")
    a("- **Folgerung:** Ein Mehrwert gegenüber den kostenlosen Wegen müsste aus **Funktion** kommen (zum Beispiel Daten mit festem Schema im eigenen System, Anreicherung), nicht aus dem Preis. "
      "„Keine Abo-Kosten“ ist kein Vorteil an sich: Kostenlose Wege bestehen, und die Eigenleistung kostet Stunden (Basismodell und symmetrische Variante).")
    a("")
    a("### Nutzenseite: die Kosten sind klein gegen einen Auftrag")
    a("")
    a(f"Gemessen an einem Auftrag (Deckungsbeitrag {eur(db)} in drei Jahren bei {int(MARGE * 100)} % Marge) sind die Kosten des Eigenbaus klein: Sie entsprechen {zahl(zusatz['Niedrig'], 2)} bis {zahl(zusatz['Hoch'], 2)} zusätzlichen Aufträgen (Niedrig bis Hoch). "
      "Das zeigt, dass **nicht die Kostenfrage entscheidet**, sondern die Frage, ob ein früher Hinweis überhaupt einen Auftrag bringt (**nicht belegt**; A1, A15). "
      "„Deckungsbeitrag“ steht hier für Umsatz × Marge, **ohne** Angebotsaufwand und **ohne** Zuschlagswahrscheinlichkeit. Der Median des Jahresumsatzes gilt nur für TED-Aufträge mit plausiblem Wert "
      "(47,7 % in der Oberpfalz-Liste: 62 von 130 Losen).")
    a("")
    a("## 5. Grenzen")
    a("")
    a("- Alle Aufwandswerte und die Marge sind Annahmen; die Spanne der Szenarien ist weit (3.500 bis 27.000 € in drei Jahren) und nicht aus einer Umsetzung abgeleitet.")
    a("- Symmetrische Variante: Dass der Eigenbau laufend weniger Stunden braucht (5 / 20 / 50 h) als die Nutzung eines Dienstes (10 / 30 / 60 h), ist eine nicht begründete Annahme; sie bestimmt, ob der Eigenbau in 3a günstiger erscheint. Beide Varianten sind Modellkonstruktionen.")
    a("- Der Stundensatz stammt aus einer sekundären Quelle (Freiberufler-Durchschnitt), nicht aus der Kostenrechnung eines Reinigungsbetriebs; ein Betrieb mit freier Büro-Kapazität rechnet anders.")
    a("- Der Median des Jahresumsatzes gilt für TED-Aufträge mit plausiblem Wert (45 %); kleine Betriebe und unterschwellige Aufträge sind nicht abgebildet.")
    a("- Die Rechnung vergleicht Kosten, nicht Funktionen: Die Dienste unterscheiden sich in Abdeckung, Alarmen und Bedienung. Eine Abdeckungsaussage (zum Beispiel 'TED reicht') folgt daraus nicht; "
      "26,7 % der Oberpfälzer Reinigungsverfahren im Bekanntmachungsservice standen nicht auf TED (Wilson 19,6 bis 35,2 %).")
    a("- AusschreibungsRadar-Jahrespreise: Die Werte 290 € und 1.490 € sind vom Auftrag vorgegeben; Monatspreise × 12 wären 348 € und 1.788 €. An den Ergebnissen („nie“) ändert das nichts.")
    a("")
    REPORT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("geschrieben:", REPORT_MD, REPORT_CSV)


if __name__ == "__main__":
    main()
