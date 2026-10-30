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

_Stand: Iteration 4 (Abschluss), 2026-10-30. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Phase 3 hat mit Iteration 4 Bausteine für Merkmale je Los bekommen. Die eigentliche Aufbereitung für die Prognose beginnt in Iteration 5,
jetzt mit Zuschlägen und ihrem Laufzeitende als Kern.

### Fakten (aus den Daten)

Quellen: **[Z4]** [zuordnung_iteration4.md](../../reports/zuordnung_iteration4.md) und [zuordnung_iteration4_korrektur.md](../../reports/zuordnung_iteration4_korrektur.md) · **[GT4]** [sichtbarkeit_iteration4_gt.csv](../../reports/sichtbarkeit_iteration4_gt.csv) · **[BP4]** [blindpruefung_iteration4.md](../../reports/blindpruefung_iteration4.md) · **[RE4]** [regel_entwicklung_iteration4.md](../../reports/regel_entwicklung_iteration4.md) · **[E4]** [evaluation_iteration4.md](../../reports/evaluation_iteration4.md). Ältere Quellen siehe Iterationslog.

- `src/los_merkmale.py` liest je Los Leistungsart, Flächen, Adressen und Objektnamen, bei eForms aus der API (mit Beschreibungen), vor
  eForms aus der XML.
- `src/zuordnung_los.py` (eingefroren 1d0e060) sucht Kandidaten über Auftraggeber, PLZ, seltene Namenswörter und Volltext; im Test
  19 Vorschläge, 17 korrekt, Trefferquote 56,7 % [Z4].
- `src/kennzahlen_iteration2.py` (`end_date()`) vereinheitlicht das Laufzeitende; `src/a11_stichprobe.py` liest es vor eForms über
  `REF_NOTICE`.
- Das Vorgänger-Ende braucht eine Herkunft: Die Auswertung zählte „grundlaufzeit, hoechstende“ zunächst nicht mit (korrigiert) [E4].

### Interpretation

- Für Iteration 5 wird eine Tabelle der Zuschläge je Los gebraucht: Laufzeitende mit Herkunft (Grundlaufzeit, Höchstende, rollierend),
  Leistungsart und Objektmerkmale aus `los_merkmale.py`.
- Die Objekt-Zuordnung bleibt nur als Werkzeug, um Paare für einen Backtest vorzuschlagen, die dann von Hand geprüft werden.

## Offene Fragen

- [ ] Tabelle pro Vertrag oder pro Los?
- [ ] Wie wird das Laufzeitende vereinheitlicht (Ende direkt oder Start + Dauer, ersatzweise Veröffentlichungsdatum + Dauer)?
- [ ] Wie werden Verlängerungen aus dem Freitext (BT-54, BT-57) strukturiert erfasst?
- [ ] Wie werden Auftraggeber normalisiert (gleiche Behörde, unterschiedliche Schreibweisen; ggf. über Kennungen)?
- [ ] Wie ordnen wir Neuausschreibungen den ursprünglichen Verträgen zu (Annahme A9)?
  _Stand Iteration 2:_ Über Auftraggeber + CPV nicht (K2 = 16,7 %). Nächster Versuch über das Objekt (A9b), zunächst in Phase 2.
- [ ] _(neu, Iteration 2)_ Wie werden Adresse, Liegenschaftsname und Titel je Los extrahiert und normalisiert, auch aus alter TED-XML?
  _Stand Iteration 3:_ erste Fassung auf Notice-Ebene in `src/objekt_merkmale.py`; vor eForms nur für Kandidaten aus der XML. Für
  Geschwisterverfahren reicht das nicht, nötig sind Objektlisten, Flächen und Leistungsart je Los (Iteration 4).
- [ ] _(neu, Iteration 3)_ Wie wird die Herkunft des Vorgänger-Endes gekennzeichnet (Grundlaufzeit, Höchstende, aufgehobenes
  Verfahren, unbekannt)?
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
| 2026-10-25 | 3 | Die Objekt-Regel aus Iteration 3 (Commit 4497743) wird nicht in die Aufbereitung übernommen; Iteration 4 baut Merkmale auf Los-Ebene (auch vor eForms) als letzten Verbesserungsversuch | Präzision 45,8 %, Trefferquote 28,9 % (reports/zuordnung_iteration3.md, reports/evaluation_iteration3.md). Entscheidung des Nutzers. |
| 2026-10-30 | 4 | Die Regel `zuordnung_los.py` wird nicht in die Aufbereitung übernommen; Merkmale je Los (`los_merkmale.py`) und Laufzeitende mit Herkunft werden Grundlage der Zuschlagstabelle in Iteration 5 | Entscheidung „Idee anpassen“ nach Iteration 4 (reports/evaluation_iteration4.md). Entscheidung des Nutzers. |

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

### Iteration 3 – 2026-10-25

- **Was gemacht:** Keine eigentliche Aufbereitung. Als Prototypen in Phase 2 entstanden:
  - Objektmerkmale je Notice (`src/objekt_merkmale.py`)
  - Zuordnungsregel über das Objekt mit unscharfem Auftraggebervergleich (`src/zuordnung_objekt.py`)
  - Laufzeit vor eForms über `REF_NOTICE` (`src/a11_stichprobe.py`)
- **Erkenntnisse – Fakten:**
  - Präzision 45,8 %, Trefferquote 28,9 %; Fehler vor allem bei Geschwisterverfahren, fehlende Vorschläge vor allem vor eForms.
  - Vorgänger-Enddaten sind teils falsch übernommen (T26, T56).
  - Laufzeit vor eForms bei 25 von 30 Zuschlägen über `REF_NOTICE` bestimmbar.
- **Erkenntnisse – Interpretation:** Merkmale auf Notice-Ebene reichen nicht; es braucht Los-Ebene und eine Herkunftskennzeichnung
  des Laufzeitendes.
- **Übergabe an die nächste Phase:** Iteration 4 (Phase 2/3) baut Objekt- und Leistungsart-Merkmale auf Los-Ebene, auch vor eForms,
  und misst die verbesserte Zuordnung auf neuen Testdaten. Erst danach beginnt die eigentliche Aufbereitung für den Backtest.

### Iteration 4 – 2026-10-30

- **Was gemacht:** Merkmale je Los (`src/los_merkmale.py`), Kandidatensuche mit Volltext und Regel (`src/zuordnung_los.py`), Download mit
  Los-Texten (`src/ted_download.py --los-texte`), Auswertung mit Korrektur der Zählung des Vorgänger-Endes (`src/auswertung_iteration4.py`).
- **Erkenntnisse – Fakten:** Merkmale je Los lassen sich für eForms aus den API-Feldern und vor eForms aus der XML gewinnen; Flächen
  stehen nur bei gut einem Drittel im Text; die Herkunft des Laufzeitendes ist oft gemischt („grundlaufzeit, hoechstende“).
- **Erkenntnisse – Interpretation:** Die Bausteine taugen für eine Zuschlagstabelle je Los; die Zuordnung taugt nur als Vorschlagswerkzeug.
- **Übergabe an die nächste Phase:** Iteration 5 baut die Tabelle der Zuschläge mit Laufzeitende und Herkunft (auch vor eForms) als Grundlage
  für Prognose und Backtest.
