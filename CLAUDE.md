# Vergabe-Radar

## Idee
Prognose, wann öffentliche Aufträge in Deutschland auslaufen und neu
ausgeschrieben werden, basierend auf Zuschlagsbekanntmachungen aus TED
(Tenders Electronic Daily). Zielgruppe: Mittelständler, die sich früh auf
Neuausschreibungen vorbereiten wollen (z. B. Gebäudereinigung, IT-Wartung,
Winterdienst).

## Aktuelle Phase: vor Iteration 5, zuerst Phase 1 (Idee anpassen)
Iteration 4 ist abgeschlossen (Entscheidung: Idee anpassen). Die automatische
Zuordnung über das Objekt wird nicht weiter verbessert: Präzision 89,5 % bei nur
19 Vorschlägen, Trefferquote 56,7 %, Zweitprüfung durch den Nutzer 65 % (< 85 %).
Sichtbare Vorgänger nach Urteilsregeln 1.1: 43 % der Ausschreibungen.
Arbeitsnische: Gebäudereinigung, Haupt-CPV 90910/90911/90919. Noch kein Modell.
Iteration 5 = Vertragsliste aus Zuschlägen (Laufzeitende meist bestimmbar):
zuerst Prognoseziel festlegen (Grundlaufzeit oder Höchstende), dann Tabelle je
Los, einfache Regel, Backtest nur auf unabhängig handgeprüften Paaren.
Kein Kundenkontakt (Iteration 7 = Prototyp, A1/A15 bleiben ungeprüft).
Daten: TED-API ab Okt. 2016; vor eForms Laufzeit über REF_NOTICE (25/30).
Details: docs/iterationen.md, reports/evaluation_iteration4.md

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
