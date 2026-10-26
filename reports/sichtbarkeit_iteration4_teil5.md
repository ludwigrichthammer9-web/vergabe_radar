# Sichtbarkeit der Vorgänger – Handsuche Iteration 4, Teil 5 (U57–U70)

- **Datum:** 2026-10-26
- **Bearbeiter:** Subagent `rechercheur` (Auftrag „Handsuche“)
- **Testfälle:** Zeilen 57–70 aus `reports/testfaelle_iteration4.txt` (U57–U70 in dieser Reihenfolge; Titel und Auftraggeber laut
  `reports/testfaelle_iteration4.md`): 107491-2026, 45854-2026, 76175-2026, 136348-2026, 190390-2026, 173981-2026, 104339-2026,
  52190-2026, 14788-2026, 139668-2026, 107129-2026, 106993-2026, 198259-2026, 37917-2026.

## Definitionen

- Kategorien nach `reports/urteilsregeln_blindpruefung.md`, **Version 1.1** (vor dem ersten Fall vollständig gelesen, einschließlich
  der Kalibrierungsbeispiele). Ergebnis je Fall: `objektgleich_hoch`, `objektgleich_mittel`, `teilmenge`, `unklar` (mit Tendenz),
  `kein_vorgaenger`.
- Begriffe nach `docs/iterationen.md`, Abschnitt „Iteration 4“ (Vorgänger-Quellen: Zuschläge und frühere Ausschreibungen auf TED,
  CPV 909, veröffentlicht ab 01.10.2016 und vor dem Testfall).
- Zeitabstand, Vertragsende, Laufzeit und Auftragswert fließen **nicht** in Urteil oder Tendenz ein. Sie werden erst danach für das
  Vorgänger-Ende notiert.

## Unabhängigkeit

Bestätigt: Nicht gelesen wurden `src/zuordnung_objekt.py`, `src/zuordnung_prototyp.py`, `src/objekt_merkmale.py`, `src/zuordnung_los.py`,
`src/los_merkmale.py`, `src/testprobe_iteration4.py`, alles unter `data/processed/` und `data/raw/ted_ft/`, `reports/zuordnung_*`,
`reports/k2_*`, `reports/blindpruefung_*`, `reports/regel_entwicklung_*`, `reports/evaluation_*`, `reports/sichtbarkeit_iteration3_*`,
`reports/testfaelle_iteration3*`, `reports/dev_gesehene_q1_notices.txt`, `reports/bekannte_notices_iteration4.txt`,
`reports/vorgaenger_ende_iteration3_korrektur.csv` sowie `reports/sichtbarkeit_iteration4_teil1.md` bis `_teil4.md`.
Gelesen wurden nur: `reports/testfaelle_iteration4.txt` (Zeilen 57–70), `reports/testfaelle_iteration4.md` (Zeilen U57–U70),
`reports/urteilsregeln_blindpruefung.md`, `docs/iterationen.md` (Abschnitt Iteration 4), die TED-API, TED-XML und die erlaubten
Rohdaten unter `data/raw/ted_search/`.

## Vorgehen und Konventionen

- **Lokale Rohdaten** (nur gelesen): `DEU_result_cpv909_20161001_20260930`, `DEU_competition_cpv909_20161001_20260930`,
  `DEU_result_cpv909_20231025_20260930_lostext`, `DEU_competition_cpv909_20231025_20260930_lostext`,
  `DEU_competition_cpv9091main_20260101_20260331_lostext`. Daraus ein Suchindex im Scratchpad (nicht im Repo); gefiltert immer auf
  Veröffentlichung ab 2016-10-01 und vor dem Testfall. Lokale Suchen (Auftraggebername, Ort, Freitext in Titel/Losbeschreibung)
  zählen **nicht** zum API-Budget, werden aber im Fall als „lokal“ protokolliert.
- **API-Abfragen** (TED Search API v3, `POST https://api.ted.europa.eu/v3/notices/search`): jede Antwort unverändert unter
  `data/raw/rechercheur_20261026/<U-Nr>/api_qNN.json`, dazu `api_qNN_request.json` mit Query und Feldern. Zeitraum in der Query
  `publication-date>=20161001 AND publication-date<=<Tag vor dem Testfall>` (im Protokoll mit „…“ abgekürzt). Mehrere
  Volltextbegriffe einzeln verknüpft (`(FT~"a" OR FT~"b")`).
- **XML:** `https://ted.europa.eu/en/notice/<nummer>/xml`, unverändert unter `data/raw/rechercheur_20261026/<U-Nr>/<nummer>.xml`.
  Die XML des Testfalls selbst zählt nicht zum XML-Budget (angegeben als „+T“).
- **Objekte zählen:** jede Einzelangabe einer Objektliste (Gebäude bzw. Gebäudeteil mit eigener Zeile/Fläche) zählt als ein Objekt;
  wo das Ergebnis von der Zählweise abhängt, wird auch die Zählung nach Adresse angegeben.
- **Vorgänger-Ende:** Ist der Vorgänger eine Ausschreibung ohne Zuschlag auf TED, wird das geplante Ende aus der Ausschreibung genannt,
  die Herkunft aber als `unbekannt` geführt (kein tatsächlicher Vertrag belegt).
- Gewertet werden nur Vorgänger mit CPV 909. Funde außerhalb davon: „außerhalb des Protokolls (anderer CPV), nicht gewertet“.

## Fälle

### U57 – 107491-2026 (2026-02-16) – Stadt Hanau Eigenbetrieb Immobilien- und Baumanagement
- Objekt(e): 34 Einzelobjekte in 8 Losen, alle in Hanau, je mit Adresse und Bodenfläche. Los 1: Gebeschusschule (+ Sporthalle),
  Volkshochschule Ulanenplatz 4, Schulzentrum Hessen-Homburg Haus A, B, Sporthalle; Los 2: Kinderburg Tümpelgarten (Buchenweg 50,
  674,74 m²), Tümpelgarten-Schule Geb. D, H, K, T, DigiLab Geb. E, Familien- und Jugendberatung Sandeldamm 21; Los 3: Hohe Landesschule
  (12.293,37 m²); Los 4: Business Triangle (Haus der Gesundheit, Jobcenter, Sozialamt); Los 5: Ludwig-Geißler-Schule Geb. A/B, C, T, W
  (zus. 19.306,76 m²); Los 6: Brüder-Grimm-Schule (2.667,31 m²), BGS-Betreuungsgebäude, BGS-Sporthalle (472,96 m²), Kita Margareten
  (733,62 m²), Eppsteinschule (3.791,56 m²), Willi-Rehbein-Halle; Los 7: Lindenauschule; Los 8: August-Gaul-Schule (+ Turnhalle),
  Eichendorffschule (+ Turnhalle), Limesschule (+ Sporthalle).
- Leistungsart (je Los): Unterhalts- und Grundreinigung (UR, GR) in allen Losen, in Los 4 nur UR; keine Glasreinigung.
- Suchschritte:
  - lokal: `buyer-name ~ Hanau` und `buyer-city ~ Hanau` (vor 2026-02-16): 16 Notices (u. a. 422243-2019/564703-2019,
    558033-2020/151782-2021, 116204-2022, 406693-2022/569827-2022, 388581-2024, 717859-2024); lokale Losbeschreibungen von 388581-2024
    und 717859-2024 gelesen.
  - q01 `buyer-name~"Hanau" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260215` → 7
  - q02 dasselbe mit `form-type=competition` → 9
  - q03 `(FT~"Lindenauschule" OR FT~"Hohe Landesschule" OR FT~"Ludwig-Geißler-Schule" OR FT~"Gebeschusschule" OR FT~"Tümpelgarten-Schule") AND classification-cpv=909* AND …` → 3 (154425-2019 Vorinformation, 211048-2019, 370499-2019, alle Stadt Hanau)
  - q04 `(FT~"Business Triangle" OR FT~"Limesschule" OR FT~"Eichendorffschule" OR FT~"August-Gaul-Schule" OR FT~"Willi-Rehbein-Halle") AND classification-cpv=909* AND …` → 50, kein Hanauer Treffer (gleichnamige Schulen anderer Städte)
  - q05 `buyer-name~"Hanau" AND form-type=result AND publication-date>=20240701 AND publication-date<=20261026` (ohne CPV, Suche nach
    dem Zuschlag zu 388581-2024) → 20; einziger Reinigungs-Zuschlag 354703-2026 (Zuschlag zum Testfall selbst, nach dem Testfall, nicht gewertet)
  - XML geöffnet: 406693-2022, 116204-2022, 388581-2024, 558033-2020, 422243-2019, 211048-2019
- Kandidatenvergleich (Fakten):
  - 388581-2024 (competition, eForms): 2 Lose, 10 Objekte. Los 1: Kita Old Argonner, Kita Spitzweg, Grundschule Pioneer (+ Sporthalle),
    Kita Wolfgang; Los 2: Kita Margareten 733,62 m², Brüder-Grimm-Schule 2.667,31 m², BGS-Sporthalle 472,96 m², Kinderburg Tümpelgarten
    (Buchenweg 50) 674,74 m², Eppsteinschule 3.791,56 m². Gemeinsam mit U57: diese 5 Objekte aus Los 2, Adressen und Flächen auf die
    Hundertstel gleich (in U57 Los 6 und Los 2).
  - 717859-2024 (competition): 6 Lose (Kaufmännische Schulen, Erich-Kästner-, Eugen-Kaiser-, Heinrich-Heine-, Otto-Hahn-Schule u. a.,
    Rathaus): kein gemeinsames Objekt.
  - 406693-2022 (Rathaus, Neustädter Rathaus, Kita New Argonner, Stadtteilzentrum Süd-Ost, Glaslos): kein gemeinsames Objekt.
  - 116204-2022 (9 Kitas, u. a. „Kindertagesstätte Tümpelgarten, Am Tümpelgarten 21 a“): kein gemeinsames Objekt (andere Adresse als
    Kinderburg Tümpelgarten, Buchenweg 50).
  - 558033-2020: „Unterhalts- und Grundreinigungsarbeiten in 29 Schulen und Sporthallen“, 9 Lose, nur Anzahl und Fläche, keine Namen
    (Summe ca. 142.705 qm gegenüber 93.302 m² in U57).
  - 211048-2019: Los 1 Ludwig-Geißler-Schule (UR/GR, ca. 17.898 qm), Los 2 Dependance Eugen-Kaiser-Schule, Los 3 Glasreinigung beider.
    Gemeinsam: Ludwig-Geißler-Schule (1 von 2); Fläche 17.898 gegenüber 19.306,76 m² (7,9 % abweichend).
  - 422243-2019: 5 Kindergärten ohne Namen.
- A (Identität): übereinstimmend für 5 Objekte (Adresse und Fläche je Objekt gleich)  Details: 388581-2024 Los 2 ↔ U57 Los 6 und Los 2.
- B (Objektraum): erkennbar und übereinstimmend  Details: Hanau, Schulen/Kitas/Sporthallen, UR + GR auf beiden Seiten.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich (wortgleich „Ausschreibung Gebäudereinigung - versch. Liegenschaften
  Stadt Hanau IBM“), Losstruktur anders (2 gegenüber 8 Lose)
- Überschneidung der Objekte: 5 von 10 (kürzere Seite 388581-2024: 50 %); 5 von 34 (längere Seite U57: 15 %). Nach Adressen gezählt: 4 von 8 (50 %).
- Ergebnis: teilmenge (genau an der 50-%-Schwelle, siehe Grenzfälle)
- Vorgänger: 388581-2024, competition, eForms, 2024-07-01 (Ausschreibung; kein Zuschlag auf TED gefunden)
- Beleg: 388581-2024 Los 2, Beschreibung: „Kindertagesstätte Margareten, Karl-Bierschenk-Straße 14, 63450 Hanau Leistungen: UR, GR
  Bodenfläche: 733,62 m² Brüder-Grimm-Schule, Stresemannstraße 10, 63450 Hanau … 2.667,31 m² … Eppsteinschule, Doorner Straße 49,
  63456 Hanau … 3.791,56 m²“ – gleichlautend in U57 Los 6.
- Weitere Teilvorgänger (Einschätzung, nicht als jüngster gewertet): 211048-2019 (Ausschreibung) / 370499-2019 (Zuschlag) für die
  Ludwig-Geißler-Schule (1 von 2 Objekten = 50 %, Fläche 7,9 % abweichend, zusätzlich Glaslos); 558033-2020 / 151782-2021 „29 Schulen
  und Sporthallen“ ohne Objektliste (allein betrachtet unklar).
- Vorgänger mit Vertrag: kein Zuschlag zu 388581-2024 auf TED (q01, q05).
- Vorgänger-Ende: unbekannt (geplant laut 388581-2024: Grundlaufzeit 2024-12-01 bis 2026-11-30, Verlängerung bis höchstens
  30.11.2028); Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar (neuer Beginn 2026-07-01 liegt 5 Monate vor dem geplanten Ende 2026-11-30; Vertrag nicht belegt)
- Abfragen/XML: 5/6 (+T)

### U58 – 45854-2026 (2026-01-21) – Gemeindeverwaltung Bietigheim
- Objekt(e): keine Objektliste. „Unterhaltsreinigung, Grundreinigung und Glasreinigung in Schulen, Hallen, Verwaltungen usw. in
  Bietigheim/Landkreis Rastatt“; Grundfläche Unterhaltsreinigung ca. 10.400 qm, Glasfläche ca. 3.000 qm.
- Leistungsart (je Los): Los IA Unterhalts- und Grundreinigung; Los IB Glasreinigung.
- Suchschritte:
  - lokal: `buyer-name ~ Bietigheim` → 12 (davon 11 Bietigheim-Bissingen bzw. RKH Kliniken, Landkreis Ludwigsburg; 1 Bietigheim/Baden:
    326187-2022); `buyer-post-code ~ 7646` → 0; Freitext `Bietigheim/|Bietigheim-Baden|76467` → 1 (326187-2022)
  - q01 `buyer-name~"Bietigheim" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260120` → 5 (alle Bietigheim-Bissingen bzw. RKH)
  - q02 dasselbe mit `form-type=competition` → 7 (darunter 326187-2022)
  - q03 `(FT~"Bietigheim" OR buyer-post-code=76467) AND classification-cpv=909* AND …` → 30, aus Bietigheim (Baden) nur 326187-2022
  - XML geöffnet: 326187-2022
- Kandidat 326187-2022 (competition, vor eForms, Gemeindeverwaltung Bietigheim/Landkreis Rastatt Hauptamt): Titel „Ausschreibung
  Gebäudereinigung Kinderhaus Bietigheim-Baden“, „Unterhaltsreinigung, Grundreinigung und Glasreinigung in einem Kindergarten …
  Grundfläche Unterhaltsreinigung ca. 2.200 qm, Reinigungsfläche Glasreinigung ca. 770 qm“, ein Los. Kein Zuschlag auf TED.
- A (Identität): nicht vergleichbar  Details: keine Objektliste in U58; Fläche 2.200 gegenüber 10.400 qm (UR) und 770 gegenüber 3.000 qm (Glas), abweichend.
- B (Objektraum): nicht erkennbar (U58)  Details: Gebiet gleich (Bietigheim, Landkreis Rastatt), Leistungsart gleich (UR, GR, Glas);
  Objektart U58 „Schulen, Hallen, Verwaltungen usw.“ einer Gemeinde mit vielen Gebäudearten, 2022 ein Kindergarten.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel anders, Losstruktur anders (1 gegenüber 2 Lose)
- Überschneidung der Objekte: nicht bestimmbar (U58 ohne Liste)
- Ergebnis: unklar
- Tendenz (nur bei unklar): eher dagegen – der Kindergarten wird in der Objektart-Aufzählung von U58 nicht genannt und deckt höchstens
  rund ein Fünftel der Fläche ab; 2022 war ein eigenes Einzelobjekt-Verfahren.
- Vorgänger (Kandidat): 326187-2022, competition, vor eForms, 2022-06-17
- Beleg: 326187-2022 II.1.4: „Unterhaltsreinigung, Grundreinigung und Glasreinigung in einem Kindergarten in Bietigheim/Landkreis
  Rastatt, Grundfläche Unterhaltsreinigung ca. 2.200 qm“ gegenüber 45854-2026: „in Schulen, Hallen, Verwaltungen usw. … ca. 10.400 qm“.
- Vorgänger mit Vertrag: kein Zuschlag zu 326187-2022 auf TED (q01).
- Vorgänger-Ende: entfällt (kein objektgleicher Vorgänger). Zur Information Kandidat laut Ausschreibung: 2023-01-01 bis 2026-12-31,
  danach jährliche Verlängerung; Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 3/1 (+T)

### U59 – 76175-2026 (2026-02-03) – Bundesnetzagentur
- Objekt(e): 3 Standorte, je ein Los: Leeheim „Satellitenmessstelle 10, 64560“ (Riedstadt-Leeheim), Detmold „Heidenoldendorfer Str. 136,
  32758“, Meschede „Nördelstr. 5, 59851“. Keine Flächen.
- Leistungsart (je Los): „Dauerschuldverhältnis Gebäudereinigung“ (CPV 90911200), nicht weiter aufgeschlüsselt; kein Hinweis auf
  Glas- oder Grundreinigung.
- Suchschritte:
  - lokal: `buyer-name ~ Bundesnetzagentur|BNetzA` → 16 (Standorte Mainz, Saarbrücken, Konstanz, Rostock/Hamburg/Schwerin, Köln/Krefeld/
    Dortmund, Hamburg/Rostock/Breitenburg, Bonn); Freitext `Leeheim|Satellitenmess|Nördelstr|Heidenoldendorfer` → 2 (180779-2025, 400405-2025)
  - q01 `buyer-name~"Bundesnetzagentur" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260202` → 6
  - q02 dasselbe mit `form-type=competition` → 10
  - q03 `(FT~"Leeheim" OR FT~"Nördelstr" OR FT~"Heidenoldendorfer" OR FT~"Satellitenmessstelle") AND classification-cpv=909* AND …` →
    HTTP 502 nach 5 Versuchen (leere Datei `api_q03.json` durch das Skript angelegt, nicht weiterverwendet)
  - q03b dieselbe Abfrage wiederholt → 6 (60380-2021/347908-2021 Kreis Groß-Gerau; 170036-2024/324253-2024 Stadt Detmold;
    180779-2025/400405-2025 BwDLZ Augustdorf)
  - q04 `FT~"Bundesnetzagentur" AND (FT~"Detmold" OR FT~"Meschede" OR FT~"Riedstadt") AND classification-cpv=909* AND …` → 4 (BImA
    321400-2020, 463931-2020, 598979-2020, 112675-2021)
  - XML geöffnet: 720751-2022, 2361-2023, 559408-2021, 547266-2019, 321400-2020, 180779-2025, 60380-2021
- Kandidatenvergleich (Fakten):
  - BNetzA-eigene Verfahren: Mainz (720751-2022), Saarbrücken (2361-2023), Konstanz (559408-2021), Rostock/Hamburg/Schwerin (547266-2019),
    Köln/Krefeld/Dortmund, Hamburg/Rostock/Breitenburg, Bonn (eForms-Titel): keiner der drei Standorte.
  - 321400-2020 (BImA Direktion Dortmund, Liegenschaften des Bundes in Ostwestfalen-Lippe, 8 Lose): „WE 144832, Bundesnetzagentur Detmold,
    Heidenoldendorferstraße 136, 32758 Detmold“ nur in **Los 3 Glasreinigung**; Unterhaltsreinigungslose 5–8 ohne BNetzA (Los 5 nennt
    „THW OV Meschede, Le-Puy-Str. 2a“, andere Adresse).
  - 180779-2025 (BwDLZ Augustdorf, eForms, Rahmenvereinbarung Gebäudereinigung): 6 Liegenschaften, 5 in Augustdorf, dazu
    „Dienstliegenschaft (DstLg) Detmold Heidenoldendorfer Str., Heidenoldendorfer Str. 136, 32758 Detmold“; Zuschlag 400405-2025.
  - 60380-2021 (Kreis Groß-Gerau): Schulen, u. a. „Grundschule Leeheim“ – andere Objektart.
- A (Identität): mehrdeutig  Details: Bester Kandidat 180779-2025 teilt mit U59 Los 2 die Adresse Heidenoldendorfer Str. 136, nennt dort
  aber eine Bundeswehr-Dienstliegenschaft statt der BNetzA; Leeheim und Meschede fehlen.
- B (Objektraum): erkennbar, nur teilweise übereinstimmend  Details: Gebiet Detmold gleich, Objektart Dienstliegenschaft/Dienststelle
  des Bundes, Leistungsart Gebäudereinigung auf beiden Seiten.
- C (Stütze): Auftraggeber nein (BwDLZ Augustdorf gegenüber BNetzA), CPV ja (90911200), Titel anders, Losstruktur anders
- Überschneidung der Objekte: 1 von 3 (U59, 33 %) bzw. 1 von 6 (180779-2025, 17 %), nur über die Adresse belegt.
- Ergebnis: unklar
- Tendenz (nur bei unklar): eher dagegen – gemeinsam ist nur eine Adresse mit anderem Nutzer (Bundeswehr), zwei der drei Standorte
  kommen nicht vor.
- Vorgänger (Kandidat): 180779-2025 (competition, eForms, 2025-03-20); Zuschlag 400405-2025 (result, eForms, 2025-06-20)
- Beleg: 180779-2025 Los-Beschreibung: „Dienstliegenschaft (DstLg) Detmold Heidenoldendorfer Str., Heidenoldendorfer Str. 136, 32758
  Detmold“; 76175-2026 LOT-0002 Leistungsort „Heidenoldendorfer Str. 136 Detmold 32758“.
- Weitere Kandidaten (Einschätzung): 321400-2020 nicht objektgleich (BNetzA Detmold dort nur Glasreinigung, andere Leistungsart).
- Vorgänger mit Vertrag: entfällt (kein objektgleicher Vorgänger)
- Vorgänger-Ende: entfällt; Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 5/7 (+T) (q03 fehlgeschlagen mitgezählt)

### U60 – 136348-2026 (2026-02-26) – Stadtverwaltung Gotha
- Objekt(e): ein Los „Los 13 - Staatliche Gemeinschaftsschule Gotha“ (Schulgebäude, Nebengebäude, Sporthallen/Turnhallen), Ort
  „Gotha 99867“; keine Straße, keine Fläche.
- Leistungsart (je Los): Unterhaltsreinigung, Grundreinigung (Ferien), Glasreinigung (Ferien).
- Suchschritte:
  - lokal: `buyer-name ~ Gotha` → 71 (Stadtverwaltung Gotha, Landkreis/Landratsamt Gotha, Friedenstein Stiftung); Freitext
    `Gemeinschaftsschule|Los 13` bei Gotha-Auftraggebern → nur 125780-2026 (Landkreis, „Staatliche Gemeinschaftsschule Tonna“);
    eForms-Losbeschreibungen der Stadtverwaltung 2025 (758285-2025 … 761968-2025: Kindergärten, Stadtbibliothek, Rathäuser,
    öffentliche WC) und des Landkreises (103862-2024, 142713-2025, 125780-2026) lokal gelesen.
  - q01 `buyer-name~"Stadtverwaltung Gotha" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260225` → 10
  - q02 dasselbe mit `form-type=competition` → 22
  - q03 `(FT~"Gemeinschaftsschule Gotha" OR FT~"Los 13") AND buyer-name~"Gotha" AND classification-cpv=909* AND …` → 0
  - q04 `(FT~"Gemeinschaftsschule" OR FT~"Schule") AND buyer-name~"Stadtverwaltung Gotha" AND classification-cpv=909* AND …` → 0
  - q05 `(FT~"Gemeinschaftsschule" OR FT~"Tonna") AND buyer-name~"Gotha" AND classification-cpv=909* AND …` → 7 (Prüfung, dass FT mit
    buyer-name funktioniert; alle Landkreis Gotha)
  - q06 `FT~"Gemeinschaftsschule" AND buyer-name~"Gotha" AND classification-cpv=909* AND …` → 7 (23280-2018/213822-2018,
    124750-2019/396894-2019, 207850-2022/371019-2022, 125780-2026)
  - q07 wie q06 `AND NOT FT~"Tonna"` → 2 (124750-2019, 396894-2019)
  - XML geöffnet: 707246-2022, 709051-2022, 95149-2023, 95264-2023, 39575-2020, 39577-2020, 39583-2020, 39585-2020, 39586-2020, 216413-2021
- Kandidatenvergleich (Fakten): Alle 10 geöffneten Verfahren der Stadtverwaltung Gotha betreffen Kindergärten (Sonnenblume, Montessori,
  Fröbel, Bummi, Sternenzauber, August-Köhler-Kinderhaus) oder die Stadtbibliothek „Heinrich-Heine“, jeweils Unterhaltsreinigung mit
  Tagesfrau/Hausmeister – andere Objektart, nicht objektgleich. Landkreis Gotha (eForms): 103862-2024 (Gymnasien, KGS, Berufsschulen,
  Förderzentren in Gotha – Gemeinschaftsschule nicht genannt), 142713-2025 (Schulen Ohrdruf/Georgenthal/Tambach-Dietharz,
  Verwaltungsgebäude), 125780-2026 (u. a. „Staatliche Gemeinschaftsschule Tonna“, andere Gemeinde) – kein gemeinsames Objekt.
- A (Identität): nicht vergleichbar  Details: kein Kandidat nennt die Staatliche Gemeinschaftsschule Gotha (Phrasensuche q03 = 0).
- B (Objektraum): bei allen geöffneten Kandidaten widersprüchlich (Kindergarten/Bibliothek) oder andere Schulen
- C (Stütze): –
- Überschneidung der Objekte: 0
- Ergebnis: kein_vorgaenger (Abbruch durch XML-Budget, siehe Hinweis)
- Vorgänger: –
- Beleg: q03 `FT~"Gemeinschaftsschule Gotha"` bei Auftraggebern „Gotha“ ergibt 0 Treffer; geöffnete Stadt-Verfahren z. B. 39575-2020
  „Kita „Sonnenblume“, Bendastraße in Gotha“.
- Offene Spur (nicht geprüft, XML-Budget erschöpft): 124750-2019 (Landratsamt Gotha, competition) / 396894-2019 (result) enthalten im
  Volltext „Gemeinschaftsschule“, aber nicht „Tonna“ (q07). Ob dort die Gemeinschaftsschule in Gotha gemeint ist, bleibt offen; nach der
  Rangfolge gilt die vorsichtigere Kategorie.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: entfällt; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 7/10 (+T) – **Budgetabbruch (XML)**

### U61 – 190390-2026 (2026-03-19) – Seniorenzentrum Grullbad gGmbH
- Objekt(e): Einzelstandort Hochstraße 52, 45661 Recklinghausen; „Gebäudekomplex besteht aus zwei Gebäudeteilen“: vollstationäre Pflege
  und „Kastanienhof“ (Unterkunft für geflüchtete Familien). Keine Fläche.
- Leistungsart (je Los): Unterhaltsreinigung (ein Los).
- Suchschritte:
  - lokal: Freitext `Grullbad|Recklinghausen` → 46, davon Auftraggeber Seniorenzentrum Grullbad: 305562-2023, 491137-2023
  - q01 `buyer-name~"Grullbad" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260318` → 1 (491137-2023)
  - q02 dasselbe mit `form-type=competition` → 1 (305562-2023)
  - Suche B/C nicht nötig (Suche A ergibt Objektgleiches, Einzelstandort ohne weitere Objektnamen)
  - XML geöffnet: 305562-2023, 491137-2023
- A (Identität): übereinstimmend (eingeschränkt)  Details: Adresse gleich „Hochstr. 52, 45661 Recklinghausen“ (zählt beim Einzelstandort
  nicht); Gebäudeteile gleich (vollstationäre Pflege und Unterkunft für Geflüchtete) – ein zählendes A-Merkmal; keine Flächen.
- B (Objektraum): erkennbar und übereinstimmend  Details: Recklinghausen, Pflegeheim mit Flüchtlingsunterkunft, Unterhaltsreinigung.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich (wortgleiche Kurzbeschreibung „Unterhaltsreinigung in der vollstationären
  Pflege und in der Unterkunft für Geflüchtete“), Losstruktur gleich (1 Los)
- Überschneidung der Objekte: 1 von 1
- Ergebnis: objektgleich_mittel
- Vorgänger: 305562-2023 (competition, vor eForms, 2023-05-22) und 491137-2023 (result, vor eForms, 2023-08-11)
- Beleg: 305562-2023 II.2.3/II.2.4: „Seniorenzentrum Grullbad gGmbH Hochstr. 52 45661 Recklinghausen“ – „Unterhaltsreinigung in der
  vollstationären Pflege und in der Unterkunft für Geflüchtete“; gleichlautend in 190390-2026.
- Vorgänger mit Vertrag: 491137-2023 (Vertragsschluss „2023-07-31“)
- Vorgänger-Ende: 2026-07-31 (305562-2023 II.2.7: Beginn 2023-08-01, Ende 2026-07-31, „NO_RENEWAL“); Herkunft: grundlaufzeit
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-08-01)
- Abfragen/XML: 2/2 (+T)

### U62 – 173981-2026 (2026-03-12) – Fraunhofer-Gesellschaft - Einkauf B12
- Objekt(e): Einzelstandort Fraunhofer IGD, Leistungsort „Darmstadt 64283“ (Straße nicht genannt); keine Fläche, keine Gebäudebeschreibung.
- Leistungsart (je Los): Los 1 Unterhaltsreinigung (90911200); Los 2 Fensterreinigung (90911300).
- Suchschritte:
  - lokal: Freitext `IGD|Graphische Datenverarbeitung` → 2 (95199-2021 Darmstadt, 469310-2023 IGD-R Rostock); `buyer-name ~ Fraunhofer`
    und `Darmstadt|64283` → 3 (95199-2021; 413955-2022/673618-2022 Fraunhofer LBF); Fraunhofer-Zuschläge 2021–2022 lokal durchgesehen
    (60, keiner mit IGD oder Darmstadt außer LBF)
  - q01 `buyer-name~"Fraunhofer" AND (FT~"IGD" OR FT~"Graphische Datenverarbeitung") AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260311` → 9 (andere Institute; „IGD“ offenbar auch in Textbausteinen)
  - q02 dasselbe mit `form-type=competition` → 33 (darunter 95199-2021, 469310-2023; sonst andere Institute)
  - q03 `buyer-name~"Fraunhofer" AND buyer-city~"Darmstadt" AND classification-cpv=909* AND …` → 3
  - q04 `(FT~"Fraunhoferstrasse 5" OR FT~"Fraunhoferstraße 5" OR FT~"Institut IGD") AND classification-cpv=909* AND …` → 5 (nur
    95199-2021 und 469310-2023 betreffen Fraunhofer; kein Zuschlag zu 95199-2021)
  - XML geöffnet: 95199-2021
- A (Identität): nicht vergleichbar  Details: 2021 „Fraunhoferstrasse 5, 64283 Darmstadt“, Gebäudebeschreibung (Büro, EDV-Labore,
  Hörsaal, Tiefgarage); 2026 nur PLZ 64283 Darmstadt. Einzelstandort, keine Fläche oder Geschosse auf beiden Seiten.
- B (Objektraum): erkennbar und übereinstimmend  Details: Darmstadt, Fraunhofer-Institut IGD (Forschungsinstitut), Unterhaltsreinigung
  + Fensterreinigung auf beiden Seiten.
- C (Stütze): Auftraggeber ja (Fraunhofer, 2021 Institut selbst, 2026 Einkauf B12 – gleiche Körperschaft), CPV ja (90911200/90911300),
  Titel ähnlich, Losstruktur gleich (Los 1 UR, Los 2 Fenster)
- Überschneidung der Objekte: 1 von 1
- Ergebnis: objektgleich_mittel
- Vorgänger: 95199-2021 (competition, vor eForms, 2021-02-24)
- Beleg: 95199-2021 Los 1 „Unterhaltsreinigung des Gesamtgebäudes“, Los 2 „Fensterreinigung“, Ort „Fraunhoferstrasse 5 64283 Darmstadt“,
  Titel „Fraunhofer-Institut IGD in 64283 Darmstadt“; 173981-2026 „Unterhalts- und Fensterreinigung - Fraunhofer IGD“, Los 1/Los 2 gleich geschnitten.
- Vorgänger mit Vertrag: kein Zuschlag zu 95199-2021 auf TED gefunden (q01, q04, lokale Durchsicht)
- Vorgänger-Ende: unbekannt (95199-2021: Laufzeit 18 Monate, Verlängerung „3 x 12 Monate“, Beginn nicht angegeben); Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 4/1 (+T)

### U63 – 104339-2026 (2026-02-13) – Land Hessen, vertreten durch das Hessische Competence Center
- Objekt(e): Einzelstandort „Finanzamt Offenbach, Bieberer Straße 59 und 59a, 63065 Offenbach“ (LBIH Niederlassung Rhein-Main);
  ca. 1.161.000 m² Jahresvollreinigungsfläche, ca. 1.990.000 m² Jahressichtreinigungsfläche.
- Leistungsart (je Los): Unterhalts- und Sonderreinigung (ein Los, CPV 90910000).
- Suchschritte:
  - lokal: Freitext `Finanzamt Offenbach|Bieberer` → 0 (eForms-Zeit); Auftraggeber `Hessen|LBIH|Competence` mit `Offenbach` → 4 (andere
    Auftraggeber); HCC-Finanzamtsverfahren 2023–2025 (Nidda, Bad Homburg, Friedberg, Hofheim, Darmstadt, Michelstadt, Dillenburg) – nicht Offenbach
  - q01 `(FT~"Finanzamt Offenbach" OR FT~"Bieberer Straße 59" OR FT~"Bieberer Str") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260212` → 2 (612622-2020, 268702-2021)
  - q02 `buyer-name~"Competence Center" AND FT~"Offenbach" AND classification-cpv=909* AND …` → 41 (HCC-Verfahren; Reinigung mit Bezug
    Finanzamt Offenbach nur 612622-2020/268702-2021)
  - q03 `(FT~"Bieberer Straße 59" OR FT~"Bieberer Straße 39" OR FT~"Bieberer Str. 59" OR FT~"Bieberer Str. 39") AND publication-date>=20161001 AND publication-date<=20261026` (ohne CPV, Prüfung der Hausnummer) → 9
  - q04 `publication-number=87912-2024` mit Feldern Leistungsort/Beschreibung (Prüfung der Hausnummer) → 1
  - XML geöffnet: 612622-2020, 268702-2021
- Kandidat 612622-2020 (competition, vor eForms) / 268702-2021 (result): „Unterhaltsreinigung Finanzamt Offenbach“, Ort „Finanzamt
  Bieberer Straße 39 und 39a 63065 Offenbach“, Vollreinigung ca. 1.286.367 m², Sichtreinigung ca. 2.165.493 m² Jahresreinigungsfläche,
  Unterhaltsreinigung + Sonderreinigung + Hygienebehälter + Mattenservice, Referenzschema „VG-0437-2020-0391“ (2026: „VG-0437-2026-0014“).
- A (Identität): abweichend  Details: Gebäudename gleich („Finanzamt Offenbach“); Hausnummer 39/39a (2020/2021) gegenüber 59/59a (2026);
  Flächen abweichend (Vollreinigung −9,7 %, Sichtreinigung −8,1 %). Hilfsbeleg außerhalb des Protokolls (anderer CPV, nicht gewertet):
  87912-2024 „Postdienstleistungen Finanzämter“ nennt als Leistungsort „Bieberer Straße 59“ – die Nummer 39 in 2020/2021 ist daher
  vermutlich ein Schreibfehler (Einschätzung).
- B (Objektraum): erkennbar und übereinstimmend  Details: Offenbach, Finanzamt (Verwaltung), Unterhalts- und Sonderreinigung.
- C (Stütze): Auftraggeber ja, CPV ja (90910000), Titel ähnlich, Losstruktur gleich (1 Los), Kennungsschema gleich (VG-0437-…)
- Überschneidung der Objekte: 1 von 1 (über den Namen; Adresse nach Wortlaut abweichend)
- Ergebnis: unklar (Grenzfall: Adresse nach Wortlaut verschieden, vermutlich Schreibfehler – Regel „andere Adresse“ passt nicht sicher)
- Tendenz (nur bei unklar): eher dafür – gleicher Gebäudename, gleiche Straße mit gleichem Muster „… und …a“, gleiche Leistung und
  Kennung; die dritte Bekanntmachung 87912-2024 nennt das Finanzamt unter Nr. 59.
- Vorgänger (Kandidat): 612622-2020 (competition, vor eForms, 2020-12-18) und 268702-2021 (result, vor eForms, 2021-05-28)
- Beleg: 612622-2020 II.2.3: „Finanzamt Bieberer Straße 39 und 39a 63065 Offenbach“ gegenüber 104339-2026 LOT-0000: „im Finanzamt
  Offenbach, Bieberer Straße 59 und 59a, 63065 Offenbach“.
- Vorgänger mit Vertrag: 268702-2021 (Vertragsschluss 2021-05-06)
- Vorgänger-Ende (nur zur Information, da unklar): Grundlaufzeit 2021-06-01 bis 2024-05-31, zwei Verlängerungen um je ein Jahr,
  „maximale Vertragslaufzeit beträgt 5 Jahre“ → 2026-05-31; Herkunft: hoechstende
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-06-01 = Tag nach dem Höchstende)
- Abfragen/XML: 4/2 (+T)

### U64 – 52190-2026 (2026-01-23) – Bundeswehr-Dienstleistungszentrum Rotenburg
- Objekt(e): 2 Objekte laut Titel: Elbe-Weser-Kaserne (Leistungsort „Elbe-Weser-Kaserne Bremervörde-Hesedorf 27432“) und
  Karriereberatungsbüro Stade. Keine Flächen; Los-Beschreibung nur „Gesamtmenge“.
- Leistungsart (je Los): Gebäudereinigung (Rahmenvertrag, CPV 90911200), ein Los.
- Suchschritte:
  - lokal: `buyer-name ~ Rotenburg` → 15 (BwDLZ Rotenburg: 1323-2017; 578867–578870-2021; 38758/38884/38887-2022)
  - q01 `buyer-name~"Dienstleistungszentrum Rotenburg" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260122` → 4
  - q02 dasselbe mit `form-type=competition` → 4
  - q03 `(FT~"Elbe-Weser-Kaserne" OR FT~"Hesedorf" OR FT~"Karriereberatungsbüro Stade") AND classification-cpv=909* AND …` → 2 (578867-2021, 38758-2022)
  - XML geöffnet: 578867-2021, 38758-2022
- A (Identität): übereinstimmend  Details: Objektliste gleich (Elbe-Weser-Kaserne und Karriereberatungsbüro Stade); keine Adressen
  (2021 „Siehe Verzeichnis der Empfängeranschriften“), keine Flächen → ein A-Merkmal.
- B (Objektraum): erkennbar und übereinstimmend  Details: Bremervörde/Stade, Kaserne und Karriereberatungsbüro der Bundeswehr,
  Gebäudereinigung (Rahmenvertrag).
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich (bis auf die Vorgangsnummer wortgleich), Losstruktur gleich (1 Los,
  „Gesamtmenge“), Kennungsschema gleich („6002…-BwDLZ Rotenburg Wümme“)
- Überschneidung der Objekte: 2 von 2
- Ergebnis: objektgleich_mittel
- Vorgänger: 578867-2021 (competition, vor eForms, 2021-11-12) und 38758-2022 (result, vor eForms, 2022-01-24)
- Beleg: 578867-2021 II.1.1: „Abschluss eines Rahmenvertrages für die Gebäudereinigung Elbe-Weser-Kaserne u. Karriereberatungsbüro Stade,
  6002193936-BwDLZ Rotenburg Wümme“; 52190-2026: „… Elbe-Weser-Kaserne u. Karriereberatungsbüro Stade,6002981024-BwDLZ Rotenburg Wümme“.
- Vorgänger mit Vertrag: 38758-2022 (Vertragsschluss 2022-01-10)
- Vorgänger-Ende: 2026-01-31 (578867-2021 II.2.7: 2022-02-01 bis 2026-01-31, „NO_RENEWAL“, „NO_OPTIONS“); Herkunft: grundlaufzeit
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-07-01 liegt nach dem Ende)
- Abfragen/XML: 3/2 (+T)

### U65 – 14788-2026 (2026-01-09) – Landratsamt Kyffhäuserkreis, Amt für Recht und Vergabe
- Objekt(e): Staatliche Regelschule Franzberg, Bahnhofstraße 8, 99706 Sondershausen: 1. Schulgebäude, 2. Schulsporthalle. Keine Fläche.
- Leistungsart (je Los): Los 1 Unterhalts-, Grund- und Sonderreinigung mit Verbrauchsmitteln; Los 2 Glas- und Rahmenreinigung.
- Suchschritte:
  - lokal: `buyer-name ~ Kyffh` → 31; Freitext `Regelschule Franzberg|Bahnhofstraße 8 … Sondershausen` → 0 (eForms-Zeit);
    415126-2025 lokal gelesen (Grundschule Franzberg/FÖZ Pestalozzi, „Talstraße 34“)
  - q01 `buyer-name~"Kyffhäuserkreis" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260108` → 16
  - q02 dasselbe mit `form-type=competition` → 15
  - q03 `(FT~"Regelschule Franzberg" OR FT~"Franzberg") AND classification-cpv=909* AND …` → 4 (155476-2020, 272214-2020, 415126-2025, 573073-2025)
  - XML geöffnet: 155476-2020, 272214-2020, 302196-2023, 109402-2022, 598256-2023
- Kandidatenvergleich (Fakten): 155476-2020 „Reinigungsleistungen für 3 Schulen des Kyffhäuserkreises in 4 Losen“: Los 1 Kurstadt-Grundschule
  Bad Frankenhausen, **Los 2 „Staatliche Regelschule Franzberg Sondershausen, Bahnhofstraße 8, 99706 Sondershausen (1 Schulgebäude
  Neubau 2018 und 1 Bestandsturnhalle)“** (UHR, GrundR, SonderR), Los 3 Gemeinschaftsschule Greußen, **Los 4 Glasreinigung** der drei
  Schulen einschließlich Franzberg. 415126-2025 (Grundschule Franzberg, Talstraße 34): andere Adresse, nicht objektgleich.
  302196-2023, 598256-2023 (Verwaltungsgebäude), 109402-2022 (Schulen in Artern): andere Objekte.
- A (Identität): übereinstimmend  Details: Adresse Bahnhofstraße 8, 99706 Sondershausen, Gebäudename „Staatliche Regelschule Franzberg“,
  Gebäudezahl gleich (1 Schulgebäude + 1 Turnhalle/Sporthalle).
- B (Objektraum): erkennbar und übereinstimmend  Details: Sondershausen, Regelschule mit Sporthalle; Leistungsarten UHR/GrundR/SonderR
  und Glasreinigung auf beiden Seiten (2020 Lose 2 und 4).
- C (Stütze): Auftraggeber ja, CPV ähnlich (2020 90919300/90911300, 2026 90911000), Titel ähnlich („Reinigungsleistungen … mit
  Werkvertrag“), Losstruktur anders (4 Lose für 3 Schulen gegenüber 2 Lose für 1 Schule), Kennungsschema gleich (KYF/REV/…)
- Überschneidung der Objekte: 1 von 1 Schule (U65, 100 %); 1 von 3 Schulen (2020, 33 %). Lose mit Überschneidung: 2020 Los 2 und Los 4.
- Ergebnis: teilmenge
- Vorgänger: 155476-2020 (competition, vor eForms, 2020-04-01) und 272214-2020 (result, vor eForms, 2020-06-11)
- Beleg: 155476-2020 Los 2 II.2.3: „Staatliche Regelschule Franzberg Sondershausen Bahnhofstraße 8 99706 Sondershausen“, II.2.4: „(1 Schulgebäude
  Neubau 2018 und 1 Bestandsturnhalle)“; 14788-2026: „das Schulgebäude der Staatlichen Regelschule Franzberg, Bahnhofstraße 8,
  99706 Sondershausen 2. die Schulsporthalle …“.
- Hinweis (Fakt): Auf TED gibt es zwischen dem Vertragsende 2024 und dem Testfall keine Bekanntmachung zur Regelschule Franzberg (q03).
- Vorgänger mit Vertrag: 272214-2020 (Los 2.1 und 4.1, Vertragsschluss 2020-06-08)
- Vorgänger-Ende: 2024-06-30 (Los 2: 2020-08-01 bis 2024-06-30; Glas Los 4: 2021-03-01 bis 2024-04-30; „NO_RENEWAL“, „NO_OPTIONS“);
  Herkunft: grundlaufzeit
- Hinweis auf vorzeitige Neuvergabe: nein (neuer Beginn 2026-07-01 liegt zwei Jahre nach dem Ende; Zwischenvertrag nicht auf TED)
- Abfragen/XML: 3/5 (+T)

### U66 – 139668-2026 (2026-02-27) – Bundeswehr-Dienstleistungszentrum Munster
- Objekt(e): Einzelstandort Wehrwissenschaftliches Institut, Leistungsort „Humboldtstr. 100 Munster 29633“; keine Fläche.
- Leistungsart (je Los): Unterhaltsreinigung (Rahmenvertrag, ein Los, CPV 90911200).
- Suchschritte:
  - lokal: Freitext `Wehrwissenschaftliche|WIS|WIWEB` → 3 (711340-2023, 215020-2024 Munster; 762563-2023 WIWeB München/Erding, anderes
    Institut); `buyer-name ~ Munster` mit `Humboldt|WIS|Wehrwissenschaft` → nur 711340-2023/215020-2024 (sonst Schriftgutvernichtung,
    CPV 90918000); die Munster-Rahmenverträge 2025/2026 (770090-2025 ff., 103103-2026 ff.) nennen Humboldtstraße nicht
  - q01 `buyer-name~"Dienstleistungszentrum Munster" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260226` → 26 (Munster und Münster)
  - q02 dasselbe mit `form-type=competition` → 47
  - q03 `(FT~"Wehrwissenschaftliches Institut" OR FT~"Humboldtstr. 100" OR FT~"Humboldtstraße 100") AND classification-cpv=909* AND …` → 6 (711340-2023, 215020-2024; sonst Schriftgutvernichtung)
  - XML geöffnet: 711340-2023, 215020-2024
- A (Identität): übereinstimmend (eingeschränkt)  Details: Adresse „Humboldtstraße 100, 29633 Munster“ gleich (Einzelstandort, zählt
  nicht); keine Flächen, Geschosse oder Gebäudezahlen.
- B (Objektraum): erkennbar und übereinstimmend  Details: Munster, Wehrwissenschaftliches Institut (WIS), Unterhaltsreinigung.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich, Losstruktur gleich (1 Los, Rahmenvereinbarung), Kennungsschema gleich
- Überschneidung der Objekte: 1 von 1
- Ergebnis: objektgleich_mittel
- Vorgänger: 711340-2023 (competition, eForms, 2023-11-23) und 215020-2024 (result, eForms, 2024-04-11)
- Beleg: 215020-2024 Los-Titel „Unterhaltsreinigung Wehrwissenschaftliches Institut für Schutztechnologien - ABC-Schutz (WIS)“, Leistungsort
  „Humboldtstraße 100 Munster 29633“; 139668-2026: „Unterhaltsreinigung im Wehrwissenschaftlichen Institut“, „Humboldtstr. 100 Munster 29633“.
- Vorgänger mit Vertrag: 215020-2024 (Vertrag CON-0001, Datum 2024-03-11)
- Vorgänger-Ende: 2028-05-31 (215020-2024 Laufzeit 2024-06-03 bis 2028-05-31, keine Verlängerung angegeben); Herkunft: grundlaufzeit
- Hinweis auf vorzeitige Neuvergabe: ja (neuer Beginn 2026-06-01 liegt 24 Monate vor dem Ende der Grundlaufzeit)
- Abfragen/XML: 3/2 (+T)

### U67 – 107129-2026 (2026-02-16) – Landeshauptstadt Kiel - Der Oberbürgermeister
- Objekt(e): Einzelstandort „Fridtjof-Nansen-Schule Geschwister-Scholl-Straße 15 24143 Kiel“; keine Fläche.
- Leistungsart (je Los): Unterhaltsreinigung und Grundreinigung (ein Los).
- Suchschritte:
  - lokal: Freitext `Nansen` → 5 (734682-2023 Kassel „Fridtjof-Nansen-Schule“; Bitburg-Treffer über anderen Text); keine Kieler Notice
  - q01 `(FT~"Fridtjof-Nansen-Schule" OR FT~"Geschwister-Scholl-Straße 15") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260215` → 4 (Frankfurt 181107-2021/392457-2022, Kassel 478485-2023/734682-2023)
  - q02 `buyer-name~"Kiel" AND classification-cpv=909* AND form-type=result AND …` → 42 (Landeshauptstadt Kiel, BwDLZ Kiel, FH Kiel, GEOMAR, KVG u. a.)
  - q03 `buyer-name~"Kiel" AND (FT~"Nansen" OR FT~"Geschwister-Scholl" OR FT~"24143") AND classification-cpv=909* AND …` → 7
  - XML geöffnet: 167023-2021 (Abfallwirtschaftsbetrieb, 11 Liegenschaften), 248237-2018 (Schwimmhallen Hörnbad/Schilksee),
    658847-2021 (Baureinigung Busbetriebshof) – keines nennt die Fridtjof-Nansen-Schule
- A (Identität): nicht vergleichbar  Details: kein Kieler Kandidat nennt die Schule oder die Adresse.
- B (Objektraum): widersprüchlich bei allen Kandidaten  Details: Frankfurt/Kassel (gleichnamige Schulen, andere Stadt); Kieler Treffer
  andere Objektarten (Abfallwirtschaft, Schwimmhallen, Busbetriebshof, Grundschule Gaarden 329001-2025 lt. Titel).
- C (Stütze): –
- Überschneidung der Objekte: 0
- Ergebnis: kein_vorgaenger
- Vorgänger: –
- Beleg: q01 `FT~"Fridtjof-Nansen-Schule"` liefert nur 181107-2021 (Stadt Frankfurt am Main) und 478485-2023/734682-2023 (Stadt Kassel,
  „Unterhalts- und Grundreinigung in der Fridtjof-Nansen-Schule“) – andere Städte.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: entfällt; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 3/3 (+T)

### U68 – 106993-2026 (2026-02-16) – Stadt Leipzig
- Objekt(e): Einzelobjekt „Sporthalle Radrennbahn“ (Leipzig), ohne Adresse; Unterhaltsreinigung monatlich 35.896,57 m²
  Reinigungsfläche, Glasreinigung 1.366,80 m² je Vertragsjahr.
- Leistungsart (je Los): Unterhalts-, Glas-, Grund-, Sonder- und Samstagsreinigung (ein Los, CPV 90911000).
- Suchschritte:
  - lokal: Freitext `Radrennbahn` → 0 vor dem Testfall; Leipziger Notices mit `Sporthalle|Sportforum|Sport|Rennbahn|Halle` → 12
    (Flughafen, Graffitientfernung, Sportinternat 388260-2025/551532-2025, Sammelverfahren 671492-2025, 707705-2025 mit „Am Sportforum 10“);
    Treffer `Radrennbahn` nur 106993-2026 selbst und 340078-2026 (nach dem Testfall, nicht gewertet)
  - q01 `(FT~"Radrennbahn" OR FT~"Sporthalle Radrennbahn") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260215` → 7 (Mönchengladbach, Gera, Chemnitz – keine Leipziger Notice)
  - q02 `buyer-name~"Stadt Leipzig" AND classification-cpv=909* AND form-type=result AND …` → 37 (eForms-Titel ohne Bezug; vor eForms ohne Titel, über q01 ausgeschlossen)
  - q03 dasselbe mit `form-type=competition` → 39 (eForms-Titel: Technisches Rathaus, Arvato-Gebäude, Stadtreinigung, Oper/Gewandhaus,
    Schulen, Sportinternat, Verwaltungsobjekte, Sammelverfahren 671492-2025/707705-2025)
  - q04 `buyer-name~"Leipzig" AND (FT~"Sporthalle" OR FT~"Radsport") AND classification-cpv=909* AND …` → 9 (394947-2018/556482-2018,
    71683-2022/251100-2022, 350159-2022/550183-2022, Graffiti-Rahmenvereinbarung)
  - XML geöffnet: 394947-2018, 71683-2022, 350159-2022
- Kandidatenvergleich (Fakten): 394947-2018 und 350159-2022 „Gebäudereinigung in vier Sporthallen des Amtes für Sport“: Sporthalle
  Mannheimer Straße, Nordanlage (Am Sportforum 5), Brüderstraße 15, Am Rabet (Konradstraße 30, 37.053,33 m²/Monat) – die Radrennbahn
  ist nicht darunter (anderer Gebäudename bzw. andere Adresse). 71683-2022: Schulen in den Territorien F und H.
- A (Identität): nicht vergleichbar bzw. widersprüchlich  Details: kein Kandidat nennt die Sporthalle Radrennbahn; die vier Hallen
  2018/2022 tragen andere Namen und Adressen.
- B (Objektraum): bei den Sporthallen-Verfahren Objektart gleich (Sporthalle, Stadt Leipzig), Objekte verschieden; Sportinternat
  (388260-2025) andere Objektart.
- C (Stütze): –
- Überschneidung der Objekte: 0
- Ergebnis: kein_vorgaenger
- Vorgänger: –
- Beleg: q01 `FT~"Radrennbahn"` (CPV 909, bis 2026-02-15) liefert keine Notice der Stadt Leipzig.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: entfällt; Herkunft: –
- Hinweis auf vorzeitige Neuvergabe: –
- Abfragen/XML: 4/3 (+T)

### U69 – 198259-2026 (2026-03-23) – Friedrich-Alexander-Universität Erlangen-Nürnberg
- Objekt(e): Einzelstandort „Gebäude 211.01 Lange Gasse 20 90403 Nürnberg“; Grundfläche ca. 50.000 m², jährliche Reinigungsfläche
  ca. 2.800.000 m².
- Leistungsart (je Los): Unterhaltsreinigung (ein Los, CPV 90910000).
- Suchschritte:
  - lokal: Freitext `Lange Gasse` → 4 (540553-2025 und die Änderungsbekanntmachungen 547505-2025, 562230-2025, 600400-2025, alle
    „change-reason-code: cor-buy“, gleiche procedure-identifier)
  - q01 `(FT~"Lange Gasse 20" OR FT~"Lange Gasse") AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<=20260322` → 4 (dieselben)
  - q02 `buyer-name~"Friedrich-Alexander" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20261026` (bis heute, Suche nach Zuschlag) → 4 (Freyeslebenstraße 1, Bismarckstraße/Kochstraße; 400339-2016, 43002-2018) – kein Zuschlag zu Lange Gasse
  - q03 dasselbe mit `form-type=competition` bis 20260322 → 10
  - XML geöffnet: 540553-2025, 600400-2025
- A (Identität): übereinstimmend (eingeschränkt)  Details: Adresse „Lange Gasse 20, 90403 (Nürnberg)“ gleich (Einzelstandort, zählt
  nicht); Flächen nur 2026 angegeben, 2025 keine.
- B (Objektraum): erkennbar und übereinstimmend  Details: Nürnberg, Gebäude der FAU (2025 „Verwaltungsgebäude“, 2026 „Gebäude 211.01“),
  Unterhaltsreinigung.
- C (Stütze): Auftraggeber ja (FAU, ZUV Referat G5), CPV ähnlich (90911200 gegenüber 90910000), Titel ähnlich, Losstruktur gleich (1 Los),
  Kennungsschema gleich (25-607-21-VV-231-E gegenüber 26-607-21-VV-005-E)
- Überschneidung der Objekte: 1 von 1
- Ergebnis: objektgleich_mittel
- Vorgänger: 540553-2025 (competition, eForms, 2025-08-19); Änderungen 547505-2025, 562230-2025, 600400-2025 (competition, eForms, Berichtigungen „cor-buy“)
- Beleg: 540553-2025 Titel „Unterhaltsreinigung Lange Gasse 20, 90403“, Beschreibung „Unterhaltsreinigung Verwaltungsgebäude“, Ort
  „Nürnberg 90403“; 198259-2026: „Unterhaltsreinigung in folgendem Objekt: Gebäude 211.01 Lange Gasse 20 90403 Nürnberg“.
- Vorgänger mit Vertrag: nicht auf TED. Zu 540553-2025 gibt es keinen Zuschlag (q02, bis 2026-10-26); ein Vertrag vor 2025 ist auf TED
  nicht bekannt gemacht (q01). Einschätzung: 540553-2025 wurde vermutlich nicht vergeben oder aufgehoben, belegt ist das nicht.
- Vorgänger-Ende: unbekannt (540553-2025 plante 2025-12-15 bis 2027-12-14); Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 3/2 (+T)

### U70 – 37917-2026 (2026-01-19) – Wiesbaden Congress & Marketing GmbH
- Objekt(e): Einzelstandort RheinMain CongressCenter (RMCC), Wiesbaden; Bereiche: Foyer Zentral/Nord/Süd, Halle Nord, Halle Süd,
  Obergeschoss Nord/Süd, Außenbereich-Vorplatz, Sanitäranlagen, Aufzüge, Treppenhäuser, Künstlergarderoben/Backstage, Verwaltungsbereich;
  Gesamt-Veranstaltungsfläche ca. 27.000 qm (brutto). Keine Straße im Los.
- Leistungsart (je Los): Unterhaltsreinigung und veranstaltungsbezogene Reinigung (ein Los, CPV 90910000).
- Suchschritte:
  - lokal: Freitext `Wiesbaden Congress|WICM|RheinMain CongressCenter|Kurhaus|Congress & Marketing` → 22 (WiCM: Sanitäranlagen
    Outdoor 2024/2025, Reinigungsleistungen 337994-2025, 424628-2025, 758702-2025; sonst andere Auftraggeber)
  - q01 `buyer-name~"Wiesbaden Congress" AND classification-cpv=909* AND form-type=result AND publication-date>=20161001 AND publication-date<=20260118` → 4
  - q02 dasselbe mit `form-type=competition` → 8
  - XML geöffnet: 758702-2025, 424628-2025
- Kandidat (Fakten): Verfahren 337994-2025 / 424628-2025 (competition, eForms, gleiche procedure-identifier 6506dae3-…) und Zuschlag
  758702-2025: „Reinigungsleistungen im RheinMain CongressCenter sowie im Kurhaus Wiesbaden und Jagdschloss Platte aufgeteilt in drei
  Losen“; Los 1 RheinMain CongressCenter, Friedrich-Ebert-Allee 1, 65185 Wiesbaden, mit derselben Bereichsliste (Foyer Zentral, Foyer
  Nord, Foyer Süd, Halle Nord, Halle Süd, Obergeschoss Nord, Obergeschoss Süd, Außenbereich-Vorplatz …); Los 2 Kurhaus, Los 3
  Jagdschloss Platte. Alle drei Lose bezuschlagt (Verträge CON-0001 bis CON-0003 vom 2025-10-15).
- A (Identität): übereinstimmend  Details: Gebäudeteile/Bereiche wortgleich aufgezählt (Foyers, Hallen Nord/Süd, Obergeschosse Nord/Süd,
  Backstage, Büroräume/Küche); Einzelstandort, Adresse nur 2025 genannt.
- B (Objektraum): erkennbar und übereinstimmend  Details: Wiesbaden, Kongresszentrum RMCC, Unterhalts- und veranstaltungsbezogene Reinigung.
- C (Stütze): Auftraggeber ja, CPV ja (90910000), Titel ähnlich („Wiesbaden Congress & Marketing GmbH, Vergabe Reinigungsleistung(en)“),
  Losstruktur anders (3 Lose gegenüber 1), Kalkulationsmodell (Faktorentabelle) wortgleich
- Überschneidung der Objekte: 1 von 1 (U70, 100 %); 1 von 3 (2025, 33 %). Los mit Überschneidung: 2025 Los 1.
- Ergebnis: teilmenge
- Vorgänger: 758702-2025 (result, eForms, 2025-11-17); dazu 337994-2025 und 424628-2025 (competition, eForms, 2025-05-26 und 2025-07-01)
- Beleg: 758702-2025 LOT-0001 „RheinMain CongressCenter“, Ort „Friedrich-Ebert-Allee 1 Wiesbaden 65185“, Beschreibung „Unterhalts- sowie
  veranstaltungsbezogene Reinigung - Foyer Zentral, Foyer Nord, Foyer Süd - Halle Nord - Halle Süd …“; 37917-2026 gleiche Bereichsliste.
- Vorgänger mit Vertrag: 758702-2025 (LOT-0001, Vertrag CON-0001 vom 2025-10-15)
- Vorgänger-Ende: 2029-09-30 (758702-2025 LOT-0001: 2025-10-01 bis 2029-09-30; Optionen im Text nur „Vertragslaufzeit und Optionen“);
  Herkunft: grundlaufzeit
- Hinweis auf vorzeitige Neuvergabe: ja (neuer Beginn 2026-05-01 liegt rund 41 Monate vor dem Ende; der 2025 vergebene Vertrag für das
  RMCC wird nach etwa sieben Monaten neu ausgeschrieben)
- Abfragen/XML: 2/2 (+T)

## Übersichtstabelle

| U | Notice | Ergebnis | Tendenz | jüngster Vorgänger | alle Notices desselben Vorgängers | Vorgänger mit Vertrag | Vorgänger-Ende | Herkunft | vorzeitig |
|---|---|---|---|---|---|---|---|---|---|
| U57 | 107491-2026 | teilmenge | – | 388581-2024 | 388581-2024 | – (kein Zuschlag auf TED) | unbekannt (Plan 2026-11-30) | unbekannt | unklar |
| U58 | 45854-2026 | unklar | eher dagegen | (Kandidat 326187-2022) | 326187-2022 | – | entfällt | – | – |
| U59 | 76175-2026 | unklar | eher dagegen | (Kandidat 180779-2025) | 180779-2025, 400405-2025 | – | entfällt | – | – |
| U60 | 136348-2026 | kein_vorgaenger (Budgetabbruch XML) | – | – | – | – | – | – | – |
| U61 | 190390-2026 | objektgleich_mittel | – | 491137-2023 | 305562-2023, 491137-2023 | 491137-2023 | 2026-07-31 | grundlaufzeit | nein |
| U62 | 173981-2026 | objektgleich_mittel | – | 95199-2021 | 95199-2021 | – (kein Zuschlag auf TED) | unbekannt | unbekannt | unklar |
| U63 | 104339-2026 | unklar | eher dafür | (Kandidat 268702-2021) | 612622-2020, 268702-2021 | (268702-2021) | (2026-05-31, nur Information) | (hoechstende) | (nein) |
| U64 | 52190-2026 | objektgleich_mittel | – | 38758-2022 | 578867-2021, 38758-2022 | 38758-2022 | 2026-01-31 | grundlaufzeit | nein |
| U65 | 14788-2026 | teilmenge | – | 272214-2020 | 155476-2020, 272214-2020 | 272214-2020 | 2024-06-30 | grundlaufzeit | nein |
| U66 | 139668-2026 | objektgleich_mittel | – | 215020-2024 | 711340-2023, 215020-2024 | 215020-2024 | 2028-05-31 | grundlaufzeit | ja |
| U67 | 107129-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U68 | 106993-2026 | kein_vorgaenger | – | – | – | – | – | – | – |
| U69 | 198259-2026 | objektgleich_mittel | – | 540553-2025 | 540553-2025, 547505-2025, 562230-2025, 600400-2025 | – (kein Zuschlag auf TED) | unbekannt (Plan 2027-12-14) | unbekannt | unklar |
| U70 | 37917-2026 | teilmenge | – | 758702-2025 | 337994-2025, 424628-2025, 758702-2025 | 758702-2025 | 2029-09-30 | grundlaufzeit | ja |

## Übersicht

**Fakten (Zählung aus der Tabelle):**

| Ergebnis | Anzahl | Fälle |
|---|---|---|
| objektgleich_hoch | 0 | – |
| objektgleich_mittel | 5 | U61, U62, U64, U66, U69 |
| teilmenge | 3 | U57, U65, U70 |
| unklar | 3 | U58 (eher dagegen), U59 (eher dagegen), U63 (eher dafür) |
| kein_vorgaenger | 3 | U60, U67, U68 |
| **Summe** | **14** | |

- Objektgleich oder Teilmenge: 8 von 14; nur objektgleich: 5 von 14.
- Budgetabbruch: 1 Fall (U60, 10 von 10 XML geöffnet; API 7 von 15). Kein Fall hat das API-Budget erreicht.
- Vorgänger mit Zuschlag auf TED: 5 von 8 Treffern (U61, U64, U65, U66, U70). Ohne Zuschlag auf TED: U57, U62, U69.
- Bestimmbares Ende der Grundlaufzeit eines belegten Vertrags: U61, U64, U65, U66, U70 (5 Fälle).
- Vorzeitige Neuvergabe (neuer Beginn ≥ 3 Monate vor Ende der Grundlaufzeit): ja bei U66 (24 Monate) und U70 (rund 41 Monate);
  unklar bei U57, U62, U69 (kein Vertrag belegt).

**Einschätzungen:**
- Kein Fall erreicht „hoch“. Ursache ist meist, dass Einzelstandorte nur über Adresse und Name verbunden sind und Flächen fehlen
  oder nur auf einer Seite stehen (U61, U62, U66, U69) bzw. die Objektliste keine Adressen enthält (U64).
- Die drei Teilmengen entstehen durch einen anderen Losschnitt: Die frühere Bekanntmachung bündelte mehrere Schulen bzw. Häuser
  (U65, U70) oder verteilte die Objekte anders (U57).

## Grenzfälle der Regeln

1. **U57 (Teilmenge genau an der Schwelle):** Die kürzere Liste (388581-2024, 10 Objekte) ist zu genau 50 % in U57 belegt, nach Adressen
   ebenfalls 4 von 8. Nach dem Wortlaut („mindestens 50 %“) ist das „teilmenge“. Die andere Hälfte der kürzeren Liste (Kitas Old Argonner,
   Spitzweg, Wolfgang, Grundschule Pioneer mit Halle) fehlt in U57. Die Regel ist erfüllt, beschreibt aber eher eine Überschneidung als eine
   echte Teilmenge. Bei einem Objekt weniger wäre das Urteil „unklar“.
2. **U63 (Adresse nach Wortlaut verschieden):** 2020/2021 „Bieberer Straße 39 und 39a“, 2026 „Bieberer Straße 59 und 59a“, bei gleichem
   Gebäudenamen „Finanzamt Offenbach“. Nach Wortlaut wäre das „andere Adresse“, also nicht objektgleich. Eine dritte Bekanntmachung
   (87912-2024, anderer CPV) nennt das Finanzamt unter Nr. 59, deshalb liegt ein Schreibfehler nahe. Die Regel ist nicht neu ausgelegt
   worden: Urteil „unklar“, Tendenz eher dafür.
3. **U59 (gleiche Adresse, anderer Nutzer):** 180779-2025 nennt „Dienstliegenschaft (DstLg) Detmold Heidenoldendorfer Str. 136“ der
   Bundeswehr, U59 die BNetzA an derselben Adresse. Die Regeln sagen nicht, ob eine gleiche Adresse mit anderem Nutzer bzw. Gebäudenamen
   als gemeinsames Objekt zählt. Gezählt wurde nur über die Adresse (1 von 3 = 33 %, Bereich 20–50 %), daher „unklar“, eher dagegen.
4. **U58 (Objektart „Schulen, Hallen, Verwaltungen usw.“):** Die Aufzählung ist teilweise spezifisch, endet aber mit „usw.“. Sie wurde
   als nicht erkennbare Objektart (Gemeinde mit vielen Gebäudearten) gewertet. Bei anderer Lesart wäre der Kandidat (ein Kindergarten)
   wegen anderer Objektart „nicht objektgleich“ und U58 hätte „kein_vorgaenger“.
5. **U60 (Budgetabbruch mit offener Spur):** 124750-2019/396894-2019 (Landratsamt Gotha) enthalten „Gemeinschaftsschule“, aber nicht
   „Tonna“. Sie wurden nicht geöffnet, weil das XML-Budget erschöpft war. Vergeben wurde die vorsichtigere Kategorie „kein_vorgaenger“.

## Auffälligkeiten

**Fakten:**
- **Zentrale Vergabestellen:** Hessisches Competence Center (U63, Finanzamt Offenbach), Fraunhofer-Gesellschaft Einkauf B12 (U62; 2021
  schrieb noch das Institut IGD selbst aus), Bundeswehr-Dienstleistungszentren (U59 Kandidat, U64, U66), BImA Direktion Dortmund
  (321400-2020 reinigt Bundesliegenschaften, darunter die Glasreinigung der BNetzA Detmold).
- **Namenswechsel der Vergabestelle:** Kyffhäuserkreis „Stabsstelle Recht und Vergabe“ (2020) → „Amt für Recht und Vergabe“ (2026);
  Hanau „Hanau Immobilien- und Baumanagement - Eigenbetrieb der Stadt Hanau“ / „Stadt Hanau EigenbetriebImmobilien- und Baumanagement“
  (Schreibvarianten 2022–2024).
- **Außerhalb des Protokolls (anderer CPV), nicht gewertet:** 87912-2024 (Postdienstleistungen Finanzämter, CPV 60160000) nur als
  Hilfsbeleg für die Hausnummer in U63.
- **Neuvergabe kurz nach Zuschlag:** U70 (RMCC) wurde am 2025-10-15 vergeben (758702-2025, Laufzeit bis 2029-09-30) und am
  2026-01-19 mit Beginn 2026-05-01 neu ausgeschrieben. U66 (WIS Munster): Vertrag bis 2028-05-31, Neuausschreibung mit Beginn 2026-06-01.
- **Lücke auf TED:** U65 – der Vertrag von 2020 endete am 2024-06-30. Zwischen 2024 und 2026 gibt es auf TED keine Bekanntmachung zur
  Regelschule Franzberg.
- **Vorgänger ohne Zuschlag:** U57 (388581-2024), U62 (95199-2021) und U69 (540553-2025 mit drei Berichtigungen) haben keinen
  Zuschlag auf TED.
- **Gleichnamige Objekte in anderen Städten:** Fridtjof-Nansen-Schule in Frankfurt und Kassel (U67), Limesschule und
  Eichendorffschule in mehreren Städten (U57). Die Volltextsuche findet sie, sie werden über das Gebiet ausgeschlossen.
- **Technisches:** In U59 brach q03 mit HTTP 502 ab. Das Skript legte dabei die leere Datei `api_q03.json` an; die Wiederholung
  steht in `api_q03b.json`. `FT~"IGD"` trifft auch Fraunhofer-Bekanntmachungen anderer Institute (U62), vermutlich über Textbausteine.

**Einschätzungen:**
- Hanau (U57) verteilt seine Liegenschaften bei jeder Ausschreibungsrunde neu auf Verfahren und Lose. Objektgleiche Vorgänger auf der
  Ebene ganzer Bekanntmachungen sind dort kaum zu erwarten, eher Teilmengen.
- Die Volltextsuche (`FT`) war für Bekanntmachungen vor eForms in allen Fällen das entscheidende Werkzeug (U59, U63, U65, U66, U67, U68).
