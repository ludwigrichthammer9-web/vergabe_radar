# Paket B: Robustheitsprüfung zu „0 von 84 Verfahren unterhalb der EU-Schwelle (Oberpfalz)“

Stand: 2026-11-05. Skript: `src/oeffentlichevergabe_robustheit.py` (neu; liest die drei OCDS-Jahresdateien streamend und unverändert; Laufzeit rund 2,5 bis 6 Minuten; Aufruf `.venv\Scripts\python.exe -I -X utf8 src\oeffentlichevergabe_robustheit.py`). Kriterien B1 bis B5 in `docs/iterationen.md` und `reports/oeffentlichevergabe_test.md` wurden nicht geändert. Vergabeweiser-API: nicht aufgerufen. Einzige Netzabfragen: TED-Suche je Verfahrenskennung für die nicht lokal gefundenen Oberpfalz-Treffer (Antworten in `data/raw/ted_nachpruefung_robustheit/`; ein HTTP 429 wurde wiederholt).

Setzung wie in Paket B: „EU“ = Verfahrenskennung steht auf TED (7.143 Kennungen aus `data/raw/ted_search` und `ted_xml`), sonst „national“. Verfahren mit Datum ab 2026-09-01 liegen hinter dem Ende der lokalen TED-Abfragen und sind in den Bundesanteilen weggelassen (Nenner jeweils angegeben).

## 1. Fakten

### 1.0 Ergebnis in einem Satz
Der Filter von Paket B (NUTS-3-Code DE231 bis DE23A am Lieferort) kann nationale Verfahren fast nie finden, weil sie im Lieferort überwiegend nur einen NUTS-1-Code („DE2“ = Bayern) tragen (Zahlen 1.1).

### 1.1 Ursache im Feld: Genauigkeit des Lieferort-Codes (Teil e des Skripts)
Haupt-CPV 909xxxxx, Datum vor 2026-09-01, ein Verfahren zählt mit seiner genauesten Position:

| Gruppe | n | kein DE-Code | NUTS-1 (z. B. DE2) | NUTS-3 (z. B. DE234) |
|---|---|---|---|---|
| national | 2.852 | 757 (26,5 %) | 2.030 (71,2 %) | 65 (2,3 %) |
| EU (auf TED) | 5.817 | 444 (7,6 %) | 0 (0,0 %) | 5.373 (92,4 %) |

Ein NUTS-2-Code kommt in keiner Gruppe vor. Wer nach NUTS-3 filtert, sieht also nur 2,3 % der nationalen, aber 92,4 % der EU-Verfahren. Bei Reinigung per Textsuche ist das Bild gleich (national 34,3 % NUTS-3, EU 92,0 %; siehe 1.2).

### 1.2 a) Bundesweit, Verfahren je Jahr (Datei) und Anteil national
Haupt-CPV 909xxxxx an einer Position (Anteil national mit Wilson 95 %):

| Jahr (Datei) | Verfahren | davon vor 2026-09-01 | national |
|---|---|---|---|
| 2024 | 3.215 | 3.215 | 1.140/3.215 = 35,5 % [33,8; 37,1] |
| 2025 | 3.128 | 3.128 | 1.085/3.128 = 34,7 % [33,0; 36,4] |
| 2026 | 3.201 | 2.326 | 627/2.326 = 27,0 % [25,2; 28,8] |
| alle | 9.544 | 8.669 | 2.852/8.669 = 32,9 % [31,9; 33,9] |

Ab 2026-09-01 weitere 875 Verfahren, davon 372 ohne lokalen TED-Treffer (unsicher, nicht eingerechnet). Mit CPV 909 als Haupt- oder Zusatz-CPV: 10.285 Verfahren, national 3.172/9.347 = 33,9 %.
Ohne CPV-Filter, Titel/Beschreibung enthält „Reinigung“: 25.936 Verfahren (2024: 8.841; 2025: 8.678; 2026: 8.417). Davon ohne jede CPV-909-Angabe 16.357; dort gelten 99,8 % als national. Dieser Wert ist nicht belastbar: Der lokale TED-Index stammt aus CPV-909-Abfragen und kennt Verfahren mit anderer CPV (z. B. Baureinigung, Kanalreinigung) nicht; „national“ ist dort nur „nicht in meinem Index“.

Merkmale der Haupt-CPV-909-Verfahren (Datum vor Grenze), Anteil mit Angabe:

| Merkmal | national (n=2.852) | EU (n=5.817) |
|---|---|---|
| (i) NUTS-Code im Lieferort (beliebige Länge, beginnt mit DE) | 2.095 = 73,5 % | 5.373 = 92,4 % |
| (i) davon NUTS-3 | 65 = 2,3 % | 5.373 = 92,4 % |
| (ii) PLZ oder Ort im Lieferort | 2.476 = 86,8 % | 4.060 = 69,8 % |
| (ii) nur PLZ | 49 = 1,7 % | 3.785 = 65,1 % |
| (iii) Auftraggeber mit Postleitzahl | 390 = 13,7 % | 5.817 = 100 % |
| (iii) Auftraggeber mit NUTS-Code | 73 = 2,6 % | 5.810 = 99,9 % |
| (iv) CPV-Angabe an einer Position | 100 % | 100 % |
| ohne jede Ortsangabe im Lieferort | 360 = 12,6 % | 439 = 7,5 % |

Der Ort steht bei nationalen Verfahren also meist als Text (Ort, Straße) im Lieferort, aber nicht als NUTS-3-Code; der Auftraggeber-Sitz fehlt bei 86,3 % der nationalen Verfahren. Die in Paket B probierte Erweiterung über den Auftraggeber-Sitz (6 Verfahren, alle EU) konnte deshalb nationale Verfahren gar nicht erfassen. Eine CPV-Angabe haben nationale Verfahren mit CPV-909-Auswahl naturgemäß immer; in der Textgruppe haben 95,5 % der nationalen irgendeine CPV (EU: 100 %).

### 1.3 b) Anteil national je Bundesland (Haupt-CPV 909, Datum vor Grenze)
Zuordnung: NUTS-Lieferort, sonst NUTS-Auftraggeber, sonst PLZ-Auftraggeber (Quellen: 7.466 / 448 / 319 / 1 Lieferort-PLZ; 435 ohne Zuordnung). PLZ-Bereich (zwei Ziffern) zu Bundesland aus dem Datensatz selbst gelernt (97 Bereiche aus 14.421 Auftraggebern; stimmt in 96,3 % mit dem häufigsten Land überein, Näherung).

| Bundesland | Verfahren | national |
|---|---|---|
| Bayern | 1.561 | 463 = 29,7 % [27,4; 32,0] |
| Nordrhein-Westfalen | 1.444 | 498 = 34,5 % |
| Niedersachsen | 819 | 326 = 39,8 % |
| Baden-Württemberg | 751 | 152 = 20,2 % |
| Hessen | 631 | 152 = 24,1 % |
| Brandenburg | 559 | 302 = 54,0 % |
| Sachsen | 424 | 13 = 3,1 % [1,8; 5,2] |
| Berlin | 417 | 91 = 21,8 % |
| Rheinland-Pfalz | 277 | 103 = 37,2 % |
| Mecklenburg-Vorpommern | 272 | 107 = 39,3 % |
| Thüringen | 265 | 46 = 17,4 % |
| Sachsen-Anhalt | 252 | 40 = 15,9 % |
| Schleswig-Holstein | 232 | 51 = 22,0 % |
| Hamburg | 177 | 46 = 26,0 % |
| Saarland | 93 | 21 = 22,6 % |
| Bremen | 60 | 6 = 10,0 % |
| ohne Ort/Sitz („unbekannt“) | 435 | 435 = 100 % |
| gesamt | 8.669 | 2.852 = 32,9 % |

Bayern liegt mit 29,7 % nicht auffällig niedrig, sondern knapp unter dem Bundesmittel; deutlich niedrig ist nur Sachsen (3,1 %).
Bayern nach Regierungsbezirk (nur wo ein NUTS-3-Code vorliegt): Oberbayern 14/575 national (2,4 %), Mittelfranken 4/132, Niederbayern 1/57, Oberfranken 0/81, Unterfranken 0/93, Schwaben 1/95, **Oberpfalz 0/79**. Daneben 407 bayerische Verfahren ohne NUTS-3 (nur „DE2“), davon 403 national (99,0 %). Das ist die Verteilung aus 1.1 in anderer Form: Auf NUTS-3-Ebene ist der nationale Anteil in jedem Regierungsbezirk nahe null, nicht nur in der Oberpfalz.
Häufigste Auftraggeber national in Bayern: Stadt Nürnberg - Zentrale Dienste (88), Bayerisches Landesamt für Steuern (56), BwDLZ Landsberg am Lech (33), Gemeinde Unterföhring (15), Stadt Landshut (11).

### 1.4 c) Oberpfalz mit breiterem Filter
**Breiter Filter** (Treffer, wenn NUTS DE231 bis DE23A bei Position oder Auftraggeber, oder PLZ 92xxx/93xxx [ohne Landkreis Kelheim 93309 bis 93359 und 93077] bei Auftraggeber oder Lieferort, oder Ortsname der Liste im Lieferort-Text, Auftraggeber-Ort oder Auftraggeber-Name; 95xxx nur mit Ort des Landkreises Tirschenreuth; Ortstreffer verworfen, wenn ein NUTS-Code außerhalb DE23 oder eine PLZ außerhalb der Regel widerspricht; Listen im Skript):

| Gruppe | Verfahren (alle Jahre) | national nach TED-Einzelabfrage |
|---|---|---|
| Haupt-CPV 909 | 141 (davon 88 im engen Filter) | 43 = 30,5 % [23,5; 38,5] |
| CPV 909 Haupt oder Zusatz | 148 | 46 = 31,1 % [24,2; 38,9] |
| ohne CPV, Text „Reinigung“ | 287 | 103 = 35,9 % [30,6; 41,6] |

(Der enge Filter liefert hier 88 statt 84 Verfahren, weil ich das volle CPV-Präfix 909 statt 90910/90911/90919 nehme.)
Von 194 Verfahren ohne lokalen TED-Treffer standen nach Einzelabfrage 89 doch auf TED, 105 nicht.

**Fehlerquelle des breiten Filters:** Er enthält Treffer, die nur über Auftraggeber-Sitz oder -Name entstehen und nicht in der Oberpfalz liegen: 31 Verfahren des Wasserstraßen- und Schifffahrtsamts Donau MDK (Sitz Regensburg, Leistungen u. a. in Straubing, Passau, Erlangen, Nürnberg), 5 des Katholischen Wohnungsbau- und Siedlungswerks (Lieferorte teils Straubing, Oberschneiding), 4 der Autobahn GmbH NL Nordbayern (Ortslisten über ganz Nordbayern), 2 des Studierendenwerks Niederbayern/Oberpfalz (Passau, Deggendorf). Von den 105 nationalen Treffern sind also mindestens etwa 40 nicht oberpfälzisch; manche Textsuche-Treffer sind keine Gebäudereinigung (z. B. Kanalreinigung, Winterdienst, Gerüstbau, Hausverwaltung).

**Strenger Filter** (nur Lieferort der Position: NUTS DE231 bis DE23A, oder PLZ 92/93, oder Ortsliste in Ort/Straße):

| Gruppe | Verfahren | national | je Jahr (Datei) national |
|---|---|---|---|
| Haupt-CPV 909 | 120 | 32 = 26,7 % [19,6; 35,2] | 2024: 8/35 = 22,9 %; 2025: 18/40 = 45,0 %; 2026: 6/45 = 13,3 % |
| CPV 909 Haupt oder Zusatz | 126 | 34 = 27,0 % [20,0; 35,3] | |
| Text „Reinigung“ | 230 | 66 = 28,7 % [23,2; 34,9] | |

Unter den 32 nationalen Haupt-CPV-909-Treffern tragen 30 am Lieferort nur den NUTS-1-Code DE2 und 2 keinen; keiner hat NUTS-3 der Oberpfalz. (Bei der Gruppe „Haupt oder Zusatz“ sind 2 nationale mit NUTS-3-Code dabei, bei „Text“ 4.) Die 2026er Zahl ist unvollständig (Zuschläge folgen, Datensatz bis Anfang November).

Beispiele für jeden der 32 nationalen Treffer (strenger Filter, Haupt-CPV 909; Auftraggeber, Titel, Jahr der Datei; gleichlautende Titel sind getrennte Verfahren, nicht dedupliziert):
- Freistaat Bayern, Bayerisches Landesamt für Steuern: Unterhalts- sowie Glas- und Rahmenreinigung LfF Weiden (2024); Glas- und Rahmenreinigung ADBV Neumarkt i.d.OPf. (2024); Unterhaltsreinigung LfF Weiden (2024, 2 Verfahren).
- IHK-Akademie in Ostbayern GmbH und IHK Regensburg: Gebäudereinigung an drei Standorten (2024; Lieferort „00000 Regensburg / Weiden“).
- Landesbaudirektion Bayern: Glasreinigung 3 Dienstgebäude in Regensburg (2024).
- Landkreis Regensburg: Jugendzeltplatz Zaar, Grund- und Unterhaltsreinigung (2024).
- Zweckverband Nahverkehr Amberg-Sulzbach: Gebäudereinigung (Unterhalts- und Glasreinigung) (2024).
- Freistaat Bayern, AELF Amberg-Neumarkt i.d.OPf.: Unterhalts- und Glasrahmenreinigung Amtsgebäude Amberg (2025, 3 Verfahren); Unterhalts- und Glasreinigung Amtsgebäude Neumarkt (2025, 3 Verfahren).
- Die Autobahn GmbH des Bundes NL Nordbayern: RV Glas-/Fensterreinigung AS Bayreuth und NL/VBZ/AS Fürth (2025; Ortslisten über Nordbayern, in der Oberpfalz nur mit einzelnen Orten, wahrscheinlich Fehltreffer).
- Gemeinde Tegernheim: Grundschule, Mensa, Turnhalle, Unterhalts- und Grundreinigung (2025, 2026); Gemeinde Wenzenbach: Baureinigungsarbeiten (2025, 2 Verfahren).
- Kassenärztliche Vereinigung Bayerns: Gebäudereinigung Betriebsstätte Regensburg und Straubing (2025).
- Regensburg Tourismus GmbH: Grundreinigung Parkettboden Veranstaltungssaal (2025).
- Stadt Regensburg: Glasreinigung (2025, 2 Verfahren); Gebäudereinigung nach DIN EN 18299, 13549 (2025); Reinigungsdienstleistungen von fünf Objekten (2025); von zwei Objekten (2026).
- Freistaat Bayern, Direktor des Amtsgerichts Cham: Gebäude- und Glasreinigung (2026).
- Klinikum St. Marien Amberg: Baureinigung GA 2 und BA 2 (2026).
- Stadt Nittenau: Gebäudereinigung Regentalhalle (2026).
Die übrigen nationalen Treffer des breiten Filters (Text „Reinigung“, ohne CPV 909, u. a. Baureinigung Stadt Cham, Markt Lappersdorf, Gemeinde Bernhardswald, Stadt Neutraubling; Polizeipräsidium Oberpfalz: Reinigungsleistungen PI Nabburg; Stadtwerke Maxhütte-Haidhof: Kanalreinigung) stehen mit Auftraggeber, Titel und Jahr in der Ausgabe des Skripts (Teil c).

### 1.5 d) Vollständigkeit der Jahresdateien (Verfahren je Monat, Monat des Feldes `date` = letzte Aktualisierung)
Datensätze: 2024: 220.094; 2025: 220.029; 2026: 186.497 (zusammen 626.620; keine doppelte `ocid` unter den ausgewerteten Kandidaten).
- 2024 je Monat: 16.808; 17.657; 17.534; 18.813; 17.484; 20.796; 19.627; 17.703; 19.443; 19.841; 17.548; 16.840.
- 2025: 16.734; 18.281; 20.638; 19.209; 16.133; 19.422; 21.823; 17.644; 18.038; 18.203; 18.467; 15.437.
- 2026: 15.046; 15.915; 20.604; 17.266; 17.672; 18.333; 18.796; 18.838; 20.381; 22.928 (Oktober); November nur 718 (bis zum Abrufstand 5. November).
Kein Monat von Januar 2024 bis November 2026 ist leer; die Streuung (15.046 bis 22.928) hat keinen auffälligen Einbruch. Jedes Verfahren steht mit seinem Stand der letzten Aktualisierung; Verfahren, deren letzter Stand vor 2024 liegt, fehlen.

## 2. Abweichungen und Grenzen
1. Die Ortszuordnung im breiten und strengen Filter ist eine Textregel (Ortsliste, PLZ-Bereiche 92/93, 95 nur mit Tirschenreuther Orten). Mehrdeutige Namen (Cham, Weiden, Neumarkt, Amberg) werden angenommen, wenn nichts widerspricht; Fehltreffer und Auslassungen sind möglich und nicht von Hand geprüft.
2. „National“ bleibt die Setzung „nicht auf TED gefunden“. Der Datensatz hat kein Schwellenfeld; „national“ heißt nicht beweisbar „unterhalb der EU-Schwelle“. Wertprüfung der 32 strengen Treffer habe ich nicht gemacht.
3. Der lokale TED-Index stammt aus CPV-909-Abfragen; für Verfahren ohne CPV 909 ist er unvollständig, deshalb Einzelabfrage bei TED für die Oberpfalz-Treffer. Die Bundesanteile der Textgruppe ohne CPV 909 (99,8 %) sind nicht belastbar.
4. Die Bundesland-Zuordnung über PLZ ist gelernt und eine Näherung; 435 Verfahren (5,0 %) ohne Ort oder Sitz fehlen in allen Ländern (alle national, weil auch diese Zuordnung scheitert).
5. Der strenge Filter kennt Mehrfachstandorte nur teilweise (IHK, KVB, Autobahn GmbH); mindestens die zwei Autobahn-Verfahren sind vermutlich keine echten Oberpfalz-Treffer. Wiederholte Ausschreibungen derselben Leistung zählen als mehrere Verfahren.
6. Gründe für unterschiedliche Anteile je Bundesland (z. B. Sachsen 3,1 %) wurden nicht untersucht.
7. Die Handprüfung (B4) und die Feldabdeckung (B2) für die nationale Gruppe wurden nicht wiederholt.

## 3. Deutung (nicht Fakt)
- Die Null ist sehr wahrscheinlich ein Artefakt des NUTS-3-Filters: 71,2 % der nationalen Haupt-CPV-909-Verfahren tragen nur DE2 (Bayern) oder einen anderen NUTS-1-Code. Die Ursache im Formular der nationalen Bekanntmachung (nur Auswahl auf Landesebene?) ist nicht geprüft.
- Mit Orten und PLZ im Lieferort liegt der nationale Anteil in der Oberpfalz bei etwa 27 % (Haupt-CPV 909) und ähnlich über dem Bundesland Bayern (29,7 %) und dem Bund (32,9 %); die Oberpfalz ist dann nicht auffällig. Das Konfidenzintervall [19,6; 35,2] schließt die B1-Schwelle von 33 % ein und die Jahre schwanken stark (13 % bis 45 %): weder Erfüllung noch Verfehlung von B1 ist damit belegt.
- Mögliche Gründe, warum Bayern nicht niedriger liegt: Kommunen und Staatsbehörden nutzen den Bekanntmachungsservice für Verfahren, die auch national sind. Diese Gründe sind nicht belegt.
- Regionale Plattformen (z. B. evergabe.bayern.de) sind in den Daten sichtbar (Links in den Verfahren), ob sie vollständig in den Bekanntmachungsservice einspeisen, zeigen die Daten nicht.

## 4. Schluss in drei Sätzen
1. Die Null in der Oberpfalz ist ein Artefakt des Filters: Nationale Verfahren tragen im Lieferort zu 71,2 % nur einen NUTS-1-Code (EU-Verfahren zu 92,4 % einen NUTS-3-Code), und mit Ort/PLZ im Lieferort stehen in der Oberpfalz 32 von 120 Haupt-CPV-909-Verfahren (26,7 %, Wilson 19,6 bis 35,2 %) nicht auf TED.
2. Zulässig ist: „Im Bekanntmachungsservice stehen auch Reinigungsverfahren mit Lieferort in der Oberpfalz, die nicht auf TED stehen (32 in 2024 bis Oktober 2026, rund ein Viertel; Wertgrenze nicht geprüft); die frühere Aussage ‚keines‘ gilt nicht“; nicht zulässig ist, B1 (≥ 33 %) als verfehlt oder als erfüllt zu bezeichnen, den Anteil unterhalb der EU-Schwelle als 0 oder als 27 % genau anzugeben, oder die Abdeckung unterschwelliger Verfahren außerhalb des Bekanntmachungsservice zu behaupten.
3. Offen bleiben Feldabdeckung und Handprüfung (B2, B4) für diese 32 nationalen Verfahren, die Wertprüfung gegen die Schwelle und die Genauigkeit der Ortsregel.
