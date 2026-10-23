"""Berechnet die Kriterien K4 und K5 aus Iteration 2 (siehe docs/iterationen.md).

Eingabe: Zuschläge mit CPV 909 seit Oktober 2016 aus ted_download.py
    (--form-type result --cpv 909 --cpv-field classification-cpv --from 20161001 --to 20261022).
Die Tabelle entsteht mit build_table() aus analyze_completeness.py, also mit denselben Definitionen wie in Iteration 1.

- Gegenprobe: Das Fenster aus Iteration 1 (22.07.–21.10.2026) muss 440 Notices und 356 mit bestimmbarem Ende ergeben.
- K4: Anteil „Laufzeitende bestimmbar“ für Zuschläge vom 01.04.–30.06.2025, mit Wilson-95-%-Intervall.
- K5: eForms-Zuschläge (25.10.2023–22.10.2026) mit bestimmbarem Laufzeitende <= Stichtag 23.10.2026.

Nische = Haupt-CPV beginnt mit 909 (cpv_group aus build_table). Nur eForms-Notices (Haupt-CPV vorhanden), denn vor eForms
liefert die API weder Haupt-CPV noch Laufzeit.

Ergebnis: reports/kennzahlen_iteration2.md und data/processed/k5_vertraege.csv

Aufruf:
    .venv\\Scripts\\python src/kennzahlen_iteration2.py
"""

import argparse
import math
import sys
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from analyze_completeness import (
    MAX_PLAUSIBLE_MONTHS, PROCESSED_DIR, RAW_SEARCH_DIR, REPORT_DIR, build_table, load_notices, num, pct,
)

DEFAULT_RUN = "DEU_result_cpv909_20161001_20261022"
EFORMS_START = "2023-10-25"
STICHTAG = date(2026, 10, 23)  # K5: Laufzeitende <= Stichtag gilt als abgelaufen

ITERATION1_WINDOW = ("2026-07-22", "2026-10-21")
ITERATION1_EXPECTED = (440, 356)  # reports/datenqualitaet_DEU_20260722_20261021.md §5
K4_WINDOW = ("2025-04-01", "2025-06-30")
K5_WINDOW = (EFORMS_START, "2026-10-22")
DAYS_PER_MONTH = 30.44  # wie months_between() in analyze_completeness.py


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson-Konfidenzintervall für einen Anteil (wie in reports/evaluation_iteration1.md)."""
    if n == 0:
        return (math.nan, math.nan)
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (centre - half, centre + half)


def niche(df: pd.DataFrame, window: tuple[str, str]) -> pd.DataFrame:
    """eForms-Notices mit Haupt-CPV 909 im Veröffentlichungsfenster."""
    mask = (
        df["filled:main-classification-proc"]
        & (df["cpv_group"] == "909")
        & (df["publication_date"] >= window[0])
        & (df["publication_date"] <= window[1])
    )
    return df[mask].copy()


def end_date(row) -> tuple[date | None, str]:
    """Laufzeitende des ersten Loses und seine Herkunft.

    Enddatum (BT-537) direkt, sonst Beginn (BT-536) + Dauer (BT-36). Laufzeiten <= 0 oder > 240 Monate werden verworfen,
    wie in Iteration 1.
    """
    if row["end_date_lot1"]:
        if row["duration_dates_implausible"]:
            return None, "verworfen: Beginn/Ende unplausibel"
        try:
            return date.fromisoformat(row["end_date_lot1"]), "Enddatum"
        except ValueError:
            return None, "verworfen: Enddatum ungültig"
    months = row["duration_months_lot1"]
    if row["start_date_lot1"] and pd.notna(months):
        if not 0 < months <= MAX_PLAUSIBLE_MONTHS:
            return None, "verworfen: Dauer unplausibel"
        try:
            start = date.fromisoformat(row["start_date_lot1"])
        except ValueError:
            return None, "verworfen: Beginn ungültig"
        return start + timedelta(days=round(months * DAYS_PER_MONTH)), "Beginn + Dauer"
    return None, "nicht bestimmbar"


def quote_line(name: str, sub: pd.DataFrame) -> tuple[str, int, int, tuple[float, float]]:
    n = len(sub)
    k = int(sub["end_determinable"].sum())
    lo, hi = wilson(k, n)
    ci = f"{lo * 100:.1f}–{hi * 100:.1f} %".replace(".", ",")
    return f"| {name} | {num(n)} | {num(k)} | {pct(k, n)} | {ci} |", n, k, (lo, hi)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run", default=DEFAULT_RUN, help="Unterordner in data/raw/ted_search")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # Windows-Konsole: Sonderzeichen im Report

    run_dir = RAW_SEARCH_DIR / args.run
    notices = load_notices(run_dir)
    df = build_table(notices).drop_duplicates("publication_number")
    print(f"{num(len(df))} Notices geladen aus {run_dir.name}")

    out = ["# Kennzahlen Iteration 2: K4 (Replikation) und K5 (Backtest-Basis)", ""]
    out.append(f"Erzeugt mit `src/kennzahlen_iteration2.py` aus `data/raw/ted_search/{run_dir.name}/` "
               f"({num(len(df))} Zuschläge, CPV 909 in der CPV-Liste, DEU). Definitionen aus `build_table()` "
               "in `src/analyze_completeness.py` (Iteration 1). Nische: Haupt-CPV 909…, nur eForms-Notices.")
    out.append("")

    # Gegenprobe und K4
    out.append("## 1. Laufzeitende bestimmbar (Gegenprobe und K4)\n")
    out.append("„Bestimmbar“: Enddatum (BT-537) vorhanden oder Beginn (BT-536) und Dauer (BT-36) vorhanden, erstes Los bzw. "
               "mindestens ein Los wie in Iteration 1. Intervall: Wilson 95 %.\n")
    out.append("| Fenster | Notices | bestimmbar | Anteil | 95-%-KI |")
    out.append("|---|---|---|---|---|")
    line, n1, k1, _ = quote_line(f"Gegenprobe Iteration 1 ({ITERATION1_WINDOW[0]} bis {ITERATION1_WINDOW[1]})",
                                 niche(df, ITERATION1_WINDOW))
    out.append(line)
    line, n4, k4, (lo4, _) = quote_line(f"**K4** ({K4_WINDOW[0]} bis {K4_WINDOW[1]})", niche(df, K4_WINDOW))
    out.append(line)
    check_ok = (n1, k1) == ITERATION1_EXPECTED
    out.append("")
    out.append(f"- Gegenprobe: erwartet {ITERATION1_EXPECTED[0]} / {ITERATION1_EXPECTED[1]}, erhalten {n1} / {k1} → "
               + ("**stimmt überein**." if check_ok else "**weicht ab, K4/K5 nicht verwenden, bevor das geklärt ist.**"))
    k4_ok = n4 > 0 and k4 / n4 >= 0.80 and lo4 >= 0.75
    out.append(f"- K4-Schwelle (Punktwert ≥ 80 % und KI-Untergrenze ≥ 75 %): **{'erfüllt' if k4_ok else 'nicht erfüllt'}**.")

    out.append("\n### Ergänzend: Quote je Veröffentlichungsjahr (nicht Teil von K4, nachträglich ausgewertet)\n")
    out.append("| Fenster | Notices | bestimmbar | Anteil | 95-%-KI |")
    out.append("|---|---|---|---|---|")
    for label, window in [("2023 (ab 25.10.)", (EFORMS_START, "2023-12-31")), ("2024", ("2024-01-01", "2024-12-31")),
                          ("2025", ("2025-01-01", "2025-12-31")), ("2026 (bis 22.10.)", ("2026-01-01", K5_WINDOW[1]))]:
        out.append(quote_line(label, niche(df, window))[0])

    # K5
    k5 = niche(df, K5_WINDOW)
    ends = k5.apply(end_date, axis=1, result_type="expand")
    # pandas macht beim Aufteilen aus None ein NaN, daher auf den Typ prüfen
    k5["end_date"] = ends[0].apply(lambda d: d if isinstance(d, date) else None)
    k5["end_source"] = ends[1]
    k5["expired"] = k5["end_date"].apply(lambda d: d is not None and d <= STICHTAG)
    k5["end_before_publication"] = k5.apply(
        lambda r: r["end_date"] is not None and r["end_date"] < date.fromisoformat(r["publication_date"]), axis=1)
    expired = k5[k5["expired"]]

    out.append(f"\n## 2. K5: abgelaufene eForms-Verträge (Stichtag {STICHTAG.isoformat()})\n")
    out.append(f"eForms-Zuschläge mit Haupt-CPV 909, veröffentlicht {K5_WINDOW[0]} bis {K5_WINDOW[1]}: **{num(len(k5))}**.\n")
    src = k5["end_source"].value_counts().rename_axis("Herkunft Laufzeitende").reset_index(name="Notices")
    out.append(src.to_markdown(index=False))
    out.append("")
    n_exp = len(expired)
    n_exp_after_pub = int((expired["end_before_publication"] == False).sum())  # noqa: E712
    out.append(f"- Laufzeitende ≤ {STICHTAG.isoformat()}: **{num(n_exp)}** → K5-Schwelle (≥ 100): "
               f"**{'erfüllt' if n_exp >= 100 else 'nicht erfüllt'}**.")
    out.append(f"- Davon endet bei {num(n_exp - n_exp_after_pub)} der Vertrag schon **vor** der Veröffentlichung des Zuschlags "
               f"(verspätete Bekanntmachung oder Datenfehler). Ohne diese Fälle: {num(n_exp_after_pub)}.")

    out.append("\n### Verteilung der Laufzeitenden (bestimmbare Fälle, Jahr des Endes)\n")
    years = k5[k5["end_date"].notna()]["end_date"].apply(lambda d: d.year).value_counts().sort_index()
    out.append(years.rename_axis("Jahr Laufzeitende").reset_index(name="Verträge").to_markdown(index=False))

    out.append("\n### Abgelaufene Verträge nach Veröffentlichungsjahr des Zuschlags\n")
    by_pub = expired["publication_date"].str[:4].value_counts().sort_index()
    out.append(by_pub.rename_axis("Veröffentlichung").reset_index(name="abgelaufen").to_markdown(index=False))

    out.append("\n### Laufzeit der abgelaufenen Verträge (Monate, aus Beginn/Ende, wo vorhanden)\n")
    d = expired["duration_dates_months_lot1"].dropna()
    if len(d):
        out.append(f"n = {len(d)}, Median {d.median():.0f}, Quartile {d.quantile(.25):.0f} / {d.quantile(.75):.0f}. "
                   f"Zum Vergleich alle K5-Notices: Median "
                   f"{k5['duration_dates_months_lot1'].dropna().median():.0f} Monate.")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = PROCESSED_DIR / "k5_vertraege.csv"
    k5[["publication_number", "publication_date", "buyer_name", "main_cpv", "start_date_lot1", "end_date_lot1",
        "duration_months_lot1", "renewal_max", "end_date", "end_source", "expired", "end_before_publication"]].to_csv(
        csv_path, index=False, encoding="utf-8-sig")

    report_path = REPORT_DIR / "kennzahlen_iteration2.md"
    report_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))
    print(f"\nReport: {report_path}\nCSV:    {csv_path}")
    if not check_ok:
        sys.exit("WARNUNG: Gegenprobe weicht von Iteration 1 ab.")


if __name__ == "__main__":
    main()
