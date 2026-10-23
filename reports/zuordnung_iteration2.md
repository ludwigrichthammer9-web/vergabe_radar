# Zuordnung Ausschreibung → früherer Zuschlag (Iteration 2, Schritt 5)

Erzeugt mit `src/zuordnung_prototyp.py`. Ausschreibungen: `data/raw/ted_search/DEU_competition_cpv909main_20260401_20260630/` (nur Originale, ohne Änderungsbekanntmachungen). Pool: `data/raw/ted_search/DEU_result_cpv909_20161001_20261022/`.

Regel: gleicher normalisierter Auftraggebername (Kleinschreibung, Umlaute umgeschrieben, Satzzeichen entfernt) oder gleiche normalisierte Auftraggeber-Kennung (ohne Präfix, ≥ 8 Zeichen, keine Telefonnummer); Zuschlag vor der Ausschreibung veröffentlicht. Auswahl unter mehreren Kandidaten: (1) eForms-Kandidat mit Vertragsende -3 bis +18 Monate relativ zur Ausschreibung (ähnlichster Titel), (2) sonst jüngster Kandidat vor eForms, (3) sonst ähnlichster Titel bzw. jüngster.

## K1: Anteil der Ausschreibungen mit Vorgänger-Kandidat

| Variante | Treffer | von | Anteil | 95-%-KI (Wilson) |
|---|---|---|---|---|
| **Name oder Kennung (K1)** | 461 | 551 | 83,7 % | 80,3–86,5 % |
| nur Name | 441 | 551 | 80,0 % | 76,5–83,2 % |

K1-Schwelle ≥ 50 %: **erfüllt** (vor manueller Prüfung, siehe K2).

## Kandidaten je Ausschreibung (nur Treffer)

| Kandidaten   |   Ausschreibungen |
|:-------------|------------------:|
| 1            |                56 |
| 2            |                39 |
| 3–5          |                70 |
| 6–10         |                48 |
| 11–50        |               126 |
| > 50         |               122 |

## Gewählter Kandidat

- über Name: 390, nur über Kennung: 71
- Stufe der Auswahlregel: 1 Ende passt: 236, 2 vor eForms: 188, 3 sonstige: 37
- **K3 (vorläufig, vor Prüfung):** Vorgänger im eForms-Format 273 von 461 = 59,2 %
- mit Titelähnlichkeit (beide Titel vorhanden): 273, davon Ähnlichkeit > 0: 207

Veröffentlichungsjahr des gewählten Vorgängers:

|   Jahr |   Vorgänger |
|-------:|------------:|
|   2017 |           5 |
|   2018 |           2 |
|   2019 |           5 |
|   2020 |           9 |
|   2021 |          19 |
|   2022 |          54 |
|   2023 |          98 |
|   2024 |          81 |
|   2025 |         130 |
|   2026 |          58 |

## Vorlauf (explorativ, A8)

Vorlauf = Vertragsende des Vorgängers minus Veröffentlichung der Ausschreibung, in Monaten (positiv = Ausschreibung vor Vertragsende). Nur Vorgänger mit bestimmbarem Ende (praktisch nur eForms). **Ungeprüfte Paare**: Fehlzuordnungen verzerren die Verteilung. **Zirkulär für Stufe 1:** Dort wurde nach dem Vorlauf-Fenster ausgewählt, die Verteilung ist also nur beschreibend und kein Test von A8.

n = 257; Median 10.0; Quartile 5.6 / 15.2; 10.–90. Perzentil 2.0 / 17.3.
Anteil Ausschreibung vor Vertragsende: 94,6 %; 0–12 Monate vor Ende: 54,9 %.
