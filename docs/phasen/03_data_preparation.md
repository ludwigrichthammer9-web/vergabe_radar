# Phase 3: Data Preparation

> **Ziel:** Aus Rohdaten einen sauberen, analysierbaren Datensatz bauen.
> **Weiter, wenn:** Der Datensatz reproduzierbar per Skript aus den Rohdaten entsteht.
> **Zurück zu Phase 2, wenn:** Neue Datenprobleme auftauchen, die erst verstanden werden müssen.
> Details: [CRISP-DM.md](../CRISP-DM.md#3-data-preparation)
>
> **Artefakte laut CRISP-DM.md:**
> - `data/processed/`: vorhanden (`notices_DEU_20260722_20261021.csv`, Nebenprodukt der Analyse)
> - Skripte in `src/prepare/`: fehlen; die Tabelle entsteht derzeit in `src/analyze_completeness.py`
> - dokumentierte Bereinigungsregeln: fehlen

---

## Aktueller Stand

_Stand: Iteration 1, 2026-10-22. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

### Fakten (aus den Daten)

- `data/processed/notices_DEU_20260722_20261021.csv` hat 15.706 Zeilen, eine pro Notice. Erzeugt von
  `build_table()` in [src/analyze_completeness.py](../../src/analyze_completeness.py).
- Start- und Enddatum sowie Dauer stammen nur aus dem **ersten Los**. 15,3 % der Notices haben mehrere Lose. [Report §1]
- Die Laufzeit liegt in drei Formen vor: Dauer mit Einheit DAY/WEEK/MONTH/YEAR (BT-36), Start- und Enddatum (BT-536/537)
  und „sonstige“ wie UNLIMITED (BT-538). (Rohdaten, Stichprobe)
- `buyer-name` ist ein mehrsprachiges Feld (`{"deu": [...]}`). Normalisiert wurde nichts. (Rohdaten)

### Interpretation

- Die CSV ist ein Analyse-Nebenprodukt, noch kein Vertragsdatensatz für den Backtest.
- Für den Backtest braucht es eine Tabelle pro Los mit vereinheitlichtem Laufzeitende.

## Offene Fragen

- [ ] Tabelle pro Vertrag oder pro Los?
- [ ] Wie wird das Laufzeitende vereinheitlicht (Ende direkt oder Start + Dauer, ersatzweise Veröffentlichungsdatum + Dauer)?
- [ ] Wie werden Verlängerungen aus dem Freitext (BT-54, BT-57) strukturiert erfasst?
- [ ] Wie werden Auftraggeber normalisiert (gleiche Behörde, unterschiedliche Schreibweisen; ggf. über Kennungen)?
- [ ] Wie ordnen wir Neuausschreibungen den ursprünglichen Verträgen zu (Annahme A9)?
- [ ] Sollen die Skripte in die Ordnerstruktur aus CRISP-DM.md wandern (`src/ingest/`, `src/prepare/`)?
- [ ] _(aus Iteration 1)_ Laufzeit aus Beginn/Ende (BT-536/BT-537) als Hauptquelle nutzen, BT-36 nur ergänzend. Bei Dauer ohne
  Beginn eventuell den Vertragsabschluss als Näherung nehmen (Platzhalter wie `AwardDate 2000-01-01` beachten).
- [ ] _(aus Iteration 1)_ Verlängerungen aus dem Freitext BT-54/BT-57 strukturiert extrahieren (Anzahl, Dauer, Höchstlaufzeit).
- [ ] _(aus Iteration 1)_ Enddaten auf Plausibilität prüfen (z. B. Enddatum ≥ 2050).

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| – | – | Noch keine Entscheidungen | – |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

### Iteration 1 – 2026-10-22

- **Was gemacht:** Keine eigene Arbeit in dieser Phase. Als Nebenprodukt der Vollständigkeitsanalyse entstand eine
  Tabelle mit einer Zeile pro Notice in `data/processed/`.
- **Erkenntnisse – Fakten:** Die Tabelle nutzt bei Datumsfeldern nur das erste Los. Auftraggebernamen sind nicht normalisiert.
- **Erkenntnisse – Interpretation:** Für den Backtest reicht die Tabelle so nicht aus.
- **Übergabe an die nächste Phase:** Keine. Phase 3 beginnt richtig in Iteration 2.
