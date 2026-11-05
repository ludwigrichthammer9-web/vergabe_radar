# Lab-Log: Vergabe-Radar

_Big Data Analytics, Leistungsnachweis B (Zweierteam). Chronologisch nach CRISP-DM-Zyklen. Zahlen und Quellen stehen in `docs/iterationen.md`, `docs/business.md`, `docs/phasen/` und `reports/`; hier steht die Erzählung mit den Entscheidungen. Fakten und Deutung sind getrennt gekennzeichnet._

_Erzeugt mit `src/report/lab_log.py` aus `docs/lab_log_vorlage.md`, `docs/zeitprotokoll.md` und `docs/ki_irrwege.md`._

## 0. Überblick

**Frage.** Mittelständler (Beispiel Gebäudereinigung) wollen sich früh auf Neuausschreibungen öffentlicher Aufträge vorbereiten. Lässt sich aus den Zuschlagsbekanntmachungen auf TED (Tenders Electronic Daily) vorhersagen, wann ein Vertrag neu ausgeschrieben wird, und wäre eine Liste auslaufender Verträge ein Produkt, das sich vom Markt abhebt?

**Antwort in drei Sätzen.**
1. Der Termin der Neuausschreibung lässt sich mit den TED-Daten nicht brauchbar vorhersagen: Die beste einfache Regel trifft das Fenster ±3 Monate in 28,8 % der 52 geprüften Fälle (Schwelle 60 %, naive Referenz 17,3 %).
2. Brauchbar ist eine Liste der Verträge mit dem Ende ihrer Laufzeit („laut Bekanntmachung“; 79,4 % der Lose abgedeckt, 94,3 % Übereinstimmung mit dem Vergleichswert zweier KI-Leser, Mensch 14/15; „die Liste ist korrekt“ ist nicht belegt), aber diese Art Liste gibt es schon kostenlos (Vergabeweiser) und günstig (AusschreibungsRadar).
3. Belegt ist nur ein Merkmalsunterschied (Ende je Los, Ende der Grundlaufzeit statt Höchstende; auf zwei Stichproben in rund 10 % der Lose), kein Qualitätsvorteil beim Lesen; Zahlungsbereitschaft zeigte sich in drei Gesprächen nur für Wettbewerbsdaten, die TED nur teilweise liefert, und Nachfrage bleibt ungeprüft.

**Verlauf.** Zehn Iterationen in vier Zyklen. Die Entscheidung am Ende jeder Iteration (weiter, zurück zu Phase X, Idee anpassen) war vorab an Schwellen gebunden, die vor dem Ergebnis committet wurden. Zyklus 4 entstand, weil der Dozent mehr Gewicht auf Business Understanding verlangte (Wie gehen Unternehmen vor? Wer ist Konkurrenz? Was ist der Mehrwert, was hebt uns ab?).

| Zyklus | Iterationen | Leitfrage | Ergebnis |
|---|---|---|---|
| 1 | 1 bis 4 | Lässt sich ein neuer Auftrag seinem Vorgänger zuordnen? | Nein, jede Variante verfehlte die Schwelle; Idee angepasst |
| 2 | 5 | Trägt eine einfache Terminprognose? | Nein (28,8 % statt 60 %); Idee angepasst auf eine Vertragsliste |
| 3 | 6 bis 9 | Wie genau ist die Vertragsliste? | Brauchbar, zuletzt 94,3 % Übereinstimmung mit zwei KI-Lesern; nicht als korrekt belegt |
| 4 | 10 und 10b (mit Paketen A, C, F, drei Gesprächen, Nebentest) | Was bietet der Markt schon, und hebt sich die Liste ab? | Kernprodukt gibt es kostenlos; belegt ist nur ein Merkmalsunterschied; Nachfrage offen |

**Grenzen vorweg.** Vor Iteration 10 gab es keinen Kundenkontakt (Entscheidung des Nutzers, 2026-10-29); in Iteration 10 folgten drei kurze Telefonate (Hinweise, keine Stichprobe). Ob jemand für eine solche Liste zahlt (A1, A15), ist weiter ungeprüft. Alle Messungen gelten für eForms-Bekanntmachungen (ab Herbst 2023) oberhalb der EU-Schwelle, Haupt-CPV 909, Deutschland.

## 1. Business Understanding im Überblick

_Kurzfassung für den Dozenten. Quellen und Einzelheiten: `docs/business.md` §6 bis §8, `reports/wettbewerbsbild_oberpfalz.md`. Angaben aus Web-Recherche eines KI-Agenten und eines KI-Gutachtens sind nur dort „geprüft“, wo `docs/business.md` es vermerkt._

**Wie gehen Betriebe heute vor (Fakten).**
- Zugang zu Ausschreibungen: kostenlos über den Bekanntmachungsservice oeffentlichevergabe.de, Suchprofile auf TED und IHK-Dienste; kostenpflichtig über Dienste wie subreport (84 bis 198 € pro Monat), DTAD (Angebot über den Vertrieb) oder evergabe.de (83 € pro Monat) (`docs/business.md` §8.1).
- Gespräche (n = 3, Hinweise): Ein Betrieb mit etwa 120 Beschäftigten zahlt knapp 1.500 € pro Jahr für DTAD; ein Betrieb mit 15 Beschäftigten zahlt für kein Portal und liest Webseiten und Lokalzeitung. Ob mitgeboten wird, entscheiden Entfernung, Personal und Kapazität; Vertragsenden bei anderen kennt keiner („Blackbox“, „Flurfunk“). Beide Betriebe kennen Vergabeweiser und AusschreibungsRadar nicht oder nur vom Hörensagen (`docs/business.md` §8.9).
- Die Vergabestelle (ein Landratsamt) verlängert „fast immer“, wenn eine Option im Vertrag steht, plant etwa 9 Monate vor Vertragsende und veröffentlicht meist 3 bis 4 Monate vor Start; sie vergibt Reinigung „sehr oft“ unterhalb der EU-Schwelle in Einzellosen (n = 1).
- Vergabe überwiegend nach Preis: 63 % aller Vergaben 2024 wurden nur nach Preis entschieden (Zusammenfassung des Vergabestatistik-Berichts, `docs/business.md` §8.1).

**Konkurrenz mit der Funktion „auslaufende Verträge“ (Fakten, Stand 2026-11-05).**

| Anbieter | Was er zeigt | Preis | Stand der Prüfung |
|---|---|---|---|
| Vergabeweiser | Verträge, die in 12 Monaten enden (1.005 in Gebäudereinigung), mit Zuschlagsempfänger, Angebotszahl, Optionen; ober- und unterschwellig; kostenlose API und Marktzahlen | kostenlos | Seite und API von uns geprüft und genutzt |
| AusschreibungsRadar | rund 26.000 Aufträge mit Ende in 1 bis 18 Monaten, „verlängerbar“ markiert, geschätzter Ausschreibungsmonat; Wettbewerber-Tracking in der Business-Stufe | 0 bis 149 € pro Monat | Seiten von uns geprüft; Nebentest mit 2 sicher zugeordneten Losen |
| aufträge.io | 43.373 Verträge mit Ende in 12 Monaten, Analyse bisheriger Gewinner | auf Anfrage | nur Recherche, nicht von uns geprüft |
| subreport | Ausschreibungsdienst (laufende Ausschreibungen); eine Funktion für auslaufende Verträge ist in unseren Quellen nicht belegt | 84 bis 198 € pro Monat | Preis laut Produktübersicht des Anbieters und Wettbewerbervergleich |
| DTAD | Ausschreibungsdienst; im Gespräch 1 kannte der Nutzer dort keine Liste auslaufender Verträge | Angebot über den Vertrieb (ein Betrieb: knapp 1.500 € pro Jahr) | nur Gespräch und Wettbewerberseiten |

Beide geprüften deutschen Anbieter schreiben selbst, dass der Auftraggeber entscheidet, ob und wann neu ausgeschrieben wird. Im Ausland gibt es ähnliche Dienste (Stotles, Tussell, GovSpend; `docs/business.md` §8.2).

**Mehrwert für Betriebe (Deutung, n = 3).** Der größere Betrieb sähe Nutzen in einem frühen Hinweis (Personal in der Zielregion früher suchen), würde aber eher für Wettbewerbsdaten zahlen (aktueller Auftragnehmer, alte Preise) als für Enddaten. Der kleine Betrieb hätte von 6 bis 12 Monaten Vorlauf nichts und will für Informationen nichts zahlen; sein Engpass ist die Bürokratie der Angebote. Die Zielgruppe „Mittelstand“ ist damit enger als gedacht: größere Betriebe, die für Kommunen und Behörden bieten.

**Positionierung (Deutung).** Die Liste der Vertragsenden als eigenes Produkt trägt nicht, weil sie kostenlos vorhanden ist. Wettbewerbsdaten (Gewinner, Wert, Bieterzahl) zeigt Vergabeweiser kostenlos; aus TED allein sind sie nur teilweise zu bekommen (Oberpfalz, 130 Lose: Auftragnehmer 99,2 %, Zuschlagswert über 1 € 47,7 %, Gesamtzahl der Angebote 60,8 %, alle drei zusammen 24,6 %). Nicht ausgeschlossen sind Nischenrollen: Datenqualität als Zulieferung, Beratung über einen Verband, Benchmark für Vergabestellen (die Vergabestelle nannte sinkende Bieterzahlen, n = 1). Keine dieser Rollen ist geprüft.

**Competitive Edge, ehrlich.**
- *Was bleibt (belegt, mit Einschränkung):* ein Merkmalsunterschied. Die Liste führt das Ende je Los und das Ende der Grundlaufzeit statt des Höchstendes. Auf zwei Stichproben (n = 70 und n = 160) weicht Vergabeweisers Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt; in 10b waren 11 von 15 dieser Fälle Höchstende oder Losebene. Dazu kommen ein offen dokumentiertes Prüfverfahren mit benannten Fehlerarten und der Backtest, dass ein fester Abstand den Termin nicht vorhersagt.
- *Was nicht bleibt:* Preis (Konkurrenz kostenlos), Daten (offen: TED, Bekanntmachungsservice CC0), Wettbewerbsbild (bei Vergabeweiser vorhanden), Abdeckung (die Liste enthält nur TED-Lose oberhalb der Schwelle, Vergabeweiser auch darunter), Terminprognose (Iteration 5).
- *Was wir ausdrücklich nicht behaupten:* dass die Liste genauer ist als Vergabeweiser oder dass Vergabeweiser falsch liest; dass es einen belegten Vorsprung oder Marktvorteil gibt; dass Betriebe die Liste nachfragen oder bezahlen. Ob das Ende der Grundlaufzeit für Betriebe nützlicher ist als das Höchstende, ist offen; die Vergabestelle sagt, es werde fast immer verlängert.

## 2. Zyklus 1: Zuordnung zum Vorgänger (Iteration 1 bis 4)

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

## 3. Zyklus 2: Terminprognose (Iteration 5)

### Iteration 5 (2026-10-30 bis 11-04): Vertragsliste und Backtest
- **Business Understanding (geschärft).** Prognoseziel: Veröffentlichungstermin der Neuausschreibung. Regel R1 = Höchstende − 6 Monate; Baseline R0 = Ende der Grundlaufzeit − 6 Monate. Treffer = Fenster ±3 Monate. Schwelle 60 %, festgelegt vor jeder Berechnung (`docs/business.md` §7.1).
- **Data Preparation.** Zuschlagstabelle je Los (`src/prepare/vertragsliste.py`): Ende der Grundlaufzeit, Höchstende (aus Datum, Höchstlaufzeit, BT-36 und Anzahl × Länge im Freitext), Herkunft. 9.915 Lose; Laufzeit bei 79,7 % bestimmbar. Leakage vermieden: nur Wissen zum Zeitpunkt des Vorgänger-Zuschlags.
- **Modeling/Evaluation.** Backtest auf 52 von Hand bestätigten Paaren (Zweitprüfung 61/67 = 91,0 %, mit KI-Hilfe, deshalb nicht als unabhängig gewertet).
- **Fakten.** R1 28,8 % (Wilson 18,3–42,3), R0 17,3 %. 20 Neuausschreibungen kamen mehr als 3 Monate früher, 17 später. Robust gegen Ausreißer, Vorlauf und Gewichtung.
- **Deutung.** Der Termin ist zweigipflig verteilt; ein fester Abstand trägt nicht.
- **Entscheidung (Idee anpassen).** Keine Terminprognose. Produktkern ist die Vertragsliste mit Enddaten.

## 4. Zyklus 3: Qualität der Vertragsliste (Iteration 6 bis 9)

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
- **Entscheidung.** Weiter, Projektabschluss, eingeschränkt formuliert. Die Fassung der Iteration 9 wird der Prototyp, das Höchstende bleibt Hinweis. V4, V7 und V8 werden offen als verfehlt bzw. teilweise berichtet; nicht zulässig ist „V1 bis V8 erfüllt“. Keine weitere Iteration (später durch Zyklus 4 aufgehoben, siehe unten).

## 5. Zyklus 4: Business Understanding und Wettbewerb (Iteration 10 und 10b)

_Anlass (2026-11-05, nach Iteration 9): Der Dozent verlangt mehr Gewicht auf Business Understanding. Die Recherche dazu zeigte, dass die Sichtung der Wettbewerber, im Projektplan früh vorgesehen (G1.1), nie erfolgt war: Eine Suche vom 2026-10-24 hatte keinen deutschen Dienst für auslaufende Verträge gefunden (Fehler, siehe KI-Irrwege). Abweichend von „keine weitere Iteration“ (Iteration 8 und 9) hat der Nutzer deshalb am 2026-11-05 einen Rücksprung zu Phase 1 beschlossen. Iteration 9 blieb unverändert; ihre Stichprobe und ihr Vergleichswert dienten als fester Maßstab. Details: `docs/iterationen.md` (Iteration 10, 10b, Pakete A, C, F)._

### Iteration 10 (2026-11-05): Wettbewerber gegen eigene Liste
**Business Understanding.**
- **Fakten.** Recherche (KI-Agent plus KI-Gutachten aus BWL-Sicht, einzelne Seiten von Claude nachgelesen): Vergabeweiser bietet eine kostenlose Liste auslaufender Verträge samt API, AusschreibungsRadar eine günstige (Tabelle in Abschnitt 1). **A2 („es gibt keinen deutschen Dienst für auslaufende Verträge“) ist widerlegt.** Das Gutachten hielt das Kernprodukt „Liste“ für nicht tragfähig und empfahl ein Wettbewerbsbild als stärkste Richtung (`docs/business.md` §8.4, §8.5).
- **Gespräche (W5).** Leitfaden vorab festgelegt (`docs/business.md` §8.8). Der Nutzer rief neunmal an und erreichte drei Stellen: zwei Reinigungsbetriebe und eine Vergabestelle. Notizen ohne Namen von Personen (`docs/business.md` §8.9). Zahlungsbereitschaft zeigte sich nur für Wettbewerbsdaten; die Vergabestelle bestätigt, dass das Vertragsende kein Neuausschreibungstermin ist (Verlängerung ist der Normalfall). n = 3, Hinweise, keine Belege.

**Data Understanding.**
- Die API von Vergabeweiser (OpenAPI-Beschreibung und Antworten unverändert in `data/raw/vergabeweiser_20261105/`, ohne Schlüssel 60 Abfragen pro Stunde) liefert das Vertragsende je Verfahren (`ends_on`, „laut Bekanntmachung, ohne Verlängerungen“), nicht je Los.
- Zuordnung eines Loses zu einem Vergabeweiser-Eintrag per Skript ohne Handentscheid: Verweis der Zuschlagsbekanntmachung auf die Auftragsbekanntmachung, dann Verfahrenskennung, dann die eigene Kennung (erste 8 Zeichen der `notice-id`).
- Wettbewerbsbild aus TED (Paket A, 130 Oberpfalz-Lose) und Ursachen der 33 Lose ohne Ende (Paket C, siehe unten).

**Hypothese** _(vorab festgelegt 2026-11-05, vor dem Abruf)_. „Beim Ende der Grundlaufzeit stimmt Vergabeweiser auf den 70 Zufallslosen der Iteration 9 seltener mit dem Vergleichswert der Iteration 9 überein als die Liste (66/70).“

**Kriterien vorab (Auszug).** W1: Vorsprung der Liste (Treffer Liste − Treffer Vergabeweiser auf den gemeinsamen Losen) ≥ 5 Lose = Vorteil, 1 bis 4 = kein gesicherter Vorteil, ≤ 0 = kein Vorteil; beurteilbar nur bei ≥ 40 gemeinsamen Losen. W2 bis W5 und W7 beschreibend (Abdeckung, Ursachen der Fehltreffer, Abdeckung unterhalb der EU-Schwelle, Gespräche, Nebentest AusschreibungsRadar). W6: Verfahren (Kriterien und Skript vor dem Abruf committet, Abweichungen offen).

**Fakten (Evaluation).** Quellen: `reports/vergleich_iteration10.md`, `reports/evaluation_iteration10.md`, `reports/nebentest_ausschreibungsradar.md`.
- **W1:** Liste 66/70, Vergabeweiser 58/70, Vorsprung +8 (Schwelle ≥ 5), exakter Test p = 0,0078; formal erfüllt. Ursachen der 8 Fälle (Evaluator): Losebene 4, Höchstende statt Grundlaufzeit 2, fehlender Wert 1, 2 Tage Abweichung 1. Die Basisregel „Feld EndDate“ erreicht 63/70; Vergabeweiser verhält sich laut Evaluator wie diese Regel plus Verfahrensebene. Zählt Vergabeweisers Verfahrensdatum als richtig, wenn es dem Ende irgendeines Loses entspricht, sinkt der Vorsprung auf +4 (kein gesicherter Vorteil).
- **W2:** Vergabeweiser hat zu 70 von 70 Losen einen Eintrag (zirkulär: beide Quellen stammen aus demselben Bekanntmachungsservice). **W4** (Abdeckung unterhalb der EU-Schwelle) ist nicht aussagekräftig, weil die API nur die 50 frühesten Verträge liefert.
- **W7 (Nebentest AusschreibungsRadar,** Seed 20261111, 15 Lose, ohne API, 52 Seitenabrufe): nur 2 von 15 Losen sicher zugeordnet, beide gleich dem Vergleichswert und der Liste. Für eine Aussage zur Genauigkeit reicht das nicht.

**Deutung (Evaluator und Projekt).** 6 von 8 Fällen sind Granularitäts- oder Begriffsunterschiede (Los gegen Verfahren, Höchstende gegen Grundlaufzeit), reine Lesefehler von Vergabeweiser höchstens 1 bis 2. Maßstab und Befund fallen teilweise zusammen: Der Vergleichswert ist je Los definiert, die API liefert je Verfahren.

**Abweichungen von der Vorab-Planung (offen).** Zuordnungsweg 2 wurde nach dem Trockenlauf ergänzt (vor jedem Abruf der Stichprobe); das Abruf-Skript wurde nach einem DNS-Fehler im ersten Lauf angepasst (Zuordnung und Auswertung unverändert); der Nebentest W7 wurde nach Beginn des Abrufs aufgenommen (ohne Schwelle, Ziehung vor dem Nachsehen). Entwicklungstest: Beim Test der Zuordnung wurde ein Eintrag abgerufen, der ein Z-Los enthält; deshalb läuft der Vergleich nur per Skript.

### Iteration 10b (2026-11-05): größere Stichprobe
**Anlass und Entscheidung.** Der Evaluator nannte den Vorsprung +8 auf 70 Losen überwiegend Verfahrens- gegen Losebene und forderte eine zweite, größere Stichprobe (mindestens 150 Lose). Der Nutzer beschloss sie am selben Tag; die Entscheidung zu Iteration 10 blieb bis zur Auswertung offen.

**Hypothese** _(vorab)_. „Auf einer neuen Stichprobe von mindestens 150 Losen trifft die Liste das Ende der Grundlaufzeit häufiger als Vergabeweiser, und der Unterschied reicht über die Granularität (Verfahren statt Los) hinaus.“

**Vorgehen und Kriterien vorab.** 160 Lose (Seed 20261112; Lose mit Zuschlag und Listenende, höchstens 2 je Bekanntmachung; alle Bekanntmachungen früherer Stichproben ausgeschlossen). Nur die Lose, in denen Liste und Vergabeweiser mehr als einen Tag auseinanderliegen oder eine Seite kein Datum hat („diskordant“), lasen zwei KI-Leser (Opus, Sonnet) ohne Angabe der Quelle nach der neutralen Definition aus Iteration 9. W8a: Vorsprung ≥ 10 % der Stichprobe (≥ 16 Lose) und McNemar p < 0,05. W8b: wie W8a, aber Vergabeweiser gilt als richtig, wenn sein Datum dem Ende irgendeines Loses desselben Verfahrens entspricht (≥ 8 Lose, p < 0,05). W9: Ursachenklassen (beschreibend).

**Fakten (Evaluation).** Quellen: `reports/vergleich_iteration10b.md`, `reports/evaluation_iteration10b.md`.
- Vergabeweiser hat zu allen 160 Losen einen Eintrag; 145 Lose sind gleich, **15 diskordant**. Die beiden Leser stimmen bei 15/15 überein; nach ihrem Vergleichswert liegt die Liste bei 15/15 richtig, Vergabeweiser bei 0/15.
- **W8a** (≥ 16 Lose): +15, p = 0,0001. **Formal verfehlt und rechnerisch unerreichbar**, weil nur 15 Lose diskordant waren (Fehler der Vorab-Schwelle, die aus der Diskordanzrate der Iteration 10 übernommen wurde; siehe KI-Irrwege). **W8b** (≥ 8 Lose): +10, p = 0,0020, erfüllt.
- **Einordnung der 15 durch den Evaluator** (je Los am Rohtext): Höchstende statt Grundlaufzeit 7 (eine einzige Textvorlage), Losebene 4, Zuordnungsfehler der Pipeline 1 (M54, gehört nicht zu „Vergabeweiser liest falsch“), Abweichung mit offener Ursache 2 (M3, M22), mehrdeutig 1 (M49). Zählt das Höchstende für Vergabeweiser als richtig, bleiben 3 : 0, p = 0,25.
- **Beide Stichproben zusammen:** nur die Liste richtig bei 23 von 230 Losen = 10,0 % (Wilson etwa 6,8–14,6 %).
- **Übereinstimmende Lose:** Zehn systematisch gewählte (nicht zufällig gezogen) wurden geprüft; bei einem (M59, Textmuster „läuft vom … bis … und verlängert sich um 12 weitere Monate“) liegen Liste und Vergabeweiser beide falsch. Ein Los in zehn ist ein Hinweis, keine Rate.

**Deutung.** Der Vorsprung der Liste ist ein **Merkmalsunterschied** (Ende je Los, Ende der Grundlaufzeit statt Höchstende), kein belegter Qualitätsvorteil beim Lesen: Liste und Vergabeweiser nutzen dasselbe TED-Feld, gemeinsame Fehler bleiben unsichtbar, und die Leser stammen aus derselben Modellfamilie wie die Regeln. 15 von 15 Übereinstimmungen der Leser sind kein Zeichen von Unabhängigkeit.

### Pakete A, C und F (Nachträge zu Iteration 10, Entscheidung des Nutzers 2026-11-05)
Ziel: Business Understanding vertiefen, ohne die Iterationen 1 bis 10 zu ändern; jedes Paket schreibt neue Dateien.
- **A, Wettbewerbsbild aus TED** (`reports/wettbewerbsbild_oberpfalz.md`): Für die 130 Oberpfalz-Lose liefert das TED-XML den Auftragnehmer bei 99,2 % der Lose, einen Zuschlagswert über 1 € bei 47,7 % (36,2 % Platzhalter), die Gesamtzahl der Angebote bei 60,8 % und alle drei Felder zusammen bei 24,6 %. Handabgleich von 5 Losen (Seed 20261113) gegen die Bekanntmachung: 5 von 5. **Deutung:** Ein Wettbewerbsbild aus TED allein ist nur zu etwa einem Viertel der Lose vollständig; Vergabeweiser zeigt Gewinner, Angebotszahl und Zuschlagssummen kostenlos.
- **C, Ursachen der Lücken und Fehlertyp** (`reports/stufe_f_ursachen.md`): Die 33 Lose ohne Ende (25,4 % der Oberpfalz-Lose) haben alle keine Laufzeitfelder im XML; 18 ohne Laufzeit im Text, 14 mit Dauer oder Datum nur im Freitext (höchstens 10 mit einer Zusatzregel lesbar), 1 keine Gebäudereinigung. Außerdem fand die Suche den Fehlertyp „Dauerfeld enthält die Option schon“ (z. B. Interimsvergabe „4 Monate + 6 Monate Option = 10 Monate“): **12 Lose in 5 Bekanntmachungen, 0,13 % der 9.325 Lose**, alle bei der Herkunft `beginn_plus_dauer`. Zwei Fälle bestätigte Claude am Rohtext, die übrigen sind eine einzelne KI-Lesung. Ein erster Nachtrag hatte „nur dieser Fall“ geschrieben; das war falsch (KI-Irrwege).
- **F, Optionsanalyse** (`reports/optionsanalyse.md`): An den 52 Backtest-Paaren lag die Neuausschreibung bei belegter Option (n = 24) in 70,8 % zwischen dem Ende der Grundlaufzeit und dem Höchstende (Wilson 50,8–85,1). **Hinweis, kein Beleg:** Die Aussage der Vergabestelle („fast immer verlängert“) ist damit nicht prüfbar.
- Ein Paket B (Schnittstelle von oeffentlichevergabe.de) wurde nicht umgesetzt, weil die Dokumentation nur im Browser lesbar war.

### Entscheidung (2026-11-05, Nutzer): Weiter, Projektabschluss, eingeschränkt formuliert
- **Begründung.** W1 ist formal erfüllt, aber überwiegend Los- und Definitionsunterschied; W8a ist formal verfehlt wegen eines Fehlers der Vorab-Schwelle (+15 von höchstens 15), W8b ist erfüllt. Nach der Vorab-Regel gilt „kein belegter Vorteil im definierten Maß“. Befund: Merkmalsunterschied, kein belegter Qualitätsvorteil, Nachfrage offen.
- **Abweichung von der Vorab-Folge (offen begründet).** Die Folge „W8a verfehlt → die Aussage ‚kein Vorteil gegenüber Vergabeweiser‘ gilt weiter“ wird nicht übernommen, weil sie der gemessenen Richtung widerspricht und die Schwelle unerreichbar war; für „W8a verfehlt und W8b erfüllt“ gab es keine Regel. Die Aussage „kein Vorteil“ wird nicht als Gleichheit gelesen, und „die Liste ist genauer“ wird ebenso wenig behauptet.
- **Geschäftlich.** „Liste als eigenes Produkt nicht tragfähig“ (`docs/business.md` §8.4) bleibt bestehen; A2 bleibt widerlegt, A1, A3 und A15 bleiben ungeprüft.
- **Grenzen des Zyklus.** Leser und Regeln aus derselben Modellfamilie, keine Menschenprüfung der 15 diskordanten Lose; Auswahl nur aus Losen mit Listenende (5.754 von 9.325); Gespräche n = 3; nur Lose oberhalb der EU-Schwelle; das Protokoll der Leserläufe 10b liegt außerhalb des Repos.

## 6. Was wir empfehlen und was nicht

- **Empfehlung.** Die Vertragsliste „Ende der Laufzeit laut Bekanntmachung“ ist als Ausgangspunkt nutzbar; vor jeder Entscheidung die verlinkte Bekanntmachung lesen. Als eigenes Produkt empfehlen wir sie **nicht**, weil es das Kernprodukt kostenlos (Vergabeweiser) und günstig (AusschreibungsRadar) gibt. Weiterverfolgen ließe sich nur eine Nische (z. B. Wettbewerbsdaten, Datenqualität als Zulieferung, Vergabestellen), nach Gesprächen mit mehr Beteiligten.
- **Zulässige Aussagen.** „Zu 94,3 % identisch mit dem Vergleichswert zweier KI-Leser; an 15 Losen bestätigt ein Mensch (14/15); Höchstende nur Hinweis.“ Und: „Auf zwei Stichproben (n = 70 und n = 160) weicht Vergabeweisers Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt; in 10b waren 11 von 15 dieser Fälle Höchstende oder Losebene.“
- **Nicht belegt.** Eine Terminprognose; „die Liste ist korrekt“; „Fehlerarten behoben und bestätigt“; „V1 bis V8 erfüllt“; ein Qualitätsvorteil gegenüber Vergabeweiser (und ebenso Gleichheit); Nachfrage, Zahlungsbereitschaft und Marktvorteil (A1, A15); Abdeckung unterhalb der EU-Schwelle (A3).
- **Offene Grenzen der Liste.**
  - Das Höchstende ist oft zu hoch (laut Evaluator 7 von 11 Z-Fällen Überschätzung) und nur ein Hinweis; Schuljahres-Verträge sind nicht tagesgenau; Ergebnisse „nicht veröffentlicht“ (`unpublished`) werden nicht erkannt.
  - **Fehlertyp „Dauerfeld enthält die Option“:** 12 Lose in 5 Bekanntmachungen (0,13 %); Ursache nur durch Lesen des Codes vermutet (Regel 1b greift in `laufzeit()` nur bei der Herkunft `enddatum`), nicht getestet. 6 weitere Lose in 4 Bekanntmachungen sind unklar.
  - **Textmuster:** „läuft vom … bis … und verlängert sich um …“ (M59) und „gilt bis … ohne ‚zunächst‘“ (12853-2024, Los 3) werden nicht gefangen; Häufigkeit unbekannt.
  - **Zuordnungsfehler** der Pipeline beim Vergleich (M54: Eintrag einer anderen Ausschreibung zugeordnet); die Zuordnung wurde nicht für alle 160 Lose von Hand geprüft.
  - **Auswahl:** Die Stichprobe 10b enthält nur Lose mit Listenende; Lose ohne Listenende (etwa ein Fünftel) gehen nicht ein.
  - **Keine Menschenprüfung der 15 diskordanten Lose;** die übrigen Fehlerarten aus Iteration 8 (Lose ohne Zuschlag, Übertragung von Einzelwerten, Monatsnamen, „um N Jahre“, „N Jahre mit Option“) sind in der Fassung 9 behoben, aber nicht bestätigt; eine zweite Modellfamilie fehlt.
  - **Stand bei Vergabeweiser:** Ob es den Stand der Ausschreibung oder des Zuschlags zeigt, ist ungeklärt (M3, M22, M49).

## 7. KI-Irrwege und ihre Prüfung

Die KI (Claude Code) hat Hypothesen, Regeln, Stichproben und Auswertungen mitgebaut. Die Fehler wurden vom Nutzer, vom Evaluator (eigener Subagent, nur Lesezugriff) oder von Claude selbst gefunden. Für Zyklus 4 sind die wichtigsten: die unterlassene Sichtung der Wettbewerber (Zeile vom 2026-11-05 zu Business Understanding), der Fehlertyp „Dauerfeld enthält die Option“ mit der falschen Aussage „nur dieser Fall“, die unerreichbare Schwelle W8a und der Zuordnungsfehler bei M54.

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
| 2026-11-05 | Business Understanding: Claude fand am 2026-10-24 in zwei Suchen keinen deutschen Dienst für auslaufende Verträge und schrieb das in `docs/business.md` §6; die Sichtung der Wettbewerber (Projektplan G1.1) blieb danach offen. Tatsächlich bieten Vergabeweiser (kostenlos, 1.005 Reinigungsverträge) und AusschreibungsRadar genau diese Funktion, mit Daten auch unterhalb der EU-Schwelle | Recherche-Agent, beauftragt nach dem Hinweis des Dozenten auf mehr Business Understanding; beide Seiten von Claude nachgelesen | A2 widerlegt; `docs/business.md` §8; die Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos schon gibt; im Lab-Log offen genannt |
| 2026-11-05 | Liste, Regel `beginn_plus_dauer`: Das Dauerfeld wird als Grundlaufzeit gelesen, auch wenn es die Option schon enthält (Beispiele: 527230-2026 „4 Monate + 6 Monate Option = 10 Monate“; 533946-2026 „2 Jahre Festlaufzeit + 3×1 Jahr Option“, Dauerfeld 5 Jahre, Liste Ende 30.09.2031 statt 30.09.2028). Claude schrieb im ersten Nachtrag, nur 527230-2026 sei betroffen (grobe Textprüfung, 3 Treffer); Paket C fand 12 Lose in 5 Bekanntmachungen | Nutzer (Hinweis auf 527230-2026), dann Paket C (Agent, Prüfung von 407 Losen mit Textherkunft), zwei Fälle von Claude am Rohtext bestätigt | Fehlerart offen im Lab-Log (0,13 % der Liste, 12 von 9.325 Lose); Liste (Fassung 9) bleibt eingefroren, Messungen unverändert; Aussage „nur dieser Fall“ im Nachtrag in `docs/iterationen.md` richtiggestellt |
| 2026-11-05 | Iteration 10b: Claude legte die Schwelle W8a (Vorsprung ≥ 16 Lose = 10 % von 160) fest, indem er die Diskordanzrate der Iteration 10 (12/70 = 17 %) übernahm; tatsächlich waren nur 15 von 160 Losen diskordant, die Schwelle war damit rechnerisch unerreichbar. Außerdem gab es keine Folgeregel für „W8a verfehlt, W8b erfüllt“, und das Skript gibt den Satz „Abweichungen von der Vorab-Festlegung: keine“ fest aus | Claude nach dem Abruf (vor den Leserantworten) und Evaluator ([evaluation_iteration10b.md](../reports/evaluation_iteration10b.md)) | Kriterium nicht nachträglich geändert; im Ergebnis „formal verfehlt, rechnerisch unerreichbar“ mit gemessener Differenz (+15, p = 0,0001) ausgewiesen; Folge der Vorab-Regel nicht als Gleichheit gelesen |
| 2026-11-05 | Iteration 10b: Die Zuordnung zu Vergabeweiser über die Verfahrenskennung (Weg 2) ordnete bei M54 (346782-2025) einen fremden Eintrag zu (Vreden statt Lengerich), und M7 wurde durch die Reihenfolge der Ursachenklassen als „Losebene“ statt „Höchstende“ geführt (begünstigt Vergabeweiser in W8b) | Evaluator (Gesamtprüfung) | M54 gehört nicht zu „Vergabeweiser liest falsch“; W8b mit M7 als Höchstende wäre +11 statt +10; als Grenzen im Ergebnis genannt |

## 8. Zeitaufwand

Untergrenze aus der Git-Historie (Sitzung = Commits mit höchstens 90 Minuten Abstand, plus 30 Minuten Vorlauf; Iteration 10 enthält 10b und die Pakete A, C, F, weil der Tag `iteration-10` am Ende liegt). Nicht enthalten: Lesen, Prüfen von Hand, Recherche, Vorbereitung des Vortrags.

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
| 10 | 3 | 21 | 4.4 |
| **Summe** | 29 | 118 | **36.2** |

**Zyklus 4 im Einzelnen.**
- Git-Untergrenze: 3 Sitzungen am 2026-11-05 mit 4,4 Stunden (15:55 bis 18:00 Anlegen, Abruf, Nebentest, Auswertung W1 bis W4, Evaluator, Pakete F und A, Übergabe; 20:22 Paket C; 22:01 bis 22:48 Ende des Abrufs 10b, Leser, Auswertung, Evaluator, Abschluss).
- Wartezeit des gedrosselten Abrufs (Rechnung, nicht gemessen): Iteration 10 etwa 75 Minuten laut Plan; 10b 160 Abfragen im Abstand von 61 Sekunden, rund 2,7 Stunden. In dieser Zeit lief die Arbeit an den Paketen weiter.
- **Handeinträge.** Nutzer: Gespräche der Iteration 10 (Vorbereitung, neun Anrufe, Abtippen) 105 Minuten (1,75 Stunden, Angabe des Nutzers). Kommilitone: Lesen von 15 Losen in Iteration 9, Stunden **offen**. Weitere Handarbeit des Nutzers (Zweitprüfungen und Handprüfungen der Iterationen 5 bis 7, Lesen der Berichte, Vortrag) ist nicht erfasst; die Summe oben bleibt eine Untergrenze.

## 9. Reproduzierbarkeit und Quellen

- **Code.** Alle Schritte als Skripte in `src/`, Abhängigkeiten in `requirements.txt`. Aufrufe in `docs/reproduzierbarkeit.md`.
- **Seeds und Hashes.** Iteration 6: `src/prepare/stichprobe_iteration6.py`; Iteration 7: Seed 20261106, SHA-256 des Schlüssels `eade66c0…`; Iteration 8: Seed 20261108 für die Kontrolle, SHA-256 der Vorlage `5be683ad…`; Iteration 9: Seed 20261109, SHA-256 des Schlüssels `9dbf5c1a…`, der neuen Liste `5ec73364…`.
  - **Iteration 10:** kein eigener Seed; die 70 Z-Lose der Iteration 9 (Schlüssel `9dbf5c1a…`), Skript `src/prepare/vergleich_iteration10.py`, Kriterien und Skript vor dem Abruf committet (`81a3b90`). Nebentest: Seed 20261111, Ziehung vor dem Nachsehen (`2002ac8`), Auswertung `0eeab99`.
  - **Iteration 10b:** Seed 20261112, SHA-256 des Schlüssels `2cd00206…`, `src/prepare/stichprobe_iteration10b.py`; Hypothese, Kriterien und Seed vor dem Ziehen (`4f50436`), Ziehung (`9d63c59`), Abrufskript vor dem Abruf (`49bb198`), Abruf (`64a23e3`), Paket für die Leser vor den Antworten (`6b7e8d8`), Antworten unverändert (`69917ff`), Auswertung und Evaluator (`f6583cc`), Abschluss (`0419609`).
  - **Pakete:** Paket A Seeds 20261113 (Handabgleich von 5 Losen) und 20261114 (3 Beispiel-Lose), beide im Skript `src/prepare/wettbewerbsbild_oberpfalz.py` vorab festgelegt (`ea5ebfb`); Paket F `d6e2335`; Paket C `79fd0df`.
  - Die Reihenfolge der Commits belegt, dass Regeln und Kriterien vor dem Ziehen feststanden; Ausnahmen stehen in Abschnitt 5.
- **Daten.** Rohdaten unverändert in `data/raw` (nicht im Git, Abruf per Skript `src/ted_download.py`); Datenlink für die Abgabe: _offen_.
- **Quellen.** Vollständig in `docs/quellen.md`. TED Search API v3 (Quellenangabe; **Lizenz der TED-Daten: offen, vor Abgabe zu prüfen**), eForms SDK, CRISP-DM. Neu in Zyklus 4: **Vergabeweiser** (API und Seiten, CC BY 4.0, Nennung „Vergabeweiser“); **AusschreibungsRadar** (einzelne Seiten, `robots.txt` beachtet, keine Massenabrufe); **Bekanntmachungsservice oeffentlichevergabe.de** der BeschA (Rohdaten CC0); Web-Quellen zu Preisen und Branche mit URL in `docs/business.md` §8.
- **Annahmen.** Status und Nachweis aller Annahmen in `docs/annahmen.md` (A1 bis A20).
