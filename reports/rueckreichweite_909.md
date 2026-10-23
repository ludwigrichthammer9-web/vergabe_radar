# Rückreichweite und Basisrate: Gebäudereinigung (CPV 909), Deutschland

Iteration 2, Schritt 2. Erstellt am 2026-10-23.

**Quellen**
- **[C]** Trefferzahlen je Quartal, erzeugt mit [src/ted_counts.py](../src/ted_counts.py). Rohantworten unverändert in
  `data/raw/ted_counts/DEU_909_20261023/` (205 Antworten + `request_meta.json`), Tabelle in `data/processed/counts_DEU_909_quartale.csv`.
- **[P]** Probeabfragen vom 23.10.2026 in `data/raw/ted_probes/20261023/` (Dateiname als Kürzel).
- **[X]** Original-XML in `data/raw/ted_xml/probe_20261023/`.

**Abfragen** (je Quartal, `buyer-country=DEU`, Veröffentlichungsdatum im Quartal, nur `totalNoticeCount`)

| Spalte | Filter | gilt für |
|---|---|---|
| Zuschläge (CPV-Liste) | `form-type=result AND classification-cpv=909*` | alle Jahre (Haupt- oder Zusatz-CPV) |
| Ausschreibungen (CPV-Liste) | `form-type=competition AND classification-cpv=909*` | alle Jahre |
| Vorinformationen (CPV-Liste) | `form-type=planning AND classification-cpv=909*` | alle Jahre |
| Zuschläge (Haupt-CPV) | `form-type=result AND main-classification-proc=909*` | nur eForms |
| Ausschreibungen (Haupt-CPV) | `form-type=competition AND main-classification-proc=909*` | nur eForms |

---

## Fakten

### 1. Rückreichweite der Such-API

- Die ersten Notices stammen aus der Zeit zwischen dem 21. und 28.10.2016. Für 2014, 2015 und die Zeit vom 01.01. bis 20.10.2016
  gibt es 0 Treffer. [P q04–q09, q17]
- Das Quartal 2016-Q4 ist deshalb nur teilweise abgedeckt (etwa 10 Wochen).
- Das Feld Haupt-CPV (`main-classification-proc`) ist bis 2023-Q3 immer 0 und ab 2023-Q4 befüllt (2023-Q4: 239 Zuschläge). [C]
  Das passt zur eForms-Pflicht ab dem 25.10.2023.

### 2. Anzahl je Jahr [C]

| Jahr | Zuschläge (CPV-Liste) | Ausschreibungen (CPV-Liste) | Vorinformationen | Zuschläge (Haupt-CPV) | Ausschreibungen (Haupt-CPV) | Ausschreibungen / Zuschläge (CPV-Liste) |
|---|---|---|---|---|---|---|
| 2016 (ab ca. 21.10.) | 236 | 244 | 14 | – | – | 1,03 |
| 2017 | 1.252 | 1.428 | 56 | – | – | 1,14 |
| 2018 | 1.376 | 1.494 | 59 | – | – | 1,09 |
| 2019 | 1.464 | 1.568 | 56 | – | – | 1,07 |
| 2020 | 1.351 | 1.488 | 45 | – | – | 1,10 |
| 2021 | 1.410 | 1.680 | 35 | – | – | 1,19 |
| 2022 | 1.602 | 1.885 | 36 | – | – | 1,18 |
| 2023 | 1.655 | 2.184 | 39 | 239 (nur Q4) | 374 (nur Q4) | 1,32 |
| 2024 | 1.746 | 2.784 | 35 | 1.623 | 2.578 | 1,59 |
| 2025 | 1.739 | 2.777 | 32 | 1.619 | 2.558 | 1,60 |
| 2026 (bis 22.10.) | 1.530 | 2.561 | 28 | 1.424 | 2.399 | 1,67 |

Quartalswerte: `data/processed/counts_DEU_909_quartale.csv`.

- **Zuschläge im eForms-Format** mit Haupt-CPV 909 (2023-Q4 bis 22.10.2026): 4.905. Daraus wird K5 berechnet (Schritt 4).
- **Zuschläge vor eForms** (CPV-Liste, 2016-Q4 bis 2023-Q3): 9.948. Das ist der Vorgänger-Pool vor eForms für K1.
- **Ausschreibungen mit Haupt-CPV 909 in Q2 2026** (Nenner von K1 vor Bereinigung): 710 Notices.

### 3. Änderungsbekanntmachungen unter den Ausschreibungen [P q18]

Geprüft wurden die ersten 250 von 710 Ausschreibungen (Haupt-CPV 909, Q2 2026), also keine Zufallsstichprobe.
- 40 von 250 (16 %) haben `change-notice-version-identifier`, sind also Änderungen einer früheren Bekanntmachung. Änderungsgründe
  (`change-reason-code`): `cor-buy` 20, `update-add` 13, `cor-pub` 6, `info-release` 1.
- 250 Notices gehören zu 235 verschiedenen `procedure-identifier`. 15 Verfahren erscheinen innerhalb dieser 250 mehrfach.
- Beispiel: 225677-2026 (Original) und 291501-2026 (Änderung, `cor-buy`). Die Änderung verweist über
  `change-notice-version-identifier` = `notice-identifier` des Originals + `-01`.

### 4. Vorinformationen [C]

- 28 bis 59 pro Jahr, seit 2021 höchstens 39. In Q2 2026 sind es 11 mit CPV-Liste bzw. 5 mit Haupt-CPV [P q13].

---

## Interpretation

- **Die Rückreichweite reicht für die Zuordnung.** Knapp 10 Jahre (Ende 2016 bis 2026) entsprechen etwa drei Vertragszyklen bei
  36 Monaten Median-Laufzeit. Ein Vorgänger aus Q2 2026 sollte also in den meisten Fällen im Zeitraum der API liegen, wenn er auf TED
  veröffentlicht wurde. Vor eForms fehlen in der Such-API aber Laufzeit, Haupt-CPV und Auftraggeber-Kennung (siehe
  [02_data_understanding.md](../docs/phasen/02_data_understanding.md)).
- **Die Zahl der Zuschläge ist über die Jahre stabil** (1.250 bis 1.750 pro Jahr) und steigt leicht. Es gibt keinen Bruch beim
  Formatwechsel. Für das Projekt ist das ein gutes Zeichen: Das Zielereignis tritt regelmäßig auf.
- **Mit eForms springt die Zahl der Ausschreibungen.** Pro Zuschlag sind es vorher etwa 1,1, nachher etwa 1,6. Änderungsbekanntmachungen
  erklären vermutlich nur einen Teil: 16 % in der geprüften Teilmenge, die Ausschreibungen steigen aber um etwa 45 %. Weitere mögliche
  Gründe sind ungeprüft:
  - Ausschreibungen ohne veröffentlichten Zuschlag, z. B. aufgehoben oder unter der Schwelle bezuschlagt
  - CPV-909-Lose in anderen Verfahren (`classification-cpv` enthält in eForms auch CPVs der Lose)
  - echte Zunahme

  Für K1 ist das wichtig: Der Nenner zählt deshalb Verfahren, nicht Notices (Präzisierung in `docs/iterationen.md`).
- **Vorinformationen sind als Frühsignal praktisch bedeutungslos.** Es sind etwa 2 % der Ausschreibungen.
- Die Basisrate des Prognoseziels liegt in den vollen eForms-Jahren 2024 und 2025 bei **etwa 2.560 bis 2.780 Ausschreibungs-Notices
  pro Jahr** (Haupt-CPV bzw. CPV-Liste). Nach Abzug von etwa 16 % Änderungen wären das grob 2.150 bis 2.350 Verfahren. Das ist eine
  Hochrechnung aus einer nicht zufälligen Teilmenge; die bereinigte Zahl folgt aus dem Download in Schritt 3.

## Offene Punkte für die nächsten Schritte

- Schritt 3: Ausschreibungen aus Q2 2026 vollständig laden und auf Verfahren deduplizieren (genaue Zahl für den K1-Nenner).
- Schritt 4: K5 aus den eForms-Zuschlägen berechnen (Laufzeitende ≤ 23.10.2026).
- Prüfen, warum die Zahl der Ausschreibungen mit eForms um etwa 45 % steigt (siehe Interpretation).
