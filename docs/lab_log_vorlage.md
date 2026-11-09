# Lab-Log: Vergabe-Radar

_Big Data Analytics, Leistungsnachweis B (Zweierteam). Chronologisch nach CRISP-DM-Zyklen. Zahlen und Quellen stehen in `docs/iterationen.md`, `docs/business.md`, `docs/phasen/` und `reports/`; hier steht die Erzählung mit den Entscheidungen. Fakten und Deutung sind getrennt gekennzeichnet. Hauptteil: Abschnitte 0 bis 11 (bis vor Anhang A); Details im Anhang A (Hashes und Commits) und B (alle KI-Irrwege). Stand: 2026-11-09._

_Erzeugt mit `src/report/lab_log.py` aus `docs/lab_log_vorlage.md`, `docs/zeitprotokoll.md` und `docs/ki_irrwege.md`; Bilder mit `src/report/lab_log_bilder.py`._

> **In einfachen Worten.** Wir wollten wissen, ob sich aus den Bekanntmachungen vergebener öffentlicher Aufträge (Datenbank TED, das EU-Amtsblatt für Ausschreibungen) vorhersagen lässt, wann ein Reinigungsvertrag in Deutschland neu ausgeschrieben wird, damit sich ein Betrieb früh vorbereiten kann. Wir haben dafür drei Ansätze gegen vorab festgelegte Schwellen geprüft: neue Aufträge ihren Vorgängern zuordnen, den Termin der Neuausschreibung berechnen und eine Liste der Vertragsenden bauen. Der Termin lässt sich nicht vorhersagen (Trefferquote 28,8 % statt der geforderten 60 %). Das Ende eines Vertrags lässt sich meist aus der Bekanntmachung lesen (bei 66 von 70 Stichprobenverträgen gleich wie der Vergleichswert zweier KI-Leser), doch diese Liste gibt es schon kostenlos, und unsere Prüfung ergab keinen tragfähigen Business Case. Wir empfehlen deshalb, die Liste als Hilfsmittel zu nutzen und kein eigenes Produkt zu bauen; für einen Reinigungsbetrieb ist „kostenlos nutzen“ im Modell mit Annahmen besser als „selbst bauen“. Grenzen: nur drei Gespräche, die KI-Leser sind nicht unabhängig, ob jemand für die Liste zahlt, ist ungeprüft.

## 0. Überblick

**Frage.** Mittelständler (Beispiel Gebäudereinigung) wollen sich früh auf Neuausschreibungen öffentlicher Aufträge vorbereiten. Lässt sich aus den Zuschlagsbekanntmachungen auf TED (Tenders Electronic Daily) vorhersagen, wann ein Vertrag neu ausgeschrieben wird, und wäre eine Liste auslaufender Verträge ein Produkt, das sich vom Markt abhebt?

**Antwort in drei Sätzen.**
1. Der Termin der Neuausschreibung lässt sich mit den TED-Daten nicht brauchbar vorhersagen: Die beste einfache Regel trifft das Fenster ±3 Monate in 28,8 % der 52 geprüften Fälle (Schwelle 60 %, naive Referenz 17,3 %).
2. Brauchbar ist eine Liste der Verträge mit dem Ende ihrer Laufzeit („laut Bekanntmachung“): 6.803 von 9.325 Losen (rund 73 %) haben ein Ende der Grundlaufzeit (Abschnitt 4); bei 66 von 70 Stichprobenlosen (94,3 %) ist das Ende gleich wie der Vergleichswert zweier KI-Leser (Mensch aus dem Team 14/15; „die Liste ist korrekt“ ist nicht belegt). Diese Art Liste gibt es aber schon kostenlos (Vergabeweiser) und günstig (AusschreibungsRadar).
3. Belegt ist nur ein Merkmalsunterschied (Ende je Los, Grundlaufzeit statt Höchstende): Auf zwei Stichproben weicht Vergabeweiser bei 27 von 230 Losen ab (11,7 %), bei 23 (10,0 %) liegt nur unsere Liste richtig. Ein Qualitätsvorteil beim Lesen ist nicht belegt. Zahlungsbereitschaft zeigte sich in einem von drei Gesprächen und nur für Wettbewerbsdaten; Nachfrage bleibt ungeprüft.

**Verlauf.** Zehn Iterationen in vier Zyklen; danach (2026-11-06 bis 11-09) Business-Case-Auswahl, Demo, Live-Demo, Video und Folienumbau (Abschnitt 5 und 6). Die Entscheidung am Ende jeder Iteration (weiter, zurück zu Phase X, Idee anpassen) war vorab an Schwellen gebunden, die vor dem Ergebnis committet wurden. Zyklus 4 entstand, weil der Dozent mehr Gewicht auf Business Understanding verlangte.

| Zyklus | Iterationen | Leitfrage | Ergebnis |
|---|---|---|---|
| 1 | 1 bis 4 | Lässt sich ein neuer Auftrag seinem Vorgänger zuordnen? | Nein, jede Variante verfehlte die Schwelle; Idee angepasst |
| 2 | 5 | Trägt eine einfache Terminprognose? | Nein (28,8 % statt 60 %); Idee angepasst auf eine Vertragsliste |
| 3 | 6 bis 9 | Wie genau ist die Vertragsliste? | Brauchbar, zuletzt 94,3 % Übereinstimmung mit zwei KI-Lesern; nicht als korrekt belegt |
| 4 | 10 und 10b (mit Paketen A bis D und F, drei Gesprächen, Nebentest) | Was bietet der Markt schon, und hebt sich die Liste ab? Was ändert die Sicht des Betriebs (selbst filtern)? | Kernprodukt gibt es kostenlos; belegt ist nur ein Merkmalsunterschied; Eigenbau gegen kostenlose Dienste im Modell (Annahmen) nie günstiger (Modellkonstruktion); Nachfrage offen |

**CRISP-DM-Phasen je Zyklus** (Einzelheiten in den Abschnitten 2 bis 5; „–“ = in diesem Zyklus nicht bearbeitet).

| Zyklus | 1 Business Understanding | 2 Data Understanding | 3 Data Preparation | 4 Modeling | 5 Evaluation | 6 Deployment |
|---|---|---|---|---|---|---|
| 1 (It. 1–4) | Nische Gebäudereinigung, Ziel Vorgänger finden | Befüllung der TED-Felder, Platzhalter | Zuschlagstabelle, Objekttexte | Zuordnungsregeln (Auftraggeber, Objekt) | Blindprüfung, Handsuche; Schwellen verfehlt | – (entfällt) |
| 2 (It. 5) | Prognoseziel und Schwelle vorab (±3 Monate, 60 %) | Laufzeitfelder, Vorgänger vor eForms | Paare Vorgänger/Neuausschreibung | Regel R1 gegen Baseline R0 | 52 Paare, Zweitprüfung; 28,8 % | – (entfällt) |
| 3 (It. 6–9) | Produktkern: Liste statt Prognose | Fehlerarten im Enddatum | Leseregeln 1b, 6 bis 10 | Regelbasierte Liste (Stufen A–F) | Neue Stichproben, KI-Leser, Teammitglied; 66 von 70 gleich wie der Vergleichswert | Prototyp Webseite (Abschnitt 6) |
| 4 (It. 10/10b) | Rücksprung: Konkurrenz, Sicht des Betriebs, Gespräche | Vergabeweiser-API, Bekanntmachungsservice | Abgleich je Los | – (keine neue Regel) | Pakete A–D, F, Auswahlbogen | Nur Veranschaulichung: Demo, Live-Demo, Video |

**Grenzen vorweg.** Vor Iteration 10 gab es keinen Kundenkontakt (Entscheidung des Nutzers, 2026-10-29); dann folgten drei kurze Telefonate (Hinweise, keine Stichprobe). Ob jemand für eine solche Liste zahlt (A1, A15), ist ungeprüft. Die Vertragsliste und ihre Prüfungen (Iteration 6 bis 10b) beruhen auf eForms-Bekanntmachungen ab 25.10.2023. Der Backtest der Iteration 5 nutzt auch ältere TED-Formulare: 41 der 52 Vorgänger stammen aus der Zeit vor eForms (`reports/backtest_iteration5.md`). Alle Messungen gelten nur oberhalb der EU-Schwelle, Haupt-CPV 909, Deutschland.

**Kleines Glossar** (Kennungen erscheinen in den Tabellen wieder).

| Begriff | Bedeutung |
|---|---|
| Los | Teil einer Ausschreibung mit eigenem Zuschlag; Einheit der Liste |
| Ende der Grundlaufzeit / Höchstende | Ende der ersten festen Laufzeit / Ende einschließlich aller Verlängerungsoptionen |
| Vergleichswert | Ende der Grundlaufzeit nach einer vorab committeten, neutralen Definition, gelesen von zwei KI-Lesern |
| Kriterien K, V, W, X, Y, Z, D | Schwellen, je Iteration neu vergeben und vor dem Ergebnis festgelegt; gelten nur in der genannten Iteration (V Iteration 3 und 9, W Iteration 4, 10 und 10b, X Iteration 5, Y Iteration 6 und 7, Z Iteration 8, D Paket D) |
| L, N, M mit Zahl | Nummer eines Loses in der Stichprobe (L Iteration 6 bis 8, N Iteration 9, M Iteration 10b), z. B. M54 |
| Regeln 1a, 1b, 6 bis 10 | Leseregeln der Liste; 1b: „das Enddatum der Bekanntmachung ist schon das Höchstende“; 6 bis 10 aus Iteration 9 |
| Stufe A bis F | Güteklasse je Listeneintrag (Herkunft des Endes): A aus Text gelesen oder unauffällig, B berechnet, C ohne Angabe, D unbestimmbar, E geschätzt, F kein Ende |
| diskordant | Liste und Vergabeweiser weichen um mehr als einen Tag ab oder eine Seite hat kein Datum |
| Wilson | 95-%-Konfidenzintervall für einen Anteil |
| Zuschlagsbekanntmachung | Veröffentlichung, dass ein Auftrag vergeben wurde (an wen, für welche Laufzeit) |
| naive Referenz (Baseline) | einfache Vergleichsregel, die eine Prognose übertreffen muss, um etwas zu taugen |
| Make or Buy | Entscheidung „selbst bauen oder kaufen/abonnieren“ |
| Push-Nachricht | Meldung, die von selbst im Arbeitswerkzeug (Teams, E-Mail) ankommt |

## 1. Business Understanding im Überblick

_Kurzfassung für den Dozenten. Quellen: `docs/business.md` §6 bis §8, `reports/wettbewerbsbild_oberpfalz.md`. Angaben aus Web-Recherche eines KI-Agenten und eines KI-Gutachtens sind nur dort „geprüft“, wo `docs/business.md` es vermerkt._

**Rahmen: die Entscheidung eines Gebäudereinigungsunternehmens (Wunsch des Nutzers).** Ein Betrieb, der für Kommunen und Behörden bietet, fragt: _Selbst bauen, kostenlos nutzen oder abonnieren?_ (Make or Buy). Kosten und Break-even rechnen wir nur mit Annahmen (Aufwand, Stundensatz, Pflege nicht gemessen; `reports/make_or_buy.md`); dass Eigenbau gegen kostenlose Dienste „nie günstiger“ ist, ist eine Modellkonstruktion und keine Messung. Ob es einen tragfähigen Business Case gibt, prüften wir mit einem vorab festgelegten Auswahlbogen (`docs/business_case_auswahl.md`).

**Ergebnis der Business-Case-Prüfung (Fakten, 2026-11-06 bis 11-09).**
- _Auswahlbogen:_ Acht Kandidaten (K-A bis K-H) wurden nach sieben Kriterien mit je 0 bis 2 Punkten bewertet (höchstens 14; Schwelle 8, vorab). Die höchste Summe war 7 (K-A, Amtsinhaber-Quote), also unter 8: **kein tragfähiger Business Case.** Die Kriterien wurden festgelegt, nachdem die Recherchen vorlagen (Bestätigungsgefahr).
- _Test K-A abgebrochen:_ Nach der vorab festgelegten Regel (Abbruch unter 30 verwertbaren Paaren) hatten nur 23 von 52 Paaren einen Zuschlag des Nachfolgers.
- _Nachtrag K-J_ (Push in Teams, Outlook, Planner per Power Automate; Evaluation 2026-11-08/09; Quellen, gelesen 2026-11-06, in Abschnitt 11 und `docs/quellen.md`; Details `docs/business_case_auswahl.md`): Den Ablauf gibt es schon kostenlos (TED-Suchprofile mit E-Mail-Alarm und RSS, Vergabeweiser-Alerts, Weiterleitung per Standard-Flow); die HTTP-Aktion in Power Automate ist Premium (13 € je Nutzer und Monat; laut Microsoft-Seite zu Flows mit Dienstprinzipal, indirekte Aussage). Das Problem „Suchaufwand“ ist in den drei Gesprächen nicht belegt; im Datensatz ergeben sich etwa 13 bis 19 Treffer pro Jahr und Profil (Profile erfunden). Punkte K1 bis K7 (Evaluator): 0 (wohlwollend 1), 0 (wohlwollend 1), 1, 1, 2 (Schätzung), 1, 0; Summe streng 5, wohlwollend 7 von 14, K7 = 0: **Ergebnis unverändert.** Billiger Test (nicht durchgeführt), Schwelle vorab am 2026-11-09: mindestens 2 von 3 Betrieben nutzen Teams oder Planner aktiv, nennen mindestens 1 Stunde pro Woche für Sichten und Übertragen und übertragen heute von Hand; sonst wird K-J verworfen.
- _Offen:_ Der billige Test (eine Stunde Alarm-Weiterleitung bauen, drei Anrufe mit vorab festgelegter Schwelle) ist vorbereitet, **nicht durchgeführt**; Hypothesen H1/H2 (Annahmen A21, A22) ungeprüft; Wizard-of-Oz-Blatt (`docs/wizard_of_oz_blatt.md`) nicht durchgeführt.

**Wie gehen Betriebe heute vor (Fakten).**
- Zugang zu Ausschreibungen: kostenlos über den Bekanntmachungsservice oeffentlichevergabe.de, Suchprofile auf TED und IHK-Dienste; kostenpflichtig über Dienste wie subreport (84 bis 198 € pro Monat), DTAD (Vertrieb) oder evergabe.de (83 € pro Monat) (`docs/business.md` §8.1). 63 % aller Vergaben 2024 nur nach Preis.
- Gespräche (n = 3, Hinweise; `docs/business.md` §8.9): Ein Betrieb mit etwa 120 Beschäftigten zahlt knapp 1.500 € pro Jahr für DTAD; ein Betrieb mit 15 Beschäftigten zahlt für kein Portal. Ob mitgeboten wird, entscheiden Entfernung, Personal und Kapazität; Vertragsenden bei anderen kennt keiner. Die Vergabestelle (Oberpfalz) verlängert „fast immer“, wenn eine Option im Vertrag steht (n = 1).

**Konkurrenz mit der Funktion „auslaufende Verträge“ (Fakten, Stand 2026-11-05).**

| Anbieter | Was er zeigt | Preis | Stand der Prüfung |
|---|---|---|---|
| Vergabeweiser | Verträge, die in 12 Monaten enden (1.005 in Gebäudereinigung), mit Zuschlagsempfänger, Angebotszahl, Optionen; nach eigener Angabe auch unterhalb der EU-Schwelle (von uns nicht gemessen); kostenlose API und Marktzahlen | kostenlos | Seite und API von uns geprüft und genutzt |
| AusschreibungsRadar | rund 26.000 Aufträge mit Ende in 1 bis 18 Monaten, „verlängerbar“ markiert, geschätzter Ausschreibungsmonat; ab Starter (29 €) volle KI-Eignungsanalyse, ab Business (79 €) Match-Score, Bid/No-Bid-Check und Wettbewerber-Tracking, Professional 149 € | 0 bis 149 € pro Monat | Seiten und Preisseite von uns gelesen; Nebentest mit 2 sicher zugeordneten Losen |
| aufträge.io, subreport, DTAD | aufträge.io: 43.373 Verträge mit Ende in 12 Monaten (auf Anfrage); subreport, DTAD: Ausschreibungsdienste, eine Funktion für auslaufende Verträge in unseren Quellen nicht belegt | subreport 84 bis 198 € pro Monat, DTAD knapp 1.500 € im Jahr | Recherche, Gespräch 1 |

Beide geprüften deutschen Anbieter schreiben selbst, dass der Auftraggeber entscheidet, ob und wann neu ausgeschrieben wird. Ein Profilfilter („Eignung“, „Match“) wird bei AusschreibungsRadar schon angeboten (`docs/business.md` §8.2).

### Warum wir eine Prognose für möglich hielten und was sie dem Betrieb gebracht hätte

**Fakten: die damalige Annahme.** Die Projektidee (`CLAUDE.md`, Abschnitt „Idee“) war eine Kette: Die Zuschlagsbekanntmachung nennt die Laufzeit. Damit ist das Vertragsende bekannt. Neu ausgeschrieben wird vor diesem Ende. Also sollte der Termin ungefähr „Vertragsende minus Vorlauf“ sein (Annahme A8 in `docs/annahmen.md`; Regel T3.2.2 in `docs/projektplan.md`). Die erste Stufe trug: Bei Gebäudereinigung war das Ende in 80,9 % der Zuschläge bestimmbar (Iteration 1, A13). Für den Anker wählte der Nutzer am 2026-10-30 das Höchstende, weil die Neuausschreibung in Iteration 4 meist erst nach dem Ende der Grundlaufzeit erschien (Median etwa 6 Monate danach, 11 Paare; `docs/business.md` §7.1).

**Fakten: der Nutzen für den Betrieb.** Das vorab festgelegte fachliche Kriterium lautete: Der Betrieb kann Angebot, Referenzen und Personal gezielt vorbereiten, statt Bekanntmachungen dauernd zu beobachten (§7.1). Im Gespräch 1 (rund 120 Beschäftigte, §8.9) kam die Meldung der letzten Ausschreibung 28 Tage vor Abgabe. Es wurde eng bei der Objektbegehung (ein Termin, bester Vorarbeiter krank), kalkuliert wurde nachts. Einen Hinweis 6 bis 12 Monate vorher fände der Betrieb „absolut“ hilfreich, um Personal in der Zielregion früher zu suchen. Der Kleinbetrieb (Gespräch 2) sagte „eigentlich nicht“, weil er Kapazität nicht 6 Monate im Voraus planen kann.

**Deutung.** Ein treffender Termin hätte einem größeren Betrieb statt rund 28 Tagen einige Monate für Begehung, Kalkulation, Personal und Referenzen gegeben. Getragen hat die Kette nicht, weil das Vertragsende kein Termin der Neuausschreibung ist. Ob eine Option gezogen wird, entscheidet die Verwaltung, und diese Entscheidung steht nicht in den TED-Daten. Die Vergabestelle verlängert „fast immer, wenn eine Verlängerungsoption im Vertrag steht“ (n = 1). Auch der im Nachhinein beste Vorlauf trifft nur 28,8 % (Abschnitt 3).

### Fachliches Erfolgskriterium (nachträglich formuliert, begründete Setzung)

> **Einordnung.** Ein fachliches Kriterium gab es seit 2026-11-04 (`docs/business.md` §7.1): Nutzen = „Der Betrieb kann Angebot, Referenzen und Personal gezielt vorbereiten, statt Bekanntmachungen dauernd zu beobachten“; Schwelle = Terminfenster ±3 Monate in mindestens 60 % und 10 Prozentpunkte über der naiven Referenz (vorab, vor dem Backtest). Es trug nicht (28,8 %). Die Schärfung unten wurde **erst nach Iteration 10** formuliert, ohne Kundenkontakt vor dem Projekt; sie ist eine begründete Setzung und kein vorab festgelegtes Kriterium.
>
> **Nutzen (Setzung).** Die Liste auslaufender Verträge ist ein Produkt, wenn ein Reinigungsbetrieb, der für Kommunen und Behörden bietet, damit früher als bisher weiß, wo sich ein Angebot vorzubereiten lohnt, und dafür zahlt.

| Bedingung (Setzung) | Begründung | Ergebnis (Stand 2026-11-05) |
|---|---|---|
| (i) Ein belegter Unterschied zur kostenlosen Konkurrenz | Wer dieselbe Information kostenlos bekommt, zahlt nicht | **Merkmalsunterschied, kein Qualitätsvorteil:** Ende je Los und der Grundlaufzeit; auf zwei Stichproben nur die Liste richtig bei 23 von 230 Losen (10,0 %), davon in 10b 11 von 15 Höchstende oder Losebene |
| (ii) Zahlungsbereitschaft von mindestens 2 von 3 größeren Betrieben über 50 € im Monat | ein Preis oberhalb des Free- und Starter-Niveaus der Konkurrenz | **nicht geprüft, in den Hinweisen gespalten:** nur ein größerer Betrieb erreicht; er nannte keinen Betrag für die Liste, für Wettbewerbsdaten „klang nach 50 bis 100 €“ (Einschätzung des Nutzers); der Kleinbetrieb „für gar nichts“ |
| (iii) Ausreichende Abdeckung der Zielregion | Fehlt der Vertrag in der Liste, hilft sie nicht | **Lücke der TED-Basis (Paket B, Hinweis):** Im Bekanntmachungsservice stehen 32 von 120 Oberpfälzer Reinigungsverfahren (26,7 %, Wilson 19,6–35,2 %) nicht auf TED; „national“ heißt „nicht auf TED gefunden“. Wert gegen die Schwelle nicht geprüft, B1 nicht entscheidbar. |

**Gesamturteil zum fachlichen Erfolgskriterium (Stand 2026-11-05).** (i) teilweise erfüllt (Merkmalsunterschied, kein Qualitätsvorteil); (ii) nicht prüfbar (nur ein größerer Betrieb erreicht); (iii) nicht entscheidbar (rund ein Viertel nicht auf TED, Wert gegen die Schwelle nicht geprüft). **Das Produkt als eigenes Angebot ist nicht belegt.** Die Sicht des Betriebs (Paket D, unten) ändert das nicht: Sie liefert eine Kostenrechnung unter Annahmen und einen Export, aber keinen Nachfragebeleg.

**Entscheidung gegen den gebauten LLM-Profilfilter.** Der Filter (Eignung eines Loses per Sprachmodell) wurde nicht verworfen, sondern nach einem billigen Test zurückgestellt: dem Wizard-of-Oz-Blatt (fünf echte laufende Oberpfälzer Lose, vom Betrieb zu bewerten; vorbereitet, **nicht durchgeführt**). Gründe: AusschreibungsRadar bietet KI-Eignungsanalyse ab 29 € und Match-Score ab 79 € schon; die Gesprächsgründe Personal, Kapazität und Bürokratie sind aus TED-Feldern kaum ablesbar; erst bauen und dann prüfen wiederholte den Fehler aus dem Marktgate (Lernpunkt unten).

### Risiken

| Risiko | Beleg (Fakt) | Gegenmaßnahme / Stand |
|---|---|---|
| Markt: Konkurrenz kostenlos | Vergabeweiser zeigt 1.005 Reinigungsverträge kostenlos; AusschreibungsRadar ab 0 € (A2 widerlegt) | eingetreten; Zyklus 4; Positionierung in einer Nische ungeprüft |
| Nachfrage | 3 Gespräche, gespalten; A1, A15 ungeprüft; Datenübergabe nicht erfragt | offen; keine Nachfrageaussage |
| Zielgruppe ohne IT | Kleinbetrieb ohne Verwaltungssystem (Gespräch 2); nur rund ein Drittel mit Branchensoftware (sekundär); Importschnittstellen nicht geprüft | Export hilft nur Betrieben mit Zielsystem; Kurztest vorbereitet, nicht durchgeführt |
| Pflege | Eigenbau 5 bis 50 Stunden je Jahr (Annahme); TED-Felder, Schema und Dienste ändern sich | in Rechnung als Annahme; nicht gemessen |
| Daten | TED nur oberhalb der EU-Schwelle (über alle Branchen 88 % der Vergaben darunter); 25,4 % der Oberpfalz-Lose ohne Ende; Zuschlagswert nur bei 47,7 %; die meisten Vorgänger heutiger Neuausschreibungen vor eForms (55 von 68 zusammengestellten Paaren; nach der Zweitprüfung 41 der 52 Backtest-Paare) | Paket B: Lücke von rund einem Viertel im Bekanntmachungsservice, Erweiterung nur als Ausblick |
| Listenfehler | 12 Lose (0,13 %), bei denen das Dauerfeld die Option schon enthält; bei 1 von 10 übereinstimmenden Losen beide Quellen falsch | Liste eingefroren; als offene Grenze genannt (Abschnitt 7) |
| KI-Methode | Regeln, Leser und Evaluator gleiche Modellfamilie; Menschenprüfung nur 14/15, durch Teammitglied Manuel Strobel (nicht unabhängig), nicht an den 15 diskordanten Losen | offengelegt; zweite Modellfamilie und Menschenprüfung fehlen |
| Recht | TED-Bekanntmachungen laut Rechtsseite frei wiederverwendbar mit Quellenangabe (Wortlaut am 2026-11-06 gelesen); Vergabeweiser CC BY 4.0 (Namensnennung); Bekanntmachungsservice CC0; bei Einzelunternehmern kann der Firmenname des Auftragnehmers einen Personennamen enthalten (Vorprüfung: 4 von 47 Namen ohne Rechtsform; Fassung ohne Auftragnehmer vorhanden); kein Scraping, nur einzelne Seiten von AusschreibungsRadar, `robots.txt` beachtet | Quellenangabe in Webseite, Export und Demos; Datenschutz siehe Abschnitt 11 |

**Mehrwert und Positionierung (Deutung, n = 3).** Der größere Betrieb sähe Nutzen in einem frühen Hinweis, würde aber eher für Wettbewerbsdaten zahlen (aktueller Auftragnehmer, alte Preise); der kleine will nichts zahlen. Aus TED allein sind diese Daten nur teilweise zu bekommen (130 Oberpfalz-Lose: Auftragnehmer 99,2 %, Zuschlagswert über 1 € 47,7 %, Angebote 60,8 %, alle drei 24,6 %).

**Competitive Edge, ehrlich.** _Was bleibt:_ ein Merkmalsunterschied auf Los- und Definitionsebene (nur die Liste richtig bei 23 von 230 Losen, Abschnitt 5), ein offen dokumentiertes Prüfverfahren und der Backtest, dass ein fester Abstand den Termin nicht vorhersagt. _Was nicht bleibt:_ Preis, Daten (offen), Wettbewerbsbild, Terminprognose; Vergabeweiser nennt nach eigener Angabe auch Verfahren unterhalb der EU-Schwelle, wir haben das nicht gemessen. _Ausblick, kein Vorteil:_ Daten unterhalb von TED (Zeile (iii)). _Nicht behauptet:_ dass die Liste genauer ist als Vergabeweiser, dass Vergabeweiser falsch liest, dass ein Marktvorteil besteht oder dass Betriebe die Liste nachfragen oder bezahlen.

**Perspektive des Betriebs (Make or Buy; Paket D).** Rahmen und Ergebnis stehen oben; Modell und Szenarien in Abschnitt 5. Im Basismodell ist Eigenbau gegen Vergabeweiser und AusschreibungsRadar Starter nie günstiger (Modellkonstruktion, keine Messung), gegen ein Abo wie DTAD nur im Szenario „niedrig“; symmetrisch gerechnet 1,0 bis 12,0 Jahre. _Deutung:_ „Keine Abo-Kosten“ trägt nicht, weil kostenlose Wege existieren und der Eigenbau Betriebs- und Pflegekosten hat.

### Lernpunkt: Die Konkurrenz wurde erst spät gesehen (Prozessfehler)

- **Fakten.** Der Projektplan sah früh vor, die Wettbewerber zu sichten (G1.1); sie blieb offen. Am 2026-10-24 fanden zwei Suchen von Claude keinen deutschen Dienst für auslaufende Verträge (`docs/business.md` §6). Am 2026-10-29 entschied der Nutzer gegen Kundenkontakt; G1.1 wurde erst am 2026-11-05 erledigt.
- **Deutung und Konsequenz.** Ein Prozessfehler, nicht nur ein Suchfehler der KI: Keine Stelle erzwang G1.1 vor der Modellierung. Phase 1 braucht ein **Marktgate vor der Modellierung** (Wettbewerber gesichtet und dokumentiert; jede Streichung eines Plan-Punktes braucht eine Ersatzprüfung). Kosten: Zyklus 4; die Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos gibt.

## 2. Zyklus 1: Zuordnung zum Vorgänger (Iteration 1 bis 4)

Business Understanding: Kandidaten für eine Nische waren Gebäudereinigung, IT-Wartung, Winterdienst, Sicherheit, Kantine; Kriterium war genug Zuschläge mit Laufzeit. Datenbasis: TED Search API v3, Rohdaten unverändert in `data/raw`.

| Iteration (Datum) | Frage | Kriterium vorab | Ergebnis (Fakten) | Entscheidung |
|---|---|---|---|---|
| 1 (10-22) | Sind die Daten für eine Nische machbar? | genug Zuschläge mit bestimmbarer Laufzeit | Laufzeitende bei Gebäudereinigung 90,0 % bestimmbar (streng 80,9 %); Verlängerungsfeld BT-58 nur 18,9 % befüllt (A5 widerlegt); Wertfelder mit Platzhaltern (A6 widerlegt) | Gebäudereinigung vorläufig; weiter |
| 2 (10-23) | Genügen Auftraggeber + CPV, um einen neuen Auftrag dem Vorgänger zuzuordnen? | K2 ≥ 80 % | K2 = 5/30 = 16,7 % (Wilson 7,3–33,6); 629 abgelaufene eForms-Verträge; Median-Laufzeit 12 Monate | Zuordnung über das Objekt (Adresse, Titel) versuchen |
| 3 (10-24/25) | Trägt eine Objekt-Regel? | Sichtbarkeit eines Vorgängers (V1), Präzision (V2) ≥ 80 %, Trefferquote (V3) ≥ 60 % | V1 63,3 %, V2 45,8 %, V3 28,9 %; auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test 11 von 24 korrekt | Regel verworfen; letzter Versuch auf neuen Testdaten |
| 4 (10-25 bis 10-30) | Verbessert eine erweiterte Regel auf neuen Testdaten? | W2 Präzision, Mindestzahl 25 Vorschläge; W3 Trefferquote ≥ 60 %; W4 Zweitprüfung des Nutzers ≥ 85 % | W2 17/19 = 89,5 %, aber nur 19 Vorschläge; W3 56,7 %; W4 13/20 = 65 % | **Idee anpassen:** keine weitere Zuordnungsregel; Vertragsliste aus den Zuschlägen selbst |

_Deutung._ Große Auftraggeber vergeben viele Verträge parallel; die Kennung reicht nicht. Vor eForms liefert `REF_NOTICE` die Laufzeit (A11: 25/30).

_Phasen:_ Business Understanding und Data Understanding (Iteration 1 und 2: Nische, Machbarkeit), Data Preparation und Modeling (3 und 4: Zuordnungsregel), Evaluation (Blindprüfung, Handsuche), Deployment entfällt; Rücksprung innerhalb des Zyklus nach jeder verfehlten Schwelle.

_Für Laien: Wir wollten einen neuen Auftrag automatisch seinem Vorgänger zuordnen. Das gelang auch mit besserer Regel nicht zuverlässig genug, also haben wir diesen Weg aufgegeben._

**Datenqualität auf einen Blick (Data Understanding).** „Alle DE“ = 15.706 deutsche Zuschläge, 22.07. bis 21.10.2026, je Bekanntmachung; „CPV 909“ = davon 440 Reinigungs-Bekanntmachungen; „Reinigung eForms“ = 4.307 Zuschläge Haupt-CPV 90910/90911/90919, Okt. 2023 bis Sept. 2026; „Liste“ = Vertragsliste Fassung 9, je Los.

| Feld/Prüfung | Befund (Zahl, Bezugsmenge) | Behandlung | Quelle |
|---|---|---|---|
| Ebene | Alle DE: 15,3 % der Bekanntmachungen mit mehr als einem Los. Liste: 9.325 Lose aus 4.011 Zuschlägen; 101 Lose mit nicht eindeutiger Feldliste; 590 Lose ohne Zuschlag | Iteration 1 je Bekanntmachung („befüllt“ = mindestens ein Los); Liste je Los; Lose ohne Zuschlag entfernt (Regel 7) | `reports/datenqualitaet_DEU_20260722_20261021.md` §1, §6; `reports/vertragsliste_iteration9.md` |
| Laufzeitende bestimmbar (Enddatum, oder Beginn + Dauer) | Alle DE 61,7 %; CPV 909 80,9 %; Reinigung eForms: keine verwertbare Laufzeit 22,4 %; Liste: 73 % aller Lose, 79,4 % im letzten Jahr | Kein geschätztes Ende als Enddatum; Lose ohne Ende bleiben ohne Ende | `reports/datenqualitaet_…md` §5; `reports/verlaengerung_praxis_iteration5.md`; `reports/vertragsliste_iteration9.md` |
| Bedeutung des Enddatums (BT-537) | Reinigung eForms: in 274 von 289 Fällen (94,8 %) kürzer als die im Text genannte Höchstlaufzeit | Gilt als Ende der Grundlaufzeit; Höchstende aus dem Freitext | `reports/verlaengerung_praxis_iteration5.md` |
| Verlängerungen (BT-58) | Alle DE: vorhanden 18,9 %, > 0 bei 14,7 %; CPV 909: > 0 bei 42,0 %; Reinigung eForms mit Ende: > 0 bei 1.048 von 3.279 (32,0 %). Die Länge steht nur im Freitext | A5 widerlegt; Länge und Höchstende aus BT-57/BT-54 mit Lese-Regeln | `reports/datenqualitaet_…md` §2, §4; `docs/annahmen.md` A5; `reports/verlaengerung_praxis_iteration5.md` |
| Laufzeit (Monate) | Alle DE aus Beginn/Ende (n = 9.459): Median 16, Quartile 7 und 36; CPV 909 (n = 350): Median 36, Quartile 24 und 48. BT-36 nur bei 21,3 % befüllt | Laufzeit aus Beginn und Ende statt aus BT-36 | `reports/datenqualitaet_…md` §2, §5 |
| Unplausible Laufzeiten (≤ 0 oder > 240 Monate) | Alle DE: 14 Datumspaare; Liste: 9 von 3.503 Losen (0,3 %, letztes Jahr) | Verworfen, Los zählt als ohne Ende | `reports/datenqualitaet_…md` §5; `reports/vertragsliste_iteration9.md`; `src/prepare/vertragsliste.py` |
| Zuschlagswert | Alle DE: Wert > 1 € 58,8 %, `-1` in mindestens einem Wertfeld 25,6 %; CPV 909: Wert > 1 € 51,4 %; Oberpfalz (130 Lose): Wert je Los > 1 € 47,7 %, Platzhalter ≤ 1 € 36,2 % | `-1` = „nicht veröffentlicht“ (A7, 2 Fälle); 0 € und 0,01 € sind Platzhalter (A6) und zählen nicht als Wert | `reports/datenqualitaet_…md` §2, §6; `docs/annahmen.md` A6, A7; `reports/wettbewerbsbild_oberpfalz.md` |
| Auftragnehmer | Oberpfalz (130 Lose): genannt bei 129 (99,2 %) | keine | `reports/wettbewerbsbild_oberpfalz.md` |
| Daten vor eForms | Zuschläge vor eForms (CPV 909, 30 zufällige): 0 von 30 mit eigener Laufzeit; über `REF_NOTICE` bestimmbar bei 25 von 30 (83,3 %) | Laufzeit aus der verknüpften alten Ausschreibung (XML) | `reports/a11_stichprobe.md` |

_Deutung:_ Ein Ende der Grundlaufzeit steht bei etwa drei von vier Reinigungslosen in den Feldern; weiter kann die Liste nicht reichen. Das Höchstende hängt am Freitext, und ob eine Option gezogen wird, steht in keinem Feld; das begrenzt jede Terminprognose (Abschnitt 3).

## 3. Zyklus 2: Terminprognose (Iteration 5)

| Iteration (Datum) | Frage | Kriterium vorab | Ergebnis (Fakten) | Entscheidung |
|---|---|---|---|---|
| 5 (10-30 bis 11-04) | Sagt „Höchstende − 6 Monate“ (R1) den Termin der Neuausschreibung voraus? | Treffer = Fenster ±3 Monate; X3: ≥ 60 % und ≥ 10 Prozentpunkte über der Baseline R0 (Ende der Grundlaufzeit − 6 Monate); Schwelle vor jeder Berechnung festgelegt | 52 von Hand bestätigte Paare (Zweitprüfung 61/67 = 91,0 %, mit KI-Hilfe, nicht als unabhängig gewertet): R1 28,8 % (Wilson 18,3–42,3), R0 17,3 %; 20 Neuausschreibungen kamen mehr als 3 Monate früher, 17 später | **Idee anpassen:** keine Terminprognose; Produktkern ist die Vertragsliste mit Enddaten |

_Phasen:_ Business Understanding (Prognoseziel und Schwelle vorab), Data Preparation (Zuschlagstabelle), Modeling (Regel R1 gegen Baseline R0), Evaluation (52 Paare, Zweitprüfung), Deployment entfällt.

_Für Laien: Wir haben getestet, ob ein fester Abstand zum Vertragsende den Termin der Neuausschreibung trifft. Er traf nur in 28,8 % der Fälle (gefordert: 60 %); eine einfache Vergleichsregel kam auf 17,3 %._

_Data Preparation:_ Zuschlagstabelle je Los (`src/prepare/vertragsliste.py`) mit Ende der Grundlaufzeit, Höchstende und Herkunft; Leakage vermieden (nur Wissen zum Zeitpunkt des Vorgänger-Zuschlags). _Deutung:_ Der Termin ist zweigipflig verteilt; ein fester Abstand trägt nicht; die Vergabestelle stützt das (Verlängerung ist der Normalfall).

**Nachtrag Sensitivität (2026-11-09; nachträgliche Obergrenze, kein neuer Test).** Quelle: `reports/sensitivitaet_iteration5.md`, erzeugt von `src/model/sensitivitaet_backtest.py` aus der Paartabelle des Backtest-Berichts. Vorlauf und Fenster wurden im Nachhinein auf denselben 52 Paaren variiert; das beste Ergebnis ist deshalb optimistisch.
- Bester Vorlauf (0 bis 24 Monate, Fenster ±3) ist der vorab gesetzte: 6 Monate mit 15 von 52 = 28,8 %. Für 60 % wären 32 Treffer nötig.
- Erst ein breites Fenster hebt die Quote: ±6 Monate 16/52 = 30,8 %, ±12 Monate 26/52 = 50,0 %. Ein Jahr Unsicherheit hilft bei der Planung kaum.
- R1 gegen R0 auf denselben Paaren: nur R1 trifft bei 10 Paaren, nur R0 bei 4. Exakter McNemar-Test p ≈ 0,18. Der Vorsprung von R1 vor der naiven Referenz ist nicht gesichert.

**Warum eine feste Regel und kein gelerntes Modell?** Unser Vorgehen sah „einfach vor komplex“ vor, ein statistisches oder ML-Modell „nur wenn die Regeln klar an Grenzen stoßen“ (`docs/CRISP-DM.md`, Phase 4; `docs/projektplan.md`, T4.4.1). Deshalb haben wir die vorab eingefrorene Regel R1 gegen die naive Referenz R0 getestet; „es werden keine Parameter aus den Paaren geschätzt“ (`src/model/baseline.py`). Es gab nur 52 geprüfte Paare, und ob eine Option gezogen wird, ist aus dem Zuschlag des Vorgängers nicht lesbar (`reports/evaluation_iteration5.md`); die Vergabestelle sagte später, verlängert werde „fast immer, wenn eine Verlängerungsoption im Vertrag steht“ (`docs/business.md` §8.9, n = 1). _Deutung:_ Für Training und getrennten Test eines gelernten Modells (z. B. Klassifikation oder Überlebenszeitmodell) reichen 52 Paare nicht, und es hätte dieselben Merkmale wie die Regel; weil selbst der nachträglich beste Vorlauf bei 28,8 % bleibt, sehen wir dafür wenig Spielraum. Eine feste Regel ist zudem für einen Betrieb nachvollziehbar. Ein Modell bräuchte deutlich mehr Paare und Merkmale zur Verlängerungsentscheidung des Auftraggebers (Abschnitt 7, Ausblick).

**Grenzen des Backtests (offen benannt).**
- _Leck zwischen Entwicklung und Test:_ Das Prognoseziel (Höchstende) wurde gewählt, nachdem die Vorlaufzeiten derselben Paare in Iteration 3 und 4 explorativ angesehen worden waren (`reports/backtest_iteration5.md`, Grenzen; `docs/business.md` §7.1: „Median etwa 6 Monate“ nach der Grundlaufzeit). Der Vorlauf von 6 Monaten wurde gesetzt, nicht aus den Paaren geschätzt (`docs/projektplan.md`, T3.2.1). Das Leck begünstigt R1. Die Sensitivität zeigt, dass es das Ergebnis nicht ändert.
- _Überlebensverzerrung:_ Die Paare stammen aus einer Rückwärtssuche, von der neuen Ausschreibung zum Vorgänger. Verträge, die verlängert und nicht neu ausgeschrieben wurden, fehlen. Die Quote ist deshalb keine Präzision einer späteren Liste (`reports/evaluation_iteration5.md`).
- _Formate:_ 41 der 52 Vorgänger stammen aus der Zeit vor eForms; die Leseregeln für das Höchstende wurden nur an eForms getestet.

## 4. Zyklus 3: Qualität der Vertragsliste (Iteration 6 bis 9)

| Iteration (Datum) | Frage | Kriterium vorab | Ergebnis (Fakten) | Entscheidung |
|---|---|---|---|---|
| 6 (11-04) | Wie genau ist der Prototyp (Oberpfalz, 146 Lose, Stufen A–F)? | Y1 Ende der Grundlaufzeit ≥ 90 % an 60 Zufallslosen (Prüfung durch den Nutzer); Y3 Abdeckung ≥ 80 % | Y1 54/60 = 90,0 % laut Auswertung, 53/60 = 88,3 % nach Fehler L60; Höchstende 91,7 %; Abdeckung 79,7 % (damalige Fassung). Die Vorlage zeigte den Listenwert (Verankerung, vom Evaluator gefunden) | Zurück zu Phase 3: Regel 1b, neue Stichprobe |
| 7 (11-04) | Behebt Regel 1b den Fehlertyp „Enddatum ist schon Höchstende“? | Y1 ≥ 90 %, Y1r ≥ 12/15 Regelwirkungs-Lose; vorab: Y1 zwischen 70 und 90 % → kein dritter Regelversuch | Y1 36/47 = 76,6 % (Wilson 62,8–86,4), Y1r 8/15, Höchstende verfehlt. Mischmaß aus Listen- und Prüfungsfehlern (bei 45 von 47 Losen schrieb die Nachprüfung dasselbe Feld ab) | Abschluss mit diesem Stand; Ende „laut Bekanntmachung“, Höchstende nur Hinweis |
| 8 (11-04/05) | Bestätigen zwei KI-Leser die Liste? | Z0 Leser untereinander ≥ 90 %, Z1 bis Z4 (Liste gegen Vergleichswert, Regelwirkung, Höchstende, Kontrolle) | Z0 94/95; Z1 77/80 = 96,25 %; Z2 14/15 (bei einheitlichem Maßstab 11/15, verfehlt); Z3 75/80 und 67/72; Z4 10/10. Neue Listenfehler: Lose ohne Zuschlag, Übertragung von Werten, „3 Jahre mit Option“ | Weiter (Projektabschluss), eingeschränkt: Leser nicht unabhängig, nicht von Menschen bestätigt |
| 9 (11-05) | Beheben Regeln 6 bis 10 diese Fehler; hält die Liste auf einer neuen Stichprobe (Seed 20261109, 110 Lose)? | V1 ≥ 90 %, V2 bis V8 (u. a. Höchstende V4, Lose ohne Zuschlag V7, Verfahren V8) | Liste 9.325 statt 9.915 Lose; V1 66/70 = 94,3 % (Wilson 86,2–97,8); V2 28/30; V3 66 gegen 65 von 70 (alte Fassung); V5 110/110; V6 Teammitglied Manuel Strobel 14/15. **Verfehlt:** V4 (87,1 % bei Schwelle 90 %), V7 (Los N51); V8 teilweise | Weiter, eingeschränkt: Fassung 9 wird Prototyp, Höchstende nur Hinweis; „V1 bis V8 erfüllt“ wird nicht behauptet |

_Phasen:_ Rücksprung zu Phase 3 und 4 (Regeln 1b, 6 bis 10), Evaluation je Iteration an neuen Stichproben, Deployment: Prototyp der Webseite (Abschnitt 6).

_Für Laien: Wir haben die Liste der Vertragsenden mehrfach an Stichproben geprüft und die Leseregeln verbessert. Zuletzt ist das Ende bei 66 von 70 Verträgen gleich wie der Vergleichswert zweier KI-Leser; „fehlerfrei“ ist das nicht belegt._

**Abdeckung (Zähler und Nenner, an einer Stelle).** Quelle: `data/processed/vertragsliste_909.csv` (Fassung 9) und `reports/vertragsliste_iteration9.md`, nachgerechnet.
- **Alle Lose:** 6.803 von 9.325 haben ein Ende der Grundlaufzeit, **rund 73 %** (72,95 %); 2.522 Lose (27,0 %) haben keines.
- **Letztes Jahr (X4):** Unter den Losen aus Zuschlägen, veröffentlicht 2025-10-01 bis 2026-09-30, haben 2.783 von 3.503 ein Ende; der **Anteil der Lose mit Enddatum** ist **79,4 %** (eine Abdeckung, keine Genauigkeit) (Wilson 78,1–80,8; Schwelle 80 % knapp verfehlt). Der Anteil schwankt nach Halbjahr zwischen 63,6 % und 80,7 %; das letzte Jahr liegt deshalb über dem Gesamtwert.
- **Lose ohne Ende:** über alle Lose 27,0 %, im letzten Jahr 20,6 %.

_Deutung._ Die Fassung 9 ist auf der Stichprobe zu 94,3 % mit dem Vergleichswert identisch (alte Fassung 92,9 %, bloßes Feld 90,0 %). Der Nutzen der Regeländerung ist nicht gesichert: Die Stichprobe trennt die Fassungen kaum, der Vergleichswert ist teilweise zirkulär, V5 zeigt vor allem gleiche Anweisung und gleiche Rohtexte. _Grenzen:_ gleiche Modellfamilie von Regel, Leser und Evaluator; V6 mit 15 Losen dünn. Der einzige menschliche Leser der Fassung 9 (14/15) ist Teammitglied Manuel Strobel und damit nicht unabhängig; auch die Prüfungen der Iterationen 6 und 7 machte ein Teammitglied, der Nutzer (`docs/beitraege.md`, `docs/zeitprotokoll.md`). Details: `docs/iterationen.md`, `reports/evaluation_iteration7.md` bis `_iteration9.md`.

## 5. Zyklus 4: Business Understanding und Wettbewerb (Iteration 10 und 10b)

_Anlass (2026-11-05, nach Iteration 9): Der Dozent verlangt mehr Gewicht auf Business Understanding; die Sichtung der Wettbewerber war nie erfolgt (Abschnitt 1). Abweichend von „keine weitere Iteration“ beschloss der Nutzer einen Rücksprung zu Phase 1. Stichprobe und Vergleichswert der Iteration 9 dienten als fester Maßstab._

_Phasen:_ Rücksprung zu Phase 1 (Business Understanding), dann Data Understanding (Vergabeweiser-API, Bekanntmachungsservice), Evaluation (10b, Pakete), Deployment nur als Veranschaulichung (Abschnitt 6).

_Für Laien: Wir haben geprüft, was es am Markt schon gibt und ob sich mit der Liste ein Geschäft machen lässt. Ergebnis: Die Liste gibt es kostenlos, ein Geschäft ist nicht belegt._

**Iteration 10: Business Understanding und Wettbewerber.** Recherche (KI-Agent plus KI-Gutachten aus BWL-Sicht, einzelne Seiten von Claude nachgelesen): Vergabeweiser bietet eine kostenlose Liste auslaufender Verträge samt API, AusschreibungsRadar eine günstige; **A2 („es gibt keinen deutschen Dienst“) ist widerlegt.** Das Gutachten hielt das Kernprodukt „Liste“ für nicht tragfähig (`docs/business.md` §8.4, §8.5). Gespräche (W5, Leitfaden vorab): neun Anrufe, drei Stellen erreicht (zwei Reinigungsbetriebe, eine Vergabestelle); Notizen ohne Namen. Zahlungsbereitschaft zeigte sich nur für Wettbewerbsdaten; die Vergabestelle bestätigt, dass das Vertragsende kein Neuausschreibungstermin ist. n = 3, Hinweise.

**Vorgehen.** Vergabeweisers API (Rohantworten in `data/raw/vergabeweiser_20261105/`) liefert das Vertragsende je Verfahren, nicht je Los; die Zuordnung eines Loses lief per Skript ohne Handentscheid. **Hypothese** _(vorab, vor dem Abruf)_: Auf den 70 Zufallslosen der Iteration 9 stimmt Vergabeweiser seltener mit dem Vergleichswert überein als die Liste (66/70). In 10b (Seed 20261112, 160 neue Lose mit Listenende) lasen zwei KI-Leser nur die diskordanten Lose, ohne Quellenangabe, nach der neutralen Definition; Hypothese vorab: die Liste trifft häufiger, und der Unterschied reicht über die Granularität hinaus.

| Kriterium (vorab) | Schwelle | Ergebnis (Fakten) | Urteil |
|---|---|---|---|
| W1 (Iteration 10, 70 Lose) | Differenz Liste − Vergabeweiser ≥ 5 Lose | Liste 66/70, Vergabeweiser 58/70, +8, exakter Test p = 0,0078; Ursachen der 8: Losebene 4, Höchstende statt Grundlaufzeit 2, fehlender Wert 1, 2 Tage 1; Basisregel „Feld EndDate“ 63/70 | formal erfüllt, überwiegend Los- und Definitionsunterschied; zählt Vergabeweisers Verfahrensdatum als richtig, wenn es irgendeinem Los entspricht, sinkt die Differenz auf +4 |
| W8a (10b) | ≥ 16 Lose (10 %) und p < 0,05 | 15 von 160 Losen diskordant; Leser 15/15 einig; Liste 15/15, Vergabeweiser 0/15; +15, p = 0,0001 | **formal verfehlt, rechnerisch unerreichbar** (Schwelle aus der Diskordanzrate der Iteration 10 übernommen, Fehler der Vorab-Festlegung) |
| W8b (10b) | ≥ 8 Lose und p < 0,05, Vergabeweiser gilt auch bei Datum irgendeines Loses desselben Verfahrens als richtig | +10, p = 0,0020 | erfüllt, schwach aussagekräftig |
| W7 Nebentest AusschreibungsRadar | beschreibend (Seed 20261111, 15 Lose) | nur 2 von 15 sicher zugeordnet, beide wie Liste und Vergleichswert | keine Aussage zur Genauigkeit möglich |

**Einordnung der 15 diskordanten Lose (Evaluator, je Los am Rohtext).** Höchstende statt Grundlaufzeit 7 (eine einzige Textvorlage), Losebene 4, Zuordnungsfehler der Pipeline 1 (M54), Ursache offen 2, mehrdeutig 1. Zählt das Höchstende für Vergabeweiser als richtig, bleiben 3 : 0, p = 0,25. Beide Stichproben zusammen: Abweichung bei 27 von 230 Losen = 11,7 %, davon nur die Liste richtig bei 23 von 230 = 10,0 % (Wilson 6,8–14,6 %). _Grenze:_ Die Werte sind roh aus zwei verschieden gezogenen Stichproben zusammengelegt. Einzeln: Abweichung 12/70 = 17,1 % (Iteration 10) und 15/160 = 9,4 % (10b), nur die Liste richtig 8/70 = 11,4 % und 15/160 = 9,4 % (`reports/evaluation_iteration10b.md`).

**Deutung.** Der Unterschied zugunsten der Liste ist ein **Merkmalsunterschied** (Ende je Los, Grundlaufzeit statt Höchstende), kein belegter Qualitätsvorteil beim Lesen: Liste und Vergabeweiser nutzen dasselbe TED-Feld, gemeinsame Fehler bleiben unsichtbar, die Leser stammen aus derselben Modellfamilie wie die Regeln.

**Pakete A, C, F und B (Nachträge, Entscheidung des Nutzers 2026-11-05).**
- **A, Wettbewerbsbild aus TED** (`reports/wettbewerbsbild_oberpfalz.md`): Zahlen siehe Abschnitt 1; Handabgleich von 5 Losen 5 von 5. Deutung: Ein Wettbewerbsbild aus TED allein ist nur zu etwa einem Viertel der Lose vollständig.
- **C, Ursachen der Lücken** (`reports/stufe_f_ursachen.md`): Die 33 Lose ohne Ende haben alle keine Laufzeitfelder im XML. Dabei fand sich der Fehlertyp „Dauerfeld enthält die Option schon“: **12 Lose in 5 Bekanntmachungen, 0,13 % der 9.325 Lose**; zwei Fälle am Rohtext bestätigt.
- **F, Optionsanalyse** (`reports/optionsanalyse.md`): Bei belegter Option (n = 24 von 52 Backtest-Paaren) lag die Neuausschreibung in 70,8 % zwischen dem Ende der Grundlaufzeit und dem Höchstende (Wilson 50,8–85,1). Hinweis, kein Beleg.
- **B, Abdeckung unterhalb der EU-Schwelle (A3, Oberpfalz)** (`reports/oeffentlichevergabe_test.md`, `_robustheit.md`). _Hypothese und Kriterien (vorab, `0e83dfa`):_ Mindestens ein Drittel der Oberpfälzer Reinigungsverfahren (Haupt-CPV 909) liegt unterhalb der EU-Schwelle (B1 ≥ 33 %); B2 bis B5: Feldabdeckung, Überlappung mit der Liste, Handabgleich von 5 Verfahren, Machbarkeit. Daten: OCDS-Jahresdateien des Bekanntmachungsservice 2024 bis 2026 (CC0, 626.620 Datensätze), ohne Kennzeichen für die Schwelle; „national“ heißt „nicht auf TED gefunden“.
  - _Erste Auswertung (Filter NUTS-3-Code am Lieferort):_ 84 Verfahren, alle auf TED, 0 national. _Artefakt:_ Nationale Verfahren tragen am Lieferort zu 71,2 % nur den NUTS-1-Code „DE2“ (EU-Verfahren zu 92,4 % einen NUTS-3-Code); der Filter schloss sie aus. Die erste Auswertung („B1 deutlich verfehlt“) ist nicht gültig.
  - _Ergebnis (Postleitzahl, Ortsliste):_ 32 von 120 Verfahren nicht auf TED = 26,7 % (Wilson 19,6–35,2 %; Jahreswerte 13 bis 45 %). **B1 ist nicht entscheidbar**, das Intervall schließt 33 % ein. 62 von 64 Bekanntmachungen der Liste stehen im Datensatz.
  - _Deutung:_ Rund ein Viertel der Reinigungsverfahren im Bekanntmachungsservice fehlt auf TED: ein Hinweis auf eine Lücke der TED-Basis und ein Argument für die Erweiterung als Ausblick, **kein belegter Vorsprung**. A3 bleibt ungeprüft; die Aussage der Vergabestelle (n = 1) ist weder bestätigt noch widerlegt. _Lernpunkt:_ Eine Null ist ein Verdachtsmoment, kein Ergebnis.
  - _Grenzen:_ „National“ ist nicht „unterhalb der Schwelle“; Ortsregeln nicht von Hand geprüft; B2 und B4 stehen aus.

- **D, Perspektive des Betriebs (Make or Buy, Datenübergabe)** (`docs/business.md` §9; Stand: **Test vorbereitet, nicht durchgeführt**). _Vorab (2026-11-06):_ H1 Ein befragter Betrieb mit Branchensoftware kann Treffer nicht ohne Abtippen übernehmen; H2 ein Betrieb könnte eine CSV mit festem Schema laden. D1 Modell mit Break-even; D2 Export mit Schema; D3 Test mit 1 bis 3 Betrieben durchgeführt; D4 „Datenübergabe ist relevant“ nur, wenn H1 und H2 bei mindestens 2 von 3 bestätigt sind.
  - _Fakten:_ **D1 ja**, **D2 ja** (Schema 1.1, 26 Felder: CSV, CSV deutsch, JSON, dazu Variante ohne Auftragnehmer; vom Skript gegen das Schema validiert, in Excel nicht getestet), **D3 nein**, **D4 offen**.

| Szenario (Annahme, Basismodell) | Kosten 3 Jahre | Break-even gegen DTAD | gegen Vergabeweiser, AusschreibungsRadar Starter | zusätzliche Aufträge in 3 Jahren (Marge 5 %) |
|---|---|---|---|---|
| Niedrig (20 h einmalig, 5 h/Jahr) | 3.500 € | 2,0 Jahre | nie | 0,14 |
| Mittel (60 h, 20 h) | 12.000 € | nie | nie | 0,48 |
| Hoch (120 h, 50 h) | 27.000 € | nie | nie | 1,08 |

  - _Deutung:_ „Nie günstiger“ ist eine Modellkonstruktion (Annahmen). „Keine Abo-Kosten“ trägt nicht; ein Mehrwert müsste aus Funktion kommen. Die „zusätzlichen Aufträge“ (Deckungsbeitrag 25.110 € je Auftrag, Median-Jahresumsatz 167.404 €) sind eine Größenordnung, kein Nutzenbeleg. _Grenzen:_ Aufwände, Marge und Stundensatz nicht gemessen; keine Aussage zur Relevanz der Datenübergabe (D3 nein).

- **Nach Iteration 10b (2026-11-06 bis 11-09; Fakten, kein Erfolg behauptet).** (1) Business-Case-Auswahl mit vorab festgelegten Kriterien: kein tragfähiger Case (Abschnitt 1). (2) Demo Profil-Match mit Push-Vorschau, auf Wunsch des Nutzers nach dem Auswahlbogen gebaut (K7 = 0): Veranschaulichung der Datenübergabe, kein Business Case; Abnahmekriterien A1 bis A7 vorab, aber keine Hypothese zu Nachfrage oder Genauigkeit (`docs/demo_push.md`). (3) Live-Demo mit großem Datensatz und Filterlauf. (4) Video „Franz und die Glaskugel“, Fassungen v1 bis v4; aktuell v4 mit Edge-Stimmen; eine Fassung nach v4 ist in Arbeit (Manuel). (5) Umbau der Folien auf zehn sichtbare Folien. (6) Prüfung von K-J (Abschnitt 1). Ergebnisse zum Anfassen: Abschnitt 6.

**Abweichungen von der Vorab-Planung (offen).** Zuordnungsweg 2 nach dem Trockenlauf ergänzt; Abrufskript nach DNS-Fehler angepasst; Nebentest W7 nach Beginn des Abrufs.

### Entscheidung (2026-11-05, Nutzer): Weiter, Projektabschluss, eingeschränkt formuliert
- **Begründung.** W1 ist formal erfüllt, aber überwiegend Los- und Definitionsunterschied; W8a ist formal verfehlt wegen eines Fehlers der Vorab-Schwelle, W8b erfüllt. Nach der Vorab-Regel gilt „kein belegter Vorteil im definierten Maß“, und das ist nicht als Gleichheit zu lesen. Befund: Merkmalsunterschied, kein belegter Qualitätsvorteil, Nachfrage offen.
- **Abweichung von der Vorab-Folge (offen begründet).** „W8a verfehlt → ‚kein Vorteil gegenüber Vergabeweiser‘ gilt weiter“ wird nicht übernommen, weil sie der gemessenen Richtung widerspricht und die Schwelle unerreichbar war; „Die Liste ist genauer“ wird ebenso wenig behauptet.
- **Geschäftlich.** „Liste als eigenes Produkt nicht tragfähig“ (`docs/business.md` §8.4) bleibt bestehen; A2 bleibt widerlegt; A1, A3 und A15 bleiben ungeprüft. Weitere Grenzen: Abschnitt 7; das Protokoll der Leserläufe 10b liegt außerhalb des Repos.

## 6. Ergebnisse zum Anfassen: Vertragsliste, Webseite, Demo und Video

_Alle Dateien liegen im Repository. Sie veranschaulichen die Datenübergabe, sind **kein Business Case** (K7 = 0) und belegen weder Nachfrage noch KI-Genauigkeit noch einen Vorteil gegenüber den bestehenden Diensten. Screenshots: Abschnitt 11._

| Ergebnis | Datei | Was es zeigt (Fakten) | Grenzen |
|---|---|---|---|
| Vertragsliste (Fassung Iteration 9) | `data/processed/vertragsliste_909.csv` (nicht im Git, erzeugbar), Export `docs/prototyp/export/` (Schema 1.1, `docs/export_schema.md`) | 9.325 Lose; je Los Ende der Grundlaufzeit, Höchstende (nur Hinweis) und Herkunft in den Stufen A bis F (Glossar); 6.803 Lose mit Ende | Ende „laut Bekanntmachung“; „korrekt“ nicht belegt (Abschnitt 4) |
| Webseite | `docs/prototyp/vertragsliste.html` | Prototyp für die Oberpfalz (130 Lose aus 64 Bekanntmachungen, Stand 04.11.2026) mit Filtern (Suche, Auftragnehmer, Region, Status, Stufe, Zeitraum), CSV-Export der Auswahl, Hell/Dunkel/Automatisch | Prototyp, Darstellung; kein Produkt |
| Demo Profil-Match | `docs/demo_push.md`, `docs/demo/push_demo.html` | zwei erfundene Profile; Trichter der Filter; KI-Stufe urteilt „passt/unklar/passt nicht“ nur mit prüfbarem Zitat (7 gespeicherte Urteile); Teams-Karte und E-Mail nur als Vorschau, **nichts gesendet** | KI gegen Regel 13 von 14 (5 trivial, kein Mensch): keine Genauigkeit; Karten nie in echtem Teams gerendert |
| Live-Demo | `docs/demo/live_demo.html` | Beispieldatensatz (621 Bekanntmachungen, Auszug 150) und großer Datensatz (590 Bekanntmachungen, Bayern, 12 Monate bis 06.11.2026); erfundene Firma einstellen, Knopf „Filterung starten“ mit Filterlauf; KI-Urteile nur für P1/P2, sonst Stichwortregel; keine KI-Aufrufe, nichts gesendet | Beispiel: mit Frist-Filter 0, 1 und 2 Treffer für drei erfundene Firmen, keine Marktaussage; Vorgänger-Hinweis abgeschaltet (3 von 3 Auslösungen falsch) |

<div class="bilder">
<figure><img src="lab_log_bilder/webseite_1.png"><figcaption>Webseite: Kopf und Hinweis zur Quelle</figcaption></figure>
<figure><img src="lab_log_bilder/push_demo_1.png"><figcaption>Push-Demo: Kopf, Profil P1 (erfunden)</figcaption></figure>
<figure><img src="lab_log_bilder/live_demo_1.png"><figcaption>Live-Demo: Filterlauf mitten in der Animation</figcaption></figure>
<figure><img src="lab_log_bilder/webseite_2.png"><figcaption>Webseite: Filter und Tabelle</figcaption></figure>
<figure><img src="lab_log_bilder/push_demo_2.png"><figcaption>Push-Demo: Teams-Vorschau und Posteingang</figcaption></figure>
<figure><img src="lab_log_bilder/live_demo_2.png"><figcaption>Live-Demo: Ergebnis für „Beispiel Cham GmbH (erfunden)“</figcaption></figure>
</div>

<div class="video" markdown="1">
<figure><img src="lab_log_bilder/video_standbild.png"><figcaption>Standbild, Szene „Ergebnis“ (Quellzeit 171 s)</figcaption></figure>
<div markdown="1">

**Video „Franz und die Glaskugel“** (`docs/video/franz_und_die_glaskugel_szenen_0-5_v4.mp4`, Szenen 1 bis 5, 170 s (2:50), mit Quizpause im Vortrag etwa 3 Minuten; Quelle der Animation `docs/video/franz_und_die_glaskugel.html`).

- _Zweck:_ Zusammenfassung des Projekts für den Vortrag, mit erfundenen Figuren (Franz, Bit, Prüfi). Veranschaulichung, kein zusätzlicher Beleg.
- _Herkunft:_ Die Animation hat Manuel Strobel KI-gestützt erstellt; Ludwig und Manuel haben sie abwechselnd gemeinsam überarbeitet (Angabe des Nutzers, 2026-11-09). Mit Claude: Zahlen gegen Belege geprüft (keine falschen Zahlen gefunden), zu starke Sätze eingeschränkt, Stimme und Export ergänzt; Liste der Korrekturen in `docs/video/README.md`.
- _Grenzen:_ Stimmen synthetisch (Microsoft-Neuralstimmen über edge-tts, inoffizieller Zugang; Lizenzlage der erzeugten Audiodaten ungeklärt); Figuren erfunden, Gespräche nachgestellt (es gab drei echte); vereinfacht (vier „Runden“ statt zehn Iterationen).
- _Offene Punkte:_ Eine Hörprobe der Fassung v4 ist nicht dokumentiert. Manuel optimiert das Video weiter; eine Fassung nach v4 folgt.

</div>
</div>

## 7. Was wir empfehlen und was nicht

- **Rahmen: Sicht eines Gebäudereinigungsunternehmens.** Entscheidungsfrage des Betriebs: _Selbst bauen, kostenlos nutzen oder abonnieren?_ Antwort nach unserem Stand (Deutung, unter Annahmen): zuerst die kostenlosen Wege nutzen (TED-Suchprofile mit E-Mail-Alarm, Vergabeweiser-Alerts, diese Liste als CSV); abonnieren nur für eine Funktion, die man braucht (im Gespräch genannt: Wettbewerbsdaten; Zahlungsbereitschaft in einem von drei Gesprächen); selbst bauen lohnt im Basismodell gegen kostenlose Dienste nie (Modellkonstruktion, Aufwand und Pflege nicht gemessen). Ergebnis der Business-Case-Prüfung: **kein tragfähiger Business Case** (Abschnitt 1). Nächster billiger Test (vorbereitet, **nicht durchgeführt**): eine Stunde Alarm-Weiterleitung bauen und drei Anrufe mit vorab festgelegter Schwelle.
- **Empfehlung.** Die Vertragsliste „Ende der Laufzeit laut Bekanntmachung“ ist als Ausgangspunkt nutzbar; vor jeder Entscheidung die verlinkte Bekanntmachung lesen. Als eigenes Produkt empfehlen wir sie **nicht**, weil es das Kernprodukt kostenlos (Vergabeweiser) und günstig (AusschreibungsRadar) gibt. Weiterverfolgen ließe sich nur eine Nische (Wettbewerbsdaten, Datenqualität als Zulieferung, Vergabestellen), nach Gesprächen mit mehr Beteiligten.
- **Lohnt eine weitere Prognose-Iteration? (Deutung)** Mit TED-Zuschlägen allein nicht. Gründe: Auch der im Nachhinein beste Vorlauf trifft nur 15 von 52 (28,8 %), selbst ±12 Monate nur 26 von 52 (50 %), und der Vorsprung vor der naiven Referenz ist nicht gesichert (10 zu 4, p ≈ 0,18; Abschnitt 3). Die Gespräche erklären das: Verlängert wird „fast immer“, wenn eine Option besteht, und darüber entscheidet die Verwaltung (Vergabestelle, n = 1). _Ausblick, kein Ergebnis:_ Eine Prognose bräuchte andere Daten, die etwas über die Entscheidung des Auftraggebers sagen: ausgeübte Verlängerungen, Haushalts- oder Beschaffungspläne, Vorinformationen (PIN; laut Iteration 2 etwa 30 pro Jahr in CPV 909, `reports/ergebnis_iteration2.md`). Dazu deutlich mehr Paare als 52 (heutiges Intervall 18,3 bis 42,3 %) und eine Vorwärtsprüfung ab dem Zuschlag statt der Rückwärtssuche.
- **Zulässige Aussagen.** „Bei 94,3 % gleich wie der Vergleichswert zweier KI-Leser; an 15 Losen bestätigt ein Mensch aus dem Team (14/15); Höchstende nur Hinweis.“ Und: „Auf zwei Stichproben (n = 70 und n = 160) weicht Vergabeweisers Datum bei 27 von 230 Losen (11,7 %) ab; bei 23 (10,0 %) liegt die Liste nach neutraler Definition richtig, roh zusammengelegt.“
- **Offene Grenzen der Messungen.** Der Vergleichswert ist teilweise zirkulär: Definition und Liste nehmen standardmäßig dasselbe Feld als Ende der Grundlaufzeit (`reports/evaluation_iteration9.md`). Leser und einziger menschlicher Prüfer der Fassung 9 sind nicht unabhängig (Abschnitt 4). Backtest: Leck und Überlebensverzerrung (Abschnitt 3).
- **Nicht belegt.** Eine Terminprognose; „die Liste ist korrekt“; „Fehlerarten behoben und bestätigt“; „V1 bis V8 erfüllt“; ein Qualitätsvorteil gegenüber Vergabeweiser (und ebenso Gleichheit); Nachfrage, Zahlungsbereitschaft und Marktvorteil (A1, A15); Abdeckung unterhalb der EU-Schwelle (A3); Relevanz der Datenübergabe für Betriebe (D4 offen, H1/H2 ungeprüft); Nutzbarkeit des Exports in Excel oder Branchensoftware.
- **Offene Lücke Systemlandschaft.** In den drei Gesprächen wurde die Systemlandschaft nicht erfragt; der Test ist vorbereitet (Fragen im Wizard-of-Oz-Blatt, `docs/wizard_of_oz_blatt.md`).
- **Offene Grenzen der Liste.** Das Höchstende ist oft zu hoch (laut Evaluator in 7 von 11 Fällen) und nur ein Hinweis; Schuljahres-Verträge sind nicht tagesgenau; `unpublished` wird nicht erkannt; „Dauerfeld enthält die Option“ (12 Lose, 0,13 %) und Textmuster wie M59 werden nicht gefangen. Die Zuordnung zu Vergabeweiser wurde nicht für alle 160 Lose von Hand geprüft; keine Menschenprüfung der 15 diskordanten Lose; keine zweite Modellfamilie. Die Demo Profil-Match belegt keine Nachfrage und keine KI-Genauigkeit (13 von 14, davon 5 trivial, ohne Menschenreferenz); Profile und Stichtag sind erfunden.

## 8. KI-Irrwege und ihre Prüfung

Die KI (Claude Code) hat Hypothesen, Regeln, Stichproben und Auswertungen mitgebaut. Die Fehler wurden vom Nutzer, vom Evaluator (eigener Subagent, nur Lesezugriff) oder von Claude selbst gefunden. Die sechs wichtigsten; die vollständige Tabelle mit allen Einträgen steht im Anhang B.

| Datum | Irrweg | Bemerkt durch | Konsequenz |
|---|---|---|---|
| 2026-10-25 | Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 korrekt | Test auf neuen Daten | Regel verworfen; Testdaten strikt getrennt |
| 2026-11-04 | Iteration 6 und 7: Prüfvorlage zeigte den Listenwert (Verankerung); danach wurden Felder versteckt, und die Nachprüfung übernahm das Feld | Evaluator, Auswertung | Y1 nur als Mischmaß berichtet; Vorlage ohne Listenwerte |
| 2026-11-05 | Wettbewerber nicht gesichtet (G1.1), zwei Suchen fanden keinen Dienst | Recherche-Agent nach Hinweis des Dozenten | A2 widerlegt; Marktgate (Abschnitt 1); Zyklus 4 |
| 2026-11-06 | Demo, Vorgänger-Hinweis (Titelähnlichkeit): nur an einem erfundenen Titel getestet; im großen Datensatz lagen alle 3 Auslösungen falsch | Prüfung am großen Datensatz (Claude) | im großen Datensatz abgeschaltet, als „gebaut, nicht belegt“ gekennzeichnet |
| 2026-11-08 | Video „Franz und die Glaskugel“ (Animation KI-gestützt von Manuel Strobel): erste Fassung stärker als die Belege („Genau das haben uns die Daten gezeigt“, „rund 10 Prozent“ ohne Ursache, „66 von 70“ ohne Einschränkung); Vereinfachungen (9.325 vor der Korrektur, vier Runden statt zehn Iterationen) | Prüfung der Texte gegen die Berichte (Claude, Auftrag des Nutzers) | Texte eingeschränkt, Zahlen unverändert; Vereinfachungen im README genannt |
| 2026-11-05 | Paket B: Null als Ergebnis gelesen (0 von 84 Verfahren „B1 deutlich verfehlt“); tatsächlich Filterartefakt (Landkreis-Code am Lieferort fehlt bei nationalen Verfahren) | Robustheitsprüfung | Erste Auswertung nicht gültig; B1 nicht entscheidbar |

### Was wir heute anders machen würden (Deutung)

_Abgeleitet aus dokumentierten Entscheidungen des Teams, nicht nur aus Fehlern der KI._
- **Früher anrufen.** Am 2026-10-29 entschied der Nutzer gegen Kundenkontakt (`docs/phasen/01_business_understanding.md`). Die drei Gespräche am 2026-11-05 kosteten 105 Minuten und lieferten die wichtigsten Hinweise (Verlängerung ist der Normalfall, Zahlung nur für Wettbewerbsdaten). Vor dem Backtest geführt, hätten sie Ziel und Schwelle der Prognose begründet; so blieb das Fenster ±3 Monate eine Setzung (`docs/business.md` §7.1).
- **Konkurrenz vor der Modellierung sichten.** G1.1 stand früh im Projektplan, erledigt wurde sie erst am 2026-11-05, nach neun Iterationen (Abschnitt 1, Lernpunkt).
- **Entwicklungs- und Testpaare trennen.** Das Prognoseziel wurde auf denselben Paaren mitbestimmt, auf denen später getestet wurde (Abschnitt 3).
- **Erst testen, dann bauen.** Die Demo Profil-Match entstand auf Wunsch des Nutzers nach dem Auswahlbogen (K7 = 0, `docs/demo_push.md`); der billige Test (Wizard-of-Oz-Blatt) ist bis heute nicht durchgeführt.
- **Schwellen auf Erreichbarkeit prüfen.** W8a verlangte 16 Lose bei nur 15 abweichenden (Abschnitt 5).
- **Einen unabhängigen Prüfer einplanen.** Alle menschlichen Prüfungen der Liste kamen aus dem Team (Abschnitt 4).

## 9. Beiträge beider Teammitglieder

_Stand 2026-11-09, Quelle `docs/beitraege.md`. Im Git steht nur ein Autor (alle Commits laufen über das Konto von Ludwig Richthammer, die Arbeit mit Claude Code eingeschlossen). Die Zuordnung stammt deshalb aus den Dokumenten und aus Angaben des Nutzers, nicht aus dem Git. **Manuel Strobel** (Kommilitone, Zweierteam) hat seine Beiträge noch nicht selbst eingetragen; was nicht aus den Dokumenten bekannt ist, steht als **offen: von Manuel nachzutragen**._

| Bereich | Ludwig Richthammer | Claude Code (KI-Assistenz) | Manuel Strobel |
|---|---|---|---|
| Fragestellung, Nische, Kriterien, Entscheidungen | Entscheidungen (Nische, „Idee anpassen“, Prognoseziel Höchstende, Rücksprung zum Business Understanding, Sicht des Betriebs, Wunsch nach Demo und Live-Demo); Freigaben | Vorschläge, Entwürfe der Kriterien (vor den Ergebnissen committet) | offen: von Manuel nachzutragen |
| Daten, Aufbereitung, Auswertungen | Freigaben | Skripte (`src/`), Downloads, Tabellen | offen |
| Urteilsregeln 1.1, Blindprüfungen | geschrieben und kalibriert (2026-10-24); Urteile in Iteration 3 und 4 (W4 13/20; V4 17/20) | Schlüssel, Auswertung; Handsuche durch den Subagenten `rechercheur` | – |
| Zweitprüfung Iteration 5 | P1 bis P13 (P11, P12 nicht beurteilt) | Vorlage, Schlüssel, Auswertung | P14 bis P71 (laut Nutzer, 2026-11-03) |
| Prüfung der Liste, KI-Leser | Prüfung der Stichprobe (Iteration 6) | Leser, Vergleichswert, Auswertung | 15 Lose im TED-Original gelesen (Iteration 9, V6: 14/15) |
| Gespräche mit Betrieben und Vergabestelle | neun Anrufe, drei Stellen erreicht, Notizen ohne Namen (105 Minuten mit Vorbereitung) | – | offen |
| Evaluation | Entscheidungen | Subagent `evaluator` (kritische Prüfung) | offen |
| Business-Case-Auswahl, Demo, Live-Demo | Ideen und Wünsche (Make or Buy, Push-Matching, K-J, Live-Demo), Gegencheck der Angaben | Recherche-Agenten, Bewertung, Code der Demos | offen |
| Video „Franz und die Glaskugel“ | Auftrag zur Prüfung der Texte; Überarbeitung abwechselnd gemeinsam mit Manuel | Prüfung gegen Belege, Korrekturen, Vertonung, Export | Animation KI-gestützt erstellt; Überarbeitung abwechselnd gemeinsam mit Ludwig (laut Nutzer, 2026-11-09); weitere Fassung nach v4 in Arbeit |
| Folien und Vortrag | Durchsicht, Freigaben | Foliengerüst und Umbau (`src/report/vortrag.py`) | Präsentation/Umsetzung (laut Nutzer, 2026-11-03; heutiger Stand: **offen**) |
| Dokumentation, Lab-Log | Durchsicht, Freigaben | Texte in `docs/`, `reports/` | offen |

**Verteilung laut Nutzer (2026-11-09):** ca. 50:50, gemeinsame Telefonate; Details Manuel offen. **Offen bis zur Abgabe:** Manuel trägt seine Beiträge und Stunden selbst ein (`docs/beitraege.md`, Handeinträge im Zeitprotokoll). Bis dahin gelten für ihn nur die oben genannten Angaben; weitere werden nicht angenommen.

## 10. Zeitaufwand

Untergrenze aus der Git-Historie, insgesamt **43,5 Stunden** (Stand 2026-11-09, `src/zeitprotokoll.py`; Sitzung = Commits mit höchstens 90 Minuten Abstand, plus 30 Minuten Vorlauf; Iteration 11 = Nachträge nach dem Tag `iteration-10`: Paket D, Business-Case-Auswahl, Demo, Live-Demo, Video, Folienumbau, Lab-Log). Enthalten ist die Rechenzeit von Claude. Nicht enthalten: Lesen, Handprüfung, Recherche (z. B. K-J, ohne Commit), Vortrag.

<div class="klein2" markdown="1">

{{ZEIT}}

</div>

**Arbeitsschritte mit Zeitaufwand.** Sitzungen anhand der Commit-Nachrichten zugeordnet (Näherung); „Handarbeit“ nach Angaben des Nutzers. Gespräche (105 Minuten) und Manuels Beiträge: siehe Schätzung unten. Git-Spalte rund 36 Stunden (Iteration 1 bis 10) plus 7,4 Stunden Nachträge = 43,5 Stunden (rundungsbedingt).

<div class="klein2" markdown="1">

| Arbeitsschritt | Zugeordnete Git-Sitzungen | Git (Std., ca.) | Handarbeit außerhalb Git |
|---|---|---|---|
| Data Understanding (Abruf, Befüllungsquoten, Ursachen der Lücken) | Iteration 1 und 2, Paket C | 3,6 | nicht erfasst |
| Modellierung und Regeln (Zuordnung, Backtest, Regeln 1b, 6 bis 10) | Iteration 3, 4, 5, 7, 9 (Anteile) | 10,5 | – |
| Handprüfungen (Vorbereiten und Auswerten: Blindprüfungen, Handsuche, Zweitprüfung, Prüfung von 60 und 95 Losen) | Iteration 3 bis 7 (Anteile) | 13,7 | Ausfüllen der Prüfvorlagen durch den Nutzer: **offen** |
| KI-Lesung (Leser, Vergleichswert, Auswertung) | Iteration 8, 9 (Anteil), 10b | 3,5 | Kommilitone: 15 Lose in Iteration 9, Stunden **offen** |
| Business Understanding und Recherche (Wettbewerber, Wettbewerbsbild, Nebentest) | Iteration 4 (Anteil), 10 (Anteil) | 2,1 | – |
| Lab-Log, Folien, Dokumentation | Iteration 4, 5, 10 (Anteile) | 2,8 | Lesen der Berichte, Vortrag: nicht erfasst |
| Make or Buy, Business-Case-Auswahl, Demo, Live-Demo, Video, Folienumbau, Lab-Log-Nachträge | Iteration 11 (Nachträge nach `iteration-10`) | 7,4 | Wünsche, Gegencheck, Hörprobe des Videos: nicht erfasst |

</div>

**Schätzung des Gesamtaufwands (SCHÄTZUNG, nicht gemessen; Herleitung `docs/zeitprotokoll.md`).** Nicht mitgestoppt; die Spannen sind Schätzungen von Claude mit angenommenen Minuten je Prüfeinheit, gemessen ist nur die Git-Zahl.

<div class="klein2" markdown="1">

| Block | Schätzspanne (Std.) | Grundlage |
|---|---|---|
| Git-Sitzungen (Untergrenze 43,5 h; enthält Rechenzeit von Claude) | 30 bis 43,5 | Annahme: 70 bis 100 % davon mit Mensch beteiligt |
| Blindprüfungen Iteration 3 und 4 (40 Paare, Nutzer) | 3 bis 6 | 5 bis 9 Min. je Paar angenommen |
| Zweitprüfung Iteration 5: P1 bis P13 (Nutzer), P14 bis P71 (Manuel, laut Nutzer) | 5 bis 10 | 71 Paare, 4 bis 8 Min. angenommen |
| Prüfung der Stichproben Iteration 6 und 7 (Nutzer, rund 60 Lose) | 2 bis 4 | 2 bis 4 Min. je Los angenommen |
| 15 Lose lesen (Manuel, Iteration 9) | 1 bis 2 | 4 bis 8 Min. je Los angenommen |
| Gespräche W5 (Nutzer) | 1,75 | Angabe des Nutzers: 105 Min., nicht gestoppt |
| Lesen der Berichte und Entscheidungen (beide) | 4 bis 8 | rund 10 Iterationen, 25 bis 50 Min. je Iteration angenommen |
| Telefonate und Abstimmung außerhalb der Git-Sitzungen | 2 bis 5 | laut Nutzer „immer telefoniert“; ohne Doppelzählung angesetzt |
| Video (Abstimmung, Überarbeitung; Animation durch Manuel nicht einzeln geschätzt), Vortrag und Folien (Durchsicht; Umsetzung Manuel laut Nutzer) | 3 bis 8 | Animation laut Nutzer in den rund 30 Stunden je Person enthalten; Probevortrag und Vortrag offen, nicht eingerechnet |
| **Summe** | **rund 52 bis 88** | Summe der Spannen (51,75 bis 88,25) |

</div>

Gesamt rund **52 bis 88 Stunden**; bei ungefähr 50:50 (Nutzer: gemeinsame Telefonate, alles zusammen ausgearbeitet) **rund 26 bis 44 Stunden je Person**; Richtwert des Dozenten ca. 30 Stunden je Person. **Verteilung 50:50 und Gesamtstunden sind Angaben und Schätzungen von Nutzer und Claude, bitte von beiden bestätigen.** Manuels dokumentierte Einzelarbeiten ohne die Video-Animation (nicht geschätzt) ergeben etwa 7 bis 15 Stunden, der Rest läge in der Animation und in gemeinsamen Besprechungen. Nach Angabe von Ludwig (2026-11-09) haben beide jeweils rund 30 Stunden gearbeitet (zusammen rund 60 Stunden, innerhalb der Spanne); Bestätigung durch Manuel und Aufschlüsselung nach Arbeitsschritten offen.


## 11. Reproduzierbarkeit und Quellen

- **Datensatzquelle.** TED (Tenders Electronic Daily, Amt für Veröffentlichungen der EU), Search API v3 (`https://api.ted.europa.eu/v3/notices/search`, anonym), eForms-Bekanntmachungen und ältere Formulare ab Oktober 2016, Deutschland, Haupt-CPV 909; Vergleichsdaten: Vergabeweiser-API (CC BY 4.0), Bekanntmachungsservice (CC0); Telefongespräche ohne Namen. Quellenliste und Lizenzen: `docs/quellen.md`.
- **Code und Daten.** Alle Schritte laufen als Skripte in `src/` (Abhängigkeiten in `requirements.txt`, für Video und Demo-Aufnahme zusätzlich `requirements-video.txt` in eigener Umgebung; Aufrufe in `docs/reproduzierbarkeit.md`); Make-or-Buy und Export: `src/report/make_or_buy.py`, `export_vertragsliste.py`; Sensitivität des Backtests: `src/model/sensitivitaet_backtest.py` (läuft ohne Rohdaten); Demos: `src/demo/` (offline aus Auszügen im Repo); Video: `src/report/video_vertonung.py`, `video_export.py` (`.venv-video`, `docs/video/README.md`); Bilder dieses Logs: `src/report/lab_log_bilder.py`. Rohdaten unverändert in `data/raw` (nicht im Git); Abruf per `src/ted_download.py` (öffentliche Quelle); Repository: https://github.com/ludwigrichthammer9-web/vergabe_radar.
- **Datenumfang und Datenschutz.** Analysetabelle: Vertragsliste mit 9.325 Losen und 16 Merkmalen (`data/processed/vertragsliste_909.csv`), damit im Richtwert des Dozenten (500 bis 50.000 Zeilen); die Rohdaten (rund 630 MB JSON und XML) sind die unveränderte Quelle und werden nur für die Aufbereitung gelesen. Personenbezug: Alle Angaben stammen aus öffentlichen TED-Bekanntmachungen. Bei Einzelunternehmern kann der Firmenname des Auftragnehmers einen Personennamen enthalten (Vertragsliste, Webseite, Wettbewerbsbild; Vorprüfung: 4 von 47 Namen ohne erkennbare Rechtsform, 1 e. K., `docs/export_schema.md` §8). Unverändert übernommene TED-Texte (z. B. `reports/zweitlesung_iteration9/rohtext/`) enthalten die dort veröffentlichten Kontaktdaten der Auftraggeber. Eine Fassung ohne Auftragnehmer liegt unter `docs/prototyp/export/vertragsliste_v1_ohne_auftragnehmer.csv`. Die Telefonnotizen enthalten keine Namen.
- **Vorab festgelegt.** Seeds, Kriterien und Skripte wurden vor dem Ziehen oder Abruf committet; Hashes und Commits im Anhang A. Ausnahmen: Abschnitt 5.
- **Weitere Dokumente.** Entscheidungsvorlage für die Geschäftsführung des fiktiven Betriebs: `docs/entscheidungsvorlage_betrieb.md`; vorbereitete Antworten für die Fragerunde: `docs/fragenrunde.md`; Sensitivität des Backtests: `reports/sensitivitaet_iteration5.md`.
- **Quellen.** `docs/quellen.md` (TED Search API v3, Bekanntmachungen laut TED-Rechtsseite frei wiederverwendbar mit Quellenangabe, Wortlaut am 2026-11-06 gelesen; Vergabeweiser CC BY 4.0 mit Namensnennung; AusschreibungsRadar `robots.txt` beachtet; Bekanntmachungsservice CC0; Preise `docs/business.md` §8; Annahmen `docs/annahmen.md`).
- **Quellen K-J** (Lesedatum 2026-11-06; „laut Seite“ nach der Recherche, nicht erneut abgerufen; Anbieterangaben):
<div class="quellen" markdown="1">

  - Power-Automate-Lizenzen, Seite ms.date 2026-10-17: M365-Lizenzen erlauben Standard-Konnektoren, Premium nicht enthalten. https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/deep-dive-on-specific-license
  - HTTP-Aktion Premium, ms.date 2026-08-14: eine M365-Lizenz („seeded license“) deckt Premium-Funktionen wie HTTP-Aktionen nicht ab (indirekte Aussage, Artikel über Flows mit Dienstprinzipal). https://learn.microsoft.com/en-us/power-automate/assign-user-license-service-principal-flow
  - Besitzer geplanter Flows braucht Premium, Stand 2026-09-22: https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/faqs . Preis Premium 13,00 € je Nutzer und Monat (jährlich, zzgl. MwSt.): https://www.microsoft.com/de-de/power-platform/products/power-automate/pricing
  - Standard-Konnektoren: https://learn.microsoft.com/en-us/connectors/connector-reference/connector-reference-standard-connectors, https://learn.microsoft.com/en-us/connectors/office365/, https://learn.microsoft.com/en-us/connectors/teams/, https://learn.microsoft.com/en-us/connectors/planner/, https://learn.microsoft.com/en-us/connectors/rss/; Planner: https://learn.microsoft.com/en-us/graph/api/planner-post-tasks?view=graph-rest-1.0, https://learn.microsoft.com/en-us/planner/planner-for-admins
  - Teams-Webhooks über Workflows ohne Premium: https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498
  - Abschaltung Office-365-Konnektoren in Teams (18. bis 22.05.2026), Stand 2026-04-14: https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/
  - TED, gespeicherte Suchen und Alarme (bis 25, E-Mail, RSS): https://ted.europa.eu/en/about-ted, https://ted.europa.eu/en/help/my-dashboard, https://ted.europa.eu/en/help/ted-account
  - service.bund.de, Suche mit RSS und Newsletter: https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html . Vergabeweiser, Alerts: https://vergabeweiser.de/ . AusschreibungsRadar, Preise (Watchlist 9 €, Starter 29 €, Business 79 €, Professional 149 €, netto): https://ausschreibungsradar.com/preise/ . subreport, Preise: https://subreport.de/ausschreibungen/produktuebersicht/

</div>

<div style="page-break-before: always"></div>

## Anhang A. Seeds, Hashes und Commits

- **Iteration 6:** `src/prepare/stichprobe_iteration6.py`. **Iteration 7:** Seed 20261106, SHA-256 des Schlüssels `eade66c0…`. **Iteration 8:** Seed 20261108 für die Kontrolle, SHA-256 der Vorlage `5be683ad…`. **Iteration 9:** Seed 20261109, SHA-256 des Schlüssels `9dbf5c1a…`, der neuen Liste `5ec73364…`.
- **Iteration 10:** kein eigener Seed; die 70 Zufallslose der Iteration 9 (Schlüssel `9dbf5c1a…`), Skript `src/prepare/vergleich_iteration10.py`, Kriterien und Skript vor dem Abruf committet (`81a3b90`). Nebentest: Seed 20261111, Ziehung vor dem Nachsehen (`2002ac8`), Auswertung `0eeab99`.
- **Iteration 10b:** Seed 20261112, SHA-256 des Schlüssels `2cd00206…`, `src/prepare/stichprobe_iteration10b.py`; Hypothese, Kriterien und Seed vor dem Ziehen (`4f50436`), Ziehung (`9d63c59`), Abrufskript vor dem Abruf (`49bb198`), Abruf (`64a23e3`), Paket für die Leser vor den Antworten (`6b7e8d8`), Antworten unverändert (`69917ff`), Auswertung und Evaluator (`f6583cc`), Abschluss (`0419609`).
- **Pakete:** Paket A Seeds 20261113 (Handabgleich von 5 Losen) und 20261114 (3 Beispiel-Lose), beide im Skript `src/prepare/wettbewerbsbild_oberpfalz.py` vorab festgelegt (`ea5ebfb`); Paket F `d6e2335`; Paket C `79fd0df`; Paket B Kriterien `0e83dfa`.
- Die Reihenfolge der Commits belegt, dass Regeln und Kriterien vor dem Ziehen feststanden.

## Anhang B. KI-Irrwege, vollständige Tabelle

Nur ergänzt, nie überschrieben (`docs/ki_irrwege.md`). Je Eintrag: Datum, was schieflief, wie es bemerkt wurde, Konsequenz.

<div class="klein" markdown="1">

{{KI_IRRWEGE}}

</div>
