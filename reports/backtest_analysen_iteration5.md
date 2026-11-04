# Nachträgliche Analysen zum Backtest (Iteration 5)

_Erzeugt mit `src/model/analyse_backtest.py`. Explorativ und nach dem Ergebnis ergänzt (Auflage des Evaluators); keine Schwelle, keine Änderung an R0/R1 oder den Paaren._

## 1. Paare mit langer Lücke

- Veröffentlichung **mehr als 24 Monate nach** der R1-Prognose: **12** von 52 Paaren; mehr als 24 Monate **vor** der Prognose: 4.

| Paar | Vorgänger | Veröffentl. Vorgänger | Ende GL | Höchstende | Testfall | Veröffentl. Testfall | Abw. R1 (Mon.) | gleicher Auftraggeber dazwischen (Notices) |
|---|---|---|---|---|---|---|---|---|
| T34 | 255487-2018 | 2018-06-14 | 2019-04-30 | – | 671403-2026 | 2026-09-30 | +95 | 0 () |
| T23 | 408656-2018 | 2018-09-19 | 2019-12-31 | – | 589942-2026 | 2026-08-26 | +86 | 44 (504592-2020, 285407-2021, 293878-2021, 426143-2023 …) |
| T8 | 165901-2019 | 2019-04-09 | 2020-04-30 | 2020-04-30 | 656958-2026 | 2026-09-23 | +83 | 133 (657425-2021, 21303-2022, 55498-2022, 130333-2022 …) |
| T24 | 85643-2020 | 2020-02-20 | 2021-02-28 | 2021-02-28 | 673994-2026 | 2026-09-30 | +73 | 135 (657425-2021, 21303-2022, 55498-2022, 130333-2022 …) |
| T33 | 254121-2019 | 2019-05-31 | 2022-04-30 | – | 565728-2026 | 2026-08-14 | +57 | 21 (582425-2019, 410377-2021, 5835-2024, 778168-2024 …) |
| U19 | 369209-2017 | 2017-09-20 | 2022-08-31 | – | 129778-2026 | 2026-02-24 | +48 | 461 (383197-2017, 29057-2018, 63562-2018, 237974-2018 …) |
| T38 | 32306-2021 | 2021-01-22 | 2023-04-30 | – | 494560-2026 | 2026-07-17 | +45 | 369 (61505-2021, 61579-2021, 61587-2021, 74309-2021 …) |
| U54 | 209315-2019 | 2019-05-06 | 2023-04-28 | 2023-04-28 | 100442-2026 | 2026-02-12 | +40 | 0 () |
| T37 | 697551-2022 | 2022-12-16 | 2023-12-31 | – | 573790-2026 | 2026-08-19 | +38 | 39 (426143-2023, 727139-2023, 623996-2024, 690102-2024 …) |
| T56 | 431363-2021 | 2021-08-25 | 2023-12-31 | – | 564026-2026 | 2026-08-14 | +37 | 581 (471174-2021, 510478-2021, 524542-2021, 592157-2021 …) |
| T15 | 562187-2020 | 2020-11-23 | 2021-12-31 | 2024-12-31 | 629751-2026 | 2026-09-14 | +26 | 77 (598488-2020, 602251-2020, 302867-2021, 500319-2021 …) |
| U65 | 272214-2020 | 2020-06-11 | 2024-04-30 | 2024-04-30 | 14788-2026 | 2026-01-09 | +26 | 11 (63574-2025, 199697-2025, 224470-2025, 569759-2025 …) |

- Bei **10 von 12** Paaren hat derselbe Auftraggeber zwischen Vorgänger und Testfall weitere 909-Bekanntmachungen veröffentlicht. Das ist bei großen Auftraggebern häufig und belegt keinen Zwischenvertrag für dasselbe Objekt.
- Trefferquote R1 ohne die 12 Paare mit später Lücke: 15/40 = 37,5 % (Wilson 24,2–53,0); ohne späte und frühe Lücken: 15/36 = 41,7 % (Wilson 27,1–57,8).

## 2. Nach Auftraggeber

- 52 Paare, **40 Auftraggeber** (Schlüssel: erste vier Wörter des normalisierten Namens; grob).
- Auftraggeber mit mehr als einem Paar: 6; Paare davon: 18.

| Auftraggeber (Schlüssel) | Paare | R1-Treffer |
|---|---|---|
| freistaat bayern vertreten durch | 5 | 0/5 |
| bundesanstalt für immobilienaufgaben | 4 | 3/4 |
| ikk classic | 3 | 2/3 |
| land niedersachsen vertreten durch | 2 | 0/2 |
| stadt dessauroßlau zentr vergabestelle | 2 | 0/2 |
| stadt frankfurt am main | 2 | 0/2 |

- **Jeder Auftraggeber zählt gleich** (Mittel der Cluster-Trefferquoten): R1 **28,5 %**, R0 19,2 %,
- Ein Paar je Auftraggeber (alphabetisch erstes Paar je Cluster, n = 40): R1 11/40 = 27,5 % (Wilson 16,1–42,8), R0 8/40 = 20,0 % (Wilson 10,5–34,8).

## Grenzen

- Auftraggeber-Schlüssel grob (Schreibvarianten werden nicht zusammengeführt, Zentralen großer Länder führen mehrere Dienststellen unter einem Namen).
- Ein Auftraggeber mit anderem Objekt dazwischen ist kein Beleg für einen Zwischenvertrag; die Handsuche und die Prüfer haben nur Objektidentität beurteilt.
- Beide Analysen sind nachträglich und können das Ergebnis X3 nicht ändern.
