# Sichtbarkeit der Vorgänger – Handsuche Iteration 4, Teil 4 (U43–U56)

- **Datum:** 2026-10-26
- **Bearbeiter:** Subagent `rechercheur` (Auftrag „Handsuche“)
- **Testfälle:** Zeilen 43–56 aus `reports/testfaelle_iteration4.txt` (U43–U56 in dieser Reihenfolge): 127506-2026, 134489-2026,
  62104-2026, 55335-2026, 134081-2026, 47380-2026, 29273-2026, 87147-2026, 90864-2026, 160356-2026, 123318-2026, 100442-2026,
  153719-2026, 93751-2026.
- **Definitionen:** Kategorien nach `reports/urteilsregeln_blindpruefung.md` Version 1.1 (vor dem ersten Fall vollständig gelesen,
  einschließlich der Kalibrierungsbeispiele); Begriffe nach `docs/iterationen.md`, Abschnitt „Iteration 4“. Vorgänger-Quellen: Zuschläge
  (`form-type=result`) und frühere Ausschreibungen (`form-type=competition`) auf TED mit CPV 909, veröffentlicht ab 20161001 und vor
  dem Testfall. Zeitabstand, Vertragsende, Laufzeit und Auftragswert sind nicht in die Urteile eingeflossen; das Vorgänger-Ende ist
  jeweils erst nach dem Urteil und getrennt davon notiert.
- **Unabhängigkeit:** Ich habe keine der ausgeschlossenen Dateien gelesen (insbesondere nicht `src/zuordnung_*.py`, `src/objekt_merkmale.py`,
  `src/los_merkmale.py`, `src/testprobe_iteration4.py`, `data/processed/`, `data/raw/ted_ft/`, Reports zu Zuordnung, Blindprüfung,
  Regelentwicklung, Evaluation, Iteration 3 sowie die Teile 1–3 dieser Handsuche). Gelesen wurden nur `reports/testfaelle_iteration4.txt`
  (Zeilen 43–56), die zugehörigen Zeilen in `reports/testfaelle_iteration4.md`, die Urteilsregeln, `docs/iterationen.md` (Iteration 4),
  die erlaubten Rohdaten unter `data/raw/ted_search/`, die TED-API und die TED-XML.

## Vorgehen und Konventionen

- **Lokale Suche (Suche A/B, ohne API-Kosten):** Die erlaubten Rohdaten unter `data/raw/ted_search/` (Zuschläge und Ausschreibungen
  CPV 909 ab 2016-10, eForms-Lostexte ab 2023-10-25) wurden zu einem Index zusammengeführt (35.150 Notices) und per regulärem Ausdruck
  über alle Felder (bzw. über `buyer-name`) durchsucht, gefiltert auf Veröffentlichung ab 20161001 und vor dem Testfall. Das entspricht
  Suche A bzw. B mit `classification-cpv=909*` für beide Formulartypen. Lokale Suchen sind mit „lokal:“ und dem Ausdruck notiert; sie
  zählen nicht zum API-Budget. Vor eForms enthalten die lokalen Daten keine Titel, daher ergänzt die Volltextsuche `FT` (API).
- **API-Abfragen:** `POST https://api.ted.europa.eu/v3/notices/search`, jede Antwort unverändert mit Anfrage unter
  `data/raw/rechercheur_20261026/U<Nr>/api_q<NN>.json`. Die Datumsgrenze ist in jeder Abfrage als
  `publication-date>=20161001 AND publication-date<<Testfalldatum>` enthalten (unten abgekürzt mit „[Zeitraum]“).
- **XML:** `https://ted.europa.eu/en/notice/<nummer>/xml`, gespeichert unter `data/raw/rechercheur_20261026/U<Nr>/<nummer>.xml`.
  Die XML des Testfalls selbst zählt nicht zum Budget von 10 XML (angegeben als „+1 Testfall“).
- Zitate aus der XML sind mit Umlauten wiedergegeben, so wie sie in der XML stehen; „qm“/„m²“ wie im Original.
- **Rangfolge bei Zweifel** (vorsichtig zuerst): nicht objektgleich, unklar, teilmenge, objektgleich (mittel), objektgleich (hoch).
- **Vorzeitige Neuvergabe** „ja“, wenn der neue Vertragsbeginn mindestens 3 Monate vor dem Ende der Grundlaufzeit des Vorgängers liegt.

## Fälle

### U43 – 127506-2026 (2026-02-24) – Freistaat Bayern vertreten durch das Bayerische Landesamt für Steuern – Zentrale Vergabestelle
- Objekt(e): Amt für Digitalisierung, Breitband und Vermessung (ADBV) Traunstein, 83278 Traunstein (keine Straße); ein Los (LOT-0001),
  Note: „Grundfläche: ca. 2.979,39 qm, Jahresreinigungsfläche ca. 260.767,52 qm“. Einzelstandort.
- Leistungsart (je Los): Los 1 Unterhaltsreinigung (CPV 90911200).
- Suchschritte:
  - lokal: `Landesamt f.r Steuern` in `buyer-name` → 539 Notices (vor eForms ohne Titel; eForms-Titel nennen kein ADBV Traunstein);
    lokal: `Vermessung|ADBV|Digitalisierung, Breitband` → 49 (andere ADBV/FA, kein Traunstein); lokal: `Traunstein` → 42 (Finanzamt
    Traunstein 405769-2024/544321-2024, 262573-2025/488397-2025, Landgericht, Landkreis, Stadt – andere Objekte, kein ADBV).
  - q01 (Suche C): `(FT~"ADBV Traunstein" OR FT~"Vermessung Traunstein" OR FT~"Vermessungsamt Traunstein") AND classification-cpv=909* AND [Zeitraum]` → 4
    (279881-2022, 415309-2022, 207575-2023, 343780-2023).
  - XML geöffnet: 207575-2023, 343780-2023, 415309-2022 (+1 Testfall).
- A (Identität): übereinstimmend (eine Fläche gleich, eine abweichend)  Details: Grundfläche 2.979,39 qm in 207575-2023/343780-2023 und
  im Testfall identisch; Jahresreinigungsfläche 268.730,96 qm (2023) gegenüber 260.767,52 qm (2026), Abweichung 3,0 % → abweichend.
  Einzelstandort: Adresse (Traunstein) zählt nicht. Damit nur ein übereinstimmendes A-Merkmal; die abweichende Jahresfläche schließt „hoch“ zusätzlich aus.
- B (Objektraum): erkennbar und übereinstimmend  Details: Gebiet Traunstein; Objektart Dienststelle ADBV (Verwaltung); Leistung Unterhaltsreinigung auf beiden Seiten.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich (wortgleich „Unterhaltsreinigung für das ADBV Traunstein“), Losstruktur gleich (1 Los); Kennung 2023NSC000003 / 2026NSC000003.
- Überschneidung der Objekte: 1 von 1 (Einzelstandort)
- Ergebnis: objektgleich_mittel
- Vorgänger: 343780-2023 (result, vor eForms, 2023-06-09) mit Ausschreibung 207575-2023 (competition, vor eForms, 2023-04-07)
- Beleg: 207575-2023, II.2.4: „Grundfläche: ca. 2.979,39 qm“ und „Jahresreinigungsfläche: ca. 268.730,96 qm“; Testfall LOT-0001 Note: „Grundfläche: ca. 2.979,39 qm, Jahresreinigungsfläche ca. 260.767,52 qm“.
- Vorgänger mit Vertrag: 343780-2023 (Vertragsschluss 2023-06-05, Zuschlag an „Münchner Gebäudereinigung“)
- Vorgänger-Ende: 2026-07-31; Herkunft: grundlaufzeit (207575-2023, II.2.7: „tritt am 01.08.2023 in Kraft und gilt zunächst bis zum 31.07.2026 … endet spätestens mit Ablauf des 31.07.2029“; Höchstende 2029-07-31)
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-08-01, direkt nach Ende der Grundlaufzeit)
- Weitere Fakten: Ein noch früheres Verfahren 279881-2022/415309-2022 (Unterhalts- sowie Glas- und Rahmenreinigung ADBV Traunstein, 2 Lose,
  Los 1 mit gleicher Grundfläche 2.979,39 qm und Jahresfläche 268.730,96 qm, Zuschlag 2022-07-26 an Wackler) ist ebenfalls objektgleich (Los 1),
  aber nicht der jüngste Vorgänger. Einschätzung: Der Vertrag von 2022 wurde offenbar nach einem Jahr ersetzt (Ursache aus TED nicht ersichtlich).
- Abfragen/XML: 1/3

### U44 – 134489-2026 (2026-02-26) – Landkreis Ammerland
- Objekt(e): Berufsbildende Schulen (BBS) Ammerland, Elmendorfer Str. 59, 26160 Bad Zwischenahn: Schulgebäude mit Verwaltung und Sporthalle,
  Medienzentrum und Umweltbildungszentrum (UBZ). Los 1 „Seeseite (Trakt 1 - 3)“, Grundfläche ca. 12.500 m², jährliche Reinigungsfläche
  ca. 1.965.000 m²; Los 2 „Werkstattseite (Trakt 4-10, UBZ)“, Grundfläche ca. 9.600 m², jährliche Reinigungsfläche ca. 1.550.000 m².
- Leistungsart (je Los): Los 1 und Los 2 je Unterhalts-, Grund- und Sonderreinigung.
- Suchschritte:
  - lokal: `Ammerland` → 4 (401478-2018, 551122-2018 Landkreis Ammerland; 170455-2022, 362257-2022 BBS Ammerland);
    lokal: `Bad Zwischenahn|Elmendorfer|Westerstede` → 13 (zusätzlich Gemeinde Bad Zwischenahn 2020/2021, BA, Staatliches Baumanagement, Landwirtschaftskammer – andere Objekte).
  - q01 (Suche C): `(FT~"BBS Ammerland" OR FT~"Berufsbildende Schulen Ammerland" OR FT~"Elmendorfer") AND classification-cpv=909* AND [Zeitraum]` → 2 (170455-2022, 362257-2022).
  - XML geöffnet: 170455-2022, 362257-2022 (+1 Testfall).
- A (Identität): übereinstimmend (Gebäudeteile; Fläche Los 1 gleich, Los 2 abweichend)  Details: Losschnitt nach Gebäudeteilen identisch
  (2022 Los 1 „Trakt 1 - 3“ Seeseite, Los 2 „Trakt 4 - 10, MZ, UBZ“ Werkstattseite mit Kreismedienzentrum und Umweltbildungszentrum).
  Jahresfläche Los 1: 2022 Unterhaltsreinigung 1.940.395,59 qm (+ Grundreinigung 3.067,15 qm) gegenüber 2026 ca. 1.965.000 m² → +1,3 % bzw. +1,1 % (gleich).
  Los 2: 1.668.693,76 qm (+ 2.385,08 qm) gegenüber 1.550.000 m² → −7,1 % (abweichend). Einzelstandort (Schulgelände): Adresse zählt nicht.
- B (Objektraum): erkennbar und übereinstimmend  Details: Bad Zwischenahn, Berufsschulgelände BBS Ammerland; Unterhalts- und Grundreinigung auf beiden
  Seiten (2026 zusätzlich „Sonderreinigung“ – kein Wechsel der Leistungsart, Hauptleistung gleich).
- C (Stütze): Auftraggeber nein (2022 „Berufsbildende Schulen Ammerland“, 2026 „Landkreis Ammerland“; gleiche Trägerkörperschaft), CPV ja (90911200), Titel ähnlich, Losstruktur gleich (2 Lose, gleicher Schnitt).
- Überschneidung der Objekte: 2 von 2 Losobjekten (Seeseite Trakt 1–3; Werkstattseite Trakt 4–10 mit MZ und UBZ)
- Ergebnis: objektgleich_mittel (Gebäudeteile und Fläche Los 1 stimmen überein, aber die Fläche Los 2 weicht um 7 % ab; nach den Regeln schließt eine abweichende Fläche „hoch“ aus)
- Vorgänger: 362257-2022 (result, vor eForms, 2022-07-05) mit Ausschreibung 170455-2022 (competition, vor eForms, 2022-04-01)
- Beleg: 170455-2022, II.2.4 Los 2: „Trakte 4 bis 10 auf der sog. Werkstattseite … Bueroräume des Kreismedienzentrums sowie des Umweltbildungszentrums“; Testfall Los 2: „Werkstattseite (Trakt 4-10, UBZ)“.
- Vorgänger mit Vertrag: 362257-2022 (Vertragsschluss 2022-06-21; Los 1 Rudolf Weber, Los 2 Götz Nordwest)
- Vorgänger-Ende: Grundlaufzeit 2024-07-31, Höchstende 2026-07-31; Herkunft: grundlaufzeit (170455-2022, II.2.7: „tritt am 01.08.2022 in Kraft und endet am 31.07.2024. Das Vertragsverhältnis verlängert sich maximal zweimal um jeweils ein weiteres Jahr“); Höchstende aus derselben Stelle.
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-08-01, nach dem Ende der Grundlaufzeit)
- Abfragen/XML: 1/2

### U45 – 62104-2026 (2026-01-28) – Große Kreisstadt Winnenden
- Objekt(e): „Ausführung der Unterhalts-, Grund- und Glasreinigung in verschiedenen städtischen Gebäuden“, 71364 Winnenden, keine Objektliste.
  Los I: „Unterhalts- und Grundreinigung in 6 Gebäuden auf einer Fläche von ca. 14.869,13 m²“; Los II: 5 Gebäude, ca. 18.002,58 m²;
  Los III: 18 Gebäude, ca. 8.875,34 m²; Los IV: „Glasreinigung in 31 Gebäuden auf einer Fläche von ca. 13.441,89 m²“.
- Leistungsart (je Los): Los I–III Unterhalts- und Grundreinigung; Los IV Glasreinigung.
- Suchschritte:
  - lokal: `Winnenden` → 19 (Stadt/Große Kreisstadt Winnenden: 490368-2017/248682-2018, 210458-2020/377478-2020, 584334-2020/307321-2021,
    117265-2023/477144-2023, 471420-2023/740328-2023; ferner Rems-Murr-Kliniken, Klinikum Schloss Winnenden, BImA – andere Auftraggeber/Objekte).
  - Keine API-Abfrage: Der Testfall nennt keine Objektnamen oder Straßen, eine Volltextsuche hätte keinen kennzeichnenden Begriff.
  - XML geöffnet: 117265-2023, 477144-2023, 740328-2023 (+1 Testfall).
- A (Identität): abweichend / nicht vergleichbar  Details: keine Objektlisten auf beiden Seiten. Gebäudezahl: 2023 (117265-2023) Los 1–4
  zusammen 10+13+14+16 = 53 Gebäude Unterhaltsreinigung (Los 3 neu vergeben in 740328-2023 mit 17 Gebäuden) und 48 Gebäude Glas; 2026
  6+5+18 = 29 Gebäude Unterhaltsreinigung und 31 Gebäude Glas → abweichend. Fläche Unterhaltsreinigung gesamt: 2023 16.007 + 8.431 + 8.137,80
  (Los III neu) + 9.588 = 42.163,80 m² gegenüber 2026 41.747,05 m² (−1,0 %; mit ursprünglichem Los 3: 42.630 m², −2,1 %); Glasfläche
  10.820 gegenüber 13.441,89 m² (+24 %). Los-weise passen weder Gebäudezahl noch Fläche.
- B (Objektraum): nicht erkennbar  Details: Gebiet Winnenden; Objektart „verschiedene städtische Gebäude“ einer Stadt (Regel: nicht erkennbar); Leistungen auf beiden Seiten Unterhalts-, Grund- und Glasreinigung.
- C (Stütze): Auftraggeber ja, CPV ja (909112/909113), Titel ähnlich („Gebäudereinigung“ wortgleich), Losstruktur anders (5 gegenüber 4 Lose); Mindestumsatz 400.000/46.000 EUR wortgleich.
- Überschneidung der Objekte: keine Listen
- Ergebnis: unklar
- Tendenz: keine (Gesamtfläche Unterhaltsreinigung fast gleich, aber Gebäudezahl 53 gegenüber 29 und Glasfläche +24 % sprechen gegen denselben Bestand; die Hinweise heben sich auf)
- Vorgänger (Kandidat bei unklar): 477144-2023 (result, vor eForms, 2023-08-04) mit Ausschreibung 117265-2023 (competition, vor eForms, 2023-02-24); für Los 3 Neuvergabe 471420-2023 (competition, vor eForms, 2023-08-04) / 740328-2023 (result, eForms, 2023-12-06)
- Beleg: 117265-2023, II.2.4 Los 1: „Unterhalts- und Grundreinigung in 10 Gebäuden auf einer Fläche von ca. 16.007 m2“; Testfall Los I: „in 6 Gebäuden auf einer Fläche von ca. 14.869,13 m2“.
- Vorgänger mit Vertrag: 477144-2023 (Vertragsschluss 2023-07-31) bzw. 740328-2023 (Los III)
- Vorgänger-Ende: Grundlaufzeit Los 1 bis 2027-10-15, Los 2 bis 2027-11-14, Los 4 und 5 bis 2027-12-14 (jeweils 4 Jahre ab Auftragsstart, danach jährliche Verlängerung ohne Höchstdauer); Los III (740328-2023) Beginn 2024-01-15, Laufzeittext abgeschnitten; Herkunft: grundlaufzeit (117265-2023, II.2.7: „Auftragsstart ist für Los I der 16. Oktober 2023. Der Reinigungsvertrag wird für die Dauer von 4 Jahren ab Auftragsstart abgeschlossen … verlängert sich somit jeweils um ein Jahr“)
- Hinweis auf vorzeitige Neuvergabe: unklar (Testfall Beginn 2026-10-01, rund ein Jahr vor dem Ende der Grundlaufzeit des Kandidaten; da der Kandidat nicht als objektgleich belegt ist, nicht bewertbar)
- Abfragen/XML: 0/3

### U46 – 55335-2026 (2026-01-26) – Berufsgenossenschaft Verkehrswirtschaft Post-Logistik Telekommunikation (BG Verkehr)
- Objekt(e): Los 1 (einziges Los dieser Bekanntmachung; laut Beschreibung werden 8 regionale Lose zeitlich parallel ausgeschrieben):
  Verwaltungsgebäude der Hauptverwaltung/Bezirksverwaltung Hamburg (HV/BV2), Ottenser Hauptstraße 54, 22765 Hamburg, sowie
  Schlüsselrevier in angemieteten Räumen Friesenweg 2a-c, 22763 Hamburg. Keine Flächenangabe.
- Leistungsart (je Los): Los 1 Unterhaltsreinigung.
- Suchschritte:
  - lokal: `BG Verkehr|Berufsgenossenschaft (für )?(Fahrzeughaltungen|Verkehr)|BG Verkehrswirtschaft|Post-Logistik` in `buyer-name` → 2 (404919-2019, 552382-2019, Sitz Tübingen);
    lokal: `Ottenser|Friesenweg` → 0.
  - q01: `(FT~"BG Verkehr" OR FT~"Ottenser Hauptstraße" OR FT~"Ottenser Hauptstrasse" OR FT~"Friesenweg") AND classification-cpv=909* AND [Zeitraum]` → 0.
  - q02: `buyer-name~"Verkehrswirtschaft" AND classification-cpv=909* AND [Zeitraum]` → 2 (404919-2019, 552382-2019).
  - q03 (Suche B): `FT~"Berufsgenossenschaft" AND buyer-city="Hamburg" AND classification-cpv=909* AND [Zeitraum]` → 125 (nur VBG, BG Klinikum, Finanzbehörde, NDR u. a.; keine BG Verkehr).
  - q04: `(FT~"Verkehrswirtschaft" OR FT~"Telekommunikation Hamburg") AND classification-cpv=909* AND [Zeitraum]` → 2 (dieselben).
  - XML geöffnet: 552382-2019 (+1 Testfall).
- A (Identität): widersprüchlich (Kandidat 552382-2019)  Details: 552382-2019 betrifft „Gebäudeinnenreinigung monatlich ca. 75 500 qm“ (Los 1) und Glasreinigung (Los 2) des Auftraggebers mit Sitz Tübingen (NUTS DE14), keine Nennung Hamburgs; Testfall: Ottenser Hauptstraße 54, Hamburg.
- B (Objektraum): widersprüchlich  Details: Gebiet Tübingen (DE14) gegenüber Hamburg.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel anders, Losstruktur anders.
- Überschneidung der Objekte: 0 von 1
- Ergebnis: kein_vorgaenger
- Vorgänger: –
- Beleg: 552382-2019, II.2.4 Los 1: „Gebäudeinnenreinigung monatlich ca. 75 500 qm“, NUTS DE14, Auftraggeber Tübingen 72072; Testfall LOT-0001: „Verwaltungsgebäude der Hauptverwaltung/ Bezirksverwaltung Hamburg … Ottenser Hauptstraße 54“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: unbekannt; Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 4/1

### U47 – 134081-2026 (2026-02-25) – Fachhochschule Südwestfalen – Vergabestelle
- Objekt(e): „Unterhalts- und Glas- und Rahmenreinigung an allen Standorten der Fachhochschule Südwestfalen“, 10 Lose mit Adressen:
  Hagen (Haldener Straße 182, Im Alten Holz 131), Iserlohn (Frauenstuhlweg 31, Baarstraße 6, Baarstraße 5; Glas zusätzlich Kalkofen 6),
  Lüdenscheid (Bahnhofsallee 5), Meschede (Lindenstraße 53, Jahnstraße 23-25, Le-Puy-Straße 15; Glas nur die ersten beiden),
  Soest/Welver/Ense (Lübecker Ring 2, Mawicker Str. 3 Ense-Gerlingen, Im Südfeld 1 Welver-Merklingsen, Detmolder Str. 7). Zusammen 14 Adressen.
- Leistungsart (je Los): LOT-0001 bis -0005 Unterhaltsreinigung (Hagen, Iserlohn, Lüdenscheid, Meschede, Soest/Welver/Ense); LOT-0006 bis -0010 Glas- und Rahmenreinigung (dieselben Standortgruppen).
- Suchschritte:
  - lokal: `Südwestfalen` → 31 (FH Südwestfalen: 62542-2019/207277-2019, 157336-2023/328497-2023; sonst Mark-E, Straßen.NRW, AOK NordWest, Südwestfalen-IT – andere Auftraggeber);
    lokal: `Haldener|Frauenstuhlweg|Lübecker Ring|Lindenstraße 53|Bahnhofsallee 5` → 0 (eForms-Zeit, keine weiteren Treffer).
  - Keine API-Abfrage nötig: Suche A ergab einen Kandidaten mit Adressliste; lokale Daten decken CPV 909 vollständig ab.
  - XML geöffnet: 157336-2023, 328497-2023 (+1 Testfall).
- A (Identität): übereinstimmend (Adressliste weitgehend gleich)  Details: 157336-2023 nennt 15 Adressen (14 Unterhaltsreinigung + Kalkofen 6 Glas).
  Gemeinsam 12: Haldener Str. 182, Im Alten Holz 131, Frauenstuhlweg 31, Baarstr. 6, Baarstr. 5, Kalkofen 6, Bahnhofsallee 5, Lindenstr. 53,
  Jahnstr. 23-25, Lübecker Ring 2, Detmolder Str. 7, Im Südfeld 1. Nur 2023: Franz-Stahlmecke-Platz 1 und Sophienweg 3 (Meschede), Arnsberger Straße 7 (Soest).
  Nur 2026: Le-Puy-Straße 15 (Meschede), Mawicker Str. 3 (Ense-Gerlingen). Keine Flächen angegeben.
- B (Objektraum): erkennbar und übereinstimmend  Details: Standorte der FH Südwestfalen in Hagen, Iserlohn, Lüdenscheid, Meschede, Soest/Welver; Hochschule; Unterhaltsreinigung bzw. Glas- und Rahmenreinigung je Standortlos auf beiden Seiten.
- C (Stütze): Auftraggeber ja, CPV ja, Titel ähnlich (wortgleich „Unterhalts- und Glas- und Rahmenreinigung“), Losstruktur gleich (10 Lose, gleicher Schnitt; Los 5 2026 um „Ense“ ergänzt).
- Überschneidung der Objekte: 12 von 14 (kürzere Seite 2026, 86 %); 12 von 15 (längere Seite 2023, 80 %). Lose mit Überschneidung: alle 10; Abweichungen nur in Los 4/9 (Meschede) und Los 5/10 (Soest/Welver/Ense).
- Ergebnis: teilmenge (Die kürzere Liste ist zu 86 % auf der längeren belegt; da sich die Listen in drei bzw. zwei Adressen unterscheiden, ist „nahezu deckungsgleich“ zweifelhaft, deshalb nach der Rangfolge das vorsichtigere Urteil teilmenge statt objektgleich. Siehe Grenzfälle.)
- Vorgänger: 328497-2023 (result, vor eForms, 2023-06-02) mit Ausschreibung 157336-2023 (competition, vor eForms, 2023-03-15)
- Beleg: 157336-2023, II.2.3 Los 2: „Frauenstuhlweg 31 58644 Iserlohn, … Baarstraße 6 58636 Iserlohn, … Baarstraße 5 58636 Iserlohn“; Testfall LOT-0002: dieselben drei Adressen.
- Vorgänger mit Vertrag: 328497-2023 (Vertragsschluss 2023-05-24; u. a. Piepenbrock, CLEAN Excellence, Wackler)
- Vorgänger-Ende: Grundlaufzeit 2025-06-30, Höchstende 2027-06-30; Herkunft: grundlaufzeit (157336-2023, II.2.7: DATE_START 2023-07-01, DATE_END 2025-06-30, „kann maximal zweimal um jeweils ein weiteres Jahr verlängert werden“)
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-07-01, nach dem Ende der Grundlaufzeit; Einschätzung: der Vertrag wurde einmal verlängert)
- Weitere Fakten: 62542-2019/207277-2019 (FH Südwestfalen, vor eForms) nicht geöffnet; älter als der gefundene Vorgänger.
- Abfragen/XML: 0/2

### U48 – 47380-2026 (2026-01-22) – Stadtwerke Kirchheim unter Teck
- Objekt(e): „Reinigung des Freibads in Kirchheim unter Teck von März bis September, Reinigung der Büros in der Betriebsstätte Hans-Böckler-Straße 3
  und Reinigung der Tiefgaragen Krautmarkt und Schweinemarkt“; LOT-0001 „Reinigungsdienstleistungen im Gebäude Stadtwerke Hans-Böckler-Straße 3 und im Freibad an der Jesinger Straße“, 73230 Kirchheim unter Teck. Keine Flächen.
- Leistungsart (je Los): Los 1 Unterhaltsreinigung (Büros 260 Reinigungstage, Freibad 153 Reinigungstage), CPV 90910000; Glas- oder Grundreinigung nicht genannt.
- Suchschritte:
  - lokal: `Kirchheim unter Teck|Kirchheim/Teck|Kirchheim u` → 14 (Stadtwerke: 561967-2020, 285809-2022; Stadtverwaltung: 561973-2020/39631-2021, 52970-2021/416538-2021; BKK Scheufelen, BA, Autobahn GmbH – andere Auftraggeber/Objekte).
  - Keine API-Abfrage nötig (Suche A ergab Kandidaten mit Objektnennung).
  - XML geöffnet: 561967-2020, 285809-2022 (+1 Testfall).
- A (Identität): übereinstimmend für die gemeinsamen Objekte  Details: 561967-2020: „Objekten der Stadtwerke Kirchheim unter Teck (Büros in der Innenstadt und am Standort Hans-Böckler-Straße 3 sowie im Freibad an der Jesinger Straße“. Gemeinsam: Hans-Böckler-Straße 3, Freibad Jesinger Straße. Nur 2026: Tiefgaragen Krautmarkt und Schweinemarkt. Nur 2020: „Büros in der Innenstadt“ (ohne Adresse, zählt nicht als belegtes Objekt).
- B (Objektraum): erkennbar und übereinstimmend  Details: Kirchheim unter Teck; Betriebsgebäude/Büros und Freibad der Stadtwerke; Unterhaltsreinigung auf beiden Seiten (2020 zusätzlich Grund- und Glasreinigung im selben Los; kein Wechsel der Hauptleistung).
- C (Stütze): Auftraggeber ja, CPV nein (2020 90911000, 2026 90910000), Titel ähnlich, Losstruktur gleich (1 Los).
- Überschneidung der Objekte: 2 von 2 belegten Objekten der kürzeren Seite (2020; mit „Büros in der Innenstadt“ als drittem Objekt 2 von 3 = 67 %); längere Seite 2026 2 von 4 (Tiefgaragen zusätzlich).
- Ergebnis: teilmenge
- Vorgänger: 285809-2022 (result, vor eForms, 2022-05-27) mit Ausschreibung 561967-2020 (competition, vor eForms, 2020-11-23)
- Beleg: 561967-2020, II.1.4: „Büros in der Innenstadt und am Standort Hand-Böckler-Straße 3 sowie im Freibad an der Jesinger Straße“; Testfall LOT-0001 Titel: „Gebäude Stadtwerke Hans-Böckler-Straße 3 und im Freibad an der Jesinger Straße“, dazu „Tiefgaragen Krautmarkt und Schweinemarkt“.
- Vorgänger mit Vertrag: 285809-2022 (Vertragsschluss 2021-03-08, Glanzgruppe Gebäudereinigung GmbH)
- Vorgänger-Ende: 2025-12-31 (abgeleitet); Herkunft: hoechstende (561967-2020: Laufzeit „24“ Monate, „Die Reinigungsleistungen ab 1.1.2024 und 1.1.2025 werden als Option mit ausgeschrieben“; Beginn nicht angegeben, das Ende der Grundlaufzeit ist damit vermutlich 2023-12-31, aber nicht ausdrücklich genannt)
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall: Ende 2028-02-29, Optionen „bis längstens 28.02.2030“; Beginn nicht angegeben, nach Einschätzung 2026-03-01, also nach dem Höchstende)
- Abfragen/XML: 0/2

### U49 – 29273-2026 (2026-01-15) – Stadt Schwarzenbek
- Objekt(e): „Unterhalts- und Glasreinigung diverser Liegenschaften im Stadtgebiet der Stadt Schwarzenbek“, 21493 Schwarzenbek, keine Objektliste.
  LOT-0001 „Unterhaltsreinigung von 14 Objekten mit rund 1.500.000 Quadratmetern Jahresreinigungsfläche“; LOT-0002 „Glas- und Rahmenreinigung von 18 Objekten“ (Beschreibung: 20 Objekte) „mit rund 5.300 Quadratmetern Jahresreinigungsfläche“.
- Leistungsart (je Los): Los 1 Unterhaltsreinigung; Los 2 Glas- und Rahmenreinigung.
- Suchschritte:
  - lokal: `Schwarzenbek` → 9 (Stadt Schwarzenbek: 492553-2023 competition; 511226-2025, 512657-2025, 658197-2025 „6 Objekte“; sonst BA, GMSH – andere Objekte).
  - q01 (Suche C): `FT~"Schwarzenbek" AND classification-cpv=909* AND [Zeitraum]` → 14 (zusätzlich Kreis Herzogtum Lauenburg 441564-2016, GMSH; kein Zuschlag zu 492553-2023).
  - XML geöffnet: 492553-2023, 658197-2025, 511226-2025 (+1 Testfall).
- A (Identität): nicht vergleichbar  Details: 492553-2023 (5 Lose: „allgemeine Objekte der Stadt Schwarzenbek“, „Objekte der Grund- und Gemeinschaftsschule“, „Objekte des Schulverbandes Schwarzenbek Nordost“, Glas Stadt, Glas Schulverband) nennt weder Objekte noch Zahlen noch Flächen („Eine Auflistung aller Liegenschaften ist in den Vergabeunterlagen enthalten“).
  511226-2025/658197-2025: „Unterhalts- und Grundreinigung von 6 Objekten mit einer Jahresreinigungsfläche von ca. 3.500.000 Quadratmetern“ – Gebäudezahl (6 gegenüber 14) und Fläche (3,5 Mio. gegenüber 1,5 Mio. m²) widersprechen dem Testfall → nicht objektgleich.
- B (Objektraum): nicht erkennbar  Details: Gebiet Schwarzenbek; Objektart „diverse Liegenschaften“ einer Stadt (Testfall) bzw. „allgemeine Objekte der Stadt“ (2023) nicht erkennbar; Leistungen Unterhalts- und Glas-/Rahmenreinigung auf beiden Seiten (2023 Lose 1 und 4).
- C (Stütze): Auftraggeber ja, CPV ja, Titel ähnlich, Losstruktur anders (5 gegenüber 2 Lose).
- Überschneidung der Objekte: keine Listen
- Ergebnis: unklar
- Tendenz: keine (beide Seiten unspezifisch, keine Zahlen oder Flächen in 492553-2023; ob die 14 Objekte des Testfalls den „allgemeinen Objekten der Stadt“ von 2023 entsprechen, ist aus TED nicht ablesbar)
- Vorgänger (Kandidat bei unklar): 492553-2023 (competition, vor eForms, 2023-08-14), Lose 1 und 4
- Beleg: 492553-2023, II.2.4 Los 1: „Sämtliche Erfüllungsorte liegen in 21493 Schwarzenbek. Eine Auflistung aller Liegenschaften ist in den Vergabeunterlagen enthalten.“; Testfall: „Unterhaltsreinigung von 14 Objekten“ ohne Liste.
- Vorgänger mit Vertrag: nicht gefunden (kein Zuschlag zu 492553-2023 auf TED, weder lokal noch per q01)
- Vorgänger-Ende: unbekannt (laut Ausschreibung 492553-2023 geplant DATE_START 2024-01-01, DATE_END 2028-07-31, „zweimalige Verlängerung von jeweils einem Jahr“); Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar (falls 492553-2023 so vergeben wurde, läge der Testfallbeginn 2026-05-01 mehr als 3 Monate vor dem geplanten Ende 2028-07-31)
- Abfragen/XML: 1/3

### U50 – 87147-2026 (2026-02-06) – Technisches Betriebszentrum AöR (Flensburg)
- Objekt(e): keine Objekte genannt. „Überlassung von Reinigungskräften/Vertretungskräften für die Unterhaltsreinigung für die Dauer von 4 Jahren, Az: 19/2026“, Leistungsort 24941 Flensburg. Keine Stunden- oder Flächenangabe.
- Leistungsart (je Los): Los 1 Arbeitnehmerüberlassung (Vertretungskräfte) für Unterhaltsreinigung, CPV 90911200.
- Suchschritte:
  - lokal: `Flensburg` → 54 (TBZ: 170349-2022, 289728-2022; sonst Hochschule, Dansk Skoleforening, Europa-Universität, KBA, Kreis Schleswig-Flensburg, GMSH, BA u. a. – andere Auftraggeber und Objekte).
  - Keine API-Abfrage nötig (Suche A ergab den Kandidaten; der Testfall nennt keinen Objektnamen für eine Volltextsuche).
  - XML geöffnet: 170349-2022, 289728-2022 (+1 Testfall).
- A (Identität): nicht vergleichbar  Details: Beide Seiten ohne Objekt; 2022 nennt als Ort nur den Sitz „Technisches Betriebszentrum AöR Schleswiger Straße 76 24941 Flensburg“ und „Jahresbedarf … ca. 10.000 Stunden“; der Testfall nennt keine Stunden.
- B (Objektraum): nicht erkennbar  Details: Gebiet Flensburg auf beiden Seiten; Leistung gleich (Vertretungskräfte für Unterhaltsreinigung); Objektart auf keiner Seite genannt (2022 nur indirekt „in den Schulferien … weniger Krankheitsvertretungen“).
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich („Vertretungskräfte Gebäudereinigung, Vertrag für vier Jahre“ / „Überlassung von Reinigungskräften/Vertretungskräften … für die Dauer von 4 Jahren“), Losstruktur gleich (1 Los); Zuschlagskriterien gleich („Anzahl Mitarbeiter im Großraum Flensburg“, „im Nahbereich“, „Entfernung der Bereichsleitung“).
- Überschneidung der Objekte: keine Listen
- Ergebnis: unklar (Personalgestellung ohne Objekt; die Urteilsregeln setzen ein Objekt voraus, siehe Grenzfälle)
- Tendenz: eher dafür (gleicher Auftraggeber, gleiche Leistung „Vertretungskräfte für die Unterhaltsreinigung“, gleicher Ort und wortgleiche Zuschlagskriterien)
- Vorgänger (Kandidat bei unklar): 289728-2022 (result, vor eForms, 2022-05-30) mit Ausschreibung 170349-2022 (competition, vor eForms, 2022-04-01)
- Beleg: 170349-2022, II.1.4: „benötigt das Technische Betriebszentrum … für die Unterhaltsreinigung Reinigungskräfte mit Erfahrung im rationellen Reinigungsverfahren“; Testfall: „Überlassung von Reinigungskräften/Vertretungskräften für die Unterhaltsreinigung“.
- Vorgänger mit Vertrag: 289728-2022 (Vertragsschluss 2022-05-25, Beyersdorf Dienstleistungen GmbH & Co. KG)
- Vorgänger-Ende: 2026-05-31; Herkunft: grundlaufzeit (170349-2022: „Für den Zeitraum vom 01.06.2022 bis 31.05.2026“, keine Verlängerung genannt)
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-06-01)
- Abfragen/XML: 0/2

### U51 – 90864-2026 (2026-02-09) – Freistaat Bayern, vertreten durch die Universität Bayreuth
- Objekt(e): Unterhaltsreinigung „von verschiedenen Gebäudekomplexen in 4 Losen“ mit Bauwerkslisten:
  LOT-0001 Campus WEST: Audimax, B1, B2, B3, B4-Glashaus, B6–B14, BLC, FAN, GEO I–III, GW I, INF, LIM, NW III, NW IV, ÖBG, PBS (26 Bauwerke) sowie Hugo-Rüdel-Straße 8 und 10, Parsifalstraße 25, Prieser Straße 2, Weiherstraße 26, Sophian-Kolb-Straße 6;
  LOT-0002 Campus OST: BGI, GW II, Sport, TAO, ZT, ZUV, ZUV-DV, FZA sowie Dr.-Hans-Frisch-Straße 1-3, Leuschnerstraße 51, Ludwig-Thoma-Straße 36a, Wölfelstraße 2;
  LOT-0003 Campus ZENTRAL: RW I, RW II, ZB, NW I, NW II, Gästehaus; LOT-0004 Kulmbach: Fritz-Hornschuch-Straße 9 und 13, Hans-Hacker-Straße 10, Schloss Thurnau-Nord (IFLG), Schloss Thurnau-Süd (FIMT). Zusammen 55 Objekte. Keine Flächen (nur Optionen für Neubauten ZUV II, E&I).
- Leistungsart (je Los): Los 1–4 Unterhaltsreinigung (CPV 90911200).
- Suchschritte:
  - lokal: `Universität Bayreuth|Bayreuth` → 190 (Universität Bayreuth: 443636-2016, 485376-2020/28537-2021, 537842-2023/773594-2023; übrige andere Auftraggeber).
  - Keine API-Abfrage nötig (Suche A ergab einen Kandidaten mit vollständiger Bauwerksliste).
  - XML geöffnet: 773594-2023, 537842-2023 (+1 Testfall).
- A (Identität): übereinstimmend (Objektliste nahezu deckungsgleich)  Details: 537842-2023/773594-2023 Lose 1–3 (Unterhaltsreinigung) nennen 57 Objekte
  (Los 1: 28 Bauwerke inkl. NW I, NW II, 6 Liegenschaften, „optional das Gästehaus“; Los 2: 11 Bauwerke inkl. RW I, RW II, ZB, 4 Liegenschaften; Los 3 Kulmbach: 7 Liegenschaften).
  Gemeinsam 54: alle 26 Bauwerke von Campus WEST, 5 Liegenschaften (ohne Sophian-Kolb-Straße 6), alle 12 Objekte Campus OST, alle 6 Objekte Campus ZENTRAL (2023 in Los 1/2 enthalten), 5 Kulmbacher Objekte.
  Nur 2023: Geschwister-Scholl-Platz, Kressenstein 15, Lichtenfelser Straße 33 (Living Lab). Nur 2026: Sophian-Kolb-Straße 6. Gebäudezahl 57 gegenüber 55 (nicht gleich). Keine Flächen.
- B (Objektraum): erkennbar und übereinstimmend  Details: Campus Bayreuth mit Außenliegenschaften und Campus Kulmbach; Hochschule; Unterhaltsreinigung auf beiden Seiten (2023 zusätzlich Los 4 Glasreinigung, im Testfall nicht enthalten – betrifft nur dieses Los).
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich (wortgleich „Leistungen für die Gebäudereinigung“), Losstruktur anders (2023: 3 Unterhaltslose + Glas; 2026: 4 Unterhaltslose, Campus ZENTRAL neu geschnitten).
- Überschneidung der Objekte: 54 von 55 (kürzere Seite 2026, 98 %); 54 von 57 (2023, 95 %). Lose mit Überschneidung: 2026 Los 1 ↔ 2023 Los 1; Los 2 ↔ Los 2; Los 3 ↔ Teile von Los 1 und 2; Los 4 ↔ Los 3.
- Ergebnis: objektgleich_mittel (Objektliste nahezu deckungsgleich = ein A-Merkmal; Gebäudenamen und Adressen gehören zu derselben Liste und werden nicht doppelt gezählt; Gebäudezahl 57/55 nicht gleich, keine Flächen → kein zweites A-Merkmal)
- Vorgänger: 773594-2023 (result, eForms, 2023-12-20) mit Ausschreibung 537842-2023 (competition, vor eForms, 2023-09-06)
- Beleg: 773594-2023, LOT-0002: „Unterhaltsreinigung für die Liegenschaft "Campus Bayreuth" mit den Bauwerken BGI, GW II, RW I, RW II, Sport, TAO, ZB, ZT, ZUV, ZUV-DV, FZA … "Dr.-Hans-Frisch-Straße 1-3", "Leuschnerstraße 51", "Ludwig-Thoma-Straße 36a", "Wölfelstraße 2"“; Testfall LOT-0002: dieselben ohne RW I, RW II, ZB (diese in LOT-0003).
- Vorgänger mit Vertrag: 773594-2023 (Vertragsschluss 2023-12-05, alle 4 Lose vergeben)
- Vorgänger-Ende: Grundlaufzeit Los 1 bis 2026-02-28, Lose 2–4 bis 2026-03-31; Höchstende 2028-02-29 bzw. 2028-03-31; Herkunft: grundlaufzeit (537842-2023, II.2.7 Los 1: DATE_START 2024-03-01, DATE_END 2026-02-28, „zweimal um jeweils zwölf Monate bis zum 29.02.2028 … zu verlängern“; 773594-2023 nennt je Los 2024-03-01 bis 2028-03-31, also das Höchstende)
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-07-01, nach dem Ende der Grundlaufzeit)
- Abfragen/XML: 0/2

### U52 – 160356-2026 (2026-03-09) – Stadt Bad Rappenau
- Objekt(e): keine Objektliste und keine Objektzahlen; Lose nach Stadtteilen: LOT-0001 „Bad Rappenau, Zimmerhof und Heinsheim“, LOT-0002 „Fürfeld und Treschklingen“,
  LOT-0003 „Babstadt, Grombach und Obergimpern“, LOT-0004 „Stadtgebiet Bad Rappenau“; 74906 Bad Rappenau.
- Leistungsart (je Los): Los 1–3 Unterhalts-/Grundreinigung (CPV 90910000); Los 4 Glas-/Rahmenreinigung (CPV 90911300).
- Suchschritte:
  - lokal: `Rappenau` → 5 (Stadt Bad Rappenau: 146943-2019/314060-2019, 244484-2023; Schwärzbergklinik 2020/2024 – anderer Auftraggeber).
  - q01 (Suche C): `(FT~"Rappenau" OR FT~"Treschklingen" OR FT~"Obergimpern") AND classification-cpv=909* AND [Zeitraum]` → 10 (keine weiteren Notices der Stadt; kein Zuschlag zu 244484-2023).
  - XML geöffnet: 244484-2023, 314060-2019 (+1 Testfall).
- A (Identität): nicht vergleichbar  Details: Testfall ohne Objektzahl und -liste. 244484-2023: Los 1 „Kernstadt und Stadtteil Heinsheim - 15 Objekte“, Los 2 „Fürfeld und Treschklingen - 9 Objekte“, Los 3 „Babstadt, Grombach und Obergimpern - 12 Objekte“, Los 4 Glas „36 Objekte“; Objekte „in den Vergabeunterlagen aufgeführt“.
- B (Objektraum): nicht erkennbar  Details: Gebiet (Stadtteile je Los) auf beiden Seiten gleich, Testfall Los 1 zusätzlich „Zimmerhof“; Leistungen je Los gleich (Unterhalts-/Grundreinigung bzw. Glas). Objektart nur 2023 genannt („Schulen, Sport- und Kindertagesstätten, öffentliche Gebäude“), im Testfall nicht → auf einer Seite nicht erkennbar.
- C (Stütze): Auftraggeber ja, CPV teils (2023 90910000/90911000/90911200, 2026 90910000/90911300), Titel ähnlich, Losstruktur gleich (4 Lose, gleicher Stadtteilschnitt).
- Überschneidung der Objekte: keine Listen
- Ergebnis: unklar
- Tendenz: eher dafür (gleicher Losschnitt nach denselben Stadtteilen und gleiche Leistung je Los; nur „Zimmerhof“ neu)
- Vorgänger (Kandidat bei unklar): 244484-2023 (competition, vor eForms, 2023-04-25); davor 314060-2019 (result, vor eForms, 2019-07-05) mit 146943-2019 (competition), gleicher Losschnitt (Los 1 „Bad Rappenau u. Heinsheim“, Los 3 „Babstadt, Grombach, Obergimpern“, Los 4 Glas „Bad Rappenau mit Stadtteilen“)
- Beleg: 244484-2023, II.2.4 Los 2: „Unterhalts- und Grundreinigung im Stadtteil Fürfeld und Treschklingen - 9 Objekte“; Testfall LOT-0002: „Fürfeld und Treschklingen“.
- Vorgänger mit Vertrag: nicht gefunden (kein Zuschlag zu 244484-2023 auf TED); letzter belegter Vertrag 314060-2019 (Vertragsschluss 2019-06-27)
- Vorgänger-Ende: 2026-08-30 laut Ausschreibung 244484-2023 (DATE_START 2023-09-01, DATE_END 2026-08-30, „Maximal zwei Mal um jeweils ein Jahr“), Vertrag auf TED nicht belegt; Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-08-01, rund einen Monat vor dem geplanten Ende; ohne belegten Vertrag nur eingeschränkt aussagekräftig)
- Abfragen/XML: 1/2

### U53 – 123318-2026 (2026-02-20) – Landkreis Freising
- Objekt(e): keine Objektliste. LOT-0001 „Amtsgebäude und Schulen im Landkreis Freising“, LOT-0002 „Schulen im Landkreis Freising“; Leistungsort 85356 Freising.
- Leistungsart (je Los): Los 1 und Los 2 Glas- und Rahmenreinigung (CPV 90911300).
- Suchschritte:
  - lokal: `Freising` in `buyer-name` → 33 (Landkreis Freising: 189982-2018/345359-2018, 388668-2018/559265-2018, 510695-2019/97293-2020, 201806-2020/415675-2020,
    186962-2024/466323-2024, 466300-2024; sonst Stadt Freising, Stadtwerke, Amtsgericht, Caritas, Erzdiözese – andere Auftraggeber).
  - q01: `buyer-name~"Landkreis Freising" AND classification-cpv=909* AND [Zeitraum]` → 11 (dieselben; kein Zuschlag zu 466300-2024).
  - q02 (Suche C): `(FT~"Glasreinigung" AND FT~"Freising") AND classification-cpv=909* AND [Zeitraum]` → 80 (keine weiteren Notices des Landkreises).
  - XML geöffnet: 466300-2024, 466323-2024, 559265-2018, 388668-2018, 345359-2018 (+1 Testfall).
- A (Identität): nicht vergleichbar (Liste nur auf einer Seite)  Details: 466300-2024 „Glasreinigung für den Landkreis Freising“, 2 Lose: Los 1 „Berufsschule Freising, Camerloher Gymnasium Freising, Domgymnasium Freising, FOS/BOS Freising,
  Karl-Meichelbeck-Realschule Freising, Wirtschaftsschule Freising, Landratsamt Freising + Außenstellen“; Los 2 „Gymnasium Moosburg, Kastulus Realschule Moosburg, Realschule Au/Hallertau“. Testfall ohne Liste.
  Dieselben Objektgruppen waren in 186962-2024/466323-2024 die Glaslose 11 und 13, beide ohne Zuschlag („clos-nw“); Glaslos 12 (Förderschulzentrum, Imma-Mack-Realschule Eching, Oskar-Maria-Graf-Gymnasium Neufahrn, Realschule Gute Änger) wurde vergeben.
- B (Objektraum): erkennbar und übereinstimmend  Details: Landkreis Freising; Los 1 Amtsgebäude und Schulen ↔ 466300-2024 Los 1 Schulen + Landratsamt; Los 2 Schulen ↔ Los 2 Schulen (Moosburg, Au); Leistung Glas(- und Rahmen)reinigung auf beiden Seiten.
- C (Stütze): Auftraggeber ja, CPV ja (90911300), Titel ähnlich, Losstruktur gleich (2 Lose: Amtsgebäude+Schulen / Schulen).
- Überschneidung der Objekte: nur eine Seite mit Liste (nicht berechenbar)
- Ergebnis: objektgleich_mittel (Zweifel: Testlos 2 „Schulen“ lässt offen, welche Schulgruppe gemeint ist; nur Los 1 ist über „Amtsgebäude“ eindeutig der Gruppe mit dem Landratsamt zuzuordnen. Nach den Regeln reicht übereinstimmender Objektraum bei fehlender Liste auf einer Seite für „mittel“.)
- Vorgänger: 466300-2024 (competition, eForms, 2024-08-02); dieselben Objektgruppen zuvor als Lose 11 und 13 in 186962-2024 (competition, eForms, 2024-03-28) / 466323-2024 (result, eForms, 2024-08-02, für diese Lose ohne Zuschlag)
- Beleg: 466300-2024, LOT-0001: „Objekte Los 1 … Landratsamt Freising + Außenstellen“ (dazu sechs Schulen); Testfall LOT-0001 „Amtsgebäude und Schulen im Landkreis Freising“, Glas- und Rahmenreinigung.
- Vorgänger mit Vertrag: nicht gefunden (kein Zuschlag zu 466300-2024 auf TED; in 466323-2024 Lose 11 und 13 „clos-nw“, also ohne Vertrag; ein davor liegender Glasvertrag für diese Objektgruppen ist auf TED nicht belegt – 345359-2018 betrifft nur Wirtschaftsschule und OMG Neufahrn, 559265-2018 Unterhaltsreinigung KMRS)
- Vorgänger-Ende: unbekannt (466300-2024: Laufzeit „36“ Monate, „2 x um 12 Monate verlängert“, Beginn nicht angegeben); Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 2/5

### U54 – 100442-2026 (2026-02-12) – Verein Jugendpflege Vilshofen e. V.
- Objekt(e): „Unterhaltsreinigung für das staatlich anerkannte private Sonderpädagogische Förderzentrum (Förderschule) sowie die staatlich anerkannte private Förderberufsschule
  und einen Teilbereich der Werkstätte des Berufsbildungszentrums in Vilshofen“ (LOT-0000). „Der jährliche Reinigungsbedarf für alle Flächen beträgt insgesamt ca. 890.000 qm bei 187 Schultagen. Hinzu kommt die Reinigung von Glasflächen mit insgesamt ca. 2.100 qm“ (zweimal jährlich).
- Leistungsart (je Los): ein Los, Unterhaltsreinigung mit Glasflächenreinigung (CPV 90911200).
- Suchschritte:
  - lokal: `Vilshofen|Jugendpflege` → 18 (Verein: 83582-2019, 209315-2019; übrige andere Auftraggeber, Treffer über „Jugendzentrum“ u. ä.).
  - q01 (Suche C): `(FT~"Jugendpflege" OR FT~"Förderberufsschule" OR FT~"Vilshofen") AND classification-cpv=909* AND [Zeitraum]` → 30 (vom Verein nur 83582-2019, 209315-2019).
  - XML geöffnet: 83582-2019, 209315-2019 (+1 Testfall).
- A (Identität): abweichend  Details: Objekte 2019: „die beiden durch den Verein für Jugendpflege Vilshofen betreuten Schulen (Sonderpädagogisches Förderzentrum und Förderberufsschule) am Standort in Vilshofen“; 2026 zusätzlich „Teilbereich der Werkstätte des Berufsbildungszentrums“.
  Jahresreinigungsfläche 800 000 qm (2019) gegenüber 890.000 qm (2026), +11 % (abweichend); Glasfläche 880 gegenüber 2.100 qm (abweichend).
- B (Objektraum): erkennbar und übereinstimmend  Details: Vilshofen, Förderschule und Förderberufsschule des Vereins; Unterhaltsreinigung mit Glasflächen auf beiden Seiten.
- C (Stütze): Auftraggeber ja, CPV ja (90911200), Titel ähnlich (fast wortgleich „Unterhaltsreinigung Verein für Jugendpflege e. V. Vilshofen“), Losstruktur gleich (1 Los); Beschreibungstext fast wortgleich.
- Überschneidung der Objekte: 2 von 2 (kürzere Seite 2019, 100 %); längere Seite 2026 mit 3 Objekten (zusätzlich Teil der Werkstätte des Berufsbildungszentrums).
- Ergebnis: teilmenge
- Vorgänger: 209315-2019 (result, vor eForms, 2019-05-06) mit Ausschreibung 83582-2019 (competition, vor eForms, 2019-02-21)
- Beleg: 83582-2019, II.2.4: „Unterhaltsreinigung der Förderberufsschule sowie des sonderpädagogischen Förderzentrums in Vilshofen … ca. 800 000 qm bei 187 Schultagen“; Testfall: dieselben Schulen „und einen Teilbereich der Werkstätte des Berufsbildungszentrums“, „ca. 890.000 qm bei 187 Schultagen“.
- Vorgänger mit Vertrag: 209315-2019 (Vertragsschluss 2019-04-11, Götz-Gebäudemanagement Ostbayern)
- Vorgänger-Ende: 2023-04-28; Herkunft: grundlaufzeit (83582-2019, II.2.7: DATE_START 2019-04-29, DATE_END 2023-04-28; „Der Vertrag endet zum 28.4.2023“, keine Verlängerung genannt)
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-05-02, nach dem Vertragsende). Einschätzung: Zwischen 2023 und 2026 lief vermutlich ein Vertrag, der nicht auf TED (CPV 909) bekannt gemacht wurde; der gefundene Vorgänger ist dann nicht der unmittelbare.
- Abfragen/XML: 1/2

### U55 – 153719-2026 (2026-03-05) – Die Autobahn GmbH des Bundes – NL Nordwest
- Objekt(e): „Betrieb, Wartung, Erhaltung BAB-GAN BK 1000, NL Nordwest - AS Bad Gandersheim, Reinigung PWC-Anlagen (2 Lose)“: LOT-0001 „Reinigung der PWC-Anlagen im Bezirk der Autobahnmeisterei Hildesheim“ (31135 Hildesheim),
  LOT-0002 „… im Bezirk der Autobahnmeisterei Göttingen“ (37081 Göttingen). Keine Liste der Anlagen.
- Leistungsart (je Los): Los 1 und Los 2 Reinigung von WC-Anlagen auf unbewirtschafteten Rastplätzen (PWC), CPV 90911200.
- Suchschritte:
  - lokal: `Autobahnmeisterei (Hildesheim|Göttingen)|PWC.*(Hildesheim|Göttingen)|Bad Gandersheim|BAB-GAN` → 11 (nur BA, Autobahn-Zentrale, UMG – keine PWC-Reinigung Hildesheim/Göttingen);
    lokal: `Nordwest` in `buyer-name` (Autobahn) → PWC-Verfahren der NL Nordwest nur für AS Kassel (214308-2024/386579-2024, 449056-2025/602309-2025), AS Fulda (640082-2024/641824-2024/789489-2024), AS Hannover (359130-2025/556141-2025), Bereich Oldenburg (43552-2023/212512-2023);
    lokal: `PWC|Rastanlage|Rastpl|WC-Anlage` (gefiltert auf Nordwest/Niedersachsen) → dieselben; lokal: `Landesbehörde für Straßenbau|NLStBV` in `buyer-name` → 5 (GB Osnabrück, GB Goslar Fahrbahnreinigung – andere Objekte).
  - q01 (Suche C): `(FT~"Autobahnmeisterei Hildesheim" OR FT~"Autobahnmeisterei Göttingen" OR FT~"Bad Gandersheim") AND classification-cpv=909* AND [Zeitraum]` → 20 (Staatliches Baumanagement Südniedersachsen, Autobahn GmbH 476368-2020/56326-2021/67287-2022, BA, UMG).
  - q02: `(FT~"PWC" OR FT~"WC-Anlagen") AND (FT~"Hildesheim" OR FT~"Göttingen") AND classification-cpv=909* AND [Zeitraum]` → 2 (Autobahn NL Ost, Halle).
  - q03 (Suche B, vor Gründung der Autobahn GmbH): `(FT~"Rastplatz" OR FT~"Rastplätze" OR FT~"WC-Anlage" OR FT~"PWC") AND buyer-city="Hannover" AND classification-cpv=909* AND publication-date>=20161001 AND publication-date<20210101` → 2 (Leibniz Universität Hannover).
  - XML geöffnet: 789489-2024, 212512-2023, 56326-2021 (+1 Testfall).
- A (Identität): widersprüchlich (alle Kandidaten)  Details: 789489-2024: PWC-Anlagen der AM Alsfeld, Fulda, Hoenebach (A4, A5, A7, A66, Außenstelle Fulda); 212512-2023: „20 Stück WC Anlagen … an den Bundesautobahnen A 28, A 29, A31 und A 1 im Bereich Oldenburg“; 56326-2021 Los 4: Unterhaltsreinigung administrativer Bürostandorte, u. a. „Bahnhofstr. 1, 37581 Bad Gandersheim“ (Büro, nicht PWC).
- B (Objektraum): widersprüchlich  Details: anderes Gebiet (Fulda/Oldenburg gegenüber Hildesheim/Göttingen) bzw. andere Objektart (Bürostandort gegenüber Rastplatz-WC).
- C (Stütze): Auftraggeber ja (Autobahn GmbH), CPV ja, Titel ähnlich („Reinigung von PWC-Anlagen“), Losstruktur anders.
- Überschneidung der Objekte: 0
- Ergebnis: kein_vorgaenger
- Vorgänger: –
- Beleg: 212512-2023, II.1.4: „Tägliche Reinigung von 20 Stück WC Anlagen auf unbewirtschafteten Rastplätzen an den Bundesautobahnen A 28, A 29, A31 und A 1 im Bereich Oldenburg“; Testfall: „PWC-Anlagen im Bezirk der Autobahnmeisterei Hildesheim“ bzw. „Göttingen“.
- Vorgänger mit Vertrag: –
- Vorgänger-Ende: unbekannt; Herkunft: unbekannt
- Hinweis auf vorzeitige Neuvergabe: unklar
- Abfragen/XML: 3/3

### U56 – 93751-2026 (2026-02-10) – Zentrale Vergabestelle – Kooperation Landkreis Lüneburg – Harburg (für den Landkreis Lüneburg)
- Objekt(e): 6 Lose mit Objekt- und Adresslisten:
  LOT-0001 Unterhaltsreinigung BBS I–III Lüneburg (BBS I, BBS II, BBS III, Sporthalle des Berufsschulzentrums, 2-Feld-Halle mit AU, Schulgebäude BBS III und IWK; Spillbrunnenweg 1, Am Schwalbenberg 25/26, Am Schierbrunnen 4);
  LOT-0002 Unterhaltsreinigung Kreisverwaltung (Gebäude 1 bis 9, Auf dem Michaeliskloster 4; Büroräume am Springintgut; Büro Fachdienst Umwelt; Konrad-Zuse-Allee 10);
  LOT-0003 Schulzentrum Oedeme (Gymnasium Oedeme, Erweiterung, Große Sporthalle Nord, Oberschule Oedeme, Schulzentrum Oedeme Süd, Turnhalle/Gymnastikhalle, Lehrschwimmbecken);
  LOT-0004 Schulzentrum Bleckede (mit Sporthallen, Schwimmhalle), Gymnasium Bleckede, Kurt-Löwenstein-Schule, Schulzentrum Neuhaus;
  LOT-0005 Glas- und Rahmenreinigung BBS 1–3, SZ Oedeme, Kreisverwaltung, Gymnasium Lüneburg, Schule am Knieberg; LOT-0006 Glas- und Rahmenreinigung Schule am Katzenberg Adendorf, SZ Scharnebeck, SZ Bleckede, Gymnasium Bleckede, Kurt-Löwenstein-Schule, SZ Neuhaus, FTZ Scharnebeck, SZ Dahlenburg, SZ Embsen. Keine Flächen.
- Leistungsart (je Los): Los 1–4 Unterhaltsreinigung (mit Grund-/Ferienreinigung); Los 5 und 6 Glas- und Rahmenreinigung.
- Suchschritte:
  - lokal: `Lüneburg` in `buyer-name` → 54 (Landkreis Lüneburg: 148457-2020/299773-2020, 415041-2020, 646195-2021, 505956-2022/79802-2023, 584542-2023; Kooperation Lüneburg-Harburg: 510751-2024/682643-2024 Baureinigung IGS Embsen; übrige Hansestadt, HWK, Klinikum u. a.);
    lokal: `Oedeme|Spillbrunnen|Schwalbenberg|Michaeliskloster|Bleckede|Scharnebeck` → 15 (eForms-Zeit; nur BImA, Bundeswehr, WSA – andere Objekte).
  - Keine API-Abfrage nötig (Suche A lieferte Kandidaten mit Objektlisten).
  - XML geöffnet: 148457-2020, 299773-2020, 584542-2023, 505956-2022, 79802-2023, 646195-2021 (+1 Testfall).
- A (Identität): übereinstimmend für die gemeinsamen Objekte  Details:
  - 505956-2022/79802-2023 („Gebäudereinigung Los 3+4“): Los 3 „Gymnasium Oedeme mit Sporthallen, Gymnasium Oedeme (Erweiterung), Oberschule Oedeme mit BBS III-Außenstelle, Schulzentrum Oedeme Süd mit Sporthallen und Lehrschwimmbecken“;
    Los 4 „Schulzentrum Bleckede mit Sporthallen und Lehrschwimmbecken … Gymnasium …, Kurt-Löwenstein-Schule, Schulzentrum Neuhaus“ – alle 8 benannten Objekte auch im Testfall (Lose 3 und 4).
  - 148457-2020/299773-2020 (7 Lose, alle Objektgruppen): von 31 benannten Objekten sind 26 auch im Testfall (BBS-Gruppe 6, Kreisverwaltung und Büro FD Umwelt 2, Oedeme 6, Bleckede/Neuhaus 6, Glas Knieberg, Katzenberg, SZ Scharnebeck, FTZ, Dahlenburg, Embsen 6);
    nur 2020: Unterhaltsreinigung Schulzentrum Adendorf, Gymnasium Scharnebeck mit Sporthalle, Turnhalle Scharnebeck, „Gymn. Oedeme (ehem. Schule Schaperdrift)“ (mögliche Entsprechung zu „Gymnasium Oedeme (Erweiterung)“, nicht gezählt); nur 2026: Büroräume am Springintgut, Konrad-Zuse-Allee 10, Gymnasium Lüneburg, Gymnasium Oedeme (Erweiterung).
  - Flächen: 2020 und 2022 Los 4 identisch „ca. 23.357 m2“; im Testfall keine Flächen (nicht vergleichbar).
- B (Objektraum): erkennbar und übereinstimmend  Details: Landkreis Lüneburg; Berufsschulen, Schulzentren mit Sporthallen, Kreisverwaltung; Unterhaltsreinigung je Schulzentrum bzw. Glasreinigung je Objektgruppe auf beiden Seiten.
- C (Stütze): Auftraggeber nein (Testfall: Zentrale Vergabestelle der Kooperation Lüneburg–Harburg; Vorgänger: Landkreis Lüneburg – gleiche Körperschaft), CPV ja, Titel ähnlich, Losstruktur ähnlich (Losschnitt 2020 nahezu gleich, 2026 ohne Unterhaltslos Adendorf/Scharnebeck).
- Überschneidung der Objekte: jüngster Vorgänger 505956-2022/79802-2023: 8 von 8 (kürzere Seite, 100 %), Testfall mit 30 Objekten länger; 148457-2020: 26 von 30 (Testfall, 87 %) bzw. 26 von 31 (2020, 84 %). Lose mit Überschneidung: Testlose 3 und 4 ↔ 2022 Lose 3 und 4; Testlose 1–6 ↔ 2020 Lose 1, 3, 4, 5, 6, 7.
- Ergebnis: teilmenge
- Vorgänger: 79802-2023 (result, vor eForms, 2023-02-07) mit Ausschreibung 505956-2022 (competition, vor eForms, 2022-09-16), betrifft Testlose 3 und 4.
  Weitere Vorgänger (Fakten): 299773-2020 (result, vor eForms, 2020-06-26) mit 148457-2020 (competition, 2020-03-27) für alle Objektgruppen (teilmenge, s. o.);
  646195-2021 (competition, vor eForms, 2021-12-17, Lose 1–4 Unterhaltsreinigung, kein Zuschlag auf TED gefunden);
  584542-2023 (competition, vor eForms, 2023-09-29, „Gebäudereinigung Los 2+5“: Unterhaltsreinigung Oberschule Adendorf/Schulzentrum Scharnebeck und Kreisverwaltung; kein Zuschlag auf TED gefunden) – gegenüber dem Testfall nur „unklar“, weil Adendorf/Scharnebeck im Testfall nur als Glasreinigung vorkommen (andere Leistungsart) und damit nur die Kreisverwaltung (1 von 3 Objektgruppen) mit gleicher Leistung übereinstimmt.
- Beleg: 505956-2022, II.2.4 Los 4: „Schulzentrum Bleckede mit Sporthallen und Lehrschwimmbecken … Kurt-Löwenstein-Schule … Schulzentrum Neuhaus“; Testfall LOT-0004: „Schulzentrum Bleckede, SZ Bleckede Sporthallen, SZ Bleckede Schwimmhalle, Gymnasium Bleckede, Kurt-Löwenstein-Schule, Schulzentrum Neuhaus“.
- Vorgänger mit Vertrag: 79802-2023 (Lose 3 und 4, „Gebäudereinigung“, Vertrag 35.22)
- Vorgänger-Ende: Grundlaufzeit 2025-07-31, Höchstende 2026-07-31; Herkunft: grundlaufzeit (505956-2022, II.2.7: DATE_START 2023-01-01, DATE_END 2025-07-31, „verlängert sich 1 x um ein Jahr … endet spätestens am 31.07.2026“).
  Für die übrigen Testlose: 148457-2020 Grundlaufzeit bis 2023-07-31, „endet spätestens am 31.7.2026“ (Höchstende).
- Hinweis auf vorzeitige Neuvergabe: nein (Testfall Beginn 2026-07-01 bzw. 2026-08-01, nach dem Ende der Grundlaufzeit)
- Abfragen/XML: 0/6

## Übersichtstabelle

| U | Notice | Ergebnis | Tendenz | jüngster Vorgänger | alle Notices desselben Vorgängers | Vorgänger mit Vertrag | Vorgänger-Ende | Herkunft | vorzeitig |
|---|---|---|---|---|---|---|---|---|---|
| U43 | 127506-2026 | objektgleich_mittel | – | 343780-2023 | 207575-2023, 343780-2023 | 343780-2023 | 2026-07-31 (Höchstende 2029-07-31) | grundlaufzeit | nein |
| U44 | 134489-2026 | objektgleich_mittel | – | 362257-2022 | 170455-2022, 362257-2022 | 362257-2022 | 2024-07-31 (Höchstende 2026-07-31) | grundlaufzeit | nein |
| U45 | 62104-2026 | unklar | keine | (Kandidat) 477144-2023 | 117265-2023, 477144-2023; Los 3: 471420-2023, 740328-2023 | 477144-2023 / 740328-2023 | 2027-10-15 bis 2027-12-14 (je Los) | grundlaufzeit | unklar |
| U46 | 55335-2026 | kein_vorgaenger | – | – | – | – | unbekannt | unbekannt | unklar |
| U47 | 134081-2026 | teilmenge | – | 328497-2023 | 157336-2023, 328497-2023 | 328497-2023 | 2025-06-30 (Höchstende 2027-06-30) | grundlaufzeit | nein |
| U48 | 47380-2026 | teilmenge | – | 285809-2022 | 561967-2020, 285809-2022 | 285809-2022 | 2025-12-31 (abgeleitet) | hoechstende | nein |
| U49 | 29273-2026 | unklar | keine | (Kandidat) 492553-2023 | 492553-2023 | nicht gefunden | unbekannt (geplant 2028-07-31) | unbekannt | unklar |
| U50 | 87147-2026 | unklar | eher dafür | (Kandidat) 289728-2022 | 170349-2022, 289728-2022 | 289728-2022 | 2026-05-31 | grundlaufzeit | nein |
| U51 | 90864-2026 | objektgleich_mittel | – | 773594-2023 | 537842-2023, 773594-2023 | 773594-2023 | 2026-02-28 (Los 1) / 2026-03-31 (Lose 2–4); Höchstende 2028-02-29 / 2028-03-31 | grundlaufzeit | nein |
| U52 | 160356-2026 | unklar | eher dafür | (Kandidat) 244484-2023 | 244484-2023 (davor 146943-2019, 314060-2019) | nicht gefunden (letzter belegter Vertrag 314060-2019) | unbekannt (geplant 2026-08-30) | unbekannt | nein |
| U53 | 123318-2026 | objektgleich_mittel | – | 466300-2024 | 466300-2024; zuvor Lose 11/13 in 186962-2024, 466323-2024 (ohne Zuschlag) | nicht gefunden | unbekannt | unbekannt | unklar |
| U54 | 100442-2026 | teilmenge | – | 209315-2019 | 83582-2019, 209315-2019 | 209315-2019 | 2023-04-28 | grundlaufzeit | nein |
| U55 | 153719-2026 | kein_vorgaenger | – | – | – | – | unbekannt | unbekannt | unklar |
| U56 | 93751-2026 | teilmenge | – | 79802-2023 (Lose 3+4) | 505956-2022, 79802-2023; ferner 148457-2020, 299773-2020 (alle Lose) | 79802-2023 | 2025-07-31 (Höchstende 2026-07-31) | grundlaufzeit | nein |

## Übersicht

**Fakten (Zählung der Urteile oben):**

| Kategorie | Anzahl | Fälle |
|---|---|---|
| objektgleich_hoch | 0 | – |
| objektgleich_mittel | 4 | U43, U44, U51, U53 |
| teilmenge | 4 | U47, U48, U54, U56 |
| unklar | 4 | U45 (keine), U49 (keine), U50 (eher dafür), U52 (eher dafür) |
| kein_vorgaenger | 2 | U46, U55 |

- Objektgleich oder teilmenge: 8 von 14; nur objektgleich: 4 von 14.
- Fälle mit Abbruch durch Budget: keine. Höchster Verbrauch: U46 mit 4 API-Abfragen, U53 mit 5 XML und U56 mit 6 XML. Zusammen 14 API-Abfragen und 38 XML (ohne die 14 Testfall-XML).
- Herkunft des Vorgänger-Endes: grundlaufzeit bei 8 Fällen (U43, U44, U45-Kandidat, U47, U50-Kandidat, U51, U54, U56), hoechstende bei 1 (U48, abgeleitet), unbekannt bei 5.
  Unter den 8 Fällen mit objektgleich/teilmenge ist das Ende der Grundlaufzeit bei 6 ausdrücklich angegeben (U43, U44, U47, U51, U54, U56); bei U48 nur abgeleitet, bei U53 unbekannt.
- Vorzeitige Neuvergabe: in keinem Fall mit objektgleichem Vorgänger oder Teilmenge belegt.

## Grenzfälle der Regeln

- **U47 (teilmenge statt objektgleich):** 12 von 14 Adressen gemeinsam (86 %), auf beiden Seiten je zwei bis drei andere Adressen (Standortwechsel in Meschede und Soest). Die Regeln sagen „nahezu deckungsgleich“, ohne Schwelle. Nach der Rangfolge wurde das vorsichtigere Urteil teilmenge vergeben; die Lesart objektgleich_mittel wäre ebenfalls vertretbar.
- **U50 (Personalgestellung):** Überlassung von Vertretungskräften für die Unterhaltsreinigung ohne Objekt. Die Urteilsregeln setzen ein Objekt voraus; die Objektart ist nicht erkennbar, daher unklar (eher dafür), ohne die Regeln neu auszulegen.
- **U51 (hoch oder mittel):** Die Objektliste (Bauwerkskürzel und Straßen) ist nahezu deckungsgleich (54 von 55). Ob Gebäudenamen und Adressen derselben Liste als zwei A-Merkmale zählen, regeln die Urteilsregeln nicht; gezählt wurde ein Merkmal, daher mittel.
- **U43 und U44 (gleiche und abweichende Fläche zugleich):** Bei U43 ist die Grundfläche gleich, die Jahresreinigungsfläche weicht um 3,0 % ab; bei U44 ist die Jahresfläche von Los 1 gleich, die von Los 2 weicht um 7 % ab. Angewendet wurde „abweichend schließt hoch aus“, daher mittel.
- **U44 und U48 (Leistungsumfang):** 2026 kommt „Sonderreinigung“ hinzu (U44), bzw. 2020 waren Grund- und Glasreinigung im selben Los enthalten, 2026 nur Unterhaltsreinigung (U48). Gewertet als gleiche Leistungsart (Hauptleistung Unterhaltsreinigung auf beiden Seiten), nicht als „andere Leistungsart“.
- **U53 (Objektraum nur aus Losbezeichnungen):** Der Testfall nennt nur „Amtsgebäude und Schulen“ bzw. „Schulen im Landkreis Freising“. Nach den Regeln reicht übereinstimmender Objektraum bei fehlender Liste auf einer Seite für „mittel“. Testlos 2 könnte aber auch eine andere Schulgruppe des Landkreises meinen; das Urteil trägt wenig.
- **U56 (mehrere Teil-Vorgänger):** Der Landkreis hat seine Lose zwischen 2020 und 2023 in mehreren Verfahren neu vergeben. Als jüngster Vorgänger mit „teilmenge“ ist 505956-2022/79802-2023 (Lose 3+4) genannt. Die jüngere Ausschreibung 584542-2023 erreicht nur „unklar“, weil zwei ihrer drei Objektgruppen im Testfall nur als Glasreinigung vorkommen. Die Regeln legen nicht fest, welcher von mehreren Teil-Vorgängern zu nennen ist.
- **U48 (Objekt ohne Adresse):** „Büros in der Innenstadt“ (2020) ohne Adresse zählt nach den Regeln nicht als belegtes Objekt; mit ihm wäre die Überschneidung 2 von 3 statt 2 von 2 (Urteil unverändert).

## Auffälligkeiten

**Fakten**
- Zentrale Vergabestellen und Namenswechsel: U43 (Bayerisches Landesamt für Steuern, Zentrale Vergabestelle, für ein ADBV), U56 (Zentrale Vergabestelle der Kooperation Landkreis Lüneburg–Harburg; Vorgänger unter „Landkreis Lüneburg“), U44 (Vorgänger unter „Berufsbildende Schulen Ammerland“, Testfall unter „Landkreis Ammerland“), U55 (Autobahn GmbH seit 2021; kein Vorgänger der früheren Landesbehörde gefunden).
- Ausschreibungen ohne Zuschlag auf TED (CPV 909): 492553-2023 (U49), 244484-2023 (U52), 466300-2024 sowie die Lose 11 und 13 in 466323-2024 („clos-nw“) (U53), 646195-2021 und 584542-2023 (U56).
- U43: Dasselbe Objekt wurde 2022 (279881-2022/415309-2022, Zuschlag 2022-07-26) und erneut 2023 (207575-2023/343780-2023) vergeben.
- U54: Der gefundene Vertrag endete 2023-04-28, der Testfall beginnt 2026-05-02; dazwischen ist auf TED (CPV 909) kein Verfahren des Auftraggebers zu finden.
- U45: Gesamtfläche der Unterhaltsreinigung fast gleich (−1,0 %), Gebäudezahl 53 gegenüber 29 (keine Objektlisten).
- Funde außerhalb des Protokolls (anderer CPV): keine.
- Technisch: Die Abfrage U46 q01 mit FT~"BG Verkehr" (verknüpft mit Straßennamen) lieferte 0 Treffer, obwohl „BG Verkehr“ im Titel des Testfalls steht. Ob Volltextphrasen mit Abkürzungen zuverlässig suchen, ist offen.

**Einschätzungen**
- Bei Landkreisen und Städten mit vielen Losen (U45, U49, U52, U56) wechseln Losschnitt und Verfahrensbündel häufig; der jüngste Vorgänger deckt dann nur einen Teil der Lose ab. Eine Zuordnung auf Los-Ebene wäre hier aussagekräftiger als auf Ebene der Bekanntmachung.
- Mehrere Auftraggeber veröffentlichen keine Zuschlagsbekanntmachung oder heben Verfahren auf; das Vorgänger-Ende ist dann nur als geplantes Ende aus der Ausschreibung bekannt.
- Bei U54 und U52 liegt vermutlich ein nicht auf TED bekannt gemachter Zwischenvertrag vor (Unterschwellen- oder nationale Vergabe).
