# Sichtbarkeit der Vorgänger – Handsuche Iteration 4, Teil 2 (U15–U28)

- **Datum:** 2026-10-25
- **Bearbeiter:** Subagent `rechercheur` (Auftrag „Handsuche“)
- **Testfälle:** Zeilen 15–28 aus `reports/testfaelle_iteration4.txt`, bezeichnet U15–U28 in dieser Reihenfolge
  (84022-2026, 122844-2026, 93297-2026, 221159-2026, 129778-2026, 137428-2026, 125546-2026, 109620-2026, 2335-2026,
  98964-2026, 209981-2026, 84590-2026, 92834-2026, 54141-2026).

## Definitionen

- Kategorien nach `reports/urteilsregeln_blindpruefung.md`, **Version 1.1** (vor dem ersten Fall vollständig gelesen, einschließlich
  der acht Kalibrierungsbeispiele). Ergebniskategorien: `objektgleich_hoch`, `objektgleich_mittel`, `teilmenge`, `unklar` (mit Tendenz),
  `kein_vorgaenger`.
- Begriffe nach `docs/iterationen.md`, Abschnitt „Iteration 4“: Vorgänger-Quellen sind Zuschläge (`form-type=result`) und frühere
  Ausschreibungen (`form-type=competition`) auf TED, veröffentlicht ab 01.10.2016 und vor dem Testfall.
- `kein_vorgaenger`: nach vollständigem Protokoll kein Kandidat objektgleich, Teilmenge oder „unklar“.
- **Zeitabstand, Vertragsende, Laufzeit und Auftragswert sind nicht in die Urteile eingeflossen**, auch nicht in die Tendenz.
  Vorgänger-Ende und der Hinweis auf vorzeitige Neuvergabe wurden erst **nach** dem Urteil und getrennt davon notiert.

## Unabhängigkeit

Ich bestätige: Gelesen wurden nur `reports/testfaelle_iteration4.txt` und `.md`, `reports/urteilsregeln_blindpruefung.md`,
`docs/iterationen.md` (Abschnitt Iteration 4), die TED-API, die TED-XML und die erlaubten Rohdaten unter `data/raw/ted_search/`
(fünf genannte Verzeichnisse). Nicht gelesen wurden insbesondere `src/zuordnung_*`, `src/objekt_merkmale.py`, `src/los_merkmale.py`,
`src/testprobe_iteration4.py`, `data/processed/`, `data/raw/ted_ft/`, alle Reports zu Zuordnung, Regelentwicklung, Blindprüfung,
Evaluation, Iteration 3 und `reports/sichtbarkeit_iteration4_teil1.md`. Die Ergebnisse anderer Teile der Handsuche kenne ich nicht.

## Vorgehen und Konventionen

- **Lokale Vorsuche (zählt nicht als API-Abfrage):** Aus den fünf erlaubten Rohdaten-Verzeichnissen wurde im Scratchpad ein
  Suchindex gebaut (35.150 Notices, dedupliziert nach Nummer). Suche mit regulären Ausdrücken über alle Felder (Auftraggeber, Ort,
  bei eForms Titel, Los-Titel, Los-Beschreibung, Leistungsort), immer gefiltert auf Veröffentlichung ab 20161001 und **vor** dem
  Testfall. Vor eForms enthalten diese Daten nur Nummer, Datum, Formular, CPV, Auftraggeber und Ort. Lokale Suchen sind unter
  „Suchschritte“ als „lokal“ mit Muster und Trefferzahl aufgeführt (Suche A über den Auftraggeber wurde in der Regel lokal geführt,
  weil die Rohdaten ein vollständiger Abzug von `buyer-country=DEU AND classification-cpv=909*` sind).
- **API-Abfragen:** TED Search API v3; jede Abfrage samt Request unter `data/raw/rechercheur_20261025/U<Nr>/api_NN.json` und
  `api_NN_request.json`. Alle Abfragen enthalten `classification-cpv=909*` und `publication-date>=20161001 AND publication-date<[Testfalldatum]`
  (in den Protokollzeilen unten als „+ Zeitfilter“ abgekürzt). Volltext stets als einzelne `FT~"…"`-Terme verknüpft.
- **XML:** jede geöffnete Notice unverändert unter `data/raw/rechercheur_20261025/U<Nr>/<nummer>.xml`. Die XML des Testfalls selbst
  zählt nicht zum Budget von 10 XML; die Zählung „Abfragen/XML“ nennt API-Abfragen / Kandidaten-XML.
- **Einzelstandort:** Eine einzelne Schule, Dienststelle oder Einrichtung gilt als Einzelstandort; Adresse allein zählt dann nicht als
  A-Merkmal (Urteilsregeln 1.1).
- **Vorzeitige Neuvergabe:** „ja“, wenn der Beginn des neuen Vertrags (laut Testfall) mindestens 3 Monate vor dem Ende der Grundlaufzeit
  des Vorgängers liegt. Reine Faktenangabe, nicht Teil des Urteils.

## Fälle

### U15 – 84022-2026 (2026-02-05) – Landeshauptstadt München, Direktorium, Vergabestelle 1, SG 1
- Objekt(e): fünf städtische Objekte in 81671 München: (A) Echardinger Str. 29, Baureferat-Gartenbau-Gebietsbetriebshof Ost; (B) Neumarkter
  Str. 93, Straßenunterhaltsbezirk; (C) Neumarkter Str. 97, Kindertagesstätte; (D) Grafinger Str. 96, Kinderkrippe; (E) Hermann-Weinhauser
  Str. 28, Haus für Kinder. Reinigungsfläche Boden 4.550 m², Glas 1.015 m². Ein Los.
- Leistungsart (je Los): Unterhalts- und Glasreinigung (CPV 90911200, 90911300).
- Suchschritte:
  - lokal, Suche A: `buyer-name: Landeshauptstadt M.nchen`, vor 20260205 → 818 Notices (davon 683 vor eForms ohne Titel). eForms-Titel
    der Vergabestelle 1 (ca. 100 Notices, Titel nach erster Adresse, z. B. „Gebäudereinigung Haager Straße 14-18“) durchgesehen: keiner nennt
    Echardinger, Neumarkter, Grafinger oder Weinhauser Str.
  - lokal, Suche B/C: `Echarding|Neumarkter Str|Grafinger|Weinhauser` → 2 Treffer, beide SVLFG Kassel (220422-2025, 701306-2024), nicht München.
  - API 01: `FT~"Echardinger"` + CPV + Zeitfilter → 0
  - API 02: `(FT~"Neumarkter" OR FT~"Weinhauser")` + CPV + Zeitfilter → 192 (überwiegend Neumarkt i. d. OPf. u. a.; zu breit, nicht ausgewertet)
  - API 03: `(FT~"Gebietsbetriebshof" OR FT~"Straßenunterhaltsbezirk")` + CPV + Zeitfilter → 6, alle LH München (364667-2017, 18730-2018,
    100953-2018, 294597-2018, 535409-2019, 121412-2020)
  - API 04: `FT~"Neumarkter" AND buyer-city=München` + CPV + Zeitfilter → 7 (Bayer. Landesamt für Steuern, AOK Bayern, Freistaat Bayern; keine LH München)
  - API 05: `(FT~"Weinhauser" OR FT~"Grafinger") AND buyer-city=München` + CPV + Zeitfilter → 2 (225757-2017, 381157-2017)
  - XML geöffnet: 535409-2019, 121412-2020 (Haidelweg 14, Lampertstr. 1, Planegger Str. 111, Richard-Riemerschmid-Allee 32, 81241);
    100953-2018 (Stadelheimer Str. 24, Lincolnstr. 71 und 65, 81549); 364667-2017 (Moosacher Str. 28, Detmoldstr. 10, Riesenfeldstr. 75, 80809);
    225757-2017 (Grafinger Str. 67, 69, 69a, 71, Grundschule und Häuser für Kinder, 81671).
- A (Identität): widersprüchlich (bei allen geöffneten Kandidaten)  Details: Keine einzige Adresse der fünf Testfall-Objekte kommt in einem
  Kandidaten vor. Nächster Kandidat 225757-2017: Grafinger Str. 67–71 gegenüber Grafinger Str. 96 im Testfall, also andere Hausnummern und
  andere Einrichtungen.
- B (Objektraum): bei 225757-2017 Gebiet gleich (81671), Objektart teils anders (Grundschule/Häuser für Kinder gegenüber Betriebshof,
  Straßenunterhaltsbezirk, Kitas); übrige Kandidaten anderer Stadtteil.
- C (Stütze): Auftraggeber ja, CPV ja, Titel anders (anderes Leitobjekt), Losstruktur gleich (1 Los).
- Überschneidung der Objekte: 0 von 5 (225757-2017: 0 von 4).
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: Volltextsuche `FT~"Echardinger"` liefert 0 Treffer; 225757-2017 nennt „Grafinger Straße 71, Grundschule; Grafinger Straße 67, Haus für
  Kinder und Hort; Grafinger Straße 69 … 69a“, nicht „Grafinger Str. 96, Kinderkrippe“ wie 84022-2026.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 5/5

### U16 – 122844-2026 (2026-02-20) – Kommunale Immobilien Jena
- Objekt(e): Jenaplanschule, Tatzendpromenade 9, 07745 Jena („kommunale Schule mit Sporthalle“). Keine Fläche angegeben. Ein Los.
- Leistungsart (je Los): Gebäudereinigung (Tagesreinigung, CPV 90911200) und Winterdienst (CPV 90620000).
- Suchschritte:
  - lokal, Suche A: `buyer-name: (Kommunale Immobilien Jena|KIJ|Stadt Jena|Eigenbetrieb Kommunale)`, vor 20260220 → 78 Notices (inkl. Rostock-Eigenbetrieb);
    eForms-Titel mit Einzelobjekten je Verfahren, darunter 50843-2024 und 181605-2024 „Gebäudereinigung + Winterdienst - Jenaplanschule,
    Tatzendpromenade 9, 07745 Jena“.
  - lokal, Suche C: `Tatzend|Jenaplan` → 5 (50843-2024, 181605-2024; übrige Weimar und Rostock)
  - API 01: `FT~"Tatzendpromenade"` + CPV + Zeitfilter → 2 (50843-2024, 181605-2024); kein Treffer vor eForms.
  - XML geöffnet: 50843-2024, 181605-2024.
- A (Identität): übereinstimmend (nur Adresse/Gebäudename)  Details: Beide Titel wortgleich „Jenaplanschule, Tatzendpromenade 9, 07745 Jena“.
  Im Leistungsort-Feld von 2024 steht „Kommunale Immobilien Jena - Jenaplanschule / Tatzendpromenade 3“, im Testfall „Tatzendpromenade 9“;
  da der eigene Titel von 2024 Hausnummer 9 nennt, werte ich das nicht als Widerspruch (siehe Auffälligkeiten). Keine Fläche, Geschosse
  oder Gebäudeteile auf beiden Seiten. Einzelstandort: Adresse zählt nicht.
- B (Objektraum): erkennbar und übereinstimmend  Details: Jena 07745, Schule, Gebäudereinigung + Winterdienst.
- C (Stütze): Auftraggeber ja, CPV ja (90911200, 90620000), Titel ähnlich (wortgleich), Losstruktur gleich (1 Los); Kriterien fast gleich
  (Leistungskennzahl 280 m²/h Unterrichtsraum, 100 m²/h Sanitär).
- Überschneidung der Objekte: 1 von 1.
- Ergebnis: **objektgleich_mittel**
- Tendenz (nur bei unklar): –
- Vorgänger: 50843-2024 (competition, eForms, 2024-01-25) und 181605-2024 (result, eForms, 2024-03-26)
- Beleg: 181605-2024, Los-Titel: „Gebäudereinigung + Winterdienst - Jenaplanschule, Tatzendpromenade 9, 07745 Jena“, Beschreibung „in einer
  kommunalen Schule“, Zuschlag an TIP-TOP Dienstleistungen GmbH.
- Vorgänger mit Vertrag: 181605-2024
- Vorgänger-Ende: 2028-04-30 (PlannedPeriod 2024-05-01 bis 2028-04-30; ContractExtension MaximumNumberNumeric 2, ohne Dauer); Herkunft: grundlaufzeit
- Hinweis auf vorzeitige Neuvergabe: ja (neuer Beginn 2026-05-01, 24 Monate vor Ende der Grundlaufzeit)
- Abfragen/XML: 1/2

### U17 – 93297-2026 (2026-02-10) – Behörde für Finanzen und Bezirke (Finanzbehörde), Hamburg
- Objekt(e): Grundschule Islandstraße, Islandstraße 25, 22145 Hamburg. Keine Fläche in der Bekanntmachung. Ein Los.
- Leistungsart (je Los): Unterhaltsreinigung (CPV 90919300), ab 02.11.2026 unbefristet.
- Suchschritte:
  - lokal, Suche C: `Islandstr|Grundschule Island` vor 20260210 → 2 (742468-2023, 193782-2024, beide SBH | Schulbau Hamburg, „Baureinigung, Islandstraße 25“)
  - API 01: `FT~"Islandstraße"` + CPV + Zeitfilter → 2 (dieselben)
  - API 02: `(FT~"Islandstr" OR FT~"Island-Straße" OR FT~"Schule Islandstraße")` + CPV + Zeitfilter → 0
  - API 03 (Suche B, Ort): `FT~"22145" AND buyer-city=Hamburg` + CPV + Zeitfilter → 7 (Finanzbehörde 336349-2017/101387-2018; SBH 451406-2020,
    673296-2023, 167000-2024 „Baureinigung, Deepenhorn 1“; 742468-2023, 193782-2024)
  - Suche A (Auftraggeber) nicht gesondert: Die Volltextsuche nach der Straße erfasst auch Bekanntmachungen vor eForms; Finanzbehörde-Treffer im
    Gebiet 22145 nur Deepenhorn 1.
  - XML geöffnet: 336349-2017 (Stadtteilschule Meiendorf, Deepenhorn 1, 22145; Gebäude- und Glasreinigung), 742468-2023 (Baureinigung, Islandstraße 25).
- A (Identität): 742468-2023: Adresse übereinstimmend (Islandstraße 25); 336349-2017: widersprüchlich (Deepenhorn 1).
- B (Objektraum): 742468-2023 widersprüchlich  Details: Leistungsart Baureinigung (CPV 45000000 + 90911200, Präqualifikation Bau) gegenüber
  Unterhaltsreinigung; andere Leistungsart gilt als Widerspruch. 336349-2017: andere Schule.
- C (Stütze): 742468-2023: Auftraggeber nein (SBH statt Finanzbehörde), CPV teils, Titel anders, Losstruktur gleich (1 Los).
- Überschneidung der Objekte: 742468-2023: 1 von 1, aber andere Leistungsart; 336349-2017: 0 von 1.
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: 742468-2023, Titel „Baureinigung, Islandstraße 25“ mit CPV 45000000; Testfall 93297-2026 „Unterhaltsreinigung in dem Objekt
  Grundschule Islandstraße … ab dem 02.11.2026 unbefristet“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 3/2

### U18 – 221159-2026 (2026-03-31) – Markt Zusmarshausen
- Objekt(e): Los 1 (Schulverband Zusmarshausen): Grund- und Mittelschule, Sporthalle, Mittagsbetreuung, Schwimmhalle, alle Stadionstraße 2,
  86441 Zusmarshausen (Boden 5.301,06 / 2.047,72 / 110,51 / 1.117,79 m², gesamt 8.577,08 m²). Los 2 (Markt): Kita ZuS „Zwischen Wald und See“,
  Holzappelstraße 12 (1.707,50 m²). Los 3: Glasreinigung aller fünf Objekte (gesamt 2.857,85 m² Glas).
- Leistungsart (je Los): Los 1 Unterhalts-, Grund- und Schwimmbadreinigung; Los 2 Unterhalts- und Grundreinigung; Los 3 Glas- und Rahmenreinigung.
- Suchschritte:
  - lokal, Suche A/B: `Zusmarshausen` (Auftraggeber, Ort, eForms-Texte) vor 20260331 → 0
  - API 01: `FT~"Zusmarshausen"` + CPV + Zeitfilter → 2 (426337-2020 competition, 470029-2020 change; beide Bezirkskliniken Schwaben, Augsburg)
  - API 02: `(FT~"Holzappelstraße" OR FT~"Schulverband Zusmarshausen")` + CPV + Zeitfilter → 0
  - XML geöffnet: 426337-2020.
- A (Identität): widersprüchlich  Details: 426337-2020 nennt „Standorte Augsburg und Zusmarshausen“ der Bezirkskliniken, keine Schule, Kita oder
  Stadionstraße.
- B (Objektraum): widersprüchlich  Details: Objektart Klinik (Stationshilfen, Hygienematerial) gegenüber Schule/Schwimmhalle/Kita.
- C (Stütze): Auftraggeber nein, CPV teils, Titel anders, Losstruktur anders.
- Überschneidung der Objekte: 0 von 5.
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: Volltextsuche `FT~"Zusmarshausen"` liefert nur 426337-2020 „Unterhalts- und Glasreinigung … für die Standorte Augsburg und Zusmarshausen“
  der Bezirkskliniken Schwaben; kein Treffer für Markt oder Schulverband Zusmarshausen.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 2/1

### U19 – 129778-2026 (2026-02-24) – Landeshauptstadt München, Direktorium, Vergabestelle 1, SG 1
- Objekt(e): Objekt A: Max-Planck-Gymnasium, Weinbergerstraße 29, 81241 München; Reinigungsfläche Boden ca. 12.828 m², Glas ca. 2.690 m². Ein Los.
- Leistungsart (je Los): Unterhalts- und Glasreinigung (Rahmenvereinbarung).
- Suchschritte:
  - lokal, Suche A: Liste der eForms-Titel der Vergabestelle 1 (siehe U15) → kein Titel mit Weinbergerstraße oder Max-Planck-Gymnasium.
  - lokal, Suche C: `Weinberger|Max-Planck-Gym` vor 20260224 → 1 (421725-2024 Stadt Delmenhorst, Max-Planck-Straße; nicht relevant)
  - API 01: `(FT~"Weinbergerstraße" OR FT~"Weinberger" OR FT~"Max-Planck-Gymnasium")` + CPV + Zeitfilter → 70; davon LH München: 122321-2017
    (competition), 369209-2017 (result), 728662-2022 (Vertragsänderung); übrige andere Städte oder Max-Planck-Institute.
  - XML geöffnet: 122321-2017, 369209-2017, 728662-2022.
- A (Identität): übereinstimmend (Adresse, Gebäudename), Fläche abweichend  Details: 2017 „Weinbergerstraße 29, Max-Planck-Gymnasium; 81241
  München“, Boden 12.281 m², Glas 3.025 m²; 2026 Boden 12.828 m² (+4,5 %), Glas 2.690 m² (−11,1 %). Einzelstandort: Adresse zählt nicht; Fläche
  über 2 % abweichend, das schließt „hoch“ aus. 2017 war ein Erweiterungsneubau mit ca. 2.300 m² zusätzlicher Bodenfläche angekündigt.
- B (Objektraum): erkennbar und übereinstimmend  Details: München 81241 (Pasing), Gymnasium, Unterhalts- und Glasreinigung.
- C (Stütze): Auftraggeber ja (Vergabestelle 1), CPV ja, Titel ähnlich (Leitobjekt Weinbergerstraße 29), Losstruktur gleich (1 Los).
- Überschneidung der Objekte: 1 von 1.
- Ergebnis: **objektgleich_mittel**
- Tendenz (nur bei unklar): –
- Vorgänger: 369209-2017 (result, vor eForms, 2017-09-20) und 122321-2017 (competition, vor eForms, 2017-04-01); dazu Vertragsänderung
  728662-2022 (2022-12-27) desselben Vertrags (Az. 045-Weinbergerstr. 29-05-kli-56/2017).
- Beleg: 369209-2017, II.2.4: „Unterhalts- und Glasreinigung im folgenden städtischen Objekt: Weinbergerstraße 29, Max-Planck-Gymnasium 81241 München
  … Reinigungsfläche Boden: 12 281 m²“.
- Vorgänger mit Vertrag: 369209-2017 (Auftragnehmer ARS Dienstleistungen Gebäudereinigung-Personalservice)
- Vorgänger-Ende: 2022-08-31 (Grundlaufzeit lt. 122321-2017, 2017-10-01 bis 2022-08-31; Verlängerung um max. 12 Monate); laut Änderung 728662-2022
  „Verlängerung der Laufzeit um 12 Monate, neues Ende 31.08.2023“ (§ 132 Abs. 2 Nr. 3 GWB); Herkunft: grundlaufzeit (Höchstende 2023-08-31, durch
  Änderungsbekanntmachung bestätigt)
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-05-01 liegt nach dem Ende)
- Abfragen/XML: 1/3

### U20 – 137428-2026 (2026-02-26) – Stadt Papenburg
- Objekt(e): Schulen im Stadtgebiet Papenburg (26871) inkl. Sporthallen, zusammen ca. 34.000 qm (Angabe in beiden Losen gleich). Los 1 „Oberschulen
  + Amandusschule und Kirchschule inkl. Sporthallen“; Los 2 „Restl. Grundschulen im gesamten Stadtgebiet inkl. Sporthallen“. Keine Adressen,
  keine Einzelflächen.
- Leistungsart (je Los): beide Lose Unterhaltsreinigung, im Einzelfall Grundreinigung auf Abruf.
- Suchschritte:
  - lokal, Suche A/B: `Papenburg` vor 20260226 → 27 Notices; Stadt Papenburg: 281296-2021, 388338-2021, 631504-2022, 55741-2023, 314184-2025,
    346170-2025, 514048-2025 (übrige: Landkreis Emsland, Staatl. Baumanagement, BA, TK, GP Papenburg Hochbau u. a.)
  - API 01: `(FT~"Amandusschule" OR FT~"Kirchschule")` + CPV + Zeitfilter → 0
  - API 02: `buyer-city=Papenburg` + CPV + Zeitfilter → 8 (die sieben genannten Stadt-Papenburg-Notices und 698424-2022 change)
  - lokal: Los-Titel und -Beschreibungen von 314184-2025, 346170-2025, 514048-2025 gelesen.
  - XML geöffnet: 514048-2025, 631504-2022, 281296-2021.
- A (Identität): nicht vergleichbar  Details: Keine Seite nennt Adressen; 2026 nennt nur „Amandusschule“ und „Kirchschule“ namentlich, diese Namen
  kommen auf TED sonst nicht vor (API 01: 0). 514048-2025 hat sieben Lose („Forum Alte Werft“, „Schulen Untenende“, „Sonstige Gebäude“,
  „Aschendorf“, „Schulen Obenende“, „Verwaltungsgebäude“, „Klärwerk“) ohne Objektliste; Fläche nur gesamt „ca. 45.000 qm … Schulen, Sporthallen
  und Verwaltungsgebäuden, Veranstaltungsgebäuden und sonstigen Gebäuden“. Fläche mehrdeutig (andere Zusammensetzung). 281296-2021: ein Los,
  „ca. 33 000 qm, die sich aufteilen in Schulen, Sporthallen und Verwaltungsgebäuden“, ebenfalls ohne Objektliste und mit anderer Flächenart-Zusammensetzung.
  631504-2022: andere Objekte (Forum Alte Werft, Bauhof, Turm Seeschleuse, Jugendzentrum, Multifunktionsgebäude), keine Schulen.
- B (Objektraum): auf Los-Ebene erkennbar und übereinstimmend (2025 Lose 2 und 5 „Schulen Untenende/Obenende“ gegenüber 2026 Lose 1 und 2), als
  Ganzes nicht deckungsgleich  Details: Papenburg, Schulen mit Sporthallen, Unterhaltsreinigung mit Grundreinigung auf Abruf (wortgleicher
  Leistungstext „Gegenstand der Unterhalts- und ggf. Grundreinigungsleistungen ist insbesondere die Reinigung der Fußböden …“). 2025 umfasst
  zusätzlich Verwaltung, Veranstaltungsgebäude, Klärwerk; ob Los „Aschendorf“ Schulen enthält, ist nicht erkennbar.
- C (Stütze): Auftraggeber ja, CPV ja, Titel anders („Unterhaltsreinigung in div. Objekten“ gegenüber „… an Schulen im Stadtgebiet“), Losstruktur
  anders (7 Lose nach Gebiet/Objektgruppe gegenüber 2 Lose nach Schulart).
- Überschneidung der Objekte: nicht bestimmbar (keine Seite mit belegter Objektliste auf beiden Seiten; 0 belegte gemeinsame Objekte).
- Ergebnis: **unklar**
- Tendenz (nur bei unklar): **eher dafür** – gleicher Auftraggeber, wortgleicher Leistungstext, und 2025 enthält ausdrücklich Schul-Lose im selben
  Stadtgebiet; dagegen spricht nur, dass kein einzelnes Objekt beidseitig belegt ist.
- Vorgänger (Kandidat): 514048-2025 (result, eForms, 2025-08-06), dazu 314184-2025 und 346170-2025 (competition, eForms, 2025-05-15 und 2025-05-28),
  Lose 2 („Schulen Untenende“) und 5 („Schulen Obenende“), evtl. 4 („Aschendorf“). Älterer Kandidat gleicher Art: 281296-2021 / 388338-2021.
- Beleg: 514048-2025, Los-Titel „Schulen Untenende“ und „Schulen Obenende“, Beschreibung „ca. 45.000 qm, die sich aufteilen in Schulen, Sporthallen
  und Verwaltungsgebäuden, Veranstaltungsgebäuden und sonstigen Gebäuden“; 137428-2026 Los 1 „Oberschulen + Amandusschule und Kirchschule inkl. Sporthallen“.
- Vorgänger mit Vertrag: 514048-2025 (alle sieben Lose „selec-w“, vergeben)
- Vorgänger-Ende: 2027-07-31 (Lose 2025-08-18 bis 2027-07-31, „verlängert sich maximal zweimal automatisch um jeweils ein weiteres Jahr“); Herkunft:
  grundlaufzeit (Höchstende 2029-07-31)
- Hinweis auf vorzeitige Neuvergabe: ja (neuer Beginn 2026-08-01, 12 Monate vor Ende der Grundlaufzeit des Kandidaten). Nur Fakt; ging nicht ins Urteil ein.
- Abfragen/XML: 2/3

### U21 – 125546-2026 (2026-02-23) – Bundeswehr-Dienstleistungszentrum Landsberg am Lech
- Objekt(e): Kanalnetze der Bundeswehr-Standortbereiche im Zuständigkeitsbereich des BwDLZ Landsberg. Los 1 „Nord“: Standortbereiche Altenstadt (86972)
  und Landsberg (86899); Los 2 „Süd“: Murnau (82418), Oberammergau (82487), Mittenwald (82481). Keine Flächen oder Längen.
- Leistungsart (je Los): beide Lose Kanalreinigung (Rahmenvereinbarung), CPV 90900000/90910000.
- Suchschritte:
  - lokal, Suche A: `Landsberg` mit Auftraggeber Bundeswehr vor 20260223 → 40 Notices des BwDLZ Landsberg (vor eForms ohne Titel); eForms-Titel:
    Unterhaltsreinigung, Dachrinnenreinigung, Gebäudereinigung, Textilien, Speiseabfälle; keine Kanalreinigung.
  - lokal: `Kanal` + Bundeswehr → 0
  - API 01: `(FT~"Kanalreinigung" OR FT~"Kanalreinigungsarbeiten") AND buyer-name~"Landsberg"` + CPV + Zeitfilter → 0
  - API 02: `FT~"Kanalreinigung" AND (FT~"Mittenwald" OR FT~"Oberammergau" OR FT~"Altenstadt")` + CPV + Zeitfilter → 0
  - API 03: `FT~"Kanalreinigung" AND (buyer-city="Landsberg am Lech" OR buyer-city=Penzing OR buyer-city=Landsberg OR buyer-city=Graben)` + CPV + Zeitfilter → 0
  - API 04: `FT~"Kanalreinigung" AND FT~"Bundeswehr"` + CPV + Zeitfilter → 0
  - API 05 (Funktionsprüfung): `FT~"Kanalreinigung" AND classification-cpv=909* AND buyer-country=DEU AND publication-date>=20161001` → 19, darunter der
    Testfall 125546-2026; vor dem Testfall kein BwDLZ-Landsberg-Treffer. Die Syntax funktioniert also.
  - API 06 (**ohne CPV-Filter, außerhalb des Protokolls**, siehe Auffälligkeiten): `(FT~"Kanalreinigung" OR FT~"Kanalspülung" OR FT~"Kanalreinigungsarbeiten")
    AND (FT~"Landsberg" OR FT~"Altenstadt" OR FT~"Mittenwald" OR FT~"Murnau") AND buyer-country=DEU` + Zeitfilter → 8, darunter 528058-2023
    (competition), 213488-2024 (result) „Abschluss RV Kanalreinigung“ (BwDLZ Landsberg) sowie 106338-2023/372862-2023 (BwDLZ Landsberg, Dienstort Lechfeld).
  - XML geöffnet: 213488-2024, 528058-2023, 106338-2023.
- **Wertung nach Protokoll (Nacharbeit 2026-10-25, Entscheidung des Nutzers):** Als Vorgänger zählen nur Bekanntmachungen mit CPV 909…. Innerhalb
  dieses Filters gibt es keinen Kandidaten (API 01–05: 0 Treffer vor dem Testfall). Der Fund 528058-2023 / 213488-2024 hat CPV 90470000 und liegt
  **außerhalb des Protokolls (anderer CPV), nicht gewertet**. Die folgenden Zeilen A bis C beschreiben diesen Fund nur zur Information.
- A (Identität) [Fund außerhalb des Protokolls]: nicht vergleichbar  Details: 528058-2023/213488-2024 nennen keine Standorte („Siehe Verzeichnis der Empfängeranschriften“); keine Längen
  oder Flächen auf beiden Seiten. 106338-2023: widersprüchlich (StOB Fürstenfeldbruck, Starnberg, Lechfeld, keiner der Testfall-Standorte).
- B (Objektraum) [Fund außerhalb des Protokolls]: erkennbar und übereinstimmend (528058-2023/213488-2024)  Details: „Kanalreinigungsarbeiten im Zuständigkeitsgebiet des BwDLZ Landsberg
  am Lech“, Los 1 „Nord“ und Los 2 „Süd“ wie im Testfall; Objektart Kanalnetz der Bundeswehrliegenschaften; Leistungsart Kanalreinigung (Rahmenvertrag).
- C (Stütze) [Fund außerhalb des Protokolls]: Auftraggeber ja, CPV nein (90470000 und 45232410 gegenüber 90900000/90910000), Titel ähnlich („Abschluss RV
  Kanalreinigung“), Losstruktur gleich (Los 1 Nord, Los 2 Süd).
- Überschneidung der Objekte: innerhalb des Protokolls kein Kandidat. Fund außerhalb: Standortliste nur im Testfall (5 Standortbereiche), beim Fund nicht
  aufgeführt; Lose 1↔1 und 2↔2.
- Ergebnis: **kein_vorgaenger** (nach Protokoll; zuerst als objektgleich_mittel eingetragen, auf Entscheidung des Nutzers geändert)
- Tendenz (nur bei unklar): –
- Vorgänger: – (nach Protokoll). Nur zur Information, außerhalb des Protokolls (anderer CPV), nicht gewertet: 213488-2024 (result, eForms, 2024-04-11) und
  528058-2023 (competition, vor eForms, 2023-09-01)
- Beleg: Innerhalb CPV 909* liefert `FT~"Kanalreinigung"` vor dem Testfall keinen BwDLZ-Landsberg-Treffer (API 05). Fund außerhalb: 213488-2024, Beschreibung „Abschluss eines Rahmenvertrages über die Durchführung von Kanalreinigungsarbeiten im Zuständigkeitsgebiet des BwDLZ
  Landsberg am Lech“, Lose „Los 1 - Nord“ und „Los 2 - Süd“, CPV 90470000.
- Vorgänger mit Vertrag: – (nach Protokoll). Zum Fund außerhalb: nicht gefunden; 213488-2024 meldet für beide Lose `winner-selection-status` = „clos-nw“ (beendet ohne Zuschlag), AwardDate
  Platzhalter 2000-01-01. Ein davor liegender Vertrag ist auf TED nicht gefunden (106338-2023 betrifft andere Standorte).
- Vorgänger-Ende: –; Herkunft: – (nach Protokoll). Zum Fund außerhalb: unbekannt, aufgehoben (geplante Laufzeit 2024-12-01 bis 2028-11-30)
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 6/3

### U22 – 109620-2026 (2026-02-16) – Stadt Burghausen
- Objekt(e): Los 3 (einziges Los dieser Bekanntmachung), 24 Objekte der Stadt Burghausen, u. a. Bahnhof (Berliner Platz 2), Bauhof 1 und 2, Bürgerhaus,
  Fotomuseum, Franz-Xaver-Gruber-Schule, FF Burghausen, FF Raitenhaslach, Freizeitheim, Hans-Kammerer-Schule Alt- und Neubau, Hans-Stethaimer-Schule,
  Haus der Familie, J-Hess-Schule, Kindergarten Raitenhaslach, Mautnerschloss, Musikschule, Rathaus (Stadtplatz 112), Schule Raitenhaslach,
  Stadtbibliothek, Stadtmuseum/Zeughaus, Stadtsaal, Turnhalle Raitenhaslach, Turnhalle St. Johann. Keine Flächen.
- Leistungsart (je Los): Los 3 Glasreinigung, Glasreinigung einschließlich Rahmen und Rahmenkomplettreinigung.
- Suchschritte:
  - lokal, Suche A/B: `Burghausen` vor 20260216 → 13 (Stadt Burghausen nur 271924-2020; sonst Hildburghausen, Stadtwerke Burghausen, FA Burghausen,
    Polizei, BA)
  - API 01: `buyer-city=Burghausen` + CPV + Zeitfilter → 2 (271924-2020; 318230-2024 Stadtwerke Burghausen, Bäderbetriebe)
  - API 02: `(FT~"Mautnerschloss" OR FT~"Hans-Kammerer-Schule" OR FT~"Raitenhaslach")` + CPV + Zeitfilter → 1 (271924-2020)
  - XML geöffnet: 271924-2020. Kein Zuschlag zu 271924-2020 in den Rohdaten oder der API.
- A (Identität): Objektliste weitgehend übereinstimmend  Details: 271924-2020 Los 1 (12 Objekte) und Los 2 (14 Objekte) nennen u. a. Bahnhof, Bibliothek,
  Fotomuseum, Franz-Xaver-Gruber-Schule, Hans-Kammerer-Schule, Rathaus, Stadtmuseum, Stadtsaal, Bauhof, Bürgerhaus, Freizeitheim, Joh-Hess-Schule,
  Mautnerschloss, Musikschule, Turnhalle Raitenhaslach, Schule Raitenhaslach, Turnhalle St. Johann.
- B (Objektraum): widersprüchlich  Details: Leistungsart 2020 „Gebäudereinigung (Unterhalts- und Grundreinigung)“, nur CPV 90911200, das Wort „Glas“
  kommt in der XML nicht vor; Testfall Glas- und Rahmenreinigung. Andere Leistungsart gilt als Widerspruch.
- C (Stütze): Auftraggeber ja, CPV nein, Titel anders, Losstruktur anders (2 Lose UR/GR gegenüber Los 3 Glas). Aktenzeichen 2020 „35-2019 UHR_Gla“
  (Stufe C, gleicht keinen Widerspruch aus).
- Überschneidung der Objekte: ca. 17 von 24 namentlich gemeinsam, aber andere Leistungsart.
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: 271924-2020, II.1.4: „Erbringung von Dienstleistungen im Bereich der Gebäudereinigung (Unterhalts- und Grundreinigung) für die Stadt Burghausen“,
  CPV 90911200; 109620-2026: „Glasreinigung, Glasreinigung einschl. Rahmen (ohne Falze) und … Rahmenkomplettreinigung“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 2/1

### U23 – 2335-2026 (2026-01-05) – Freistaat Bayern vertreten durch das Bayerische Landesamt für Steuern
- Objekt(e): Finanzamt Kitzingen, Sophienstr. 6, 97318 Kitzingen (Einzelstandort). Los 1: Grundfläche ca. 2.944,51 qm, Jahresreinigungsfläche ca.
  302.990,33 qm. Los 2: Glasfläche ca. 623,33 qm.
- Leistungsart (je Los): Los 1 Unterhaltsreinigung; Los 2 Glas- und Rahmenreinigung.
- Suchschritte:
  - lokal, Suche A/B: `Kitzingen` vor 20260105 → 23 (Landratsamt/Landkreis Kitzingen, Klinik, BA, AOK, Staatsarchiv, Stadt Kitzingen; Landesamt für
    Steuern nicht, weil Auftraggeber-Ort München und Titel vor eForms fehlen)
  - API 01: `(FT~"Kitzingen") AND (FT~"Finanzamt" OR FT~"FA")` + CPV + Zeitfilter → 11, darunter 450593-2020 (competition) und 598365-2020 (result) des
    Landesamts für Steuern; 494017-2020 Regierung von Oberbayern.
  - XML geöffnet: 450593-2020, 598365-2020, 494017-2020 (Zentrale Ausländerbehörde Geldersheim, Bieter aus Kitzingen; nicht relevant).
- A (Identität): übereinstimmend (Fläche)  Details: 450593-2020 „Unterhaltsreinigung für das FA Kitzingen“, „Grundfläche: ca. 2 904,51“; Testfall Los 1
  „Grundfläche ca. 2.944,51 qm“, Abweichung +1,4 % (innerhalb 2 %, gleiche Flächenart Grundfläche UR). Einzelstandort: Adresse/Name zählt nicht; nur
  ein weiteres A-Merkmal (Fläche), Geschosse/Gebäudeteile nicht genannt.
- B (Objektraum): erkennbar und übereinstimmend für Los 1  Details: Finanzamt Kitzingen, Unterhaltsreinigung. Los 2 (Glas- und Rahmenreinigung) hat in
  450593-2020 keine Entsprechung; 2020 war nur Unterhaltsreinigung ausgeschrieben.
- C (Stütze): Auftraggeber ja (Zentrale Vergabestelle des Landesamts für Steuern), CPV ja, Titel ähnlich, Losstruktur anders (1 Los gegenüber 2 Losen);
  Vertragsklausel fast wortgleich („tritt am … in Kraft und gilt zunächst bis … verlängert sich je um ein weiteres Jahr“).
- Überschneidung der Objekte: 1 von 1 (Lose mit Überschneidung: Testfall Los 1 ↔ 2020 einziges Los).
- Ergebnis: **objektgleich_mittel** (bezogen auf Los 1; Los 2 Glas ohne Vorgänger)
- Tendenz (nur bei unklar): –
- Vorgänger: 598365-2020 (result, vor eForms, 2020-12-11) und 450593-2020 (competition, vor eForms, 2020-09-25), Az. 2020MRB000005
- Beleg: 598365-2020, II.2.4 „Unterhaltsreinigung für das FA Kitzingen“, „Grundfläche: ca. 2 904,51“, Zuschlag an „win gemeinnützige GmbH“, Vertrag 2020-12-07.
- Vorgänger mit Vertrag: 598365-2020
- Vorgänger-Ende: Grundlaufzeit 2024-04-30, Höchstende 2027-04-30 (450593-2020: „tritt am 1.5.2021 in Kraft und gilt zunächst bis zum 30.4.2024 … verlängert
  sich je um ein weiteres Jahr … endet spätestens mit Ablauf des 30.4.2027“); Herkunft: grundlaufzeit (danach rollierend bis Höchstende)
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-05-01 liegt nach dem Ende der Grundlaufzeit; vor dem Höchstende)
- Abfragen/XML: 1/3

### U24 – 98964-2026 (2026-02-11) – Gemeinde Graal Müritz
- Objekt(e): öffentliche Toiletten im Gemeindegebiet Graal-Müritz (Leistungsort Ribnitzer Straße 21, 18181). Keine Objektliste, keine Flächen.
- Leistungsart (je Los): ein Los, Unterhaltsreinigung ganzjährig und saisonal (CPV 90910000).
- Suchschritte:
  - lokal, Suche A/B: `Graal` vor 20260211 → 1 (134543-2024 Nordwasser GmbH, Rostock; Leistungsort „Einzugsbereich Nordwasser GmbH (Rostock,
    Graal-Müritz, Tessin, Sanitz, etc.)“)
  - API 01: `(FT~"Graal-Müritz" OR FT~"Graal Müritz" OR FT~"Graal")` + CPV + Zeitfilter → 3 vor dem Testfall (616781-2019, 238386-2020 EDF SA Paris;
    134543-2024 Nordwasser), dazu 21695-2026 (Nordwasser, 2026-01-13)
  - API 02: `FT~"Toiletten" AND (FT~"Ostseebad" OR FT~"Ribnitzer")` + CPV + Zeitfilter → 0
  - XML geöffnet: keine (Kandidaten nach Rohdaten-Feldern eindeutig anders).
- A (Identität): nicht vergleichbar (keine Objektliste auf beiden Seiten).
- B (Objektraum): widersprüchlich  Details: Nordwasser GmbH reinigt Betriebsgebäude eines Wasserversorgers im Einzugsbereich mehrerer Gemeinden
  („Unterhalts- und Sonderreinigung“), Testfall öffentliche Toiletten der Gemeinde; EDF SA (Frankreich) ohne Bezug.
- C (Stütze): Auftraggeber nein, CPV teils, Titel anders, Losstruktur gleich (1 Los).
- Überschneidung der Objekte: 0.
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: 134543-2024, Feld place-performance-street-lot „Einzugsbereich Nordwasser GmbH (Rostock, Graal-Müritz, Tessin, Sanitz, etc.)“, Auftraggeber
  Nordwasser GmbH; Testfall 98964-2026 „Reinigungsdienstleistungen für die Öffentlichen Toiletten im Gemeindegebiet“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 2/0

### U25 – 209981-2026 (2026-03-26) – Stadt Ingolstadt
- Objekt(e): Kindergarten und Kinderkrippe Grüne Insel, Auf der Höh 1 und 5, 85049 Ingolstadt; Flächen Kindergarten 573,16 m², Krippe 465,05 m², gesamt
  1.038,20 m². Ein Los. Aktenzeichen 664-0007-2026-F-IN.
- Leistungsart (je Los): Gebäudereinigung (CPV 90911000), 48 Monate mit Verlängerungsoption.
- Suchschritte:
  - lokal, Suche A: `buyer-name: Stadt Ingolstadt` ab 20231001 vor 20260326 → ca. 70 Notices, eForms-Titel nach Objekten durchgesehen.
  - lokal, Suche C: `Gr.ne Insel|Auf der H.h` → 757743-2023, 629441-2024, 184953-2025 (übrige Gemeinde Gersheim, nicht relevant)
  - API 01: `(FT~"Grüne Insel" OR FT~"Auf der Höh")` + CPV + Zeitfilter → 12 (Ingolstadt: 757743-2023, 629441-2024, 184953-2025; übrige andere Städte)
  - API 02 (Zuschlagssuche zu 629441-2024): `(FT~"Mariengarten" OR FT~"Südwind") AND buyer-city=Ingolstadt` + Zeitfilter (ohne CPV) → 3, kein Zuschlag zu 629441-2024
  - lokal: `Mariengarten|S.dwind|Irgertsheim` → kein Zuschlag zu 629441-2024
  - XML geöffnet: 757743-2023, 629441-2024, 184953-2025, 98958-2026 (Kitas Am Eichenwald, Am Nordpark, Blauland; nicht Grüne Insel).
- A (Identität): übereinstimmend  Details: Gebäudename „Grüne Insel“ (Kindergarten/KiTa und Krippe) auf allen Seiten; Teilfläche Krippe 465,05 m² in 2023,
  2024 und 2026 identisch; Kindergarten/KiTa 562,32 m² (2023, 2024) gegenüber 573,16 m² (2026), +1,9 % (innerhalb 2 %). Gebäudeteile (Kindergarten +
  Krippe) gleich. Adresse „Auf der Höh 1 und 5“ nur 2026; PLZ 2024 und 2026 85049, 2023 Lieferort 85053 (Einzelangabe, nicht als Widerspruch gewertet).
- B (Objektraum): erkennbar und übereinstimmend  Details: Ingolstadt, Kindergarten/Krippe, Gebäudereinigung (CPV 90911200 bzw. 90911000).
- C (Stütze): Auftraggeber ja, CPV ähnlich, Titel ähnlich, Losstruktur anders (2023: 2 Lose; 2024: 3 Lose; 2026: 1 Los).
- Überschneidung der Objekte: 629441-2024: 1 von 1 (Testfall) in 3 Objekten/Losen (Kindergarten Auf der Höh Irgertsheim 682,72 m², Kindergarten Mariengarten
  Geb. A/B, Kindergarten Grüne Insel); 757743-2023: 1 von 1 in 2 Objekten (Grüne Insel, Kiga Südwind 528,00 m²). Lose mit Überschneidung: 2024 Los 3,
  2023 Los 1. Die kürzere Seite (Testfall) schließt nichts ausdrücklich aus.
- Ergebnis: **teilmenge** (auf Los-Ebene wäre es objektgleich mit zwei übereinstimmenden Teilflächen)
- Tendenz (nur bei unklar): –
- Vorgänger: jüngstes Verfahren 629441-2024 (competition, eForms, 2024-10-17, Az. 664-0024-2024-F-IN, Los 3 „Kindergarten Grüne Insel“). Davor
  757743-2023 (competition, eForms, 2023-12-14, Los 1) mit Zuschlag 184953-2025 (result, eForms, 2025-03-21, Az. 664-0029-2023-F-IN).
- Beleg: 629441-2024, Los 3 „Kindergarten Grüne Insel“: „KiTa Grüne Insel: 562,32m² Krippe Grüne Insel: 465,05m²“; 209981-2026: „Kindergarten 573,16 m²
  Krippe 465,05 m²“.
- Vorgänger mit Vertrag: zu 629441-2024 kein Zuschlag auf TED gefunden. Letzter belegter Vertrag: 184953-2025, Los 1 „Kindergarten und Krippe Grüne Insel“,
  `selec-w`, Auftragnehmer mit Sitz Bachweg 5 A, 86565.
- Vorgänger-Ende: unbekannt für 629441-2024; für 184953-2025/757743-2023: Beginn 2024-03-01, Laufzeit 48 Monate, also rechnerisch 2028-02-29, „mit Option auf
  Verlängerung um jeweils ein Jahr“ (ohne Höchstzahl); Herkunft: unbekannt (jüngstes Verfahren ohne Zuschlag); für den Vertrag von 2024 grundlaufzeit (berechnet)
- Hinweis auf vorzeitige Neuvergabe: unklar (Beginn im Testfall nicht angegeben; außerdem wurde Grüne Insel schon im Oktober 2024 erneut ausgeschrieben,
  obwohl der Vertrag aus dem Verfahren von 2023 ab 2024-03-01 für 48 Monate lief)
- Abfragen/XML: 2/4

### U26 – 84590-2026 (2026-02-05) – Land Hessen, vertreten durch das Hessische Competence Center (HCC)
- Objekt(e): Erstaufnahmeeinrichtung Hessen (EAEH) Bad Arolsen, 34454 Bad Arolsen, für den Landesbetrieb Bau und Immobilien Hessen, NL Nord.
  Jahresreinigungsfläche ca. 1.096.447 m² (Vollreinigung ca. 1.048.764 m², Sichtreinigung ca. 47.683 m²); ca. 150 Zimmer pro Jahr; Mensa mit 112 Plätzen. Ein Los.
- Leistungsart (je Los): Unterhaltsreinigung sowie Zimmerreinigung/-desinfektion (CPV 90910000).
- Suchschritte:
  - lokal, Suche B: `Arolsen` vor 20260205 → 4 (BA Glasreinigung RIM Gießen, AOK Hessen; keine EAEH)
  - API 01: `FT~"Arolsen"` + CPV + Zeitfilter → 23; HCC: 576059-2019/97362-2020, 662237-2021/186591-2022, 369443-2023/541700-2023; übrige AOK, pronova BKK,
    Stadt Frankfurt, Landkreis Waldeck-Frankenberg, DRV Hessen, BA.
  - API 02: `(FT~"EAEH" OR FT~"Erstaufnahmeeinrichtung" OR FT~"Erstaufnahme") AND (FT~"Arolsen" OR FT~"Hessen")` + CPV + Zeitfilter → 22 (HCC-Verfahren für
    HEAE Gießen, Fuldatal, Friedberg u. a.; Hanau, Lahn-Dill-Kreis); keines nennt Bad Arolsen (sonst wäre es in API 01 enthalten).
  - API 03: `FT~"Wilhelminenstraße" AND buyer-city=Wiesbaden` + CPV + Zeitfilter → 718 (Wilhelminenstraße 1–3 ist die Anschrift des HCC, nicht des Objekts;
    nicht ausgewertet)
  - XML geöffnet: 369443-2023 (Innenreinigung Polizeifahrzeuge), 662237-2021 (Straßenmeistereien Bad Arolsen, Bad Wildungen, Frankenberg, Korbach,
    Friedberg), 576059-2019 (4 Objekte in Bad Arolsen und Waldeck, u. a. Polizeistation Uplandstraße 4 und Wasserschutzpolizei).
- A (Identität): widersprüchlich  Details: Kein Kandidat nennt die EAEH; die Bad-Arolsen-Objekte der Kandidaten sind Straßenmeisterei (Marsbergerstr. 3),
  Polizeistation (Uplandstraße 4) bzw. Polizeifahrzeuge.
- B (Objektraum): widersprüchlich  Details: Objektart Straßenmeisterei/Polizei gegenüber Erstaufnahmeeinrichtung; 369443-2023 zudem andere Leistungsart
  (Kfz-Innenreinigung).
- C (Stütze): Auftraggeber ja (HCC), CPV teils, Titel anders, Losstruktur anders.
- Überschneidung der Objekte: 0 von 1.
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: 662237-2021, Los 1 „Straßenmeisterei Bad Arolsen, Marsbergerstr. 3, 34454 Bad Arolsen“ und 576059-2019 „Polizeistation Uplandstraße 4, 34454 Bad Arolsen“
  sind die einzigen Bad-Arolsen-Objekte des HCC; 84590-2026 „Unterhaltsreinigung in der EAEH Bad Arolsen“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 3/3

### U27 – 92834-2026 (2026-02-09) – Landesbaudirektion Bayern
- Objekt(e): „Lehrgangsgebäude in München“, Schulungsgebäude mit Seminarräumen, Küche und Übernachtungszimmern, ca. 1.870 m² Reinigungsfläche;
  Leistungsort nur „München 80539“ (keine Straße). Ein Los. Einzelstandort.
- Leistungsart (je Los): Gebäudeinnenreinigung als laufende Unterhaltsreinigung einschließlich Sonderreinigungen (CPV 90911100, 90919300).
- Suchschritte:
  - lokal, Suche A: `Landesbaudirektion` vor 20260209 → 74 Notices (vor eForms ohne Titel); eForms-Titel: Dienstgebäude Krumbach, Amberg, Rosenheim,
    Weilheim, Würzburg, Ingolstadt, München (455679-2024: „DG PAS“, „DG SA“, 81547, 9.990 und 2.990 m²), Straßenmeistereien; kein Lehrgangsgebäude.
  - lokal, Suche C: `Lehrgang` → 3 (BImA; nicht relevant)
  - API 01: `(FT~"Lehrgangsgebäude" OR FT~"Lehrgangsgebaeude")` + CPV + Zeitfilter → 2 (1067-2021 competition, 53568-2021 change; Landesbaudirektion Bayern)
  - API 02 (Zuschlagssuche): `(FT~"Heßstraße" OR FT~"Hessstraße" OR FT~"LBD-20-15-102")` + CPV + Zeitfilter → 11 (1067-2021, 53568-2021; übrige
    Wasserwirtschaftsamt, LH München, Regierung von Oberbayern, StMAS), kein Zuschlag zu LBD-20-15-102.
  - XML geöffnet: 1067-2021, 53568-2021.
  - **Nacharbeit 2026-10-25 (Prüfung des Leistungsorts):**
    - Testfall-XML 92834-2026 vollständig auf Ortsangaben durchgesehen: Beide `RealizedLocation`-Blöcke (Verfahren und Los) enthalten nur „München“,
      PostalZone „80539“, NUTS DE212. Es gibt keine Straße, keinen Zusatztext zum Leistungsort (BT-728) und keine Gebäudebezeichnung außer
      „Lehrgangsgebäude in München“. Die einzigen Straßen gehören dem Auftraggeber (Marktplatz 30, 96106 Ebern), der Vergabekammer (Promenade 27,
      Ansbach) und dem Datenservice (Bonn). Dass 80539 eine Verwaltungsadresse wäre, geht aus der Bekanntmachung nicht hervor.
    - lokal (Rohdaten, vor 20260209), Muster `He(ß|ss)str` mit PLZ: 273234-2024, 294242-2024, 409863-2024 „Heßstraße 130, 80797 München“ (Regierung von
      Oberbayern); 94037-2025, 282374-2025 „Heßstraße 104, 80797 München“ (StMAS). Jede auf TED belegte Heßstraße-Adresse hat PLZ 80797. (463288-2026,
      „Heßstraße 28, 80797“, liegt nach dem Testfall und dient nur als Ortsbeleg, nicht als Kandidat.)
    - API 03: `FT~"80539" AND (buyer-city=Ebern OR buyer-city=Nürnberg OR FT~"Landesbaudirektion")` + CPV + Zeitfilter → 3 (Autobahndirektion Nordbayern
      378791-2016, Nationalparkverwaltung Bayerischer Wald 568982-2024/723564-2024); kein Lehrgangsgebäude, keine Erklärung für 80539.
    - API 04: `(FT~"Lehrgang" OR FT~"Schulungsgebäude" OR FT~"Übernachtungszimmern") AND buyer-city=Ebern` + CPV + Zeitfilter → 0.
    - Kein weiteres XML geöffnet. Ob es die Heßstraße oder ein anderes Gebäude ist, lässt sich mit TED-Daten nicht positiv entscheiden.
- A (Identität): widersprüchlich (Adresse/PLZ); gleich ist nur die Gattungsbezeichnung  Details: 1067-2021 „Unterhaltsreinigung des Lehrgangsgebäudes in
  München, Heßstraße“, keine Fläche, keine PLZ; Testfall „Lehrgangsgebäude in München“, 1.870 m², Leistungsort PLZ 80539. Die Heßstraße hat auf TED
  durchgehend PLZ 80797. Fläche nicht vergleichbar. „Lehrgangsgebäude“ ist eine Gattungsbezeichnung, kein Eigenname.
- B (Objektraum): widersprüchlich (Gebiet)  Details: Leistungsort 80539 gegenüber Heßstraße (80797), also ein anderer Postleitzahlbereich in München.
  Objektart (Lehrgangsgebäude) und Leistungsart (Unterhaltsreinigung) stimmen überein.
- C (Stütze): Auftraggeber ja, CPV ähnlich (90911000 gegenüber 90911100/90919300), Titel ähnlich, Losstruktur gleich (1 Los); Verlängerungsklausel
  gleich gebaut („Jährliche Verlängerungsoption bis maximal …“).
- Überschneidung der Objekte: 0 belegt gemeinsam (gleiche Gattungsbezeichnung, aber abweichender Leistungsort).
- Ergebnis: **kein_vorgaenger** (zuerst objektgleich_mittel; nach der Nacharbeit geändert)
- Tendenz (nur bei unklar): –
- Begründung der Änderung: Der Leistungsort des Testfalls (PLZ 80539) widerspricht der Heßstraße des Kandidaten (auf TED stets 80797). Dass 80539 nur ein
  Platzhalter oder eine Verwaltungsadresse ist, lässt sich aus TED nicht belegen. Nach Urteilsregeln 1.1 (anderer Stadtteil bzw. andere Adresse =
  Widerspruch) und der Rangfolge bei Zweifel gilt das vorsichtigere Urteil „nicht objektgleich“. Damit bleibt kein Kandidat, der objektgleich, Teilmenge
  oder unklar wäre. Alternative Lesart (nicht gewertet): Wäre 80539 ein Platzhalter, ergäbe das Paar objektgleich_mittel.
- Vorgänger: – (geprüfter, verworfener Kandidat: 1067-2021 competition vor eForms, 2021-01-04, mit Berichtigung 53568-2021, Vergabe-Nr. LBD-20-15-102)
- Beleg: 1067-2021, II.1.4 „Unterhaltsreinigung des Lehrgangsgebäudes in München, Heßstraße“; 92834-2026, Leistungsort „München 80539“; 409863-2024
  „Heßstraße 130, 80797 München“.
- Vorgänger mit Vertrag: – (zu 1067-2021 gibt es auch keinen Zuschlag auf TED)
- Vorgänger-Ende: –; Herkunft: – (nur zur Information zum verworfenen Kandidaten: Laufzeit 2021-05-01 bis 2023-04-30, Verlängerung bis maximal 30.4.2026)
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 4/2

### U28 – 54141-2026 (2026-01-26) – Berufsgenossenschaft Verkehrswirtschaft Post-Logistik Telekommunikation (BG Verkehr)
- Objekt(e): Los 3 von 8 (je Los eine eigene Bekanntmachung): Bezirksverwaltung Berlin der BG Verkehr, Axel-Springer-Straße 52, 10969 Berlin. Keine Fläche
  in der Bekanntmachung. Einzelstandort.
- Leistungsart (je Los): Unterhaltsreinigung (CPV 90911200).
- Suchschritte:
  - lokal, Suche A/B: `BG Verkehr|Berufsgenossenschaft Verkehr|Axel-Springer` vor 20260126 → 5 (BG Verkehr 404919-2019, 552382-2019 mit Sitz Tübingen;
    BARMER „UGR-Campus“ 486239-2024, 587117-2024, 733341-2024)
  - API 01: `(FT~"Axel-Springer-Straße" OR FT~"BG Verkehr" OR FT~"Berufsgenossenschaft Verkehrswirtschaft")` + CPV + Zeitfilter → 7 (dieselben sowie BARMER
    237251-2017/449689-2017)
  - API 02: `(FT~"Bezirksverwaltung Berlin" OR FT~"Berufsgenossenschaft für Transport" OR FT~"BG Transport")` + CPV + Zeitfilter → 7 (BGW Bezirksverwaltung
    Berlin, VBG Hamburg; keine BG Verkehr)
  - lokal: Lostexte von 733341-2024 (BARMER) gelesen: Leistungsort „Axel-Springer-Straße 44-47“.
  - XML geöffnet: 404919-2019, 552382-2019.
- A (Identität): widersprüchlich  Details: 404919-2019 Leistungsort NUTS DE14 / Tübingen („Gebäudeinnenreinigung monatlich ca. 75 500 qm“), nicht Berlin;
  BARMER: Axel-Springer-Straße 44–47 statt 52 (andere Adresse, anderer Auftraggeber).
- B (Objektraum): widersprüchlich  Details: BG Verkehr 2019 anderes Gebiet (Tübingen); BARMER anderes Objekt (Campus der BARMER).
- C (Stütze): 404919-2019: Auftraggeber ja, CPV ja, Titel anders, Losstruktur anders (Gebäude-/Glasreinigung in 2 Losen).
- Überschneidung der Objekte: 0 von 1.
- Ergebnis: **kein_vorgaenger**
- Tendenz (nur bei unklar): –
- Vorgänger: –
- Beleg: 404919-2019, PERFORMANCE_NUTS „Tübingen“ (DE14) für „Gebäudereinigung (Los 1) und Glasreinigung (Los 2)“; 54141-2026 Leistungsort
  „Axel-Springer-Straße 52 10969 Berlin“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: –; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 2/2

## Übersichtstabelle

| U | Notice | Ergebnis | Tendenz | jüngster Vorgänger | alle Notices desselben Vorgängers | Vorgänger mit Vertrag | Vorgänger-Ende | Herkunft | vorzeitig |
|---|---|---|---|---|---|---|---|---|---|
| U15 | 84022-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U16 | 122844-2026 | objektgleich_mittel | – | 181605-2024 | 50843-2024, 181605-2024 | 181605-2024 | 2028-04-30 | grundlaufzeit | ja |
| U17 | 93297-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U18 | 221159-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U19 | 129778-2026 | objektgleich_mittel | – | 369209-2017 | 122321-2017, 369209-2017, 728662-2022 (Änderung) | 369209-2017 | 2022-08-31 (verlängert bis 2023-08-31) | grundlaufzeit | nein |
| U20 | 137428-2026 | unklar | eher dafür | 514048-2025 (Kandidat) | 314184-2025, 346170-2025, 514048-2025 | 514048-2025 | 2027-07-31 | grundlaufzeit | ja |
| U21 | 125546-2026 | kein_vorgaenger | – | – (Fund 213488-2024 / 528058-2023 außerhalb des Protokolls, CPV 90470000, nicht gewertet) | – | – | – | – | – |
| U22 | 109620-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U23 | 2335-2026 | objektgleich_mittel | – | 598365-2020 | 450593-2020, 598365-2020 | 598365-2020 | 2024-04-30 (Höchstende 2027-04-30) | grundlaufzeit | nein |
| U24 | 98964-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U25 | 209981-2026 | teilmenge | – | 629441-2024 | 629441-2024; früheres Verfahren 757743-2023, 184953-2025 | zu 629441-2024 nicht gefunden; zuletzt 184953-2025 | unbekannt (Vertrag 2024: rechnerisch 2028-02-29) | unbekannt | unklar |
| U26 | 84590-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U27 | 92834-2026 | kein_vorgaenger | – | – (Kandidat 1067-2021 verworfen: Leistungsort 80539 gegenüber Heßstraße 80797) | – | – | – | – | – |
| U28 | 54141-2026 | kein_vorgaenger | – | – | – | – | – | – | – |

## Übersicht (Fakten)

| Kategorie | Anzahl | Fälle |
|---|---|---|
| objektgleich_hoch | 0 | – |
| objektgleich_mittel | 3 | U16, U19, U23 |
| teilmenge | 1 | U25 |
| unklar | 1 (Tendenz eher dafür: 1) | U20 |
| kein_vorgaenger | 9 | U15, U17, U18, U21, U22, U24, U26, U27, U28 |
| **Summe** | **14** | |

- Objektgleich oder Teilmenge: 4 von 14; nur objektgleich: 3 von 14; zusammen mit „unklar, eher dafür“: 5 von 14.
- Änderung gegenüber der ersten Fassung (Nacharbeit 2026-10-25): U21 (Entscheidung des Nutzers: nur CPV 909…) und U27 (Prüfung des Leistungsorts) von
  objektgleich_mittel auf kein_vorgaenger; Gründe in den Fallprotokollen.
- **Fälle mit Abbruch durch Budget:** keiner. Höchstwerte: 6 API-Abfragen (U21), 5 Kandidaten-XML (U15). Summe: 36 API-Abfragen (davon 2 aus der Nacharbeit zu U27), 34 Kandidaten-XML
  (dazu 14 Testfall-XML).
- Vorgänger vor eForms: U19, U23 (jeweils nur über `FT` gefunden, weil die API vor eForms keine Titel liefert); eForms: U16, U25; Kandidat U20 eForms.
- Vorgänger-Ende aus einem Zuschlag mit Herkunft grundlaufzeit: U16, U19, U23 (U20 nur für den Kandidaten).
  Unbekannt: U25 (jüngstes Verfahren ohne Zuschlag).

## Grenzfälle der Regeln

- **U20 (Papenburg):** Der Kandidat 514048-2025 enthält Schul-Lose („Schulen Untenende“, „Schulen Obenende“) im selben Stadtgebiet, nennt aber keine
  einzelne Schule; die Bekanntmachung als Ganzes ist breiter (Verwaltung, Veranstaltungsgebäude, Klärwerk). Die Urteilsregeln regeln „Teilmenge“ nur über
  belegte Objektlisten und „objektgleich“ nur bei nahezu deckungsgleichen oder einseitig fehlenden Listen. Der Fall „passt auf Los-Ebene, ist als Ganzes
  breiter, und die breitere Seite hat keine Liste“ ist nicht vorgesehen. Nach Anweisung daher **unklar** statt einer neuen Auslegung (Tendenz eher dafür).
- **U25 (Ingolstadt):** Auf Los-Ebene wäre das Paar objektgleich (Krippe 465,05 m² identisch, Kindergarten +1,9 %, gleiche Gebäudeteile); als Ganzes enthält
  jeder Vorgänger weitere Objekte. Nach Regel 7 (Bekanntmachung als Ganzes) und der Rangfolge vergebe ich **teilmenge** (wie im Kalibrierungsbeispiel
  Stralsund). Für W1 macht das keinen Unterschied, für die Sicherheitsstufe schon.

- **U27 (Landesbaudirektion, Lehrgangsgebäude):** Die eine Seite nennt nur eine PLZ (80539), die andere nur eine Straße (Heßstraße, auf TED stets 80797).
  Ob die PLZ den Leistungsort trägt oder ein Platzhalter ist, regeln die Urteilsregeln nicht. Entschieden nach der Rangfolge bei Zweifel: nicht
  objektgleich, also kein_vorgaenger.

## Auffälligkeiten

Fakten (mit Notice-Nummer):
- **Zentrale Vergabestellen:** U15 und U19 (LH München, Vergabestelle 1; Titel je Verfahren nach der ersten Objektadresse, rund 100 eForms-Verfahren seit
  10/2023); U23 (Bayerisches Landesamt für Steuern, Zentrale Vergabestelle; Auftraggeber-Ort München statt Objektort); U26 (HCC Hessen; die Anschrift
  Wilhelminenstraße 1–3 steht in jeder HCC-Bekanntmachung und ist als Suchbegriff unbrauchbar: 718 Treffer); U27 (Landesbaudirektion Bayern, Sitz Ebern,
  Objekt in München).
- **U27, Leistungsort nur als PLZ:** Der Testfall nennt als Leistungsort nur „München 80539“ ohne Straße; der Kandidat 1067-2021 nennt die Heßstraße ohne
  PLZ. Auf TED hat die Heßstraße stets PLZ 80797 (409863-2024, 282374-2025). Nach der Rangfolge wurde der Kandidat verworfen.
- **Möglicher Vorgänger außerhalb des CPV-Filters (nicht gewertet):** U21. 528058-2023/213488-2024 („Abschluss RV Kanalreinigung“, BwDLZ Landsberg, Lose
  Nord/Süd) hat CPV 90470000 (und 45232410), nicht 909…, und wurde nur mit einer Abfrage **ohne** `classification-cpv=909*` gefunden (API 06). Nach
  Entscheidung des Nutzers zählt er nicht; U21 ist `kein_vorgaenger`. Inhaltlich hätte der Fund objektgleich_mittel ergeben (gleicher Auftraggeber, gleiche
  Leistung, gleicher Losschnitt). Das Verfahren endete ohne Zuschlag („clos-nw“). Der Testfall selbst hat CPV 90900000/90910000.
- **Aufgehobene bzw. ohne Zuschlag gebliebene Verfahren:** U25 (629441-2024, kein Zuschlag auf TED); außerdem bei den nicht gewerteten bzw. verworfenen
  Kandidaten U21 (213488-2024, beide Lose „clos-nw“, AwardDate-Platzhalter 2000-01-01) und U27 (1067-2021, kein Zuschlag auf TED).
- **Neuausschreibung vor Ablauf (nur Daten, nicht im Urteil):** U16 (Vertrag 2024-05-01 bis 2028-04-30, Neubeginn 2026-05-01); U20 (Kandidat bis
  2027-07-31, Neubeginn 2026-08-01); U25 (Grüne Insel im Oktober 2024 erneut ausgeschrieben, obwohl der Vertrag aus 757743-2023 ab 2024-03-01 für 48 Monate lief).
- **Lücke nach dem Vorgänger:** U19. Der Vertrag wurde bis 2023-08-31 verlängert (728662-2022), der Neubeginn ist 2026-05-01; für 2023 bis 2026 ist auf TED
  kein Verfahren zu finden.
- **Abweichende Adressangaben innerhalb einer Notice:** U16 (50843-2024/181605-2024: Titel „Tatzendpromenade 9“, Leistungsort-Feld „Tatzendpromenade 3“);
  U25 (757743-2023 Leistungsort 85053, 629441-2024 und Testfall 85049).
- **Gleiche Objekte, andere Leistungsart:** U22 (Burghausen 2020: Unterhalts- und Grundreinigung für etwa 17 der 24 Objekte; 2026 Glas- und Rahmenreinigung)
  und U17 (Islandstraße 25 nur als Baureinigung, 742468-2023). Nach der Regel „andere Leistungsart = Widerspruch“ jeweils kein Vorgänger.
- **U23:** Der Vorgänger von 2020 war nur Unterhaltsreinigung (1 Los). Der Testfall hat zusätzlich Los 2 Glas- und Rahmenreinigung ohne Vorgänger. Das Urteil
  bezieht sich auf Los 1 (Regel 7).
- **Name des Auftraggebers:** Die BG Verkehr (U28) trat 2019 mit Sitz Tübingen auf; der frühere Name „BG für Transport und Verkehrswirtschaft“ bringt keine Treffer.
- **Volltextsuche:** `FT~"Islandstr"` liefert 0, `FT~"Islandstraße"` 2 Treffer (U17); `FT` trifft offenbar nur ganze Wörter. Breite ODER-Gruppen ohne weitere
  Einschränkung liefern zu viel (192 Treffer bei U15, API 02).

Einschätzungen (nicht Teil der Urteile):
- U27: Möglich bleibt, dass 80539 nur eine Verwaltungs- oder Platzhalterangabe ist und das Lehrgangsgebäude doch in der Heßstraße liegt; TED enthält dafür
  keinen Beleg. Für das Urteil zählt nur der belegte Widerspruch (80539 gegenüber 80797). Klären ließe es sich über die Vergabeunterlagen
  (meinauftrag.rib.de, tenderId 292350); sie gehören nicht zu den erlaubten Quellen.
- U21: Ob Kanalreinigung zur Nische „Gebäudereinigung“ gehört, ist fraglich. Der Fall zeigt aber, dass Vorgänger unter einer anderen CPV liegen können.
- U18, U24, U26: Bei kleinen Gemeinden bzw. neuen Einrichtungen (EAEH Bad Arolsen) ist eine erstmalige EU-weite Ausschreibung plausibel. Ob es national
  bekanntgemachte Vorgänger gibt, wurde nicht geprüft.
