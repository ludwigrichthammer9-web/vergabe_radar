# Beitragsnachweis (Bewertung LN B: Beiträge beider sichtbar)

_Stand 2026-11-09 (zuerst 2026-11-03). Im Git steht nur ein Autor (alle Commits laufen über das Konto von Ludwig Richthammer, die Arbeit mit Claude Code eingeschlossen).
Die Zuordnung unten stammt deshalb aus den Dokumenten (Entscheidungen, Urteile, Dateien) und aus Angaben beider, nicht aus Git.
Kommilitone: **Manuel Strobel**. Wo bei ihm noch „offen“ steht, ist kein Einzelbeitrag dokumentiert; es werden keine Beiträge oder Stunden angenommen._

**Arbeitsweise (Angabe beider, 2026-11-09, nicht aus Git belegbar).** Rund 90 % der Arbeitszeit haben Ludwig Richthammer und Manuel Strobel gemeinsam im Call gearbeitet (gemeinsame Sitzungen mit Bildschirmfreigabe). Claude Code lief dabei über Ludwigs Rechner und Konto; deshalb steht im Git nur Ludwig als Autor. Zeilen, die in diesen Sitzungen entstanden sind, stehen in der Spalte „Gemeinsam (im Call)“ (Zuordnung je Zeile von Ludwig bestätigt, 2026-11-09). Einzeln belegte Beiträge bleiben in den Personenspalten.

| Bereich | Gemeinsam (im Call) | Ludwig Richthammer | Manuel Strobel | Claude Code (KI-Assistenz) |
|---|---|---|---|---|
| Fragestellung, Nische, Kriterien, Entscheidungen | Entscheidungen (Nische, „Idee anpassen“, kein Kundenkontakt vor Iteration 10, Prognoseziel Höchstende, Rücksprung zum Business Understanding, Sicht des Betriebs, Wunsch nach Demo und Live-Demo); Freigaben | – | – | Vorschläge, Entwürfe der Kriterien (vor den Ergebnissen committet) |
| Daten laden und aufbereiten, Auswertungen | Freigabe | – | – | Skripte (`src/`), Downloads, Tabellen, Auswertungen |
| Urteilsregeln Version 1.1 | – | geschrieben und kalibriert (2026-10-24) | – | |
| Handsuche (Ground Truth) | – | | – | Subagent `rechercheur` (Claude) |
| Blindprüfung Iteration 3 und 4 | – | Urteile (W4 13/20; V4 17/20) | – | Schlüssel, Auswertung |
| Zweitprüfung Iteration 5 (X1, X2) | – | P1–P13 (P11, P12 nicht beurteilt) | P14–P71 (Angabe, 2026-11-03) | Vorlage, Schlüssel, Auswertung |
| Prüfung der Liste, KI-Leser (Iteration 6 bis 9) | – | Prüfung der Stichprobe (Iteration 6) | 15 Lose im TED-Original gelesen (Iteration 9, V6: 14/15) | Leser, Vergleichswert, Auswertung |
| Gespräche mit Betrieben und Vergabestelle (W5, Iteration 10) | – | neun Anrufe, drei Stellen erreicht, Notizen ohne Namen (105 Minuten mit Vorbereitung) | offen | – |
| Evaluation | – | Entscheidungen | Kritische Business-Case-Prüfung mit Subagent `evaluator` (Details in der Zeile Business-Case-Auswahl) (Manuel, 2026-11-07, mit Claude Code) | Subagent `evaluator` (kritische Prüfung) |
| Business-Case-Auswahl, Demo, Live-Demo | Ideen und Wünsche (Make or Buy, Push-Matching, K-J, Live-Demo), Gegencheck der Angaben | – | Kritische Prüfung mit Subagent `evaluator`: Kandidaten (K-A bis K-I, Make or Buy, Bid/No-Bid, Vergabestelle) nach LN-B-Kriterium 1 und 6 bewertet; Empfehlung: Kern = Go/No-Go „nicht als Produkt bauen“ als dokumentierter Rücksprung (Strang G am 29.10. zurückgestellt, in Zyklus 4 wieder aufgenommen); Kernbotschaft entschärft; keine Iteration 11; Liste „Das dürfen wir NICHT behaupten“; Hinweise zu Datenschutz (10× „e. K.“ in der Prototyp-Webseite, K.-o.-Risiko) und zum Video (Manuel, 2026-11-07, mit Claude Code) | Recherche-Agenten, Bewertung, Code der Demos |
| Reproduzierbarkeit und Prüfung auf zweitem System | – | – | Repo frisch geklont auf macOS, `.venv` mit Python 3.15 eingerichtet, Berichts-Skripte in einer Kopie neu erzeugt und mit dem Repo verglichen (make_or_buy, lab_log, live_demo gleich; Webseite, Export, Folien nur Datum/Zeilenenden; Folientext 221/221 identisch). Befunde: `zeitprotokoll.py` überschreibt ohne Git das Zeitprotokoll leer; `lab_log_pdf.py` und `live_demo_pruefung.py` finden Browser nur unter Windows-Pfaden; `wizard_of_oz_blatt.py` verliert ohne `data/` still die Lostexte (Manuel, 2026-11-07, mit Claude Code) | – |
| Video „Franz und die Glaskugel“ | – | Auftrag zur Prüfung der Texte; Überarbeitung abwechselnd gemeinsam mit Manuel | Animation KI-gestützt erstellt; Überarbeitung abwechselnd gemeinsam mit Ludwig (Angabe, 2026-11-09); Animation und neue Fassung mit ElevenLabs-Stimmen (`franz_video_ton.mp4`, 2026-11-09) | Prüfung gegen Belege, Korrekturen, Vertonung (v2/v3 Piper, v4 Microsoft-Neuralstimmen über edge-tts; inoffizieller Zugang, Lizenzlage der Audiodaten ungeklärt), Export; Kürzung für den Vortrag (`franz_video_ton_kurz.mp4`, Runde 4 entfernt) |
| Folien und Vortrag | Durchsicht, Freigaben, Präsentation | – | Präsentation/Umsetzung (Angabe, 2026-11-03) | Foliengerüst und Umbau (`src/report/vortrag.py`) |
| Dokumentation, Lab-Log | Durchsicht, Freigaben | – | – | Texte in `docs/`, `reports/` |

**Verteilung: ca. 50:50, rund 90 % gemeinsam im Call; von beiden bestätigt (2026-11-09).** Angabe beider, nicht gemessen.

Stunden (Selbstangabe beider, geschätzt, nicht gemessen; Stand 2026-11-09): Ludwig Richthammer rund 35 Stunden, Manuel Strobel rund 35 Stunden bis zur Abgabe des Lab-Logs am 10.11., davon rund 90 % gemeinsam im Call; zusätzlich je voraussichtlich 2–3 Stunden am 11.11. für die Vortragsvorbereitung (geplant, bei Abgabe noch nicht geleistet). Verteilung damit etwa 50:50. Die Werte liegen im Bereich der Schätzung in docs/zeitprotokoll.md (je Person rund 26 bis 44 Stunden). Die Git-Sitzungen in docs/zeitprotokoll.md zählen die gemeinsame Zeit nur einmal, da nur ein Konto committet.
