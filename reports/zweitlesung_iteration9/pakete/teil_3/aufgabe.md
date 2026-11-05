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
| N45 | 808856-2025 | 5 | Ueckersporthalle und Städtische Turnhalle |
| N46 | 606053-2026 | 2 | Glasreinigung |
| N47 | 298648-2026 | 3 | Struvenhuetten Sievershuetten |
| N48 | 520463-2026 | 2 | Fachlos 2 - Glas- und Rahmenreinigung |
| N49 | 471701-2026 | 2 | WC-Anlage "Hauptbahnhof" |
| N50 | 438373-2026 | 1 | Vertretungsreinigungen in städtischen Objekten - Vertretungsreinigung |
| N51 | 368710-2026 | 4 | Unterhaltsreinigung Meschede |
| N52 | 667031-2025 | 2 | Block 22 |
| N53 | 480534-2026 | 1 | Reinigungsdienstleistungen für die Bezirksverwaltung |
| N54 | 143678-2025 | 3 | Winter- und Streudienst |
| N55 | 374160-2026 | 1 | Nord 1 |
| N56 | 220298-2026 | 5 | UHR Dienstort Regen |
| N57 | 709107-2025 | 4 | Unterhalts-, Grund-, Sonderreinigung und Tagesdienst |
| N58 | 328165-2026 | 8 | LOS 8: Gebäudereinigung Stauwehrhalle |
| N59 | 369448-2026 | 5 | Los 5 |
| N60 | 710769-2025 | 3 | Los 3: Unterhalts- und Grundreinigung |
| N61 | 20090-2026 | 3 | Los 3 - Unterhaltsreinigung Hallstattstraße Mindelheim |
| N62 | 657664-2026 | 12 | Los 12 "Winterdienst Eisenbahnhaltestellen RHB" |
| N63 | 150675-2026 | 1 | VE 4.101a Unterhaltsreinigung Ost |
| N64 | 117357-2026 | 3 | AM Hermsdorf |
| N65 | 220594-2026 | 2 | Veranstaltungsbegleitende Reinigung |
| N66 | 728855-2025 | 3 | Los 3: Glas-/Rahmenreinigung |
