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
| N89 | 491164-2026 | 1 | Gemeinde Lahnau - 1 Schule |
| N90 | 2138-2026 | 1 | Unterhalts- und Grundreinigung |
| N91 | 203509-2026 | 1 | Ausschreibung Unterhalts- und Grundreinigung Dreifachsporthalle und Schwimmbad |
| N92 | 492867-2026 | 3 | Los 3: Glasreinigung |
| N93 | 177588-2026 | 1 | RV Reinigung von Regenentwässerungsanlagen inkl. digitale Datenerfassung 2026-2029 |
| N94 | 310809-2026 | 1 | Los 7 - Unterhaltsreinigung für die Bezirksverwaltung Tübingen der BG Verkehr |
| N95 | 120111-2026 | 1 | Landkreis-Gymnasium St. Annen Annaberg-Buchholz, Pestalozzistraße 9, 09456 Annaberg-Buchholz_Unterhalts- und Grundreinig |
| N96 | 464059-2026 | 6 | Glasreinigung - Herne |
| N97 | 27949-2026 | 3 | Los 3 - Unterhaltsreinigung und Glasreinigung für die Kraftwerksliegenschaften |
| N98 | 489062-2026 | 3 | Los 3 - Standort Bergen auf Rügen |
| N99 | 560887-2026 | 12 | Los_12_Unterhalts_Glas-_und_Sonderreinigung_Los_12 |
| N100 | 562506-2026 | 4 | Los 4 - Verwaltungsgebäude 1 und 2, Rathaus, Haus am See |
| N101 | 150456-2026 | 3 | Los 3: AM Frankfurt, AM Langenselbold u. AM Reiskirchen |
| N102 | 600577-2026 | 4 | Los 4 |
| N103 | 795258-2025 | 2 | Glas- und Rahmengrundreinigung 20 Objekte |
| N104 | 488030-2026 | 1 | Unterhalts- und Grundreinigung Paula-Fürst-Schule, Kindergarten Kieselsteine, Kreisarchiv TRIWO Park |
| N105 | 307688-2026 | 1 | Unterhalts-, Grund- und Glasreinigung für den Landkreis Bautzen - Gymnasium und Sporthalle Großröhrsdorf, Oberschule Röd |
| N106 | 555604-2026 | 5 | Detmerode - Gebäudereinigung |
| N107 | 318623-2026 | 1 | Abschluss Rahmenvereinbarung Gebäudereinigung für die Liegenschaften des BwDLZ Aachen im Standortbereich Aachen |
| N108 | 391501-2026 | 3 | Glas- und Rahmenreinigung |
| N109 | 825382-2025 | 2 | Glas- und Rahmenreinigung |
| N110 | 445747-2026 | 1 | Unterhalts- und Glasreinigungsleistungen VOEK 671-25 |
