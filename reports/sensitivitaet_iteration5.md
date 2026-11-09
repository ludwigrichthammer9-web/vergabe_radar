# Sensitivität des Backtests (Nachtrag zu Iteration 5)

_Erzeugt von `src/model/sensitivitaet_backtest.py` aus der Tabelle „Alle Paare“ in `reports/backtest_iteration5.md` (52 Paare). **Nachträglich, kein neuer Test:** Vorlauf und Fenster werden hier im Nachhinein auf denselben Paaren variiert; das beste Ergebnis ist eine optimistische Obergrenze._

## Kontrolle (vorab festgelegte Regel)

R0 (Ende der Grundlaufzeit − 6 Monate, ±3): **9 von 52 = 17.3 %**; R1 (Höchstende − 6 Monate, ±3): **15 von 52 = 28.8 %** (Wilson 18.3–42.3 %). Muss mit `reports/backtest_iteration5.md` übereinstimmen (9 und 15).

## R1 gegen R0 auf denselben Paaren

Nur R1 trifft: 10 Paare; nur R0 trifft: 4 Paare. Exakter McNemar-Test (zweiseitig): p = 0.18. Der Vorsprung von R1 vor der naiven Referenz ist damit statistisch nicht gesichert.

## Vorlauf 0 bis 24 Monate (Fenster ±3)

| Vorlauf (Monate) | R0 Treffer | R1 Treffer | R1 in % |
|---|---|---|---|
| 0 | 1 | 1 | 1.9 |
| 1 | 3 | 5 | 9.6 |
| 2 | 6 | 7 | 13.5 |
| 3 | 9 | 13 | 25.0 |
| 4 | 9 | 13 | 25.0 |
| 5 | 9 | 13 | 25.0 |
| 6 (vorab) | 9 | 15 | 28.8 |
| 7 | 8 | 12 | 23.1 |
| 8 | 5 | 9 | 17.3 |
| 9 | 2 | 3 | 5.8 |
| 10 | 3 | 5 | 9.6 |
| 11 | 3 | 5 | 9.6 |
| 12 | 3 | 3 | 5.8 |
| 13 | 2 | 6 | 11.5 |
| 14 | 3 | 7 | 13.5 |
| 15 | 3 | 9 | 17.3 |
| 16 | 1 | 6 | 11.5 |
| 17 | 1 | 6 | 11.5 |
| 18 | 2 | 7 | 13.5 |
| 19 | 2 | 4 | 7.7 |
| 20 | 1 | 3 | 5.8 |
| 21 | 1 | 1 | 1.9 |
| 22 | 1 | 1 | 1.9 |
| 23 | 2 | 3 | 5.8 |
| 24 | 2 | 3 | 5.8 |

Bester Vorlauf für R1: 6 Monate mit 15 von 52 = 28.8 % (Schwelle 60 % = 32 Treffer).

## Fenster bei Vorlauf 6 Monaten

| Fenster | R0 | R1 | R1 in % |
|---|---|---|---|
| ±1 | 4 | 7 | 13.5 |
| ±2 | 7 | 9 | 17.3 |
| ±3 (vorab) | 9 | 15 | 28.8 |
| ±4 | 10 | 15 | 28.8 |
| ±6 | 11 | 16 | 30.8 |
| ±9 | 13 | 19 | 36.5 |
| ±12 | 15 | 26 | 50.0 |

## Deutung

Auch mit einem im Nachhinein optimal gewählten Vorlauf bleibt die Trefferquote weit unter der vorab festgelegten Schwelle von 60 %. Erst sehr breite Fenster (±6 Monate und mehr) erhöhen die Quote, sind für die Planung eines Betriebs aber kaum nützlich (ein Jahr Unsicherheit). Das Ergebnis „keine brauchbare Terminprognose aus TED“ hängt also nicht an der Wahl von 6 Monaten. Grenzen: 52 Paare aus einer Rückwärtssuche (verlängerte Verträge ohne Neuausschreibung fehlen), 41 von 52 Vorgängern vor eForms.
