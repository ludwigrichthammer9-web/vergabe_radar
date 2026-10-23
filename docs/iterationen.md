# Iterationen

Jede Iteration hat vorab eine **Hypothese**, ein messbares **Erfolgskriterium** und einen **Zeitrahmen**. Am Ende
werden **Ergebnis** und **Entscheidung** eingetragen: weiter / zurück zu Phase X / Idee anpassen.
Ablauf: Mit `/iteration-start` anlegen, mit `/iteration-ende` abschließen. Der Subagent `evaluator` prüft kritisch.

Regeln:
- Hypothese und Erfolgskriterium werden **vor** der Arbeit festgelegt. Ein nachträglich formuliertes Kriterium wird ausdrücklich so gekennzeichnet.
- Abgeschlossene Iterationen werden nicht mehr verändert. Korrekturen kommen als Nachtrag mit Datum dazu.
- Das Ergebnis trennt Fakten (mit Quelle) von Interpretation.

## Übersicht

| Nr | Fokus | Phasen | Zeitraum | Status | Entscheidung |
|---|---|---|---|---|---|
| 1 | Machbarkeit der Daten | 1 → 2 | 2026-10-22 | abgeschlossen | Gebäudereinigung als vorläufige Arbeitsnische; **zurück zu Phase 2** (Zielereignis und Rückreichweite prüfen) |
| 2 | Neuausschreibungen sichtbar und zuordenbar? (Gebäudereinigung, CPV 909; Rückreichweite, Replikation A13) | 2 (Prototyp für 3) | 2026-10-23 | abgeschlossen | **Idee anpassen:** Zuordnung über Auftraggeber verworfen (K2 = 16,7 %); weiter in Phase 2 mit Zuordnung über das Objekt |
| 3 | Sichtbarkeit der Vorgänger und Zuordnung über das Objekt | 2 (→ 3) | 2026-10-24 bis 2026-11-15 | läuft | offen |
| 4 | Erste Prognose und Backtest | 3 → 4 → 5 | – | geplant | – |
| 5 | Verbesserung der Prognose | 3 → 4 → 5 | – | geplant | – |
| 6 | Erster Kundentest | 6 → 1 | – | geplant | – |
| 7+ | Ausbau oder Neuausrichtung | je nach Ergebnis | – | geplant | – |

Die geplanten Iterationen stammen aus dem Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan). Nach der Entscheidung zu Iteration 1
sind sie um eine Stelle verschoben. Konkretisiert werden sie mit `/iteration-start`.
_Nachtrag 2026-10-23:_ Die geplanten Zeilen (3 bis 6+) sind an den [Projektplan](projektplan.md) angeglichen, der jetzt eine eigene
Verbesserungs-Iteration vorsieht.
_Nachtrag 2026-10-23 (Abschluss Iteration 2):_ Nach der Entscheidung zu Iteration 2 ist eine weitere Phase-2-Iteration (3)
eingeschoben; die übrigen rücken um eine Stelle.

---

## Iteration 1: Machbarkeit der Daten

**Status:** abgeschlossen am 2026-10-22

**Hypothese** _(nachträglich formuliert am 2026-10-22, nachdem die Daten bekannt waren)_
„Für mindestens eine wiederkehrende Dienstleistungsnische lässt sich bei mindestens 80 % der Zuschläge ein Laufzeitende bestimmen.“

> Frühere Fassung (ebenfalls nachträglich, 2026-10-22): „TED-Zuschlagsbekanntmachungen im eForms-Format enthalten für mindestens eine
> Dienstleistungsnische genügend Bekanntmachungen mit verwertbarer Vertragslaufzeit, um eine Prognose der Neuausschreibung zu versuchen.“
> Ihr Erfolgskriterium mit den Teilen X % Laufzeit, N Notices pro Jahr und Rückreichweite wurde **verengt**. Die Teile N/Jahr und
> Rückreichweite sind in der geprüften Fassung nicht mehr enthalten und gehen als offene Punkte in Iteration 2 ([E], Schwäche 1).

**Erfolgskriterium** _(nachträglich)_
In mindestens einer wiederkehrenden Dienstleistungsnische ist bei ≥ 80 % der Zuschläge ein Laufzeitende bestimmbar.
„Bestimmbar“ heißt: Enddatum (BT-537) vorhanden oder Beginn (BT-536) und Dauer (BT-36) vorhanden. Gezählt wird auf Notice-Ebene
nach Haupt-CPV. Vorbedingung: kein systematischer Parsing-Fehler in einer Stichprobe von 15 Notices (STOPP-Regel).

**Zeitrahmen:** 2026-10-22, ein Arbeitstag.

**Ergebnis**

Quellen: [R] [Datenqualitätsreport](../reports/datenqualitaet_DEU_20260722_20261021.md),
[S] [Stichprobe](../reports/stichprobe_iteration1.md), [E] [Evaluation](../reports/evaluation_iteration1.md).

_Fakten:_
- 15.706 deutsche Zuschläge vom 22.07. bis 21.10.2026 geladen, vollständig laut API. Auftragsbekanntmachungen wurden nicht geladen. [R]
- Parsing: 15 von 15 Notices ohne Fehler in unserem Code. `total-value` ist ein von TED berechneter Wert, nicht BT-161. [S]
- Laufzeitende bestimmbar:

  | Nische | bestimmbar | 95-%-KI | n |
  |---|---|---|---|
  | Gebäudereinigung | 80,9 % | 77,0–84,3 % | 440 |
  | Winterdienst | 84,5 % | 77,3–89,7 % | 129 |
  | Sicherheitsdienste | 83,9 % | 76,9–89,2 % | 137 |
  | IT-Dienste | 33,7 % | – | 575 |

  Großzügig gezählt (Ende oder Dauer) erreicht Gebäudereinigung 90,0 %. [R §4, §5], [E]
- Median-Laufzeit Gebäudereinigung: 36 Monate aus Beginn/Ende (Quartile 24/48, n = 350). BT-36 allein ergibt 24 Monate, aber nur bei n = 45. [R §5]
- Evaluator-Urteil zum Kriterium: **teilweise erfüllt**. Der Punktwert liegt 0,9 Prozentpunkte über einer nachträglich gesetzten Schwelle,
  das Intervall schließt Werte unter 80 % ein. Rückreichweite und Zahl pro Jahr sind nicht prüfbar. [E]

_Interpretation:_
- Die Hypothese ist vorläufig gestützt, aber nicht belastbar bestätigt.
- Gebäudereinigung, Winterdienst und Sicherheitsdienste sind sich in der Datenqualität ähnlich.
- Der entscheidende Teil der Machbarkeit ist noch offen: ob Neuausschreibungen auf TED erscheinen und sich zuordnen lassen, und ob die
  eForms-Historie für einen Backtest reicht. Bei 36 Monaten Median ist das fraglich. [E]

**Entscheidung:** **Gebäudereinigung (Haupt-CPV 909…) wird vorläufige Arbeitsnische, zurück zu Phase 2.**
Iteration 2 beginnt in Phase 2 und geht erst danach in Phase 3.

_Begründung (korrigiert gegenüber dem ersten Entwurf):_
- Gebäudereinigung ist unter den Kandidaten die häufigste Dienstleistungsnische: 440 Zuschläge in 3 Monaten, rund 3-mal so viele wie
  Sicherheitsdienste (137) oder Winterdienst (129).
- Bei 80,9 % ist ein Laufzeitende bestimmbar (KI 77–84 %; 90,0 %, wenn eine Dauer ohne Beginn mitzählt). Das liegt im Rahmen der
  anderen Facility-Nischen.
- Strukturierte Verlängerungsangaben (BT-58 > 0) sind mit 42,0 % auf dem Niveau der besten Nische (Sicherheit 42,3 %).
- Die Median-Laufzeit liegt bei 36 Monaten. Ein Backtest allein mit eForms-Daten ist damit **nicht** gesichert. Das muss Iteration 2 klären.

> Korrigiert wurden gegenüber dem ersten Entwurf: „höchster Anteil strukturierter Verlängerungsangaben“ (stimmt nicht, 42,0 % gegenüber
> 42,3 %), „ca. 90 % Laufzeitende“ (großzügige Definition) und „Median ca. 24 Monate, daher Backtest mit eForms möglich“
> (24 beruhte auf n = 45; aus Beginn/Ende ergeben sich 36 Monate).

**Offene Punkte für Iteration 2** (Hypothese und Kriterium werden mit `/iteration-start` **vorab** festgelegt)
- Phase 2:
  - Auftragsbekanntmachungen (competition) für CPV 909 laden
  - Basisrate pro Jahr bestimmen
  - Vorinformationen (PIN) als Frühsignal prüfen
  - Rückreichweite klären: 909-Zuschläge seit Herbst 2023 und Verteilung ihrer Enddaten
  - erste Zuordnung alter und neuer Ausschreibungen versuchen (A9)
  - Stichprobe der 84 nicht bestimmbaren 909-Notices
  - Replikation der 80-%-Quote in einem unabhängigen Zeitfenster (A13)
- Phase 3:
  - Laufzeit aus Beginn/Ende nutzen
  - Verlängerungen aus Freitext (BT-54/BT-57) extrahieren
  - Zuordnung alter und neuer Ausschreibungen aufbauen
- Phase 1 (parallel): erste Gespräche mit Reinigungsfirmen (A15). Idee „Facility-Services-Radar“ ist in Phase 1 notiert.

---

## Iteration 2: Neuausschreibungen sichtbar und zuordenbar?

**Status:** abgeschlossen am 2026-10-23

**Fokus und Phasen:** Phase 2 für die Arbeitsnische Gebäudereinigung (Haupt-CPV 909…), dazu ein Zuordnungs-Prototyp als Vorarbeit
für Phase 3. Abweichung vom Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan): Die erste Prognose wird verschoben, weil das
Zielereignis (Neuausschreibung) und seine Zuordnung zu alten Zuschlägen noch ungeprüft sind (Entscheidung Iteration 1).

**Vorgehen:** Rückwärtssuche. Ausgangspunkt sind aktuelle Ausschreibungen (competition), zu denen frühere Zuschläge gesucht werden.
Eine Vorwärtssuche ist nicht möglich, weil Zuschläge aus 2026 bei 36 Monaten Median-Laufzeit erst ab etwa 2029 neu ausgeschrieben werden.

**Hypothese** _(vorab festgelegt am 2026-10-23, vor Kenntnis der Ergebnisse)_
„Für die Mehrheit der deutschen Gebäudereinigungs-Ausschreibungen (competition, Haupt-CPV 909) aus Q2 2026 gibt es auf TED einen
früheren CPV-909-Zuschlag desselben Auftraggebers.“

**Erfolgskriterium** _(vorab festgelegt am 2026-10-23)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| K1 | Anteil der competition-Notices (DEU, Haupt-CPV 909, veröffentlicht 01.04.–30.06.2026) mit automatisch gefundenem Vorgänger-Zuschlag: gleicher normalisierter Auftraggeber, Haupt-CPV 909, veröffentlicht vor der Ausschreibung | ≥ 50 % | A9 |
| K2 | Manuelle Prüfung von 30 zufälligen automatischen Treffern: Anteil, bei dem plausibel dieselbe Leistung gemeint ist (Objekt/Liegenschaft, Umfang) | ~~≥ 70 %~~ **≥ 80 %** _(angepasst 2026-10-23)_ | A9 |
| K3 | Anteil der bestätigten Vorgänger im eForms-Format (veröffentlicht ab 25.10.2023) | Messwert ohne Schwelle; entscheidet, ob A10 trägt oder A11 nötig wird | A10, A11 |
| K4 | Replikation „Laufzeitende bestimmbar“ (Definition wie Iteration 1, Haupt-CPV 909, Notice-Ebene, gleiches Skript) für Zuschläge vom 01.04.–30.06.2025 | Punktwert ≥ 80 % **und** Untergrenze 95-%-KI ≥ 75 % | A13 |
| K5 _(ergänzt 2026-10-23)_ | Backtest-Basis: Anzahl eForms-Zuschläge (DEU, Haupt-CPV 909, veröffentlicht 25.10.2023–22.10.2026) mit bestimmbarem Laufzeitende (Definition wie Iteration 1, Notice-Ebene, erstes Los, Laufzeiten ≤ 0 oder > 240 Monate verworfen), dessen Ende ≤ 23.10.2026 liegt | ≥ 100 | A10 |

> **Präzisierung K1 (2026-10-23, nach API-Prüfung, vor Kenntnis von Ergebnissen):** Für Notices vor eForms liefert die Such-API
> keine Haupt-CPV ([02_data_understanding.md](phasen/02_data_understanding.md), Zwischenstand Iteration 2). Der Vorgänger-Pool wird
> deshalb für alle Jahre einheitlich über `classification-cpv=909*` gebildet (Haupt- **oder** Zusatz-CPV 909). Die Ausschreibungen
> (Nenner von K1) bleiben bei Haupt-CPV 909. Schwellen unverändert. Mögliche Fehltreffer durch Zusatz-CPV fängt K2 auf.
> Entscheidung des Nutzers.

> **Anpassung an den Projektplan (2026-10-23, vor Kenntnis von Ergebnissen; Schritt 2 noch nicht begonnen):** Abgleich mit dem
> Entscheidungstor nach Iteration 2 in [projektplan.md](projektplan.md). (1) K2 von ≥ 70 % auf ≥ 80 % angehoben, wie im Projektplan.
> Die Stichprobe bleibt eine Zufallsauswahl aus den Treffern, weil die Regel keinen Score hat und so die Präzision direkt gemessen
> wird. (2) K5 ergänzt, Richtwert „mindestens 100 abgelaufene Verträge“ aus dem Projektplan. Bisher fragte kein Kriterium, ob es
> **genug** Fälle für einen Backtest gibt. Entscheidung des Nutzers.

> **Präzisierung K1-Nenner (2026-10-23, nach Schritt 2, vor jeder Zuordnung):** In eForms werden Korrekturen als eigene
> competition-Notices veröffentlicht (16 % der ersten 250 Notices aus Q2 2026 haben `change-notice-version-identifier`,
> [rueckreichweite_909.md](../reports/rueckreichweite_909.md)). Der Nenner von K1 zählt deshalb **Verfahren** (eindeutige
> `procedure-identifier`), nicht Notices. Änderungsbekanntmachungen zählen nicht extra. Schwellen unverändert.
> Ergebnis Schritt 3: 551 Original-Ausschreibungen (159 von 710 Notices sind Änderungen).

> **Änderung der Kandidatenauswahl (2026-10-23, nach dem ersten Lauf des Prototyps, vor jeder Paarbeurteilung):** Der erste Lauf
> wählte unter mehreren Kandidaten den mit dem ähnlichsten Titel, sonst den jüngsten. Gesehen wurden nur Gesamtzahlen
> (K1 83,7 %, Vorlauf-Median 24 Monate), keine K2-Urteile. Problem: Nur eForms-Notices haben Titel. Kandidaten vor eForms
> konnten daher nie gewinnen, obwohl 358 von 461 Treffern solche haben. Gewählt wurden oft laufende Verträge mit Ende etwa 2 Jahre
> nach der Ausschreibung. **Neue Reihenfolge:** (1) eForms-Kandidat mit Vertragsende 3 Monate vor bis 18 Monate nach der Ausschreibung,
> bei mehreren der mit dem ähnlichsten Titel; (2) sonst der jüngste Kandidat vor eForms; (3) sonst ähnlichster Titel bzw. jüngster.
> K1 ist davon nicht betroffen. **Folge:** Die Vorlaufzeiten der gewählten Paare sind durch das Fenster vorgeprägt und gelten nur
> noch als Beschreibung, nicht als Test von A8. Die erste, nicht ausgefüllte Prüfliste wurde gelöscht und neu gezogen.
> Prüfung K2: Claude bewertet vor (separate Datei), der Nutzer prüft nach. Entscheidung des Nutzers.
> _Nachtrag 2026-10-23:_ Der Nutzer hat die Prüfung vollständig an Claude übertragen („alles selbst prüfen“). Zuordnungsregel und
> K2-Urteil stammen damit aus derselben Hand. Das ist eine Schwäche, die der Evaluator bewerten soll.

Explorativ, ohne Schwelle: Abstand zwischen Vertragsende des Vorgängers und Veröffentlichung der Neuausschreibung (erster Blick auf A8);
Gründe für fehlende Vorgänger (Hinweise auf A3); Anzahl der Vorinformationen (PIN) je Quartal.

**Was folgt aus welchem Ergebnis**
- K1, K2 und K5 erfüllt → **weiter zu Phase 3** (Zuordnung als Skript, Backtest-Datensatz). Iteration 3 = Baseline mit Backtest.
  Ist K3 < 50 %, muss Phase 3 auch Formate vor eForms abdecken.
- K1 und K2 erfüllt, K5 verfehlt → **Historie zu kurz:** vor Iteration 3 ältere Daten über die Original-XML erschließen (A11),
  wie im Projektplan vorgesehen. _(ergänzt 2026-10-23)_
- K1 25–50 % oder K2 50–80 % → **in Phase 2 bleiben**: Gründe für fehlende Vorgänger klären, bevor Phase 3 beginnt.
- K1 < 25 % oder K2 < 50 % → **Idee anpassen / zurück zu Phase 1** (Nachfolger auf TED kaum sichtbar, A3). Optionen: Facility-Services-Radar,
  Prognose aus Auftraggeber-Zyklen statt Vertragsende, nationale Quellen.
- K4 verfehlt → A13 widerlegt bzw. nur teilweise gestützt. Kein Abbruch, die Quote geht als Unsicherheit in den Backtest ein.

**Zeitrahmen:** 2026-10-23 bis 2026-11-08, etwa 4–5 Arbeitssitzungen.

**Plan**
1. TED-API-Dokumentation prüfen: Filter für competition, Rückreichweite der API, Felder für Notices vor eForms, Auftraggeber-Kennungen
   (Phase 2; Notiz in `docs/phasen/02_data_understanding.md`).
2. Rückreichweite und Basisrate: Trefferzahlen je Quartal für CPV-909-Zuschläge, -Ausschreibungen und -Vorinformationen (DEU), so weit die
   API zurückreicht (Ziel ab 2016) (Phase 2; `data/raw/…`, `reports/rueckreichweite_909.md`).
3. Laden: competition-Notices CPV 909 aus Q2 2026 sowie alle CPV-909-Zuschläge (DEU) als Vorgänger-Pool; `src/ted_download.py` um
   Abfrageparameter erweitern; Rohdaten unverändert in `data/raw/` (Phase 2).
4. Replikation K4 mit `src/analyze_completeness.py` auf den Zuschlägen aus Q2 2025; K5 auf den eForms-Zuschlägen ab 25.10.2023
   (Phase 2; Abschnitt im Iterationsreport).
5. Zuordnungs-Prototyp mit einfacher Namensnormalisierung und ggf. Auftraggeber-Kennungen; berechnet K1, K3, Vorlaufzeiten
   (Phase 2/3; `src/zuordnung_prototyp.py`, `reports/zuordnung_iteration2.md`).
6. Manuelle Prüfung: 30 Treffer (K2), 15 Ausschreibungen ohne Treffer (Gründe); bei Vorgängern vor eForms prüfen, ob die Laufzeit
   ablesbar ist (A11) (Phase 2).
7. Kritische Prüfung durch den Evaluator, Abschluss mit `/iteration-ende`.

Bewusst verschoben: Stichprobe der 84 nicht bestimmbaren 909-Notices, Verlängerungen aus Freitext, Los-Ebene (Phase 3 / Iteration 3).
_Vermerk 2026-10-23:_ Die Stichprobe entspricht T2.6.1/T2.6.2 im Projektplan. Sie bleibt verschoben, weil sie für das Entscheidungstor
nach Iteration 2 nicht nötig ist und der Zeitrahmen knapp ist (Entscheidung des Nutzers). T2.6.3 ist teilweise erledigt (Schritt 1).
Parallel in Phase 1, nicht Teil des Kriteriums: 2–3 Reinigungsfirmen für ein Gespräch anfragen (A15).

**Geprüfte Annahmen:** A9 (Hauptannahme), A10, A11, A13; teilweise A3 und A8 (explorativ).

**Ergebnis**

Quellen: [Erg] [ergebnis_iteration2.md](../reports/ergebnis_iteration2.md), [E2] [evaluation_iteration2.md](../reports/evaluation_iteration2.md),
[K] [kennzahlen_iteration2.md](../reports/kennzahlen_iteration2.md), [Z] [zuordnung_iteration2.md](../reports/zuordnung_iteration2.md),
[P] [k2_pruefliste.md](../reports/k2_pruefliste.md), [RR] [rueckreichweite_909.md](../reports/rueckreichweite_909.md).

_Fakten:_

| | Ergebnis | Schwelle (vorab) | Status |
|---|---|---|---|
| K1 | 461 / 551 = 83,7 % (Wilson 80,3–86,5 %) [Z] | ≥ 50 % | erfüllt |
| K2 | 5 / 30 = 16,7 % (Wilson 7,3–33,6 %); 2 unklar, 23 nein [P] | ≥ 80 % | **nicht erfüllt** |
| K3 | 2 / 5 [P] | Messwert | nicht interpretierbar (n zu klein) [E2] |
| K4 | 320 / 390 = 82,1 % (Wilson 77,9–85,5 %) [K] | ≥ 80 % und KI-Untergrenze ≥ 75 % | erfüllt |
| K5 | 629 [K] | ≥ 100 | erfüllt (formal) |

- Such-API ab Ende Okt. 2016; vor eForms ohne Laufzeit, Haupt-CPV und Kennung. Laufzeit vor eForms über `REF_NOTICE` in der alten
  Ausschreibung (10 von 10, nicht zufällig). [RR], [Erg]
- Bestimmbares Laufzeitende 2023/2024 nur ca. 70 %, ab 2025 ca. 80 %. [K]
- K5-Verträge: Median-Laufzeit 12 Monate, 410 von 629 aus 2024. [K], [E2]
- K2 nach Kandidatenzahl: 1–2 Kandidaten 3 von 6, mehr als 10 Kandidaten 1 von 15. Typischer Fehler: gleicher Auftraggeber, anderes
  Objekt. [P]
- Evaluator: 29 von 30 K2-Urteilen bestätigt. Neu gefunden: A30, der objektgleiche Vorgänger war unter den Kandidaten. 3 von 6
  objektgleichen Paaren sind vorzeitige Neuvergaben. [E2]
- K2-Prüfung durch Claude allein (auf Wunsch des Nutzers). Die Schwellen von K2 und K5 standen nachweislich vor den Ergebnissen fest
  (Commit 3fa8418, 09:26 MESZ). [E2]

_Interpretation:_
- Die Hypothese ist im Wortlaut bestätigt (K1), sagt aber wenig aus: Große Auftraggeber schreiben ständig Reinigung aus.
- Über den Auftraggeber lässt sich der Vorgängervertrag nicht zuordnen. Ob die Vorgänger auf TED überhaupt sichtbar sind, wurde
  nicht gemessen. Die Befunde zeigen in beide Richtungen. [E2]
- Ein Backtest nur mit eForms-Daten wäre stark verzerrt. Vorzeitige Neuvergaben sind ein Warnsignal für das Prognoseziel (A8, A16).

**Entscheidung:** **Idee anpassen** (Entscheidung des Nutzers, 2026-10-23). Die Zuordnung über den Auftraggeber wird verworfen.
Iteration 3 bleibt in Phase 2 und misst **getrennt**:
1. die Sichtbarkeit der Vorgänger (von Hand, unter Zuschlägen und früheren Ausschreibungen),
2. die Zuordnung über das Objekt (Adresse, Liegenschaft, Titel) auf getrennten Entwicklungs- und Testdaten.

Neue Kriterien und eine harte Abbruchregel (bei geringer Sichtbarkeit: nationale Quellen oder Auftraggeber-Zyklen) werden mit
`/iteration-start` vorab festgelegt und committet. Nicht weiter zu Phase 3.

> **Abweichung von der vorab festgelegten Regel:** Die Regel „K1 < 25 % oder K2 < 50 % → Idee anpassen / zurück zu Phase 1
> (Nachfolger auf TED kaum sichtbar, A3)“ ist ausgelöst. Ihre Optionsliste (Facility-Services-Radar, Auftraggeber-Zyklen, nationale
> Quellen) enthielt eine Zuordnung über das Objekt nicht. Begründung der Abweichung: Die Regel hat zwei Dinge vermengt, nämlich wie
> gut die Methode trifft (Präzision) und ob die Daten den Vorgänger überhaupt enthalten (Sichtbarkeit). A30 zeigt mindestens einen
> Fall, in dem die Methode versagte, obwohl die Daten vorhanden waren. Die vorab genannten Optionen bleiben als Ausweg bestehen,
> falls Iteration 3 eine zu geringe Sichtbarkeit zeigt. [E2]

**Hinweise für Iteration 3** (Vorschläge des Evaluators, [E2]):
- Population enger fassen (90911/90919, Ausschluss von Bau-, Sonder-, Fahrzeug- und Industriereinigung sowie Schädlingsbekämpfung),
  anderes Quartal als Q2 2026, höchstens 2 Ausschreibungen je Auftraggeber.
- „Objektgleich“ vorab definieren; der Zeitpunkt gehört nicht zur Definition.
- 1:1-Zuordnung ohne Zeitfenster als Auswahlkriterium; frühere Ausschreibungen als Vorgängerquelle einbeziehen.
- Zweitprüfung: Der Nutzer beurteilt mindestens 20 Paare blind.
- A11 an einer Zufallsstichprobe prüfen; zuordenbare Paare mit bekanntem Ende zählen (Backtest-Basis laut Projektplan).
- Parallel in Phase 1: Gespräche mit Reinigungsfirmen (A15).

---

## Iteration 3: Sichtbarkeit der Vorgänger und Zuordnung über das Objekt

**Status:** läuft seit 2026-10-24 (angelegt am 2026-10-23)

**Fokus und Phasen:** Phase 2, Vorarbeit für Phase 3. Abweichung vom Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan) gemäß
Entscheidung zu Iteration 2: Die erste Prognose (jetzt Iteration 4) folgt erst, wenn eine Zuordnung über das Objekt belegt ist.

**Hypothese** _(vorab festgelegt am 2026-10-23, vor Kenntnis der Ergebnisse)_
„Für mindestens die Hälfte der eng abgegrenzten deutschen Gebäudereinigungs-Ausschreibungen aus Q3 2026 gibt es auf TED einen
objektgleichen Vorgänger. Eine einfache Regel über Objektmerkmale ordnet ihn mit mindestens 80 % Präzision zu.“

**Begriffe** _(vorab festgelegt)_
- **Population:** Ausschreibungen (competition), Auftraggeber DEU, Haupt-CPV 90910/90911/90919, nur Originale (ohne
  `change-notice-version-identifier`). Ausgeschlossen über eine Stichwortliste im Titel (Bau-, Bauend-, Schimmel-, Fahrzeug- und
  Industriereinigung, Schädlingsbekämpfung). Die genaue Liste wird in Schritt 1 festgehalten und committet, **bevor** Testdaten
  angesehen werden.
- **Entwicklungsdaten:** Ausschreibungen Q2 2026 (inkl. der 30 K2-Paare aus Iteration 2). **Testdaten:** Ausschreibungen Q3 2026
  (01.07.–30.09.2026). Testprobe: 60 Zufallsfälle (Seed 20261024), höchstens 2 je Auftraggeber.
- **Vorgänger-Quellen:** Zuschläge **und** frühere Ausschreibungen auf TED, veröffentlicht ab Okt. 2016 und vor der Testausschreibung.
- **Objektgleich:** gleiche Adresse oder gleicher Liegenschaftsname **und** überlappende Leistungsart (Unterhalts-, Grund-,
  Glasreinigung). Eigene Kategorie „Teilmenge/Neuzuschnitt“: mindestens ein gemeinsames Objekt; zählt in V1 als gefunden, wird
  getrennt ausgewiesen. Der Zeitpunkt ist nicht Teil der Definition.
- **Vorzeitige Neuvergabe:** Der neue Vertrag beginnt mindestens 3 Monate vor dem Ende der Grundlaufzeit des Vorgängers.
- **Reihenfolge:** (1) Regel auf Entwicklungsdaten bauen und per Commit einfrieren, (2) erst dann Testprobe ziehen, (3) Handsuche
  mit Protokoll abschließen und committen, **bevor** die Regel auf den Testdaten läuft.

**Erfolgskriterium** _(vorab festgelegt am 2026-10-23)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| V1 Sichtbarkeit | Anteil der 60 Testfälle mit objektgleichem Vorgänger auf TED (Handsuche mit Protokoll) | ≥ 50 % | A3, A9b |
| V2 Präzision | Anteil korrekter Vorschläge der eingefrorenen Regel auf den Testfällen | ≥ 80 % **und** Wilson-Untergrenze ≥ 60 % | A9b |
| V3 Trefferquote | Anteil der in V1 gefundenen Vorgänger, die die Regel korrekt findet | ≥ 60 % | A9b |
| V4 Zweitprüfung | Übereinstimmung zwischen Claude und dem Nutzer bei 20 blind beurteilten Paaren | ≥ 85 % | – |
| V5 Backtest-Basis | Korrekt zugeordnete Paare mit bestimmbarem Vorgänger-Ende, hochgerechnet (Anteil im Test × Verfahren pro Jahr der Population, aus Q3 2026 × 4) | ≥ 100 pro Jahr | A10 |
| V6 A11 | Anteil von 30 zufälligen Zuschlägen vor eForms (2018–2023, CPV 909, DEU) mit Laufzeit über `REF_NOTICE` | ≥ 80 % | A11 |

Explorativ mit vorab festgelegter Folge: Anteil vorzeitiger Neuvergaben unter den objektgleichen Paaren mit bekanntem Vorgänger-Ende.
Über 30 % → Prognoseziel in Phase 1 neu bewerten (A16, A8).

**Was folgt aus welchem Ergebnis**
- V4 < 85 % → Definition schärfen. V1–V3 gelten nicht, die Messung wird wiederholt.
- V1 < 30 % → **zurück zu Phase 1:** nationale Quellen oder Prognose aus Auftraggeber-Zyklen (in Iteration 2 vorab als Ausweg genannt).
- V1 30–50 % → **Idee anpassen:** Teilsegment (z. B. Auftraggeber mit wenigen Verträgen) in Phase 1 festlegen, bevor Phase 3 beginnt.
- V1 ≥ 50 %, aber V2 oder V3 verfehlt → **in Phase 2/3 bleiben:** ein letzter Verbesserungsversuch der Regel, alternativ Produkt mit
  manueller Prüfung.
- V1, V2, V3 und V5 erfüllt (V4 erfüllt) → **weiter zu Phase 3**, danach Iteration 4 (erste Prognose und Backtest).
- V6 < 80 % → Backtest nur mit eForms-Daten, Verzerrung offen ausweisen; A11 widerlegt.

**Zeitrahmen:** 2026-10-24 bis 2026-11-15, etwa 5–6 Arbeitssitzungen; Nutzer etwa 1 Stunde für V4.

**Plan**
1. Population und Ausschlussliste festlegen; Q3-2026-Ausschreibungen und alle Gebäudereinigungs-Ausschreibungen seit 2016 laden
   (Phase 2; `data/raw/…`, `reports/population_iteration3.md`).
2. Objektmerkmale je Los extrahieren (Titel, Ort, PLZ, Straße): eForms über die API, Notices vor eForms über die XML (nur Kandidaten)
   (Phase 2/3; `src/objekt_merkmale.py`).
3. Zuordnungsregel auf Entwicklungsdaten bauen (unscharfer Auftraggebername und/oder gleiche PLZ, Ähnlichkeit von Titel und Adresse,
   1:1, kein Zeitfenster); Commit = eingefroren (`src/zuordnung_objekt.py`).
4. Testprobe ziehen, Handsuche mit Protokoll (V1) (`reports/sichtbarkeit_iteration3.md`).
5. Regel auf Testdaten anwenden (V2, V3, V5, vorzeitige Neuvergaben); Blindprüfung durch den Nutzer (V4)
   (`reports/zuordnung_iteration3.md`, `reports/blindpruefung_iteration3.md`).
6. A11-Zufallsstichprobe (V6) (`reports/a11_stichprobe.md`).
7. Iterationsreport, Evaluator, `/iteration-ende`.

Parallel in Phase 1, nicht Teil des Kriteriums: 2–3 Gespräche mit Reinigungsfirmen (A15), auch zur Frage, ob Auftraggeber-Ebene reicht.

**Geprüfte Annahmen:** A9b, A11 (Hauptgegenstand); A3 (nur TED-Sichtbarkeit, nicht Marktanteil); A10, A12, A16 (teilweise bzw.
explorativ); A8 (Hinweis).

**Ergebnis:** offen

**Entscheidung:** offen
