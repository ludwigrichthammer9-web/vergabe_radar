# Make or Buy: Aufträge selbst filtern oder ein Abo kaufen

Erzeugt mit `src/report/make_or_buy.py` (reine Standardbibliothek, `.venv\Scripts\python.exe -I src\report\make_or_buy.py`). CSV mit denselben Zahlen: `reports/make_or_buy.csv`. Das Modell rechnet **Kosten eines Betriebs**. Es sagt nichts über Nachfrage, Umsatz des Projekts oder die Qualität der Daten. Kontrollrechnung im Skript: bestanden.

## 1. Fakten (mit Quelle)

| Größe | Wert | Quelle |
|---|---|---|
| Jahresumsatz je Auftrag, Median | 167.404 € (Quartile 80.367 € / 422.744 €; n = 957) | `reports/auftragswerte_909.md`, TED-Zuschläge 2024 bis 2025, Haupt-CPV 909; nur 45 % der Zuschläge haben einen plausiblen Wert |
| Laufzeit | meist 2 Jahre fest plus 1 Jahr Option, also 3 Jahre | Gespräch mit einer Vergabestelle, n = 1 (`docs/business.md` §8.9) |
| Abo-Preise | siehe Tabelle 1 | `docs/business.md` §6, §8.1, §8.2, §8.9 |

**Tabelle 1: Kaufen (Preise je Jahr, netto)**

| Angebot | Preis je Jahr | Quelle / Hinweis |
|---|---|---|
| DTAD | 1.500 € | Gespräch 2026-11-05 (Betrieb mittlerer Größe): 'knapp 1.500 €' im Jahr; n = 1 |
| subreport (unterer Preis) | 1.008 € | 84 €/Monat, Wettbewerber-Vergleich (jorpex.com), nicht beim Anbieter geprüft; zzgl. USt. |
| subreport (oberer Preis) | 2.376 € | 198 €/Monat, ebd. |
| AusschreibungsRadar Starter | 290 € | 29 €/Monat laut Preisseite (gelesen 2026-11-05); 290 €/Jahr wie vom Auftrag vorgegeben, 12 x 29 = 348 € wäre der Monatspreis; Rechnung gilt für beide Werte |
| AusschreibungsRadar Business | 948 € | 79 €/Monat laut Preisseite; hier 12 x Monatspreis |
| AusschreibungsRadar Professional | 1.490 € | 149 €/Monat laut Preisseite, mit CSV-Export; 1.490 €/Jahr wie vom Auftrag vorgegeben (12 x 149 = 1.788 €) |
| Vergabeweiser | 0 € | kostenlos (API/MCP, Limits siehe business.md §9) |

## 2. Annahmen (nicht gemessen)

| Annahme | Wert | Herkunft |
|---|---|---|
| Stundensatz (extern) | 100 €/h, Spanne 60 bis 110 €/h | Annahme; freelancermap Freelancer-Kompass 2025, Durchschnitt etwa 104 €/h, sekundär über Websuche gelesen, nicht im Original geprüft |
| Aufwand Niedrig | einmalig 20 h, laufend 5 h je Jahr (fertige JSON/CSV-Quelle in Excel laden) | Annahme, keine Messung |
| Aufwand Mittel | einmalig 60 h, laufend 20 h je Jahr (eigener Filter plus Import ins Verwaltungssystem) | Annahme, keine Messung |
| Aufwand Hoch | einmalig 120 h, laufend 50 h je Jahr (TED-API plus eigene Leseregeln plus Fehlerbehandlung) | Annahme, keine Messung |
| Marge | 5 % (Sensitivität 3 / 5 / 8 %) | Annahme |
| Kostenhorizont | 3 Jahre | Annahme (entspricht einer Vertragslaufzeit) |
| Eigene Arbeitszeit | wird mit dem Stundensatz bewertet | Annahme; ein Betrieb, der selbst baut, setzt vielleicht einen anderen Satz an |

## 3. Rechnung

**Kosten des Eigenbaus.** einmalig = Stunden einmalig × Stundensatz; laufend = Stunden je Jahr × Stundensatz; Summe über 3 Jahre = einmalig + 3 × laufend.

| Szenario | Rechenweg | einmalig | laufend je Jahr | Summe 3 Jahre |
|---|---|---|---|---|
| Niedrig | 20 h × 100 € = 2.000 €; 5 h × 100 € = 500 €; 2.000 € + 3 × 500 € | 2.000 € | 500 € | 3.500 € |
| Mittel | 60 h × 100 € = 6.000 €; 20 h × 100 € = 2.000 €; 6.000 € + 3 × 2.000 € | 6.000 € | 2.000 € | 12.000 € |
| Hoch | 120 h × 100 € = 12.000 €; 50 h × 100 € = 5.000 €; 12.000 € + 3 × 5.000 € | 12.000 € | 5.000 € | 27.000 € |

**Break-even gegen ein Abo.** Eigenbau kostet nach t Jahren einmalig + laufend × t, das Abo Preis × t. Gleichstand bei t = einmalig / (Abopreis − laufend). Ist laufend ≥ Abopreis, wird der Eigenbau nie günstiger („nie“). Gegen Vergabeweiser (0 €) ist das immer so.

| Abo (Preis je Jahr) | Niedrig | Mittel | Hoch |
|---|---|---|---|
| DTAD (1.500 €) | 2,0 Jahre = 2.000 € / (1.500 € − 500 €) | nie | nie |
| subreport (unterer Preis) (1.008 €) | 3,9 Jahre (> 3) = 2.000 € / (1.008 € − 500 €) | nie | nie |
| subreport (oberer Preis) (2.376 €) | 1,1 Jahre = 2.000 € / (2.376 € − 500 €) | 16,0 Jahre (> 3) = 6.000 € / (2.376 € − 2.000 €) | nie |
| AusschreibungsRadar Starter (290 €) | nie | nie | nie |
| AusschreibungsRadar Business (948 €) | 4,5 Jahre (> 3) = 2.000 € / (948 € − 500 €) | nie | nie |
| AusschreibungsRadar Professional (1.490 €) | 2,0 Jahre = 2.000 € / (1.490 € − 500 €) | nie | nie |
| Vergabeweiser (0 €) | nie | nie | nie |

**Zusätzliche Aufträge, die der frühe Hinweis erbringen müsste.** Deckungsbeitrag je Auftrag = Jahresumsatz × Marge × Laufzeit = 167.404 € × 0,05 × 3 = 25.111 € (exakt 25.110,60 €). Zusätzliche Aufträge = Kosten der ersten drei Jahre / Deckungsbeitrag je Auftrag. Gemeint sind Aufträge, die der Betrieb **ohne** den Hinweis nicht gewonnen hätte.

| Szenario | Kosten 3 Jahre | Marge 3 % (15.066 €) | Marge 5 % (25.111 €) | Marge 8 % (40.177 €) |
|---|---|---|---|---|
| Niedrig | 3.500 € | 0,23 | 0,14 | 0,09 |
| Mittel | 12.000 € | 0,80 | 0,48 | 0,30 |
| Hoch | 27.000 € | 1,79 | 1,08 | 0,67 |

Dasselbe mit den Quartilen des Jahresumsatzes (Marge 5 %, Laufzeit 3 Jahre):

| Szenario | unteres Quartil (80.367 €) | Median | oberes Quartil (422.744 €) |
|---|---|---|---|
| Niedrig | 0,29 | 0,14 | 0,06 |
| Mittel | 1,00 | 0,48 | 0,19 |
| Hoch | 2,24 | 1,08 | 0,43 |

Sensitivität Stundensatz (Summe 3 Jahre):

| Szenario | 60 €/h | 100 €/h | 110 €/h |
|---|---|---|---|
| Niedrig | 2.100 € | 3.500 € | 3.850 € |
| Mittel | 7.200 € | 12.000 € | 13.200 € |
| Hoch | 16.200 € | 27.000 € | 29.700 € |

Kontrolle: Niedrig 2.000 € / 500 € / 3.500 €, Break-even gegen DTAD 2,0 Jahre; Mittel 6.000 € / 2.000 € / 12.000 €; Hoch 12.000 € / 5.000 € / 27.000 €; zusätzliche Aufträge 0,14 / 0,48 / 1,08 (Marge 5 %). Alle Werte oben stimmen (im Skript als Assertion geprüft).

## 3a. Symmetrische Variante: auch bei Abo und kostenlosen Diensten fallen Stunden an

Das Basismodell (Abschnitt 3) rechnet Abos und kostenlose Dienste **ohne Eigenaufwand** und den Eigenbau **mit** Stunden. Daraus folgt „gegen kostenlose Dienste ist Eigenbau nie günstiger“ **aus der Konstruktion des Modells**, nicht aus einer Messung. Die symmetrische Variante gibt auch den Alternativen Stunden (alles Annahmen, keine Messung). Das Basismodell bleibt unverändert (Abschnitt 3).

| Annahme | Wert |
|---|---|
| Nutzung bei Abo und bei kostenlosem Dienst mit Übernahme von Hand (Alerts lesen, Treffer ins eigene System übertragen) | 10 h je Jahr (Niedrig), 30 h je Jahr (Mittel), 60 h je Jahr (Hoch), je Szenario |
| Kostenlosen Dienst nutzen und selbst importieren | 20 h einmalig plus 10 h je Jahr (derselbe Importaufwand wie Eigenbau Niedrig; die Nutzung ist darin enthalten, nicht doppelt gezählt) |
| Eigenbau | unverändert wie im Basismodell (laufende Stunden enthalten Pflege und Nutzung) |
| Alternative je Jahr | Abopreis + Nutzungsstunden × 100 € |

**Break-even, Basismodell / symmetrische Variante** (Jahre bis der Eigenbau günstiger ist; „von Beginn an“ = nie teurer, „nie“ = nie günstiger, „(> 3)“ = jenseits des Horizonts):

| Alternative | Niedrig: Basis / symmetrisch | Mittel: Basis / symmetrisch | Hoch: Basis / symmetrisch |
|---|---|---|---|
| DTAD (1.500 €) | 2,0 / 1,0 | nie / 2,4 | nie / 4,8 (> 3) |
| subreport (unterer Preis) (1.008 €) | 3,9 (> 3) / 1,3 | nie / 3,0 | nie / 6,0 (> 3) |
| subreport (oberer Preis) (2.376 €) | 1,1 / 0,7 | 16,0 (> 3) / 1,8 | nie / 3,6 (> 3) |
| AusschreibungsRadar Starter (290 €) | nie / 2,5 | nie / 4,7 (> 3) | nie / 9,3 (> 3) |
| AusschreibungsRadar Business (948 €) | 4,5 (> 3) / 1,4 | nie / 3,1 (> 3) | nie / 6,2 (> 3) |
| AusschreibungsRadar Professional (1.490 €) | 2,0 / 1,0 | nie / 2,4 | nie / 4,8 (> 3) |
| Vergabeweiser (0 €) | nie / 4,0 (> 3) / von Beginn an (Hand / Import) | nie / 6,0 (> 3) / nie (Hand / Import) | nie / 12,0 (> 3) / nie (Hand / Import) |

**Kosten in 3 Jahren, symmetrische Variante** (einmalig + 3 × laufend; Eigenbau zum Vergleich):

| Weg | Niedrig | Mittel | Hoch |
|---|---|---|---|
| Eigenbau | 3.500 € | 12.000 € | 27.000 € |
| DTAD | 7.500 € | 13.500 € | 22.500 € |
| subreport (unterer Preis) | 6.024 € | 12.024 € | 21.024 € |
| subreport (oberer Preis) | 10.128 € | 16.128 € | 25.128 € |
| AusschreibungsRadar Starter | 3.870 € | 9.870 € | 18.870 € |
| AusschreibungsRadar Business | 5.844 € | 11.844 € | 20.844 € |
| AusschreibungsRadar Professional | 7.470 € | 13.470 € | 22.470 € |
| Kostenloser Dienst (Vergabeweiser, AusschreibungsRadar Free), Treffer von Hand übernehmen | 3.000 € | 9.000 € | 18.000 € |
| Kostenloser Dienst, Treffer selbst importieren | 5.000 € | 5.000 € | 5.000 € |

Kontrolle der symmetrischen Variante (im Skript als Assertion): DTAD 1,0 / 2,4 / 4,8 Jahre; kostenloser Dienst von Hand 4,0 / 6,0 / 12,0 Jahre; kostenloser Dienst mit Import: Niedrig von Beginn an, Mittel und Hoch nie.

## 4. Deutung (Interpretation, keine Fakten)

- **Im Basismodell ist Eigenbau gegen kostenlose Dienste nie günstiger (Modellkonstruktion, Annahmen, keine Messung).** Vergabeweiser (API/MCP) kostet 0 € und wird im Basismodell ohne Eigenaufwand gerechnet, der Eigenbau mit Stunden; das Ergebnis folgt aus dieser Konstruktion. Dasselbe gilt für AusschreibungsRadar Starter (laufende Eigenkosten von 500 € und mehr liegen über 290 € bzw. 348 € im Jahr).
- **Symmetrische Variante (Abschnitt 3a):** Gibt man auch Abo und kostenlosen Diensten Nutzungsstunden, wird der Eigenbau gegen DTAD schon im Niedrig-Szenario nach 1,0 Jahren und im Mittel-Szenario nach 2,4 Jahren günstiger; gegen einen kostenlosen Dienst mit Übernahme von Hand erst nach 4,0 / 6,0 / 12,0 Jahren. Gegen einen kostenlosen Dienst mit eigenem Import ist der Eigenbau Niedrig von Beginn an nicht teurer, weil der Importaufwand dort dem Eigenbau Niedrig gleich angesetzt ist und nur die laufenden Stunden höher (10 h gegen 5 h); diese Annahme trägt das Ergebnis. Die Ergebnisse hängen an den angenommenen Stunden. **Die Aussage, die beide Varianten tragen: Der Preis ist kein Vorteil des Eigenbaus.** Sie sagt nicht, dass der Eigenbau teuer wäre.
- **Im Basismodell rechnet sich Eigenbau gegen ein Abo wie DTAD nur im Niedrig-Szenario** und erst nach 2,0 Jahren. Im Mittel- und Hoch-Szenario übersteigen die laufenden Eigenkosten (2.000 € bzw. 5.000 €) den Abopreis von 1.500 € im Jahr. Gegen den oberen subreport-Preis (2.376 € im Jahr) wäre der Eigenbau im Niedrig-Szenario nach 1,1 Jahren günstiger; im Mittel-Szenario erst nach rund 16 Jahren, im Hoch-Szenario nie.
- Gegen AusschreibungsRadar Professional (1.490 € im Jahr, einzige Stufe mit CSV-Export) gilt dasselbe wie gegen DTAD: nur im Niedrig-Szenario, nach 2,0 Jahren; gegen Business (948 €) erst nach 4,5 Jahren.
- **Ein Abo kauft nicht nur Daten**, sondern auch Pflege, Suchprofile und Alarme. Der Eigenbau muss diese Arbeit selbst leisten; das Modell bewertet sie nur über den Stundensatz.
- **Die Rechnung „zusätzliche Aufträge“ ist eine Größenordnung, kein Nutzenbeleg.** Selbst im Hoch-Szenario genügt rechnerisch etwa ein zusätzlicher Auftrag in drei Jahren, im Niedrig-Szenario ein siebtel. Ob ein früher Hinweis auch nur einen Auftrag zusätzlich bringt, ist nicht belegt (A1, A15; Gespräche n = 3, gespalten). Die Marge von 5 % ist eine Annahme; bei 3 % steigt die Zahl im Hoch-Szenario auf 1,79.
- **Folgerung:** Ein Mehrwert gegenüber den kostenlosen Wegen müsste aus **Funktion** kommen (zum Beispiel Daten mit festem Schema im eigenen System, Anreicherung), nicht aus dem Preis. „Keine Abo-Kosten“ ist kein Vorteil an sich: Kostenlose Wege bestehen, und die Eigenleistung kostet Stunden (Basismodell und symmetrische Variante).

### Nutzenseite: die Kosten sind klein gegen einen Auftrag

Gemessen an einem Auftrag (Deckungsbeitrag 25.111 € in drei Jahren bei 5 % Marge) sind die Kosten des Eigenbaus klein: Sie entsprechen 0,14 bis 1,08 zusätzlichen Aufträgen (Niedrig bis Hoch). Das zeigt, dass **nicht die Kostenfrage entscheidet**, sondern die Frage, ob ein früher Hinweis überhaupt einen Auftrag bringt (**nicht belegt**; A1, A15). „Deckungsbeitrag“ steht hier für Umsatz × Marge, **ohne** Angebotsaufwand und **ohne** Zuschlagswahrscheinlichkeit. Der Median des Jahresumsatzes gilt nur für TED-Aufträge mit plausiblem Wert (47,7 % in der Oberpfalz-Liste: 62 von 130 Losen).

## 5. Grenzen

- Alle Aufwandswerte und die Marge sind Annahmen; die Spanne der Szenarien ist weit (3.500 bis 27.000 € in drei Jahren) und nicht aus einer Umsetzung abgeleitet.
- Symmetrische Variante: Dass der Eigenbau laufend weniger Stunden braucht (5 / 20 / 50 h) als die Nutzung eines Dienstes (10 / 30 / 60 h), ist eine nicht begründete Annahme; sie bestimmt, ob der Eigenbau in 3a günstiger erscheint. Beide Varianten sind Modellkonstruktionen.
- Der Stundensatz stammt aus einer sekundären Quelle (Freiberufler-Durchschnitt), nicht aus der Kostenrechnung eines Reinigungsbetriebs; ein Betrieb mit freier Büro-Kapazität rechnet anders.
- Der Median des Jahresumsatzes gilt für TED-Aufträge mit plausiblem Wert (45 %); kleine Betriebe und unterschwellige Aufträge sind nicht abgebildet.
- Die Rechnung vergleicht Kosten, nicht Funktionen: Die Dienste unterscheiden sich in Abdeckung, Alarmen und Bedienung. Eine Abdeckungsaussage (zum Beispiel 'TED reicht') folgt daraus nicht; 26,7 % der Oberpfälzer Reinigungsverfahren im Bekanntmachungsservice standen nicht auf TED (Wilson 19,6 bis 35,2 %).
- AusschreibungsRadar-Jahrespreise: Die Werte 290 € und 1.490 € sind vom Auftrag vorgegeben; Monatspreise × 12 wären 348 € und 1.788 €. An den Ergebnissen („nie“) ändert das nichts.

