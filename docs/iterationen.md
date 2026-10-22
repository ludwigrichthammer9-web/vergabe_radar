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
| 2 | Neuausschreibungen sichtbar und zuordenbar? Danach Datenaufbereitung (Arbeitsnische Gebäudereinigung) | 2 → 3 (→ 4 → 5) | – | geplant | – |
| 3 | Erste Prognose (Baseline + Backtest) | 3 → 4 → 5 | – | geplant | – |
| 4 | Erster Kundentest | 6 → 1 | – | geplant | – |
| 5+ | Ausbau | je nach Bewertung | – | geplant | – |

Die geplanten Iterationen stammen aus dem Iterationsplan in [CRISP-DM.md](CRISP-DM.md#iterationsplan). Nach der Entscheidung zu Iteration 1
sind sie um eine Stelle verschoben. Konkretisiert werden sie mit `/iteration-start`.

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
