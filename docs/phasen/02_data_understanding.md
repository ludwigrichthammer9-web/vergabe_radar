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

_Stand: Iteration 5 (Abschluss), 2026-11-04. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Quellen: **[BT5]** [backtest_iteration5.md](../../reports/backtest_iteration5.md) · **[E5]** [evaluation_iteration5.md](../../reports/evaluation_iteration5.md) · **[ZP]** [gt_pruefung_iteration5_auswertung.md](../../reports/gt_pruefung_iteration5_auswertung.md) · **[AN]** [backtest_analysen_iteration5.md](../../reports/backtest_analysen_iteration5.md) · **[VL]** [vertragsliste_iteration5.md](../../reports/vertragsliste_iteration5.md) · **[VP]** [verlaengerung_praxis_iteration5.md](../../reports/verlaengerung_praxis_iteration5.md) · **[HP]** [hoechstende_pruefung_iteration5_test.md](../../reports/hoechstende_pruefung_iteration5_test.md).

### Fakten (aus den Daten)

**Datenquelle und Datensätze**
- TED Search API v3 ab Ende Oktober 2016; vor eForms liefert die API keine Titel, Orte und Laufzeiten, die Original-XML schon. Volltextsuche `FT` findet auch Bekanntmachungen vor eForms.
- Population Gebäudereinigung (Haupt-CPV 90910/90911/90919, Originale): 1.893 Verfahren pro Jahr (Q4 2025 bis Q3 2026).

**Laufzeit und Verlängerungen (Iteration 5)** [VP]
- BT-537 und `DATE_END` bezeichnen in der Praxis das **Ende der Grundlaufzeit** (Spanne Beginn–Enddatum in 274 von 289 Fällen kürzer als die im Text genannte Höchstlaufzeit).
  BT-36 ist uneinheitlich (27 von 37 gleich der Datumsspanne). BT-58 nennt nur die Zahl der Verlängerungen; die Länge steht im Freitext (BT-57, BT-54; vor eForms `RENEWAL_DESCR`).
- eForms-Zuschläge (n = 4.307): Enddatum 75,1 %, nur Beginn + Dauer 1,0 %, keine verwertbare Laufzeit 22,4 %. 32,0 % mit BT-58 > 0.

**Vorgänger-Paare (Backtest-Basis)** [BT5], [AN]
- 68 Paare aus der Handsuche (Iteration 3 und 4), 61 mit bestimmbarem Ende der Grundlaufzeit; 52 von Rechercheur und Prüfer bestätigt. 41 der 52 Vorgänger stammen aus der Zeit vor eForms.
- Bei 12 der 52 Paare erscheint die Neuausschreibung mehr als 24 Monate nach der Prognose (Spannen bis 95 Monate), bei 4 mehr als 24 Monate davor. Bei 10 der 12 hat derselbe
  Auftraggeber dazwischen weitere 909-Bekanntmachungen veröffentlicht (kein Beleg für einen Zwischenvertrag am selben Objekt).
- 40 Auftraggeber für 52 Paare; Bayern 0/5 Treffer, Bundesanstalt für Immobilienaufgaben 3/4 (kleine Zahlen).

### Interpretation

- Das Höchstende ist nur aus dem Freitext lesbar; die Grundlaufzeit steht strukturiert. Ob Optionen gezogen werden, steht nicht im Vorgänger-Zuschlag.
- Lange Lücken deuten auf nicht-direkte Vorgänger (Zwischenverträge außerhalb TED), das Glied direkt davor fehlt auf TED oft (Iteration 3: mindestens 10 von 38).
- Ob die Ground Truth der Handsuche stimmt, ist weiter nicht unabhängig geprüft (A18).

## Offene Fragen

- [x] Wie weit zurück sind die Daten brauchbar? Zahl der 909-Zuschläge seit Ende Oktober 2023 und Verteilung ihrer Enddaten. Enthalten die Formate vor eForms Laufzeiten (A10, A11)?
  _Teilantwort 2026-10-23:_ Such-API ab Ende Oktober 2016; vor eForms keine Laufzeit über die API, wohl aber in der XML alter Ausschreibungen (1 Fall) [P], [X].
  _Antwort Iteration 2 (Abschluss):_ API ab Okt. 2016. 4.905 eForms-Zuschläge, davon 629 abgelaufen (Median 12 Monate) [K]. Vor eForms
  Laufzeit über REF_NOTICE in der alten Ausschreibung, 10 von 10 in nicht zufälliger Stichprobe [X]. Repräsentative Prüfung offen.
- [x] Erscheinen Neuausschreibungen für CPV 909 als Auftragsbekanntmachungen (competition) auf TED, und wie viele pro Jahr? Gibt es Vorinformationen (PIN) als Frühsignal?
  _Antwort Iteration 2:_ ja, grob 1.990–2.160 Verfahren pro Jahr (2024/2025, hochgerechnet); PIN rund 30 pro Jahr, als Frühsignal bedeutungslos [RR].
- [x] Lassen sich Zuschlag und Neuausschreibung zuordnen, z. B. über Auftraggeber und CPV (A9)?
  _Antwort Iteration 2:_ über Auftraggeber + CPV **nein** (K2 = 16,7 %) [P], [E2]. Zuordnung über das Objekt: siehe neue Frage unten.
- [x] _(neu, Iteration 2)_ Wie oft gibt es zu einer Ausschreibung überhaupt einen objektgleichen Vorgänger auf TED (Sichtbarkeit),
  gesucht unter Zuschlägen **und** früheren Ausschreibungen? (A3, A9b)
  _Antwort Iteration 3:_ 38/60 = 63,3 % mit Teilmengen, 29/60 = 48,3 % nur objektgleich (Q3 2026, Definition des Rechercheurs)
  [Z3], [E3]. Unter Urteilsregeln 1.1 nicht erneut gemessen.
- [x] _(neu, Iteration 2)_ Lässt sich der Vorgänger automatisch über Adresse, Liegenschaftsname und Titel zuordnen, auch bei großen
  Auftraggebern (A9b)?
  _Antwort Iteration 4:_ nicht zuverlässig genug (Präzision 89,5 % bei 19 Vorschlägen, Trefferquote 56,7 %, Zweitprüfung 65 %); nicht weiter verfolgt [Z4], [E4].
  _Stand Iteration 3:_ mit der eingefrorenen Regel **nein** (V2 45,8 %, V3 28,9 %) [Z3]. Letzter Versuch mit Merkmalen auf Los-Ebene
  in Iteration 4 (A9c).
- [ ] _(neu, Iteration 2)_ Wie häufig sind vorzeitige Neuvergaben (A16)?
  _Teilantwort Iteration 3:_ 2/36 = 5,6 % gegen die Grundlaufzeit; gegen das Höchstende häufiger (mindestens 6 Paare) [E3].
  Tatsächliche Vertragsenden und Vorlaufzeit offen.
- [ ] _(neu, Iteration 2)_ Wie grenzt man „wiederkehrende Gebäudereinigung“ ab (Ausschluss von Schädlingsbekämpfung, Bau- und
  Sonderreinigung, Fahrzeug- und Industriereinigung) (A12)?
  _Stand Iteration 3:_ Haupt-CPV 90910/90911/90919 plus Stichwortliste im Titel lässt 1 von 60 sachfremd durch (T16); die Leistungsart
  muss auf Los-Ebene geprüft werden [E3].
- [ ] _(neu, Iteration 3)_ Lassen sich Objekt- und Leistungsart-Merkmale vor eForms automatisch aus der XML oder über die
  Volltextsuche (`FT`) gewinnen, in welcher Qualität und mit welchem Abrufaufwand? (A9c)
- [ ] _(neu, Iteration 3)_ Wie trennt man Geschwisterverfahren desselben Auftraggebers (Objektlisten, Flächen, Losnummern), ohne
  Zeitfenster? (A9c)
- [ ] _(neu, Iteration 3)_ Wie oft fehlt das Glied direkt vor einer Ausschreibung auf TED (Lücke bei mindestens 10 von 38), und
  was bedeutet das für die Prognose der Kette? (A3, A8)
- [x] _(neu, Iteration 3)_ Ist Q3 ein saisonales Hoch der Ausschreibungen (Hochrechnung „× 4“ in V5)? Populationsgrößen anderer
  Quartale vergleichen.
  _Antwort Iteration 4:_ Q4 2025 381, Q1 2026 538, Q2 488, Q3 486; Q4 ist das schwache Quartal, Q1 das stärkste [Z4].
- [ ] _(neu, Iteration 4)_ Wie gut ist die Ground Truth der Handsuche, unabhängig geprüft (A18)?
- [ ] _(neu, Iteration 2)_ Warum gibt es seit eForms etwa 1,6 Ausschreibungs-Notices pro Zuschlag (vorher 1,1), auch nach Abzug der
  Änderungen etwa 1,2?
- [ ] _(neu, Iteration 2)_ Warum ist das Laufzeitende 2023/2024 nur bei etwa 70 % bestimmbar, ab 2025 bei etwa 80 %?
- [ ] Meinen BT-36/BT-536/BT-537 die Laufzeit mit oder ohne Verlängerungen? (eForms-Dokumentation prüfen)
  _Teilantwort 2026-10-23:_ BT-36 laut Definition **mit** Optionen und Verlängerungen; BT-537 ohne Aussage [SDK]. Praxis ungeprüft.
  _Antwort Iteration 5 (2026-10-30):_ In der Praxis ist BT-537 das Ende der Grundlaufzeit (94,8 % kürzer als die genannte
  Höchstlaufzeit, n = 289); BT-36 meist ebenfalls (27 von 37 gleich der Datumsspanne), teils mit Verlängerungen [VP].
- [ ] _(neu, 2026-10-23)_ Enthalten alte Zuschläge (F03) generell keine Laufzeit, und lässt sie sich zuverlässig über `REF_NOTICE`
  aus der alten Ausschreibung (F02) holen? Bisher 1 Fall [X].
  _Stand Abschluss Iteration 2:_ 10 von 10 in nicht zufälliger Stichprobe; Zufallsstichprobe (z. B. 30 aus 2018–2023) offen [E2].
  _Stand Iteration 3:_ F03/F06 enthalten selbst keine Laufzeit (0 von 30); über `REF_NOTICE` bestimmbar bei 25/30 = 83,3 % (Wilson
  66,4–92,7) [A11]. Offen: 2016–2017 und Zuschläge ohne Verweis.
- [ ] Warum ist bei 84 von 440 Gebäudereinigungs-Notices kein Laufzeitende bestimmbar? Stichprobe von etwa 20 Fällen.
- [x] Hält die Quote in einem unabhängigen Zeitfenster (z. B. ein Frühjahrsquartal 2025), mit vorab festgelegter Schwelle (A13)?
  _Antwort Iteration 2:_ ja für Q2 2025 (82,1 %, KI 77,9–85,5 %), nicht für 2023/2024 (rund 70 %) [K].
- [ ] Wie sieht die Befüllung auf Los-Ebene aus statt auf Notice-Ebene?
- [x] Bedeutet `-1` „nicht veröffentlicht“? Teilweise belegt durch 2 Fälle mit FieldsPrivacy [S] (A7).
- [ ] Wie oft stehen Verlängerungen nur im Freitext (quantifizieren statt aus einem Einzelfall verallgemeinern)?
  _Teilantwort Iteration 5:_ Die **Länge** steht immer nur im Freitext (BT-58 ist eine Anzahl). Bei fehlendem BT-58 oder BT-58 = 0
  erwähnen bis zu 42,4 % den Begriff „verläng…“ im Text (Obergrenze) [VP].
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
| 2026-10-23 | 3 | Population: Ausschreibungen DEU, Haupt-CPV 90910/90911/90919, nur Originale, Ausschlussliste im Titel; Entwicklungsdaten Q2 2026, Testdaten Q3 2026 (60 Fälle, Seed 20261024, höchstens 2 je Auftraggeber) | Vorab festgelegt und committet vor den Testdaten (af36eab, 0370c7f) |
| 2026-10-23 | 3 | Handsuche (Ground Truth) durch den Subagenten `rechercheur`, ohne Kenntnis der Regel | Trennung von Regelbau und Ground Truth; Entscheidung des Nutzers |
| 2026-10-24 | 3 | V4 über P9–P28 nach Urteilsregeln Version 1.1; P1–P8 sind Kalibrierung | Regeln des Nutzers nach erstem Ansehen der Paare; als Abweichung in iterationen.md dokumentiert |
| 2026-10-25 | 3 | **In Phase 2/3 bleiben:** ein letzter Verbesserungsversuch der Zuordnung (Iteration 4) mit Merkmalen auf Los-Ebene (auch vor eForms), harter Prüfung der Leistungsart und Trennung von Geschwisterverfahren ohne Zeitfenster; Q3 2026 wird Entwicklungsdaten, neue Testdaten aus Q1 2026, Handsuche und V4 nach Urteilsregeln 1.1 vorab | Vorab festgelegte Folge „V1 ≥ 50 %, V2/V3 verfehlt“ (V1 63,3 %, V2 45,8 %, V3 28,9 %); V1 und V4 nur knapp und definitionsabhängig erfüllt [E3]. Entscheidung des Nutzers. |
| 2026-10-30 | 4 | **Idee anpassen:** Die Zuordnung über das Objekt wird nicht weiter verbessert (A9c für `zuordnung_los.py` widerlegt); Iteration 5 nutzt Zuschläge mit Laufzeitende als Kern und die Zuordnung nur für einen Backtest auf handgeprüften Paaren | W4 65 % < 85 %, W3 56,7 %, W2 bei 19 statt 25 Vorschlägen (reports/evaluation_iteration4.md). Entscheidung des Nutzers. |
| 2026-11-04 | 5 | Das Ende der Grundlaufzeit wird aus BT-537 bzw. `DATE_END` gelesen (nicht aus BT-36); das Höchstende aus Freitext und BT-58 mit Lese-Regeln (Kopf von `src/prepare/vertragsliste.py`); Vorgänger-Ende nur aus den Bekanntmachungen des Vorgängers (keine Leckage) | Praxis der Felder (reports/verlaengerung_praxis_iteration5.md), Stichproben der Lese-Regeln (reports/hoechstende_pruefung_iteration5_*.md) |

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

### Iteration 3 – 2026-10-25

- **Was gemacht:**
  - Population Q3 2026 festgelegt, Ausschreibungen geladen, Testprobe mit 60 Fällen gezogen ([T3], `src/population_iteration3.py`,
    `src/testprobe_iteration3.py`)
  - Objektmerkmale extrahiert und Zuordnungsregel auf Q2 2026 gebaut, vor den Testdaten eingefroren ([RE], `src/objekt_merkmale.py`,
    `src/zuordnung_objekt.py`, Commit 4497743)
  - Handsuche durch den Subagenten `rechercheur` in 4 Teilen, vor dem Regel-Lauf committet ([GT])
  - Regel auf Testdaten angewendet, 14 Vorschläge außerhalb der Handsuche von Claude beurteilt ([Z3], `src/auswertung_iteration3.py`)
  - Blindprüfung V4: Urteilsregeln des Nutzers (Version 1.1), 8 Ersatzpaare, Urteile des Nutzers und eines regelbasierten
    Subagenten ([BN], `src/blindpruefung_iteration3.py`)
  - A11-Zufallsstichprobe mit 30 Zuschlägen vor eForms ([A11], `src/a11_stichprobe.py`)
  - Evaluator ([E3])
- **Erkenntnisse – Fakten:**
  - V1 38/60 = 63,3 % (davon 9 Teilmengen; nur objektgleich 48,3 %).
  - V2 11/24 = 45,8 %, V3 11/38 = 28,9 %; 9 von 11 Fehlern sind Geschwisterverfahren.
  - V4 17/20 = 85 %, V5 328 pro Jahr (robust etwa 230), V6 25/30 = 83,3 %.
  - Vorzeitige Neuvergaben 2/36. Nur etwa 5 von 38 Vorgängern sind eForms-Verträge.
- **Erkenntnisse – Interpretation:**
  - Vorgänger sind auf TED oft sichtbar, die einfache Objekt-Regel findet sie aber nicht zuverlässig.
  - Engpass sind die Objektmerkmale vor eForms und die Geschwisterverfahren großer Auftraggeber.
  - Die Definition „objektgleich/Teilmenge“ war unscharf; V4 belegt keine eindeutige Definition.
- **Übergabe an die nächste Phase:** Keine Übergabe an Phase 3 als fertige Zuordnung. Iteration 4 (Phase 2/3) unternimmt den letzten
  Verbesserungsversuch:
  - Merkmale auf Los-Ebene, auch vor eForms (XML, Volltextsuche)
  - Leistungsart hart prüfen, Geschwisterverfahren über Objektlisten und Flächen trennen, kein Zeitfenster
  - neue Testdaten aus Q1 2026, Handsuche und Zweitprüfung nach Urteilsregeln 1.1 vorab, Abbruchkriterium vorab
  - korrigierte Vorgänger-Enddaten (T26, T56, T18), Belegstärke T18–T30 in `gt.csv` nachtragen

### Iteration 4 – 2026-10-30

- **Was gemacht:**
  - Population mit erweitertem Ausschluss (Lostitel, Bauprojekte), Liste bekannter Notices, Testprobe 70 Fälle Q1 2026
    (`src/population_iteration4.py`, `src/testprobe_iteration4.py`)
  - Downloads mit Beschreibungen je Los, Merkmale je Los (`src/ted_download.py --los-texte`, `src/los_merkmale.py`)
  - Regel auf Q2/Q3 entwickelt und eingefroren (`src/zuordnung_los.py`, [RE4])
  - Handsuche durch den Rechercheur nach Urteilsregeln 1.1 in 5 Teilen, Ground Truth vor dem Regel-Lauf ([GT4])
  - Regel-Lauf, Paarbeurteilung, Blindprüfung, Auswertung mit Korrektur ([Z4], [BP4]); Evaluator ([E4])
- **Erkenntnisse – Fakten:**
  - W1 42,9 %, W2 17/19 (Mindestzahl 25 verfehlt), W3 56,7 %, W4 65 %, W5 297/Jahr (korrigiert), W6 73,3 %.
  - Prüfzeit Median 2 Minuten; vorzeitig 3/30; Vorlaufzeit −32 bis +26 Monate.
  - Population 1.893 Verfahren pro Jahr, Q4 deutlich kleiner als Q1.
- **Erkenntnisse – Interpretation:**
  - Die automatische Zuordnung über das Objekt erreicht die vorab festgelegten Schwellen nicht; sie wird nicht weiter verbessert.
  - Die Ground Truth ist nicht unabhängig bestätigt; das betrifft auch die Backtest-Basis.
- **Übergabe an die nächste Phase:** An Phase 1: Prognoseziel festlegen. An Phase 3: Tabelle der Zuschläge mit Laufzeitende je Los,
  Herkunft des Endes (Grundlaufzeit, Höchstende, rollierend), auch vor eForms über `REF_NOTICE`. An Phase 5: Backtest nur auf Paaren mit
  unabhängig geprüfter Ground Truth.

### Iteration 5 – 2026-11-04

- **Was gemacht:** eForms- und TED-Dokumentation zu Laufzeit und Verlängerungen geprüft und mit den Daten verglichen (`src/verlaengerung_praxis.py`); Vorgänger-Enden der Paare aus
  den Bekanntmachungen des Vorgängers gelesen (`src/prepare/backtest_paare.py`); nachträgliche Analysen zu langen Lücken und Auftraggebern (`src/model/analyse_backtest.py`).
- **Erkenntnisse – Fakten:** BT-537/DATE_END = Ende der Grundlaufzeit; Höchstende nur im Freitext; 12 von 52 Paaren mit Lücke über 24 Monate nach der Prognose; 41 von 52 Vorgängern vor eForms (reports/verlaengerung_praxis_iteration5.md, reports/backtest_analysen_iteration5.md).
- **Erkenntnisse – Interpretation:** Viele Vorgänger sind nicht der direkte Vorgängervertrag; Daten vor eForms sind für den Backtest nötig.
- **Übergabe an die nächste Phase:** An Phase 1: Liste ohne Terminprognose als Kern. An Phase 3: Vertragsliste je Los (vorhanden). Offen: Vorlauf je Auftraggeber aus der Historie (nur wenn Iteration 6 das aufgreift).
