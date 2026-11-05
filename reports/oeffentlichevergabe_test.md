# Paket B: Abdeckungstest unterhalb der EU-Schwelle (A3), Oberpfalz

**Hinweis (2026-11-05): Die erste Auswertung (0 von 84, B1 „verfehlt“) ist ein Filterartefakt und gilt nicht; siehe reports/oeffentlichevergabe_robustheit.md und docs/iterationen.md (Ergebnis Paket B).**

Stand: 2026-11-05. Kriterien B1 bis B5 stehen vorab in `docs/iterationen.md` (Abschnitt „Paket B“) und wurden nicht geändert. Skript: `src/oeffentlichevergabe_test.py`; Ausgabe je Los: `reports/oeffentlichevergabe_test_los.csv`.

## 1. Fakten

### 1.1 Daten und Filter
- Quelle: OCDS-Jahresdateien des Bekanntmachungsservice, Open Contracting Partnership, Veröffentlichung 136, Lizenz CC0 1.0 (https://data.open-contracting.org/en/publication/136). Geladen: `2024.jsonl.gz` (122,9 MB), `2025.jsonl.gz` (126,4 MB), `2026.jsonl.gz` (124,0 MB), zusammen 373 MB, nach `data/raw/oeffentlichevergabe_20261105/` (unverändert; dazu 4 Antwortdateien der TED-Einzelabfrage in `ted_nachpruefung/`). Alle drei Downloads: HTTP 200 beim ersten Versuch. Die Open-Data-Schnittstelle von oeffentlichevergabe.de wurde nicht genutzt, die Vergabeweiser-API nicht aufgerufen.
- Inhalt: 626.620 Datensätze (2024: 220.094; 2025: 220.029; 2026: 186.497), je Datensatz ein zusammengeführtes OCDS-Release (`tag: compiled`) je Verfahren; kein Verfahren kommt in zwei Dateien vor (geprüft für die Treffermenge).
- Gelesene Felder (an Beispielsätzen geprüft): CPV `tender.items[].classification.id`; Ort `tender.items[].deliveryAddress.region` (NUTS-3); Laufzeit `tender.lots[].contractPeriod.endDate/startDate/durationInDays`; Zuschlag `awards[]` (Status, `date`, `suppliers`, `value`), `contracts[]` (`dateSigned`, `value`); Angebote `tender.numberOfTenderers`; Parteien `parties[].roles`. Ein Feld `bids.statistics` kommt im Datensatz nicht vor.
- Filter (vorab): Haupt-CPV-Präfix 90910, 90911 oder 90919 an einer Position, deren Lieferort-NUTS-3-Code DE231 bis DE23A ist, Jahre 2024 bis 2026 (Datei = Jahr der letzten Aktualisierung des Verfahrens). **84 Verfahren**, 201 Lose (Positionen).
- Phase: „Zuschlag“, wenn das Verfahren einen `awards`-Eintrag hat, sonst „Auftragsbekanntmachung“.

### 1.2 EU/national-Regel (Setzung)
Der OCDS-Datensatz enthält kein Kennzeichen für die EU-Schwelle (kein Formulartyp, kein Schwellenhinweis; `procurementMethodDetails` unterscheidet nur das Verfahren). Regel: Ein Verfahren gilt als **EU**, wenn seine Verfahrenskennung (OCDS-`tender.id`, gleich dem UUID-Teil der `ocid`) als `procedure-identifier` (BT-04) bei TED vorkommt; Quellen: die gespeicherten TED-Abfragen (`data/raw/ted_search`, 7.143 Kennungen) und, für Verfahren ohne lokalen Treffer, eine Einzelabfrage bei der TED-API (4 Verfahren, alle auf TED). Sonst „national“. Geprüft an den 64 Listen-Bekanntmachungen: Die Verfahrenskennung aus TED stimmt mit der OCDS-Kennung überein (62 von 64 gefunden, siehe B3).

### 1.3 Zahl der Verfahren (Filter, 2024 bis 2026)
| | Auftragsbekanntmachung | Zuschlag | zusammen |
|---|---|---|---|
| EU (auf TED) | 24 | 60 | 84 |
| national (nicht auf TED) | 0 | 0 | 0 |

Je Datei: 2024: 25 EU; 2025: 21 EU; 2026: 38 EU; national in keinem Jahr. Vor der Einzelabfrage bei TED sah es nach 4 nationalen Verfahren aus (alle 2026, Oktober, nach dem Ende der lokalen TED-Abfragen); alle 4 stehen auf TED (Veröffentlichung 2. bis 26. Oktober 2026).

### 1.4 B1
Anteil unterhalb der EU-Schwelle (national nach der Regel): **0/84 = 0,0 %**, Wilson 95 %: 0,0 bis 4,4 %. Schwelle ≥ 33 %: **verfehlt**. Nur Zuschlag: 0/60 (Wilson 0 bis 6,0 %); nur Auftragsbekanntmachung: 0/24 (Wilson 0 bis 13,8 %).
Zusatzmaß, nur beschreibend: Auftragswert unter der EU-Schwelle (221.000 € bis 2025, 216.000 € 2026, jeweils die höhere, subzentrale Schwelle). Ein Wert ist für 34 von 84 Verfahren lesbar (7 `tender.value`, 2 Summe `lots.value`, 25 Summe `contracts.value`, jeweils > 1 €); davon liegen **8/34 = 23,5 %** unter der Schwelle (obwohl auf TED veröffentlicht). Bandbreite über alle 84: Untergrenze 8/84 = 9,5 %, Obergrenze (alle 50 ohne Wert als unterschwellig) 58/84 = 69 %, nicht belastbar. Ob `contracts.value` den Gesamtwert oder einen Jahreswert meint, ist nicht geklärt.
Sensitivität zum Filter: 6 weitere Verfahren mit Haupt-CPV 909, deren Positionen keinen Lieferort haben, deren Auftraggeber aber in DE231 bis DE23A sitzt: alle 6 EU, mit Zuschlag. Bundesweit (Kontext) haben 856 bis 968 von etwa 2.800 CPV-909-Verfahren je Jahr keine TED-Kennung (rund 30 %); in Bayern (Lieferort DE2) 29,3 % (357/1.220, Stand vor 2026-09-01), unter den Verfahren ohne Lieferort-Angabe 61,6 % (610/990).

### 1.5 B2 Feldabdeckung (je Los; Nenner angegeben)
| Feld | unterschwellig (national) | oberschwellig (EU) |
|---|---|---|
| Lose im Filter | 0 | 201 |
| Ende oder Dauer der Laufzeit (Nenner alle Lose) | 0/0 | 193/201 = 96,0 % |
| davon Enddatum | 0/0 | 177/201 = 88,1 % |
| Lose mit aktivem Zuschlag | 0 | 123 |
| Zuschlagsempfänger in `awards.suppliers` (Nenner Lose mit Zuschlag) | 0/0 | 28/123 = 22,8 % |
| Zuschlagsempfänger in `awards.suppliers` oder `parties` mit Rolle supplier | 0/0 | 121/123 = 98,4 % |
| Zuschlagswert > 1 € in `awards.value` | 0/0 | 0/123 = 0,0 % |
| Zuschlagswert > 1 € in `awards` oder `contracts` | 0/0 | 62/123 = 50,4 % |
| Zuschlagsdatum (`awards.date` oder `contracts.dateSigned`) | 0/0 | 121/123 = 98,4 % |
| Zahl der Angebote > 0 (Verfahrensebene, `numberOfTenderers`) | 0/0 | 121/123 = 98,4 % |

Hinweis zur Zahl der Angebote: `numberOfTenderers` ist in 55 von 56 Zuschlag-Verfahren gleich der Zahl der namentlich genannten Bieter (`tender.tenderers`). Im Handabgleich (1.7) stimmte sie nur in einem von 5 Verfahren mit der Zahl der Angebote der TED-Zuschlagsbekanntmachung (`StatisticsCode tenders`) überein. Das Feld taugt nicht als Angebotszahl, die 98,4 % zeigen nur, dass es gefüllt ist.
Die Spalte „unterschwellig“ ist leer, weil es keine unterschwelligen Verfahren im Filter gibt; B2 kann für diese Gruppe daher nicht beantwortet werden.

### 1.6 B3 Überlappung mit der Liste
Die Liste (`reports/beispiel_liste_oberpfalz.csv`) hat 64 Bekanntmachungen (TED-Nummern wie 383677-2024) aus 64 verschiedenen Verfahren. Im OCDS-Datensatz steht keine TED-Nummer; die Verknüpfung läuft über die Verfahrenskennung (`procedure-identifier` aus den gespeicherten TED-Abfragen = OCDS-`tender.id`). **62 von 64 Bekanntmachungen (96,9 %)** sind im OCDS-Datensatz 2024 bis 2026 vorhanden; 58 davon fallen auch in den Filter dieses Tests (bei 4 weicht Lieferort oder CPV der Position ab). Nicht gefunden: 757285-2023 und 788951-2023 (veröffentlicht 2023, vor dem Zeitraum der geladenen Dateien). Umgekehrt: 26 EU-Verfahren im Filter stehen nicht in der Liste (u. a. Auftragsbekanntmachungen ohne Zuschlag, Verfahren ohne Lose mit Listenende); national: 0.

### 1.7 B4 Handabgleich
**Wie vorgesehen nicht durchführbar:** Es gibt 0 unterschwellige Verfahren, aus denen 5 gezogen werden könnten. Ersatz (Abweichung, offen): 5 EU-Verfahren mit Zuschlag, gezogen mit demselben Seed 20261116 (Skript), verglichen mit den Zuschlags- und Auftragsbekanntmachungen im TED-XML. Die in den Datensätzen verlinkten Seiten (deutsche-evergabe.de, evergabe.bayern.de, dtvp.de) liefern per HTTP nur eine JavaScript-Hülle (99.439 Byte, keine Inhalte) und waren nicht lesbar; der Abgleich gegen TED prüft daher die Übernahme der Felder, nicht die Plattformseite. Stichprobe: Verfahren 36f4b321 (Amberg-Sulzbach, 2024), 82c06d98 (AELF Regensburg-Schwandorf, 2026), 5338e555 (Amberg-Sulzbach, 2026), d785040a (Bundeswehr-Dienstleistungszentrum Amberg, 2026), fce86c01 (REWAG, 2025).

| Feld | stimmt |
|---|---|
| Ende der Laufzeit (`PlannedPeriod/EndDate`) | 5 von 5 |
| Zuschlags-/Vertragsdatum (OCDS-Datum gleich `SettledContract/IssueDate`) | 5 von 5; das TED-Feld `TenderResult/AwardDate` ist in 2 Fällen der Platzhalter 2000-01-01 und weicht in 1 Fall ab |
| Zuschlagswert | 4 von 4, wo ein Wert vorhanden ist (in 2 Fällen steht in beiden Quellen der Platzhalter 1 € bzw. kein Wert) |
| Zahl der Angebote | 1 von 5 (OCDS 2, 1, 1, 4 bzw. 2 gegen TED 7, 10/8, 5, 3 bzw. 4 bis 7 je Los) |

B4-Kriterium (5 von 5 gelesene Felder stimmen): **nicht prüfbar** für unterschwellige Verfahren; im Ersatz stimmen Ende, Datum und Wert, die Angebotszahl nicht.

### 1.8 B5 Machbarkeit
**Ja.** `.venv\Scripts\python.exe -I src\oeffentlichevergabe_test.py --download` lädt die drei Dateien (streamend, 5 Versuche, nicht überschreibend, Abbruch bei weniger als 3 GB frei; hier etwa 1 bis 2 Minuten); der Aufruf ohne Option wertet aus (rund 80 Sekunden, Datei streamend gelesen). Rohdaten 373 MB unverändert (`data/raw` ist in .gitignore). Die Ergebnisse waren nach Einführung der TED-Einzelabfrage in mehreren Läufen gleich. Das Skript benötigt Internet für die TED-Einzelabfrage nur beim ersten Lauf (Antworten werden gespeichert). Nicht automatisiert ist der Handabgleich B4-Ersatz (TED-XML wurde von Hand geholt).

### 1.9 Beschreibend: unterschwellige Verfahren mit Zuschlag je Jahr, Laufzeitende
0 in 2024, 0 in 2025, 0 in 2026. Ob sich dort ein Ende der Laufzeit lesen lässt: nicht beantwortbar (0/0). Für die oberschwelligen Lose im selben Datensatz: Ende oder Dauer 96,0 %.

## 2. Abweichungen von den Kriterien
1. B4 mit Ersatz-Stichprobe (EU-Verfahren, TED-XML als Quelle), weil keine unterschwelligen Verfahren existieren; die Plattformseiten waren per HTTP nicht lesbar.
2. B2 für die Gruppe „unterschwellig“ leer.
3. Die EU/national-Regel „auf TED veröffentlicht“ ist eine Setzung, die der Datensatz nicht stützt oder widerlegt (kein Schwellenfeld).
4. Zusätzlich (nicht vorab festgelegt): Wertmaß, Erweiterung des Filters um Auftraggeber-Sitz, Einzelabfrage bei TED, Kontext Bundesländer; alle nur beschreibend und als solche gekennzeichnet.
5. Zeitraum nach „Jahr der Datei“ (letzte Aktualisierung), nicht nach Zuschlagsjahr; ein 2023 gestartetes Verfahren kann fehlen.

## 3. Deutung (nicht Fakt)
- B1 ist verfehlt, deutlich: In den OCDS-Daten steht für die Oberpfalz und Gebäudereinigung kein einziges Verfahren, das nicht auch auf TED liegt. Die Hypothese „mindestens ein Drittel unterschwellig im Bekanntmachungsservice“ ist für diese Quelle nicht gestützt. Das heißt nicht, dass die Vergabestelle sich irrt: Unterschwellige Reinigungsvergaben (Beschränkte Ausschreibung, Verhandlungsvergabe) können ohne öffentliche Bekanntmachung laufen, oder auf Plattformen, die nicht in den Bekanntmachungsservice einspeisen. Der Test misst nur, was dort veröffentlicht ist.
- Die Zahl 0 ist eine Untergrenze für „unterschwellig“, weil Verfahren unter der Schwelle, die freiwillig auf TED stehen, hier als EU zählen. Nach Wert liegen mindestens 8 der 84 darunter (23,5 % der 34 mit lesbarem Wert). Selbst dieses Zusatzmaß erreicht die 33 % nicht; wegen 50 fehlender Werte ist es aber nur eine grobe Spanne, nicht belegt.
- Auffällig: Bundesweit liegt rund ein Drittel der CPV-909-Verfahren nicht bei TED, in der Oberpfalz keines (84 und 6). Mögliche Gründe (nicht geprüft): Auftraggeber dort veröffentlichen Reinigung nur oberschwellig über den Bekanntmachungsservice; fehlende Lieferorte bei nationalen Meldungen (61,6 % der nicht auf TED stehenden Verfahren haben keinen Ort, die Erweiterung fand aber nur 6 weitere, alle EU); regionale Unterschiede in der Anbindung der Plattformen.
- Für das Feld „Zahl der Angebote“ ist `numberOfTenderers` unzuverlässig; die Zuschlagswerte stehen überwiegend in `contracts`, nicht in `awards`.

## 4. Grenzen
Ein einzelner Datensatz (Bekanntmachungsservice) mit nicht einheitlicher Veröffentlichungspflicht; Filter über Haupt-CPV je Position und Lieferort je Position (Verfahren ohne Ortsangabe nur über die Erweiterung); EU/national über TED-Veröffentlichung statt über den Schwellenwert; kleine Stichprobe (84 Verfahren, 5 im Handabgleich); Zeitraum bis Anfang November 2026, späte Zuschläge fehlen; Wertfelder lückenhaft und teils Platzhalter (1 €); keine Aussage über Verfahren, die nirgends veröffentlicht werden. Keine Änderung an Liste und Messungen der Iterationen 1 bis 10.
