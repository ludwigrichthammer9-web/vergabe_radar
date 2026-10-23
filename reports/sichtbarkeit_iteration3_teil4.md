# Sichtbarkeit der Vorgänger – Handsuche Iteration 3, Teil 4 (T46–T60)

Rechercheur (Subagent), Recherche am 2026-10-23. Testfälle: Zeilen 46–60 aus `reports/testfaelle_iteration3.txt`.
Definitionen: `docs/iterationen.md`, Iteration 3, „Begriffe“. Unabhängigkeit: Regel-, Merkmals- und Ergebnisdateien
(`src/zuordnung_*.py`, `src/objekt_merkmale.py`, `data/processed/`, `reports/zuordnung_*`, `k2_*`, `blindpruefung_*`) wurden nicht gelesen.
Aus Teil 1–3 wurde nur der Abschnitt „Vorgehen und Konventionen“ übernommen.

## Vorgehen und Konventionen (wie Teil 1–3)

**Quellen**
- *Lokal* (zählt als Abfrage): unveränderte API-Rohdaten `data/raw/ted_search/DEU_result_cpv909_20161001_20260930/` und
  `data/raw/ted_search/DEU_competition_cpv909_20161001_20260930/`. Gefiltert immer auf 20161001 ≤ Veröffentlichung < Testfalldatum.
  „buyer~x“ = regulärer Ausdruck (ohne Groß-/Kleinschreibung) über den Auftraggebernamen; „Text~x“ = regulärer Ausdruck über Auftraggebername,
  -ort, -PLZ, Titel (Verfahren/Los) und Leistungsort (Ort, PLZ, Straße). „Los-Titel buyer~x“ = Auflistung der Los-Titel und Leistungsort-Straßen
  aller eForms-Notices des Auftraggebers. Vor eForms sind dort nur Auftraggebername und -ort gefüllt. Trefferzahlen als „gesamt (result/competition)“.
- *Live-API* (`POST https://api.ted.europa.eu/v3/notices/search`): vor allem das Volltextfeld `FT`. **Kontrollabfrage je Testfall:** eine
  `FT`-Abfrage, die den Testfall selbst finden muss. Die API-Abfragen sind nicht nach `form-type` getrennt (result und competition gemeinsam;
  Berichtigungen werden ignoriert). In T51 und T60 wurde nur lokal gesucht (keine API-Abfrage), dort entfällt die FT-Kontrolle.
- *XML*: `https://ted.europa.eu/en/notice/<nr>/xml`.
- Alle API-Antworten (mit Request als `*.request.json`) und alle XML liegen unverändert unter `data/raw/rechercheur_20261023/<Testfall-Nummer>/`.
  Lokale Abfragen wurden nicht gespeichert; sie lassen sich mit den angegebenen Suchbegriffen aus den vorhandenen Rohdaten wiederholen.

**Zählung:** „Abfragen/XML“ = lokale + API-Abfragen / geöffnete Kandidaten-XML. Die XML des Testfalls selbst ist nicht mitgezählt.

**Kategorien-Konvention (aus Teil 1–3):**
- *objektgleich*: Liegenschaft(en) per Name oder Adresse identisch, Leistungsart überlappt (Unterhalts-, Grund-, Glasreinigung; Baureinigung
  zählt nicht). Kleine Abweichungen im Objektbestand (ein Objekt mehr oder weniger) oder eine neue Losaufteilung desselben Bestands bleiben objektgleich.
- *teilmenge*: nur ein Teil der Objekte gemeinsam (Bewertung auf Verfahrensebene; z. B. Vorgänger war ein größeres Bündel oder Testfall bündelt mehr).
- **Belegstärke** (Einschätzung, keine Kategorie der Definition): stark = Adresse/Liegenschaftsname wörtlich gleich; mittel = Sammelbezeichnung +
  Kennzahlen/Losnummer/Anschlusstermin; schwach = nur indirekt.
- **Amtsadressen** zentraler Vergabestellen gelten nicht als Objektbeleg.
- Nennen weder Testfall noch Kandidaten ein Objekt, aber es gibt konkrete Hinweise (gleicher Auftraggeber, gleiche Sammelbezeichnung,
  Anschlusstermin) → *unklar*. Enge Kennzahlen-Übereinstimmung bei benanntem Objektbestand → *objektgleich*, Belegstärke *mittel*.
- Notices vom selben Tag wie der Testfall oder später zählen nicht als Vorgänger.
- **Ergänzende Auslegung in Teil 4 (T46):** Nennt nur der Testfall Objekte, die Kandidaten desselben Auftraggebers aber nicht (nur „x Objekte der
  Stadt“), ist die Definition ebenfalls nicht prüfbar → *unklar*, sofern konkrete Hinweise vorliegen.
- **Vorzeitige Neuvergabe** nach Definition: neuer Vertrag beginnt mindestens 3 Monate vor Ende der *Grundlaufzeit* des Vorgängers.

---

### T46 – 638682-2026 (2026-09-16) – Stadt Bielefeld - Amt für Zentrale Leistungen
- Objekt(e): 8 Objekte in 2 Losen. Los 1: „Bezirksamt Jöllenbeck, Kita Jöllenbeck, Sporthalle Auf dem Tie 1, Feuerwehrgerätehaus Jöllenbeck,
  UWB Westerengerstr.“; Los 2: „Grundschule Sieker Interim, Grundschule Heeperholz, Sporthalle Heepen“. Laufzeit 01.02.2027–31.01.2028 + 3 × 12 Monate.
- Leistungsart: Unterhalts-, Sonder- und teilweise Ergänzungsreinigung (CPV 90911200).
- Suchschritte:
  - lokal buyer~bielefeld → 98 (45/53)
  - API `FT=Heeperholz AND classification-cpv=909*` → 1 (nur Testfall = Kontrolle erfolgreich)
  - API `FT=Jöllenbeck AND classification-cpv=909*` → 2 (Testfall; 521835-2026 BBF Kombibad Jöllenbeck, anderes Objekt/anderer AG)
  - lokal Text~(heepen|jöllenbeck|joellenbeck|sieker|westerenger|auf dem tie) → 3 (521835-2026, 503868-2026, 31781-2026)
  - API `FT=Sieker AND classification-cpv=909*` → 9 (Testfall + fremde AG: Thünen-Institut, BImA)
  - API `FT=Heepen AND classification-cpv=909*` → 7 (Testfall, 31781-2026, 503868-2026, BBF-Bäder; 708941-2026 nach Testfall)
  - XML geöffnet: 31781-2026, 503868-2026, 51552-2025, 737704-2023, 696230-2022, 461601-2022
- Ergebnis: **unklar**
- Vorgänger: kein objektgleicher Vorgänger belegbar. Kandidat mit Hinweisen: 461601-2022 (competition, vor eForms, 2022-08-24).
- Beleg / Begründung:
  - Fakt: 31781-2026 / Zuschlag 503868-2026 tragen fast denselben Titel („in 8 Objekten der Stadt Bielefeld“), nennen aber **andere** Objekte:
    „Feuerwehrgerätehaus Altenhagen, Feuerwehrgerätehaus Heepen, KiTa Am Vollbruch, Gymnasium Heepen 2“ / „Grundschule Brake, Grundschule
    Schröttinghausen, KiTa Schröttinghausen, Sporthalle Spiekeroogstraße“ → kein gemeinsames Objekt.
  - Fakt: Die übrigen Bielefelder Bündel nennen keine Objekte: 51552-2025 „Unterhalts-, Sonder- und tlw. Ergänzungsreinigung in 9 Objekten der Stadt
    Bielefeld“ (Lose „in 4 Objekten“, „in 5 Objekten“, 01.06.2025–31.05.2026); 737704-2023 „in 39 Objekten“ (6 Lose ohne Namen); 461601-2022 „in 15 Objekten
    der Stadt Bielefeld, aufgeteilt auf 3 Lose, v. 01.01.2023 - 31.12.2023 plus 3 x 12 M. Verlängerungsoption“ (Lose „in 4/5/6 Objekten“);
    696230-2022 ist Glas- und Rahmenreinigung in 297 Gebäuden ohne Namen.
  - Fakt: Volltext findet die Objektnamen (Heeperholz, Jöllenbeck, Sieker) in keiner älteren Notice der Stadt Bielefeld.
  - Einschätzung: Bielefeld vergibt die Unterhaltsreinigung in rollierenden, wechselnd zugeschnittenen Bündeln mit 1 Jahr + 3 × 12 Monaten. 461601-2022
    (Höchstende 31.12.2026) passt zeitlich ungefähr zum Start 01.02.2027, ist aber ohne Objektliste nicht zuordenbar.
- Vertragsende Vorgänger: unbekannt (Kandidat 461601-2022: Höchstende 31.12.2026); Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 6/6

### T47 – 651281-2026 (2026-09-22) – Deutsches Archäologisches Institut
- Objekt(e): „8 Liegenschaften im Berliner Stadtgebiet (u. a. Bürogebäude, Werkstätten, Archivflächen sowie Übernachtungsbereiche – siehe Anlage B0
  Objektübersicht)“; Leistungsort nur PLZ 14195 Berlin. Keine Objektnamen oder Adressen in der Bekanntmachung. Laufzeit ab 01.01.2027.
- Leistungsart: Los 1 Unterhaltsreinigung, Los 2 Glas- und Rahmenreinigung.
- Suchschritte:
  - lokal buyer~arch(ä|ae)olog → 4 (2/2; LWL-Archäologie Münster, Archäologisches Landesmuseum Konstanz)
  - API `FT=Archäologischen AND classification-cpv=909*` → 7 (Kontrolle: Testfall gefunden; 693249-2026 nach Testfall; BImA 326731-2020/575910-2020 und
    273391-2024/656919-2024 betreffen die DAI-Kommission in **München**)
  - API `FT=Podbielskiallee AND classification-cpv=909*` → 3 (nur Botschaft Dänemark, Podbielskiallee 34; Testfall selbst nicht gefunden)
  - API `FT=Wiegand AND classification-cpv=909*` → 21 (alle fremd, v. a. Autobahn GmbH)
  - API `FT=(Archäologisches OR Archäologische OR Archäologie) AND classification-cpv=909* AND publication-date<20260922` → 51 (kein DAI-Berlin-Bezug)
  - XML geöffnet: 326731-2020, 21349-2022
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: 326731-2020 (BImA) Los 4: „Kommission für Alte Geschichte und Epigraphik, Deutsches Archäologisches Institut, Amalienstraße 73 b, 80799 München“
  → anderer Ort. 21349-2022 (Senatsverwaltung Berlin, „archäologische Funde“) ist „Baureinigung“ → Leistungsart ausgeschlossen.
- Einschätzung: Der Testfall nennt keine Objekte; ein früherer Vertrag könnte unter einem unbenannten Sammelverfahren gelaufen sein. Dafür gibt es aber
  keinen konkreten Hinweis, daher nicht „unklar“.
- Vertragsende Vorgänger: –; Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 5/2

### T48 – 496932-2026 (2026-07-17) – Stadt Solingen
- Objekt(e): Gesamtschule Höhscheid, Kanalstraße 20 und Zweigstraße 15-17, 42657 Solingen. Laufzeit 01.11.2026–31.10.2029 (+1 Jahr).
- Leistungsart: Unterhaltsreinigung (inkl. Ferienreinigung Turnhallen).
- Suchschritte:
  - lokal buyer~solingen → 55 (16/39)
  - API `FT=Höhscheid AND classification-cpv=909*` → 7 (Kontrolle: Testfall gefunden; 512302-2026 nach Testfall; 683345-2024, 546264-2024, 515518-2024;
    vor eForms 202393-2020, 56893-2020)
  - XML geöffnet: 683345-2024, 546264-2024
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 683345-2024, result, eForms, 2024-11-08 (Ausschreibung 546264-2024, competition, eForms, 2024-09-11)
- Beleg: 683345-2024 Titel „Unterhaltsreinigung der Gesamtschule Höhscheid, Kanalstraße 20 und Zweigstraße 15-17, 42657 Solingen“ – wörtlich gleich
  mit dem Testfall; Beschreibung „mit einer Laufzeit von zwei Jahren sowie einer einmaligen Verlängerungsoption um ein weiteres Jahr“.
- Vertragsende Vorgänger: 31.10.2026 (PlannedPeriod 2024-11-01 bis 2026-10-31; Option bis 31.10.2027 nicht genutzt); Hinweis auf vorzeitige Neuvergabe: nein
  (Testfall beginnt 01.11.2026 direkt im Anschluss)
- Abfragen/XML: 2/2

### T49 – 481461-2026 (2026-07-13) – Landratsamt Ilm-Kreis
- Objekt(e): Staatliches Gymnasium „Goetheschule“ Haus 1 inkl. Internat, Ilmenau (PLZ 98693). Laufzeit 01.01.2027–31.12.2027, jährliche Verlängerung bis max. 31.12.2029.
- Leistungsart: Los 1 Unterhalts- und Grundreinigung, Los 2 Glasreinigung.
- Suchschritte:
  - lokal buyer~(ilm-kreis|ilmkreis|ilm kreis) → 57 (24/33; eForms-Titel nennen nur andere Schulen, z. B. GS Langewiesen, RS H. Hertz Ilmenau, BSZ Ilmenau)
  - API `FT=Goetheschule AND classification-cpv=909*` → 29 (Kontrolle: Testfall gefunden; sonst Quickborn, Marl, Linz, Bremerhaven u. a.)
  - API `FT=Ilmenau AND classification-cpv=909* AND publication-date<20260713` → 48
  - API `FT=Goethe AND FT=Ilmenau AND classification-cpv=909*` → 0
  - API `FT=Internat AND FT=Ilmenau AND classification-cpv=909*` → 1 (nur Testfall)
  - XML geöffnet: 517511-2023, 386411-2022, 116160-2022
- Ergebnis: **kein_vorgaenger**
- Vorgänger: –
- Beleg: Die Ilm-Kreis-Kandidaten in Ilmenau betreffen andere Schulen: 517511-2023 „Reinigung an der Grundschule sowie der Schulsporthalle "Ziolkowski"
  in Ilmenau“ (Ziolkowskistraße 14); 386411-2022 und 116160-2022 „Staatl. Berufsschule, Am Ehrenberg 1, 98693 Ilmenau“.
- Vertragsende Vorgänger: –; Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 5/3

### T50 – 569458-2026 (2026-08-18) – Gemeinde Dußlingen
- Objekt(e): „Gebäudereinigungsleistungen in Liegenschaften der Gemeinde Dußlingen“; keine Objektnamen, kein Leistungsort. Los 1: „ca. 1.200.000 m²
  Jahresreinigungsfläche Unterhaltsreinigung, ca. 8.700 m² Grundreinigungsfläche pro Jahr“. Laufzeit 01.01.2027–31.12.2030.
- Leistungsart: Unterhalts- und Grundreinigung.
- Suchschritte:
  - lokal Text~du(ß|ss)lingen → 3 (1/2): 99309-2026 und 399420-2025 (GVV Steinlach-Wiesaz, Baureinigung), 216353-2021
  - API `FT=Dußlingen AND classification-cpv=909*` → 6 (Kontrolle: Testfall gefunden; 576064-2026 und 632477-2026 nach Testfall)
  - XML geöffnet: 216353-2021
- Ergebnis: **unklar**
- Vorgänger (Kandidat): 216353-2021, competition, vor eForms, 2021-04-30 (kein zugehöriger Zuschlag in den Rohdaten gefunden)
- Beleg / Begründung: 216353-2021 „Vergabe von Reingungsleistungen der Gemeinde Dußlingen“: „2 Lose Unterhaltsreinigung 10 Objekte (Schule, Sportstätte,
  Verwaltungsgebäude, Veranstaltungsgebäude, Betriebsgebäude, Kindergärten, Kinderkrippe)“ + „1 Los Glasreinigung ca. 12 Objekte“; Laufzeit
  01.11.2021–31.10.2023, „Maximal 3-malige Verlängerung um jeweils 1 Jahr“. Weder Testfall noch Kandidat nennen Objekte; Hinweise: gleicher
  Auftraggeber, gleicher Gesamtzuschnitt (alle Gemeindeliegenschaften), Höchstende 31.10.2026 kurz vor Start 01.01.2027.
- Vertragsende Vorgänger: Höchstende 31.10.2026 (Grundlaufzeit bis 31.10.2023); Hinweis auf vorzeitige Neuvergabe: nein (falls Vorgänger)
- Abfragen/XML: 2/1

### T51 – 628016-2026 (2026-09-11) – Stadt Bocholt
- Objekt(e): „Objektgruppe 2: Unterhaltsreinigung Verwaltungsgebäude“, „Unterhaltreinigung eines Verwaltungsgebäudes“; Leistungsort „Stadtverwaltung
  Bocholt, 46395 Bocholt“ (kein Gebäudename, keine Straße). Laufzeit 42 Monate.
- Leistungsart: Unterhaltsreinigung.
- Suchschritte:
  - lokal Text~bocholt → 38 (15/23)
  - lokal Los-Titel buyer~„stadt bocholt“ (eForms) → 16 Notices; keine nennt ein Objekt (Los-Titel z. B. „Gebäude der Stadt Bocholt: Unterhaltsreinigung
    Bezirk 3“, „2 Schulen 2 Verwaltungsgebäude | 4 Schulen | 4 Verwaltungsgebäude“, „2. Reinigungsbezirk Bocholt …“, „Liegenschaften Schulgebäude Los 1 |
    … Los 2 inkl. Turnhallen | Verwaltungsgebäude“)
  - XML geöffnet: 483870-2026, 410442-2026
- Ergebnis: **unklar**
- Vorgänger (Kandidat): 483870-2026, competition, eForms, 2026-07-14 (erste Fassung 410442-2026, competition, eForms, 2026-06-16)
- Beleg / Begründung: 483870-2026 „Objektgruppe 2: Unterhaltsreinigung und Einpflege“, Beschreibung „Los 1 und 2: Unterhaltreinigung von Schulgebäuden /
  Turnhallen inkl. Einpflege Los 3: Unterhaltreinigung Verwaltungsgebäude“, Los 3 Name „Verwaltungsgebäude“, Dauer 44 Monate. Der Testfall übernimmt
  Sammelbezeichnung und Los-3-Inhalt; beide nennen kein Objekt. Einschätzung: sehr wahrscheinlich dieselbe Leistung (Neuausschreibung von Los 3 der
  Objektgruppe 2 zwei Monate später). Damit wäre der „Vorgänger“ eine nicht abgeschlossene Vergabe und kein ausgelaufener Vertrag.
- Fakt am Rande: 700141-2026 (Zuschlag Objektgruppe 2, 2026-10-09) liegt nach dem Testfall und zählt nicht.
- Vertragsende Vorgänger: unbekannt; Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 2/2

### T52 – 644157-2026 (2026-09-18) – Studierendenwerk Trier AöR
- Objekt(e): Mensa Schneidershof, Stuckradweg 4, 54293 Trier. Laufzeit 01.01.2027–31.12.2028 (+2 × 1 Jahr).
- Leistungsart: Unterhaltsreinigung.
- Suchschritte:
  - lokal Text~(studierendenwerk trier|studentenwerk trier|schneidershof|stuckradweg) → 7 (4/3; alle vor eForms ohne Titel)
  - API `FT=Schneidershof AND classification-cpv=909*` → 7 (Kontrolle: Testfall gefunden; 726161-2026 nach Testfall)
  - API `FT=Stuckradweg AND classification-cpv=909*` → 5
  - XML geöffnet: 716226-2022, 627861-2022
- Ergebnis: **teilmenge** (Belegstärke stark; auf Losebene objektgleich)
- Vorgänger: 716226-2022, result, vor eForms, 2022-12-23 (Ausschreibung 627861-2022, competition, vor eForms, 2022-11-11; REF „2022/S 218-627861“)
- Beleg: 716226-2022 „Gebäudereinigung der Mensen und Cafeterien“, Los 1 „Mensa Schneidershof“, MAIN_SITE „Studierendenwerk Trier Stuckradweg 4 54293
  Trier“, „Unterhaltsreinigung der Mensa und Cafeteria Schneidershof“; dazu Los 2 Mensa Tarforst (Universitätsring 12a) und Los 3 Mensa Petrisberg
  (Behringstraße 21). Vorgänger war ein 3-Mensen-Bündel, der Testfall umfasst nur noch eine Mensa → teilmenge auf Verfahrensebene.
- Vertragsende Vorgänger: 627861-2022: 01.01.2023–31.12.2024, „kann zweimalig um jeweils 1 Jahr verlängert werden“ → Höchstende 31.12.2026;
  Hinweis auf vorzeitige Neuvergabe: nein (Start 01.01.2027 = Anschluss an Höchstende)
- Abfragen/XML: 3/2

### T53 – 531216-2026 (2026-07-31) – Leipziger Wohnungs-und Baugesellschaft mbH (LWB)
- Objekt(e): Treppenhäuser/Gemeinschaftsflächen in Wohngebäuden der Region Ost, 9 Lose mit vollständigen Adresslisten: 1 Mockau West (Start 01.05.2027),
  2 Mockau (01.06.2027), 3 Thekla Erla-Siedlung (01.04.2027), 4 Schönefeld, 5 Schönefeld Ost, 6 Paunsdorf und Kiebitzmark (je 01.01.2027),
  7 Volkmarsdorf (01.06.2027), 8 Sellerhausen Engelsdorf, 9 Hochhäuser Mockau Schönefeld (je 01.01.2027). Ende spätestens 31.12.2030.
- Leistungsart: Unterhalts-, Glas- und Rahmenreinigung, jährliche Grundreinigung.
- Suchschritte:
  - lokal buyer~(leipziger wohnungs|lwb) → 78 (37/41)
  - API `FT=(Katzmannstr OR Carlebachstr OR Fullaweg OR Belterstr OR Dornbergerstr OR Volksgartenstr OR Poserstr OR Stöckelstr OR Schwantesstr OR Wodanstr
    OR Rosenowstr OR Oberläuterstr) AND classification-cpv=909*` → 5 (Kontrolle: Testfall gefunden; sonst Stadt Mönchengladbach, BwDLZ Dresden)
  - API `FT=(Mockau OR Schönefeld OR Volkmarsdorf OR Sellerhausen OR Engelsdorf OR Thekla OR Paunsdorf OR Kiebitzmark) AND classification-cpv=909* AND
    publication-date<20260731` → 87 (darunter 15 LWB-Notices)
  - XML geöffnet (Budget 10 erreicht): 255653-2026, 343641-2023, 209335-2023, 77789-2023, 180463-2023, 68020-2023, 185915-2022, 547949-2021, 604952-2020, 604953-2020
- Ergebnis: **teilmenge** (Belegstärke stark für Los 6; mittel für Los 1 und Los 7)
- Vorgänger (jüngster): 255653-2026, result, eForms, 2026-04-15 (Ausschreibung 82423-2026, nicht geöffnet)
- Beleg:
  - Los 6 (stark): 255653-2026 „Unterhaltsreinigung von Treppenhäusern in 04329 Leipzig (Paunsdorf)“, Adressen „Ahornstraße 2-17, Heiterblickallee 1-70,
    Platanenstraße 2-79, Schlehenweg 1-28, Gundermannstraße 21-37, Hainveilchenweg 1-14, Am Vorwerk 2-13, Hartriegelstraße 2-20, Haselstraße 2-33, …,
    Günselstraße 1-17, Goldsternstraße 13-19, …“; Testfall Los 6: „Ahornstr. 2, 4, 6, 8, 9, …; Am Vorwerk 2, 4, …; Goldsternstr. 13, 15, 17, 19;
    Gundermannstr. 21, …, 37; Günselstr. 1, …; Hainveilchenweg …; Hartriegelstr. …; Haselstr. …; Heiterblickallee …“. Leistungsart gleich.
  - Los 1 Mockau West (mittel): 209335-2023 (result, vor eForms, 2023-04-07) „Gebäudereinigung in 04357 Leipzig, Mockau“; Ausschreibung 68020-2023:
    01.05.2023–30.04.2024, „Eine automatische Verlängerung über den 30.04.2027 hinaus ist nicht möglich“ → Testfall Los 1 beginnt 01.05.2027.
    Nur Stadtteil, keine Adressen.
  - Los 7 Volkmarsdorf (mittel): 343641-2023 (result, vor eForms, 2023-06-09) „Gebäudereinigung in 04315 Leipzig, Volkmarsdorf“; Ausschreibung
    180463-2023: 01.06.2023–31.05.2024, max. bis 31.05.2027 → Testfall Los 7 beginnt 01.06.2027. Nur Stadtteil, keine Adressen.
  - Ältere Stadtteil-Vergaben (nur Stadtteilname): 77789-2023 (Volkmarsdorf), 185915-2022 (Paunsdorf, 2 Lose), 547949-2021 (Volkmarsdorf, 2 Lose),
    604952-2020 (Paunsdorf-West), 604953-2020 (Paunsdorf-Ost).
  - Für Thekla, Schönefeld, Schönefeld-Ost, Sellerhausen-Engelsdorf und die Hochhäuser wurde kein Vorgänger gefunden (Suche wegen XML-Budget nicht vollständig).
  - Einschätzung: Der Testfall bündelt mehrere früher einzeln vergebene Stadtteil-Verträge der LWB (Neuzuschnitt) → teilmenge.
- Vertragsende Vorgänger: 255653-2026: 31.12.2026 (PlannedPeriod 2026-05-01 bis 2026-12-31, Kurzvertrag); Mockau max. 30.04.2027; Volkmarsdorf max.
  31.05.2027. Hinweis auf vorzeitige Neuvergabe: nein (alle drei Lose schließen unmittelbar an)
- Abfragen/XML: 3/10 (**Abbruch durch XML-Budget**)

### T54 – 555833-2026 (2026-08-11) – Staatliches Baumanagement Region Nord-West (zentrale Vergabestelle)
- Objekt(e): Carl von Ossietzky Universität Oldenburg, 4 Lose: Standort A (Haarentor: Ammerländer Heerstr., Uhlhornsweg, Johann-Justus-Weg 147/147a
  Botanischer Garten, Philosophenweg 39/41, 36), Standort B (Verwaltung Ammerländer Heerstr. 114-118, 138, 140), Standort C Nord (Wechloy, Küpkersweg),
  Standort C Süd (Wechloy, Carl-von-Ossietzky-Straße). Start 01.03.2027, Verlängerung auf max. 7 Jahre.
- Leistungsart: **nur Glasreinigung** (CPV 90911300).
- Suchschritte:
  - lokal Text~(ossietzky|universit(ä|ae)t oldenburg|ammerl(ä|ae)nder heerstr|haarentor|wechloy) → 15 (8/7)
  - lokal buyer~(baumanagement.*(nord-west|nordwest)|staatliches baumanagement oldenburg|universit(ä|ae)t oldenburg) → 48 (10/38)
  - API `FT=Ossietzky AND classification-cpv=909*` → 38 (Kontrolle: Testfall gefunden)
  - API `FT=(Haarentor OR Wechloy OR Uhlhornsweg) AND classification-cpv=909*` → 3 (Testfall, 563086-2025, 330433-2025)
  - XML geöffnet: 462845-2020, 563086-2025, 465666-2022
- Ergebnis: **kein_vorgaenger** (Grenzfall: gleiche Liegenschaften, aber keine überlappende Leistungsart)
- Vorgänger: – (gleiche Liegenschaft, andere Leistungsart: 563086-2025, result, eForms, 2025-08-28; 462845-2020, competition, vor eForms, 2020-10-02)
- Beleg: 563086-2025 „IGM25E580001: Unterhaltsreinigung CvO Universität Oldenburg 2 Standorte … Los 1: CvO Uni Standort B (Haarentor), Unterhaltsreinigung
  Los 2: CvO Uni Standort C (Wechloy), Unterhaltsreinigung“, CPV 90911200/90910000, Laufzeit 01.01.2026–31.12.2026. 462845-2020 (Staatliches Baumanagement
  Ems-Weser, Vorgängerbehörde) „20E30474, Carl von Ossietzky Universität Oldenburg Standort (A), Unterhaltsreinigung“, Ammerländer Heer Str. 114-118.
  Adressen stimmen überein, Leistungsart nicht (Unterhaltsreinigung vs. Glasreinigung). Eine frühere Glasreinigung der Universität wurde auf TED nicht
  gefunden. 465666-2022 betrifft die HAWK Göttingen (Von-Ossietzky-Straße), fremd.
- Vertragsende Vorgänger: –; Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 4/3

### T55 – 568915-2026 (2026-08-17) – TraveNetz GmbH
- Objekt(e): Los 1 Hauptstandort Geniner Str. 80, 23560 Lübeck (12 Einzelgebäude, ca. 11.100 m²); Los 2 Außenstandorte: vier Wasserwerke, Netzleitstelle,
  13 Blockheizkraftwerke, Umspannwerke/Schaltanlagen, Rechenzentrum. Laufzeit 01.02.2027–31.01.2029, Verlängerungen bis 31.01.2035.
- Leistungsart: Unterhaltsreinigung.
- Suchschritte:
  - lokal Text~(travenetz|trave|stadtwerke l(ü|ue)beck|geniner) → 11 (4/7; SWL Mobil, LVG, Kreis Segeberg u. a., fremd)
  - API `FT=Geniner AND classification-cpv=909*` → 9 (Kontrolle: Testfall gefunden; Netz Lübeck GmbH 500405-2018, 513567-2018, 566298-2018, 91780-2019 + Berichtigungen)
  - XML geöffnet: 91780-2019, 566298-2018, 513567-2018
- Ergebnis: **objektgleich** (Belegstärke stark)
- Vorgänger: 91780-2019, result (F06 Sektoren), vor eForms, 2019-02-26 (Ausschreibung 513567-2018, competition, vor eForms, 2018-11-21; REF „2018/S 224-513567“).
  Früherer Zuschlag gleichen Inhalts: 566298-2018 (2018-12-21, REF „2018/S 218-500405“).
- Beleg: 91780-2019 (Auftraggeber „Netz Lübeck GmbH, Geniner Str. 80“ = früherer Name): „Ausführung von Unterhaltsreinigungen (u. a. in Büros, Werkstätten
  und Laboren) in den Gebäuden des Auftraggebers in der Geniner Str. in Lübeck, in den Wasserwerken in Klein Disnack, Kleinensee, Vorwerk und Wakenitz sowie
  an ca. 13 BHKW-Standorten im Stadtgebiet Lübeck“. Geniner Str. ist hier das Reinigungsobjekt (nicht nur Amtsadresse); 4 Wasserwerke und 13 BHKW stimmen
  mit dem Testfall überein.
- Vertragsende Vorgänger: 513567-2018: 01.02.2019–31.01.2021, „Option der Verlängerung um jeweils 2 weitere Jahre bis maximal 31.1.2027“ → Höchstende
  31.01.2027; Hinweis auf vorzeitige Neuvergabe: nein (Start 01.02.2027 = Anschluss)
- Abfragen/XML: 2/3

### T56 – 564026-2026 (2026-08-14) – Freistaat Bayern, vertreten durch den Präsidenten des Landgerichts Amberg
- Objekt(e): Amtsgericht Amberg (Lose 1/2), Landgericht Amberg (Lose 3/4), IT-Servicezentrum der bayerischen Justiz (Lose 5/6), alle 92224 Amberg.
  Laufzeit 01.01.2027–31.12.2028.
- Leistungsart: Unterhaltsreinigung (Lose 1, 3, 5) und Glas-/Fensterreinigung (Lose 2, 4, 6).
- Suchschritte:
  - lokal Text~amberg → 247 (109/138; das Muster trifft auch „Bamberg“, daher wenig trennscharf)
  - API `FT=Amberg AND FT=(Landgericht OR Amtsgericht OR Justiz OR Justizbehörden) AND classification-cpv=909*` → 4 (Kontrolle: Testfall gefunden;
    431363-2021, 128622-2021; 447008-2020 MDK fremd)
  - XML geöffnet: 128622-2021, 431363-2021
- Ergebnis: **objektgleich** (Belegstärke stark; IT-Servicezentrum kommt als Objekt hinzu)
- Vorgänger: 431363-2021, result, vor eForms, 2021-08-25 (Auftraggeber im Zuschlag: Oberlandesgericht Nürnberg; Ausschreibung 128622-2021, competition,
  vor eForms, 2021-03-15, Präsident des Landgerichts Amberg; REF „2021/S 051-128622“)
- Beleg: 128622-2021 „Gebäude- und Glasreinigung für die Justizbehörden Amberg“ (fast wörtlich wie Testfall-Titel), „Los 1 – Amtsgericht Amberg“, „Los 2 –
  Landgericht Amberg“; 431363-2021 „Gebäude- und Glasreinigung für das Amtsgericht Amberg“ / „… für das Landgericht Amberg“, Vertragsschluss 18.08.2021.
- Vertragsende Vorgänger: unbekannt; Grundlaufzeit 01.11.2021–31.12.2023, danach „verlängert sich jeweils um ein Jahr, wenn keine Kündigung erfolgt.
  DIe Haushaltsvorschriften des Freistaats Bayern sehen eine Neuvergabe im fünfjährigen Turnus vor.“ Hinweis auf vorzeitige Neuvergabe: nein nach Definition
  (Grundlaufzeit endete 31.12.2023); Einschätzung: Neuvergabe nach gut 5 Jahren entspricht dem genannten Turnus.
- Abfragen/XML: 2/2

### T57 – 607508-2026 (2026-09-03) – Gemeinde Oststeinbek (Kreis Stormarn)
- Objekt(e): Los 1 Rathaus und andere öffentliche Gebäude; Los 2 Schule, Turnhalle, Kita und Hort Gerberstraße; Los 3 Jugendzentrum, Sportforum und
  Grundschule Oststeinbek. Laufzeit 01.01.2027–31.12.2029 (+2 × 1 Jahr, spätestens 31.12.2031).
- Leistungsart: Unterhalts- und Grundreinigung.
- Suchschritte:
  - lokal Text~(oststeinbek|22113) → 18 (7/11; PLZ 22113 trifft auch Hamburg-Billstedt, fremd)
  - API `FT=Oststeinbek AND classification-cpv=909*` → 6 (Kontrolle: Testfall gefunden; 615323-2026 nach Testfall; 686803-2022, 484974-2022, 528305-2019, 375066-2019)
  - XML geöffnet: 686803-2022, 484974-2022
- Ergebnis: **objektgleich** (Belegstärke stark; neue Losaufteilung desselben Bestands)
- Vorgänger: 686803-2022, result, vor eForms, 2022-12-09 (Ausschreibung 484974-2022, competition, vor eForms, 2022-09-06; REF „2022/S 171-484974“)
- Beleg: 686803-2022 „Unterhalts- bzw. Unterhalts- und Grundreinigung in den folgenden Gebäuden: - Rathaus: 1 270 m², … - Turnhalle Gerberstraße: 722 m²,
  - Kindergarten: 591 m², … - Hort-Hauptgebäude: 472 m², … - Grundschule Gerberstraße: 1 577 m², … - Jugendzentrum: 436 m², - Walter-Ruckert-Halle:
  2 214 m², - Sportforum: 1 920 m²“, Vertragsschluss 07.11.2022.
- Vertragsende Vorgänger: 484974-2022: 01.01.2023–31.12.2025, „verlängert sich danach jeweils um ein Jahr … endet spätestens am 31.12.2027“;
  Hinweis auf vorzeitige Neuvergabe: nein nach Definition (Grundlaufzeit endete 31.12.2025); der neue Vertrag beginnt aber 12 Monate vor dem Höchstende.
- Abfragen/XML: 2/2

### T58 – 500007-2026 (2026-07-20) – Stadt Bocholt
- Objekt(e): „Objektgruppe 3: Unterhaltsreinigung und Einpflege“, Lose „Liegenschaften Schulgebäude Los 1 inkl. Turnhallen“, „Liegenschaften Schulgebäude
  Los 2 inkl. Turnhallen“, „Verwaltungsgebäude“; Leistungsort „Stadtgebiet Bocholt“. Keine Objektnamen. Beschreibung wörtlich: „Objektgruppe 2: Los 1 und 2:
  Unterhaltreinigung von Schulgebäuden / Turnhallen inkl. Einpflege Los 3: Unterhaltreinigung Verwaltungsgebäude“ (aus Objektgruppe 2 übernommen).
  Laufzeit 17.10.2026–01.07.2029.
- Leistungsart: Unterhaltsreinigung inkl. Einpflege.
- Suchschritte:
  - lokal buyer~„stadt bocholt“ → 28 (12/16)
  - lokal Los-Titel buyer~„stadt bocholt“ (aus T51 mitgenutzt; keine Objektnamen in allen eForms-Notices)
  - API `FT=Objektgruppe AND FT=Bocholt AND classification-cpv=909*` → 6 (Kontrolle: Testfall gefunden; 637113-2026 Zuschlag Objektgruppe 3 vom 2026-09-16 und
    700141-2026 liegen nach dem Testfall)
  - XML geöffnet: 795216-2023, 394832-2024
- Ergebnis: **unklar**
- Vorgänger (Kandidaten): Bocholter Bezirksverträge, u. a. 795216-2023 (result, eForms, 2023-12-29, „Bezirk 3“), 394832-2024 (result, eForms, 2024-07-03,
  „Bezirk 1 Bocholt Süd“), 702354-2025 (result, eForms, 2025-10-24, „2. Reinigungsbezirk“, nicht geöffnet)
- Beleg / Begründung: 795216-2023 „Unterhaltsreinigung einschließlich Einpflege von 9 Liegenschaften im Stadtgebiet von Bocholt: Schulen, Turnhallen und
  Verwaltungsgebäude“ (01.01.2024–16.07.2027, ohne Objektnamen). 394832-2024 nennt 16 Objekte (z. B. „Annette-von-Droste-Hülshoff-Schule inkl. Turnhalle
  (Wiesenstraße 81)“, „Verwaltungsnebenstelle (Kaiser-Wilhelm-Straße 77)“). Da der Testfall keine Objekte nennt, ist kein Abgleich möglich. Hinweise:
  gleicher Auftraggeber, gleiche Leistungsbeschreibung („Unterhaltsreinigung inkl. Einpflege“ für Schulen/Turnhallen/Verwaltungsgebäude), Bocholt vergibt
  das Stadtgebiet in Bezirken bzw. Objektgruppen. Bezirk 3 endet erst 16.07.2027, passt also nicht zum Start 17.10.2026.
- Vertragsende Vorgänger: unbekannt; Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 2/2 (zzgl. Mitnutzung der Los-Titel-Abfrage aus T51)

### T59 – 538713-2026 (2026-08-04) – Stadt Heidelberg, Hochbauamt - Objektservice
- Objekt(e): Los 1 Bürgeramt Ziegelhausen, Neckarschule, Kindertagesstätte Kanzleigasse; Los 2 Bürgeramt Boxberg Emmertsgrund, Kindertagesstätte
  Blumenstraße, Kindertagesstätte Hegenichstraße. Laufzeit 01.04.2027–31.03.2029, danach jährliche Verlängerung.
- Leistungsart: Unterhalts- und Grundreinigung.
- Suchschritte:
  - lokal buyer~heidelberg → 79 (32/47)
  - API `FT=(Kanzleigasse OR Neckarschule OR Hegenichstraße OR Emmertsgrund OR Ziegelhausen) AND classification-cpv=909*` → 6 (Kontrolle: Testfall gefunden;
    476426-2019, 284901-2019; BBS Bau- und Betriebsservice Mannheim 166386-2021/632593-2021/407186-2022, nicht geöffnet, vermutlich Mannheimer Neckarschule)
  - API `FT=Boxberg AND FT=Heidelberg AND classification-cpv=909*` → 1 (nur Testfall)
  - XML geöffnet: 284901-2019, 476426-2019
- Ergebnis: **teilmenge** (Belegstärke stark)
- Vorgänger: 476426-2019, result, vor eForms, 2019-10-10 (Ausschreibung 284901-2019, competition, vor eForms, 2019-06-19; REF „2019/S 116-284901“)
- Beleg: 476426-2019 Los 1 „Unterhaltsreinigung Grundschule Schlierbach, Neckarschule, Steinbachhalle und Bürgeramt Ziegelhausen“, Zuschlag an Richard Wirth
  Gebäudereinigung, Vertragsschluss 08.10.2019. Gemeinsam: Neckarschule und Bürgeramt Ziegelhausen (Testfall Los 1). Für Kita Kanzleigasse und Los 2
  (Boxberg/Emmertsgrund, Kitas Blumenstraße/Hegenichstraße) kein Vorgänger gefunden.
- Vertragsende Vorgänger: unbekannt; Grundlaufzeit 01.11.2019–31.10.2023, „verlängert sich jeweils um 1 Jahr, wenn er nicht Fristgemäß gekündigt wird“
  (ohne Höchstdauer). Hinweis auf vorzeitige Neuvergabe: nein nach Definition (Grundlaufzeit endete 31.10.2023)
- Abfragen/XML: 3/2

### T60 – 533980-2026 (2026-08-03) – Stadt Brandenburg an der Havel
- Objekt(e): „Gebäudereinigung Verwaltungsobjekte“, „Unterhalts-, Grund- und Glasreinigung in 39 Standorten“, Leistungsort „diverse Standorte im Stadtgebiet“.
  Keine Objektnamen. Laufzeit 01.01.2027–28.02.2031 (+2 Jahre).
- Leistungsart: Unterhalts- und Grundreinigung (Los 1), Glasreinigung (Los 2).
- Suchschritte:
  - lokal Text~(brandenburg an der havel|brandenburg a\. ?d\. ?havel|brandenburg/havel) → 41 (18/23)
  - lokal Los-Titel buyer~„stadt brandenburg“ (eForms) → 6 Notices (Winterdienst, Straßenreinigung, 699611-2024/465050-2024 „Gebäudereinigung Schulstandorte“)
  - XML geöffnet: 377220-2020, 545870-2020
- Ergebnis: **unklar**
- Vorgänger (Kandidat): 545870-2020, result, vor eForms, 2020-11-13 (Ausschreibung 377220-2020, competition, vor eForms, 2020-08-11; REF „2020/S 154-377220“;
  Auftraggeber „Eigenbetrieb Zentrales Gebäude- und Liegenschaftsmanagement“ der Stadt)
- Beleg / Begründung: 377220-2020 „Gebäudereinigung Verwaltungsobjekte“ (wörtlich wie Testfall), Los 1 „Unterhalts- und Grundreinigung in Verwaltungsobjekten“,
  Los 2 „Glasreinigung“, Leistungsort „Brandenburg an der Havel, Stadtgebiet“, Laufzeit 01.01.2021–31.12.2026. Weder Testfall noch Kandidat nennen Objekte;
  konkrete Hinweise: gleicher Auftraggeber (Eigenbetrieb der Stadt), gleiche Sammelbezeichnung und Losstruktur, exakter Anschluss (31.12.2026 → 01.01.2027).
  Einschätzung: sehr wahrscheinlich der Vorgänger, nach Definition aber nicht prüfbar.
- Vertragsende Vorgänger: 31.12.2026 (falls Vorgänger); Hinweis auf vorzeitige Neuvergabe: nein
- Abfragen/XML: 2/2

---

## Übersicht Teil 4 (T46–T60)

**Kategorien (Fakten aus dem Protokoll)**

| Kategorie | Anzahl | Fälle |
|---|---|---|
| objektgleich | 4 | T48, T55, T56, T57 |
| teilmenge | 3 | T52, T53, T59 |
| kein_vorgaenger | 3 | T47, T49, T54 |
| unklar | 5 | T46, T50, T51, T58, T60 |

Gefunden im Sinne von V1 (objektgleich + teilmenge): 7 von 15. Belegstärke: alle 7 stark (bei T53 stark für Los 6, mittel für die Lose 1 und 7).

| T | Testfall | Kategorie | Vorgänger (jüngster) | Form | Belegstärke |
|---|---|---|---|---|---|
| T46 | 638682-2026 | unklar | (Kandidat 461601-2022) | competition, vor eForms | – |
| T47 | 651281-2026 | kein_vorgaenger | – | – | – |
| T48 | 496932-2026 | objektgleich | 683345-2024 | result, eForms | stark |
| T49 | 481461-2026 | kein_vorgaenger | – | – | – |
| T50 | 569458-2026 | unklar | (Kandidat 216353-2021) | competition, vor eForms | – |
| T51 | 628016-2026 | unklar | (Kandidat 483870-2026) | competition, eForms | – |
| T52 | 644157-2026 | teilmenge | 716226-2022 | result, vor eForms | stark |
| T53 | 531216-2026 | teilmenge | 255653-2026 (dazu 209335-2023, 343641-2023) | result, eForms (dazu vor eForms) | stark (Los 6) / mittel |
| T54 | 555833-2026 | kein_vorgaenger | – (gleiche Liegenschaft nur mit Unterhaltsreinigung: 563086-2025) | – | – |
| T55 | 568915-2026 | objektgleich | 91780-2019 | result (F06), vor eForms | stark |
| T56 | 564026-2026 | objektgleich | 431363-2021 | result, vor eForms | stark |
| T57 | 607508-2026 | objektgleich | 686803-2022 | result, vor eForms | stark |
| T58 | 500007-2026 | unklar | (Kandidaten: Bocholter Bezirksverträge) | – | – |
| T59 | 538713-2026 | teilmenge | 476426-2019 | result, vor eForms | stark |
| T60 | 533980-2026 | unklar | (Kandidat 545870-2020) | result, vor eForms | – |

**Abbruch durch Budget:** T53 (10 XML geöffnet; die Lose Thekla, Schönefeld, Schönefeld-Ost, Sellerhausen-Engelsdorf und Hochhäuser sind nicht
abschließend geprüft; die Kategorie „teilmenge“ steht unabhängig davon fest). Kein Fall erreichte das Abfrage-Budget (höchstens 6 Abfragen, T46).

**Vertragsende und vorzeitige Neuvergabe (Fakten aus den XML):** Bei allen 7 gefundenen Fällen schließt der Testfall an Grundlaufzeit oder Höchstende an;
keine vorzeitige Neuvergabe nach Definition. Bekanntes Ende: T48 (31.10.2026, Grundlaufzeit), T52 (Höchstende 31.12.2026), T53 (Los 6 31.12.2026,
Los 1 30.04.2027, Los 7 31.05.2027), T55 (Höchstende 31.01.2027), T57 (Höchstende 31.12.2027; Neuvergabe 12 Monate vor Höchstende, aber nach der
Grundlaufzeit). Rollierend ohne Höchstdauer: T56, T59 (Vertragsende unbekannt).

**Auffälligkeiten (Fakten)**
- Namenswechsel: T55 „Netz Lübeck GmbH“ (2018/2019) → „TraveNetz GmbH“; T54 „Staatliches Baumanagement Ems-Weser“ (2020) → „Staatliches Baumanagement
  Region Nord-West“; T56 Zuschlag unter „Oberlandesgericht Nürnberg“, Ausschreibung unter „Präsident des Landgerichts Amberg“; T60 früher „Eigenbetrieb
  Zentrales Gebäude- und Liegenschaftsmanagement“, jetzt „Stadt Brandenburg an der Havel“; T46 „Amt für Organisation, IT und Zentrale Leistungen“ →
  „Amt für Zentrale Leistungen“.
- Zentrale Vergabestellen: T54 (Staatliches Baumanagement für die Universität Oldenburg); bei T47 wurden auch BImA-Verfahren geprüft (nur DAI München).
- Leistungsart-Grenzfall T54: Die Liegenschaften sind auf TED gut sichtbar (Unterhaltsreinigung 2020 und 2025), eine frühere Glasreinigung aber nicht.
- Auftraggeber ohne Objektnamen (Bocholt T51/T58, Brandenburg a. d. H. T60, Dußlingen T50, Bielefelder Bündel 2022–2025 bei T46) sind die Ursache aller
  fünf „unklar“-Fälle.
- Neuzuschnitte: T52 (3 Mensen → 1 Mensa), T53 (Stadtteil-Einzelverträge → 9-Lose-Bündel), T59 (Bündel 2019 teilweise übernommen).
- T51 folgt zwei Monate auf ein Verfahren mit identischer Los-Bezeichnung (483870-2026); T58 übernimmt die Beschreibung der Objektgruppe 2 wörtlich.

**Einschätzungen (keine Fakten)**
- T50 und T60 sind mit hoher Wahrscheinlichkeit echte Vorgänger (gleiche Sammelbezeichnung, Anschlusstermin). Würde man „unklar mit Anschlusstermin“ als
  gefunden werten, stiege die Quote in Teil 4 auf 9 von 15.
- T51 ist wahrscheinlich eine Wiederholung von Los 3 aus 483870-2026, also kein ausgelaufener Vertrag; für eine Laufzeitprognose wäre das kein brauchbares Paar.
- T47 (kein_vorgaenger) ist unsicher, weil der Testfall seine Objekte nur in einer Anlage nennt.
- Eine Regel, die nur Objekte vergleicht, würde bei T54 einen Vorgänger melden, der nach Definition keiner ist.

**Werkzeuge und Daten**
- Netzwerk: Zwei API-Abfragen scheiterten an einem DNS-Fehler und ein XML-Abruf an einem Verbindungsabbruch; dabei wurden keine Dateien geschrieben,
  die Abrufe wurden danach wiederholt (diese Fehlversuche sind nicht gezählt). Eine Verbindungsprobe per `curl` (nur Statuscode, nicht gespeichert) ist
  ebenfalls nicht gezählt.
- FT-Kontrolle: in allen Fällen mit API-Abfrage erfolgreich. Ausnahme ohne Folgen: `FT=Podbielskiallee` (T47) fand den Testfall nicht; die Ursache wurde
  nicht geprüft (vermutlich steht die Adresse nicht im Testfall).
- Lokale Muster mit Teilstrings sind unscharf: „amberg“ trifft „Bamberg“ (T56), PLZ „22113“ trifft Hamburg (T57).
- eForms-Zuschläge tragen teils das Platzhalter-Datum „AwardDate 2000-01-01“ (z. B. 503868-2026, 255653-2026).
