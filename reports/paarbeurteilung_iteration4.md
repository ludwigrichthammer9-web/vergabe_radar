# Paarbeurteilung Iteration 4

**Datum:** 2026-10-26
**Beurteiler:** Rechercheur (Subagent), Auftrag „Paarbeurteilung“
**Grundlage:** `reports/urteilsregeln_blindpruefung.md` Version 1.1 (vor der Beurteilung vollständig gelesen, einschließlich der Kalibrierungsbeispiele); Paarliste `reports/paarbeurteilung_iteration4_liste.md` (Q1–Q3)

**Unabhängigkeit:** Ich bestätige, dass ich keine der gesperrten Dateien gelesen habe: weder `src/zuordnung_*.py`, `src/objekt_merkmale.py`, `src/los_merkmale.py`, `src/gt_iteration4.py` noch `data/processed/`, `data/raw/ted_ft/`, `reports/zuordnung_*`, `reports/k2_*`, `reports/blindpruefung_*`, `reports/regel_entwicklung_*`, `reports/evaluation_*`, `reports/sichtbarkeit_*`, `reports/testfaelle_iteration4*`, `reports/dev_gesehene_q1_notices.txt`, `reports/bekannte_notices_iteration4.txt` und keine Dateien von Iteration 3 unter `reports/`. Gelesen habe ich nur die Urteilsregeln, die Paarliste und die TED-XML der Paare. Woher die Paare stammen, weiß ich nicht und habe es nicht zu erschließen versucht.

**Rohdaten:** unverändert unter `data/raw/rechercheur_20261026/paare/Q1/`, `Q2/` und `Q3/` (XML von `https://ted.europa.eu/en/notice/<nummer>/xml`, alle mit HTTP 200). Für das Vorgänger-Ende in Q2 zusätzlich `Q2/375094-2019_refnotice.xml`. Das ist die Auftragsbekanntmachung, auf die der Alt-Zuschlag selbst unter REF_NOTICE verweist (gleiches Verfahren). Sie wurde **nach** dem Urteil geöffnet und ging nicht in das Urteil ein.

**Nicht verwendet:** Zeitabstand, Vertragsende, Laufzeit und Auftragswert (Regel 3). Laufzeiten stehen nur im getrennten Abschnitt „Vorgänger-Ende“.

---

### Q1
- Alt: 765145-2025 (Zuschlag, eForms, veröffentlicht 2025-11-18)   Neu: 139668-2026 (Ausschreibung, eForms, IssueDate 2026-02-26)
- A (Identität): nicht vergleichbar (eine Adresse gemeinsam)  Details: Alt Los 1 „Los 1 Standort Munster“ nennt als Leistungsorte „Emminger Weg 59-61“ und „Humboldtstr. 100“, 29633 Munster. Alt Los 2 „Los 2 Standort Lüneburg“ nennt „Bleckeder Landstr. 59“, 21337 Lüneburg. Neu (ein Los) nennt nur „Humboldtstr. 100“, 29633 Munster, Liegenschaft „Wehrwissenschaftliches Institut“. Weder Flächen noch Gebäudezahl noch Geschosse auf einer der beiden Seiten.
- B (Objektraum): widersprüchlich  Details: Gebiet stimmt teilweise überein (Munster). Die **Leistungsart widerspricht**: Alt-Beschreibung „Abschluss Rahmenvereinbarung über die Entsorgung und Vernichtung von VS-Schriftgut, Datenträgern und Festplatten für die Standorte Munster und Lüneburg mit einem Schredder-Fahrzeug“. Neu-Beschreibung „Abschluss eines Rahmenvertrages über die Unterhaltsreinigung im BwDLZ Munster für die Liegenschaft Wehrwissenschaftliches Institut“.
- C (Stütze): Auftraggeber ja (beide „Bundeswehr-Dienstleistungszentrum Munster“), CPV nein (Alt 90918000, Neu 90911200), Titel anders, Losstruktur anders (2 Lose gegenüber 1 Los)
- Überschneidung der Objekte: 1 Adresse gemeinsam (Humboldtstr. 100). Bei anderer Leistungsart ohne Belang.
- Lose mit Überschneidung: Alt Los 1 (Munster), Neu Los LOT-0000 (nur über die Adresse)
- Urteil: **nicht_objektgleich**
- Tendenz: –
- Begründung: Leistungsart Alt „Entsorgung und Vernichtung von VS-Schriftgut … mit einem Schredder-Fahrzeug“ (CPV 90918000), Neu „Unterhaltsreinigung … Liegenschaft Wehrwissenschaftliches Institut“ (CPV 90911200). Das ist eine andere Leistungsart und damit ein klarer Widerspruch in Stufe B, trotz gemeinsamer Adresse Humboldtstr. 100 und gleichem Auftraggeber.
- Abfragen/XML: 0 / 2

### Q2
- Alt: 517331-2019 (Zuschlag, vor eForms, F03, veröffentlicht 2019-10-31, REF_NOTICE 2019/S 152-375094)   Neu: 195060-2026 (Ausschreibung, eForms, IssueDate 2026-03-19)
- A (Identität): übereinstimmend für 8 Objekte, mit zwei abweichenden Flächen  Details: Losweise Gegenüberstellung (Reinigungsfläche in m²):

  | Alt-Los | Alt (Name, m²) | Neu-Los | Neu (Name, Adresse, m²) | Fläche |
  |---|---|---|---|---|
  | 1 | DG Heerstraße, 821,47 | 1 | Dienstgebäude Heerstraße, Heerstr. 12/14, 662,10 | abweichend (−19,4 %) |
  | 2 | Dietrich-Bonhoeffer-Bibliothek, 1 629,90 | 3 | Dietrich-Bonhoeffer-Bibliothek, Brandenburgische Str. 2, 5.036,03 | abweichend (+209 %) |
  | 3 | Familienzentrum guk, 330,35 | 4 | Familienzentrum guk, Düsseldorfer Str. 3, 330,35 | gleich |
  | 4 | JFH Spirale, 1 056,28 | 11 | Jugendfreizeitheim Spirale, Wesfälische Str. 16 a, 1.056,28 | gleich |
  | 5 | Mommsenstadion, 1 489,64 | – | nicht aufgeführt | – |
  | 6 | Mossestift, 1 907,85 | – | nicht aufgeführt | – |
  | 7 | MS Prinzregentenstr, 400,90 | 12 | Musikschule Prinzregentenstraße, Prinzregentenstr. 72, 400,90 | gleich |
  | 8 | Rathaus Charlottenburg, 30 363,70 | 13 | Rathaus Charlottenburg, Otto-Suhr-Allee 100, 30.030,04 | gleich (−1,10 %, innerhalb 2 %) |
  | 9 | SC Wallotstr, 225,89 | 14 | Seniorenclub Wallotstraße, Wallotstr. 4, 225,89 | gleich |
  | 10 | Spielhaus Schillerstr, 287,76 | 15 | Spielhaus Schillerstraße, Schillerstr. 45, 287,76 | gleich |

  Neu enthält 16 weitere Lose, die in Alt nicht vorkommen: Neu Los 2 Dienstgebäude Hohenzollerndamm, 5 Gretel-Bergmann-Sporthalle, 6 Hans-Rosenthal-Sportanlage, 7 Haus der Jugend Anne Frank, 8 Hubertus-Sportplatz, 9 JFH Heckerdamm, 10 JFH Plöner Straße, 16 Sportanlage Am Volkspark, 17 Sportanlage Jungfernheide, 18 Sporthalle Emser Straße, 19 Sportplatz Im Jagen, 20 Stadtteilzentrum Halemweg, 21 Standesamt Alt-Lietzow, 22 Abenteuerspielplatz Holsteinische Straße, 23 Gartenarbeitsschule, 24 Erwin-von-Witzleben-Grundschule. Alt nennt nur Losnamen ohne Adressen, deshalb erfolgt die Zuordnung über den Namen. Die Flächenart ist auf beiden Seiten die Reinigungsfläche (Alt „Unterhalts-, Bedarfs- und Grundreinigungsarbeiten auf … m²“, Neu „… auf … m² Reinigungsfläche“).
- B (Objektraum): erkennbar und übereinstimmend  Details: Gebiet: beide Bezirk Charlottenburg-Wilmersdorf von Berlin (Neu: „Insgesamt 24 Einrichtungen im Bezirk Charlottenburg-Wilmersdorf“). Objektart: bezirkliche Einrichtungen, auf beiden Seiten je Los benannt. Leistungsart: Alt „Unterhalts-, Bedarfs- und Grundreinigungsarbeiten in diversen bezirklichen Einrichtungen“, Neu „Unterhalts-, Grund- und Bedarfsreinigung in diversen bezirklichen Einrichtungen“.
- C (Stütze): Auftraggeber ja (beide „Bezirksamt Charlottenburg-Wilmersdorf von Berlin“), CPV ja (90911200), Titel ähnlich, Losstruktur anders (10 gegenüber 24 Lose, ein Objekt je Los)
- Überschneidung der Objekte: 8 von 10 bezogen auf die kürzere Seite (Alt) = 80 %; 8 von 24 bezogen auf die längere Seite (Neu) = 33 %
- Lose mit Überschneidung: Alt 1, 2, 3, 4, 7, 8, 9, 10 entsprechen Neu 1, 3, 4, 11, 12, 13, 14, 15
- Urteil: **teilmenge**
- Tendenz: –
- Begründung: Die kürzere Alt-Liste (10 Lose) ist zu 8 von 10 (80 %) in der Neu-Liste belegt, fünf davon mit wortgleicher Reinigungsfläche (z. B. „Familienzentrum guk“ 330,35 m², „Spirale“ 1.056,28 m²) und „Rathaus Charlottenburg“ mit 1,1 % Abweichung. Neu enthält 16 weitere Objekte, Alt schließt nichts ausdrücklich aus. Damit ist die Bedingung für „teilmenge“ (≥ 50 %, längere Seite mit weiteren Objekten) erfüllt. Für „objektgleich“ sind die Listen nicht nahezu deckungsgleich.
- Vermerk: Zwei Alt-Objekte (Mommsenstadion, Mossestift) fehlen auf der Neu-Seite. Die Alt-Liste ist also nicht vollständig enthalten. Die Regel verlangt nur ≥ 50 %, daher bleibt es bei „teilmenge“. Bei zwei gemeinsamen Objekten weichen die Flächen stark ab (Heerstraße −19,4 %, Bibliothek +209 %). Nach Regel ist das kein Widerspruch.

**Vorgänger-Ende (getrennt vom Urteil):**
- Vorgänger mit Vertrag: 517331-2019 (Zuschlag selbst, „DATE_CONCLUSION_CONTRACT 2019-10-22“ für alle 10 Lose). Das F03-Formular enthält keine Laufzeit. Laufzeit daher aus der referenzierten Auftragsbekanntmachung 375094-2019 (gleiches Verfahren, „NOTICE_NUMBER_OJ 2019/S 152-375094“ im Alt-Zuschlag).
- Fakten aus 375094-2019 (für jedes Los gleich): „DATE_START 2019-12-01“, „DATE_END 2020-11-30“, „RENEWAL_DESCR: Verlängerung um jeweils 6 Monate (längstens um 24 Monate)“.
- Vorgänger-Ende: **2022-11-30**; Herkunft: **hoechstende** (Grundlaufzeit-Ende 2020-11-30 plus höchstens 24 Monate Verlängerung). Ohne Verlängerungen wäre das Ende 2020-11-30 (grundlaufzeit).
- Einschätzung (nicht geprüft, keine Suche durchgeführt): Zwischen dem Höchstende 2022-11-30 und dem neuen Verfahren 2026 liegen mehrere Jahre. Möglicherweise gibt es einen dazwischenliegenden Vertrag, der nicht Teil dieses Paares ist.
- Hinweis auf vorzeitige Neuvergabe: nein (das neue Verfahren beginnt nach dem Höchstende des Alt-Vertrags).
- Abfragen/XML: 0 API-Abfragen / 3 XML (2 Paar-XML, 1 referenzierte Auftragsbekanntmachung)

### Q3
- Alt: 400405-2025 (Zuschlag, eForms, IssueDate 2025-06-18)   Neu: 76175-2026 (Ausschreibung, eForms, IssueDate 2026-02-02)
- A (Identität): übereinstimmend für 1 Objekt, sonst verschieden  Details: Alt (ein Los) listet sechs Liegenschaften: „Bundeswehr-Dienstleistungszentrum Augustdorf, Lopshorner Weg 49“, „Generalfeldmarschall-Rommel-Kaserne (GFMR-Kaserne), GFM-Rommel-Str.“, „Sammelstandortschießanlage (SaStoSa), Lopshorner Weg 49“, „Standortmunitionsniederlage (StOMunNdlg) Augustdorf, Lippstädter Weg“, „Panzerwaschanlage (PzWaschanlage), Lopshorner Weg 86“ (alle 32832 Augustdorf) und „Dienstliegenschaft (DstLg) Detmold Heidenoldendorfer Str., Heidenoldendorfer Str. 136, 32758 Detmold“. Neu (drei Lose) nennt LOT-0001 „Gebäudereinigung BNetzA Leeheim“, Satellitenmessstelle 10, 64560 Leeheim; LOT-0002 „Gebäudereinigung BNetzA Detmold“, Heidenoldendorfer Str. 136, 32758 Detmold; LOT-0003 „Gebäudereinigung BNetzA Meschede“, Nördelstr. 5, 59851 Meschede. Gemeinsam ist nur die Adresse Heidenoldendorfer Str. 136, Detmold. Alt nennt nur eine Gesamtfläche („ca. 6.460.000 qm“ jährliche Fußbodenfläche), Neu keine Fläche. Flächen sind nicht vergleichbar.
- B (Objektraum): teilweise übereinstimmend, im Übrigen abweichend  Details: Leistungsart beide Gebäudereinigung (Alt „Gebäudereinigung in den Liegenschaften“, Neu „Dauerschuldverhältnis Gebäudereinigung“). Gebiet nur in Detmold gemeinsam (Alt sonst Augustdorf, Neu sonst Leeheim und Meschede). Objektart: Alt Bundeswehr-Liegenschaften (Kaserne, Schießanlage, Munitionsniederlage, Panzerwaschanlage, Dienstliegenschaft), Neu Standorte der Bundesnetzagentur (u. a. Satellitenmessstelle). Für die gemeinsame Adresse nennt Alt eine Bundeswehr-„Dienstliegenschaft“ und Neu „BNetzA Detmold“.
- C (Stütze): Auftraggeber nein (Alt „Bundeswehr-Dienstleistungszentrum Augustdorf“, Neu „Bundesnetzagentur“), CPV ja (90911200), Titel anders, Losstruktur anders (1 gegenüber 3 Lose)
- Überschneidung der Objekte: 1 von 3 bezogen auf die kürzere Seite (Neu) = 33 %; 1 von 6 bezogen auf die längere Seite (Alt) = 17 %
- Lose mit Überschneidung: Alt LOT-0000 und Neu LOT-0002 (Detmold)
- Urteil: **unklar**
- Tendenz: **eher dagegen**
- Begründung: Gemeinsam ist nur „Heidenoldendorfer Str. 136, 32758 Detmold“. Das sind 1 von 3 Neu-Objekten (33 %, also zwischen 20 % und 50 %) und 1 von 6 Alt-Objekten (17 %). Die Ausschlussregel „weniger als 20 % jeder Seite“ greift daher nicht, und nach Regel ergibt sich „unklar“. Die Tendenz ist „eher dagegen“: anderer Auftraggeber (Bundeswehr gegenüber Bundesnetzagentur), fünf von sechs Alt-Liegenschaften sind militärische Objekte in Augustdorf, zwei von drei Neu-Standorten (Leeheim, Meschede) fehlen in Alt, und die gemeinsame Adresse ist auf der Alt-Seite als Bundeswehr-„Dienstliegenschaft“ bezeichnet, auf der Neu-Seite als „BNetzA Detmold“.
- Abfragen/XML: 0 / 2

---

## Übersicht

**Anzahl je Kategorie (3 Paare):**

| Urteil | Anzahl | Paare |
|---|---|---|
| objektgleich_hoch | 0 | – |
| objektgleich_mittel | 0 | – |
| teilmenge | 1 | Q2 |
| nicht_objektgleich | 1 | Q1 |
| unklar | 1 | Q3 (eher dagegen) |

**Abbruch durch Budget:** keiner. Ich habe keine Abfrage an die Search API gestellt und insgesamt 7 XML geladen (6 Paar-XML und 1 referenzierte Auftragsbekanntmachung für das Vorgänger-Ende in Q2).

**Auffälligkeiten (Fakten):**
- Q1: Gleicher Auftraggeber (BwDLZ Munster) und eine gemeinsame Adresse (Humboldtstr. 100), aber andere Leistung (Schriftgutvernichtung mit CPV 90918000 gegenüber Unterhaltsreinigung mit CPV 90911200).
- Q2: Das Losschema wurde neu geschnitten (10 gegenüber 24 Lose), die Losnummern sind verschoben (z. B. Alt Los 8 „Rathaus Charlottenburg“ entspricht Neu Los 13). Alt-Losnamen sind abgekürzt („DG“, „JFH“, „MS“, „SC“), Neu nennt sie ausgeschrieben und mit Adresse. Fünf Flächen sind auf zwei Nachkommastellen identisch.
- Q3: Gleiche Adresse bei zwei verschiedenen Bundesbehörden (Bundeswehr und Bundesnetzagentur) als Auftraggeber. Der Beschaffer der Neu-Seite sitzt in Bonn (Tulpenfeld 4), der Leistungsort ist in Detmold.

**Grenzfälle der Regeln:**
- **Q3:** Die Regeln regeln die Überschneidung je Seite (< 20 % jeder Seite gegenüber 20–50 %). Nicht geregelt ist der Fall, dass eine Adresse übereinstimmt, Auftraggeber und Objektart der übrigen Objekte (militärische Liegenschaften gegenüber BNetzA-Standorten) aber verschieden sind. Ob das als „andere Objektart“ und damit als klarer Widerspruch in B gilt, lässt die Regel offen. Nach Vorgabe nicht neu ausgelegt, sondern „unklar“ vergeben.
- **Q2 (Vermerk, kein Grenzfall im engeren Sinn):** „teilmenge“ trotz zweier Alt-Objekte, die auf der Neu-Seite fehlen. Die Regel verlangt dafür nur ≥ 50 % der kürzeren Seite. Die Lesart „die kürzere Liste ist vollständig enthalten“ (wie im Stralsund-Beispiel) wäre strenger, sie steht aber nicht in der Regel.

## Ergebnistabelle

| Q | Alt | Neu | Urteil | Tendenz | Vorgänger-Ende | Herkunft |
|---|---|---|---|---|---|---|
| Q1 | 765145-2025 | 139668-2026 | nicht_objektgleich | – | – | – |
| Q2 | 517331-2019 | 195060-2026 | teilmenge | – | 2022-11-30 | hoechstende |
| Q3 | 400405-2025 | 76175-2026 | unklar | eher dagegen | – | – |
