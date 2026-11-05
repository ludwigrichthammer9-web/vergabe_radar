# Aufgabe: Laufzeiten aus Bekanntmachungen ablesen

Du liest Auszüge aus EU-Bekanntmachungen über vergebene Aufträge (Reinigungsleistungen) und trägst je Los **Fakten** zur Vertragslaufzeit ein.
In diesem Ordner liegen die Auszüge (`rohtext_<Nummer>.txt`, eine Datei je Bekanntmachung) und diese Aufgabe. Öffne **keine** anderen Dateien, nutze kein Internet und
starte keine weiteren Agenten. Es gibt keine „richtigen“ Werte, die du erraten sollst: Lies sorgfältig und trage nur ein, was im Text oder in den Feldern steht.

## Vorgehen je Los
Die Tabelle unten nennt je Zeile eine Nummer (N…), die Bekanntmachung, die Nummer des Loses und den Titel. Suche das Los in der Datei der Bekanntmachung (über Titel und Nummer;
Kennungen wie LOT-0001 zählen oft ab 1, manchmal ab 0) und lies **alle** Angaben dieses Loses und die allgemeine Beschreibung des Verfahrens. Trage dann die Spalten ein.

## Spalten (Tab als Trenner, eine Zeile je Los, Reihenfolge wie in der Tabelle)
`N`, `zuordnung_sicher`, `beginn`, `feld_enddatum`, `feste_dauer_monate`, `feste_ende`, `verl_status`, `verl_anzahl`, `verl_monate`, `spaetestes_ende`, `gesamtdauer_monate`,
`nicht_tagesgenau`, `kein_zuschlag`, `gebaeudereinigung`, `widerspruch`, `zitat`

- **zuordnung_sicher:** `ja` oder `nein` (nein, wenn Titel und Nummer nicht eindeutig zu einem Los passen).
- **beginn:** Beginn der Laufzeit des Loses als TT.MM.JJJJ (Feld StartDate oder Text); leer, wenn keine Angabe.
- **feld_enddatum:** Wert des Felds EndDate des Loses als TT.MM.JJJJ; leer, wenn das Feld fehlt.
- **feste_dauer_monate:** Wenn Text oder Feld ausdrücklich eine Dauer der **ersten festen Laufzeit ohne Verlängerungsoptionen** nennen: Anzahl Monate (3 Jahre = 36). Sonst leer.
- **feste_ende:** Wenn Text oder Feld ausdrücklich ein **Ende der ersten festen Laufzeit** nennen: TT.MM.JJJJ. Sonst leer.
- **verl_status:** `keine` (Verlängerung ausgeschlossen oder ausdrücklich nicht vorgesehen), `nichts_genannt` (kein Wort zu Verlängerung oder Option für dieses Los) oder `genannt`.
- **verl_anzahl:** Höchstzahl der Verlängerungen als Zahl, wenn genannt; sonst leer. **verl_monate:** Länge je Verlängerung in Monaten, wenn genannt; sonst leer.
- **spaetestes_ende:** Wenn Text oder Feld ausdrücklich ein **spätestes Ende des Vertrags einschließlich aller Verlängerungen** nennen (z. B. „endet spätestens am“, „längstens bis“): TT.MM.JJJJ. Sonst leer.
- **gesamtdauer_monate:** Wenn ausdrücklich eine **maximale Gesamtlaufzeit** genannt ist (z. B. „maximale Vertragslaufzeit vier Jahre“): Anzahl Monate. Sonst leer.
- **nicht_tagesgenau:** `ja`, wenn die erste feste Laufzeit nur über ein Ereignis ohne Datum beschrieben ist (z. B. „bis zum Schuljahresende“) und du daraus kein Datum ablesen kannst. Sonst `nein`.
- **kein_zuschlag:** `ja`, wenn die Bekanntmachung für **dieses Los** keinen Zuschlag nennt (z. B. „kein Gewinner gewählt“, „keine Angebote“). Sonst `nein`.
- **gebaeudereinigung:** `ja`, wenn das Los im Kern Gebäudereinigung ist (auch Glas- und Unterhaltsreinigung); `nein` bei anderen Leistungen (z. B. Schädlingsbekämpfung, Kanalreinigung, Mietkleidung).
- **widerspruch:** Ein kurzer Satz, wenn sich Angaben widersprechen (z. B. Feld und Text), sonst leer.
- **zitat:** Die tragenden Stellen **wörtlich** mit Feldname (höchstens etwa 400 Zeichen, ohne Tabs und Zeilenumbrüche).

Rechne **nichts** aus und schätze nichts: Trage nur ein, was ausdrücklich dasteht. Datumsangaben immer als TT.MM.JJJJ.

## Ergebnis
Schreibe die Tabelle (mit Kopfzeile) in die Datei `ergebnis.tsv` in diesem Ordner und gib sie am Ende zusätzlich im Chat aus. Danach nichts weiter erklären.

## Lose
| N | Bekanntmachung | Los | Titel |
|---|---|---|---|
| N1 | 355031-2026 | 1 | Leistungszeitraum 01. Juni 2026 bis 31. Mai 2030 |
| N2 | 72651-2026 | 3 | Los 3 Unterhalts- und Grundreinigung in Ennepetal und Gevelsberg |
| N3 | 731551-2025 | 1 | UHR Weißfrauen + Karmeliterschule_EU |
| N4 | 248450-2026 | 3 | Bereich Autobahnmeisterei Ludwigsburg |
| N5 | 265133-2026 | 1 | Unterhaltsreinigung |
| N6 | 621999-2026 | 2 | Los 2: Unterhaltsreinigungsleistungen |
| N7 | 582700-2026 | 1 | Los 9 |
| N8 | 279533-2026 | 3 | Sporthallen/LAA, etc. |
| N9 | 244318-2026 | 1 | Unterhaltsreinigung für das FA Cham |
| N10 | 713016-2025 | 1 | GGS, Am Höfling 14, 52066 Aachen |
| N11 | 428627-2026 | 2 | Glas- und Rahmenreinigung |
| N12 | 384588-2026 | 2 | Unterhalts- und Grundreinigung Büromietflächen KA Gartenstraße 76-78+82-84 und Zulassungstelle Ettlingen |
| N13 | 511911-2025 | 1 | Glas-, Jalousie und Fassadenreinigung, Bezirksdirektion Südlicher-Oberrhein inkl. Lahr, Schwarzwaldstr. 39 (Hauptverwalt |
| N14 | 750474-2025 | 1 | Unterhaltsreinigung, Grundreinigung optional und Winterdienst - Sekundarschule Am Schillerpark, einschließlich Sporthall |
| N15 | 39076-2026 | 6 | Präsenzreinigung |
| N16 | 832634-2025 | 6 | GGS Derschlag, GS Derschlag |
| N17 | 412103-2026 | 4 | Glasreinigung Olpe und Hemer |
| N18 | 471701-2026 | 3 | WC-Anlage "Rathaus" |
| N19 | 735715-2025 | 8 | Unterhaltsreinigung Verwaltungsgebäude |
| N20 | 535776-2026 | 8 | Los 8 Glasreinigung |
| N21 | 322718-2026 | 5 | Glas- und Rahmenreinigung BBS 1-3, SZ Oedeme, Kreisverwaltung, Gymnasium Lüneburg, Schule am Knieberg Lüneburg |
| N22 | 413340-2026 | 3 | Unterhaltsreinigung Bereich Wolfenbüttel |
