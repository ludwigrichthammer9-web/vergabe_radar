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

_Stand: Iteration 3 (Abschluss), 2026-10-25. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Quellen: **[R]** `reports/datenqualitaet_DEU_20260722_20261021.md` · **[S]** `reports/stichprobe_iteration1.md` ·
**[E1]** `reports/evaluation_iteration1.md` · **[RR]** [rueckreichweite_909.md](../../reports/rueckreichweite_909.md) ·
**[K]** [kennzahlen_iteration2.md](../../reports/kennzahlen_iteration2.md) · **[Z]** [zuordnung_iteration2.md](../../reports/zuordnung_iteration2.md) ·
**[P]** [k2_pruefliste.md](../../reports/k2_pruefliste.md) · **[X]** [k2_auszuege.md](../../reports/k2_auszuege.md) ·
**[E2]** [evaluation_iteration2.md](../../reports/evaluation_iteration2.md) · **[Erg]** [ergebnis_iteration2.md](../../reports/ergebnis_iteration2.md) ·
**[PR]** Probeabfragen vom 23.10.2026 in `data/raw/ted_probes/20261023/` · **[Sp]** OpenAPI https://ted.europa.eu/docs/v3 ·
**[F]** Feldliste https://docs.ted.europa.eu/ODS/latest/reuse/field-list.html · **[SDK]** eForms SDK `translations/business-term_en.xml`.
Iteration 3: **[T3]** [testfaelle_iteration3.md](../../reports/testfaelle_iteration3.md) · **[RE]** [regel_entwicklung_iteration3.md](../../reports/regel_entwicklung_iteration3.md) ·
**[GT]** [sichtbarkeit_iteration3_gt.csv](../../reports/sichtbarkeit_iteration3_gt.csv) und `sichtbarkeit_iteration3_teil1–4.md` ·
**[Z3]** [zuordnung_iteration3.md](../../reports/zuordnung_iteration3.md) · **[A11]** [a11_stichprobe.md](../../reports/a11_stichprobe.md) ·
**[BN]** [blindpruefung_iteration3_nutzer.md](../../reports/blindpruefung_iteration3_nutzer.md) · **[E3]** [evaluation_iteration3.md](../../reports/evaluation_iteration3.md).

### Fakten (aus den Daten)

**Datenquelle**
- TED Search API v3 (`POST https://api.ted.europa.eu/v3/notices/search`, ohne API-Key). Pro Seite höchstens 250 Notices,
  ITERATION-Modus unbegrenzt. [Sp]
- **Rückreichweite:** ab Ende Oktober 2016 (erste Notices 21.–28.10.2016), davor 0 Treffer. [PR q04–q09, q17]
- **Formatwechsel:** Haupt-CPV (`main-classification-proc`) ist ab Ende Oktober 2023 befüllt, davor nie. [PR q16], [RR]
- **Notices vor eForms:** Die API liefert nur Nummer, Datum, Formular- und Bekanntmachungstyp, CPV-Liste, Auftraggebername und Ort.
  Laufzeit, Haupt-CPV, Kennung und Titel fehlen. [PR q11, q15] Objektangaben (Titel, Ort, Beschreibung) stehen nur in der XML bzw.
  sind über die Volltextsuche erreichbar. [GT], [E3]
- **Laufzeit vor eForms (A11):** Alte Zuschläge (F03/F06) enthalten keine Laufzeit (0 von 30). In einer Zufallsstichprobe von 30
  Zuschlägen (CPV 909, DEU, 2018 bis Okt. 2023) ist das Laufzeitende über `REF_NOTICE` in der alten Ausschreibung bei **25/30 = 83,3 %**
  (Wilson 66,4–92,7) bestimmbar; 2 ohne Verweis, 3 nur Dauer. Gemeint ist das geplante Ende der Grundlaufzeit. [A11]
- **Definitionen:** BT-36 schließt laut eForms Optionen und Verlängerungen ein, BT-537 ist offen formuliert. [SDK]

**Geladene Datensätze** (Rohdaten unverändert in `data/raw/`)
- Iteration 1: alle deutschen Zuschläge 22.07.–21.10.2026 (15.706). [R]
- Iteration 2: Gebäudereinigungs-Ausschreibungen Q2 2026 (710 Notices, 551 Verfahren) und alle Zuschläge mit CPV 909 in der CPV-Liste
  seit Okt. 2016 (15.361). [RR], [Z]
- Iteration 3: Gebäudereinigungs-Ausschreibungen Q3 2026 (678 Notices; Population 492 Verfahren nach Haupt-CPV 90910/90911/90919,
  ohne Änderungen und Ausschlussbegriffe im Titel) [T3]; XML der Kandidaten und der A11-Stichprobe in `data/raw/ted_xml/`.

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
| vor eForms 2018–2023, über `REF_NOTICE` (V6, Schwelle vorab) | 83,3 % | 66,4–92,7 % | 30 | [A11] |

- Median-Laufzeit Gebäudereinigung aus Beginn/Ende 36 Monate (Q3 2026). [R]

**Sichtbarkeit der Vorgänger (Iteration 3, V1)** — 60 Zufallsfälle aus Q3 2026, höchstens 2 je Auftraggeber, Handsuche durch den
Subagenten `rechercheur` mit Protokoll, vor dem Regel-Lauf committet [T3], [GT]
- 29 objektgleich, 9 Teilmenge, 14 kein Vorgänger, 8 unklar. Mit Teilmengen **38/60 = 63,3 %** (Wilson 50,7–74,4), nur objektgleich
  29/60 = 48,3 % (Wilson 36,2–60,7). [Z3], [E3]
- Bei mindestens 10 der 38 Paare fehlt das Glied direkt vor dem Testfall auf TED (Lücke zwischen Vorgänger-Ende und Testfall). [E3]
- Nur etwa 5 der 38 Vorgänger sind eForms-Verträge, die übrigen Bekanntmachungen vor eForms. [E3]
- 1 von 60 Testfällen ist sachfremd (T16, Bauendreinigung), weil die Ausschlussliste nur den Titel prüft. [E3]

**Zuordnung über das Objekt (Iteration 3, V2/V3/V5)** — Regel `src/zuordnung_objekt.py`, auf Q2 2026 gebaut und vor den Testdaten
eingefroren (Commit 4497743) [RE]
- **V2 Präzision 11/24 = 45,8 %** (Wilson 27,9–64,9), **V3 Trefferquote 11/38 = 28,9 %** (Wilson 17,0–44,8). [Z3]
- 9 von 11 falschen Vorschlägen sind Geschwisterverfahren desselben Auftraggebers, 2 dasselbe Objekt mit anderer Leistungsart (T31,
  T54); alle 11 sind Notices aus 2025/2026. Bei 19 von 38 gefundenen Fällen kein Vorschlag. [E3]
- Auf den Entwicklungsdaten hielt Claude etwa 10–11 von 12 Vorschlägen für plausibel (ohne Handsuche). [RE]
- V5: 10/60 korrekt zugeordnet mit bestimmbarem Vorgänger-Ende, hochgerechnet 328 pro Jahr [Z3]. Enddaten bei T26 (Ende eines
  aufgehobenen Verfahrens), T56 (jährliche Verlängerung, Ende unbekannt) und T18 (nur Lose 8/9) fragwürdig; robust etwa 230,
  nur eForms-Vorgänger etwa 98–131 pro Jahr. [E3]
- Vorzeitige Neuvergaben (Beginn ≥ 3 Monate vor Ende der Grundlaufzeit): 2/36 = 5,6 % (T18, T32). Neuvergabe nach der Grundlaufzeit,
  aber vor dem Höchstende bei mindestens 6 Paaren. [E3]

**Zweitprüfung (V4)** — Urteile des Nutzers nach Urteilsregeln Version 1.1 über P9–P28: 17/20 = 85 % (Wilson 64,0–94,8; κ ≈ 0,70);
regelbasierter Subagent ebenfalls 17/20. Die Regeln entstanden nach dem ersten Ansehen der Paare; P1–P8 wurden Kalibrierung. [BN], [E3]

**Aus Iteration 2 (Zuordnung über den Auftraggeber)** [Z], [P], [E2]
- K1: 461 von 551 (83,7 %) haben einen früheren Zuschlag desselben Auftraggebers; K2: nur 5 von 30 objektgleich (16,7 %).
- Haupt-CPV 909 enthält auch Schädlingsbekämpfung, Fahrzeug- und Industriereinigung sowie Bau- und Sonderreinigung. [X], [E2]
- Backtest-Basis K5: 629 eForms-Zuschläge mit Laufzeitende bis 23.10.2026, Median-Laufzeit 12 Monate. [K]

### Interpretation

- **Objektgleiche Vorgänger sind auf TED oft sichtbar**, aber knapp und nur, wenn Teilmengen mitzählen. Die Abbruchregel „V1 < 30 %
  → nationale Quellen“ ist klar nicht ausgelöst, die Sichtbarkeit unter strenger Definition liegt aber um 50 %.
- **Die einfache Objekt-Regel taugt nicht.** Sie verwechselt Geschwisterverfahren großer Auftraggeber und findet vor eForms kaum
  etwas, weil die Objektmerkmale in den API-Daten fehlen. Das zweite ist eher ein Problem des Datenzugangs als der Vergleichslogik.
- **Ein Zeitfenster ist keine Lösung**: Es würde vorzeitige Neuvergaben ausschließen und den Backtest zirkulär machen.
- **Für den Backtest sind Daten vor eForms praktisch nötig** (nur etwa 5 von 38 Vorgängern sind eForms-Verträge). A11 ist dafür
  vorläufig gestützt.
- **Die Kategorien „objektgleich“ und „Teilmenge“ sind unscharf.** Die Definition hat sich während der Handsuche verschoben, und V4
  belegt keine eindeutige Definition. Für Iteration 4 gelten die Urteilsregeln 1.1 vorab.
- **Die Nische muss auf Los-Ebene über die Leistungsart abgegrenzt werden**, nicht nur über Haupt-CPV und Titel.
- **Die 80-%-Quote für ein bestimmbares Laufzeitende gilt ab 2025** und, über `REF_NOTICE`, vorläufig auch für 2018–2023, nicht für
  2023/2024 in eForms.

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
- [ ] _(neu, Iteration 2)_ Lässt sich der Vorgänger automatisch über Adresse, Liegenschaftsname und Titel zuordnen, auch bei großen
  Auftraggebern (A9b)?
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
- [ ] _(neu, Iteration 3)_ Ist Q3 ein saisonales Hoch der Ausschreibungen (Hochrechnung „× 4“ in V5)? Populationsgrößen anderer
  Quartale vergleichen.
- [ ] _(neu, Iteration 2)_ Warum gibt es seit eForms etwa 1,6 Ausschreibungs-Notices pro Zuschlag (vorher 1,1), auch nach Abzug der
  Änderungen etwa 1,2?
- [ ] _(neu, Iteration 2)_ Warum ist das Laufzeitende 2023/2024 nur bei etwa 70 % bestimmbar, ab 2025 bei etwa 80 %?
- [ ] Meinen BT-36/BT-536/BT-537 die Laufzeit mit oder ohne Verlängerungen? (eForms-Dokumentation prüfen)
  _Teilantwort 2026-10-23:_ BT-36 laut Definition **mit** Optionen und Verlängerungen; BT-537 ohne Aussage [SDK]. Praxis ungeprüft.
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
