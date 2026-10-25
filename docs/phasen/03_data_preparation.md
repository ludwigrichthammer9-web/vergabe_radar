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

_Stand: Iteration 3 (Abschluss), 2026-10-25. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Phase 3 ist noch nicht richtig begonnen. In Iteration 3 sind weitere Bausteine für die Aufbereitung entstanden. Iteration 4 arbeitet
in Phase 2/3 an den Objektmerkmalen auf Los-Ebene.

### Fakten (aus den Daten)

- `build_table()` in [src/analyze_completeness.py](../../src/analyze_completeness.py) erzeugt eine Tabelle pro Notice. Datumsfelder
  stammen aus dem ersten Los; 15,3 % der Notices haben mehrere Lose. [R §1]
- `end_date()` in [src/kennzahlen_iteration2.py](../../src/kennzahlen_iteration2.py) vereinheitlicht das Laufzeitende: Enddatum,
  sonst Beginn + Dauer; Laufzeiten ≤ 0 oder > 240 Monate werden verworfen.
  [reports/kennzahlen_iteration2.md](../../reports/kennzahlen_iteration2.md)
- [src/k2_xml_auszug.py](../../src/k2_xml_auszug.py) liest Titel, Lose, Ort und Laufzeit aus eForms- und alter TED-XML und folgt
  bei alten Zuschlägen `REF_NOTICE` zur alten Ausschreibung. [src/a11_stichprobe.py](../../src/a11_stichprobe.py) nutzt das für die
  A11-Stichprobe (25/30 bestimmbar). [reports/a11_stichprobe.md](../../reports/a11_stichprobe.md)
- _(neu, Iteration 3)_ [src/objekt_merkmale.py](../../src/objekt_merkmale.py) extrahiert Titel, Ort, PLZ und Straße je Notice (eForms
  über die API, vor eForms über die XML, nur für Kandidaten). [src/zuordnung_objekt.py](../../src/zuordnung_objekt.py) vergleicht
  Auftraggeber unscharf (Jaccard bzw. Überlappung der Namenswörter) und Objektwörter ohne Allerweltswörter und ohne Namen/Sitz des
  Auftraggebers. [reports/regel_entwicklung_iteration3.md](../../reports/regel_entwicklung_iteration3.md)
- _(neu, Iteration 3)_ Auf den Testdaten: Präzision 45,8 %, Trefferquote 28,9 %. 9 von 11 Fehlern sind Geschwisterverfahren desselben
  Auftraggebers, 2 dasselbe Objekt mit anderer Leistungsart. Bei 19 von 38 Fällen kein Vorschlag, meist weil vor eForms Titel und Ort
  in den Rohdaten fehlen. [reports/zuordnung_iteration3.md](../../reports/zuordnung_iteration3.md),
  [reports/evaluation_iteration3.md](../../reports/evaluation_iteration3.md)
- _(neu, Iteration 3)_ `auswertung_iteration3.py` nimmt als Vorgänger-Ende das Ende der Grundlaufzeit des vorgeschlagenen Notice; bei
  T26 (aufgehobenes Verfahren) und T56 (jährliche Verlängerung) ist das falsch bzw. unbekannt. [E3]
- `buyer-identifier` ist uneinheitlich und teils für mehrere Niederlassungen gleich. [reports/evaluation_iteration2.md](../../reports/evaluation_iteration2.md)

### Interpretation

- Merkmale auf **Los-Ebene** (Objektliste, Adresse, Fläche, Leistungsart) sind der Engpass, vor allem vor eForms. Ohne sie lassen
  sich Geschwisterverfahren nicht trennen.
- Das Vorgänger-Ende braucht eine Herkunftskennzeichnung (Grundlaufzeit, Höchstende, aufgehoben, unbekannt), bevor es in einen
  Backtest geht.
- Eine Tabelle pro Los mit vereinheitlichtem Laufzeitende bleibt das Ziel für den Backtest.

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
