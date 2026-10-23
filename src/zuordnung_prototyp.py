"""Zuordnungs-Prototyp (Iteration 2, Schritt 5): Ausschreibung (competition) -> früherer Zuschlag desselben Auftraggebers.

Rückwärtssuche: Für jede Original-Ausschreibung (keine Änderungsbekanntmachung) aus Q2 2026 mit Haupt-CPV 909 wird im
Vorgänger-Pool (alle Zuschläge mit CPV 909 in der CPV-Liste seit Oktober 2016) ein Zuschlag gesucht, der
- denselben normalisierten Auftraggebernamen ODER dieselbe normalisierte Auftraggeber-Kennung (nur eForms) hat und
- vor der Ausschreibung veröffentlicht wurde.

Auswahl bei mehreren Kandidaten (geändert am 2026-10-23, siehe docs/iterationen.md):
    1. eForms-Kandidat, dessen Vertrag 3 Monate vor bis 18 Monate nach der Ausschreibung endet; bei mehreren der mit dem
       ähnlichsten Titel (Jaccard der Wörter), dann der jüngste
    2. sonst der jüngste Kandidat vor eForms (diese haben in der API weder Titel noch Laufzeit)
    3. sonst ähnlichster Titel, dann jüngster
Die Vorlaufzeiten der gewählten Paare sind durch Stufe 1 vorgeprägt und nur beschreibend.
Einfach vor komplex: keine unscharfen Namensvergleiche.

Ergebnis:
    data/processed/zuordnung_q2_2026.csv   eine Zeile pro Ausschreibung mit gewähltem Kandidaten
    reports/zuordnung_iteration2.md        Kennzahlen K1, K3 (vorläufig), Vorlaufzeiten
    reports/k2_pruefliste.md               Stichprobe für die manuelle Prüfung (wird nur angelegt, nie überschrieben)

Aufruf:
    .venv\\Scripts\\python src/zuordnung_prototyp.py
"""

import argparse
import random
import re
import sys
from datetime import date
from pathlib import Path

import pandas as pd

from analyze_completeness import PROCESSED_DIR, RAW_SEARCH_DIR, REPORT_DIR, build_table, flatten, load_notices, num, pct
from kennzahlen_iteration2 import DAYS_PER_MONTH, end_date, wilson

COMP_RUN = "DEU_competition_cpv909main_20260401_20260630"
POOL_RUN = "DEU_result_cpv909_20161001_20261022"
SEED = 20261023
END_WINDOW_MONTHS = (-3, 18)  # Stufe 1: Vertragsende relativ zur Ausschreibung
K2_SAMPLE = 30
NO_MATCH_SAMPLE = 15
TED_URL = "https://ted.europa.eu/de/notice/-/detail/{}"

UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
ID_PREFIXES = re.compile(r"^(UST-?ID(NR)?\.?|LEITWEG-?ID|USTIDNR\.?)[:\s]*", re.IGNORECASE)
STOPWORDS = {"und", "der", "die", "das", "des", "fuer", "von", "im", "in", "mit", "zur", "zum", "dem", "den", "auf", "an", "am"}


def norm_name(text: str) -> str:
    text = str(text).lower().translate(UMLAUTS)
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def norm_id(text: str) -> str | None:
    """Kennung vereinheitlichen; None für Werte, die nicht als Kennung taugen (zu kurz, Telefonnummer)."""
    raw = str(text).strip()
    if "tel" in raw.lower():
        return None
    value = re.sub(r"[^0-9A-Z-]", "", ID_PREFIXES.sub("", raw).upper())
    return value if len(re.sub(r"[^0-9A-Z]", "", value)) >= 8 else None


def buyer_names(notice: dict) -> set[str]:
    """Alle Auftraggebernamen, bevorzugt deutsch; sonst alle Sprachen."""
    names = notice.get("buyer-name") or {}
    values = names.get("deu") if isinstance(names, dict) and names.get("deu") else flatten(names)
    return {n for n in (norm_name(v) for v in values) if n}


def buyer_ids(notice: dict) -> set[str]:
    return {i for i in (norm_id(v) for v in flatten(notice.get("buyer-identifier"))) if i}


def title_tokens(notice: dict) -> set[str]:
    title = notice.get("title-proc") or {}
    text = title.get("deu") if isinstance(title, dict) and title.get("deu") else " ".join(map(str, flatten(title)))
    return {t for t in norm_name(text or "").split() if len(t) > 2 and t not in STOPWORDS}


def jaccard(a: set, b: set) -> float | None:
    return len(a & b) / len(a | b) if a and b else None


def first_title(notice: dict) -> str:
    title = notice.get("title-proc") or {}
    if isinstance(title, dict) and title.get("deu"):
        return str(title["deu"])
    vals = flatten(title)
    return str(vals[0]) if vals else ""


def first_buyer(notice: dict) -> str:
    names = notice.get("buyer-name") or {}
    vals = names.get("deu") if isinstance(names, dict) and names.get("deu") else flatten(names)
    return str(vals[0]) if vals else ""


def months_until(end: date | None, start: str) -> float | None:
    return (end - date.fromisoformat(start)).days / DAYS_PER_MONTH if end else None


def pick(cands: list[dict], c_date: str, c_title: set[str], pool_end: dict) -> tuple[dict, str]:
    """Wählt den wahrscheinlichsten Vorgänger und nennt die Stufe der Auswahlregel."""
    def by_title(n):
        sim = jaccard(c_title, title_tokens(n))
        return (sim if sim is not None else -1, str(n["publication-date"])[:10])

    def recent(n):
        return str(n["publication-date"])[:10]

    lo, hi = END_WINDOW_MONTHS
    timely = [n for n in cands if n.get("main-classification-proc")
              and (m := months_until(pool_end.get(n["publication-number"]), c_date)) is not None and lo <= m <= hi]
    if timely:
        return max(timely, key=by_title), "1 Ende passt"
    old = [n for n in cands if not n.get("main-classification-proc")]
    if old:
        return max(old, key=recent), "2 vor eForms"
    return max(cands, key=by_title), "3 sonstige"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    comps = [n for n in load_notices(RAW_SEARCH_DIR / COMP_RUN) if not n.get("change-notice-version-identifier")]
    pool = list({n["publication-number"]: n for n in load_notices(RAW_SEARCH_DIR / POOL_RUN)}.values())
    print(f"{num(len(comps))} Original-Ausschreibungen, {num(len(pool))} Zuschläge im Pool")

    # Laufzeitende der Pool-Notices mit derselben Logik wie K5 (nur eForms liefert Laufzeiten)
    table = build_table(pool).set_index("publication_number")
    pool_end = {pn: end_date(row)[0] for pn, row in table.iterrows()}

    by_name: dict[str, list[dict]] = {}
    by_id: dict[str, list[dict]] = {}
    for n in pool:
        for key in buyer_names(n):
            by_name.setdefault(key, []).append(n)
        for key in buyer_ids(n):
            by_id.setdefault(key, []).append(n)

    rows = []
    for c in comps:
        c_date = str(c["publication-date"])[:10]
        c_names, c_ids, c_title = buyer_names(c), buyer_ids(c), title_tokens(c)
        via_name = {n["publication-number"]: n for k in c_names for n in by_name.get(k, [])}
        via_id = {n["publication-number"]: n for k in c_ids for n in by_id.get(k, [])}
        cands = {
            pn: n for pn, n in {**via_name, **via_id}.items()
            if str(n["publication-date"])[:10] < c_date and n.get("procedure-identifier") != c.get("procedure-identifier")
        }
        name_hits = [pn for pn in cands if pn in via_name]
        best, rule = pick(list(cands.values()), c_date, c_title, pool_end) if cands else (None, "")
        row = {
            "comp_publication_number": c["publication-number"],
            "comp_publication_date": c_date,
            "comp_buyer": first_buyer(c),
            "comp_title": first_title(c),
            "candidates": len(cands),
            "candidates_via_name": len(name_hits),
            "matched": bool(cands),
            "matched_via_name": bool(name_hits),
        }
        if best is not None:
            pn = best["publication-number"]
            b_end = pool_end.get(pn)
            row.update({
                "pred_publication_number": pn,
                "pred_publication_date": str(best["publication-date"])[:10],
                "pred_buyer": first_buyer(best),
                "pred_title": first_title(best),
                "pred_eforms": bool(best.get("main-classification-proc")),
                "pred_main_cpv": table.at[pn, "main_cpv"],
                "pred_title_similarity": jaccard(c_title, title_tokens(best)),
                "pred_via": "Name" if pn in via_name else "Kennung",
                "pred_rule": rule,
                "pred_end_date": b_end.isoformat() if b_end else "",
                # Vorlauf: Monate zwischen Ausschreibung und Vertragsende des Vorgängers (positiv = Ausschreibung vor Ende)
                "lead_months": round(months_until(b_end, c_date), 1) if b_end else None,
            })
        rows.append(row)
    df = pd.DataFrame(rows)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = PROCESSED_DIR / "zuordnung_q2_2026.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    n = len(df)
    k_any, k_name = int(df["matched"].sum()), int(df["matched_via_name"].sum())
    m = df[df["matched"]]
    out = ["# Zuordnung Ausschreibung → früherer Zuschlag (Iteration 2, Schritt 5)", ""]
    out.append(f"Erzeugt mit `src/zuordnung_prototyp.py`. Ausschreibungen: `data/raw/ted_search/{COMP_RUN}/` "
               f"(nur Originale, ohne Änderungsbekanntmachungen). Pool: `data/raw/ted_search/{POOL_RUN}/`.\n")
    out.append("Regel: gleicher normalisierter Auftraggebername (Kleinschreibung, Umlaute umgeschrieben, Satzzeichen entfernt) "
               "oder gleiche normalisierte Auftraggeber-Kennung (ohne Präfix, ≥ 8 Zeichen, keine Telefonnummer); Zuschlag vor "
               "der Ausschreibung veröffentlicht. Auswahl unter mehreren Kandidaten: (1) eForms-Kandidat mit Vertragsende "
               f"{END_WINDOW_MONTHS[0]} bis +{END_WINDOW_MONTHS[1]} Monate relativ zur Ausschreibung (ähnlichster Titel), "
               "(2) sonst jüngster Kandidat vor eForms, (3) sonst ähnlichster Titel bzw. jüngster.\n")

    out.append("## K1: Anteil der Ausschreibungen mit Vorgänger-Kandidat\n")
    out.append("| Variante | Treffer | von | Anteil | 95-%-KI (Wilson) |")
    out.append("|---|---|---|---|---|")
    for label, k in [("**Name oder Kennung (K1)**", k_any), ("nur Name", k_name)]:
        lo, hi = wilson(k, n)
        out.append(f"| {label} | {num(k)} | {num(n)} | {pct(k, n)} | "
                   + f"{lo * 100:.1f}–{hi * 100:.1f} %".replace(".", ",") + " |")
    out.append(f"\nK1-Schwelle ≥ 50 %: **{'erfüllt' if k_any / n >= 0.5 else 'nicht erfüllt'}** (vor manueller Prüfung, siehe K2).")

    out.append("\n## Kandidaten je Ausschreibung (nur Treffer)\n")
    bins = pd.cut(m["candidates"], [0, 1, 2, 5, 10, 50, 10_000], labels=["1", "2", "3–5", "6–10", "11–50", "> 50"])
    out.append(bins.value_counts().sort_index().rename_axis("Kandidaten").reset_index(name="Ausschreibungen").to_markdown(index=False))

    out.append("\n## Gewählter Kandidat\n")
    out.append(f"- über Name: {num((m['pred_via'] == 'Name').sum())}, nur über Kennung: {num((m['pred_via'] == 'Kennung').sum())}")
    out.append("- Stufe der Auswahlregel: "
               + ", ".join(f"{k}: {num(v)}" for k, v in m["pred_rule"].value_counts().sort_index().items()))
    k3 = int(m["pred_eforms"].sum())
    out.append(f"- **K3 (vorläufig, vor Prüfung):** Vorgänger im eForms-Format {num(k3)} von {num(len(m))} = {pct(k3, len(m))}")
    out.append(f"- mit Titelähnlichkeit (beide Titel vorhanden): {num(m['pred_title_similarity'].notna().sum())}, "
               f"davon Ähnlichkeit > 0: {num((m['pred_title_similarity'] > 0).sum())}")
    years = m["pred_publication_date"].str[:4].value_counts().sort_index()
    out.append("\nVeröffentlichungsjahr des gewählten Vorgängers:\n")
    out.append(years.rename_axis("Jahr").reset_index(name="Vorgänger").to_markdown(index=False))

    out.append("\n## Vorlauf (explorativ, A8)\n")
    lead = m["lead_months"].dropna()
    out.append("Vorlauf = Vertragsende des Vorgängers minus Veröffentlichung der Ausschreibung, in Monaten (positiv = Ausschreibung "
               "vor Vertragsende). Nur Vorgänger mit bestimmbarem Ende (praktisch nur eForms). **Ungeprüfte Paare**: "
               "Fehlzuordnungen verzerren die Verteilung. **Zirkulär für Stufe 1:** Dort wurde nach dem Vorlauf-Fenster "
               "ausgewählt, die Verteilung ist also nur beschreibend und kein Test von A8.\n")
    if len(lead):
        q = lead.quantile([0.1, 0.25, 0.5, 0.75, 0.9])
        out.append(f"n = {len(lead)}; Median {q[0.5]:.1f}; Quartile {q[0.25]:.1f} / {q[0.75]:.1f}; "
                   f"10.–90. Perzentil {q[0.1]:.1f} / {q[0.9]:.1f}.")
        out.append(f"Anteil Ausschreibung vor Vertragsende: {pct((lead > 0).sum(), len(lead))}; "
                   f"0–12 Monate vor Ende: {pct(((lead > 0) & (lead <= 12)).sum(), len(lead))}.")

    report_path = REPORT_DIR / "zuordnung_iteration2.md"
    report_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))
    print(f"\nReport: {report_path}\nCSV:    {csv_path}")

    write_checklist(df)


def write_checklist(df: pd.DataFrame) -> None:
    """Prüfliste für K2 und für Ausschreibungen ohne Treffer. Wird nur einmal angelegt, damit Prüfnotizen erhalten bleiben."""
    path = REPORT_DIR / "k2_pruefliste.md"
    if path.exists():
        print(f"Prüfliste existiert bereits, nicht überschrieben: {path}")
        return
    rng = random.Random(SEED)
    matched = df[df["matched"]].sort_values("comp_publication_number")
    unmatched = df[~df["matched"]].sort_values("comp_publication_number")
    sample = matched.iloc[sorted(rng.sample(range(len(matched)), min(K2_SAMPLE, len(matched))))]
    sample_none = unmatched.iloc[sorted(rng.sample(range(len(unmatched)), min(NO_MATCH_SAMPLE, len(unmatched))))]

    out = ["# Prüfliste K2 (Iteration 2, Schritt 6)", ""]
    out.append(f"Angelegt von `src/zuordnung_prototyp.py`, Zufallsauswahl mit Seed {SEED}. Diese Datei wird nicht überschrieben.\n")
    out.append("**Frage je Paar:** Ist plausibel dieselbe Leistung gemeint (gleiches Objekt bzw. gleiche Liegenschaften, ähnlicher "
               "Umfang), sodass die Ausschreibung die Neuausschreibung des Vorgängervertrags ist?\n")
    out.append("Urteil: **ja** / **nein** / **unklar**. K2 = ja / (ja + nein + unklar); unklar zählt als nein. Schwelle ≥ 80 %.\n")
    out.append("## A. 30 zufällige Treffer\n")
    for i, (_, r) in enumerate(sample.iterrows(), 1):
        out.append(f"### A{i}")
        out.append(f"- Ausschreibung: [{r.comp_publication_number}]({TED_URL.format(r.comp_publication_number)}) "
                   f"({r.comp_publication_date}) – {r.comp_buyer} – „{r.comp_title}“")
        out.append(f"- Vorgänger: [{r.pred_publication_number}]({TED_URL.format(r.pred_publication_number)}) "
                   f"({r.pred_publication_date}, {'eForms' if r.pred_eforms else 'vor eForms'}, über {r.pred_via}, "
                   f"Auswahlstufe {r.pred_rule}, {int(r.candidates)} Kandidaten) – {r.pred_buyer} – „{r.pred_title or '(kein Titel in der API)'}“")
        out.append(f"- Vertragsende Vorgänger: {r.pred_end_date or 'unbekannt'}")
        out.append("- Urteil: ")
        out.append("- Begründung: ")
        out.append("")
    out.append("## B. 15 zufällige Ausschreibungen ohne Treffer\n")
    out.append("Frage: Warum kein Vorgänger? (z. B. erstmalige Vergabe, Name abweichend, Vorgänger unter Schwellenwert, "
               "anderer CPV, Vorgänger vor 2016)\n")
    for i, (_, r) in enumerate(sample_none.iterrows(), 1):
        out.append(f"### B{i}")
        out.append(f"- Ausschreibung: [{r.comp_publication_number}]({TED_URL.format(r.comp_publication_number)}) "
                   f"({r.comp_publication_date}) – {r.comp_buyer} – „{r.comp_title}“")
        out.append("- Vermuteter Grund: ")
        out.append("")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Prüfliste: {path}")


if __name__ == "__main__":
    main()
