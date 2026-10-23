# Sichtbarkeit der Vorgänger – Handsuche Iteration 3, Teil 1 (T1–T15)

Rechercheur (Subagent), Recherche am 2026-10-23. Testfälle: Zeilen 1–15 aus `reports/testfaelle_iteration3.txt`.
Definitionen: `docs/iterationen.md`, Iteration 3, „Begriffe“. Unabhängigkeit: Regel-, Merkmals- und Ergebnisdateien
(`src/zuordnung_*.py`, `src/objekt_merkmale.py`, `data/processed/`, `reports/zuordnung_*`, `k2_*`, `blindpruefung_*`) wurden nicht gelesen.

## Vorgehen und Konventionen

**Quellen**
- *Lokal* (zählt als Abfrage): unveränderte API-Rohdaten `data/raw/ted_search/DEU_result_cpv909_20161001_20260930/` (15.274 Notices) und
  `data/raw/ted_search/DEU_competition_cpv909_20161001_20260930/` (19.876 Notices). Gefiltert immer auf 20161001 ≤ Veröffentlichung < Testfalldatum.
  „buyer-name~x“ = Teilstring im Auftraggebernamen; „Text~x“ = Teilstring in Auftraggebername, -ort, -PLZ, Titel (Verfahren/Los),
  Leistungsort (Ort, PLZ, Straße). Vor eForms sind in diesen Rohdaten nur Auftraggebername und -ort gefüllt, keine Titel.
- *Live-API* (`POST https://api.ted.europa.eu/v3/notices/search`): vor allem das Volltextfeld `FT`, das auch Notices vor eForms abdeckt.
  `FT` wurde per Kontrollabfrage geprüft (T2: `FT~"30.445,00"` findet den Testfall selbst). Die API-Abfragen sind nicht nach
  `form-type` getrennt (eine Abfrage liefert result und competition, ggf. auch Berichtigungen, die ignoriert wurden).
- *XML*: `https://ted.europa.eu/en/notice/<nr>/xml`.
- Alle API-Antworten (mit Request) und XML liegen unverändert unter `data/raw/rechercheur_20261023/<Testfall-Nummer>/`.

**Zählung:** „Abfragen/XML“ = lokale + API-Abfragen / geöffnete Kandidaten-XML. Die XML des Testfalls selbst ist nicht mitgezählt.

**Kategorien-Konvention (Auslegung der Definition, auf Verfahrensebene):**
- *objektgleich*: Liegenschaft(en) per Name oder Adresse identisch, Leistungsart überlappt; kleine Abweichungen im Objektbestand
  (ein Objekt mehr/weniger) oder eine neue Losaufteilung desselben Bestands bleiben objektgleich.
- *teilmenge*: nur ein Teil der Objekte gemeinsam (z. B. Testfall deutlich erweitert, oder Vorgänger war ein größeres Bündel).
- Zusätzlich angegeben: **Belegstärke** (stark = Adresse/Liegenschaftsname wörtlich gleich; mittel = Sammelbezeichnung + Kennzahlen/Losnummer;
  schwach = nur indirekt). Das ist eine Einschätzung und keine Kategorie der Definition.

---

### T1 – 644509-2026 (2026-09-18) – Regionalverband Saarbrücken
- Objekt(e): 12 Schulen in 3 Losen. Los 1: Schule Winterbachsroth (FSG) Dudweiler, Gemeinschaftsschule Saarbrücken-Dudweiler, Gymnasium am Schloss,
  Deutsch-Französisches Gymnasium, TGBBZ II Sporthalle Mügelsberg. Los 2: WWG, GemS Rastbachtal, Friedrich-Joachim-Stengel-Schule (FSG),
  Internationale Schule. Los 3: Katharine-Weißgerber-Schule GemS Klarenthal + Außenstelle Gersweiler, GemS Kleinblittersdorf, KBBZ Halberg.
  Laufzeit 01.01.2027–31.12.2030 (+1 Jahr Option).
- Leistungsart: Unterhalts- und Grundreinigung.
- Suchschritte:
  - lokal buyer-name~"regionalverband saarbr" → 13 (6 result, 7 competition)
  - lokal buyer-name~"saarbr" → 64 (29/35)
  - Suche B nicht nötig (A ergab objektgleichen Treffer).
  - XML: 241031-2026 (18 Schulen, andere Objekte), 624151-2025 (15 Schulen, andere Objekte), 418222-2022 (18 Schulstandorte, enthält „TGBBZ I und II
    Mügelsberg“), 601599-2023 (nur Glasreinigung 44 Schulen), **387492-2021**, 365553-2020 (15 Schulen Sulzbachtal/Saarbrücken/Völklingen),
    18921-2019 (Verwaltungsgebäude), **547893-2021**.
- Ergebnis: **objektgleich** (Belegstärke: stark)
- Vorgänger: **547893-2021**, result, vor eForms, 2021-10-27 (REF `2021/S 146-387492` → 387492-2021, competition, 2021-07-30)
- Beleg: 547893-2021 „Unterhalts- und Grundreinigung an 13 Schulstandorte“; Los 1 „FSG Winterbachsroth Dudweiler - GemS Sulzbachtal Dudweiler“,
  Los 2 „FSG Saarbrücken - GemS Rastbachtal - TGBBZII_AS_Malstatt - WWG - TGBBII_Turnhalle_Mügelsberg“, Los 3 „GemS Klarenthal Außenstelle
  Gersweiler - GemS Klarenthal - GemS Kleinblittersdorf - KBBZ Halberg“, Los 4 „DFG - Gymnasium am Schloss“. Leistungsart identisch.
  Abweichung: „TGBBZII_AS_Malstatt“ entfällt, „Internationale Schule“ kommt hinzu (Einschätzung: „GemS Sulzbachtal Dudweiler“ = „Gemeinschaftsschule
  Saarbrücken-Dudweiler“ und „FSG Saarbrücken“ = „Friedrich-Joachim-Stengel-Schule“).
- Vertragsende Vorgänger: 31.12.2025 (387492-2021: DATE_START 2022-01-01, DATE_END 2025-12-31, `NO_RENEWAL`). Hinweis auf vorzeitige Neuvergabe:
  **nein** (neuer Beginn 01.01.2027, ein Jahr nach Grundlaufzeitende; Überbrückung 2026 auf TED nicht sichtbar).
- Abfragen/XML: 2/8

### T2 – 554609-2026 (2026-08-11) – Vermögen und Bau Baden-Württemberg, Amt Freiburg
- Objekt(e): nicht benannt. Leistungsort im XML nur „Mozartstraße 58, 79104 Freiburg“ (= Adresse des Amtes). Kennzahlen: UHR ca. 30.445 m²/Monat,
  Grundreinigung ca. 7.304 m², Glas ca. 1.794 m². Laufzeit 01.12.2026–30.11.2031. Interne ID 26-33311.
- Leistungsart: Unterhalts-, Grund- und Glasreinigung.
- Suchschritte:
  - lokal buyer-name~"vermögen und bau" UND ~"freiburg" → 88 (41/47)
  - API `FT~"30.445" AND buyer-country=DEU AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260810` → 0
  - API (Kontrolle) `FT~"30.445,00" AND buyer-country=DEU AND publication-date>=20260801 AND publication-date<=20260930` → 1 (der Testfall selbst)
  - API `FT~"30.445,00" AND buyer-country=DEU AND publication-date>=20161001 AND publication-date<=20260810` → 0
  - API `(FT~"7.304,00" OR FT~"1.794,00") AND buyer-country=DEU AND classification-cpv=909* AND …<=20260810` → 0
  - Suche B nicht möglich (kein objektspezifischer Ort).
  - XML: 542576-2026, 665966-2023, 319819-2021, 431549-2021, 600677-2021, 600793-2021, 661992-2021.
- Ergebnis: **unklar**
- Vorgänger: keiner belegbar.
- Beleg / Begründung: Das Objekt ist im Testfall nicht identifizierbar. Zwei Zuschläge desselben Amtes tragen formal dieselbe Leistungsort-Adresse
  „Mozartstraße 58“ und dieselbe Leistungsart, sind aber nach Flächen andere Objekte: 542576-2026 „Fläche der UHR pro Monat ca. : 24.180 m²“
  (REF 361366-2026, 01.09.2026–31.08.2031) und 665966-2023 „monatl. Reinigungsfläche ca. 46.000 m²“ (01.12.2023–30.11.2028). Ältere Kandidaten
  sind andere Liegenschaften: PH Freiburg, Kunzenweg 21 (319819-2021/431549-2021, 285.000 m²), Polizei Offenburg (600677-2021), Bauendreinigung
  Breisacher Str. 62 (600793-2021), Müllheimer Str. 7 (661992-2021). Die Flächenangaben des Testfalls kommen in keiner früheren Notice vor.
- Vertragsende Vorgänger: unbekannt; vorzeitige Neuvergabe: unklar.
- Abfragen/XML: 5/7 (davon 1 Kontrollabfrage)

### T3 – 546143-2026 (2026-08-06) – Stadt Heidelberg, Hochbauamt – Objektservice
- Objekt(e): Bürogebäude Eppelheimer Straße 13, 69115 Heidelberg. Laufzeit 01.04.2027–31.03.2029, danach jährliche Verlängerung.
- Leistungsart: Unterhaltsreinigung.
- Suchschritte:
  - lokal buyer-name~"heidelberg" → 80 (32/48)
  - lokal buyer-name~"stadt heidelberg" → 18 (8/10)
  - lokal Text~"eppelheimer" → 0
  - API `(FT~"Eppelheimer" OR FT~"Eppelheimerstraße" OR FT~"Eppelheimer Straße") AND buyer-country=DEU AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260805` → 3
    (747880-2025 Stadt Eppelheim Sporthalle; 595211-2021 und 125161-2022 VB-BW, Objekt „Handelsstr. 13, 69214 Eppelheim“)
  - Suche B: lokal Leistungsort-PLZ = 69115 → 11 (Johannes-Gutenberg-Schule, HCC, bundesweite Bündel; nichts mit Eppelheimer Straße)
  - XML: 595211-2021, 284901-2019, 475171-2018, 216395-2018, 538713-2026, 503205-2017, 132645-2017, 63376-2017.
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Keine Notice vor dem Testfall nennt „Eppelheimer Straße 13“ oder ein Bürogebäude dort. Die geöffneten Ausschreibungen der Stadt
  Heidelberg 2017–2019 betreffen Schulen, Sporthallen, Friedhöfe, Berufsfeuerwehr, Bürgerämter. 538713-2026 (2 Tage vor dem Testfall) ist eine
  Parallelausschreibung mit gleichem Starttermin (01.04.2027) für andere Objekte (Bürgeramt Ziegelhausen, Kitas u. a.).
- Vertragsende Vorgänger: –; vorzeitige Neuvergabe: –
- Abfragen/XML: 5/8

### T4 – 530979-2026 (2026-07-31) – Stadt Wuppertal
- Objekt(e): Rahmenvereinbarung Fenster- und Innenglasreinigung im Bezirk Wuppertal-Uellendahl (Verwaltungen, Schulen, Kitas, Sportstätten;
  Einzelobjekte nur im Flächenverzeichnis). Laufzeit 36 Monate (+ bis 12 Monate Option), Beginn nicht angegeben.
- Leistungsart: Glasreinigung.
- Suchschritte:
  - lokal buyer-name~"wuppertal" → 161 (35/126)
  - API `FT~"Uellendahl" AND buyer-country=DEU AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260730` → 13
  - XML: 578851-2023 (Innenreinigung u. a. Uellendahl 1), **202519-2022**, 463753-2021, 454080-2021 (Unterhaltsreinigung Uellendahl 2),
    270869-2022 und 270960-2022 (Zuschläge Glas Vohwinkel).
- Ergebnis: **objektgleich** (Belegstärke: mittel – gleiche Bündelbezeichnung, Einzelobjekte in beiden Notices nicht gelistet)
- Vorgänger: **202519-2022**, competition, vor eForms, 2022-04-15 (Zuschlag auf TED nicht gefunden). Älter: 463753-2021 (competition, Glas Uellendahl).
- Beleg: 202519-2022 „Fenster- und Glasreinigung in Wuppertal Uellendahl … an und in Gebäuden der Schulen, Tagesstätten für Kinder (TfK),
  Sporthallen und Verwaltungen im Bereich Wuppertal-Uellendahl … 32 Liegenschaften“. Testfall: „Glas und Innenglasreinigung Wuppertal Uellendahl in
  Verwaltungen, Schulen, Kindestagesstäten sowie Sportstätten“.
- Vertragsende Vorgänger: Grundlaufzeit 01.09.2022–31.08.2025, Option bis 12 Monate (also spätestens 31.08.2026). Vorzeitige Neuvergabe: **nein**.
- Abfragen/XML: 2/6

### T5 – 598474-2026 (2026-08-31) – IKK classic
- Objekt(e): Universitätsstraße 68, 44789 Bochum. Los 1 Unterhaltsreinigung, Los 2 Glas- und Rahmenreinigung. 01.01.2027–31.12.2027, jährliche
  Verlängerung bis längstens 31.12.2030.
- Leistungsart: Unterhalts- und Glasreinigung.
- Suchschritte:
  - lokal buyer-name~"ikk" → 144 (72/72) (gemeinsame Abfrage mit T15, Stichtag 20260914; für T5 nur Treffer vor 20260831 betrachtet)
  - API `buyer-name~"IKK" AND FT~"Bochum" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260830` → 5
  - lokal buyer~"ikk" UND Text~(westfalen|bochum|universitätsstr) → 0 (Kontrolle auf jüngere eForms-Vergabe)
  - XML: 477850-2022, 670866-2022, 665652-2022.
- Ergebnis: **objektgleich** (Belegstärke: stark)
- Vorgänger: **670866-2022**, result, vor eForms, 2022-12-02 (zweiter Zuschlag zum selben Verfahren: 665652-2022 vom 2022-11-30; REF
  `2022/S 169-477850` → 477850-2022, competition, 2022-09-02, „Reinigung Westfalen-Lippe (11/AD/2022)“)
- Beleg: Los 3 „Unterhaltsreinigung Universitätsstraße 68, 44789 Bochum“, Los 4 „Glas- und Rahmenreinigung Universitätsstraße 68, 44789 Bochum“.
- Vertragsende Vorgänger: 477850-2022 Lose 3/4: 01.08.2023–31.12.2024, „verlängert sich um ein weiteres Jahr, längstens jedoch bis zum 31.12.2026“.
  Vorzeitige Neuvergabe: **nein** (nahtloser Anschluss 01.01.2027).
- Abfragen/XML: 3/3 (inkl. gemeinsamer IKK-Abfrage)

### T6 – 461152-2026 (2026-07-06) – Kreis Weimarer Land
- Objekt(e) (8 Lose, alle 99510 Apolda): Gemeinschaftsunterkünfte Auf dem Angespanne 3, Lessingstraße 48a, Nordstraße 25, Stobraer Straße 2
  (Lose 1–4); Landratsamt Bahnhofstraße 28 und Robert-Koch-Straße 4 (Los 5); Jobcenter/Landratsamt Herderstraße 10 (Los 6); Kreisarchiv
  Lessingstraße 48b und Kreisvolkshochschule Bernhardstraße 16 (Los 7); Glasreinigung einzelner Objekte (Los 8). 01.01.2027–31.12.2028 (+2×1 Jahr).
- Leistungsart: Unterhaltsreinigung, Glasreinigung.
- Suchschritte:
  - lokal buyer-name~"weimarer land" → 16 (5/11)
  - lokal Text~"apolda" → 19 (6/13)
  - API `buyer-name~"Weimarer Land" AND (FT~"Gemeinschaftsunterkunft" OR FT~"Angespanne" OR FT~"Stobraer" OR FT~"Herderstraße" OR FT~"Bahnhofstraße" OR FT~"Kreisarchiv" OR FT~"Jobcenter") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260705` → 21
    (nicht trennscharf, „Bahnhofstraße“ ist auch die Auftraggeberadresse)
  - API `buyer-name~"Weimarer Land" AND (FT~"Gemeinschaftsunterkunft" OR FT~"Flüchtlinge" OR FT~"Angespanne" OR FT~"Stobraer") AND publication-date>=20161001 AND publication-date<=20260705` → 6
    (nur Bewachung/Schülerbeförderung, keine Reinigung)
  - XML: 417745-2023 (Schulen), **364258-2023**, 247271-2021 (Schulen).
- Ergebnis: **teilmenge** (Belegstärke: stark für die gemeinsamen Objekte)
- Vorgänger: **364258-2023**, competition, vor eForms, 2023-06-19 (Zuschlag auf TED nicht gefunden)
- Beleg: 364258-2023 „Gebäude- und Glasreinigung für das Landratsamt Weimarer Land in 4 Losen“: Los 1 „Landratsamt Weimarer Land, Bahnhofstraße 28
  und Schulplatz 3 in 99510 Apolda“, Los 2 „Kreisvolkshochschule, Bernhardstraße 16“, Los 3 „Jobcenter Apolda, Herderstraße 10 …“, Los 4 Glas.
  Gemeinsam: Bahnhofstraße 28, Bernhardstraße 16, Herderstraße 10, Glas. Neu im Testfall: vier Gemeinschaftsunterkünfte, Robert-Koch-Straße 4,
  Kreisarchiv (für diese kein 909-Vorgänger auf TED).
- Vertragsende Vorgänger: Grundlaufzeit 01.01.2024–31.12.2025, Option jährlich „längstens jedoch bis zum 31.12.2027“. Vorzeitige Neuvergabe:
  **nein** nach Definition (Bezug Grundlaufzeit); Einschätzung: Neuvergabe vor Ausschöpfung der letzten Option.
- Abfragen/XML: 4/3

### T7 – 503493-2026 (2026-07-21) – Bundesanstalt für Immobilienaufgaben
- Objekt(e): Kassel: FKS Zollamt Gießen, Lilienthalstr. 3 (WE 129867); Zollamt Kassel, Lilienthalstr. 1 (WE 141739); Bürogebäude BImA & Zoll,
  Hasselweg 20 (WE 129862); Zollfahndungsamt, Elsässer Str. 15 (WE 129863); Los 3 Bundespolizeiinspektion Kassel (WE 132156). VOEK 077-26.
  01.04.2027–31.03.2031, jährliche Verlängerung bis max. 31.03.2033.
- Leistungsart: Unterhalts- und Glasreinigung.
- Suchschritte:
  - lokal buyer~"bundesanstalt für immobilien" UND Text~"kassel" → 0 (vor eForms fehlen Titel/Orte in den Rohdaten)
  - API `FT~"Kassel" AND (FT~"Lilienthalstr" OR FT~"Lilienthalstraße" OR FT~"Hasselweg" OR FT~"Elsässer") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260720` → 8
  - XML: 607469-2020, **155215-2021**, 317212-2017.
- Ergebnis: **objektgleich** (Belegstärke: stark)
- Vorgänger: **155215-2021**, result, vor eForms, 2021-03-29 (REF `2020/S 245-607469` → 607469-2020, competition, 2020-12-16, VOEK 154-20).
  Älter: 317212-2017 (VOEK-209-16, dieselben WE-Nummern, 01.02.2018–31.01.2019).
- Beleg: 155215-2021 MAIN_SITE „Behördenhaus BImA & Zoll Hasselweg 20 34131 Kassel / Zollfahndungsamt Elsässer Str. 15 / FKS d. Zollamt Gießen
  Lilienthalstr. 3 / Zollamt Kassel Lilienthalstr. 1“ (Lose 1 und 2), Los 3 „Bundespolizeiinspektion Kassel Heerstr. 5“; Titel „… (Unterhalts- und
  Glasreinigungsleistungen) für Dienstliegenschaften in Kassel“.
- Vertragsende Vorgänger: „zunächst für die Dauer von 4 Jahren bis zum 31.3.2025 … verlängert sich … jeweils um ein weiteres Jahr“. Vorzeitige
  Neuvergabe: **nein**.
- Abfragen/XML: 2/3

### T8 – 656958-2026 (2026-09-23) – Land Niedersachsen, vertreten durch das Staatliche Baumanagement Braunschweig
- Objekt(e): Polizeiinspektion Stade, 21680 Stade, plus umliegende Liegenschaften (Buxtehude, Fredenbeck, Horneburg, Jork, Drochtersen, Himmelpforten,
  Steinkirchen, Harsefeld). UHR ca. 9.006 m², Glas ca. 1.925 m². 01.02.2027–31.01.2028, Verlängerung bis 31.01.2034. IGM 26E1011.
- Leistungsart: Unterhalts- und Glasreinigung.
- Suchschritte:
  - lokal Text~"stade" → 74 (30/44)
  - API `FT~"Polizeiinspektion Stade" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260922` → 2
  - API `(FT~"Polizeidirektion Lüneburg" OR FT~"PI Stade" OR (FT~"Polizei" AND FT~"Stade")) AND classification-cpv=909* AND …<=20260922` → 112 (Rauschen;
    in Niedersachsen nur die beiden bekannten Notices)
  - XML: 472607-2018, **165901-2019**.
- Ergebnis: **objektgleich** (Belegstärke: stark für den Liegenschaftsnamen)
- Vorgänger: **165901-2019**, result, vor eForms, 2019-04-09 (REF `2018/S 207-472607` → 472607-2018, competition, 2018-10-26)
- Beleg: „18 E 10064 – Polizeidirektion Lüneburg – Gebäudereinigung … – Unterhalts- und Glasreinigung“, Los 4 „Gebäudereinigung Polizeiinspektion
  Stade“, Zuschlag Los 4 „Polizeiinspektion Stade - Unterhaltsreinigung“ an Prior & Peußner GmbH (2019-03-27). Glas-Lose 9–11 betreffen nur Celle,
  Behördenzentrum Lüneburg und Lüchow; die Leistungsart überlappt über die Unterhaltsreinigung.
- Vertragsende Vorgänger: 01.05.2019–30.04.2020, `NO_RENEWAL`. Vorzeitige Neuvergabe: **nein**. Einschätzung: Zwischen 2020 und 2027 muss ein
  weiterer Vertrag bestanden haben, der auf TED nicht als 909-Notice auffindbar war.
- Abfragen/XML: 3/2

### T9 – 610118-2026 (2026-09-04) – Vermögen und Bau Baden-Württemberg, Amt Schwäbisch Gmünd
- Objekt(e): „Polizei Heidenheim“ (keine Objektadresse; im XML nur Amtsadresse Rektor-Klaus-Straße 76, Schwäbisch Gmünd). UHR ca. 16.600 m²/Monat,
  Grund ca. 3.400 m², Glas ca. 200 m². 01.01.2027–31.12.2031. Interne ID 26-75185.
- Leistungsart: Unterhalts- und Grundreinigung (zusätzlich Glas).
- Suchschritte:
  - lokal Text~"heidenheim" → 20 (5/15)
  - API `FT~"Heidenheim" AND FT~"Polizei" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260903` → 0
  - API `FT~"Heidenheim" AND (FT~"Polizeirevier" OR FT~"Polizeipräsidium" OR FT~"Polizeigebäude" OR FT~"Polizeidienstgebäude" OR FT~"Polizeidirektion" OR FT~"Polizeiposten") AND classification-cpv=909* AND …<=20260903` → 0
  - lokal buyer-name~"schwäbisch gmünd" UND ~"verm" → 53 (24/29)
  - API `FT~"Heidenheim" AND (buyer-name~"Vermögen" OR buyer-name~"Landesbetrieb") AND classification-cpv=909* AND …<=20260903` → 9
  - XML: 153652-2020, 145160-2018, 396574-2017, 431239-2016, 365115-2025, 384781-2025, 567540-2025.
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Alle Heidenheim-Treffer des Amtes betreffen andere Objekte: Duale Hochschule, Hanns-Voith-Campus 1 (365115-2025, 384781-2025, 567540-2025),
  Winterdienst Bezirk Heidenheim (431239-2016). Die übrigen geöffneten Notices: Hochschule Aalen, Finanzamt Aalen, Geislingen. Keine Notice nennt
  ein Polizeigebäude in Heidenheim.
- Vertragsende Vorgänger: –. Auffällig (Fakt aus den lokalen Rohdaten): Zwischen 2020-03-31 und 2022-08-12 gibt es keine 909-Notice des Amtes
  Schwäbisch Gmünd; ein Vorgänger mit Beginn 01.01.2022 (5 Jahre) wäre in diese Lücke gefallen. Einschätzung: Ein Vorgänger existiert vermutlich,
  ist auf TED aber nicht (als 909) veröffentlicht oder nicht auffindbar.
- Abfragen/XML: 5/7

### T10 – 514223-2026 (2026-07-24) – Stadt Blankenburg (Harz)
- Objekt(e): „städtische Objekte und Einrichtungen der Stadt Blankenburg (Harz) und Ortsteile“, 53 Objekte, ca. 3,6 Mio m² Jahresreinigungsfläche,
  11.200 m² Grundreinigung, Glas ca. 3.400 m². Keine Einzelobjekte in der Bekanntmachung. 01.01.2027–31.12.2030.
- Leistungsart: Unterhalts-, Grund-, Glas- und Rahmenreinigung.
- Suchschritte:
  - lokal Text~"blankenburg" → 2 (0/2)
  - API `FT~"Blankenburg" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260723` → 9 (sonst nur Bundeswehr,
    Landkreis Harz, Saalfeld-Rudolstadt, DB)
  - XML: **465718-2022**.
- Ergebnis: **teilmenge** (Belegstärke: mittel – Sammelbezeichnung und Kennzahlen; kein Einzelobjekt im Testfall namentlich bestätigt)
- Vorgänger: **465718-2022**, competition, vor eForms, 2022-08-26 (Zuschlag auf TED nicht gefunden)
- Beleg: 465718-2022 (gleicher Auftraggeber, „OV-BlankenburgHarz-22“): „Unterhalts- und Grundreinigung von 45 Objekten mit einer Jahresreinigungsfläche von
  ca. 3,2 Mio. Quadratmetern und einer Grundreinigungsfläche von ca. 7.000 Quadratmetern“, Begehung u. a. „Grundschulen Martin Luther, Am Regenstein,
  Derenburg und Timmenrode sowie im Sportforum“. Testfall: 53 Objekte/3,6 Mio m² plus Glas → erweiterter Zuschnitt desselben städtischen Bestands
  (Einschätzung). Wer einen namentlichen Objektbeleg verlangt, müsste diesen Fall als „unklar“ werten.
- Vertragsende Vorgänger: 48 Monate (`DURATION 48`, `NO_RENEWAL`), Beginn nicht angegeben; Einschätzung: etwa 01.01.2023–31.12.2026. Vorzeitige
  Neuvergabe: **nein** (Einschätzung).
- Abfragen/XML: 2/1

### T11 – 506593-2026 (2026-07-22) – WISTA.Service GmbH
- Objekt(e): „Gebiet-Los 3“, neun Gebäude auf dem Wissenschaftscampus Berlin-Adlershof (Leistungsort im XML: Kekuléstr. 2-4, 12489 Berlin =
  Auftraggeberadresse). Ab 01.01.2027, 24 Monate + 4×12 Monate (bis 31.12.2032).
- Leistungsart: Unterhaltsreinigung.
- Suchschritte:
  - lokal buyer-name~"wista" → 9 (5/4)
  - API `(buyer-name~"WISTA" OR FT~"Adlershof") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260721` → 32
  - XML: 312117-2023, 146804-2022 (nur Glasreinigung), 375021-2019, **574481-2023**, 514877-2025.
- Ergebnis: **objektgleich** (Belegstärke: mittel – Losnummer und Gelände gleich, Gebäudelisten in keiner Bekanntmachung)
- Vorgänger: **574481-2023**, result, vor eForms, 2023-09-25 (REF `2023/S 101-312117` → 312117-2023, competition, 2023-05-26, „Unterhaltsreinigung ab
  2024 in 5 Losen“). Älter: 375021-2019 (Los 3 – WISTA Süd 2, 02.01.2020–31.12.2021).
- Beleg: 574481-2023 „Los 3 - WISTA Süd 2“, Zuschlag an Veolia Gebäudeservice Deutschland GmbH (2023-09-18); 312117-2023: „Unterhaltsreinigung …
  für den Standort Technologiepark Adlerhof für verschiedene Gebäude“. Stützend: Gebiet-Los 1 wurde zum Grundlaufzeitende des alten Loses 1 neu
  vergeben (514877-2025 „Gebiet-Los1 ab 01.01.2026“, zehn Gebäude), d. h. WISTA vergibt die alten Lose einzeln neu (Einschätzung).
- Vertragsende Vorgänger: 01.01.2024–31.12.2025, „kann um zweimal 12 Monate verlängert werden … max. 48 Monate“ (also spätestens 31.12.2027).
  Vorzeitige Neuvergabe: **nein** nach Definition (Grundlaufzeit endete 31.12.2025); Einschätzung: Neuvergabe vor Ausschöpfung der zweiten Option.
- Abfragen/XML: 2/5

### T12 – 615831-2026 (2026-09-07) – Stadt Pulheim
- Objekt(e): „alle städtischen Objekte“, 5 Lose: Pulheim Nord (11 Objekte, 32.750 qm), Pulheim Süd (19 Objekte, 29.120 qm), Brauweiler/Dansweiler
  (13 Objekte), Sinthern/Geyen, Stommeln, … (20 Objekte), Glasreinigung alle Objekte im Stadtgebiet (63 Objekte). 01.01.2027–31.12.2028 (+2×1 Jahr).
- Leistungsart: Unterhalts-, Grund- und Glasreinigung.
- Suchschritte:
  - lokal Text~"pulheim" → 11 (5/6)
  - API `FT~"Pulheim" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260906` → 30
  - XML: 378529-2023 (Abfallentsorgung), 172338-2023, 459072-2022, 567572-2023 (Abfallentsorgung), **434268-2023**, 652257-2022.
- Ergebnis: **objektgleich** (Belegstärke: stark über Sammelbezeichnung und Kennzahlen; Losgrenzen neu geschnitten)
- Vorgänger (jüngster): **434268-2023**, result, vor eForms, 2023-07-18 (REF `2023/S 058-172338` → 172338-2023, competition, 2023-03-22) für
  „städtische Objekte Pulheim Zentrum“. Für die übrigen Lose: **652257-2022**, result, vor eForms, 2022-11-25 (REF `2022/S 161-459072` → 459072-2022,
  competition, 2022-08-23).
- Beleg: 434268-2023 „Reinigungsdienstleistungen für städtische Objekte Pulheim Zentrum … 30 Objekte, 62.000 qm Reinigungsfläche“ = Testfall Los 1+2
  (11+19 = 30 Objekte, 32.750+29.120 = 61.870 qm). 459072-2022 „Reinigungsdienstleistungen für alle städtischen Objekte im Zeitraum 2023/2024 mit 2 x
  Verlängerungsoption … aufgeteilt in 4 Lose“: Pulheim, Brauweiler, „Stommeln, Sinnersdorf, Sinthern/ Geyen und Dansweiler“, „Glasreinigung gesamtes
  Stadtgebiet“; dort auch „Neuausschreibung im Jahr 2026“.
- Vertragsende Vorgänger: 434268/172338: 01.07.2023–31.12.2024 + max. 2 Jahre; 652257/459072: 01.01.2023–31.12.2024, „2 x Verlängerungsoption um je
  1 Jahr. Maximale Laufzeit 4 Jahre“ (also spätestens 31.12.2026). Vorzeitige Neuvergabe: **nein** (nahtlos 01.01.2027).
- Abfragen/XML: 2/6

### T13 – 613923-2026 (2026-09-07) – Verbandsgemeindeverwaltung Freinsheim
- Objekt(e): Einrichtungen der VG Freinsheim, 6 Lose (Glas, Sonderreinigung, vier Lose UHR/GR nach Ortsgemeinden), u. a. Kindergarten An der Bach
  (An der Bach 12), Grundschule Freinsheim (Haintorstraße 27), Kindergarten und Grundschule Kallstadt (Weinstraße 79), Feuerwehrgerätehäuser
  (Dackenheimer Straße 24, Freinsheimer Straße 75 u. a.), Rathaus Bahnhofstraße 12, Sporthalle Bahnhofstraße 12e. Ende 31.12.2028, Beginn nicht angegeben.
- Leistungsart: Unterhalts-, Grund-, Glas- und Sonderreinigung.
- Suchschritte:
  - lokal Text~"freinsheim" → 2 (1/1)
  - API `FT~"Freinsheim" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260906` → 2 (dieselben)
  - XML: 38357-2022, **285864-2022**.
- Ergebnis: **objektgleich** (Belegstärke: stark; Lose neu geschnitten – 2022 nach Leistungsart, 2026 nach Ortsgemeinde)
- Vorgänger: **285864-2022**, result, vor eForms, 2022-05-27 (REF `2022/S 016-038357` → 38357-2022, competition, 2022-01-24)
- Beleg: 38357-2022 Los 1 Unterhaltsreinigung: „Kindergarten An der Bach, An der Bach 12, 67251 Freinsheim“, „Grundschule Kallstadt, Weinstraße 79,
  67169 Kallstadt“, „Grundschule Freinsheim, Haintorstraße 27“, „Vertretungsreinigung Rathaus … Bahnhofstraße 12“; Los 2 Grundreinigung u. a.
  „Feuerwehrgerätehaus Freinsheim, Dackenheimer Straße 24“, „Sporthalle Freinsheim, Bahnhofstraße 12e“.
- Vertragsende Vorgänger: 48 Monate (`DURATION 48`), Vertragsschluss 2022-04-29, Beginn nicht angegeben; Einschätzung: Ende etwa Mitte 2026.
  Vorzeitige Neuvergabe: **unklar** (Testfall-Beginn nicht angegeben).
- Abfragen/XML: 2/2

### T14 – 599457-2026 (2026-08-31) – Deutsches Meeresmuseum
- Objekt(e): OZEANEUM, Hafenstraße 11, 18439 Stralsund (Verfahrensebene); auf Losebene nur „Stiftung Deutsches Meeresmuseum“. 01.01.2027–31.12.2027.
- Leistungsart: Unterhaltsreinigung, Sanitärreinigung, Stundenlohnarbeiten, Materiallieferung.
- Suchschritte:
  - lokal Text~"meeresmuseum"|"ozeaneum"|"stralsund" → 58 (20/38)
  - API `(FT~"Meeresmuseum" OR FT~"Ozeaneum") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260830` → 6
  - XML: 643048-2024, 153003-2023 (Baureinigung, ausgeschlossen), 364629-2019, **569523-2019**, 570728-2024.
- Ergebnis: **teilmenge** (Belegstärke: stark für das Ozeaneum)
- Vorgänger: **569523-2019**, result, vor eForms, 2019-12-02 (REF `2019/S 148-364629` → 364629-2019, competition, 2019-08-02).
  Möglicher jüngerer Vorgänger, nicht entscheidbar: 643048-2024 (competition, eForms, 2024-10-23; frühere Fassung 570728-2024), „Gebäudereinigung“,
  Leistungsort „Katharinenberg 14 - 20“ (Stammhaus bzw. Stiftungsadresse), 01.01.2025–31.12.2025, Umfang „siehe Vergabeunterlagen“.
- Beleg: 364629-2019 „Gebäudereinigung in folgenden Objekten: — Meeresmuseum, Stralsund, — Ozeaneum, Stralsund, — Nautineum, … — Natureum, Prerow …
  — Burmeisterhaus … — Neue Badenstraße 4 … — Sammlungsräume Türmchenspeicher“; Leistungen „Unterhaltsreinigung, Sanitärreinigung, Glasreinigung, …
  Lieferung von Verbrauchsmaterial, Stundenlohnarbeiten“ (Leistungsbild fast wortgleich mit dem Testfall). Gemeinsames Objekt: Ozeaneum. Ob der
  Testfall auch die übrigen Stiftungsobjekte umfasst, ist aus der Bekanntmachung nicht erkennbar → teilmenge.
- Vertragsende Vorgänger: 01.01.2020–31.12.2020, Option 12 Monate. Vorzeitige Neuvergabe: **nein**.
- Abfragen/XML: 2/5

### T15 – 629751-2026 (2026-09-14) – IKK classic
- Objekt(e): Gladbecker Straße 24, 46236 Bottrop (Lose 1 UHR, 2 Glas); Bebelstraße 22, 44623 Herne (Lose 3 UHR, 4 Glas). 01.01.2027–31.12.2027,
  jährliche Verlängerung bis längstens 31.12.2030.
- Leistungsart: Unterhalts- und Glasreinigung.
- Suchschritte:
  - lokal buyer-name~"ikk" → 144 (72/72)
  - API `buyer-name~"IKK" AND (FT~"Bottrop" OR FT~"Herne") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260913` → 2
  - lokal buyer~"ikk" UND Text~(westfalen|bottrop|herne|gladbecker|bebel) → 0 (Kontrolle auf jüngere eForms-Vergabe)
  - XML: 374922-2020, **562187-2020**.
- Ergebnis: **objektgleich** (Belegstärke: stark)
- Vorgänger: **562187-2020**, result, vor eForms, 2020-11-23 (REF `2020/S 153-374922` → 374922-2020, competition, 2020-08-10, „Reinigung Westfalen-Lippe
  (13/AD/2020)“)
- Beleg: Lose 3–6: „Unterhaltsreinigung Gladbecker Straße 24, 46236 Bottrop“, „Glas- und Rahmenreinigung Gladbecker Straße 24, 46236 Bottrop“,
  „Unterhaltsreinigung Bebelstraße 22, 44623 Herne“, „Glas- und Rahmenreinigung Bebelstraße 22, 44623 Herne“; Vertragsschluss 2020-10-21.
- Vertragsende Vorgänger: 01.01.2021–31.12.2021, „verlängert sich um ein weiteres Jahr, längstens jedoch bis zum 31.12.2024“. Vorzeitige Neuvergabe:
  **nein**. Auffällig: Lücke 2025–2026 ohne auffindbare TED-Notice.
- Abfragen/XML: 3/2

---

## Übersicht Teil 1 (T1–T15)

**Fakten (Kategorien nach diesem Protokoll)**

| Kategorie | Anzahl | Fälle |
|---|---|---|
| objektgleich | 9 | T1, T4, T5, T7, T8, T11, T12, T13, T15 |
| teilmenge | 3 | T6, T10, T14 |
| kein_vorgaenger | 2 | T3, T9 |
| unklar | 1 | T2 |

Gefunden im Sinne von V1 (objektgleich + teilmenge): 12 von 15.

| Nr | Testfall | Kategorie | Jüngster Vorgänger | Formular | Datum |
|---|---|---|---|---|---|
| T1 | 644509-2026 | objektgleich | 547893-2021 (REF 387492-2021) | result, vor eForms | 2021-10-27 |
| T2 | 554609-2026 | unklar | – | – | – |
| T3 | 546143-2026 | kein_vorgaenger | – | – | – |
| T4 | 530979-2026 | objektgleich | 202519-2022 | competition, vor eForms | 2022-04-15 |
| T5 | 598474-2026 | objektgleich | 670866-2022 (auch 665652-2022; REF 477850-2022) | result, vor eForms | 2022-12-02 |
| T6 | 461152-2026 | teilmenge | 364258-2023 | competition, vor eForms | 2023-06-19 |
| T7 | 503493-2026 | objektgleich | 155215-2021 (REF 607469-2020) | result, vor eForms | 2021-03-29 |
| T8 | 656958-2026 | objektgleich | 165901-2019 (REF 472607-2018) | result, vor eForms | 2019-04-09 |
| T9 | 610118-2026 | kein_vorgaenger | – | – | – |
| T10 | 514223-2026 | teilmenge | 465718-2022 | competition, vor eForms | 2022-08-26 |
| T11 | 506593-2026 | objektgleich | 574481-2023 (REF 312117-2023) | result, vor eForms | 2023-09-25 |
| T12 | 615831-2026 | objektgleich | 434268-2023 (REF 172338-2023); dazu 652257-2022 (REF 459072-2022) | result, vor eForms | 2023-07-18 |
| T13 | 613923-2026 | objektgleich | 285864-2022 (REF 38357-2022) | result, vor eForms | 2022-05-27 |
| T14 | 599457-2026 | teilmenge | 569523-2019 (REF 364629-2019); evtl. 643048-2024 | result, vor eForms | 2019-12-02 |
| T15 | 629751-2026 | objektgleich | 562187-2020 (REF 374922-2020) | result, vor eForms | 2020-11-23 |

**Budget:** Kein Fall hat das Budget erreicht (höchstens 5 Abfragen und 8 XML je Fall). Kein Abbruch.

**Auffälligkeiten (Fakten mit Quelle)**
- Alle zwölf gefundenen jüngsten Vorgänger stammen aus der Zeit vor eForms (2019–2023). Nur bei T14 gibt es einen möglichen eForms-Vorgänger
  (643048-2024), dessen Umfang nicht entscheidbar ist. In den lokalen API-Rohdaten haben diese Notices keine Titel und keine Orte; gefunden wurden sie
  über Auftraggebernamen und die API-Volltextsuche (`FT`), bestätigt nur über die XML.
- Zentrale Vergabestellen geben die eigene Amtsadresse als Leistungsort an (VB-BW Freiburg: T2 sowie 542576-2026 und 665966-2023, alle „Mozartstraße 58“;
  VB-BW Schwäbisch Gmünd: T9 „Rektor-Klaus-Straße 76“; WISTA: „Kekuléstr. 2-4“). Gleiche Adresse heißt dort nicht gleiches Objekt (T2: andere Flächen).
- Namensvarianten desselben Auftraggebers: „Bundesanstalt für Immobillienaufgaben“ (Tippfehler, 607469-2020, 155215-2021) neben „…Immobilienaufgaben“;
  „Land Baden-Württemberg, vertreten durch den Landesbetrieb Vermögen und Bau …“ (bis 2020) neben „Vermögen und Bau Baden-Württemberg, Amt …“;
  „Gebäudemanagement der Stadt Wuppertal“ (bis 2023) neben „Stadt Wuppertal“; „Landratsamt Weimarer Land“ neben „Kreis Weimarer Land“;
  „Deutsches Meeresmuseum, Museum für Meereskunde und Fischerei“ / „Stiftung Deutsches Meeresmuseum“ / „Deutsches Meeresmuseum“; IKK classic mit
  `buyer-city` Dresden (vor eForms) und Erfurt (eForms); „Staatliches Baumanagement Braunschweig“ neben „Land Niedersachsen vertreten durch …“.
- Rotierende Bündel: Regionalverband Saarbrücken (Schulpakete 2019–2026 mit wechselndem Zuschnitt), WISTA (Lose einzeln neu), Wuppertal (Bezirke).
- Zwei Zuschlagsbekanntmachungen zu einem Verfahren: T5 (665652-2022 und 670866-2022).
- Lücken zwischen Vorgänger-Ende und neuem Beginn: T8 (Vorgänger bis 30.04.2020, neu ab 01.02.2027), T15 (bis 31.12.2024, neu ab 01.01.2027),
  T1 (bis 31.12.2025, neu ab 01.01.2027).
- Bei drei Vorgängern ist auf TED nur die Ausschreibung zu finden, kein Zuschlag: 202519-2022 (T4), 364258-2023 (T6), 465718-2022 (T10).

**Einschätzungen**
- Kein Fall mit Hinweis auf vorzeitige Neuvergabe nach Definition (Bezug Grundlaufzeit). Bei T6 und T11 wird vor Ausschöpfung der letzten
  Verlängerungsoption neu vergeben.
- T10 (teilmenge) sowie T4 und T11 (objektgleich) stützen sich auf Sammelbezeichnungen bzw. Losnummern, nicht auf Einzeladressen; bei strenger
  Auslegung wären sie „unklar“. Ein Zweitprüfer sollte diese Fälle gezielt ansehen.
- Bei T9 sowie T8/T15 ist wahrscheinlich, dass Vorgänger- oder Zwischenverträge außerhalb von TED (bzw. nicht unter CPV 909) vergeben wurden.

**Werkzeug- und Datenprobleme**
- `FT` trifft nur ganze Wörter: „Polizei“ findet nicht „Polizeirevier“ (T9, daher eigene Abfrage mit Komposita). Allgemeine Begriffe wie
  „Bahnhofstraße“ treffen auch die Auftraggeberadresse (T6, nicht trennscharf). Eine `FT`-Abfrage mit „Polizei AND Stade“ lieferte 112 Treffer Rauschen (T8).
- Ein Hilfsskript brach bei T3 einmal an einem leeren Feld ab (Fehler im eigenen Skript, behoben, Abfrage wiederholt; keine Daten betroffen).
- Die Recherche wurde durch ein Nutzungslimit unterbrochen und danach fortgesetzt; bereits gespeicherte Rohdaten wurden nicht überschrieben.
