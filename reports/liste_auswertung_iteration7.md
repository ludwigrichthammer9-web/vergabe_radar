# Auswertung der Prüfung der Vertragsliste (Iteration 7, Y1, Y1r, Y2, Y2b)

_Erzeugt mit `src/prepare/auswertung_iteration7.py`. Schlüssel-Hash geprüft: `eade66c0…df9b` = vorab festgehaltener Wert. Eingaben des Prüfers aus der abgegebenen Datei in `reports/liste_pruefung_iteration7_urteile.csv` übertragen._

## Fakten

- **Y1 (80 Zufallslose, Ende der Grundlaufzeit): 20/80 = 25,0 % (Wilson 16,8–35,5)** (Schwelle ≥ 72/80 = 90 %).
- **Y1r (15 Regelwirkungs-Lose): 10/15 = 66,7 % (Wilson 41,7–84,8)** (Schwelle ≥ 12/15).
- **Y2 (Höchstende korrekt oder „unbestimmbar“): 52/80 = 65,0 % (Wilson 54,1–74,5)** (Schwelle ≥ 90 %).
- **Y2b (nur Lose, bei denen die Liste ein Höchstende nennt): 44/72 = 61,1 % (Wilson 49,6–71,5)** (Schwelle ≥ 85 %).
- Abweichungen bei Y1 (Typ Y): 60, davon 60 mit Prüfereintrag „unbekannt“ und 0 mit abweichendem Datum. Typ R: 5, davon 5 „unbekannt“.
- Quelle laut Prüfer: {'Text': 76, 'unbekannt': 19}. Hilfsmittel: {'Kalender': 14, 'keine': 81}.
- Prüfzeit je Los: Median 1 Minuten, Summe 137 Minuten für 95 Lose. Eine Sitzungstabelle (Start und Ende) liegt in der abgegebenen Datei nicht vor.

### Beschreibend (ohne Schwelle)

- Y1 nach Losen gewichtet: 29,7 %.
- Y1 nur für Lose mit Quelle „Text“ (Typ Y): 20/61 = 32,8 % (Wilson 22,3–45,3).
- Gesamtschätzung für das Fenster = (128 · 0.667 + 2.796 · 0.250) / 2.924 = 26,8 %.

### Y1 nach Herkunft des Enddatums der Liste

| Typ | Herkunft | Lose | korrekt | davon Prüfer „unbekannt“ |
|---|---|---|---|---|
| R | text_laufzeit_option | 15 | 10 | 5 |
| Y | beginn_plus_dauer | 2 | 0 | 2 |
| Y | enddatum | 76 | 18 | 58 |
| Y | text_zunaechst | 2 | 2 | 0 |

### Abweichungen mit abweichendem Datum

| L | Notice, Los | Typ | Liste: Ende GL (Herkunft) | Prüfer: Ende GL |
|---|---|---|---|---|

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
| L42 | 655547-2025, 3 | 2029-11-30 (anzahl_x_laenge) | unbestimmbar |
| L45 | 612858-2026, 1 | 2030-09-30 (anzahl_x_laenge) | unbestimmbar |
| L54 | 209475-2026, 1 | 2030-03-31 (anzahl_x_laenge) | unbestimmbar |
| L56 | 325043-2026, 1 | 2031-06-30 (anzahl_x_laenge) | unbestimmbar |
| L60 | 1971-2026, 2 | 2031-03-31 (anzahl_x_laenge) | unbestimmbar |
| L61 | 821096-2025, 1 | 2029-07-31 (anzahl_x_laenge) | unbestimmbar |
| L71 | 341885-2026, 1 | 2033-05-31 (hoechstlaufzeit_text) | unbestimmbar |
| L72 | 557125-2026, 1 | 2037-08-31 (anzahl_x_laenge) | 31.08.2031 |
| L76 | 771566-2025, 3 | 2030-12-31 (anzahl_x_laenge) | unbestimmbar |
| L78 | 688875-2025, 1 | 2029-10-31 (keine_angabe) | unbestimmbar |
| L81 | 10154-2026, 2 | 2029-11-30 (anzahl_x_laenge) | unbestimmbar |
| L82 | 707425-2025, 1 | 2029-10-31 (anzahl_x_laenge) | 31.10.2030 |
| L85 | 269152-2026, 1 | 2033-07-31 (hoechstlaufzeit_text) | unbestimmbar |

## Interpretation (Vorbehalt: Gültigkeit der Prüfung offen)

- **Kein einziges abweichendes Datum:** Wo der Prüfer ein Ende der Grundlaufzeit eintrug (30 Einträge), stimmt die Liste in allen Fällen. Die Y1-Quote entsteht allein durch Einträge „unbekannt“ (65).
- 60 dieser Einträge betreffen Lose, deren Ende die Liste aus den Feldern der Bekanntmachung (BT-537 bzw. Beginn + Dauer) nimmt. Die Vorlage zeigt diese Felder absichtlich nicht (kein Verankern an der Liste); sie sind nur im Original auf TED sichtbar. Die Quelle „Feld“ wurde kein einziges Mal vergeben (Quellen: {'Text': 76, 'unbekannt': 19}), die mittlere Prüfzeit liegt bei 1 Minute je Los. Das spricht dafür, dass die Originale nicht geöffnet wurden und nur die Auszüge der Vorlage gelesen wurden. Dann misst Y1 hier nicht die Genauigkeit der Liste, sondern wie viele Laufzeiten im Auszug stehen.
- Y2: 26 von 28 Abweichungen sind Folgefehler derselben Ursache (Liste nennt ein Höchstende aus Anzahl × Länge, der Prüfer kennt das Ende der Grundlaufzeit nicht und trägt „unbestimmbar“ ein). Echte Abweichungen mit Datum: L72, L82.
- Belastbar sind nur: die Treffer bei den Datumsangaben des Prüfers, die Y2-Abweichungen mit Datum und die Zahl der Lose, deren Laufzeit im Auszug steht. Ob Y1 erfüllt ist, lässt sich mit dieser Eingabe nicht entscheiden; dafür müssten die Lose mit „unbekannt“ im Original geprüft werden.

