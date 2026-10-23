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

_Stand: Iteration 2 (Abschluss), 2026-10-23. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Phase 3 ist noch nicht richtig begonnen. In Iteration 2 sind aber Bausteine für die Aufbereitung entstanden.

### Fakten (aus den Daten)

- `build_table()` in [src/analyze_completeness.py](../../src/analyze_completeness.py) erzeugt eine Tabelle pro Notice. Datumsfelder
  stammen aus dem ersten Los; 15,3 % der Notices haben mehrere Lose. [R §1]
- `end_date()` in [src/kennzahlen_iteration2.py](../../src/kennzahlen_iteration2.py) vereinheitlicht das Laufzeitende: Enddatum,
  sonst Beginn + Dauer; Laufzeiten ≤ 0 oder > 240 Monate werden verworfen.
  [reports/kennzahlen_iteration2.md](../../reports/kennzahlen_iteration2.md)
- [src/zuordnung_prototyp.py](../../src/zuordnung_prototyp.py) normalisiert Auftraggebernamen (Kleinschreibung, Umlaute,
  Satzzeichen) und Kennungen. Exakte Gleichheit verpasst Schreibvarianten (z. B. „Hansestadt Demmin“ vs. „Hansestadt Demmin –
  Der Bürgermeister“) und trennt nicht zwischen Objekten desselben Auftraggebers.
  [reports/k2_pruefliste.md](../../reports/k2_pruefliste.md)
- [src/k2_xml_auszug.py](../../src/k2_xml_auszug.py) liest Titel, Lose, Ort und Laufzeit aus eForms- und alter TED-XML und folgt
  bei alten Zuschlägen `REF_NOTICE` zur alten Ausschreibung.
- `buyer-identifier` ist uneinheitlich (Leitweg-ID, USt-ID, UUID, teils Telefonnummer) und teils für mehrere Niederlassungen gleich
  (Autobahn GmbH). [reports/evaluation_iteration2.md](../../reports/evaluation_iteration2.md)

### Interpretation

- Für die Zuordnung über das Objekt braucht es Merkmale auf Los-Ebene (Adresse, Liegenschaftsname, Titel). Bei Notices vor eForms
  stehen sie nur in der XML.
- Eine Tabelle pro Los mit vereinheitlichtem Laufzeitende bleibt das Ziel für den Backtest, sobald Phase 2 die Zuordnung klärt.

## Offene Fragen

- [ ] Tabelle pro Vertrag oder pro Los?
- [ ] Wie wird das Laufzeitende vereinheitlicht (Ende direkt oder Start + Dauer, ersatzweise Veröffentlichungsdatum + Dauer)?
- [ ] Wie werden Verlängerungen aus dem Freitext (BT-54, BT-57) strukturiert erfasst?
- [ ] Wie werden Auftraggeber normalisiert (gleiche Behörde, unterschiedliche Schreibweisen; ggf. über Kennungen)?
- [ ] Wie ordnen wir Neuausschreibungen den ursprünglichen Verträgen zu (Annahme A9)?
  _Stand Iteration 2:_ Über Auftraggeber + CPV nicht (K2 = 16,7 %). Nächster Versuch über das Objekt (A9b), zunächst in Phase 2.
- [ ] _(neu, Iteration 2)_ Wie werden Adresse, Liegenschaftsname und Titel je Los extrahiert und normalisiert, auch aus alter TED-XML?
- [ ] _(neu, Iteration 2)_ Wie werden Auftraggeber-Schreibvarianten zusammengeführt (unscharfer Vergleich, ohne Objekte verschiedener
  Niederlassungen zu vermischen)?
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
| 2026-10-23 | 2 | Zuordnung über Auftraggeber + CPV wird nicht in eine Aufbereitung übernommen; Phase 3 wartet auf die Zuordnung über das Objekt (Iteration 3, Phase 2) | K2 = 16,7 % (reports/ergebnis_iteration2.md) |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

### Iteration 1 – 2026-10-22

- **Was gemacht:** Keine eigene Arbeit in dieser Phase. Als Nebenprodukt der Vollständigkeitsanalyse entstand eine
  Tabelle mit einer Zeile pro Notice in `data/processed/`.
- **Erkenntnisse – Fakten:** Die Tabelle nutzt bei Datumsfeldern nur das erste Los. Auftraggebernamen sind nicht normalisiert.
- **Erkenntnisse – Interpretation:** Für den Backtest reicht die Tabelle so nicht aus.
- **Übergabe an die nächste Phase:** Keine. Phase 3 beginnt richtig in Iteration 2.

### Iteration 2 – 2026-10-23

- **Was gemacht:** Keine eigentliche Aufbereitung. Als Prototypen in Phase 2 entstanden:
  - einheitliches Laufzeitende (`end_date()` in `src/kennzahlen_iteration2.py`)
  - Normalisierung von Namen und Kennungen (`src/zuordnung_prototyp.py`)
  - XML-Auszug für eForms und alte TED-Formulare (`src/k2_xml_auszug.py`)
- **Erkenntnisse – Fakten:**
  - Exakte Namensgleichheit verpasst 5 von 15 Vorgängern mit abweichender Schreibweise.
  - Kennungen sind uneinheitlich bzw. zu grob.
  - Vor eForms liegen Laufzeit und Objektangaben nur in der XML.
- **Erkenntnisse – Interpretation:** Für eine Zuordnung über das Objekt braucht es Merkmale auf Los-Ebene und das Lesen der XML.
- **Übergabe an die nächste Phase:** Keine. Phase 3 beginnt erst, wenn Iteration 3 eine tragfähige Zuordnung zeigt.
