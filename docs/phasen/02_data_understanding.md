# Phase 2: Data Understanding

> **Ziel:** Verstehen, welche Daten es gibt, wie gut sie sind und was sie hergeben.
> **Weiter, wenn:** Für die gewählte Nische genug Datensätze mit verwertbarer Laufzeit vorliegen.
> **Zurück zu Phase 1, wenn:** Die Daten für die Nische nicht reichen.
> Details: [CRISP-DM.md](../CRISP-DM.md#2-data-understanding)
>
> **Artefakte laut CRISP-DM.md:**
> - Datenqualitätsreport: vorhanden als [reports/datenqualitaet_DEU_20260722_20261021.md](../../reports/datenqualitaet_DEU_20260722_20261021.md)
> - Skripte in `src/ingest/`: liegen derzeit direkt in `src/` ([ted_download.py](../../src/ted_download.py), [analyze_completeness.py](../../src/analyze_completeness.py))

---

## Aktueller Stand

_Stand: Iteration 2 (Abschluss), 2026-10-23. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Quellen: **[R]** `reports/datenqualitaet_DEU_20260722_20261021.md` · **[S]** `reports/stichprobe_iteration1.md` ·
**[E1]** `reports/evaluation_iteration1.md` · **[RR]** [rueckreichweite_909.md](../../reports/rueckreichweite_909.md) ·
**[K]** [kennzahlen_iteration2.md](../../reports/kennzahlen_iteration2.md) · **[Z]** [zuordnung_iteration2.md](../../reports/zuordnung_iteration2.md) ·
**[P]** [k2_pruefliste.md](../../reports/k2_pruefliste.md) · **[X]** [k2_auszuege.md](../../reports/k2_auszuege.md) ·
**[E2]** [evaluation_iteration2.md](../../reports/evaluation_iteration2.md) · **[Erg]** [ergebnis_iteration2.md](../../reports/ergebnis_iteration2.md) ·
**[PR]** Probeabfragen vom 23.10.2026 in `data/raw/ted_probes/20261023/` · **[Sp]** OpenAPI https://ted.europa.eu/docs/v3 ·
**[F]** Feldliste https://docs.ted.europa.eu/ODS/latest/reuse/field-list.html · **[SDK]** eForms SDK `translations/business-term_en.xml`.

### Fakten (aus den Daten)

**Datenquelle**
- TED Search API v3 (`POST https://api.ted.europa.eu/v3/notices/search`, ohne API-Key). Pro Seite höchstens 250 Notices,
  ITERATION-Modus unbegrenzt. [Sp]
- **Rückreichweite:** ab Ende Oktober 2016 (erste Notices 21.–28.10.2016), davor 0 Treffer. [PR q04–q09, q17]
- **Formatwechsel:** Haupt-CPV (`main-classification-proc`) ist ab Ende Oktober 2023 befüllt, davor nie. [PR q16], [RR]
- **Notices vor eForms:** Die API liefert nur Nummer, Datum, Formular- und Bekanntmachungstyp, CPV-Liste, Auftraggebername und Ort.
  Laufzeit, Haupt-CPV, Kennung und Titel fehlen. [PR q11, q15]
- **Laufzeit vor eForms:** Alte Zuschläge (F03/F06) enthalten keine Laufzeit. Sie verweisen aber über `REF_NOTICE` auf die alte
  Ausschreibung (F02/F05), und dort stehen Beginn und Ende. Das gilt für 10 von 10 Fällen in der Stichprobe (5 mit Verlängerung);
  die Stichprobe ist durch die Auswahlregel bestimmt, nicht zufällig. [X], [E2]
- **Definitionen:** BT-36 schließt laut eForms Optionen und Verlängerungen ein, BT-537 ist offen formuliert. [SDK]

**Geladene Datensätze** (Rohdaten unverändert in `data/raw/ted_search/`)
- Iteration 1: alle deutschen Zuschläge 22.07.–21.10.2026 (15.706). [R]
- Iteration 2: Gebäudereinigungs-Ausschreibungen Q2 2026 (710 Notices, davon 159 = 22,4 % Änderungen, 551 Verfahren) und alle
  Zuschläge mit CPV 909 in der CPV-Liste seit Okt. 2016 (15.361; vollständig, gleich der Summe der Quartalszählungen). [RR], [Z]

**Basisraten Gebäudereinigung (DEU)** [RR]
- Zuschläge 1.250–1.750 pro Jahr, stabil. Ausschreibungs-Notices 2024/2025 je ca. 2.560–2.780, nach Abzug der Änderungen grob
  1.990–2.160 Verfahren. Pro Zuschlag vor eForms ca. 1,1, seit eForms ca. 1,6 Ausschreibungs-Notices (ungeklärt).
- Vorinformationen: rund 30 pro Jahr.

**Laufzeitende bestimmbar (Haupt-CPV 909, Notice-Ebene)**

| Fenster | Anteil | 95-%-KI | n | Quelle |
|---|---|---|---|---|
| Q3 2026 (Iteration 1, Schwelle nachträglich) | 80,9 % | 77,0–84,3 % | 440 | [R], [E1] |
| Q2 2025 (K4, Schwelle vorab) | 82,1 % | 77,9–85,5 % | 390 | [K] |
| 2023 ab 25.10. | 70,7 % | 64,7–76,1 % | 239 | [K] |
| 2024 | 70,1 % | 67,8–72,2 % | 1.623 | [K] |
| 2025 | 79,7 % | 77,7–81,6 % | 1.619 | [K] |

- Median-Laufzeit Gebäudereinigung aus Beginn/Ende 36 Monate (Q3 2026). [R]
- Vergleich der Nischen aus Iteration 1 (Q3 2026): Winterdienst 84,5 %, Sicherheitsdienste 83,9 %, IT-Dienste 33,7 %. [R §5]

**Zuordnung Ausschreibung → früherer Zuschlag** (Q2 2026, Regel: gleicher Auftraggebername oder gleiche Kennung) [Z], [P]
- K1: 461 von 551 (83,7 %) haben einen früheren Zuschlag desselben Auftraggebers. Bei 248 davon gibt es mehr als 10 Kandidaten.
- K2: Nur bei 5 von 30 zufälligen Treffern ist plausibel dieselbe Leistung gemeint (16,7 %, KI 7,3–33,6 %). Beurteilt von Claude,
  der Evaluator stimmte in 29 von 30 Fällen zu. Typischer Fehler: gleicher Auftraggeber, anderes Objekt. [E2]
- A30: Der objektgleiche Vorgänger (775273-2024) war unter den Kandidaten und wurde nicht gewählt. [E2]
- Unter 6 objektgleichen Paaren (5 aus K2 plus A30) sind 3 vorzeitige Neuvergaben (A8, A24, A30). Nur bei A13 ist der Vorlauf
  unabhängig gemessen: 5,1 Monate. [Erg]
- Von 15 Ausschreibungen ohne Treffer haben 5 einen früheren 909-Zuschlag unter abweichendem Namen. 3 sind einmalige Leistungen,
  bei 6 gibt es per Namenssuche keinen früheren Zuschlag im Pool. [P]
- Haupt-CPV 909 enthält auch Schädlingsbekämpfung, Fahrzeug- und Industriereinigung sowie Bau- und Sonderreinigung. [X], [E2]

**Backtest-Basis (K5)** [K]
- 629 eForms-Zuschläge mit Laufzeitende bis 23.10.2026. Median-Laufzeit 12 Monate (alle eForms-Zuschläge: 36). 410 davon
  wurden 2024 veröffentlicht. 187 haben eine Verlängerungsoption (BT-58 ≥ 1). [E2]

### Interpretation

- **Die Zuordnung über den Auftraggeber taugt nicht für das Radar.** Große Auftraggeber vergeben viele Reinigungsverträge parallel.
  Die Regel erkennt, *dass* sie wieder ausschreiben, nicht *welcher* Vertrag ausläuft.
- **Ob die Vorgänger überhaupt auf TED stehen (Sichtbarkeit), ist nicht gemessen.** Einige Befunde sprechen für ein Methodenproblem
  (A30, Fehler fast nur bei vielen Kandidaten), andere für Lücken in den Daten (Fälle ohne Vorgänger, 1,6 Ausschreibungen pro
  Zuschlag). Das klärt Iteration 3.
- **Eine Prognose aus „Vertragsende minus Vorlauf“ ist fraglich.** Verlängerungen verschieben das Ende um Jahre, und vorzeitige
  Neuvergaben kommen vor. Bei n = 6 ist das nur ein Hinweis.
- **Ein Backtest nur mit eForms-Daten wäre verzerrt** (fast nur Einjahresverträge, überwiegend aus 2024 mit schwächerer Befüllung).
  Daten vor eForms sind über die XML erreichbar und für einen unverzerrten Backtest wohl nötig.
- **Die 80-%-Quote für ein bestimmbares Laufzeitende gilt ab 2025, nicht für 2023/2024.**
- **Die Nische muss enger abgegrenzt werden** als „Haupt-CPV 909“, damit nur wiederkehrende Gebäudereinigung zählt.

## Offene Fragen

- [x] Wie weit zurück sind die Daten brauchbar? Zahl der 909-Zuschläge seit Ende Oktober 2023 und Verteilung ihrer Enddaten. Enthalten die Formate vor eForms Laufzeiten (A10, A11)?
  _Teilantwort 2026-10-23:_ Such-API ab Ende Oktober 2016; vor eForms keine Laufzeit über die API, wohl aber in der XML alter Ausschreibungen (1 Fall) [P], [X].
  _Antwort Iteration 2 (Abschluss):_ API ab Okt. 2016. 4.905 eForms-Zuschläge, davon 629 abgelaufen (Median 12 Monate) [K]. Vor eForms
  Laufzeit über REF_NOTICE in der alten Ausschreibung, 10 von 10 in nicht zufälliger Stichprobe [X]. Repräsentative Prüfung offen.
- [x] Erscheinen Neuausschreibungen für CPV 909 als Auftragsbekanntmachungen (competition) auf TED, und wie viele pro Jahr? Gibt es Vorinformationen (PIN) als Frühsignal?
  _Antwort Iteration 2:_ ja, grob 1.990–2.160 Verfahren pro Jahr (2024/2025, hochgerechnet); PIN rund 30 pro Jahr, als Frühsignal bedeutungslos [RR].
- [x] Lassen sich Zuschlag und Neuausschreibung zuordnen, z. B. über Auftraggeber und CPV (A9)?
  _Antwort Iteration 2:_ über Auftraggeber + CPV **nein** (K2 = 16,7 %) [P], [E2]. Zuordnung über das Objekt: siehe neue Frage unten.
- [ ] _(neu, Iteration 2)_ Wie oft gibt es zu einer Ausschreibung überhaupt einen objektgleichen Vorgänger auf TED (Sichtbarkeit),
  gesucht unter Zuschlägen **und** früheren Ausschreibungen? (A3, A9b)
- [ ] _(neu, Iteration 2)_ Lässt sich der Vorgänger automatisch über Adresse, Liegenschaftsname und Titel zuordnen, auch bei großen
  Auftraggebern (A9b)?
- [ ] _(neu, Iteration 2)_ Wie häufig sind vorzeitige Neuvergaben (A16)?
- [ ] _(neu, Iteration 2)_ Wie grenzt man „wiederkehrende Gebäudereinigung“ ab (Ausschluss von Schädlingsbekämpfung, Bau- und
  Sonderreinigung, Fahrzeug- und Industriereinigung) (A12)?
- [ ] _(neu, Iteration 2)_ Warum gibt es seit eForms etwa 1,6 Ausschreibungs-Notices pro Zuschlag (vorher 1,1), auch nach Abzug der
  Änderungen etwa 1,2?
- [ ] _(neu, Iteration 2)_ Warum ist das Laufzeitende 2023/2024 nur bei etwa 70 % bestimmbar, ab 2025 bei etwa 80 %?
- [ ] Meinen BT-36/BT-536/BT-537 die Laufzeit mit oder ohne Verlängerungen? (eForms-Dokumentation prüfen)
  _Teilantwort 2026-10-23:_ BT-36 laut Definition **mit** Optionen und Verlängerungen; BT-537 ohne Aussage [SDK]. Praxis ungeprüft.
- [ ] _(neu, 2026-10-23)_ Enthalten alte Zuschläge (F03) generell keine Laufzeit, und lässt sie sich zuverlässig über `REF_NOTICE`
  aus der alten Ausschreibung (F02) holen? Bisher 1 Fall [X].
  _Stand Abschluss Iteration 2:_ 10 von 10 in nicht zufälliger Stichprobe; Zufallsstichprobe (z. B. 30 aus 2018–2023) offen [E2].
- [ ] Warum ist bei 84 von 440 Gebäudereinigungs-Notices kein Laufzeitende bestimmbar? Stichprobe von etwa 20 Fällen.
- [x] Hält die Quote in einem unabhängigen Zeitfenster (z. B. ein Frühjahrsquartal 2025), mit vorab festgelegter Schwelle (A13)?
  _Antwort Iteration 2:_ ja für Q2 2025 (82,1 %, KI 77,9–85,5 %), nicht für 2023/2024 (rund 70 %) [K].
- [ ] Wie sieht die Befüllung auf Los-Ebene aus statt auf Notice-Ebene?
- [x] Bedeutet `-1` „nicht veröffentlicht“? Teilweise belegt durch 2 Fälle mit FieldsPrivacy [S] (A7).
- [ ] Wie oft stehen Verlängerungen nur im Freitext (quantifizieren statt aus einem Einzelfall verallgemeinern)?
- [ ] Wie häufig ist Kantinenbetrieb, und wie gut ist er befüllt?
- [ ] Zeigen Vertragsänderungen (can-modif) ausgeübte Verlängerungen?
- [x] Wie viele Datensätze mit verwertbarer Laufzeit gelten als „genug“? Nachträglich: ≥ 80 % bestimmbares Laufzeitende (siehe iterationen.md).

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| 2026-10-22 | 1 | Abfrage mit `form-type=result`, ohne can-modif und veat | Nur echte Zuschläge sind neue Verträge |
| 2026-10-22 | 1 | Download im ITERATION-Modus | Mehr als 15.000 Treffer |
| 2026-10-22 | 1 | Rohantworten byteweise unverändert in `data/raw/`, `data/` nicht in Git | CLAUDE.md-Regel; 77 MB, jederzeit reproduzierbar |
| 2026-10-22 | 1 | Auswertung auf Notice-Ebene (befüllt = mindestens ein Los) | Einfach zuerst; Los-Ebene als offene Frage |
| 2026-10-22 | 1 | `-1` gilt als nicht befüllt; zusätzlich Kennzahl „plausibler Wert > 1 €“ | Platzhalter verfälschen sonst die Quote |
| 2026-10-22 | 1 | CPV-Bezeichnungen aus der offiziellen Liste im eForms SDK | Offizielle Quelle mit deutschen Labels |
| 2026-10-22 | 1 | „Laufzeitende bestimmbar“ = Enddatum, oder Beginn + Dauer; „Ende oder Dauer“ wird nur ergänzend ausgewiesen | Eine Dauer ohne Beginn ergibt kein Enddatum |
| 2026-10-22 | 1 | Laufzeit zusätzlich aus Beginn/Ende berechnen; Werte ≤ 0 oder > 240 Monate verwerfen | BT-36 nur bei 21 % befüllt, Median dadurch verzerrt |
| 2026-10-22 | 1 | `total-value` als „von TED berechnet“ kennzeichnen, nicht als BT-161 | Parsing-Stichprobe 573266-2026 |
| 2026-10-22 | 1 | Iteration 2 beginnt in Phase 2 mit competition-Daten, Rückreichweite und erster Zuordnung (CPV 909), erst danach Phase 3 | Evaluation: Zielereignis und Backtest-Machbarkeit sind ungeprüft |
| 2026-10-23 | 2 | Vorgänger-Pool vor eForms über `classification-cpv=909*` (Haupt- oder Zusatz-CPV) | API liefert vor eForms keine Haupt-CPV |
| 2026-10-23 | 2 | Ausschreibungen werden als Verfahren gezählt (ohne Änderungsbekanntmachungen) | 22,4 % der competition-Notices sind Änderungen |
| 2026-10-23 | 2 | Laufzeiten vor eForms werden über `REF_NOTICE` aus der XML der alten Ausschreibung gelesen | Zuschläge F03 enthalten keine Laufzeit |
| 2026-10-23 | 2 | **Idee anpassen:** Zuordnung über den Auftraggeber wird verworfen; Iteration 3 bleibt in Phase 2 und misst Sichtbarkeit der Vorgänger und Zuordnung über das Objekt getrennt, mit vorab festgelegter Abbruchregel. Abweichung von der vorab genannten Optionsliste. | K2 = 16,7 % (Schwelle 80 %), Regel „K2 < 50 % → Idee anpassen“ ausgelöst; Sichtbarkeit nicht gemessen; A30 zeigt Methodenversagen trotz vorhandener Daten [E2]. Entscheidung des Nutzers. |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

### Iteration 1 – 2026-10-22

- **Was gemacht:** TED Search API v3 recherchiert (Doku, OpenAPI-Spezifikation, Probeabfragen). Alle deutschen
  Zuschlagsbekanntmachungen vom 22.07. bis 21.10.2026 geladen (`src/ted_download.py`). Vollständigkeitsanalyse mit Report
  erstellt (`src/analyze_completeness.py`). Eine Notice manuell mit der TED-Website verglichen.
- **Erkenntnisse – Fakten:** 15.706 Notices. Laufzeit (Ende oder Dauer) 82,0 %, in den Dienstleistungsnischen 90–93 %.
  BT-58 > 0 nur 14,7 %. Plausibler Wert nur 58,8 %. Etwa 21 % der Gesamtwerte ≤ 1 €. In 505084-2026 steht die
  Verlängerung nur im Freitext.
- **Erkenntnisse – Interpretation:** Die Laufzeit trägt eine Baseline. Verlängerungen brauchen Textextraktion. Der Wert
  ist nur eingeschränkt nutzbar.
- **Übergabe an die nächste Phase:** An Phase 3 gehen die Feldliste und Fallstricke (`-1`, Platzhalterwerte, Listen je Los,
  mehrsprachige Namen, Verlängerung im Freitext). An Phase 1 geht die Häufigkeit und Befüllung je Nische als Grundlage
  für die Nischenwahl. Vor Phase 3 noch offen: Rückreichweite der Daten.

### Iteration 1 (Abschluss) – 2026-10-22

- **Was gemacht:**
  - Parsing-Stichprobe mit 15 Notices gegen die Original-XML ([S], `src/stichprobe_parsing.py`)
  - Laufzeit aus Beginn/Ende nachberechnet und Kennzahl „Laufzeitende bestimmbar“ eingeführt ([R §5])
  - Kritische Prüfung durch den Evaluator ([E])
- **Erkenntnisse – Fakten:**
  - Kein Parsing-Fehler in 15 von 15 Fällen. `total-value` ist nicht BT-161.
  - Gebäudereinigung: Ende bestimmbar 80,9 % (KI 77,0–84,3 %), Median-Laufzeit 36 Monate aus Beginn/Ende (BT-36: 24, n = 45).
  - Winterdienst 84,5 %, Sicherheit 83,9 %, IT-Dienste 33,7 %.
- **Erkenntnisse – Interpretation:**
  - Die Datenbasis trägt eine vorläufige Arbeitsnische.
  - Ob ein Backtest nur mit eForms-Daten gelingt und ob Neuausschreibungen sich zuordnen lassen, ist offen und eher kritisch.
- **Übergabe an die nächste Phase:** Iteration 2 bleibt zunächst in Phase 2:
  - Auftragsbekanntmachungen (competition) für CPV 909 laden
  - Rückreichweite klären
  - erste Zuordnung von Zuschlag und Neuausschreibung versuchen

  Danach geht an Phase 3:
  - Laufzeit aus Beginn/Ende nutzen
  - Verlängerungen aus BT-54/BT-57 extrahieren
  - Zuordnung alter und neuer Ausschreibungen aufbauen

### Iteration 2 – 2026-10-23

- **Was gemacht:**
  - TED-API geprüft: Rückreichweite, Felder vor eForms, Definitionen BT-36/537 ([PR], [SDK])
  - Quartalszählungen seit 2016 (`src/ted_counts.py`, [RR])
  - Ausschreibungen Q2 2026 und Zuschläge seit 2016 geladen (`src/ted_download.py` erweitert)
  - K4/K5 berechnet (`src/kennzahlen_iteration2.py`, [K])
  - Zuordnungs-Prototyp gebaut (`src/zuordnung_prototyp.py`, [Z])
  - 30 Paare und 15 Fälle ohne Treffer anhand der Original-XML geprüft (`src/k2_xml_auszug.py`, [P], [X])
  - Evaluator ([E2])
- **Erkenntnisse – Fakten:**
  - API ab Okt. 2016; vor eForms ohne Laufzeit, Haupt-CPV und Kennung.
  - K1 83,7 %, K2 16,7 % (5/30), K4 82,1 % (2024 nur 70,1 %), K5 629 (Median 12 Monate).
  - Laufzeit vor eForms über REF_NOTICE in 10 von 10 Fällen (nicht zufällig).
  - 3 von 6 objektgleichen Paaren sind vorzeitige Neuvergaben.
- **Erkenntnisse – Interpretation:**
  - Die Zuordnung über den Auftraggeber taugt nicht.
  - Ob die Vorgänger auf TED sichtbar sind, ist offen.
  - Ein Backtest nur mit eForms-Daten wäre stark verzerrt.
- **Übergabe an die nächste Phase:** Keine Übergabe an Phase 3. Iteration 3 bleibt in Phase 2:
  - Sichtbarkeit der Vorgänger von Hand messen (Zuschläge und frühere Ausschreibungen)
  - Zuordnung über das Objekt (Adresse, Liegenschaft, Titel) auf getrennten Entwicklungs- und Testdaten aufbauen und messen
  - Nische enger abgrenzen
  - A11 an einer Zufallsstichprobe prüfen
  - vorab festgelegte Abbruchregel: bei zu geringer Sichtbarkeit nationale Quellen oder Auftraggeber-Zyklen
