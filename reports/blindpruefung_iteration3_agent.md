# Blindprüfung Iteration 3: regelbasierte Prüfung durch einen Subagenten

Regelbasierte Prüfung durch einen Subagenten nach urteilsregeln_blindpruefung.md (Version 1), 2026-10-24. Ersetzt nicht die Prüfung durch den Nutzer.

**Quellen:** Je Paar nur die beiden Original-XML von `https://ted.europa.eu/en/notice/<nummer>/xml`, am 2026-10-24 geladen
und unverändert gespeichert unter `data/raw/blindpruefung_agent_20261024/<nummer>.xml` (40 Dateien, alle HTTP 200).
Gelesene Felder: eForms `ProcurementProject` (Wurzel und je Los): `cbc:Name`, `cbc:Description`, `cac:RealizedLocation`
(Beschreibung und Adresse), CPV, Organisationen; alte TED-Formulare (F02/F03/F06): `TITLE`, `SHORT_DESCR`,
`OBJECT_DESCR` (TITLE, LOT_NO, MAIN_SITE, SHORT_DESCR, NUTS, CPV), `ADDRESS_CONTRACTING_BODY`, `COMPLEMENTARY_INFO/INFO_ADD`.
Weitere Reports, Lösungsschlüssel oder Projektdaten wurden nicht geöffnet.

**Vorgehen:** Zeitabstand, Vertragsende, Laufzeiten und Verlängerungsoptionen sind nicht eingeflossen, auch wo sie im Text
stehen. „Alt“ ist der mögliche Vorgänger, „Neu“ die Ausschreibung von 2026. Werte in den Details sind wörtlich oder
sinngemäß aus den genannten Feldern übernommen (Fakten). Urteil und Begründung sind die Anwendung der Regeln
(Interpretation). Wo ein Fall knapp war, steht das unter „Grenzfall“.

---

## P1

```
Paar: P1
Alt:  https://ted.europa.eu/de/notice/-/detail/202519-2022       Neu: https://ted.europa.eu/de/notice/-/detail/530979-2026
A (Identität):  nicht vergleichbar  Details: Alt SHORT_DESCR: „32 Liegenschaften z.T. mit mehreren Gebäuden mit ca. 22 Tsd. m2
                Fenster- und Innenglas-Flächen (vergl. Flächenverzeichnis)“. Neu: keine Liegenschaftszahl, keine Fläche,
                Flächenverzeichnis nur als Anlage („Flaechenverzeichnis.xlsx“ in Note). Adresse Neu nur „Wuppertal 42285“.
B (Objektraum): übereinstimmend     Details: Gebiet Alt MAIN_SITE „Wuppertal- Uellendahl“ / Neu Name „… in Wuppertal Uellendahl“;
                Objektarten Alt „Schulen, Tagesstätten für Kinder (TfK), Sporthallen und Verwaltungen“ / Neu „Verwaltungen,
                Schulen, Kindestagesstäten sowie Sportstätten“; Leistung Alt „Fenster- und Glasreinigung … Fenster- und
                Innenglas-Flächen“ / Neu „Fenster- und Innenglasreinigung“.
C (Stütze):     Auftraggeber ja (Gebäudemanagement der Stadt Wuppertal / Stadt Wuppertal), CPV ja (90911300 / 90911300),
                Titel ähnlich
Urteil: objektgleich   Sicherheit: mittel
Begründung: Beide: Wuppertal-Uellendahl, Schulen/Kitas/Sporthallen/Verwaltungen, Fenster- und Innenglasreinigung, CPV 90911300;
            Umfang nur Alt genannt (SHORT_DESCR: 32 Liegenschaften, ca. 22 Tsd. m²), Neu nur per Anlage → A nicht vergleichbar.
```

## P2

```
Paar: P2
Alt:  https://ted.europa.eu/de/notice/-/detail/509902-2022       Neu: https://ted.europa.eu/de/notice/-/detail/574953-2026
A (Identität):  übereinstimmend  Details: Adresse Alt MAIN_SITE „Spichernstraße 2, 10777 Berlin“ / Neu RealizedLocation
                „BGW, Bezirksverwaltung Berlin Spichernstraße 2 10777 Berlin“; Fläche beide „Nettogrundfläche von ca. 4.459,84 m²
                (HNF = ca. 2.456,32 m², NNF = ca. 972,18 m² und VF = ca. 1.031,34 m²)“; Gebäude beide „Objekt der BGW
                Bezirksverwaltung Berlin … Erdgeschoss – 3. Obergeschoss“.
B (Objektraum): übereinstimmend  Details: Berlin, Bürofläche der BGW-Bezirksverwaltung; Leistung beide „Unterhalts-, Grund- und
                einseitige Glasreinigung“ (Beschreibung wortgleich).
C (Stütze):     Auftraggeber ja (BGW), CPV teils (Alt 90919200; Neu 90911200, 90911300, 90919000), Titel ähnlich
Urteil: objektgleich   Sicherheit: hoch
Begründung: Adresse Spichernstraße 2, 10777 Berlin und Nettogrundfläche ca. 4.459,84 m² stimmen in Alt SHORT_DESCR/MAIN_SITE und
            Neu Description/RealizedLocation überein, Leistung beide Unterhalts-, Grund- und Glasreinigung → 3 A-Merkmale.
```

## P3

```
Paar: P3
Alt:  https://ted.europa.eu/de/notice/-/detail/306431-2026       Neu: https://ted.europa.eu/de/notice/-/detail/656958-2026
A (Identität):  widersprüchlich  Details: Gebäude Alt „Polizeiinspektion Harburg“ / Neu „Polizeiinspektion Stade“; Fläche Alt
                „Unterhaltsreinigung: ca. 8.785 m2, Glasreinigung: ca. 2.057 m2“ / Neu „ca. 9.006 m2 … ca. 1.925 m2“;
                Adresse Alt „Harburg-Buchholz 21244“ / Neu „Stade 21680“.
B (Objektraum): widersprüchlich  Details: Gebiet Alt „Maschen, Seevetal, Winsen/Luhe, Nenndorf, Neu Wulmsdorf, Salzhausen und
                Tostedt“ (NUTS DE933) / Neu „Buxtehude, Fredenbeck, Horneburg, Jork, Drochtersen, Himmelpforten, Steinkirchen,
                Harsefeld“ (NUTS DE939); Objektart (Polizei) und Leistung (Unterhalt + Glas, 2 Lose) gleich.
C (Stütze):     Auftraggeber ja (Staatliches Baumanagement Braunschweig), CPV ja (90911200, 90911300), Titel ähnlich
                (IGM 26E1010 / IGM 26E1011)
Urteil: nicht objektgleich   Sicherheit: –
Begründung: Alt Name „Polizeiinspektion Harburg“ mit Liegenschaften in Seevetal, Winsen/Luhe u. a., Neu Name „Polizeiinspektion
            Stade“ mit Liegenschaften in Buxtehude, Jork u. a. → anderes Gebiet und andere Gebäude.
```

## P4

```
Paar: P4
Alt:  https://ted.europa.eu/de/notice/-/detail/569523-2019       Neu: https://ted.europa.eu/de/notice/-/detail/599457-2026
A (Identität):  teils  Details: Alt SHORT_DESCR nennt 7 Objekte „Meeresmuseum, Stralsund, Ozeaneum, Stralsund, Nautineum,
                Stralsund, Natureum, Prerow (Darß), Burmeisterhaus, Stralsund, Neue Badenstraße 4, Stralsund,
                Sammlungsräume Türmchenspeicher, Stralsund“. Neu RealizedLocation nur „OZEANEUM, Hafenstraße 11, Stralsund 18439“
                (Wurzel und Los 1); andere Objekte im XML nicht genannt.
B (Objektraum): teils  Details: Objektart Museum, Gebiet Stralsund (Alt zusätzlich Prerow); Leistung Alt „Unterhaltsreinigung,
                Sanitärreinigung, Glasreinigung, Entstaubungsarbeiten, Freiflächenreinigung, Winterdienst, Dachrinnenreinigung,
                Schmutzmattenservice, Lieferung von Verbrauchsmaterial, Stundenlohnarbeiten“ / Neu „Unterhaltsreinigung,
                Sanitärreinigung, Stundenlohnarbeiten, Materiallieferung“.
C (Stütze):     Auftraggeber ja (Deutsches Meeresmuseum), CPV ja (90911200), Titel ähnlich („Reinigungs- und Serviceleistungen“)
Urteil: teilmenge   Sicherheit: –
Begründung: Alt SHORT_DESCR umfasst 7 Objekte mit u. a. Glasreinigung und Winterdienst, Neu RealizedLocation nur „OZEANEUM,
            Hafenstraße 11“ mit Unterhalts- und Sanitärreinigung → Schnittmenge Ozeaneum/Unterhaltsreinigung belegt, Neu ist kleiner.
Grenzfall: Ob Neu wirklich nur das Ozeaneum umfasst, ergibt sich nur aus dem einzigen Erfüllungsort; das Leistungsverzeichnis ist
           nicht einsehbar.
```

## P5

```
Paar: P5
Alt:  https://ted.europa.eu/de/notice/-/detail/327439-2022       Neu: https://ted.europa.eu/de/notice/-/detail/457874-2026
A (Identität):  teils übereinstimmend (1 Merkmal)  Details: Adresse Alt MAIN_SITE „Hochschule Düsseldorf Münsterstr. 156 40476
                Düsseldorf“ / Neu RealizedLocation „Münsterstr. 156 Düsseldorf 40476“. Keine Fläche, keine Gebäudezahl; Neu
                „aller Gebäude der Hochschule Düsseldorf“, Details nur in „Anlage 01_Leistungsbeschreibung Glasreinigung“.
B (Objektraum): übereinstimmend  Details: Objektart Hochschule (Hochschule Düsseldorf), Gebiet Düsseldorf (NUTS DEA11); Leistung
                Alt „Innen- und Aussenglasreinigung“ / Neu „Komplettreinigung sämtlicher Glasflächen innen und außen inkl. der
                Rahmen- und Einfassungen“.
C (Stütze):     Auftraggeber ja (Hochschule Düsseldorf), CPV ja (90911300), Titel ähnlich
Urteil: objektgleich   Sicherheit: mittel
Begründung: Beide Hochschule Düsseldorf, Münsterstr. 156, Innen- und Außenglasreinigung als Rahmenvereinbarung, CPV 90911300;
            nur ein A-Merkmal (Adresse) vergleichbar, Umfang steht in keiner der beiden Bekanntmachungen → mittel.
```

## P6

```
Paar: P6
Alt:  https://ted.europa.eu/de/notice/-/detail/436672-2026       Neu: https://ted.europa.eu/de/notice/-/detail/595492-2026
A (Identität):  widersprüchlich (Fläche)  Details: Fläche Alt Los 1/2 „ca. 36.191,26 m² lfd. Unterhalts-, Grund-, und
                Vertretungsreinigung“, Los 3 „ca. 20.794,66 m² Glasreinigungsarbeiten“ / Neu „ca. 34.568,35 m² …“ und
                „Ca. 17.834,89 m² Glasreinigungsarbeiten“. Liegenschaftsliste nur Neu (27 Einträge, u. a. Behördenzentrum
                Beblingerstr. 1-3, Neues Rathaus Rathausplatz 2, Mörike Gymnasium Neckarstr. 38); Alt ohne Liste. Lose Alt 3 / Neu 4.
B (Objektraum): übereinstimmend  Details: Gebiet Esslingen am Neckar; Objektart beide „div. kommunalen Gebäuden der Stadt Esslingen
                am Neckar“ (RealizedLocation beide „Kommunale Gebäude der Stadt Esslingen am Neckar“); Leistung Unterhalts-,
                Vertretungs-, Grund- und Glasreinigung.
C (Stütze):     Auftraggeber ja (Stadt Esslingen, Städtische Gebäude), CPV ja (90911200, 90911300), Titel gleich
                („Reinigung an diversen kommunalen Gebäuden der Stadt Esslingen am Neckar“)
Urteil: teilmenge   Sicherheit: –
Begründung: Gleicher Bestand „div. kommunale Gebäude der Stadt Esslingen“ mit gleichen Leistungen, aber Neu Description nennt
            34.568,35 m² Unterhalt und 17.834,89 m² Glas gegenüber Alt 36.191,26 m² und 20.794,66 m² → Neu erkennbar kleiner.
Grenzfall: Die Schnittmenge ist nur über den gleichen Bestand belegt, nicht über einzelne Gebäude (Alt nennt keine).
           Wer die Flächendifferenz als klaren Widerspruch in A wertet, käme zu „nicht objektgleich“.
```

## P7

```
Paar: P7
Alt:  https://ted.europa.eu/de/notice/-/detail/442059-2026       Neu: https://ted.europa.eu/de/notice/-/detail/644509-2026
A (Identität):  widersprüchlich  Details: Anzahl Alt „18 Schulen … (4 Lose) in 20 Schulgebäuden“ / Neu „12 Schulen … (3 Lose)“;
                Gebäudenamen Alt z. B. „Günter-Wöhe-Schulen“, „Ludwigsgymnasium“, „Gemeinschaftsschule Ludwigspark“,
                Völklinger Schulen / Neu z. B. „Schule Winterbachsroth“, „Gymnasium am Schloss“, „Deutsch-Französisches Gymnasium“,
                „Katharine-Weißgerber-Schule“. Flächen Alt 40.890,82 / 20.564,26 / 38.965,38 / 19.006,14 m² / Neu 25.811,01 /
                19.627,70 / 14.729,95 m². Einzige Namensnähe: Alt „Technisch-gewerbliches BBZ II“ / Neu „TGBBZ II Sporthalle Mügelsberg“.
B (Objektraum): widersprüchlich  Details: Gebiete Alt Saarbrücken, Altenkessel, Güdingen, Völklingen, Püttlingen, Riegelsberg,
                Heusweiler / Neu Saarbrücken, Dudweiler, Altenkessel, Güdingen, Klarenthal, Kleinblittersdorf, Halberg;
                Objektart (Schulen) und Leistung (Unterhalts- und Grundreinigung) gleich.
C (Stütze):     Auftraggeber ja (Regionalverband Saarbrücken), CPV ja (90911200), Titel ähnlich
Urteil: nicht objektgleich   Sicherheit: –
Begründung: Die Schulnamen in den Los-Beschreibungen unterscheiden sich fast vollständig (Alt z. B. Ludwigsgymnasium, Völklinger
            Schulen; Neu z. B. Gymnasium am Schloss, Deutsch-Französisches Gymnasium), Gebiete Völklingen/Püttlingen nur Alt →
            andere Gebäude.
Grenzfall: Eine Überschneidung bei „TGBBZ II“ (Alt Schule, Neu nur Sporthalle Mügelsberg) ist möglich, aber nicht belegt.
```

## P8

```
Paar: P8
Alt:  https://ted.europa.eu/de/notice/-/detail/390156-2023       Neu: https://ted.europa.eu/de/notice/-/detail/623928-2026
A (Identität):  nicht vergleichbar / abweichend  Details: Alt SHORT_DESCR „ca. 52.500 m² Reinigungsfläche und ca. 10.000 m²
                Glasfläche in mehreren Losen“ (5 Unterhalts-Lose 19.200/14.200/5.000/6.500/7.600 m², 2 Glas-Lose je 4.000 m²) /
                Neu Description „ca. 63.400 m² Reinigungsfläche in 3 Losen“ (Lose 31.200/28.300/3.900 m², in den Losen als
                „Glasfläche“ bezeichnet). Keine Gebäudenamen oder Adressen in beiden.
B (Objektraum): teils  Details: Gebiet beide Stadt Springe und Ortsteile (NUTS DE929); Objektart beide nur „diverse Objekte“ /
                „verschiedene Objekte“; Leistung Alt Unterhalts-, Grund- und Glas-/Rahmenreinigung (Lose A, B) / Neu „Unterhalts-
                und Grundreinigung“ ohne Glas-Los (kein CPV 90911300).
C (Stütze):     Auftraggeber ja (Stadt Springe; Neu über Kommunal Agentur NRW), CPV teils (Alt 90911000 + 90911300 u. a. / Neu
                90911200, 90919200, 90919300, 90910000), Titel ähnlich
Urteil: unklar   Sicherheit: –
Begründung: Objektart ist in beiden nur „diverse Objekte“ in Springe (OBJECT_DESCR TITLE / Description), Objekte stehen nur in
            Anlagen, und Umfang (52.500 gegenüber 63.400 m²) sowie Leistung (Glas-Lose nur Alt) weichen in verschiedene
            Richtungen ab → weder Übereinstimmung noch Teilmenge belegbar.
```

## P9

```
Paar: P9
Alt:  https://ted.europa.eu/de/notice/-/detail/216353-2021       Neu: https://ted.europa.eu/de/notice/-/detail/569458-2026
A (Identität):  nicht vergleichbar  Details: Alt „10 Objekte … mit insgesamt ca. 7 800 m 2 Grundfläche“ (Los 1: 4 Objekte ca.
                2 000 m², Los 2: 6 Objekte „ca. 58 000 m 2“), Glas-Los ca. 12 Objekte, 3 800 m² / Neu Los 1 „ca. 1.200.000 m²
                Jahresreinigungsfläche Unterhaltsreinigung, ca. 8.700 m² Grundreinigungsfläche pro Jahr“. Andere Flächenart,
                keine Objektzahl, keine Namen.
B (Objektraum): teils  Details: Gebiet Gemeinde Dußlingen (NUTS DE142); Objektarten Alt „Schule, Sportstätte, Verwaltungsgebäude,
                Veranstaltungsgebäude, Betriebsgebäude, Kindergärten, Kinderkrippe“ / Neu nur „ihre Liegenschaften“; Leistung Alt
                Unterhaltsreinigung (2 Lose) + Glasreinigung (1 Los) / Neu „Los 1 Unterhalts- und Grundreinigung“, kein Glas.
C (Stütze):     Auftraggeber ja (Gemeinde Dußlingen), CPV teils (Alt 90910000 u. a. / Neu 90911200), Titel ähnlich
Urteil: unklar   Sicherheit: –
Begründung: Neu Description nennt nur „Gebäudereinigungsleistungen für ihre Liegenschaften“ ohne Objektarten oder Objektzahl, die
            Fläche ist eine Jahresreinigungsfläche statt Grundfläche → Stufe B nicht vollständig erkennbar.
```

## P10

```
Paar: P10
Alt:  https://ted.europa.eu/de/notice/-/detail/683345-2024       Neu: https://ted.europa.eu/de/notice/-/detail/496932-2026
A (Identität):  übereinstimmend  Details: Gebäudename beide „Gesamtschule Höhscheid“; Adressen beide „Kanalstraße 20 und
                Zweigstraße 15-17, 42657 Solingen“; Anzahl beide „in 2 Gebäudetrakten untergebracht“. Fläche nur Neu
                („1.301.095,60 qm pro Jahr“).
B (Objektraum): übereinstimmend  Details: Stadtteil Solingen-Höhscheid, Objektart Schule, Leistung Unterhaltsreinigung.
C (Stütze):     Auftraggeber ja (Stadt Solingen), CPV ja (90919300), Titel gleich
Urteil: objektgleich   Sicherheit: hoch
Begründung: Name „Unterhaltsreinigung der Gesamtschule Höhscheid, Kanalstraße 20 und Zweigstraße 15-17, 42657 Solingen“ ist in
            beiden wortgleich, beide Description „2 Gebäudetrakte“ → Gebäudename, Adresse und Gebäudezahl stimmen überein.
```

## P11

```
Paar: P11
Alt:  https://ted.europa.eu/de/notice/-/detail/670866-2022       Neu: https://ted.europa.eu/de/notice/-/detail/598474-2026
A (Identität):  teils übereinstimmend  Details: Alt 4 Lose an zwei Adressen: „Ringstraße 52, 32427 Minden“ (Los 1 Unterhalt,
                Los 2 Glas) und „Universitätsstraße 68, 44789 Bochum“ (Los 3 Unterhalt, Los 4 Glas) / Neu nur „Standort
                Universitätsstraße 68, 44789 Bochum“ (Los 1 Unterhalt, Los 2 Glas- und Rahmenreinigung).
B (Objektraum): teils  Details: Gebiet Alt Minden (DEA46) und Bochum (DEA51) / Neu nur Bochum (DEA51); Objektart Geschäftsstelle
                der IKK classic; Leistung beide Unterhaltsreinigung und Glas- und Rahmenreinigung.
C (Stütze):     Auftraggeber ja (IKK classic, Alt Dresden / Neu Erfurt), CPV ja (90911200, 90911300), Titel ähnlich
                („Reinigung Westfalen-Lippe“ / „Reinigungsdienstleistungen Bochum“)
Urteil: teilmenge   Sicherheit: –
Begründung: Neu Description nennt nur „Universitätsstraße 68, 44789 Bochum“ mit Unterhalts- und Glasreinigung, das entspricht den
            Alt-Losen 3 und 4; die Minden-Lose 1 und 2 (Ringstraße 52) fehlen → Neu ist eine belegte Teilmenge.
```

## P12

```
Paar: P12
Alt:  https://ted.europa.eu/de/notice/-/detail/165984-2026       Neu: https://ted.europa.eu/de/notice/-/detail/478291-2026
A (Identität):  widersprüchlich  Details: Standort Alt „Finanzamt Mittelfranken-Ost, Schwabach“, Adresse „Schwabach 91126“ /
                Neu „Finanzamt Mittelfranken-Ost am Standort Erlangen“, „Erlangen 91052“; Grundfläche Alt „ca. 5.922,16 qm“ /
                Neu „ca. 6.900,06 qm“.
B (Objektraum): widersprüchlich  Details: Gebiet Alt Schwabach (NUTS DE255) / Neu Erlangen (DE252); Objektart Finanzamt und
                Leistung Unterhaltsreinigung gleich.
C (Stütze):     Auftraggeber ja (Bayerisches Landesamt für Steuern), CPV ja (90911200), Titel ähnlich
Urteil: nicht objektgleich   Sicherheit: –
Begründung: Name Alt „… FA Mittelfranken-Ost, Schwabach“ und Neu „… FA Mittelfranken-Ost, Standort Erlangen“ mit Grundflächen
            5.922,16 qm gegenüber 6.900,06 qm → anderer Standort desselben Finanzamts.
```

## P13

```
Paar: P13
Alt:  https://ted.europa.eu/de/notice/-/detail/563086-2025       Neu: https://ted.europa.eu/de/notice/-/detail/555833-2026
A (Identität):  teils  Details: Adressen überschneiden sich (beide u. a. Ammerländer Heerstr. 114-118, Johann-Justus-Weg 147/147a,
                Philosophenweg 39/41, Carl-von-Ossietzky-Str./Küpkersweg); Lose Alt Standort B und C (Unterhalt, 54.739 m² /
                57.050 m²) / Neu Standort A, B, C NORD, C SÜD (Glas, 15.341 / 8.577 / 3.646 / 13.532 m²).
B (Objektraum): widersprüchlich  Details: Objektart Universität Oldenburg (gleich), Gebiet Oldenburg (gleich); Leistung Alt
                „Unterhaltsreinigung“ / Neu „Glasreinigung“.
C (Stütze):     Auftraggeber ja (Staatliches Baumanagement Region Nord-West), CPV teils (Alt 90911200, 90910000 / Neu zusätzlich
                90911300), Titel ähnlich
Urteil: nicht objektgleich   Sicherheit: –
Begründung: Alt Name „IGM25E580001: Unterhaltsreinigung CvO Universität Oldenburg 2 Standorte“, Neu Name „IGM26E580015:
            Glasreinigung Carl von Ossietzky Universität Oldenburg 4 Lose“ → andere Leistungsart an teils denselben Gebäuden.
```

## P14

```
Paar: P14
Alt:  https://ted.europa.eu/de/notice/-/detail/488753-2023       Neu: https://ted.europa.eu/de/notice/-/detail/533895-2026
A (Identität):  nicht vergleichbar  Details: Alt nennt je Los Liegenschaften (Los 1 neun Grundschulen + Kulturwerkstatt, Los 2
                „Albert-Schweizer-Gymnasium“ + 9 Kitas, Los 3 Gesamtschule, Rathaus, Feuerwehr u. a., Los 4 Realschule,
                Ernst-Mach-Gymnasium u. a., Los 5 Glas „für alle städtische Liegenschaften“) / Neu keine Gebäudenamen, keine
                Flächen (RealizedLocation nur „städtische Liegenschaften“).
B (Objektraum): teils  Details: Gebiet Stadtgebiet Hürth (DEA27); Objektarten Alt „Verwaltungsgebäude, Feuerwachen, Schulen und
                Kindertagesstätten“ / Neu „Verwaltungsgebäude, Feuerwachen, Schulen und Kindertagesstätten sowie Unterkünfte für
                Geflüchtete“; Leistung beide Unterhalts-, Vertretungs-, Grund- und Glas-/Rahmenreinigung; Lose Alt 4 + 1 Glas /
                Neu 5 + 1 Glas.
C (Stütze):     Auftraggeber ja (Stadt Hürth), CPV ja (90910000, 90911200, 90919xxx), Titel ähnlich („Reinigungsleistungen
                2023-2027“ / „Reinigungsleistungen 2026 bis 2031 (Lose 1 bis 6)“)
Urteil: teilmenge   Sicherheit: –
Begründung: Neu Los-Description ergänzt gegenüber Alt SHORT_DESCR die Objektart „Unterkünfte für Geflüchtete“ und ein fünftes
            Unterhalts-Los, die Objektarten von Alt (Verwaltung, Feuerwachen, Schulen, Kitas in Hürth) sind darin enthalten
            → Neu beschreibt erkennbar mehr Objekte.
Grenzfall: Welche einzelnen Gebäude Neu umfasst, steht nur in den Vergabeunterlagen.
```

## P15

```
Paar: P15
Alt:  https://ted.europa.eu/de/notice/-/detail/467991-2026       Neu: https://ted.europa.eu/de/notice/-/detail/630789-2026
A (Identität):  teils übereinstimmend  Details: Gebäudename beide „Bildungshaus Winkelwiese“; Adresse Alt „Haußerstraße 128-132“ /
                Neu „Haußerstraße 132“, 72076 Tübingen; Fläche nur Alt („ca. 4.200 m2 Schule, KITA und Sporthalle“).
B (Objektraum): widersprüchlich  Details: Leistung Alt „Baureinigung Fertigstellung Neubau“ / Neu „Unterhalts und Grundreinigung
                ohne Glasreinigung“; Objektart (Schule, Kita, Sporthalle) und Gebiet Tübingen gleich.
C (Stütze):     Auftraggeber ja (Universitätsstadt Tübingen), CPV teils (beide 90911200, 90910000; Neu zusätzlich 90900000,
                90911000), Titel ähnlich
Urteil: nicht objektgleich   Sicherheit: –
Begründung: Alt Name „Baureinigung I Bildungshaus Winkelwiese“, Neu Name „Grund- und Unterhaltsreinigung Bildungshaus
            Winkelwiese“ → gleiches Gebäude, aber andere Leistungsart (Baureinigung gegenüber Unterhaltsreinigung).
```

## P16

```
Paar: P16
Alt:  https://ted.europa.eu/de/notice/-/detail/582425-2019       Neu: https://ted.europa.eu/de/notice/-/detail/565728-2026
A (Identität):  widersprüchlich / nicht belegt  Details: Alt 6 Lose: „Liegenschaften Spandau, Machandelweg inkl. Kantine“,
                „Liegenschaften Cicerostraße, Kundenzentrum Steglitz“, „Liegenschaften Usedomer Str. (Bestands-/Neubau),
                Niederschönhausen“, „Liegenschaften Marzahn“, „Liegenschaften Gleichrichterwerke“, „Liegenschaften Fundbüro
                Rudolfstraße“ / Neu „Los 29 - Kundenzentrum Köpenick“, „Los 30 - Kundenzentrum Marzahn“. Keine Adressen der
                Kundenzentren, keine Flächen.
B (Objektraum): widersprüchlich  Details: Gebiet: Köpenick in keinem Alt-Los; Marzahn in beiden, aber Alt ohne Hinweis auf ein
                Kundenzentrum (Kundenzentrum nur bei Steglitz genannt); Leistung Alt Unterhalts- und Glasreinigung („Weiterhin wird
                die Glasreinigung … mit ausgeschrieben“) / Neu nur „Unterhaltsreinigung“.
C (Stütze):     Auftraggeber ja (Berliner Verkehrsbetriebe, Einkauf/Materialwirtschaft), CPV teils (Alt 90910000, 90911300 /
                Neu 90911000), Titel anders
Urteil: nicht objektgleich   Sicherheit: –
Begründung: Neu Los-Namen „Kundenzentrum Köpenick“ und „Kundenzentrum Marzahn“ finden sich in keinem Alt-Los-TITLE (dort
            Spandau, Steglitz, Niederschönhausen, Marzahn, Gleichrichterwerke, Fundbüro), Köpenick fehlt ganz → anderer Zuschnitt.
Grenzfall: Dass das Kundenzentrum Marzahn in Alt-Los 4 „Liegenschaften Marzahn“ enthalten war, ist möglich, aber nicht belegt; mit
           Beleg wäre es eine Teilmenge.
```

## P17

```
Paar: P17
Alt:  https://ted.europa.eu/de/notice/-/detail/574481-2023       Neu: https://ted.europa.eu/de/notice/-/detail/506593-2026
A (Identität):  nicht vergleichbar  Details: Neu „Das Gebiet-Los 3 beinhaltet neun Gebäude auf dem Wissenschaftscampus
                Berlin-Adlerhof“ (ohne Namen/Adressen); Alt 5 Lose „Los 1 - WISTA Nord“, „Los 2 - WISTA Süd 1“, „Los 3 - WISTA
                Süd 2“, „Los 4 - WISTA Süd 3“, „Los 5 - WISTA - CHIC“, je „verschiedene Gebäude“ ohne Zahl.
B (Objektraum): teils  Details: Gebiet beide Technologiepark/Wissenschaftscampus Berlin-Adlershof; Objektart Gebäude der WISTA
                (Allgemeinflächen, teils Büros); Leistung beide Unterhaltsreinigung. Neu nur ein Gebiets-Los, Alt fünf Lose.
C (Stütze):     Auftraggeber ja (WISTA.Service GmbH), CPV ja (90911200, 90919200), Titel ähnlich
Urteil: teilmenge   Sicherheit: –
Begründung: Alt SHORT_DESCR vergibt die Unterhaltsreinigung für den „Standort Technologiepark Adlerhof“ in fünf Losen, Neu Name
            „Unterhaltsreinigung Bereich Los 3“ betrifft nur ein Gebiets-Los mit neun Gebäuden desselben Campus → einzelnes Los.
Grenzfall: Ob „Gebiet-Los 3“ (Neu) dem Alt-Los „Los 3 - WISTA Süd 2“ entspricht, ist nicht belegt; belegt ist nur, dass Neu auf dem
           von Alt insgesamt abgedeckten Campus liegt.
```

## P18

```
Paar: P18
Alt:  https://ted.europa.eu/de/notice/-/detail/465718-2022       Neu: https://ted.europa.eu/de/notice/-/detail/514223-2026
A (Identität):  abweichend  Details: Anzahl Alt „45 Objekten“ / Neu „53 Objekten“; Jahresreinigungsfläche Alt „ca. 3,2 Mio.
                Quadratmetern“ / Neu „rund 3.600.000 Quadratmetern“; Grundreinigungsfläche Alt „ca. 7.000“ / Neu „11.200
                Quadratmetern“. Keine Gebäudenamen in Neu; Alt INFO_ADD nennt als Besichtigungsobjekte „Grundschulen Martin
                Luther, Am Regenstein, Derenburg und Timmenrode sowie im Sportforum“.
B (Objektraum): teils  Details: Gebiet beide Stadt Blankenburg (Harz) mit Ortsteilen (NUTS DEE09); Objektart Neu „städtischer
                Objekte und Einrichtungen“, Alt ohne Objektart in SHORT_DESCR; Leistung Alt „Unterhalts- und Grundreinigung“ / Neu
                zusätzlich „Glas- und Rahmenreinigung mit rund 3.400 Quadratmetern“.
C (Stütze):     Auftraggeber ja (Stadt Blankenburg (Harz)), CPV teils (Alt 90911200 / Neu 90911200, 90911300), Titel anders
                („OV-BlankenburgHarz-22“ / „Durchführung der Unterhalts- und Grundreinigung sowie Glas- und Rahmenreinigung …“)
Urteil: teilmenge   Sicherheit: –
Begründung: Alt SHORT_DESCR „Unterhalts- und Grundreinigung von 45 Objekten“, Neu Description „Unterhalts- und Grundreinigung von
            53 Objekten“ plus Glasreinigung, beide für den Objektbestand der Stadt Blankenburg (Harz) → Neu erkennbar größer.
Grenzfall: Die Schnittmenge ist nur über Auftraggeber, Gebiet und Leistung belegt, nicht über einzelne Gebäude; bei strengerer
           Lesart von „belegbar“ wäre das Urteil „unklar“.
```

## P19

```
Paar: P19
Alt:  https://ted.europa.eu/de/notice/-/detail/410442-2026       Neu: https://ted.europa.eu/de/notice/-/detail/500007-2026
A (Identität):  widersprüchlich  Details: Liegenschaftsgruppe Alt Name „Objektgruppe 2: Unterhaltsreinigung und Einpflege“ und
                „Die Unterhaltsreinigung der Gebäude der Objektgruppe 2 erfolgt dauerhaft“ / Neu Name „Objektgruppe 3: …“ und
                „… der Gebäude der Objektgruppe 3 erfolgt dauerhaft“. Keine Adressen, Gebäudenamen oder Flächen.
                (Neu Wurzel-Description beginnt mit „Objektgruppe 2: Los 1 und 2 …“, offenbar aus der Vorlage übernommen.)
B (Objektraum): übereinstimmend  Details: Gebiet „Stadtgebiet Bocholt“; Objektart Schulgebäude/Turnhallen + Verwaltungsgebäude;
                Leistung Unterhaltsreinigung inkl. Einpflege; Losstruktur gleich (Los 1, Los 2 Schulen, Los 3 Verwaltung).
C (Stütze):     Auftraggeber ja (Stadt Bocholt), CPV ja (90911200, 90919000; Lose 90919300/90919200), Titel ähnlich
Urteil: nicht objektgleich   Sicherheit: –
Begründung: Name und Los-Text bezeichnen in Alt die „Gebäude der Objektgruppe 2“, in Neu die „Gebäude der Objektgruppe 3“ → andere
            Liegenschaftsgruppe desselben Auftraggebers bei gleicher Objektart und Leistung.
Grenzfall: Der Widerspruch beruht auf der Gruppennummer; die Wurzel-Description von Neu nennt widersprüchlich „Objektgruppe 2“.
           Name und viermalige Nennung „Objektgruppe 3“ wurden höher gewichtet.
```

## P20

```
Paar: P20
Alt:  https://ted.europa.eu/de/notice/-/detail/155215-2021       Neu: https://ted.europa.eu/de/notice/-/detail/503493-2026
A (Identität):  teils übereinstimmend  Details: Los 2 Glas beide dieselben 4 Liegenschaften (Hasselweg 20, Elsässer Str. 15,
                Lilienthalstr. 3, Lilienthalstr. 1, Kassel) und „1.271,16 m²“ / „3.813,48 m²“; Los 3 beide „Bundespolizeiinspektion
                Kassel, Heerstr. 5, 34119 Kassel“ und „3.097,75 m²“ Fußbodenfläche, „653,99 m²“ Glas. Los 1 Unterhalt Alt 4
                Liegenschaften, „6 267,07 m 2“ / Neu nur „FKS Zollamt Gießen, Lilienthalstr. 3“ und „Zollamt Kassel,
                Lilienthalstr. 1“, „ca. 2.424,06 m²“.
B (Objektraum): teils  Details: Gebiet Kassel (DE731), Objektart Bundesliegenschaften (Zoll, BImA, Bundespolizei), Leistung
                Unterhalts- und Glasreinigung in gleicher Losstruktur; Unterhaltsreinigung Hasselweg 20 und Elsässer Str. 15 nur Alt.
C (Stütze):     Auftraggeber ja (Bundesanstalt für Immobilienaufgaben), CPV ja (90911200, 90911300), Titel fast gleich
                („VOEK 154-20“ / „VOEK 077-26“)
Urteil: teilmenge   Sicherheit: –
Begründung: Lose 2 und 3 sind nach Adresse und m² identisch, aber Neu Los 1 umfasst nur Lilienthalstr. 1 und 3 mit 2.424,06 m²
            statt Alt MAIN_SITE 4 Liegenschaften mit 6.267,07 m² → Neu ist erkennbar kleiner, Schnittmenge per Adresse belegt.
```

---

## Auszählung (Schritt 4)

**Anzahl je Urteil**

| Urteil | Anzahl | Paare |
|---|---|---|
| objektgleich, hoch | 2 | P2, P10 |
| objektgleich, mittel | 2 | P1, P5 |
| teilmenge | 7 | P4, P6, P11, P14, P17, P18, P20 |
| nicht objektgleich | 7 | P3, P7, P12, P13, P15, P16, P19 |
| unklar | 2 | P8, P9 |
| **Summe** | **20** | |

**Liste P-Nr → Urteil**

| Paar | Neu | Alt | Urteil |
|---|---|---|---|
| P1 | 530979-2026 | 202519-2022 | objektgleich (mittel) |
| P2 | 574953-2026 | 509902-2022 | objektgleich (hoch) |
| P3 | 656958-2026 | 306431-2026 | nicht objektgleich |
| P4 | 599457-2026 | 569523-2019 | teilmenge |
| P5 | 457874-2026 | 327439-2022 | objektgleich (mittel) |
| P6 | 595492-2026 | 436672-2026 | teilmenge |
| P7 | 644509-2026 | 442059-2026 | nicht objektgleich |
| P8 | 623928-2026 | 390156-2023 | unklar |
| P9 | 569458-2026 | 216353-2021 | unklar |
| P10 | 496932-2026 | 683345-2024 | objektgleich (hoch) |
| P11 | 598474-2026 | 670866-2022 | teilmenge |
| P12 | 478291-2026 | 165984-2026 | nicht objektgleich |
| P13 | 555833-2026 | 563086-2025 | nicht objektgleich |
| P14 | 533895-2026 | 488753-2023 | teilmenge |
| P15 | 630789-2026 | 467991-2026 | nicht objektgleich |
| P16 | 565728-2026 | 582425-2019 | nicht objektgleich |
| P17 | 506593-2026 | 574481-2023 | teilmenge |
| P18 | 514223-2026 | 465718-2022 | teilmenge |
| P19 | 500007-2026 | 410442-2026 | nicht objektgleich |
| P20 | 503493-2026 | 155215-2021 | teilmenge |

**Quote als Spanne (Rechnung nach der Tabelle in Schritt 4)**

| Variante | Treffer | Fehler | Ausgeschlossen | Quote |
|---|---|---|---|---|
| streng | 2 (objektgleich hoch) | 18 (alle anderen, auch unklar) | – | 2/20 = 10 % |
| breit | 11 (hoch 2 + mittel 2 + teilmenge 7) | 7 (nicht objektgleich) | 2 (unklar) | 11/18 ≈ 61 % |

Interpretation: Die beiden Werte liegen weit auseinander. Laut Regeln hängt die Aussage damit an den Zweifelsfällen, vor allem an den
7 Teilmengen. Davon unklar: 2 von 20.

## Grenzfälle und Hinweise

- **Grenzfälle mit Einfluss auf die Quote** (siehe jeweils „Grenzfall“): P6 und P18 (Teilmenge nur über den gleichen Objektbestand
  belegt, nicht über einzelne Gebäude), P17 (Zuordnung des Gebiets-Loses nicht belegt), P16 (mögliche Überschneidung Marzahn),
  P19 (Gruppennummer widersprüchlich innerhalb von Neu), P4 (Umfang von Neu nur über den einzigen Erfüllungsort).
- **Fakten aus den XML, die nicht ins Urteil eingeflossen sind:** Mehrere „Alt“-Bekanntmachungen sind keine
  Zuschlagsbekanntmachungen, sondern Auftragsbekanntmachungen (Formular F02 bei 202519-2022, 509902-2022, 390156-2023,
  216353-2021, 488753-2023, 465718-2022; eForms `cn-standard` bei 410442-2026). Für die Frage „dasselbe Objekt?“ spielt der Typ
  laut Regeln keine Rolle. Laufzeiten und Hinweise wie „Der laufende Vertrag … endet am 31.Dez.2023“ (574481-2023) wurden bewusst
  nicht verwendet.
- **Laden und Lesen:** Alle 40 XML ließen sich laden (HTTP 200, `application/xml`) und parsen. Keine fehlenden Felder, die ein
  Urteil verhindert hätten. Auffälligkeiten in den Texten: 623928-2026 bezeichnet die Los-Flächen als „Glasfläche“, obwohl die
  Wurzel von „Reinigungsfläche“ spricht; 216353-2021 nennt für Los 2 „ca. 58 000 m 2“ bei insgesamt 7 800 m² (vermutlich
  Tippfehler, nicht verwendet); 500007-2026 nennt in der Wurzel-Description „Objektgruppe 2“, sonst „Objektgruppe 3“.
