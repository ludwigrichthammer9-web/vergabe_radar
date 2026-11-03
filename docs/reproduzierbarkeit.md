# Reproduzierbarkeit

_Stand 2026-11-03. `data/` liegt nicht im Git (CLAUDE.md-Regel; `data/raw` etwa 630 MB). Alles dort lässt sich aus der TED-Quelle neu laden.
Quellen: `docs/quellen.md`._

## Einrichten
```
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

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

## Was sich nicht neu erzeugen lässt
- **Handsuche (Ground Truth):** Protokolle des Subagenten `rechercheur` liegen als Reports im Git
  (`reports/sichtbarkeit_iteration3_*`, `…iteration4_*`); eine erneute Suche würde wegen des Modells und der wachsenden API-Bestände
  nicht identisch ausfallen. Maßgeblich sind die committeten Reports und die `*_gt.csv`.
- **Urteile von Menschen** (Blindprüfungen) stehen als Dateien in `reports/` (Originale der Nutzerurteile, Iteration 5 siehe
  `reports/gt_pruefung_iteration5*.md`).
- **Lösungsschlüssel** der Blindprüfungen liegen lokal in `data/processed/` und sind nur über ihren SHA-256 in `docs/iterationen.md`
  belegt. Für die Abgabe kann der Schlüssel nach Abschluss der Prüfung als Datei in `reports/` abgelegt werden.
- **Ausgabe der Subagenten** (`data/raw/rechercheur_*`, `blindpruefung_agent_*`): Arbeitsprotokolle, nicht reproduzierbar.

## Datenlink für die Abgabe
Offen: Entweder diese Anleitung als Datenzugang abgeben (Quelle öffentlich) oder einen Ordner mit den verwendeten Läufen
(`data/raw/ted_search/`, ca. 470 MB, ohne Rechercheur-Ordner) bereitstellen. Entscheidung des Nutzers.
