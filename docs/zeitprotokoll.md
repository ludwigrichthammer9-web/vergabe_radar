# Zeitprotokoll (aus der Git-Historie)

_Erzeugt mit `src/zeitprotokoll.py` am 2026-11-09. Methode: Commits mit höchstens 90 min Abstand = eine Sitzung; Dauer = erster bis letzter Commit + 30 min Vorlauf. **Untergrenze:** Arbeit ohne Commit (Lesen, Handprüfung, Recherche, Gespräche) fehlt; die Rechenzeit von Claude ist enthalten. Beiträge anderer Personen (Kommilitone) stehen nicht im Git und werden unten von Hand ergänzt._

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
| 11 | 5 | 32 | 7.4 |
| **Summe** | 34 | 150 | **43.5** |

## Iteration 1

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-10-22 | 12:22–13:01 | 2 | 1.2 | Initial commit / Projektstruktur: gitignore und CLAUDE.md |
| 2026-10-22 | 16:51–16:51 | 1 | 0.5 | Iteration 1: Machbarkeit der TED-Daten abgeschlossen |

## Iteration 2

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-10-23 | 09:26–09:26 | 1 | 0.5 | Iteration 2 gestartet: API-Prüfung, Rückreichweite, Projektplan |
| 2026-10-23 | 11:01–11:25 | 3 | 0.9 | Iteration 2: Download, K4/K5, Zuordnungs-Prototyp und K2-Prüfung / Iteration 2 abgeschlossen: Idee anpassen |

## Iteration 3

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-10-23 | 11:30–14:13 | 14 | 3.2 | Iteration 3 angelegt: Sichtbarkeit und Zuordnung über das Objekt / Iteration 3: Blindprüfung (V4) vorbereitet, Zählweise und Schlüssel-Ha |
| 2026-10-24 | 09:43–09:46 | 2 | 0.5 | Iteration 3: Urteilsregeln für die Blindprüfung (Version 1) des Nutzer / Blindprüfung: Auswertung nach Urteilsregeln (Sicherheit, streng/breit) |
| 2026-10-24 | 11:35–11:54 | 3 | 0.8 | Urteilsregeln Version 2 (zwei Klarstellungen), Agent-Prüfung nach Vers / Blindprüfung: 8 Ersatzpaare P21–P28, Auswertung ohne Kalibrierungspaar |
| 2026-10-25 | 13:40–14:52 | 3 | 1.7 | Blindprüfung: Agentenprüfung P9–P28 nach Urteilsregeln Version 1.1 / Iteration 3 abgeschlossen: in Phase 2/3 bleiben |

## Iteration 4

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-10-25 | 15:01–16:34 | 6 | 2.0 | Iteration 4 angelegt: letzter Verbesserungsversuch der Zuordnung / Iteration 4: Testprobe gezogen (70 Fälle aus Q1 2026) |
| 2026-10-25 | 18:46–19:27 | 2 | 1.2 | Iteration 4: Handsuche Teil 1 (U1–U14) abgeschlossen / Iteration 4: Handsuche Teil 2 (U15–U28) abgeschlossen |
| 2026-10-26 | 07:27–08:32 | 4 | 1.6 | Iteration 4: Handsuche Teil 3 (U29–U42) abgeschlossen / Iteration 4: Handsuche abgeschlossen, Ground Truth (W1 30/70) |
| 2026-10-26 | 13:43–13:43 | 1 | 0.5 | Iteration 4: Regel auf Testdaten – W2 17/19, W3 56,7 %, W6 73,3 % |
| 2026-10-28 | 10:39–11:14 | 3 | 1.1 | Dashboard-Daten aus den Projektdokumenten; T2c.5 und T2c.7 abgehakt / Iteration 4: Blindprüfung (W4) vorbereitet, Schlüssel-Hash festgelegt |
| 2026-10-29 | 13:04–13:04 | 1 | 0.5 | Kein Kundenkontakt: Iteration 7 als Prototyp, Strang G als Recherche |
| 2026-10-30 | 13:39–14:00 | 2 | 0.8 | Blindprüfung Iteration 4: Urteile des Nutzers, W4 = 13/20 (65 %) / Iteration 4 abgeschlossen: Idee anpassen |

## Iteration 5

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-10-30 | 14:08–15:24 | 7 | 1.8 | Iteration 5 angelegt: Prognoseziel Höchstende, Kriterien X1-X4 vorab / Iteration 5, Schritt 4: 68 Backtest-Paare, Vorlage zur Zweitprüfung (7 |
| 2026-11-03 | 23:19–23:31 | 2 | 0.7 | Quellenliste, Reproduzierbarkeitsanleitung, KI-Irrwege und Bewertungsk / Zeitprotokoll aus Git-Historie und Beitragsnachweis |
| 2026-11-04 | 12:32–13:07 | 9 | 1.1 | Iteration 5, Schritt 5: Zweitprüfung ausgewertet, X2 = 91,0 %, X1 = 52 / Iteration 6 angelegt, Regeln Abdeckung festgelegt (vor Stichprobe) |

## Iteration 6

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-11-04 | 13:07–16:16 | 4 | 3.6 | Iteration 6, Schritt 2: Stichprobe gezogen, Prüfvorlage, Schlüssel-Has / Iteration 6 abgeschlossen: zurück zu Phase 3 |

## Iteration 7

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-11-04 | 16:40–18:09 | 4 | 2.0 | Iteration 7 angelegt, Hypothese und Kriterien festgelegt (vor Regeländ / Iteration 7, Schritt 2: Stichprobe gezogen, Vorlage ohne Listenwerte,  |
| 2026-11-04 | 20:06–21:31 | 7 | 1.9 | Iteration 7, Schritt 4: Prüfung ausgewertet, Rohwerte Y1 25 %, Gültigk / ki_irrwege: Einträge zu Iteration 6 und 7 |
| 2026-11-04 | 23:36–23:36 | 1 | 0.5 | Iteration 7 abgeschlossen: Abschluss mit diesem Stand |

## Iteration 8

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-11-04 | 23:39–23:54 | 4 | 0.8 | Iteration 8 angelegt: KI-Zweitlesung, Kriterien und Vorlage (vor dem L / Iteration 8: Evaluator-Entscheide, Z4 und Auswertung |
| 2026-11-05 | 09:02–09:02 | 1 | 0.5 | Iteration 8 abgeschlossen: weiter, Projektabschluss |

## Iteration 9

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-11-05 | 09:02–09:33 | 6 | 1.0 | Lab-Log und Foliengerüst für den Vortrag / Iteration 9: Nachtrag zum Pfad des Schlüssels |
| 2026-11-05 | 14:08–14:31 | 4 | 0.9 | Iteration 9, Schritt 4: Antworten der Leser und des Kommilitonen (unve / Iteration 9 abgeschlossen: weiter, Projektabschluss |

## Iteration 10

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-11-05 | 15:55–18:00 | 15 | 2.6 | Lab-Log und Folien auf Iteration 9, Lab-Log als PDF, Prototyp-Webseite / Paket A: Wettbewerbsbild der 130 Oberpfalz-Lose aus TED (Auftragnehmer |
| 2026-11-05 | 20:22–20:22 | 1 | 0.5 | Paket C: Ursachen der 33 Lose ohne Ende, Fehlertyp Dauerfeld = Gesamtd |
| 2026-11-05 | 22:01–22:48 | 5 | 1.3 | Iteration 10b: Abruf abgeschlossen (160 Lose, Vergabeweiser hat 160, d / Iteration 10 und 10b abgeschlossen: weiter, Projektabschluss, eingesch |

## Iteration 11

| Tag | Zeit | Commits | Std. | Erster / letzter Commit |
|---|---|---|---|---|
| 2026-11-05 | 22:58–00:16 | 12 | 1.8 | Lab-Log auf Iteration 10 und 10b: Zyklus 4 (Business Understanding und / Letzte Korrekturen nach Gesamtprüfung: Abdeckung mit Zeitraum, Vergabe |
| 2026-11-06 | 08:32–10:41 | 15 | 2.7 | Paket D (Teil 1): Make-or-Buy-Modell, business.md §9 Perspektive des B / Vortrag: Demo-Folie, Folien 9/10 zusammengelegt (12 Folien), Namen; Ap |
| 2026-11-06 | 13:13–13:51 | 2 | 1.1 | Live-Demo (docs/demo/live_demo.html), Dark-Mode-Reparatur mit Umschalt / Live-Demo: grosser Datensatz (Bayern, 590 Ausschreibungen), Filterlauf |
| 2026-11-08 | 19:51–20:38 | 2 | 1.3 | Video 'Franz und die Glaskugel' (korrigiert, vertont, MP4), Vortrag mi / Video v2: Piper-Stimme (Thorsten), eigener Sprechertext, ElevenLabs-Zw |
| 2026-11-09 | 14:05–14:05 | 1 | 0.5 | Video v3: Bildereignisse zum Wort verschoben, einordnender Schlusssatz |

## Ergänzungen von Hand (nicht im Git)

| Datum | Person | Tätigkeit | Std. |
|---|---|---|---|
| 2026-11-05 | Nutzer | Gespräche Iteration 10 (W5): Vorbereitung, 9 Anrufe, Abtippen (business.md §8.9) | 1.75 |
| 2026-11-05 | Kommilitone (Manuel Strobel) | Lesen von 15 Losen im TED-Original (Iteration 9, V6) | offen |
| 2026-11-03 | Kommilitone (Manuel Strobel) | Zweitprüfung P14–P71 (Iteration 5; Angabe des Nutzers) | offen |
| | Kommilitone (Manuel Strobel) | Präsentation/Umsetzung der Folien (Angabe des Nutzers, 2026-11-03) | offen |
| 2026-11-08 | Kommilitone (Manuel Strobel) | Erstellung der Video-Animation „Franz und die Glaskugel“ (KI-gestützt), danach Überarbeitung abwechselnd mit dem Nutzer (Angabe des Nutzers, 2026-11-09) | offen (in den rund 35 Stunden je Person enthalten, Selbstangabe beider, 2026-11-09) |
| | | weitere Handarbeit (Zweitprüfungen, Handprüfungen der Iterationen 5 bis 7) | offen |

## Schätzung des Gesamtaufwands (2026-11-09; **SCHÄTZUNG, nicht gemessen**)

_Anlass: Frage des Nutzers, wie lange das Team gearbeitet hat. Es wurde nicht mitgestoppt. Die Zahlen unten sind Schätzungen von Claude auf Grundlage der dokumentierten Handarbeiten, mit angenommenen Minuten je Prüfeinheit (Annahmen, keine Messung). Gemessen ist nur die Git-Untergrenze von 43,5 Stunden._

| Block | Schätzspanne (Std.) | Grundlage |
|---|---|---|
| Git-Sitzungen (Untergrenze 43,5 h, enthält Rechenzeit von Claude) | 30 bis 43,5 | Annahme: 70 bis 100 % dieser Zeit war mindestens eine Person aktiv beteiligt (Telefonate, Durchsicht); der Rest ist Rechenzeit ohne Mensch. Gemessen ist nur die Git-Zahl. |
| Blindprüfungen Iteration 3 und 4 (je 20 Paare, Urteile des Nutzers) | 3 bis 6 | 40 Paare, angenommen 5 bis 9 Minuten je Paar (zwei Bekanntmachungen lesen und beurteilen). |
| Zweitprüfung Iteration 5, P1 bis P13 (Nutzer) | 1 bis 2 | 13 Paare (2 nicht beurteilt), angenommen 5 bis 9 Minuten je Paar. |
| Zweitprüfung Iteration 5, P14 bis P71 (Manuel; laut Nutzer) | 4 bis 8 | 58 Paare, angenommen 4 bis 8 Minuten je Paar. Manuels eigene Angabe fehlt. |
| Prüfung der Stichproben Iteration 6 und 7 (Nutzer, rund 60 Lose) | 2 bis 4 | Nur als „Prüfung der Stichprobe“ dokumentiert; Umfang und Zeit je Los nicht erfasst, angenommen 2 bis 4 Minuten je Los bei rund 60 Losen. |
| 15 Lose im TED-Original lesen (Manuel, Iteration 9) | 1 bis 2 | 15 Lose, angenommen 4 bis 8 Minuten je Los. |
| Gespräche mit Betrieben und Vergabestelle (W5, Nutzer) | 1,75 | Angabe des Nutzers: 105 Minuten (Vorbereitung, neun Anrufe, Abtippen). Einzige Handzahl mit Angabe, aber ebenfalls nicht gestoppt. |
| Lesen der Berichte und Entscheidungen (beide) | 4 bis 8 | Rund 10 Iterationsberichte, Evaluator-Prüfungen, Business-Case-Auswahl; angenommen 25 bis 50 Minuten je Iteration. |
| Telefonate und Abstimmung außerhalb der Git-Sitzungen (beide) | 2 bis 5 | Laut Nutzer „immer telefoniert und alles zusammen ausgearbeitet“; nur der Teil ohne Commit-Zeitraum ist hier angesetzt, um Doppelzählung zu vermeiden. |
| Video: Abstimmung, Überarbeitung, Durchsicht (Animation durch Manuel nicht einzeln geschätzt) | 1 bis 3 | Die Animation hat Manuel erstellt; ihre Stunden sind in den rund 35 Stunden je Person enthalten (Selbstangabe beider), hier nicht gesondert eingerechnet. Eine Hörprobe ist nicht dokumentiert. |
| Vortrag und Folien: Durchsicht, Umsetzung (Manuel laut Nutzer) | 2 bis 5 | Probevortrag und der Vortrag selbst sind noch offen und nicht eingerechnet. |
| **Summe** | **51,75 bis 88,25** | Rundung: **rund 52 bis 88 Stunden** gemeinsam |

**Gesamtspanne:** rund **52 bis 88 Stunden** für das Team (Schätzung). **Je Person** bei ungefähr 50:50 (Angabe des Nutzers: „wir haben knapp 50:50 gemacht, auch wenn ich viel in Claude gemacht habe, haben wir immer telefoniert und alles zusammen ausgearbeitet“): **rund 26 bis 44 Stunden je Person**. Richtwert des Dozenten: ca. 30 Stunden je Person, liegt in der Spanne. **Selbstangabe beider (2026-11-09, nicht gemessen): Ludwig Richthammer und Manuel Strobel je rund 35 Stunden bis zur Abgabe des Lab-Logs am 10.11. (zusammen rund 70 Stunden, innerhalb der Schätzung), davon rund 90 % gemeinsam im Call; zusätzlich je voraussichtlich 2–3 Stunden am 11.11. für die Vortragsvorbereitung (geplant). Frühere Angabe (rund 30 Stunden je Person) damit ersetzt, da am 9. und 10.11. weitergearbeitet wurde; siehe docs/beitraege.md.**

**Was diese Schätzung nicht ist.** Die Verteilung 50:50 und die Gesamtstunden sind Angaben und Schätzungen von Nutzer und Claude; **bitte von beiden (Ludwig und Manuel) bestätigen oder korrigieren.** Manuels dokumentierte Einzelarbeiten (Zweitprüfung P14 bis P71, 15 Lose, Folien) ergeben für sich nur etwa 7 bis 15 Stunden; der Rest seines Anteils läge in den gemeinsamen Telefonaten und Besprechungen, die nicht einzeln dokumentiert sind. Manuels Gesamtzeit: rund 35 Stunden (Selbstangabe, 2026-11-09); Aufschlüsselung nach Arbeitsschritten: offen. Nicht eingerechnet: Animation des Kollegen, Probevortrag, Vortrag. Die Spanne ist breit, weil die Annahmen (Minuten je Paar oder Los, Anteil der Git-Zeit mit Mensch) sich um den Faktor zwei ändern lassen.
