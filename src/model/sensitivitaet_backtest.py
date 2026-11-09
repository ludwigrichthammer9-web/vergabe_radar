"""Nachtrag zu Iteration 5: Sensitivität des Backtests (Vorlauf und Fenster), offline aus dem Bericht.

NACHTRÄGLICH, KEIN NEUER TEST. Die Regeln R0 und R1 und das Kriterium X3 (Treffer ±3 Monate in mindestens 60 %) wurden vor
Iteration 5 festgelegt (src/model/baseline.py). Dieses Skript fragt rückblickend: Wie gut wäre die Regel bestenfalls gewesen,
wenn man Vorlauf oder Fenster im Nachhinein auf genau diesen 52 Paaren optimiert? Das ist eine Obergrenze (optimistisch verzerrt),
kein Beleg für eine bessere Regel.

Daten: die Tabelle „Alle Paare“ in reports/backtest_iteration5.md (im Git, 52 Paare). Es werden keine lokalen Rohdaten gebraucht;
das Skript eignet sich deshalb auch für den Live-Nachweis „Parameter ändern“ (Argumente --vorlauf und --fenster).

Aufruf:
  python src/model/sensitivitaet_backtest.py                      # Bericht reports/sensitivitaet_iteration5.md
  python src/model/sensitivitaet_backtest.py --vorlauf 9 --fenster 2   # nur eine Variante auf dem Bildschirm
"""

import argparse
import calendar
import math
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
QUELLE = ROOT / "reports" / "backtest_iteration5.md"
REPORT = ROOT / "reports" / "sensitivitaet_iteration5.md"

ZEILE = re.compile(r"^\| (\w+) \| \S+ \| (\d{4}-\d\d-\d\d) \| (\d{4}-\d\d-\d\d) \| (\d{4}-\d\d-\d\d|–)")


def plus_monate(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    y, mo = d.year + y, mo + 1
    return date(y, mo, min(d.day, calendar.monthrange(y, mo)[1]))


def lade_paare():
    paare = []
    for zeile in QUELLE.read_text(encoding="utf-8").splitlines():
        m = ZEILE.match(zeile)
        if m:
            hoechst = None if m[4] == "–" else date.fromisoformat(m[4])
            paare.append((m[1], date.fromisoformat(m[2]), date.fromisoformat(m[3]), hoechst))
    return paare


def treffer(paare, regel, vorlauf, fenster):
    """Liste von True/False je Paar. R0: Ende der Grundlaufzeit − Vorlauf; R1: Höchstende − Vorlauf (sonst wie R0)."""
    out = []
    for _, veroeff, gl_ende, hoechst in paare:
        basis = gl_ende if regel == "R0" else (hoechst or gl_ende)
        prognose = plus_monate(basis, -vorlauf)
        out.append(plus_monate(prognose, -fenster) <= veroeff <= plus_monate(prognose, fenster))
    return out


def wilson(k, n, z=1.96):
    p = k / n
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    return 100 * (c - m), 100 * (c + m)


def mcnemar_exakt(b, c):
    """Zweiseitiger exakter McNemar-Test (Binomial mit p = 0,5 auf den diskordanten Paaren)."""
    n = b + c
    k = min(b, c)
    p = 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vorlauf", type=int, help="Vorlauf in Monaten (vorab festgelegt: 6)")
    ap.add_argument("--fenster", type=int, help="Treffer-Fenster ± Monate (vorab festgelegt: 3)")
    a = ap.parse_args()
    paare = lade_paare()
    n = len(paare)
    assert n == 52, f"erwartet 52 Paare, gefunden {n}"

    if a.vorlauf is not None or a.fenster is not None:
        v = 6 if a.vorlauf is None else a.vorlauf
        f = 3 if a.fenster is None else a.fenster
        for regel in ("R0", "R1"):
            k = sum(treffer(paare, regel, v, f))
            lo, hi = wilson(k, n)
            print(f"{regel}: Vorlauf {v} Monate, Fenster ±{f}: {k} von {n} = {100 * k / n:.1f} % (Wilson {lo:.1f}–{hi:.1f} %)")
        print("Vorab festgelegt: Vorlauf 6, Fenster ±3, Schwelle 60 %.")
        return

    z = ["# Sensitivität des Backtests (Nachtrag zu Iteration 5)", "",
         "_Erzeugt von `src/model/sensitivitaet_backtest.py` aus der Tabelle „Alle Paare“ in `reports/backtest_iteration5.md` "
         f"({n} Paare). **Nachträglich, kein neuer Test:** Vorlauf und Fenster werden hier im Nachhinein auf denselben Paaren variiert; "
         "das beste Ergebnis ist eine optimistische Obergrenze._", ""]
    # Kontrolle gegen den Bericht
    r0 = treffer(paare, "R0", 6, 3)
    r1 = treffer(paare, "R1", 6, 3)
    z += ["## Kontrolle (vorab festgelegte Regel)", "",
          f"R0 (Ende der Grundlaufzeit − 6 Monate, ±3): **{sum(r0)} von {n} = {100 * sum(r0) / n:.1f} %**; "
          f"R1 (Höchstende − 6 Monate, ±3): **{sum(r1)} von {n} = {100 * sum(r1) / n:.1f} %** "
          f"(Wilson {wilson(sum(r1), n)[0]:.1f}–{wilson(sum(r1), n)[1]:.1f} %). Muss mit `reports/backtest_iteration5.md` übereinstimmen (9 und 15).", ""]
    b = sum(1 for x, y in zip(r1, r0) if x and not y)
    c = sum(1 for x, y in zip(r1, r0) if y and not x)
    z += ["## R1 gegen R0 auf denselben Paaren", "",
          f"Nur R1 trifft: {b} Paare; nur R0 trifft: {c} Paare. Exakter McNemar-Test (zweiseitig): p = {mcnemar_exakt(b, c):.2f}. "
          "Der Vorsprung von R1 vor der naiven Referenz ist damit statistisch nicht gesichert.", ""]
    # Vorlauf variieren
    z += ["## Vorlauf 0 bis 24 Monate (Fenster ±3)", "", "| Vorlauf (Monate) | R0 Treffer | R1 Treffer | R1 in % |", "|---|---|---|---|"]
    beste = (0, None)
    for v in range(25):
        k0, k1 = sum(treffer(paare, "R0", v, 3)), sum(treffer(paare, "R1", v, 3))
        if k1 > beste[0]:
            beste = (k1, v)
        z.append(f"| {v}{' (vorab)' if v == 6 else ''} | {k0} | {k1} | {100 * k1 / n:.1f} |")
    z += ["", f"Bester Vorlauf für R1: {beste[1]} Monate mit {beste[0]} von {n} = {100 * beste[0] / n:.1f} % "
          f"(Schwelle 60 % = {math.ceil(0.6 * n)} Treffer).", ""]
    # Fenster variieren
    z += ["## Fenster bei Vorlauf 6 Monaten", "", "| Fenster | R0 | R1 | R1 in % |", "|---|---|---|---|"]
    for f in (1, 2, 3, 4, 6, 9, 12):
        k0, k1 = sum(treffer(paare, "R0", 6, f)), sum(treffer(paare, "R1", 6, f))
        z.append(f"| ±{f}{' (vorab)' if f == 3 else ''} | {k0} | {k1} | {100 * k1 / n:.1f} |")
    z += ["", "## Deutung", "",
          "Auch mit einem im Nachhinein optimal gewählten Vorlauf bleibt die Trefferquote weit unter der vorab festgelegten Schwelle "
          "von 60 %. Erst sehr breite Fenster (±6 Monate und mehr) erhöhen die Quote, sind für die Planung eines Betriebs aber kaum "
          "nützlich (ein Jahr Unsicherheit). Das Ergebnis „keine brauchbare Terminprognose aus TED“ hängt also nicht an der Wahl "
          "von 6 Monaten. Grenzen: 52 Paare aus einer Rückwärtssuche (verlängerte Verträge ohne Neuausschreibung fehlen), "
          "41 von 52 Vorgängern vor eForms.", ""]
    REPORT.write_text("\n".join(z), encoding="utf-8")
    print(f"{REPORT}  (R0 {sum(r0)}, R1 {sum(r1)}, bester Vorlauf {beste[1]} -> {beste[0]}, McNemar p={mcnemar_exakt(b, c):.2f})")


if __name__ == "__main__":
    main()
