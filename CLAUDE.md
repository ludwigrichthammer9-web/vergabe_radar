# Vergabe-Radar

## Idee
Prognose, wann öffentliche Aufträge in Deutschland auslaufen und neu
ausgeschrieben werden, basierend auf Zuschlagsbekanntmachungen aus TED
(Tenders Electronic Daily). Zielgruppe: Mittelständler, die sich früh auf
Neuausschreibungen vorbereiten wollen (z. B. Gebäudereinigung, IT-Wartung,
Winterdienst).

## Aktuelle Phase: nach Iteration 5, vor Iteration 6 (Phase 1: Idee anpassen)
Iteration 5 ist abgeschlossen (Entscheidung: Idee anpassen). Die Punktprognose „Höchstende − 6 Monate“ trägt nicht: Trefferquote ±3 Monate
28,8 % (Schwelle 60 %, naive Referenz 17,3 %) auf 52 handgeprüften Paaren; Abdeckung der Vertragsliste 79,7 % der Lose.
Produktkern: Vertragsliste mit Enddaten (Grundlaufzeit, Höchstende, Herkunft) ohne Terminprognose.
Arbeitsnische: Gebäudereinigung, Haupt-CPV 90910/90911/90919.
Iteration 6 wird mit /iteration-start neu zugeschnitten (Kriterium für eine Liste ohne Prognose; Prognose je Auftraggeber nur bei Begründung).
Kein Kundenkontakt (Iteration 7 = Prototyp, A1/A15 bleiben ungeprüft).
Bewertung als Leistungsnachweis: docs/bewertung_LN.md; Quellen: docs/quellen.md; Reproduzierbarkeit: docs/reproduzierbarkeit.md.
Daten: TED-API ab Okt. 2016; vor eForms Laufzeit über REF_NOTICE.
Details: docs/iterationen.md, reports/evaluation_iteration5.md

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
