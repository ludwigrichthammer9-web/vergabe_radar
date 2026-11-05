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
| 5 | Vertragsliste aus Zuschlägen: Prognoseziel Höchstende, erste Prognose, Backtest auf handgeprüften Paaren | 1 → 3 → 4 → 5 | 2026-10-30 bis 2026-11-04 | abgeschlossen | **Idee anpassen:** R1 28,8 % < 40 % (Schwelle 60 %); Vertragsliste mit Enddaten bleibt Kern, keine Terminprognose |
| 6 | Prototyp der Vertragsliste und Qualität der Enddaten (Iteration 6 und 7 zusammengelegt) | 3 → 6 → 5 | 2026-11-04 (geplant 2026-11-05 bis 2026-11-15) | abgeschlossen | **Zurück zu Phase 3:** Y1 88,3 % nach Korrektur (L60), 90,0 % laut Auswertung, Verankerung und Unabhängigkeit offen; Y2 91,7 %, Y3 79,7 % (knapp verfehlt), Y4 Prototyp erfüllt mit bekannten Fehlern; Regel „Enddatum = Höchstende“ nachbessern, neue Stichprobe |
| 7 | Prototyp der Vertragsliste (statt Kundentest): in Iteration 6 aufgegangen | – | – | entfällt | – |
| 7 (neu) | Lese-Regel „Enddatum = Höchstende“ nachbessern, neue Stichprobe ohne Listenwerte, Prototyp neu erzeugen | 3 → 5 → 6 | 2026-11-04 (geplant 2026-11-05 bis 2026-11-09) | abgeschlossen | **Abschluss mit diesem Stand, kein dritter Regelversuch:** Y1 36/47 = 76,6 % (Kürzung auf L1–L50), Y1r 8/15, Y2 und Y2b verfehlt, Y3 nicht sauber erfüllt, Y4 teilweise; Y1 ist ein Mischmaß aus Listen- und Prüfungsfehlern, Regel 1b weder belegt noch widerlegt; Ende der Grundlaufzeit „laut Bekanntmachung“, Höchstende nur Hinweis |
| 8 | KI-Zweitlesung der Stichprobe von Iteration 7 (zwei KI-Leser, Liste eingefroren, reine Messung) | 5 | 2026-11-04 bis 2026-11-05 | abgeschlossen | **Weiter (Projektabschluss), eingeschränkt formuliert:** Z0 94/95, Z1 77/80, Z3 75/80 und 67/72, Z4 10/10 erfüllt; Z2 14/15, bei einheitlichem Maßstab 11/15 (verfehlt); Leser nicht unabhängig, nicht von Menschen bestätigt |
| 9 | Verbesserte Liste, neue Stichprobe, KI-Lesung ohne die Grenzen der Iteration 8 (Rohtext, Fakten statt Anleitung, eigene Sitzung, menschliche Kontrolle an 15 Losen) | 3 → 5 → 6 | 2026-11-05 bis etwa 2026-11-12 (geplant) | läuft | offen |
| 10+ | Ausbau oder Neuausrichtung | je nach Ergebnis | – | außerhalb des Projekts | – |

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

_Nachtrag 2026-11-04 (Abschluss Iteration 5):_ Nach der Entscheidung „Idee anpassen“ werden die Iterationen 6 und 7 mit `/iteration-start` neu zugeschnitten (Vertragsliste als Prototyp; eine Prognose je Auftraggeber nur, wenn Phase 1 sie begründet).

_Nachtrag 2026-11-04 (Abschluss Iteration 6):_ Nach der Entscheidung „zurück zu Phase 3“ folgt eine weitere Iteration (Lese-Regel nachbessern, neue Stichprobe, Prototyp neu erzeugen); Nummer und Zuschnitt legt `/iteration-start` fest. Die Zeile 7 oben (Prototyp, „entfällt“) bleibt als historischer Stand stehen.

_Nachtrag 2026-11-04 (Abschluss Iteration 7):_ Nach der Entscheidung „Abschluss mit diesem Stand“ wird die Lese-Regel nicht weiter verändert. Als letzte Iteration ist eine reine Messung geplant (KI-Zweitlesung der Stichprobe von Iteration 7 mit eingefrorener Liste); sie ersetzt das Ergebnis von Iteration 7 nicht und wird mit `/iteration-start` angelegt.

_Nachtrag 2026-11-05 (Abschluss Iteration 8):_ Nach der Entscheidung „weiter (Projektabschluss)“ folgt keine weitere Iteration; offene Grenzen kommen ins Lab-Log. Die Zeile „8+“ ist damit gegenstandslos („9+“, außerhalb des Projekts).

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

**Status:** abgeschlossen am 2026-11-04 (angelegt am 2026-10-30)

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

> **Fortschritt 2026-10-30 (Schritte 1 und 2, Kriterien unverändert):** Prognoseziel und Regeln R0/R1 in `docs/business.md` §7.1
> (d36f556; Nutzer hat die Detailregeln gelesen und freigegeben). Dokumentation und Praxis der Laufzeitfelder geprüft
> ([verlaengerung_praxis_iteration5.md](../reports/verlaengerung_praxis_iteration5.md)): BT-537 und `DATE_END` sind in der Praxis das
> Ende der Grundlaufzeit, BT-36 meist auch. Das Höchstende steht nur im Freitext (BT-57/BT-54, vor eForms `RENEWAL_DESCR`), Länge oder
> Datum bei etwa 80 % der verlängerbaren Verträge erkennbar. Folge für Schritt 3: Höchstende aus dem Freitext extrahieren.

> **Fortschritt 2026-10-30 (Schritt 3, Kriterien unverändert):** Zuschlagstabelle je Los ([vertragsliste_iteration5.md](../reports/vertragsliste_iteration5.md)).
> **X4 = 2.924/3.668 = 79,7 %** (Wilson 78,4–81,0), Schwelle 80 % knapp verfehlt; X4 hängt nur an der seit Schritt 1 festen Regel für die
> Grundlaufzeit und wurde nicht nachjustiert. Lese-Regeln für das Höchstende auf 40 Losen entwickelt, vor der Teststichprobe eingefroren
> (a0aa419), Test 53/60 richtig, gewichtet etwa 91 % (Urteile von Claude). Zwei Präzisierungen von §7.1 (spätester Kandidat, Regel 1a)
> in `docs/business.md`. Nach dem Test nur noch die Erkennung der früheren Grundlaufzeit bei Regel 1a ergänzt (betrifft R0, nicht das
> Höchstende). Backtest-Paare wurden dabei nicht angesehen (aus den Stichproben ausgeschlossen).

> **Fortschritt 2026-10-30 (Schritt 4, vor der Zweitprüfung, Kriterien unverändert):** `src/prepare/backtest_paare.py` stellt 68 Paare
> der Handsuche zusammen (Iteration 3: 38, Iteration 4: 30; Vorgänger = jüngster Vorgänger laut GT, T26 laut Korrekturdatei). Vorgänger-Ende
> nur aus dessen Bekanntmachungen (vor eForms über `REF_NOTICE`), Lese-Regeln aus Schritt 3. **61 Paare** haben ein bestimmbares Ende der
> Grundlaufzeit (X1 höchstens 61); 7 ohne (U37: Verteidigungsformular F18 nicht lesbar). 55 der 68 Vorgänger stammen aus der Zeit vor
> eForms; die Lese-Regeln wurden nur an eForms getestet (Schritt 3), bei 17 der 61 bleibt das Höchstende unbestimmbar.
> **Festlegung zur Zweitprüfung (Präzisierung von X2, vor dem Urteil des Nutzers):** Die Vorlage enthält die 61 Paare und 10 Köder-Paare
> (Iteration 4, Kategorie „unklar“, bester Kandidat der Handsuche, ohne in W4 gesehene Testfälle), gemischt mit Seed 20261101. Köder zählen
> wie in W4 als „nicht gefunden“; X2 wird über alle 71 Paare gezählt und zusätzlich getrennt nach echten Paaren und Ködern ausgewiesen.
> Grund: Ohne Köder ergäbe „alles bestätigen“ 100 %. 12 der 71 Paare hat der Nutzer in W4 schon gesehen (wird ausgewiesen).
> Vorlage [gt_pruefung_iteration5.md](../reports/gt_pruefung_iteration5.md), Lesehilfe mit Feldnamen
> [gt_pruefung_iteration5_lesehilfe.md](../reports/gt_pruefung_iteration5_lesehilfe.md). Schlüssel und Vorgänger-Enden lokal in
> `data/processed/` (nicht im Git); Schlüssel `gt_pruefung_iteration5_schluessel.csv`, SHA-256
> `05abddc9a8e450dd2fa9706bfaf06e507740ab3f0fb507d8836c340043df0b8c`.

> **Nachtrag 2026-11-03 (Zweitprüfung, Kriterien unverändert):** Der Nutzer hat P1–P13 ausgefüllt; P11 und P12 sind Kalibrierungsbeispiele
> der Urteilsregeln (nicht beurteilt). Auch P60 und P62 sind identisch mit Kalibrierungsbeispielen (Düsseldorf, Wuppertal), P27, P51 und
> P64 haben dieselbe neue Bekanntmachung wie Stade/Harburg, Esslingen und Saarbrücken (anderer Vorgänger). P11, P12, P60, P62 werden bei
> X1 und X2 nicht gezählt, P27, P51, P64 gezählt und getrennt ausgewiesen. **Die Paare P14–P71 beurteilt ein Kommilitone des Nutzers**
> (nach denselben Regeln); X2 vergleicht damit zwei Prüfer (P1–P13 Nutzer, übrige Kommilitone), das wird ausgewiesen. Abschluss laut
> Nutzer am 2026-11-04. Quellenliste (`docs/quellen.md`) und Reproduzierbarkeitsanleitung (`docs/reproduzierbarkeit.md`) ergänzt.

> **Fortschritt 2026-11-04 (Schritt 5 abgeschlossen, Kriterien unverändert):** Zweitprüfung abgegeben, Schlüssel-Hash geprüft
> (stimmt). Auswertung [gt_pruefung_iteration5_auswertung.md](../reports/gt_pruefung_iteration5_auswertung.md): 4 Paare nicht
> beurteilt (Kalibrierungsbeispiele P11, P12, P60, P62), **X2 = 61/67 = 91,0 %** (Wilson 81,8–95,8, κ 0,70; Schwelle ≥ 85 %),
> **X1 = 52** bestätigte Paare mit bestimmbarem Ende (Schwelle ≥ 30). Vorbehalt: Unabhängigkeit der Prüfung durch den Kommilitonen
> (P14–P71) offen, Minuten fehlen; A18 bleibt „ungeprüft“.

> **Fortschritt 2026-11-04 (Schritt 6, Backtest gelaufen, Kriterien unverändert):** Fachliches Kriterium (Nutzen, Schwelle) in
> `docs/business.md` §7.1 vor dem Lauf festgelegt (f0ee271); `src/model/baseline.py` vor dem ersten Lauf committet (4ab0f36); danach nur
> Zahlenformat im Report geändert, Ergebnis identisch. Report [backtest_iteration5.md](../reports/backtest_iteration5.md):
> **R1 15/52 = 28,8 % (Wilson 18,3–42,3), R0 9/52 = 17,3 %, Abstand +11,5 Prozentpunkte → X3 nicht erfüllt** (Schwelle ≥ 60 %).
> Median-Abweichung R1 +0,6 Monate, aber breit gestreut: 20 Veröffentlichungen mehr als 3 Monate vor, 17 mehr als 3 Monate nach der Prognose.
> Nach der vorab festgelegten Folge („X1 ≥ 30 und R1 < 40 % → Idee anpassen“) bliebe die Vertragsliste ohne Terminprognose; Ergebnis,
> Evaluator und Entscheidung folgen mit `/iteration-ende`.

> **Nachtrag 2026-11-04 (Evaluator und nachträgliche Analysen, explorativ):** Bericht [evaluation_iteration5.md](../reports/evaluation_iteration5.md)
> (X3 robust verfehlt; Zweitprüfung als unabhängige Bestätigung fraglich; „Idee anpassen“ trägt formal). Analysen laut Auflage
> ([backtest_analysen_iteration5.md](../reports/backtest_analysen_iteration5.md), `src/model/analyse_backtest.py`): 12 von 52 Paaren mit
> Veröffentlichung mehr als 24 Monate nach der Prognose (4 weitere mehr als 24 Monate davor); ohne die späten Lücken R1 15/40 = 37,5 %, ohne
> alle Lücken 15/36 = 41,7 %. 40 Auftraggeber für 52 Paare, bei gleicher Gewichtung je Auftraggeber R1 28,5 % (ein Paar je Auftraggeber
> 11/40 = 27,5 %). Keines der Ergebnisse nähert X3 (≥ 60 %).

**Ergebnis** _(2026-11-04)_

Quellen: **[BT5]** [backtest_iteration5.md](../reports/backtest_iteration5.md) · **[E5]** [evaluation_iteration5.md](../reports/evaluation_iteration5.md) ·
**[ZP]** [gt_pruefung_iteration5_auswertung.md](../reports/gt_pruefung_iteration5_auswertung.md) · **[AN]** [backtest_analysen_iteration5.md](../reports/backtest_analysen_iteration5.md) ·
**[VL]** [vertragsliste_iteration5.md](../reports/vertragsliste_iteration5.md) · **[VP]** [verlaengerung_praxis_iteration5.md](../reports/verlaengerung_praxis_iteration5.md) ·
**[HP]** [hoechstende_pruefung_iteration5_test.md](../reports/hoechstende_pruefung_iteration5_test.md).

_Fakten_

| Kriterium | Ergebnis | Schwelle (vorab) | Urteil Evaluator [E5] |
|---|---|---|---|
| X1 Backtest-Basis | 52 bestätigte Paare mit bestimmbarem Ende [ZP] | ≥ 30 | nur formal erfüllt |
| X2 Zweitprüfung | 61/67 = 91,0 % (Wilson 81,8–95,8, κ 0,70); 9/10 Köder erkannt; KI-unterstützt [ZP] | ≥ 85 % | nur formal; blindes Bestätigen = 85,1 % |
| **X3 Trefferquote** | **R1 15/52 = 28,8 % (Wilson 18,3–42,3), R0 9/52 = 17,3 %, Abstand +11,5 Prozentpunkte** [BT5] | **≥ 60 % und ≥ +10 Prozentpunkte** | **nicht erfüllt, robust** |
| X4 Abdeckung | 2.924/3.668 = 79,7 % (Wilson 78,4–81,0) [VL] | ≥ 80 % | nicht erfüllt (knapp), kein Abbruch |
| Fachliches Kriterium | gleiche Schwelle wie X3 (`docs/business.md` §7.1) | ≥ 60 %, +10 Prozentpunkte | nicht erfüllt; belegt keinen Nutzen |

- Veröffentlichung relativ zur R1-Prognose: 20 mehr als 3 Monate früher, 17 später, 15 im Fenster; Median +0,6 Monate (zweigipflig) [BT5].
- Robustheit: ohne unbestimmbare Höchstenden 35,9 %, ohne lange Lücken 41,7 %, ein Paar je Auftraggeber 27,5 %; kein Vorlauf rettet X3 [E5], [AN].
- Das Höchstende hilft, wo der Text ein Datum nennt (7/14 gegenüber 1/14 bei R0) und bei belegter Verlängerung (10/24 gegenüber 4/24); ohne belegte Verlängerung 5/28 für beide [BT5].
- 12 von 52 Paaren mit Veröffentlichung mehr als 24 Monate nach der Prognose (bis 95 Monate) [AN]; 41 von 52 Vorgängern vor eForms [BT5].
- Lese-Regeln Höchstende: Entwicklung 30/40, Test 53/60 (nur eForms-Lose, Claude allein) [HP]. BT-537/DATE_END = Ende der Grundlaufzeit [VP].
- Die Vorab-Festlegung (Hypothese, X1–X4, fachliches Kriterium, R0/R1 und Baseline-Skript vor dem Lauf committet) ist belegt (25f7dd3, f0ee271, 4ab0f36).

_Interpretation_

- **Die Hypothese ist widerlegt.** Die einfache Regel „Höchstende − 6 Monate“ trifft deutlich seltener als vorab verlangt; R1 ist nur besser als R0.
- Die Fehler streuen in beide Richtungen (Optionen werden gezogen oder nicht, Zwischenverträge, nicht direkte Vorgänger); sie lassen sich aus Vorgänger-Daten allein nicht auflösen.
- Die Zweitprüfung bestätigt die Handsuche nicht unabhängig (A18); die Paare messen Objektidentität, nicht den direkten Vorgänger [E5].
- Selektion (Rückwärtssuche, nur auffindbare Vorgänger) und Rechtszensierung verzerren die Quote in unbekannter Richtung; sie ist keine Präzision eines späteren Produkts [E5].
- Dass eine Vertragsliste ohne Terminprognose Nutzen hat, ist nicht belegt (A1, A15) [E5].

**Entscheidung** _(2026-11-04, Entscheidung des Nutzers nach Vorschlag von Claude und Evaluator)_

**Idee anpassen (Phase 1)**, gemäß der vorab festgelegten Folge „X1 ≥ 30 und R1 < 40 % → Idee anpassen“.
- Die Punktprognose „Höchstende − 6 Monate“ wird verworfen (A8 und A14 für diese Variante widerlegt, A10 für die Variante „nur eForms-Vorgänger“).
- **Produktkern:** Vertragsliste mit Enddaten (Ende der Grundlaufzeit, Höchstende, Herkunft; Abdeckung etwa 80 % der Lose) **ohne Terminprognose**.
- Phase 1 bestimmt in Iteration 6, welches Kriterium eine Liste ohne Terminprognose erfüllen soll und ob ein Prognosefenster je Auftraggeber (Optionsausübung) einen zweiten Versuch lohnt.
- A11 und A18 bleiben unverändert (A18: Zweitprüfung KI-unterstützt, nicht unabhängig); A16 bleibt „ungeprüft“ mit verstärktem Warnsignal.
- Offen aus der Evaluation: unabhängige Handprüfung (z. B. 10 Paare ohne Hilfsmittel), Test der Lese-Regeln für Vorgänger vor eForms, Prüfung der langen Lücken auf Zwischenverträge.

---

## Iteration 6: Prototyp der Vertragsliste und Qualität der Enddaten

**Status:** abgeschlossen (angelegt und abgeschlossen am 2026-11-04)

**Fokus und Phasen:** 3 → 6 → 5. Abweichung vom Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan) (dort „Verbesserung der Prognose“) gemäß der
Entscheidung zu Iteration 5: Die Terminprognose ist verworfen, der Produktkern ist die Vertragsliste mit Enddaten. Iteration 6 und 7 (Prototyp)
sind **zusammengelegt** (Entscheidung des Nutzers, 2026-11-04). Die geforderten zwei CRISP-DM-Zyklen sind mit den Iterationen 1 bis 5 erfüllt.

**Hypothese** _(vorab festgelegt am 2026-11-04, vor Kenntnis der Ergebnisse)_
„Eine Vertragsliste aus den eForms-Zuschlägen der Gebäudereinigung nennt in einer unabhängig von Hand geprüften Zufallsstichprobe für mindestens 90 %
der Einträge ein korrektes Ende der Grundlaufzeit und macht beim Höchstende in höchstens 10 % der Fälle eine falsche Angabe. Dabei deckt sie
mindestens 80 % der Lose ab.“

**Begriffe** _(vorab festgelegt)_
- **Liste:** `data/processed/vertragsliste_909.csv` aus `src/prepare/vertragsliste.py` (je Los Ende der Grundlaufzeit, Höchstende, Herkunft). Änderungen an den
  Lese-Regeln zur Abdeckung (Schritt 1) werden committet, **bevor** die Stichprobe gezogen wird.
- **Stichprobe:** 60 zufällige Lose (Seed vor dem Ziehen festgelegt, höchstens 2 Lose je Zuschlag), aus der Liste mit Veröffentlichung Q4 2025 bis Q3 2026; ohne
  die Lose der früheren Stichproben (`reports/hoechstende_pruefung_iteration5_*.md`) und ohne Notices der Handsuche.
- **Korrekt (Y1):** Das Ende der Grundlaufzeit der Liste stimmt (ein Tag Toleranz) mit der Original-Bekanntmachung überein. **Y2:** Das Höchstende ist korrekt oder als
  „unbestimmbar“ gekennzeichnet; „Höchstende = Grundlaufzeit“ wegen „keine Angabe“ zählt als korrekt, wenn der Text keine Verlängerung nennt.
- **Prüfung:** durch den Nutzer (oder den Kommilitonen) **ohne KI-Hilfe**, anhand der Original-Bekanntmachung (TED-Link, Texte BT-57/BT-54/BT-24); Hilfsmittel je Prüfer vermerkt.
- **Abdeckung (Y3):** Anteil der Lose der eForms-Zuschläge (Population wie Iteration 4, veröffentlicht Q4 2025 bis Q3 2026) mit Prognosedatum bzw. Ende der Grundlaufzeit.

**Erfolgskriterium** _(vorab festgelegt am 2026-11-04)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| Y1 | Ende der Grundlaufzeit korrekt (60 Zufallslose) | ≥ 90 % | A4, A13, A11 |
| Y2 | Höchstende korrekt oder als „unbestimmbar“ gekennzeichnet (nie falsch behauptet) | ≥ 90 % | A12 |
| Y3 | Abdeckung der Lose mit Enddatum (Los-Ebene, Q4 2025 bis Q3 2026) | ≥ 80 % | A4, A13 |
| Y4 | Prototyp vorhanden: Liste für eine Region mit Quelle und Unsicherheit je Eintrag | Ja/Nein | – |

Explorativ, ohne Schwelle: Zahl der Lose, deren Grundlaufzeit in den nächsten 12 und 24 Monaten endet; Anteil der 52 Backtest-Paare im **vorab festgelegten**
Beobachtungsfenster „Ende der Grundlaufzeit − 12 Monate bis Höchstende + 12 Monate“ (nur beschreibend, weil die Paare bekannt sind); 10 Paare der Handsuche, die der Prüfer ohne
Hilfsmittel beurteilt (A18); Prüfzeit je Eintrag (A17).

**Was folgt aus welchem Ergebnis**
- Y1 bis Y4 erfüllt → **weiter:** Der Prototyp ist das Ergebnis; danach Lab-Log, Vortrag, Abschluss des Projekts. Eine eigene Iteration 7 entfällt.
- Y1 oder Y2 verfehlt, Y1 ≥ 70 % → **zurück zu Phase 3:** Lese-Regeln nachbessern und eine neue Stichprobe ziehen (ohne Wiederverwendung der geprüften Lose).
- Y1 < 70 % → **Idee anpassen:** Liste nur mit gesicherten Feldern (Grundlaufzeit aus BT-537), Höchstende nur als Hinweis.
- Y3 verfehlt → **kein Abbruch,** die Abdeckung wird im Prototyp offen genannt.
- Y4 nicht erfüllt → Phase 6 wiederholen, bevor die Iteration abgeschlossen wird.

**Zeitrahmen:** 2026-11-05 bis 2026-11-15, etwa 3 bis 4 Arbeitssitzungen; Nutzer etwa 2 Stunden für die Stichprobenprüfung (ohne KI-Hilfe).

**Plan**
1. Phase 3: Abdeckung prüfen und, wenn sinnvoll, Ersatzquellen für fehlende Laufzeiten ergänzen; Regeln vorab committen (`src/prepare/vertragsliste.py`).
2. Phase 5: Stichprobe mit 60 Losen ziehen (Seed vorab) und Prüfvorlage mit TED-Links erzeugen (`reports/liste_pruefung_iteration6.md`).
3. Prüfung durch den Nutzer ohne KI-Hilfe (60 Lose und 10 Paare der Handsuche), Hilfsmittel vermerkt.
4. Auswertung Y1 bis Y3 mit Schlüssel-Hash und Lese-Regeln für Vorgänger vor eForms, soweit in der Stichprobe (`reports/liste_auswertung_iteration6.md`).
5. Phase 6: Prototyp der Liste für eine Region (z. B. Oberpfalz) als Tabelle und Markdown mit Quelle und Unsicherheit je Eintrag (`src/report/`, `reports/beispiel_liste.md`).
6. Selbstbewertung des Prototyps, Evaluator, `/iteration-ende`.

**Geprüfte Annahmen:** A4, A13 (Los-Ebene), A11 (nur soweit in der Stichprobe), A12 (Abgrenzung auf Los-Ebene), A18 (10 Paare ohne Hilfsmittel), A17 (teilweise, Prüfzeit).
A1 und A15 bleiben außerhalb des Projektumfangs (kein Kundenkontakt).

> **Fortschritt 2026-11-04 (Datum korrigiert, zuerst irrtümlich 2026-11-05; Schritt 1, Kriterien Y1–Y4 unverändert, vor dem Ziehen der Stichprobe):** Analyse der 744 Lose ohne Enddatum (Q4 2025 bis Q3 2026):
> 283 mit Dauer, aber ohne Beginn; 364 ohne Beginn und ohne Dauer (28 davon „unbefristet“); 97 mit Beginn, aber ohne Dauer (79 „unbefristet“); 9 unplausibel.
> Um Y3 (≥ 80 %) zu erreichen, fehlen 12 Lose (2.936/3.668); das ginge nur über Schätzungen. **Festlegung:** Y3 und Y1 bleiben strikt (nur Enddatum aus den Feldern bzw.
> Beginn + Dauer), die Abdeckung bleibt bei 79,7 % und Y3 gilt damit voraussichtlich als knapp verfehlt. Für den Prototyp gibt es zusätzlich die Spalte `gl_geschaetzt`
> (Veröffentlichung + Dauer, wenn nur die Dauer vorliegt; 87,4 % der Lose mit Schätzung); sie wird im Prototyp als „geschätzt“ gekennzeichnet und zählt weder für Y1 noch für Y3.
> Grund: Der Beginn liegt meist Monate nach der Veröffentlichung; eine Schätzung würde sonst als geprüftes Enddatum erscheinen. Skript `src/prepare/vertragsliste.py`
> (neue Spalte, bestehende Spalten und X4 unverändert).

> **Fortschritt 2026-11-04 (Datum korrigiert, zuerst irrtümlich 2026-11-05; Schritt 2, Stichprobe gezogen, Kriterien unverändert):** Regeln committet (6baaab5), danach `src/prepare/stichprobe_iteration6.py` mit Seed 20261105:
> 60 Lose aus 59 Zuschlägen (Pool 2.885 Lose) und 10 Paare der Handsuche (aus den 57 gewerteten Paaren der Zweitprüfung Iteration 5). Vorlage
> [liste_pruefung_iteration6.md](../reports/liste_pruefung_iteration6.md); Schlüssel lokal in `data/processed/liste_pruefung_iteration6_schluessel.csv`,
> **SHA-256 `3de3e81270ee2488f8b8b2f60c42d4f7271eb196bfcf7e8aa92809a0ba689d0e`**. Hinweis: Die Auszüge zeigen die Rohfelder (Beginn, Ende, Dauer, BT-58); das kann
> den Prüfer beeinflussen (Verankerung). Er trägt Ende der Grundlaufzeit und Höchstende nach dem Originaltext selbst ein; Hilfsmittel werden vermerkt.

> **Fortschritt 2026-11-04 (Schritte 3 und 4, Kriterien unverändert):** Prüfung abgegeben (PDF `Iteration6_Blindpruefung_TeilA_und_TeilB_vollstaendig.pdf`),
> Einträge in [liste_pruefung_iteration6_urteile.csv](../reports/liste_pruefung_iteration6_urteile.csv) übertragen, Schlüssel-Hash geprüft (stimmt).
> Auswertung [liste_auswertung_iteration6.md](../reports/liste_auswertung_iteration6.md) (`src/prepare/auswertung_iteration6.py`):
> **Y1 = 54/60 = 90,0 %** (Wilson 79,9–95,3; Schwelle ≥ 90 %, genau erreicht), **Y2 = 55/60 = 91,7 %** (Wilson 81,9–96,4). Echte Fehler der Liste: L1, L42, L43
> (Enddatum ist das Höchstende, Regel 1a greift nicht) und L56; drei Auslegungsfälle („unbekannt“ beim Prüfer, L8, L48, L49). Prüfzeit Median 3 Minuten.
> **Vorbehalte:** (1) Das Feld „Hilfsmittel“ ist in allen 60 Einträgen leer; ob Teil A ohne KI-Hilfe entstand, ist nicht vermerkt. (2) **Teil B (10 Paare) ist nicht
> unabhängig:** Urteil, Sicherheit und Begründung aller 10 Paare stimmen wörtlich mit der KI-unterstützten Zweitprüfung von Iteration 5 überein (P55, P14, P16, P21, P29,
> P1, P53, P34, P4, P30); Teil B zählt nicht als Prüfung ohne Hilfsmittel (A18 unverändert). Klärung beim Nutzer offen.

> **Fortschritt 2026-11-04 (Schritt 5, Prototyp, Kriterien unverändert):** [beispiel_liste.md](../reports/beispiel_liste.md) und
> [beispiel_liste_oberpfalz.csv](../reports/beispiel_liste_oberpfalz.csv) aus `src/report/beispiel_liste.py`: Oberpfalz (NUTS DE23), Stichtag 04.11.2026,
> **146 Lose** aus 67 Zuschlägen (70 im Abruf vom 23.10.2026, 3 durch die Population ausgeschlossen); je Eintrag TED-Link, Herkunft von Grundlaufzeit und
> Höchstende sowie eine Unsicherheitsstufe A–F. 108 Lose (74,0 %) mit Ende der Grundlaufzeit aus den Feldern, 5 nur geschätzt, 33 ohne Ende.
> Fakten zur Umsetzung: Region je Los bei 9 Bekanntmachungen erst über das eForms-XML zuordenbar (die Such-API liefert die NUTS-Codes als flache Liste);
> XML unverändert in `data/raw/ted_xml/beispiel_liste_20261104/` (Adresse aus dem Feld `links` der API-Antwort). `auswertung_iteration6.py` nur umgebaut
> (Funktion `bewertung`), Bericht unverändert.
> **Interpretation/Vorbehalt:** Die Stufen und ihre Quoten (A 19/19, B 13/16, C 13/16, D 9/9 beim Ende der Grundlaufzeit) sind **nach** Kenntnis der
> Prüfergebnisse eingeteilt und beruhen auf der bundesweiten Stichprobe, nicht auf der Oberpfalz; kein Eintrag der Oberpfalz wurde geprüft. Y4 aus eigener Sicht
> erfüllt; Selbstbewertung und Evaluator stehen aus (Schritt 6).

> **Fortschritt 2026-11-04 (Abschluss, Nachträge und Korrekturen; frühere Einträge bleiben stehen):**
> - Evaluator-Bericht: [evaluation_iteration6.md](../reports/evaluation_iteration6.md). Das Abgabe-PDF liegt jetzt im Repo ([liste_pruefung_iteration6_abgabe.pdf](../reports/liste_pruefung_iteration6_abgabe.pdf));
>   alle 60 Einträge der Urteils-CSV stimmen mit dem PDF überein (Übertragung geprüft).
> - **Angaben des Nutzers:** Teil A (60 Lose) ohne KI-Hilfe geprüft (mündlich; im Feld „Hilfsmittel“ nicht vermerkt, die beiden Vorbehalte (1) bleiben deshalb als „nicht belegt“ stehen).
>   Teil B aus der Zweitprüfung Iteration 5 übernommen, weil es dieselben Paare waren; **Ursache war mein Aufbau in Schritt 2** (die 10 Paare wurden aus den 57 schon bekannten Paaren gezogen).
>   Prüfzeit: „Habe davor schon gearbeitet, aber nicht durchgängig“ (auf die Frage nach Arbeit vor dem Commit um 13:07); die 163 Minuten sind eine Selbstangabe.
> - **Korrektur zu Schritt 5:** „Kein Eintrag der Oberpfalz wurde geprüft“ war falsch; L6 (617709-2026, Los 3) steht in der Liste. `beispiel_liste.md` nennt das jetzt.
> - **Korrektur zu Schritt 1:** Bis 80 % fehlen 11 Lose (2.935/3.668), nicht 12.
> - **Korrektur zu Schritt 4 (Evaluator, nachgeprüft):** L60 (392720-2026) ist ein Fehler der Liste und des Prüfers: Der Text nennt „zwei Jahre … (2+1+1)“, die Grundlaufzeit endet am 30.06.2028,
>   nicht am 30.06.2030. Y1 = **53/60 = 88,3 %** (Wilson 77,8–94,2). Die Auswertung `liste_auswertung_iteration6.md` bleibt unverändert (54/60 laut Prüfereintrag); die Korrektur gilt nur im Prototyp und hier.
>   Die Deutungen zu L43 und L56 in der Auswertung sind durch die Stichprobe nicht gedeckt (L43: das Feld 14.08.2028 ist weder Grundlaufzeit noch Höchstende; L56: Verlängerung im Originaltext laut Evaluator nicht auffindbar, Abruf über Zusammenfassung).
> - Explorativ (Skript im Repo, [explorativ_iteration6.md](../reports/explorativ_iteration6.md)): bundesweit 1.368 Lose mit Ende der Grundlaufzeit in den nächsten 12 Monaten und 3.024 in 24 Monaten;
>   32/52 Backtest-Paare im Fenster „Ende GL − 12 Monate bis Höchstende + 12 Monate“ (für unbestimmbare Höchstenden Obergrenze GL + 12 Monate, **nicht vorab festgelegt**; nur beschreibend).
>   Prüfzeit-Median 2,5 Minuten (nicht 3; das Skript nimmt den oberen Median).

**Ergebnis** _(2026-11-04, nach Evaluator)_

_Fakten_

| Kriterium | Ergebnis | Schwelle | Urteil |
|---|---|---|---|
| Y1 Ende der Grundlaufzeit | 54/60 = 90,0 % (Wilson 79,9–95,3) laut Auswertung [LA]; **53/60 = 88,3 %** (Wilson 77,8–94,2) nach dem Fehler L60 [E6] | ≥ 90 % | **verfehlt** nach Korrektur; auch ohne Korrektur nur genau auf der Schwelle |
| Y2 Höchstende korrekt oder „unbestimmbar“ | 55/60 = 91,7 % (Wilson 81,9–96,4) [LA]; nur auf die 51 Lose bezogen, bei denen die Liste ein Höchstende nennt: 46/51 = 90,2 % [E6] | ≥ 90 % | formal erfüllt, wenig Spielraum |
| Y3 Abdeckung | 2.924/3.668 = 79,7 % (Wilson 78,4–81,0) [VL] | ≥ 80 % | verfehlt (knapp), vorab: kein Abbruch |
| Y4 Prototyp | [beispiel_liste.md](../reports/beispiel_liste.md): Oberpfalz, 146 Lose, je Eintrag TED-Link, Herkunft, Status, Stufe A–F [BL] | Ja/Nein | erfüllt; die Liste enthält bekannte Fehler |

- Prüfung: 60 Lose, Prüfer ohne KI-Hilfe laut eigener Angabe (Feld „Hilfsmittel“ leer), Prüfzeit Median 2,5 Minuten, Summe 163 Minuten (Selbstangabe) [LA], [E6].
- Die Vorlage zeigte das Enddatum der Liste; bei 59 von 60 Losen stammt das Ende der Grundlaufzeit der Liste aus diesem Feld (`gl_herkunft = enddatum`) [E6].
- Fehler der Liste beim Ende der Grundlaufzeit: L1, L42, L43, L60 (Enddatum der Bekanntmachung ist schon das Höchstende) und drei Auslegungsfälle (L8, L48, L49, „unbekannt“ beim Prüfer). L56: Prüfer und Liste nennen 31.12.2028 als Ende, der Prüfer als Höchstende 31.12.2030; die Liste „keine Angabe“ [LA], [E6].
- Teil B (10 Paare) wörtlich identisch mit der KI-unterstützten Zweitprüfung Iteration 5; zählt nicht für A18 [LA], Antwort des Nutzers.
- Hypothese und Kriterien blieben seit 6baaab5 unverändert (Diff geprüft, [E6] Abschnitt 7). Die Stichprobe wurde nach den Regeln vom 13:07 gezogen; der Seed wurde im selben Commit festgehalten wie die Stichprobe.
- In der Stichprobe liegen 0 Lose vor eForms (A11 nicht geprüft); je Zuschlag höchstens 2 Lose, große Bekanntmachungen sind untergewichtet (z. B. 143100-2026 mit mehr als 56 Losen).
- Prototyp: bei 143100-2026 stehen in der Oberpfalz-Liste die Lose 8, 9 und 14 mit Enddatum ein Jahr nach der laut Text festen Laufzeit (Stufe B) [E6].
- Quellen: [LA] [liste_auswertung_iteration6.md](../reports/liste_auswertung_iteration6.md) · [VL] [vertragsliste_iteration5.md](../reports/vertragsliste_iteration5.md) · [BL] [beispiel_liste.md](../reports/beispiel_liste.md) · [E6] [evaluation_iteration6.md](../reports/evaluation_iteration6.md).

_Interpretation_

- **Die Hypothese ist nicht bestätigt.** Y1 liegt nach der Korrektur unter der Schwelle; ohne Korrektur liegt es genau darauf und ist wegen der Verankerung (Vorlage zeigt das Enddatum der Liste) und der offenen Unabhängigkeit kaum aussagekräftig. Die Quote ist eher eine Untergrenze der Fehler als eine Genauigkeit.
- **Fehlertyp „Enddatum der Bekanntmachung = Höchstende“:** Er tritt bei L1, L42, L43 und L60 auf und in der Bekanntmachung 143100-2026 vermutlich in allen Losen. Regel 1a erkennt nur „spätestens“, „längstens“ und „inkl. Verlängerungen“; Formulierungen wie „Festlaufzeit von … bis …“, „2+1+1“, „Laufzeit von 2 Jahren“, „erste feste Laufzeit bis …“ und „zunächst für die Dauer von …“ ohne Datum greifen nicht. Das ist der Ansatz für Phase 3.
- Dass Y2 erreicht wird, liegt zu einem guten Teil an der Kategorie „unbestimmbar“ (9 von 60 Einträgen, bei 8 davon gab der Prüfer ein Datum an): Die Liste ist dort vorsichtig, aber nicht informativ.
- Y3 bringt keine neue Messung; ein Ersatzweg über „Veröffentlichung + Dauer“ erreicht 87,4 %, zählt aber nicht und ist ungenau.
- Die Unsicherheitsstufen im Prototyp (nach Kenntnis der Prüfergebnisse eingeteilt, kleine Zahlen je Stufe) helfen beim Lesen, ersetzen aber keine Prüfung.
- Dass eine Vertragsliste ohne Terminprognose Nutzen hat, ist weiter nicht belegt (A1, A15, außerhalb des Projektumfangs).

**Entscheidung** _(2026-11-04, Entscheidung des Nutzers nach Vorschlag von Claude und Evaluator)_

**Zurück zu Phase 3.** Gemäß der vorab festgelegten Folge „Y1 oder Y2 verfehlt, Y1 ≥ 70 % → zurück zu Phase 3: Lese-Regeln nachbessern und eine neue Stichprobe ziehen (ohne Wiederverwendung der geprüften Lose)“.
- Die Lese-Regel für „Enddatum = Höchstende“ wird um die oben genannten Formulierungen erweitert und **vor dem Ziehen** der neuen Stichprobe committet.
- Die neue Stichprobe (60 Lose, ohne die geprüften Lose und ohne Notices der früheren Stichproben) wird mit festem Seed gezogen, der **vor** dem Ziehen committet wird. Die Vorlage zeigt **keine** Felder der Liste (Beginn, Ende, Dauer, BT-58), nur den Originaltext und den TED-Link; die Hilfsmittel werden je Eintrag vermerkt. Die Stichprobe berücksichtigt große Bekanntmachungen (z. B. Gewichtung oder getrennte Auswertung).
- Teil B (A18) wird nur mit Paaren wiederholt, die der Prüfer noch **nicht** gesehen hat, oder entfällt.
- Der Prototyp wird nach den neuen Regeln neu erzeugt; bekannte Fehler (143100-2026) verschwinden dadurch oder werden gekennzeichnet.
- A4, A11, A12, A13, A17, A18: Status unverändert, Nachweise ergänzt (siehe `docs/annahmen.md`); A1 und A15 bleiben außerhalb des Projektumfangs.
- Die Nummerierung der Folge-Iteration (Iteration 7, Phase 3 → 5) legt `/iteration-start` fest.

---

## Iteration 7 (neu): Lese-Regel „Enddatum = Höchstende“ nachbessern und Vertragsliste neu prüfen

**Status:** abgeschlossen am 2026-11-04 (angelegt am 2026-11-04)

**Fokus und Phasen:** 3 → 5 → 6. Abweichung vom Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan) („7+ Ausbau“): Rücksprung gemäß der Entscheidung zu Iteration 6
(„zurück zu Phase 3“, vorab festgelegte Folge). Die Zeile „7“ in der Übersicht (Prototyp, entfällt) bleibt als historischer Stand stehen.
LN B (Zweierteam, Entscheidung des Nutzers 2026-11-04); die Moodle-Frist ist nicht bekannt, der Zeitrahmen ist deshalb knapp gehalten.

**Hypothese** _(vorab festgelegt am 2026-11-04, vor Kenntnis der Ergebnisse)_
„Mit einer erweiterten Lese-Regel, die ein Enddatum als Höchstende erkennt, wenn der Text eine kürzere feste Laufzeit nennt, stimmt das Ende der Grundlaufzeit der
Vertragsliste in einer neuen, nicht gesehenen Zufallsstichprobe bei mindestens 90 % der Lose. Geprüft wird ohne Listenwerte in der Vorlage und ohne KI-Hilfe.“

**Begriffe** _(vorab festgelegt)_
- **Regel-Erweiterung:** Regel 1a in `src/prepare/vertragsliste.py` erkennt zusätzlich Formulierungen wie „Festlaufzeit von … bis …“, „2+1+1“ bzw. „zwei Jahre mit Option …“,
  „Laufzeit von X Jahren“, „erste feste Laufzeit bis …“ und „zunächst für die Dauer von …“ ohne Datum. Die Muster und die Stufen A–F für den Prototyp werden in Schritt 1 festgelegt und
  **committet, bevor die Stichprobe gezogen wird.** Entwicklungstest (zählt nicht): L1, L42, L43, L60 der Iteration 6.
- **Stichprobe:** 80 zufällige Lose aus `data/processed/vertragsliste_909.csv` (Veröffentlichung Q4 2025 bis Q3 2026, Ende der Grundlaufzeit vorhanden), höchstens 2 Lose je Zuschlag.
  Ausgeschlossen: die 60 Lose der Iteration-6-Prüfung, die Lose der Stichproben aus Iteration 5 (`reports/hoechstende_pruefung_iteration5_*.md`), die Notices der Handsuche und die
  Bekanntmachungen der vier Entwicklungsfehler (143100-2026, 448962-2026, 418442-2026, 392720-2026). Der Seed wird **vor dem Ziehen** committet.
- **Regelwirkung (beschreibend, ohne Schwelle):** bis zu 15 weitere Lose, bei denen die neue Regel das Ende der Grundlaufzeit gegenüber der Fassung der Iteration 6 (Commit c6c8c32) ändert;
  Prüfung wie die Stichprobe. Sie gehören nicht zu Y1 bis Y2b.
- **Prüfung:** durch den Nutzer **ohne KI-Hilfe** anhand der Original-Bekanntmachung (TED-Link). Die Vorlage zeigt Los-Titel, TED-Link und die Originaltexte BT-57, BT-54, BT-24, **nicht** die
  Felder Beginn, Ende, Dauer und BT-58 und nicht die Werte der Liste. Je Eintrag: Ende der Grundlaufzeit, Höchstende, **Quelle** (Text oder Feld der Bekanntmachung), Hilfsmittel (Pflicht,
  auch „keine“), Minuten sowie Start- und Endzeit je Sitzung. Nennt nur das Feld der Bekanntmachung ein Ende und der Text nichts, trägt der Prüfer dieses Ende mit Quelle „Feld“ ein;
  „unbekannt“ nur, wenn weder Text noch Feld ein Ende nennen (Klarstellung nach den Auslegungsfällen L8, L48, L49 der Iteration 6). Das ausgefüllte PDF und die CSV kommen mit Hash ins Repo.
- **Korrekt (Y1):** Das Ende der Grundlaufzeit der Liste stimmt (ein Tag Toleranz) mit dem Eintrag des Prüfers überein. **Y2:** Höchstende korrekt oder als „unbestimmbar“ gekennzeichnet;
  „Höchstende = Grundlaufzeit“ zählt als korrekt, wenn der Prüfer „keine Verlängerung“ oder „keine Angabe“ einträgt. **Y2b:** wie Y2, aber nur für Lose, bei denen die Liste ein Höchstende nennt.
- **Gewichtet (beschreibend):** Y1 nach Losen gewichtet (Gewicht = Lose des Zuschlags ÷ gezogene Lose desselben Zuschlags).

**Erfolgskriterium** _(vorab festgelegt am 2026-11-04)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| Y1 | Ende der Grundlaufzeit korrekt (80 Zufallslose) | ≥ 72/80 = 90 % (untere Wilson-Grenze dann etwa 81 %) | A4, A13 |
| Y2 | Höchstende korrekt oder „unbestimmbar“ (80 Zufallslose) | ≥ 90 % | A12 |
| Y2b | Höchstende korrekt, nur Lose mit behauptetem Höchstende | ≥ 85 % | A12 |
| Y3 | Verfahren eingehalten: Regel und Seed vor dem Ziehen committet, Vorlage ohne Listenwerte, Hilfsmittel je Eintrag vermerkt | Ja/Nein | A17 |
| Y4 | Prototyp neu erzeugt, die Fehler in 143100-2026 (Lose 8, 9, 14 der Oberpfalz-Liste) behoben, Stufen vorab definiert | Ja/Nein | – |

Die Abdeckung (79,7 %) ändert sich durch die Regel nicht und ist kein Kriterium; sie wird im Prototyp offen genannt.
Beschreibend, ohne Schwelle: Y1 nach Losen gewichtet; Y1 nur für Lose, bei denen der Text etwas zur Laufzeit sagt (Quelle „Text“); Prüfzeit je Los; Regelwirkung an den bis zu 15 geänderten Losen.

**Was folgt aus welchem Ergebnis**
- Y1 bis Y4 erfüllt → **weiter:** Der neu erzeugte Prototyp ist das Ergebnis; danach Lab-Log, Vortrag, Abschluss des Projekts.
- Y1 zwischen 70 % und 90 % → **kein dritter Regelversuch:** Die Liste führt das Ende der Grundlaufzeit als „laut Bekanntmachung“, die Fehlerquote wird offen genannt, das Projekt wird mit diesem Stand abgeschlossen.
- Y1 < 70 % → **Idee anpassen:** Liste nur mit gesicherten Feldern, das Ende der Grundlaufzeit nur als Hinweis.
- Y1 erfüllt, Y2 oder Y2b verfehlt → Höchstende nur als Hinweis kennzeichnen.
- Y3 oder Y4 nicht erfüllt → den Schritt wiederholen, bevor die Iteration abgeschlossen wird.

**Zeitrahmen:** 2026-11-05 bis 2026-11-09, etwa 3 bis 4 Arbeitssitzungen; Nutzer etwa 5 bis 6 Stunden für die Prüfung der 80 Lose und etwa 40 Minuten für die Regelwirkungs-Lose (ohne KI-Hilfe).

**Plan**
1. Phase 3: Regel 1a erweitern, Stufen A–F für den Prototyp festlegen, Entwicklungstest an L1, L42, L43, L60; Regeländerung committen (`src/prepare/vertragsliste.py`).
2. Phase 3/5: Seed committen, danach 80 Lose und bis zu 15 Regelwirkungs-Lose ziehen; Vorlage ohne Listenwerte; Schlüssel lokal, SHA-256 von Schlüssel und Vorlage im Commit (`src/prepare/stichprobe_iteration7.py`, `reports/liste_pruefung_iteration7.md`).
3. Prüfung durch den Nutzer ohne KI-Hilfe mit Quelle, Hilfsmittel und Zeitprotokoll je Eintrag; PDF und CSV ins Repo.
4. Phase 5: Auswertung Y1, Y2, Y2b und beschreibende Kennzahlen (`src/prepare/auswertung_iteration7.py`, `reports/liste_auswertung_iteration7.md`).
5. Phase 6: Prototyp der Oberpfalz-Liste mit den neuen Regeln und den vorab definierten Stufen neu erzeugen (`src/report/beispiel_liste.py`).
6. Selbstbewertung, Evaluator, `docs/ki_irrwege.md` ergänzen (Aufbaufehler in Teil B der Iteration 6, verankerte Vorlage, falsche Aussage zu L6), `/iteration-ende`.

**Geprüfte Annahmen:** A4, A13 (Los-Ebene, Enddatum = Grundlaufzeit?), A12 (nur Hinweis), A17 (Prüfzeit mit Zeitprotokoll).
A11 bleibt ungeprüft (auch diese Stichprobe enthält nur eForms-Lose). **A18 wird in dieser Iteration nicht geprüft** (die Paare gehören zum verworfenen Backtest; ein weiterer Test hätte nur mit Paaren Sinn, die der Prüfer noch nicht kennt); A18 bleibt als offene Grenze stehen.
A1 und A15 bleiben außerhalb des Projektumfangs (kein Kundenkontakt).

> **Fortschritt 2026-11-04 (Schritt 1, Regel 1b erweitert; Kriterien unverändert, vor dem Ziehen der Stichprobe):** Regel 1b in `src/prepare/vertragsliste.py` (`kurze_festlaufzeit`, Beschreibung im Kopf des Skripts).
> Zwei Fälle: (a) Datum der festen Laufzeit im Text („Festlaufzeit von … bis …“, „erste feste Laufzeit bis …“, „zunächst … bis“) mehr als 20 Tage vor dem Enddatum; (b) feste Dauer im Text („Vertragsdauer beträgt zwei Jahre“, „Laufzeit von 2 Jahren“, „(2+1+1)“),
> Beginn + Dauer mehr als 31 Tage vor dem Enddatum und das Enddatum passt (± 31 Tage) zu Anzahl × Länge, Höchstlaufzeit, BT-36 oder der Summe. Beide nur bei Verlängerung/Option im Text; erklärt eine genannte Dauer das Enddatum schon, greift die Regel nicht.
> Entwicklungstest `src/prepare/entwicklungstest_iteration7.py` (zählt nicht): An den 60 Losen der Iteration 6 (Eingaben der Vorlage, Soll = Prüfer, L60 korrigiert) werden genau L1, L42, L43, L60 richtig, die übrigen 56 bleiben unverändert.
> Die erste Fassung machte L6, L14 und L46 falsch (Kündigungsfristen als Dauer gelesen, Datum im Text als Beleg) und wurde deshalb eingeschränkt (Dauer ≥ 12 Monate, keine Fristen, Datum im Text zählt nicht als Beleg, kein Eingreifen bei erklärter Dauer).
> Wirkung auf die Liste: 165 von 9.915 Losen ändern das Ende der Grundlaufzeit (43 Herkunft „text_laufzeit_option“, 122 „text_festlaufzeit“), 107 davon in der Bekanntmachung 143100-2026; 28 Bekanntmachungen betroffen.
> Beim Entwickeln habe ich etwa 20 Bekanntmachungen einzeln angesehen (`reports/entwicklung_iteration7_notices.txt`); sie bleiben aus der Stichprobe und der Regelwirkungs-Stichprobe ausgeschlossen. Stufen A–F für den Prototyp sind in `src/report/beispiel_liste.py` (`stufe`) festgelegt:
> Ende der Grundlaufzeit aus dem Text berichtigt → A; sonst nach Herkunft des Höchstendes (Anzahl × Länge → B, keine Angabe → C, unbestimmbar → D, übrige → A); ohne Ende E (nur geschätzt) oder F.
> **Interpretation/Vorbehalt:** Die Regel ist bewusst eng; Fehler außerhalb dieses Musters (z. B. L56 mit Verlängerung nur im Volltext) fängt sie nicht. Bei 412612-2025 trifft sie das Richtige teils zufällig (Länge der Verlängerung als Dauer gelesen, vom Konsistenztest abgesichert). Ob sie neue Fehler erzeugt, zeigt erst die Prüfung.

> **Fortschritt 2026-11-04 (Schritt 2, Stichprobe gezogen; vor der Prüfung):** Seed 20261106 und Skript `src/prepare/stichprobe_iteration7.py` wurden **vor dem Ziehen** committet (c7fb0c0).
> Gezogen: 80 Lose aus 76 Zuschlägen (Pool 2.527 Lose aus 1.218 Zuschlägen) und 15 Regelwirkungs-Lose aus 9 Zuschlägen (Pool 15, alle genommen), gemischt und nummeriert als L1 bis L95.
> Vorlage [liste_pruefung_iteration7.md](../reports/liste_pruefung_iteration7.md) (ohne Listenwerte, kein Feld zu Beginn/Ende/Dauer/BT-58; geprüft); Schlüssel lokal, **SHA-256 `eade66c033ab13d541dda2f7af3f5b074f1b5a4587e711f6a29e0ba1916ddf9b`**;
> SHA-256 der Vorlage `3ec40816384384f350dda99607d5e4763f543b93de73dbc5160c7eed84edc85c`.
> **Befund zur Zusammensetzung:** Regel 1b ändert im Fenster Q4 2025 bis Q3 2026 128 von 2.924 Losen (12 Bekanntmachungen). Die Hauptstichprobe enthält davon **kein einziges** (fast alle stecken in den ausgeschlossenen Entwicklungs- und angesehenen
> Bekanntmachungen). Die 15 Regelwirkungs-Lose sind alle von der Herkunft „text_laufzeit_option“; der Typ „text_festlaufzeit“ (z. B. 143100-2026) ist nur durch die Entwicklungslose L1 und L43 belegt und bleibt **ungetestet**.
> **Folge, vor der Prüfung festgelegt (Ergänzung der Kriterien, keine Änderung von Y1 bis Y4; ohne Kenntnis der Ergebnisse):** Y1, Y2 und Y2b messen die Liste für Lose, die die Regel nicht ändert, plus die Fehler, die die Regel nicht erkennt; sie belegen die Regel selbst nicht.
> Neu: **Y1r (Regelwirkung):** mindestens 12/15 der Regelwirkungs-Lose haben ein korrektes Ende der Grundlaufzeit (nur Typ „text_laufzeit_option“). Beschreibend: Gesamtschätzung für das Fenster = (128 · a_R + 2.796 · a_Y) / 2.924 mit a_R aus den 15 und a_Y aus den 80 Losen.
> „Weiter“ gilt nur, wenn Y1, Y1r, Y2, Y2b, Y3 und Y4 erfüllt sind; bei verfehltem Y1r gilt die Folge „Y1 zwischen 70 % und 90 %“ (Ende der Grundlaufzeit bei Losen mit Herkunft Regel 1b als „laut Bekanntmachung“ kennzeichnen, kein dritter Regelversuch).
> Der Typ „text_festlaufzeit“ wird im Abschluss als ungetestet benannt.

> **Fortschritt 2026-11-04 (Schritt 3/4, Prüfung abgegeben und ausgewertet; Gültigkeit offen):** Der Nutzer gab die ausgefüllte Datei (95 Lose, Summe 137 Minuten, Median 1 Minute je Los, Hilfsmittel: 81 × „keine“, 14 × „Kalender“) zurück.
> Einträge nach `reports/liste_pruefung_iteration7_urteile.csv` übertragen; Schlüssel-Hash vor dem Öffnen geprüft (eade66c0…df9b). Auswertung: `reports/liste_auswertung_iteration7.md`.
> **Rohwerte nach den vorab festgelegten Regeln:** Y1 20/80 = 25,0 %, Y1r 10/15, Y2 52/80 = 65,0 %, Y2b 44/72 = 61,1 %. **Alle 65 Abweichungen bei Y1 sind Einträge „unbekannt“; bei den 30 Datumsangaben des Prüfers gibt es keine einzige Abweichung.**
> Die Quelle „Feld“ wurde nie vergeben, 60 der „unbekannt“-Einträge betreffen Lose mit Enddatum aus den Feldern (BT-537 bzw. Beginn + Dauer), die die Vorlage absichtlich nicht zeigt. Die Prüfzeit passt zu einem Lesen der Auszüge ohne Öffnen der TED-Originale.
> In der abgegebenen Datei steht bei jedem Los eine Zeile „XML-Felder: Start=- | Ende(BT-537)=- | Dauer(BT-36)=-“, die weder in der Vorlage (SHA-256 3ec40816…) noch im Skript vorkommt; die Sitzungstabelle fehlt. Herkunft der Zeile ist zu klären (betrifft Y3, Verfahren).
> **Interpretation (vorläufig):** Die Rohwerte messen hier vor allem, ob die Laufzeit im Auszug steht, nicht die Genauigkeit der Liste. Echte Fehler mit Datum bei Y2: L72 (Liste 31.08.2037, Prüfer 31.08.2031) und L82 (Liste 31.10.2029, Prüfer 31.10.2030).
> Entscheidung über die Folge (Y1 verfehlt → „zwischen 70 % und 90 %“ bzw. „< 70 %“) erst nach Klärung, ob die 65 Lose im Original nachgeprüft werden.

> **Nachtrag 2026-11-04 (zweite Abgabe ersetzt die erste):** Der Nutzer teilte mit, die erste Datei sei eine unfertige Version gewesen, und gab eine zweite Datei ab (ohne die Zeile „XML-Felder“, im Format der Vorlage; damit ist die offene Frage zur Zeile erledigt).
> Die erste Abgabe bleibt als `reports/liste_pruefung_iteration7_urteile_abgabe1.csv` erhalten (Auswertung im Commit d684471); maßgeblich ist `reports/liste_pruefung_iteration7_urteile.csv`. Die Sitzungstabelle fehlt auch in der zweiten Datei.
> **Rohwerte der zweiten Abgabe:** Y1 19/80 = 23,8 %, Y1r 8/15, Y2 51/80 = 63,8 %, Y2b 43/72 = 59,7 %; Summe 143 Minuten, Median 1 Minute. Quelle: 28 × „Text“, 67 × „unbekannt“, nie „Feld“; Hilfsmittel 79 × „keine“, 16 × „Kalenderberechnung“.
> Wieder keine einzige Datumsabweichung (27 Datumsangaben), alle Abweichungen bei Y1 sind „unbekannt“; bei Quelle „Text“ stimmt die Liste in 19 von 20 Fällen der Hauptstichprobe (Wilson 76,4–99,1). Echte Y2-Fehler mit Datum: L72, L82. Die Einordnung der ersten Abgabe gilt unverändert.

> **Nachprüfung (Schritt 3b, vor dem Ausfüllen festgelegt):** Für die 68 Lose mit „unbekannt“ erzeugt `src/prepare/nachpruefung_iteration7.py` eine verkürzte Vorlage `reports/liste_nachpruefung_iteration7.md` (SHA-256 `129c22afa0a65d80892c7150b6963854916f381966a3e0ab84a5e93bedf9dcac`), nur mit Link und Los-Titel, ohne Listenwerte.
> Der Prüfer öffnet das TED-Original und trägt Beginn/Ende/Dauer der Felder, Ende der Grundlaufzeit, Quelle, Hilfsmittel und Minuten ein. Kriterien und Schwellen bleiben unverändert; für Lose mit Nachprüfung zählt der Nachprüfungs-Eintrag, die erste Abgabe bleibt als Rohwert dokumentiert.
> Ich (Claude) kenne die Listenwerte; die Eingaben des Prüfers werden nicht durch mich ergänzt oder korrigiert.
> **Kürzung der Nachprüfung (Abweichung vom Plan, festgelegt vor dem Ergebnis der Nachprüfung):** Der Prüfer hat die Nachprüfung bis L50 gemacht und will nicht alle 68 Lose prüfen. Die Nummern sind zufällig gemischt; **L1 bis L50 sind eine Zufallsteilmenge** (47 Lose Typ Y, 3 Typ R).
> Y1, Y2, Y2b werden **nur für L1 bis L50 (Typ Y)** ausgewertet, Schwellen prozentual unverändert (90 %, 90 %, 85 %), mit Wilson-Intervall. Für Y1r werden zusätzlich die 4 offenen Regelwirkungs-Lose **L57, L62, L65, L88** nachgeprüft; Damit liegt für alle 15 Regelwirkungs-Lose ein Eintrag mit Datum oder Nachprüfung vor; **Y1r bleibt unverändert (≥ 12/15)**, ausgewertet mit dem Eintrag der Nachprüfung, wo es sie gibt, sonst mit der ersten Abgabe.
> **Nachprüfung abgegeben und ausgewertet (2026-11-04, Zwischenstand, Einträge unverändert übernommen):** Ausgefüllte Datei `reports/liste_nachpruefung_iteration7.md`, Übertragung `reports/liste_nachpruefung_iteration7_urteile.csv`, Auswertung `reports/liste_auswertung_iteration7.md`, Abschreibe-Check `reports/abschreibecheck_iteration7.md`.
> **Rohwerte:** Y1 36/47 = 76,6 % (Wilson 62,8–86,4), Y1r 8/15 = 53,3 %, Y2 29/47 = 61,7 %, Y2b 24/42 = 57,1 %. Y2/Y2b ohne veraltete „unbestimmbar“-Einträge (15 Lose, die Nachprüfung lieferte das Ende der Grundlaufzeit, das Höchstende wurde nicht neu eingetragen): Y2 29/32 = 90,6 %, Y2b 24/27 = 88,9 %.
> **Befunde (Fakten):** (1) 34 von 38 Nachprüfungen mit Eintrag; 4 Lose (L25, L27, L31, L38) blieben leer und zählen mit der ersten Abgabe („unbekannt“). (2) Abschreibe-Check: Bei 33 von 38 Losen stimmen die abgeschriebenen Felder Beginn/Ende exakt mit den Rohdaten überein; 5 weichen ab
> (L16: Ende des Loses 3 statt Los 2; L26, L30, L32: andere Daten als die Rohdaten des Loses; L48: Jahr 2026 statt 2027 als Ende). Die 4 Y-Abweichungen mit Datum bei L16, L26, L30, L32 gehen darauf zurück, dass der abgeschriebene Feldwert von den Rohdaten abweicht (Liste = Rohdaten); L18 ist ein Tippfehler im Ende der Grundlaufzeit (31.10. statt 31.12.2029, Feld 31.12.2029).
> (3) Alle 7 Abweichungen bei den Regelwirkungs-Losen (L3, L7, L49, L57, L62, L65, L88) haben dieselbe Form: Der Prüfer übernahm das Enddatum des Feldes als Ende der Grundlaufzeit, die Liste setzt nach Regel 1b ein früheres Datum aus dem Text (feste Laufzeit mit Option). Bei L65 stand in der ersten Abgabe noch das Textdatum 29.06.2026 (Quelle Text); die Nachprüfung ersetzte es nach der vorab festgelegten Regel „Nachprüfung ersetzt die erste Abgabe“ durch das Feld.
> **Offen vor dem Abschluss:** Die 4 leeren Lose und die 6 abgeschriebenen Feldwerte (L16, L18, L26, L30, L32, L48) sollen vom Prüfer nochmals im Original angesehen werden; die Einträge ändert nur der Prüfer.
> L51 bis L95 gehen nicht in Y1, Y2, Y2b ein. Dass L57, L62, L65, L88 Regelwirkungs-Lose sind, ist dem Prüfer bekannt (ihm mitgeteilt, um die Nachprüfung zu begrenzen).

> **Nachtrag 2026-11-04 (Korrekturen beim Abschluss, nach dem Evaluator-Bericht [evaluation_iteration7.md](../reports/evaluation_iteration7.md)):**
> (1) Befund 3 oben ist zu L65 falsch: Das Textdatum 29.06.2026 (Quelle Text) stand nur in der unfertigen ersten Datei (`reports/liste_pruefung_iteration7_urteile_abgabe1.csv`). In der maßgeblichen zweiten Abgabe stand bei L65 und L88 „unbekannt“. Richtig bleibt: Alle 7 Abweichungen der Regelwirkungs-Lose stehen in nachgeprüften Losen, in denen das Feld übernommen wurde; alle 8 Treffer stehen in Losen ohne Nachprüfung.
> (2) Befund 2 oben („Liste = Rohdaten“) ist nur für L26 an TED bestätigt (Evaluator); für L16, L30, L32 ist es eine Annahme. Der Abschreibe-Check vergleicht mit denselben Rohdaten, aus denen die Liste stammt.
> (3) Die Quelle der Nachprüfungs-Einträge hat der Prüfer nicht eingetragen; sie ist von Claude nach fester Regel abgeleitet (`quelle_ableiten`). Das Feld Hilfsmittel ist bei allen 38 Nachprüfungs-Einträgen leer; der Prüfer gab im Gespräch an, keine benutzt zu haben (Selbstangabe). Sitzungstabellen fehlen in beiden Abgaben.
> (4) Die offenen Punkte („4 leere Lose und 6 abgeschriebene Feldwerte nochmals ansehen“) werden **nicht** nachgeholt (Entscheidung des Nutzers; nach Kenntnis des Ergebnisses bestünde Bestätigungsgefahr).
> (5) Im Prototyp hieß es, Stufe A sei „die sicherste“; das ist nicht gedeckt und wurde umformuliert (`src/report/beispiel_liste.py`, `reports/beispiel_liste.md`). In `reports/liste_auswertung_iteration7.md` heißt es nicht mehr „Quelle laut Prüfer“. Die Zahlen sind unverändert.

**Ergebnis** _(2026-11-04)_

_Fakten_ (Quellen: [liste_auswertung_iteration7.md](../reports/liste_auswertung_iteration7.md), **[E7]** [evaluation_iteration7.md](../reports/evaluation_iteration7.md), [beispiel_liste.md](../reports/beispiel_liste.md), [abschreibecheck_iteration7.md](../reports/abschreibecheck_iteration7.md))

| | Kriterium | Ergebnis | erfüllt? |
|---|---|---|---|
| Y1 | Ende der Grundlaufzeit (Typ Y, L1–L50) ≥ 90 % | 36/47 = 76,6 % (Wilson 62,8–86,4) | nein |
| Y1r | Regelwirkungs-Lose ≥ 12/15 | 8/15 | nein |
| Y2 | Höchstende korrekt oder „unbestimmbar“ ≥ 90 % | 29/47 = 61,7 %; ohne 15 veraltete Einträge 29/32 = 90,6 % (selektiv) | nein |
| Y2b | nur Lose mit behauptetem Höchstende ≥ 85 % | 24/42 = 57,1 %; ohne veraltete Einträge 24/27 = 88,9 % (selektiv) | nein |
| Y3 | Verfahren | Regel, Seed und Vorlage vor dem Ziehen committet; Hilfsmittel der Nachprüfung leer, Quelle der Nachprüfung abgeleitet, keine Sitzungstabellen | nicht sauber erfüllt |
| Y4 | Prototyp | neu erzeugt (146 Lose), Stufen vorab, 143100-2026 Lose 8, 9, 14 jetzt 31.03.2030 / 31.03.2031 (Los 8 an TED bestätigt) | teilweise |

- Die 11 Y1-Abweichungen: 6 „unbekannt“ (4 leere Nachprüfungen L25, L27, L31, L38; L24 und L44 trotz abgeschriebener Felder) und 5 Datumsabweichungen (L16, L26, L30, L32 abgeschriebener Feldwert ≠ Rohdaten, L26 an TED bestätigt; L18 Tippfehler). Ein Listenfehler ist bei keiner belegt [E7].
- Bei 45 der 47 Lose nimmt die Liste das Enddatum-Feld; der Prüfer schrieb in der Nachprüfung dasselbe Feld ab. Inhaltlich (Text gelesen) geprüft sind die 12 Lose mit Quelle „Text“: 12/12 [E7].
- Y1r: Alle 7 Abweichungen stehen in nachgeprüften Losen mit Feldübernahme, alle 8 Treffer in Losen ohne Nachprüfung; gleiche Sachlage, gegensätzliches Urteil bei L74/L84 und L65/L88. Die 15 Lose stammen aus 9 Zuschlägen; L57, L62, L65, L88 waren dem Prüfer als Regelwirkungs-Lose bekannt [E7].
- Beschreibend: Y1 nach Losen gewichtet 80,2 %. Echte Höchstende-Fehler mit Datum: L72, L82 (außerhalb L1–L50, nicht unabhängig geprüft).
- Prüfzeit: erste Abgabe 143 Minuten, Median 1 Minute; A17 nicht belegt.

_Interpretation_
- Die Hypothese ist mit diesem Verfahren **nicht nachweisbar**, aber auch nicht widerlegt. Y1 ist ein Mischmaß aus möglichen Listenfehlern und Prüfungsfehlern; je nach Auflösung der Prüferfehler läge es zwischen 36/47 und 47/47 [E7].
- Regel 1b ist weder belegt noch widerlegt: Die Daten unterscheiden nicht, ob die Nachprüfung (Feld übernommen) oder die Regel (früheres Textdatum) recht hat. Der Typ „text_festlaufzeit“ ist ungetestet.
- Das Höchstende aus „Anzahl × Länge“ ist praktisch ungeprüft (Stufe B im Prototyp 2/5).
- Ursache liegt zu einem großen Teil im Prüfdesign, das Claude vorgeschlagen hat (Felder versteckt, „Nachprüfung ersetzt die erste Abgabe“, Rat „Feld übernehmen“); siehe [ki_irrwege.md](ki_irrwege.md).

**Entscheidung** _(Nutzer, 2026-11-04):_ **Abschluss mit diesem Stand, kein dritter Regelversuch** (vorab festgelegte Folge „Y1 zwischen 70 % und 90 %“; „weiter“ ist ausgeschlossen, „Idee anpassen“ greift nicht).
Die Liste führt das Ende der Grundlaufzeit als „laut Bekanntmachung“, das Höchstende nur als Hinweis; die Fehlerquote wird offen genannt (Y1 76,6 % als Mischmaß). Die Prüfer-Einträge werden nicht nachträglich korrigiert.
Als letzte Iteration folgt eine reine Messung (KI-Zweitlesung mit eingefrorener Liste), die das Ergebnis von Iteration 7 nicht ersetzt.

---

## Iteration 8: KI-Zweitlesung der Stichprobe von Iteration 7

**Status:** abgeschlossen am 2026-11-05 (angelegt am 2026-11-04)

**Fokus und Phasen:** nur Phase 5 (Messung). Liste und Lese-Regeln bleiben im Stand von Commit a93785e eingefroren (Entscheidung zu Iteration 7: kein dritter Regelversuch).
Abweichung vom Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan) („7+ Ausbau“): Der Evaluator nennt eine unabhängige Lesung der Originale als das, was für ein belastbares Urteil fehlt [E7]; ohne zweiten menschlichen Prüfer ist ein KI-Leser die einfachste Lösung.
**Diese Iteration ersetzt das Ergebnis von Iteration 7 nicht**; beide Messungen werden nebeneinander berichtet. Der Nutzer prüft nicht mehr selbst (Entscheidung des Nutzers, 2026-11-04).

**Hypothese** _(vorab festgelegt am 2026-11-04, vor dem Lauf der Leser)_
„Zwei voneinander unabhängige KI-Leser, die nur das TED-Original sehen (ohne Listenwerte und ohne Einträge des Prüfers), kommen beim Ende der Grundlaufzeit bei mindestens 90 % der 80 Zufallslose
der Iteration 7 zum selben Datum wie die Vertragsliste.“

**Begriffe** _(vorab festgelegt)_
- **Lose:** alle 95 Lose der Iteration 7 (80 Typ Y, 15 Typ R), Nummern L1–L95 wie dort. Beschreibend zusätzlich 143100-2026 Lose 8, 9, 14 (Oberpfalz-Prototyp, Typ „text_festlaufzeit“; Entwicklungsdaten, zählt nicht).
  Für den Typ „text_festlaufzeit“ gibt es keine Lose außerhalb der bei der Entwicklung angesehenen Bekanntmachungen (122 Lose in 9 Bekanntmachungen, alle in `reports/entwicklung_iteration7_notices.txt`); er bleibt ungetestet.
- **Vorlage für die Leser:** je Los nur Nummer, Bekanntmachung, Los-Nummer, Los-Titel, TED-Link (`reports/zweitlesung_iteration8_vorlage.md`, SHA-256 im Commit vor dem Lauf). Keine Listenwerte, keine Prüfer-Einträge, keine Hinweise auf Typ Y/R.
- **Leser:** zwei Subagenten in getrennten Läufen, **Leser A = Opus, Leser B = Sonnet**, ohne Kenntnis voneinander. Sie bekommen die Vorlage im Auftrag, lesen je Los die TED-Seite der Bekanntmachung (ganzer Abschnitt zur Laufzeit des Loses: Beginn, Ende, Dauer, Verlängerung, Beschreibung) und dürfen **keine Projektdateien** öffnen.
  Je Los: Ende der Grundlaufzeit (Datum oder `unbekannt`), Höchstende (Datum, `keine Verlängerung`, `keine Angabe` oder `unbestimmbar`), wörtliches Zitat der tragenden Textstelle, Gebäudereinigung ja/nein. Die Antworten werden unverändert gespeichert (`reports/zweitlesung_iteration8_leser_a.csv`, `…_leser_b.csv`).
  Nach dem Lauf prüft Claude in den Protokollen der Subagenten, welche Dateien sie geöffnet haben; jeder Zugriff auf Projektdateien wird im Ergebnis genannt.
- **Vergleichswert:** Stimmen A und B überein (ein Tag Toleranz), gilt ihr Wert. Sonst entscheidet der Subagent `evaluator` am TED-Original anhand der Zitate; kann er nicht entscheiden, gilt `unklar`.
  `unklar` und `unbekannt` beim Vergleichswert zählen als Abweichung der Liste (vorsichtig) und werden getrennt ausgewiesen.
- **Korrekt** wie in Iteration 7: Ende der Grundlaufzeit ein Tag Toleranz; Höchstende korrekt oder Liste „unbestimmbar“, „Höchstende = Grundlaufzeit“ korrekt bei Vergleichswert „keine Verlängerung“ oder „keine Angabe“.

**Erfolgskriterium** _(vorab festgelegt am 2026-11-04)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| Z0 | Leser A und B stimmen beim Ende der Grundlaufzeit überein (95 Lose) | ≥ 90 % | A19 (neu) |
| Z1 | Ende der Grundlaufzeit: Liste = Vergleichswert (80 Zufallslose) | ≥ 72/80 = 90 % | A4, A13 |
| Z2 | dasselbe bei den 15 Regelwirkungs-Losen (Regel 1b, Typ „text_laufzeit_option“) | ≥ 12/15 | – |
| Z3 | Höchstende korrekt oder „unbestimmbar“ (80 Lose) / nur Lose, bei denen die Liste ein Höchstende nennt | ≥ 90 % / ≥ 85 % | – |
| Z4 | Kontrolle: Der Evaluator prüft 10 zufällig gezogene Übereinstimmungen von A und B am TED-Original (Seed 20261108, vor dem Lauf committet) | ≥ 9/10 bestätigt | A19 |

Beschreibend, ohne Schwelle: Vergleich Liste / Vergleichswert / Prüfer der Iteration 7 für L1–L50 (Welche der 11 Abweichungen waren Listenfehler, welche Lesefehler?); Y1 nach Losen gewichtet;
Lose, die ein Leser als „keine Gebäudereinigung“ einstuft (A12); die drei Kontroll-Lose aus 143100-2026.

**Was folgt aus welchem Ergebnis**
- Z0 oder Z4 verfehlt → die KI-Lesung taugt nicht als Prüfung; Z1 bis Z3 werden nicht gewertet, es bleibt beim Abschluss von Iteration 7.
- Z0 bis Z4 erfüllt → **weiter (Projektabschluss):** Die Liste gilt beim Ende der Grundlaufzeit als „durch zwei KI-Lesungen gestützt, nicht von Menschen bestätigt“; Regel 1b für den Typ „text_laufzeit_option“ als gestützt. Danach Lab-Log, Vortrag.
- Z1 zwischen 70 % und 90 % oder Z2 verfehlt (bei erfüllten Z0, Z4) → Abschluss wie Iteration 7 (Ende „laut Bekanntmachung“), Fehlerquote mit beiden Messungen und den Fehlerarten.
- Z1 < 70 % → **Idee anpassen:** Das Ende der Grundlaufzeit erscheint in der Liste nur als Hinweis.
- Z3 verfehlt → Höchstende bleibt nur Hinweis (wie bisher).
- In keinem Fall wird die Regel in dieser Iteration geändert.

**Zeitrahmen:** 2026-11-04 bis 2026-11-05, eine Sitzung; Aufwand des Nutzers nur für Entscheidungen.

**Plan**
1. Phase 5: Vorlage erzeugen (`src/prepare/zweitlesung_iteration8.py` → `reports/zweitlesung_iteration8_vorlage.md`), Seed für Z4 festlegen; Kriterien, Skript und SHA-256 der Vorlage **vor dem Lauf** committen.
2. Leser A (Opus) und Leser B (Sonnet) getrennt laufen lassen; Antworten unverändert speichern; Protokolle auf Dateizugriffe prüfen.
3. Auswertung Z0–Z3 und Dreiervergleich (`src/prepare/auswertung_iteration8.py` → `reports/zweitlesung_iteration8_auswertung.md`).
4. Evaluator: Uneinigkeiten entscheiden und Z4 am Original prüfen, danach kritische Gesamtprüfung.
5. `/iteration-ende`; Genauigkeitsangabe im Prototyp nur ergänzen, wenn die Folge es vorsieht.

**Geprüfte Annahmen:** A4, A13 (Enddatum = Ende der Grundlaufzeit auf Los-Ebene); neu vorgeschlagen **A19** „Ein KI-Leser liest Laufzeiten aus TED-Bekanntmachungen so genau, dass er als Zweitprüfer taugt“ (Z0, Z4); A12 nur beschreibend.
A11, A17, A18 werden nicht geprüft (nur eForms-Lose, keine menschliche Prüfzeit, keine Paare). A1 und A15 bleiben außerhalb des Projektumfangs.
**Grenzen (vorab benannt):** Die Lese-Regel stammt ebenfalls von einer KI (Claude); gleiche Lesefehler bei Regel und Lesern sind möglich, Z4 fängt das nur teilweise ab.
Den Zugriff auf Projektdateien kann Claude den Lesern nicht technisch sperren, nur verbieten und hinterher kontrollieren. Die 95 Lose sind Claude samt Listenwerten bekannt; die Leser bekommen sie nicht.

> **Fortschritt 2026-11-04 (Schritt 1, vor dem Lauf der Leser; Kriterien unverändert):** Vorlage `reports/zweitlesung_iteration8_vorlage.md` aus `src/prepare/zweitlesung_iteration8.py` (98 Zeilen: L1–L95, K1–K3), **SHA-256 `5be683ad1fb69c6ea5ee933f6a27f06d9a6f13fc0f952444a025f0615e846450`**; Seed Z4 = 20261108 (im Skript).
> Durchführung (festgelegt vor dem Lauf): Die TED-Detailseite lädt ihren Inhalt per JavaScript und ist für WebFetch leer (Test an 143100-2026); die Vorlage verlinkt deshalb die HTML-Fassung `ted.europa.eu/de/notice/<Nr>/html`.
> Jeder Leser läuft in **4 Teilläufen** (L1–L25, L26–L50, L51–L75, L76–L95 + K1–K3), jeweils neuer Subagent desselben Modells; die Teilläufe von A und B wissen nichts voneinander.
> **Zusätzliche Grenze:** WebFetch gibt die Seite über ein kleines Hilfsmodell weiter; die Leser sollen deshalb wörtliche Zitate verlangen und lange Seiten mit `offset` weiterlesen. Fehler dieses Hilfsmodells treffen beide Leser gleich und sind nur über Z4 (Evaluator am Original) teilweise erkennbar.

> **Fortschritt 2026-11-04/05 (Schritte 2 bis 4; Kriterien unverändert):** Auswertungsskript `src/prepare/auswertung_iteration8.py` vor den Antworten committet (9645fa8). Leser A (Opus) und B (Sonnet), je 4 Teilläufe, Rohantworten unverändert in `reports/zweitlesung_iteration8_roh/` (Commit 74f95d0); die CSV je Leser sind nur im Format angepasst (Semikolons im Zitat von Leser B → Kommas).
> Protokollprüfung: nur WebFetch auf ted.europa.eu, keine Projektdateien geöffnet [`reports/zweitlesung_iteration8_hinweise.md`]. **Nachträglich festgestellt:** Die Leser hatten `CLAUDE.md` automatisch im Kontext und damit den Satz „Das Enddatum der Bekanntmachung ist manchmal schon das Höchstende“ (in den Protokollen beider Leser gefunden); die Listenwerte kannten sie nicht. Der Auftragstext an die Leser ist im Repo nur über die Vorlage nachvollziehbar, die Protokolle liegen nicht im Repo.
> Der Evaluator entschied die Uneinigkeiten L7 (Ende der Grundlaufzeit: unklar) und L33 (Höchstende: unklar) und bestätigte 10/10 Übereinstimmungen am Original (Seed 20261108); er nutzte dasselbe WebFetch-Hilfsmodell und kannte die Werte der Leser (Commit 3e9178b).

**Ergebnis** _(2026-11-05)_

_Fakten_ (Quellen: [zweitlesung_iteration8_auswertung.md](../reports/zweitlesung_iteration8_auswertung.md), **[E8]** [evaluation_iteration8.md](../reports/evaluation_iteration8.md), [zweitlesung_iteration8_hinweise.md](../reports/zweitlesung_iteration8_hinweise.md))

| | Kriterium | Ergebnis | erfüllt? |
|---|---|---|---|
| Z0 | Leser A = B beim Ende der Grundlaufzeit (95 Lose) ≥ 90 % | 94/95 = 98,9 % (nur L7 uneinig); Höchstende 94/95 (nur L33) | ja |
| Z1 | Liste = Vergleichswert (80 Zufallslose) ≥ 72/80 | **77/80 = 96,2 %** (Wilson 89,5–98,7); Abweichungen L5, L33, L81 | ja |
| Z2 | Regelwirkungs-Lose ≥ 12/15 | 14/15 nach Regel; bei einheitlichem Maßstab für „zum Schuljahresende“ 11/15 [E8] | formal ja, mit einheitlichem Maßstab nein |
| Z3 | Höchstende korrekt oder „unbestimmbar“ ≥ 90 % / nur behauptetes Höchstende ≥ 85 % | 75/80 und 67/72 = 93,1 %; ohne „unbestimmbar = korrekt“ 69/80 = 86,3 % [E8] | ja |
| Z4 | Evaluator bestätigt 10 zufällige Übereinstimmungen ≥ 9/10 | 10/10 (Wilson-Untergrenze etwa 72 %); 9 von 10 einfache Fälle | formal ja, schwach belegt |

- Dreiervergleich L1–L50 (Typ Y): Liste = Vergleichswert bei 45/47, Prüfer der Iteration 7 = Vergleichswert bei 34/47. In allen 11 Abweichungen der Iteration 7 steht die KI-Lesung auf der Seite der Liste; bei L5 und L33 folgten Prüfer und Liste dem Feld, die KI dem Text [E8].
- Echte Listenfehler am Original bestätigt (Evaluator): L5 (Enddatum ist schon Höchstende, Regel 1b erkennt „3 Jahre mit Option“ nicht), L81 (Wert von Los 1 auf Los 2 übertragen, Regel 6), L72 (Höchstende 2037 statt 2031, „um 3 Jahre“ als Länge je Verlängerung gelesen), L82 (Datum „31. Oktober 2030“ nicht erkannt). L33: Quelle widerspricht sich, nicht belegbar. L69 und L72: Lose ohne Zuschlag stehen in der Liste (am Original bestätigt, nicht gezählt) [E8].
- Schuljahres-Lose (acht Lose des Landkreises Börde): Das Ende des ersten Jahres ist „zum Schuljahresende“, ein tagesgenaues Datum steht nirgends; Liste und Leser rechnen Beginn + 1 Jahr − 1 Tag (die Vorlage gab diese Rechnung vor) [E8].
- Kontroll-Lose 143100-2026 Lose 8, 9, 14: Liste und beide Leser 31.03.2030 / 31.03.2031.

_Interpretation_
- Nach den vorab festgelegten Regeln folgt „weiter“. Z1 ist tragfähig: Das Ende der Grundlaufzeit der Liste stimmt bei 77/80 Zufallslosen mit zwei getrennten KI-Lesungen überein, nicht von Menschen bestätigt (Intervall ohne Berücksichtigung der Klumpung).
- Die meisten der 11 Abweichungen aus Iteration 7 sind mit Prüferfehlern vereinbar; Iteration 7 wird dadurch nicht ersetzt, beide Messungen stehen nebeneinander.
- „Regel 1b gestützt“ gilt nur für Fälle mit ausdrücklich genannter Grunddauer (L3, L73, L77 am Original). Für den Typ „zum Schuljahresende“ und den Typ „text_festlaufzeit“ (nur die Kontroll-Lose) ist die Regel nicht belegt; die Vorlage gab den Lesern die Logik von Regel 1b vor (Zirkelschluss-Risiko).
- Die Leser sind getrennt, aber nicht unabhängig: gleiche Modellfamilie wie Regel und Evaluator, gleiches Hilfsmodell, `CLAUDE.md` im Kontext. Z0 und Z4 messen deshalb vor allem die Einheitlichkeit des Verfahrens. Aussagen wie „Liste korrekt“, „Regel 1b belegt“, „unabhängig geprüft“ sind nicht zulässig.

**Entscheidung** _(Nutzer, 2026-11-05):_ **Weiter, Projektabschluss, eingeschränkt formuliert.** Die Liste gilt beim Ende der Grundlaufzeit als „durch zwei KI-Lesungen gestützt (77/80), nicht von Menschen bestätigt, Leser nicht unabhängig“.
Z2 wird mit beiden Zahlen berichtet (14/15 und 11/15). Die neuen Fehlerarten (L5, L81 Regel 6, L69/L72 Lose ohne Zuschlag, L72/L82 Höchstende) bleiben als offene Grenzen für das Lab-Log; die Regel wird nicht mehr geändert. Keine weitere Iteration.

---

## Iteration 9: Verbesserte Liste, neue Stichprobe, KI-Lesung ohne die Grenzen der Iteration 8

**Status:** läuft (angelegt am 2026-11-05)

**Fokus und Phasen:** 3 → 5 → 6. Abweichung vom Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan) („7+ Ausbau“): Die in Iteration 8 gefundenen Fehlerarten sind bekannt und günstig zu beheben, der Nutzer hat noch etwa eine Woche.
Die Messung läuft diesmal mit einem Aufbau, der die Grenzen der Iteration 8 behebt, soweit das ohne zweiten unabhängigen Menschen möglich ist. LN B, Zweierteam. Iteration 8 und ihr Ergebnis bleiben unverändert stehen.

**Ausgangslage (Fakten aus Iteration 8 [E8]):** Fehlerarten der Liste: „3 Jahre mit Option“ nicht als Grundlaufzeit erkannt (L5), Regel 6 überträgt einen Einzelwert auf andere Lose (L81), „um 3 Jahre“ als Länge je Verlängerung gelesen (L72), Datum mit Monatsnamen nicht erkannt (L82), Lose ohne Zuschlag stehen in der Liste (L69, L72).
Grenzen der Lesung in Iteration 8: Hilfsmodell des Abrufwerkzeugs kürzt und fasst zusammen; die Leser hatten `CLAUDE.md` mit dem Fehlertyp im Kontext; die Vorlage gab Regel 1b als Anweisung vor; Schuljahres-Fälle nicht tagesgenau; Kontrolle nicht blind; gleiche Modellfamilie.

**Hypothese** _(vorab festgelegt am 2026-11-05, vor jeder Regeländerung)_
„Nach Behebung der in Iteration 8 gefundenen Fehlerarten stimmt das Ende der Grundlaufzeit der Liste in einer neuen, ungesehenen Stichprobe bei mindestens 90 % der Lose mit einem Vergleichswert zweier KI-Leser überein. Die Leser lesen in einer Sitzung ohne Projektkontext Rohtexte der Bekanntmachung und tragen nur Fakten ein.“

**Begriffe** _(vorab festgelegt)_
- **Stichprobe:** 100 Lose, Seed wird vor dem Ziehen committet. **70 Zufallslose** (höchstens 2 je Zuschlag) und **30 geschichtete Lose:** 10 aus Bekanntmachungen, in denen nur ein Teil der Lose Laufzeitfelder hat (Regel 6), 10, deren Ende der Grundlaufzeit sich durch die neuen Regeln gegenüber der Fassung a93785e ändert, 10 aus Bekanntmachungen mit mehreren Losen.
  Ausgeschlossen: die 95 Lose der Iteration 7 und 8, alle Bekanntmachungen, die beim Entwickeln der neuen Regeln angesehen werden (Liste vor dem Ziehen committet), und die Bekanntmachungen der Entwicklungsfälle. Schlüssel lokal, SHA-256 im Commit.
- **Rohtext:** Ein Skript lädt die TED-Bekanntmachung als XML unverändert nach `data/raw` und schneidet je Los den vollständigen Text aller Laufzeit-, Options- und Beschreibungsfelder mit Los-Kennung heraus. Die Zuordnung Los zu Titel nimmt der Leser vor, nicht die Regel (unabhängig von Regel 6).
  Ein Hilfsmodell zwischen Leser und Text entfällt. Das Skript wird vor dem Lauf an Stichproben geprüft, die Prüfung wird offen ausgewiesen.
- **Leser:** A = Opus, B = Sonnet, je in neuen Sitzungen des Nutzers in einem leeren Ordner **ohne `CLAUDE.md`** (Nachweis über `/memory`), je Teil eine neue Sitzung. Die Anweisung wird vorab committet und unverändert eingefügt.
  Die Leser tragen nur **Fakten** mit Zitat ein: Beginn, Dauer der festen Laufzeit, Verlängerungen (Anzahl, Länge), genanntes spätestes Ende, Widersprüche, „nicht tagesgenau“, „kein Zuschlag erteilt“, Gebäudereinigung ja/nein. Die Projektregel („die kürzere gilt“) steht nicht in der Anweisung.
- **Vergleichswert:** wird aus den Fakten mit einer **vorab committeten, neutralen Definition** berechnet (Ende der Grundlaufzeit = Ende der ersten festen Laufzeit ohne Optionen; Beginn + Dauer − 1 Tag). Stimmen A und B überein (ein Tag Toleranz), gilt ihr Wert; sonst entscheidet der Evaluator blind am Rohtext, ersatzweise `unklar` (zählt als Abweichung der Liste).
- **Nicht tagesgenau:** Fälle, bei denen ein Leser „nicht tagesgenau“ einträgt (z. B. „zum Schuljahresende“), kommen aus Zähler und Nenner heraus und werden einzeln ausgewiesen.
- **Menschliche Kontrolle:** Der Kommilitone liest 15 Lose (Zufallsauswahl aus der Stichprobe, Seed vorab), ohne Listenwerte, im TED-Original, und trägt Ende der Grundlaufzeit und Höchstende ein.
- **Korrekt** wie in Iteration 8: Ende der Grundlaufzeit mit einem Tag Toleranz; Höchstende korrekt oder Liste „unbestimmbar“, „Höchstende = Grundlaufzeit“ korrekt bei Vergleichswert „keine Verlängerung“ oder „keine Angabe“. Zusätzlich streng: „unbestimmbar“ zählt nicht automatisch als korrekt (beschreibend, beide Werte berichtet).

**Erfolgskriterium** _(vorab festgelegt am 2026-11-05)_

| | Kriterium | Schwelle | Annahme |
|---|---|---|---|
| V1 | Ende der Grundlaufzeit: Liste = Vergleichswert, 70 Zufallslose | ≥ 63/70 = 90 % | A4, A13 |
| V2 | dasselbe, 30 geschichtete Lose | ≥ 24/30 = 80 % | A4, A13 |
| V3 | Die neue Fassung ist auf den Zufallslosen nicht schlechter als die alte Fassung (a93785e), gemessen am selben Vergleichswert | Ja/Nein | – |
| V4 | Höchstende korrekt oder „unbestimmbar“ (Zufallslose) / nur Lose mit behauptetem Höchstende | ≥ 90 % / ≥ 85 % | – |
| V5 | Leser A und B stimmen bei den Fakten überein (Ende der Grundlaufzeit, 100 Lose) | ≥ 90 % | A19 |
| V6 | Menschliche Kontrolle: Der Vergleichswert stimmt mit dem Kommilitonen bei 15 Losen überein | ≥ 13/15 | A19 |
| V7 | Lose ohne Zuschlag: keines davon steht in den 100 Losen der neuen Liste; Anteil in der alten Liste wird gezählt (beschreibend) | 0 von 100 | A20 |
| V8 | Verfahren: Regeln, Seed, Anweisung, Definition und Kriterien vor dem Lauf committet; Sitzung ohne `CLAUDE.md` nachweisbar; Rohtexte unverändert | Ja/Nein | A19 |

Beschreibend, ohne Schwelle: Z-Vergleich mit der alten Fassung je Fehlerart, Anteil der neuen Fehlerarten in der Population, Lose mit „nicht tagesgenau“, Einstufung „Gebäudereinigung ja/nein“ (A12), Vergleich Mensch / Leser / Liste an den 15 Losen.

**Was folgt aus welchem Ergebnis**
- V1 bis V8 erfüllt → **weiter:** Die neue Fassung wird der Prototyp (neu erzeugt, Stufen unverändert); Lab-Log und Folien aktualisieren, Projekt abschließen.
- V1 zwischen 70 % und 90 %, V2 zwischen 60 % und 80 % oder V3 verfehlt → **Abschluss mit der Fassung a93785e als Prototyp;** die neue Fassung wird als Ausblick genannt, beide Messungen werden offen berichtet.
- V1 < 70 % → **zurück zu Phase 3** mit dem Fehlerbild; eine weitere Iteration nur, wenn Zeit bleibt. Der Prototyp bleibt a93785e.
- V6 verfehlt → das Ergebnis gilt als „nur KI-gestützt“; der Prototyp folgt V1 bis V4.
- V7 verfehlt → Filter für Lose ohne Zuschlag nachbessern, bevor die Iteration abgeschlossen wird.
- V8 oder V5 nicht erfüllt → den Schritt wiederholen, bevor die Iteration abgeschlossen wird.

**Zeitrahmen:** 2026-11-05 bis etwa 2026-11-12, rund 5 Arbeitstage. Aufwand des Nutzers etwa 2 bis 3 Stunden für die Leser-Sitzungen, Kommilitone etwa 30 Minuten.

**Plan**
1. Phase 3: Fehlerarten beheben (Lose ohne Zuschlag filtern, Regel 6 einschränken, Monatsnamen, „N Jahre mit Option“, „um N Jahre“) in `src/prepare/vertragsliste.py`; Entwicklungstest an den 95 Losen aus Iteration 7 und 8 (zählt nicht); Regel einfrieren und committen; Liste der angesehenen Bekanntmachungen committen.
2. Phase 3/5: Seed committen, danach Stichprobe ziehen (`src/prepare/stichprobe_iteration9.py`); Schlüssel lokal, SHA-256 im Commit.
3. Phase 5: Skript für die Rohtexte (`src/prepare/rohtext_iteration9.py`), Anweisung für die Leser, Blatt für den Kommilitonen, neutrale Definition des Vergleichswerts und Auswertungsskript (`src/prepare/auswertung_iteration9.py`); alles **vor dem Lauf** committen.
4. Phase 5: KI-Lesung in den Sitzungen des Nutzers (A und B, je 4 bis 5 Teile); der Kommilitone liest 15 Lose. Rohantworten unverändert nach `reports/zweitlesung_iteration9_roh/`.
5. Phase 5: Auswertung V1 bis V8; Kontrolle des Evaluators blind am Rohtext; Gesamtprüfung durch den Evaluator.
6. Phase 6: Prototyp neu erzeugen (falls die Folge es vorsieht), Lab-Log und Folien aktualisieren.
7. `/iteration-ende`.

**Geprüfte Annahmen:** A4, A13 (Ende der Grundlaufzeit auf Los-Ebene), A19 (KI-Leser als Zweitprüfer, diesmal mit menschlicher Kontrolle), A20 (Anteil Lose ohne Zuschlag). A12 nur beschreibend. A11, A17, A18 bleiben ungeprüft; A1 und A15 außerhalb des Projektumfangs.
**Grenzen (vorab benannt):** Regel, Leser und Evaluator stammen aus derselben Modellfamilie; V6 mit 15 Losen ist ein menschlicher Anker, aber statistisch dünn. Das Skript für die Rohtexte und die neutrale Definition stammen von Claude; ein Fehler dort träfe beide Leser gleich, deshalb werden beide vorab an Stichproben geprüft und offen ausgewiesen.
Claude kennt die Listenwerte der Stichprobe; die Leser bekommen sie nicht. Der Nachweis „ohne `CLAUDE.md`“ stützt sich auf die Angabe des Nutzers und die Ausgabe von `/memory`.

> **Fortschritt 2026-11-05 (Schritt 1, Regeln behoben; vor dem Ziehen der Stichprobe; Kriterien unverändert, zwei Präzisierungen unten):**
> **Nachlieferung der Zuschlagsfelder:** Die bisherigen Rohdaten enthalten keinen Hinweis auf einen Zuschlag je Los. Mit `src/ted_download.py --felder …` wurden `winner-selection-status`, `result-lot-identifier` und `tender-lot-identifier` nachgeladen (5.215 Bekanntmachungen, `data/raw/ted_search/DEU_result_cpv909_20231025_20260930_felder`, unverändert; Feldnamen laut Feldliste der TED-Dokumentation geprüft). Die Status stehen in der Reihenfolge der Ergebnis-Lose und werden über die sortierte Los-Kennung den Losen zugeordnet; bei 82 Bekanntmachungen fehlt der Status oder passt nicht zur Zahl der Lose („unbekannt“, Los bleibt in der Liste).
> **Regeln 6 bis 10 in `src/prepare/vertragsliste.py`** (Beschreibung im Kopf des Skripts): (6) bei Beginn, Ende und Dauer bleibt das Feld leer, wenn die Liste kürzer ist als die Zahl der Lose (Textfelder wie bisher; betroffen 17 Bekanntmachungen mit 76 Losen); (7) Lose ohne Zuschlag (Status ≠ „selec-w“) kommen nicht in die Liste; (8) Monatsnamen- und Schrägstrich-Daten werden normalisiert; (9) „maximal um N Jahre“ ist die Gesamtdauer der Verlängerungen; (10) „N Jahre mit Option …“ zählt als feste Dauer in Regel 1b (b).
> **Wirkung auf die Liste (Fakten):** 9.325 statt 9.915 Lose (590 Lose ohne Zuschlag entfernt, 6,0 %); bei 46 Losen ändert sich das Ende der Grundlaufzeit (39 × entfällt durch Regel 6, 7 × früher durch Regel 10, 3 Bekanntmachungen), bei 56 weiteren nur das Höchstende; Abdeckung X4 2.783/3.503 = 79,4 % (vorher 79,7 %). SHA-256 der neuen Liste `data/processed/vertragsliste_909.csv`: `5f0a07a2…` (siehe Commit), der alten Fassung (Referenz, `vertragsliste_909_iteration8.csv`): `0e8b25b1…`.
> **Entwicklungstest (zählt nicht):** An den 95 Losen der Iteration 7 und 8 sind die vier Fehler behoben (L5 jetzt 31.08.2029, L81 ohne Ende, L72 und L69 ohne Zuschlag entfernt, L82 Höchstende 31.10.2030); zusätzlich entfällt L50, bei dem TED selbst „kein Gewinner gewählt“ meldet (`clos-nw`). Der Regressionstest der Iteration 7 (60 Lose der Iteration 6) zeigt keine Abweichung. Angesehene Bekanntmachungen: `reports/entwicklung_iteration9_notices.txt`.
> **Präzisierung 1 (Stichprobe, vor dem Ziehen):** Es gibt gegenüber a93785e nur 7 Regelwirkungs-Lose (3 Bekanntmachungen). Die 30 geschichteten Lose werden deshalb so gezogen: **alle** Regelwirkungs-Lose, deren neues Ende nicht leer ist (bis zu 10), der Rest aus Bekanntmachungen mit mindestens 3 Losen (zufällig, bis 30 Lose). Zusätzlich bis zu 10 **beschreibende** Lose, bei denen das Ende durch Regel 6 entfällt (nicht in V1/V2; es wird ausgewiesen, wie oft der Leser ein bestimmbares Ende findet, das die Liste nicht mehr nennt). V2 bleibt ≥ 24/30.
> **Präzisierung 2 (V7, vor dem Ziehen):** Weil der Filter Lose ohne Zuschlag per Konstruktion entfernt, wäre „0 von 100“ ein Selbstgänger. V7 gilt deshalb für die Aussage der Leser: **kein Los der Stichprobe, für das ein Leser aus dem Rohtext „kein Zuschlag erteilt“ meldet** (unabhängig vom Statusfeld). Beschreibend: Anteil der Lose ohne Zuschlag in der alten Liste (590 von 9.915 nach Statusfeld).

> **Nachtrag 2026-11-05 (Schritt 1):** Im Eintrag oben steht für die neue Liste der Hash `5f0a07a2…`; richtig ist **`5ec73364…`** (SHA-256 `5ec733643f88ed8bd51e83617d471bead6b52a95ea4da305a0bd3a6f6d64f2b5`, 9.325 Lose; Tippfehler).
> **Schritt 2 (vor dem Ziehen):** `src/prepare/stichprobe_iteration9.py` mit **Seed 20261109** festgelegt (Z 70, R bis 10, M bis zum Rest von 30, S bis 10, Mensch 15 aus Z, R, M). Trockenlauf mit Seed 1: Z 70, R 4 (alle Regelwirkungs-Lose, die nach den Ausschlüssen übrig sind), M 26, S 10. Damit hat V2 30 Lose (4 R + 26 M); die 4 R-Lose stammen aus 2 Bekanntmachungen.

> **Fortschritt 2026-11-05 (Schritt 2 und 3; Kriterien unverändert; vor dem Lauf der Leser):**
> **Stichprobe gezogen** (Seed 20261109, im Commit 4521952 vor dem Ziehen): 110 Lose aus 104 Bekanntmachungen: Z 70, **R 2** (von 4 möglichen; eine der beiden Bekanntmachungen war schon durch Z belegt, die Reihenfolge Z vor R war vorab so festgelegt), M 28, S 10; menschliche Kontrolle 15 Lose. V2 hat damit 30 Lose (2 R + 28 M).
> Schlüssel lokal (), **SHA-256 `9dbf5c1a1b30256fa70d8f16759c9c613edf41cb54102c76c50b5440bbdc8753`**; Liste der Lose ohne Listenwerte (`reports/stichprobe_iteration9_lose.csv`) SHA-256 `f3bff58035bae110fedacf8f4ea4cd7c6c803d8c7d4c9e65a0e938b9685639ca`.
> **Rohtext** (`src/prepare/rohtext_iteration9.py`): TED-XML unverändert in `data/raw/ted_xml/iteration9_20261105/` (104 Dateien; die ersten Abrufe brachen ab, danach mit Wiederholung vollständig geladen); je Bekanntmachung ein Auszug der Felder und Texte mit Feldnamen (`reports/zweitlesung_iteration9/rohtext/`, SHA-256 aller Dateien zusammen `5909d2d4928c885bb03a365919b641006d0df5da1723fee2269bcf43f4b50c31`).
> **Prüfung des Skripts** (`reports/zweitlesung_iteration9/pruefung_rohtext.md`): Bei 108 von 110 Losen stimmen Titel, Beginn und Enddatum des XML mit den API-Daten der Liste überein; die 2 Abweichungen (N34, N54) sind S-Lose, bei denen die Liste durch Regel 6 keinen Beginn mehr hat, das XML ihn aber enthält. Bei Bekanntmachungen mit mehr als 8 Losen sind nur die Lose der Stichprobe vollständig, die übrigen gekürzt.
> **Anweisung für die Leser** (`reports/zweitlesung_iteration9/pakete/teil_1` bis `teil_5`, je etwa 22 Lose; SHA-256 der Anfänge der aufgabe.md: 9de7866e 456fb4a6 ddd9c942 8fe50e39 469f83a3 ): Sie nennt weder Projekt noch Regeln noch Fehlerarten und verlangt nur Fakten (Beginn, Feld-Enddatum, Dauer der festen Laufzeit, Ende der festen Laufzeit, Verlängerungen, spätestes Ende, Gesamtdauer, „nicht tagesgenau“, „kein Zuschlag“, Gebäudereinigung ja/nein, Zuordnung sicher, Zitat). Ausdrücklich: „Rechne nichts aus.“ Der Start-Prompt steht in `start_prompt.txt`.
> **Vergleichswert und Auswertung** (`src/prepare/auswertung_iteration9.py`, vor den Antworten committet, an erfundenen Antworten im Scratchpad getestet): Die neutrale Definition des Endes der Grundlaufzeit und des Höchstendes aus den Fakten steht im Kopf des Skripts; die Projektregeln werden nicht benutzt. Die Kontrolle des Evaluators (10 Lose, Seed 20261110) ist beschreibend und liest den Rohtext blind.
> **Menschliche Kontrolle:** Blatt `reports/zweitlesung_iteration9/blatt_mensch.md` (15 Lose, ohne Listenwerte), SHA-256 `63321fe9fd86df65cd4f45a8683e7a6e98eab5fa0e476f45638b633f7d16014b`.

> **Nachtrag 2026-11-05 (Schritt 2):** Im Eintrag oben fehlt wegen eines Schreibfehlers der Pfad des Schlüssels: Er liegt lokal unter `data/processed/stichprobe_iteration9_schluessel.csv` (nicht im Git; SHA-256 wie oben).
