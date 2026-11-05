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
| N23 | 199184-2026 | 2 | 2025-73 Gebäude- und Unterhaltsreinigung im PREVIER, HH |
| N24 | 537921-2026 | 1 | Unterhalts- und Grundreinigung |
| N25 | 170192-2026 | 2 | Los 2: Glasreinigungsleistungen |
| N26 | 7674-2026 | 4 | Los 4: Glasreinigungsleistungen |
| N27 | 64803-2026 | 1 | Unterhalts- und Tagesreinigung |
| N28 | 418297-2026 | 4 | Bezirk 4 |
| N29 | 542576-2026 | 1 | Unterhalts-, Grund- und Glasreinigung |
| N30 | 806407-2025 | 4 | Los 4 - Unterhalts- und Grundreinigung Ausbildungszentrum Meldorf 1, Bojestraße 3, 25704 Meldorf, Wohnheim Meldorf, Mars |
| N31 | 391727-2026 | 1 | Untehalts-/ Grundreinigng |
| N32 | 440545-2026 | 1 | Gebäudereinigung Gefahrenabwehrzentrum, Am Anger 28, 07743 Jena |
| N33 | 637113-2026 | 3 | Verwaltungsgebäude |
| N34 | 604188-2024 | 1 | Gebäudereinigung (Unterhaltsreinigung, Grundreinigung, Sonderreinigung) |
| N35 | 657794-2025 | 3 | 3: Reinigung Objekte Köthen: bitte hier nur den Gesamtangebotspreis eintragen |
| N36 | 135973-2026 | 2 | Objekte in Burgdorf, Ramlingen, Ehlershausen und Otze |
| N37 | 585652-2026 | 3 | Holzkirchen |
| N38 | 446621-2026 | 2 | Glas- und Rahmenreinigung |
| N39 | 217759-2026 | 1 | Glasreinigung |
| N40 | 168212-2026 | 2 | Los 2: Glasreinigungsleistungen |
| N41 | 661664-2026 | 1 | UHR Viktoria-Luise-Schule |
| N42 | 541310-2024 | 2 | Dillmann-Gymnasium |
| N43 | 239965-2026 | 3 | Haus der Kulturen der Welt (HKW) |
| N44 | 143678-2025 | 1 | Unterhalts- und Grundreinigung |
