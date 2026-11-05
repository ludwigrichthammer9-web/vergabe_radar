# Lab-Log: Vergabe-Radar

_Big Data Analytics, Leistungsnachweis B (Zweierteam). Chronologisch nach CRISP-DM-Zyklen. Zahlen und Quellen stehen in `docs/iterationen.md`, `docs/business.md`, `docs/phasen/` und `reports/`; hier steht die Erzählung mit den Entscheidungen. Fakten und Deutung sind getrennt gekennzeichnet. Hauptteil: Abschnitte 0 bis 9; Details im Anhang A (Hashes und Commits) und B (alle KI-Irrwege)._

_Erzeugt mit `src/report/lab_log.py` aus `docs/lab_log_vorlage.md`, `docs/zeitprotokoll.md` und `docs/ki_irrwege.md`._

## 0. Überblick

**Frage.** Mittelständler (Beispiel Gebäudereinigung) wollen sich früh auf Neuausschreibungen öffentlicher Aufträge vorbereiten. Lässt sich aus den Zuschlagsbekanntmachungen auf TED (Tenders Electronic Daily) vorhersagen, wann ein Vertrag neu ausgeschrieben wird, und wäre eine Liste auslaufender Verträge ein Produkt, das sich vom Markt abhebt?

**Antwort in drei Sätzen.**
1. Der Termin der Neuausschreibung lässt sich mit den TED-Daten nicht brauchbar vorhersagen: Die beste einfache Regel trifft das Fenster ±3 Monate in 28,8 % der 52 geprüften Fälle (Schwelle 60 %, naive Referenz 17,3 %).
2. Brauchbar ist eine Liste der Verträge mit dem Ende ihrer Laufzeit („laut Bekanntmachung“): Rund 73 % aller Lose haben ein Ende der Grundlaufzeit (6.803 von 9.325; im letzten Jahr 79,4 %, Erklärung in Abschnitt 4), und 94,3 % stimmen mit dem Vergleichswert zweier KI-Leser überein (Mensch 14/15; „die Liste ist korrekt“ ist nicht belegt). Diese Art Liste gibt es aber schon kostenlos (Vergabeweiser) und günstig (AusschreibungsRadar).
3. Belegt ist nur ein Merkmalsunterschied (Ende je Los, Ende der Grundlaufzeit statt Höchstende; auf zwei Stichproben in rund 10 % der Lose), kein Qualitätsvorteil beim Lesen. Zahlungsbereitschaft zeigte sich in drei Gesprächen nur für Wettbewerbsdaten, die TED nur teilweise liefert; Nachfrage bleibt ungeprüft.

**Verlauf.** Zehn Iterationen in vier Zyklen. Die Entscheidung am Ende jeder Iteration (weiter, zurück zu Phase X, Idee anpassen) war vorab an Schwellen gebunden, die vor dem Ergebnis committet wurden. Zyklus 4 entstand, weil der Dozent mehr Gewicht auf Business Understanding verlangte.

| Zyklus | Iterationen | Leitfrage | Ergebnis |
|---|---|---|---|
| 1 | 1 bis 4 | Lässt sich ein neuer Auftrag seinem Vorgänger zuordnen? | Nein, jede Variante verfehlte die Schwelle; Idee angepasst |
| 2 | 5 | Trägt eine einfache Terminprognose? | Nein (28,8 % statt 60 %); Idee angepasst auf eine Vertragsliste |
| 3 | 6 bis 9 | Wie genau ist die Vertragsliste? | Brauchbar, zuletzt 94,3 % Übereinstimmung mit zwei KI-Lesern; nicht als korrekt belegt |
| 4 | 10 und 10b (mit Paketen A, C, F, drei Gesprächen, Nebentest) | Was bietet der Markt schon, und hebt sich die Liste ab? | Kernprodukt gibt es kostenlos; belegt ist nur ein Merkmalsunterschied; Nachfrage offen |

**Grenzen vorweg.** Vor Iteration 10 gab es keinen Kundenkontakt (Entscheidung des Nutzers, 2026-10-29); in Iteration 10 folgten drei kurze Telefonate (Hinweise, keine Stichprobe). Ob jemand für eine solche Liste zahlt (A1, A15), ist weiter ungeprüft. Alle Messungen gelten für eForms-Bekanntmachungen (ab Herbst 2023) oberhalb der EU-Schwelle, Haupt-CPV 909, Deutschland.

**Kleines Glossar** (Kennungen erscheinen in den Tabellen wieder).

| Begriff | Bedeutung |
|---|---|
| Los | Teil einer Ausschreibung mit eigenem Zuschlag; Einheit der Liste |
| Ende der Grundlaufzeit / Höchstende | Ende der ersten festen Laufzeit / Ende einschließlich aller Verlängerungsoptionen |
| Vergleichswert | Ende der Grundlaufzeit nach einer vorab committeten, neutralen Definition, gelesen von zwei KI-Lesern |
| Kriterien K, V, W, X, Y, Z | Schwellen, je Iteration neu vergeben und vor dem Ergebnis festgelegt; gelten nur in der genannten Iteration (V1 bis V3 Iteration 3, W2 bis W4 Iteration 4, X Iteration 5, Y Iteration 6 und 7, Z0 bis Z4 Iteration 8, V1 bis V8 Iteration 9, W1 bis W7 Iteration 10, W8a, W8b, W9 Iteration 10b) |
| L, N, M mit Zahl | Nummer eines Loses in der Stichprobe (L Iteration 6 bis 8, N Iteration 9, M Iteration 10b), z. B. M54 |
| Regeln 1a, 1b, 6 bis 10 | Leseregeln der Liste; 1b: „das Enddatum der Bekanntmachung ist schon das Höchstende“; 6 bis 10 aus Iteration 9 |
| Stufe A bis F | Güteklasse je Listeneintrag: A Ende aus Text gelesen oder Höchstende unauffällig, B Höchstende aus Anzahl × Länge, C Höchstende ohne Angabe, D unbestimmbar, E nur geschätztes Ende, F kein Ende |
| diskordant | Liste und Vergabeweiser weichen um mehr als einen Tag ab oder eine Seite hat kein Datum |
| Wilson | 95-%-Konfidenzintervall für einen Anteil |

## 1. Business Understanding im Überblick

_Kurzfassung für den Dozenten. Quellen: `docs/business.md` §6 bis §8, `reports/wettbewerbsbild_oberpfalz.md`. Angaben aus Web-Recherche eines KI-Agenten und eines KI-Gutachtens sind nur dort „geprüft“, wo `docs/business.md` es vermerkt._

**Wie gehen Betriebe heute vor (Fakten).**
- Zugang zu Ausschreibungen: kostenlos über den Bekanntmachungsservice oeffentlichevergabe.de, Suchprofile auf TED und IHK-Dienste; kostenpflichtig über Dienste wie subreport (84 bis 198 € pro Monat), DTAD (Vertrieb) oder evergabe.de (83 € pro Monat) (`docs/business.md` §8.1). Vergabe überwiegend nach Preis: 63 % aller Vergaben 2024 nur nach Preis (Zusammenfassung des Vergabestatistik-Berichts).
- Gespräche (n = 3, Hinweise; `docs/business.md` §8.9): Ein Betrieb mit etwa 120 Beschäftigten zahlt knapp 1.500 € pro Jahr für DTAD; ein Betrieb mit 15 Beschäftigten zahlt für kein Portal. Ob mitgeboten wird, entscheiden Entfernung, Personal und Kapazität; Vertragsenden bei anderen kennt keiner („Blackbox“, „Flurfunk“). Beide kennen Vergabeweiser und AusschreibungsRadar nicht oder nur vom Hörensagen. Die Vergabestelle (Oberpfalz) verlängert „fast immer“, wenn eine Option im Vertrag steht, und vergibt Reinigung „sehr oft“ unterhalb der EU-Schwelle in Einzellosen (n = 1).

**Konkurrenz mit der Funktion „auslaufende Verträge“ (Fakten, Stand 2026-11-05).**

| Anbieter | Was er zeigt | Preis | Stand der Prüfung |
|---|---|---|---|
| Vergabeweiser | Verträge, die in 12 Monaten enden (1.005 in Gebäudereinigung), mit Zuschlagsempfänger, Angebotszahl, Optionen; ober- und unterschwellig; kostenlose API und Marktzahlen | kostenlos | Seite und API von uns geprüft und genutzt |
| AusschreibungsRadar | rund 26.000 Aufträge mit Ende in 1 bis 18 Monaten, „verlängerbar“ markiert, geschätzter Ausschreibungsmonat; ab Starter (29 €) volle KI-Eignungsanalyse, ab Business (79 €) Match-Score, Bid/No-Bid-Check und Wettbewerber-Tracking, Professional 149 € | 0 bis 149 € pro Monat | Seiten und Preisseite von uns gelesen; Nebentest mit 2 sicher zugeordneten Losen |
| aufträge.io | 43.373 Verträge mit Ende in 12 Monaten, Analyse bisheriger Gewinner | auf Anfrage | nur Recherche |
| subreport, DTAD | Ausschreibungsdienste; eine Funktion für auslaufende Verträge ist in unseren Quellen nicht belegt | 84 bis 198 € pro Monat bzw. Vertrieb | Preisangaben und Gespräch 1 |

Beide geprüften deutschen Anbieter schreiben selbst, dass der Auftraggeber entscheidet, ob und wann neu ausgeschrieben wird. Ein Profilfilter („Eignung“, „Match“) wird bei AusschreibungsRadar schon angeboten (`docs/business.md` §8.2).

### Fachliches Erfolgskriterium (nachträglich formuliert, begründete Setzung)

> **Einordnung.** Ein fachliches Kriterium gab es seit 2026-11-04 (`docs/business.md` §7.1): Nutzen = „Der Betrieb kann Angebot, Referenzen und Personal gezielt vorbereiten, statt Bekanntmachungen dauernd zu beobachten“; Schwelle = Terminfenster ±3 Monate in mindestens 60 % und 10 Prozentpunkte über der naiven Referenz (vorab, vor dem Backtest). Es trug nicht (28,8 %). Die Schärfung unten wurde **erst nach Iteration 10** formuliert, ohne Kundenkontakt vor dem Projekt; sie ist eine begründete Setzung und kein vorab festgelegtes Kriterium.
>
> **Nutzen (Setzung).** Die Liste auslaufender Verträge ist ein Produkt, wenn ein Reinigungsbetrieb, der für Kommunen und Behörden bietet, damit früher als bisher weiß, wo sich ein Angebot vorzubereiten lohnt, und dafür zahlt.

| Bedingung (Setzung) | Begründung | Ergebnis (Stand 2026-11-05) |
|---|---|---|
| (i) Ein belegter Unterschied zur kostenlosen Konkurrenz | Wer dieselbe Information kostenlos bekommt, zahlt nicht | **Merkmalsunterschied, kein Qualitätsvorteil:** Ende je Los und der Grundlaufzeit; auf zwei Stichproben in rund 10 % der Lose, davon in 10b 11 von 15 Höchstende oder Losebene |
| (ii) Zahlungsbereitschaft von mindestens 2 von 3 größeren Betrieben über 50 € im Monat | ein Preis oberhalb des Free- und Starter-Niveaus der Konkurrenz | **nicht geprüft, in den Hinweisen gespalten:** nur ein größerer Betrieb erreicht; er nannte keinen Betrag für die Liste, für Wettbewerbsdaten „klang nach 50 bis 100 €“ (Einschätzung des Nutzers); der Kleinbetrieb „für gar nichts“ |
| (iii) Ausreichende Abdeckung der Zielregion | Fehlt der Vertrag in der Liste, hilft sie nicht | **Lücke der TED-Basis (Paket B, Hinweis):** Im Bekanntmachungsservice stehen 32 von 120 Oberpfälzer Reinigungsverfahren (26,7 %, Wilson 19,6–35,2 %) nicht auf TED; „national“ heißt „nicht auf TED gefunden“. Wert gegen die Schwelle nicht geprüft, B1 nicht entscheidbar. Dazu 33 von 130 Oberpfalz-Losen (25,4 %) ohne Ende |

### Risiken

| Risiko | Beleg (Fakt) | Gegenmaßnahme / Stand |
|---|---|---|
| Markt: Konkurrenz kostenlos | Vergabeweiser zeigt 1.005 Reinigungsverträge kostenlos; AusschreibungsRadar ab 0 € (A2 widerlegt) | eingetreten; Zyklus 4; Positionierung in einer Nische ungeprüft |
| Nachfrage | 3 Gespräche (2 Betriebe, 1 Vergabestelle), gespalten; A1, A15 ungeprüft | offen; keine Nachfrageaussage im Lab-Log |
| Daten | TED nur oberhalb der EU-Schwelle (über alle Branchen 88 % der Vergaben darunter); 25,4 % der Oberpfalz-Lose ohne Ende; Zuschlagswert nur bei 47,7 %; die meisten Vorgänger heutiger Neuausschreibungen vor eForms (55 von 68) | Paket B: Lücke von rund einem Viertel im Bekanntmachungsservice (Zeile (iii)), Erweiterung nur als Ausblick; Ursachen der Lücken in Paket C belegt |
| Listenfehler | 12 Lose (0,13 %), bei denen das Dauerfeld die Option schon enthält; Textmuster (M59) nicht gefangen; bei 1 von 10 übereinstimmenden Losen beide Quellen falsch | Liste eingefroren; als offene Grenze genannt (Abschnitt 6) |
| KI-Methode | Regeln, Leser und Evaluator gleiche Modellfamilie; Menschenprüfung nur 14/15 (Kommilitone), nicht an den 15 diskordanten Losen | offengelegt; zweite Modellfamilie und Menschenprüfung fehlen |
| Recht | TED-Lizenz offen; Vergabeweiser CC BY 4.0 (Nennung); Auftragnehmernamen können bei Einzelunternehmern personenbezogen sein (nicht geprüft); Scraping und Wettbewerbsrecht (UWG): nicht betrieben, nur einzelne Seiten von AusschreibungsRadar, `robots.txt` beachtet | TED-Lizenz vor Abgabe klären |
| Zeit | Git-Untergrenze 36,2 Stunden (Abschnitt 8); Zyklus 4 nach Hinweis des Dozenten | Menschenprüfung der 15 Lose, Handprüfung der Ortsregeln und Wertprüfung zu Paket B nicht mehr eingeplant |

**Mehrwert und Positionierung (Deutung, n = 3).** Der größere Betrieb sähe Nutzen in einem frühen Hinweis (Personal früher suchen), würde aber eher für Wettbewerbsdaten zahlen (aktueller Auftragnehmer, alte Preise) als für Enddaten; der kleine Betrieb will für Informationen nichts zahlen. Die Zielgruppe ist damit enger als gedacht: größere Betriebe, die für Kommunen und Behörden bieten. Wettbewerbsdaten zeigt Vergabeweiser kostenlos; aus TED allein sind sie nur teilweise zu bekommen (130 Oberpfalz-Lose: Auftragnehmer 99,2 %, Zuschlagswert über 1 € 47,7 %, Zahl der Angebote 60,8 %, alle drei zusammen 24,6 %). Nischenrollen (Datenqualität als Zulieferung, Verbandsberatung, Benchmark für Vergabestellen) sind nicht geprüft.

**Competitive Edge, ehrlich.** _Was bleibt:_ ein Merkmalsunterschied auf Los- und Definitionsebene (rund 10 % der Lose auf zwei Stichproben, Abschnitt 5), ein offen dokumentiertes Prüfverfahren und der Backtest, dass ein fester Abstand den Termin nicht vorhersagt. _Was nicht bleibt:_ Preis, Daten (offen), Wettbewerbsbild, Abdeckung (Vergabeweiser führt auch unterschwellige Verfahren), Terminprognose. _Ausblick, kein Vorteil:_ Im Bekanntmachungsservice, aus dem auch Vergabeweiser schöpft, stehen rund ein Viertel der Oberpfälzer Reinigungsverfahren nicht auf TED (Paket B, Abschnitt 5); das begründet eine Erweiterung um Daten unterhalb von TED, belegt aber keinen Vorsprung. _Nicht behauptet:_ dass die Liste genauer ist als Vergabeweiser, dass Vergabeweiser falsch liest, dass ein belegter Marktvorteil besteht oder dass Betriebe die Liste nachfragen oder bezahlen.

### Lernpunkt: Die Konkurrenz wurde erst spät gesehen (Prozessfehler)

- **Fakten.** Der Projektplan sah früh vor, die Wettbewerber zu sichten (Aufgabe G1.1). Sie blieb offen. Am 2026-10-24 fanden zwei Suchen von Claude keinen deutschen Dienst für auslaufende Verträge, und das wurde in `docs/business.md` §6 festgehalten. Am 2026-10-29 entschied der Nutzer gegen Kundenkontakt; damit entfielen die Aufgaben G2 bis G4, und von Strang G blieb nur die Recherche. G1.1 wurde erst am 2026-11-05 erledigt (abgehakt als „verspätet“).
- **Deutung.** Das ist ein Prozessfehler, nicht nur ein Suchfehler der KI: Es gab keine Stelle, die den offenen Punkt G1.1 vor der Modellierung erzwungen hätte, und nach dem Wegfall der Gespräche fehlte die Gegenprobe am Markt. Zwei Suchen genügten, um den Punkt gedanklich zu schließen.
- **Konsequenz.** Phase 1 braucht ein **Marktgate vor der Modellierung**: Erst wenn die Wettbewerber gesichtet und dokumentiert sind (Funktion, Preis, eigene Prüfung der Seiten), beginnt die erste Modellierung; jede Streichung eines Plan-Punktes ersetzt ihn durch eine Ersatzprüfung.
- **Folge und Kosten.** Zyklus 4 (Iteration 10 und 10b). Die Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos schon gibt.

## 2. Zyklus 1: Zuordnung zum Vorgänger (Iteration 1 bis 4)

Business Understanding: Kandidaten für eine Nische waren Gebäudereinigung, IT-Wartung, Winterdienst, Sicherheit, Kantine; Kriterium war genug Zuschläge mit Laufzeit. Datenbasis: TED Search API v3, Rohdaten unverändert in `data/raw`.

| Iteration (Datum) | Frage | Kriterium vorab | Ergebnis (Fakten) | Entscheidung |
|---|---|---|---|---|
| 1 (10-22) | Sind die Daten für eine Nische machbar? | genug Zuschläge mit bestimmbarer Laufzeit | Laufzeitende bei Gebäudereinigung 90,0 % bestimmbar (streng 80,9 %); Verlängerungsfeld BT-58 nur 18,9 % befüllt (A5 widerlegt); Wertfelder mit Platzhaltern (A6 widerlegt) | Gebäudereinigung vorläufig; weiter |
| 2 (10-23) | Genügen Auftraggeber + CPV, um einen neuen Auftrag dem Vorgänger zuzuordnen? | K2 ≥ 80 % | K2 = 5/30 = 16,7 % (Wilson 7,3–33,6); 629 abgelaufene eForms-Verträge; Median-Laufzeit 12 Monate | Zuordnung über das Objekt (Adresse, Titel) versuchen |
| 3 (10-24/25) | Trägt eine Objekt-Regel? | Sichtbarkeit eines Vorgängers (V1), Präzision (V2) ≥ 80 %, Trefferquote (V3) ≥ 60 % | V1 63,3 %, V2 45,8 %, V3 28,9 %; auf den Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test 11 von 24 korrekt | Regel verworfen; letzter Versuch auf neuen Testdaten |
| 4 (10-25 bis 10-30) | Verbessert eine erweiterte Regel auf neuen Testdaten? | W2 Präzision, Mindestzahl 25 Vorschläge; W3 Trefferquote ≥ 60 %; W4 Zweitprüfung des Nutzers ≥ 85 % | W2 17/19 = 89,5 %, aber nur 19 Vorschläge; W3 56,7 %; W4 13/20 = 65 % | **Idee anpassen:** keine weitere Zuordnungsregel; Vertragsliste aus den Zuschlägen selbst |

_Deutung._ Große Auftraggeber vergeben viele Verträge parallel; die Kennung des Auftraggebers reicht nicht. Daten vor eForms liefern die Laufzeit über `REF_NOTICE` (A11: 25/30). Trennung Entwicklung/Test: Die Regel wurde auf Entwicklungsdaten gebaut und auf neuen Daten getestet.

## 3. Zyklus 2: Terminprognose (Iteration 5)

| Iteration (Datum) | Frage | Kriterium vorab | Ergebnis (Fakten) | Entscheidung |
|---|---|---|---|---|
| 5 (10-30 bis 11-04) | Sagt „Höchstende − 6 Monate“ (R1) den Termin der Neuausschreibung voraus? | Treffer = Fenster ±3 Monate; X3: ≥ 60 % und ≥ 10 Prozentpunkte über der Baseline R0 (Ende der Grundlaufzeit − 6 Monate); Schwelle vor jeder Berechnung festgelegt | 52 von Hand bestätigte Paare (Zweitprüfung 61/67 = 91,0 %, mit KI-Hilfe, nicht als unabhängig gewertet): R1 28,8 % (Wilson 18,3–42,3), R0 17,3 %; 20 Neuausschreibungen kamen mehr als 3 Monate früher, 17 später | **Idee anpassen:** keine Terminprognose; Produktkern ist die Vertragsliste mit Enddaten |

_Data Preparation:_ Zuschlagstabelle je Los (`src/prepare/vertragsliste.py`) mit Ende der Grundlaufzeit, Höchstende und Herkunft; damals 9.915 Lose. Leakage vermieden: nur Wissen zum Zeitpunkt des Vorgänger-Zuschlags. _Deutung:_ Der Termin ist zweigipflig verteilt; ein fester Abstand trägt nicht. In Zyklus 4 stützt die Vergabestelle das: Verlängerung ist der Normalfall.

## 4. Zyklus 3: Qualität der Vertragsliste (Iteration 6 bis 9)

| Iteration (Datum) | Frage | Kriterium vorab | Ergebnis (Fakten) | Entscheidung |
|---|---|---|---|---|
| 6 (11-04) | Wie genau ist der Prototyp (Oberpfalz, 146 Lose, Stufen A–F)? | Y1 Ende der Grundlaufzeit ≥ 90 % an 60 Zufallslosen (Prüfung durch den Nutzer); Y3 Abdeckung ≥ 80 % | Y1 54/60 = 90,0 % laut Auswertung, 53/60 = 88,3 % nach Fehler L60; Höchstende 91,7 %; Abdeckung 79,7 % (damalige Fassung). Die Vorlage zeigte den Listenwert (Verankerung, vom Evaluator gefunden) | Zurück zu Phase 3: Regel 1b, neue Stichprobe |
| 7 (11-04) | Behebt Regel 1b den Fehlertyp „Enddatum ist schon Höchstende“? | Y1 ≥ 90 %, Y1r ≥ 12/15 Regelwirkungs-Lose; vorab: Y1 zwischen 70 und 90 % → kein dritter Regelversuch | Y1 36/47 = 76,6 % (Wilson 62,8–86,4), Y1r 8/15, Höchstende verfehlt. Mischmaß aus Listen- und Prüfungsfehlern (bei 45 von 47 Losen schrieb die Nachprüfung dasselbe Feld ab) | Abschluss mit diesem Stand; Ende „laut Bekanntmachung“, Höchstende nur Hinweis |
| 8 (11-04/05) | Bestätigen zwei KI-Leser die Liste? | Z0 Leser untereinander ≥ 90 %, Z1 bis Z4 (Liste gegen Vergleichswert, Regelwirkung, Höchstende, Kontrolle) | Z0 94/95; Z1 77/80 = 96,2 %; Z2 14/15 (bei einheitlichem Maßstab 11/15, verfehlt); Z3 75/80 und 67/72; Z4 10/10. Neue Listenfehler: Lose ohne Zuschlag, Übertragung von Werten, „3 Jahre mit Option“ | Weiter (Projektabschluss), eingeschränkt: Leser nicht unabhängig, nicht von Menschen bestätigt |
| 9 (11-05) | Beheben Regeln 6 bis 10 diese Fehler; hält die Liste auf einer neuen Stichprobe (Seed 20261109, 110 Lose)? | V1 ≥ 90 %, V2 bis V8 (u. a. Höchstende V4, Lose ohne Zuschlag V7, Verfahren V8) | Liste 9.325 statt 9.915 Lose; V1 66/70 = 94,3 % (Wilson 86,2–97,8); V2 28/30; V3 66 gegen 65 von 70 (alte Fassung); V5 110/110; V6 Kommilitone 14/15. **Verfehlt:** V4 (87,1 % bei Schwelle 90 %), V7 (Los N51); V8 teilweise | Weiter, eingeschränkt: Fassung 9 wird Prototyp, Höchstende nur Hinweis; „V1 bis V8 erfüllt“ wird nicht behauptet |

**Abdeckung (Zähler und Nenner, an einer Stelle).** Quelle: `data/processed/vertragsliste_909.csv` (Fassung 9) und `reports/vertragsliste_iteration9.md`, nachgerechnet.
- **Alle Lose:** 6.803 von 9.325 haben ein Ende der Grundlaufzeit, **rund 73 %** (72,95 %); 2.522 Lose (27,0 %) haben keines.
- **Letztes Jahr (X4):** Unter den Losen aus Zuschlägen, veröffentlicht 2025-10-01 bis 2026-09-30, haben 2.783 von 3.503 ein Ende, **79,4 %** (Wilson 78,1–80,8; Schwelle 80 % knapp verfehlt). Die frühere Fassung hatte 2.924 von 3.668 = 79,7 %. Der Anteil schwankt nach Halbjahr der Veröffentlichung zwischen 63,6 % (2. Halbjahr 2024) und 80,7 % (1. Halbjahr 2026); das letzte Jahr liegt deshalb über dem Gesamtwert (Nachrechnung aus der Liste).
- **Ziehungspool 10b:** 5.754 Lose (keine Abdeckung): Lose mit Zuschlag und Ende, ohne Lose früherer Stichproben.
- **Lose ohne Ende:** Der Anteil liegt über alle Lose bei 27,0 %, im letzten Jahr bei 20,6 %. Beide Zahlen, nicht nur die kleinere, gehören zur Aussage über Lücken.

_Deutung._ Die Fassung 9 ist auf der Stichprobe zu 94,3 % mit dem Vergleichswert identisch (alte Fassung 92,9 %, bloßes Feld 90,0 %). Der Nutzen der Regeländerung ist nicht gesichert: Die Stichprobe trennt die Fassungen kaum, der Vergleichswert ist teilweise zirkulär, V5 zeigt vor allem gleiche Anweisung und gleiche Rohtexte. N51 trägt `unpublished` (Ergebnis aus geschäftlichen Interessen nicht veröffentlicht), nicht „kein Zuschlag“; die Ursache liegt in der Anweisung an die Leser. _Grenzen:_ gleiche Modellfamilie von Regel, Leser und Evaluator; Gruppe R nur 2 Lose; V6 mit 15 Losen dünn. Details: `docs/iterationen.md`, `reports/evaluation_iteration7.md` bis `_iteration9.md`.

## 5. Zyklus 4: Business Understanding und Wettbewerb (Iteration 10 und 10b)

_Anlass (2026-11-05, nach Iteration 9): Der Dozent verlangt mehr Gewicht auf Business Understanding. Die Recherche zeigte, dass die Sichtung der Wettbewerber nie erfolgt war (Lernpunkt in Abschnitt 1). Abweichend von „keine weitere Iteration“ (Iteration 8 und 9) hat der Nutzer am 2026-11-05 einen Rücksprung zu Phase 1 beschlossen. Iteration 9 blieb unverändert; ihre Stichprobe und ihr Vergleichswert dienten als fester Maßstab._

**Iteration 10: Business Understanding und Wettbewerber.** Recherche (KI-Agent plus KI-Gutachten aus BWL-Sicht, einzelne Seiten von Claude nachgelesen): Vergabeweiser bietet eine kostenlose Liste auslaufender Verträge samt API, AusschreibungsRadar eine günstige; **A2 („es gibt keinen deutschen Dienst“) ist widerlegt.** Das Gutachten hielt das Kernprodukt „Liste“ für nicht tragfähig und empfahl ein Wettbewerbsbild (`docs/business.md` §8.4, §8.5). Gespräche (W5, Leitfaden vorab): Der Nutzer rief neunmal an und erreichte drei Stellen (zwei Reinigungsbetriebe, eine Vergabestelle); Notizen ohne Namen. Zahlungsbereitschaft zeigte sich nur für Wettbewerbsdaten; die Vergabestelle bestätigt, dass das Vertragsende kein Neuausschreibungstermin ist. n = 3, Hinweise.

**Vorgehen.** Die API von Vergabeweiser (Rohantworten in `data/raw/vergabeweiser_20261105/`) liefert das Vertragsende je Verfahren, nicht je Los. Die Zuordnung eines Loses zu einem Eintrag lief per Skript ohne Handentscheid (Verweis der Zuschlagsbekanntmachung, dann Verfahrenskennung, dann eigene Kennung). **Hypothese** _(vorab, vor dem Abruf)_: Auf den 70 Zufallslosen der Iteration 9 stimmt Vergabeweiser seltener mit dem Vergleichswert überein als die Liste (66/70). In 10b (Seed 20261112, 160 neue Lose mit Listenende) lasen zwei KI-Leser nur die diskordanten Lose, ohne Angabe der Quelle, nach der neutralen Definition; Hypothese vorab: die Liste trifft häufiger, und der Unterschied reicht über die Granularität hinaus.

| Kriterium (vorab) | Schwelle | Ergebnis (Fakten) | Urteil |
|---|---|---|---|
| W1 (Iteration 10, 70 Lose) | Differenz Liste − Vergabeweiser ≥ 5 Lose | Liste 66/70, Vergabeweiser 58/70, +8, exakter Test p = 0,0078; Ursachen der 8: Losebene 4, Höchstende statt Grundlaufzeit 2, fehlender Wert 1, 2 Tage 1; Basisregel „Feld EndDate“ 63/70 | formal erfüllt, überwiegend Los- und Definitionsunterschied; zählt Vergabeweisers Verfahrensdatum als richtig, wenn es irgendeinem Los entspricht, sinkt die Differenz auf +4 |
| W8a (10b) | ≥ 16 Lose (10 %) und p < 0,05 | 15 von 160 Losen diskordant; Leser 15/15 einig; Liste 15/15, Vergabeweiser 0/15; +15, p = 0,0001 | **formal verfehlt, rechnerisch unerreichbar** (Schwelle aus der Diskordanzrate der Iteration 10 übernommen, Fehler der Vorab-Festlegung) |
| W8b (10b) | ≥ 8 Lose und p < 0,05, Vergabeweiser gilt auch bei Datum irgendeines Loses desselben Verfahrens als richtig | +10, p = 0,0020 | erfüllt, schwach aussagekräftig |
| W7 Nebentest AusschreibungsRadar | beschreibend (Seed 20261111, 15 Lose) | nur 2 von 15 sicher zugeordnet, beide wie Liste und Vergleichswert | keine Aussage zur Genauigkeit möglich |

**Einordnung der 15 diskordanten Lose (Evaluator, je Los am Rohtext).** Höchstende statt Grundlaufzeit 7 (eine einzige Textvorlage), Losebene 4, Zuordnungsfehler der Pipeline 1 (M54, gehört nicht zu „Vergabeweiser liest falsch“), Abweichung mit offener Ursache 2 (M3, M22), mehrdeutig 1 (M49). Zählt das Höchstende für Vergabeweiser als richtig, bleiben 3 : 0, p = 0,25. Beide Stichproben zusammen: nur die Liste richtig bei 23 von 230 Losen = 10,0 % (Wilson 6,8–14,6 %). Von 10 übereinstimmenden Losen lag bei einem (M59) beide falsch: ein Hinweis, keine Rate.

**Deutung.** Der Unterschied zugunsten der Liste ist ein **Merkmalsunterschied** (Ende je Los, Grundlaufzeit statt Höchstende), kein belegter Qualitätsvorteil beim Lesen: Liste und Vergabeweiser nutzen dasselbe TED-Feld, gemeinsame Fehler bleiben unsichtbar, und die Leser stammen aus derselben Modellfamilie wie die Regeln. 15 von 15 Übereinstimmungen der Leser sind kein Zeichen von Unabhängigkeit.

**Pakete A, C, F und B (Nachträge, Entscheidung des Nutzers 2026-11-05).**
- **A, Wettbewerbsbild aus TED** (`reports/wettbewerbsbild_oberpfalz.md`): Zahlen siehe Abschnitt 1; Handabgleich von 5 Losen 5 von 5. Deutung: Ein Wettbewerbsbild aus TED allein ist nur zu etwa einem Viertel der Lose vollständig.
- **C, Ursachen der Lücken** (`reports/stufe_f_ursachen.md`): Die 33 Lose ohne Ende haben alle keine Laufzeitfelder im XML (18 ohne Laufzeit im Text, 14 mit Dauer oder Datum nur im Freitext). Dabei fand sich der Fehlertyp „Dauerfeld enthält die Option schon“: **12 Lose in 5 Bekanntmachungen, 0,13 % der 9.325 Lose**; zwei Fälle am Rohtext bestätigt, die übrigen eine einzelne KI-Lesung. Ein erster Nachtrag hatte „nur dieser Fall“ geschrieben; das war falsch (Anhang B).
- **F, Optionsanalyse** (`reports/optionsanalyse.md`): An den 52 Backtest-Paaren lag die Neuausschreibung bei belegter Option (n = 24) in 70,8 % zwischen dem Ende der Grundlaufzeit und dem Höchstende (Wilson 50,8–85,1). Hinweis, kein Beleg.
- **B, Abdeckung unterhalb der EU-Schwelle (A3, Oberpfalz)** (`reports/oeffentlichevergabe_test.md`, `_robustheit.md`). _Hypothese und Kriterien (vorab, `0e83dfa`):_ Mindestens ein Drittel der Oberpfälzer Reinigungsverfahren (Haupt-CPV 909) liegt unterhalb der EU-Schwelle (B1 ≥ 33 %); B2 bis B5: Feldabdeckung, Überlappung mit der Liste, Handabgleich von 5 Verfahren, Machbarkeit. Daten: OCDS-Jahresdateien des Bekanntmachungsservice 2024 bis 2026 (CC0, 626.620 Datensätze), ohne Kennzeichen für die Schwelle; „national“ heißt „nicht auf TED gefunden“.
  - _Erste Auswertung (Filter NUTS-3-Code am Lieferort):_ 84 Verfahren, alle auf TED, 0 national. _Artefakt:_ Nationale Verfahren tragen am Lieferort zu 71,2 % nur den NUTS-1-Code „DE2“ (EU-Verfahren zu 92,4 % einen NUTS-3-Code); der Filter schloss sie aus. Die erste Auswertung („B1 deutlich verfehlt“) ist nicht gültig.
  - _Ergebnis (Postleitzahl, Ortsliste):_ 32 von 120 Verfahren nicht auf TED = 26,7 % (Wilson 19,6–35,2 %; Jahreswerte 13 bis 45 %). **B1 ist nicht entscheidbar**, das Intervall schließt 33 % ein. 62 von 64 Bekanntmachungen der Liste stehen im Datensatz.
  - _Deutung:_ Rund ein Viertel der Reinigungsverfahren im Bekanntmachungsservice fehlt auf TED: ein Hinweis auf eine Lücke der TED-Basis und ein Argument für die Erweiterung als Ausblick, **kein belegter Vorsprung**. A3 bleibt ungeprüft; die Aussage der Vergabestelle (n = 1) ist weder bestätigt noch widerlegt. _Lernpunkt:_ Eine Null ist ein Verdachtsmoment, kein Ergebnis; erst die Robustheitsprüfung hat sie als Filterartefakt erklärt.
  - _Grenzen:_ „National“ ist nicht „unterhalb der Schwelle“; Ortsregeln nicht von Hand geprüft (zwei Autobahn-Treffer vermutlich nicht Oberpfalz); B2 und B4 für die 32 Verfahren stehen aus.

**Abweichungen von der Vorab-Planung (offen).** Zuordnungsweg 2 nach dem Trockenlauf ergänzt (vor dem Abruf); Abrufskript nach einem DNS-Fehler angepasst; Nebentest W7 nach Beginn des Abrufs; ein beim Test abgerufener Eintrag enthält ein Los der Stichprobe.

### Entscheidung (2026-11-05, Nutzer): Weiter, Projektabschluss, eingeschränkt formuliert
- **Begründung.** W1 ist formal erfüllt, aber überwiegend Los- und Definitionsunterschied; W8a ist formal verfehlt wegen eines Fehlers der Vorab-Schwelle, W8b erfüllt. Nach der Vorab-Regel gilt „kein belegter Vorteil im definierten Maß“, und das ist nicht als Gleichheit zu lesen. Befund: Merkmalsunterschied, kein belegter Qualitätsvorteil, Nachfrage offen.
- **Abweichung von der Vorab-Folge (offen begründet).** Die Folge „W8a verfehlt → die Aussage ‚kein Vorteil gegenüber Vergabeweiser‘ gilt weiter“ wird nicht übernommen, weil sie der gemessenen Richtung widerspricht und die Schwelle unerreichbar war; für „W8a verfehlt und W8b erfüllt“ gab es keine Regel. „Die Liste ist genauer“ wird ebenso wenig behauptet.
- **Geschäftlich.** „Liste als eigenes Produkt nicht tragfähig“ (`docs/business.md` §8.4) bleibt bestehen; A2 bleibt widerlegt; A1, A3 und A15 bleiben ungeprüft. Weitere Grenzen: Abschnitt 6; das Protokoll der Leserläufe 10b liegt außerhalb des Repos.

## 6. Was wir empfehlen und was nicht

- **Empfehlung.** Die Vertragsliste „Ende der Laufzeit laut Bekanntmachung“ ist als Ausgangspunkt nutzbar; vor jeder Entscheidung die verlinkte Bekanntmachung lesen. Als eigenes Produkt empfehlen wir sie **nicht**, weil es das Kernprodukt kostenlos (Vergabeweiser) und günstig (AusschreibungsRadar) gibt. Weiterverfolgen ließe sich nur eine Nische (Wettbewerbsdaten, Datenqualität als Zulieferung, Vergabestellen), nach Gesprächen mit mehr Beteiligten.
- **Zulässige Aussagen.** „Zu 94,3 % identisch mit dem Vergleichswert zweier KI-Leser; an 15 Losen bestätigt ein Mensch (14/15); Höchstende nur Hinweis.“ Und: „Auf zwei Stichproben (n = 70 und n = 160) weicht Vergabeweisers Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt; in 10b waren 11 von 15 dieser Fälle Höchstende oder Losebene.“
- **Nicht belegt.** Eine Terminprognose; „die Liste ist korrekt“; „Fehlerarten behoben und bestätigt“; „V1 bis V8 erfüllt“; ein Qualitätsvorteil gegenüber Vergabeweiser (und ebenso Gleichheit); Nachfrage, Zahlungsbereitschaft und Marktvorteil (A1, A15); Abdeckung unterhalb der EU-Schwelle (A3).
- **Offene Grenzen der Liste.** Das Höchstende ist oft zu hoch (laut Evaluator in 7 von 11 Fällen) und nur ein Hinweis; Schuljahres-Verträge sind nicht tagesgenau; `unpublished` wird nicht erkannt. „Dauerfeld enthält die Option“ (12 Lose, 0,13 %; Ursache nur vermutet, nicht getestet; 6 weitere Lose unklar) und Textmuster wie M59 oder „gilt bis … ohne ‚zunächst‘“ (12853-2024, Los 3) werden nicht gefangen, Häufigkeit unbekannt. Die Zuordnung zu Vergabeweiser (M54) wurde nicht für alle 160 Lose von Hand geprüft; ob Vergabeweiser Ausschreibung oder Zuschlag zeigt, ist ungeklärt (M3, M22, M49). Die Stichprobe 10b enthält nur Lose mit Listenende (die 27 % ohne Ende gehen nicht ein). Keine Menschenprüfung der 15 diskordanten Lose; Fehlerarten aus Iteration 8 in Fassung 9 behoben, nicht bestätigt; keine zweite Modellfamilie.

## 7. KI-Irrwege und ihre Prüfung

Die KI (Claude Code) hat Hypothesen, Regeln, Stichproben und Auswertungen mitgebaut. Die Fehler wurden vom Nutzer, vom Evaluator (eigener Subagent, nur Lesezugriff) oder von Claude selbst gefunden. Die neun wichtigsten; die vollständige Tabelle mit allen Einträgen steht im Anhang B.

| Datum | Irrweg | Bemerkt durch | Konsequenz |
|---|---|---|---|
| 2026-10-23 | K2-Urteile und Zuordnungsregel stammten von derselben Hand (Claude) | Evaluator | Handsuche durch getrennten Subagenten, Zweitprüfung durch den Nutzer |
| 2026-10-25 | Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 korrekt | Test auf neuen Daten | Regel verworfen; Testdaten strikt getrennt |
| 2026-11-04 | Iteration 6 und 7: Prüfvorlage zeigte den Listenwert (Verankerung); danach wurden Felder versteckt, und die Nachprüfung übernahm das Feld | Evaluator, Auswertung | Y1 nur als Mischmaß berichtet; Vorlage ohne Listenwerte |
| 2026-11-05 | Iteration 8: Claude nannte die KI-Leser „blind“, sie hatten aber `CLAUDE.md` mit dem Fehlertyp im Kontext | Evaluator | Leser gelten als nicht unabhängig; Z2 mit beiden Zahlen (14/15, 11/15) |
| 2026-11-05 | Iteration 9: V4 mit zwei unverbundenen Schwellen; Stichprobe trennt die Fassungen kaum; N51 als „Lesefehler“ gedeutet, tatsächlich Anweisung | Evaluator | V4, V7 offen als verfehlt berichtet; „Fehlerarten behoben“ nicht behauptet |
| 2026-11-05 | Wettbewerber nicht gesichtet (G1.1), zwei Suchen fanden keinen Dienst | Recherche-Agent nach Hinweis des Dozenten | A2 widerlegt; Marktgate (Abschnitt 1); Zyklus 4 |
| 2026-11-05 | Fehlertyp „Dauerfeld enthält die Option“: Claude schrieb „nur dieser Fall“, tatsächlich 12 Lose in 5 Bekanntmachungen | Nutzer, dann Paket C | Fehlerart offen im Lab-Log; Aussage richtiggestellt |
| 2026-11-05 | Iteration 10b: Schwelle W8a unerreichbar (aus der Diskordanzrate der Iteration 10 übernommen); Zuordnungsfehler M54 | Claude vor den Leserantworten, Evaluator | Kriterium nicht nachträglich geändert; „formal verfehlt, unerreichbar“ berichtet |
| 2026-11-05 | Paket B: Null als Ergebnis gelesen (0 von 84 Verfahren „B1 deutlich verfehlt“); tatsächlich Filterartefakt (Landkreis-Code am Lieferort fehlt bei nationalen Verfahren) | Robustheitsprüfung | Erste Auswertung nicht gültig; B1 nicht entscheidbar |

## 8. Zeitaufwand

Untergrenze aus der Git-Historie (Sitzung = Commits mit höchstens 90 Minuten Abstand, plus 30 Minuten Vorlauf; Iteration 10 enthält 10b und die Pakete A, C, F, weil der Tag `iteration-10` am Ende liegt). Enthalten ist die Rechenzeit von Claude. Nicht enthalten: Lesen, Prüfen von Hand, Recherche, Vortrag und alle Commits nach dem Tag (Lab-Log, Folien, Webseite, Paket B).

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
| 11 | 1 | 10 | 1.5 |
| **Summe** | 30 | 128 | **37.7** |

**Arbeitsschritte mit Zeitaufwand.** Näherung: Sitzungen anhand der Commit-Nachrichten zugeordnet (gemischte grob geteilt); „Handarbeit“ nach Angaben des Nutzers. Summe der Git-Spalte = 36,2 Stunden.

| Arbeitsschritt | Zugeordnete Git-Sitzungen | Git (Std., ca.) | Handarbeit außerhalb Git |
|---|---|---|---|
| Data Understanding (Abruf, Befüllungsquoten, Ursachen der Lücken) | Iteration 1 und 2, Paket C | 3,6 | nicht erfasst |
| Modellierung und Regeln (Zuordnung, Backtest, Regeln 1b, 6 bis 10) | Iteration 3, 4, 5, 7, 9 (Anteile) | 10,5 | – |
| Handprüfungen (Vorbereiten und Auswerten: Blindprüfungen, Handsuche, Zweitprüfung, Prüfung von 60 und 95 Losen) | Iteration 3 bis 7 (Anteile) | 13,7 | Ausfüllen der Prüfvorlagen durch den Nutzer: **offen** |
| KI-Lesung (Leser, Vergleichswert, Auswertung) | Iteration 8, 9 (Anteil), 10b | 3,5 | Kommilitone: 15 Lose in Iteration 9, Stunden **offen** |
| Business Understanding und Recherche (Wettbewerber, Wettbewerbsbild, Nebentest) | Iteration 4 (Anteil), 10 (Anteil) | 2,1 | – |
| Gespräche mit Betrieben und Vergabestelle (W5) | – | – | **105 Minuten** (1,75 Stunden: Vorbereitung, neun Anrufe, Abtippen; Angabe des Nutzers) |
| Lab-Log, Folien, Dokumentation | Iteration 4, 5, 10 (Anteile) | 2,8 | Lesen der Berichte, Vortrag: nicht erfasst |

_Deutung._ Handprüfungen und Regelarbeit machen rund 24 von 36 Git-Stunden aus, Wettbewerb und Gespräche zusammen rund 4. Der Marktschritt hätte am Anfang wenig gekostet (Lernpunkt in Abschnitt 1).

## 9. Reproduzierbarkeit und Quellen

- **Code und Daten.** Alle Schritte laufen als Skripte in `src/`, Abhängigkeiten in `requirements.txt`; Aufrufe und Reihenfolge in `docs/reproduzierbarkeit.md`. Rohdaten stehen unverändert in `data/raw` (nicht im Git, Abruf per `src/ted_download.py`); Datenlink für die Abgabe: _offen_.
- **Vorab festgelegt.** Seeds, Kriterien und Skripte wurden vor dem Ziehen oder Abruf committet; Hashes und Commits je Iteration stehen im Anhang A. Ausnahmen stehen in Abschnitt 5.
- **Quellen.** Vollständig in `docs/quellen.md`: TED Search API v3 (**Lizenz offen, vor Abgabe zu prüfen**), eForms SDK, CRISP-DM; Vergabeweiser (CC BY 4.0, Nennung); AusschreibungsRadar (einzelne Seiten, `robots.txt` beachtet); Bekanntmachungsservice (CC0); Preisquellen in `docs/business.md` §8. Status aller Annahmen: `docs/annahmen.md` (A1 bis A20).

<div style="page-break-before: always"></div>

## Anhang A. Seeds, Hashes und Commits

- **Iteration 6:** `src/prepare/stichprobe_iteration6.py`. **Iteration 7:** Seed 20261106, SHA-256 des Schlüssels `eade66c0…`. **Iteration 8:** Seed 20261108 für die Kontrolle, SHA-256 der Vorlage `5be683ad…`. **Iteration 9:** Seed 20261109, SHA-256 des Schlüssels `9dbf5c1a…`, der neuen Liste `5ec73364…`.
- **Iteration 10:** kein eigener Seed; die 70 Zufallslose der Iteration 9 (Schlüssel `9dbf5c1a…`), Skript `src/prepare/vergleich_iteration10.py`, Kriterien und Skript vor dem Abruf committet (`81a3b90`). Nebentest: Seed 20261111, Ziehung vor dem Nachsehen (`2002ac8`), Auswertung `0eeab99`.
- **Iteration 10b:** Seed 20261112, SHA-256 des Schlüssels `2cd00206…`, `src/prepare/stichprobe_iteration10b.py`; Hypothese, Kriterien und Seed vor dem Ziehen (`4f50436`), Ziehung (`9d63c59`), Abrufskript vor dem Abruf (`49bb198`), Abruf (`64a23e3`), Paket für die Leser vor den Antworten (`6b7e8d8`), Antworten unverändert (`69917ff`), Auswertung und Evaluator (`f6583cc`), Abschluss (`0419609`).
- **Pakete:** Paket A Seeds 20261113 (Handabgleich von 5 Losen) und 20261114 (3 Beispiel-Lose), beide im Skript `src/prepare/wettbewerbsbild_oberpfalz.py` vorab festgelegt (`ea5ebfb`); Paket F `d6e2335`; Paket C `79fd0df`; Paket B Kriterien `0e83dfa`.
- Die Reihenfolge der Commits belegt, dass Regeln und Kriterien vor dem Ziehen feststanden.

## Anhang B. KI-Irrwege, vollständige Tabelle

Nur ergänzt, nie überschrieben (`docs/ki_irrwege.md`). Je Eintrag: Datum, was schieflief, wie es bemerkt wurde, Konsequenz.

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
| 2026-11-05 | Paket B: Die erste Auswertung (Filter auf NUTS-3-Codes der Oberpfalz) fand 0 von 84 Verfahren unterhalb der EU-Schwelle und wurde im Bericht als „B1 deutlich verfehlt“ gelesen; das Feld für den Lieferort trägt bei nationalen Verfahren meist nur NUTS-1 („DE2“, 71,2 %), sodass der Filter nationale Verfahren aussortierte | Claude (Misstrauen gegenüber der Null, bevor das Ergebnis in Lab-Log oder Folien kam) und die Robustheitsprüfung des Agenten | Erste Auswertung nicht gültig; mit Postleitzahl und Ortsliste 32 von 120 (26,7 %, Wilson 19,6–35,2 %), B1 nicht entscheidbar; Lernpunkt „Eine Null ist ein Verdachtsmoment, kein Ergebnis“ |
