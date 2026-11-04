# Vergabe-Radar

## Idee
Prognose, wann öffentliche Aufträge in Deutschland auslaufen und neu
ausgeschrieben werden, basierend auf Zuschlagsbekanntmachungen aus TED
(Tenders Electronic Daily). Zielgruppe: Mittelständler, die sich früh auf
Neuausschreibungen vorbereiten wollen (z. B. Gebäudereinigung, IT-Wartung,
Winterdienst).

## Aktuelle Phase: nach Iteration 7 (Abschluss mit diesem Stand), vor Iteration 8 (KI-Zweitlesung, Phase 5)
Iteration 5 ist abgeschlossen (Entscheidung: Idee anpassen). Die Punktprognose „Höchstende − 6 Monate“ trägt nicht: Trefferquote ±3 Monate
28,8 % (Schwelle 60 %, naive Referenz 17,3 %) auf 52 handgeprüften Paaren; Abdeckung der Vertragsliste 79,7 % der Lose.
Produktkern: Vertragsliste mit Enddaten (Grundlaufzeit, Höchstende, Herkunft) ohne Terminprognose.
Arbeitsnische: Gebäudereinigung, Haupt-CPV 90910/90911/90919.
Iteration 6 ist abgeschlossen (Entscheidung: zurück zu Phase 3). Prüfung an 60 Zufallslosen: Ende der Grundlaufzeit 54/60 = 90,0 % laut Auswertung,
53/60 = 88,3 % nach dem Fehler L60 (Schwelle 90 %); Höchstende 91,7 %; Abdeckung 79,7 % (Schwelle 80 %); Prototyp der Liste (Oberpfalz) vorhanden, mit bekannten Fehlern.
Fehlertyp: Das Enddatum der Bekanntmachung ist manchmal schon das Höchstende.
Iteration 7 ist abgeschlossen (Entscheidung: Abschluss mit diesem Stand, kein dritter Regelversuch). Regel 1b eingebaut; Ende der Grundlaufzeit 36/47 = 76,6 %
(Mischmaß aus Listen- und Prüfungsfehlern), Regelwirkungs-Lose 8/15, Höchstende verfehlt; Regel 1b weder belegt noch widerlegt. Liste eingefroren (a93785e):
Ende „laut Bekanntmachung“, Höchstende nur Hinweis. Iteration 8 (mit /iteration-start): zwei KI-Leser auf allen 95 Losen als getrennte Messung, Kriterien vorab.
Kein Kundenkontakt (A1/A15 bleiben ungeprüft).
Bewertung als Leistungsnachweis: docs/bewertung_LN.md; Quellen: docs/quellen.md; Reproduzierbarkeit: docs/reproduzierbarkeit.md.
Daten: TED-API ab Okt. 2016; vor eForms Laufzeit über REF_NOTICE.
Details: docs/iterationen.md, reports/evaluation_iteration5.md, reports/evaluation_iteration6.md, reports/evaluation_iteration7.md

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
