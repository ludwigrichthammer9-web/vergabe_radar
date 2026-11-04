"""Iteration 5, nachträgliche Analysen zum Backtest (Auflagen des Evaluators, reports/evaluation_iteration5.md). Explorativ, ohne Schwelle.

(1) Paare mit langer Lücke: Liegt die Veröffentlichung mehr als 24 Monate nach der R1-Prognose, kann ein Zwischenvertrag desselben
    Auftraggebers dazwischen liegen (Vorgänger nicht direkt). Je Paar werden Zuschläge und Ausschreibungen (CPV 909, DEU) desselben
    Auftraggebers gezählt, die nach dem Vorgänger und vor dem Testfall veröffentlicht wurden. Das zeigt nur, ob ein Zwischenvertrag
    **möglich** ist (gleicher Auftraggeber, anderes Objekt ist häufig), nicht, dass er das Objekt betrifft.
(2) Auswertung nach Auftraggeber: Trefferquote je Auftraggeber-Cluster, und eine Variante mit höchstens einem Paar je Auftraggeber.

Die Regeln R0/R1 und die Paare bleiben unverändert (src/model/baseline.py).

Aufruf:  .venv\\Scripts\\python src/model/analyse_backtest.py      Ausgabe: reports/backtest_analysen_iteration5.md
"""

import csv
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyze_completeness import RAW_SEARCH_DIR, load_notices  # noqa: E402
from baseline import lade, pct  # noqa: E402

POOLS = ("DEU_result_cpv909_20161001_20260930", "DEU_competition_cpv909_20161001_20260930",
         "DEU_competition_cpv909_20231025_20260930_lostext")
REPORT = ROOT / "reports" / "backtest_analysen_iteration5.md"
LUECKE = 24  # Monate


def name(n: dict) -> str:
    b = n.get("buyer-name")
    if isinstance(b, dict):
        v = b.get("deu") or next(iter(b.values()), [])
        b = v[0] if isinstance(v, list) and v else (v if isinstance(v, str) else "")
    elif isinstance(b, list):
        b = b[0] if b else ""
    return re.sub(r"[^a-zäöüß0-9 ]", "", str(b or "").lower()).strip()


def schluessel(n: str) -> str:
    return " ".join(n.split()[:4])


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rows = lade()
    notices, by_buyer = {}, defaultdict(list)
    for pool in POOLS:
        for n in load_notices(RAW_SEARCH_DIR / pool):
            pn = n["publication-number"]
            if pn in notices:
                continue
            notices[pn] = n
            by_buyer[schluessel(name(n))].append(n)
    for r in rows:
        t = notices.get(r["testfall"])
        v = notices.get(r["vorgaenger"])
        r["buyer"] = schluessel(name(t)) if t else "?"
        r["vorg_datum"] = str(v.get("publication-date", ""))[:10] if v else ""
    out = ["# Nachträgliche Analysen zum Backtest (Iteration 5)", "",
           "_Erzeugt mit `src/model/analyse_backtest.py`. Explorativ und nach dem Ergebnis ergänzt (Auflage des Evaluators); keine Schwelle, "
           "keine Änderung an R0/R1 oder den Paaren._", "", "## 1. Paare mit langer Lücke", ""]
    spaet = sorted([r for r in rows if r["d1"] > LUECKE], key=lambda r: -r["d1"])
    frueh = [r for r in rows if r["d1"] < -LUECKE]
    out += [f"- Veröffentlichung **mehr als {LUECKE} Monate nach** der R1-Prognose: **{len(spaet)}** von {len(rows)} Paaren; "
            f"mehr als {LUECKE} Monate **vor** der Prognose: {len(frueh)}.", "",
            "| Paar | Vorgänger | Veröffentl. Vorgänger | Ende GL | Höchstende | Testfall | Veröffentl. Testfall | Abw. R1 (Mon.) | gleicher Auftraggeber dazwischen (Notices) |",
            "|---|---|---|---|---|---|---|---|---|"]
    mit_zwischen = 0
    for r in spaet:
        zw = [n["publication-number"] for n in by_buyer.get(r["buyer"], [])
              if r["vorg_datum"] < str(n.get("publication-date", ""))[:10] < str(r["pub"]) and n["publication-number"] != r["testfall"]]
        mit_zwischen += bool(zw)
        out.append(f"| {r['pid']} | {r['vorgaenger']} | {r['vorg_datum']} | {r['gl']} | {r['h'] or '–'} | {r['testfall']} | {r['pub']} | "
                   f"{r['d1']:+.0f} | {len(zw)} ({', '.join(zw[:4])}{' …' if len(zw) > 4 else ''}) |".replace("+", "+"))
    out += ["", f"- Bei **{mit_zwischen} von {len(spaet)}** Paaren hat derselbe Auftraggeber zwischen Vorgänger und Testfall weitere 909-Bekanntmachungen "
            "veröffentlicht. Das ist bei großen Auftraggebern häufig und belegt keinen Zwischenvertrag für dasselbe Objekt.",
            f"- Trefferquote R1 ohne die {len(spaet)} Paare mit später Lücke: {pct(sum(r['t1'] for r in rows if r['d1'] <= LUECKE), len(rows) - len(spaet))}; "
            f"ohne späte und frühe Lücken: {pct(sum(r['t1'] for r in rows if abs(r['d1']) <= LUECKE), sum(abs(r['d1']) <= LUECKE for r in rows))}.", ""]

    out += ["## 2. Nach Auftraggeber", ""]
    cl = defaultdict(list)
    for r in rows:
        cl[r["buyer"]].append(r)
    gross = sorted(cl.items(), key=lambda kv: -len(kv[1]))
    out += [f"- {len(rows)} Paare, **{len(cl)} Auftraggeber** (Schlüssel: erste vier Wörter des normalisierten Namens; grob).",
            f"- Auftraggeber mit mehr als einem Paar: {sum(len(v) > 1 for v in cl.values())}; Paare davon: {sum(len(v) for v in cl.values() if len(v) > 1)}.", "",
            "| Auftraggeber (Schlüssel) | Paare | R1-Treffer |", "|---|---|---|"]
    for k, v in gross[:12]:
        if len(v) > 1:
            out.append(f"| {k} | {len(v)} | {sum(r['t1'] for r in v)}/{len(v)} |")
    # ein Paar je Auftraggeber: Erwartungswert über alle Wahlen = Mittel der Cluster-Trefferquoten
    mittel = sum(sum(r["t1"] for r in v) / len(v) for v in cl.values()) / len(cl)
    mittel0 = sum(sum(r["t0"] for r in v) / len(v) for v in cl.values()) / len(cl)
    erster = [sorted(v, key=lambda r: r["pid"])[0] for v in cl.values()]
    out += ["", f"- **Jeder Auftraggeber zählt gleich** (Mittel der Cluster-Trefferquoten): R1 **{100 * mittel:.1f} %**, R0 {100 * mittel0:.1f} %.".replace(".", ","),
            f"- Ein Paar je Auftraggeber (alphabetisch erstes Paar je Cluster, n = {len(erster)}): R1 {pct(sum(r['t1'] for r in erster), len(erster))}, "
            f"R0 {pct(sum(r['t0'] for r in erster), len(erster))}.", ""]
    out += ["## Grenzen", "",
            "- Auftraggeber-Schlüssel grob (Schreibvarianten werden nicht zusammengeführt, Zentralen großer Länder führen mehrere Dienststellen unter einem Namen).",
            "- Ein Auftraggeber mit anderem Objekt dazwischen ist kein Beleg für einen Zwischenvertrag; die Handsuche und die Prüfer haben nur Objektidentität beurteilt.",
            "- Beide Analysen sind nachträglich und können das Ergebnis X3 nicht ändern."]
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"späte Lücke: {len(spaet)}, frühe: {len(frueh)}, mit Zwischen-Notices: {mit_zwischen}; Auftraggeber: {len(cl)}; "
          f"R1 je Auftraggeber gleich gewichtet {100 * mittel:.1f}%")


if __name__ == "__main__":
    main()
