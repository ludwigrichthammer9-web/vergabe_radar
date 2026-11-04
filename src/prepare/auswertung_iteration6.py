"""Iteration 6, Schritt 4: Auswertung der Prüfung der Vertragsliste (Y1, Y2) und der 10 Paare (Teil B).

Vorab festgelegt (docs/iterationen.md, Iteration 6):
- Y1: Ende der Grundlaufzeit der Liste stimmt mit dem Eintrag des Prüfers überein (ein Tag Toleranz). Ein Eintrag „unbekannt“ des Prüfers zählt als Abweichung.
- Y2: Höchstende korrekt oder in der Liste als „unbestimmbar“ gekennzeichnet; „Höchstende = Grundlaufzeit“ (keine Angabe/keine Verlängerung) zählt als
  korrekt, wenn der Prüfer „keine Verlängerung“ (oder „keine Angabe“) einträgt. Jede andere Abweichung zählt als falsch.
Eingaben: reports/liste_pruefung_iteration6_urteile.csv (Einträge des Prüfers, aus dem PDF übertragen) und der lokale Schlüssel
data/processed/liste_pruefung_iteration6_schluessel.csv (SHA-256 vor dem Öffnen geprüft).

Aufruf:  python -I src/prepare/auswertung_iteration6.py      Ausgabe: reports/liste_auswertung_iteration6.md
"""

import csv
import hashlib
import math
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SCHLUESSEL = ROOT / "data" / "processed" / "liste_pruefung_iteration6_schluessel.csv"
URTEILE = ROOT / "reports" / "liste_pruefung_iteration6_urteile.csv"
REPORT = ROOT / "reports" / "liste_auswertung_iteration6.md"
SHA_VORAB = "3de3e81270ee2488f8b8b2f60c42d4f7271eb196bfcf7e8aa92809a0ba689d0e"


def datum(s: str) -> date | None:
    s = s.strip()
    try:
        if "." in s:
            t, m, j = s.split(".")
            return date(int(j), int(m), int(t))
        return date.fromisoformat(s[:10])
    except ValueError:
        return None


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return c - h, c + h


def pct(k: int, n: int) -> str:
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {100 * k / n:.1f} % (Wilson {100 * lo:.1f}–{100 * hi:.1f})".replace(".", ",")


def main() -> None:
    sha = hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()
    assert sha == SHA_VORAB, "Schlüssel verändert"
    with SCHLUESSEL.open(encoding="utf-8") as f:
        key = {r["L"]: r for r in csv.DictReader(f, delimiter=";") if r["L"].startswith("L")}
    with URTEILE.open(encoding="utf-8") as f:
        pr = {r["L"]: r for r in csv.DictReader(f, delimiter=";")}
    rows = []
    for L in sorted(key, key=lambda x: int(x[1:])):
        k, p = key[L], pr[L]
        gl_l, gl_p = datum(k["gl_ende"]), datum(p["gl_pruefer"])
        ok1 = bool(gl_l and gl_p and abs((gl_l - gl_p).days) <= 1)
        hl, hh = datum(k["hoechstende"]), k["hoechstende_herkunft"]
        hp_raw = p["hoechstende_pruefer"].strip()
        hp = datum(hp_raw)
        if hh == "unbestimmbar":
            ok2 = True
        elif hp:
            ok2 = bool(hl and abs((hl - hp).days) <= 1)
        elif hp_raw.lower().startswith("keine"):
            ok2 = bool(hl and gl_l and hl == gl_l)
        else:
            ok2 = False
        rows.append({**k, "gl_p": p["gl_pruefer"], "h_p": hp_raw, "ok1": ok1, "ok2": ok2, "min": p["minuten"], "hilf": p["hilfsmittel"]})
    n = len(rows)
    k1, k2 = sum(r["ok1"] for r in rows), sum(r["ok2"] for r in rows)
    unbekannt = [r for r in rows if not r["ok1"] and r["gl_p"].strip().lower() == "unbekannt"]
    mins = sorted(int(r["min"]) for r in rows if r["min"].strip().isdigit())
    out = ["# Auswertung der Prüfung der Vertragsliste (Iteration 6, Y1 und Y2)", "",
           f"_Erzeugt mit `src/prepare/auswertung_iteration6.py`. Schlüssel-Hash geprüft: `{sha[:8]}…{sha[-4:]}` = vorab festgehaltener Wert._", "",
           "## Fakten", "",
           f"- **Y1 Ende der Grundlaufzeit korrekt: {pct(k1, n)}** (Schwelle ≥ 90 %).",
           f"- **Y2 Höchstende korrekt oder als „unbestimmbar“ gekennzeichnet: {pct(k2, n)}** (Schwelle ≥ 90 %).",
           f"- Davon bei Y1 {len(unbekannt)} Abweichungen, weil der Prüfer „unbekannt“ eintrug, wo die Liste das Enddatum führt und der Text keine Verlängerung nennt "
           f"({', '.join(r['L'] for r in unbekannt)}). Werden sie als korrekt gezählt (nachträgliche Lesart, nicht das Kriterium): {pct(k1 + len(unbekannt), n)}.",
           f"- Prüfzeit je Los: Median {mins[len(mins) // 2] if mins else '–'} Minuten, Summe {sum(mins)} Minuten.",
           f"- Hilfsmittel: in {sum(1 for r in rows if not r['hilf'].strip())} von {n} Einträgen leer (weder „keine“ noch ein Hilfsmittel vermerkt).", "",
           "### Abweichungen", "",
           "| L | Notice, Los | Liste: Ende GL (Herkunft) | Prüfer: Ende GL | Liste: Höchstende (Herkunft) | Prüfer: Höchstende | Y1 | Y2 |",
           "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if not (r["ok1"] and r["ok2"]):
            out.append(f"| {r['L']} | {r['notice']}, {r['los']} | {r['gl_ende']} ({r['gl_herkunft']}) | {r['gl_p']} | {r['hoechstende'] or '–'} ({r['hoechstende_herkunft']}) | "
                       f"{r['h_p']} | {'✓' if r['ok1'] else '✗'} | {'✓' if r['ok2'] else '✗'} |")
    out += ["", "## Interpretation", "",
            "- Echte Fehler der Liste: L1, L42, L43 (das Enddatum BT-537 ist schon das Höchstende; der Text nennt die feste Laufzeit ohne „zunächst“, z. B. „Festlaufzeit von …“, "
            "„Laufzeit von 2 Jahren“, „erste feste Laufzeit bis …“; Regel 1a erkennt das nicht) und L56 (Verlängerung steht nur im Originaltext außerhalb der gelesenen Felder).",
            "- L8, L48, L49 sind Auslegungsfälle: Ohne Verlängerung sind Ende der Grundlaufzeit und Höchstende dasselbe Datum; der Prüfer trug „unbekannt“ ein. L26: Prüfer „unbekannt“ beim Höchstende.",
            "- Y1 liegt genau auf der Schwelle; das Intervall reicht weit darunter. Das Ergebnis ist knapp und hängt an wenigen Fällen.", ""]
    REPORT.write_text("\n".join(out), encoding="utf-8")
    print(f"Y1 {k1}/{n}, Y2 {k2}/{n}; Report {REPORT}")


if __name__ == "__main__":
    main()
