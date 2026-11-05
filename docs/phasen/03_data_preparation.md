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

_Stand: Iteration 9 (Abschluss), 2026-11-05. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Die Vertragsliste wurde in Iteration 9 um die Regeln 6 bis 10 verbessert (`src/prepare/vertragsliste.py`, Commit a03a4a8) und ist jetzt in dieser Fassung eingefroren: 9.325 statt 9.915 Lose, 590 Lose ohne Zuschlag entfernt. Auf einer neuen, ungesehenen Stichprobe stimmt das Ende der Grundlaufzeit zu 94,3 % mit dem Vergleichswert zweier KI-Leser überein (alte Fassung 92,9 %); das Höchstende bleibt ein Hinweis.

Quellen: **[BT5]** [backtest_iteration5.md](../../reports/backtest_iteration5.md) · **[E5]** [evaluation_iteration5.md](../../reports/evaluation_iteration5.md) · **[ZP]** [gt_pruefung_iteration5_auswertung.md](../../reports/gt_pruefung_iteration5_auswertung.md) · **[AN]** [backtest_analysen_iteration5.md](../../reports/backtest_analysen_iteration5.md) · **[VL]** [vertragsliste_iteration5.md](../../reports/vertragsliste_iteration5.md) · **[VP]** [verlaengerung_praxis_iteration5.md](../../reports/verlaengerung_praxis_iteration5.md) · **[HP]** [hoechstende_pruefung_iteration5_test.md](../../reports/hoechstende_pruefung_iteration5_test.md).
Iteration 6: **[LA6]** [liste_auswertung_iteration6.md](../../reports/liste_auswertung_iteration6.md) · **[E6]** [evaluation_iteration6.md](../../reports/evaluation_iteration6.md).
Iteration 7: **[LA7]** [liste_auswertung_iteration7.md](../../reports/liste_auswertung_iteration7.md) · **[E7]** [evaluation_iteration7.md](../../reports/evaluation_iteration7.md) · **[AC7]** [abschreibecheck_iteration7.md](../../reports/abschreibecheck_iteration7.md) · **[BL]** [beispiel_liste.md](../../reports/beispiel_liste.md).
Iteration 8: **[ZA8]** [zweitlesung_iteration8_auswertung.md](../../reports/zweitlesung_iteration8_auswertung.md) · **[E8]** [evaluation_iteration8.md](../../reports/evaluation_iteration8.md).
Iteration 9: **[ZA9]** [zweitlesung_iteration9_auswertung.md](../../reports/zweitlesung_iteration9_auswertung.md) · **[E9]** [evaluation_iteration9.md](../../reports/evaluation_iteration9.md) · **[VL9]** [vertragsliste_iteration9.md](../../reports/vertragsliste_iteration9.md).

### Fakten (aus den Daten)

- **Iteration 9:** Regeln 6 bis 10: Einzelwert nur bei längerer Liste (Regel 6 verschärft), Lose ohne Zuschlag entfallen (Status `winner-selection-status`, Nachlieferung der API, 5.215 Bekanntmachungen), Monatsnamen und Schrägstrichdaten, „maximal um N Jahre“ als Gesamtdauer, „N Jahre mit Option“ [VL9].
- Wirkung auf die Liste: 590 von 9.915 Losen (6,0 %) ohne Zuschlag entfernt, 79 mit Status „unbekannt“; 46 Lose ändern das Ende (39 entfallen durch Regel 6, 7 früher durch Regel 10), 56 nur das Höchstende; die Abdeckung beträgt 79,4 % [VL9].
- Neue Stichprobe (Seed 20261109, 110 Lose aus 104 Bekanntmachungen): V1 66/70 = 94,3 %, V2 28/30 = 93,3 %, V4 87,1 % und 85,2 % (verfehlt) [ZA9].
- Fehler im Ende der Grundlaufzeit (6 von 100): N7, N108, N79, N5 (Feld ist schon das Höchstende bzw. späteres Datum), N32 und N39 (Textdauer gegen Feld) [ZA9].
- Basisregel „Ende = Feld EndDate“ (nachträglich): Z 63/70 = 90,0 %, neue Fassung 66/70, alte 65/70; nur die neue Fassung trifft bei N9, N11 und N23 [ZA9].
- _Frühere Iterationen (weiter gültig):_
- Ende der Grundlaufzeit der Liste = Vergleichswert zweier KI-Leser bei 77/80 Zufallslosen (Wilson 89,5–98,7); Abweichungen L5, L33, L81 [ZA8].
- Am Original bestätigte Listenfehler [E8]: L5 („3 Jahre mit Option“ von Regel 1b nicht erkannt), L81 (Regel 6 überträgt den Einzelwert von Los 1 auf Los 2), L72 („um 3 Jahre“ als Länge je Verlängerung gelesen, Höchstende 2037 statt 2031), L82 (Datum „31. Oktober 2030“ nicht erkannt).
- Lose ohne Zuschlag (L69, L72) stehen in der Liste; die Liste filtert nicht nach dem Ergebnis je Los. Der Anteil ist nicht gezählt [E8].
- Regel 1b liest Fälle mit ausdrücklich genannter Grunddauer richtig (L3, L73, L77); der Typ „zum Schuljahresende“ (acht Lose des Landkreises Börde) ist nicht tagesgenau belegbar [E8].

### Interpretation

- Die Verbesserung der Regeln ist auf dieser Stichprobe kaum messbar (ein Los Vorsprung vor der alten Fassung, drei bis vier Lose vor dem bloßen Feld); die Regeln wirken nur bei wenigen Losen.
- Der Vergleichswert ist teilweise zirkulär (Definition und Liste nehmen standardmäßig das Feld als Ende der Grundlaufzeit); Fehler vom Typ „Feld ist schon das Höchstende“ lassen sich so kaum aufdecken [E9].
- Höchstende der Liste ist oft zu hoch (Anzahl mal Länge statt Textdatum): Es bleibt Hinweis, keine Zusage.
- Die Tabelle ist brauchbar, aber nicht als korrekt belegt: Die Leser gehören zur selben Modellfamilie wie die Regel und lasen über dasselbe Hilfsmodell.
- Regel 6 (Einzelwert gilt für alle Lose) ist systematisch fehleranfällig; die Abdeckung 79,7 % kann leicht zu hoch sein, das Ausmaß ist unbekannt.

## Offene Fragen

- [x] _(erledigt Iteration 9: 590 von 9.915 Losen = 6,0 % ohne Zuschlag nach Statusfeld, 39 Lose verlieren das Ende durch Regel 6)_ Wie viele Lose der Liste haben keinen Zuschlag, und wie viele sind von Regel 6 (Übertragung eines Einzelwerts auf andere Lose) betroffen?
- [ ] _(neu, Iteration 7)_ Stimmt Regel 1b, wenn ein zweiter, unabhängiger Leser die Originale liest (auch Typ „text_festlaufzeit“)? Nennt der Text bei Losen mit Feldübernahme eine kürzere feste Laufzeit?
- [x] _(neu, Iteration 6)_ Welche Formulierungen und Feldkombinationen zeigen, dass BT-537 schon das Höchstende ist (Regel 1a erweitern, z. B. BT-54 „zwei Jahre … (2+1+1)“, „Festlaufzeit von … bis …“, Beginn + Dauer im Text kürzer als Beginn–Ende)? Test nur an neuen Losen.
  _Antwort Iteration 7:_ Regel 1b (`kurze_festlaufzeit`): feste Laufzeit mit Datum oder Dauer im Text, nur bei Option/Verlängerung; Wirkung nicht belegt (8/15, Prüfdesign verzerrt) [E7].
- [ ] _(neu, Iteration 6)_ Wie wird die Stichprobe so gezogen, dass große Bekanntmachungen (viele Lose mit derselben Formulierung) nicht untergewichtet sind?
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
| 2026-11-04 | 6 | Zurück zu Phase 3: Regel für „Enddatum = Höchstende“ erweitern und vor dem Ziehen einer neuen Stichprobe committen; neue Stichprobe (ohne geprüfte Lose) mit Vorlage ohne Listenwerte | Y1 88,3 % nach Korrektur (L60), Verankerung, offene Unabhängigkeit (reports/evaluation_iteration6.md). Entscheidung des Nutzers. |
| 2026-11-04 | 7 | Kein dritter Regelversuch: Regel 1b bleibt im Stand von Commit a93785e eingefroren; Ende der Grundlaufzeit gilt als „laut Bekanntmachung“, Höchstende nur als Hinweis | Y1 76,6 % (zwischen 70 und 90 %, vorab festgelegte Folge), Y1r 8/15, Y2/Y2b verfehlt (reports/evaluation_iteration7.md). Entscheidung des Nutzers. |
| 2026-11-05 | 8 | Keine weitere Regeländerung; Fehlerarten L5, L81 (Regel 6), L69/L72 (kein Zuschlag), L72/L82 (Höchstende) bleiben offene Grenzen | Z1 77/80, aber Leser nicht unabhängig (reports/evaluation_iteration8.md). Entscheidung des Nutzers. |
| 2026-11-05 | 9 | Weiter (Projektabschluss), eingeschränkt formuliert: Die Fassung der Iteration 9 (Regeln 1 bis 10) wird der Prototyp; das Höchstende bleibt Hinweis; V4, V7 und V8 werden offen als verfehlt bzw. teilweise berichtet; keine weitere Iteration | V1 66/70, V2 28/30, V3 66 gegen 65 (erfüllt), V5 110/110, V6 14/15; V4 verfehlt, V7 verfehlt (Ursache in der Anweisung, nicht im Filter), V8 teilweise ([ZA9], [E9]). Entscheidung des Nutzers nach dem Vorschlag und der Gesamtprüfung des Evaluators. |

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

### Iteration 6 – 2026-11-04

- **Was gemacht:** Abdeckung der 744 Lose ohne Enddatum analysiert (neue Spalte `gl_geschaetzt` nur für den Prototyp, zählt nicht); Stichprobe von 60 Zufallslosen mit Seed (`src/prepare/stichprobe_iteration6.py`), Prüfung durch den Nutzer, Auswertung (`src/prepare/auswertung_iteration6.py`), Evaluator.
- **Erkenntnisse – Fakten:** Ende der Grundlaufzeit 54/60 = 90,0 % laut Auswertung, 53/60 = 88,3 % nach L60; Höchstende 55/60 = 91,7 %; Abdeckung 79,7 %. Fehlertyp: Enddatum der Bekanntmachung ist schon das Höchstende (L1, L42, L43, L60; 143100-2026) (reports/liste_auswertung_iteration6.md, reports/evaluation_iteration6.md).
- **Erkenntnisse – Interpretation:** Die Lese-Regeln tragen für das Höchstende, aber nicht für das Ende der Grundlaufzeit bei „fester Laufzeit mit Option“; die Prüfung war durch den angezeigten Listenwert verankert, die Quote ist eher eine Untergrenze der Fehler.
- **Übergabe an die nächste Phase:** Regel 1a erweitern und vor dem Ziehen committen; neue Stichprobe mit Vorlage ohne Listenwerte und Hilfsmittel je Eintrag; danach Prototyp (Phase 6) neu erzeugen.

### Iteration 7 – 2026-11-04

- **Was gemacht:** Regel 1b (`kurze_festlaufzeit`) gebaut und vor dem Ziehen committet; Entwicklungstest an den 60 Losen der Iteration 6; Stichprobe (80 Zufallslose + 15 Regelwirkungs-Lose, Seed 20261106), Prüfung und Nachprüfung durch den Nutzer, Abschreibe-Check, Auswertung.
- **Erkenntnisse – Fakten:** Regel 1b ändert 165 Lose; Y1 36/47 = 76,6 %, Y1r 8/15, Quelle „Text“ 12/12; 45 der 47 Zufallslose mit Ende aus dem Feld (reports/liste_auswertung_iteration7.md, reports/evaluation_iteration7.md).
- **Erkenntnisse – Interpretation:** Die Prüfung konnte die Regel nicht von Lesefehlern trennen; die Regel ist weder belegt noch widerlegt. Weitere Regelarbeit lohnt ohne unabhängigen Leser nicht.
- **Übergabe an die nächste Phase:** Liste eingefroren (a93785e) an Phase 5 (KI-Zweitlesung als reine Messung) und Phase 6 (Kennzeichnung „laut Bekanntmachung“, Höchstende als Hinweis).

### Iteration 8 – 2026-11-05

- **Was gemacht:** Keine Änderung an Daten oder Regeln; die Liste (Stand a93785e) wurde von zwei KI-Lesern gegengelesen.
- **Erkenntnisse – Fakten:** Z1 77/80; neue Fehlerarten L5, L81, L69/L72, L72/L82 (reports/zweitlesung_iteration8_auswertung.md, reports/evaluation_iteration8.md).
- **Erkenntnisse – Interpretation:** Die Liste trägt als „laut Bekanntmachung, durch KI-Lesung gestützt“; ihre Fehlerquote bleibt ohne menschliche Prüfung offen.
- **Übergabe an die nächste Phase:** Keine weitere Iteration; offene Grenzen ins Lab-Log.

### Iteration 9 – 2026-11-05

- **Was gemacht:** Regeln 6 bis 10 vor der Stichprobe festgelegt und committet, Zuschlagsfelder nachgeladen, neue Stichprobe gezogen (Seed 20261109), Rohtexte aus dem TED-XML, Fassung der Liste eingefroren.
- **Erkenntnisse – Fakten:** 9.325 Lose; V1 66/70, V2 28/30; Fehlerarten L5, L81, L72, L82 behoben, neue Fehler vom Typ „Feld = Höchstende“ in 6 von 100 Losen (reports/zweitlesung_iteration9_auswertung.md, reports/evaluation_iteration9.md).
- **Erkenntnisse – Interpretation:** Die neue Fassung ist etwas besser als die alte, der Nutzen ist durch die Stichprobe nicht gesichert; das Höchstende bleibt Hinweis.
- **Übergabe an die nächste Phase:** Prototyp neu erzeugen (Phase 6), Lab-Log und Folien aktualisieren.
