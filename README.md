# Vergabe-Radar

**Frage:** Lässt sich aus den Zuschlagsbekanntmachungen der EU-Plattform TED vorhersagen, wann ein öffentlicher Reinigungsvertrag in Deutschland neu ausgeschrieben wird?

**Ergebnis in vier Sätzen**
- Den Termin der Neuausschreibung kann man so nicht vorhersagen: Die beste einfache Regel trifft in 28,8 % der 52 geprüften Fälle, vorab gefordert waren 60 %.
- Das Vertragsende lässt sich aus der Bekanntmachung lesen: Bei 66 von 70 Stichproben stimmt unsere Liste mit dem Wert zweier KI-Leser überein (die Leser sind nicht unabhängig, ein Teammitglied prüfte 15 Fälle, 14 stimmen).
- Eine solche Liste gibt es schon kostenlos (Vergabeweiser).
- Unsere Prüfung mit vorab festgelegten Kriterien ergab keinen tragfähigen Business Case.

**Empfehlung für einen Reinigungsbetrieb:** Kostenlosen Alarm nutzen · Abo nur, wenn eine Funktion fehlt – vorher testen · nicht selbst bauen, solange niemand Treffer von Hand ins eigene System überträgt.

Quellen der Zahlen: [Lab-Log](docs/lab_log.md), Abschnitte 0, 3, 4 und 7.

**Team:** Manuel Strobel, Ludwig Richthammer. OTH Amberg-Weiden, Master Digital Business, Kurs Big Data Analytics, Leistungsnachweis B (Zweierteam).

## Wegweiser

| Was | Datei | Hinweis |
|---|---|---|
| Lab-Log | [docs/lab_log.pdf](docs/lab_log.pdf), [docs/lab_log.md](docs/lab_log.md) | Hauptdokument: Verlauf, Entscheidungen, KI-Irrwege |
| Folien | [docs/vortrag/vortrag_vergabe_radar.pdf](docs/vortrag/vortrag_vergabe_radar.pdf), [.pptx](docs/vortrag/vortrag_vergabe_radar.pptx) | 12 sichtbare Folien, Anhang für die Fragerunde ausgeblendet; Sprechernotizen in der PPTX |
| Video „Franz und die Glaskugel“ | [docs/video/franz_und_die_glaskugel_szenen_0-5_v4.mp4](docs/video/franz_und_die_glaskugel_szenen_0-5_v4.mp4) | Download, rund 2:50 Minuten. Animation: Manuel Strobel, KI-gestützt; gemeinsam überarbeitet; Stimmen synthetisch; Fassung wird noch aktualisiert. Details: [docs/video/README.md](docs/video/README.md) |
| Webseiten-Prototyp | [docs/prototyp/vertragsliste.html](docs/prototyp/vertragsliste.html) | Vertragsliste Oberpfalz, 130 Lose, mit Filtern |
| Live-Demo | [docs/demo/live_demo.html](docs/demo/live_demo.html) | erfundene Firma, nichts wird gesendet; kein Business Case |
| Entscheidungsvorlage | [docs/entscheidungsvorlage_betrieb.md](docs/entscheidungsvorlage_betrieb.md) | eine Seite aus Sicht eines (fiktiven) Reinigungsbetriebs |
| Fragenrunde | [docs/fragenrunde.md](docs/fragenrunde.md) | wahrscheinliche Fragen, Antworten, Live-Nachweise |

**HTML-Dateien:** GitHub zeigt sie nur als Quelltext. Wer die HTML-Seiten im Browser sehen will: herunterladen und lokal öffnen. Beide Seiten laufen offline.

## Ordnerstruktur

```
src/        Python-Skripte: Abruf (ted_download.py), Aufbereitung (prepare/), Modell (model/), Berichte und Folien (report/), Demo (demo/)
reports/    Auswertungen je Iteration, Stichproben, Evaluator-Berichte
docs/       Lab-Log, Folien, Video, Prototyp, Demo, Business-Dokumente, Quellen, Reproduzierbarkeit
.claude/    Arbeitsanweisungen an die KI (Subagenten evaluator und rechercheur, Abläufe für Iterationen)
data/       nicht im Repo (Rohdaten und Zwischentabellen, siehe unten)
```

## Reproduzieren

Unter Windows (PowerShell), im Wurzelordner des Repos:

```
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python src/model/sensitivitaet_backtest.py --vorlauf 9 --fenster 2
```

Der dritte Befehl braucht keine Rohdaten. Er rechnet den Backtest der Terminprognose (52 Paare aus `reports/backtest_iteration5.md`) mit anderen Parametern nach. Ohne Argumente erzeugt er `reports/sensitivitaet_iteration5.md` neu. Alle übrigen Schritte mit Aufrufen: [docs/reproduzierbarkeit.md](docs/reproduzierbarkeit.md).

## Code: die Kernpipeline

In Ausführungsreihenfolge. Zweck aus dem Kopf (Docstring) des Skripts. „Ohne Rohdaten“ heißt: läuft ohne `data/raw/` (den TED-Abruf). Die Spalte haben wir am 2026-11-09 geprüft; „geprüft“ heißt, der Lauf erzeugte dieselbe Datei wie im Repo.

| # | Skript | Zweck | Eingabe | Ausgabe | Ohne Rohdaten? |
|---|---|---|---|---|---|
| 1 | [src/ted_download.py](src/ted_download.py) | Lädt Bekanntmachungen aus der TED Search API v3 und speichert jede Antwort unverändert | TED-API (Internet, kein Schlüssel) | `data/raw/ted_search/<lauf>/` | nein, erzeugt die Rohdaten |
| 2 | [src/prepare/vertragsliste.py](src/prepare/vertragsliste.py) | Zuschlagstabelle je Los mit Ende der Grundlaufzeit, Höchstende und Herkunft (Leseregeln 1 bis 10) | `data/raw/ted_search/DEU_result_cpv909_…` | `data/processed/vertragsliste_909.csv`, Bericht (Standard `reports/vertragsliste_iteration5.md`, Pfad als Argument) | nein |
| 2a | [src/report/beispiel_liste.py](src/report/beispiel_liste.py) | Oberpfalz-Auszug der Liste mit Stufe A bis F und Status | `vertragsliste_909.csv`, Oberpfalz-Abruf in `data/raw/`, eForms-XML | `reports/beispiel_liste_oberpfalz.csv`, `reports/beispiel_liste.md` | nein |
| 3 | [src/prepare/backtest_paare.py](src/prepare/backtest_paare.py) | Backtest-Paare aus der Handsuche (Iteration 3 und 4) mit dem Ende des Vorgängers; Vorlage der Zweitprüfung (Seed 20261101) | `reports/sichtbarkeit_iteration3_gt.csv`, `…iteration4_gt.csv`, Rohdaten und Original-XML von TED | `data/processed/backtest_paare_iteration5.csv`, Schlüssel der Zweitprüfung, `reports/gt_pruefung_iteration5.md` | nein |
| 4 | [src/model/baseline.py](src/model/baseline.py) | Regeln R0 und R1 und Backtest | `data/processed/backtest_paare_iteration5.csv`, `data/processed/x1_paare_iteration5.txt` | `reports/backtest_iteration5.md` | ja, mit den Kopien aus `reports/daten/` (geprüft) |
| 5 | [src/model/sensitivitaet_backtest.py](src/model/sensitivitaet_backtest.py) | Nachträgliche Sensitivität (Vorlauf, Fenster), kein neuer Test | `reports/backtest_iteration5.md` | `reports/sensitivitaet_iteration5.md`; mit `--vorlauf`/`--fenster` nur Bildschirm | ja (geprüft) |
| 6 | [src/prepare/stichprobe_iteration9.py](src/prepare/stichprobe_iteration9.py) | Stichprobe der Iteration 9 (110 Lose, Seed 20261109); `--trockenlauf` zieht mit anderem Seed und schreibt nichts | `vertragsliste_909.csv`, `vertragsliste_909_iteration8.csv`, Schlüssel der Iteration 7, Listen der Entwicklungsfälle | `reports/stichprobe_iteration9_lose.csv`, `data/processed/stichprobe_iteration9_schluessel.csv` | nur mit Zwischentabellen; die alte Fassung `vertragsliste_909_iteration8.csv` fehlt in `reports/daten/` (Stand 2026-11-09) |
| 7 | [src/prepare/stichprobe_iteration10b.py](src/prepare/stichprobe_iteration10b.py) | Stichprobe für den Vergleich mit Vergabeweiser (160 Lose, Seed 20261112) | `vertragsliste_909.csv`, Schlüssel der Iterationen 6, 7 und 9, Listen der Entwicklungsfälle | `data/processed/stichprobe_iteration10b_schluessel.csv`, `reports/stichprobe_iteration10b_lose.csv` | ja, mit den Kopien aus `reports/daten/` (geprüft) |
| 8 | [src/report/diagramme.py](src/report/diagramme.py) | Zwei Diagramme zur Terminprognose (Abweichung, Trefferquote je Vorlauf) | `reports/backtest_iteration5.md` | `docs/lab_log_bilder/diagramm_abweichung.png`, `diagramm_vorlauf.png` | ja (geprüft) |
| 9 | [src/report/webseite.py](src/report/webseite.py) | Prototyp-Webseite der Vertragsliste mit Filtern | `reports/beispiel_liste_oberpfalz.csv`, `reports/wettbewerbsbild_oberpfalz.csv` | `docs/prototyp/vertragsliste.html` | ja (läuft; nur das Datum „Seite erzeugt am“ ändert sich) |
| 10 | [src/report/export_vertragsliste.py](src/report/export_vertragsliste.py) | Export der Liste nach festem Schema 1.1, mit Validierung | wie 9, dazu `reports/beispiel_liste.md`, `reports/wettbewerbsbild_oberpfalz.md` | `docs/prototyp/export/vertragsliste_v1*.csv/.json` | ja (geprüft für die CSV) |
| 11 | [src/report/lab_log.py](src/report/lab_log.py), [lab_log_pdf.py](src/report/lab_log_pdf.py) | Lab-Log aus Vorlage, Zeitprotokoll und KI-Irrwegen; dann PDF über Edge oder Chrome | `docs/lab_log_vorlage.md`, `docs/zeitprotokoll.md`, `docs/ki_irrwege.md` | `docs/lab_log.md`, `docs/lab_log.pdf` | ja (nicht erneut ausgeführt) |
| 12 | [src/report/vortrag.py](src/report/vortrag.py) | Foliengerüst mit Sprechernotizen | Code, Video und Bilder in `docs/` | `docs/vortrag/vortrag_vergabe_radar.pptx` | ja (nicht erneut ausgeführt) |

**Daten zum Nachrechnen ohne TED-Abruf:** [reports/daten/](reports/daten/) (Analysetabelle und Lösungsschlüssel). Die Skripte lesen fest aus `data/processed/`; die Dateien also dorthin kopieren (Befehl und geprüfte Läufe: [docs/reproduzierbarkeit.md](docs/reproduzierbarkeit.md), Abschnitt 5).

### Wo steckt was

| Was | Stelle |
|---|---|
| Seed der Stichprobe (Iteration 9) | [stichprobe_iteration9.py#L33](src/prepare/stichprobe_iteration9.py#L33) (`SEED = 20261109`); verwendet in [#L67-L68](src/prepare/stichprobe_iteration9.py#L67-L68) (Trockenlauf: Seed 1), [#L79](src/prepare/stichprobe_iteration9.py#L79), [#L91](src/prepare/stichprobe_iteration9.py#L91) und [#L93](src/prepare/stichprobe_iteration9.py#L93) (Mischen, Auswahl der 15 Lose für die Menschenprüfung) |
| Ausschluss der Entwicklungsfälle | [stichprobe_iteration9.py#L69-L73](src/prepare/stichprobe_iteration9.py#L69-L73) (Handsuche, Iteration 7, Entwicklungslisten); angewendet in [#L78](src/prepare/stichprobe_iteration9.py#L78) |
| Prognoseregel R0/R1 | [baseline.py#L30-L31](src/model/baseline.py#L30-L31) (`VORLAUF_MONATE = 6`, `FENSTER_MONATE = 3`), Funktionen `r0`/`r1` [#L46-L51](src/model/baseline.py#L46-L51), `treffer` [#L54-L55](src/model/baseline.py#L54-L55) |
| Fehlwerte: kein Ende, unplausible Laufzeit | [vertragsliste.py#L164-L173](src/prepare/vertragsliste.py#L164-L173) (`grundlaufzeit`: „unbekannt“, „unplausibel“ bei Laufzeit ≤ 0 oder > 240 Monate, [#L78](src/prepare/vertragsliste.py#L78)) |
| Geschätztes Ende (Stufe E) | [vertragsliste.py#L397-L400](src/prepare/vertragsliste.py#L397-L400) (Veröffentlichung + Dauer, eigene Spalte `gl_geschaetzt`) |
| Einteilung Stufe E/F | [beispiel_liste.py#L74-L78](src/report/beispiel_liste.py#L74-L78) (`stufe`: ohne Ende → E, wenn geschätzt, sonst F) |

## Daten

- `data/` liegt nicht im Repo (rund 630 MB Rohdaten). Alles lässt sich aus der öffentlichen TED-API neu laden, ohne Schlüssel: `src/ted_download.py`, Parameter je Lauf in [docs/reproduzierbarkeit.md](docs/reproduzierbarkeit.md).
- Ein neuer Abruf liefert nicht in jedem Detail dieselben Zahlen, weil der TED-Bestand wächst.
- Die Demos laufen aus Auszügen, die im Repo liegen (`docs/demo/daten/`).
- Analysetabelle (`vertragsliste_909.csv`), Backtest-Paare und Lösungsschlüssel der Stichproben liegen als Kopie in `reports/daten/` (Analysetabelle und Lösungsschlüssel), damit man ohne TED-Abruf nachrechnen kann.

## Lizenzen und Quellen

**Eigene Inhalte dieses Repos** (© 2026 Manuel Strobel, Ludwig Richthammer):

| Teil | Lizenz |
|---|---|
| Code (`src/`, `.claude/`) | MIT, siehe [LICENSE](LICENSE) |
| Texte, Lab-Log, Folien, Berichte (`docs/`, `reports/`, außer Video) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de): Weiterverwendung erlaubt, mit Nennung der Urheber und Hinweis auf Änderungen |
| Video und Audio (`docs/video/`: MP4, WAV, Animation) | keine Freigabe, alle Rechte vorbehalten (synthetische Stimmen mit ungeklärter Lizenzlage; Fassung wird noch überarbeitet) |

Die Lizenzen gelten nur für eigene Inhalte. Übernommene Daten und Texte Dritter behalten ihre eigenen Bedingungen:

Vollständige Liste: [docs/quellen.md](docs/quellen.md).
- **TED** (Amt für Veröffentlichungen der EU): Bekanntmachungen laut TED-Rechtsseite frei wiederverwendbar, auch kommerziell. Quellenangabe: „TED, Publications Office of the European Union“; alle Tabellen sind eigene Auswertungen.
- **Vergabeweiser** (Vergleichsdaten über die API): CC BY 4.0.
- **Bekanntmachungsservice** oeffentlichevergabe.de (OCDS-Jahresdateien): CC0.

## Datenschutz

- Wir nutzen nur öffentliche TED-Angaben. Auftraggeber und Auftragnehmer sind meist Behörden und Firmen.
- Alle Angaben zu Aufträgen stammen aus öffentlichen TED-Bekanntmachungen. Bei Einzelunternehmern kann der Firmenname des Auftragnehmers einen Personennamen enthalten (Vertragsliste, Webseite, `reports/wettbewerbsbild_oberpfalz.*`); unverändert übernommene TED-Texte (z. B. `reports/zweitlesung_iteration9/`) enthalten die dort veröffentlichten Kontaktdaten der Auftraggeber. Eine Fassung der Liste ohne Auftragnehmer liegt unter `docs/prototyp/export/vertragsliste_v1_ohne_auftragnehmer.csv`.
- Die Notizen der drei Telefongespräche enthalten keine Namen von Personen oder Firmen.

## KI-Nutzung

- Wir haben mit Claude Code (Anthropic) als Assistenz gearbeitet: Skripte, Auswertungen, Entwürfe der Texte.
- Fehler der KI und wie sie gefunden wurden: [Lab-Log §8](docs/lab_log.md) und die vollständige Liste in [docs/ki_irrwege.md](docs/ki_irrwege.md).
- `CLAUDE.md` und `.claude/` sind Arbeitsanweisungen an die KI, keine Projektergebnisse.
- Alle Commits laufen über ein Konto. Wer was beigetragen hat, steht in [docs/beitraege.md](docs/beitraege.md).
