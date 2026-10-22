# Datenqualität TED-Zuschlagsbekanntmachungen DEU

Zeitraum (Veröffentlichung): **22.07.2026 – 21.10.2026** · Bekanntmachungen: **15.706** ·Download: 2026-10-22T12:12 UTC

Query: `buyer-country=DEU AND form-type=result AND publication-date>=20260722 AND publication-date<=20261021`

## 1. Überblick

| Notice-Typ   |   Anzahl | Anteil   |
|:-------------|---------:|:---------|
| can-standard |    15301 | 97,4 %   |
| can-social   |      275 | 1,8 %    |
| can-desg     |      127 | 0,8 %    |
| can-tran     |        3 | 0,0 %    |

| Vertragsart   |   Anzahl | Anteil   |
|:--------------|---------:|:---------|
| services      |     6527 | 41,6 %   |
| works         |     5538 | 35,3 %   |
| supplies      |     3641 | 23,2 %   |

2.409 Bekanntmachungen (15,3 %) haben mehr als ein Los.

## 2. Befüllungsgrad der Kernkategorien

Eine Kategorie gilt als befüllt, wenn mindestens eines ihrer Felder in mindestens einem Los einen echten Wert hat (`-1` zählt nicht).

| Kategorie             | befüllt   |   Anzahl |
|:----------------------|:----------|---------:|
| Vertragslaufzeit      | 86,4 %    |    13569 |
| Verlängerungsoptionen | 30,5 %    |     4794 |
| CPV-Code              | 100,0 %   |    15706 |
| Auftraggeber          | 100,0 %   |    15706 |
| Auftragswert          | 70,8 %    |    11123 |

### Einzelfelder

| Kategorie             | Feld                               | Bedeutung                                                | befüllt   | enthält `-1`   |
|:----------------------|:-----------------------------------|:---------------------------------------------------------|:----------|:---------------|
| Vertragslaufzeit      | `contract-duration-period-lot`     | BT-36 Laufzeit (Dauer)                                   | 21,3 %    |                |
| Vertragslaufzeit      | `contract-duration-start-date-lot` | BT-536 Laufzeitbeginn                                    | 62,3 %    |                |
| Vertragslaufzeit      | `contract-duration-end-date-lot`   | BT-537 Laufzeitende                                      | 60,8 %    |                |
| Vertragslaufzeit      | `contract-duration-period-oth-lot` | BT-538 Laufzeit sonstige (z. B. unbefristet)             | 4,2 %     |                |
| Verlängerungsoptionen | `renewal-maximum-lot`              | BT-58 max. Anzahl Verlängerungen                         | 18,9 %    |                |
| Verlängerungsoptionen | `renewal-description-lot`          | BT-57 Beschreibung Verlängerung                          | 10,8 %    |                |
| Verlängerungsoptionen | `option-description-lot`           | BT-54 Beschreibung Optionen                              | 19,0 %    |                |
| CPV-Code              | `main-classification-proc`         | BT-262 Haupt-CPV (Verfahren)                             | 100,0 %   |                |
| CPV-Code              | `main-classification-lot`          | BT-262 Haupt-CPV (Los)                                   | 100,0 %   |                |
| CPV-Code              | `classification-cpv`               | alle CPV-Codes                                           | 100,0 %   |                |
| Auftraggeber          | `buyer-name`                       | BT-500 Name Auftraggeber                                 | 100,0 %   |                |
| Auftragswert          | `total-value`                      | Gesamtwert, von TED berechnet (BT-161, sonst abgeleitet) | 68,6 %    | 0,6 %          |
| Auftragswert          | `result-value-lot`                 | BT-709 Höchstwert Rahmenvertrag (Los)                    | 5,2 %     | 5,4 %          |
| Auftragswert          | `tender-value`                     | BT-720 Wert des Zuschlagsangebots                        | 61,9 %    | 20,1 %         |
| Auftragswert          | `estimated-value-proc`             | BT-27 geschätzter Wert (Verfahren)                       | 14,6 %    | 0,0 %          |
| Auftragswert          | `estimated-value-lot`              | BT-27 geschätzter Wert (Los)                             | 8,5 %     | 0,0 %          |
| Auftragswert          | `framework-maximum-value-lot`      | Höchstwert Rahmenvereinbarung (Los)                      | 2,7 %     | 0,0 %          |

### Zusatzkennzahlen für die Prognose

| Kennzahl                                                    | Anteil   |
|:------------------------------------------------------------|:---------|
| Laufzeitende (BT-537) **oder** Dauer (BT-36) vorhanden      | 82,0 %   |
| Beginn **und** Ende vorhanden                               | 60,3 %   |
| Laufzeit „sonstige“ (meist UNLIMITED/UNKNOWN)               | 4,2 %    |
| BT-58 vorhanden (auch `0`)                                  | 18,9 %   |
| BT-58 > 0 (mind. eine Verlängerung möglich)                 | 14,7 %   |
| mind. ein Wertfeld enthält `-1` (Wert nicht veröffentlicht) | 25,6 %   |
| **plausibler Auftragswert** (mind. ein Wertfeld > 1 €)      | 58,8 %   |

Laufzeit laut BT-36 (erstes Los, n = 3.349): Median **24 Monate**, 25 %-Quantil 8, 75 %-Quantil 48 Monate.

## 3. Häufigste CPV-Bereiche (Haupt-CPV der Bekanntmachung)

### CPV-Abteilungen (2-stellig), Top 20

|   Abteilung | Bezeichnung                                                                                               |   Anzahl | Anteil   |
|------------:|:----------------------------------------------------------------------------------------------------------|---------:|:---------|
|          45 | Bauarbeiten                                                                                               |     5538 | 35,3 %   |
|          71 | Dienstleistungen von Architektur-, Konstruktions- und Ingenieurbüros und Prüfstellen                      |     2699 | 17,2 %   |
|          90 | Abwasser- und Abfallbeseitigungs-, Reinigungs- und Umweltschutzdienste                                    |      948 | 6,0 %    |
|          34 | Transportmittel und Erzeugnisse für Verkehrszwecke                                                        |      863 | 5,5 %    |
|          72 | IT-Dienste: Beratung, Software-Entwicklung, Internet und Hilfestellung                                    |      575 | 3,7 %    |
|          79 | Dienstleistungen für Unternehmen: Recht, Marketing, Consulting, Einstellungen, Druck und Sicherheit       |      548 | 3,5 %    |
|          48 | Softwarepaket und Informationssysteme                                                                     |      375 | 2,4 %    |
|          33 | Medizinische Ausrüstungen, Arzneimittel und Körperpflegeprodukte                                          |      372 | 2,4 %    |
|          09 | Mineralölerzeugnisse, Brennstoff, Elektrizität und andere Energiequellen                                  |      321 | 2,0 %    |
|          38 | Laborgeräte, optische Geräte und Präzisionsgeräte (außer Gläser)                                          |      303 | 1,9 %    |
|          80 | Allgemeine und berufliche Bildung                                                                         |      284 | 1,8 %    |
|          60 | Transport- und Beförderungsdienstleistungen (außer Abfalltransport)                                       |      258 | 1,6 %    |
|          50 | Reparatur- und Wartungsdienste                                                                            |      234 | 1,5 %    |
|          30 | Maschinen, Material und Zubehör für Büro und Computer, außer Möbeln und Softwarepaketen                   |      213 | 1,4 %    |
|          39 | Möbel (einschließlich Büromöbel), Zubehör, Haushaltsgeräte (ausgenommen Beleuchtung) und Reinigungsmittel |      198 | 1,3 %    |
|          77 | Dienstleistungen in Landwirtschaft, Forstwirtschft, Gartenbau, Aquakultur und Bienenzucht                 |      164 | 1,0 %    |
|          42 | Industrielle Maschinen                                                                                    |      158 | 1,0 %    |
|          35 | Ausrüstung für Sicherheitszwecke, Brandbekämpfung, Polizei und Verteidigung                               |      141 | 0,9 %    |
|          31 | Elektrische Maschinen, Geräte, Ausstattung und Verbrauchsartikel; Beleuchtung                             |      139 | 0,9 %    |
|          85 | Dienstleistungen des Gesundheits- und Sozialwesens                                                        |      136 | 0,9 %    |

### CPV-Gruppen (3-stellig), Top 25

|   Gruppe | Bezeichnung                                                                                    |   Anzahl | Anteil   |
|---------:|:-----------------------------------------------------------------------------------------------|---------:|:---------|
|      452 | Komplett- oder Teilbauleistungen im Hochbau sowie Tiefbauarbeiten                              |     2158 | 13,7 %   |
|      453 | Bauinstallationsarbeiten                                                                       |     1179 | 7,5 %    |
|      454 | Baufertigstellung                                                                              |     1056 | 6,7 %    |
|      713 | Dienstleistungen von Ingenieurbüros                                                            |     1050 | 6,7 %    |
|      710 | Dienstleistungen von Architektur-, Konstruktions- und Ingenieurbüros und Prüfstellen           |      766 | 4,9 %    |
|      450 | Bauarbeiten                                                                                    |      735 | 4,7 %    |
|      712 | Dienstleistungen von Architekturbüros                                                          |      647 | 4,1 %    |
|      341 | Kraftfahrzeuge                                                                                 |      589 | 3,8 %    |
|      909 | Reinigungs- und Hygienedienste                                                                 |      440 | 2,8 %    |
|      451 | Baureifmachung                                                                                 |      410 | 2,6 %    |
|      720 | IT-Dienste: Beratung, Software-Entwicklung, Internet und Hilfestellung                         |      268 | 1,7 %    |
|      722 | Softwareprogrammierung und -beratung                                                           |      255 | 1,6 %    |
|      905 | Dienstleistungen im Zusammenhang mit Siedlungs- und anderen Abfällen                           |      207 | 1,3 %    |
|      601 | Straßentransport/-beförderung                                                                  |      200 | 1,3 %    |
|      480 | Softwarepaket und Informationssysteme                                                          |      184 | 1,2 %    |
|      336 | Arzneimittel                                                                                   |      181 | 1,2 %    |
|      093 | Elektrizität, Heizung, Sonnen- und Kernenergie                                                 |      174 | 1,1 %    |
|      906 | Reinigung und Sanierung des städtischen und ländlichen Raumes, und zugehörige Dienstleistungen |      164 | 1,0 %    |
|      804 | Erwachsenenbildung und sonstiger Unterricht                                                    |      158 | 1,0 %    |
|      715 | Dienstleistungen im Bauwesen                                                                   |      153 | 1,0 %    |
|      331 | Medizinische Geräte                                                                            |      151 | 1,0 %    |
|      797 | Dienstleistungen von Detekteien und Sicherheitsdiensten                                        |      145 | 0,9 %    |
|      302 | Computeranlagen und Zubehör                                                                    |      145 | 0,9 %    |
|      091 | Brennstoffe                                                                                    |      125 | 0,8 %    |
|      391 | Möbel                                                                                          |      123 | 0,8 %    |

## 4. Befüllungsgrad je CPV-Abteilung (Top 15)

Beantwortet: Welche Kategorien sind häufig **und** gut befüllt?

|   Abt. | Bezeichnung                                                  |   Anzahl | Laufzeit   | Ende/Dauer   | Verlängerung   | BT-58 > 0   | Wert   | Wert > 1 €   |
|-------:|:-------------------------------------------------------------|---------:|:-----------|:-------------|:---------------|:------------|:-------|:-------------|
|     45 | Bauarbeiten                                                  |     5538 | 87,7 %     | 84,6 %       | 9,0 %          | 1,5 %       | 77,5 % | 71,2 %       |
|     71 | Dienstleistungen von Architektur-, Konstruktions- und Ingeni |     2699 | 83,3 %     | 76,7 %       | 43,0 %         | 12,7 %      | 72,8 % | 55,4 %       |
|     90 | Abwasser- und Abfallbeseitigungs-, Reinigungs- und Umweltsch |      948 | 94,0 %     | 90,8 %       | 61,2 %         | 39,3 %      | 64,0 % | 49,6 %       |
|     34 | Transportmittel und Erzeugnisse für Verkehrszwecke           |      863 | 80,4 %     | 72,1 %       | 23,8 %         | 7,5 %       | 63,8 % | 51,4 %       |
|     72 | IT-Dienste: Beratung, Software-Entwicklung, Internet und Hil |      575 | 83,1 %     | 78,6 %       | 45,4 %         | 34,3 %      | 70,3 % | 52,7 %       |
|     79 | Dienstleistungen für Unternehmen: Recht, Marketing, Consulti |      548 | 91,2 %     | 88,5 %       | 57,7 %         | 38,9 %      | 72,1 % | 54,9 %       |
|     48 | Softwarepaket und Informationssysteme                        |      375 | 87,7 %     | 79,5 %       | 32,5 %         | 20,8 %      | 68,8 % | 52,0 %       |
|     33 | Medizinische Ausrüstungen, Arzneimittel und Körperpflegeprod |      372 | 85,5 %     | 82,8 %       | 26,1 %         | 19,1 %      | 73,7 % | 32,5 %       |
|     09 | Mineralölerzeugnisse, Brennstoff, Elektrizität und andere En |      321 | 91,0 %     | 89,7 %       | 27,7 %         | 19,6 %      | 81,0 % | 66,0 %       |
|     38 | Laborgeräte, optische Geräte und Präzisionsgeräte (außer Glä |      303 | 66,7 %     | 57,4 %       | 11,9 %         | 3,6 %       | 66,7 % | 51,2 %       |
|     80 | Allgemeine und berufliche Bildung                            |      284 | 87,7 %     | 87,7 %       | 78,2 %         | 13,4 %      | 26,8 % | 23,9 %       |
|     60 | Transport- und Beförderungsdienstleistungen (außer Abfalltra |      258 | 85,3 %     | 84,1 %       | 50,0 %         | 26,0 %      | 69,4 % | 47,7 %       |
|     50 | Reparatur- und Wartungsdienste                               |      234 | 92,7 %     | 91,0 %       | 53,4 %         | 40,6 %      | 62,0 % | 50,0 %       |
|     30 | Maschinen, Material und Zubehör für Büro und Computer, außer |      213 | 81,7 %     | 77,5 %       | 33,8 %         | 23,0 %      | 65,3 % | 57,3 %       |
|     39 | Möbel (einschließlich Büromöbel), Zubehör, Haushaltsgeräte ( |      198 | 78,8 %     | 74,7 %       | 26,8 %         | 15,7 %      | 68,2 % | 60,6 %       |

### Beispiel-Nischen aus CLAUDE.md

| Nische                                       |   Anzahl (3 Monate) | Laufzeit   | Ende/Dauer   | Verlängerung   | BT-58 > 0   | Wert   | Wert > 1 €   |   Median-Laufzeit BT-36 (Mon.) |
|:---------------------------------------------|--------------------:|:-----------|:-------------|:---------------|:------------|:-------|:-------------|-------------------------------:|
| Gebäudereinigung (CPV 909…)                  |                 440 | 93,9 %     | 90,0 %       | 65,2 %         | 42,0 %      | 62,7 % | 51,4 %       |                             24 |
| Winterdienst (CPV 90620000, 90630000)        |                 129 | 97,7 %     | 93,0 %       | 55,0 %         | 33,3 %      | 64,3 % | 51,9 %       |                             48 |
| IT-Dienste (CPV 72…)                         |                 575 | 83,1 %     | 78,6 %       | 45,4 %         | 34,3 %      | 70,3 % | 52,7 %       |                             48 |
| IT-Wartung/Support (CPV 503…, 7225…, 72267…) |                  47 | 87,2 %     | 83,0 %       | 38,3 %         | 29,8 %      | 70,2 % | 53,2 %       |                             36 |
| Sicherheitsdienste (CPV 7971…)               |                 137 | 95,6 %     | 93,4 %       | 77,4 %         | 42,3 %      | 62,0 % | 32,8 %       |                             24 |

## 5. Laufzeit aus Beginn und Ende (BT-536/BT-537)

BT-36 (Dauer) ist nur bei rund 21 % befüllt. Hier wird die Laufzeit zusätzlich aus Beginn und Ende des ersten Loses berechnet (Ende − Beginn + 1 Tag, in Monaten à 30,44 Tage). Werte ≤ 0 oder > 240 Monate gelten als unplausibel und werden ausgeschlossen.

**Laufzeitende bestimmbar** heißt: Enddatum (BT-537) vorhanden **oder** Beginn (BT-536) und Dauer (BT-36) vorhanden. Das ist strenger als „Ende/Dauer“ in Abschnitt 2 und 4, wo eine Dauer ohne Beginn mitzählt.

### Gesamt (Monate)

| Quelle        | Anteil   |     n |   Median |   25 % |   75 % |
|:--------------|:---------|------:|---------:|-------:|-------:|
| BT-36 Dauer   | 21,3 %   | 3.349 |       24 |      8 |     48 |
| Ende − Beginn | 60,2 %   | 9.459 |       16 |      7 |     36 |

Laufzeitende bestimmbar: **61,7 %** aller Notices. Unplausible Datumspaare ausgeschlossen: 14. Notices mit BT-36 **und** Datumspaar: 10, davon stimmen 40,0 % auf ±1 Monat überein.

### Je Beispielnische (Monate)

| Nische                                       |   n | Ende bestimmbar   |   BT-36: n |   BT-36: Median |   Datum: n |   Datum: Median |   Datum: 25 % |   Datum: 75 % |
|:---------------------------------------------|----:|:------------------|-----------:|----------------:|-----------:|----------------:|--------------:|--------------:|
| Gebäudereinigung (CPV 909…)                  | 440 | 80,9 %            |         45 |              24 |        350 |              36 |            24 |            48 |
| Winterdienst (CPV 90620000, 90630000)        | 129 | 84,5 %            |         11 |              48 |        109 |              36 |            17 |            47 |
| IT-Dienste (CPV 72…)                         | 575 | 33,7 %            |        264 |              48 |        185 |              36 |            18 |            48 |
| IT-Wartung/Support (CPV 503…, 7225…, 72267…) |  47 | 29,8 %            |         25 |              36 |         14 |              44 |            25 |            48 |
| Sicherheitsdienste (CPV 7971…)               | 137 | 83,9 %            |         13 |              24 |        115 |              24 |            13 |            48 |

## 6. Methodische Hinweise

- **Ebene:** Ausgewertet wird pro Bekanntmachung. Lot-Felder sind Listen; „befüllt“ heißt: mindestens ein Los hat einen Wert. Ob *alle* Lose befüllt sind, ist hier nicht geprüft.
- **`-1`:** Wertfelder enthalten oft `-1`. Wir werten das als Platzhalter für „nicht veröffentlicht“ und zählen es als nicht befüllt.
- **Platzhalterwerte:** Zusätzlich tragen viele Vergabestellen `0` oder `0,01 €` ein (z. B. 505084-2026: Gesamtwert 0,00 €, Angebot 0,01 €). Diese zählen in Abschnitt 2 als „befüllt“. Realistischer ist die Kennzahl „plausibler Auftragswert (> 1 €)“.
- **`total-value` ist nicht BT-161:** TED berechnet dieses Feld auch, wenn die Bekanntmachung keinen Gesamtwert (BT-161) enthält (Stichprobe 573266-2026, siehe reports/stichprobe_iteration1.md). Seine Befüllungsquote überschätzt daher, wie oft Vergabestellen selbst einen Gesamtwert angeben.
- **Verlängerungen oft nur als Freitext:** In 505084-2026 stehen zwei Verlängerungsjahre nur in BT-54 (Optionen-Text), BT-58 ist leer. Für die Prognose müssen Verlängerungen also aus dem Text extrahiert werden.
- **Verlängerungen:** Ein fehlendes Verlängerungsfeld kann eine Datenlücke sein, aber auch „es gibt keine Verlängerung“ bedeuten. Der Befüllungsgrad ist hier also keine reine Datenqualitätskennzahl. Ein vorhandenes BT-58 = `0` bedeutet ausdrücklich „keine Verlängerung“.
- **Haupt-CPV:** `main-classification-proc`, ersatzweise das erste Los. Bei Bekanntmachungen mit vielen Losen verschiedener Branchen wird nur der Haupt-Code gezählt.
- **Auswahl:** `form-type=result` (can-standard, can-social, can-desg, can-tran). Vertragsänderungen (can-modif) und Ex-ante-Transparenz (veat) sind nicht enthalten.
- **CPV-Bezeichnungen:** offizielle CPV-2008-Liste aus dem eForms SDK (https://raw.githubusercontent.com/OP-TED/eForms-SDK/develop/codelists/cpv.gc).
