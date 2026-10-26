# Sichtbarkeit der Vorgänger – Handsuche Iteration 4, Teil 3 (U29–U42)

- **Datum:** 2026-10-25
- **Bearbeiter:** Subagent `rechercheur` (Auftrag „Handsuche“)
- **Testfälle:** Zeilen 29–42 aus `reports/testfaelle_iteration4.txt` (U29–U42 in dieser Reihenfolge): 135556-2026, 112103-2026,
  195153-2026, 164478-2026, 161174-2026, 199877-2026, 195060-2026, 36379-2026, 150041-2026, 173541-2026, 183269-2026, 108283-2026,
  34825-2026, 187770-2026. Titel und Auftraggeber laut `reports/testfaelle_iteration4.md`.
- **Definitionen:** Kategorien nach `reports/urteilsregeln_blindpruefung.md` **Version 1.1** (vor dem ersten Fall vollständig gelesen,
  einschließlich der Kalibrierungsbeispiele); Begriffe nach `docs/iterationen.md`, Abschnitt „Iteration 4“. Ergebnis je Fall:
  `objektgleich_hoch` | `objektgleich_mittel` | `teilmenge` | `unklar` (mit Tendenz) | `kein_vorgaenger`.
  Vorgänger-Quellen: Zuschläge (`form-type=result`) und frühere Ausschreibungen (`form-type=competition`) auf TED mit CPV 909…,
  veröffentlicht ab 01.10.2016 und vor dem Testfall. Zeitabstand, Vertragsende, Laufzeit und Auftragswert fließen nicht ins Urteil ein
  (auch nicht in die Tendenz); das Vorgänger-Ende wird erst **nach** dem Urteil und getrennt davon notiert.
- **Unabhängigkeit:** Ich bestätige, dass ich keine der ausgeschlossenen Dateien gelesen habe (insbesondere nicht `src/zuordnung_*.py`,
  `src/objekt_merkmale.py`, `src/los_merkmale.py`, `src/testprobe_iteration4.py`, `data/processed/`, `data/raw/ted_ft/`,
  `reports/zuordnung_*`, `reports/k2_*`, `reports/blindpruefung_*`, `reports/regel_entwicklung_*`, `reports/evaluation_*`,
  `reports/sichtbarkeit_iteration3_*`, `reports/testfaelle_iteration3*`, `reports/dev_gesehene_q1_notices.txt`,
  `reports/bekannte_notices_iteration4.txt`, `reports/vorgaenger_ende_iteration3_korrektur.csv`, `reports/sichtbarkeit_iteration4_teil1.md`
  und `_teil2.md`). Gelesen wurden nur die Urteilsregeln, `docs/iterationen.md` (Iteration 4), die Testfallliste, die erlaubten Rohdaten unter
  `data/raw/ted_search/`, die TED-API und die TED-XML. Von den Ordnern unter `data/raw/rechercheur_20261025/` anderer Teile habe ich nur
  die Dateiliste von U1 angesehen (Ablageschema), keinen Inhalt.

## Vorgehen und Konventionen

- **Lokale Vorsuche (nicht im API-Budget):** Die erlaubten Rohdaten (`DEU_result_cpv909_20161001_20260930`,
  `DEU_competition_cpv909_20161001_20260930`, die beiden `_lostext`-Ordner der eForms-Zeit und der Testfall-Ordner) wurden in einen
  Index geladen (35.150 Notices) und nach Auftraggebername, Ort, Titel/Lostitel/Beschreibung/Straße gefiltert, immer mit Veröffentlichung
  ab 20161001 und vor dem Testfalldatum. Das ist inhaltlich Suche A/B über bereits gespeicherte API-Antworten (CPV 909…). Diese
  lokalen Filter werden im Protokoll als „lokal:“ genannt und **nicht** auf das Budget von 15 API-Abfragen angerechnet.
- **API-Abfragen** (TED Search API v3) sind nummeriert; Anfrage und Antwort liegen unverändert unter
  `data/raw/rechercheur_20261025/[U-Nr]/api_[NN]_request.json` und `api_[NN].json`. Alle Abfragen enthalten
  `classification-cpv=909* AND publication-date>=20161001 AND publication-date` kleiner als das Testfalldatum (unten abgekürzt mit „+ Std.“).
- **XML:** jede geöffnete XML liegt unter `data/raw/rechercheur_20261025/[U-Nr]/[Notice].xml`. Die XML des Testfalls selbst wird
  **mitgezählt** (vorsichtige Zählung); die Zahl „XML“ unter „Abfragen/XML“ enthält sie also.
- **Volltext:** Mehrere Begriffe werden als `(FT~"a" OR FT~"b")` verknüpft. Die Volltextsuche erfasst nach Probe (U29, Abfrage 04:
  `FT~"Bendastraße"` findet die Bekanntmachung 39575-2020 vor eForms) auch Bekanntmachungen vor eForms.
- **Einzelstandort:** Die Adresse allein zählt nicht als A-Merkmal (Urteilsregeln, Abschnitt Einzelstandorte).
- **Vorgänger-Ende** wird aus dem Vorgänger **mit Vertrag** abgeleitet; vor eForms stehen Laufzeiten nur in der Auftragsbekanntmachung
  (II.2.7), daher wird dafür die zum Zuschlag gehörende Auftragsbekanntmachung herangezogen (über „NOTICE_NUMBER_OJ“ im Zuschlag).
- Fakten stehen mit Notice-Nummer und Zitat; Einschätzungen sind als solche gekennzeichnet („Einschätzung:“).

## Fälle

### U29 – 135556-2026 (2026-02-26) – Stadtverwaltung Gotha
- Objekt(e): „Los 18 - Staatliche Grundschule Gotha Siebleben“ (Schulgebäude/Nebengebäude, Sport-/Turnhallen); Ort Gotha, PLZ 99867;
  keine Straße, keine Fläche angegeben. Die Bekanntmachung enthält nur dieses eine Los (LOT-0001), interne Kennung VgV-OV-51/26/054.
- Leistungsart (je Los): Unterhaltsreinigung, Grundreinigung (in den Ferien), Glasreinigung (in den Ferien) in einem Los; CPV 90911200.
- Suchschritte:
  - lokal: Auftraggeber `gotha` (alle Gotha-Auftraggeber), vor 20260226: 71 Treffer (Stadtverwaltung Gotha, Landkreis/Landratsamt Gotha,
    Friedenstein Stiftung). Stadtverwaltung Gotha vor eForms: 2020 (39575/39577/39583/39585/39586-2020, Zuschläge 169146/169206/169207/
    169208/169212-2020), 2021 (216413-2021, CPV 85312100+90911200), 2022/23 (707246-2022, 709051-2022, 95149-2023, 95264-2023, Zuschläge
    45556-2023, 46846-2023, 307579-2023, 308907-2023); eForms: 29196-2025 (Küche Kindergärten), 758285…761968-2025 (Los 1–8:
    Kindergärten, Stadtbibliothek, Rathaus, Öffentliche Toiletten).
  - API 01: `FT~"Siebleben"` + Std. → 1 Treffer (760117-2025, Stadtverwaltung Gotha, „Los 2 – Neues Rathaus und weitere Objekte“).
  - API 02: `buyer-name~"Gotha"` + Std. → 74 Treffer (deckt sich mit der lokalen Liste, zusätzlich 3 Berichtigungen des Landratsamts).
  - API 03: `FT~"Grundschule" AND buyer-name~"Stadtverwaltung Gotha"` + Std. → 0 Treffer.
  - API 04: `FT~"Bendastraße" AND buyer-name~"Gotha"` + Std. → 2 Treffer (39575-2020, 169146-2020); Probe, ob FT vor eForms greift.
  - API 05: `FT~"Grundschule" AND buyer-name~"Gotha"` + Std. → 17 Treffer, alle Landkreis/Landratsamt Gotha (2018–2023) und 125780-2026.
  - XML geöffnet: 135556-2026 (Testfall), 39575-2020, 707246-2022, 95149-2023, 23280-2018, 124668-2019.
  - lokal (eForms-Beschreibungen): 103862-2024 / 320553-2024, 142713-2025 / 409434-2025 und 125780-2026 (Landkreis Gotha, Schulen) gelesen.
- Geprüfte Kandidaten (Fakten):
  - Stadtverwaltung Gotha 2020/2022/2023: 39575-2020 „Kita „Sonnenblume“, Bendastraße in Gotha“, „Unterhaltsreinigung und Tagesfrau“;
    707246-2022 und 95149-2023 „Unterhaltsreinigung und Serviceleistung Tagesfrau mit Küche“, 95149-2023 „Los 1 - Kindergarten
    „Sternenzauber“, Gotha“ → Objektart Kindergarten, nicht Schule.
  - 760117-2025: nennt „Trauerhalle Siebleben, Högernweg 13“ unter städtischen Verwaltungs-/Friedhofsobjekten → andere Objektart.
  - Landkreis Gotha (Schulträger der übrigen Schulen): 23280-2018 „Grundschule Dachwig, … Regelschule Molschleben“; 124668-2019 „Grundschule
    Goldbach, … Grundschule Mechterstädt …“; 103862-2024 Gymnasien, KGS, Berufsschulen, Förderzentren in Gotha; 142713-2025 Schulen mit
    Adressliste (Ohrdruf, Georgenthal, Tambach-Dietharz, Gotha 18.-März-Str. 50, Emminghausstr. 8, …); 125780-2026 BSZ „Hugo Mairich“,
    Dachwig, Großfahner, … Keiner nennt „Siebleben“ (API 01 findet keinen dieser Notices).
- A (Identität): nicht vergleichbar  Details: Der Testfall nennt nur den Schulnamen; kein Kandidat nennt die Grundschule Siebleben.
- B (Objektraum): widersprüchlich (für alle geprüften Kandidaten)  Details: Stadt-Gotha-Kandidaten sind Kindergärten bzw. Verwaltungs-/
  Friedhofsgebäude (andere Objektart); Landkreis-Kandidaten nennen namentlich andere Schulen (andere Objekte).
- C (Stütze): Auftraggeber ja (Stadtverwaltung Gotha bei den Kita-Verfahren), CPV ja (90911200), Titel anders, Losstruktur anders
  (Testfall: ein Los je Bekanntmachung, Los-Nr. 18).
- Überschneidung der Objekte: 0 von 1 (bei allen Kandidaten mit Objektliste).
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: Testfall 135556-2026, `ProcurementProject/Name`: „Los 18 - Staatliche Grundschule Gotha Siebleben“; `FT~"Siebleben"` (API 01)
  liefert vor dem Testfall nur 760117-2025 mit „Trauerhalle Siebleben, Högernweg 13“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 5/6
- Einschätzung (nicht Teil des Urteils): Die Stadt Gotha schreibt Schulen auf TED offenbar erstmals aus; frühere Verfahren der Stadt
  betrafen Kindergärten. Ob die Grundschule zuvor national oder in einem Landkreis-Verfahren ohne Nennung des Ortsteils vergeben wurde,
  lässt sich aus TED nicht belegen.

### U30 – 112103-2026 (2026-02-17) – Bundesanstalt für Immobilienaufgaben
- Objekt(e): Bundesanstalt für Arbeitsschutz und Arbeitsmedizin (BAuA), Fabricestr. 8, 01099 Dresden (Einzelstandort). Los 1:
  „2.982,16 m² Grundfläche, 260.671,35 jährl. Reinigungsfläche“; Los 2: „842,61 m² Glasfläche, 2.048,60 m² jährl. Reinigungsfläche“.
  Kennung VOEK 667-25.
- Leistungsart (je Los): Los 1 Unterhaltsreinigung (+ Grund-/Intensivreinigung, Bedarf); Los 2 Glasreinigung (+ Jalousien, Bedarf).
- Suchschritte:
  - lokal: Auftraggeber `Arbeitsschutz` → 13 Treffer (BAuA Dortmund 82377-2022, 581073-2023, 154428-2024 „… in Berlin“; LUA Saarland);
    Text `Arbeitsschutz|Fabrice` → 36 Treffer, nur über allgemeinen Text, kein BAuA Dresden in eForms.
  - API 01: `(FT~"Fabricestr" OR FT~"Fabricestraße")` + Std. → 5 Treffer (104121-2020, 146410-2020 Berichtigung, 265170-2020 Zuschlag,
    alle BImA; 548299-2023 und 772361-2023 Landeshauptstadt Dresden, Schulen „SB Neustadt“).
  - API 02: `FT~"Arbeitsschutz und Arbeitsmedizin"` + Std. → 11 Treffer (u. a. 479091-2019 / 92987-2020 BImA für BAuA Berlin,
    104121-2020, 265170-2020, 82377-2022, 581073-2023, 154428-2024).
  - XML geöffnet: 112103-2026 (Testfall), 104121-2020, 479091-2019, 265170-2020.
- Geprüfte Kandidaten: 479091-2019 betrifft „Nöldnerstraße 40-42, 10317 Berlin“ → andere Adresse/Stadt, nicht objektgleich.
  548299-2023/772361-2023 (Stadt Dresden, Schulen) → andere Objektart, nicht objektgleich.
- A (Identität): abweichend  Details: Adresse gleich (104121-2020: „WE 144365 Bundesanstalt für Arbeitsschutz und Arbeitsmedizin,
  Fabricestraße 8, 01099 Dresden“), zählt beim Einzelstandort nicht allein. Flächen gleicher Art: Unterhalt Grundfläche 2.913,10 m²
  (2020) gegenüber 2.982,16 m² (2026) = plus 2,4 % (abweichend, knapp über 2 %); Jahresreinigungsfläche 299.680,18 gegenüber
  260.671,35 m² (minus 13 %); Glas-Grundfläche 1.184,95 gegenüber 842,61 m² Glasfläche (abweichend). Kein Widerspruch.
- B (Objektraum): erkennbar und übereinstimmend  Details: Dresden-Neustadt (01099), Bundesbehörde/Dienstgebäude BAuA, Unterhalts- und
  Glasreinigung in zwei getrennten Losen auf beiden Seiten.
- C (Stütze): Auftraggeber ja (BImA), CPV ja (90911200), Titel ähnlich („Offenes Verfahren (EU-weit) zur Vergabe von
  Gebäudereinigungsleistungen (Unterhalts- und Glasreinigungsleistungen) für …“), Losstruktur gleich (Los 1 Unterhalt, Los 2 Glas).
- Überschneidung der Objekte: 1 von 1 (ein Objekt je Seite).
- Ergebnis: **objektgleich_mittel** (Flächen abweichend, Adresse beim Einzelstandort allein, daher kein „hoch“)
- Tendenz (nur bei unklar): –
- Vorgänger: 265170-2020 (Zuschlag, vor eForms, 2020-06-08); weitere Notices desselben Vorgängers: 104121-2020 (Ausschreibung, vor
  eForms, 2020-03-03), 146410-2020 (Berichtigung, 2020-03-26, nicht geöffnet).
- Beleg: 104121-2020, II.1.4: „Los 1: Unterhaltsreinigungsleistungen: — WE 144365 Bundesanstalt für Arbeitsschutz und Arbeitsmedizin,
  Fabricestraße 8, 01099 Dresden, — 2 913,10 qm Grundfläche“; Testfall: „Fabricestr. 8, 01099 Dresden“, „2.982,16 m² Grundfläche“.
- Vorgänger mit Vertrag: 265170-2020 (Zuschlag beider Lose, Vertragsschluss 2020-05-26; Laufzeit aus 104121-2020)
- Vorgänger-Ende: 2026-10-31; Herkunft: **hoechstende** (104121-2020, II.2.7: Grundlaufzeit 2020-11-01 bis 2024-10-31, jährliche
  Verlängerung, „Der Vertrag endet spätestens am 31.10.2026“). Grundlaufzeit-Ende 2024-10-31.
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-11-01 liegt nach dem Ende der Grundlaufzeit).
- Abfragen/XML: 2/4

### U31 – 195153-2026 (2026-03-20) – Land Berlin – Sondervermögen Immobilien des Landes Berlin (SILB) c/o BIM
- Objekt(e): keine Objektliste in der Bekanntmachung. Gesamtbeschreibung: „Unterhalts-, Grund-, Glas- und Sondereinigungen im Segment
  Polizei-, Justiz- und Verwaltungsgebäuden und sonst. Dienststellen (Lose 1-11; 67 Liegenschaften) sowie im Segment Berliner Feuerwehr
  (Los 12-19; 76 Liegenschaften) im Berliner Stadtgebiet in 19 Losen (Gesamt 143 Liegenschaften)“. Lose 1–11: „diverse Liegenschaften
  zum Segment Polizei-, Justiz- und Verwaltungsgebäuden und sonst. Dienststellen im gesamten Berliner Stadtgebiet“; Lose 12–19: „diverse
  Liegenschaften zum Segment Feuerwehr“. Keine Flächen, keine Adressen (Ort je Los „Siehe EVB“). Kennung EKP-VA-26-01104.
- Leistungsart (je Los): alle 19 Lose Unterhalts-, Grund- und Sonderreinigung sowie Glas-/Rahmenreinigung (kombiniert).
- Suchschritte:
  - lokal: Auftraggeber `SILB|BIM Berliner|Sondervermögen Immobilien|Berliner Immobilienmanagement` vor 20260320 → 115 Notices
    (2016–2026). Davon eForms mit passendem Titel: 766765-2023 / 279714-2024 („Reinigungs- und Pflegedienste - Unterhalts-, Glas-, Grund-
    und Sonderreinigung“, 15 Lose, „Segment Polizei-, Justiz- und Verwaltungsgebäuden“), 115580-2024 / 484673-2024 („… FW Nord-Ost“).
  - API 01: `FT~"Feuerwehr" AND (buyer-name~"Sondervermögen" OR buyer-name~"BIM")` + Std. → 30 Treffer (u. a. 11778-2019/240337-2019,
    55109-2022, 99015-2022, 195952-2022, 507117-2022, 115580-2024, 82229-2026 Vertragsänderung).
  - API 02: `FT~"Justiz" AND (buyer-name~"Sondervermögen" OR buyer-name~"BIM")` + Std. → 25 Treffer (u. a. 195952-2022, 507117-2022,
    766765-2023, 279714-2024, Vertragsänderungen 537457/542806/741435-2025, 82229-2026).
  - API 03: `FT~"Segment Feuerwehr"` (ohne CPV-Filter) + Datum → 5 Treffer (55109-2022, 99015-2022, 195952-2022, 507117-2022, 82229-2026).
  - XML geöffnet: 195153-2026 (Testfall), 766765-2023, 82229-2026 (Vertragsänderung, nur als Wegweiser; verweist auf
    „ChangedNoticeIdentifier: 052661-2022“ und den Titel „Unterhalts-, Grund-, Glas- und Rahmenreinigung zum Segment Feuerwehr sowie
    Polizei-, Justiz- und Verwaltungsgebäuden …“), 195952-2022, 507117-2022.
- Bester Kandidat: 195952-2022 (Ausschreibung, vor eForms, 2022-04-13) mit Zuschlag 507117-2022 (2022-09-16, „NOTICE_NUMBER_OJ:
  2022/S 073-195952“, Vertragsschluss 2022-09-07, 20 Lose), Az. EKP-VA-22-01820.
- A (Identität): mehrdeutig  Details: Keine Seite nennt eine Objektliste (2022 nur zwei Besichtigungsobjekte „WE 30218 - Tempelhofer
  Damm 12 (Los 1)“ und „WE 30168 - Nikolaus-Groß-Weg 2 (Los 15)“; der Testfall nennt keine). Gebäudezahl: Segment Polizei/Justiz/Verwaltung
  2022 „Lose 1-14=67 Liegenschaften“, 2026 „Lose 1-11; 67 Liegenschaften“ (gleich); Segment Feuerwehr 2022 „72 Liegenschaften … Los
  15-19“, 2026 „76 Liegenschaften“ (abweichend); 2022 zusätzlich „11 WE mit ausschl. Leistungen zur Glasreinigung (Los 20)“. Flächen nur
  2022 (ca. 520.000 m² Unterhalt, ca. 148.000 m² Glas), im Testfall keine.
- B (Objektraum): nicht erkennbar  Details: Gebiet (gesamtes Berliner Stadtgebiet) und Leistungsart (Unterhalt, Grund, Glas, Sonder)
  stimmen überein. Die Objektart ist auf beiden Seiten ein Bündel „diverse Liegenschaften“ verschiedener Arten (Polizei, Justiz,
  Verwaltung, „sonst. Dienststellen“, Feuerwehr) eines Landes-Auftraggebers mit vielen Gebäudearten; nach den Urteilsregeln gilt das als
  nicht erkennbar. Dass dasselbe Segment auch in einem Schwesterverfahren vorkommt (766765-2023, 15 Lose, „Segment Polizei-, Justiz- und
  Verwaltungsgebäuden“), zeigt, dass die Segmentangabe allein das Objektbündel nicht festlegt.
- C (Stütze): Auftraggeber ja (BIM für SILB/Liegenschaftsfonds/SODA), CPV ja (90910000), Titel ähnlich, Losstruktur anders (20 Lose mit
  reinem Glaslos gegenüber 19 Losen; Segmentgrenzen 1–14/15–19 gegenüber 1–11/12–19), Zuschlagslimitierung ähnlich (2022 „LOT_MAX_ONE_TENDERER:
  7“, 2026 „max. 7 Lose“).
- Überschneidung der Objekte: nicht bestimmbar (keine Listen).
- Weitere geprüfte Kandidaten: 766765-2023 / 279714-2024 (Schwesterverfahren desselben Segments, keine Objektliste, keine Gebäudezahl
  in der XML; beide Seiten unspezifisch → höchstens unklar, schwächer belegt als 195952-2022); 115580-2024 (nur Feuerwehr Nord-Ost,
  einzelnes Teilgebiet).
- Ergebnis: **unklar**
- Tendenz (nur bei unklar): **eher dafür** – gleiche Segmentbeschreibung und gleiche Zahl von 67 Liegenschaften im Segment Polizei/Justiz/
  Verwaltung, gleicher Auftraggeber und gleiche Zuschlagslimitierung; dagegen spricht die abweichende Zahl im Segment Feuerwehr (72 zu 76)
  und das Schwesterverfahren 766765-2023 mit demselben Segment.
- Vorgänger (Kandidat): 195952-2022 (competition, vor eForms, 2022-04-13) und 507117-2022 (result, vor eForms, 2022-09-16);
  Vertragsänderung 82229-2026 (2026-02-04, außerhalb der Vorgänger-Quellen, nur Hinweis). 55109-2022 / 99015-2022 (Feb. 2022, gleicher
  Auftraggeber, von API 03 gefunden) nicht geöffnet.
- Beleg: 195952-2022, II.1.4: „Lose 1-14=67 Liegenschaften, 72 Liegenschaften des Segments Berliner Feuerwehr=Los 15-19 sowie 11 WE mit
  ausschl. Leistungen zur Glasreinigung (Los 20)“; Testfall: „(Lose 1-11; 67 Liegenschaften) … (Los 12-19; 76 Liegenschaften)“.
- Vorgänger mit Vertrag: 507117-2022 (Zuschlag aller 20 Lose; Laufzeiten aus 195952-2022)
- Vorgänger-Ende: Grundlaufzeit je Los 2026-10-31 (13 Lose), 2026-11-30 (4 Lose) bzw. 2026-12-31 (3 Lose); Herkunft: **grundlaufzeit**
  (195952-2022, II.2.7; danach Verlängerung „um jeweils 3 Monate“ ohne Höchstdauer, also rollierend). Vertragsänderung 82229-2026 nennt
  für die Verträge „PlannedPeriod … EndDate: 2026-12-31“.
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-11-01).
- Abfragen/XML: 3/5

### U32 – 164478-2026 (2026-03-10) – Bundesanstalt für Immobilienaufgaben
- Objekt(e): „HZA Dresden, Weststr. 16, 02708 Löbau“ (Hauptzollamt, Einzelstandort); „Unterhaltsreinigung: 2.460,69 m² Grundfläche,
  251.915,00 m² jährl. Reinigungsfläche“, „Glasreinigung: 381,32 m² Glasfläche, 762,64 m² jährliche Reinigungsfläche“. Ein Los, VOEK 670-25.
- Leistungsart (je Los): ein Los mit Unterhaltsreinigung, Grund-/Intensivreinigung, Bedarf und Glasreinigung.
- Suchschritte:
  - lokal: Text `Löbau|Weststr` → 11 Treffer, Ort `Löbau` → 7 Treffer (Landkreis Görlitz „Standort Löbau“ 604206-2025/10154-2026,
    SachsenEnergie, BA Glasreinigung RIM Chemnitz); kein BImA-Treffer in eForms.
  - API 01: `FT~"Löbau" AND (FT~"Weststr" OR FT~"Weststraße" OR FT~"Hauptzollamt" OR FT~"HZA")` + Std. → 2 Treffer (480055-2020,
    151676-2021, beide BImA).
  - API 02: `FT~"Löbau" AND buyer-name~"Immobilienaufgaben"` + Std. → 4 Treffer (480055-2020, 575359-2020, 138612-2021, 151676-2021).
  - XML geöffnet: 164478-2026 (Testfall), 480055-2020, 575359-2020, 151676-2021.
- Geprüfte Kandidaten: 575359-2020 (BImA, „Dienstgebäude der BImA, Wilhelm-Leuschner-Platz 4“ und „Fortbildungsstätte,
  James-von-Moltke-Str. 8“, Löbau) → andere Adressen, nicht objektgleich. Landkreis Görlitz „Standort Löbau“ (anderer Auftraggeber,
  Landratsamts-Standort) → nicht als Kandidat gewertet, da keine Übereinstimmung mit der Weststr. 16 belegt.
- A (Identität): übereinstimmend (für das gemeinsame Objekt)  Details: 480055-2020, Los 2: „WE 105519, Hauptzollamt Dresden,
  Arbeitsgebiet Löbau, Weststr. 16, 02708 Löbau, 2 449,23 qm Grundfläche 250 714,65 qm Jahresreinigungsfläche Unterhaltsreinigung,
  378,52 qm Grundfläche 1 514,08 qm Jahresreinigungsfläche Glasreinigung“. Unterhalt-Grundfläche 2.449,23 zu 2.460,69 m² (0,5 %),
  Glas-Grundfläche 378,52 zu 381,32 m² (0,7 %), Jahresreinigungsfläche Unterhalt 250.714,65 zu 251.915,00 m² (0,5 %) → gleich
  (Einzelstandort: Adresse allein zählt nicht, aber zwei Flächenarten stimmen überein).
- B (Objektraum): erkennbar und übereinstimmend  Details: Löbau, Dienstgebäude des Hauptzollamts Dresden, Unterhalts- mit Glasreinigung.
- C (Stütze): Auftraggeber ja (BImA), CPV ja (90911200/90911300), Titel ähnlich, Losstruktur anders (2020: zwei Lose mit zusammen fünf
  Liegenschaften; Löbau gemeinsam mit Bautzen in Los 2).
- Überschneidung der Objekte: 1 von 1 (kürzere Seite = Testfall); auf der längeren Seite (480055-2020, Los 2) 1 von 2 (Bautzen,
  Käthe-Kollwitz-Str. 15, zusätzlich), bezogen auf die ganze Bekanntmachung 1 von 5.
- Ergebnis: **teilmenge** (Testfall-Objekt vollständig und mit gleichen Flächen in Los 2 von 480055-2020 enthalten; die längere Seite
  enthält zusätzlich WE 142603 Bautzen; nichts ausdrücklich ausgeschlossen)
- Tendenz (nur bei unklar): –
- Vorgänger: 151676-2021 (Zuschlag, vor eForms, 2021-03-26, Los 2: „Veolia Gebäudeservice Deutschland GmbH“, Vertragsschluss 2021-03-22);
  weitere Notice desselben Vorgängers: 480055-2020 (Ausschreibung, vor eForms, 2020-10-12, VOEK 260-20).
- Beleg: 480055-2020, II.2.4 Los 2: „WE 105519, Hauptzollamt Dresden, Arbeitsgebiet Löbau, Weststr. 16, 02708 Löbau, 2 449,23 qm
  Grundfläche“; Testfall: „HZA Dresden, Weststr. 16, 02708 Löbau“, „2.460,69 m² Grundfläche“.
- Vorgänger mit Vertrag: 151676-2021 (Laufzeit aus 480055-2020)
- Vorgänger-Ende: 2027-03-31; Herkunft: **hoechstende** (480055-2020, Los 2: Grundlaufzeit 2021-04-01 bis 2025-03-31, jährliche
  Verlängerung, „Der Vertrag endet spätestens am 31.3.2027“). Grundlaufzeit-Ende 2025-03-31.
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2027-04-01).
- Abfragen/XML: 2/4

### U33 – 161174-2026 (2026-03-09) – Stadtwerke Speyer GmbH
- Objekt(e): nicht genannt. Gesamtbeschreibung nur „Unterhalts- und Glasreinigung“; kein Leistungsort je Los, keine Fläche, keine
  Adresse außer der des Auftraggebers (Georg-Peter-Süß-Str. 2, 67346 Speyer). Interne Kennung E24352238.
- Leistungsart (je Los): Los 1 „Reinigungsleistung Unterhaltsreinigung“; Los 2 „Reinigungsleistung Glasreinigung“.
- Suchschritte:
  - lokal: Auftraggeber `Speyer` → 6 Treffer (Speyer-Haus Frankfurt, Universität für Verwaltungswissenschaften, Entsorgungsbetriebe
    Speyer), Ort `Speyer` → 16 Treffer; kein Treffer der Stadtwerke Speyer.
  - API 01: `buyer-name~"Stadtwerke Speyer"` + Std. → 0 Treffer.
  - API 02: `FT~"Stadtwerke Speyer"` + Std. → 0 Treffer.
  - API 03: `buyer-name~"Stadtwerke Speyer"` ohne CPV-Filter (Datum wie Std.) → 7 Treffer, alle andere CPV (34144511, 90420000, 90514000,
    48214000, 72200000) → außerhalb des Protokolls (anderer CPV), nicht gewertet.
  - API 04: `(FT~"Georg-Peter-Süß" OR FT~"bademaxx")` + Std. → 1 Treffer (553186-2024, Entsorgungsbetriebe Speyer,
    „Schadnagerbekämpfung“, CPV 90922000).
  - XML geöffnet: 161174-2026 (Testfall).
- A (Identität): nicht vergleichbar  Details: kein Kandidat mit Reinigungsleistung der Stadtwerke Speyer.
- B (Objektraum): nicht erkennbar (Testfall)  Details: Objektart und Leistungsort fehlen im Testfall; einziger Treffer 553186-2024 hat
  eine andere Leistungsart (Schädlingsbekämpfung) und einen anderen Auftraggeber.
- C (Stütze): –
- Überschneidung der Objekte: –
- Ergebnis: **kein_vorgaenger** (kein Kandidat gefunden, der als objektgleich, Teilmenge oder unklar in Frage kommt)
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: API 01 `buyer-name~"Stadtwerke Speyer" AND classification-cpv=909*` liefert vor 2026-03-09 „totalNoticeCount 0“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 4/1

### U34 – 199877-2026 (2026-03-23) – Bundesagentur für Arbeit (BA), Geschäftsbereich Einkauf
- Objekt(e): „Reinigung von Rechenzentren (RZ) an drei Standorten im Stadtgebiet Nürnberg“ (IT-Systemhaus der BA), „Feinstaubreinigung
  von 700 Serverschränken“; keine Adressen, keine Flächen. Kennung 13-25-00433, ein Los (LOT-0000).
- Leistungsart (je Los): Spezialreinigung Rechenzentrum (jährliche Komplettreinigung mit Doppelboden-/Hohlraum- und Deckenreinigung
  nach DIN EN ISO 14644-1 Kl. 8, monatliche Bodenreinigung), im Titel „UHR“; CPV 90910000.
- Suchschritte:
  - lokal: Text `Rechenzentr|Serverschr|IT-Systemhaus|Doppelboden` vor 20260323 → 25 Treffer, keiner der BA (u. a. ITDZ Berlin
    „Spezialreinigung RZ“, RZF NRW Kaarst, Leibniz-Rechenzentrum Garching); Auftraggeber BA mit Text `Nürnberg|Rechenz|IT-` → 8 Treffer
    („Unterhaltsreinigung RIM Nürnberg“ 88488/127349/141870/164961-2024, Zuschlag 760791-2024; „Glas- und Rahmenreinigung RIM Nürnberg“
    16694/86897-2024, Zuschlag 286868-2024), keiner erwähnt Rechenzentren.
  - API 01: `(FT~"Rechenzentren" OR FT~"Rechenzentrum" OR FT~"Rechenzentrumsreinigung") AND buyer-name~"Bundesagentur für Arbeit"`
    + Std. → 0 Treffer.
  - API 02: `(FT~"IT-Systemhaus" OR FT~"Serverschränke" OR FT~"Rechenzentrumsreinigung")` + Std. → 2 Treffer (Flughafen Berlin
    Brandenburg 145608-2018 / 533519-2018).
  - API 03: `(FT~"Rechenzentrum" OR FT~"Rechenzentren") AND buyer-city="Nürnberg"` + Std. → 2 Treffer (TH Nürnberg 350277-2022 /
    492732-2022).
  - XML geöffnet: 199877-2026 (Testfall).
- A (Identität): nicht vergleichbar  Details: kein Kandidat nennt die Rechenzentren der BA.
- B (Objektraum): widersprüchlich (für alle Treffer)  Details: BA „RIM Nürnberg“ betrifft Dienststellen der Region (Unterhalts- bzw.
  Glasreinigung, andere Objektart); Flughafen BER, TH Nürnberg, ITDZ Berlin usw. sind andere Auftraggeber und andere Objekte.
- C (Stütze): –
- Überschneidung der Objekte: –
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: API 01 (`FT~"Rechenzentren" …` mit Auftraggeber BA) liefert „totalNoticeCount 0“; Testfall: „Reinigung von Rechenzentren (RZ)
  an drei Standorten im Stadtgebiet Nürnberg“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 3/1

### U35 – 195060-2026 (2026-03-20) – Bezirksamt Charlottenburg-Wilmersdorf von Berlin
- Objekt(e): 24 Lose, je ein Objekt mit Adresse und Reinigungsfläche: 1 Dienstgebäude Heerstraße (Heerstr. 12/14, 662,10 m²),
  2 Dienstgebäude Hohenzollerndamm (174-177, 21.106,65 m²), 3 Dietrich-Bonhoeffer-Bibliothek (Brandenburgische Str. 2, 5.036,03 m²),
  4 Familienzentrum guk (Düsseldorfer Str. 3), 5 Gretel-Bergmann-Sporthalle (Rudolstädter Str. 77, 2.333,56 m²), 6 Hans-Rosenthal-
  Sportanlage (Kühler Weg 12), 7 Haus der Jugend Anne Frank (Mecklenburgische Str. 15), 8 Hubertus-Sportplatz (Hubertusallee 50),
  9 Jugendfreizeitheim Heckerdamm (Heckerdamm 210), 10 Jugendfreizeitheim Plöner Straße, 11 Jugendfreizeitheim Spirale (Wesfälische
  Str. 16 a), 12 Musikschule Prinzregentenstraße (Prinzregentenstr. 72), 13 Rathaus Charlottenburg (Otto-Suhr-Allee 100, 30.030,04 m²),
  14 Seniorenclub Wallotstraße, 15 Spielhaus Schillerstraße, 16 Sportanlage Am Volkspark, 17 Sportanlage Jungfernheide, 18 Sporthalle
  Emser Straße, 19 Sportplatz Im Jagen, 20 Stadtteilzentrum Halemweg, 21 Standesamt Alt-Lietzow, 22 Abenteuerspielplatz Holsteinische
  Straße, 23 Gartenarbeitsschule (Dillenburger Str. 57), 24 Erwin-von-Witzleben-Grundschule (Halemweg 34/42). Kennung 11200.
- Leistungsart (je Los): alle Lose „Unterhalts-, Grund- und Bedarfsreinigung“.
- Suchschritte:
  - lokal: Auftraggeber `Charlottenburg` vor 20260320 → 26 Treffer (2016–2025), darunter 325959-2023 (Gebäudereinigung), Schulverfahren
    734669-2023, 23249-2024, 265728-2024/328394-2024/497591-2024, 136880-2025, und die Gruppe 102284/173796/177950-2025 (25 andere
    Einrichtungen, z. B. Dienstgebäude Haubachstraße, Rathaus Schmargendorf, Mommsenstadion, Mossestift).
  - API 01: `(FT~"Dietrich-Bonhoeffer-Bibliothek" OR FT~"Hohenzollerndamm" OR FT~"Otto-Suhr-Allee" OR FT~"Gretel-Bergmann") AND
    buyer-name~"Charlottenburg"` + Std. → 27 Treffer (praktisch alle Bezirksamt-Notices; „Hohenzollerndamm“ ist die Anschrift des
    Bezirksamts, daher unspezifisch).
  - API 02: `(FT~"Dietrich-Bonhoeffer-Bibliothek" OR FT~"Gretel-Bergmann" OR FT~"Hans-Rosenthal" OR FT~"Alt-Lietzow" OR FT~"Heckerdamm"
    OR FT~"Wallotstr")` + Std. → 19 Treffer, für das Bezirksamt nur 2016–2023 (jüngster: 325959-2023), keiner danach.
  - API 03: `(FT~"Mossestift" OR FT~"Mommsenstadion" OR FT~"Gartenarbeitsschule" OR FT~"Abenteuerspielplatz")` + Std. → 41 Treffer
    (überwiegend andere Auftraggeber; Bezirksamt 2016–2023 und 2025er-Gruppe).
  - API 04: `(FT~"Mossestift" OR FT~"Standesamt Alt-Lietzow" OR FT~"Spielhaus Schillerstr")`, ohne CPV, 20230601 bis vor Testfall → 3
    Treffer (102284/173796/177950-2025, Grund: Mossestift).
  - API 05: `buyer-name~"Charlottenburg" AND (form-type=result OR form-type=change OR form-type=cont-modif)`, ohne CPV, 20230601 bis vor
    Testfall → 23 Treffer; Reinigung (CPV 909) nur 438157-2023 (Berichtigung zu 325959-2023) und 497591-2024 (Schulen). **Kein Zuschlag zu
    325959-2023.**
  - XML geöffnet: 195060-2026 (Testfall), 325959-2023, 438157-2023.
- Bester Kandidat: 325959-2023 (Ausschreibung „Gebäudereinigung“, vor eForms, 2023-05-31, Az. „10121 Ö-II-23“, 34 Lose, je Los ein Objekt).
- A (Identität): übereinstimmend (Objektnamen), Fläche mehrdeutig  Details: 22 der 24 Testfall-Objekte stehen als Los in 325959-2023
  (Los_06 „DG_Herrstr“ als Schreibvariante von Heerstraße gewertet, Los_07 „DG-Hohenzollerndamm“, Los_08 „Dietrich-Bonhoeffer-Bibliothek“,
  Los_09 „Erwin-von-Witzleben-GS“, Los_10 „Familienzentrum-guk“, Los_12 „Hans-Rosenthal-Sportanlage“, Los_13 „Hdj-Anne-Frank“, Los_14
  „Hubertus-Sportplatz“, Los_15–17 JFH Heckerdamm/Plöner Str/Spirale, Los_23 „MS-Prinzregentenstr“, Los_25 „Rathaus-Charlottenburg“, Los_26
  „SC-Wallotstr“, 27 „Spielhaus Schillerstr.“, Los_28–31 Sportanlage Jungfernheide/Sporthalle Emser Str/Sportplatz im Jagen/Stadtteilzentrum
  Halemweg, Los_32 „Standesamt-Alt-Lietzow“, Los_33 „Gretel-Bergmann-Sporthalle“, Los_34 „Sportanlage-am-Volkspark“). Fehlend 2023:
  Abenteuerspielplatz Holsteinische Straße, Gartenarbeitsschule. Flächen 2023 als „m2 Reinigungsfläche pro Woche“, 2026 als
  „m² Reinigungsfläche“ (andere Flächenart; z. B. Rathaus 70.044,39 gegenüber 30.030,04) → mehrdeutig; nur Gretel-Bergmann-Sporthalle
  2.333,56 = 2.333,56. Kein Widerspruch.
- B (Objektraum): erkennbar und übereinstimmend  Details: Bezirk Charlottenburg-Wilmersdorf, je Los namentlich benannte bezirkliche
  Einrichtungen, Unterhalts-, Grund- und Bedarfsreinigung auf beiden Seiten.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich („Unterhalts-, Grund- und Bedarfsreinigung in diversen bezirklichen
  Einrichtungen“ wortgleich in der Beschreibung), Losstruktur anders (34 gegenüber 24 Lose, je ein Objekt pro Los auf beiden Seiten),
  Verlängerungsformel gleich („Verlängerung um jeweils 6 Monate (längstens um 24 Monate)“).
- Überschneidung der Objekte: 22 von 24 (92 %, kürzere Seite = Testfall); auf der längeren Seite 22 von 34 (65 %). 2023 zusätzlich:
  Birger-Forell-GS, Cecilien-GS, Charles-Dickens-GS, Comenius-Schule, DG-Goslaer-Ufer, Gottfried-Keller-Gymnasium, Joan-Miro-GS,
  Johann-Peter-Hebel-GS, Katharina-Heinroth-GS, Mommsenstadion, Mossestift, Otto-von-Guericke-Schule. Lose mit Überschneidung (Testfall):
  1–21 und 24.
- Weitere geprüfte Kandidaten: 102284/173796/177950-2025 (25 Einrichtungen, 0 von 24 gemeinsam → nicht objektgleich); 265728/328394/
  497591-2024 (11 Schulen, 1 von 24 gemeinsam, Erwin-von-Witzleben-GS, 4 % → nicht objektgleich).
- Ergebnis: **teilmenge** (kürzere Liste zu 92 % in der längeren belegt, die längere enthält 12 weitere Objekte; nicht nahezu
  deckungsgleich, daher nicht „objektgleich“)
- Tendenz (nur bei unklar): –
- Vorgänger: 325959-2023 (competition, vor eForms, 2023-05-31); weitere Notice desselben Vorgängers: 438157-2023 (Berichtigung, 2023-07-19,
  nur Fristverlängerung). Kein Zuschlag auf TED gefunden.
- Beleg: 325959-2023, II.1.4: „Unterhalts-, Grund- und Bedarfsreinigung in diversen bezirklichen Einrichtungen“, Lose u. a.
  „Los_25_Rathaus-Charlottenburg“, „Los_08_Dietrich-Bonhoeffer-Bibliothek“, „Los_33_Gretel-Bergmann-Sporthalle … 2.333,56 m2“; Testfall
  Los 5 „Gretel-Bergmann-Sporthalle … 2.333,56 m² Reinigungsfläche“.
- Vorgänger mit Vertrag: nicht gefunden (API 05: kein Zuschlag zu 325959-2023)
- Vorgänger-Ende: unbekannt; Herkunft: **unbekannt** (laut Ausschreibung 325959-2023 geplant: Grundlaufzeit 2023-12-01 bis 2024-11-30,
  Verlängerung um je 6 Monate, längstens 24 Monate, also rechnerisch bis 2026-11-30; ob und mit wem ein Vertrag geschlossen wurde, ist auf
  TED nicht belegt).
- Hinweis auf vorzeitige Neuvergabe: unklar (kein belegter Vertrag; gegenüber der geplanten Grundlaufzeit beginnt der neue Vertrag
  2026-12-01, also danach).
- Abfragen/XML: 5/3

### U36 – 36379-2026 (2026-01-19) – Bundesanstalt für Materialforschung und -prüfung (BAM)
- Objekt(e): „Reinigung von Hallen, Werkstätten und Technikräumen auf den Liegenschaften (Stammgelände, Zweiggelände Fabeckstraße und
  Zweiggelände Adlershof)“; Leistungsorte: Stammgelände Unter den Eichen (UE), Unter den Eichen 87, 12205 Berlin; Zweiggelände
  Fabeckstraße (FB), 12203 Berlin; Zweiggelände Adlershof (AH), 12489 Berlin. Keine Flächen. Kennung 11/25, ein Los.
- Leistungsart (je Los): Reinigung bestimmter Raumarten (Hallen, Werkstätten, Technikräume), laufende Reinigung; CPV 909…
- Suchschritte:
  - lokal: Auftraggeber `Materialforschung|BAM` → 92 Treffer (Regex traf auch „Bamberg“); BAM selbst: 63195-2018 / 193740-2018 (Glas),
    298512-2019 / 520490-2019 (Unterhalt), 457823-2021 / 619277-2021 (Glas), 385169-2024 (TTS Baruth), 386380-2024 mit den
    Neufassungen 461988/476735/481919-2024 („Unterhaltsreinigung“ Los 1 UE, Los 2 FB, Los 3 AH).
  - API 01: `buyer-name~"Materialforschung"` + Std. → 13 Treffer (wie lokal, zusätzlich Berichtigungen 355502-2019, 511353-2021).
  - API 02: `(FT~"Werkstätten" OR FT~"Technikräume" OR FT~"Technikräumen" OR FT~"Hallen") AND buyer-name~"Materialforschung"` + Std. → 0.
  - API 03: `buyer-name~"Materialforschung" AND (form-type=result OR form-type=competition)`, ohne CPV, 20240901 bis vor Testfall → 49
    Treffer, darunter keine Reinigung (kein Zuschlag zu 386380-2024).
  - XML geöffnet: 36379-2026 (Testfall), 481919-2024 (letzte Fassung von 386380-2024; „ChangeDescription: … Vergabe-/Auftragsbekanntmachung
    inkl. der Vergabeunterlagen überarbeitet“).
- Bester Kandidat: 386380-2024 (Ausschreibung „Unterhaltsreinigung“, eForms, 2024-06-28) mit Neufassungen 461988-2024, 476735-2024,
  481919-2024.
- A (Identität): mehrdeutig  Details: Gleiche drei Liegenschaften (Unter den Eichen 87; Fabeckstraße bzw. „Unter den Eichen 44-46, 12203“;
  Adlershof „Richard-Willstätter-Straße 11“). Der Testfall beschränkt sich auf die Raumarten „Hallen, Werkstätten und Technikräume“; der
  Kandidat nennt nur „Unterhaltsreinigung“ der Liegenschaften ohne Raumarten. Keine Flächen auf beiden Seiten.
- B (Objektraum): erkennbar (Gebiet, Objektart), Leistungsart nicht eindeutig vergleichbar  Details: Gebiet und Objektart (BAM-Standorte in
  Berlin) gleich; ob die laufende Reinigung von Hallen/Werkstätten/Technikräumen dieselbe Leistung ist wie die allgemeine
  Unterhaltsreinigung der Liegenschaften oder ein abgegrenzter Teil davon, lässt sich aus den Texten nicht entscheiden.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel anders („Reinigung von Hallen, Werkstätten und Technikräumen“ gegenüber
  „Unterhaltsreinigung“), Losstruktur anders (ein Los über drei Standorte gegenüber drei Losen je Standort).
- Überschneidung der Objekte: Liegenschaften 3 von 3; Raumarten nicht vergleichbar.
- Ergebnis: **unklar**
- Tendenz (nur bei unklar): **eher dagegen** – der Testfall grenzt ausdrücklich Raumarten (Hallen, Werkstätten, Technikräume) ab, die im
  Kandidaten nicht vorkommen, hat einen anderen Titel und einen anderen Losschnitt; das spricht für einen eigenen Leistungsteil und nicht für
  dasselbe Objekt.
- Vorgänger (Kandidat): 386380-2024 (competition, eForms, 2024-06-28); Neufassungen 461988-2024, 476735-2024, 481919-2024. Ältere
  Unterhaltsreinigung 298512-2019 / 520490-2019 nicht geöffnet.
- Beleg: Testfall `ProcurementProject/Description`: „Reinigung von Hallen, Werkstätten und Technikräumen auf den Liegenschaften
  (Stammgelände, Zweiggelände Fabeckstraße und Zweiggelände Adlershof)“; 481919-2024: „Los 1 „Unterhaltsreinigung“ … Stammgelände Unter
  den Eichen (UE)“.
- Vorgänger mit Vertrag: nicht gefunden (kein Zuschlag zu 386380-2024 auf TED)
- Vorgänger-Ende: unbekannt; Herkunft: **unbekannt** (Plan laut 386380-2024: 2025-01-01 bis 2028-12-31, „einmalige Verlängerung der
  Vertragslaufzeit um 1 Jahr“).
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 3/2

### U37 – 150041-2026 (2026-03-04) – Bundeswehr-Dienstleistungszentrum Husum
- Objekt(e): 4 Lose mit zusammen 16 Liegenschaften. Los 1 Stadum: Südtondern-Kaserne (Stadum), Materiallager Ladelund,
  Aufklärungsstellung Bramstedtlund, Patriot-Stellung Leck, „MatLgr Bargum, 25842 Bargum (vss. ab 2027)“. Los 2 Flensburg I/Glücksburg:
  Schule für Strategische Aufklärung der Bundeswehr, Glücksburg-Meierwik Kaserne, Offiziersheim (Flensburg), Dienstgebäude Schiffbrücke.
  Los 3 Flensburg II: Marineschule Mürwik, Zivilberufliche Aus- und Weiterbildung Flensburg. Los 4 Schleswig/Kropp/Jagel:
  Kai-Uwe-von-Hassel-Kaserne (Kropp), NATO-Flugplatz Schleswig (Jagel), Sammelstandortschießanlage (Schleswig), Geländebetreuung Jagel,
  Karriereberatungsbüro (Schleswig). Keine Flächen. Kennung 6003008254-BwDLZ Husum.
- Leistungsart (je Los): alle Lose „Gebäudereinigung OHNE Fenster“ (Rahmenvereinbarung, Unterhaltsreinigung).
- Suchschritte:
  - lokal: Auftraggeber `Husum` → 19 Treffer (BwDLZ Husum 2017–2025: 106986-2017/373958-2017, 362422-2018, 62737-2019/132241-2019/
    350191-2019, 86806-2021/367681-2021 (Glas), 277910-2021/642246-2021, 611534-2022, 649185-2022, 213866-2023, 374899-2023; eForms:
    Dachrinnen 549107/605446-2024, Lüftung Truppenküchen 165447/501260-2025, Fensterreinigung 846845-2025); Text `Stadum|Mürwik|…`
    → 7 Treffer (nur eForms-Sonderleistungen).
  - API 01: `(FT~"Südtondern" OR FT~"Mürwik" OR FT~"Meierwik" OR FT~"Hassel-Kaserne" OR FT~"Stadum" OR FT~"Jagel")` + Std. → 161
    Treffer (unscharf, u. a. „Stade“, ausländische Notices; erste Seite mit 100 gesichtet), BwDLZ Husum darunter 106986-2017, 373958-2017,
    86806-2021, 277910-2021, 367681-2021, 642246-2021.
  - API 02: `FT~"Kai-Uwe-von-Hassel" AND buyer-name~"Husum"` + Std. → 4 Treffer (86806-2021, 277910-2021, 367681-2021, 846845-2025).
  - XML geöffnet: 150041-2026 (Testfall), 277910-2021, 642246-2021.
- A (Identität): übereinstimmend (Objektliste)  Details: 277910-2021 (Verteidigungsformular F17) nennt dieselben vier Lose mit denselben
  Titeln und je Los die Liegenschaften: Los 1 „Südtondern-Kaserne Stadum (967 Räume …), MatLgr Ladelund, Aufklärungsstellung Bramstedtlund,
  Patriot Stellung Leck“; Los 2 „Schule für Strategische Aufklärung der Bundeswehr, Offizierheim Mürwik, Glücksburg-Meierwik-Kaserne,
  Lagerfläche Harrislee, DstGeb Flensburg Schiffbrücke“; Los 3 „Marineschule Mürwik, zivilberufliche Aus- und Weiterbildung Flensburg“;
  Los 4 „SaStOSchAnl Schleswig, Kai-Uwe-von-Hassel-Kaserne, FlPl Schleswig (NATO), Geländebetreuung Jagel, DstGeb Schleswig Schwarzer Weg“.
  Flächen nur 2021 („qm/Jahr“), daher nicht vergleichbar.
- B (Objektraum): erkennbar und übereinstimmend  Details: Bundeswehr-Liegenschaften in den Bereichen Stadum, Flensburg/Glücksburg,
  Schleswig/Kropp/Jagel; Unterhaltsreinigung ohne Fenster (2021: „Unterhaltsreinigung als Raum- und Sonderreinigung“; Fenster 2021 in einem
  eigenen Verfahren 86806-2021).
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich („Rahmenvertrag(e) über die Gebäudereinigung in Liegenschaften des BwDLZ
  Husum“), Losstruktur gleich (vier Lose, gleiche Losbezeichnungen).
- Überschneidung der Objekte: 14 von 16 auf beiden Seiten (87,5 %). Nur 2026: MatLgr Bargum („vss. ab 2027“), Karriereberatungsbüro Schleswig.
  Nur 2021: Lagerfläche Harrislee, DstGeb Schleswig Schwarzer Weg. Lose mit Überschneidung: 1–4.
- Ergebnis: **objektgleich_mittel** (Objektlisten nahezu deckungsgleich, je zwei abweichende Nebenobjekte; nur ein A-Merkmal belegt
  (Objektliste), Flächen nicht vergleichbar)
- Tendenz (nur bei unklar): –
- Vorgänger: 642246-2021 (Zuschlag, vor eForms, 2021-12-15, alle vier Lose, Zuschlag 2021-11-22); weitere Notice desselben Vorgängers:
  277910-2021 (Ausschreibung, vor eForms, 2021-06-02, „6002105338-BwDLZ Husum“).
- Beleg: 277910-2021, Los 4: „Kai-Uwe-von-Hassel-Kaserne (887 Räume, 1 841 675,16 qm/Jahr), FlPl Schleswig (NATO) …, Geländebetreuung
  Jagel“; Testfall Los 4: „Kai-Uwe-von-Hassel-Kaserne, 24848 Kropp, NATO-Flugplatz Schleswig, 24878 Jagel, … Geländebetreuung Jagel“.
- Vorgänger mit Vertrag: 642246-2021 (Laufzeit aus 277910-2021)
- Vorgänger-Ende: 2026-03-31; Herkunft: **grundlaufzeit** (277910-2021: „F17_FRAMEWORK/DURATION_FRAMEWORK_YEAR: 4“, Beginn 01.04.2022, Ende
  31.03.2026, „NO_OPTIONS“).
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2027-06-01 liegt nach dem Ende).
- Abfragen/XML: 2/3
- Einschätzung (nicht Teil des Urteils): Zwischen 2026-03-31 und 2027-06-01 liegt eine Lücke von 14 Monaten; eine Zwischenlösung
  (Verlängerung, Interimsvergabe) ist auf TED nicht belegt.

### U38 – 173541-2026 (2026-03-12) – Landeshauptstadt Düsseldorf, Amt für Recht, Vergabe und Versicherungen, Zentrale Vergabestelle
- Objekt(e): „Gebäudeunterhaltsreinigung ab 01.11.2026 in 7 Objekten (3 Stadtbezirke)“; keine Objektnamen, keine Stadtbezirke, keine
  Adressen (Leistungsort nur „Düsseldorf, 40200“), keine Flächen. Kennung DUS-2026-0176, ein Los (LOT-0000).
- Leistungsart (je Los): Gebäudeunterhaltsreinigung.
- Suchschritte:
  - lokal: Auftraggeber `Landeshauptstadt Düsseldorf` vor 20260312 → 141 Notices (2016–2026), davon in eForms 37 Verfahren mit Titel
    „Gebäudeunterhaltsreinigung ab …“ (u. a. „ein Objekt“ 691452-2023, „6 Objekte“ 138286-2024, „Eulerstraße“ 183425/376340-2024, „in 11
    Losen“ 512995…22338-2025, „in 5 Losen“, „in 6 Losen“, „in 12 Lose“, „Objekt Auf dem Draap“, „Objekt Teerstegenstraße“); keine Beschreibung
    nennt „7 Objekte“ oder „3 Stadtbezirke“.
  - API 01: `(FT~"Stadtbezirke" OR FT~"Stadtbezirken") AND buyer-name~"Landeshauptstadt Düsseldorf"` + Std. → 6 Treffer (476438-2021,
    8618-2022, 44476-2022, 377044-2023, 468518-2023, 500752-2023).
  - API 02: `FT~"Gebäudeunterhaltsreinigung" AND buyer-name~"Landeshauptstadt Düsseldorf"` + CPV, 20161001 bis 20231024 → 19 Treffer
    (2019–2023, vor eForms).
  - XML geöffnet: 173541-2026 (Testfall), 476438-2021, 377044-2023, 500752-2023.
- Geprüfte Kandidaten (Fakten): 476438-2021 „Unterhaltsreinigung im gesamten Stadtgebiet“, Lose je Stadtbezirk („Unterhaltsreinigung
  diverser Objekte Stadtbezirk 3“, … „Dienststellen der Landeshauptstadt Düsseldorf verteilt über das gesamte Stadtgebiet“); 377044-2023 und
  500752-2023 „Gebäudeunterhaltsreinigung ab 01.01.2024“, vier Lose „Stadtbezirk 1/3/6/9“, Beschreibung nur „Los 1“ usw. Keine Objektlisten.
- A (Identität): nicht vergleichbar  Details: Testfall ohne Objektnamen, Adressen, Flächen; Kandidaten ebenfalls ohne Objektlisten.
- B (Objektraum): nicht erkennbar  Details: Testfall nennt weder Objektart noch Stadtbezirke („7 Objekten (3 Stadtbezirke)“); Auftraggeber
  ist eine Großstadt mit vielen Gebäudearten.
- C (Stütze): Auftraggeber ja (Zentrale Vergabestelle der Stadt), CPV ja, Titel ähnlich („Gebäudeunterhaltsreinigung ab …“), Losstruktur anders.
- Überschneidung der Objekte: nicht bestimmbar.
- Ergebnis: **unklar** (Stufe B auf der Testfallseite nicht erkennbar; ein Widerspruch zu den Kandidaten ist ebenso wenig belegbar)
- Tendenz (nur bei unklar): **keine** – kein Kandidat ist inhaltlich näher als ein anderer; die Stadt führt viele parallele Verfahren mit
  gleichem Titelmuster.
- Vorgänger (Kandidat): kein bevorzugter Einzelkandidat; nächstliegend dem Muster „Objekte in Stadtbezirken“: 500752-2023 (competition,
  vor eForms, 2023-08-18) bzw. 476438-2021 (competition, vor eForms, 2021-09-21, Zuschläge 8618-2022 / 44476-2022 nicht geöffnet).
- Beleg: Testfall `ProcurementProject/Description`: „Gebäudeunterhaltsreinigung ab 01.11.2026 in 7 Objekten (3 Stadtbezirke)“;
  476438-2021, II.2.4 Los 1: „Unterhaltsreinigung diverser Objekte Stadtbezirk 3“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: unbekannt; Herkunft: **unbekannt**
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 2/4

### U39 – 183269-2026 (2026-03-17) – Gemeinde Jork
- Objekt(e): Los 1 (4.513 m²): Grundschule Westerminnerweg, Grundschule Ladekop mit Schulkindergarten, Archiv (alt). Los 2 (11.044 m²):
  Verwaltungsgebäude Osterjork 5-7, Tourist-Info, Bücherei, Sporthalle Schulzentrum (Oberschule), Archiv (in neuer Grundschule, nach
  Fertigstellung Neubau), Turnhalle Schützenhofstraße, Festhalle Schützenhofstraße, Jugendzentrum, Feuerwehr Ladekop, Sporthalle
  Wetternweg, Toilette Friedhof Estebrügge, Grundschule an der Este (nur Turnhalle und Sportlerheim), Bauhof (Neubau), Feuerwehr Borstel,
  Feuerwehr Estebrügge (Altbau), „3 Feuerwehren (Sanitärräume)“, Feuerwehr Estebrügge (Neubau, Fertigstellung ca. Ende 2027 / Anfang 2028).
  Kennung E18982481. Zwei Lose (technische Kennungen LOT-0001 und LOT-0003, intern „LOT-0002 E18982481“).
- Leistungsart (je Los): Los 1 und Los 2 Unterhalts- und Grundreinigung.
- Suchschritte:
  - lokal: Auftraggeber `Jork` und Ort `Jork` vor 20260317 → je 2 Treffer (125967-2022, 347828-2022).
  - API 01: `(FT~"Westerminnerweg" OR FT~"Osterjork" OR FT~"Ladekop")` + Std. → 2 Treffer (125967-2022, 347828-2022).
  - API 02: `buyer-name~"Jork"` + Std. → 4 Treffer (zusätzlich EU-Delegation Jordanien, nicht einschlägig).
  - XML geöffnet: 183269-2026 (Testfall), 125967-2022, 347828-2022.
- A (Identität): übereinstimmend (Objektliste), Flächen abweichend  Details: 125967-2022 / 347828-2022 nennen 18 Gebäude mit Flächen
  („Verwaltungsgebäude Osterjork 5‐7: 634,92 m², Tourist‐Info: 153,84 m², Gemeindebücherei: 268,74 m², Sporthalle Schulzentrum: 2.371,99 m²,
  Turnhalle Schützenhofstraße, Festhalle Schützenhofstraße, Jugendzentrum, Grundschule Am Westerminnerweg: 2.802,19 m², Grundschule Ladekop:
  783,10 m², Archiv: 103,15 m², Feuerwehr Ladekop, Sporthalle Wetternweg, Grundschule Este (Turnhalle / Sportlerheim), Toilette Friedhof
  Estebrügge, Feuerwehr Borstel, Feuerwehr Moorende, Feuerwehr Königreich, Feuerwehr Hove … Gesamt: 12.920,48 m²“). Fläche der Los-1-Objekte
  2022 zusammen 3.688,44 m² gegenüber 4.513 m² (mit Schulkindergarten), übrige 9.232,04 gegenüber 11.044 m² → abweichend (kein Widerspruch).
- B (Objektraum): erkennbar und übereinstimmend  Details: Gemeinde Jork, namentlich benannte Schulen, Sporthallen, Feuerwehren und
  Verwaltungsgebäude, Unterhalts- und Grundreinigung auf beiden Seiten.
- C (Stütze): Auftraggeber ja, CPV ja (90919300/90911200), Titel gleich („Unterhalts- und Grundreinigung in den Gebäuden der Gemeinde Jork“,
  Beschreibung wortgleich), Losstruktur anders (2022 ein Los, 2026 zwei Lose).
- Überschneidung der Objekte: 15 von 18 (83 %, kürzere Seite = 2022); auf der längeren Seite 15 von 20 Einträgen (75 %). Nur 2022:
  Feuerwehr Moorende, Königreich, Hove (mögliche Entsprechung zu „3 Feuerwehren (Sanitärräume)“, nicht gezählt). Nur 2026: Archiv (neu),
  Bauhof (Neubau), Feuerwehr Estebrügge (Alt- und Neubau), „3 Feuerwehren“. Lose mit Überschneidung (Testfall): 1 und 2.
- Ergebnis: **teilmenge** (kürzere Liste zu 83 % auf der längeren belegt, die längere enthält weitere Objekte, u. a. Neubauten; bei
  Zweifel zwischen „nahezu deckungsgleich“ und Teilmenge gilt nach der Rangfolge Teilmenge)
- Tendenz (nur bei unklar): –
- Vorgänger: 347828-2022 (Zuschlag, vor eForms, 2022-06-28, „Erich Niediek GmbH & Co. KG“, Vertragsschluss 2022-06-16); weitere Notice
  desselben Vorgängers: 125967-2022 (Ausschreibung, vor eForms, 2022-03-10).
- Beleg: 347828-2022, II.1.4: „Grundschule Am Westerminnerweg:2.802,19 m² … Grundschule Ladekop: 783,10 m² … Gesamt: 12.920,48 m²“;
  Testfall Los 1: „Grundschule Westerminnerweg, der Grundschule Ladekop mit Schulkindergarten und dem Archiv (alt)“.
- Vorgänger mit Vertrag: 347828-2022 (Laufzeit aus 125967-2022)
- Vorgänger-Ende: Grundlaufzeit 2025-07-31, danach jährliche Verlängerung ohne Höchstdauer; Herkunft: **rollierend** (125967-2022, II.2.7:
  2022-07-14 bis 2025-07-31, „Der Vertrag verlängert sich danach jeweils um ein Jahr, wenn er nicht mit einer Frist von 6 Monaten
  gekündigt wurde“).
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-07-01 liegt nach dem Ende der Grundlaufzeit).
- Abfragen/XML: 2/3

### U40 – 108283-2026 (2026-02-16) – Stadtverwaltung Kaiserslautern, Stabstelle IV.1 Zentrale Vergabestelle
- Objekt(e): „RV Glas- und Rahmenreinigung an allen städtischen Gebäuden im Stadtgebiet Kaiserslautern“; 4 Gebietslose „Ortsteile“,
  „Stadtgebiet“, „Rathaus und Umgebung“, „Altstadt und Umgebung“, je Los „ca. 54200 qm Glasflächen“ (vermutlich Gesamtangabe). Keine
  Objektliste, keine Adressen. Kennung 2026/02-040.
- Leistungsart (je Los): Glas- und Rahmenreinigung (Rahmenvereinbarung), alle Lose.
- Suchschritte:
  - lokal: Auftraggeber `Kaiserslautern` vor 20260216 → 37 Treffer; Stadtverwaltung: 43472-2019 / 378111-2019 (Stadtbildpflege, Los 1
    Unterhalt, Los 2 Glas), 662197-2021 / 262973-2022 (Stadtbildpflege, Los 1 Unterhalt, Los 2 Glas), 71361-2025 (Barbarossahalle);
    übrige: TU/RPTU, Landkreis, LBB, ZAK, SWK, Stadtentwässerung (andere Auftraggeber).
  - API 01: `(FT~"Glasreinigung" OR FT~"Rahmenreinigung" OR FT~"Glasflächen") AND buyer-name~"Stadtverwaltung Kaiserslautern"` + Std. →
    5 Treffer (43472-2019, 378111-2019, 662197-2021, 262973-2022, 71361-2025).
  - API 02: `(FT~"Altstadt und Umgebung" OR FT~"Rathaus und Umgebung" OR FT~"städtischen Gebäuden") AND buyer-city="Kaiserslautern"`
    + Std. → 0 Treffer.
  - XML geöffnet: 108283-2026 (Testfall), 43472-2019, 662197-2021.
- Geprüfte Kandidaten (Fakten): 662197-2021 „Gebäudereinigungsleistungen (Unterhalt- und Glasreinigung) für Objekte der Stadtbildpflege
  Kaiserslautern“, Los 2 „Glasreinigung“, Ort „Stadtbildpflege Kaiserslautern - Eigenbetrieb der Stadt Kaiserslautern Daennerstraße 11“;
  43472-2019 gleiche Liegenschaften („Liegenschaften der Stadtbildpflege Kaiserslautern, Glasreinigung“, Daennerstraße 11); 71361-2025
  „Reinigung der Barbarossahalle“ (Ludwig-Thoma-Str. 1, ein Objekt).
- A (Identität): nicht vergleichbar  Details: Testfall ohne Objektliste; Kandidaten nennen nur Stadtbildpflege-Liegenschaften bzw. eine Halle.
- B (Objektraum): nicht erkennbar (Testfall)  Details: „alle städtischen Gebäude“ einer Stadt mit vielen Gebäudearten → Objektart nicht
  erkennbar; Gebiet (Stadtgebiet Kaiserslautern) und Leistungsart (Glas-/Rahmenreinigung) stimmen mit Los 2 der Stadtbildpflege-Verfahren überein.
- C (Stütze): Auftraggeber ja (Zentrale Vergabestelle der Stadt), CPV ja (90911300), Titel anders, Losstruktur anders (4 Gebietslose
  gegenüber Los 1 Unterhalt / Los 2 Glas).
- Überschneidung der Objekte: nicht bestimmbar.
- Ergebnis: **unklar**
- Tendenz (nur bei unklar): **eher dagegen** – die Kandidaten betreffen die Liegenschaften eines Eigenbetriebs (Stadtbildpflege,
  Daennerstraße 11) bzw. eine einzelne Halle, der Testfall „alle städtischen Gebäude“ in vier Gebietslosen; eine Rahmenvereinbarung für die
  Glasreinigung aller städtischen Gebäude ist auf TED vorher nicht zu finden.
- Vorgänger (Kandidat): 662197-2021 (competition, vor eForms, 2021-12-24, Los 2 Glasreinigung) mit Zuschlag 262973-2022 (result, vor eForms,
  2022-05-17, nicht geöffnet).
- Beleg: Testfall `ProcurementProject/Description`: „RV Glas- und Rahmenreinigung an allen städtischen Gebäuden im Stadtgebiet
  Kaiserslautern“; 662197-2021, II.2.3: „Stadtbildpflege Kaiserslautern - Eigenbetrieb der Stadt Kaiserslautern Daennerstraße 11“.
- Vorgänger mit Vertrag: (Kandidat) 262973-2022
- Vorgänger-Ende: (Kandidat, aus 662197-2021) Grundlaufzeit 2022-04-01 bis 2024-03-31, „verlängert sich maximal zweimal um weitere 12
  Monate“, also Höchstende 2026-03-31; Herkunft: **hoechstende** (Zuschlag nicht geöffnet, nur als Hinweis).
- Hinweis auf vorzeitige Neuvergabe: nein (bezogen auf den Kandidaten; neuer Beginn 2026-05-01)
- Abfragen/XML: 2/3

### U41 – 34825-2026 (2026-01-19) – Team 65 Gebäudemanagement (Gemeinde Uetze)
- Objekt(e): „Unterhalts- und Grundreinigung für die Gebäude der Gemeinde Uetze sowie der umliegenden Ortschaften“; Los 1 „Gemeinde Uetze“,
  „gesamt ca. 26.795 m²“; Los 2 „Umliegende Ortschaften“, „gesamt ca. 12.233 m²“; Ortschaften „Dollbergen, Eltze, Dedenhausen, Katensen,
  Obershagen, Schwüblingsen“; „Vollständige Adressen: siehe „Losübersicht / Objekte und Adressen“ in den Vergabeunterlagen“. Keine
  Objektliste in der Bekanntmachung. Kennung FBIV-05/26 65.14; Auftraggeberanschrift Marktstraße 9, 31311 Uetze.
- Leistungsart (je Los): Los 1 und Los 2 Unterhalts- und Grundreinigung (keine Glasreinigung).
- Suchschritte:
  - lokal: Auftraggeber `Uetze|Team 65` und Ort `Uetze` vor 20260119 → je 1 Treffer (102756-2021, „Gebäudeservice und Bauhof Uetze“).
  - API 01: `(FT~"Uetze" OR buyer-name~"Uetze")` + Std. → 4 Treffer (102756-2021; sonst Puerto Real, OOWV Kanalreinigung, Region Hannover
    BBS – nicht einschlägig). Kein Zuschlag zu 102756-2021.
  - XML geöffnet: 34825-2026 (Testfall), 102756-2021.
- Kandidat (Fakten): 102756-2021 „OV-Uetze21“: „Unterhalts- und Grundreinigung von 24 Objekten mit einer Jahresreinigungsfläche von ca.
  4 400 000 Quadratmetern und einer Grundreinigungsfläche von ca. 21 800 Quadratmetern. Sowie die Glasreinigung …“; Los 1 „10 Objekte
  (u. a. Schulen, Kita, Feuerwehr, Sportanlage, Verwaltung)“, Los 2 „14 Objekte (u. a. Schulen, Feuerwehr, Sportanlage,
  Flüchtlingswohnungen)“, Los 3 „Glas- und Rahmenreinigung“.
- A (Identität): mehrdeutig  Details: Keine Objektlisten auf beiden Seiten. Flächen verschiedener Art (2021 Jahres- und
  Grundreinigungsfläche, 2026 „gesamt ca. … m²“ ohne Art) → mehrdeutig. Objektzahl nur 2021 (24).
- B (Objektraum): nicht erkennbar  Details: Gebiet (Gemeinde Uetze mit Ortschaften) und Leistungsart (Unterhalt und Grund) stimmen
  überein; die Objektart ist auf beiden Seiten ein Gemisch („Gebäude der Gemeinde“ bzw. Schulen, Kita, Feuerwehr, Sport, Verwaltung,
  Flüchtlingswohnungen) eines kommunalen Auftraggebers mit vielen Gebäudearten → nach den Regeln nicht erkennbar.
- C (Stütze): Auftraggeber ja (kommunaler Gebäudebetrieb der Gemeinde Uetze; Namenswechsel „Gebäudeservice und Bauhof Uetze“ → „Team 65
  Gebäudemanagement“), CPV ja (90911200), Titel anders („OV-Uetze21“ gegenüber „Unterhalts-, Grundreinigung …“), Losstruktur anders (2021 zwei
  Unterhaltslose plus Glaslos, 2026 zwei Unterhaltslose).
- Überschneidung der Objekte: nicht bestimmbar.
- Ergebnis: **unklar** (beide Seiten unspezifisch; „unklar“ ist das höchste erreichbare Urteil)
- Tendenz (nur bei unklar): **eher dafür** – gleiche Gemeinde und gleicher kommunaler Gebäudebetrieb, gleiche Leistungsart in zwei
  Unterhaltslosen, Objektarten der Lose 2021 (Schulen, Kita, Feuerwehr, Sport, Verwaltung) passen zu „Gebäude der Gemeinde Uetze“; es gibt
  keinen anderen Uetzer Kandidaten.
- Vorgänger (Kandidat): 102756-2021 (competition, vor eForms, 2021-03-01); kein Zuschlag auf TED.
- Beleg: 102756-2021, II.1.4: „Unterhalts- und Grundreinigung von 24 Objekten“; Testfall: „Unterhalts- und Grundreinigung für die Gebäude
  der Gemeinde Uetze sowie der umliegenden Ortschaften“.
- Vorgänger mit Vertrag: nicht gefunden
- Vorgänger-Ende: unbekannt; Herkunft: **unbekannt** (102756-2021 nennt nur „DURATION: 48“ Monate und „Eine Verlängerungsoptionen von 12
  Monaten“, ohne Beginn).
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 1/2

### U42 – 187770-2026 (2026-03-18) – Verbandsgemeindeverwaltung Wissen
- Objekt(e): Christophorus-Grundschule, „Hauptstraße 134, 57587 Birken-Honigsessen“ (Einzelstandort); „5x wöchentlich - 1702,62 qm …,
  1x wöchentlich - 15,98 qm …, 1x monatlich - 108,05 qm …, 1x jährlich - 1.826,65 qm Grundreinigung“. Kennung W24/2026, ein Los.
- Leistungsart (je Los): Unterhaltsreinigung mit jährlicher Grundreinigung.
- Suchschritte:
  - lokal: Auftraggeber `\bWissen\b` vor 20260318 → 1 Treffer (117649-2026, „Rathaus Wissen (Neubau) - Unterhaltsreinigung“); Text
    `Birken-Honigsessen|Christophorus` → 2 Treffer (Stadt Vechta 164507-2024/328025-2024, Treffer über anderen Text).
  - API 01: `(FT~"Birken-Honigsessen" OR FT~"Christophorus-Grundschule" OR FT~"Christophorus Grundschule")` + Std. → 0 Treffer.
  - API 02: `(buyer-name~"Verbandsgemeinde Wissen" OR buyer-name~"Verbandsgemeindeverwaltung Wissen" OR buyer-city="Wissen")` + Std. →
    1 Treffer (117649-2026).
  - API 03: `(FT~"Honigsessen" OR FT~"Hauptstraße 134")` ohne CPV, Datum wie Std. → 67 Treffer, nur unscharfe Fremdtreffer (u. a.
    Bezirksgemeinschaft Vinschgau, Gemeinde Stilfs), keine Reinigung in Birken-Honigsessen → außerhalb des Protokolls (anderer CPV), nicht gewertet.
  - XML geöffnet: 187770-2026 (Testfall).
- A (Identität): nicht vergleichbar  Details: kein Kandidat nennt die Christophorus-Grundschule oder Birken-Honigsessen.
- B (Objektraum): widersprüchlich (für den einzigen Treffer)  Details: 117649-2026 betrifft das Rathaus Wissen (Neubau), andere Objektart
  und anderer Ort.
- C (Stütze): Auftraggeber ja (bei 117649-2026), sonst –
- Überschneidung der Objekte: 0 von 1.
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: API 01 (`FT~"Birken-Honigsessen" …`) „totalNoticeCount 0“; 117649-2026 Titel „Rathaus Wissen (Neubau) - Unterhaltsreinigung“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 3/1

## Übersichtstabelle

| U | Notice | Ergebnis | Tendenz | jüngster Vorgänger (bzw. Kandidat bei unklar) | alle Notices desselben Vorgängers | Vorgänger mit Vertrag | Vorgänger-Ende | Herkunft | vorzeitig |
|---|---|---|---|---|---|---|---|---|---|
| U29 | 135556-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U30 | 112103-2026 | objektgleich_mittel | – | 265170-2020 | 104121-2020, 146410-2020 (Berichtigung), 265170-2020 | 265170-2020 | 2026-10-31 | hoechstende | nein |
| U31 | 195153-2026 | unklar | eher dafür | 507117-2022 (Kandidat) | 195952-2022, 507117-2022 (Vertragsänderung 82229-2026 nur Hinweis) | 507117-2022 | 2026-10-31 / 2026-11-30 / 2026-12-31 je Los | grundlaufzeit (danach rollierend) | nein |
| U32 | 164478-2026 | teilmenge | – | 151676-2021 | 480055-2020, 151676-2021 | 151676-2021 | 2027-03-31 | hoechstende | nein |
| U33 | 161174-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U34 | 199877-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U35 | 195060-2026 | teilmenge | – | 325959-2023 | 325959-2023, 438157-2023 (Berichtigung) | nicht gefunden | unbekannt (Plan: Grundlaufzeit bis 2024-11-30, rechnerisch längstens 2026-11-30) | unbekannt | unklar |
| U36 | 36379-2026 | unklar | eher dagegen | 386380-2024 (Kandidat) | 386380-2024, 461988-2024, 476735-2024, 481919-2024 | nicht gefunden | unbekannt (Plan 2025-01-01 bis 2028-12-31 + 1 Jahr) | unbekannt | unklar |
| U37 | 150041-2026 | objektgleich_mittel | – | 642246-2021 | 277910-2021, 642246-2021 | 642246-2021 | 2026-03-31 | grundlaufzeit | nein |
| U38 | 173541-2026 | unklar | keine | kein Einzelkandidat (nächstliegend 500752-2023 bzw. 476438-2021) | – | – | unbekannt | unbekannt | unklar |
| U39 | 183269-2026 | teilmenge | – | 347828-2022 | 125967-2022, 347828-2022 | 347828-2022 | Grundlaufzeit 2025-07-31, danach jährlich | rollierend | nein |
| U40 | 108283-2026 | unklar | eher dagegen | 662197-2021 (Kandidat, Los 2) | 662197-2021, 262973-2022 | 262973-2022 (nicht geöffnet) | 2026-03-31 (aus Ausschreibung) | hoechstende | nein |
| U41 | 34825-2026 | unklar | eher dafür | 102756-2021 (Kandidat) | 102756-2021 | nicht gefunden | unbekannt | unbekannt | unklar |
| U42 | 187770-2026 | kein_vorgaenger | – | – | – | – | – | – | – |

Abfragen/XML je Fall (XML einschließlich Testfall): U29 5/6, U30 2/4, U31 3/5, U32 2/4, U33 4/1, U34 3/1, U35 5/3, U36 3/2, U37 2/3,
U38 2/4, U39 2/3, U40 2/3, U41 1/2, U42 3/1. Insgesamt 39 API-Abfragen und 42 XML.

## Übersicht (Fakten)

| Kategorie | Anzahl | Fälle |
|---|---|---|
| objektgleich_hoch | 0 | – |
| objektgleich_mittel | 2 | U30, U37 |
| teilmenge | 3 | U32, U35, U39 |
| unklar | 5 | U31 (eher dafür), U41 (eher dafür), U36 (eher dagegen), U40 (eher dagegen), U38 (keine) |
| kein_vorgaenger | 4 | U29, U33, U34, U42 |
| **Summe** | **14** | |

- Objektgleich oder Teilmenge (Variante „breit“ ohne unklar): 5 von 14; nur objektgleich: 2 von 14; „hoch“: 0.
- Mit „unklar, eher dafür“ (Zusatzvariante): 7 von 14.
- **Abbruch durch Budget:** keiner. Höchstwerte: 5 API-Abfragen (U29, U35), 6 XML (U29).
- **Vorgänger-Ende** aus einem belegten Vertrag (Zuschlag gefunden, Laufzeit aus der zugehörigen Ausschreibung): U30 (hoechstende),
  U32 (hoechstende), U37 (grundlaufzeit), U39 (rollierend; Grundlaufzeit-Ende 2025-07-31). Bei U35 fehlt der Zuschlag (Herkunft unbekannt).
  Hinweis auf vorzeitige Neuvergabe: in keinem bestätigten Fall.

## Grenzfälle der Regeln

1. **„Nahezu deckungsgleich“ ist nicht quantifiziert (U37, U39).** U37: je 16 Objekte, 14 gemeinsam, auf jeder Seite zwei andere
   Nebenobjekte; Teilmenge passt nicht, weil keine Seite die andere enthält und beide gleich lang sind, daher objektgleich (mittel).
   U39: 15 von 18 gegenüber 15 von 20, die neue Seite enthält zusätzlich Neubauten, daher nach der Rangfolge Teilmenge. Beide Urteile
   hängen an dieser Lesart; mit einer festen Schwelle (zum Beispiel mindestens 90 Prozent beider Seiten für „objektgleich“) wäre U37
   nicht mehr objektgleich.
2. **Benannte Objektbündel eines Landes-Auftraggebers (U31).** „Segment Polizei-, Justiz- und Verwaltungsgebäuden und sonst. Dienststellen“
   und „Segment Feuerwehr“ nennen Objektarten, aber als Bündel „diverser Liegenschaften“; ich habe Stufe B als nicht erkennbar gewertet
   (Regel „diverse Gebäude … Land“). Die gleiche Zahl von 67 Liegenschaften im ersten Segment ist ein A-Merkmal (Gebäudezahl), reicht aber
   ohne erkennbare Stufe B nicht. Andere Lesart: objektgleich (mittel).
3. **Teilleistung nach Raumarten (U36).** „Reinigung von Hallen, Werkstätten und Technikräumen“ gegenüber „Unterhaltsreinigung“ derselben
   drei Liegenschaften: Die Regeln kennen „andere Leistungsart“ (Unterhalt, Glas, Grund) und „Gebäudeteile“, aber keine Abgrenzung nach
   Raumarten innerhalb der Unterhaltsreinigung. Daher unklar statt nicht objektgleich oder objektgleich.
4. **Unspezifischer Testfall (U38).** Der Testfall nennt nur „7 Objekte (3 Stadtbezirke)“. Nach Definition ist „kein_vorgaenger“ nur
   zulässig, wenn kein Kandidat „unklar“ wäre; bei nicht erkennbarer Stufe B ist aber jeder gleichartige Kandidat desselben Auftraggebers
   formal „unklar“. Ergebnis daher unklar ohne Tendenz und ohne bevorzugten Einzelkandidaten.
5. **Einzelobjekt in einem Mehrobjekt-Los (U32).** Flächen (Unterhalt 0,5 Prozent, Glas 0,7 Prozent Abweichung) und Adresse belegen das
   Objekt eindeutig, das Vorgänger-Los umfasst aber zusätzlich Bautzen. Nach den Regeln (Kalibrierung Stralsund) Teilmenge, obwohl die
   Identität des gemeinsamen Objekts stärker belegt ist als bei den beiden „objektgleich (mittel)“-Fällen.
6. **Flächenabweichung knapp über 2 Prozent (U30).** Unterhalt-Grundfläche plus 2,37 Prozent, also abweichend, daher nur „mittel“ (Regel
   angewendet, nicht neu ausgelegt; als Grenzfall vermerkt).

## Auffälligkeiten

**Fakten**
- **Namenswechsel und Zuständigkeit:** U41 „Gebäudeservice und Bauhof Uetze“ (2021), jetzt „Team 65 Gebäudemanagement“ (2026). U30: Der
  Vorgänger 2020 nennt im Titel „Bundesamt für Arbeitsschutz und Arbeitsmedizin Dresden“, im Text „Bundesanstalt“. U29: Schulen in Gotha
  wurden bisher vom Landkreis Gotha ausgeschrieben; die Stadt Gotha vergab auf TED nur Kindergärten und Verwaltungsobjekte.
- **Zentrale Vergabestellen und Beschaffungsdienstleister:** BImA (U30, U32), BIM Berliner Immobilienmanagement für SILB, SODA und
  Liegenschaftsfonds (U31), Zentrale Vergabestelle Düsseldorf (U38) und Kaiserslautern (U40), BA Geschäftsbereich Einkauf (U34). In Düsseldorf
  laufen sehr viele gleich betitelte Verfahren („Gebäudeunterhaltsreinigung ab …“) ohne Objektnamen in der Bekanntmachung (37 in der
  eForms-Zeit).
- **Fehlende Zuschläge auf TED:** U35 (325959-2023), U36 (386380-2024), U41 (102756-2021).
- **Vertragsänderung als Wegweiser:** 82229-2026 (cont-modif, außerhalb der Vorgänger-Quellen) führte bei U31 zum Verfahren 195952-2022.
- **Außerhalb des Protokolls (anderer CPV), nicht gewertet:** U33 API 03 (Stadtwerke Speyer, CPV 34144511, 90420000, 90514000, 48214000,
  72200000); U35 API 05 (Bezirksamt: Schulmittagessen, Parkscheinautomaten u. a.); U36 API 03 (BAM: Laborgeräte, Software u. a.); U42 API 03
  (Fremdtreffer ohne CPV-Filter). Kein Fund außerhalb CPV 909 war ein Reinigungsvorgänger.
- **Volltextsuche unscharf:** `FT~` findet ähnliche Wörter (U37: „Stadum“ trifft „Stade“, 161 Treffer; U42: „Honigsessen“ und
  „Hauptstraße 134“ treffen Südtiroler Notices). Begriffe, die zugleich Anschrift des Auftraggebers sind (U35: „Hohenzollerndamm“), liefern
  fast alle Notices des Auftraggebers.
- **Lokale Filter:** Der Regex `BAM` traf auch „Bamberg“ (U36), `Arbeitsschutz` traf Beschreibungstexte (U30); die Treffer wurden von Hand
  aussortiert.

**Einschätzungen**
- U37: Zwischen dem Ende des Vorgängers (2026-03-31) und dem neuen Beginn (2027-06-01) liegen 14 Monate; vermutlich gibt es eine nicht auf
  TED veröffentlichte Zwischenlösung.
- U35: Die Objekte des Verfahrens 325959-2023 wurden später auf mehrere Verfahren verteilt (Schulen 2024, andere Einrichtungen 2025, Rest
  2026). Für eine automatische Zuordnung heißt das: Ein Vorgänger kann sich auf mehrere Nachfolger aufteilen.
- U31: Bei Sammelverfahren ohne Objektliste ist die Zahl der Liegenschaften je Segment das einzige Identitätsmerkmal.
