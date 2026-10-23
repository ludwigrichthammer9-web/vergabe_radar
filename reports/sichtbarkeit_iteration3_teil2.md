# Sichtbarkeit der Vorgänger – Handsuche Iteration 3, Teil 2 (T16–T30)

Rechercheur (Subagent), Recherche am 2026-10-23. Testfälle: Zeilen 16–30 aus `reports/testfaelle_iteration3.txt`.
Definitionen: `docs/iterationen.md`, Iteration 3, „Begriffe“. Unabhängigkeit: Regel-, Merkmals- und Ergebnisdateien
(`src/zuordnung_*.py`, `src/objekt_merkmale.py`, `data/processed/`, `reports/zuordnung_*`, `k2_*`, `blindpruefung_*`) wurden nicht gelesen.
Aus Teil 1 wurde nur der Abschnitt „Vorgehen und Konventionen“ übernommen (dazu der Hinweis auf Amtsadressen zentraler Vergabestellen).

## Vorgehen und Konventionen (wie Teil 1)

**Quellen**
- *Lokal* (zählt als Abfrage): unveränderte API-Rohdaten `data/raw/ted_search/DEU_result_cpv909_20161001_20260930/` und
  `data/raw/ted_search/DEU_competition_cpv909_20161001_20260930/` (zusammen 35.150 Notices). Gefiltert immer auf 20161001 ≤ Veröffentlichung < Testfalldatum.
  „buyer~x“ = Teilstring im Auftraggebernamen; „Text~x“ = Teilstring in Auftraggebername, -ort, -PLZ, Titel (Verfahren/Los) und
  Leistungsort (Ort, PLZ, Straße); „Text~(a|b)“ = regulärer Ausdruck über dieselben Felder. Vor eForms sind dort nur Auftraggebername und -ort gefüllt.
- *Live-API* (`POST https://api.ted.europa.eu/v3/notices/search`): vor allem das Volltextfeld `FT`. **Kontrollabfrage je Testfall:** In jedem Fall
  wurde eine `FT`-Abfrage ohne Datumsfilter gestellt, die den Testfall selbst finden muss. Das hat in allen 15 Fällen funktioniert. Die API-Abfragen
  sind nicht nach `form-type` getrennt (result und competition gemeinsam; Berichtigungen `corr` werden ignoriert).
- *XML*: `https://ted.europa.eu/en/notice/<nr>/xml`.
- Alle API-Antworten (mit Request als `*.request.json`) und alle XML liegen unverändert unter `data/raw/rechercheur_20261023/<Testfall-Nummer>/`.
  Lokale Abfragen wurden nicht gespeichert; sie lassen sich mit den angegebenen Suchbegriffen aus den vorhandenen Rohdaten wiederholen.

**Zählung:** „Abfragen/XML“ = lokale + API-Abfragen / geöffnete Kandidaten-XML. Die XML des Testfalls selbst ist nicht mitgezählt.

**Kategorien-Konvention (Auslegung der Definition, auf Verfahrensebene, aus Teil 1):**
- *objektgleich*: Liegenschaft(en) per Name oder Adresse identisch, Leistungsart überlappt. Kleine Abweichungen im Objektbestand
  (ein Objekt mehr oder weniger) oder eine neue Losaufteilung desselben Bestands bleiben objektgleich.
- *teilmenge*: nur ein Teil der Objekte gemeinsam (z. B. Testfall deutlich erweitert oder Vorgänger war ein größeres Bündel).
- **Belegstärke** (Einschätzung, keine Kategorie der Definition): stark = Adresse/Liegenschaftsname wörtlich gleich; mittel = Sammelbezeichnung +
  Kennzahlen/Losnummer; schwach = nur indirekt.
- **Amtsadressen:** Zentrale Vergabestellen tragen oft die eigene Dienstadresse als Leistungsort ein (hier T26: „L 4, 4-6, Mannheim“; T30: Amtsadresse
  Breite Gasse 28 des Gesundheitsamts). Eine solche Adresse gilt nicht als Objektbeleg.
- **Ergänzende Auslegung in Teil 2:** Nennen weder der Testfall noch die Kandidaten ein Objekt (nur „diverse Objekte“, „3 Objekte im Bezirk 3“),
  lässt sich die Definition (Adresse oder Liegenschaftsname) nicht prüfen. Gibt es trotzdem konkrete Hinweise (gleicher Auftraggeber, gleiche
  Sammelbezeichnung, Anschlusstermin), lautet die Kategorie *unklar* (T27, T28). Stimmen dagegen Kennzahlen eng überein und ist der Objektbestand
  des Vorgängers benannt, gilt *objektgleich* mit Belegstärke *mittel* (T21, T30).

---

### T16 – 559458-2026 (2026-08-12) – Hansestadt Anklam
- Objekt(e): Nikolaikirche Anklam, „Nikolaikirchstr. 7, 17389 Anklam“ (Umbau zum Lilienthal Flight Museum, Bauabschnitt 3 des Projekts IKAREUM).
- Leistungsart: **Bauzwischen- und Bauendreinigung**, keine Unterhalts-, Grund- oder Glasreinigung. Zitat Los: „Diese umfassen die Bauzwischenreinigung
  als Grobreinigung, sowie die Bauendreinigung bestehend aus Grob- und Feinreinigung der neuen Bauteile“. CPV 90910000, 90911200, 45212300.
- Suchschritte:
  1. lokal buyer~„Anklam“: 6 (3 result, 3 competition), alle „Schulcampus Innenstadt Anklam“, Baustraße (477312-2024, 678865-2024, 739814-2025, 63986-2026, 194593-2026, 540558-2026)
  2. lokal Text~„Anklam“: 18 (zusätzlich Landkreis Vorpommern-Greifswald, SBL Greifswald, AMEOS, BA; keine Nikolaikirche)
  3. lokal Text~„17389“: 13 (Teilmenge von 2)
  4. API `FT=IKAREUM AND classification-cpv=909*` (Kontrolle): 1 = Testfall
  5. API `FT=Nikolaikirche AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260812`: 0
  6. API `FT=Anklam AND …` (gleicher Zeitraum): 52, Liste durchgesehen, keine Kirche/kein Museum
  7. API `(FT=Nikolaikirchstraße OR FT=Lilienthal OR FT=Ikareum) AND …`: 27, alle aus anderen Orten (Lilienthal/LK Osterholz, Bundeswehr u. a.)
  - geöffnete XML: keine
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: –. Einschätzung: Einmalige Baureinigung, ein Vorgänger ist sachlich nicht zu erwarten. Der Fall gehört inhaltlich nicht zur Population
  (die Stichwortliste greift nicht, weil der Titel „Umbau und Sanierung …“ lautet).
- Vertragsende Vorgänger: entfällt; Hinweis auf vorzeitige Neuvergabe: entfällt
- Abfragen/XML: 7/0

### T17 – 540820-2026 (2026-08-05) – Gemeinde Südharz
- Objekt(e): „Gebäudeunterhalts- und Glasreinigung für die Gemeinde Südharz überwiegend Kitas und Schule sowie die Thyragrotte (Schwimmbad)“.
  9 Lose nach Ortsteilen: Los 1 Roßla, Los 2 Rottleberode und Uftrungen, Los 3 Rottleberode, Hayn und Schwenda, Los 4 Stolberg, Los 5 Thyragrotte
  (Stolberg), Lose 6–9 Glasreinigung (Roßla/Wickerode/Kleinleinungen; Rottleberode/Uftrungen; Hayn/Schwenda; Stolberg mit Thyragrotte).
  Keine Straßenadressen; Amtsadresse Hüttenhof 1, 06536 Südharz.
- Leistungsart: Unterhaltsreinigung (Lose 1–5), Glasreinigung (Lose 6–9); Beginn 01.01.2027, 36 Monate + 2 × 1 Jahr.
- Suchschritte:
  1. lokal buyer~„Südharz“: 2 (Landkreis Mansfeld-Südharz 333038-2021; VGS Verkehrsgesellschaft Südharz 77068-2026, Busreinigung)
  2. lokal Text~„Südharz“: 2 (dieselben)
  3. lokal Text~„06536“: 0
  4. API `FT=Thyragrotte AND classification-cpv=909*` (Kontrolle): 2 = Testfall + späterer Zuschlag 707205-2026 (2026-10-13)
  5. API `FT=Südharz AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260805`: 84, kein Verfahren der Gemeinde Südharz
  6. API `(FT=Rottleberode OR FT=Roßla OR FT=Rossla OR FT=Uftrungen OR FT=Schwenda OR FT=Thyragrotte) AND …`: 0
  7. lokal Text~„Stolberg“: 17, alle Stolberg (Rhld.) bzw. Köln/Aachen
  - geöffnete XML: keine
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: –. Fakt: Vor dem Testfall gibt es auf TED keine Notice der Gemeinde Südharz mit CPV 909 und keine, die einen ihrer Ortsteile nennt.
- Vertragsende Vorgänger: entfällt; Hinweis auf vorzeitige Neuvergabe: entfällt
- Abfragen/XML: 7/0

### T18 – 658725-2026 (2026-09-24) – Regierung von Schwaben
- Objekt(e) (9 Lose, Adressen aus dem XML): Los 1 Behördenzentrum Aindlinger Str. 16, 86167 Augsburg; Los 2 ANKER-Dependance Kobelweg 82a, 86156 Augsburg;
  Los 3 Gemeinschaftsunterkunft Hohenstaufenstr. 57, 86199 Augsburg-Inningen; Los 4 ANKER-Dependance Steinerne Furt 75/77, 86167 Augsburg;
  Los 5 ANKER-Dependance Gubener Str. 4+6, 86156 Augsburg; Los 6 Hörmannsberger Str. 18, 86415 Mering; Los 7 Im Starkfeld 61, 89231 Neu-Ulm;
  Los 8 Kaufbeurer Str. 82, 87437 Kempten; Los 9 Maria-Merian-Str. 4, 89312 Günzburg.
- Leistungsart: „Reinigungsleistungen“ (CPV 90910000); laut Eignungskriterien Unterhaltsreinigung („Die Referenzen umfassen Unterhaltsreinigungen in einer
  Erstaufnahmeeinrichtung …“). Laufzeit je Los 01.02.2027–31.01.2028, Verlängerung bis spätestens 31.01.2031.
- Suchschritte:
  1. lokal buyer~„Regierung von Schwaben“: 38 (17 result, 21 competition; 2019–2023 ohne Titel)
  2. lokal Text~„ANKER“: 44 (darunter 506236-2024/687529-2024 Kempten; 254854-2026/334987-2026/488398-2026 Kempten + Günzburg)
  3. API `FT=Starkfeld AND classification-cpv=909*` (Kontrolle): 6, darunter Testfall und 694585-2026 (nach dem Testfall)
  4. API `(FT=Aindlinger OR FT=Kobelweg OR FT=Hohenstaufenstr OR FT=Hohenstaufenstraße OR FT=Gubener OR FT=Starkfeld OR FT=Hörmannsberger OR FT="Steinerne Furt") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260924`: 59
  5. lokal Text~(Aindlinger|Kobelweg|Hohenstaufen|Gubener|Starkfeld|Hörmannsberger|Steinerne Furt|Unterkunfts): 35 (Regierung von Oberbayern: 710461-2023, 755423-2023, 5266-2024, 95722-2024, 227031-2024)
  6. API `FT=Gubener AND …` (gleicher Zeitraum): 9, keiner in Augsburg
  - geöffnete XML: 488398-2026, 755423-2023, 710461-2023, 227031-2024, 571224-2023, 557041-2023, 524787-2023, 581814-2022
- Ergebnis: **teilmenge** (Neuzuschnitt aus mehreren Einzelvergaben; 8 von 9 Objekten haben einen Vorgänger, Los 5 Gubener Str. 4+6 keinen)
- Vorgänger (jüngster): **488398-2026**, result, eForms, 2026-07-15 (deckt Lose 8 und 9). Je Los der jüngste gefundene:
  - Los 1 Aindlinger Str. 16: 557041-2023, result, vor eForms, 2023-09-15 (REF_NOTICE 428420-2023)
  - Los 2 Kobelweg 82a: 755423-2023, result, eForms, 2023-12-13 (API-Auftraggeber: Regierung von Oberbayern)
  - Los 3 Hohenstaufenstr. 57: 710461-2023, result, eForms, 2023-11-22 (Regierung von Oberbayern)
  - Los 4 Steinerne Furt 75/77: 524787-2023, result, vor eForms, 2023-08-31 (REF_NOTICE 376239-2023); älter 581814-2022 (REF 421186-2022)
  - Los 6 Hörmannsberger Str. 18, Mering: 571224-2023, result, vor eForms, 2023-09-22 (REF_NOTICE 442141-2023)
  - Los 7 Im Starkfeld 61, Neu-Ulm: 227031-2024, result, eForms, 2024-04-17 (Regierung von Oberbayern, Zentrale Vergabestelle)
  - Los 8/9 Kempten, Günzburg: 488398-2026
- Beleg (Adressen wörtlich, Leistungsart Unterhaltsreinigung): 488398-2026 „Los 1: ANKER-Dependance Kaufbeurer Str. 82, 87437 Kempten“, „Los 2: ANKER-Dependance
  Maria-Merian-Str. 4, 89312 Günzburg“; 557041-2023 „Unterhaltsreinigung des Behördenzentrums ANKER-Schwaben (einschließlich des Zentrallagers) in der
  Aindlinger Str. 16 in 86167 Augsburg“; 755423-2023 „Unterhaltsreinigungsleistung Unterkunfts-Dependance Kobelweg 82a, Augsburg“; 710461-2023
  „Unterhaltsreinigungsleistung Unterkunfts-Dep. Hohenstaufenstr. 57, Augsburg-Inningen“; 524787-2023 „Unterhaltsreinigungsleistung Unterkunfts-Dependance
  Steinerne Furt 75/77, Augsburg“; 571224-2023 „Unterhaltsreinigungsleistung Unterkunfts-Dependance Hörmannsberger Str. 18, Mering“; 227031-2024 „Unterhaltsreinigung
  der Einrichtung Neu-Ulm, Im Starkfeld 61“. **Belegstärke: stark.**
- Vertragsende Vorgänger: 488398-2026 je Los StartDate 2026-08-01, EndDate 2028-01-31. Lose 2/3: 2024-02-01 bis 2025-01-31; Los 7: 2024-07-01 bis 2025-06-30
  (Nachfolgeverträge 2025/26 dazu nicht auf TED gefunden).
  Hinweis auf vorzeitige Neuvergabe: **ja** für Lose 8/9 (Testfall-Beginn 2027-02-01 liegt 12 Monate vor dem EndDate 2028-01-31 des Vorgängers; Grund nicht erkennbar).
- Nicht geprüft: 144303-2025 (Regierung von Schwaben, „Unterhaltsreinigung bei der Regierung von Schwaben“, Lostitel nennt „Kobelweg 82“ ohne „a“; Einschätzung: Dienstgebäude, nicht die Dependance).
- Abfragen/XML: 6/8

### T19 – 474898-2026 (2026-07-09) – Land Rheinland-Pfalz, Ministerium der Justiz, vertreten durch das Amts- und Landgericht Koblenz
- Objekt(e): „Hauptjustizgebäude Koblenz“ (Leistungsort nur „Koblenz“, keine Straße); Vergabestelle LBB NL Kaiserslautern.
- Leistungsart: Unterhalts- und Glasreinigung; 01.01.2027–31.12.2029.
- Suchschritte:
  1. lokal buyer~„Landgericht Koblenz“: 2 (286526-2023, 636701-2023)
  2. lokal buyer~„Justiz“: 86 (RLP-Justiz u. a. Neues Justizzentrum Koblenz 479792-2024, Kastorhof 313813-2025 – andere Objekte)
  3. API `FT=Hauptjustizgebäude AND classification-cpv=909*` (Kontrolle): 3 = 286526-2023, 636701-2023, Testfall
  4. API `(FT=Hauptjustizgebäude OR FT=Karmeliterstraße OR FT=Justizgebäude) AND FT=Koblenz AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260709`: 4 (zusätzlich Kastorhof 313813-2025/50037-2026)
  - geöffnete XML: 636701-2023, 286526-2023
- Ergebnis: **objektgleich**
- Vorgänger: **636701-2023**, result, vor eForms, 2023-10-20 (Ausschreibung 286526-2023, competition, vor eForms, 2023-05-15)
- Beleg: 636701-2023 Titel „890223002 / 23E0177 Unterhalts- und Glasreinigungsleistungen im Hauptjustizgebäude Koblenz“, MAIN_SITE „56068 Koblenz“,
  Zuschlag an Gies Dienstleistungen GmbH (Vertrag 2023-08-28). Liegenschaftsname und Leistungsart identisch. **Belegstärke: stark.**
- Vertragsende Vorgänger: 286526-2023 DATE_START 2024-01-01, DATE_END 2026-12-31, RENEWAL „unbefristet max. 5 Jahre“. Testfall beginnt 2027-01-01 (nahtlos).
  Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 4/2

### T20 – 601496-2026 (2026-09-01) – Stadt Sindelfingen, Zentrale Vergabestelle
- Objekt(e): Badezentrum Sindelfingen, „Hohenzollernstraße 23, 71067 Sindelfingen“.
- Leistungsart: Unterhalts- und Grundreinigung der Bäder; 01.01.–31.12.2027 mit Verlängerungsoption.
- Suchschritte:
  1. lokal buyer~„Sindelfingen“: 10 (2018 und 2022 ohne Titel; 2024 Glasreinigung; 2025/26 Gemeinschaftsunterkünfte; 469202-2026 „73 städtische Objekte 2027“)
  2. lokal Text~„Sindelfingen“: 16 (zusätzlich BImA, BA)
  3. API `FT=Badezentrum AND FT=Sindelfingen AND classification-cpv=909*` (Kontrolle): 1 = Testfall
  4. API `(FT=Badezentrum OR FT=Hohenzollernstraße OR FT=Hallenbad OR FT=Bäder) AND FT=Sindelfingen AND … <20260901`: 0
  5. API `(FT=Badezentrums OR FT=Schwimmbad OR FT=Freibad OR FT=Hallenbäder OR FT=Schwimmhalle OR FT=Badbetriebe OR FT=Bad) AND FT=Sindelfingen AND …`: 6 (TK, BA – keine Bäder)
  - geöffnete XML: 674421-2022, 522340-2018
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Fakten: 674421-2022 „Unterhalts- und Grundreinigung von 54 städtischen Objekten“ (4 Bezirkslose, MAIN_SITE „in den Vergabeunterlagen aufgeführt“) und
  522340-2018 „Unterhalts- und Grundreinigung von 38 städtischen Objekten“ nennen keine Objekte; die Zeichenfolgen „Bad“/„Bäder“ kommen in beiden XML nicht vor.
  Einschätzung: Restunsicherheit, ob das Badezentrum in diesen Bündeln steckte; ein konkreter Hinweis darauf fehlt.
- Vertragsende Vorgänger: entfällt; Hinweis auf vorzeitige Neuvergabe: entfällt
- Abfragen/XML: 5/2

### T21 – 478291-2026 (2026-07-10) – Freistaat Bayern, vertreten durch das Bayerische Landesamt für Steuern (Zentrale Vergabestelle)
- Objekt(e): „Finanzamt Mittelfranken-Ost am Standort Erlangen“, Leistungsort „Erlangen, 91052“ (keine Straße); „Grundfläche: ca. 6.900,06 qm, Jahresreinigungsfläche ca. 980.342,50 qm“.
- Leistungsart: Unterhaltsreinigung; 01.01.2027–31.12.2029, Verlängerung bis spätestens 31.12.2032.
- Suchschritte:
  1. lokal buyer~„Landesamt für Steuern“: 578 (zentrale Vergabestelle; eForms-Titel nach Amt, Erlangen nur 656845-2024/45054-2025)
  2. lokal Text~„Erlangen“: 110
  3. API `FT="Mittelfranken-Ost" AND FT=Erlangen AND classification-cpv=909*` (Kontrolle): 2 = Testfall + späterer Zuschlag 671266-2026
  4. API `FT=Finanzamt AND FT=Erlangen AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20260710`: 10 (BayLfSt: 130483-2018, 309063-2018, 656845-2024, 45054-2025)
  5. API `FT=Erlangen AND FT=Steuern AND …`: 296 (zu unscharf, „Steuern“ steht in vielen Notices; ausgewertet nur die BayLfSt-Treffer, darunter 142984-2022 und 301495-2022)
  - geöffnete XML: 45054-2025, 656845-2024 (nur Flächenangabe), 309063-2018, 130483-2018, 301495-2022, 142984-2022
- Ergebnis: **objektgleich**
- Vorgänger: **301495-2022**, result, vor eForms, 2022-06-03 (Ausschreibung 142984-2022, competition, vor eForms, 2022-03-18). Davor 309063-2018 (result, 2018-07-17).
- Beleg: 301495-2022 Los 1 „Unterhaltsreinigung FA Erlangen“, INFO_ADD „Grundfläche: ca. 6.862,69 qm“ (Testfall 6.900,06 qm, +0,5 %); gleicher Auftraggeber.
  Namenswechsel „FA Erlangen“ → „FA Mittelfranken-Ost, Standort Erlangen“. Leistungsart Unterhaltsreinigung überlappt (Vorgänger zusätzlich Glas in Los 2).
  **Belegstärke: mittel** (Name nicht wörtlich gleich, Fläche fast gleich).
- Abgrenzung: 45054-2025 (result, eForms, 2025-01-22) „Unterhalts- sowie Glas- und Rahmenreinigung für das ADBV Erlangen und FA Erlangen“ nennt zwar das FA Erlangen,
  hat aber nur „Grundfläche: ca. 2.412,87 qm“ (Laufzeit 2025-04-01 bis 2031-03-31). Einschätzung: andere Fläche bzw. anderes Gebäude, daher nicht als objektgleich gewertet.
- Vertragsende Vorgänger: 142984-2022 „Der Vertrag tritt am 01.09.2022 in Kraft und gilt zunächst bis zum 31.08.2025. … endet spätestens mit Ablauf des 31.08.2028.“
  Hinweis auf vorzeitige Neuvergabe: nein (Grundlaufzeit endete 31.08.2025). Der Beginn 01.01.2027 liegt mitten im Verlängerungsjahr bis 31.08.2027 (Grund unklar).
  Fakt am Rande: Der Vorgänger von 2018 (130483-2018: 2018-09-01 bis 2021-08-31, spätestens 31.08.2024) wurde bereits zum 01.09.2022 abgelöst.
- Abfragen/XML: 5/6

### T22 – 574953-2026 (2026-08-19) – Berufsgenossenschaft für Gesundheitsdienst und Wohlfahrtspflege (BGW)
- Objekt(e): BGW Bezirksverwaltung Berlin, „Spichernstraße 2-3“ (angemietete Flächen EG–3. OG), 10777 Berlin; Nettogrundfläche ca. 4.459,84 m².
- Leistungsart: Unterhalts-, Grund- und einseitige Glasreinigung; 01.02.2027–31.01.2029.
- Suchschritte:
  1. lokal buyer~„Berufsgenossenschaft für Gesundheitsdienst“: 6 (nur 2025/26, andere Standorte)
  2. lokal buyer~„BGW“: 37 (u. a. „BGW Bezirksverwaltung Berlin“ 482658-2018, 509902-2022)
  3. API `FT=Spichernstraße AND classification-cpv=909*` (Kontrolle): 6 (inkl. Testfall)
  4. API `(FT=Spichernstraße OR FT=Spichernstr) AND … <20260819`: 5 (482658-2018, 509902-2022; außerdem DRV 410580-2018, BVG-Berichtigung)
  - geöffnete XML: 509902-2022
- Ergebnis: **objektgleich**
- Vorgänger: **509902-2022**, competition, vor eForms, 2022-09-19 (kein Zuschlag auf TED; ältere Ausschreibung 482658-2018 nicht geöffnet)
- Beleg: 509902-2022 MAIN_SITE „Spichernstraße 2, 10777 Berlin“; Beschreibung wortgleich: „Die BGW ist Mieterin in der Spichernstraße 2-3. … Nettogrundfläche von
  ca. 4.459,84 m²“; Leistungsart identisch. **Belegstärke: stark.**
- Vertragsende Vorgänger: DATE_START 2023-02-01, DATE_END 2025-01-31, „Option, den Vertrag zweimal für jeweils 1 Jahr zu verlängern“ → spätestens 31.01.2027.
  Testfall beginnt 01.02.2027 (nahtlos nach maximaler Verlängerung). Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 4/1

### T23 – 589942-2026 (2026-08-26) – Stadt Dessau-Roßlau, Zentrale Vergabestelle
- Objekt(e): Anhaltisches Berufsschulzentrum „Hugo Junkers“, Junkersstraße 30 (einschl. Sporthalle), Außenstelle Mosigkau (Am Reitplatz 1),
  Wohnheim für Auszubildende (Randelstraße 6-10), alle Dessau-Roßlau; 24.373,4 m².
- Leistungsart: Unterhaltsreinigung/Grundreinigung, Grundreinigung optional; 01.01.–31.12.2027, Verlängerung bis spätestens 31.12.2030.
- Suchschritte:
  1. lokal buyer~„Dessau“: 92 (2020–2023 ohne Titel)
  2. API `FT=Berufsschulzentrum AND FT=Dessau-Roßlau AND classification-cpv=909*` (Kontrolle): 3 = 408656-2018, Testfall, späterer Zuschlag 668565-2026
  3. API `(FT=Berufsschulzentrum OR FT=Junkersstraße OR FT=Randelstraße OR FT="Am Reitplatz" OR FT=Mosigkau) AND (FT=Dessau OR FT=Dessau-Roßlau) AND … <20260826`: 1 (408656-2018)
  4. API `(FT=Berufsschule OR FT=Berufsschulen OR FT="Hugo Junkers" OR FT=Wohnheim OR FT=Auszubildende OR FT=ABSZ) AND …`: 7
  5. API `(FT=BSZ OR FT=Gärtnerei OR FT=Berufsbildende) AND …`: 2 (23048-2018, 408656-2018)
  - geöffnete XML: 408656-2018, 23048-2018, 626494-2022, 36085-2023
- Ergebnis: **objektgleich**
- Vorgänger: **408656-2018**, result, vor eForms, 2018-09-19 (Ausschreibung 23048-2018, competition, 2018-01-18)
- Beleg: 408656-2018 Titel „Unterhalts- und Glasreinigung im Anhaltischen Berufsschulzentrum „Hugo Junkers“ einschl. der Sporthalle und Außenstelle Gärtnerei sowie
  im Wohnheim für Auszubildende“, „ca. 25 000 m² Fußbodenfläche … an 3 Standorten in Dessau-Roßlau“ (Testfall 24.373,4 m²). Leistungsart Unterhaltsreinigung überlappt.
  **Belegstärke: stark.**
- Abgrenzung: 626494-2022 und 36085-2023 betreffen die Grundschule „Hugo Junkers“ (anderes Objekt).
- Vertragsende Vorgänger: 23048-2018 DATE_START 2019-01-01, DATE_END 2019-12-31, „Option der Verlängerung um jeweils 1 Jahr …, insgesamt für 3 Jahre“ → spätestens 31.12.2022.
  Für 2023–2026 kein Verfahren auf TED gefunden (Lücke). Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 5/4

### T24 – 673994-2026 (2026-09-30) – Land Niedersachsen, vertreten durch das Staatliche Baumanagement Niedersachsen (Vergabestelle SB Südniedersachsen)
- Objekt(e): Amtsgericht Goslar Haus I „Hoher Weg 9“ und Haus II „Kaiserbleek 8“, 38640 Goslar; Amtsgericht Seesen „Wilhelmsplatz 1“, 38723 Seesen;
  Finanzamt Goslar-Bad Gandersheim, Standort Goslar „Wachtelpforte 40“, 38644 Goslar, und Standort Bad Gandersheim „Alte Gasse 24“, 37581 Bad Gandersheim.
- Leistungsart: Unterhaltsreinigung (Lose 1–4: 3.550/1.490/4.510/3.000 m²) und Glasreinigung (Lose 5–8); 01.03.2027–29.02.2028.
- Suchschritte:
  1. lokal Text~(Goslar|Seesen|Gandersheim): 27 (keine Treffer des SB Südniedersachsen vor eForms, da Ort dort Clausthal-Zellerfeld)
  2. API `FT=Wachtelpforte AND classification-cpv=909*` (Kontrolle): 3 = 488738-2019, 85643-2020, Testfall
  3. API `(FT=Wachtelpforte OR FT=Kaiserbleek OR FT="Hoher Weg" OR FT=Wilhelmsplatz OR FT="Alte Gasse") AND (FT=Goslar OR FT=Seesen OR FT=Gandersheim) AND … <20260930`: 4
  - geöffnete XML: 85643-2020, 488738-2019, 449918-2021
- Ergebnis: **objektgleich**
- Vorgänger: **85643-2020**, result, vor eForms, 2020-02-20 (Ausschreibung 488738-2019, Vergabenummer 19 E 70293)
- Beleg: 85643-2020 MAIN_SITE „Amtsgericht Goslar – Haus I Hoher Weg 9, 38640 Goslar Amtsgericht Goslar – Haus II Kaiserbleek 8“, „Amtsgericht Seesen Wilhelmsplatz 1
  38723 Seesen“, „Finanzamt Goslar Wachtelpforte 40, 38644 Goslar Finanzamt Bad Gandersheim Alte Gasse 24, 37581 Bad Gandersheim“; Unterhalts- und Fensterreinigung.
  Flächen 2020: AG Goslar 3.300, AG Seesen 1.400, beide Finanzämter 7.400 m² (2026: 3.550, 1.490, 7.510). Neue Losaufteilung (6 → 8 Lose) desselben Bestands.
  **Belegstärke: stark.**
- Abgrenzung: 449918-2021 (Polizeiinspektion Goslar und Ambulanter Justizsozialdienst, Hoher Weg 8) ist ein anderes Objekt.
- Vertragsende Vorgänger: 488738-2019 DATE_START 2020-03-01, DATE_END 2021-02-28, NO_RENEWAL. Einschätzung: Der Testfall beginnt genau 7 Jahre nach dem
  Vorgängerbeginn; tatsächliches Vertragsende damit unbekannt (Verlängerungen nicht auf TED). Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 3/3

### T25 – 616444-2026 (2026-09-08) – Bezirksregierung Detmold
- Objekt(e): Erstaufnahmeeinrichtung (EAE) Bielefeld Südring, „Gütersloher Straße 259, 33649 Bielefeld“.
- Leistungsart: laufende Unterhaltsreinigung, Grundreinigung, Reinigung der Bewohnerzimmer nach Auszug; 01.01.2027–31.07.2028.
- Suchschritte:
  1. lokal buyer~„Bezirksregierung Detmold“: 2 (ZUE Lage 74633-2025, 121744-2025)
  2. API `FT=Südring AND FT=Bielefeld AND classification-cpv=909*` (Kontrolle): 2 = 88195-2020, Testfall
  3. API `(FT=Südring OR FT="Gütersloher Straße" OR FT=Erstaufnahmeeinrichtung OR FT=EAE) AND FT=Bielefeld AND … <20260908`: 1 (88195-2020)
  4. lokal Text~„Bielefeld“: 127 (keine EAE)
  5. API `(FT=Landeseinrichtung OR FT=Flüchtlingsunterkunft OR FT=Flüchtlinge OR FT=Asylbewerber OR FT=Unterbringungseinrichtung OR FT=Erstaufnahme OR FT=Catterick) AND FT=Bielefeld AND …`: 11
  6. lokal buyer~„Bezirksregierung“: 36 (nur ZUE anderer Bezirke)
  - geöffnete XML: 88195-2020, 250172-2021, 252711-2021, 317384-2021, 31700-2022
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Fakten: 88195-2020 (BImA) betrifft „Südring 60-63, 18059 Rostock“ (Wohnliegenschaften Rostock). 250172-2021, 252711-2021, 317384-2021, 31700-2022 (BLB NRW Bielefeld)
  betreffen das „Aus- und Fortbildungszentrum der Bundespolizei Bielefeld, in der ehem. Catterick Barracks“, Detmolder Str. 440. Keine Notice zur Gütersloher Straße 259.
- Vertragsende Vorgänger: entfällt; Hinweis auf vorzeitige Neuvergabe: entfällt
- Abfragen/XML: 6/5

### T26 – 555139-2026 (2026-08-11) – Vermögen und Bau Baden-Württemberg, Amt Mannheim und Heidelberg
- Objekt(e): „HD, Maaßstr. 32: Finanzamt Heidelberg“ (aus dem Titel). Leistungsort im XML ist die **Amtsadresse** „L 4, 4-6, Mannheim, 68161“ (kein Objektbeleg).
  „Bodenflächen von ca. 11.731 qm und einer monatlichen Reinigungsfläche von ca. 64.700 qm“.
- Leistungsart: Unterhalts- und Grundreinigung; 01.12.2026–30.11.2031.
- Hinweis im Testfall: „Erneute Ausschreibung des Objektes HD, Maaßstr. 32 aufgrund Verfahrensaufhebung der VergabeNr. 26-59191.“
- Suchschritte:
  1. lokal Text~„Maaß“: 1 (462151-2026)
  2. lokal buyer~„Mannheim und Heidelberg“: 42 (einschließlich der früheren Bezeichnung „Land Baden-Württemberg, vertreten durch den Landesbetrieb …“)
  3. API `(FT=Maaßstr OR FT=Maaßstraße) AND classification-cpv=909*` (Kontrolle, ohne Datumsfilter): 6 = 557850-2020, 95743-2021, 462151-2026, 554730-2026 (2026-08-11,
     gleicher Tag wie der Testfall, also nicht „vor“ ihm), Testfall, 568569-2026 (danach)
  - geöffnete XML: 462151-2026, 95743-2021, 557850-2020
- Ergebnis: **objektgleich**
- Vorgänger: formal jüngster: **462151-2026**, competition, eForms, 2026-07-06 (das aufgehobene Verfahren; ProcurementProject-ID „26-59191“, gleicher Titel, gleiche Flächen,
  geplante Laufzeit 2026-11-01 bis 2031-10-31). Jüngster mit Vertrag: **95743-2021**, result, vor eForms, 2021-02-24 (Ausschreibung 557850-2020).
- Beleg: 95743-2021 Titel „HD, Maaßstr. 28/1 + 32_Finanzamt HD und HD, Adlerstr. 1/4_Polizeiposten: Unterhalts- und Grundreinigung“, „Finanzamt Heidelberg (HD, Maaßstr. 28/1 + 32)
  mit einer Bodenflächen von rund 12 350 qm“ (zusätzlich Polizeiposten mit rund 120 qm). Adresse und Leistungsart gleich; das zusätzliche kleine Objekt ist nach Konvention
  unerheblich. **Belegstärke: stark.**
- Vertragsende Vorgänger: 557850-2020 DATE_START 2021-04-01, DATE_END 2026-03-31. Einschätzung: April bis November 2026 vermutlich Interimslösung (nicht auf TED).
  Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 3/3

### T27 – 623928-2026 (2026-09-10) – Stadt Springe (durchgeführt von der Kommunal Agentur NRW GmbH)
- Objekt(e): „Unterhalts-und Grundreinigung in verschiedenen Objekten mit ca. 63.400 m² Reinigungsfläche in 3 Losen“; Lose „in diversen Objekten“ mit 31.200, 28.300 und
  3.900 m² (im XML als „Glasfläche“ bezeichnet; Einschätzung: Schreibfehler, die Summe ist die Reinigungsfläche). Ort „Springe, 31832“. **Keine Objektnamen.**
- Leistungsart: Unterhalts- und Grundreinigung; 01.04.2027–31.03.2030.
- Suchschritte:
  1. lokal Text~„Springe“: 24 (Stadt Springe: 66608-2018, 293080-2018, 390156-2023, 513559-2024 Glasreinigung; sonst Bad Lippspringe, BA, SBM)
  2. API `FT=Springe AND classification-cpv=909*` (Kontrolle): 34 (inkl. Testfall)
  - geöffnete XML: 390156-2023, 293080-2018, 66608-2018
- Ergebnis: **unklar**
- Vorgänger (Kandidat): 390156-2023, competition, vor eForms, 2023-06-30 (kein Zuschlag auf TED)
- Beleg: 390156-2023 „Unterhalts- und Grundreinigung in diversen Objekten“, MAIN_SITE „Stadt Springe und Ortsteile“, 5 Lose mit 19.200/14.200/5.000/6.500/7.600 m²
  (= 52.500 m²) plus 2 Glaslose, beschaffende Stelle ebenfalls Kommunal Agentur NRW; DATE_START 2024-02-01, DATE_END 2027-03-31, Verlängerung „zweimalig um je 12 Monate“.
  2018 (66608-2018/293080-2018): „Unterhalts- und Grundreinigung von Schulen, Turnhallen, Kitas und öffentlichen Gebäuden“, 1 Los.
  Begründung: Weder der Testfall noch die Kandidaten nennen ein Objekt, die Definition (Adresse oder Liegenschaftsname) ist nicht prüfbar. Hinweise dafür: gleicher
  Auftraggeber, gleiche Leistungsart und Sammelbezeichnung, Vertragsende 31.03.2027 und Testfall-Beginn 01.04.2027. Dagegen: Fläche +21 %, 5 → 3 Lose.
  Einschätzung: sehr wahrscheinlich Nachfolgevergabe (mindestens Teilmenge), aber nicht belegbar.
- Vertragsende Vorgänger (Kandidat): 31.03.2027 (Grundlaufzeit; Verlängerung bis höchstens 31.03.2029 möglich). Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 2/3

### T28 – 455814-2026 (2026-07-02) – Landeshauptstadt Düsseldorf, Amt für Recht, Vergabe und Versicherungen, Zentrale Vergabestelle
- Objekt(e): „Unterhaltsreinigung von 3 Objekte im Stadtgebiet im Bezirk 3 ab 01.12.2026“; Ort „Düsseldorf, 40200“. **Keine Objektnamen oder Adressen.**
- Leistungsart: Unterhaltsreinigung; 01.12.2026–30.11.2029.
- Suchschritte:
  1. lokal buyer~„Landeshauptstadt Düsseldorf“: 156 (73 result, 83 competition; 97 vor eForms ohne Titel; alle eForms-Titel sind Sammeltitel wie „Gebäudeunterhaltsreinigung ab …“)
  2. API `FT="Bezirk 3" AND FT=Düsseldorf AND classification-cpv=909*` (Kontrolle): 9 (Testfall; vorher 122460-2026, 202355-2026, 253014-2026, 219041-2026, 418297-2026;
     danach 529555-2026, 617598-2026; dazu 462918-2016 Wuppertal)
  - geöffnete XML: 691452-2023, 253014-2026, 418297-2026
- Ergebnis: **unklar**
- Vorgänger: – (einziger zeitlicher Kandidat: 691452-2023, result, eForms, 2023-11-14)
- Beleg: Fakten: 691452-2023 „Gebäudeunterhaltsreinigung ab 01.12.2023 ein Objekt“, Laufzeit 2023-12-01 bis 2026-11-30, ohne Ort. Das Ende passt genau zum Testfall-Beginn,
  aber es ist 1 statt 3 Objekte und kein Bezirk angegeben. 253014-2026 (Los 2 „Gebäudeunterhaltsreinigung Bezirk 3 und 4“, 2026-05-01 bis 2029-04-30) und 418297-2026
  (Rahmenvertrag ab 2027, Preisblatt „Bezirk3“) laufen parallel, sind also keine Vorgänger. Begründung: Ohne Objektangaben ist die Definition nicht prüfbar.
  Einschätzung: Düsseldorfer Bekanntmachungen sind über TED nicht objektgenau zuordenbar.
- Vertragsende Vorgänger: unbekannt; Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 2/3

### T29 – 620007-2026 (2026-09-09) – Bädergesellschaft Bremerhaven mbH
- Objekt(e): Freizeitschwimmbad „Bad 1“, „Kurt-Schumacher-Straße 14, 27578 Bremerhaven“.
- Leistungsart: Unterhaltsreinigung der Umkleide-, Sanitär-, Eingangs- und Personalbereiche; ab 01.01.2027, 1 Jahr.
- Suchschritte:
  1. lokal Text~„Bremerhaven“: 139 (keine Bädergesellschaft; Seestadt Immobilien, AWI, BA u. a.)
  2. API `(FT="Bad 1" OR FT=Freizeitschwimmbad) AND FT=Bremerhaven AND classification-cpv=909*` (Kontrolle): 1 = Testfall
  3. API `(FT=Bädergesellschaft OR FT="Kurt-Schumacher-Straße" OR FT=Freizeitbad OR FT=Schwimmbad OR FT=Hallenbad OR FT=Bad) AND FT=Bremerhaven AND … <20260909`: 12
     (LK Cuxhaven, Wurster Nordseeküste, TK, BA, DWD – kein Bad in Bremerhaven)
  - geöffnete XML: keine
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Fakt: Vor dem Testfall gibt es auf TED keine Notice der Bädergesellschaft Bremerhaven mit CPV 909 und keine, die das Bad oder die Adresse nennt.
- Vertragsende Vorgänger: entfällt; Hinweis auf vorzeitige Neuvergabe: entfällt
- Abfragen/XML: 3/0

### T30 – 555680-2026 (2026-08-11) – Stadt Frankfurt am Main, Gesundheitsamt
- Objekt(e): nicht benannt; Leistungsort „Frankfurt am Main, 60313“ (die Auftraggeberadresse Breite Gasse 28, 60313, ist Amtsadresse); „Gesamtfläche von 12.642,04 m² bei einer
  jährlichen Reinigungsfläche von insgesamt 1.794.355,62 m²“.
- Leistungsart: Unterhaltsreinigung; 01.01.2027–31.12.2030 + 2 × 1 Jahr.
- Suchschritte:
  1. lokal buyer~„Gesundheitsamt“: 6 (Paare 184286-2018/412645-2018, 426517-2019/17768-2020, 19547-2023/434089-2023)
  2. API `FT="Breite Gasse" AND FT=Frankfurt AND classification-cpv=909*` (Kontrolle): 11 (inkl. Testfall)
  3. API `FT=Gesundheitsamt AND FT=Frankfurt AND … <20260811`: 12
  - geöffnete XML: 434089-2023, 19547-2023
- Ergebnis: **objektgleich**
- Vorgänger: **434089-2023**, result, vor eForms, 2023-07-18, Los 3 (Ausschreibung 19547-2023, competition, 2023-01-13)
- Beleg: 434089-2023 Los 3 „Gebäudereinigung Haupgebäude: 10.343,17 m² + Gebäudereinigung Außenstelle Zeil 5, 2./4./5. OG: 2.222,83 m² + Gebäudereinigung Außenstelle
  Töngesgasse 4, 1.-4. OG: 1.483,39 m²“; Zuschlag an WISAG (Vertrag 2023-07-13). Gleicher Auftraggeber, gleiche Leistungsart. Hauptgebäude + Zeil 5 = 12.566,00 m²,
  Testfall 12.642,04 m² (+0,6 %). Einschätzung: Außenstelle Töngesgasse entfallen. Die Objekte sind im Testfall nicht benannt. **Belegstärke: mittel.**
  Fakt: Der Vorgänger war ein FM-Bündel (4 Lose: Sicherheit, technisches Gebäudemanagement, Gebäudereinigung, Arealbewirtschaftung); 2026 wird die Reinigung allein ausgeschrieben.
- Vertragsende Vorgänger: 19547-2023 DATE_START 2024-01-01, DATE_END 2026-12-31, „2x optionale Verlängerung um jeweils 1 Jahr (max. bis 31.12.2028)“. Testfall beginnt
  01.01.2027 (nach der Grundlaufzeit, Option nicht gezogen). Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 3/2

---

## Übersicht Teil 2 (T16–T30)

**Anzahl je Kategorie (Fakten aus den Einzelprotokollen)**

| Kategorie | Anzahl | Fälle |
|---|---|---|
| objektgleich | 7 | T19, T21, T22, T23, T24, T26, T30 |
| teilmenge | 1 | T18 |
| kein_vorgaenger | 5 | T16, T17, T20, T25, T29 |
| unklar | 2 | T27, T28 |

Gefunden im Sinne von V1 (objektgleich + teilmenge): **8 von 15**.

| T | Kategorie | Jüngster Vorgänger | Form, Stand, Datum | Belegstärke |
|---|---|---|---|---|
| T16 | kein_vorgaenger | – | – | – |
| T17 | kein_vorgaenger | – | – | – |
| T18 | teilmenge | 488398-2026 (je Los weitere: 557041-2023, 755423-2023, 710461-2023, 524787-2023, 571224-2023, 227031-2024) | result, eForms, 2026-07-15 | stark |
| T19 | objektgleich | 636701-2023 (CN 286526-2023) | result, vor eForms, 2023-10-20 | stark |
| T20 | kein_vorgaenger | – | – | – |
| T21 | objektgleich | 301495-2022 (CN 142984-2022) | result, vor eForms, 2022-06-03 | mittel |
| T22 | objektgleich | 509902-2022 | competition, vor eForms, 2022-09-19 | stark |
| T23 | objektgleich | 408656-2018 (CN 23048-2018) | result, vor eForms, 2018-09-19 | stark |
| T24 | objektgleich | 85643-2020 (CN 488738-2019) | result, vor eForms, 2020-02-20 | stark |
| T25 | kein_vorgaenger | – | – | – |
| T26 | objektgleich | 462151-2026 (aufgehoben); mit Vertrag: 95743-2021 (CN 557850-2020) | competition, eForms, 2026-07-06 / result, vor eForms, 2021-02-24 | stark |
| T27 | unklar | Kandidat 390156-2023 | competition, vor eForms, 2023-06-30 | – |
| T28 | unklar | Kandidat 691452-2023 (nur zeitlich) | result, eForms, 2023-11-14 | – |
| T29 | kein_vorgaenger | – | – | – |
| T30 | objektgleich | 434089-2023 Los 3 (CN 19547-2023) | result, vor eForms, 2023-07-18 | mittel |

**Abbruch durch Budget:** keiner. Höchstwerte: 7 Abfragen (T16, T17), 8 XML (T18).

**Vertragsende und vorzeitige Neuvergabe (Fakten aus den XML)**
- Vorgänger-Ende bestimmbar: T18 (2028-01-31 für Lose 8/9), T19 (2026-12-31), T21 (Grundlaufzeit 2025-08-31, spätestens 2028-08-31), T22 (spätestens 2027-01-31),
  T23 (spätestens 2022-12-31), T24 (laut TED 2021-02-28), T26 (2026-03-31), T30 (Grundlaufzeit 2026-12-31).
- Vorzeitige Neuvergabe nach Definition (neuer Beginn mindestens 3 Monate vor Ende der Grundlaufzeit): **nur T18** (Lose 8/9: Beginn 2027-02-01, Vorgänger bis 2028-01-31).

**Auffälligkeiten (Fakten mit Quelle)**
- Sieben der acht gefundenen Fälle hängen an Verträgen aus der Zeit vor eForms (T19, T21, T22, T23, T24, T26 mit Vertrag, T30); nur T18 hat eForms-Vorgänger.
  In den lokalen Rohdaten haben die alten Notices keine Titel; gefunden wurden sie über `FT`, bestätigt über die XML. Bei T22 gibt es auf TED nur die Ausschreibung,
  keinen Zuschlag; ebenso beim Kandidaten zu T27.
- Zentrale Vergabestellen und Beschaffer: Regierung von Oberbayern vergab 2023/24 für die Regierung von Schwaben (755423-2023, 710461-2023, 227031-2024; im XML
  „vertreten durch die Regierung von Schwaben“); BayLfSt (T21, 578 Verfahren); VB-BW mit Amtsadresse „L 4, 4-6“ als Leistungsort (T26); LBB RLP (T19);
  SB Südniedersachsen mit Sitz Clausthal-Zellerfeld (T24); Kommunal Agentur NRW für die Stadt Springe (T27; im XML als erste Organisation).
- Namensvarianten: „FA Erlangen“ → „FA Mittelfranken-Ost, Standort Erlangen“ (T21); „BGW Bezirksverwaltung Berlin“ → „Berufsgenossenschaft für Gesundheitsdienst und
  Wohlfahrtspflege (BGW)“ (T22); „Unterkunfts-Dependance“ → „ANKER-Dependance“ (T18); „Land Baden-Württemberg, vertreten durch den Landesbetrieb …“ → „Vermögen und Bau
  Baden-Württemberg, Amt Mannheim und Heidelberg“ (T26).
- Neuzuschnitte: T18 bündelt sieben frühere Einzelvergaben (zwei Auftraggeber) zu einem Verfahren mit 9 Losen; T24 teilt 6 Lose in 8 auf; T30 löst die Reinigung aus einem FM-Bündel.
- Lücken auf TED zwischen Vorgänger-Ende und Testfall: T23 (2023–2026), T24 (laut TED Ende 2021, neuer Beginn 2027), T18 Lose 2, 3 und 7 (Verträge bis 2025), T26 (April–November 2026).
- Bekanntmachungen ohne Objektangaben: T27 und T28 (Testfall und Kandidaten), T30 (nur Testfall), T20 (nur die Sammelvergaben).
- T16 ist eine Bauzwischen- und Bauendreinigung und fällt sachlich aus der Population (Stichwortliste greift wegen des Titels nicht).

**Werkzeuge und Daten (Fakten)**
- `FT` trifft nur ganze Wörter. Eine ODER-Abfrage zeigt nicht, welcher Begriff getroffen hat; die XML muss geöffnet werden. Gleichnamige Straßen oder Orte anderswo
  erzeugen Fehltreffer („Südring“ Rostock statt Bielefeld, „Lilienthal“ Landkreis Osterholz). Häufige Wörter wie „Steuern“ machen eine Abfrage unbrauchbar (296 Treffer, T21).
- Kleine Datenfehler im XML: 488398-2026 Los Kempten mit PLZ 89312 (Günzburg) im Leistungsort; 623928-2026 nennt Bodenflächen „Glasfläche“.
- Notices vom selben Tag wie der Testfall (554730-2026 bei T26) wurden nicht als Vorgänger gezählt („vor dem Testfall“).
- Keine HTTP-Fehler, kein 429.

**Einschätzungen (keine Fakten)**
- Die beiden unklaren Fälle (T27, T28) und die Belegstärke „mittel“ (T21, T30) hängen an der Auslegung, wie viel Kennzahl- und Terminübereinstimmung ohne Objektnamen reicht.
  Würde T27 als Teilmenge gewertet, wären es 9 von 15.
- Für einen Backtest sind T19 und T22 die saubersten Paare (Ende der Vorgänger = neuer Beginn, gleiche Beschreibung). T18 zeigt, dass Neuzuschnitte über mehrere
  Auftraggeber hinweg eine Zuordnung allein über den Auftraggebernamen verfehlen würden.
