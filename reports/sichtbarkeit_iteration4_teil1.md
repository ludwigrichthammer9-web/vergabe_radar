# Sichtbarkeit der Vorgänger – Handsuche Iteration 4, Teil 1 (U1–U14)

- **Datum:** 2026-10-25
- **Bearbeiter:** Subagent `rechercheur` (Auftrag „Handsuche“)
- **Testfälle:** Zeilen 1–14 aus `reports/testfaelle_iteration4.txt` (U1–U14 in dieser Reihenfolge; Titel und Auftraggeber laut `reports/testfaelle_iteration4.md`)
- **Rohdaten dieses Teils:** `data/raw/rechercheur_20261025/U1/` bis `U14/` (jede API-Antwort als `api_NN.json` mit der Anfrage in `api_NN_request.json`, jede XML als `<Notice>.xml`, unverändert)

## Definitionen

- Kategorien nach `reports/urteilsregeln_blindpruefung.md`, **Version 1.1** (vor dem ersten Fall vollständig gelesen, einschließlich der Kalibrierungsbeispiele).
- Ergebnis je Fall: `objektgleich_hoch`, `objektgleich_mittel`, `teilmenge`, `unklar` (mit Tendenz), `kein_vorgaenger`.
- Begriffe (Population, Vorgänger-Quellen, Vorgänger-Ende mit Herkunft, korrekt) nach `docs/iterationen.md`, Abschnitt „Iteration 4“.
- Vorgänger-Quellen: Zuschläge (`form-type=result`) und frühere Ausschreibungen (`form-type=competition`) auf TED, veröffentlicht ab 2016-10-01 und vor dem Testfall.
- **Zeitabstand, Vertragsende, Laufzeit und Auftragswert sind nicht in das Urteil eingeflossen, auch nicht in die Tendenz.** Laufzeiten stehen nur in den getrennten Zeilen „Vorgänger-Ende“ und „vorzeitige Neuvergabe“, die erst nach dem Urteil ausgefüllt wurden.

## Bestätigung der Unabhängigkeit

Gelesen habe ich nur: `reports/testfaelle_iteration4.txt` und `.md`, `reports/urteilsregeln_blindpruefung.md`, `docs/iterationen.md` (Abschnitt Iteration 4; eine Stichwortsuche nach „Iteration 4“ zeigte zusätzlich einzelne Zeilen anderer Abschnitte derselben Datei), die erlaubten Rohdaten unter `data/raw/ted_search/` (die fünf genannten Ordner, gefiltert auf 2016-10-01 bis Vortag des Testfalls), die TED-API und die TED-XML.
Nicht gelesen: alle Dateien der Leseverbotslisten (u. a. `src/zuordnung_*.py`, `src/objekt_merkmale.py`, `src/los_merkmale.py`, `src/testprobe_iteration4.py`, `data/processed/`, `data/raw/ted_ft/`, alle `reports/zuordnung_*`, `k2_*`, `blindpruefung_*`, `regel_entwicklung_*`, `evaluation_*`, `sichtbarkeit_iteration3_*`, `testfaelle_iteration3*`, `dev_gesehene_q1_notices.txt`, `bekannte_notices_iteration4.txt`, `vorgaenger_ende_iteration3_korrektur.csv`). Ich kenne die Zuordnungsregel nicht und habe nicht versucht, ihre Logik nachzubilden. Hinweis: `reports/testfaelle_iteration4.md` zeigt in der Tabelle auch die Titel von U15–U36. Diese Fälle habe ich nicht bearbeitet.

## Vorgehen und Konventionen

1. **Testfall lesen:** XML des Testfalls geladen (liegt im jeweiligen Fallordner). Diese XML zählt **nicht** zum Budget von 10 XML.
2. **Suche A/B lokal:** Die erlaubten Rohdaten sind genau die Antworten der Suchen `buyer-country=DEU AND form-type=result|competition AND classification-cpv=909*` ab 2016-10-01. Ich habe sie zu einem Index zusammengeführt (Hilfsskript im Scratchpad, nicht im Projekt) und mit regulären Ausdrücken auf Auftraggebername, Ort, Titel, Los-Titel, Los-Beschreibung und Leistungsort durchsucht, jeweils nur Notices vom 2016-10-01 bis zum Vortag des Testfalls. Diese lokalen Abfragen ersetzen die API-Abfragen der Suchen A und B, sie zählen **nicht** zum Budget von 15 API-Abfragen und sind je Fall als „lokal“ protokolliert. Einschränkung: Vor eForms enthalten die lokalen Daten keine Titel und Texte, daher findet die lokale Suche dort nur Auftraggeber und Ort.
3. **Suche C über die API:** `POST https://api.ted.europa.eu/v3/notices/search`, Volltext mit `FT~"…"`, meist mit `buyer-country=DEU`, `classification-cpv=909*` und `publication-date>=20161001 AND publication-date<[Testfalldatum]`. Ergebnis aus den Probeabfragen dieses Teils (Fakten mit Beleg):
   - `FT~` findet auch Bekanntmachungen vor eForms (z. B. U4 `api_11`: `FT~"WE2714"` findet 625281-2022).
   - `FT~` arbeitet mit Wortstämmen bzw. Teilwörtern: `FT~"Karlskron"` findet auch die schwedische Stadt Karlskrona (U2 `api_01`, 115 Treffer). Ab U3 deshalb immer mit `buyer-country=DEU`.
   - **Die Syntax `FT~("A" OR "B")` liefert stets 0 Treffer** (Gegenprobe U9 `api_04`: `FT~("Jenaplanschule" OR "Barbara Grundschule") … buyer-city=Rostock` ergibt 0, `FT~"Jenaplanschule" AND buyer-city=Rostock` in U7 `api_01` dagegen 1). Die zwei Abfragen mit dieser Syntax (U4 `api_05`, U9 `api_03`) sind ungültig. Sie stehen im Protokoll, zählen zum Budget und wurden durch Einzelabfragen ersetzt.
   - `buyer-name~"…"` funktioniert als Filter (U6 `api_03`, U13 `api_01` bis `api_06`).
4. **Kandidaten prüfen:** XML über `https://ted.europa.eu/en/notice/<Nummer>/xml` geladen, deutschsprachige Inhaltsfelder ausgelesen (Titel, Lose, Leistungsort, Beschreibung, Laufzeit, Verlängerung, Verweis auf die Ausschreibung `NOTICE_NUMBER_OJ`). Vergleich nach Urteilsregeln 1.1, Stufen A, B, C.
5. **Zählweise „Abfragen/XML“:** API-Abfragen dieses Falls / geöffnete Kandidaten-XML (ohne Testfall-XML). Lokale Abfragen werden getrennt genannt.
6. **Vorgänger-Ende:** nach dem Urteil, aus Vorgänger mit Vertrag (Zuschlag). Fehlt der Zuschlag auf TED, steht die geplante Laufzeit aus der Ausschreibung mit diesem Hinweis. Angegeben werden das Ende der Grundlaufzeit (`grundlaufzeit`) und, falls genannt, das Höchstende (`hoechstende`). Bei „unklar“ werden die Laufzeitangaben des Kandidaten nur informativ genannt.
7. **Vorzeitige Neuvergabe:** „ja“, wenn der geplante Beginn des Testfalls mindestens 3 Monate vor dem Ende der Grundlaufzeit des Vorgängers liegt.
8. Alle Zitate stammen aus der jeweiligen XML (gekürzt mit „…“).

---

## Protokoll je Fall

### U1 – 152665-2026 (2026-03-05) – 1.102.3 Zentrale Verwaltungsdienste, Statistik und Wahlen – Hansestadt Lübeck – Der Bürgermeister
- **Objekt(e):** keine Objektliste. Verfahren „Unterhalts-, Grund-, und Sonderreinigungen für div. Objekte im Stadtgebiet der Hansestadt Lübeck“, 3 Lose mit identischem Text „Unterhalts-, Ferien-, Grund- und Sonderreinigungen für verschiedene Schul- und Bürostandorte im Stadtgebiet Lübeck“; Leistungsort nur „Lübeck“. Keine Flächen, keine Adressen.
- **Leistungsart (je Los):** Lose 1–3: Unterhalts-, Ferien-, Grund- und Sonderreinigung (CPV 90911200, 90919000).
- **Suchschritte:**
  - lokal: `buyer ~ /l(ü|ue)beck/`, 2016-10-01 bis 2026-03-04 → 39 Treffer, darunter dieselbe Vergabestelle: 393360/427817/433324-2025 (competition), 471736-2025 (result), 526136/538529/582515-2025 (competition, wortgleicher Titel), 691234-2025 (result), sowie die Hansestadt (Bereich 5.061.2) mit 152544-2022, 235138-2023, 82724-2024, 714838-2024 (Glas), 166054/201559-2025 (Viermastbark Passat).
  - API `api_01`: `FT~"Bürostandorte" AND buyer-city=Lübeck AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260305` → 8 Treffer (die genannten 2025er Notices der Vergabestelle 1.102.3).
  - XML geöffnet: 691234-2025, 235138-2023, 152544-2022.
- **A (Identität):** nicht vergleichbar. Details: U1 nennt keine Objekte, Flächen oder Adressen. 691234-2025 nennt zwei Lose mit je 8 Standorten (z. B. „Schule Lauerholz (Grundschule) … Burgtorfriedhof (Verwaltungsbüros)“).
- **B (Objektraum):** nicht eindeutig erkennbar (Grenzfall). Details: Beide Seiten nennen wortgleich „verschiedene Schul- und Bürostandorte im Stadtgebiet Lübeck“ und dieselben Leistungsarten. Gebiet ist nur die ganze Stadt. Dieselbe Stadt schreibt mehrere Schulpakete mit ähnlicher Objektart aus (235138-2023: Schulen in Buntekuh, Innenstadt, St. Jürgen, Marli; 152544-2022: Hanse Schule, Dorothea-Schlözer-Schule, Gewerbeschule). Ob „Schul- und Bürostandorte im Stadtgebiet“ als erkennbare Objektart mit Gebiet gilt, regeln die Urteilsregeln nicht eindeutig.
- **C (Stütze):** Auftraggeber ja (gleiche Vergabestelle 1.102.3), CPV ja (90911200, 90919000), Titel ähnlich (Losbeschreibung wortgleich), Losstruktur anders (3 Lose gegenüber 2).
- **Überschneidung der Objekte:** nicht bestimmbar (Liste nur auf der Kandidatenseite).
- **Ergebnis:** unklar
- **Tendenz:** eher dafür. Wortgleiche Leistungs- und Objektbeschreibung derselben Vergabestelle mit denselben Leistungsarten. Dagegen spricht nur der andere Losschnitt (Stufe C, kein Widerspruch).
- **Kandidat:** 691234-2025 (result, eForms, 2025-10-21), zugehörige Ausschreibungen 526136-2025, 538529-2025, 582515-2025 (competition, eForms, gleiche Verfahrenskennung 87939461-…). Ein inhaltlich fast gleiches Vorverfahren desselben Jahres: 393360-2025 / 471736-2025 (18 statt 16 Standorte).
- **Beleg:** 691234-2025, `ProcurementProject/Name`: „Unterhalts-, Ferien-, Grund- und Sonderreinigungen für verschiedene Schul- und Bürostandorte im Stadtgebiet Lübeck“; U1, Los-`Description`: wortgleich „… für verschiedene Schul- und Bürostandorte im Stadtgebiet Lübeck“.
- **Vorgänger mit Vertrag:** (Kandidat) 691234-2025
- **Vorgänger-Ende:** nur informativ für den Kandidaten: 2027-07-31 (grundlaufzeit); „einmalige Option auf Verlängerung um zwei Jahre bis zum 31.07.2029“ (hoechstende).
- **Hinweis auf vorzeitige Neuvergabe:** unklar (falls dasselbe Objekt: ja, Beginn U1 2026-08-01 liegt fast 12 Monate vor 2027-07-31).
- **Abfragen/XML:** 1/3 (lokal: 1)

### U2 – 213443-2026 (2026-03-27) – Gemeinde Karlskron
- **Objekt(e):** 1 Los mit 7 Objekten: Kindergarten St. Josef – Haus Regenbogen, Bürgermeister-Stoll-Straße 2 (335,04 m²); Kindergarten St. Josef – Haus Sonnenschein, Bürgermeister-Stoll-Straße 2 (871,50 m²); Kinderkrippe Kinderland, Hauptstraße 26 (500,56 m²); Kindergarten Farbenfroh, Hauptstraße 24 (1.077,74 m²); Freiherr-von-Hertling Grund- und Mittelschule, Bürgermeister-Stoll-Straße 1 (4.290,06 m²); dieselbe Schule – Sporthalle (1.818,30 m²); Rathaus Karlskron, Hauptstraße 34 (605,35 m², nur VR). Gesamt 9.498,55 m², alle in 85123 Karlskron.
- **Leistungsart (je Los):** Los 1: Unterhalts-, Grund- und Vertretungsreinigung (UR, GR, VR).
- **Suchschritte:**
  - lokal: `buyer ~ /karlskron/` → 2 Treffer (270164-2022 competition, 444675-2022 result); `city ~ /karlskron/` → dieselben 2; `any ~ /karlskron|85123/` → 5 (zusätzlich 3 nicht einschlägige: Stadtwerke Offenbach, BImA Berlin).
  - API `api_01`: `FT~"Karlskron" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260327` → 115 Treffer (Stammsuche trifft Karlskrona/Schweden); deutsche Treffer nur 270164-2022 und 444675-2022.
  - XML geöffnet: 270164-2022, 444675-2022.
- **A (Identität):** übereinstimmend (Objektliste, Gebäudenamen), Fläche abweichend. Details: Alle 7 Objekte stehen 2022 in Los 1 mit gleicher Adresse und Leistung (die Kita Hauptstraße 24 heißt 2022 „Kindertagesstätte“, 2026 „Kindergarten Farbenfroh“). Flächen gleich bei Regenbogen (333,31 / 335,04 m², 0,5 %), Kinderland (500,56 / 500,56), Hauptstraße 24 (1.077,74 / 1.077,74), Rathaus (605,35 / 605,35); abweichend bei Haus Sonnenschein (515,33 / 871,50), Schule (2.785,84 / 4.290,06) und Sporthalle (1.707,87 / 1.818,30, 6 %).
- **B (Objektraum):** erkennbar und übereinstimmend. Details: Gemeinde Karlskron, Kitas, Schule mit Sporthalle, Rathaus; UR, GR, VR.
- **C (Stütze):** Auftraggeber ja, CPV ja (90911200), Titel ähnlich (wortgleich „Ausschreibung Gebäudereinigung - Gemeinde Karlskron“), Losstruktur anders (2022: Los 1 UR/VR/GR + Los 2 Glas; 2026: nur 1 Los).
- **Überschneidung der Objekte:** 7 von 7 (Los 1 von 2022; beide Seiten). Das Glaslos 2022 (Los 2) ist eine andere Leistungsart und hat in U2 keine Entsprechung. Verglichen wurde Los 1.
- **Ergebnis:** objektgleich_mittel (zwei A-Merkmale stimmen überein, „hoch“ ist aber ausgeschlossen, weil die Flächen bei 3 von 7 Objekten um mehr als 2 % abweichen)
- **Vorgänger:** 270164-2022 (competition, vor eForms, 2022-05-20) und 444675-2022 (result, vor eForms, 2022-08-12), jeweils Los 1.
- **Beleg:** 270164-2022, Los 1 `SHORT_DESCR`: „Kindergarten St. Josef Haus Regenbogen Bürgermeister-Stoll-Straße 2, 85123 Karlskron Leistungen: UR, GR Bodenfläche: 333,31 m² … Rathaus Karlskron Hauptstraße 34 … Leistung: VR Bodenfläche: 605,35 m²“.
- **Vorgänger mit Vertrag:** 444675-2022 (Los 1 an MBR Gebäudemanagement GmbH, Vertragsschluss 2022-07-25)
- **Vorgänger-Ende:** 2024-08-31 (grundlaufzeit, 270164-2022 `DATE_END`); 2026-08-31 (hoechstende: „Er endet in jedem Fall automatisch nach 4 Jahren am 31.8.2026“).
- **Hinweis auf vorzeitige Neuvergabe:** nein (Beginn U2 2026-09-01, nach Ende der Grundlaufzeit)
- **Abfragen/XML:** 1/2 (lokal: 3)

### U3 – 193121-2026 (2026-03-20) – Gemeinde Kochel am See
- **Objekt(e):** keine Objektliste. „Unterhalts-, Grund- und Glasreinigungsarbeiten in verschiedenen öffentlichen Gebäuden verteilt auf zwei Gemeinden mit verschiedenen Ortsteilen“. Los 1 UR Kochel am See ca. 5.158,26 m²; Los 2 UR Walchensee ca. 513,78 m²; Los 3 UR Schlehdorf ca. 1.647,70 m²; Los 4 Glasreinigung Kochel/Walchensee/Schlehdorf ca. 3.008,62 m².
- **Leistungsart (je Los):** Lose 1–3 Unterhaltsreinigung (+ Sonderarbeiten); Los 4 Glasreinigung.
- **Suchschritte:**
  - lokal: `any ~ /kochel/` → 5 Treffer (163548-2022, 474577-2022 Gemeinde; Polizeipräsidium Oberbayern Süd 54277/279353-2024; DB Regio 579553-2025); `any ~ /schlehdorf|walchensee|82431|82444/` → 4 Treffer, keiner von der Gemeinde.
  - API `api_01`: `FT~"Kochel" AND buyer-country=DEU AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260320` → 7 Treffer (dieselben, dazu Polizei 53991/242003-2020).
  - XML geöffnet: 163548-2022, 474577-2022.
- **A (Identität):** Glasfläche übereinstimmend, UR-Flächen abweichend. Details: Glas Los 4: 3.009,00 (2022) / 3.008,62 m² (2026), Abweichung 0,01 %. UR Los 1: 5.653,00 / 5.158,26 m² (−8,8 %), Los 2: 295,00 / 513,78 m², Los 3: 1.167,00 / 1.647,70 m². Objektliste nur 2022 (z. B. Los 1: „Rathaus, Grundschule, Heimatbühne, Klärwerk, Touristeninformation, Wohnungen, Bahnhof, Kindergarten …“).
- **B (Objektraum):** nicht erkennbar (Seite U3). Details: Gebiet je Los übereinstimmend (Kochel am See, Walchensee, Schlehdorf), Leistungsart je Los übereinstimmend. Die Objektart steht in U3 aber nur als „verschiedene öffentliche Gebäude“ einer Gemeinde; nach Regel 1.1 ist das nicht erkennbar.
- **C (Stütze):** Auftraggeber ja, CPV ja, Titel ähnlich, Losstruktur gleich (je 4 Lose: 3 UR nach Ortsteil + 1 Glas).
- **Überschneidung der Objekte:** nicht bestimmbar (Liste nur 2022).
- **Ergebnis:** unklar
- **Tendenz:** eher dafür. Gleiche Gemeinde, gleicher Losschnitt nach Ortsteilen, gleiche Leistungsart je Los, Glasfläche bis auf 0,4 m² gleich.
- **Kandidat:** 163548-2022 (competition, vor eForms, 2022-03-29), 474577-2022 (result, vor eForms, 2022-08-31).
- **Beleg:** 163548-2022, `OBJECT_CONTRACT/SHORT_DESCR`: „… Kochel am See, Walchensee und Schlehdorf … ca. 3.009,00 m2 für die Glasreinigung Los 4“; U3: „… ca. 3.008,62 m² für die Glasreinigung Los 4“.
- **Vorgänger mit Vertrag:** (Kandidat) 474577-2022 (4 Lose vergeben, Vertragsschluss 2022-06-02)
- **Vorgänger-Ende:** unbekannt (163548-2022: „DURATION 36“ Monate ohne Beginndatum; „Der Vertrag kann sich um ein weiteres Jahr verlängern, wenn keiner der Beteiligten vorab kündigt“). Herkunft: unbekannt.
- **Hinweis auf vorzeitige Neuvergabe:** unklar
- **Abfragen/XML:** 1/2 (lokal: 2)

### U4 – 130379-2026 (2026-02-24) – Bau- und Liegenschaftsbetrieb NRW Düsseldorf
- **Objekt(e):** Einzelobjekt „Rotationsgebäude Polizei“, Wirtschaftseinheit WE3642(-1), „DDA4 Polizei Düsseldorf“, Derendorfer Allee 4, 40476 Düsseldorf; „werktägliche Reinigung eines Bürogebäudes“. Keine Fläche.
- **Leistungsart (je Los):** 1 Los, Unterhaltsreinigung (CPV 90911200).
- **Suchschritte:**
  - lokal: `any ~ /WE ?3642|derendorfer|rotationsgeb|DDA ?4/` → 1 Treffer (Fehltreffer Gemeinde Barsbüttel); `buyer ~ /Bau- und Liegenschaftsbetrieb NRW D(ü|ue)sseldorf/` → 3 (443328-2018, 46312-2019, 569368-2024 Baureinigung Wuppertal); `buyer ~ /liegenschaftsbetrieb|BLB/` und `any ~ /düsseldorf/` → 174 (zentrale Vergabestelle BLB NRW Zentrale, vor eForms ohne Titel); `any ~ /polizei/` und `any ~ /düsseldorf/` → 6 (Bundespolizei Flughafen, Autobahn GmbH).
  - API `api_01`: `FT~"Derendorfer Allee" AND buyer-country=DEU AND classification-cpv=909* AND …<20260224` → 1 (408601-2017 Statkraft, Prüfsystem, nicht einschlägig)
  - API `api_02`: `FT~"Rotationsgebäude" …` → 0
  - API `api_03`: `FT~"WE3642" AND buyer-country=DEU …` (ohne CPV) → 0
  - API `api_04`: `FT~"WE 3642" …` → 0
  - API `api_05`: `FT~("Polizeipräsidium Düsseldorf" OR "Polizei Düsseldorf") …` → 0 (**ungültig**, OR-Syntax, siehe Konventionen; ersetzt durch `api_08`)
  - API `api_06`: `FT~"Polizei" AND FT~"Derendorf" … cpv 909*` → 0
  - API `api_07`: `FT~"Polizeipräsidium" AND buyer-name~"Liegenschaftsbetrieb" AND buyer-city=Düsseldorf …` → 0
  - API `api_08`: `FT~"Polizei" AND buyer-city=Düsseldorf AND classification-cpv=909* …` → 3 (253144-2018, 418604-2018, 524374-2021)
  - API `api_09`: `FT~"NL Düsseldorf" AND FT~"Unterhaltsreinigung" … cpv 909*` → 28 (Gebietslose der BLB-Niederlassung Düsseldorf 2016–2024)
  - API `api_10`: `FT~"3642" AND buyer-city=Düsseldorf … cpv 909*` → 0
  - API `api_11`: `FT~"WE2714" AND buyer-country=DEU …` → 4 (Kontrolle, dass WE-Nummern im Volltext auffindbar sind: 625281-2022, 94501-2023, 298124-2023, 318890-2023)
  - XML geöffnet: 524374-2021, 253144-2018, 625281-2022, 309942-2023, 137627-2023.
- **Geprüfte Kandidaten (Fakten):** 524374-2021 = NL Dortmund, Fachlose 2–6 (Glas, Empfang, Hausmeister usw.), anderes Gebiet. 253144-2018 = NL Köln, UHR Los 1.4. 137627-2023 = externe Qualitätskontrolle (andere Leistungsart). 309942-2023 = Los 1.23, 1 WE in 40217, Besichtigung WE8241. 625281-2022 = NL Düsseldorf UHR, 21 Gebietslose ohne Objektliste; Los 1.22 („in 1 WE“, 40476 Düsseldorf) nennt als Besichtigungsobjekt „WE2714“, also nicht WE3642; die Lose 1.11 (5 WE; 40474, 40476, 40427), 1.12 (8 WE; „40476 Düsseldorf (Großraum) Neuss, Ratingen, Remscheid“) und 1.21 (4 WE; u. a. 40476) nennen keine WE-Nummern.
- **A (Identität):** nicht vergleichbar. Details: Kein Kandidat nennt WE3642, die Derendorfer Allee oder das Rotationsgebäude (Volltextsuchen `api_01`–`api_04`, `api_10` jeweils 0).
- **B (Objektraum):** nicht erkennbar (Kandidatenseite). Details: Die Gebietslose 1.11/1.12/1.21 aus 625281-2022 umfassen PLZ 40476 und dieselbe Leistungsart (UHR), nennen aber weder Objektart noch Objekte („in 5 WE (Wirtschaftseinheiten)“).
- **C (Stütze):** Auftraggeber ja (BLB NRW, hier Zentrale statt Niederlassung; gleiche Körperschaft), CPV ja (90911200), Titel anders, Losstruktur anders (Gebietslos gegenüber Einzelobjekt).
- **Überschneidung der Objekte:** nicht bestimmbar.
- **Ergebnis:** unklar
- **Tendenz:** keine. Kein Merkmal belegt oder widerlegt, dass WE3642 in einem Düsseldorfer Gebietslos enthalten war. WE-Nummern erscheinen in den Gebietslosen nur für Pflichtbesichtigungen, ihr Fehlen ist also kein Gegenbeleg.
- **Kandidat:** 625281-2022 (competition, vor eForms, 2022-11-11), Lose 1.11, 1.12, 1.21 (nicht nach Los aufgelöst; zugehörige Zuschläge nicht geöffnet).
- **Beleg:** 625281-2022, Los 1.12 `MAIN_SITE`: „40476 Düsseldorf (Großraum) Neuss, Ratingen, Remscheid“, `SHORT_DESCR`: „Unterhaltsreinigung Los 1.12 in 8 WE (Wirtschaftseinheiten)“.
- **Vorgänger mit Vertrag:** nicht bestimmt
- **Vorgänger-Ende:** unbekannt (nur informativ: 625281-2022 Los 1.11 geplant 2023-05-01 bis 2027-07-31, Los 1.22 bis 2027-09-30, jeweils „3-malige Verlängerungsoption um jeweils 1 Jahr“). Herkunft: unbekannt.
- **Hinweis auf vorzeitige Neuvergabe:** unklar
- **Abfragen/XML:** 11/5 (lokal: 4)

### U5 – 27535-2026 (2026-01-15) – Stadt Bad Bramstedt
- **Objekt(e):** Jürgen-Fuhlendorf-Schule, Düsternhoop 48, 24576 Bad Bramstedt (Einzelstandort). Keine Fläche.
- **Leistungsart (je Los):** 1 Los, Unterhalts- und Grundreinigung.
- **Suchschritte:**
  - lokal: `any ~ /bramstedt|fuhlendorf/` → 15 Treffer: Schulverband Bad Bramstedt 187792-2021, 406685-2022, 664503-2022; Stadt Bad Bramstedt 192485/249732/436108-2024 (Rathaus, Nebengebäude, Schloss), 732846/799216-2024 und 149730-2025 (Gemeinschaftsschule Auenland); Kreis Segeberg; BwDLZ Husum.
  - API `api_01`: `FT~"Fuhlendorf" AND buyer-country=DEU AND …<20260115` (ohne CPV) → 100 (50 geliefert; überwiegend nicht einschlägig, z. B. Gemeinde Fuhlendorf/Amt Barth, BImA)
  - API `api_02`: `FT~"Düsternhoop" …` → 2 (491140-2023 Schulverband/Stadt, 855945-2025 „LOS09 Abbrucharbeiten JFS“)
  - API `api_03`: `buyer-city="Bad Bramstedt" AND classification-cpv=909* …` → 10 (wie lokal, dazu 459756-2022 Änderung)
  - API `api_04`: `FT~"Fuhlendorf-Schule" …` (ohne CPV) → 16 (Stadt Bad Bramstedt 2022–2025; keiner davon in den CPV-909-Rohdaten; 62230-2024: „Neubau für ca. 8 Klassenzimmer der Jürgen-Fuhlendorf-Schule und energetische Sanierung …“)
  - API `api_05`: `FT~"Fuhlendorf" AND … classification-cpv=909*` → 6 (alle BImA Berlin, nicht einschlägig)
  - XML geöffnet: 406685-2022, 187792-2021.
- **A (Identität):** widersprüchlich (für die geprüften Reinigungskandidaten). Details: 406685-2022: „Unterhaltsreinigung der Gemeinschaftssschule Auenland“; 187792-2021: „Unterhaltsreinigung der Auenlandschule Bad Bramstedt“, also eine andere Schule (Auenland, Schäferberg 28 laut 732846-2024).
- **B (Objektraum):** widersprüchlich. Details: gleiche Stadt und Objektart (Schule), aber ein anderes Objekt.
- **C (Stütze):** Auftraggeber nein (Schulverband statt Stadt), CPV ja, Titel anders, Losstruktur gleich (1 Los).
- **Überschneidung der Objekte:** 0 von 1.
- **Ergebnis:** kein_vorgaenger
- **Vorgänger:** –
- **Beleg:** Kein Reinigungsverfahren (CPV 909*) nennt die Jürgen-Fuhlendorf-Schule oder den Düsternhoop (`api_05`: 0 einschlägige; Treffer von `api_02`/`api_04` sind Bauleistungen). 406685-2022 `SHORT_DESCR`: „Unterhaltsreinigung der Gemeinschaftssschule Auenland“.
- **Vorgänger mit Vertrag / Vorgänger-Ende:** – 
- **Hinweis auf vorzeitige Neuvergabe:** –
- **Abfragen/XML:** 5/2 (lokal: 1)

### U6 – 72981-2026 (2026-02-02) – IKK classic
- **Objekt(e):** 8 Dienststellen, 14 Lose: Annaberger Straße 89, 09120 Chemnitz (Los 1 UR); Niedermarkt 15, 04720 Döbeln (Los 2 UR, Los 3 Glas); Mühlweg 5, 09599 Freiberg (Los 4 UR, Los 5 Glas); Adam-Ries-Straße 16, 09456 Annaberg-Buchholz (Los 6 UR); Schwarzenberger Straße 7, 08280 Aue (Los 7 UR, Los 8 Glas); Mühlpfortstraße 76, 08058 Zwickau (Los 9 UR, Los 10 Glas); Friedrich-Naumann-Straße 3, 08209 Auerbach (Los 11 UR, Los 12 Glas); Marienstraße 21, 08527 Plauen (Los 13 UR, Los 14 Glas). Keine Flächen.
- **Leistungsart (je Los):** wie oben, Unterhaltsreinigung bzw. Glas- und Rahmenreinigung je Standort.
- **Suchschritte:**
  - lokal: `buyer ~ /IKK/` → 134 Treffer (IKK classic überwiegend vor eForms ohne Titel; eForms-Titel 2023–2026 nennen andere Bereiche: Bautzen, Leipzig, Dresden, Thüringen usw., kein Bereich Chemnitz).
  - API `api_01`: `FT~"Annaberger Straße 89" AND buyer-country=DEU AND classification-cpv=909* AND …<20260202` → 2 (48085-2022, 226910-2022)
  - API `api_02`: `FT~"Mühlpfortstraße" …` → 2 (dieselben)
  - API `api_03`: `FT~"Chemnitz" AND buyer-name~"IKK" AND classification-cpv=909* …` → 4 (zusätzlich 35538-2022 und 680752-2022)
  - XML geöffnet: 48085-2022, 226910-2022, 680752-2022, 35538-2022.
- **Geprüfte Kandidaten (Fakten):** 680752-2022 = „Reinigung Helmstedt (24/AD/2022)“, 35538-2022 = „Reinigung Sachsen - Bereich Dresden (13/AD/2021)“. In beiden steht „Chemnitz“ nur als Sitz des Auftragnehmers. Andere Adressen, also nicht objektgleich.
- **A (Identität):** übereinstimmend (Objektliste). Details: Alle 8 Adressen und die Zuordnung der 14 Lose (Los-Nummer, Standort, Leistungsart) sind in 48085-2022 identisch, z. B. Los 1 „Unterhaltsreinigung Annaberger Straße 89, 09120 Chemnitz“. Jede Dienststelle ist ein Einzelstandort, die Adresse zählt dort nicht als eigenes Merkmal. Weitere A-Merkmale (Fläche, Geschosse) fehlen auf beiden Seiten.
- **B (Objektraum):** erkennbar und übereinstimmend. Details: Geschäftsstellen der IKK classic in Südwestsachsen, UR bzw. Glas je Los.
- **C (Stütze):** Auftraggeber ja, CPV ja (90911200, 90911300), Titel ähnlich („Reinigung Sachsen - Bereich Chemnitz (07/AD/2022)“ / „Reinigungsdienstleistungen Sachsen - Bereich Chemnitz (12/FI-AD/2026)“), Losstruktur gleich (14 Lose).
- **Überschneidung der Objekte:** 8 von 8 Standorten, 14 von 14 Losen.
- **Ergebnis:** objektgleich_mittel (nur die Objektliste bzw. Adressen als A-Merkmal, keine Fläche; für „hoch“ fehlt ein zweites A-Merkmal)
- **Vorgänger:** 48085-2022 (competition, vor eForms, 2022-01-28), 226910-2022 (result, vor eForms, 2022-04-29).
- **Beleg:** 48085-2022, `OBJECT_CONTRACT/SHORT_DESCR`: „… Unterhalts- sowie die Glas- und Rahmenreinigung an den Standorten Chemnitz (nur Unterhaltsreinigung), Döbeln, Freiberg, Annaberg-Buchholz (nur Unterhaltsreinigung), Aue, Zwickau, Auerbach und Plauen der Auftraggeberin.“
- **Vorgänger mit Vertrag:** 226910-2022 (alle 14 Lose vergeben; Vertragsschlüsse 2022-04-08, Los 5 2022-01-14)
- **Vorgänger-Ende:** 2023-05-31 (grundlaufzeit, 48085-2022 je Los 2022-06-01 bis 2023-05-31); 2026-05-31 (hoechstende: „Der Vertrag verlängert sich um ein weiteres Jahr, längstens jedoch bis zum 31.05.2026 …“).
- **Hinweis auf vorzeitige Neuvergabe:** nein (Beginn U6 2026-06-01)
- **Abfragen/XML:** 3/4 (lokal: 1)

### U7 – 74601-2026 (2026-02-02) – Eigenbetrieb Kommunale Objektbewirtschaftung und -entwicklung der Hanse- und Universitätsstadt Rostock
- **Objekt(e):** Jenaplanschule mit zwei Standorten: WE 2003 Blücherstraße 42 (Haus I Schule + Container, Haus I Sporthalle; Jahresreinigungsfläche 558.796 m², Grundreinigung 3.445 m²) und WE 2053 Lindenstraße 3a/c (Haus II Schulgebäude, Haus II Sporthalle; 640.169 m², Grundreinigung 3.762 m²), 18055 Rostock. Summe 1.198.965 m² Jahresfläche, 7.207 m² Grundreinigung, 4 Gebäude.
- **Leistungsart (je Los):** 1 Los, Unterhalts- und Grundreinigung.
- **Suchschritte:**
  - lokal: `any ~ /jenaplan|bl(ü|ue)cherstr|lindenstra(ß|ss)e 3/` → 26 (Jenaplanschulen in Jena 50843/181605-2024 und Weimar 169068/458230-2025, andere Städte); `buyer ~ /rostock/` → 141 (Eigenbetrieb vor eForms ohne Titel).
  - API `api_01`: `FT~"Jenaplanschule" AND buyer-city=Rostock AND classification-cpv=909* AND …<20260202` → 1 (509878-2022)
  - API `api_02`: `FT~"Blücherstraße" …` → 0; API `api_03`: `FT~"Lindenstraße" …` → 0 (2022 abgekürzt „Blücherstr.“/„Lindenstr.“)
  - API `api_04`: `form-type=result AND buyer-city=Rostock AND classification-cpv=909* AND publication-date>=20221001 …` → 33 (Suche nach dem Zuschlag zu 509878-2022)
  - XML geöffnet: 509878-2022, 223447-2023, 36368-2023, 402792-2023.
- **Geprüfte Zuschläge (Fakten):** 223447-2023 verweist auf 617819-2022 (Kunsthalle), 36368-2023 auf 129525-2022 (Schulstandort Pablo-Picasso-Str.), 402792-2023 auf 379966-2022 (Feuerwache 3). Einen Zuschlag zu 509878-2022 habe ich auf TED nicht gefunden.
- **A (Identität):** übereinstimmend (Adressen, Gebäudename, Gebäudezahl), Fläche abweichend. Details: 509878-2022: „Unterhalts- und Grundreinigung Jenaplanschule, Blücherstr. 42 und Lindenstr. 3a+c, 18055 Rostock“, „4 Objekten mit einer Jahresreinigungsfläche von ca. 1,13 Mio. Quadratmetern und einer Grund- und Intensivreinigungsfläche von ca. 7.000 Quadratmetern“. Gebäudezahl 4 = 4; Jahresfläche 1,13 Mio. / 1,199 Mio. m² (+6 %), Grundreinigung 7.000 / 7.207 m² (+3 %).
- **B (Objektraum):** erkennbar und übereinstimmend. Details: Schule mit Sporthallen, Rostock, UR + GR.
- **C (Stütze):** Auftraggeber ja, CPV ja (90911200), Titel ähnlich, Losstruktur gleich (1 Los).
- **Überschneidung der Objekte:** 2 von 2 Standorten (4 von 4 Gebäuden).
- **Ergebnis:** objektgleich_mittel (Adresse, Name und Gebäudezahl stimmen überein; Jenaplanschule als Einzelstandort, Adresse zählt nicht; „hoch“ ausgeschlossen, weil die Flächen um mehr als 2 % abweichen)
- **Vorgänger:** 509878-2022 (competition, vor eForms, 2022-09-19). Zuschlag auf TED nicht gefunden.
- **Beleg:** 509878-2022, `MAIN_SITE`: „Blücherstr. 42, 18055 Rostock Lindenstr. 3a+c, 18055 Rostock“; U7 `StreetName`: „Blücherstraße 42 und Lindenstraße 3a/c“.
- **Vorgänger mit Vertrag:** nicht gefunden (nur die Ausschreibung 509878-2022 liegt vor)
- **Vorgänger-Ende:** 2027-02-19 (grundlaufzeit, nur geplant laut 509878-2022: 2023-02-20 bis 2027-02-19; Verlängerung „unbefristet“). Ohne Zuschlag nicht bestätigt.
- **Hinweis auf vorzeitige Neuvergabe:** unklar (nach der geplanten Laufzeit: ja, Beginn U7 2026-05-01 liegt fast 10 Monate vor 2027-02-19; der Vertrag ist aber nicht belegt)
- **Abfragen/XML:** 4/4 (lokal: 2)

### U8 – 78859-2026 (2026-02-03) – Stadt Nürnberg – Zentrale Dienste
- **Objekt(e):** „B12, Nunnenbeckstraße 40, 90489 Nürnberg“ (Einzelstandort; laut 451488-2023 „Städtische und Staatliche Wirtschaftsschule Nürnberg (B12)“). Keine Fläche.
- **Leistungsart (je Los):** 1 Los, laufende Innen-, Grund- und Glasreinigung.
- **Suchschritte:**
  - lokal: `any ~ /nunnenbeck|B ?12/` (mit Wortgrenzen) → 52 Treffer, keiner mit Bezug zu Nürnberg; `buyer ~ /stadt n(ü|ue)rnberg/` → 148 (Zentrale Dienste und Vorgänger „Amt für Organisation …“, vor eForms ohne Titel; eForms-Titel nennen jeweils ein Einzelobjekt mit Adresse, keines davon Nunnenbeckstraße).
  - API `api_01`: `FT~"Nunnenbeckstraße" AND buyer-country=DEU AND classification-cpv=909* AND …<20260203` → 0
  - API `api_02`: `FT~"Nunnenbeckstr" AND buyer-country=DEU …` (ohne CPV) → 5 (DB Netz 616844-2019, 427801-2020, 640584-2023; Stadt Nürnberg – Hochbauamt 451488-2023, 554182-2023)
  - API `api_03`: `FT~"B12" AND buyer-city=Nürnberg AND classification-cpv=909* …` → 2 (257320-2018, 473157-2018)
  - API `api_04`: `FT~"Berufliche Schule 12" AND buyer-city=Nürnberg …` → 0
  - API `api_05`: `FT~"90489" AND buyer-city=Nürnberg AND classification-cpv=909* …` → 75 (PLZ steht in fast allen Bekanntmachungen der Stadt, nicht trennscharf, nicht weiter verfolgt)
  - API `api_06`: `FT~"Wirtschaftsschule" AND buyer-city=Nürnberg AND classification-cpv=909* …` → 0
  - XML geöffnet: 257320-2018, 451488-2023.
- **Geprüfte Kandidaten (Fakten):** 257320-2018 = „Abfallentsorgung für das Marktamt“ („B12“ ist dort eine Abfallfraktion), andere Leistungsart. 451488-2023 = „Nunnenbeckstr. 40, Städtische und Staatliche Wirtschaftsschule Nürnberg (B12), Netzwerk an Schulen, W-LAN-Vernetzung, Elektrotechnik“ (CPV 45310000), keine Reinigung.
- **A (Identität):** nicht vergleichbar (kein Reinigungskandidat). **B:** –. **C:** –.
- **Überschneidung der Objekte:** –
- **Ergebnis:** kein_vorgaenger
- **Vorgänger:** –
- **Beleg:** Volltextsuchen nach „Nunnenbeckstraße“ (`api_01`) und „Wirtschaftsschule“ (`api_06`) mit CPV 909* ergeben 0 Treffer; der einzige Nunnenbeckstraße-Treffer der Stadt ist eine Elektroinstallation (451488-2023, `CPV_MAIN` 45310000).
- **Vorgänger mit Vertrag / Vorgänger-Ende:** –
- **Hinweis auf vorzeitige Neuvergabe:** –
- **Abfragen/XML:** 6/2 (lokal: 2)

### U9 – 186753-2026 (2026-03-18) – Verbandsgemeindeverwaltung Wissen
- **Objekt(e):** Barbara-Grundschule, Knappenstraße 55a, 57581 Katzwinkel (Sieg); Grundfläche 648,84 m² (Einzelstandort). Im Los steht als Ort zusätzlich „Hauptstraße 134, 57587 Birken-Honigsessen“ (Einschätzung: vermutlich ein Übertragungsfehler der Vorlage).
- **Leistungsart (je Los):** 1 Los, Unterhaltsreinigung.
- **Suchschritte:**
  - lokal: `any ~ /katzwinkel|wissen/` → 306 (zu breit, trifft „Wissenschaft“); enger mit Katzwinkel, Knappenstraße, PLZ 57581/57537 und „Wissen“ als ganzem Wort → 12, einschlägig nur 117649-2026 „Rathaus Wissen (Neubau) - Unterhaltsreinigung“ (anderes Objekt).
  - API `api_01`: `FT~"Katzwinkel" AND buyer-country=DEU AND …<20260318` (ohne CPV) → 22 (u. a. 253595-2021 VG Wissen; sonst Forst, Verkehr, Landkreis Altenkirchen)
  - API `api_02`: `buyer-city=Wissen AND classification-cpv=909* …` → 1 (117649-2026)
  - API `api_03`: `FT~("Barbara-Grundschule" OR "Barbara Grundschule" OR "Knappenstraße 55") …` → 0 (**ungültig**, OR-Syntax)
  - API `api_04`: Gegenprobe `FT~("Jenaplanschule" OR "Barbara Grundschule") … buyer-city=Rostock` → 0 (belegt die Ungültigkeit, vgl. U7 `api_01` mit 1 Treffer)
  - API `api_05`: `FT~"Barbara" AND FT~"Grundschule" AND buyer-country=DEU AND classification-cpv=909* …` → 4 (Brühl 2017, Trier 2019, Amberg 2022 ×2; andere Städte)
  - API `api_06`: `FT~"Knappenstraße" AND … classification-cpv=909*` → 5 (LMBV Senftenberg; nicht einschlägig)
  - XML geöffnet: 253595-2021.
- **Geprüfte Kandidaten (Fakten):** 253595-2021 = „Beschaffung eines Hilfeleistungslöschgruppenfahrzeuges 10 (HLF 10) … Freiwillige Feuerwehr Katzwinkel“ (CPV 34144210), keine Reinigung.
- **A/B/C:** kein Reinigungskandidat.
- **Ergebnis:** kein_vorgaenger
- **Vorgänger:** –
- **Beleg:** Kein Reinigungsverfahren mit Katzwinkel, Barbara-Grundschule oder Knappenstraße (`api_01`, `api_05`, `api_06`); das einzige Reinigungsverfahren der VG Wissen auf TED ist 117649-2026 (Rathaus Wissen, Neubau).
- **Vorgänger mit Vertrag / Vorgänger-Ende:** –
- **Hinweis auf vorzeitige Neuvergabe:** –
- **Abfragen/XML:** 6/1 (lokal: 2)

### U10 – 56181-2026 (2026-01-26) – Landeshauptstadt Wiesbaden – Hochbauamt
- **Objekt(e):** „Gebäudeinnenreinigung von 28 Schulen im Stadtgebiet Wiesbaden“ ohne Namen (Schulen laut Übersichtstabelle in den Vergabeunterlagen). Los 1: 11 Schulen, ca. 53.000 m² UR-Fläche; Los 2: 9 Schulen, ca. 48.000 m²; Los 3: 8 Schulen, ca. 46.500 m².
- **Leistungsart (je Los):** Lose 1–3 Unterhalts- und Grundreinigung.
- **Suchschritte:**
  - lokal: `buyer ~ /wiesbaden/` → 88 Treffer (Hochbauamt Reinigungsmanagement mit vielen Schulverfahren vor eForms ohne Titel; eForms: 676269-2023 „9 Schulen“, 2025 Elisabeth-Selbert-Schule, Fritz-Gansberg-Schule, „3 Schulen“).
  - API `api_01`: `FT~"28 Schulen" AND buyer-city=Wiesbaden AND classification-cpv=909* AND …<20260126` → 0
  - API `api_02`: `FT~"Schulen" AND buyer-city=Wiesbaden AND classification-cpv=909* …` → 58
  - API `api_03`: `FT~"26 Schulen" AND buyer-city=Wiesbaden …` → 1 (535545-2019)
  - API `api_04`: `FT~"535545" …` → 1; API `api_05`: `FT~"64-891" …` → 1 (Suche nach dem Zuschlag über Bekanntmachungsnummer und Aktenzeichen; gefunden wurde nur die Ausschreibung selbst)
  - XML geöffnet: 121305-2020, 569470-2019, 535545-2019, 102291-2020, 676269-2023, 432558-2020.
- **Geprüfte Kandidaten (Fakten):** 121305-2020/432558-2020 Hermann-Ehlers-Schule und 569470-2019/102291-2020 Werner-von-Siemens-Schule sind Einzelschulen (ob sie zu den 28 gehören, lässt sich nicht feststellen). 676269-2023 „9 Schulen im Stadtgebiet Wiesbaden“, 2 Lose (4 + 5 Schulen); Schulzahl und Losschnitt passen nicht zu U10.
- **A (Identität):** Gebäudezahl abweichend, Flächen mehrdeutig. Details: 535545-2019 „Gebäudeinnenreinigung 26 Schulen in 3 Losen“ (Los 1: 9, Los 2: 9, Los 3: 8 Schulen) gegenüber 28 Schulen (11/9/8). 2019 nennt nur Jahresflächen („ca. 5,4 Mio. qm Unterhaltsreinigung pro Jahr, ca. 42 000 qm Grundreinigung pro Jahr“ in Los 1; 6 Mio./43.000 in Los 2; 5,2 Mio./44.000 in Los 3), 2026 nur die UR-Fläche je Los. Keine Schulnamen auf beiden Seiten.
- **B (Objektraum):** formal erkennbar und übereinstimmend (Schulen, Stadtgebiet Wiesbaden, UR + GR), aber beide Seiten ohne Objektliste und Gebiet nur auf Stadtebene (Grenzfall, siehe unten).
- **C (Stütze):** Auftraggeber ja (Hochbauamt, Reinigungsmanagement), CPV ja (90911200), Titel ähnlich, Losstruktur ähnlich (je 3 Lose; Lose 2 und 3 mit 9 und 8 Schulen auf beiden Seiten).
- **Überschneidung der Objekte:** nicht bestimmbar.
- **Ergebnis:** unklar
- **Tendenz:** eher dafür. Gleiche Vergabestelle, Objektart und Leistung, gleicher Losschnitt mit gleicher Schulzahl in Los 2 und 3. Zwei Schulen mehr in Los 1 sprechen eher für eine Erweiterung als für ein anderes Paket.
- **Kandidat:** 535545-2019 (competition, vor eForms, 2019-11-12). Zuschlag auf TED nicht gefunden.
- **Beleg:** 535545-2019, `OBJECT_CONTRACT/SHORT_DESCR`: „Gebäudeinnenreinigung für 26 Schulen im Stadtgebiet von Wiesbaden, aufgeteilt in 3 Lose.“; U10, Los 1: „11 von insgesamt 28 Schulen …“.
- **Vorgänger mit Vertrag:** nicht gefunden
- **Vorgänger-Ende:** nur informativ für den Kandidaten: 2026-04-30 (grundlaufzeit, geplant laut 535545-2019: 2020-05-01 bis 2026-04-30; ohne Zuschlag nicht bestätigt).
- **Hinweis auf vorzeitige Neuvergabe:** unklar (nach Plan: nein, Beginn U10 2026-05-01)
- **Abfragen/XML:** 5/6 (lokal: 1)

### U11 – 126685-2026 (2026-02-23) – Staatsbetrieb Sächsisches Immobilien- und Baumanagement (SIB), Zentrale, Zentralstelle Vergabe- und Vertragsmanagement
- **Objekt(e):** TU Bergakademie Freiberg, „Haus Formgebung mit Hallen, Bernhard-von-Cotta-Str. 4 in 09599 Freiberg“; UR ca. 50.500 m² monatliche Reinigungsfläche, Glas ca. 8.520 m² jährlich, Grundreinigung (Bedarf) ca. 9.600 m².
- **Leistungsart (je Los):** 1 Los, Unterhalts-, Glas- und Grundreinigung.
- **Suchschritte:**
  - lokal: `any ~ /formgebung|cotta-str|Bernhard-von-Cotta/` → 0; `any ~ /bergakademie|freiberg/` → 27 (SIB eForms: 762659-2023 „Liegenschaften in Freiberg (siehe Fbl. 911.1)“, 784195/48003-2023/24 Polizeirevier/Amtsgericht, 209073/436148-2024 „Institutsgebäude“ Lessingstr. 45, 797404-2025 „Gellert-Bau“ Leipziger Str. 23; dazu andere Auftraggeber).
  - API `api_01`: `FT~"Formgebung" AND buyer-country=DEU AND classification-cpv=909* AND …<20260223` → 0
  - API `api_02`: `FT~"Bernhard-von-Cotta" …` → 0
  - API `api_03`: `FT~"Bergakademie" … cpv 909*` → 22 (SIB 2018–2025)
  - API `api_04`: `FT~"Cotta" … cpv 909*` → 20 (Dresden-Cotta und Stuttgart; kein Freiberg)
  - XML geöffnet (alle SIB-Verfahren zur TU vor eForms): 512709-2022, 527099-2022, 541233-2022, 37505-2023, 31287-2020, 46138-2020, 148458-2020, 545165-2020, 124695-2021, 537450-2018.
- **Geprüfte Kandidaten (Fakten):** Jedes Verfahren betrifft ein namentlich genanntes anderes Gebäude: Universitätsbibliothek mit Hörsaalgebäude, Winklerstr. 3 (512709/527099-2022); Werner-Bau, Brennhausgasse 14 (541233-2022); Clemens-Winkler-Bau Laborflügel, Leipziger Str. 29 (37505-2023, 537450-2018); Weisbach-Bau, Lampadiusstr. 4 (31287-2020); Otto-Meisser-Bau, Gustav-Zeuner-Str. 12 (46138-2020); ZeHS, Winklerstr. 5 (148458-2020); Kegel-/Rammler-Bau, Agricolastr. 1/3 und Leipziger Str. 28 (545165-2020); Universitätshauptgebäude, Akademiestr. 6 (124695-2021). Die eForms-Verfahren nennen Lessingstr. 45 und Leipziger Str. 23.
- **A (Identität):** widersprüchlich (für alle Kandidaten). Details: andere Gebäude und Adressen (siehe oben).
- **B (Objektraum):** Objektart und Gebiet gleich (Hochschulgebäude TU Freiberg), Objekt verschieden.
- **C (Stütze):** Auftraggeber ja (SIB), CPV ja, Titel ähnlich („Gebäudereinigung - TU Bergakademie Freiberg, …“), Losstruktur gleich (1 Los).
- **Überschneidung der Objekte:** 0 von 1 bei jedem Kandidaten.
- **Ergebnis:** kein_vorgaenger
- **Vorgänger:** –
- **Beleg:** Volltextsuchen nach „Formgebung“ und „Bernhard-von-Cotta“ mit CPV 909* ergeben 0 Treffer (`api_01`, `api_02`). Das SIB schreibt die TU-Gebäude einzeln mit Gebäudenamen aus, z. B. 541233-2022 `MAIN_SITE`: „TU Bergakademie Freiberg, Werner-Bau, Brennhausgasse 14“.
- **Vorgänger mit Vertrag / Vorgänger-Ende:** –
- **Hinweis auf vorzeitige Neuvergabe:** –
- **Abfragen/XML:** 4/10 (XML-Budget ausgeschöpft; Ergebnis durch die Volltextsuchen gestützt) (lokal: 2)

### U12 – 147547-2026 (2026-03-03) – Stadt Tauberbischofsheim
- **Objekt(e):** Los 1 „Unterhaltsreinigung diverser Liegenschaften im Stadtgebiet und Stadtteilen“: Sporthalle am Wört, Schulzentrum am Wört (Bauteile A bis C), Christian-Morgenstern-Grundschule mit Container-Schule, Altes Rathaus Distelhausen, Grundschule mit Halle in Impfingen, Freibad. Los 2: Sporthalle Laurentiusberg, Laurentiusberg Archiv mit HM-Büro, Grünewaldhalle, Grünewald-Gymnasium, Bauhof-Verwaltung, Erich-Kästner-Grundschule Distelhausen, Dorfgemeinschaftshaus Dienstadt. Los 3: Fensterreinigung in den Gebäuden der Lose 1 und 2 sowie Mediothek, Rathaus, Stadthalle, Jugendhaus, Richard-Trunk-Musikschule, Peterskapelle, Feuerwehrgerätehaus. Keine Flächen.
- **Leistungsart (je Los):** Lose 1 und 2 Unterhaltsreinigung; Los 3 Fensterreinigung.
- **Suchschritte:**
  - lokal: `any ~ /tauberbischofsheim/` → 8 (298479-2019 Stadtverwaltung; Main-Tauber-Kreis 132511/528266-2018, 326080/641558-2022; Bundesagentur für Arbeit 2024).
  - API `api_01`: `FT~"Tauberbischofsheim" AND buyer-country=DEU AND classification-cpv=909* AND …<20260303` → 20 (dazu BImA, BA, Medizinischer Dienst; von der Stadt nur 298479-2019, kein Zuschlag der Stadt)
  - XML geöffnet: 298479-2019, 326080-2022.
- **Geprüfte Kandidaten (Fakten):** 326080-2022 = Main-Tauber-Kreis, „Gebäudereinigung in Objekten des Main-Tauber-Kreises“, Lose Nord/Süd ohne Objektliste. Anderer Auftraggeber (Kreisliegenschaften), nicht weiter verfolgt.
- **A (Identität):** nicht vergleichbar. Details: 298479-2019 („Ausschreibung von Gebäudereinigungsarbeiten“, „Unterhalts-, Grund- und Sonderreinigung in 2 Losen“) nennt weder Objekte noch Flächen.
- **B (Objektraum):** nicht erkennbar (Seite 2019). Details: Objektart und Gebiet fehlen 2019; Leistungsart UR (+ GR, Sonder) passt zu den Losen 1 und 2.
- **C (Stütze):** Auftraggeber ja (Stadtverwaltung Tauberbischofsheim), CPV ja (90911200), Titel anders, Losstruktur ähnlich (2 UR-Lose; 2026 zusätzlich ein Fensterlos).
- **Überschneidung der Objekte:** nicht bestimmbar.
- **Ergebnis:** unklar
- **Tendenz:** eher dafür. Gleiche Stadt, zwei Unterhaltsreinigungslose auf beiden Seiten, gleiche Leistungsart. Die Tendenz stützt sich nur auf Stufe C und B-Leistungsart und ist schwach.
- **Kandidat:** 298479-2019 (competition, vor eForms, 2019-06-27). Zuschlag auf TED nicht gefunden.
- **Beleg:** 298479-2019, `OBJECT_CONTRACT/SHORT_DESCR`: „Unterhalts-, Grund- und Sonderreinigung in 2 Losen.“
- **Vorgänger mit Vertrag:** nicht gefunden
- **Vorgänger-Ende:** nur informativ für den Kandidaten: 2024-12-31 (grundlaufzeit, geplant laut 298479-2019, 2020-01-01 bis 2024-12-31; ohne Zuschlag nicht bestätigt).
- **Hinweis auf vorzeitige Neuvergabe:** unklar (nach Plan: nein)
- **Abfragen/XML:** 1/2 (lokal: 1)

### U13 – 21073-2026 (2026-01-13) – Burgenlandkreis
- **Objekt(e):** 8 Objekte, je ein UR/GR-Los (1–8) und ein Glaslos (1a–8a): Sekundarschule Elsteraue, Ostrauer Straße 7, Elsteraue; Sekundarschule Droyßig, Friedensstraße 6; Domgymnasium Naumburg, Thomas-Müntzer-Straße 22/23; Berufsbildende Schulen BLK, Markgrafenweg 46, Naumburg; Sekundarschule Bad Bibra, Steinbacher Straße 2; Sporthalle Seminarstraße 1, Naumburg; Goethegymnasium Haus 1 (Am Kloster 4) und Haus 2 (Friedrichstraße 23), Weißenfels; Ökowegsekundarschule, Kugelbergring 32, Weißenfels. Keine Flächen.
- **Leistungsart (je Los):** Lose 1–8 Unterhalts- und Grundreinigung; Lose 1a–8a Glas- und Rahmenreinigung.
- **Suchschritte:**
  - lokal: `buyer ~ /burgenlandkreis/` → 34 Treffer (vor eForms ohne Titel 2017–2023; eForms 2025: „Gebäudereinigung in 6 Schulobjekten“ 9748/78175/433230/435061-2025, Verwaltungsobjekte Zeitz, Weißenfels, Naumburg).
  - API `api_01` bis `api_04`: `FT~"<Name>" AND buyer-name~"Burgenlandkreis" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260113` mit „Ökowegsekundarschule“, „Domgymnasium“, „Elsteraue“, „Bad Bibra“ → je 4 Treffer, jeweils 74566-2019, 316847-2019, 11901-2022, 316381-2022
  - API `api_05`: `FT~"Goethegymnasium" …` → 2 (279130-2017, 440814-2017)
  - API `api_06`: `FT~"Sporthalle Seminarstraße" …` → 6 (279130-2017, 440814-2017, 313109-2018, 44024-2019, 420911-2022, 45161-2023)
  - XML geöffnet: 11901-2022, 420911-2022, 316381-2022.
- **A (Identität):** übereinstimmend für 6 Objekte. Details: 11901-2022 „Gebäudereinigungsleistungen in 13 Schulobjekten des Burgenlandkreises“ enthält mit gleicher Adresse Ökowegsekundarschule (Los 1), Sekundarschule Droyßig (Los 2), Sekundarschule Elsteraue (Los 3), Sekundarschule Bad Bibra (Los 4), Domgymnasium (Los 6) und BbS Markgrafenweg 46 (Los 10). Los 12 „Objekt Seminarstraße 1 (Volkshochschule, Musikschule, Seitengebäude mit A.-Schweitzer-Schule)“ hat dieselbe Adresse wie die Sporthalle Seminarstraße 1 in U13, ist aber ein anderes Gebäude. Das zählt nach Regel 1.1 nur als mögliche Entsprechung, nicht als gemeinsames Objekt. Das Goethegymnasium fehlt 2022 (es steht in 420911-2022).
- **B (Objektraum):** erkennbar und übereinstimmend. Details: Schulen des Burgenlandkreises; UR/GR und Glas je Objekt in getrennten Losen.
- **C (Stütze):** Auftraggeber ja, CPV ja (90910000), Titel ähnlich („Gebäudereinigungsleistungen in 13 / 8 Schulobjekten …“), Losstruktur gleich im Prinzip (je Objekt Los n + na), Anzahl anders.
- **Überschneidung der Objekte:** 6 von 8 bezogen auf die kürzere Seite U13 (75 %); 6 von 13 bezogen auf 11901-2022 (46 %). Lose mit Überschneidung (U13 → 2022): 1→3, 2→2, 3→6, 4→10, 5→4, 8→1, jeweils mit den a-Losen. Zum Vergleich 420911-2022 („8 Schulobjekte“): gemeinsam nur Goethe-Gymnasium Haus 1 + 2 und Sporthalle Seminarstraße 1, also 2 von 8 (25 %, für sich allein „unklar“).
- **Ergebnis:** teilmenge (die kürzere Liste U13 ist zu 75 % auf der längeren belegt, die längere enthält weitere Objekte, U13 schließt nichts aus)
- **Vorgänger:** 11901-2022 (competition, vor eForms, 2022-01-10), 316381-2022 (result, vor eForms, 2022-06-13). Älter, gleiche Objekte laut Volltext: 74566-2019 / 316847-2019 (nicht geöffnet).
- **Beleg:** 11901-2022, `OBJECT_CONTRACT/SHORT_DESCR`: „Los 1 + 1a Ökowegsekundarschule, Kugelbergring 32, 06667 Weißenfels, Los 2 + 2a: Sekundarschule Droyßig, Friedensstraße 6 … Los 6 + 6a: Domgymnasium, Thomas-Müntzer-Str. 22/23, 06618 Naumburg … Los 10 + 10a: Berufsbildende Schulen BLK, Standort Markgrafenweg 46 …“.
- **Vorgänger mit Vertrag:** 316381-2022 (13 Lose vergeben, Vertragsschluss 2022-05-17)
- **Vorgänger-Ende:** 2025-07-06 (grundlaufzeit, 11901-2022 je Los 2022-07-14 bis 2025-07-06); 2026-07-06 (hoechstende: „Option der Verlängerung um 1 weiteres Jahr“).
- **Hinweis auf vorzeitige Neuvergabe:** nein (Beginn U13 2026-07-04, nach Ende der Grundlaufzeit)
- **Abfragen/XML:** 6/3 (lokal: 1)

### U14 – 137283-2026 (2026-02-26) – Blindeninstitutsstiftung
- **Objekt(e):** Blindeninstitut Rückersdorf, Dachsbergweg 1, 90607 Rückersdorf (Einzelstandort). Keine Flächen.
- **Leistungsart (je Los):** Los 1 Unterhalts- und Grundreinigung; Los 2 Glasreinigung.
- **Suchschritte:**
  - lokal: `any ~ /blindeninstitut|r(ü|ue)ckersdorf|dachsberg/` → 9 Treffer (203678-2018 / 365432-2018 Rückersdorf; 549037/701231-2022 Regensburg; 398720-2023; 540647/782908-2024 „Objektreinigung 2025“ Regensburg; 383615/584381-2025 München Romanstraße 12).
  - API `api_01`: `FT~"Rückersdorf" AND buyer-country=DEU AND classification-cpv=909* AND …<20260226` → 6 (LRA Nürnberger Land 17946-2017, 203678/219928/365432-2018, 204616-2023, 398720-2023)
  - API `api_02`: `FT~"Blindeninstitut" … cpv 909*` → 11
  - XML geöffnet: 204616-2023, 203678-2018, 398720-2023.
- **A (Identität):** übereinstimmend (Adresse). Details: 204616-2023 „Blindeninstitut Rückersdorf … 90607 Rückersdorf, Dachsbergweg 1“; Flächen nur 2023 (3.760 m² Grundfläche, 3.850 m² Glas). Einzelstandort, die Adresse zählt nicht als eigenes A-Merkmal; ein zweites Merkmal fehlt in U14.
- **B (Objektraum):** erkennbar und übereinstimmend. Details: Förderzentrum mit Schule, Tagesstätte, Internat am Standort Rückersdorf; Los 1 UR/GR, Los 2 Glas auf beiden Seiten.
- **C (Stütze):** Auftraggeber ja (Blindeninstitutsstiftung, 2023 mit Tippfehler „Blindeninstiutsstiftung“), CPV ja, Titel ähnlich („Objektreinigung 2023“ / „Objektreinigung 2026“), Losstruktur gleich (2 Lose).
- **Überschneidung der Objekte:** 1 von 1.
- **Ergebnis:** objektgleich_mittel (Einzelstandort: Die Adresse allein trägt kein „hoch“)
- **Vorgänger:** 204616-2023 (competition, vor eForms, 2023-04-05), 398720-2023 (result, vor eForms, 2023-07-03). Älterer objektgleicher Vorgänger: 203678-2018 (competition) / 365432-2018 (result), Blindeninstitut Rückersdorf, Dachsbergweg 1, 2 Lose.
- **Beleg:** 204616-2023, `OBJECT_CONTRACT/TITLE`: „Maßnahme: RüD1 Blindeninstitut Rückersdorf Auftrag: 301 Objektreinigung 2023“, Los 1 `MAIN_SITE`: „90607 Rückersdorf, Dachsbergweg 1“.
- **Vorgänger mit Vertrag:** 398720-2023 (beide Lose an Götz Gebäudemanagement Franken GmbH, Vertragsschluss 2023-06-27)
- **Vorgänger-Ende:** 2026-08-31 (grundlaufzeit, 204616-2023: 2023-09-01 bis 2026-08-31); 2028-08-31 (hoechstende: „Option, den Vertrag zweimal um je ein Jahr zu verlängern“).
- **Hinweis auf vorzeitige Neuvergabe:** nein (Beginn U14 2026-09-01)
- **Abfragen/XML:** 2/3 (lokal: 1)

---

## Übersichtstabelle

Bei „unklar“ stehen in den Vorgänger-Spalten der beste Kandidat und seine Laufzeitangaben (in Klammern, nur informativ). „–“ = nicht zutreffend.

| U | Notice | Ergebnis | Tendenz | jüngster Vorgänger | alle Notices desselben Vorgängers | Vorgänger mit Vertrag | Vorgänger-Ende | Herkunft | vorzeitig |
|---|---|---|---|---|---|---|---|---|---|
| U1 | 152665-2026 | unklar | eher dafür | (Kandidat 691234-2025) | (526136-2025, 538529-2025, 582515-2025, 691234-2025) | (691234-2025) | (2027-07-31; Höchstende 2029-07-31) | (grundlaufzeit / hoechstende) | unklar |
| U2 | 213443-2026 | objektgleich_mittel | – | 444675-2022 | 270164-2022, 444675-2022 (je Los 1) | 444675-2022 | 2024-08-31; Höchstende 2026-08-31 | grundlaufzeit; hoechstende | nein |
| U3 | 193121-2026 | unklar | eher dafür | (Kandidat 474577-2022) | (163548-2022, 474577-2022) | (474577-2022) | unbekannt | unbekannt | unklar |
| U4 | 130379-2026 | unklar | keine | (Kandidat 625281-2022, Lose 1.11/1.12/1.21) | (625281-2022) | nicht bestimmt | unbekannt | unbekannt | unklar |
| U5 | 27535-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U6 | 72981-2026 | objektgleich_mittel | – | 226910-2022 | 48085-2022, 226910-2022 | 226910-2022 | 2023-05-31; Höchstende 2026-05-31 | grundlaufzeit; hoechstende | nein |
| U7 | 74601-2026 | objektgleich_mittel | – | 509878-2022 | 509878-2022 (Zuschlag nicht gefunden) | nicht gefunden | 2027-02-19 (nur Plan) | grundlaufzeit (aus Ausschreibung) | unklar (nach Plan ja) |
| U8 | 78859-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U9 | 186753-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U10 | 56181-2026 | unklar | eher dafür | (Kandidat 535545-2019) | (535545-2019; Zuschlag nicht gefunden) | nicht gefunden | (2026-04-30, nur Plan) | (grundlaufzeit aus Ausschreibung) | unklar (nach Plan nein) |
| U11 | 126685-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U12 | 147547-2026 | unklar | eher dafür | (Kandidat 298479-2019) | (298479-2019; Zuschlag nicht gefunden) | nicht gefunden | (2024-12-31, nur Plan) | (grundlaufzeit aus Ausschreibung) | unklar (nach Plan nein) |
| U13 | 21073-2026 | teilmenge | – | 316381-2022 | 11901-2022, 316381-2022 (älter: 74566-2019, 316847-2019) | 316381-2022 | 2025-07-06; Höchstende 2026-07-06 | grundlaufzeit; hoechstende | nein |
| U14 | 137283-2026 | objektgleich_mittel | – | 398720-2023 | 204616-2023, 398720-2023 (älter: 203678-2018, 365432-2018) | 398720-2023 | 2026-08-31; Höchstende 2028-08-31 | grundlaufzeit; hoechstende | nein |

## Übersicht

**Fakten (Zählung aus der Tabelle):**

| Ergebnis | Anzahl | Fälle |
|---|---|---|
| objektgleich_hoch | 0 | – |
| objektgleich_mittel | 4 | U2, U6, U7, U14 |
| teilmenge | 1 | U13 |
| unklar | 5 | U1 (eher dafür), U3 (eher dafür), U4 (keine), U10 (eher dafür), U12 (eher dafür) |
| kein_vorgaenger | 4 | U5, U8, U9, U11 |
| **Summe** | **14** | |

- Objektgleich oder Teilmenge (Zählweise W1): 5 von 14. Nur objektgleich: 4 von 14. Mit „unklar, eher dafür“: 9 von 14.
- Bestimmbares Ende der Grundlaufzeit eines belegten Vorgängervertrags (Zuschlag auf TED): U2, U6, U13, U14 (4 Fälle). U7 hat nur die geplante Laufzeit aus der Ausschreibung.
- Vorzeitige Neuvergabe bei belegten Vorgängern: 0 von 4. U7 nach Plan ja, ohne Vertrag aber nicht belegt.
- Abbruch durch Budget: kein Fall ohne Ergebnis. In U11 ist das XML-Budget mit 10/10 ausgeschöpft, das Ergebnis stützt sich zusätzlich auf Volltextsuchen ohne Treffer. Höchster API-Verbrauch: U4 mit 11/15.
- Insgesamt 56 API-Abfragen (davon 2 ungültig wegen der OR-Syntax, 1 Gegenprobe) und 49 Kandidaten-XML.

## Grenzfälle der Regeln

1. **U1 (Lübeck) und U10 (Wiesbaden): Objektart mit Gebiet „ganzes Stadtgebiet“.** Beide nennen eine Objektart („Schul- und Bürostandorte“ bzw. „Schulen“) und als Gebiet nur das Stadtgebiet. Wörtlich gelesen wäre Stufe B erkennbar und übereinstimmend, und weil die Liste auf einer Seite fehlt, wäre „objektgleich (mittel)“ möglich (wie Wuppertal, dort aber mit Stadtteil). Dieselben Städte schreiben jedoch mehrere Schulpakete mit derselben Objektart aus, und die Regel sagt nicht, ob ein ganzes Stadtgebiet als Gebiet genügt. Bei U10 fehlt die Objektliste auf beiden Seiten, und die Schulzahl weicht ab (26 gegenüber 28). Nicht neu ausgelegt, sondern „unklar“ vergeben.
2. **U3 (Kochel): ein A-Merkmal stimmt, Stufe B ist formal nicht erkennbar.** Die Glasfläche stimmt auf 0,01 % überein, ebenso Losschnitt und Gebiet je Los. Die Objektart lautet in U3 aber nur „verschiedene öffentliche Gebäude“ einer Gemeinde und gilt damit als nicht erkennbar. Die Regel sieht nicht vor, dass ein A-Merkmal eine fehlende Objektart ersetzt. Daher „unklar“.
3. **U4 (BLB NRW): Gebietslose einer zentralen Vergabestelle ohne Objektliste.** Wörtlich gelesen macht jedes Düsseldorfer Gebietslos mit passender PLZ einen „unklaren“ Kandidaten. Dann ist „kein_vorgaenger“ praktisch nicht erreichbar, obwohl kein Merkmal einen Zusammenhang belegt. Vergeben: „unklar, Tendenz keine“.
4. **U13 (Burgenlandkreis): Teilmenge aus einem Mischpaket.** 6 der 8 Objekte stammen aus 11901-2022 (75 % der kürzeren Seite), 2 aus 420911-2022 (25 %). Die Teilmengenregel ist erfüllt, obwohl die kürzere Seite auch Objekte enthält, die auf der längeren fehlen. Diesen Fall regeln die Urteilsregeln nicht ausdrücklich.
5. **U13 (Seminarstraße 1):** gleiche Adresse, aber 2022 „Objekt Seminarstraße 1 (Volkshochschule, Musikschule, Seitengebäude …)“ und 2026 „Sporthalle Seminarstraße“. Nach der Regel nur eine mögliche Entsprechung, daher nicht gezählt.
6. **U2 (Karlskron): Vergleich auf Losebene.** Das Glaslos von 2022 hat in U2 keine Entsprechung (andere Leistungsart). Verglichen wurde Los 1. Für das Objekt ergibt sich daraus kein Widerspruch.

## Auffälligkeiten

**Fakten:**
- **Zentrale Vergabestellen:** BLB NRW Zentrale (U4; Gebietslose mit „n WE“, Objekte nur in den Unterlagen), SIB Sachsen Zentrale (U11; Gebäude einzeln und namentlich), Hochbauamt Wiesbaden (U10; Pakete und Einzelschulen), IKK classic (U6; Sitz der Vergabestelle 2022 Dresden, 2026 Erfurt, Auftraggebername gleich).
- **Namenswechsel und Fehler im Auftraggeberfeld:** Schulverband statt Stadt Bad Bramstedt (U5); „Blindeninstiutsstiftung“ in 204616-2023 (U14); in 203678-2018 steht im Feld Auftraggebername der Titel „Unterhalts- und Grundreinigung, Glasreinigung“ (U14).
- **Fehlende Zuschläge auf TED:** zu 509878-2022 (U7), 535545-2019 (U10) und 298479-2019 (U12) nicht gefunden.
- **Zwei Verfahren im selben Jahr:** Lübeck 2025 mit zwei Verfahren nahezu gleicher Objektlisten (393360/471736-2025 mit 18 Standorten, 526136/691234-2025 mit 16 Standorten); U1 folgte im März 2026 mit 3 Losen ohne Liste.
- **Volltextsuche:** `FT~` findet Bekanntmachungen vor eForms und WE-Nummern, trifft aber auch Teilwörter (Karlskron/Karlskrona). Klammerausdrücke mit OR liefern stets 0 Treffer.
- **Andere TED-Verfahren zum Objekt, aber keine Reinigung:** U5 (Neubau und Abbruch an der Jürgen-Fuhlendorf-Schule 2022–2025), U8 (W-LAN-Vernetzung der Wirtschaftsschule B12, 2023), U9 (Feuerwehrfahrzeug Katzwinkel, 2021).

**Einschätzungen:**
- Für U5, U8, U9 liegt nahe, dass die Reinigung bisher unterhalb der EU-Schwelle, in einem anderen Vertrag oder gar nicht vergeben wurde. Beim Rotationsgebäude (U4) und Haus Formgebung (U11) kommt auch ein neues oder neu genutztes Gebäude in Frage. Belegt ist das nicht.
- U2, U6, U13 und U14 beginnen jeweils unmittelbar nach dem Höchstende bzw. Ende der Grundlaufzeit des Vorgängers. Das passt zu einer Neuausschreibung nach Ausschöpfen der Verlängerungen. In das Urteil ist dieser Zusammenhang nicht eingeflossen.
- Viele Auftraggeber (BLB, Wiesbaden, Lübeck, Tauberbischofsheim 2019) nennen die Objekte nur in den Vergabeunterlagen. Nach Regel 1.1 bleibt dann meist nur „unklar“. Das begrenzt, wie viel Sichtbarkeit sich allein aus den TED-Texten belegen lässt.
