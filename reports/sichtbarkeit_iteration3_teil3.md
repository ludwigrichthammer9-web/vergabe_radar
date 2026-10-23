# Sichtbarkeit der Vorgänger – Handsuche Iteration 3, Teil 3 (T31–T45)

Rechercheur (Subagent), Recherche am 2026-10-23. Testfälle: Zeilen 31–45 aus `reports/testfaelle_iteration3.txt`.
Definitionen: `docs/iterationen.md`, Iteration 3, „Begriffe“. Unabhängigkeit: Regel-, Merkmals- und Ergebnisdateien
(`src/zuordnung_*.py`, `src/objekt_merkmale.py`, `data/processed/`, `reports/zuordnung_*`, `k2_*`, `blindpruefung_*`) wurden nicht gelesen.
Aus Teil 1 und Teil 2 wurde nur der Abschnitt „Vorgehen und Konventionen“ übernommen.

## Vorgehen und Konventionen (wie Teil 1 und 2)

**Quellen**
- *Lokal* (zählt als Abfrage): unveränderte API-Rohdaten `data/raw/ted_search/DEU_result_cpv909_20161001_20260930/` und
  `data/raw/ted_search/DEU_competition_cpv909_20161001_20260930/`. Gefiltert immer auf 20161001 ≤ Veröffentlichung < Testfalldatum.
  „buyer~x“ = regulärer Ausdruck (ohne Groß-/Kleinschreibung) über den Auftraggebernamen; „Text~x“ = regulärer Ausdruck über Auftraggebername,
  -ort, -PLZ, Titel (Verfahren/Los) und Leistungsort (Ort, PLZ, Straße). Vor eForms sind dort nur Auftraggebername und -ort gefüllt.
- *Live-API* (`POST https://api.ted.europa.eu/v3/notices/search`): vor allem das Volltextfeld `FT`. **Kontrollabfrage je Testfall:** eine
  `FT`-Abfrage ohne Datumsfilter, die den Testfall selbst finden muss. Die API-Abfragen sind nicht nach `form-type` getrennt
  (result und competition gemeinsam; Berichtigungen werden ignoriert).
- *XML*: `https://ted.europa.eu/en/notice/<nr>/xml`.
- Alle API-Antworten (mit Request als `*.request.json`) und alle XML liegen unverändert unter `data/raw/rechercheur_20261023/<Testfall-Nummer>/`.
  Lokale Abfragen wurden nicht gespeichert; sie lassen sich mit den angegebenen Suchbegriffen aus den vorhandenen Rohdaten wiederholen.

**Zählung:** „Abfragen/XML“ = lokale + API-Abfragen / geöffnete Kandidaten-XML. Die XML des Testfalls selbst ist nicht mitgezählt.

**Kategorien-Konvention (aus Teil 1 und 2):**
- *objektgleich*: Liegenschaft(en) per Name oder Adresse identisch, Leistungsart überlappt (Unterhalts-, Grund-, Glasreinigung; Baureinigung
  zählt nicht). Kleine Abweichungen im Objektbestand (ein Objekt mehr oder weniger) oder eine neue Losaufteilung desselben Bestands bleiben objektgleich.
- *teilmenge*: nur ein Teil der Objekte gemeinsam.
- **Belegstärke** (Einschätzung, keine Kategorie der Definition): stark = Adresse/Liegenschaftsname wörtlich gleich; mittel = Sammelbezeichnung +
  Kennzahlen/Losnummer; schwach = nur indirekt.
- **Amtsadressen** zentraler Vergabestellen gelten nicht als Objektbeleg.
- Nennen weder Testfall noch Kandidaten ein Objekt, aber es gibt konkrete Hinweise (gleicher Auftraggeber, gleiche Sammelbezeichnung,
  Anschlusstermin) → *unklar*. Enge Kennzahlen-Übereinstimmung bei benanntem Objektbestand → *objektgleich*, Belegstärke *mittel*.
- Notices vom selben Tag wie der Testfall zählen nicht als Vorgänger.

---

### T31 – 630789-2026 (2026-09-14) – Universitätsstadt Tübingen - Zentrale Vergabestelle
- Objekt(e): „Bildungshaus Winkelwiese“, Haußerstraße 132, 72076 Tübingen (ein Los, LOT-0001). Laufzeit 60 Monate.
- Leistungsart: Unterhalts- und Grundreinigung „ohne Glasreinigung“.
- Suchschritte:
  1. lokal buyer~`Tübingen` → 54 Treffer (alle Tübinger Auftraggeber; Stadt Tübingen: 9)
  2. lokal Text~`Winkelwiese|Haußerstr|Hausserstr` → 2 Treffer (291547-2026, 467991-2026, beide „Baureinigung I Bildungshaus Winkelwiese“)
  3. API Kontrolle `FT=Winkelwiese AND classification-cpv=909*` → 3 Treffer (inkl. Testfall selbst; sonst 291547-2026, 467991-2026)
  4. API `FT=Haußerstraße AND buyer-city=Tübingen AND classification-cpv=909*` → 3 Treffer (dieselben)
  5. API `buyer-name~"Universitätsstadt Tübingen" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260914` → 9 Treffer
  6. lokal Text~`72076` (Suche B) → 7 Treffer (Vermögen und Bau Amt Tübingen, Max-Planck-Institute, Baureinigung Winkelwiese; keine Stadt-Notices zur Reinigung)
  - XML geöffnet: 144029-2021, 144030-2021, 235777-2021, 370483-2021, 790947-2024
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Fakten: Die einzigen Notices mit „Winkelwiese“/„Haußerstraße“ sind 291547-2026 (competition, eForms, 2026-04-28) und 467991-2026
  (result, eForms, 2026-07-07): „Baureinigung I Bildungshaus Winkelwiese“, Leistungsort „Haußerstraße 128-132“, Laufzeit 30 Tage. Baureinigung
  überlappt nicht mit Unterhalts-/Grund-/Glasreinigung. Die Stadt-Verfahren 144029-2021 (Lose GyS + FÖS + Stadtbücherei, GyU, THU, GyW,
  Französische Schule, Glas), 235777-2021/370483-2021 (Kinderhaus Weilheim, Kindervilla Alexanderpark, Kinderhaus Mühlenviertel) und
  790947-2024 (Grund- und Glasreinigung „Gesamtes Stadtgebiet“, Los Süd 30 / Nord 32 Objekte, ohne Objektliste) nennen weder Winkelwiese noch
  die Haußerstraße. 144030-2021 (Unterhalts-/Grundreinigung, ein Los „ca. 62 186,54 m² mtl.“, 2021-09-01 bis 2026-08-31) nennt kein Objekt.
  Einschätzung: Das Bildungshaus ist ein Neubau (Baureinigung 2026), daher vermutlich echter Erstbezug. Ein Vorgängerbau am Standort ließe sich
  nur über 144030-2021 vermuten (Laufzeitende 2026-08-31 passt zeitlich zu „Zu Vertragsablauf“), dafür gibt es aber keinen Objektbeleg.
- Vertragsende Vorgänger: entfällt; Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 6/5

### T32 – 535765-2026 (2026-08-03) – Landkreis Ludwigslust-Parchim - Der Landrat
- Objekt(e): ein Los „Los 4 Standorte Parchim und Lübz“: 10 Gebäude in Parchim (Friedrich-Franz-Gymnasium + Sporthalle, Ziegendorfer Chaussee 71;
  Musikschule Johann Matthias Sperger und Schule am Alten Hafen, Ziegendorfer Chaussee 11; Kreisstraßenmeisterei Parchim und FD Brand- und
  Katastrophenschutz, Dargelützer Weg 15; RBB Hauptstelle Parchim + Sporthalle + Volkshochschule, Eldestraße 7; Pestalozzischule, Brunnenstraße 21)
  und 6 Gebäude in Lübz (Kreisstraßenmeisterei Lübz, Am Hafen 8; Schule am Neuen Teich + Sporthalle + Hort, Neuer Teich 1; Eldenburg-Gymnasium +
  Sporthalle, Blücherstraße 22a). Vergabe über KSM Kommunalservice Mecklenburg AöR. Laufzeit 2027-01-01 bis 2029-07-31.
- Leistungsart: Unterhalts- und Grundreinigung.
- Suchschritte:
  1. lokal buyer~`Ludwigslust|Parchim|Kommunalservice Mecklenburg` → 21 Treffer (Landkreis: 188740-2020, 337315-2020, 321892-2022, 501946-2022,
     279541-2025, 498737-2025, 54074-2017, 228650-2017; Rest Städte Parchim/Ludwigslust, DRK)
  2. API Kontrolle `FT=Ziegendorfer AND classification-cpv=909*` → 5 Treffer (Testfall, 279541-2025, 498737-2025, 188740-2020, 337315-2020)
  - XML geöffnet: 279541-2025, 498737-2025
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 498737-2025 (result, eForms, 2025-07-30), Los LOT-0004; zugehörige Ausschreibung 279541-2025 (competition, eForms, 2025-04-30).
  Ältere Kandidaten mit demselben Straßennamen: 188740-2020/337315-2020 (vor eForms, nicht geöffnet, da nicht jüngster).
- Beleg: 279541-2025, LOT-0004 „Los 4 Unterhalts- und Grundreinigung in Gebäuden des LRA Ludwigslust-Parchim - Bereiche: Parchim, Lübz“,
  „Liegenschaften Los 4 - 30.601,39 qm“, Leistungsorte u. a. „Friedrich-Franz-Gymnasium-Parchim“ / „Parchim, Ziegendorfer Chaussee 71“,
  „Schule am Alten Hafen Parchim …“, „Kreisstraßenmeisterei Parchim“ / „Parchim, Dargelützer Weg 15“, „Regionales Berufliches Bildungszentrum …
  Hauptstelle Parchim“ / „Parchim, Eldestraße 7“, „Pestalozzischule Parchim“ / „Parchim, Brunnenstraße 21“, „Kreisstraßenmeisterei Lübz“ /
  „Lübz, Am Hafen 8“, „Lübz, Neuer Teich 1“. Zusätzlich im Vorgänger: „Parchim, Walter-Hase-Straße 42“ (im Testfall nicht genannt; kleine Abweichung).
  498737-2025: LotResult LOT-0004 mit `TenderResultCode` „selec-w“ (Zuschlag erteilt). Leistungsart identisch.
- Vertragsende Vorgänger: 2027-08-31 (279541-2025/498737-2025, Los 4: StartDate 2025-09-01, EndDate 2027-08-31). Testfall-Start 2027-01-01.
  Hinweis auf vorzeitige Neuvergabe: **ja** (Fakt: neuer Vertrag beginnt 8 Monate vor dem Ende der Grundlaufzeit; Grund im Testfall nicht genannt).
- Abfragen/XML: 2/2

### T33 – 565728-2026 (2026-08-14) – Berliner Verkehrsbetriebe, Bereich Einkauf/ Materialwirtschaft
- Objekt(e): „Los 29 - Kundenzentrum Köpenick“ und „Los 30 - Kundenzentrum Marzahn“ (BVG). Leistungsorte nur mit PLZ 10179 (= Zentrale
  Holzmarktstraße 15-17, Amtsadresse, kein Objektbeleg). Laufzeit 2026-12-01 bis 2028-11-30, zwei Optionen bis 2032-11-30.
- Leistungsart: Unterhaltsreinigung.
- Suchschritte:
  1. lokal buyer~`Berliner Verkehrsbetriebe|BVG` → 39 Treffer (Gebäudereinigung u. a. 395698-2018, 75546-2019, 254121-2019, 250469-2019,
     582425-2019, 258434-2024; Rest Fahrzeug-, WC-, Gleisreinigung, Schädlingsbekämpfung)
  2. API Kontrolle `FT=Kundenzentrum AND buyer-city=Berlin AND classification-cpv=909*` → 9 Treffer (Testfall; BVG: 395698-2018, 63712-2019,
     75546-2019, 250469-2019, 254121-2019, 582425-2019; degewo 2×)
  - XML geöffnet: 258434-2024, 395698-2018, 75546-2019, 250469-2019, 254121-2019, 593458-2021, 409893-2023
- Ergebnis: **teilmenge** (Belegstärke stark für die Namen; Vorgänger war ein größeres Bündel)
- Vorgänger: 254121-2019 (result, vor eForms, 2019-05-31; Ausschreibung 75546-2019, competition, vor eForms, 2019-02-15). Für Marzahn zusätzlich
  250469-2019 (competition, vor eForms, 2019-05-29, Los 4 „Liegenschaften Marzahn“, Neuausschreibung nach nicht vergebenem Los).
- Beleg: 75546-2019 / 254121-2019 (Gebäude- und Glasreinigung der Verwaltungs- und Betriebsgebäude der BVG in 11 Losen):
  Los 9 „Betriebshof Marzahn inkl. Kantine, Kundenzentrum Marzahn“, Los 10 „Betriebshof und Kundenzentrum Köpenick, Schöneweide“. In 254121-2019
  ist Los 10 an „Sasse Traffic Logistic GmbH“ vergeben (Datum 2019-05-07); Los 9 hat dort keinen Vergabeblock. 250469-2019 schreibt „Liegenschaften
  Marzahn“ (Los 4) neu aus, mit dem Hinweis, die Reinigung umfasse u. a. „Kundenzentren“ (ohne Einzelnennung). Leistungsart überlappt
  (Unterhaltsreinigung + Glasreinigung im Vorgänger, Unterhaltsreinigung im Testfall). Die Kundenzentren waren Teil größerer Lose (Betriebshof + Kantine) → teilmenge.
  Fakt: 258434-2024 (competition, eForms, 2024-04-30, „Unterhaltsreinigung Liegenschaften in 28 Losen (BVG-weit)“, Laufzeit 2024-12-01 bis 2026-11-30)
  enthält Lose „BFKÖ“ (Wendenschlossstraße 138, 12557) und „BFMAR“ (Landsberger Allee 576, 12681), das Wort „Kunden“ kommt in der XML nicht vor.
  Einschätzung: Der Testfall nummeriert seine Lose 29/30 und beginnt am Tag nach dem Ende der 28 Lose von 2024. Ob die Kundenzentren 2024 in
  BFKÖ/BFMAR enthalten waren (dann wäre 258434-2024 der jüngste Vorgänger), ist aus TED nicht entscheidbar.
- Vertragsende Vorgänger: 75546-2019: 2019-05-01 bis 2022-04-30, „Einmalige Verlängerungsmöglichkeit … von max. 24 Monaten“ (max. 2024-04-30).
  Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 2/7

### T34 – 671403-2026 (2026-09-30) – Kreisstadt Saarlouis, Vergabestelle
- Objekt(e): „Los 1 MZH Neuforweiler“, „Los 2 MZH Picard“, „Los 3 Hans-Welsch-Halle“ (Mehrzweckhallen); Leistungsorte nur „Saarlouis 66740“
  bzw. Amtsadresse „Großer Markt 1“ (kein Objektbeleg). Laufzeit ab 2027-01-01, jährlich verlängernd, höchstens 4 Jahre.
- Leistungsart: Unterhaltsreinigung „einschl. 1 x jährlich Grundreinigung“.
- Suchschritte:
  1. lokal buyer~`Saarlouis` → 37 Treffer (Kreisstadt und Landkreis Saarlouis)
  2. lokal Text~`Neuforweiler|Picard|Hans-Welsch` → 5 Treffer (alle Kita Neuforweiler: 314490-2024, 318095-2024, 488327-2024, 46459-2025, 234510-2025)
  3. API Kontrolle `FT=Picard AND buyer-city=Saarlouis AND classification-cpv=909*` → 1 Treffer (nur Testfall)
  4. API `FT=(Mehrzweckhalle OR Mehrzweckhallen OR MZH OR Neuforweiler) AND buyer-city=Saarlouis AND classification-cpv=909*` → 14 Treffer
     (vor eForms: 56913-2018, 255487-2018, 611252-2022, 70555-2023, 358847-2023, 578937-2023; Rest Kitas und Testfall)
  5. API `FT=Welsch AND buyer-city=Saarlouis AND classification-cpv=909*` → 1 Treffer (nur Testfall)
  - XML geöffnet: 611252-2022, 358847-2023, 56913-2018, 255487-2018
- Ergebnis: **teilmenge** (Belegstärke stark für das gemeinsame Objekt)
- Vorgänger: 255487-2018 (result, vor eForms, 2018-06-14), REF_NOTICE „2018/S 026-056913“ → 56913-2018 (competition, vor eForms, 2018-02-07)
- Beleg: 56913-2018 „Los 2: Mehrzweckhalle Neuforweiler, Neuhofstraße 12“, „3 x wöchentliche Reinigung einer Mehrzweckhalle mit insgesamt
  553,92 m²“ (Unterhaltsreinigung). 255487-2018: Los 2 „Unterhaltsreinigung der Mehrzweckhalle Neuforweiler, Neuhofstraße 12“ vergeben an
  „GEMIS Gesellschaft für Gebäudemanagement und Industrieservice mbH“. Gemeinsam ist nur MZH Neuforweiler; für „MZH Picard“ und
  „Hans-Welsch-Halle“ fand sich nichts (FT `Picard`, `Welsch` nur Testfall). Nicht objektgleich: 358847-2023 „Mehrzweckhalle Beaumarais“ (andere Halle),
  611252-2022 (Kita Neuforweiler, Neuhofstraße 18).
- Vertragsende Vorgänger: 56913-2018 Los 2: 2018-05-01 bis 2019-04-30, „verlängert sich automatisch um je 1 weiteres Jahr … endet jedoch nach
  Ablauf von insgesamt 4 Jahren“ (spätestens 2022-04-30). Zwischen 2022 und 2026 ist auf TED kein Verfahren für die Halle sichtbar
  (Einschätzung: vermutlich unterschwellig oder im Bündel ohne Nennung vergeben). Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 5/4

### T35 – 506448-2026 (2026-07-22) – Gemeinde Grünheide (Mark)
- Objekt(e): Grundschule im Ortsteil Hangelsberg; der Testfall nennt keine Straße (nur Amtsadresse Am Marktplatz 1, 15537). Laufzeit 2026-08-10 bis 2030-08-09.
- Leistungsart: Unterhalts- und Grundreinigung.
- Suchschritte:
  1. lokal buyer~`Grünheide` → 3 Treffer (431973-2016 result, 268024-2023 competition, 522179-2023 result)
  2. lokal Text~`Hangelsberg|15537` → 2 Treffer (nur Autobahn GmbH, 79 Lose bundesweit; nicht einschlägig)
  3. API Kontrolle `FT=Hangelsberg AND classification-cpv=909*` → 1 Treffer (nur Testfall)
  - XML geöffnet: 268024-2023, 431973-2016
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Fakt: Testfall-Beschreibung „Leistungen der Grund- und Unterhaltsreinigung für die **neu errichtete** Grundschule im Ortsteil Hangelsberg“.
  „Hangelsberg“ kommt in keiner älteren CPV-909-Notice vor (FT nur Testfall). Die Gemeinde-Verfahren 268024-2023 („aktuell 32 Gebäude in der
  Anlage T-Objektadressen“, Laufzeit 2023-10-01 bis 2027-09-30, Optionen je ein Jahr) und 431973-2016 („27 verschiedene Gebäude“) nennen keine Objekte.
  Einschätzung: Neubau, daher erstmalige Vergabe. Ob ein Altbau der Grundschule Hangelsberg im 32-Gebäude-Vertrag 268024-2023/522179-2023 enthalten
  war, ist aus TED nicht prüfbar; selbst dann wäre der Neubau ein anderes Objekt.
- Vertragsende Vorgänger: entfällt; Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 3/2

### T36 – 595492-2026 (2026-08-28) – Stadt Esslingen am Neckar, Städtische Gebäude, Baurechtsamt, Vergabestelle
- Objekt(e): 27 kommunale Gebäude, u. a. „Behördenzentrum, Beblingerstr. 1-3“, „GS Waisenhofschule, Marktplatz 9/11“, „Museum im Schwörhaus,
  Marktplatz 12“, „Schreibermuseum, Untere Beutau 8-10“, „Schelztorturm“, „Stadtarchiv alt/neu“, „Neues Rathaus, Rathausplatz 2“, „Stadtbücherei“,
  „Musikschule, Blarerplatz 1“, „Makers In“, „Wolfstorturm“, „Technisches Rathaus, Ritterstr. 17“, „Mörike Gymnasium + Villa Kienlin + Turnhalle“,
  „KITA Neckarstr. 51“, „KITA Merkelstr. 19“, „KIGA Färbertörlesweg 23“; „ca. 34.568,35 m²“ Unterhaltsreinigung, „ca. 17.834,89 m²“ Glasreinigung.
  4 Lose (2× Unterhalts-/Grund-/Vertretungsreinigung, 2× Glas). Beginn 2027-02-01 bzw. 2027-02-15, 2 Jahre + 2× 1 Jahr.
- Leistungsart: Unterhalts-, Vertretungs-, Grund- und Glasreinigung.
- Suchschritte:
  1. lokal buyer~`Esslingen|Eßlingen` → 36 Treffer (Stadt Esslingen/SGE: 349017-2018, 524457-2018, 244641-2019, 481978-2019, 229935-2021,
     413597-2021, 258439-2023, 501333-2023, 607255-2023, 92431-2024, 174453-2024, 334039-2024, 535376-2024, 768502-2024, 219690-2025, 469734-2025,
     637462-2025, 844462-2025, 174734-2026, 436672-2026; Rest Landkreis, Pflegeheime, Abfallwirtschaft, Klinikum, Verkehrsbetrieb)
  2. API Kontrolle `FT=Waisenhofschule AND classification-cpv=909*` → 3 Treffer (Testfall, 607255-2023, 92431-2024)
  3. API `FT=(Schelztorturm OR Wolfstorturm OR Schwörhaus OR Schreibermuseum OR Behördenzentrum OR Mörike) AND classification-cpv=909* AND buyer-city~Esslingen`
     → 3 Treffer (dieselben)
  - XML geöffnet: 92431-2024, 607255-2023
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 92431-2024 (result, eForms, 2024-02-14); zugehörige Ausschreibung vermutlich 607255-2023 (competition, vor eForms, 2023-10-09; per FT
  mit denselben Objektnamen gefunden, Inhalt nicht im Detail ausgewertet).
- Beleg: 92431-2024, LOT-0001/LOT-0005 „Unterhalte-, Grundreinigung“: „an einer Fläche von ca. 34.431 m² Unterhalts-, Grund-, Vertretungsreinigung
  an folgenden kommunalen Objekten …: Behördenzentrum, GS Waisenhofschule, Orgelbau, Öffentliches WC Agneshof, Verwaltungs Abt-Fulrad-Str, Museum im
  Schwörhaus, Schreibermuseum, Schelztorturm, Stadtarchive, Neues Rathaus, Dekanat, Altes Rathaus-Fraktionszimmer, Stadtbücherei, Stadtmuseum,
  Musikschule, Verwaltung IT, Makers In, Wolfstorturm, Technisches Rathaus, Verwaltung Ritterstr. 15, Wohnhaus Bahnhofstr.2, Mörike Gymnasium,
  KITA Neckarstraße, KITA Merkelstraße, KIGA Färbertörlesweg“; Glaslose LOT-0002/3/4/6. Alle Lose `selec-w`. Objektliste nahezu identisch
  (im Vorgänger zusätzlich „Altes Rathaus-Fraktionszimmer“, „Wohnhaus Bahnhofstr.2“), Fläche fast gleich. Die übrigen Esslinger „diverse Gebäude“-Verfahren
  2024–2026 enthalten diese Namen nicht (FT-Abfragen 2 und 3).
- Vertragsende Vorgänger: Grundlaufzeit 2024-02-01 (LOT-0005: 2024-02-19) bis 2026-01-31, „Mit der Option der zweimaligen Verlängerung um jeweils
  ein Jahr“ (max. 2028-01-31). Testfall-Beginn 2027-02-01 passt zu einer gezogenen Option. Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 3/2

### T37 – 573790-2026 (2026-08-19) – Stadt Dessau-Roßlau, Zentr. Vergabestelle
- Objekt(e): „Pestalozzischule“ Schule für Lernbehinderte einschl. Sporthalle (Stenesche Straße 88, 06842), „Schule an der Muldaue“ Schule für
  Körperbehinderte einschl. Sporthalle, „Regenbogenschule“ Schule für Geistigbehinderte einschl. Container; weitere Leistungsorte Kreuzbergstraße 200
  (06849) und Breite Straße 6/7 (06844). „ca. 10.321 m²“ in 3 Schulgebäuden, 1 Container, 2 Sporthallen. Laufzeit 2027-01-01 bis 2027-12-31.
- Leistungsart: Unterhaltsreinigung/Grundreinigung, Grundreinigung optional (inkl. Glasinnenflächen ca. 572 m²).
- Suchschritte:
  1. lokal buyer~`Dessau` → 89 Treffer (Stadt Dessau-Roßlau sehr viele Einzelschul-Verfahren, dazu DVV, DEKITA, IHK, Kulturstiftung, Bauhaus)
  2. lokal Text~`Stenesche|Kreuzbergstr|Pestalozzi.*Dessau|Muldaue|Regenbogenschule` → 2 Treffer (Landkreis Gotha; nicht einschlägig)
  3. API Kontrolle `FT=Muldaue AND classification-cpv=909*` → 5 Treffer (Testfall, 384752-2022, 384753-2022, 627097-2022, 697551-2022)
  4. API `FT=(Regenbogenschule OR Pestalozzischule OR Lernbehinderte OR Körperbehinderte OR Geistigbehinderte) AND buyer-city~Dessau AND classification-cpv=909*`
     → 5 Treffer (dieselben)
  - XML geöffnet: 384752-2022, 384753-2022, 627097-2022, 697551-2022
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 697551-2022 (result, vor eForms, 2022-12-16), REF_NOTICE „2022/S 135-384752“ → 384752-2022 (competition, vor eForms, 2022-07-15).
  Parallel für Glas- und Rahmenreinigung: 627097-2022 (result, 2022-11-11) → 384753-2022.
- Beleg: 384752-2022/697551-2022: „Unterhaltsreinigung, Grundreinigung optional und Winterdienst in der "Pestalozzischule" Förderschule für
  Lernbehinderte einschl. der Sporthalle, "Schule an der Muldaue" Förderschule für Körperbehinderte einschl. Sporthalle und der "Regenbogenschule"
  Förderschule für Geistigbehinderte einschl. Container“, „Unterhaltsreinigung in 3 Schulgebäuden, 1 Container, 2 Schulsporthallen“, „ca. 8.294,00 m²“.
  697551-2022: Zuschlag 2022-12-06 an „Clean up“, Merseburg. Gleiche drei Schulen, gleiche Gebäudezahl; Fläche im Testfall größer (10.321 m²).
- Vertragsende Vorgänger: 384752-2022: 2023-01-01 bis 2023-12-31, „mit Verlängerungsoption um jeweils 1 Jahr für insgesamt 3 Jahre“ (je nach Lesart
  2025-12-31 oder 2026-12-31). Testfall-Beginn 2027-01-01 passt zur Lesart „drei Verlängerungsjahre“. Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 4/4

### T38 – 494560-2026 (2026-07-17) – Stadt Frankfurt am Main, Amt für Bau und Immobilien
- Objekt(e): Palmengarten, Siesmayerstraße 61, 60323 Frankfurt am Main. „Unterhaltsreinigung Montag bis Samstag 4.460,53 m², … Sonntag 688,58 m²“,
  dazu Reinigungsfachkräfte auf Stundenbasis. Beginn 2027-01-01, Dauer 43 Monate.
- Leistungsart: Unterhaltsreinigung (plus Stundenkontingente und Vertretung Eigenreinigung).
- Suchschritte:
  1. lokal Text~`Palmengarten|Siesmayer` → 0 Treffer
  2. API Kontrolle `FT=Palmengarten AND classification-cpv=909*` → 5 Treffer (32306-2021; Testfall; nach dem Testfall 540201-2026, 670788-2026, 700159-2026)
  3. API `FT=Siesmayerstraße AND classification-cpv=909*` → 5 Treffer (dieselben)
  4. lokal buyer~`Frankfurt am Main.*(Bau und Immobilien|Hochbau)` → 444 Treffer (zu viele zum Öffnen; vor eForms ohne Titel)
  5. API `FT=LDL020 AND classification-cpv=909*` (Vergabe-Kürzel aus 32306-2021, Suche nach dem Zuschlag) → 351 Treffer (allgemeiner Code, unbrauchbar)
  - XML geöffnet: 32306-2021
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 32306-2021 (competition, vor eForms, 2021-01-22). Ein zugehöriger Zuschlag mit „Palmengarten“ wurde per FT nicht gefunden.
- Beleg: 32306-2021: Titel „UHR Palmengarten [LDL020]“, „Unterhaltsreinigung 5 943,33 m² + Reinigungsfachkräfte auf Stundenbasis. Palmengarten
  Siesmayerstraße 61 60323 Frankfurt am Main.“ Gleiche Liegenschaft, gleiche Adresse, gleiche Leistungsart. Fläche heute 5.149,11 m² (4.460,53 + 688,58).
- Vertragsende Vorgänger: 2021-05-01 bis 2023-04-30, „Option zur Verlängerung für 2 weitere Jahre“ (max. 2025-04-30). Zwischen 2025-04-30 und dem
  Testfall-Beginn 2027-01-01 ist auf TED kein Verfahren sichtbar (Einschätzung: Interimsvergabe oder unterschwellige Verlängerung). Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 5/1

### T39 – 599823-2026 (2026-09-01) – Gemeinde Dettenheim
- Objekt(e): „Gebäude der Gemeinde Dettenheim in den Ortsteilen Liedolsheim und Rußheim“, „Objekte gemäß Vergabeunterlagen“ (keine Einzelobjekte
  genannt; Schulen, Kindergärten, Sporthallen erwähnt). Los 1 Unterhalts-/Grundreinigung, Los 2 Glas-/Rahmenreinigung. Beginn 2027-01-01, bis 2029-07-31, +2× 1 Jahr.
- Leistungsart: Unterhalts-, Grund-, Glas- und Rahmenreinigung.
- Suchschritte:
  1. lokal buyer~`Dettenheim` → 0 Treffer
  2. lokal Text~`Dettenheim|76706` → 2 Treffer (262449-2026, 302902-2026: Bundesanstalt für Immobilienaufgaben, Bundesliegenschaften Karlsruhe u. U.)
  3. API Kontrolle `FT=(Dettenheim OR Liedolsheim OR Rußheim) AND classification-cpv=909*` → 6 Treffer (Testfall; BImA 561920-2020, 203497-2021,
     262449-2026, 302902-2026; Vermögen und Bau BW Amt Ludwigsburg 745753-2025 „Baureinigung“)
  - XML geöffnet: keine (Treffer anderer Auftraggeber mit Bundes- bzw. Landesliegenschaften, nicht die Gebäude der Gemeinde)
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Fakt: Von der Gemeinde Dettenheim gibt es vor dem Testfall keine CPV-909-Notice auf TED (lokal 0, FT nur Notices von BImA und
  Vermögen und Bau). Einschätzung: Die Gemeinde schreibt erstmals EU-weit aus oder lag bisher unter dem Schwellenwert. Da es keinerlei Kandidaten
  des Auftraggebers gibt, ist „unklar“ nicht angebracht, obwohl der Testfall keine Objekte nennt.
- Vertragsende Vorgänger: unbekannt; Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 3/0

### T40 – 457874-2026 (2026-07-03) – Hochschule Düsseldorf
- Objekt(e): „sämtliche Glasflächen innen und außen … aller Gebäude der Hochschule Düsseldorf“; Leistungsort Münsterstr. 156, 40476 Düsseldorf
  (Campus und zugleich Dienstadresse). Rahmenvereinbarung 2026-09-01 bis 2028-12-31, Option bis 2029-12-31.
- Leistungsart: Glasreinigung (innen und außen, inkl. Rahmen).
- Suchschritte:
  1. lokal buyer~`Hochschule Düsseldorf|Fachhochschule Düsseldorf` → 5 Treffer (145764-2020, 423262-2020, 138159-2022, 327439-2022, 244625-2024)
  2. lokal Text~`Münsterstr.*156|Josef-Gockeln|Campus Derendorf` → 0 Treffer
  3. API `buyer-name~"Hochschule Düsseldorf" AND classification-cpv=909*` → 7 Treffer (dieselben 5, Testfall, 676568-2026 Robert Schumann Hochschule nach dem Testfall)
  4. API Kontrolle `FT=(Glasreinigung OR Aussenglasreinigung OR Außenglasreinigung) AND buyer-city=Düsseldorf AND buyer-name~Hochschule AND classification-cpv=909*`
     → 3 Treffer (Testfall, 138159-2022, 327439-2022)
  - XML geöffnet: 145764-2020, 138159-2022, 327439-2022
- Ergebnis: **objektgleich** (Belegstärke mittel)
- Vorgänger: 327439-2022 (result, vor eForms, 2022-06-17), REF_NOTICE „2022/S 053-138159“ → 138159-2022 (competition, vor eForms, 2022-03-16)
- Beleg: 138159-2022/327439-2022 „Innen- und Aussenglasreinigung EU 03 - 2022“: „Rahmenvereinbarung über die Innen- und Aussenglasreinigung mit einer
  Laufzeit von 01.05.2022 bis 31.12.2024 und der zusätzlichen Option auf eine Verlängerung um ein weiteres Jahr (31.12.2025)“, Leistungsort
  „Hochschule Düsseldorf Münsterstr. 156 40476 Düsseldorf“; Zuschlag 2022-05-16 an „Joba Gebäudereinigung und Service GmbH“, Tönisvorst.
  Gleiche Leistung (Innen- und Außenglas, Rahmenvereinbarung), gleiche Sammelbezeichnung (Gebäude der Hochschule Düsseldorf), gleicher
  Vertragsaufbau. Belegstärke nur mittel, weil die Adresse zugleich die Dienstadresse ist und keine Einzelgebäude genannt werden.
  Nicht objektgleich wegen Leistungsart: 145764-2020 und 244625-2024 (nur Unterhaltsreinigung).
- Vertragsende Vorgänger: 2024-12-31, Option bis 2025-12-31. Testfall-Beginn 2026-09-01. Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 4/3

### T41 – 571136-2026 (2026-08-18) – Bundeswehr-Dienstleistungszentrum Bogen
- Objekt(e): Graf-Aswin-Kaserne Bogen (Leistungsort Bayerwaldstr. 36, 94327 Bogen), Bundeswehr-Dienstleistungszentrum Bogen (Bayerwaldstr. 26)
  und Pionierübungsplatz Wasser (Hutterhof 1, 94327 Bogen). Beginn 2027-02-01, 4 Jahre.
- Leistungsart: Unterhaltsreinigung und Sonderreinigung, „ohne Glasflächenreinigung“.
- Suchschritte:
  1. lokal buyer~`Bogen` → 39 Treffer (BwDLZ Bogen 34, vergibt für viele Kasernen in Bayern; HafenCity Hamburg 5 als Fehltreffer)
  2. lokal Text~`94327|Graf-Aswin|Bayerwaldstr` → 11 Treffer (nur eForms-Notices des BwDLZ mit Amts-PLZ; Titel nennen andere Kasernen)
  3. API `FT=Graf-Aswin-Kaserne AND classification-cpv=909*` → 802 Treffer (Bindestrich-Begriff wird zerlegt; unbrauchbar, verworfen)
  4. API Kontrolle `FT=Aswin AND classification-cpv=909*` → 5 Treffer (Testfall, 289719-2018, 448821-2018, 347342-2022, 676959-2022)
  - XML geöffnet: 347342-2022, 676959-2022
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 676959-2022 (result, vor eForms, 2022-12-06), REF_NOTICE „2022/S 122-347342“ → 347342-2022 (competition, vor eForms, 2022-06-28).
  Älter: 289719-2018 / 448821-2018 (nicht geöffnet).
- Beleg: 347342-2022/676959-2022: „Gebäudereinigung (Unterhalts- und Glasflächenreinigung) in der Graf-Aswin-Kaserne/ BwDLZ/ PiÜbPlW Bogen“,
  Los 1 Unterhaltsreinigung, Leistungsorte „Bayerwaldstraße 36, 94327 Bogen“ und „Bayerwaldstraße 26, 94327 Bogen“, „Reinigungsbedarf ca. 17.150 m²
  Fußbodenfläche“; Los 2 Glasreinigung. Zuschlag beider Lose 2022-11-14 an „Moritz Fürst GmbH & Co. KG“. Gleiche drei Liegenschaften, gleiche Adressen;
  Leistungsart überlappt über Los 1 (der Testfall lässt die Glasreinigung weg).
- Vertragsende Vorgänger: 2027-01-31 (347342-2022: 2023-02-01 bis 2027-01-31). Testfall-Beginn 2027-02-01 schließt direkt an.
  Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 4/2

### T42 – 533895-2026 (2026-08-03) – Stadt Hürth
- Objekt(e): „städtische Liegenschaften“ (Verwaltungsgebäude, Feuerwachen, Schulen, Kindertagesstätten „sowie Unterkünfte für Geflüchtete“),
  Lose 1–5 Unterhaltsreinigung, Los 6 Glas-/Rahmenreinigung; keine Objektliste je Los. Als „repräsentativ“ zur Besichtigung genannt:
  „Grundschule im Zentrum, Bonnstraße 109“, „Ernst-Mach-Gymnasium, Bonnstraße 64“, „Familienzentrum Wibbelstätz, Bonnstraße 40“ (alle 50354 Hürth).
  Laufzeit 2026-12-01 bis 2029-11-30.
- Leistungsart: Unterhalts-, Vertretungs-, Grund- und Glasreinigung.
- Suchschritte:
  1. lokal buyer~`Hürth` → 16 Treffer (Stadt Hürth: 274708-2017, 336554-2017, 391731-2017, 485794-2018, 574173-2018, 404324-2020, 558557-2020,
     488753-2023, 584972-2024, 585758-2024, 162173-2025, 334240-2025, 519520-2025, 672894-2025; Stadtwerke Hürth 2)
  2. API Kontrolle `FT=Wibbelstätz AND classification-cpv=909*` → 5 Treffer (404324-2020, 558557-2020, 488753-2023, Testfall, 554188-2026 nach dem Testfall)
  3. API `FT=Bonnstraße AND buyer-city=Hürth AND classification-cpv=909*` → 2 Treffer (nur Testfall und 554188-2026)
  - XML geöffnet: 488753-2023, 558557-2020, 585758-2024
- Ergebnis: **objektgleich** (Belegstärke stark für die drei genannten Objekte; vollständiger Objektbestand des Testfalls unbekannt)
- Vorgänger: 488753-2023 (competition, vor eForms, 2023-08-11), „Reinigungsleistungen 2023-2027“. Ein Zuschlag dazu ist in den Rohdaten nicht
  sichtbar. Jünger, aber ohne Objektnamen: 585758-2024 (competition, eForms, 2024-09-30, „Reinigungsleistungen (Los 2)“, Neuausschreibung von Los 2).
- Beleg: 488753-2023: Los 1 „GS Carl-Orff - … - GS Im Zentrum - Kulturwerkstatt“; Los 2 „Albert-Schweizer-Gymnasium - KiTa Hürther Strolche - … -
  KiTa Wibbelstätz“; Los 3 Gesamtschule, Rathaus, Feuerwehr u. a.; Los 4 „GS Efferen - HS Kendenich - Realschule - Ernst-Mach-Gymnasium - …“;
  Los 5 „Glas- und Rahmenreinigung für alle städtische Liegenschaften“. Gleiche Sammelbeschreibung („Verwaltungsgebäude, Feuerwachen, Schulen und
  Kindertagesstätten auf dem Stadtgebiet von Hürth“), gleiche Leistungsarten. Ältere Runde: 558557-2020 (result, REF 404324-2020) mit denselben Objekten
  (Los 1 „Kindertagesstätte Wibbelstätz“, Los 3 „Gemeinschaftsgrundschule Im Zentrum“, Los 4 „Ernst-Mach-Gymnasium“).
  Einschätzung: Der Testfall ist ein Neuzuschnitt in 6 statt 5 Losen und schließt neu „Unterkünfte für Geflüchtete“ ein (2025 eigenes Verfahren
  „Reinigungsleistungen Übergangsheime (Los 7)“, 519520-2025/672894-2025, nicht geöffnet). Der Kernbestand ist identisch; ohne Objektliste des
  Testfalls lässt sich der Umfang der Erweiterung nicht beziffern (Grenzfall zu teilmenge).
- Vertragsende Vorgänger: 488753-2023: 2023-12-01 bis 2026-11-30, „einmalige Verlängerung … um ein Jahr“ (spätestens 2027-11-30). Testfall-Beginn
  2026-12-01 schließt an die Grundlaufzeit an. Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 3/3

### T43 – 508130-2026 (2026-07-22) – Bundesanstalt für Immobilienaufgaben
- Objekt(e): BImA-Wohnliegenschaften (zentrale Vergabestelle Bonn), „VOEK 175-26“: Los 1/7 Schwerin (WE 120208 Erich-Weinert-Str. 16–23,
  WE 120209 Jean-Sibelius-Str. 19–25, WE 120210 Hagenower Str. 49–71); Los 2/8 Sanitz (4 WE, Ernst-Schneller-Str., Ribnitzer Str.); Los 3/9 Greifswald
  (6 WE, Erich-Weinert-Str., Gerhardt-Katsch-Str., Paul-Uhlenhuth-Str.); Los 4/10 Rügen (8 WE in Sassnitz, Binz, Bergen, Putbus); Los 5/10 Stralsund
  (11 WE, Große Parower Str., Bertolt-Brecht-Str.); Los 6/9 Stralsund (6 WE, Herrmann-Burmeister-Str., Leo-Tolstoi-Weg, Lion-Feuchtwanger-Str.,
  Arnold-Zweig-Str.). Lose 1–6 Treppenhausreinigung, Lose 7–10 Glasreinigung. Laufzeit 2027-02-01 bis 2031-01-31.
- Leistungsart: Treppenhausreinigung (regelmäßige Reinigung der Eingangsbereiche und Verkehrswege = Unterhaltsreinigung) und Glasreinigung.
- Suchschritte:
  1. API Kontrolle `FT=(Sibelius OR Parower OR Uhlenhuth OR Feuchtwanger) AND classification-cpv=909*` → 16 Treffer (Testfall; BImA 222266-2020,
     472319-2020; Rest andere Auftraggeber wie Kita gGmbH Schwerin, Hansestadt Stralsund, Bezirkskliniken Mittelfranken, Helsinki)
  2. API `FT=(120208 OR 116089 OR 118359 OR 118390 OR 118367 OR 118419) AND classification-cpv=909*` (WE-Nummern) → 21 Treffer (nur Testfall
     einschlägig; Rest Zahlen-Fehltreffer aus RO/LT/ES)
  3. lokal buyer~`Immobilienaufgaben` und Text~`Stralsund|Greifswald|Sanitz|Schwerin|Sassnitz|Rügen|Rostock` (Suche B, eForms) → 41 Treffer;
     einziges Treppenhaus-Verfahren 499653-2025/7674-2026 betrifft „Rostock und Bentwisch“ (andere Objekte)
  - XML geöffnet: 222266-2020, 472319-2020
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 472319-2020 (result, vor eForms, 2020-10-07), REF_NOTICE „2020/S 093-222266“ → 222266-2020 (competition, vor eForms, 2020-05-13), „VOEK 046-20“
- Beleg: 222266-2020/472319-2020 „Gebäudereinigungsleistungen (Unterhalts-/Treppenhaus und Glasreinigungsleistungen) für diverse Wohnliegenschaften
  in Mecklenburg-Vorpommern, … Direktion Rostock“: Los 1 „6 Liegenschaften in Stralsund: Hermann-Burmeister-Str. 41-45; Leo-Tolstoi-Weg 5 (A/B) + 7 (A/B);
  Lion-Feuchtwanger-Str. 17-21 …; Arnold-Zweig-Str. 57-64; … 108-110; … 124-127“; Los 2 „11 Liegenschaften in Stralsund: Große Parower Str. 119-125 … Berthold-Brecht-Str. …“;
  Los 3 „6 Liegenschaften in Greifswald: Erich-Weinert-Str. 1; Gerhardt-Katsch-Str. 5 + 7; …“; Los 4 „8 Liegenschaften in Sassnitz, Binz, Bergen und Putbus“;
  Los 5 „4 Liegenschaften in Sanitz“; Los 6 „3 Liegenschaften in Schwerin“; Los 7/8 Glasreinigung für 31 bzw. 7 Liegenschaften. Alle 8 Lose am 2020-09-28 vergeben
  (u. a. „Treppenhausreinigung Rostock GmbH“, „SRS Stralsunder Reinigungsservice GmbH“). Objektbestand und Adressen identisch, Lose neu nummeriert, Glaslose neu geschnitten.
- Vertragsende Vorgänger: 2021-02-01 bis 2025-01-31, jährliche Verlängerung, „Max Vertragsdauer: 6 Jahre (31.1.2027)“. Testfall-Beginn 2027-02-01 schließt an
  die Höchstlaufzeit an. Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 3/2

### T44 – 632635-2026 (2026-09-14) – Staatsbetrieb Sächsisches Immobilien- und Baumanagement, Zentrale, Zentralstelle Vergabe- und Vertragsmanagement
- Objekt(e): „Reinigung IHI Zittau“ (Internationales Hochschulinstitut Zittau; Leistungsort nur „Zittau 02763“, keine Straße). „Unterhaltsreinigung:
  ca. 31.418,00 m² Reinigungsfläche pro Monat, Glasreinigung: ca. 4.491,00 m² … pro Jahr, Grundreinigung: ca. 17.186,00 m² … pro Laufzeit“.
  Laufzeit 2026-12-01 bis 2033-11-30. Zentrale Vergabestelle (SIB Dresden).
- Leistungsart: Unterhalts-, Grund- und Glasreinigung.
- Suchschritte:
  1. API Kontrolle `FT=(IHI OR Zittau) AND classification-cpv=909*` → 34 Treffer (u. a. SIB 631639-2021, 120164-2022, 354705-2022, 515983-2022,
     605875-2024, 776194-2024, 6116-2025, 135543-2025, 433835-2016; Stadt Zittau, BImA, Studentenwerk Dresden, BA, IKK, Fraunhofer)
  2. lokal Text~`Zittau|02763` (Suche B) → 16 Treffer (Stadt Zittau, BA, SIB „Reinigung AG Zittau“, SIB „Reinigung HS ZI/GR Standort Zittau“,
     Studentenwerk „Oberlausitz“, BImA)
  3. API `FT=(IHI OR Hochschulinstitut) AND classification-cpv=909*` → 1 Treffer (nur Testfall)
  - XML geöffnet: 631639-2021, 120164-2022, 354705-2022, 515983-2022, 776194-2024, 433835-2016
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Fakt: „IHI“ und „Hochschulinstitut“ kommen in keiner älteren CPV-909-Notice vor. Die SIB-Verfahren in Zittau betreffen andere Einrichtungen:
  „Reinigung HS Zi/GR, Standort Zittau“ (631639-2021/120164-2022: „Hochschule Zittau/Görlitz; Standort Zittau“, ca. 357.675,80 m² pro Monat;
  Neuausschreibung 776194-2024/135543-2025: ca. 358.907 m² pro Monat), „Reinigungsleistungen HS Zittau/Görlitz, Standort Görlitz“ (354705-2022/515983-2022),
  „Reinigung AG Zittau“ (605875-2024/6116-2025, Amtsgericht, nicht geöffnet), 433835-2016 („Hochschule Zittau / Görlitz, Standorte in Zittau“).
  Keine dieser XML nennt IHI, Hochschulinstitut oder Markt 23 (grep: 0 Treffer in 776194-2024 und 433835-2016).
  Einschätzung: Das IHI (Einrichtung der TU Dresden) wurde vermutlich bisher unterschwellig oder über einen nicht auf TED veröffentlichten Vertrag gereinigt.
  Die Hochschulflächen sind 2021 und 2024 fast gleich, ein Herauslösen des IHI aus dem Hochschulvertrag ist daher nicht erkennbar.
- Vertragsende Vorgänger: unbekannt; Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 3/6

### T45 – 609162-2026 (2026-09-03) – Stadt Zeitz, Der Oberbürgermeister, Fachbereich Ordnungswesen
- Objekt(e): Rathaus (Altmarkt 1) und Gewandhaus (Altmarkt 16), 06712 Zeitz. Los 1 Unterhalts-/Grundreinigung, Los 2 Glasreinigung.
  Laufzeit 2027-01-01 bis 2030-12-31. (Altmarkt 1 ist zugleich die Amtsadresse; hier aber ausdrücklich als Reinigungsobjekt „Rathaus“ benannt.)
- Leistungsart: Unterhalts-, Grund- und Glasreinigung.
- Suchschritte:
  1. lokal buyer~`Zeitz` → 23 Treffer (Stadt Zeitz 18, u. a. 353504-2018, 36406-2019, 385160-2022, 669356-2022; VG Droyßiger-Zeitzer Forst; 1 Fehltreffer Berlin)
  2. API Kontrolle `FT=Gewandhaus AND buyer-city=Zeitz AND classification-cpv=909*` → 5 Treffer (353504-2018, 36406-2019, 385160-2022, 669356-2022, Testfall)
  - XML geöffnet: 385160-2022, 669356-2022
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 669356-2022 (result, vor eForms, 2022-12-02), REF_NOTICE „2022/S 135-385160“ → 385160-2022 (competition, vor eForms, 2022-07-15).
  Ältere Runde: 353504-2018 / 36406-2019 (per FT „Gewandhaus“ gefunden, nicht geöffnet).
- Beleg: 385160-2022: „Unterhalts-, Grund- und Glasreinigung im Rathaus der Stadt Zeitz, Altmarkt 1, und Im Gewandhaus, Altmarkt 16, 06712 Zeitz in 2 Losen
  im Zeitraum 01.01.2023 bis 31.12.2026“, „Los 1: Unterhaltsreinigung und Grundreinigung von Rathaus und Gewandhaus“, „Los 2: Glasreinigung von Rathaus
  und Gewandhaus“. 669356-2022: Los 1 vergeben 2022-11-15 an „clamex Gebäudereinigung GmbH“, Los 2 an „TÜ-Gebäudeservice GmbH“. Objekte, Adressen,
  Losaufteilung und Leistungsart identisch.
- Vertragsende Vorgänger: 2026-12-31. Testfall-Beginn 2027-01-01 schließt direkt an. Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 2/2

---

## Übersicht Teil 3 (T31–T45)

**Fakten: Anzahl je Kategorie (15 Fälle)**

| Kategorie | Anzahl | Fälle |
|---|---|---|
| objektgleich | 9 | T32, T36, T37, T38, T40, T41, T42, T43, T45 |
| teilmenge | 2 | T33, T34 |
| kein_vorgaenger | 4 | T31, T35, T39, T44 |
| unklar | 0 | – |

Gefunden (objektgleich + teilmenge): 11 von 15.

| Fall | Kategorie | Jüngster Vorgänger (Formular) | Belegstärke | Vertragsende Vorgänger | vorzeitig |
|---|---|---|---|---|---|
| T31 | kein_vorgaenger | – (nur Baureinigung 291547-2026/467991-2026) | – | – | nein |
| T32 | objektgleich | 498737-2025 (result, eForms) ← 279541-2025 | stark | 2027-08-31 | **ja** (Start 2027-01-01) |
| T33 | teilmenge | 254121-2019 (result, vor eForms) ← 75546-2019; Marzahn auch 250469-2019 | stark | max. 2024-04-30 | nein |
| T34 | teilmenge | 255487-2018 (result, vor eForms) ← 56913-2018 | stark | max. 2022-04-30 | nein |
| T35 | kein_vorgaenger | – (Neubau) | – | – | nein |
| T36 | objektgleich | 92431-2024 (result, eForms); Ausschreibung vermutl. 607255-2023 | stark | 2026-01-31 (+2× 1 J.) | nein |
| T37 | objektgleich | 697551-2022 (result, vor eForms) ← 384752-2022 | stark | 2025-12-31 oder 2026-12-31 | nein |
| T38 | objektgleich | 32306-2021 (competition, vor eForms) | stark | max. 2025-04-30 | nein |
| T39 | kein_vorgaenger | – | – | – | unklar |
| T40 | objektgleich | 327439-2022 (result, vor eForms) ← 138159-2022 | mittel | 2024-12-31 (Option 2025-12-31) | nein |
| T41 | objektgleich | 676959-2022 (result, vor eForms) ← 347342-2022 | stark | 2027-01-31 | nein |
| T42 | objektgleich | 488753-2023 (competition, vor eForms) | stark (3 genannte Objekte) | 2026-11-30 (+1 J.) | nein |
| T43 | objektgleich | 472319-2020 (result, vor eForms) ← 222266-2020 | stark | max. 2027-01-31 | nein |
| T44 | kein_vorgaenger | – | – | – | unklar |
| T45 | objektgleich | 669356-2022 (result, vor eForms) ← 385160-2022 | stark | 2026-12-31 | nein |

**Budget:** Kein Fall hat das Budget (15 Abfragen / 10 XML) erreicht. Höchstwerte: T31 6/5, T33 2/7, T44 3/6, T38 5/1.

**Auffälligkeiten (Fakten mit Notice-Nummer)**
- *Neubauten:* T31 (Bildungshaus Winkelwiese, vorher nur Baureinigung 291547-2026/467991-2026) und T35 („neu errichtete Grundschule“ Hangelsberg).
- *Zentrale Vergabestellen:* T32 (KSM Kommunalservice Mecklenburg für den Landkreis), T43 (BImA Bonn, früher „Direktion Rostock“, Verfahren 222266-2020 unter
  Auftraggeberort Berlin), T44 (SIB Dresden, viele Zittauer Objekte verschiedener Einrichtungen), T41 (BwDLZ Bogen vergibt für viele Kasernen; nur der
  Kasernenname trennt).
- *Namens- und Formwechsel:* T33 „Berliner Verkehrsbetriebe (BVG) / AöR“ → „Berliner Verkehrsbetriebe, Bereich Einkauf/ Materialwirtschaft“; T45
  „Fachbereich Baurecht / Vergabestelle“ (2018) → „Fachbereich Ordnungswesen“ (2022); T36 Tippfehler „Baurechtesamt“ in 174453-2024.
- *Neuzuschnitte:* T33 (Kundenzentren 2019 mit Betriebshöfen gebündelt, 2026 eigene Lose 29/30), T34 (1 von 3 Hallen), T42 (5 → 6 Lose, Unterkünfte für
  Geflüchtete neu), T43 (Glaslose neu geschnitten).
- *Amtsadressen:* T33 (PLZ 10179 = BVG-Zentrale), T40 (Münsterstr. 156 = Campus und Dienstadresse) – nicht als Objektbeleg gewertet.
- *Lücken auf TED:* T34 (Halle Neuforweiler: Vertrag bis spätestens 2022-04-30, danach nichts bis 2026) und T38 (Palmengarten: max. 2025-04-30, Neubeginn
  2027-01-01); T38 außerdem ohne auffindbaren Zuschlag zu 32306-2021.
- *Vorzeitige Neuvergabe:* nur T32 (Start 2027-01-01, Grundlaufzeit des Vorgängers bis 2027-08-31).

**Werkzeuge**
- `FT` funktionierte in allen 15 Fällen als Kontrollabfrage (Testfall jeweils gefunden). Bindestrich-Begriffe werden zerlegt (T41: `FT=Graf-Aswin-Kaserne`
  → 802 Treffer; `FT=Aswin` → 5). Zahlen (WE-Nummern, T43) und Vergabekürzel (T38 „LDL020“) erzeugen viele Fehltreffer.
- Notices nach dem Testfall (z. B. 540201-2026, 670788-2026, 700159-2026 bei T38; 554188-2026 bei T42; 676568-2026 bei T40) wurden nicht als Vorgänger gewertet.

**Einschätzungen (keine Fakten)**
- Die vier Fälle ohne Vorgänger haben erkennbare Gründe: zwei Neubauten (T31, T35), ein Auftraggeber ohne frühere TED-Präsenz (T39) und ein Objekt, das
  bisher offenbar nicht auf TED vergeben wurde (T44).
- Bei T33 könnte 258434-2024 der eigentliche jüngste Vorgänger sein (Kundenzentren in BFKÖ/BFMAR enthalten?); das ist aus TED nicht entscheidbar.
- Bei T42 liegt ein Grenzfall zwischen objektgleich und teilmenge vor, weil der Testfall nur drei Beispielobjekte nennt.
