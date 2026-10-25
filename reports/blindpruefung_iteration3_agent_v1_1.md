Regelbasierte Prüfung durch einen Subagenten nach urteilsregeln_blindpruefung.md (Version 1.1), 2026-10-24, Paare P9–P28. Ersetzt nicht die Prüfung durch den Nutzer.

# Blindprüfung Iteration 3: Urteile nach Version 1.1 (Subagent)

## Vorgehen und Quellen (Fakten)

- Regeln: `reports/urteilsregeln_blindpruefung.md`, Version 1.1. Andere Reports, `docs/`, `src/`, `data/processed/` wurden nicht geöffnet.
- Quellen: je Paar nur die beiden Original-XML aus `data/raw/blindpruefung_agent_20261024/`. Die 24 XML für P9–P20 lagen schon vor. Die 16 XML für P21–P28 wurden am 2026-10-24 von `https://ted.europa.eu/en/notice/<nummer>/xml` geladen (alle HTTP 200, etwa 0,6 s Pause zwischen den Abrufen) und unverändert gespeichert. Überschrieben wurde nichts.
- Ausgelesen: alte TED-Schemata (F02/F03/F06): `OBJECT_CONTRACT/TITLE`, `SHORT_DESCR`, `OBJECT_DESCR` (`TITLE`, `LOT_NO`, `MAIN_SITE`, `SHORT_DESCR`, `CPV`, `NUTS`), `COMPLEMENTARY_INFO`, `AWARD_CONTRACT/TITLE`. eForms: `ProcurementProject` (`Name`, `Description`, `Note`) auf Verfahrens- und Losebene, `RealizedLocation/Address`, `RecurringProcurementDescription`, Organisationen.
- Nicht verwendet (Spielregel 3): Zeitabstand, Vertragsende, Laufzeit, Auftragswert. Das gilt auch für Hinweise im Text auf eine geplante Neuausschreibung (P14).
- Fakten sind die zitierten Feldwerte. Interpretation ist die Einstufung nach den Regeln (Urteil, Sicherheit, Tendenz).
- Keines der Paare P9–P28 gehört zu den acht Kalibrierungspaaren der Regeldatei. Alle 20 Paare werden gezählt.
- Link-Schema: `https://ted.europa.eu/de/notice/-/detail/<nummer>`.

## Urteile je Paar

### P9

- Paar: P9
- Alt: https://ted.europa.eu/de/notice/-/detail/216353-2021 (F02, Auftragsbekanntmachung)   Neu: https://ted.europa.eu/de/notice/-/detail/569458-2026
- A (Identität): mehrdeutig. Details: Neu nennt keine Objektliste, Los 1 hat „ca. 1.200.000 m² Jahresreinigungsfläche Unterhaltsreinigung, ca. 8.700 m² Grundreinigungsfläche pro Jahr“. Alt (SHORT_DESCR) nennt „10 Objekte (Schule, Sportstätte, Verwaltungsgebäude, Veranstaltungsgebäude, Betriebsgebäude, Kindergärten, Kinderkrippe) mit insgesamt ca. 7 800 m2 Grundfläche“. Los 1 hat 4 Objekte mit ca. 2 000 m², Los 2 hat 6 Objekte mit „ca. 58 000 m2“ Grundfläche, was im alten Text nicht zur Summe passt. Los 3 ist Glasreinigung mit 3 800 m². Jahresreinigungsfläche und Grundfläche sind verschiedene Flächenarten, daher ist keine eindeutige Lesart möglich.
- B (Objektraum): nicht erkennbar. Details: Neu sagt nur „Gebäudereinigungsleistungen für ihre Liegenschaften“ der Gemeinde, also eines Auftraggebers mit vielen Gebäudearten. Die Objektart ist neu deshalb nicht erkennbar. Gebiet: beide Dußlingen, NUTS DE142. Leistung: neu Unterhalts- und Grundreinigung, alt Unterhaltsreinigung (Lose 1–2) und Glasreinigung (Los 3).
- C (Stütze): Auftraggeber ja (Gemeinde Dußlingen), CPV teils (neu 90911200; alt Haupt-CPV 90910000, 90911200 in den Losen), Titel ähnlich, Losstruktur anders (1 gegenüber 3 Losen)
- Überschneidung der Objekte: keine Liste auf der neuen Seite
- Lose mit Überschneidung: neu Los 1 ↔ alt Lose 1 und 2 (Unterhaltsreinigung); alt Los 3 (Glas) hat kein Gegenstück

Urteil: unklar

Sicherheit: –

Tendenz: eher dafür

Begründung: Neu nennt nur „Liegenschaften der Gemeinde Dußlingen“, die Objektart ist also nicht erkennbar und das Urteil höchstens „unklar“. Für dasselbe Objekt sprechen der gleiche Auftraggeber, der gleiche NUTS DE142 und die Unterhaltsreinigung auf beiden Seiten, ohne dass eine Angabe widerspricht. Die Flächen sind mehrdeutig (Jahresreinigungsfläche gegenüber Grundfläche), und die Glasreinigung fehlt neu.

### P10

- Paar: P10
- Alt: https://ted.europa.eu/de/notice/-/detail/683345-2024 (Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/496932-2026
- A (Identität): übereinstimmend. Details: Beide nennen „Gesamtschule Höhscheid, Kanalstraße 20 und Zweigstraße 15-17, 42657 Solingen“ (Titel und Description) und „in 2 Gebäudetrakten untergebracht“. Eine Fläche steht nur neu (1.301.095,60 qm pro Jahr, Ferienreinigung Turnhallen 20.624,40 qm). Es ist ein Einzelstandort (eine Schule), die Adresse zählt also nicht. Übrig bleibt ein weiteres A-Merkmal (2 Gebäudetrakte).
- B (Objektraum): erkennbar und übereinstimmend. Details: Stadtteil Solingen-Höhscheid, Objektart Gesamtschule, Leistung Unterhaltsreinigung (neu zusätzlich Ferienreinigung der Turnhallen).
- C (Stütze): Auftraggeber ja (Stadt Solingen), CPV ja (90919300), Titel wortgleich, Losstruktur gleich (1 Los)
- Überschneidung der Objekte: 1 von 1 (Schule mit 2 Trakten)

Urteil: objektgleich

Sicherheit: mittel

Begründung: Beide nennen Gesamtschule Höhscheid, Kanalstraße 20 und Zweigstraße 15-17, „2 Gebäudetrakte“ und Unterhaltsreinigung. Bei diesem Einzelstandort zählt die Adresse nicht, und mit den Gebäudetrakten stimmt nur ein weiteres A-Merkmal überein. Eine Fläche steht nur neu, daher „mittel“.

### P11

- Paar: P11
- Alt: https://ted.europa.eu/de/notice/-/detail/670866-2022 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/598474-2026
- A (Identität): übereinstimmend für Bochum. Details: Neu nennt nur den Standort „Universitätsstraße 68, 44789 Bochum“. Alt nennt Los 1/2 „Ringstraße 52, 32427 Minden“ und Los 3/4 „Universitätsstraße 68, 44789 Bochum“. Flächen nennt keine Seite.
- B (Objektraum): erkennbar und übereinstimmend. Details: Gebiet Bochum, NUTS DEA51 (alt zusätzlich Minden, DEA46). Objektart Standort/Dienststelle der Krankenkasse, ergibt sich aus Auftraggeber und Standort. Leistung auf beiden Seiten Unterhaltsreinigung sowie Glas- und Rahmenreinigung.
- C (Stütze): Auftraggeber ja (IKK classic; Anschrift Dresden gegenüber Erfurt ist kein Widerspruch), CPV ja (90911200/90911300), Titel anders („Reinigung Westfalen-Lippe“ gegenüber „Reinigungsdienstleistungen Bochum“), Losstruktur anders (4 gegenüber 2), Zuschlagskriterien gleich (Konzept, Preis, Quadratmeter-Stundenleistung)
- Überschneidung der Objekte: 1 von 1 auf der kürzeren Seite (neu) = 100 %, 1 von 2 auf der längeren Seite (alt) = 50 %
- Lose mit Überschneidung: neu Los 1 ↔ alt Los 3 (Unterhalt Bochum), neu Los 2 ↔ alt Los 4 (Glas Bochum); alt Lose 1–2 (Minden) haben kein Gegenstück

Urteil: teilmenge

Sicherheit: –

Begründung: Neu nennt nur Universitätsstraße 68, Bochum. Das ist einer von zwei alten Standorten (alt zusätzlich Ringstraße 52, Minden), bei gleicher Leistung (Unterhalt sowie Glas/Rahmen). Die kürzere Liste ist also zu 100 % enthalten, und neu wird nichts ausdrücklich ausgeschlossen.

### P12

- Paar: P12
- Alt: https://ted.europa.eu/de/notice/-/detail/165984-2026 (Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/478291-2026
- A (Identität): widersprüchlich. Details: Neu „FA Mittelfranken-Ost, Standort Erlangen“, Erlangen 91052. Alt „FA Mittelfranken-Ost, Schwabach“, Schwabach 91126. Grundfläche neu ca. 6.900,06 qm, alt ca. 5.922,16 qm (−14 %). Jahresreinigungsfläche neu 980.342,50 qm, alt 700.963,38 qm.
- B (Objektraum): widersprüchlich. Details: anderer Ort (NUTS DE252 gegenüber DE255). Objektart Finanzamt und Leistung Unterhaltsreinigung auf beiden Seiten.
- C (Stütze): Auftraggeber ja (Freistaat Bayern, LfSt), CPV ja (90911200), Titel ähnlich, Losstruktur gleich (1 Los)
- Überschneidung der Objekte: 0 von 1

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Der Standort ist neu Erlangen (91052), alt Schwabach (91126), und die Grundfläche weicht ab (6.900,06 gegenüber 5.922,16 qm). Damit liegt ein klarer Widerspruch in A und B vor. Die gleiche Finanzamtsbezeichnung ist nur Stufe C.

### P13

- Paar: P13
- Alt: https://ted.europa.eu/de/notice/-/detail/563086-2025 (Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/555833-2026
- A (Identität): nicht vergleichbar. Details: Neu nennt Standorte A, B, C Nord und C Süd der Carl von Ossietzky Universität Oldenburg (Haarentor, Wechloy), alt die Standorte B (Haarentor) und C (Wechloy). Neu sind es Glasflächen (15.341 / 8.577 / 3.646 / 13.532 m²), alt Unterhaltsflächen (54.739 / 57.050 m²). Die Flächenarten sind verschieden.
- B (Objektraum): widersprüchlich. Details: Gebiet Oldenburg und Objektart Universität sind gleich, die Leistungsart aber nicht: neu „Glasreinigung“ (alle 4 Lose), alt „Unterhaltsreinigung“ (beide Lose).
- C (Stütze): Auftraggeber ja (Staatliches Baumanagement Niedersachsen), CPV teils, Titel ähnlich, Losstruktur anders (4 gegenüber 2)
- Lose mit Überschneidung: räumlich neu Lose 2–4 ↔ alt Lose 1–2, aber mit anderer Leistung

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Neu ist Glasreinigung (Titel „Glasreinigung Carl von Ossietzky Universität Oldenburg 4 Lose“), alt Unterhaltsreinigung (Titel „Unterhaltsreinigung CvO Universität Oldenburg 2 Standorte“). Eine andere Leistungsart gilt als Widerspruch, auch bei denselben Gebäuden.

### P14

- Paar: P14
- Alt: https://ted.europa.eu/de/notice/-/detail/488753-2023 (F02, Auftragsbekanntmachung)   Neu: https://ted.europa.eu/de/notice/-/detail/533895-2026
- A (Identität): übereinstimmend, soweit belegt. Details: Alt hat Objektlisten in Los 1–4 mit zusammen 42 Liegenschaften (z. B. GS Im Zentrum, Ernst-Mach-Gymnasium, KiTa Wibbelstätz, Rathaus, HFW Feuerwehr); Los 5 ist Glas „für alle städtische Liegenschaften“. Neu hat keine vollständige Liste. Im Feld `Note` stehen drei als „repräsentativ“ bezeichnete Objekte: Grundschule im Zentrum (Bonnstraße 109), Ernst-Mach-Gymnasium (Bonnstraße 64), Familienzentrum Wibbelstätz (Bonnstraße 40). Alle drei kommen alt vor (Los 1, Los 4, Los 2). Flächen nennt keine Seite.
- B (Objektraum): erkennbar und übereinstimmend. Details: Stadtgebiet Hürth, NUTS DEA27. Objektart laut Text auf beiden Seiten „Verwaltungsgebäude, Feuerwachen, Schulen und Kindertagesstätten“, neu zusätzlich „Unterkünfte für Geflüchtete“. Leistung auf beiden Seiten Unterhalts-, Vertretungs-, Grund- und Glasreinigung.
- C (Stütze): Auftraggeber ja (Stadt Hürth), CPV ja (Haupt-CPV 90910000), Titel ähnlich („Reinigungsleistungen 2023-2027“ gegenüber „Reinigungsleistungen 2026 bis 2031 (Lose 1 bis 6)“), Losstruktur anders (5 gegenüber 6)
- Überschneidung der Objekte: 3 von 3 auf der kürzeren Seite (neu, nur repräsentative Auswahl) = 100 %, 3 von 42 auf der längeren Seite
- Lose mit Überschneidung: neu Lose 1–5 (Unterhalt) ↔ alt Lose 1–4, neu Los 6 (Glas) ↔ alt Los 5. Die neuen Lose lassen sich keinen einzelnen Objekten zuordnen.

Urteil: teilmenge

Sicherheit: –

Begründung: Gebiet, Objektarten und Leistungen stimmen überein, und die drei neu genannten Objekte (GS im Zentrum, Ernst-Mach-Gymnasium, Wibbelstätz) stehen alle in der alten Liste. Neu nennt aber nur diese drei und zusätzlich die Objektart „Unterkünfte für Geflüchtete“. Die Alternative „objektgleich (mittel)“ verliert nach der Rangfolge bei Zweifel, wie im Kalibrierungsfall Stralsund. Der Hinweis im alten `COMPLEMENTARY_INFO` auf eine erneute Bekanntmachung „Mitte 2026“ ist eine Zeitangabe und wurde nicht verwendet.

### P15

- Paar: P15
- Alt: https://ted.europa.eu/de/notice/-/detail/467991-2026 (Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/630789-2026
- A (Identität): abweichend. Details: Neu „Bildungshaus Winkelwiese“, Haußerstraße 132, Tübingen. Alt „Bildungshaus Winkelwiese“, Haußerstraße 128-132. Eine Fläche nennt nur alt („ca. 4.200 m2 Schule, KITA und Sporthalle“).
- B (Objektraum): widersprüchlich. Details: Gebiet und Objekt sind gleich (Tübingen, DE142), die Leistungsart aber nicht: alt „Baureinigung Fertigstellung Neubau“, neu „Unterhalts und Grundreinigung ohne Glasreinigung“.
- C (Stütze): Auftraggeber ja (Universitätsstadt Tübingen), CPV teils, Titel ähnlich („Baureinigung I Bildungshaus Winkelwiese“ gegenüber „Grund- und Unterhaltsreinigung Bildungshaus Winkelwiese“), Losstruktur gleich (1 Los)

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Das Gebäude ist dasselbe (Bildungshaus Winkelwiese, Haußerstraße 128-132), aber die Leistungsart unterscheidet sich: Baureinigung nach Fertigstellung (alt) gegenüber Unterhalts- und Grundreinigung (neu). Das gilt nach den Regeln als Widerspruch.

### P16

- Paar: P16
- Alt: https://ted.europa.eu/de/notice/-/detail/582425-2019 (F06, Zuschlag Sektoren)   Neu: https://ted.europa.eu/de/notice/-/detail/565728-2026
- A (Identität): widersprüchlich (keine gemeinsamen Objekte). Details: Neu hat 2 Objekte (Los 29 „Kundenzentrum Köpenick“, Los 30 „Kundenzentrum Marzahn“). Alt hat 6 Lose: „Liegenschaften Spandau, Machandelweg inkl. Kantine“, „Liegenschaften Cicerostraße, Kundenzentrum Steglitz“, „Liegenschaften Usedomer Str. (Bestands-/Neubau), Niederschönhausen“, „Liegenschaften Marzahn“, „Liegenschaften Gleichrichterwerke“, „Liegenschaften Fundbüro Rudolfstraße“. Mögliche Entsprechung: alt „Liegenschaften Marzahn“ ↔ neu „Kundenzentrum Marzahn“. Sie ist nicht belegt und zählt nicht.
- B (Objektraum): teils widersprüchlich. Details: Gebiet Berlin (DE300); Köpenick kommt alt nicht vor. Objektart: alt Verwaltungs- und Betriebsliegenschaften einschließlich Kundenzentren, neu nur Kundenzentren. Leistung: neu Unterhaltsreinigung (CPV 90911000), alt Unterhalts- und Glasreinigung.
- C (Stütze): Auftraggeber ja (BVG), CPV teils, Titel anders, Losstruktur anders (2 gegenüber 6)
- Überschneidung der Objekte: 0 von 2 auf der kürzeren Seite (0 %), 0 von 6 Losen auf der längeren Seite

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Neu nennt Kundenzentrum Köpenick und Kundenzentrum Marzahn. Davon ist keines alt namentlich belegt; die alten Lose nennen Spandau, Steglitz, Usedomer Str., „Marzahn“ allgemein, Gleichrichterwerke und Fundbüro. Gemeinsame Objekte liegen damit unter 20 %, und die mögliche Entsprechung „Marzahn“ zählt nicht.

### P17

- Paar: P17
- Alt: https://ted.europa.eu/de/notice/-/detail/574481-2023 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/506593-2026
- A (Identität): nicht vergleichbar. Details: Neu „Gebiet-Los 3 beinhaltet neun Gebäude auf dem Wissenschaftscampus Berlin-Adlerhof“, ohne Namen und ohne Fläche. Alt 5 Lose („Los 1 - WISTA Nord“, „Los 2 - WISTA Süd 1“, „Los 3 - WISTA Süd 2“, „Los 4 - WISTA Süd 3“, „Los 5 - WISTA - CHIC“), jeweils „für verschiedene Gebäude“, ohne Anzahl und ohne Fläche.
- B (Objektraum): nicht erkennbar. Details: Gebiet auf beiden Seiten Technologiepark/Wissenschaftscampus Adlershof. Das neue Teilgebiet „Gebiet-Los 3“ lässt sich aber keinem alten Teilgebiet zuordnen, und die Objektart steht alt nur als „verschiedene Gebäude“ da. Leistung auf beiden Seiten Unterhaltsreinigung.
- C (Stütze): Auftraggeber ja (WISTA.Service GmbH), CPV ja (90911200), Titel ähnlich, Losstruktur anders (1 gegenüber 5). Die Losnummer 3 kommt auf beiden Seiten vor (alt „Los 3 - WISTA Süd 2“), ist aber nur Stufe C.
- Lose mit Überschneidung: nicht belegbar; möglich ist alt Los 3

Urteil: unklar

Sicherheit: –

Tendenz: eher dafür

Begründung: Beide Seiten beschreiben Unterhaltsreinigung auf dem Campus Adlershof ohne Objektliste. Alt steht nur „verschiedene Gebäude“, neu „neun Gebäude“ im „Gebiet-Los 3“, damit ist das Teilgebiet nicht zuordenbar. Für eine Überschneidung sprechen der gleiche Auftraggeber, der gleiche Campus und die gleiche Leistung. Wenn es eine Überschneidung gibt, dann wahrscheinlich als Teil des alten Gesamtumfangs.

### P18

- Paar: P18
- Alt: https://ted.europa.eu/de/notice/-/detail/465718-2022 (F02, Auftragsbekanntmachung)   Neu: https://ted.europa.eu/de/notice/-/detail/514223-2026
- A (Identität): abweichend. Details: Anzahl Objekte neu 53, alt 45. Jahresreinigungsfläche neu rund 3.600.000 m², alt ca. 3,2 Mio. m² (+12,5 %). Grundreinigungsfläche neu 11.200 m², alt ca. 7.000 m² (+60 %). Keine Seite hat eine Objektliste. Alt nennt Besichtigungsobjekte (Grundschulen Martin Luther, Am Regenstein, Derenburg, Timmenrode, Sportforum), neu nennt keine Namen.
- B (Objektraum): nicht erkennbar. Details: Neu „städtischer Objekte und Einrichtungen der Stadt Blankenburg (Harz) und Ortsteile“, alt „45 Objekte“, auf beiden Seiten ohne Objektart. Gebiet Blankenburg (Harz), NUTS DEE09. Leistung: neu Unterhalts-, Grund- sowie Glas- und Rahmenreinigung (3.400 m²), alt Unterhalts- und Grundreinigung.
- C (Stütze): Auftraggeber ja (Stadt Blankenburg (Harz)), CPV ja (90911200), Titel anders („OV-BlankenburgHarz-22“), Losstruktur gleich (je ein Los)

Urteil: unklar

Sicherheit: –

Tendenz: eher dafür

Begründung: Beide Seiten beschreiben Unterhalts- und Grundreinigung städtischer Objekte in Blankenburg (Harz) ohne Objektart und ohne Liste. Die Zahlen weichen ab: 53 gegenüber 45 Objekte, Jahresreinigungsfläche 3,6 gegenüber 3,2 Mio. m² (+12,5 %). Gleiche Stadt, gleiche Kernleistung und ähnliche Größenordnung sprechen eher für dasselbe Portfolio, neu wohl erweitert und um Glasreinigung ergänzt.

### P19

- Paar: P19
- Alt: https://ted.europa.eu/de/notice/-/detail/410442-2026 (Auftragsbekanntmachung)   Neu: https://ted.europa.eu/de/notice/-/detail/500007-2026
- A (Identität): widersprüchlich. Details: Neu Titel „Objektgruppe 3: Unterhaltsreinigung und Einpflege“ und `RecurringProcurementDescription` „Die Unterhaltsreinigung der Gebäude der Objektgruppe 3 erfolgt dauerhaft“. Alt in beiden Feldern „Objektgruppe 2“. Die neue `Description` beginnt allerdings ebenfalls mit „Objektgruppe 2: …“ (wortgleich mit alt). Keine Seite hat eine Objektliste oder Fläche.
- B (Objektraum): erkennbar und übereinstimmend. Details: Stadtgebiet Bocholt (DEA34), Schulgebäude/Turnhallen und ein Verwaltungsgebäude, Unterhaltsreinigung mit Einpflege.
- C (Stütze): Auftraggeber ja (Stadt Bocholt), CPV ja, Titel bis auf die Gruppennummer gleich, Losstruktur gleich (Los 1–2 Schulen, Los 3 Verwaltung)
- Lose mit Überschneidung: nicht belegt

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Neu ist in Titel und `RecurringProcurementDescription` „Objektgruppe 3“, alt „Objektgruppe 2“. Das sind zwei verschieden bezeichnete Gebäudegruppen desselben Auftraggebers (Schwesterverfahren), die Übereinstimmung in Stufe B und C gleicht das nicht aus. Die neue `Description` mit „Objektgruppe 2“ macht den Fall zweifelhaft, und zwischen „nicht objektgleich“ und „unklar“ gilt nach der Rangfolge das vorsichtigere Urteil.

### P20

- Paar: P20
- Alt: https://ted.europa.eu/de/notice/-/detail/155215-2021 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/503493-2026
- A (Identität): Objektliste übereinstimmend, Fläche teils abweichend. Details: Die Objekte sind auf beiden Seiten dieselben 5: Hasselweg 20, Elsässer Str. 15, Lilienthalstr. 3, Lilienthalstr. 1 und Heerstr. 5 in Kassel. Glasreinigung Los 2: 1.271,16 m² und 3.813,48 m² jährlich, auf beiden Seiten identisch. Los 3: Fußbodenfläche 3.097,75 m² identisch, jährlich 290.726,57 gegenüber 289.972,38 m² (0,26 %), Glas 653,99 m² identisch. Los 1 Unterhalt: neu nur Lilienthalstr. 3 und 1 mit 2.424,06 m² Fußbodenfläche, alt alle 4 Liegenschaften mit 6.267,07 m² (−61 %, abweichend).
- B (Objektraum): erkennbar und übereinstimmend. Details: Kassel (DE731), Dienstliegenschaften (Zoll, BImA, Bundespolizeiinspektion), Unterhalts- und Glasreinigung.
- C (Stütze): Auftraggeber ja (BImA; Anschrift Berlin gegenüber Bonn ist kein Widerspruch), CPV ja (90911200/90911300), Titel ähnlich (VOEK 154-20 gegenüber VOEK 077-26), Losstruktur gleich (Los 1 Unterhalt, Los 2 Glas, Los 3 Unterhalt und Glas)
- Überschneidung der Objekte: 5 von 5 = 100 % auf beiden Seiten
- Lose mit Überschneidung: Los 2 ↔ Los 2 (identisch), Los 3 ↔ Los 3 (Fläche gleich), Los 1 ↔ Los 1 (nur 2 von 4 Liegenschaften)

Urteil: objektgleich

Sicherheit: mittel

Begründung: Die fünf Adressen, die Glasflächen (1.271,16 und 653,99 m²) und die Fläche von Los 3 (3.097,75 m²) sind identisch. Die Unterhaltsfläche in Los 1 weicht aber um 61 % ab (2.424,06 gegenüber 6.267,07 m²), weil Hasselweg 20 und Elsässer Str. 15 neu nur noch Glasreinigung erhalten. Diese abweichende Fläche schließt „hoch“ aus. Eine alternative Lesart wäre „teilmenge“ bezogen auf die Unterhaltsreinigung; die Objektlisten selbst sind aber deckungsgleich.

### P21

- Paar: P21
- Alt: https://ted.europa.eu/de/notice/-/detail/676959-2022 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/571136-2026
- A (Identität): übereinstimmend (Objekte), Fläche nicht vergleichbar. Details: Beide nennen Graf-Aswin-Kaserne, BwDLZ Bogen und Pionierübungsplatz Wasser. Adressen: alt Bayerwaldstraße 36 und 26, neu Bayerwaldstr. 36, Bayerwaldstr. 26 und Hutterhof 1. Eine Fläche nennt nur alt (Los 1: ca. 17.150 m² Fußbodenfläche, Los 2: ca. 2.213 m² Fensterfläche). Die Liegenschaften sind einzelne Dienststellen, die Adressen zählen also nicht. Zwei weitere A-Merkmale sind nicht belegt.
- B (Objektraum): erkennbar und übereinstimmend. Details: Bogen (DE22B), Kaserne und Bundeswehrdienststellen, Unterhaltsreinigung. Alt kommt Glasreinigung hinzu (Los 2), neu steht ausdrücklich „ohne Glasflächenreinigung“.
- C (Stütze): Auftraggeber ja (BwDLZ Bogen), CPV teils (90910000 gegenüber 90911000/90911200), Titel ähnlich, Losstruktur anders (1 gegenüber 2)
- Überschneidung der Objekte: 3 von 3
- Lose mit Überschneidung: neu einziges Los ↔ alt Los 1 (Unterhaltsreinigung); alt Los 2 (Glas) hat kein Gegenstück

Urteil: objektgleich

Sicherheit: mittel

Begründung: Beide Seiten nennen dieselben drei Liegenschaften in Bogen (Graf-Aswin-Kaserne, BwDLZ, Pionierübungsplatz Wasser) mit Unterhaltsreinigung (alt Los 1). Bei diesen Dienststellen zählen die Adressen nicht als A-Merkmal, und eine Fläche steht nur alt, daher „mittel“. Das alte Glas-Los 2 hat neu kein Gegenstück.

### P22

- Paar: P22
- Alt: https://ted.europa.eu/de/notice/-/detail/285864-2022 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/613923-2026
- A (Identität): teils übereinstimmend. Details: Neu hat 18 Objekte (Vereinigung der Lose 1–5), alt 25 (Vereinigung der Lose 1–4). Gemeinsam sind 17: die Kindergärten Bobenheim am Berg, Erpolzheim, An der Bach, Haus für Kinder, Kallstadt und Weisenheim am Sand, die Grundschulen Freinsheim, Kallstadt und Weisenheim am Berg, die Sporthalle Freinsheim, das Rathaus der VG und die Feuerwehrgerätehäuser Dackenheim, Freinsheim, Herxheim, Kallstadt, Bobenheim/Weisenheim am Berg und Weisenheim am Sand. Nur neu: Dorfgemeinschaftshaus Dackenheim. Nur alt: Kindergarten Weisenheim am Berg, I-Punkt Freinsheim, I-Punkt Kallstadt, Dorfgemeinschaftshaus Herxheim, Grundschule Weisenheim am Sand, Feuerwehrgerätehaus Erpolzheim, Asylunterkunft Freinsheim, Asylunterkunft Weisenheim am Sand. Flächen nennt keine Seite.
- B (Objektraum): erkennbar und übereinstimmend. Details: Verbandsgemeinde Freinsheim (DEB3C), Kindergärten/Schulen/Feuerwehr/Verwaltung, Unterhalts-, Grund-, Sonder- und Glasreinigung. Alt kamen ausdrücklich Einrichtungen der Ortsgemeinden Weisenheim am Berg und Weisenheim am Sand hinzu.
- C (Stütze): Auftraggeber ja (Verbandsgemeindeverwaltung Freinsheim), CPV teils, Titel ähnlich, Losstruktur anders (4 Lose nach Leistung gegenüber 6 Losen nach Leistung und Ortsgemeinde)
- Überschneidung der Objekte: 17 von 18 auf der kürzeren Seite (neu) = 94 %, 17 von 25 auf der längeren Seite (alt) = 68 %
- Lose mit Überschneidung: neu Los 1 (Glas) ↔ alt Los 4; neu Lose 2–5 (Unterhalt und Grund nach Ortsgemeinde) ↔ alt Lose 1 und 2; neu Los 6 (Sonder) ↔ alt Los 3. Neu Lose 4 und 5 heißen „Glasreinigungsarbeiten“, beschreiben aber Unterhalts- und Grundreinigung, ein Fehler in der Quelle.

Urteil: teilmenge

Sicherheit: –

Begründung: 17 der 18 neuen Objekte stehen namentlich mit Adresse in der alten Liste (94 %). Die alte Liste hat 8 weitere Objekte (I-Punkte, Asylunterkünfte, GS Weisenheim am Sand u. a.), deckt sich mit 68 % also nicht nahezu. Neu wird nichts ausdrücklich ausgeschlossen.

### P23

- Paar: P23
- Alt: https://ted.europa.eu/de/notice/-/detail/156628-2026 (Auftragsbekanntmachung)   Neu: https://ted.europa.eu/de/notice/-/detail/508130-2026
- A (Identität): widersprüchlich. Details: Neu 38 Wohnliegenschaften (WE-Nummern) in Schwerin, Sanitz, Greifswald, auf Rügen und in Stralsund (Große Parower Str., Bertolt-Brecht-Str., Arnold-Zweig-Str. u. a.). Alt eine Liegenschaft „Hauptzollamt Stralsund // WE 117648 // Rudenstraße 26“, die neu nicht vorkommt.
- B (Objektraum): widersprüchlich. Details: Objektart neu Wohnliegenschaften „in privater Nutzung“ (Mehrfamilienhäuser), alt „gewerblich bzw. behördlich genutzte Gebäude“. Leistung neu Treppenhaus- und Glasreinigung, alt Unterhalts-, Grund- und Glas-/Rahmenreinigung.
- C (Stütze): Auftraggeber ja (BImA), CPV ja (90911200/90911300), Titel ähnlich (Muster „Offenes Verfahren (EU-weit) …“), Losstruktur anders (10 gegenüber 2)
- Überschneidung der Objekte: 0 von 1

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Neu sind es Wohnliegenschaften (Treppenhausreinigung), alt das Hauptzollamt Stralsund in der Rudenstraße 26. Objektart und Adresse sind verschieden, gemeinsame Objekte gibt es nicht.

### P24

- Paar: P24
- Alt: https://ted.europa.eu/de/notice/-/detail/431363-2021 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/564026-2026
- A (Identität): übereinstimmend für 2 Objekte. Details: Alt hat 2 Objekte, Amtsgericht Amberg (Los 1) und Landgericht Amberg (Los 2). Neu hat 3 Objekte, nämlich Amtsgericht (Lose 1/2), Landgericht (Lose 3/4) und „IT-Servicezentrum der bayerischen Justiz“ (Lose 5/6). Flächen: Amtsgericht Unterhalt ca. 5.749 gegenüber ca. 5.750 m² (0,02 %) und Glas ca. 753 gegenüber ca. 750 m² (0,4 %); Landgericht Unterhalt ca. 5.797 gegenüber ca. 5.800 m² (0,05 %) und Glas ca. 1.242 gegenüber ca. 1.300 m² (4,5 %, abweichend).
- B (Objektraum): erkennbar und übereinstimmend. Details: Amberg (DE231), Justizbehörden (Gerichte), Unterhaltsreinigung sowie Glas- und Fensterreinigung.
- C (Stütze): Auftraggeber ja (Freistaat Bayern / OLG Nürnberg), CPV ja, Titel fast gleich („Gebäude- und Glasreinigung für/der Justizbehörden Amberg“), Losstruktur anders (2 gegenüber 6)
- Überschneidung der Objekte: 2 von 2 auf der kürzeren Seite (alt) = 100 %, 2 von 3 auf der längeren Seite (neu) = 67 %
- Lose mit Überschneidung: neu Lose 1–2 ↔ alt Los 1 (Amtsgericht), neu Lose 3–4 ↔ alt Los 2 (Landgericht); neu Lose 5–6 (IT-Servicezentrum) haben kein Gegenstück

Urteil: teilmenge

Sicherheit: –

Begründung: Amtsgericht und Landgericht Amberg stehen auf beiden Seiten, mit fast gleichen Unterhaltsflächen (5.749/5.750 und 5.797/5.800 m²). Neu kommt das IT-Servicezentrum hinzu (Lose 5–6). Die kürzere alte Liste ist also zu 100 % in der längeren neuen enthalten.

### P25

- Paar: P25
- Alt: https://ted.europa.eu/de/notice/-/detail/495197-2026 (Auftragsbekanntmachung)   Neu: https://ted.europa.eu/de/notice/-/detail/673994-2026
- A (Identität): widersprüchlich. Details: Neu nennt Amtsgericht Goslar (Hoher Weg 9, Kaiserbleek 8), Amtsgericht Seesen (Wilhelmsplatz 1), Finanzamt Goslar (Wachtelpforte 40) und Finanzamt Bad Gandersheim (Alte Gasse 24). Alt nennt NLStBV Bad Gandersheim (Stiftsfreiheit 3, Abteihof 4), NLWKN Hildesheim (An der Scharlake 39, Am Flugplatz 16) und die Straßenmeistereien Uslar, Einbeck und Northeim. Keine Adresse kommt auf beiden Seiten vor.
- B (Objektraum): widersprüchlich. Details: Objektart neu Gerichte und Finanzamt, alt Straßenbau- und Wasserwirtschaftsverwaltung sowie Straßenmeistereien. Die Gebiete überschneiden sich nur in Bad Gandersheim, dort aber mit anderen Adressen.
- C (Stütze): Auftraggeber ja (Staatliches Baumanagement Niedersachsen), CPV ja, Titel nach gleichem Muster („26E7… - … (UR/GlasR)“), Losstruktur anders (8 gegenüber 3)
- Überschneidung der Objekte: 0 von 5 Adressen (neu), 0 von 7 Adressen (alt)

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Neu nennt Amtsgerichte Goslar und Seesen sowie das Finanzamt Goslar/Bad Gandersheim, alt NLStBV Bad Gandersheim, NLWKN Hildesheim und drei Straßenmeistereien. Kein Objekt ist gemeinsam (0 %). Nur das Verfahrensmuster (Stufe C) ist gleich.

### P26

- Paar: P26
- Alt: https://ted.europa.eu/de/notice/-/detail/503868-2026 (Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/638682-2026
- A (Identität): widersprüchlich. Details: Neu 8 Objekte: Bezirksamt Jöllenbeck, Kita Jöllenbeck, Sporthalle Auf dem Tie 1, Feuerwehrgerätehaus Jöllenbeck, UWB Westerengerstr. (Los 1) sowie Grundschule Sieker Interim, Grundschule Heeperholz, Sporthalle Heepen (Los 2). Alt 8 Objekte: Feuerwehrgerätehaus Altenhagen, Feuerwehrgerätehaus Heepen, KiTa Am Vollbruch, Gymnasium Heepen 2 (Los 1) sowie Grundschule Brake, Grundschule Schröttinghausen, KiTa Schröttinghausen, Sporthalle Spiekeroogstraße (Los 2). Mögliche Entsprechung: neu „Sporthalle Heepen“ ↔ alt „Gymnasium Heepen 2“. Sie ist nicht belegt und zählt nicht.
- B (Objektraum): teils widersprüchlich. Details: Stadt Bielefeld (DEA41) auf beiden Seiten, aber andere Stadtteile (neu Jöllenbeck, Sieker, Heepen; alt Altenhagen, Heepen, Brake, Schröttinghausen). Objektarten gemischt, Leistung Unterhalts-, Sonder- und Ergänzungsreinigung auf beiden Seiten.
- C (Stütze): Auftraggeber ja (Stadt Bielefeld, Amt für Zentrale Leistungen), CPV ja (90911200), Titel fast wortgleich („… in 8 Objekten der Stadt Bielefeld …“), Losstruktur gleich (2 Lose)
- Überschneidung der Objekte: 0 von 8 (0 %)

Urteil: nicht objektgleich

Sicherheit: –

Begründung: Beide Seiten nennen je 8 Objekte namentlich, aber kein einziges gemeinsam (z. B. neu Bezirksamt Jöllenbeck, alt Grundschule Brake). Die Überschneidung liegt also unter 20 %. Der fast wortgleiche Titel ist nur Stufe C.

### P27

- Paar: P27
- Alt: https://ted.europa.eu/de/notice/-/detail/669356-2022 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/609162-2026
- A (Identität): übereinstimmend. Details: Beide nennen „Rathaus … Altmarkt 1“ und „Gewandhaus, Altmarkt 16, 06712 Zeitz“ (2 Gebäude). Flächen oder Geschosse nennt keine Seite. Rathaus und Gewandhaus sind der Verwaltungssitz, also ein Einzelstandort, und die Adressen zählen nicht. Als weiteres A-Merkmal bleibt nur die Gebäudezahl (2 = 2).
- B (Objektraum): erkennbar und übereinstimmend. Details: Zeitz (DEE08), Rathaus und Gewandhaus, Los 1 Unterhalts- und Grundreinigung, Los 2 Glasreinigung.
- C (Stütze): Auftraggeber ja (Stadt Zeitz, Fachbereich Ordnungswesen), CPV teils (90911000 gegenüber 90911200), Titel fast gleich, Losstruktur gleich (2 Lose gleicher Art), Zuschlagskriterien gleich (80/20)
- Überschneidung der Objekte: 2 von 2
- Lose mit Überschneidung: Los 1 ↔ Los 1, Los 2 ↔ Los 2

Urteil: objektgleich

Sicherheit: mittel

Begründung: Beide Seiten nennen Rathaus (Altmarkt 1) und Gewandhaus (Altmarkt 16) in Zeitz mit denselben zwei Losen (Unterhalt und Grund, Glas). Bei diesem Verwaltungssitz zählen die Adressen nicht, und außer der Gebäudezahl gibt es kein weiteres A-Merkmal (keine Fläche, keine Geschosse), daher „mittel“.

### P28

- Paar: P28
- Alt: https://ted.europa.eu/de/notice/-/detail/524790-2022 (F03, Zuschlag)   Neu: https://ted.europa.eu/de/notice/-/detail/533980-2026
- A (Identität): nicht vergleichbar. Details: Neu „Unterhalts-, Grund- und Glasreinigung in 39 Standorten“, Ort „diverse Standorte im Stadtgebiet“, ohne Liste. Alt „diverse Objekte 14770 Brandenburg an der Havel“, ohne Anzahl und ohne Liste. Flächen nennt keine Seite.
- B (Objektraum): erkennbar, aber auf beiden Seiten unspezifisch. Details: Gebiet Brandenburg an der Havel (DE401). Objektart neu „Verwaltungsstandorte“, alt „Verwaltungsstandorte und Feuerwehren“. Leistung neu Unterhalts-, Grund- und Glasreinigung, alt Unterhalts-, Grund- und „teilweise Glasreinigung“.
- C (Stütze): Auftraggeber ja (Stadt Brandenburg an der Havel / GLM der Stadt), CPV teils (90911000 gegenüber 90911200), Titel gleich („Gebäudereinigung Verwaltungsobjekte“), Losstruktur anders (3 gegenüber 1), Zuschlagskriterien ähnlich (Preis und Fragenkatalog)

Urteil: unklar

Sicherheit: –

Tendenz: eher dafür

Begründung: Beide Seiten nennen nur „diverse“ Standorte/Objekte ohne Liste, daher ist „unklar“ das höchste erreichbare Urteil. Für dasselbe Objekt sprechen der gleiche Titel „Gebäudereinigung Verwaltungsobjekte“, die gleiche Stadt, die Objektart Verwaltungsstandorte und die gleiche Leistung. Die Feuerwehren, die nur alt erwähnt sind, schwächen die Tendenz etwas ab.

## Auswertung nach Schritt 5

### Anzahl je Urteil (20 Paare)

| Urteil | Anzahl | Paare |
|---|---|---|
| objektgleich (hoch) | 0 | – |
| objektgleich (mittel) | 4 | P10, P20, P21, P27 |
| teilmenge | 4 | P11, P14, P22, P24 |
| nicht objektgleich | 8 | P12, P13, P15, P16, P19, P23, P25, P26 |
| unklar | 4 | P9, P17, P18, P28 |
| davon unklar, eher dafür | 4 | P9, P17, P18, P28 |
| davon unklar, eher dagegen | 0 | – |
| davon unklar, keine Tendenz | 0 | – |

### Spanne

| Variante | Treffer | Fehler | Ausgeschlossen | Quote |
|---|---|---|---|---|
| streng | 0 (objektgleich hoch) | 20 | 0 | 0 von 20 = 0 % |
| breit | 8 (4 objektgleich mittel + 4 teilmenge) | 8 (nicht objektgleich) | 4 (unklar) | 8 von 16 = 50 % |
| Zusatz mit Tendenz | 12 (breit + 4 unklar, eher dafür) | 8 | 0 | 12 von 20 = 60 % |

Interpretation: Streng und breit liegen weit auseinander (0 % gegenüber 50 %). Die Aussage hängt also an den Zweifelsfällen und an der Sicherheitsstufe. Kein Paar erreicht „hoch“, weil die Regeln zu Einzelstandorten und abweichenden Flächen die Kandidaten mit den meisten Übereinstimmungen (P10, P20, P27) auf „mittel“ begrenzen. Die Variante mit Tendenz ist nur Zusatzinformation.

### Liste P-Nr → Urteil

- P9 → unklar (Tendenz eher dafür)
- P10 → objektgleich (mittel)
- P11 → teilmenge
- P12 → nicht objektgleich
- P13 → nicht objektgleich
- P14 → teilmenge
- P15 → nicht objektgleich
- P16 → nicht objektgleich
- P17 → unklar (Tendenz eher dafür)
- P18 → unklar (Tendenz eher dafür)
- P19 → nicht objektgleich
- P20 → objektgleich (mittel)
- P21 → objektgleich (mittel)
- P22 → teilmenge
- P23 → nicht objektgleich
- P24 → teilmenge
- P25 → nicht objektgleich
- P26 → nicht objektgleich
- P27 → objektgleich (mittel)
- P28 → unklar (Tendenz eher dafür)

## Randfälle und Hinweise (Interpretation)

- **P14:** Einstufung als „teilmenge“ nach der Rangfolge bei Zweifel. Neu nennt nur drei „repräsentative“ Objekte und die zusätzliche Objektart „Unterkünfte für Geflüchtete“. Die Alternative wäre „objektgleich (mittel)“. In der breiten Auswertung zählen beide gleich.
- **P20:** Wegen der um 61 % kleineren Unterhaltsfläche in Los 1 nur „mittel“. Andere Flächen sind auf zwei Nachkommastellen identisch. Die Alternative wäre „teilmenge“ (Unterhaltsreinigung neu nur für 2 von 4 Liegenschaften). In der breiten Auswertung zählen beide gleich.
- **P19:** Die neue Bekanntmachung widerspricht sich selbst (Titel „Objektgruppe 3“, Description „Objektgruppe 2“). Entschieden wurde nach der Rangfolge.
- **P21 und P9:** Alt gibt es ein Glas-Los, das neu fehlt. Das gilt nicht als Widerspruch, weil die Unterhaltsreinigung auf beiden Seiten vorkommt. Vermerkt ist es unter „Lose mit Überschneidung“.
- Bei P12, P15, P19, P23, P25 und P26 ist der mögliche Vorgänger selbst eine Bekanntmachung aus 2025/2026, bei P19, P23 und P25 sogar eine Auftragsbekanntmachung. Das ist eine Beobachtung zum Datensatz und floss nicht in die Urteile ein (Spielregel 3).

## Probleme beim Laden oder Lesen (Fakten)

- Laden: keine Probleme. Alle 16 fehlenden XML (P21–P28) kamen mit HTTP 200 und `application/xml`.
- Lesen: Im ersten Durchlauf hat das Hilfsskript das eForms-Feld `cbc:Note` auf Losebene nicht ausgegeben. Dort stehen bei P14 die repräsentativen Objekte und bei P12 die Flächen. Das wurde korrigiert, und alle neuen Bekanntmachungen wurden mit dem Feld erneut geprüft.
- Unstimmigkeiten in den Quellen selbst: P9 alt (Los 2 „ca. 58 000 m2“ passt nicht zur Summe von 7 800 m²), P19 neu (Objektgruppe 2/3), P22 neu (Lose 4/5 heißen „Glasreinigungsarbeiten“, beschreiben aber Unterhalts- und Grundreinigung), P17 (Schreibweise „Adlerhof“ statt Adlershof in beiden Quellen).
