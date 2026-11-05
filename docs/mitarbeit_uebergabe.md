# Mitarbeit am Vergabe-Radar: Einstieg und Übergabe

_Für Teammitglieder, die neu einsteigen (und für deren Claude Code). Stand 2026-11-06: Iteration 10 und 10b abgeschlossen, Paket A, B, C, F und Wizard-of-Oz-Blatt vorbereitet (nicht durchgeführt). Wenn du Claude Code benutzt: Lass es zuerst `CLAUDE.md`, diese Datei, `docs/iterationen.md` (Übersicht und Iteration 10) und `docs/business.md` §8 lesen._

## 1. Worum es geht (in fünf Sätzen)

- **Idee:** Aus Zuschlagsbekanntmachungen auf TED (EU-Amtsblatt) eine Liste öffentlicher Gebäudereinigungsverträge in Deutschland mit Vertragsende erzeugen; Zielgruppe Reinigungsbetriebe, die sich früh auf Neuausschreibungen vorbereiten wollen.
- **Ergebnisse:** Eine Terminprognose der Neuausschreibung trägt nicht (28,8 % Treffer im Fenster ±3 Monate, Schwelle 60 %). Das Ende der Grundlaufzeit der Liste stimmt zu 94,3 % mit zwei KI-Lesern überein (Mensch 14/15); das Höchstende ist nur ein Hinweis.
- **Neu (Business Understanding):** Es gibt die Liste kostenlos bei Vergabeweiser und günstig bei AusschreibungsRadar (`docs/business.md` §8). Die Gespräche (3) zeigen Zahlungsbereitschaft in einem von drei Gesprächen (ein größerer Betrieb), gespalten, und nur für Wettbewerbsdaten (Auftragnehmer, alte Preise). Gesamturteil: Produkt als eigenes Angebot nicht belegt.
- **Aktuell:** Iteration 10 und 10b (Vergleich mit Vergabeweiser, W1 bis W9) sind abgeschlossen, ebenso die Pakete A, B, C, F. Das Wizard-of-Oz-Blatt (`docs/wizard_of_oz_blatt.md`, erzeugt mit `src/report/wizard_of_oz_blatt.py`) ist vorbereitet, aber nicht durchgeführt. Offen bis zur Abgabe: Namen auf Folie 1 eintragen, TED-Rechtsseite selbst bestätigen, Datenlink, Probevortrag.
- **Bewertung:** Leistungsnachweis B (Zweierteam, Big Data Analytics, OTH Amberg-Weiden): 15 Minuten Vortrag, höchstens 12 Folien, Lab-Log. Kriterien in `docs/bewertung_LN.md`.

## 2. Einrichten (Windows, Python 3.12)

```
git clone https://github.com/ludwigrichthammer9-web/vergabe_radar.git
cd vergabe_radar
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

- Skripte immer so starten: `.venv\Scripts\python -I src/...` (`-I` = isolierter Modus).
- **Claude Code** im Projektordner starten (VS Code-Erweiterung oder `claude`). Es liest `CLAUDE.md` und die Dateien in `.claude/` (Subagenten `evaluator`, `rechercheur`, Skills `iteration-start`, `iteration-ende`).
- Für das PDF des Lab-Logs braucht ihr Microsoft Edge oder Chrome (`src/report/lab_log_pdf.py`).
- Git zeigt Warnungen „LF will be replaced by CRLF“. Die sind harmlos.

## 3. Wo liegt was

| Ort | Inhalt |
|---|---|
| `CLAUDE.md` | Projektstand und Arbeitsregeln (lesen!) |
| `docs/iterationen.md` | **Zentrales Logbuch**: je Iteration Hypothese, Kriterien (vorab), Ergebnis, Entscheidung. Nur ergänzen, nie überschreiben |
| `docs/business.md` | Business Understanding; §6 früher Stand, **§8 Markt, Wettbewerb, Gespräche (neu)** |
| `docs/annahmen.md` | Annahmen A1 bis A20 mit Status und Nachweis |
| `docs/projektplan.md`, `docs/CRISP-DM.md`, `docs/phasen/` | Planung und Stand je Phase |
| `docs/lab_log.md` und `docs/lab_log.pdf` | Lab-Log (**erzeugt**, nicht von Hand ändern, siehe unten) |
| `docs/lab_log_vorlage.md` | Quelle des Lab-Logs (hier wird geschrieben) |
| `docs/ki_irrwege.md`, `docs/zeitprotokoll.md` | Tabellen, die ins Lab-Log einfließen |
| `docs/vortrag/…pptx` | Folien (**erzeugt** mit `src/report/vortrag.py`) |
| `docs/prototyp/vertragsliste.html` | Prototyp-Webseite (**erzeugt** mit `src/report/webseite.py`) |
| `docs/telefonnotizen_iteration10.md` | Leeres Notizblatt für weitere Gespräche |
| `reports/` | Berichte und Auswertungen je Iteration, auch `evaluation_iterationN.md` des Evaluators |
| `src/` | Code: `ted_download.py`, `prepare/` (Regeln, Stichproben, Auswertungen), `report/` (Lab-Log, Folien, Webseite) |
| `docs/reproduzierbarkeit.md`, `docs/quellen.md` | Wie man alles neu erzeugt; Quellenliste |

## 4. Daten: nicht im Git

`data/` steht in `.gitignore` (etwa 680 MB). Du brauchst sie nur, wenn du Auswertungen nachrechnen oder Skripte der Iterationen 9 und 10 laufen lassen willst. Zwei Wege:

1. **Von Ludwig bekommen** (empfohlen, ein ZIP über Laufwerk oder USB). Es enthält `data/processed/` (13 MB, u. a. `vertragsliste_909.csv` und die Schlüssel der Stichproben) und die benötigten Teile von `data/raw/` (TED-XML, Abfragen, Vergabeweiser, AusschreibungsRadar).
2. **Neu laden:** `src/ted_download.py` (TED Search API v3, öffentlich, kein Schlüssel); Aufrufe in `docs/reproduzierbarkeit.md`. Das dauert und liefert nicht die Schlüssel der Stichproben (die sind in `data/processed/` und gehören zu den Hashes in den Commits).

**Wichtig:** Die Schlüsseldateien der Stichproben (`data/processed/*schluessel*.csv`) dürfen nicht ins Git (sie sind das Prüfgeheimnis der blinden Messungen; nur ihr SHA-256 steht in den Commits).

## 5. Regeln der Zusammenarbeit (aus `CLAUDE.md`, ergänzt)

- Vor dem Coden die aktuelle TED-API-Dokumentation prüfen, nicht aus dem Gedächtnis arbeiten.
- **Rohdaten nie verändern** (`data/raw`), Auswertungen getrennt.
- **Kriterien vor dem Ergebnis festlegen und committen** (Schwellen, Seeds, Skripte), dann erst abrufen oder ziehen. Nachträgliche Änderungen offen als Nachtrag kennzeichnen.
- **Fakten (mit Quelle) und Interpretation trennen**. Logs nur ergänzen.
- Eigenen Fehlern offen nachgehen: Sie kommen mit Bemerkt-durch und Folge in `docs/ki_irrwege.md` (das Lab-Log braucht diese Tabelle für die Bewertung).
- Iterationen mit `/iteration-start` anlegen und mit `/iteration-ende` abschließen; Ergebnisse vom Subagenten `evaluator` kritisch prüfen lassen.
- Kurz erklären, was getan wird (die Projektregel: der Student soll dabei lernen).

## 6. Zusammenarbeit mit Git (ohne Streit)

- **Vor jeder Arbeit** `git pull`, **danach** `git add` (einzelne Dateien), `git commit`, `git push`. Nie blind `git add .` (in `data/` liegt zwar nichts im Git, aber Temporäres kann stören).
- **Gemeinsam beschriebene Dateien** (`docs/iterationen.md`, `docs/ki_irrwege.md`, `docs/business.md`): kleine Commits, oft pullen; am besten schreibt je Abschnitt nur eine Person.
- **Erzeugte Dateien nicht von Hand ändern:** `docs/lab_log.md` (aus `lab_log_vorlage.md`, `zeitprotokoll.md`, `ki_irrwege.md` mit `src/report/lab_log.py`), `docs/lab_log.pdf` (`src/report/lab_log_pdf.py`), `docs/zeitprotokoll.md` (`src/zeitprotokoll.py`), Folien (`src/report/vortrag.py`), Webseite (`src/report/webseite.py`). Wer ändern will, ändert die Quelle und erzeugt neu. Bei Merge-Konflikten in erzeugten Dateien: Quelle abgleichen und neu erzeugen, nicht von Hand mergen.
- **Zeitprotokoll:** Die Handeinträge unten in `docs/zeitprotokoll.md` werden beim Neuerzeugen überschrieben. Eigene Stunden (Lesen, Prüfen, Gespräche) deshalb zusätzlich in `docs/beitraege.md` festhalten.
- **Commit-Nachrichten** deutsch, kurz, mit Iteration und Schritt (Beispiele in `git log --oneline`).

## 7. Wo gerade Hilfe gebraucht wird (Vorschlag zur Aufteilung)

Stand 2026-11-06. Iteration 10 und 10b sind ausgewertet (`docs/iterationen.md`), Lab-Log, Folien und Webseite sind erzeugt. Offen sind die Punkte unten.

| Aufgabe | Aufwand | Dateien | Hinweis |
|---|---|---|---|
| Prototyp-Webseite prüfen und verbessern (Filter, Standardsortierung nach laufenden Verträgen, Texte, Handy-Ansicht) | 1–2 Std. | `src/report/webseite.py` | Regionennamen der NUTS-Codes sind aus dem Gedächtnis eingetragen und müssen gegen Eurostat geprüft werden |
| Lizenz der TED-Daten: Wortlaut der Rechtsseite (ted.europa.eu/en/legal-notice) selbst bestätigen (Eintrag steht in `docs/quellen.md`: laut Rechtsseite frei wiederverwendbar, vor Abgabe zu bestätigen); Datenlink für die Abgabe festlegen | 0,5 Std. | `docs/quellen.md`, `docs/lab_log_vorlage.md` | K.-o.-Kriterium: Datensatz ohne Quellenangabe |
| Wizard-of-Oz-Gespräche (3 bis 5 Betriebe, auch ein Betrieb ohne öffentliche Aufträge; Einwilligung vorher klären; Ergebnis nur Hinweis) | je 15 Min. | Blatt `docs/wizard_of_oz_blatt.md`, Notizblatt `docs/telefonnotizen_iteration10.md`, dann `docs/business.md` §8.9 | Notizen ohne Namen von Personen; ohne Antworten bleibt es „vorbereitet, nicht durchgeführt“ |
| Folien durchgehen: Verständlichkeit, Dramaturgie, Zeit (15 Minuten, 12 Folien); Namen auf Folie 1 eintragen | 1 Std. | `src/report/vortrag.py` (Folien sind Code) | Mit Ludwig abstimmen |
| Probevortrag und Fragerunde üben (Methodenfrage, Live-Nachweis im Werkzeug, Transferfrage) | 1 Std. | `docs/bewertung_LN.md` | Live-Nachweis: `git log`, Skripte öffnen, Regel zeigen |
| Dashboard zum Projektverlauf (nur, wenn der Dozent es verlangt; **erst fragen**) | offen | `src/dashboard_daten.py` | Ersetzt das Lab-Log nicht (Bogen sagt „PDF/Web-App“) |

## 8. Dinge, die man leicht falsch macht

- **Kriterien nachträglich ändern.** Ergebnisse dürfen die Schwellen nicht verschieben. Abweichungen kommen als Nachtrag mit Begründung.
- **Aussagen größer machen als die Belege.** Zulässig ist: „Zu 94,3 % identisch mit dem Vergleichswert zweier KI-Leser; an 15 Losen bestätigt ein Mensch (14/15); Höchstende nur Hinweis.“ Nicht zulässig: „die Liste ist korrekt“, „V1 bis V8 erfüllt“.
- **KI-Leser nicht als unabhängig darstellen** (gleiche Modellfamilie wie die Regeln).
- **Gespräche (n = 3) nicht als Stichprobe verkaufen.** Es sind Hinweise.
- **Konkurrenzdaten:** Vergabeweiser-Daten stehen unter CC BY 4.0 (Quelle „Vergabeweiser“ nennen), Rohdaten des Bekanntmachungsservice unter CC0. AusschreibungsRadar nur einzelne Seiten abrufen (robots.txt beachten), keine Massenabrufe.
- **Namen von Personen** gehören nicht in Dokumente.

## 9. Was dein Claude Code nicht weiß (Übergabe)

Die „Erinnerungen“ von Claude (Dateien unter `~/.claude/projects/…`) liegen nur bei Ludwig. Dein Claude kennt nur, was im Repo steht. Kurzfassung zum Eintippen am Anfang:

> „Lies CLAUDE.md, docs/mitarbeit_uebergabe.md, docs/iterationen.md (Übersicht und Iteration 10) und docs/business.md §8. Ich arbeite im Zweierteam mit Ludwig am Vergabe-Radar (Leistungsnachweis B). Halte dich an die Regeln dort (Kriterien vor dem Ergebnis, Rohdaten unverändert, Fakten und Deutung trennen). Frage nach, bevor du etwas committest oder pushst.“

Offene Entscheidungen, die bei Ludwig liegen: ob ein Dashboard gebaut wird (Rückfrage beim Dozenten), Abgabeformat (PDF/Web-App).
