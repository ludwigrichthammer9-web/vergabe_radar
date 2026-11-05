# Wettbewerbsbild der 130 Oberpfalz-Lose aus TED (Paket A)

_Erzeugt von `src/prepare/wettbewerbsbild_oberpfalz.py` (Aufruf im Kopf des Skripts). Zahlen stammen aus der zugehörigen CSV `reports/wettbewerbsbild_oberpfalz.csv`. Nachtrag zu Iteration 10; Fakten (mit Quelle) und Deutung sind getrennt. Nenner aller Anteile fest 130 Lose._

## 1. Frage und Vorgehen

**Frage (Fakt, Quelle `docs/business.md` §8.9):** In den drei Gesprächen zeigte sich Zahlungsbereitschaft nur für Wettbewerbsdaten (aktueller Auftragnehmer, alte Preise, Bieterzahl), nicht für Enddaten. Welche dieser Felder lassen sich für die 130 Lose der Liste `reports/beispiel_liste_oberpfalz.csv` (64 Bekanntmachungen) aus TED ergänzen, wie vollständig und wie plausibel?

**Vorgehen (Fakt):**

- Quelle ist das eForms-XML der Zuschlagsbekanntmachung. 64 der 64 Dateien lagen lokal bzw. wurden in diesem Lauf vorgefunden; 0 wurden in diesem Lauf nach `data/raw/ted_xml/wettbewerbsbild_20261105/` nachgeladen (Pause 1,2 s). Rohdaten blieben unverändert.
- Zuordnung Los der Liste zum Los der Bekanntmachung: n-tes Los nach sortierter Kennung (wie `src/prepare/vertragsliste.py`, Regel 7), Kontrolle über den Lostitel.
- Felder: Gewinner = `efac:LotResult/efac:LotTender` → `efac:TenderingParty` → `efac:Tenderer` → `efac:Organization` (Name, Größe). Wert = `efac:LotTender/cac:LegalMonetaryTotal/cbc:PayableAmount` (Wert des Gewinnerangebots, BT-720). Zahl der Angebote = `efac:ReceivedSubmissionsStatistics` mit Code `tenders` (BT-759). Zusätzlich `cbc:HigherTenderAmount`/`cbc:LowerTenderAmount` (teuerstes/billigstes Angebot) und `cbc:TotalAmount` (Gesamtwert der Bekanntmachung, wird nicht auf Lose verteilt).
- Werte ≤ 1 € gelten als Platzhalter und werden getrennt ausgewiesen (wie `src/auftragswerte.py`). Hat ein Gewinnerangebot mehrere Lose (`TenderLot`), wird der Wert nicht einem Los zugeteilt.
- Gegenproben (nicht Quelle): Gewinnernamen und Gebotswerte der Suchabfragen `zielgruppe_oberpfalz_20261023` und `DEU_result_cpv909_20231025_20260930_lostext`.

## 2. Ergebnis: Anteil der 130 Lose je Feld (Fakten)

Quelle: `reports/wettbewerbsbild_oberpfalz.csv`, Spalten in Klammern. Nenner fest 130.

| Feld | Anteil der 130 Lose | Anmerkung |
|---|---|---|
| Bekanntmachung als XML vorhanden (`xml_vorhanden`) | 130 von 130 (100,0 %) | |
| Los der Liste einem Los im XML zugeordnet (`los_zugeordnet`) | 130 von 130 (100,0 %) | |
| … Lostitel stimmt überein (`titel_stimmt`, Kontrolle) | 130 von 130 (100,0 %) | Vergleich der ersten 40 Zeichen, normalisiert |
| … davon Lostitel im XML eindeutig (`titel_eindeutig`) | 118 von 130 (90,8 %) | Bei den übrigen kommt derselbe Titel in mehreren Losen vor; dort trägt nur die Nummer die Zuordnung |
| Zuschlag erteilt (`ergebnis_status` = selec-w) | 130 von 130 (100,0 %) | Status: selec-w: 130 |
| **Auftragnehmer genannt** (`gewinner`) | 129 von 130 (99,2 %) | |
| … davon genau ein Gewinnerangebot je Los | 129 von 130 (99,2 %) | |
| … davon mehrere Gewinner je Los (Mehrfachgewinner, `mehrfachgewinner`) | 0 von 130 (0,0 %) | Rahmenvereinbarung mit mehreren Partnern o. ä.; Werte werden je Gebot ausgewiesen |
| … davon Bietergemeinschaft als Gewinner (`bietergemeinschaft`) | 0 von 130 (0,0 %) | Mitglieder mit „ // “ verbunden |
| **Zuschlagswert je Los > 1 €** (`wert_status` = angegeben) | 62 von 130 (47,7 %) | |
| … nur Platzhalter ≤ 1 € (`platzhalter`) | 47 von 130 (36,2 %) | getrennt, nicht als Wert gezählt |
| … Wert fehlt im Gewinnerangebot (`fehlt`) | 20 von 130 (15,4 %) | |
| … Wert gilt für mehrere Lose zusammen (`gemeinsam_mehrere_lose`) | 0 von 130 (0,0 %) | nicht je Los zugeteilt |
| … mehrere Gewinner mit Werten (`angegeben_mehrere_gewinner`) | 0 von 130 (0,0 %) | Werte je Gebot in der CSV, nicht summiert |
| … ohne Gewinnerangebot (`kein_gewinnergebot`) / ohne XML | 1 von 130 (0,8 %) | |
| Wert als „nicht veröffentlicht“ gekennzeichnet (`wert_zurueckgehalten`, FieldsPrivacy `win-ten-val`) | 8 von 130 (6,2 %) | Auftraggeber hat die Veröffentlichung des Zuschlagswerts ausdrücklich ausgesetzt; kann zusätzlich zu einem Platzhalter auftreten |
| Nur Gesamtwert der Bekanntmachung bekannt, Los-Wert fehlt (`gesamtwert_bekanntmachung` > 1 €) | 16 von 130 (12,3 %) | Gesamtwert wird nicht auf Lose verteilt |
| **Zahl der Angebote angegeben, ≥ 1** (`angebote_status` = angegeben) | 79 von 130 (60,8 %) | |
| … Angabe 0 (`null`) | 0 von 130 (0,0 %) | |
| … Platzhalter/negativ (`platzhalter`) | 0 von 130 (0,0 %) | |
| … nur „elektronisch eingegangene Angebote“ angegeben (Code `t-esubm`, `nur_elektronisch`) | 51 von 130 (39,2 %) | Gesamtzahl fehlt; Zahl ist Untergrenze, nicht in der Zeile darüber gezählt |
| … Zahl der Angebote nach Gesamtzahl oder Untergrenze (Summe der beiden Zeilen) | 130 von 130 (100,0 %) | |
| … gar keine Angabe | 0 von 130 (0,0 %) | |
| Preisspanne der Angebote (billigstes/teuerstes, > 1 €; `spanne_status` = angegeben) | 0 von 130 (0,0 %) | Zusatzfeld (BT-710/711); Platzhalter (0 u. ä.) in 16 Losen |
| **Alle drei Felder je Los vorhanden** (genau ein Gewinner, Wert > 1 €, Angebote ≥ 1) | 32 von 130 (24,6 %) | |
| … dasselbe, wenn die Untergrenze (nur elektronische Angebote) als Bieterzahl genügt | 62 von 130 (47,7 %) | |
| Vertragsende aus der Liste (`vertragsende_gl`) | 92 von 130 (70,8 %) | Stufe F = ohne Ende; Herkunft in `vertragsende_herkunft` |

Aufteilung nach Veröffentlichungsjahr (Fakt; Lose / genau ein Gewinner / Wert > 1 € / Gesamtzahl der Angebote / nur elektronische Angebote):

| Jahr | Lose | Auftragnehmer | Wert | Angebote (Gesamt) | nur elektronisch |
|---|---|---|---|---|---|
| 2023 | 4 | 4 | 2 | 2 | 2 |
| 2024 | 38 | 37 | 19 | 16 | 22 |
| 2025 | 46 | 46 | 26 | 23 | 23 |
| 2026 | 42 | 42 | 15 | 38 | 4 |

## 3. Plausibilität (Fakten)

- **Gewinnernamen gegen die Suchabfrage** (`winner-name` in `zielgruppe_oberpfalz_20261023`), je Bekanntmachung: identische Namensmenge (alle Gewinner der Bekanntmachung) in 61, abweichend in 0, in der Suche ohne Namen in 3 von 64 Bekanntmachungen.
- **Gebotswerte gegen die Suchabfrage** (`tender-value` in `DEU_result_cpv909_…_lostext`), je Bekanntmachung (alle Lose der Bekanntmachung), nur Werte > 1 €: gleich in 32, abweichend in 0, beide ohne Wert in 32 von 64.
- **Verteilung der angegebenen Zuschlagswerte (je Los, n = 62):** kleinster 3.842 €, Median 197.250 €, größter 1.502.046 €.
- **Jahreswert** (Zuschlagswert geteilt durch Dauer von Beginn bis Ende der Grundlaufzeit aus der Liste, mal 12; n = 42): kleinster 2.488 €, Median 84.202 €, größter 901.599 €. Nur eine Größenordnungsprüfung: der Zuschlagswert kann die Option mit enthalten (dann ist der Jahreswert zu klein), die Dauer stammt aus der Liste (Stufe C/F möglich).
- **Wert innerhalb der Preisspanne der Angebote** (billigstes bis teuerstes Angebot, soweit beide angegeben): 0 Lose innerhalb, 0 außerhalb.
- **Gleicher Wert in mehreren Losen derselben Bekanntmachung** (Verdacht auf eingetragenen Gesamtwert): Bekanntmachungen keine.
- **Los-Wert gleich dem Gesamtwert der Bekanntmachung bei mehreren Losen der Liste:** 0 Lose.
- **Gleicher Auftragnehmer in mehreren Losen** (genau ein Gewinner): 25 Namen kommen mehrfach vor, häufigster 21 Lose.

## 4. Handabgleich von 5 Losen mit der verlinkten Bekanntmachung

**Ziehung (vorab im Skript festgelegt):** `random.Random(20261113).sample(sorted(Lose-Schlüssel), 5)`, Schlüssel = `<Bekanntmachung>|<Los dreistellig>` (Spalte `schluessel` der CSV), sortiert als Zeichenkette über alle 130 Lose.

| Schlüssel | Auftragnehmer (Skript) | Wert (Skript) | Angebote (Skript) | Ergebnis Handabgleich | Grund |
|---|---|---|---|---|---|
| [446124-2025 Los 1](https://ted.europa.eu/de/notice/-/detail/446124-2025) | Wackler Service Group GmbH & Co. KG | 1.0 | 5 | stimmt | LOT-0001, Titel gleich; Gewinner Wackler Service Group GmbH & Co. KG; PayableAmount = 1 (Platzhalter, als solcher ausgewiesen); tenders = 5. |
| [143100-2026 Los 14](https://ted.europa.eu/de/notice/-/detail/143100-2026) | Krätschmer Gebäudereinigung + Dienstleistungs-GmbH | -1.0 | 1 | stimmt | LOT-0014; Gewinner Krätschmer Gebäudereinigung + Dienstleistungs-GmbH; PayableAmount = -1 mit FieldsPrivacy win-ten-val (Wert nicht veröffentlicht); tenders = 1. Einschränkung: Lostitel „Nordbayern“ kommt mehrfach vor, die Zuordnung Los 14 = LOT-0014 beruht nur auf der Nummer. |
| [354636-2026 Los 1](https://ted.europa.eu/de/notice/-/detail/354636-2026) | Götz-Gebäudemanagement RSL GmbH | -1.0 | 8 | stimmt | LOT-0001, Titel gleich; Gewinner Götz-Gebäudemanagement RSL GmbH; PayableAmount = -1 mit win-ten-val; tenders = 8, davon t-esubm nur 2 (t-esubm ist also nicht die Gesamtzahl). |
| [687086-2025 Los 4](https://ted.europa.eu/de/notice/-/detail/687086-2025) | Albert Gebäudereinigung | 811772.64 | 6 | stimmt | LOT-0004, Titel gleich; Gewinner Albert Gebäudereinigung (Name am TenderingParty); PayableAmount = 811.772,64 €; tenders = 6. |
| [143100-2026 Los 8](https://ted.europa.eu/de/notice/-/detail/143100-2026) | Krätschmer Gebäudereinigung + Dienstleistungs-GmbH | -1.0 | 2 | stimmt | LOT-0008; Gewinner Krätschmer Gebäudereinigung + Dienstleistungs-GmbH; PayableAmount = -1 mit win-ten-val; tenders = 2. Lostitel „Nordbayern“ nicht eindeutig (wie Los 14). |

**Quelle des Vergleichs und Grenze:** Verglichen wurde mit dem Rohtext der Bekanntmachung (eForms-XML von ted.europa.eu/en/notice/<Nr>/xml, von Hand mit Textsuche gelesen, nicht mit dem Parser des Skripts). Die verlinkte HTML-Seite (ted.europa.eu/de/notice/-/detail/<Nr>) liefert beim Abruf ohne Browser keinen Inhalt (Seite wird per JavaScript aufgebaut); der Abgleich gegen die Browseransicht steht deshalb aus.

**Ergebnis:** 5 von 5 Losen stimmen (Auslesen und Zuordnung); die Platzhalter und die Zurückhaltung des Werts wurden am Rohtext ebenfalls so gefunden.

## 5. Beispiel-Wettbewerbsblatt für 3 Lose (beschreibend)

Auswahl: drei Lose mit allen drei Feldern, per `random.Random(20261114).sample` aus den 32 vollständigen Losen gezogen (nicht handverlesen). So könnte ein Eintrag aussehen; die Angaben stammen aus den verlinkten Bekanntmachungen.

**Landkreis Amberg-Sulzbach, Unterhalts-, Grund- und Zwischenreinigung** ([266771-2024, Los 1](https://ted.europa.eu/de/notice/-/detail/266771-2024))

- Aktueller Auftragnehmer: Firma Kattenbeck GmbH (Größe laut Bekanntmachung: medium)
- Zuschlagswert: 75.357 €
- Zahl der Angebote: 6, davon von KMU 1
- Vertragsende (Grundlaufzeit): keine Angabe (Herkunft: unbekannt); Höchstende nur Hinweis: –

**Universität Regensburg als staatliche Einrichtung in Vertretung des Freistaates Bayern, Unterhaltsreinigung Campus Süd** ([527230-2026, Los 1](https://ted.europa.eu/de/notice/-/detail/527230-2026))

- Aktueller Auftragnehmer: Götz-Gebäudemanagement RSL GmbH (Größe laut Bekanntmachung: large)
- Zuschlagswert: 593.384 €
- Zahl der Angebote: 3, davon von KMU 0
- Vertragsende (Grundlaufzeit): 2027-07-31 (Herkunft: beginn_plus_dauer); Höchstende nur Hinweis: –

**Stadt Neumarkt i.d.OPf., Grundschule Pölling, Sonnenstraße 17, Neumarkt i.d.OPf.** ([722423-2025, Los 1](https://ted.europa.eu/de/notice/-/detail/722423-2025))

- Aktueller Auftragnehmer: Reinigung YELL e. K. (Größe laut Bekanntmachung: micro)
- Zuschlagswert: 246.954 €
- Zahl der Angebote: 9, davon von KMU 5
- Vertragsende (Grundlaufzeit): keine Angabe (Herkunft: unbekannt); Höchstende nur Hinweis: –

## 6. Was Vergabeweiser schon zeigt und welche Lücken bleiben

**Fakten (Quelle `docs/business.md` §8.2, Tabelle, dort als „geprüft“ markiert, die API von Vergabeweiser wurde für diesen Bericht nicht aufgerufen):** Vergabeweiser zeigt je auslaufendem Vertrag Zuschlagsempfänger, Zahl der Angebote und Verlängerungsoptionen, dazu Erinnerung per E-Mail, ober- und unterschwellig, kostenlos; für Gebäudereinigung 1.005 von 10.265 Verträgen mit Ende in 12 Monaten. Nach §8.9 (Interpretation des Nutzers) zeigt Vergabeweiser auch Zuschlagssummen; das ist in §8.2 nicht belegt. AusschreibungsRadar nennt Zuschlagsempfänger und Wettbewerber-Tracking (§8.9). Einordnung in §8.4 Punkt 1.

**Deutung (nicht belegt, aus dem Vergleich):**

- Auftragnehmer und Bieterzahl sind damit **kein Alleinstellungsmerkmal**: Was TED hier liefert, bietet Vergabeweiser nach eigener Darstellung ohnehin kostenlos.
- Ein Vorsprung bliebe nur bei Feldern, die dort nicht stehen oder nicht je Los/Jahr aufbereitet sind: Zuschlagswert je Los und Jahreswert, Preisspanne der Angebote (billigstes/teuerstes), Größe/KMU-Anteil der Bieter, Mehrfachgewinner und Bietergemeinschaften. Ob Vergabeweiser diese Felder zeigt, wurde hier nicht geprüft (API nicht aufgerufen, Seite nicht ausgewertet).
- Bleibende Lücken unseres Wettbewerbsbildes: nur TED (oberhalb der EU-Schwelle), nur eForms-Zuschläge ab Oktober 2023, daher fehlen die Vorgänger der Neuausschreibungen der nächsten Jahre (`docs/business.md` §8.4 Punkt 3); Werte teils zurückgehalten oder Platzhalter (siehe Abschnitt 2); der Zuschlagswert kann Optionen einschließen; Bieterzahl ist die Zahl der eingegangenen Angebote, nicht der Bieter mit gültigem Angebot.

## 7. Grenzen

- Stichprobe ist die Oberpfalz-Liste (130 Lose, Region-Auswahl, Nische Gebäudereinigung), nicht der Markt; die Anteile gelten für diese Liste, nicht für Deutschland.
- Die Liste enthält nur Lose mit eForms-Zuschlag; ältere Bekanntmachungen haben ein anderes Format und sind nicht enthalten.
- Die Zuordnung Los der Liste zu Los im XML beruht auf Reihenfolge und Titelkontrolle (siehe `titel_stimmt`); bei abweichendem Titel ist die Zuordnung unsicher.
- Der Handabgleich (5 Lose) ist ein Stichprobenbeleg, kein Beleg für alle 130 Lose. Er prüft Auslesen und Zuordnung gegen die Bekanntmachung, nicht, ob die Angaben der Vergabestelle selbst stimmen.
- Keine Aussage über Zahlungsbereitschaft: Dass die Felder vorhanden sind, belegt keine Nachfrage (A15 bleibt ungeprüft; n = 3 Gespräche sind Hinweise).
