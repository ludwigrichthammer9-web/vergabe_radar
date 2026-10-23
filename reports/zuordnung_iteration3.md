# Zuordnung über das Objekt: Testergebnis (Iteration 3)

Erzeugt mit `src/auswertung_iteration3.py`. Regel: Stand Commit 4497743 (eingefroren vor den Testdaten). Handsuche: `reports/sichtbarkeit_iteration3_teil1.md` bis `_teil4.md`, übertragen in `sichtbarkeit_iteration3_gt.csv`.

| Kriterium | Ergebnis | Schwelle |
|---|---|---|
| V1 Sichtbarkeit | 38/60 = 63,3 % (Wilson 50,7–74,4 %) | ≥ 50 % |
| V2 Präzision | 11/24 = 45,8 % (Wilson 27,9–64,9 %) | ≥ 80 % und Untergrenze ≥ 60 % |
| V3 Trefferquote | 11/38 = 28,9 % (Wilson 17,0–44,8 %) | ≥ 60 % |
| V5 Backtest-Basis | 10/60 Fälle × 492 × 4 = 328 pro Jahr | ≥ 100 pro Jahr |

| T | Testfall | Handsuche | Vorgänger (Handsuche) | Vorschlag der Regel | Stufe | Status | Vorgänger-Ende |
|---|---|---|---|---|---|---|---|
| T1 | 644509-2026 | objektgleich | 387492-2021 547893-2021 | 442059-2026 | B | falsch (Einzelurteil) |  |
| T2 | 554609-2026 | unklar | – | – |  | kein Vorschlag |  |
| T3 | 546143-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T4 | 530979-2026 | objektgleich | 202519-2022 463753-2021 | – |  | kein Vorschlag |  |
| T5 | 598474-2026 | objektgleich | 477850-2022 665652-2022 670866-2022 | – |  | kein Vorschlag |  |
| T6 | 461152-2026 | teilmenge | 364258-2023 | 364258-2023 | A | korrekt (Handsuche) | 2025-12-31 |
| T7 | 503493-2026 | objektgleich | 155215-2021 607469-2020 | 380581-2026 | B | falsch (Einzelurteil) |  |
| T8 | 656958-2026 | objektgleich | 165901-2019 472607-2018 | 306431-2026 | B | falsch (Einzelurteil) |  |
| T9 | 610118-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T10 | 514223-2026 | teilmenge | 465718-2022 | – |  | kein Vorschlag |  |
| T11 | 506593-2026 | objektgleich | 312117-2023 574481-2023 | – |  | kein Vorschlag |  |
| T12 | 615831-2026 | objektgleich | 172338-2023 434268-2023 459072-2022 652257-2022 | 459072-2022 | B | korrekt (Handsuche) | 2024-12-31 |
| T13 | 613923-2026 | objektgleich | 285864-2022 38357-2022 | – |  | kein Vorschlag |  |
| T14 | 599457-2026 | teilmenge | 364629-2019 569523-2019 | 569523-2019 | B | korrekt (Handsuche) | 2020-12-31 |
| T15 | 629751-2026 | objektgleich | 374922-2020 562187-2020 | – |  | kein Vorschlag |  |
| T16 | 559458-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T17 | 540820-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T18 | 658725-2026 | teilmenge | 227031-2024 488398-2026 524787-2023 557041-2023 571224-2023 710461-2023 755423-2023 | 488398-2026 | B | korrekt (Handsuche) | 2028-01-31 |
| T19 | 474898-2026 | objektgleich | 286526-2023 636701-2023 | – |  | kein Vorschlag |  |
| T20 | 601496-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T21 | 478291-2026 | objektgleich | 142984-2022 301495-2022 309063-2018 | 165984-2026 | B | falsch (Einzelurteil) |  |
| T22 | 574953-2026 | objektgleich | 482658-2018 509902-2022 | – |  | kein Vorschlag |  |
| T23 | 589942-2026 | objektgleich | 23048-2018 408656-2018 | 821004-2025 | B | falsch (Einzelurteil) |  |
| T24 | 673994-2026 | objektgleich | 488738-2019 85643-2020 | 495197-2026 | B | falsch (Einzelurteil) |  |
| T25 | 616444-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T26 | 555139-2026 | objektgleich | 462151-2026 557850-2020 95743-2021 | 462151-2026 | T | korrekt (Handsuche) | 2031-10-31 |
| T27 | 623928-2026 | unklar | – | – |  | kein Vorschlag |  |
| T28 | 455814-2026 | unklar | – | – |  | kein Vorschlag |  |
| T29 | 620007-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T30 | 555680-2026 | objektgleich | 19547-2023 434089-2023 | – |  | kein Vorschlag |  |
| T31 | 630789-2026 | kein_vorgaenger | – | 467991-2026 | A | falsch (Einzelurteil) |  |
| T32 | 535765-2026 | objektgleich | 279541-2025 498737-2025 | 498737-2025 | B | korrekt (Handsuche) | 2027-08-31 |
| T33 | 565728-2026 | teilmenge | 250469-2019 254121-2019 75546-2019 | 582425-2019 | B | korrekt (Einzelurteil) |  |
| T34 | 671403-2026 | teilmenge | 255487-2018 56913-2018 | – |  | kein Vorschlag |  |
| T35 | 506448-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T36 | 595492-2026 | objektgleich | 607255-2023 92431-2024 | 436672-2026 | T | unklar (Einzelurteil) |  |
| T37 | 573790-2026 | objektgleich | 384752-2022 697551-2022 | – |  | kein Vorschlag |  |
| T38 | 494560-2026 | objektgleich | 32306-2021 | – |  | kein Vorschlag |  |
| T39 | 599823-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T40 | 457874-2026 | objektgleich | 138159-2022 327439-2022 | – |  | kein Vorschlag |  |
| T41 | 571136-2026 | objektgleich | 347342-2022 676959-2022 | – |  | kein Vorschlag |  |
| T42 | 533895-2026 | objektgleich | 488753-2023 | – |  | kein Vorschlag |  |
| T43 | 508130-2026 | objektgleich | 222266-2020 472319-2020 | 156628-2026 | B | falsch (Einzelurteil) |  |
| T44 | 632635-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T45 | 609162-2026 | objektgleich | 385160-2022 669356-2022 | 669356-2022 | A | korrekt (Handsuche) | 2026-12-31 |
| T46 | 638682-2026 | unklar | – | 503868-2026 | B | falsch (Einzelurteil) |  |
| T47 | 651281-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T48 | 496932-2026 | objektgleich | 546264-2024 683345-2024 | 683345-2024 | T | korrekt (Handsuche) | 2026-10-31 |
| T49 | 481461-2026 | kein_vorgaenger | – | – |  | kein Vorschlag |  |
| T50 | 569458-2026 | unklar | – | – |  | kein Vorschlag |  |
| T51 | 628016-2026 | unklar | – | – |  | kein Vorschlag |  |
| T52 | 644157-2026 | teilmenge | 627861-2022 716226-2022 | 716226-2022 | A | korrekt (Handsuche) | 2024-12-31 |
| T53 | 531216-2026 | teilmenge | 209335-2023 255653-2026 343641-2023 82423-2026 | – |  | kein Vorschlag |  |
| T54 | 555833-2026 | kein_vorgaenger | – | 563086-2025 | A | falsch (Einzelurteil) |  |
| T55 | 568915-2026 | objektgleich | 513567-2018 91780-2019 | – |  | kein Vorschlag |  |
| T56 | 564026-2026 | objektgleich | 128622-2021 431363-2021 | 128622-2021 | B | korrekt (Handsuche) | 2023-12-31 |
| T57 | 607508-2026 | objektgleich | 484974-2022 686803-2022 | – |  | kein Vorschlag |  |
| T58 | 500007-2026 | unklar | – | 410442-2026 | A | falsch (Einzelurteil) |  |
| T59 | 538713-2026 | teilmenge | 284901-2019 476426-2019 | – |  | kein Vorschlag |  |
| T60 | 533980-2026 | unklar | – | 524790-2022 | T | unklar (Einzelurteil) |  |
