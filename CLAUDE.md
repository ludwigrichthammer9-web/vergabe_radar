# Vergabe-Radar

## Idee
Prognose, wann öffentliche Aufträge in Deutschland auslaufen und neu
ausgeschrieben werden, basierend auf Zuschlagsbekanntmachungen aus TED
(Tenders Electronic Daily). Zielgruppe: Mittelständler, die sich früh auf
Neuausschreibungen vorbereiten wollen (z. B. Gebäudereinigung, IT-Wartung,
Winterdienst).

## Aktuelle Phase: Iteration 3, Phase 2 (Data Understanding)
Iteration 2 ist abgeschlossen (Entscheidung: Idee anpassen). Die Zuordnung
über den Auftraggeber trifft den Vorgänger nur in 17 % der Fälle. Vorläufige
Arbeitsnische bleibt Gebäudereinigung (Haupt-CPV 909…, enger abzugrenzen).
Noch kein Modell. Als Nächstes getrennt messen:
- Gibt es zu Ausschreibungen überhaupt einen objektgleichen Vorgänger auf TED
  (unter Zuschlägen und früheren Ausschreibungen)?
- Lässt sich der Vorgänger über das Objekt (Adresse, Liegenschaft, Titel)
  automatisch zuordnen?
Bei zu geringer Sichtbarkeit: nationale Quellen oder Auftraggeber-Zyklen.
Daten: TED-API ab Okt. 2016; vor eForms Laufzeit nur in der XML (REF_NOTICE).
Details: docs/iterationen.md, reports/ergebnis_iteration2.md

## Später geplant
- Nische wählen, Backtest (erwartetes Auslaufdatum vs. tatsächliche
  Neuausschreibung), einfache monatliche Vertragsliste als erstes Produkt.

## Regeln für die Zusammenarbeit
- Vor dem Coden die aktuelle TED-API-Dokumentation prüfen, nicht aus dem
  Gedächtnis arbeiten.
- Rohdaten immer unverändert in data/raw speichern, Auswertungen getrennt.
- Python, Abhängigkeiten in requirements.txt festhalten.
- Kurz erklären, was du tust, ich bin Student und lerne dabei.

## Prozess und Dokumentation (CRISP-DM, iterativ)
- Grobplanung (Aufgaben, Stränge, Entscheidungstore): docs/projektplan.md, erledigte Punkte dort abhaken.
- Vorgehen: docs/CRISP-DM.md. Stand je Phase: docs/phasen/01_… bis 06_…,
  Iterationen: docs/iterationen.md, Annahmen: docs/annahmen.md.
- Iteration mit /iteration-start beginnen und mit /iteration-ende abschließen;
  Ergebnisse vom Subagenten evaluator kritisch prüfen lassen.
- In allen Dokumenten Fakten (mit Quelle) und Interpretationen trennen.
  Iterationslogs nur ergänzen, nie überschreiben.
