"""Iteration 8, Schritt 3: Auswertung der KI-Zweitlesung (Z0 bis Z4 und beschreibende Kennzahlen).

Vorab festgelegt (docs/iterationen.md, Iteration 8; dieses Skript vor dem Eintreffen der Antworten der Leser committet):
- Z0: Leser A und B stimmen beim Ende der Grundlaufzeit überein (ein Tag Toleranz, oder beide `unbekannt`), alle 95 Lose, Schwelle 90 %.
- Vergleichswert: bei Übereinstimmung der Wert von A; sonst die Entscheidung des Evaluators am Original (`…_entscheide.csv`), ersatzweise `unklar`.
  `unklar` und `unbekannt` beim Vergleichswert zählen als Abweichung der Liste. Für das Höchstende gilt dasselbe (Übereinstimmung: Datum ±1 Tag oder gleiche Kategorie).
- Z1: Liste = Vergleichswert (Ende der Grundlaufzeit), 80 Lose Typ Y, Schwelle 72/80. Z2: dasselbe, 15 Lose Typ R, Schwelle 12/15.
- Z3: Höchstende korrekt oder in der Liste „unbestimmbar“ (80 Lose, ≥ 90 %); nur Lose mit behauptetem Höchstende (≥ 85 %). „Höchstende = Grundlaufzeit“ korrekt bei Vergleichswert „keine …“.
- Z4: 10 Lose, mit SEED_Z4 aus den Übereinstimmungen von A und B (Ende der Grundlaufzeit, nach Nummer sortiert) gezogen; Prüfung des Evaluators in `…_z4.csv`, Schwelle 9/10.
- Beschreibend: Vergleich Liste / Vergleichswert / Prüfer der Iteration 7 (L1–L50, Typ Y), Z1 gewichtet, „keine Gebäudereinigung“, Kontroll-Lose K1–K3.

Eingaben: reports/zweitlesung_iteration8_leser_a.csv, …_leser_b.csv (Antworten der Leser, unverändert), …_entscheide.csv und …_z4.csv (Evaluator),
Schlüssel data/processed/liste_pruefung_iteration7_schluessel.csv (SHA-256 geprüft), Prüfer-Einträge über auswertung_iteration7.bewertung().
Fehlen Entscheidungen oder die Z4-Prüfung, schreibt das Skript die offenen Lose in die Ausgabe und rechnet Z1 bis Z3 noch nicht.

Aufruf:  .venv\\Scripts\\python -I src/prepare/auswertung_iteration8.py      Ausgabe: reports/zweitlesung_iteration8_auswertung.md
"""

import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src" / "prepare"))

from auswertung_iteration6 import datum, pct  # noqa: E402
from auswertung_iteration7 import MAX_Y, bewertung, gewichte  # noqa: E402
from zweitlesung_iteration8 import N_Z4, SEED_Z4  # noqa: E402

R_DIR = ROOT / "reports"
LESER = {"A": R_DIR / "zweitlesung_iteration8_leser_a.csv", "B": R_DIR / "zweitlesung_iteration8_leser_b.csv"}
ENTSCHEIDE = R_DIR / "zweitlesung_iteration8_entscheide.csv"   # Nr;gl;hoechstende;begruendung
Z4_DATEI = R_DIR / "zweitlesung_iteration8_z4.csv"             # Nr;bestaetigt;begruendung
OBERPFALZ = R_DIR / "beispiel_liste_oberpfalz.csv"
REPORT = R_DIR / "zweitlesung_iteration8_auswertung.md"
KONTROLLE = {"K1": "8", "K2": "9", "K3": "14"}


def lesen(pfad: Path) -> dict[str, dict]:
    if not pfad.exists():
        return {}
    with pfad.open(encoding="utf-8") as f:
        return {r["Nr"].strip(): r for r in csv.DictReader(f, delimiter=";")}


def norm(s: str) -> str:
    """Datum als ISO-Text, sonst kleingeschriebene Kategorie (unbekannt, keine verlängerung, keine angabe, unbestimmbar, unklar)."""
    d = datum(s.replace("/", "."))
    return d.isoformat() if d else s.strip().lower()


def gleich(a: str, b: str) -> bool:
    da, db = datum(a), datum(b)
    if da and db:
        return abs((da - db).days) <= 1
    return not da and not db and a == b


def ok_gl(liste: str, ref: str) -> bool:
    return bool(datum(liste) and datum(ref)) and gleich(liste, ref)


def ok_h(k: dict, ref_h: str) -> bool:
    """Wie Y2 in Iteration 7, mit dem Vergleichswert statt des Prüfers."""
    hl, gl_l = datum(k["hoechstende"]), datum(k["gl_ende"])
    if k["hoechstende_herkunft"] == "unbestimmbar":
        return True
    if datum(ref_h):
        return bool(hl) and gleich(k["hoechstende"], ref_h)
    if ref_h.startswith("keine"):
        return bool(hl and gl_l and hl == gl_l)
    return False


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rows, sha = bewertung()                      # Schlüssel (Hash geprüft) + Prüfer der Iteration 7
    key = {r["L"]: r for r in rows}
    a, b = lesen(LESER["A"]), lesen(LESER["B"])
    alle = [f"L{i}" for i in range(1, 96)]
    fehlt = [n for n in alle + list(KONTROLLE) if n not in a or n not in b]
    assert not fehlt, f"Antworten fehlen: {fehlt}"
    ent, z4 = lesen(ENTSCHEIDE), lesen(Z4_DATEI)

    v = {}
    for n in alle + list(KONTROLLE):
        ga, gb = norm(a[n]["ende_grundlaufzeit"]), norm(b[n]["ende_grundlaufzeit"])
        ha, hb = norm(a[n]["hoechstende"]), norm(b[n]["hoechstende"])
        e = ent.get(n)
        v[n] = {"ga": ga, "gb": gb, "ha": ha, "hb": hb, "einig_gl": gleich(ga, gb), "einig_h": gleich(ha, hb),
                "gl": ga if gleich(ga, gb) else (norm(e["gl"]) if e and e["gl"].strip() else None),
                "h": ha if gleich(ha, hb) else (norm(e["hoechstende"]) if e and e["hoechstende"].strip() else None),
                "rein": "nein" if "nein" in (a[n]["gebaeudereinigung"].strip().lower(), b[n]["gebaeudereinigung"].strip().lower()) else "ja"}

    einig = [n for n in alle if v[n]["einig_gl"]]
    z4_lose = sorted(random.Random(SEED_Z4).sample(sorted(einig, key=lambda x: int(x[1:])), N_Z4), key=lambda x: int(x[1:]))
    offen = [n for n in alle + list(KONTROLLE) if v[n]["gl"] is None or v[n]["h"] is None]
    z4_offen = [n for n in z4_lose if n not in z4]

    out = ["# Auswertung der KI-Zweitlesung (Iteration 8, Z0 bis Z4)", "",
           f"_Erzeugt mit `src/prepare/auswertung_iteration8.py`. Schlüssel-Hash geprüft (`{sha[:8]}…`). Leser A = Opus, Leser B = Sonnet, je 4 Teilläufe; Antworten unverändert in "
           "`reports/zweitlesung_iteration8_leser_a.csv` und `…_leser_b.csv`. Liste eingefroren (Commit a93785e)._", "",
           "## Fakten", "",
           f"- **Z0 (Leser A = Leser B beim Ende der Grundlaufzeit, 95 Lose): {pct(len(einig), len(alle))}** (Schwelle ≥ 90 %). "
           f"Höchstende einig: {sum(v[n]['einig_h'] for n in alle)}/95.",
           f"- Z4-Stichprobe (Seed {SEED_Z4}): {', '.join(z4_lose)}."]
    if offen or z4_offen:
        out += ["", f"**Noch offen:** Entscheidung des Evaluators für {', '.join(offen) or '–'}; Z4-Prüfung für {', '.join(z4_offen) or '–'}. Z1 bis Z4 werden erst danach berechnet."]
        REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"Z0 {len(einig)}/95; offen: {offen}; Z4 offen: {z4_offen}")
        return

    Y = [n for n in alle if key[n]["typ"] == "Y"]
    R = [n for n in alle if key[n]["typ"] == "R"]
    ok1 = {n: ok_gl(key[n]["gl_ende"], v[n]["gl"]) for n in alle}
    ok2 = {n: ok_h(key[n], v[n]["h"]) for n in alle}
    yb = [n for n in Y if key[n]["hoechstende_herkunft"] != "unbestimmbar"]
    k4 = sum(z4[n]["bestaetigt"].strip().lower() == "ja" for n in z4_lose)
    w = gewichte([key[n] for n in Y])
    wz1 = sum(w[key[n]["notice"]] * ok1[n] for n in Y) / sum(w[key[n]["notice"]] for n in Y)
    ref_unsicher = [n for n in Y + R if v[n]["gl"] in ("unbekannt", "unklar")]
    out += [
        f"- **Z1 (Liste = Vergleichswert, 80 Lose Typ Y): {pct(sum(ok1[n] for n in Y), len(Y))}** (Schwelle ≥ 72/80). Davon Vergleichswert „unbekannt“/„unklar“: "
        f"{sum(1 for n in Y if n in ref_unsicher)}.",
        f"- **Z2 (15 Regelwirkungs-Lose): {pct(sum(ok1[n] for n in R), len(R))}** (Schwelle ≥ 12/15).",
        f"- **Z3 (Höchstende korrekt oder „unbestimmbar“, 80 Lose): {pct(sum(ok2[n] for n in Y), len(Y))}** (Schwelle ≥ 90 %); "
        f"**nur Lose mit behauptetem Höchstende: {pct(sum(ok2[n] for n in yb), len(yb))}** (Schwelle ≥ 85 %).",
        f"- **Z4 (Evaluator bestätigt Übereinstimmungen am Original): {k4}/{N_Z4}** (Schwelle ≥ 9/10).",
        f"- Uneinigkeiten vom Evaluator entschieden: {len(ent)} Lose ({', '.join(sorted(ent, key=lambda x: (x[0], int(x[1:])))) or '–'}).", "",
        "### Beschreibend (ohne Schwelle)", "",
        f"- Z1 nach Losen gewichtet: {f'{100 * wz1:.1f}'.replace('.', ',')} %.",
        f"- Von mindestens einem Leser als „keine Gebäudereinigung“ eingestuft: {', '.join(n for n in alle if v[n]['rein'] == 'nein') or '–'}.", "",
        "### Abweichungen der Liste vom Vergleichswert", "",
        "| Nr | Typ | Herkunft (Liste) | Liste GL | Vergleichswert GL | Leser A | Leser B | Liste Höchstende | Vergleichswert Höchstende |",
        "|---|---|---|---|---|---|---|---|---|"]
    for n in alle:
        if not ok1[n] or not ok2[n]:
            k = key[n]
            out.append(f"| {n} | {k['typ']} | {k['gl_herkunft']} | {k['gl_ende']}{'' if ok1[n] else ' ✗'} | {v[n]['gl']} | {v[n]['ga']} | {v[n]['gb']} | "
                       f"{k['hoechstende'] or k['hoechstende_herkunft']}{'' if ok2[n] else ' ✗'} | {v[n]['h']} |")
    out += ["", f"### Dreiervergleich mit dem Prüfer der Iteration 7 (L1–L{MAX_Y}, Typ Y)", "",
            "| Nr | Liste GL | Vergleichswert GL | Prüfer GL (Iteration 7) | Liste = Vergleich | Prüfer = Vergleich |", "|---|---|---|---|---|---|"]
    y50 = [n for n in Y if int(n[1:]) <= MAX_Y]
    pr_ok = {n: ok_gl(norm(key[n]["gl_p"]), v[n]["gl"]) for n in y50}
    for n in y50:
        if not key[n]["ok1"] or not ok1[n] or not pr_ok[n]:
            out.append(f"| {n} | {key[n]['gl_ende']} | {v[n]['gl']} | {key[n]['gl_p']} | {'ja' if ok1[n] else 'nein'} | {'ja' if pr_ok[n] else 'nein'} |")
    out += ["", f"Liste = Vergleichswert bei {sum(ok1[n] for n in y50)}/{len(y50)}, Prüfer = Vergleichswert bei {sum(pr_ok.values())}/{len(y50)}, "
            f"Liste = Prüfer (Y1 der Iteration 7) bei {sum(key[n]['ok1'] for n in y50)}/{len(y50)}. Nur Lose mit mindestens einer Abweichung sind aufgeführt.", "",
            "### Kontroll-Lose 143100-2026 (Entwicklungsdaten, zählen nicht)", "",
            "| Nr | Los | Liste GL | Liste Höchstende | Vergleichswert GL | Vergleichswert Höchstende |", "|---|---|---|---|---|---|"]
    with OBERPFALZ.open(encoding="utf-8-sig") as f:
        op = {r["los"]: r for r in csv.DictReader(f, delimiter=";") if r["notice"] == "143100-2026"}
    for n, los in KONTROLLE.items():
        out.append(f"| {n} | {los} | {op[los]['gl_ende']} | {op[los]['hoechstende']} | {v[n]['gl']} | {v[n]['h']} |")
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Z0 {len(einig)}/95, Z1 {sum(ok1[n] for n in Y)}/80, Z2 {sum(ok1[n] for n in R)}/15, Z3 {sum(ok2[n] for n in Y)}/80 | {sum(ok2[n] for n in yb)}/{len(yb)}, Z4 {k4}/{N_Z4}")


if __name__ == "__main__":
    main()
