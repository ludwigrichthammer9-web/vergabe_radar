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
| N67 | 453533-2026 | 2 | Unterhalts- und Grundreinigung |
| N68 | 251654-2026 | 1 | Unterhaltsreinigung |
| N69 | 361445-2026 | 2 | Los 2: Unterhalts-, Grund- und Glasreinigung |
| N70 | 63836-2026 | 1 | Los 1 Unterhaltsreinigung Gerichte Greifswald |
| N71 | 3360-2026 | 1 | Treppenhausreinigung in diversen Wohnobjekten der WGS - Wohnungsgesellschaft Schwerin mbH |
| N72 | 346929-2026 | 1 | Los I |
| N73 | 473724-2026 | 1 | Gebäudereinigung - Justizvollzugsanstalt Dresden |
| N74 | 448077-2026 | 2 | Glasreinigung |
| N75 | 844214-2025 | 5 | Los 5: Glasreinigung |
| N76 | 661861-2026 | 6 | Unterhaltsreinigung - Los 5 |
| N77 | 328997-2026 | 2 | Objektreinigung 2026 - Glasreinigung |
| N78 | 511911-2025 | 2 | Glas-, Jalousie und Fassadenreinigung, Bezirksdirektion Ulm-Biberach |
| N79 | 686455-2025 | 1 | Unterhalts- und Grundreinigung / OT Graben |
| N80 | 348029-2026 | 1 | Ausschreibung Unterhalts- und Grundreinigung Gesamtschule Mittelkreis |
| N81 | 105754-2026 | 3 | Los 3 |
| N82 | 600199-2026 | 1 | Unterhaltsreinigung ADBV Freyung |
| N83 | 792749-2025 | 3 | Los 3: Unterhaltsreinigung Kreissitz |
| N84 | 832634-2025 | 2 | Kindergarten Dieringhausen, Kindergarten Dieringhausen-Familienzentrum, Jugentreff Martinstraße |
| N85 | 528615-2026 | 1 | Reinigung Behördenzentrum Hoyerswerda |
| N86 | 520463-2026 | 1 | Fachlos 1 - Unterhalts- und Grundreinigung |
| N87 | 2138-2026 | 4 | Unterhalts- und Grundreinigung |
| N88 | 149458-2026 | 2 | UR Berlin |
