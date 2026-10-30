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
| 3 | Sichtbarkeit der Vorgänger und Zuordnung über das Objekt | 2 (→ 3) | 2026-10-24 bis 2026-10-25 | abgeschlossen | **In Phase 2/3 bleiben:** V1 63,3 % (knapp, definitionsabhängig), V2 45,8 % und V3 28,9 % verfehlt; ein letzter Verbesserungsversuch der Regel auf neuen Testdaten, parallel „Produkt mit manueller Prüfung“ in Phase 1 bewerten |
| 4 | Letzter Verbesserungsversuch der Objekt-Zuordnung (neue Testdaten Q1 2026) | 2/3 (parallel 1) | 2026-10-25 bis 2026-10-30 | abgeschlossen | **Idee anpassen (Phase 1):** W4 65 % < 85 % (W2 89,5 % bei nur 19 Vorschlägen, W3 56,7 %, W1 42,9 %); keine weitere Regel, Iteration 5 baut eine Vertragsliste aus Zuschlägen |
| 5 | Vertragsliste aus Zuschlägen: Prognoseziel Höchstende, erste Prognose, Backtest auf handgeprüften Paaren | 1 → 3 → 4 → 5 | 2026-10-31 bis 2026-11-21 (geplant) | läuft | offen |
| 6 | Verbesserung der Prognose | 3 → 4 → 5 | – | geplant | – |
| 7 | Prototyp der Vertragsliste (statt Kundentest) | 6 | – | geplant | – |
| 8+ | Ausbau oder Neuausrichtung | je nach Ergebnis | – | geplant | – |

Die geplanten Iterationen stammen aus dem Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan). Nach der Entscheidung zu Iteration 1
sind sie um eine Stelle verschoben. Konkretisiert werden sie mit `/iteration-start`.
_Nachtrag 2026-10-23:_ Die geplanten Zeilen (3 bis 6+) sind an den [Projektplan](projektplan.md) angeglichen, der jetzt eine eigene
Verbesserungs-Iteration vorsieht.
_Nachtrag 2026-10-23 (Abschluss Iteration 2):_ Nach der Entscheidung zu Iteration 2 ist eine weitere Phase-2-Iteration (3)
eingeschoben; die übrigen rücken um eine Stelle.
_Nachtrag 2026-10-25 (Abschluss Iteration 3):_ Nach der Entscheidung zu Iteration 3 ist Iteration 4 (letzter Verbesserungsversuch der
Zuordnung) eingeschoben; die übrigen rücken erneut um eine Stelle.
_Nachtrag 2026-10-29 (Entscheidung des Nutzers):_ Kein Kundenkontakt im Projekt. Iteration 7 wird ein Prototyp der Vertragsliste,
selbst bewertet gegen den Backtest, statt eines Kundentests. Annahmen A1 und A15 bleiben ungeprüft (außerhalb des Projektumfangs).
_Nachtrag 2026-10-30 (Abschluss Iteration 4):_ Iteration 5 wird nach der Entscheidung „Idee anpassen“ eine Vertragsliste aus Zuschlägen
mit Backtest auf handgeprüften Paaren; die automatische Objekt-Zuordnung wird nicht weiter verbessert.

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

**Status:** abgeschlossen am 2026-10-25 (angelegt am 2026-10-23, Arbeit ab 2026-10-24)

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

> **Nachtrag 2026-10-23 (vor Schritt 1, Kriterien unverändert):** Die Handsuche für V1 (Schritt 4) führt der Subagent `rechercheur`
> (`.claude/agents/rechercheur.md`) nach festem Protokoll durch. Er kennt die Zuordnungsregel und ihre Ergebnisse nicht. Damit sind
> der Bau der Regel und die Ground Truth personell getrennt (es ist aber dasselbe Modell, also keine echte Zweitmeinung; dafür V4).
> Entscheidung des Nutzers.

> **Fortschritt 2026-10-23:** Population festgelegt (Commit af36eab), Zuordnungsregel auf Entwicklungsdaten gebaut und eingefroren
> (Commit 4497743, [regel_entwicklung_iteration3.md](../reports/regel_entwicklung_iteration3.md)), danach Testprobe gezogen
> ([testfaelle_iteration3.md](../reports/testfaelle_iteration3.md): Population Q3 2026 = 492 Verfahren, 60 Fälle, 54 Auftraggeber).
> Die Handsuche läuft in 4 Teilen zu je 15 Fällen nacheinander, mit identischem Auftrag an den Rechercheur.

> **Fortschritt 2026-10-24:** Handsuche abgeschlossen und vor dem Regel-Lauf committet (850747c). Regel auf Testdaten angewendet,
> 14 Vorschläge außerhalb der Handsuche von Claude einzeln beurteilt (84313ea, [zuordnung_iteration3.md](../reports/zuordnung_iteration3.md)).
> **Festlegung V4 (vor dem Urteil des Nutzers):** 20 Paare laut `src/blindpruefung_iteration3.py` (3 schwach belegte und 7 zufällige
> Treffer der Handsuche, 8 Einzelurteile von Claude, 2 unklare Kandidaten), zufällig gemischt. Übereinstimmung wird binär gezählt:
> „gefunden“ (objektgleich/teilmenge) gegen „nicht gefunden“ (nicht objektgleich/unklar). Der Lösungsschlüssel liegt lokal in
> `data/processed/blindpruefung_iteration3_schluessel.csv`, SHA-256 `c45d448c11ab1d2296e63581ec1a0ca258a735d8b6e34757d5dc37556e319eaf`.

> **Nachtrag 2026-10-24 (V4, vor Kenntnis des Schlüssels):** Der Nutzer hat alle 20 Paare angesehen und berichtet pauschal, er hätte
> jedes Paar als passend oder als unsicher eingestuft. Paarweise erfasst wurde das nicht. Danach hat er Urteilsregeln geschrieben
> ([urteilsregeln_blindpruefung.md](../reports/urteilsregeln_blindpruefung.md), Version 1; am selben Tag Version 2 mit zwei Klarstellungen, Details in der Datei). Sie entstanden also **nach** dem ersten
> Ansehen der Paare und gelten ab diesem Commit unverändert. Weiteres Vorgehen (Entscheidung des Nutzers, als Abweichung dokumentiert):
> (1) Ein Subagent beurteilt alle 20 Paare nach diesen Regeln in einer eigenen Datei, ohne Zugriff auf Schlüssel, Handsuche und Einzelurteile.
> Er ist ein zusätzlicher regelbasierter Prüfer und **ersetzt nicht** den Menschen in V4 (dasselbe Modell wie Claude). (2) Der Nutzer
> trägt seine Urteile nach denselben Regeln in `blindpruefung_iteration3.md` ein, bevor er die Datei des Agenten öffnet. **V4 zählt
> die Urteile des Nutzers** gegen den Schlüssel (binär wie oben; zusätzlich streng/breit laut Regeln). Die pauschale erste Einschätzung
> („alle passen“) wird im Ergebnis als Hinweis auf eine zu unscharfe Ausgangsdefinition berichtet.

> **Nachtrag 2026-10-24 (Urteilsregeln, vor dem ersten eingetragenen Urteil des Nutzers):** Der Nutzer hat die Regeln zu
> „Version 1.1“ ausgebaut (u. a. Schwellen für Fläche und Objektlisten, Einzelstandorte, Tendenz bei „unklar“). Sie ersetzt Version 1
> (eff8f55) und Claudes „Version 2“ (d8eb31f), deren zwei Klarstellungen sie enthält. **Die acht Kalibrierungsbeispiele der
> Version 1.1 sind die Prüfpaare P1–P8** (Wuppertal, Berlin BGW, Stade/Harburg, Stralsund, Düsseldorf, Esslingen, Saarbrücken,
> Springe). Nach Regel 1.1 („wird dort nicht gezählt“) fallen sie aus V4 heraus; gewertet werden **P9–P20 (n = 12)**. Die
> Kalibrierung wurde teils nach Kenntnis der Grenzfall-Hinweise des Subagenten (Version 1) erstellt (z. B. Esslingen, Flächen).
> Der Lösungsschlüssel ist dem Nutzer weiterhin unbekannt. Die Agentenprüfung nach Version 1 ist mit Version 1.1 nicht direkt
> vergleichbar.
> **Ergänzung (Entscheidung des Nutzers):** 8 Ersatzpaare P21–P28 in derselben Zusammensetzung wie P1–P8 (4 „gefunden“, 4 „nicht“),
> nur aus Testfällen, die in keinem anderen Paar vorkommen (`--ergaenzen`, Seed 20261025). Schlüssel lokal in
> `data/processed/blindpruefung_iteration3_schluessel_ergaenzung.csv`, SHA-256
> `59672f7ece76b5f6e8c54f3c7e43d653197cda4f23939bf3daf66778727ab4f2`. **V4 wird über P9–P28 (n = 20) gezählt.** Der Subagent
> beurteilt P9–P28 erneut nach Version 1.1 (eigene Datei).

**Geprüfte Annahmen:** A9b, A11 (Hauptgegenstand); A3 (nur TED-Sichtbarkeit, nicht Marktanteil); A10, A12, A16 (teilweise bzw.
explorativ); A8 (Hinweis).

**Ergebnis** _(2026-10-25)_

Quellen: **[Z3]** [zuordnung_iteration3.md](../reports/zuordnung_iteration3.md) · **[GT]** [sichtbarkeit_iteration3_gt.csv](../reports/sichtbarkeit_iteration3_gt.csv)
und `sichtbarkeit_iteration3_teil1–4.md` · **[A11]** [a11_stichprobe.md](../reports/a11_stichprobe.md) · **[BN]**
[blindpruefung_iteration3_nutzer.md](../reports/blindpruefung_iteration3_nutzer.md) · **[BA]**
[blindpruefung_iteration3_agent_v1_1.md](../reports/blindpruefung_iteration3_agent_v1_1.md) · **[E3]**
[evaluation_iteration3.md](../reports/evaluation_iteration3.md) · **[RE]** [regel_entwicklung_iteration3.md](../reports/regel_entwicklung_iteration3.md).

_Fakten_

| Kriterium | Ergebnis | Schwelle | formal | Urteil Evaluator [E3] |
|---|---|---|---|---|
| V1 Sichtbarkeit | 38/60 = 63,3 % (Wilson 50,7–74,4) [Z3]; davon 29 objektgleich, 9 Teilmenge [GT]; nur objektgleich 29/60 = 48,3 % [E3] | ≥ 50 % | erfüllt | knapp, abhängig von der Definition |
| V2 Präzision | 11/24 = 45,8 % (Wilson 27,9–64,9) [Z3] | ≥ 80 %, Untergrenze ≥ 60 % | verfehlt | klar verfehlt |
| V3 Trefferquote | 11/38 = 28,9 % (Wilson 17,0–44,8) [Z3] | ≥ 60 % | verfehlt | klar verfehlt |
| V4 Zweitprüfung | Urteile des Nutzers P9–P28: 17/20 = 85 % (Wilson 64,0–94,8; κ ≈ 0,70) [BN], [E3]; Abweichungen P16, P18, P28. Regelbasierter Subagent ebenfalls 17/20 (Abweichungen P16, P17, P18) [BA] | ≥ 85 % | erfüllt (genau auf der Schwelle) | als Beleg nicht tragfähig |
| V5 Backtest-Basis | 10/60 × 492 × 4 = 328 pro Jahr [Z3]; Enddaten T26, T56, T18 fragwürdig, robust etwa 230; nur eForms-Vorgänger etwa 98–131 [E3] | ≥ 100 pro Jahr | erfüllt | überschätzt |
| V6 A11 | 25/30 = 83,3 % (Wilson 66,4–92,7); 2 ohne `REF_NOTICE`, 3 nur Dauer [A11] | ≥ 80 % | erfüllt | knapp, enger Geltungsbereich |
| Explorativ: vorzeitige Neuvergaben | 2/36 = 5,6 % (Wilson 1,5–18,1; T18 Lose 8/9, T32) [E3] aus [GT] | Folge bei > 30 % | nicht ausgelöst | – |

- Fehlertypen der Regel: 9 von 11 falschen Vorschlägen sind Geschwisterverfahren desselben Auftraggebers, 2 betreffen dasselbe Objekt
  mit anderer Leistungsart (T31, T54); alle 11 sind Notices aus 2025/2026. Bei 19 von 38 gefundenen Fällen macht die Regel keinen
  Vorschlag [E3].
- Die meisten Vorgänger sind Bekanntmachungen vor eForms. Die Handsuche fand sie über die Volltextsuche und die XML; in den lokalen
  Rohdaten fehlen dort Titel und Ort [GT], [E3]. Nur etwa 5 der 38 Vorgänger sind eForms-Verträge [E3].
- Bei mindestens 10 der 38 Paare liegt zwischen Vorgänger und Testfall eine Lücke; das Glied direkt davor fehlt auf TED [E3].
- Auf den Entwicklungsdaten hielt Claude etwa 10–11 von 12 Vorschlägen für plausibel [RE], im Test waren 11 von 24 korrekt.
- Abweichungen vom Vorab-Plan, alle in den Nachträgen oben dokumentiert: Urteilsregeln für V4 nach dem ersten Ansehen der Paare,
  P1–P8 als Kalibrierung ausgeschlossen und durch P21–P28 ersetzt, pauschale Ersteinschätzung des Nutzers („alle passen oder
  unsicher“). Ergänzende Auslegungen während der Handsuche (Teil 2 und Teil 4) [E3].
- T16 (Bauendreinigung) fällt sachlich aus der Population, weil die Ausschlussliste nur den Titel prüft [E3].

_Interpretation_

- **Die Hypothese ist zur Hälfte gestützt.** Objektgleiche Vorgänger sind auf TED oft sichtbar, knapp über der Schwelle und nur, wenn
  Teilmengen mitzählen. Die einfache Regel ordnet sie aber nicht zuverlässig zu (Präzision 46 % statt 80 %).
- **Die Regel scheitert vor allem an zwei Stellen:** an Geschwisterverfahren großer Auftraggeber und an fehlenden Objektmerkmalen vor
  eForms. Das zweite ist eher ein Problem des Datenzugangs als der Vergleichslogik [E3].
- **V4 = 85 % zeigt keine eindeutige Definition.** Die Regeln entstanden an denselben Paaren, und die regelfreie erste Einschätzung
  wich stark ab. Wie im Nachtrag angekündigt, wird das als Hinweis auf eine zu unscharfe Ausgangsdefinition berichtet.
- **Ein Zeitfenster als schnelle Lösung ist ausgeschlossen.** Es hätte zwar alle 11 Fehler entfernt, aber auch die beiden vorzeitigen
  Neuvergaben. Damit würde A16 in die Regel eingebaut, und der Backtest wäre zirkulär [E3].
- **V5 beschreibt eine Basis mit manueller Prüfung**, keine automatische. Ein Backtest nur mit eForms-Daten läge an der Grenze von V5.
- **Vorzeitige Neuvergaben sind hier selten (5,6 %).** Das ist ein Gegenbeleg zum Warnsignal aus Iteration 2 (3 von 6). Die beiden
  Auswahlen sind aber nicht vergleichbar. Neuvergaben vor dem Höchstende (nach der Grundlaufzeit) kommen häufiger vor.

**Entscheidung** _(2026-10-25, Entscheidung des Nutzers nach Vorschlag von Claude und Evaluator)_

**In Phase 2/3 bleiben**, gemäß der vorab festgelegten Folge „V1 ≥ 50 %, aber V2 oder V3 verfehlt“. Vermerk: V1 und V4 sind nur knapp
und abhängig von der Definition erfüllt. Bei strengerer Lesart griffe „Definition schärfen“ bzw. „Idee anpassen“; an der Aussage
„die Regel reicht nicht“ ändert das nichts.
- **Iteration 4 wird der letzte Verbesserungsversuch der Zuordnung:**
  - Objekt- und Leistungsart-Merkmale auf Los-Ebene, auch vor eForms aus XML bzw. Volltextsuche
  - harte Prüfung der Leistungsart
  - Geschwisterverfahren über Objektlisten und Flächen trennen, **kein Zeitfenster**
  - Q3 2026 wird zu Entwicklungsdaten; **neue Testdaten aus Q1 2026**, etwa 60–70 Fälle
  - Handsuche nach Urteilsregeln Version 1.1, **vor** dem Regel-Lauf
  - V4 mit frischen, vorher nicht angesehenen Paaren, gezielt mit schwach belegten Treffern und „kein Vorgänger“-Fällen
  - Abbruchkriterium vorab festlegen
- **Parallel in Phase 1:** die Alternative „Produkt mit manueller Prüfung“ bewerten. Die Regel liefert dann nur Kandidaten.
- Die erste Prognose mit Backtest wird Iteration 5.
- A11 bleibt „vorläufig gestützt“, A9b ist für die eingefrorene Regel widerlegt; die allgemeine Objekt-Zuordnung wird als A9c weitergeführt.
- Offen aus der Evaluation: korrigierte Enddaten für V5 (T26, T56, T18), Belegstärke T18–T30 in `gt.csv`, Originaldatei der
  Nutzerurteile im Repo.

> **Nachtrag 2026-10-25 (nach Abschluss, Korrekturen aus der Evaluation; Entscheidung unverändert):**
> - **Vorgänger-Enddaten** ([vorgaenger_ende_iteration3_korrektur.csv](../reports/vorgaenger_ende_iteration3_korrektur.csv), belegt aus
>   den Protokollen der Handsuche): T26 hatte das geplante Ende des aufgehobenen Verfahrens 462151-2026 (2031-10-31); das Ende des
>   tatsächlichen Vorgängervertrags ist 2026-03-31, aber nicht über den Regelvorschlag erreichbar. T56 verlängert sich jährlich ohne
>   Höchstdauer, das Ende ist unbekannt. T18 gilt nur für die Lose 8/9. **V5 korrigiert: 8/60 × 492 × 4 = 262 pro Jahr**
>   (Wilson 136–476), Schwelle ≥ 100 weiterhin erfüllt. `reports/zuordnung_iteration3.md` bleibt als Stand des Laufs unverändert.
> - **Belegstärke** in `sichtbarkeit_iteration3_gt.csv` für T18, T19, T21, T22, T23, T24, T26, T30 aus Teil 2 nachgetragen (Übertragungsfehler;
>   T21 und T30 „mittel“, die übrigen „stark“). Die Auswahl der Paare für V4 erfolgte mit den leeren Feldern; `src/blindpruefung_iteration3.py`
>   wird nicht erneut ausgeführt.
> - **Originalurteile des Nutzers** liegen jetzt in [blindpruefung_iteration3_nutzer_original.md](../reports/blindpruefung_iteration3_nutzer_original.md)
>   (Commit 877674d). Urteile, Sicherheit und Tendenz stimmen mit der kompakten Übertragung überein; V4 bleibt 17/20.

## Iteration 4: Letzter Verbesserungsversuch der Objekt-Zuordnung

**Status:** abgeschlossen am 2026-10-30 (angelegt am 2026-10-25)

**Fokus und Phasen:** Phase 2/3, parallel Phase 1. Abweichung vom Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan) gemäß
Entscheidung zu Iteration 3: Die erste Prognose (jetzt Iteration 5) folgt erst, wenn eine Zuordnung belegt ist. Dies ist der **letzte**
Regelversuch; einen dritten gibt es nicht.

**Hypothese** _(vorab festgelegt am 2026-10-25, vor Kenntnis der Ergebnisse)_
„Eine Regel, die Objektliste, Adresse, Fläche und Leistungsart auf Los-Ebene vergleicht (vor eForms aus der XML), ordnet auf neuen
Testdaten (Ausschreibungen Q1 2026) den objektgleichen Vorgänger mit mindestens 80 % Präzision und mindestens 60 % Trefferquote zu.“

**Begriffe** _(vorab festgelegt)_
- **Population:** wie Iteration 3 (competition, Auftraggeber DEU, Haupt-CPV 90910/90911/90919, nur Originale, Stichwortliste aus
  `src/population_iteration3.py`). **Neu:** Die Ausschlussliste wird auch auf Los-Titel und Beschreibung angewendet, nicht nur auf den
  Titel der Bekanntmachung (Anlass: T16). Die genaue Fassung wird in Schritt 1 committet, **bevor** Testdaten angesehen werden.
- **Testdaten:** Ausschreibungen Q1 2026 (01.01.–31.03.2026). Testprobe: **70 Zufallsfälle**, höchstens 2 je Auftraggeber, Seed wird
  in Schritt 1 festgelegt. Ausgeschlossen sind Notices, die in einem Report von Iteration 2 oder 3 vorkommen (einige Q1-2026-Notices
  waren dort Vorgänger-Kandidaten, z. B. 165984-2026, 156628-2026).
- **Entwicklungsdaten:** Ausschreibungen Q2 2026 und Q3 2026. Für Q3 ist die Handsuche aus Iteration 3 der Maßstab.
- **Vorgänger-Quellen:** wie Iteration 3 (Zuschläge und frühere Ausschreibungen auf TED, ab Okt. 2016, vor der Testausschreibung).
- **Ground Truth:** Handsuche durch den Subagenten `rechercheur` mit festem Protokoll, **Kategorien nach
  [Urteilsregeln Version 1.1](../reports/urteilsregeln_blindpruefung.md)** (u. a. Teilmenge = mindestens 50 % der kürzeren Objektliste
  auf beiden Seiten belegt; andere Leistungsart = nicht objektgleich). Regelvorschläge außerhalb der Handsuche beurteilt ebenfalls der
  Rechercheur nach Version 1.1, ohne Kenntnis der Herkunft des Paares (nicht mehr Claude).
- **Korrekt** (W2, W3) = objektgleich (hoch oder mittel) oder teilmenge nach Version 1.1. Unklar zählt als nicht korrekt.
- **Vorgänger-Ende:** mit Herkunft gekennzeichnet (Grundlaufzeit, Höchstende, aufgehobenes Verfahren, unbekannt). Für W5 zählt nur ein
  bestimmbares Ende der Grundlaufzeit des tatsächlichen Vorgängervertrags.
- **Kein Zeitfenster** in der Regel, weder als Filter noch als Score-Merkmal.
- **Reihenfolge:** (1) Regel auf Entwicklungsdaten bauen und per Commit einfrieren, (2) erst dann Testprobe ziehen, (3) Handsuche mit
  Protokoll abschließen und committen, (4) erst dann die Regel auf den Testdaten anwenden, (5) danach die Blindprüfung W4.

**Erfolgskriterium** _(vorab festgelegt am 2026-10-25)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| W1 Sichtbarkeit | Anteil der 70 Testfälle mit objektgleichem Vorgänger oder Teilmenge (nach Version 1.1); nur objektgleich wird zusätzlich ausgewiesen | ≥ 50 % | A3 |
| W2 Präzision | korrekte Vorschläge / alle Vorschläge der eingefrorenen Regel | ≥ 80 % **und** Wilson-Untergrenze ≥ 60 %, bei mindestens 25 Vorschlägen | A9c |
| W3 Trefferquote | von der Regel korrekt gefundene / in W1 gefundene Vorgänger | ≥ 60 % | A9c |
| W4 Zweitprüfung | Übereinstimmung zwischen Nutzer und Ground Truth bei 20 frischen, vorher nicht angesehenen Paaren (binär: gefunden = objektgleich/teilmenge, nicht = nicht objektgleich/unklar) | ≥ 85 % | – |
| W5 Backtest-Basis | korrekte Paare mit bestimmbarem Vorgänger-Ende, hochgerechnet: Anteil im Test × Populationsgröße der letzten 4 Quartale (Q4 2025 bis Q3 2026) | ≥ 100 pro Jahr | A10, A11 |
| W6 Kandidatenliste | Anteil der W1-Fälle, bei denen der Vorgänger unter den höchstens 3 angezeigten Kandidaten der Regel ist | ≥ 70 % | A9c (Produkt mit manueller Prüfung) |

Explorativ, ohne Schwelle: Prüfzeit je Paar in W4 (Nutzer notiert Minuten), Vorlaufzeit (Veröffentlichung des Testfalls bis
Vorgänger-Ende) bei bestätigten Paaren (A8), Anteil vorzeitiger Neuvergaben wie in Iteration 3 (A16).

**Was folgt aus welchem Ergebnis**
- W4 < 85 % → W2, W3 und W6 gelten nur als Hinweis. Kein weiterer Regelversuch; Entscheidung in Phase 1 (**Idee anpassen**).
- W1 < 30 % → **zurück zu Phase 1:** nationale Quellen oder Prognose aus Auftraggeber-Zyklen.
- W2, W3 und W5 erfüllt (W4 erfüllt) → **weiter zu Phase 3**, danach Iteration 5 (erste Prognose und Backtest).
- W2 oder W3 verfehlt, aber W6 ≥ 70 % und Median-Prüfzeit ≤ 5 Minuten je Paar → **Idee anpassen: Produkt mit manueller Prüfung**;
  Iteration 5 macht den Backtest auf manuell bestätigten Paaren.
- sonst → **zurück zu Phase 1:** Objekt-Zuordnung aufgeben; Auftraggeber-Ebene, nationale Quellen oder Projektziel neu bewerten.

**Zeitrahmen:** 2026-10-26 bis 2026-11-22, etwa 6–8 Arbeitssitzungen; Nutzer etwa 1,5 Stunden für W4, dazu Gespräche.

**Plan**
1. Aufräumen und Vorarbeiten (Phase 2/3), Commit vor dem Regelbau: Enddaten T26, T56, T18 korrigieren; Belegstärke T18–T30 in
   `reports/sichtbarkeit_iteration3_gt.csv` nachtragen; Originaldatei der Nutzerurteile ablegen; Rechercheur auf Urteilsregeln 1.1
   umstellen (`.claude/agents/rechercheur.md`); Ausschlussliste erweitern und Testpopulation festlegen (`src/population_iteration4.py`).
2. Merkmale auf Los-Ebene (Phase 3, `src/objekt_merkmale.py`): Objektliste, Adressen, Flächen und Leistungsart je Los, vor eForms aus
   der XML. Vorher die TED-Doku prüfen, ob die Volltextsuche `FT` für Kandidaten vor eForms taugt.
3. Regel auf Q2 + Q3 2026 verbessern und per Commit einfrieren (`src/zuordnung_objekt.py`, `reports/regel_entwicklung_iteration4.md`):
   Leistungsart hart prüfen, Geschwisterverfahren über Objektlisten und Flächen trennen, kein Zeitfenster, Kandidatenliste mit
   höchstens 3 Einträgen.
4. Testprobe Q1 2026 ziehen, Handsuche in 5 Teilen zu je 14 Fällen, committet vor dem Regel-Lauf (`reports/sichtbarkeit_iteration4_teil*.md`).
5. Regel auf Testdaten anwenden (W2, W3, W5, W6); Vorschläge außerhalb der Handsuche beurteilt der Rechercheur
   (`reports/zuordnung_iteration4.md`).
6. Blindprüfung W4: 20 frische Paare, Zusammensetzung vorab festgelegt (schwach belegte Treffer, Regelvorschläge, Fälle ohne Vorgänger
   mit bestem Kandidaten, Zufall); Prüfzeit je Paar (`reports/blindpruefung_iteration4.md`).
7. Report, Evaluator, `/iteration-ende`.

Parallel in Phase 1, nicht Teil des Kriteriums: mindestens 2 Gespräche mit Reinigungsfirmen (A15), dabei auch fragen, ob eine geprüfte
Liste ohne Automatik reicht.

> **Fortschritt 2026-10-25 (Schritt 1, vor dem Regelbau und vor dem Laden der Testdaten):**
> - Population festgelegt in `src/population_iteration4.py`: zusätzlich ausgeschlossen, wenn **alle** Los-Titel einen Ausschlussbegriff
>   enthalten oder der Verfahrenstitel ein Bauprojekt nennt (Umbau, Neubau, Sanierung, Erweiterung, Rohbau, Modernisierung) ohne Hinweis
>   auf wiederkehrende Reinigung. Auf den Entwicklungsdaten: Q2 unverändert 488, Q3 492 → 486 (6 einmalige Reinigungen in
>   Bauprojekten, darunter T16). Beschreibungen (BT-24) fehlen in den Rohdaten und werden nicht geprüft.
> - Testprobe vorab: Seed **20261026**, 70 Fälle, höchstens 2 je Auftraggeber, ohne die 223 Notices aus
>   [bekannte_notices_iteration4.txt](../reports/bekannte_notices_iteration4.txt) (alle Notices mit Jahr 2026 in `reports/` und `docs/`).
> - Rechercheur auf Urteilsregeln 1.1 umgestellt, mit Volltextsuche als Suche C, Herkunft des Vorgänger-Endes und Auftrag
>   „Paarbeurteilung“ ohne Kenntnis der Herkunft (`.claude/agents/rechercheur.md`).
> - Korrekturen zu Iteration 3 als Nachtrag dort (Enddaten, Belegstärke, Originalurteile).

> **Fortschritt 2026-10-25 (Schritt 2, vor der Regelentwicklung):**
> - Volltextsuche `FT` findet auch Bekanntmachungen vor eForms (Probeabfragen `data/raw/ted_probes/20261025/`); die TED-Doku sagt dazu nichts.
> - Neu geladen mit `ted_download.py --los-texte` (Beschreibungen je Los, BT-24/BT-728): Ausschreibungen Q2 und Q3 2026 (gleiche
>   Notices wie zuvor) sowie der Kandidatenpool der eForms-Zeit (Zuschläge und Ausschreibungen CPV 909, 25.10.2023–30.09.2026).
> - Merkmale je Los in `src/los_merkmale.py` (Leistungsart, Flächen, Adressen, Objektnamen); `objekt_merkmale.py` bleibt für die
>   Reproduzierbarkeit von Iteration 3 unverändert.
> - **Festlegung zum Schutz der Testdaten:** Der Kandidatenpool enthält Ausschreibungen aus Q1 2026. Jede Q1-2026-Notice, die bei der
>   Regelentwicklung als Kandidat oder Vorschlag ausgegeben wird, wird automatisch in `reports/dev_gesehene_q1_notices.txt` protokolliert
>   und **nicht als Testfall gezogen**.

> **Fortschritt 2026-10-25 (Schritt 3, Regel eingefroren mit diesem Commit, vor dem Ziehen der Testprobe):**
> Regel `src/zuordnung_los.py` mit `src/los_merkmale.py`, 8 Entwicklungsläufe auf Q3 und 3 auf Q2
> ([regel_entwicklung_iteration4.md](../reports/regel_entwicklung_iteration4.md)). Auf Q3 gegen die Handsuche aus Iteration 3:
> 25 Vorschläge, Präzision 84–100 %, Trefferquote 55,3 %, Top 3 68,4 %. Auf Q2 nach Urteil von Claude etwa 14 von 17 korrekt.
> Beide Werte stammen aus Entwicklungsdaten und sind optimistisch. 20 Q1-2026-Notices als gesehen protokolliert.

> **Fortschritt 2026-10-26 (Schritte 4 und 5):** Testprobe gezogen (e2223ea; Population Q1 2026 = 538, 70 Fälle). Handsuche in 5 Teilen
> nach Urteilsregeln 1.1, je Teil committet, Ground Truth vor dem Regel-Lauf (d43c547). Abweichungen: U21 (Vorgänger nur mit anderem CPV
> gefunden, nach Protokoll „kein Vorgänger“) und U27 (PLZ-Widerspruch) nachgearbeitet; lokale Suchen zählen nicht zum API-Budget
> (Wortlaut der Agentendefinition). Regel auf Testdaten: [zuordnung_iteration4.md](../reports/zuordnung_iteration4.md) (ec4733e).
> **Festlegung W4 (vor dem Urteil des Nutzers):** 20 Paare laut `src/blindpruefung_iteration4.py`, Seed 20261027, je Testfall
> höchstens ein Paar: 6 Vorschläge der Regel, 6 weitere Vorgänger der Handsuche, 4 beste Kandidaten bei „unklar“, 4 erste Kandidaten der
> Regel bei „kein Vorgänger“. Zählweise binär wie Iteration 3; Prüfzeit je Paar in Minuten. Schlüssel lokal in
> `data/processed/blindpruefung_iteration4_schluessel.csv`, SHA-256 `45aff7a4eb2399d0aafd3ff74c330016b858026e89d8f3738df3de966dbe9bcc`.

> **Nachtrag 2026-10-29 (Entscheidung des Nutzers, Kriterien unverändert):** Die parallel geplanten Gespräche mit Reinigungsfirmen
> entfallen, weil das Projekt ohne Kundenkontakt läuft. Sie waren nicht Teil des Kriteriums. Die Folge „Produkt mit manueller
> Prüfung“ bleibt bewertbar über W6 und die Prüfzeit aus W4; ob jemand dafür zahlt (A1, A15), bleibt offen.

**Geprüfte Annahmen:** A9c (Hauptgegenstand); A3 (Wiederholung unter Version 1.1); A12 (Leistungsart auf Los-Ebene); A10, A11 (W5);
A8, A16 (explorativ); A15, A1 (Gespräche, parallel).

**Ergebnis** _(2026-10-30)_

Quellen: **[Z4]** [zuordnung_iteration4.md](../reports/zuordnung_iteration4.md) (Lauf, Commit ec4733e) und
[zuordnung_iteration4_korrektur.md](../reports/zuordnung_iteration4_korrektur.md) (korrigierte Zählung W5 und vorzeitig) ·
**[GT4]** [sichtbarkeit_iteration4_gt.csv](../reports/sichtbarkeit_iteration4_gt.csv) und `sichtbarkeit_iteration4_teil1–5.md` ·
**[PB4]** [paarbeurteilung_iteration4.md](../reports/paarbeurteilung_iteration4.md) · **[BP4]** [blindpruefung_iteration4.md](../reports/blindpruefung_iteration4.md)
· **[RE4]** [regel_entwicklung_iteration4.md](../reports/regel_entwicklung_iteration4.md) · **[E4]** [evaluation_iteration4.md](../reports/evaluation_iteration4.md).

_Fakten_

| Kriterium | Ergebnis | Schwelle | Urteil Evaluator [E4] |
|---|---|---|---|
| W1 Sichtbarkeit | 30/70 = 42,9 % (Wilson 31,9–54,5); 18 objektgleich (alle „mittel“, 0 „hoch“), 12 Teilmenge, 18 unklar (10 eher dafür), 22 kein Vorgänger [GT4] | ≥ 50 % | nicht erfüllt |
| W2 Präzision | 17/19 = 89,5 % (Wilson 68,6–97,1); nur 19 Vorschläge; 3 Vorschläge außerhalb der Handsuche blind beurteilt [Z4], [PB4] | ≥ 80 %, Untergrenze ≥ 60 %, mindestens 25 Vorschläge | formal nicht erfüllt (Mindestzahl), nur Hinweis |
| W3 Trefferquote | 17/30 = 56,7 % (Wilson 39,2–72,6) [Z4] | ≥ 60 % | knapp nicht erfüllt |
| W4 Zweitprüfung | 13/20 = 65 % (Wilson 43,3–81,9; κ ≈ 0,29); Gruppen A 4/6, B 5/6, C 0/4, D 4/4 [BP4], [E4] | ≥ 85 % | nicht erfüllt |
| W5 Backtest-Basis | 11/70 × 1.893 = 297 pro Jahr nach Korrektur (Lauf: 7/70 = 189, Parser zählte „grundlaufzeit, hoechstende“ nicht) [Z4] | ≥ 100 pro Jahr | erfüllt (Punktwert) |
| W6 Kandidatenliste | 22/30 = 73,3 % (Wilson 55,6–85,8) [Z4] | ≥ 70 % | knapp erfüllt, nur Hinweis |

- Explorativ: Prüfzeit Median 2 Minuten je Paar (49 Minuten für 20 Paare) [BP4]. Vorzeitige Neuvergabe 3/30 (U16, U66, U70; im Lauf
  fälschlich mit U20) [Z4]. Vorlaufzeit bis Ende der Grundlaufzeit bei 11 korrekten Paaren −32 bis +26 Monate, Median etwa −6 Monate [Z4].
- Population Q1 2026: 538 Verfahren; Population der letzten 4 Quartale 1.893 (Q4 2025 381, Q1 538, Q2 488, Q3 486) [Z4].
- Die Regel wurde in 8 Läufen auf Q3 (gegen die Handsuche aus Iteration 3) und auf Q2 entwickelt und vor der Testprobe eingefroren [RE4].
- Blindprüfung: Ein erster Satz von 20 Einträgen (P1–P6 ausführlich, P7–P20 ohne Objekte, alle „objektgleich, mittel“, 2 Minuten) wurde
  von Claude nicht übernommen und nicht ausgewertet, weil er nicht nach eigenen Urteilen aussah; ausgewertet sind die danach geschickten
  eigenen Einträge des Nutzers. Lesehilfe: Text der 40 Bekanntmachungen ohne Feldnamen (`src/lesehilfe_blindpruefung_iteration4.py`).
- Mehrere Begründungen in der Blindprüfung stützen sich auf Stufe C, auf die Leistungsart allein oder auf den Zeitbezug (P9) [E4].
- Hash des W4-Schlüssels geprüft: stimmt mit dem vorab festgehaltenen Wert überein.

_Interpretation_

- **Die Hypothese ist nicht bestätigt.** Die Regel ist präzise, wo sie vorschlägt, macht aber zu wenige Vorschläge und findet zu wenige
  Vorgänger. Die Mindestzahl für W2 und die Trefferquote W3 sind verfehlt.
- **W4 misst hier eher die Sorgfalt der Zweitprüfung als die Eindeutigkeit der Definition** [E4]. Die Ground Truth ist damit weder
  bestätigt noch widerlegt. Alle Kennzahlen hängen an einer Handsuche desselben Modelltyps.
- **„Produkt mit manueller Prüfung“ ist nicht belegt:** Die gemessene Prüfung war schnell (2 Minuten), aber nur zu 65 % übereinstimmend.
  Kandidaten ohne Vorgänger wurden zuverlässig verworfen (4/4), „unklar“-Kandidaten durchweg angenommen (0/4).
- **Sichtbarkeit unter strenger Definition um 43 %.** Mit Iteration 3 (63 %) wegen anderer Definition nicht direkt vergleichbar.
- **Das Ende der Grundlaufzeit taugt allein nicht als Prognoseanker** (Vorlaufzeiten streuen über Jahre, Verlängerungen).

**Entscheidung** _(2026-10-30, Entscheidung des Nutzers nach Vorschlag von Claude und Evaluator)_

**Idee anpassen (Phase 1)**, gemäß der vorab festgelegten Folge „W4 < 85 % → W2, W3 und W6 nur Hinweis, kein weiterer Regelversuch“.
Das Ergebnis ist robust: Auch mit den Urteilen des Nutzers für die strittigen Paare bliebe W3 verfehlt [E4].
- Die automatische Zuordnung über das Objekt wird **nicht weiter verbessert** (A9c für die Variante widerlegt).
- **Richtung für Iteration 5:** Vertragsliste aus Zuschlägen (Laufzeitende bei rund 80 % bestimmbar, A4/A13). Die Zuordnung dient nur
  noch als Werkzeug für einen Backtest auf **handgeprüften** Paaren; deren Ground Truth wird vorher unabhängig und mit vorab festgelegter
  Vorlage geprüft. Phase 1 legt vorher das Prognoseziel fest (Ende der Grundlaufzeit oder Höchstende) und benennt die Abdeckung offen
  (etwa 43 % der Ausschreibungen mit sichtbarem Vorgänger).
- Korrekturen als Nachtrag: W5 297 statt 189 pro Jahr, vorzeitig 3/30 statt 4 Fälle; Skript `auswertung_iteration4.py` korrigiert.
- Neue Annahmen A3b, A17, A18; Lücke im Plan (keine Folge für W1 zwischen 30 und 50 %) als Lehre für künftige Kriterien.

---

## Iteration 5: Vertragsliste aus Zuschlägen, erste Prognose und Backtest

**Status:** läuft (angelegt am 2026-10-30)

**Fokus und Phasen:** 1 → 3 → 4 → 5. Entspricht der „ersten Prognose“ im Iterationsplan ([CRISP-DM.md](CRISP-DM.md#iterationsplan)),
angepasst nach der Entscheidung zu Iteration 4: Kern ist eine Vertragsliste aus Zuschlägen. Die Objekt-Zuordnung dient nur noch dazu,
Paare für den Backtest bereitzustellen, die von Hand geprüft werden. Das Prognoseziel wird in Phase 1 festgelegt, bevor gerechnet wird.

**Hypothese** _(vorab festgelegt am 2026-10-30, vor Kenntnis der Ergebnisse)_
„Bei Gebäudereinigungs-Ausschreibungen mit handgeprüftem Vorgänger erscheint die Neuausschreibung in mindestens 60 % der Fälle
innerhalb von ±3 Monaten um das Datum, das die Regel ‚Höchstende des Vorgängers minus 6 Monate‘ vorhersagt. Die Regel trifft damit
häufiger als die naive Referenz ‚Ende der Grundlaufzeit minus 6 Monate‘.“

**Begriffe** _(vorab festgelegt)_
- **Prognoseziel (Entscheidung des Nutzers, 2026-10-30):** Höchstende = Ende des Vorgängervertrags einschließlich aller
  Verlängerungsoptionen. Fehlt eine Verlängerungsangabe, gilt das Ende der Grundlaufzeit.
- **Hauptregel R1:** prognostizierte Neuausschreibung = Höchstende − 6 Monate.
- **Referenz R0** (naive Referenz aus [projektplan.md](projektplan.md), T3.3.4): Ende der Grundlaufzeit − 6 Monate.
- **Treffer:** Die erste Bekanntmachung des neuen Verfahrens (Testfall der Handsuche) ist innerhalb von ±3 Monaten um die
  Prognose veröffentlicht. ±6 Monate werden zusätzlich ausgewiesen, ohne Schwelle.
- **Keine Parameterschätzung aus den Paaren.** R0 und R1 werden in `src/model/baseline.py` eingefroren und committet, bevor sie auf
  die Paare angewendet werden.
- **Rollierende und unbefristete Verträge:** Der Umgang wird in Schritt 1 festgelegt und committet, bevor Prognosen berechnet werden.
- **Backtest-Paare (Entscheidung des Nutzers):** vorhandene Paare der Handsuche aus Iteration 3 (38, Q3 2026) und Iteration 4 (30,
  Q1 2026; davon 23 mit bestimmbarem Ende laut [sichtbarkeit_iteration4_gt.csv](../reports/sichtbarkeit_iteration4_gt.csv)), Kategorie
  objektgleich oder Teilmenge. **Vorbehalt:** Die Vorlaufzeiten eines Teils dieser Paare wurden in Iteration 3 und 4 explorativ angesehen
  (Iteration 4: −32 bis +26 Monate, Median etwa 6 Monate nach der Grundlaufzeit). Das hat die Wahl des Prognoseziels beeinflusst.
- **Zweitprüfung:** Der Nutzer beurteilt alle Paare mit bestimmbarem Vorgänger-Ende nach Urteilsregeln 1.1 mit einer festen Vorlage.
  Die Ansicht zeigt Feldnamen, eine Zeitgrenze gibt es nicht. Prognosen und Vorlaufzeiten sieht er dabei nicht. Die Vorlage wird
  committet, bevor er prüft.
- **Geltungsbereich:** Die Trefferquote gilt nur für Neuausschreibungen, die auf TED erscheinen. Die Präzision (Prognosen ohne
  Nachfolger) wird in dieser Iteration nicht gemessen.

**Erfolgskriterium** _(vorab festgelegt am 2026-10-30)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| X1 Backtest-Basis | Paare, die Rechercheur **und** Nutzer als objektgleich oder Teilmenge bestätigen und deren Vorgänger-Ende (Grundlaufzeit) bestimmbar ist | ≥ 30 | A18, A10, A11 |
| X2 Zweitprüfung | Übereinstimmung zwischen Nutzer und Rechercheur (binär wie W4) über alle geprüften Paare | ≥ 85 % (entscheidet nur über den Status von A18, kein Abbruch) | A18 |
| X3 Trefferquote | Anteil der X1-Paare mit Treffer (±3 Monate) für R1 | ≥ 60 % **und** mindestens 10 Prozentpunkte über R0 auf denselben Paaren | A8, A14 |
| X4 Abdeckung der Liste | Anteil der eForms-Zuschläge (Los-Ebene, Population wie Iteration 4, veröffentlicht Q4 2025 bis Q3 2026), für die R1 ein Datum liefert | ≥ 80 % | A4, A13 |

Explorativ, ohne Schwelle: Anteil vorzeitiger Neuvergaben (A16), Anteil der Vorgänger aus der Zeit vor eForms (A10, A11), Treffer getrennt
nach Herkunft des Endes (Grundlaufzeit, Höchstende) und nach Iteration (Q3 bzw. Q1 2026), Abweichung in Monaten für R0 und R1.

**Was folgt aus welchem Ergebnis**
- X1 < 30 → Backtest nicht aussagekräftig. **Zurück zu Phase 2:** frische Handsuche (z. B. Q4 2025) mit menschlicher Prüfung von Anfang an.
- X1 ≥ 30 und X3 erfüllt → **weiter:** Iteration 6 verbessert die Prognose (Verlängerungen aus dem Freitext, Auftraggeber-Historie).
- X1 ≥ 30 und R1 zwischen 40 und 60 % oder nicht mindestens 10 Prozentpunkte über R0 → **weiter mit Iteration 6, gezielt** auf die
  häufigsten Fehlerursachen ausgerichtet.
- X1 ≥ 30 und R1 < 40 % → **Idee anpassen (Phase 1):** Das Produkt wird eine Vertragsliste mit Enddaten und Zeitfenster, ohne Terminprognose.
- X2 < 85 % → A18 bleibt ungeprüft mit Warnsignal. Der Backtest nutzt nur die von beiden bestätigten Paare (X1), das wird offen ausgewiesen.
- X4 < 80 % → kein Abbruch. Die Abdeckung wird im Prototyp (Iteration 7) offen genannt.

**Zeitrahmen:** 2026-10-31 bis 2026-11-21, etwa 5–7 Arbeitssitzungen. Der Nutzer braucht etwa 3–4 Stunden für die Zweitprüfung,
verteilt auf mehrere Termine.

**Plan**
1. Phase 1: Prognoseziel, Trefferdefinition, Umgang mit rollierenden und unbefristeten Verträgen und die Backtest-Kennzahlen in
   `docs/phasen/01_business_understanding.md` festschreiben und committen.
2. Phase 2: eForms- und TED-Dokumentation prüfen (BT-36, BT-536, BT-537, BT-538, BT-57, BT-58; vor eForms `DATE_END` und Angaben zur
   Verlängerung in F02/F05). Notiz in `docs/phasen/02_data_understanding.md`.
3. Phase 3: Zuschlagstabelle je Los mit Ende der Grundlaufzeit, Höchstende und Herkunft (`src/prepare/vertragsliste.py`,
   `data/processed/`, `reports/vertragsliste_iteration5.md`; X4).
4. Phase 3/5: Backtest-Paare aus der Handsuche von Iteration 3 und 4 zusammenstellen, mit Vorgänger-Ende je Paar (vor eForms über
   `REF_NOTICE`) (`reports/backtest_paare_iteration5.csv`). Prüfvorlage erstellen und committen.
5. Zweitprüfung durch den Nutzer, ohne Prognosen und Vorlaufzeiten (`reports/gt_pruefung_iteration5.md`; X1, X2).
6. Phase 4/5: R0 und R1 in `src/model/baseline.py` einfrieren und committen, dann den Backtest laufen lassen (`reports/backtest_iteration5.md`; X3).
7. Report, Evaluator, `/iteration-ende`.

**Geprüfte Annahmen:** A8 (Hauptgegenstand); A18 (X2); A10, A11 (X1, Herkunft der Vorgänger); A4, A13 (X4, Los-Ebene); A14 (teilweise);
A16 (explorativ).

**Ergebnis:** offen

**Entscheidung:** offen
