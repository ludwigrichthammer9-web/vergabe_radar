# Auswertung der Prüfung der Vertragsliste (Iteration 6, Y1 und Y2)

_Erzeugt mit `src/prepare/auswertung_iteration6.py`. Schlüssel-Hash geprüft: `3de3e812…9d0e` = vorab festgehaltener Wert._

## Fakten

- **Y1 Ende der Grundlaufzeit korrekt: 54/60 = 90,0 % (Wilson 79,9–95,3)** (Schwelle ≥ 90 %).
- **Y2 Höchstende korrekt oder als „unbestimmbar“ gekennzeichnet: 55/60 = 91,7 % (Wilson 81,9–96,4)** (Schwelle ≥ 90 %).
- Davon bei Y1 3 Abweichungen, weil der Prüfer „unbekannt“ eintrug, wo die Liste das Enddatum führt und der Text keine Verlängerung nennt (L8, L48, L49). Werden sie als korrekt gezählt (nachträgliche Lesart, nicht das Kriterium): 57/60 = 95,0 % (Wilson 86,3–98,3).
- Prüfzeit je Los: Median 3 Minuten, Summe 163 Minuten.
- Hilfsmittel: in 60 von 60 Einträgen leer (weder „keine“ noch ein Hilfsmittel vermerkt).

### Abweichungen

| L | Notice, Los | Liste: Ende GL (Herkunft) | Prüfer: Ende GL | Liste: Höchstende (Herkunft) | Prüfer: Höchstende | Y1 | Y2 |
|---|---|---|---|---|---|---|---|
| L1 | 143100-2026, 29 | 2031-03-31 (enddatum) | 31.03.2030 | 2032-03-31 (anzahl_x_laenge) | 31.03.2031 | ✗ | ✗ |
| L8 | 750900-2025, 1 | 2029-10-31 (enddatum) | unbekannt | 2029-10-31 (keine_angabe) | 31.10.2029 | ✗ | ✓ |
| L26 | 138138-2026, 2 | 2030-02-28 (enddatum) | 28.02.2030 | 2030-02-28 (keine_angabe) | unbekannt | ✓ | ✗ |
| L42 | 448962-2026, 5 | 2030-05-31 (enddatum) | 31.05.2028 | 2032-05-31 (anzahl_x_laenge) | 31.05.2030 | ✗ | ✗ |
| L43 | 418442-2026, 2 | 2028-08-14 (enddatum) | 14.07.2028 | 2030-08-14 (anzahl_x_laenge) | unbestimmbar | ✗ | ✗ |
| L48 | 430737-2026, 1 | 2030-08-31 (enddatum) | unbekannt | 2030-08-31 (keine_angabe) | 31.08.2030 | ✗ | ✓ |
| L49 | 581372-2026, 2 | 2030-10-31 (enddatum) | unbekannt | 2030-10-31 (keine_angabe) | 31.10.2030 | ✗ | ✓ |
| L56 | 832634-2025, 5 | 2028-12-31 (enddatum) | 31.12.2028 | 2028-12-31 (keine_angabe) | 31.12.2030 | ✓ | ✗ |

## Interpretation

- Echte Fehler der Liste: L1, L42, L43 (das Enddatum BT-537 ist schon das Höchstende; der Text nennt die feste Laufzeit ohne „zunächst“, z. B. „Festlaufzeit von …“, „Laufzeit von 2 Jahren“, „erste feste Laufzeit bis …“; Regel 1a erkennt das nicht) und L56 (Verlängerung steht nur im Originaltext außerhalb der gelesenen Felder).
- L8, L48, L49 sind Auslegungsfälle: Ohne Verlängerung sind Ende der Grundlaufzeit und Höchstende dasselbe Datum; der Prüfer trug „unbekannt“ ein. L26: Prüfer „unbekannt“ beim Höchstende.
- Y1 liegt genau auf der Schwelle; das Intervall reicht weit darunter. Das Ergebnis ist knapp und hängt an wenigen Fällen.
