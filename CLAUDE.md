# Vergabe-Radar

## Idee
Prognose, wann öffentliche Aufträge in Deutschland auslaufen und neu
ausgeschrieben werden, basierend auf Zuschlagsbekanntmachungen aus TED
(Tenders Electronic Daily). Zielgruppe: Mittelständler, die sich früh auf
Neuausschreibungen vorbereiten wollen (z. B. Gebäudereinigung, IT-Wartung,
Winterdienst).

## Aktuelle Phase: vor Iteration 4, Phase 2/3 (Zuordnung über das Objekt)
Iteration 3 ist abgeschlossen (Entscheidung: in Phase 2/3 bleiben). Objektgleiche
Vorgänger sind auf TED oft sichtbar (63 %, knapp und definitionsabhängig), die
einfache Objekt-Regel ordnet sie aber nicht zuverlässig zu (Präzision 46 %,
Trefferquote 29 %; Fehler meist Geschwisterverfahren, vor eForms fehlen Merkmale).
Arbeitsnische: Gebäudereinigung, Haupt-CPV 90910/90911/90919. Noch kein Modell.
Iteration 4 = letzter Verbesserungsversuch: Merkmale auf Los-Ebene (auch vor
eForms aus XML/Volltextsuche), Leistungsart hart prüfen, kein Zeitfenster;
neue Testdaten Q1 2026, Handsuche und Zweitprüfung nach Urteilsregeln 1.1 vorab.
Parallel in Phase 1: Produkt mit manueller Prüfung bewerten, Gespräche führen.
Daten: TED-API ab Okt. 2016; vor eForms Laufzeit über REF_NOTICE (25/30).
Details: docs/iterationen.md, reports/evaluation_iteration3.md

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
