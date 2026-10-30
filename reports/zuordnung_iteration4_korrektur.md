# Zuordnung über Merkmale je Los: Testergebnis (Iteration 4)

Erzeugt mit `src/auswertung_iteration4.py`. Regel: `src/zuordnung_los.py`, Stand Commit 1d0e060 (eingefroren vor den Testdaten). Handsuche: `reports/sichtbarkeit_iteration4_teil1.md` bis `_teil5.md`, übertragen in `sichtbarkeit_iteration4_gt.csv` (Commit d43c547, vor dem Regel-Lauf). Vorschläge außerhalb der Handsuche: blind beurteilt in `paarbeurteilung_iteration4.md`.

| Kriterium | Ergebnis | Schwelle |
|---|---|---|
| W1 Sichtbarkeit | 30/70 = 42,9% (Wilson 31,9%–54,5%); nur objektgleich 18/70 = 25,7% (Wilson 16,9%–37,0%) | ≥ 50 % |
| W2 Präzision | 17/19 = 89,5% (Wilson 68,6%–97,1%) | ≥ 80 % und Untergrenze ≥ 60 %, mindestens 25 Vorschläge |
| W3 Trefferquote | 17/30 = 56,7% (Wilson 39,2%–72,6%) | ≥ 60 % |
| W5 Backtest-Basis | 11/70 × 1893 = 297 pro Jahr | ≥ 100 pro Jahr |
| W6 Kandidatenliste | 22/30 = 73,3% (Wilson 55,6%–85,8%) | ≥ 70 % |

Population der letzten 4 Quartale: Q4 2025 381, Q1 2026 538, Q2 2026 488, Q3 2026 486 = 1893.
Wilson-Untergrenze W2: 68,6%,

**Explorativ**

- Vorlaufzeit (Veröffentlichung Testfall bis Ende der Grundlaufzeit des Vorgängers), korrekte Paare: U2 -18.8 Monate, U6 -32.1 Monate, U13 -6.3 Monate, U14 6.1 Monate, U16 26.3 Monate, U47 -7.9 Monate, U51 0.6 Monate, U56 -6.4 Monate, U61 4.4 Monate, U64 0.3 Monate, U65 -18.3 Monate
- Vorzeitige Neuvergabe laut Handsuche: U16, U66, U70 (von 30 Fällen mit Vorgänger)

| U | Testfall | Handsuche | Vorgänger (Handsuche) | Vorschlag | Status | Top 3 | Vorgänger-Ende | Herkunft |
|---|---|---|---|---|---|---|---|---|
| U1 | 152665-2026 | unklar | – | – | – |  |  |  |
| U2 | 213443-2026 | objektgleich_mittel | 444675-2022 270164-2022 | 270164-2022 | korrekt (Handsuche) | ✓ | 2024-08-31, Höchstende 2026-08-31 | grundlaufzeit, hoechstende |
| U3 | 193121-2026 | unklar | – | – | – |  |  |  |
| U4 | 130379-2026 | unklar | – | – | – |  |  |  |
| U5 | 27535-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U6 | 72981-2026 | objektgleich_mittel | 226910-2022 48085-2022 | 226910-2022 | korrekt (Handsuche) | ✓ | 2023-05-31, Höchstende 2026-05-31 | grundlaufzeit, hoechstende |
| U7 | 74601-2026 | objektgleich_mittel | 509878-2022 | 509878-2022 | korrekt (Handsuche) | ✓ | 2027-02-19 (nur Plan) | grundlaufzeit (aus Ausschreibung) |
| U8 | 78859-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U9 | 186753-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U10 | 56181-2026 | unklar | – | – | – |  |  |  |
| U11 | 126685-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U12 | 147547-2026 | unklar | – | – | – |  |  |  |
| U13 | 21073-2026 | teilmenge | 316381-2022 11901-2022 74566-2019 316847-2019 | 316381-2022 | korrekt (Handsuche) | ✓ | 2025-07-06, Höchstende 2026-07-06 | grundlaufzeit, hoechstende |
| U14 | 137283-2026 | objektgleich_mittel | 398720-2023 204616-2023 203678-2018 365432-2018 | 398720-2023 | korrekt (Handsuche) | ✓ | 2026-08-31, Höchstende 2028-08-31 | grundlaufzeit, hoechstende |
| U15 | 84022-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U16 | 122844-2026 | objektgleich_mittel | 181605-2024 50843-2024 | 181605-2024 | korrekt (Handsuche) | ✓ | 2028-04-30 | grundlaufzeit |
| U17 | 93297-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U18 | 221159-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U19 | 129778-2026 | objektgleich_mittel | 369209-2017 122321-2017 728662-2022 | – | verpasst | ✓ |  |  |
| U20 | 137428-2026 | unklar | – | – | – |  |  |  |
| U21 | 125546-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U22 | 109620-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U23 | 2335-2026 | objektgleich_mittel | 598365-2020 450593-2020 | – | verpasst |  |  |  |
| U24 | 98964-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U25 | 209981-2026 | teilmenge | 629441-2024 757743-2023 184953-2025 | – | verpasst |  |  |  |
| U26 | 84590-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U27 | 92834-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U28 | 54141-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U29 | 135556-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U30 | 112103-2026 | objektgleich_mittel | 265170-2020 104121-2020 146410-2020 | – | verpasst |  |  |  |
| U31 | 195153-2026 | unklar | – | – | – |  |  |  |
| U32 | 164478-2026 | teilmenge | 151676-2021 480055-2020 | 151676-2021 | korrekt (Handsuche) | ✓ | 2027-03-31 | hoechstende |
| U33 | 161174-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U34 | 199877-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U35 | 195060-2026 | teilmenge | 325959-2023 438157-2023 | 517331-2019 | korrekt (Paarurteil: teilmenge) |  | 2022-11-30 | hoechstende |
| U36 | 36379-2026 | unklar | – | – | – |  |  |  |
| U37 | 150041-2026 | objektgleich_mittel | 642246-2021 277910-2021 | – | verpasst |  |  |  |
| U38 | 173541-2026 | unklar | – | – | – |  |  |  |
| U39 | 183269-2026 | teilmenge | 347828-2022 125967-2022 | 347828-2022 | korrekt (Handsuche) | ✓ | Grundlaufzeit 2025-07-31, danach jährlich | rollierend |
| U40 | 108283-2026 | unklar | – | – | – |  |  |  |
| U41 | 34825-2026 | unklar | – | – | – |  |  |  |
| U42 | 187770-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U43 | 127506-2026 | objektgleich_mittel | 343780-2023 207575-2023 | – | verpasst | ✓ |  |  |
| U44 | 134489-2026 | objektgleich_mittel | 362257-2022 170455-2022 | – | verpasst | ✓ |  |  |
| U45 | 62104-2026 | unklar | – | – | – |  |  |  |
| U46 | 55335-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U47 | 134081-2026 | teilmenge | 328497-2023 157336-2023 | 328497-2023 | korrekt (Handsuche) | ✓ | 2025-06-30 (Höchstende 2027-06-30) | grundlaufzeit |
| U48 | 47380-2026 | teilmenge | 285809-2022 561967-2020 | 285809-2022 | korrekt (Handsuche) | ✓ | 2025-12-31 (abgeleitet) | hoechstende |
| U49 | 29273-2026 | unklar | – | – | – |  |  |  |
| U50 | 87147-2026 | unklar | – | – | – |  |  |  |
| U51 | 90864-2026 | objektgleich_mittel | 773594-2023 537842-2023 | 773594-2023 | korrekt (Handsuche) | ✓ | 2026-02-28 (Los 1) / 2026-03-31 (Lose 2–4), Höchstende 2028-02-29 / 2028-03-31 | grundlaufzeit |
| U52 | 160356-2026 | unklar | – | – | – |  |  |  |
| U53 | 123318-2026 | objektgleich_mittel | 466300-2024 186962-2024 466323-2024 | – | verpasst | ✓ |  |  |
| U54 | 100442-2026 | teilmenge | 209315-2019 83582-2019 | – | verpasst |  |  |  |
| U55 | 153719-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U56 | 93751-2026 | teilmenge | 79802-2023 505956-2022 148457-2020 299773-2020 | 79802-2023 | korrekt (Handsuche) | ✓ | 2025-07-31 (Höchstende 2026-07-31) | grundlaufzeit |
| U57 | 107491-2026 | teilmenge | 388581-2024 | – | verpasst | ✓ |  |  |
| U58 | 45854-2026 | unklar | – | – | – |  |  |  |
| U59 | 76175-2026 | unklar | – | 400405-2025 | falsch (Paarurteil: unklar) |  | – | – |
| U60 | 136348-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U61 | 190390-2026 | objektgleich_mittel | 491137-2023 305562-2023 | 491137-2023 | korrekt (Handsuche) | ✓ | 2026-07-31 | grundlaufzeit |
| U62 | 173981-2026 | objektgleich_mittel | 95199-2021 | – | verpasst |  |  |  |
| U63 | 104339-2026 | unklar | – | – | – |  |  |  |
| U64 | 52190-2026 | objektgleich_mittel | 38758-2022 578867-2021 | 38758-2022 | korrekt (Handsuche) | ✓ | 2026-01-31 | grundlaufzeit |
| U65 | 14788-2026 | teilmenge | 272214-2020 155476-2020 | 272214-2020 | korrekt (Handsuche) | ✓ | 2024-06-30 | grundlaufzeit |
| U66 | 139668-2026 | objektgleich_mittel | 215020-2024 711340-2023 | 765145-2025 | falsch (Paarurteil: nicht_objektgleich) | ✓ | – | – |
| U67 | 107129-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U68 | 106993-2026 | kein_vorgaenger | – | – | – |  |  |  |
| U69 | 198259-2026 | objektgleich_mittel | 540553-2025 547505-2025 562230-2025 600400-2025 | 540553-2025 | korrekt (Handsuche) | ✓ | unbekannt (Plan 2027-12-14) | unbekannt |
| U70 | 37917-2026 | teilmenge | 758702-2025 337994-2025 424628-2025 | – | verpasst |  |  |  |
