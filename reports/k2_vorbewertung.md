# Vorbewertung K2 durch Claude (Iteration 2, Schritt 6)

Erstellt am 2026-10-23. **Vorläufig.** Verbindlich ist das Urteil des Nutzers in [k2_pruefliste.md](k2_pruefliste.md).
Empfehlung: Die Prüfliste zuerst selbst ausfüllen und erst danach mit dieser Datei vergleichen (Ankereffekt).

> **Nachtrag 2026-10-23:** Der Nutzer hat die Prüfung an Claude übertragen. Die verbindlichen Urteile stehen in
> [k2_pruefliste.md](k2_pruefliste.md). Gegenüber dieser Vorbewertung wurde **A4 von „ja“ auf „unklar“** geändert: Laut alter
> Ausschreibung 529954-2022 war das Los „Kitas und Friedhof“ nur 2 × 1 Jahr verlängerbar, neu werden nur zwei Kitas vergeben.
> Endstand: ja 5, nein 23, unklar 2 → K2 = 5/30 = 16,7 % (Wilson 7,3–33,6 %). Die Tabellen unten zeigen den Stand vor dem Nachtrag.

Grundlage: Auszüge aus der Original-XML in [k2_auszuege.md](k2_auszuege.md) (`src/k2_xml_auszug.py`, XML in
`data/raw/ted_xml/k2_20261023/`). Die TED-Webseiten selbst habe ich nicht geöffnet.
Frage je Paar: Ist plausibel dieselbe Leistung gemeint (gleiches Objekt bzw. gleiche Liegenschaften, ähnlicher Umfang)?

## A. 30 zufällige Treffer

| Fall | Stufe | Kand. | Urteil | Begründung (Fakten aus der XML) |
|---|---|---|---|---|
| A1 | 1 | 116 | nein | Autobahn GmbH: neu NL Nordost, PWC AM Fürstenwalde; Vorgänger NL Westfalen, PWC Werl/Wünnenberg/Münster/Lengerich. Treffer nur über gemeinsame Kennung der Autobahn GmbH. |
| A2 | 2 | 1 | ja | Gemeinde Wenden, Gebäudereinigung beide Male. Alte Ausschreibung 147163-2017: 01.08.2017–31.07.2021 mit Verlängerung; neu ab 01.08.2026. Fortlaufende Kette denkbar, Zwischenvertrag nicht ausgeschlossen. |
| A3 | 1 | 249 | nein | Stadt Frankfurt: neu Schillerschule, Vorgänger Ebelfeldschule. |
| A4 | 2 | 1 | ja | Stadt Traunreut: neu Kita Gartenstraße und Kita Traunwalchen; Vorgänger Los 1 „Reinigung Kitas und Friedhof“, 27.02.2023–27.02.2026 mit Verlängerung (529954-2022). Neuzuschnitt, Kitas waren Teil des alten Loses. |
| A5 | 1 | 120 | nein | Wie A1: neu AM Michendorf (NL Nordost), Vorgänger NL Westfalen. |
| A6 | 1 | 27 | nein | BLB NRW Düsseldorf: neu Schädlingsbekämpfung, Vorgänger Unterhaltsreinigung. Andere Leistung. |
| A7 | 3 | 2 | nein | LBM: neu Bereich Diez, Vorgänger Bereich Trier. |
| A8 | 3 | 5 | ja | DPMA Glasreinigung München: Vorgänger Zweibrückenstraße und Cincinnatistraße (48 Monate ab Okt. 2024), neu zusätzlich Anzinger Straße. Gleiche Leistung, aber Neuvergabe vor Ablauf der 48 Monate (Grund unbekannt). |
| A9 | 2 | 10 | nein | Bundeswehr: neu Fritzlar, Vorgänger Frankenberg (Eder). |
| A10 | 1 | 6 | nein | Neu Berufliches Bildungszentrum Ettlingen, Vorgänger Straßenmeistereien Bruchsal/Ettlingen. |
| A11 | 1 | 41 | nein | Uniklinik Aachen: neu UBFT-Gebäude Etagen E–2, Vorgänger OP/Intensivbereich. |
| A12 | 2 | 12 | nein | Justiz Sachsen-Anhalt: neu Landgericht und Sozialer Dienst Halle, Vorgänger Ministerium in Magdeburg. |
| A13 | 2 | 2 | ja | Bezirk Oberbayern: gleiche Standorte (Prinzregentenstraße 14, Dingolfinger Straße 15). Alter Vertrag 01.10.2022–30.09.2026 (242495-2022), neuer ab 01.10.2026. Lückenloser Anschluss. |
| A14 | 1 | 30 | nein | FHH: neu Grundschule Georg-Kerschensteiner, Vorgänger Dom-Veranstaltungen Heiligengeistfeld. |
| A15 | 1 | 5 | nein | Gießen: neu drei Sporthallen, Vorgänger Albert-Schweitzer-Schule/GS Lützellinden. |
| A16 | 2 | 2 | ja | WZB Berlin: gleicher Titel, gleicher Hinweis „Objektbesichtigung zwingend“. Alter Vertrag ab 01.09.2022, 12 Monate mit Verlängerung (315851-2022); neu ab 01.09.2026. Passt zu 3 Verlängerungen. |
| A17 | 1 | 422 | nein | BImA: neu Regensburg, Vorgänger Sindelfingen/Wolfschlugen. |
| A18 | 2 | 27 | nein | München: neu Haltestellenreinigung Bus/Tram, Vorgänger HKW Süd und Ausbildungszentrum. |
| A19 | 1 | 252 | nein | Stadt Frankfurt: neu Niddaschule, Vorgänger Ebelfeldschule. |
| A20 | 1 | 83 | nein | Dresden: neu GS Naußlitz, Vorgänger 32. Grundschule. |
| A21 | 3 | 3 | nein | BSR: neu Gebäudereinigung Mühlenstraße, Vorgänger Feuerfest-Reinigung Müllheizkraftwerk. |
| A22 | 1 | 2 | nein | Regierung von Unterfranken: neu Schädlingsbekämpfung in Unterkünften, Vorgänger Reinigung ANKER-Zentrum. |
| A23 | 1 | 17 | nein | Ulm: neu Kita Lettenwald, Vorgänger Gemeinschaftsunterkunft Eberhard-Finckh-Straße. |
| A24 | 1 | 102 | ja | Land Hessen: Polizeirevier Ost Kassel, Forstbachweg 80, beide Male. Alter Vertrag 01.04.2024–31.03.2027 mit 4 Optionsjahren; neu ab 01.11.2026, also vor Ablauf (Grund unbekannt). |
| A25 | 2 | 4 | unklar | Wupperverband Buchenhofen: neu Glas- und Unterhaltsreinigung am Standort (Buchenhofen 45), Vorgänger nur Abwasserlabor (Buchenhofen 37), 2022–2023 mit Verlängerung. Teilüberschneidung möglich. |
| A26 | 1 | 8 | nein | DESY: neu Reinraum/Labor (Dauerleistung), Vorgänger Bauendreinigung Neubau. |
| A27 | 3 | 4 | nein | Wiesbaden: neu 11 Schulen, Vorgänger 3 andere Schulen (läuft bis 2031). |
| A28 | 2 | 10 | nein | Neu Finanzamt Pforzheim/Neuenbürg und Polizeirevier Neuenbürg, Vorgänger Polizeiposten im Landkreis Calw. |
| A29 | 1 | 32 | nein | Neu Bundesarchiv Berlin-Lichterfelde, Vorgänger BMI Bonn. |
| A30 | 2 | 14 | nein | JKI: neu Quedlinburg, Vorgänger Siebeldingen. |

**Zusammenfassung (vorläufig):** ja 6, nein 23, unklar 1 → **K2 vorläufig 6/30 = 20 %** (Wilson 9,5–37,3 %), deutlich unter
der Schwelle von 80 %.

| Aufschlüsselung | ja / Fälle |
|---|---|
| Stufe 1 (Ende passt) | 1 / 16 |
| Stufe 2 (vor eForms, jüngster) | 4 / 10 |
| Stufe 3 (sonstige) | 1 / 4 |
| 1–2 Kandidaten | 4 / 6 |
| 3–10 Kandidaten | 1 / 9 (dazu 1 unklar) |
| mehr als 10 Kandidaten | 1 / 15 |
| Treffer über Kennung | 2 / 9 |

## B. 15 Ausschreibungen ohne Treffer

| Fall | Auftraggeber | Vermuteter Grund | Beleg |
|---|---|---|---|
| B1 | Gemeinde Ohlstadt | einmalige Leistung | Baureinigung nach Sanierung, 3 Wochen |
| B2 | Stadt Nettetal | kein früherer Zuschlag gefunden | kein Pool-Name mit „nettetal“ |
| B3 | MPI für molekulare Genetik | kein früherer Zuschlag gefunden | nur ein späterer Zuschlag (2026-06-22, vermutlich derselbe Auftrag) |
| B4 | REVG | **Name abweichend** | 45397-2024 „Innenreinigung von Fahrzeugen der REVG“ unter „REVG Rhein-Erft-Verkehrsgesellschaft“ (ohne „mbH“) |
| B5 | DAkkS | **Name abweichend** | 506639-2022 u. a. unter „Deutsche Akkreditierungsstelle GmbH“ (ohne „(DAkkS)“) |
| B6 | Stadt Niederkassel | kein früherer Zuschlag gefunden | nur der Zuschlag dieser Ausschreibung (2026-07-13) |
| B7 | Brandenburgisches OLG | einmalige Leistung | Schimmelreinigung von Archivgut |
| B8 | Stadt Wetzlar | kein früherer Zuschlag gefunden | nur der Zuschlag dieser Ausschreibung (2026-09-22) |
| B9 | OWL-IT | kein früherer Zuschlag gefunden | nur der Zuschlag dieser Ausschreibung (2026-08-19) |
| B10 | Stadt Ladenburg | kein früherer Zuschlag gefunden | nur der Zuschlag dieser Ausschreibung (2026-08-04) |
| B11 | Hansestadt Demmin | **Name abweichend** | 265131-2020 unter „Hansestadt Demmin“ (ohne „Der Bürgermeister“) |
| B12 | Museum für Gegenwartskunst | einmalige Leistung | Bauendreinigung Erweiterungsbau |
| B13 | Stadt Rösrath | **Name abweichend** | 638720-2022 „Stadt Rösrath“, 2018/2020 „Stadtverwaltung Rösrath Zentrale Vergabestelle“ |
| B14 | Stadt Schramberg | **Name abweichend** | 2018/2019 „Große Kreisstadt Schramberg Abt. Gebäudemanagement und Hochbau“ |
| B15 | ENTEGA AG MHKW | unklar | „ENTEGA AG“ 2025-11-26 und „ENTEGA AG Zentraleinkauf“ 2021 im Pool, Inhalt nicht geprüft |

Ob die Treffer bei abweichendem Namen inhaltlich passen, ist nicht geprüft.

## Nebenbefund A11: Laufzeit bei Vorgängern vor eForms

Alle 10 Vorgänger vor eForms in der Stichprobe verweisen über `REF_NOTICE` auf eine frühere Bekanntmachung (9 × F02, 1 × F05
Sektoren). In allen 10 stehen `DATE_START` und `DATE_END`, in 5 eine Verlängerungsoption (`RENEWAL`). Die Zuschläge selbst (F03/F06) enthalten
keine Laufzeit. Siehe [k2_auszuege.md](k2_auszuege.md).

## Interpretation (vorläufig)

- **Die Zuordnung über den Auftraggeber findet häufig einen früheren Zuschlag (K1), aber selten den richtigen.** Große Auftraggeber
  (Städte, BImA, Bundeswehr, Autobahn GmbH, Länder) vergeben viele Reinigungsverträge parallel. Wie viele Kandidaten es gibt,
  erklärt fast alles: Bei 1–2 Kandidaten stimmt die Zuordnung meist, bei mehr als 10 fast nie.
- **Die Auswahl nach passendem Vertragsende (Stufe 1) hilft nicht**, weil große Auftraggeber zu jedem Zeitpunkt irgendeinen
  auslaufenden Vertrag haben.
- **Kennungen sind zu grob:** Die Autobahn GmbH nutzt eine Kennung für mehrere Niederlassungen.
- **Exakte Namensgleichheit ist zu streng:** 5 von 15 Fällen ohne Treffer haben einen Vorgänger unter leicht anderem Namen.
- Nötig wäre eine Zuordnung auf **Objektebene** (Adresse, Liegenschaftsname, Titel). Bei Notices vor eForms stehen diese Angaben
  nur in der XML.
- Die echten Paare (A2, A13, A16, A24) zeigen, dass das Zielereignis existiert und sich mit der richtigen Information zuordnen lässt.
