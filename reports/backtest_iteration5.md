# Backtest Iteration 5 (Schritt 6, Kriterium X3)

_Erzeugt mit `src/model/baseline.py` (eingefroren und vor dem Lauf committet). Regeln und Treffer-Definition in `docs/business.md` §7.1; fachliches Kriterium dort vor dem Lauf festgelegt._

## Fakten

- Paare: **52** (von Rechercheur und Prüfer bestätigt, Ende der Grundlaufzeit bestimmbar; Zweitprüfung [gt_pruefung_iteration5_auswertung.md](gt_pruefung_iteration5_auswertung.md)).
- Parameter: Vorlauf 6 Monate, Fenster ±3 Monate; keine Schätzung aus den Paaren.

| | Treffer ±3 Monate | ±6 Monate (ohne Schwelle) | Median Abweichung (Monate, Veröffentlichung − Prognose) |
|---|---|---|---|
| **R0** Grundlaufzeit − 6 | 9/52 = 17,3 % (Wilson 9,4–29,7) | 11/52 = 21,2 % (Wilson 12,2–34,0) | +14,0 |
| **R1** Höchstende − 6 | 15/52 = 28,8 % (Wilson 18,3–42,3) | 16/52 = 30,8 % (Wilson 19,9–44,3) | +0,6 |

**X3:** R1 28,8 % (Schwelle ≥ 60 %), Abstand zu R0 +11,5 Prozentpunkte (Schwelle ≥ +10) → **nicht erfüllt**.

### Aufschlüsselung (explorativ, ohne Schwelle)

| Gruppe | n | R0 Treffer | R1 Treffer | Differenz (Prozentpunkte) |
|---|---|---|---|---|
| Iteration 3 (Testfälle Q3 2026) | 28 | 6/28 = 21,4 % (Wilson 10,2–39,5) | 9/28 = 32,1 % (Wilson 17,9–50,7) | +10,7 |
| Iteration 4 (Testfälle Q1 2026) | 24 | 3/24 = 12,5 % (Wilson 4,3–31,0) | 6/24 = 25,0 % (Wilson 12,0–44,9) | +12,5 |
| Vorgänger vor eForms (XML) | 41 | 7/41 = 17,1 % (Wilson 8,5–31,3) | 14/41 = 34,1 % (Wilson 21,6–49,5) | +17,1 |
| Vorgänger eForms (API) | 11 | 2/11 = 18,2 % (Wilson 5,1–47,7) | 1/11 = 9,1 % (Wilson 1,6–37,7) | -9,1 |
| Höchstende: anzahl_x_laenge | 6 | 2/6 = 33,3 % (Wilson 9,7–70,0) | 2/6 = 33,3 % (Wilson 9,7–70,0) | +0,0 |
| Höchstende: datum_text | 14 | 1/14 = 7,1 % (Wilson 1,3–31,5) | 7/14 = 50,0 % (Wilson 26,8–73,2) | +42,9 |
| Höchstende: enddatum_ist_hoechstende | 4 | 1/4 = 25,0 % (Wilson 4,6–69,9) | 0/4 = 0,0 % (Wilson 0,0–49,0) | -25,0 |
| Höchstende: hoechstlaufzeit_text | 1 | 0/1 = 0,0 % (Wilson 0,0–79,3) | 1/1 = 100,0 % (Wilson 20,7–100,0) | +100,0 |
| Höchstende: keine_angabe | 4 | 1/4 = 25,0 % (Wilson 4,6–69,9) | 1/4 = 25,0 % (Wilson 4,6–69,9) | +0,0 |
| Höchstende: keine_verlaengerung | 10 | 3/10 = 30,0 % (Wilson 10,8–60,3) | 3/10 = 30,0 % (Wilson 10,8–60,3) | +0,0 |
| Höchstende: unbestimmbar | 13 | 1/13 = 7,7 % (Wilson 1,4–33,3) | 1/13 = 7,7 % (Wilson 1,4–33,3) | +0,0 |
| Höchstende ≠ Grundlaufzeit (Verlängerung belegt) | 24 | 4/24 = 16,7 % (Wilson 6,7–35,9) | 10/24 = 41,7 % (Wilson 24,5–61,2) | +25,0 |
| Höchstende = Grundlaufzeit oder unbekannt | 28 | 5/28 = 17,9 % (Wilson 7,9–35,6) | 5/28 = 17,9 % (Wilson 7,9–35,6) | +0,0 |
| Objektgleich laut Handsuche | 37 | 8/37 = 21,6 % (Wilson 11,4–37,2) | 12/37 = 32,4 % (Wilson 19,6–48,5) | +10,8 |
| Teilmenge laut Handsuche | 15 | 1/15 = 6,7 % (Wilson 1,2–29,8) | 3/15 = 20,0 % (Wilson 7,0–45,2) | +13,3 |

### Lage der Veröffentlichung relativ zur R1-Prognose

| Lage | Paare |
|---|---|
| früher als −3 | 20 |
| später als +3 | 17 |
| im Fenster | 15 |

### Alle Paare (Prognose und Veröffentlichung)

| Paar | Testfall | Veröffentlicht | Ende GL | Höchstende (Herkunft) | R0 | R1 | Abw. R1 (Mon.) | R0 | R1 |
|---|---|---|---|---|---|---|---|---|---|
| U70 | 37917-2026 | 2026-01-19 | 2029-09-30 | – (unbestimmbar) | 2029-03-30 | 2029-03-30 | -38.3 | ✗ | ✗ |
| U43 | 127506-2026 | 2026-02-24 | 2026-07-31 | 2029-07-31 (enddatum_ist_hoechstende) | 2026-01-31 | 2029-01-31 | -35.2 | ✓ | ✗ |
| U57 | 107491-2026 | 2026-02-16 | 2026-11-30 | 2028-11-30 (datum_text) | 2026-05-30 | 2028-05-30 | -27.4 | ✗ | ✗ |
| U14 | 137283-2026 | 2026-02-26 | 2026-08-31 | 2028-08-31 (anzahl_x_laenge) | 2026-02-28 | 2028-02-29 | -24.1 | ✓ | ✗ |
| T30 | 555680-2026 | 2026-08-11 | 2026-12-31 | 2028-12-31 (datum_text) | 2026-06-30 | 2028-06-30 | -22.6 | ✓ | ✗ |
| T18 | 658725-2026 | 2026-09-24 | 2028-01-31 | 2029-01-31 (datum_text) | 2027-07-31 | 2028-07-31 | -22.2 | ✗ | ✗ |
| U66 | 139668-2026 | 2026-02-27 | 2028-05-31 | 2028-05-31 (keine_angabe) | 2027-11-30 | 2027-11-30 | -21.1 | ✗ | ✗ |
| U16 | 122844-2026 | 2026-02-20 | 2028-04-30 | – (unbestimmbar) | 2027-10-30 | 2027-10-30 | -20.3 | ✗ | ✗ |
| T21 | 478291-2026 | 2026-07-10 | 2025-08-31 | 2028-08-31 (enddatum_ist_hoechstende) | 2025-02-28 | 2028-02-29 | -19.7 | ✗ | ✗ |
| U51 | 90864-2026 | 2026-02-09 | 2028-03-31 | 2028-03-31 (keine_angabe) | 2027-09-30 | 2027-09-30 | -19.6 | ✗ | ✗ |
| U69 | 198259-2026 | 2026-03-23 | 2027-12-14 | 2027-12-14 (keine_angabe) | 2027-06-14 | 2027-06-14 | -14.7 | ✗ | ✗ |
| T6 | 461152-2026 | 2026-07-06 | 2025-12-31 | 2027-12-31 (datum_text) | 2025-06-30 | 2027-06-30 | -11.8 | ✗ | ✗ |
| T36 | 595492-2026 | 2026-08-28 | 2026-01-31 | 2028-01-31 (anzahl_x_laenge) | 2025-07-31 | 2027-07-31 | -11.1 | ✗ | ✗ |
| U47 | 134081-2026 | 2026-02-25 | 2025-06-30 | 2027-06-30 (anzahl_x_laenge) | 2024-12-30 | 2026-12-30 | -10.1 | ✗ | ✗ |
| T57 | 607508-2026 | 2026-09-03 | 2025-12-31 | 2027-12-31 (datum_text) | 2025-06-30 | 2027-06-30 | -9.9 | ✗ | ✗ |
| U23 | 2335-2026 | 2026-01-05 | 2024-04-30 | 2027-04-30 (enddatum_ist_hoechstende) | 2023-10-30 | 2026-10-30 | -9.8 | ✗ | ✗ |
| T48 | 496932-2026 | 2026-07-17 | 2026-10-31 | 2027-10-31 (anzahl_x_laenge) | 2026-04-30 | 2027-04-30 | -9.4 | ✓ | ✗ |
| T32 | 535765-2026 | 2026-08-03 | 2027-08-31 | 2027-08-31 (enddatum_ist_hoechstende) | 2027-02-28 | 2027-02-28 | -6.9 | ✗ | ✗ |
| U32 | 164478-2026 | 2026-03-10 | 2025-03-31 | 2027-03-31 (datum_text) | 2024-09-30 | 2026-09-30 | -6.7 | ✗ | ✗ |
| U7 | 74601-2026 | 2026-02-02 | 2027-02-19 | – (unbestimmbar) | 2026-08-19 | 2026-08-19 | -6.5 | ✗ | ✗ |
| U30 | 112103-2026 | 2026-02-17 | 2024-10-31 | 2026-10-31 (datum_text) | 2024-04-30 | 2026-04-30 | -2.4 | ✗ | ✓ |
| T7 | 503493-2026 | 2026-07-21 | 2025-03-31 | 2027-03-31 (hoechstlaufzeit_text) | 2024-09-30 | 2026-09-30 | -2.3 | ✗ | ✓ |
| T43 | 508130-2026 | 2026-07-22 | 2025-01-31 | 2027-01-31 (datum_text) | 2024-07-31 | 2026-07-31 | -0.3 | ✗ | ✓ |
| T19 | 474898-2026 | 2026-07-09 | 2026-12-31 | – (unbestimmbar) | 2026-06-30 | 2026-06-30 | +0.3 | ✓ | ✓ |
| U56 | 93751-2026 | 2026-02-10 | 2025-07-31 | 2026-07-31 (datum_text) | 2025-01-31 | 2026-01-31 | +0.3 | ✗ | ✓ |
| T55 | 568915-2026 | 2026-08-17 | 2021-01-31 | 2027-01-31 (datum_text) | 2020-07-31 | 2026-07-31 | +0.6 | ✗ | ✓ |
| T41 | 571136-2026 | 2026-08-18 | 2027-01-31 | 2027-01-31 (keine_verlaengerung) | 2026-07-31 | 2026-07-31 | +0.6 | ✓ | ✓ |
| U44 | 134489-2026 | 2026-02-26 | 2024-07-31 | 2026-07-31 (anzahl_x_laenge) | 2024-01-31 | 2026-01-31 | +0.9 | ✗ | ✓ |
| U2 | 213443-2026 | 2026-03-27 | 2024-08-31 | 2026-08-31 (datum_text) | 2024-02-29 | 2026-02-28 | +0.9 | ✗ | ✓ |
| T53 | 531216-2026 | 2026-07-31 | 2026-12-31 | 2026-12-31 (keine_angabe) | 2026-06-30 | 2026-06-30 | +1.0 | ✓ | ✓ |
| U61 | 190390-2026 | 2026-03-19 | 2026-07-31 | 2026-07-31 (keine_verlaengerung) | 2026-01-31 | 2026-01-31 | +1.5 | ✓ | ✓ |
| T5 | 598474-2026 | 2026-08-31 | 2023-12-31 | 2026-12-31 (datum_text) | 2023-06-30 | 2026-06-30 | +2.0 | ✗ | ✓ |
| U6 | 72981-2026 | 2026-02-02 | 2023-05-31 | 2026-05-31 (datum_text) | 2022-11-30 | 2025-11-30 | +2.1 | ✗ | ✓ |
| T45 | 609162-2026 | 2026-09-03 | 2026-12-31 | 2026-12-31 (keine_verlaengerung) | 2026-06-30 | 2026-06-30 | +2.1 | ✓ | ✓ |
| T52 | 644157-2026 | 2026-09-18 | 2024-12-31 | 2026-12-31 (anzahl_x_laenge) | 2024-06-30 | 2026-06-30 | +2.6 | ✗ | ✓ |
| U64 | 52190-2026 | 2026-01-23 | 2026-01-31 | 2026-01-31 (keine_verlaengerung) | 2025-07-31 | 2025-07-31 | +5.8 | ✗ | ✗ |
| T26 | 555139-2026 | 2026-08-11 | 2026-03-31 | 2026-03-31 (keine_verlaengerung) | 2025-09-30 | 2025-09-30 | +10.3 | ✗ | ✗ |
| U13 | 21073-2026 | 2026-01-13 | 2025-07-06 | – (unbestimmbar) | 2025-01-06 | 2025-01-06 | +12.2 | ✗ | ✗ |
| U39 | 183269-2026 | 2026-03-17 | 2025-07-31 | – (unbestimmbar) | 2025-01-31 | 2025-01-31 | +13.5 | ✗ | ✗ |
| T1 | 644509-2026 | 2026-09-18 | 2025-12-31 | 2025-12-31 (keine_verlaengerung) | 2025-06-30 | 2025-06-30 | +14.6 | ✗ | ✗ |
| U65 | 14788-2026 | 2026-01-09 | 2024-04-30 | 2024-04-30 (keine_verlaengerung) | 2023-10-30 | 2023-10-30 | +26.3 | ✗ | ✗ |
| T15 | 629751-2026 | 2026-09-14 | 2021-12-31 | 2024-12-31 (datum_text) | 2021-06-30 | 2024-06-30 | +26.5 | ✗ | ✗ |
| T56 | 564026-2026 | 2026-08-14 | 2023-12-31 | – (unbestimmbar) | 2023-06-30 | 2023-06-30 | +37.5 | ✗ | ✗ |
| T37 | 573790-2026 | 2026-08-19 | 2023-12-31 | – (unbestimmbar) | 2023-06-30 | 2023-06-30 | +37.7 | ✗ | ✗ |
| U54 | 100442-2026 | 2026-02-12 | 2023-04-28 | 2023-04-28 (keine_verlaengerung) | 2022-10-28 | 2022-10-28 | +39.5 | ✗ | ✗ |
| T38 | 494560-2026 | 2026-07-17 | 2023-04-30 | – (unbestimmbar) | 2022-10-30 | 2022-10-30 | +44.6 | ✗ | ✗ |
| U19 | 129778-2026 | 2026-02-24 | 2022-08-31 | – (unbestimmbar) | 2022-02-28 | 2022-02-28 | +47.9 | ✗ | ✗ |
| T33 | 565728-2026 | 2026-08-14 | 2022-04-30 | – (unbestimmbar) | 2021-10-30 | 2021-10-30 | +57.5 | ✗ | ✗ |
| T24 | 673994-2026 | 2026-09-30 | 2021-02-28 | 2021-02-28 (keine_verlaengerung) | 2020-08-28 | 2020-08-28 | +73.1 | ✗ | ✗ |
| T8 | 656958-2026 | 2026-09-23 | 2020-04-30 | 2020-04-30 (keine_verlaengerung) | 2019-10-30 | 2019-10-30 | +82.8 | ✗ | ✗ |
| T23 | 589942-2026 | 2026-08-26 | 2019-12-31 | – (unbestimmbar) | 2019-06-30 | 2019-06-30 | +85.9 | ✗ | ✗ |
| T34 | 671403-2026 | 2026-09-30 | 2019-04-30 | – (unbestimmbar) | 2018-10-30 | 2018-10-30 | +95.0 | ✗ | ✗ |

## Grenzen

- Nur Neuausschreibungen, die auf TED erscheinen (Trefferquote, nicht Präzision der Prognosen ohne Nachfolger).
- Paare stammen aus der Handsuche (Rückwärtssuche); ob sie für alle Verträge typisch sind, ist offen.
- Die Vorlaufzeiten dieser Paare wurden in Iteration 3 und 4 explorativ gesehen; das hat das Prognoseziel mitbestimmt.
- 5 Paare ohne Bestätigung beider Prüfer und die Paare ohne bestimmbares Ende fehlen.
- Höchstende vor eForms nur an eForms-Texten getestet (`reports/hoechstende_pruefung_iteration5_test.md`).
- Unabhängigkeit der Zweitprüfung für P14–P71 offen (A18).
