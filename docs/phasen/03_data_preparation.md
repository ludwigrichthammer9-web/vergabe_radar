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

_Stand: Iteration 5 (Abschluss), 2026-11-04. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Die Zuschlagstabelle je Los ist gebaut. Offen bleiben Lese-Regeln für Vorgänger vor eForms und Auftraggeber-Normalisierung.

Quellen: **[BT5]** [backtest_iteration5.md](../../reports/backtest_iteration5.md) · **[E5]** [evaluation_iteration5.md](../../reports/evaluation_iteration5.md) · **[ZP]** [gt_pruefung_iteration5_auswertung.md](../../reports/gt_pruefung_iteration5_auswertung.md) · **[AN]** [backtest_analysen_iteration5.md](../../reports/backtest_analysen_iteration5.md) · **[VL]** [vertragsliste_iteration5.md](../../reports/vertragsliste_iteration5.md) · **[VP]** [verlaengerung_praxis_iteration5.md](../../reports/verlaengerung_praxis_iteration5.md) · **[HP]** [hoechstende_pruefung_iteration5_test.md](../../reports/hoechstende_pruefung_iteration5_test.md).

### Fakten (aus den Daten)

- `src/prepare/vertragsliste.py`: 9.915 Lose aus 4.209 eForms-Zuschlägen (Population wie Iteration 4); je Los Ende der Grundlaufzeit, Höchstende, Herkunft, R0, R1 [VL].
- Abdeckung: 2.924/3.668 = 79,7 % der Lose (Q4 2025–Q3 2026) mit Prognosedatum; 20,0 % ohne Laufzeit [VL].
- Höchstende-Herkunft: keine Angabe 32,3 %, Anzahl × Länge 22,0 %, Datum im Text 17,7 %, unbestimmbar 13,3 %, Höchstlaufzeit 8,8 %, Enddatum = Höchstende 4,5 % [VL].
- Lese-Regeln: Entwicklung 30/40, Test 53/60 richtig (gewichtet etwa 91 %), Urteile von Claude allein, nur eForms-Lose; „keine_verlaengerung“ ungeprüft [HP], [E5].
- `src/prepare/backtest_paare.py`: Paare aus der Handsuche, Vorgänger-Ende aus der Bekanntmachung (vor eForms über `REF_NOTICE` aus der XML); 61 von 68 bestimmbar.

### Interpretation

- Die Vertragsliste ist reproduzierbar aus den Rohdaten gebaut und deckt etwa vier Fünftel der Lose ab; fehlende Laufzeiten bremsen, nicht die Lese-Regeln.
- Für den Einsatz auf Verträgen vor eForms sind die Lese-Regeln nicht getestet; im Backtest 41 von 52 Vorgängern.

## Offene Fragen

- [x] Tabelle pro Vertrag oder pro Los? _Antwort Iteration 5:_ pro Los (`src/prepare/vertragsliste.py`).
- [x] Wie wird das Laufzeitende vereinheitlicht (Ende direkt oder Start + Dauer, ersatzweise Veröffentlichungsdatum + Dauer)?
  _Antwort Iteration 5:_ Ende direkt, sonst Beginn + Dauer; Ausnahme Regel 1a; Höchstende aus BT-58 und Freitext [VL].
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
| 2026-10-30 | 5 | Zuschlagstabelle je Los mit Grundlaufzeit und Höchstende; Höchstende = spätester plausibler Kandidat aus Datum, Höchstlaufzeit, BT-36 und Anzahl × Länge im Freitext; Regel 1a (Enddatum ist Höchstende) | Praxis der Felder (reports/verlaengerung_praxis_iteration5.md), Entwicklungs- und Teststichprobe (reports/hoechstende_pruefung_iteration5_*.md) |
| 2026-10-30 | 4 | Die Regel `zuordnung_los.py` wird nicht in die Aufbereitung übernommen; Merkmale je Los (`los_merkmale.py`) und Laufzeitende mit Herkunft werden Grundlage der Zuschlagstabelle in Iteration 5 | Entscheidung „Idee anpassen“ nach Iteration 4 (reports/evaluation_iteration4.md). Entscheidung des Nutzers. |
| 2026-11-04 | 5 | Die Vertragsliste je Los (Grundlaufzeit, Höchstende, Herkunft) ist der Datenstand für Iteration 6/7; die Backtest-Paare werden nur für die Bewertung genutzt | Entscheidung „Idee anpassen“ nach Iteration 5 (reports/evaluation_iteration5.md). Entscheidung des Nutzers. |

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

### Iteration 5 – 2026-11-04

- **Was gemacht:** Zuschlagstabelle je Los mit Lese-Regeln für das Höchstende (Entwicklungs- und Teststichprobe); Backtest-Paare mit Vorgänger-Ende; Zweitprüfungsvorlage mit Ködern.
- **Erkenntnisse – Fakten:** 9.915 Lose, X4 = 79,7 %, Höchstende-Genauigkeit im Test 53/60; 61 von 68 Paaren mit bestimmbarem Ende (reports/vertragsliste_iteration5.md, reports/hoechstende_pruefung_iteration5_test.md).
- **Erkenntnisse – Interpretation:** Die Tabelle trägt eine Vertragsliste; Vorgänger vor eForms sind für die Lese-Regeln ungeprüft.
- **Übergabe an die nächste Phase:** An Phase 6 (Prototyp, Iteration 7): Liste je Los. An Phase 4: nur bei Prognose-Variante je Auftraggeber.
