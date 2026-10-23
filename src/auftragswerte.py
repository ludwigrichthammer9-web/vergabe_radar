"""Auftragswerte von Gebäudereinigungs-Zuschlägen auf TED (für die Einordnung von Markt und Produktnutzen).

Grundlage: eForms-Zuschläge mit Haupt-CPV 90910/90911/90919, Auftraggeber DEU, veröffentlicht 2024 und 2025 (zwei volle Jahre), aus
data/raw/ted_search/DEU_result_cpv909_20161001_20260930/. Tabelle über build_table() aus analyze_completeness.py.

Wert je Zuschlag: `total-value` (von TED berechnet, siehe Iteration 1), ersatzweise `tender-value` (BT-720). Werte <= 1 € gelten als
Platzhalter und werden nicht verwendet; Werte > 500 Mio. € werden als unplausibel verworfen. Jahreswert = Wert / Laufzeit in Monaten
(aus Beginn/Ende des ersten Loses) × 12, nur wo die Laufzeit bekannt ist.

Ergebnis: reports/auftragswerte_909.md
"""

import sys
from pathlib import Path

import pandas as pd

from analyze_completeness import RAW_SEARCH_DIR, build_table, load_notices

RUN = "DEU_result_cpv909_20161001_20260930"
REPORT = Path(__file__).resolve().parent.parent / "reports" / "auftragswerte_909.md"
MAX_PLAUSIBLE = 500_000_000


def eur(x: float) -> str:
    return f"{x:,.0f} €".replace(",", ".")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    df = build_table(load_notices(RAW_SEARCH_DIR / RUN)).drop_duplicates("publication_number")
    df = df[df["filled:main-classification-proc"] & df["main_cpv"].str[:5].isin(["90910", "90911", "90919"])
            & df["publication_date"].between("2024-01-01", "2025-12-31")].copy()
    value = df["total_value"].where(df["total_value"] > 1, df["tender_value"].where(df["tender_value"] > 1))
    df["value"] = value.where(value <= MAX_PLAUSIBLE)
    v = df["value"].dropna()
    withdur = df.dropna(subset=["value", "duration_dates_months_lot1"])
    withdur = withdur[withdur["duration_dates_months_lot1"] >= 1]
    per_year = withdur["value"] / withdur["duration_dates_months_lot1"] * 12

    q = v.quantile([0.25, 0.5, 0.75, 0.9])
    qy = per_year.quantile([0.25, 0.5, 0.75])
    out = ["# Auftragswerte Gebäudereinigung auf TED (Zuschläge 2024–2025)", "",
           f"Erzeugt mit `src/auftragswerte.py` aus `data/raw/ted_search/{RUN}/`. eForms-Zuschläge, Haupt-CPV 90910/90911/90919, DEU, "
           "veröffentlicht 01.01.2024–31.12.2025.", "",
           "**Wichtig:** `total-value` ist ein von TED berechneter Gesamtwert der Bekanntmachung (Iteration 1), bei Rahmenverträgen ggf. "
           "der Höchstwert. Werte ≤ 1 € sind Platzhalter und wurden entfernt.", "",
           "| Kennzahl | Wert |", "|---|---|",
           f"| Zuschläge | {len(df)} |",
           f"| davon mit plausiblem Wert (> 1 €) | {len(v)} ({len(v) / len(df) * 100:.0f} %) |".replace(".", ",", 1),
           f"| Median Auftragswert (Gesamtlaufzeit) | {eur(q[0.5])} |",
           f"| Quartile (25 % / 75 %) | {eur(q[0.25])} / {eur(q[0.75])} |",
           f"| 90-%-Quantil | {eur(q[0.9])} |",
           f"| Summe der plausiblen Werte (2 Jahre) | {eur(v.sum())} |",
           f"| Jahreswert: Median (n = {len(per_year)}, Laufzeit bekannt) | {eur(qy[0.5])} |",
           f"| Jahreswert: Quartile | {eur(qy[0.25])} / {eur(qy[0.75])} |", "",
           "Lesehilfe: Der Median ist robust gegen einzelne Großaufträge; die Summe wird von wenigen Rahmenverträgen dominiert und ist "
           "nur eine grobe Obergrenze des auf TED sichtbaren Volumens."]
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out[8:17]))


if __name__ == "__main__":
    main()
