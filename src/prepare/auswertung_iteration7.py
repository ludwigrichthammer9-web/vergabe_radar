"""Iteration 7, Schritt 4: Auswertung der Prüfung der Vertragsliste (Y1, Y1r, Y2, Y2b und beschreibende Kennzahlen).

Vorab festgelegt (docs/iterationen.md, Iteration 7):
- Y1: Ende der Grundlaufzeit der Liste stimmt mit dem Eintrag des Prüfers überein (ein Tag Toleranz); „unbekannt“ des Prüfers zählt als Abweichung. Hauptstichprobe: 80 Lose (Typ Y).
- Y1r: wie Y1, nur für die 15 Regelwirkungs-Lose (Typ R), Schwelle 12/15.
- Y2: Höchstende korrekt oder in der Liste „unbestimmbar“; „Höchstende = Grundlaufzeit“ zählt als korrekt, wenn der Prüfer „keine Verlängerung“ einträgt.
  Y2b: wie Y2, nur für Lose, bei denen die Liste ein Höchstende nennt. Beide für die 80 Lose des Typs Y.
- Beschreibend: Y1 gewichtet, Y1 nur für Quelle „Text“, Prüfzeit, Gesamtschätzung (128 · a_R + 2.796 · a_Y) / 2.924.
Eingaben: reports/liste_pruefung_iteration7_urteile.csv (aus der Datei des Prüfers übertragen) und der lokale Schlüssel
data/processed/liste_pruefung_iteration7_schluessel.csv (SHA-256 vor dem Öffnen geprüft).

Aufruf:  .venv\\Scripts\\python -I src/prepare/auswertung_iteration7.py      Ausgabe: reports/liste_auswertung_iteration7.md
"""

import csv
import hashlib
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src" / "prepare"))

from auswertung_iteration6 import datum, pct  # noqa: E402
from vertragsliste import OUT_CSV, X4_BIS, X4_VON  # noqa: E402

SCHLUESSEL = ROOT / "data" / "processed" / "liste_pruefung_iteration7_schluessel.csv"
URTEILE = ROOT / "reports" / "liste_pruefung_iteration7_urteile.csv"
NACH = ROOT / "reports" / "liste_nachpruefung_iteration7_urteile.csv"
MAX_Y = 50  # Kürzung (docs/iterationen.md, vor dem Ergebnis festgelegt): Typ Y nur L1 bis L50
REPORT = ROOT / "reports" / "liste_auswertung_iteration7.md"
SHA_VORAB = "eade66c033ab13d541dda2f7af3f5b074f1b5a4587e711f6a29e0ba1916ddf9b"
N_REGEL_FENSTER, N_REST_FENSTER, N_FENSTER = 128, 2796, 2924


def bewertung() -> tuple[list[dict], str]:
    """Je Los Schlüssel und Prüfereintrag mit ok1 (Y1) und ok2 (Y2); zweiter Wert der geprüfte Schlüssel-Hash."""
    sha = hashlib.sha256(SCHLUESSEL.read_bytes()).hexdigest()
    assert sha == SHA_VORAB, "Schlüssel verändert"
    with SCHLUESSEL.open(encoding="utf-8") as f:
        key = {r["L"]: r for r in csv.DictReader(f, delimiter=";")}
    with URTEILE.open(encoding="utf-8") as f:
        pr = {r["L"]: r for r in csv.DictReader(f, delimiter=";")}
    assert key.keys() == pr.keys(), "Lose in Schlüssel und Urteilen stimmen nicht überein"
    with NACH.open(encoding="utf-8") as f:
        nach = {r["L"]: r for r in csv.DictReader(f, delimiter=";")}
    rows = []
    for L in sorted(key, key=lambda x: int(x[1:])):
        k, p = key[L], dict(pr[L])
        n = nach.get(L)
        status, min_nach = "keine", 0
        if n:
            min_nach = int(n["minuten"]) if n["minuten"].strip().isdigit() else 0
            if n["gl_nach"].strip():
                # Eintrag der Nachprüfung ersetzt den Eintrag der ersten Abgabe (vorab festgelegt); Quelle nach fester Regel abgeleitet
                status = "ja"
                p["gl_pruefer"] = n["gl_nach"].strip().replace("/", ".")
                p["quelle"] = quelle_ableiten(n)
                if datum(n["hoechstende_nach"]):
                    p["hoechstende_pruefer"] = n["hoechstende_nach"]
            else:
                status = "leer"
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
        rows.append({**k, "gl_p": p["gl_pruefer"], "h_p": hp_raw, "quelle": p["quelle"], "ok1": ok1, "ok2": ok2,
                     "min": int(p["minuten"]), "min_nach": min_nach, "nach": status, "nach_zeile": n,
                     "hilf": p["hilfsmittel"].strip() or "keine (leer gelassen, laut Nutzer keine benutzt)", "nennt_h": hh != "unbestimmbar"})
    return rows, sha


def quelle_ableiten(n: dict) -> str:
    """Feste Regel (vorab mitgeteilt): Ende = Ende (Feld) oder Beginn + Dauer ohne Ende → Feld; Felder leer und Datum → Text; kein Datum → unbekannt; sonst abweichend."""
    gl, ende, beginn = datum(n["gl_nach"]), datum(n["ende_feld"]), datum(n["beginn_feld"])
    if gl is None:
        return "unbekannt"
    if ende and gl == ende:
        return "Feld"
    if not ende and beginn and n["dauer_feld"].strip():
        return "Feld"
    if not ende and not beginn:
        return "Text"
    return "abweichend"


def gewichte(rows: list[dict]) -> dict[str, float]:
    """Gewicht je Zuschlag = Lose des Zuschlags im Fenster (mit Ende der Grundlaufzeit) ÷ gezogene Lose desselben Zuschlags (Typ Y)."""
    with OUT_CSV.open(encoding="utf-8") as f:
        pool = Counter(r["notice"] for r in csv.DictReader(f, delimiter=";") if X4_VON <= r["veroeffentlicht"] <= X4_BIS and r["gl_ende"])
    gezogen = Counter(r["notice"] for r in rows if r["typ"] == "Y")
    return {n: pool[n] / gezogen[n] for n in gezogen}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rows, sha = bewertung()
    Y = [r for r in rows if r["typ"] == "Y" and int(r["L"][1:]) <= MAX_Y]
    R = [r for r in rows if r["typ"] == "R"]
    k1, k2 = sum(r["ok1"] for r in Y), sum(r["ok2"] for r in Y)
    kr = sum(r["ok1"] for r in R)
    yb = [r for r in Y if r["nennt_h"]]
    k2b = sum(r["ok2"] for r in yb)
    w = gewichte(Y)
    wy = sum(w[r["notice"]] * r["ok1"] for r in Y) / sum(w[r["notice"]] for r in Y)
    a_y, a_r = k1 / len(Y), kr / len(R)
    gesamt = (N_REGEL_FENSTER * a_r + N_REST_FENSTER * a_y) / N_FENSTER
    text = [r for r in Y if r["quelle"] == "Text"]
    mins = sorted(r["min"] for r in rows)
    min_nach = sum(r["min_nach"] for r in rows)
    nach_ja = [r for r in rows if r["nach"] == "ja"]
    nach_leer = [r for r in Y + R if r["nach"] == "leer"]
    hilf = Counter(r["hilf"] for r in rows)
    quellen = Counter(r["quelle"] for r in rows)

    stale = [r for r in Y if r["nach"] == "ja" and r["h_p"].strip().lower() == "unbestimmbar" and r["nennt_h"]]
    Y2e = [r for r in Y if r not in stale]
    unb = [r for r in Y if not r["ok1"] and r["gl_p"].strip().lower() == "unbekannt"]
    unb_r = [r for r in R if not r["ok1"] and r["gl_p"].strip().lower() == "unbekannt"]
    echt = [r for r in Y + R if not r["ok1"] and r["gl_p"].strip().lower() != "unbekannt"]
    nach_herkunft = defaultdict(lambda: [0, 0, 0])  # gesamt, ok, unbekannt
    for r in Y + R:
        z = nach_herkunft[(r["typ"], r["gl_herkunft"])]
        z[0] += 1
        z[1] += r["ok1"]
        z[2] += (not r["ok1"]) and r["gl_p"].strip().lower() == "unbekannt"

    out = ["# Auswertung der Prüfung der Vertragsliste (Iteration 7, Y1, Y1r, Y2, Y2b)", "",
           f"_Erzeugt mit `src/prepare/auswertung_iteration7.py`. Schlüssel-Hash geprüft: `{sha[:8]}…{sha[-4:]}` = vorab festgehaltener Wert. Eingaben des Prüfers aus der abgegebenen Datei in "
           "`reports/liste_pruefung_iteration7_urteile.csv` (erste Abgabe) und `reports/liste_nachpruefung_iteration7_urteile.csv` (Nachprüfung, ersetzt die erste Abgabe, wo ein Eintrag vorliegt) übertragen. "
           f"Typ Y nur L1 bis L{MAX_Y} (Kürzung, vor dem Ergebnis festgelegt), Typ R alle 15._", "",
           "## Fakten", "",
           f"- **Y1 ({len(Y)} Zufallslose, Ende der Grundlaufzeit): {pct(k1, len(Y))}** (Schwelle ≥ 90 %).",
           f"- **Y1r (15 Regelwirkungs-Lose): {pct(kr, len(R))}** (Schwelle ≥ 12/15).",
           f"- **Y2 (Höchstende korrekt oder „unbestimmbar“): {pct(k2, len(Y))}** (Schwelle ≥ 90 %).",
           f"- **Y2b (nur Lose, bei denen die Liste ein Höchstende nennt): {pct(k2b, len(yb))}** (Schwelle ≥ 85 %).",
           f"- Abweichungen bei Y1 (Typ Y): {len(Y) - k1}, davon {len(unb)} mit Prüfereintrag „unbekannt“ und {len(Y) - k1 - len(unb)} mit abweichendem Datum. "
           f"Typ R: {len(R) - kr}, davon {len(unb_r)} „unbekannt“.",
           f"- Quelle laut Prüfer: {dict(quellen)}. Hilfsmittel: {dict(hilf)}.",
           f"- Nachprüfung: {len(nach_ja)} Lose mit Eintrag, {len(nach_leer)} Lose im Umfang ohne Eintrag ({', '.join(r['L'] for r in nach_leer) or '–'}; es bleibt der Eintrag der ersten Abgabe). Prüfzeit: erste Abgabe Summe {sum(mins)} Minuten (Median {mins[len(mins) // 2]}), Nachprüfung {min_nach} Minuten. Sitzungstabellen (Start und Ende) liegen nicht vor.", "",
           f"- Y2 und Y2b mit Vorbehalt: In {len(stale)} der {len(Y)} Lose steht in der ersten Abgabe „unbestimmbar“, weil das Ende der Grundlaufzeit damals fehlte; die Nachprüfung lieferte es, das Höchstende wurde nicht neu eingetragen (nur bei Änderung gefordert). "
           f"Ohne diese veralteten Einträge: Y2 {pct(sum(r['ok2'] for r in Y2e), len(Y2e))}, Y2b {pct(sum(r['ok2'] for r in Y2e if r['nennt_h']), len([r for r in Y2e if r['nennt_h']]))}.", "",
           "### Beschreibend (ohne Schwelle)", "",
           f"- Y1 nach Losen gewichtet: {f'{100 * wy:.1f}'.replace('.', ',')} %.",
           f"- Y1 nur für Lose mit Quelle „Text“ (Typ Y): {pct(sum(r['ok1'] for r in text), len(text))}.",
           f"- Gesamtschätzung für das Fenster = (128 · {a_r:.3f} + 2.796 · {a_y:.3f}) / 2.924 = {f'{100 * gesamt:.1f}'.replace('.', ',')} %.", "",
           "### Y1 nach Herkunft des Enddatums der Liste", "",
           "| Typ | Herkunft | Lose | korrekt | davon Prüfer „unbekannt“ |", "|---|---|---|---|---|"]
    for (t, h), (n, ok, u) in sorted(nach_herkunft.items()):
        out.append(f"| {t} | {h} | {n} | {ok} | {u} |")
    out += ["", "### Abweichungen mit abweichendem Datum", "", "| L | Notice, Los | Typ | Liste: Ende GL (Herkunft) | Prüfer: Ende GL | Prüfer: Ende (Feld) |", "|---|---|---|---|---|---|"]
    for r in echt:
        n = r["nach_zeile"] or {}
        out.append(f"| {r['L']} | {r['notice']}, {r['los']} | {r['typ']} | {r['gl_ende']} ({r['gl_herkunft']}) | {r['gl_p']} | {n.get('ende_feld', '–') or '–'} |")
    out += ["", "### Abweichungen bei Y2", "", "| L | Notice, Los | Liste: Höchstende (Herkunft) | Prüfer: Höchstende |", "|---|---|---|---|"]
    for r in Y:
        if not r["ok2"]:
            out.append(f"| {r['L']} | {r['notice']}, {r['los']} | {r['hoechstende'] or '–'} ({r['hoechstende_herkunft']}) | {r['h_p']} |")
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Y1 {k1}/{len(Y)}, Y1r {kr}/{len(R)}, Y2 {k2}/{len(Y)}, Y2b {k2b}/{len(yb)}; gewichtet {100 * wy:.1f} %; Report {REPORT}")


if __name__ == "__main__":
    main()
