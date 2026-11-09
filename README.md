# Vergabe-Radar

**Frage:** Lässt sich aus den Zuschlagsbekanntmachungen der EU-Plattform TED vorhersagen, wann ein öffentlicher Reinigungsvertrag in Deutschland neu ausgeschrieben wird?

**Ergebnis in vier Sätzen**
- Den Termin der Neuausschreibung kann man so nicht vorhersagen: Die beste einfache Regel trifft in 28,8 % der 52 geprüften Fälle, vorab gefordert waren 60 %.
- Das Vertragsende lässt sich aus der Bekanntmachung lesen: Bei 66 von 70 Stichproben stimmt unsere Liste mit dem Wert zweier KI-Leser überein (die Leser sind nicht unabhängig, ein Mensch prüfte 15 Fälle, 14 stimmen).
- Eine solche Liste gibt es schon kostenlos (Vergabeweiser).
- Unsere Prüfung mit vorab festgelegten Kriterien ergab keinen tragfähigen Business Case.

Quellen der Zahlen: [Lab-Log](docs/lab_log.md), Abschnitte 0, 3, 4 und 7.

**Team:** Manuel Strobel, Ludwig Richthammer. OTH Amberg-Weiden, Master Digital Business, Kurs Big Data Analytics, Leistungsnachweis B (Zweierteam).

## Wegweiser

| Was | Datei | Hinweis |
|---|---|---|
| Lab-Log | [docs/lab_log.pdf](docs/lab_log.pdf), [docs/lab_log.md](docs/lab_log.md) | Hauptdokument: Verlauf, Entscheidungen, KI-Irrwege |
| Folien | [docs/vortrag/vortrag_vergabe_radar.pdf](docs/vortrag/vortrag_vergabe_radar.pdf), [.pptx](docs/vortrag/vortrag_vergabe_radar.pptx) | Sprechernotizen in der PPTX |
| Video „Franz und die Glaskugel“ | [docs/video/franz_und_die_glaskugel_szenen_0-5_v4.mp4](docs/video/franz_und_die_glaskugel_szenen_0-5_v4.mp4) | Download, rund 2:50 Minuten. Animation: Manuel Strobel, KI-gestützt; gemeinsam überarbeitet; Stimmen synthetisch; Fassung wird noch aktualisiert. Details: [docs/video/README.md](docs/video/README.md) |
| Webseiten-Prototyp | [docs/prototyp/vertragsliste.html](docs/prototyp/vertragsliste.html) | Vertragsliste Oberpfalz, 130 Lose, mit Filtern |
| Live-Demo | [docs/demo/live_demo.html](docs/demo/live_demo.html) | erfundene Firma, nichts wird gesendet; kein Business Case |
| Entscheidungsvorlage | [docs/entscheidungsvorlage_betrieb.md](docs/entscheidungsvorlage_betrieb.md) | eine Seite aus Sicht eines (fiktiven) Reinigungsbetriebs |
| Fragenrunde | [docs/fragenrunde.md](docs/fragenrunde.md) | wahrscheinliche Fragen, Antworten, Live-Nachweise |

**HTML-Dateien:** GitHub zeigt sie nur als Quelltext. Bitte herunterladen und lokal im Browser öffnen. Beide Seiten laufen offline.

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

## Daten

- `data/` liegt nicht im Repo (rund 630 MB Rohdaten). Alles lässt sich aus der öffentlichen TED-API neu laden, ohne Schlüssel: `src/ted_download.py`, Parameter je Lauf in [docs/reproduzierbarkeit.md](docs/reproduzierbarkeit.md).
- Ein neuer Abruf liefert nicht in jedem Detail dieselben Zahlen, weil der TED-Bestand wächst.
- Die Demos laufen aus Auszügen, die im Repo liegen (`docs/demo/daten/`).

## Lizenzen und Quellen

Vollständige Liste: [docs/quellen.md](docs/quellen.md).
- **TED** (Amt für Veröffentlichungen der EU): Bekanntmachungen laut TED-Rechtsseite frei wiederverwendbar, auch kommerziell. Quellenangabe: „TED, Publications Office of the European Union“; alle Tabellen sind eigene Auswertungen.
- **Vergabeweiser** (Vergleichsdaten über die API): CC BY 4.0.
- **Bekanntmachungsservice** oeffentlichevergabe.de (OCDS-Jahresdateien): CC0.
- Lizenz für den Code dieses Repos: noch offen.

## Datenschutz

- Wir nutzen nur öffentliche TED-Angaben. Auftraggeber und Auftragnehmer sind meist Behörden und Firmen.
- Alle Angaben zu Aufträgen stammen aus öffentlichen TED-Bekanntmachungen. Bei Einzelunternehmern kann der Firmenname des Auftragnehmers einen Personennamen enthalten (Vertragsliste, Webseite, `reports/wettbewerbsbild_oberpfalz.*`); unverändert übernommene TED-Texte (z. B. `reports/zweitlesung_iteration9/`) enthalten die dort veröffentlichten Kontaktdaten der Auftraggeber. Eine Fassung der Liste ohne Auftragnehmer liegt unter `docs/prototyp/export/vertragsliste_v1_ohne_auftragnehmer.csv`.
- Die Notizen der drei Telefongespräche enthalten keine Namen von Personen oder Firmen.

## KI-Nutzung

- Wir haben mit Claude Code (Anthropic) als Assistenz gearbeitet: Skripte, Auswertungen, Entwürfe der Texte.
- Fehler der KI und wie sie gefunden wurden: [Lab-Log §8](docs/lab_log.md) und die vollständige Liste in [docs/ki_irrwege.md](docs/ki_irrwege.md).
- `CLAUDE.md` und `.claude/` sind Arbeitsanweisungen an die KI, keine Projektergebnisse.
- Alle Commits laufen über ein Konto. Wer was beigetragen hat, steht in [docs/beitraege.md](docs/beitraege.md).
