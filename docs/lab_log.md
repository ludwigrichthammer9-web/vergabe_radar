# Lab-Log: Vergabe-Radar

_Big Data Analytics, Leistungsnachweis B (Zweierteam). Chronologisch nach CRISP-DM-Zyklen. Zahlen und Quellen stehen in `docs/iterationen.md`, `docs/phasen/` und `reports/`; hier steht die Erzählung mit den Entscheidungen. Fakten und Deutung sind getrennt gekennzeichnet._

_Erzeugt mit `src/report/lab_log.py` aus `docs/lab_log_vorlage.md`, `docs/zeitprotokoll.md` und `docs/ki_irrwege.md`._

## 0. Überblick

**Frage.** Mittelständler (Beispiel Gebäudereinigung) wollen sich früh auf Neuausschreibungen öffentlicher Aufträge vorbereiten. Lässt sich aus den Zuschlagsbekanntmachungen auf TED (Tenders Electronic Daily) vorhersagen, wann ein Vertrag neu ausgeschrieben wird?

**Antwort in drei Sätzen.**
1. Der Termin der Neuausschreibung lässt sich mit den TED-Daten nicht brauchbar vorhersagen: Die beste einfache Regel trifft das Fenster ±3 Monate in 28,8 % der 52 geprüften Fälle (Schwelle 60 %, naive Referenz 17,3 %).
2. Brauchbar ist eine Liste der Verträge mit dem Ende ihrer Laufzeit („laut Bekanntmachung“). Sie deckt 79,4 % der Lose ab (Fassung der Iteration 9, 9.325 Lose).
3. Wie genau diese Liste ist, haben wir viermal gemessen (zwei Handprüfungen, zwei KI-Zweitlesungen, die letzte mit Kontrolle durch einen Kommilitonen an 15 Losen). Zuletzt stimmt das Ende der Grundlaufzeit zu 94,3 % mit dem Vergleichswert zweier KI-Leser überein (Mensch 14/15). Jede Messung hat Schwächen; „die Liste ist korrekt“ ist damit nicht belegt.

**Verlauf.** Neun Iterationen in drei Zyklen. Die Entscheidung am Ende jeder Iteration (weiter, zurück zu Phase X, Idee anpassen) war vorab an Schwellen gebunden, die vor dem Ergebnis committet wurden.

| Zyklus | Iterationen | Leitfrage | Ergebnis |
|---|---|---|---|
| 1 | 1 bis 4 | Lässt sich ein neuer Auftrag seinem Vorgänger zuordnen? | Nein, jede Variante verfehlte die Schwelle; Idee angepasst |
| 2 | 5 | Trägt eine einfache Terminprognose? | Nein (28,8 % statt 60 %); Idee angepasst auf eine Vertragsliste |
| 3 | 6 bis 9 | Wie genau ist die Vertragsliste? | Brauchbar, zuletzt 94,3 % Übereinstimmung mit zwei KI-Lesern; nicht als korrekt belegt |

**Grenzen vorweg.** Kein Kundenkontakt (Entscheidung des Nutzers, 2026-10-29): Ob jemand für die Liste zahlt (A1, A15), ist ungeprüft. Alle Aussagen gelten für eForms-Bekanntmachungen (ab Herbst 2023), Haupt-CPV 909, Deutschland.

## 1. Zyklus 1: Zuordnung zum Vorgänger (Iteration 1 bis 4)

### Iteration 1 (2026-10-22): Machbarkeit der Daten
- **Business Understanding.** Kandidaten für eine Nische: Gebäudereinigung, IT-Wartung, Winterdienst, Sicherheit, Kantine. Kriterium: genug Zuschläge mit Laufzeit.
- **Data Understanding.** Abruf über die TED Search API v3, Rohdaten unverändert in `data/raw`. Befüllungsquoten je Nische.
- **Fakten.** Ein Laufzeitende ist in Gebäudereinigung bei 90,0 % bestimmbar (streng 80,9 %). Das strukturierte Verlängerungsfeld BT-58 ist nur bei 18,9 % befüllt (A5 widerlegt). Wertfelder enthalten Platzhalter (0,01 €, A6 widerlegt).
- **Entscheidung.** Gebäudereinigung als vorläufige Nische; weiter in Phase 2.

### Iteration 2 (2026-10-23): Neuausschreibungen sichtbar und zuordenbar?
- **Hypothese und Kriterium.** Auftraggeber + CPV genügen, um eine Neuausschreibung ihrem Vorgänger zuzuordnen (K2 ≥ 80 %).
- **Fakten.** K2 = 5/30 = 16,7 % (Wilson 7,3–33,6). 629 abgelaufene eForms-Verträge (K5 erfüllt), Median-Laufzeit nur 12 Monate.
- **Deutung.** Große Auftraggeber vergeben viele Verträge parallel; die Kennung des Auftraggebers reicht nicht.
- **Entscheidung (Rücksprung/Anpassung).** Zuordnung über das Objekt (Adresse, Titel) versuchen.

### Iteration 3 (2026-10-24/25): Zuordnung über das Objekt
- **Fakten.** Sichtbarkeit eines Vorgängers 63,3 % (V1, knapp), Präzision der Objekt-Regel 45,8 % (V2, Schwelle 80 %), Trefferquote 28,9 % (V3, Schwelle 60 %). Daten vor eForms liefern die Laufzeit über `REF_NOTICE` (A11: 25/30 = 83,3 %).
- **Trennung Entwicklung/Test.** Die Regel wurde auf Entwicklungsdaten gebaut (Claude hielt 10–11 von 12 Vorschlägen für plausibel) und auf neuen Daten getestet (11 von 24 korrekt).
- **Entscheidung.** Regel verworfen; ein letzter Versuch auf neuen Testdaten.

### Iteration 4 (2026-10-25 bis 10-30): letzter Verbesserungsversuch
- **Fakten.** Bei den vorgeschlagenen Paaren stimmt die Regel oft (W2 17/19 = 89,5 %), sie schlägt aber nur bei 19 Fällen etwas vor (Mindestzahl 25 verfehlt). Trefferquote W3 56,7 % (Schwelle 60 %), Zweitprüfung durch den Nutzer nur 65 % (Schwelle 85 %).
- **Entscheidung (Idee anpassen).** Keine weitere Zuordnungsregel. Stattdessen eine Vertragsliste aus den Zuschlägen selbst.

## 2. Zyklus 2: Terminprognose (Iteration 5)

### Iteration 5 (2026-10-30 bis 11-04): Vertragsliste und Backtest
- **Business Understanding (geschärft).** Prognoseziel: Veröffentlichungstermin der Neuausschreibung. Regel R1 = Höchstende − 6 Monate; Baseline R0 = Ende der Grundlaufzeit − 6 Monate. Treffer = Fenster ±3 Monate. Schwelle 60 %, festgelegt vor jeder Berechnung (`docs/business.md` §7.1).
- **Data Preparation.** Zuschlagstabelle je Los (`src/prepare/vertragsliste.py`): Ende der Grundlaufzeit, Höchstende (aus Datum, Höchstlaufzeit, BT-36 und Anzahl × Länge im Freitext), Herkunft. 9.915 Lose; Laufzeit bei 79,7 % bestimmbar. Leakage vermieden: nur Wissen zum Zeitpunkt des Vorgänger-Zuschlags.
- **Modeling/Evaluation.** Backtest auf 52 von Hand bestätigten Paaren (Zweitprüfung 61/67 = 91,0 %, mit KI-Hilfe, deshalb nicht als unabhängig gewertet).
- **Fakten.** R1 28,8 % (Wilson 18,3–42,3), R0 17,3 %. 20 Neuausschreibungen kamen mehr als 3 Monate früher, 17 später. Robust gegen Ausreißer, Vorlauf und Gewichtung.
- **Deutung.** Der Termin ist zweigipflig verteilt; ein fester Abstand trägt nicht.
- **Entscheidung (Idee anpassen).** Keine Terminprognose. Produktkern ist die Vertragsliste mit Enddaten.

## 3. Zyklus 3: Qualität der Vertragsliste (Iteration 6 bis 9)

### Iteration 6 (2026-11-04): Prototyp und erste Handprüfung
- **Gemacht.** Prototyp der Liste für die Oberpfalz (146 Lose, Stufen A–F je Eintrag). Handprüfung von 60 Zufallslosen durch den Nutzer.
- **Fakten.** Ende der Grundlaufzeit 54/60 = 90,0 % laut Auswertung, 53/60 = 88,3 % nach einem später gefundenen Fehler (Schwelle 90 %). Höchstende 91,7 %. Abdeckung 79,7 % (Schwelle 80 % knapp verfehlt).
- **Fehlertyp.** Das Enddatum der Bekanntmachung ist manchmal schon das Höchstende (z. B. „Festlaufzeit von … bis …“).
- **Schwäche (vom Evaluator gefunden).** Die Vorlage zeigte den Listenwert, die Prüfung war dadurch verankert.
- **Entscheidung (zurück zu Phase 3).** Regel erweitern, vor dem Ziehen einer neuen Stichprobe committen, Vorlage ohne Listenwerte.

### Iteration 7 (2026-11-04): Regel 1b und neue Prüfung
- **Gemacht.** Regel 1b gebaut und getestet an den Fehlerfällen der Iteration 6 (Entwicklungstest, zählt nicht). Regel und Seed wurden vor dem Ziehen committet. 80 Zufallslose plus 15 Lose, die Regel 1b ändert. Prüfung durch den Nutzer ohne Listenwerte; Lose mit „unbekannt“ wurden im TED-Original nachgeprüft.
- **Fakten.** Ende der Grundlaufzeit 36/47 = 76,6 % (Wilson 62,8–86,4) der Lose L1–L50. Regelwirkungs-Lose 8/15. Höchstende verfehlt.
- **Deutung.** Das Ergebnis ist ein Mischmaß aus Listenfehlern und Prüfungsfehlern: Bei 45 von 47 Losen nimmt die Liste das Enddatum-Feld, und die Nachprüfung schrieb dasselbe Feld ab. Regel 1b ist weder belegt noch widerlegt.
- **Eigene Fehler im Prüfdesign** (siehe KI-Irrwege): Felder in der Vorlage versteckt, „Nachprüfung ersetzt die erste Abgabe“, Rat zur Feldübernahme.
- **Entscheidung.** Abschluss mit diesem Stand, kein dritter Regelversuch (vorab festgelegte Folge für Y1 zwischen 70 und 90 %). Das Ende der Grundlaufzeit gilt als „laut Bekanntmachung“, das Höchstende nur als Hinweis.

### Iteration 8 (2026-11-04/05): KI-Zweitlesung
- **Gemacht.** Liste und Regeln eingefroren. Zwei KI-Leser (Opus, Sonnet) lasen die 95 Lose aus dem TED-Original, ohne Listenwerte und ohne Einträge des Prüfers. Kriterien Z0 bis Z4 und Vorlage vor dem Lauf committet. Den Vergleichswert bei Uneinigkeit und eine Kontrolle von 10 Übereinstimmungen übernahm der Evaluator.
- **Fakten.** Leser untereinander 94/95. Liste = Vergleichswert 77/80 = 96,2 % (Wilson 89,5–98,7). Regelwirkungs-Lose 14/15, bei einheitlichem Maßstab für „zum Schuljahresende“ 11/15. Höchstende 75/80 und 67/72. Kontrolle 10/10. Im Dreiervergleich stimmt die Liste in 45/47 Losen mit dem Vergleichswert überein, der Prüfer der Iteration 7 in 34/47.
- **Neu gefundene Fehler der Liste** (am Original bestätigt): Enddatum ist schon Höchstende bei „3 Jahre mit Option“ (L5); Wert von Los 1 auf Los 2 übertragen (L81); Höchstende falsch gelesen (L72, L82); Lose ohne Zuschlag stehen in der Liste (L69, L72).
- **Grenzen.** Die Leser sind nicht unabhängig: gleiche Modellfamilie wie die Regel und der Evaluator, gleiches Abrufwerkzeug mit Hilfsmodell, und sie hatten die Projektbeschreibung mit dem Fehlertyp im Kontext. Die Vorlage gab Regel 1b als Leseanweisung vor.
- **Entscheidung.** Weiter (Projektabschluss), eingeschränkt formuliert: Die Liste ist durch zwei KI-Lesungen gestützt, nicht durch einen unabhängigen Menschen bestätigt.

### Iteration 9 (2026-11-05): Regeln 6 bis 10 und neue Stichprobe
- **Gemacht.** Die in Iteration 8 gefundenen Fehlerarten behoben (Regeln 6 bis 10): Lose ohne Zuschlag entfernt (Zuschlagsfelder nachgeladen), Regel 6 eingeschränkt, Monatsnamen-Daten, „maximal um N Jahre“ als Gesamtdauer, „N Jahre mit Option“ als feste Dauer. Neue Liste: 9.325 statt 9.915 Lose (590 ohne Zuschlag, 6,0 %). Neue Stichprobe von 110 Losen (Seed 20261109, vor dem Ziehen committet; 70 Zufallslose, 30 geschichtete, 10 beschreibende). Zwei KI-Leser (Opus, Sonnet) lasen den Rohtext des TED-XML in Sitzungen ohne `CLAUDE.md` und trugen nur Fakten ein; der Vergleichswert folgt aus einer vorab committeten, neutralen Definition. Ein Kommilitone las 15 Lose im TED-Original.
- **Fakten.** V1 66/70 = 94,3 % (Wilson 86,2–97,8; Schwelle 90 %). V2 28/30 = 93,3 %. V3 neue gegen alte Fassung 66 gegen 65 von 70. V5 Leser untereinander 110/110. V6 Kommilitone 14/15. **Verfehlt:** V4 Höchstende (87,1 % bei Schwelle 90 %; 85,2 % bei 85 %), V7 ein Los mit „kein Zuschlag“ (N51); V8 Verfahren nur teilweise.
- **Deutung.** Die Fassung der Iteration 9 ist auf dieser Stichprobe zu 94,3 % mit dem Vergleichswert identisch (alte Fassung 92,9 %, bloßes Feld 90,0 %). Der Nutzen der Regeländerung ist nicht gesichert: Die Stichprobe trennt die Fassungen kaum, der Vergleichswert ist teilweise zirkulär, V5 zeigt vor allem gleiche Anweisung und gleiche Rohtexte. N51 trägt `unpublished` (Ergebnis aus geschäftlichen Interessen nicht veröffentlicht), nicht „kein Zuschlag“; die Ursache liegt in der Anweisung an die Leser.
- **Grenzen.** Gleiche Modellfamilie (Regel, Leser, Evaluator); Läufe teils per Skript statt im Fenster (Abweichung vom Plan, Skript erst mit den Antworten committet); `~/.claude` nicht geprüft; Gruppe R nur 2 Lose; V6 mit 15 Losen dünn.
- **Entscheidung.** Weiter, Projektabschluss, eingeschränkt formuliert. Die Fassung der Iteration 9 wird der Prototyp, das Höchstende bleibt Hinweis. V4, V7 und V8 werden offen als verfehlt bzw. teilweise berichtet; nicht zulässig ist „V1 bis V8 erfüllt“. Keine weitere Iteration.

## 4. Was wir empfehlen und was nicht

- **Empfehlung.** Die Vertragsliste „Ende der Laufzeit laut Bekanntmachung“ ist als Ausgangspunkt nutzbar. Vor einer Entscheidung die verlinkte Bekanntmachung lesen.
- **Zulässige Aussage.** „Zu 94,3 % identisch mit dem Vergleichswert zweier KI-Leser; an 15 Losen bestätigt ein Mensch (14/15); Höchstende nur Hinweis.“
- **Nicht belegt.** Eine Terminprognose; „die Liste ist korrekt“; „Fehlerarten behoben und bestätigt“; „V1 bis V8 erfüllt“; Nachfrage und Zahlungsbereitschaft (A1, A15).
- **Offene Grenzen.** Das Höchstende der Liste ist oft zu hoch (laut Evaluator in 7 von 11 Z-Fällen Überschätzung); Ergebnisse, die „nicht veröffentlicht“ sind (`unpublished`), werden nicht erkannt; Schuljahres-Verträge nicht tagesgenau; mehr menschliche Kontrolle und eine zweite Modellfamilie fehlen. Die in Iteration 8 gefundenen Fehlerarten (Lose ohne Zuschlag, Übertragung von Einzelwerten, Monatsnamen, „um N Jahre“, „N Jahre mit Option“) sind in der Fassung 9 behoben, aber nicht bestätigt.

## 5. KI-Irrwege und ihre Prüfung

Die KI (Claude Code) hat Hypothesen, Regeln, Stichproben und Auswertungen mitgebaut. Die Fehler wurden vom Nutzer, vom Evaluator (eigener Subagent, nur Lesezugriff) oder von Claude selbst gefunden.

| Datum | Irrweg | Bemerkt durch | Konsequenz |
|---|---|---|---|
| 2026-10-23 | K2-Urteile und Zuordnungsregel stammten von derselben Hand (Claude) | Evaluator ([evaluation_iteration2.md](../reports/evaluation_iteration2.md)) | Handsuche durch getrennten Subagenten, Zweitprüfung durch den Nutzer |
| 2026-10-25 | Auf den Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 korrekt | Test auf neuen Daten ([evaluation_iteration3.md](../reports/evaluation_iteration3.md)) | Regel verworfen; Testdaten strikt getrennt |
| 2026-10-30 | Iteration 4: Parser zählte „grundlaufzeit, hoechstende“ nicht mit, W5 zu niedrig (189 statt 297) | Evaluator ([evaluation_iteration4.md](../reports/evaluation_iteration4.md)) | Auswertung korrigiert, Nachtrag |
| 2026-11-03 | Kalibrierungsbeispiele der Urteilsregeln nicht aus der Zweitprüfung (Iteration 5) ausgeschlossen: 4 Paare identisch, 3 mit gleicher neuer Bekanntmachung | Nutzer beim Ausfüllen (P11, P12) | Paare werden abgezogen, in der Auswertung dokumentiert |
| 2026-10-30 | Lese-Regeln für das Höchstende nur an eForms-Texten getestet, 55 von 68 Backtest-Vorgängern stammen aus der Zeit vor eForms | Selbstprüfung beim Zusammenstellen der Paare | offen ausgewiesen, keine Nachjustierung |
| 2026-11-04 | Claude schrieb in der Auswertung der Zweitprüfung „‚Alles bestätigen‘ ist damit ausgeschlossen“; rechnerisch erreicht blindes Bestätigen der 57 echten Paare bei 10 abgelehnten Ködern schon 57/67 = 85,1 % (Schwelle 85 %) | Evaluator (Nachrechnung, `reports/evaluation_iteration5.md`) | Aussage in der Entscheidung nicht verwenden; X2 nur mit den Ködern (9/10) und den Abweichungen deuten |
| 2026-11-04 | Hinweis des Evaluators: Begründungen der Zweitprüfung (auch P1–P13) ähneln dem Stil der Handsuche; Nutzung von Hilfsmitteln nicht dokumentiert | Evaluator | Nutzer bestätigt KI-Unterstützung (Urteile „nur geschärft“); X2 nicht als unabhängige Bestätigung werten; A18 bleibt ungeprüft |
| 2026-11-04 | Iteration 6, Teil B: Claude stellte die „unabhängige“ Paarprüfung aus Paaren zusammen, die der Prüfer schon aus Iteration 5 kannte | Nutzer beim Ausfüllen („warum gibst du mir auch die selben Paare?!“) | Teil B zählt nicht; Aufbau im Protokoll als Fehler vermerkt |
| 2026-11-04 | Iteration 6: Die Prüfvorlage zeigte das Enddatum der Liste neben den Texten (Verankerung); Claude schrieb außerdem fälschlich, kein Eintrag der Oberpfalz sei geprüft, dabei war L6 in der Liste | Evaluator und Nachprüfung durch Claude | Iteration 7: Vorlage ohne Listenwerte, Aussage korrigiert |
| 2026-11-04 | Iteration 7: Regel 1b machte in der ersten Fassung L6, L14, L46 falsch (Kündigungsfristen als Dauer, Datum im Text als Beleg) | Entwicklungstest an den 60 Losen der Iteration 6 | Regel eingeschränkt, vor dem Ziehen der Stichprobe committet |
| 2026-11-04 | Iteration 7: Die Zufallsstichprobe enthielt kein Los, das Regel 1b ändert (Entwicklungs-Notices ausgeschlossen); Claude merkte das erst nach dem Ziehen | Selbstprüfung nach dem Ziehen | Kriterium Y1r vor der Prüfung ergänzt; Typ „Festlaufzeit-Datum“ bleibt ungetestet |
| 2026-11-04 | Iteration 7: Claude versteckte Beginn, Ende und Dauer in der Vorlage, damit kein Listenwert verankert; die Quelle „Feld“ war damit ohne TED-Original nicht erreichbar, und 65 von 95 Einträgen lauteten „unbekannt“ (Y1 zunächst 25 %) | Auswertung (0 Datumsabweichungen, 67 Einträge „unbekannt“) | Nachprüfung der 68 Lose im Original; Aufbau als Fehler im Vorgehen vermerkt |
| 2026-11-04 | Iteration 7: Claude legte vor, dass die Nachprüfung die erste Abgabe ersetzt, und riet, das Enddatum des Feldes zu übernehmen, wenn der Text nicht widerspricht; bei den Regelwirkungs-Losen (z. B. L65) verschlechterte das einen zuvor richtigen Texteintrag | Auswertung der Nachprüfung (Y1r 8/15) | im Abschluss offen genannt; Eintrag des Prüfers nicht verändert |
| 2026-11-04 | Iteration 7: Das Höchstende sollte nur bei Änderung neu eingetragen werden; 15 Einträge „unbestimmbar“ blieben veraltet, Y2 war dadurch rechnerisch zu niedrig (61,7 % statt 90,6 % ohne diese) | Claude bei der Auswertung | beide Werte ausgewiesen, Y2 nur mit Vorbehalt |
| 2026-11-04 | Korrektur zum Eintrag „Nachprüfung ersetzt die erste Abgabe“: Claude schrieb, das habe bei L65 einen zuvor richtigen Texteintrag verschlechtert. Das gilt nur für die unfertige erste Datei (`…_abgabe1.csv`); in der maßgeblichen zweiten Abgabe stand bei L65 und L88 „unbekannt“. Dieselbe falsche Aussage steht in `docs/iterationen.md` (Befund 3 der Nachprüfung) | Evaluator ([evaluation_iteration7.md](../reports/evaluation_iteration7.md)) | Nachtrag in `docs/iterationen.md`; der Kern bleibt: Bei allen 7 Abweichungen der Regelwirkungs-Lose übernahm die Nachprüfung das Feld |
| 2026-11-04 | Iteration 7: Claude schrieb im Prototyp, Stufe A sei „die sicherste“, obwohl die Regel-1b-Lose (Stufe A per Definition) nur 8/15 erreichten, und in der Auswertung „Quelle laut Prüfer“, obwohl die Quelle der Nachprüfung von Claude abgeleitet war; außerdem „Liste = Rohdaten“ als Tatsache für L16, L30, L32 (an TED nur L26 bestätigt) | Evaluator ([evaluation_iteration7.md](../reports/evaluation_iteration7.md)) | Formulierungen in den Skripten korrigiert und Berichte neu erzeugt; in `docs/iterationen.md` als Nachtrag richtiggestellt |
| 2026-11-05 | Iteration 8: Claude nannte die KI-Leser „blind“; sie hatten aber `CLAUDE.md` automatisch im Kontext (Satz: „Das Enddatum der Bekanntmachung ist manchmal schon das Höchstende“), und die Vorlage gab Regel 1b als Leseanweisung vor („kürzere feste Laufzeit gilt“, „Beginn + Dauer − 1 Tag“) | Evaluator (Gesamtprüfung) und Claude (Protokolle der Leser) | Im Abschluss offen genannt; Z2 mit beiden Zahlen (14/15, 11/15); Leser gelten als nicht unabhängig |
| 2026-11-05 | Iteration 8: Der Evaluator in Schritt 4a bestätigte 10 Übereinstimmungen mit demselben WebFetch-Hilfsmodell wie die Leser und kannte deren Werte; Z4 kann gemeinsame Auslassungen des Hilfsmodells nicht aufdecken | Evaluator (Schlussbemerkung) | Z4 als „schwach belegt“ berichtet |
| 2026-11-05 | Iteration 8: Claude formulierte die Kriterien ohne Antwort auf Lose ohne Zuschlag und fehlerhafte Los-Zuordnung (Regel 6); L69, L72, L81 fielen erst dem Evaluator auf | Evaluator (Gesamtprüfung) | als offene Grenzen ins Lab-Log; keine Regeländerung |
| 2026-11-05 | Iteration 9: Claude legte V4 mit zwei Schwellen (≥ 90 % und ≥ 85 %) ohne Verknüpfung und ohne Folge in „Was folgt“ fest; die erste Schwelle wurde verfehlt (87,1 %), die zweite knapp erfüllt (85,2 %) | Evaluator ([evaluation_iteration9.md](../reports/evaluation_iteration9.md)) | nachträglich „beide müssen gelten“ gewertet und als Lücke der Vorab-Festlegung ausgewiesen |
| 2026-11-05 | Iteration 9: Claude schrieb zunächst, bei Los N51 liege ein Lesefehler von Leser B vor; im XML steht `TenderResultCode: unpublished` mit `FieldsPrivacy` „geschäftliche Interessen“, also nicht veröffentlicht, nicht „kein Zuschlag“. Die Anweisung an die Leser deckte den Fall nicht ab, B befolgte sie wörtlich | Evaluator und Nachprüfung am XML | Aussage „Lesefehler“ zurückgenommen; V7 bleibt nach dem Kriterium verfehlt (1 von 100), Ursache in der Anweisung |
| 2026-11-05 | Iteration 9: Das Lauf-Skript für die Leser (`leser_lauf_iteration9.ps1`) wurde erst zusammen mit den Antworten committet, und die Abweichung vom Plan (Skriptläufe statt Sitzungen im Fenster) stand zunächst nicht in `docs/iterationen.md`; geprüft wurde nur der Eltern-Ordner auf eine `CLAUDE.md`, nicht `~/.claude` | Evaluator (Gesamtprüfung) | Nachtrag in `docs/iterationen.md`; V8 nur „teilweise“; die 230 Dateien der Pakete per SHA-256 als byte-gleich belegt |
| 2026-11-05 | Iteration 9: Claude legte Messaufbau und Kriterien fest, ohne dass die Stichprobe die beiden Fassungen der Liste trennt (nur 7 Regelwirkungs-Lose in 3 Bekanntmachungen, Gruppe R am Ende 2 statt 10 Lose); der Vergleichswert nutzt wie die Liste das Feld als Ende der Grundlaufzeit und ist teilweise zirkulär; die Basisregel „Feld EndDate“ (63/70) wurde erst nachträglich berechnet | Claude (vor dem Ziehen, Präzision 1) und Evaluator | V3 (66 gegen 65 von 70) als kaum aussagekräftig berichtet; „Fehlerarten behoben, Stichprobe bestätigt“ nicht behauptet |

## 6. Zeitaufwand

Untergrenze aus der Git-Historie (Sitzung = Commits mit höchstens 90 Minuten Abstand, plus 30 Minuten Vorlauf). Nicht enthalten: Lesen, Prüfen von Hand (Nutzer), Recherche, Vorbereitung des Vortrags. Handeinträge des Nutzers und des Kommilitonen fehlen noch.

| Iteration | Sitzungen | Commits | Stunden (Untergrenze) |
|---|---|---|---|
| 1 | 2 | 3 | 1.7 |
| 2 | 2 | 4 | 1.4 |
| 3 | 4 | 22 | 6.3 |
| 4 | 7 | 19 | 7.8 |
| 5 | 3 | 18 | 3.5 |
| 6 | 1 | 4 | 3.6 |
| 7 | 3 | 12 | 4.4 |
| 8 | 2 | 5 | 1.3 |
| 9 | 2 | 10 | 1.9 |
| **Summe** | 26 | 97 | **31.8** |

## 7. Reproduzierbarkeit und Quellen

- **Code.** Alle Schritte als Skripte in `src/`, Abhängigkeiten in `requirements.txt`. Aufrufe in `docs/reproduzierbarkeit.md`.
- **Seeds und Hashes.** Iteration 6: `src/prepare/stichprobe_iteration6.py`; Iteration 7: Seed 20261106, SHA-256 des Schlüssels `eade66c0…`; Iteration 8: Seed 20261108 für die Kontrolle, SHA-256 der Vorlage `5be683ad…`; Iteration 9: Seed 20261109, SHA-256 des Schlüssels `9dbf5c1a…`, der neuen Liste `5ec73364…`. Reihenfolge der Commits belegt, dass Regeln und Kriterien vor dem Ziehen feststanden.
- **Daten.** Rohdaten unverändert in `data/raw` (nicht im Git, Abruf per Skript `src/ted_download.py`); Datenlink für die Abgabe: _offen_.
- **Quellen.** TED Search API v3, eForms SDK, CRISP-DM; vollständig in `docs/quellen.md`. Lizenz der TED-Daten: _vor Abgabe zu prüfen_.
- **Annahmen.** Status und Nachweis aller Annahmen in `docs/annahmen.md` (A1 bis A20).
