# Kennzahlen Iteration 2: K4 (Replikation) und K5 (Backtest-Basis)

Erzeugt mit `src/kennzahlen_iteration2.py` aus `data/raw/ted_search/DEU_result_cpv909_20161001_20261022/` (15.361 Zuschläge, CPV 909 in der CPV-Liste, DEU). Definitionen aus `build_table()` in `src/analyze_completeness.py` (Iteration 1). Nische: Haupt-CPV 909…, nur eForms-Notices.

## 1. Laufzeitende bestimmbar (Gegenprobe und K4)

„Bestimmbar“: Enddatum (BT-537) vorhanden oder Beginn (BT-536) und Dauer (BT-36) vorhanden, erstes Los bzw. mindestens ein Los wie in Iteration 1. Intervall: Wilson 95 %.

| Fenster | Notices | bestimmbar | Anteil | 95-%-KI |
|---|---|---|---|---|
| Gegenprobe Iteration 1 (2026-07-22 bis 2026-10-21) | 440 | 356 | 80,9 % | 77,0–84,3 % |
| **K4** (2025-04-01 bis 2025-06-30) | 390 | 320 | 82,1 % | 77,9–85,5 % |

- Gegenprobe: erwartet 440 / 356, erhalten 440 / 356 → **stimmt überein**.
- K4-Schwelle (Punktwert ≥ 80 % und KI-Untergrenze ≥ 75 %): **erfüllt**.

### Ergänzend: Quote je Veröffentlichungsjahr (nicht Teil von K4, nachträglich ausgewertet)

| Fenster | Notices | bestimmbar | Anteil | 95-%-KI |
|---|---|---|---|---|
| 2023 (ab 25.10.) | 239 | 169 | 70,7 % | 64,7–76,1 % |
| 2024 | 1.623 | 1.137 | 70,1 % | 67,8–72,2 % |
| 2025 | 1.619 | 1.291 | 79,7 % | 77,7–81,6 % |
| 2026 (bis 22.10.) | 1.424 | 1.175 | 82,5 % | 80,5–84,4 % |

## 2. K5: abgelaufene eForms-Verträge (Stichtag 2026-10-23)

eForms-Zuschläge mit Haupt-CPV 909, veröffentlicht 2023-10-25 bis 2026-10-22: **4.905**.

| Herkunft Laufzeitende              |   Notices |
|:-----------------------------------|----------:|
| Enddatum                           |      3716 |
| nicht bestimmbar                   |      1134 |
| Beginn + Dauer                     |        48 |
| verworfen: Beginn/Ende unplausibel |         7 |

- Laufzeitende ≤ 2026-10-23: **629** → K5-Schwelle (≥ 100): **erfüllt**.
- Davon endet bei 3 der Vertrag schon **vor** der Veröffentlichung des Zuschlags (verspätete Bekanntmachung oder Datenfehler). Ohne diese Fälle: 626.

### Verteilung der Laufzeitenden (bestimmbare Fälle, Jahr des Endes)

|   Jahr Laufzeitende |   Verträge |
|--------------------:|-----------:|
|                2024 |         54 |
|                2025 |        266 |
|                2026 |        475 |
|                2027 |        718 |
|                2028 |        828 |
|                2029 |        613 |
|                2030 |        536 |
|                2031 |        170 |
|                2032 |         71 |
|                2033 |         25 |
|                2034 |          2 |
|                2036 |          1 |
|                2046 |          5 |

### Abgelaufene Verträge nach Veröffentlichungsjahr des Zuschlags

|   Veröffentlichung |   abgelaufen |
|-------------------:|-------------:|
|               2023 |           63 |
|               2024 |          410 |
|               2025 |          141 |
|               2026 |           15 |

### Laufzeit der abgelaufenen Verträge (Monate, aus Beginn/Ende, wo vorhanden)

n = 622, Median 12, Quartile 12 / 24. Zum Vergleich alle K5-Notices: Median 36 Monate.
