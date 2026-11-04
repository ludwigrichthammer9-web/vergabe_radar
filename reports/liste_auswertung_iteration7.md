# Auswertung der Prüfung der Vertragsliste (Iteration 7, Y1, Y1r, Y2, Y2b)

_Erzeugt mit `src/prepare/auswertung_iteration7.py`. Schlüssel-Hash geprüft: `eade66c0…df9b` = vorab festgehaltener Wert. Eingaben des Prüfers aus der abgegebenen Datei in `reports/liste_pruefung_iteration7_urteile.csv` (erste Abgabe) und `reports/liste_nachpruefung_iteration7_urteile.csv` (Nachprüfung, ersetzt die erste Abgabe, wo ein Eintrag vorliegt) übertragen. Typ Y nur L1 bis L50 (Kürzung, vor dem Ergebnis festgelegt), Typ R alle 15._

## Fakten

- **Y1 (47 Zufallslose, Ende der Grundlaufzeit): 36/47 = 76,6 % (Wilson 62,8–86,4)** (Schwelle ≥ 90 %).
- **Y1r (15 Regelwirkungs-Lose): 8/15 = 53,3 % (Wilson 30,1–75,2)** (Schwelle ≥ 12/15).
- **Y2 (Höchstende korrekt oder „unbestimmbar“): 29/47 = 61,7 % (Wilson 47,4–74,2)** (Schwelle ≥ 90 %).
- **Y2b (nur Lose, bei denen die Liste ein Höchstende nennt): 24/42 = 57,1 % (Wilson 42,2–70,9)** (Schwelle ≥ 85 %).
- Abweichungen bei Y1 (Typ Y): 11, davon 6 mit Prüfereintrag „unbekannt“ und 5 mit abweichendem Datum. Typ R: 7, davon 0 „unbekannt“.
- Quelle: {'Text': 27, 'Feld': 34, 'abweichend': 2, 'unbekannt': 32}. Bei Losen mit Nachprüfung hat der Prüfer die Quelle nicht eingetragen; sie ist von Claude nach fester Regel abgeleitet (`quelle_ableiten`). Hilfsmittel (nur erste Abgabe): {'Kalenderberechnung': 16, 'keine': 79}. In der Nachprüfung ist das Feld Hilfsmittel bei allen Einträgen leer; der Prüfer gab im Gespräch an, keine Hilfsmittel benutzt zu haben (nur Selbstangabe).
- Nachprüfung: 38 Lose mit Eintrag, 4 Lose im Umfang ohne Eintrag (L25, L27, L31, L38; es bleibt der Eintrag der ersten Abgabe). Prüfzeit: erste Abgabe Summe 143 Minuten (Median 1), Nachprüfung 65 Minuten. Sitzungstabellen (Start und Ende) liegen nicht vor.

- Y2 und Y2b mit Vorbehalt: In 15 der 47 Lose steht in der ersten Abgabe „unbestimmbar“, weil das Ende der Grundlaufzeit damals fehlte; die Nachprüfung lieferte es, das Höchstende wurde nicht neu eingetragen (nur bei Änderung gefordert). Ohne diese veralteten Einträge: Y2 29/32 = 90,6 % (Wilson 75,8–96,8), Y2b 24/27 = 88,9 % (Wilson 71,9–96,1).

### Beschreibend (ohne Schwelle)

- Y1 nach Losen gewichtet: 80,2 %.
- Y1 nur für Lose mit Quelle „Text“ (Typ Y): 12/12 = 100,0 % (Wilson 75,7–100,0).
- Gesamtschätzung für das Fenster = (128 · 0.533 + 2.796 · 0.766) / 2.924 = 75,6 %.

### Y1 nach Herkunft des Enddatums der Liste

| Typ | Herkunft | Lose | korrekt | davon Prüfer „unbekannt“ |
|---|---|---|---|---|
| R | text_laufzeit_option | 15 | 8 | 0 |
| Y | beginn_plus_dauer | 1 | 0 | 1 |
| Y | enddatum | 45 | 35 | 5 |
| Y | text_zunaechst | 1 | 1 | 0 |

### Abweichungen mit abweichendem Datum

| L | Notice, Los | Typ | Liste: Ende GL (Herkunft) | Prüfer: Ende GL | Prüfer: Ende (Feld) |
|---|---|---|---|---|---|
| L16 | 423541-2026, 2 | Y | 2030-09-30 (enddatum) | 31.08.2030 | 31.08.2030 |
| L18 | 787336-2025, 10 | Y | 2029-12-31 (enddatum) | 31.10.2029 | 31.12.2029 |
| L26 | 650531-2026, 2 | Y | 2029-09-30 (enddatum) | 31.12.2029 | 31.12.2029 |
| L30 | 444388-2026, 1 | Y | 2028-06-30 (enddatum) | 28.02.2029 | 28.02.2029 |
| L32 | 581750-2026, 1 | Y | 2027-09-30 (enddatum) | 30.04.2029 | 30.04.2029 |
| L3 | 108370-2024, 1 | R | 2024-12-31 (text_laufzeit_option) | 31.12.2027 | 31.12.2027 |
| L7 | 340183-2026, 1 | R | 2027-07-03 (text_laufzeit_option) | 12.07.2030 | 12.07.2030 |
| L49 | 104444-2024, 1 | R | 2024-12-31 (text_laufzeit_option) | 31.12.2027 | 31.12.2027 |
| L57 | 340183-2026, 2 | R | 2027-07-03 (text_laufzeit_option) | 12.07.2030 | 12.07.2030 |
| L62 | 108077-2024, 1 | R | 2025-02-28 (text_laufzeit_option) | 29.02.2028 | 29.02.2028 |
| L65 | 360180-2025, 1 | R | 2026-06-29 (text_laufzeit_option) | 22.07.2029 | 22.07.2029 |
| L88 | 360180-2025, 2 | R | 2026-06-29 (text_laufzeit_option) | 22.07.2029 | 22.07.2029 |

### Abweichungen bei Y2

| L | Notice, Los | Liste: Höchstende (Herkunft) | Prüfer: Höchstende |
|---|---|---|---|
| L5 | 538350-2026, 3 | 2033-08-31 (anzahl_x_laenge) | unbestimmbar |
| L11 | 813327-2025, 1 | 2030-03-31 (anzahl_x_laenge) | unbestimmbar |
| L12 | 427959-2026, 1 | 2030-08-31 (anzahl_x_laenge) | unbestimmbar |
| L17 | 326312-2026, 1 | 2031-10-31 (anzahl_x_laenge) | unbestimmbar |
| L18 | 787336-2025, 10 | 2031-12-31 (anzahl_x_laenge) | unbestimmbar |
| L20 | 771566-2025, 1 | 2030-12-31 (anzahl_x_laenge) | unbestimmbar |
| L21 | 403178-2026, 2 | 2031-08-31 (anzahl_x_laenge) | unbestimmbar |
| L24 | 109604-2026, 3 | 2031-03-31 (anzahl_x_laenge) | unbestimmbar |
| L27 | 116801-2026, 6 | 2031-02-28 (anzahl_x_laenge) | unbestimmbar |
| L31 | 253014-2026, 1 | 2031-04-30 (anzahl_x_laenge) | unbestimmbar |
| L32 | 581750-2026, 1 | 2030-09-30 (anzahl_x_laenge) | unbestimmbar |
| L33 | 112593-2026, 1 | 2033-03-31 (hoechstlaufzeit_text) | unbestimmbar |
| L34 | 460218-2026, 5 | 2030-06-30 (anzahl_x_laenge) | unbestimmbar |
| L35 | 831847-2025, 2 | 2030-01-31 (anzahl_x_laenge) | unbestimmbar |
| L38 | 787336-2025, 7 | 2031-12-31 (anzahl_x_laenge) | unbestimmbar |
| L41 | 397515-2026, 1 | 2031-06-30 (keine_angabe) | unbestimmbar |
| L42 | 655547-2025, 3 | 2029-11-30 (anzahl_x_laenge) | unbestimmbar |
| L45 | 612858-2026, 1 | 2030-09-30 (anzahl_x_laenge) | unbestimmbar |
