# Reproduzierbarkeit

_Stand 2026-11-09 (zuerst 2026-11-03). `data/` liegt nicht im Git (CLAUDE.md-Regel; `data/raw` etwa 630 MB). Alles dort lässt sich aus der TED-Quelle neu laden.
Ausnahme seit 2026-11-09: Analysetabelle, Backtest-Paare und alle Lösungsschlüssel liegen als Kopie in `reports/daten/` (Abschnitt 5).
Quellen: `docs/quellen.md`._

## Einrichten
```
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```
Für Video, Demo-Aufnahme und die Bilder des Lab-Logs gibt es eine zweite Umgebung `.venv-video` mit `requirements-video.txt`
(Playwright, imageio-ffmpeg, Piper, edge-tts; Einrichtung in `docs/video/README.md`, Abschnitt „MP4-Export“).

**HTML-Seiten auf GitHub:** GitHub zeigt `.html`-Dateien (Webseite `docs/prototyp/vertragsliste.html`, Demos in `docs/demo/`, Video
`docs/video/franz_und_die_glaskugel.html`) nur als Quelltext. Zum Ansehen die Datei herunterladen (beim Video mit dem Ordner `audio/`)
und lokal im Browser öffnen.

## 1. Rohdaten laden (TED Search API, öffentlich, kein Schlüssel)
Jeder Lauf speichert die Antworten unverändert in `data/raw/ted_search/<Lauf>/` und schreibt `request_meta.json` (Abfrage, Felder, Zeitpunkt).
Die API-Bestände wachsen laufend; ein neuer Abruf liefert für denselben Zeitraum im Kern dieselben Notices, einzelne Korrekturen
(Änderungsbekanntmachungen) können hinzukommen. Maßgeblich bleibt `request_meta.json` des jeweiligen Laufs.

Für die Pipeline der Iteration 5 (Vertragsliste und Backtest-Paare) werden diese Läufe gebraucht:

| Lauf | Aufruf (jeweils `.venv\Scripts\python src/ted_download.py …`) |
|---|---|
| `DEU_result_cpv909_20231025_20260930_lostext` | `--form-type result --cpv 909 --cpv-field classification-cpv --from 20231025 --to 20260930 --los-texte` |
| `DEU_competition_cpv909_20231025_20260930_lostext` | `--form-type competition --cpv 909 --cpv-field classification-cpv --from 20231025 --to 20260930 --los-texte` |
| `DEU_competition_cpv9091main_20251001_20251231_lostext` | `--form-type competition --cpv 9091 --cpv-field main-classification-proc --from 20251001 --to 20251231 --los-texte` |
| `DEU_competition_cpv9091main_20260101_20260331_lostext` | `… --from 20260101 --to 20260331 --los-texte` (sonst wie oben) |
| `DEU_competition_cpv9091main_20260401_20260630_lostext` | `… --from 20260401 --to 20260630 --los-texte` |
| `DEU_competition_cpv9091main_20260701_20260930_lostext` | `… --from 20260701 --to 20260930 --los-texte` |
| `DEU_result_cpv909_20161001_20260930` (Vorgänger-Pool seit 2016, ohne Lostexte) | `--form-type result --cpv 909 --cpv-field classification-cpv --from 20161001 --to 20260930` |

Die älteren Läufe der Iterationen 1 bis 4 stehen mit ihrer Abfrage in den jeweiligen `request_meta.json` und in `docs/iterationen.md`
(z. B. `DEU_20260722_20261021` für die Datenqualität in Iteration 1: `--from 20260722 --to 20261021`).

## 2. XML einzelner Bekanntmachungen
Die Skripte laden fehlende XML bei Bedarf selbst nach `data/raw/ted_xml/<Ordner>/` (Pause 0,5 s je Abruf, Wiederholungen bei Fehlern):
`objekt/` (Iteration 3/4), `a11_20261023/` (A11-Stichprobe), `backtest_20261030/` (Iteration 5). Kein manueller Schritt nötig.

## 3. Auswertungen und Tabellen (Reihenfolge Iteration 5)
```
.venv\Scripts\python src/verlaengerung_praxis.py          # reports/verlaengerung_praxis_iteration5.md
.venv\Scripts\python src/prepare/vertragsliste.py         # data/processed/vertragsliste_909.csv, reports/vertragsliste_iteration5.md
.venv\Scripts\python src/prepare/pruefung_hoechstende.py entwicklung|test
.venv\Scripts\python src/prepare/backtest_paare.py        # Paare, Vorlage der Zweitprüfung (Seed 20261101)
```
Frühere Iterationen: Skripte `src/*_iteration2…4.py`, jeweils mit Aufruf im Kopf der Datei. Alle Zufallsziehungen haben einen
festen Seed (in `docs/iterationen.md` genannt).

**Spätere Schritte (Iteration 9 bis Abschluss).** Aufrufe wie im Kopf der jeweiligen Skripte; Stichproben- und Leser-Skripte der
Iterationen 6 bis 10b (`src/prepare/*_iteration*.py`) ebenfalls mit Aufruf im Kopf.
```
.venv\Scripts\python src/prepare/vertragsliste.py [Berichtspfad]       # Fassung 9 der Liste (Regeln 1 bis 10): data/processed/vertragsliste_909.csv
.venv\Scripts\python -I src/report/beispiel_liste.py                  # Oberpfalz-Auszug der Liste
.venv\Scripts\python.exe -I src/prepare/wettbewerbsbild_oberpfalz.py  # Paket A (lädt fehlende XML nach; --offline lädt nichts)
.venv\Scripts\python.exe -I src/report/export_vertragsliste.py [--ohne-auftragnehmer]   # docs/prototyp/export/ (Schema 1.1), mit Validierung
.venv\Scripts\python -I src/report/webseite.py                        # docs/prototyp/vertragsliste.html
.venv\Scripts\python.exe -I src\report\make_or_buy.py                 # reports/make_or_buy.md und .csv (nur Standardbibliothek)
python src/model/sensitivitaet_backtest.py [--vorlauf 9 --fenster 2]  # reports/sensitivitaet_iteration5.md; läuft ohne Rohdaten
.venv\Scripts\python.exe -I src/report/vortrag.py [--ohne-anhang]     # docs/vortrag/vortrag_vergabe_radar.pptx
.venv\Scripts\python -I src/report/lab_log.py                         # docs/lab_log.md aus docs/lab_log_vorlage.md
python -I src/report/lab_log_pdf.py                                   # docs/lab_log.pdf (Edge oder Chrome, headless)
.venv-video\Scripts\python.exe -I src\report\lab_log_bilder.py        # Bilder des Lab-Logs (Playwright, Edge)
.venv\Scripts\python.exe -I src/report/diagramme.py                   # Diagramme Abbildung 1 und 2 des Lab-Logs (matplotlib, aus reports/backtest_iteration5.md)
```

## 4. Demo (Profil-Match, Live-Demo für den Vortrag)
Beschreibung, Abfragen und Grenzen: `docs/demo_push.md` (Abschnitte 3, 10, 11). Beide Datensätze der Live-Demo liegen als Auszug im Repo
(`docs/demo/daten/schnappschuss_demo.json`, `docs/demo/daten/datensatz_bayern.json`); die Rohdaten (`data/raw/demo_push_20261106/`,
`data/raw/demo_live_20261106/`) nur lokal. Ein neuer Abruf ergibt nicht dieselben Zahlen (TED-Bestand wächst, Änderungsbekanntmachungen).
```
.venv\Scripts\python.exe -I src\demo\live_daten.py          # Auszug Bayern aus data\raw\demo_live_20261106 (Abruf nur, wenn der Ordner fehlt)
.venv\Scripts\python.exe -I src\demo\live_demo.py           # docs\demo\live_demo.html (offline, beide Datensätze eingebettet)
.venv\Scripts\python.exe -I src\demo\live_demo_pruefung.py  # Selbsttest in Edge headless: P1/P2 = ergebnis_lauf.json, Treffer gegen Rohdaten
```

## 5. Nachrechnen ohne TED-Abruf (Dateien in `reports/daten/`)
Seit 2026-11-09 liegen im Repo byte-gleiche Kopien von `vertragsliste_909.csv` (Analysetabelle, 9.325 Lose, ohne Auftragnehmer),
`backtest_paare_iteration5.csv`, `x1_paare_iteration5.txt` und allen Lösungsschlüsseln der abgeschlossenen Blindprüfungen und Stichproben
(Iteration 3, 4, 5, 6, 7, 9, 10b); zusammen rund 1,8 MB. Tabelle mit Inhalt, Zeilen, SHA-256 und Hash-Prüfung: `reports/daten/README.md`
(alle 9 dokumentierten Hashes stimmen). Die Skripte lesen aus `data/processed/`; zum Nachrechnen die Dateien dorthin kopieren
(Git Bash; vorhandene Dateien mit gleichem Namen werden überschrieben, `-n` verhindert das):
```
mkdir -p data/processed && cp -n reports/daten/*.csv reports/daten/*.txt data/processed/
```
Danach laufen ohne Rohdaten und ohne TED-Abruf (am 2026-11-09 in einer Kopie des Repos geprüft, Ergebnisse in `reports/daten/README.md`):
```
.venv\Scripts\python -I src/model/baseline.py                  # Backtest Iteration 5: reports/backtest_iteration5.md (byte-gleich)
.venv\Scripts\python -I src/report/optionsanalyse.py           # Paket F: reports/optionsanalyse.md (byte-gleich)
.venv\Scripts\python -I src/model/sensitivitaet_backtest.py    # reports/sensitivitaet_iteration5.md (byte-gleich)
.venv\Scripts\python -I src/prepare/auswertung_iteration6.py   # Y1 54/60
.venv\Scripts\python -I src/prepare/auswertung_iteration7.py   # Y1 36/47 (eine beschreibende, gewichtete Zeile weicht ab)
.venv\Scripts\python -I src/prepare/auswertung_iteration8.py   # Z0 bis Z4 (eine beschreibende, gewichtete Zeile weicht ab)
.venv\Scripts\python -I src/prepare/auswertung_iteration9.py   # V1 66/70, V2 28/30, V5 110/110
.venv\Scripts\python -I src/prepare/stichprobe_iteration10b.py # Ziehung mit Seed 20261112, Schlüssel-Hash identisch
```
Die Auswertungsskripte prüfen den SHA-256 des Schlüssels vor dem Öffnen und lesen die Urteile aus `reports/`. Nicht ohne Weiteres:
`src/prepare/stichprobe_iteration9.py` braucht zusätzlich die alte Fassung `vertragsliste_909_iteration8.csv` (nicht veröffentlicht);
`vergleich_iteration10*.py` und `blindpruefung_iteration3.py` brauchen Rohdaten aus `data/raw`.

## Was sich nicht neu erzeugen lässt
- **Handsuche (Ground Truth):** Protokolle des Subagenten `rechercheur` liegen als Reports im Git
  (`reports/sichtbarkeit_iteration3_*`, `…iteration4_*`); eine erneute Suche würde wegen des Modells und der wachsenden API-Bestände
  nicht identisch ausfallen. Maßgeblich sind die committeten Reports und die `*_gt.csv`.
- **Urteile von Menschen** (Blindprüfungen) stehen als Dateien in `reports/` (Originale der Nutzerurteile, Iteration 5 siehe
  `reports/gt_pruefung_iteration5*.md`).
- **Lösungsschlüssel** der Blindprüfungen und Stichproben (`data/processed/*schluessel*.csv`) sind über ihren SHA-256 in
  `docs/iterationen.md` und den Commits belegt. _Korrektur 2026-11-09:_ Sie liegen jetzt als byte-gleiche Kopie in `reports/daten/`
  (alle Prüfungen abgeschlossen; Hashes geprüft, `reports/daten/README.md`); die Auswertungen lassen sich damit neu rechnen (Abschnitt 5).
  Der frühere Satz „keiner im Git … ohne die Schlüssel nicht neu rechnen“ gilt nicht mehr.
- **Ausgabe der Subagenten** (`data/raw/rechercheur_*`, `blindpruefung_agent_*`): Arbeitsprotokolle, nicht reproduzierbar.

## Datenlink für die Abgabe
Gewählt (2026-11-06, Nutzer): Diese Anleitung samt Repository https://github.com/ludwigrichthammer9-web/vergabe_radar ist der Datenzugang (Quelle öffentlich, Abruf per `src/ted_download.py`). Voraussetzung: Das Repository ist gepusht und für den Dozenten lesbar (Stand 2026-11-06: nicht erreichbar, nicht gepusht). _Nachtrag 2026-11-09:_ Das Repository ist öffentlich (Seite am 2026-11-09 abrufbar, HTTP 200); lokale Commits müssen vor der Abgabe noch gepusht werden. Ein Ordner mit den Läufen (`data/raw/ted_search/`, ca. 470 MB) wurde nicht bereitgestellt.
