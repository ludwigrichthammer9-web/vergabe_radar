# Auswertung der KI-Zweitlesung (Iteration 8, Z0 bis Z4)

_Erzeugt mit `src/prepare/auswertung_iteration8.py`. Schlüssel-Hash geprüft (`eade66c0…`). Leser A = Opus, Leser B = Sonnet, je 4 Teilläufe; Antworten (nur Semikolons im Zitat von Leser B zu Kommas) in `reports/zweitlesung_iteration8_leser_a.csv` und `…_leser_b.csv`. Liste eingefroren (Commit a93785e)._

## Fakten

- **Z0 (Leser A = Leser B beim Ende der Grundlaufzeit, 95 Lose): 94/95 = 98,9 % (Wilson 94,3–99,8)** (Schwelle ≥ 90 %). Höchstende einig: 94/95.
- Z4-Stichprobe (Seed 20261108): L2, L12, L30, L40, L43, L51, L56, L59, L72, L87.
- **Z1 (Liste = Vergleichswert, 80 Lose Typ Y): 77/80 = 96,2 % (Wilson 89,5–98,7)** (Schwelle ≥ 72/80). Davon Vergleichswert „unbekannt“/„unklar“: 1.
- **Z2 (15 Regelwirkungs-Lose): 14/15 = 93,3 % (Wilson 70,2–98,8)** (Schwelle ≥ 12/15).
- **Z3 (Höchstende korrekt oder „unbestimmbar“, 80 Lose): 75/80 = 93,8 % (Wilson 86,2–97,3)** (Schwelle ≥ 90 %); **nur Lose mit behauptetem Höchstende: 67/72 = 93,1 % (Wilson 84,8–97,0)** (Schwelle ≥ 85 %).
- **Z4 (Evaluator bestätigt Übereinstimmungen am Original): 10/10** (Schwelle ≥ 9/10).
- Uneinigkeiten vom Evaluator entschieden: 2 Lose (L7, L33).

### Beschreibend (ohne Schwelle)

- Z1 nach Losen gewichtet: 98,0 %.
- Von mindestens einem Leser als „keine Gebäudereinigung“ eingestuft: –.

### Abweichungen der Liste vom Vergleichswert (Abweichung von einer KI-Lesung; ob ein Listenfehler vorliegt, steht in `evaluation_iteration8.md`)

| Nr | Typ | Herkunft (Liste) | Liste GL | Vergleichswert GL | Leser A | Leser B | Liste Höchstende | Vergleichswert Höchstende |
|---|---|---|---|---|---|---|---|---|
| L5 | Y | enddatum | 2031-08-31 ✗ | 2029-08-31 | 2029-08-31 | 2029-08-31 | 2033-08-31 ✗ | 2031-08-31 |
| L7 | R | text_laufzeit_option | 2027-07-03 ✗ | unklar | 2027-07-03 | unbekannt | 2030-07-12 | 2030-07-12 |
| L33 | Y | enddatum | 2030-03-31 ✗ | 2029-03-31 | 2029-03-31 | 2029-03-31 | 2033-03-31 ✗ | unklar |
| L72 | Y | enddatum | 2028-08-31 | 2028-08-31 | 2028-08-31 | 2028-08-31 | 2037-08-31 ✗ | 2031-08-31 |
| L74 | R | text_laufzeit_option | 2026-06-29 | 2026-06-29 | 2026-06-29 | 2026-06-29 | 2029-07-22 ✗ | 2029-07-20 |
| L81 | Y | enddatum | 2027-11-30 ✗ | unbekannt | unbekannt | unbekannt | 2029-11-30 ✗ | unbestimmbar |
| L82 | Y | beginn_plus_dauer | 2028-10-31 | 2028-10-31 | 2028-10-31 | 2028-10-31 | 2029-10-31 ✗ | 2030-10-31 |
| L84 | R | text_laufzeit_option | 2026-06-29 | 2026-06-29 | 2026-06-29 | 2026-06-29 | 2029-07-22 ✗ | 2029-07-20 |

### Dreiervergleich mit dem Prüfer der Iteration 7 (L1–L50, Typ Y)

| Nr | Liste GL | Vergleichswert GL | Prüfer GL (Iteration 7) | Liste = Vergleich | Prüfer = Vergleich |
|---|---|---|---|---|---|
| L5 | 2031-08-31 | 2029-08-31 | 31.08.2031 | nein | nein |
| L16 | 2030-09-30 | 2030-09-30 | 31.08.2030 | ja | nein |
| L18 | 2029-12-31 | 2029-12-31 | 31.10.2029 | ja | nein |
| L24 | 2028-03-31 | 2028-03-31 | unbekannt | ja | nein |
| L25 | 2029-12-31 | 2029-12-31 | unbekannt | ja | nein |
| L26 | 2029-09-30 | 2029-09-30 | 31.12.2029 | ja | nein |
| L27 | 2029-02-28 | 2029-02-28 | unbekannt | ja | nein |
| L30 | 2028-06-30 | 2028-06-30 | 28.02.2029 | ja | nein |
| L31 | 2029-04-30 | 2029-04-30 | unbekannt | ja | nein |
| L32 | 2027-09-30 | 2027-09-30 | 30.04.2029 | ja | nein |
| L33 | 2030-03-31 | 2029-03-31 | 31.03.2030 | nein | nein |
| L38 | 2029-12-31 | 2029-12-31 | unbekannt | ja | nein |
| L44 | 2030-02-28 | 2030-02-28 | unbekannt | ja | nein |

Liste = Vergleichswert bei 45/47, Prüfer = Vergleichswert bei 34/47, Liste = Prüfer (Y1 der Iteration 7) bei 36/47. Nur Lose mit mindestens einer Abweichung sind aufgeführt.

### Kontroll-Lose 143100-2026 (Entwicklungsdaten, zählen nicht)

| Nr | Los | Liste GL | Liste Höchstende | Vergleichswert GL | Vergleichswert Höchstende |
|---|---|---|---|---|---|
| K1 | 8 | 2030-03-31 | 2031-03-31 | 2030-03-31 | 2031-03-31 |
| K2 | 9 | 2030-03-31 | 2031-03-31 | 2030-03-31 | 2031-03-31 |
| K3 | 14 | 2030-03-31 | 2031-03-31 | 2030-03-31 | 2031-03-31 |
