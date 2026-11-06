# Vergabe-Radar

## Idee
Prognose, wann öffentliche Aufträge in Deutschland auslaufen und neu
ausgeschrieben werden, basierend auf Zuschlagsbekanntmachungen aus TED
(Tenders Electronic Daily). Zielgruppe: Mittelständler, die sich früh auf
Neuausschreibungen vorbereiten wollen (z. B. Gebäudereinigung, IT-Wartung,
Winterdienst).

## Aktuelle Phase: nach Iteration 10/10b und Business-Case-Prüfung, Projektabschluss (Lab-Log, Vortrag)
Iteration 5 ist abgeschlossen (Entscheidung: Idee anpassen). Die Punktprognose „Höchstende − 6 Monate“ trägt nicht: Trefferquote ±3 Monate
28,8 % (Schwelle 60 %, naive Referenz 17,3 %) auf 52 handgeprüften Paaren; Abdeckung der Vertragsliste 79,7 % der Lose.
Produktkern: Vertragsliste mit Enddaten (Grundlaufzeit, Höchstende, Herkunft) ohne Terminprognose.
Arbeitsnische: Gebäudereinigung, Haupt-CPV 90910/90911/90919.
Iteration 6 ist abgeschlossen (Entscheidung: zurück zu Phase 3). Prüfung an 60 Zufallslosen: Ende der Grundlaufzeit 54/60 = 90,0 % laut Auswertung,
53/60 = 88,3 % nach dem Fehler L60 (Schwelle 90 %); Höchstende 91,7 %; Abdeckung 79,7 % (Schwelle 80 %); Prototyp der Liste (Oberpfalz) vorhanden, mit bekannten Fehlern.
Fehlertyp: Das Enddatum der Bekanntmachung ist manchmal schon das Höchstende.
Iteration 7 ist abgeschlossen (Entscheidung: Abschluss mit diesem Stand, kein dritter Regelversuch). Regel 1b eingebaut; Ende der Grundlaufzeit 36/47 = 76,6 %
(Mischmaß aus Listen- und Prüfungsfehlern), Regelwirkungs-Lose 8/15, Höchstende verfehlt; Regel 1b weder belegt noch widerlegt. Liste eingefroren (a93785e):
Ende „laut Bekanntmachung“, Höchstende nur Hinweis.
Iteration 8 ist abgeschlossen (Entscheidung: weiter, Projektabschluss, eingeschränkt formuliert): zwei KI-Leser (Opus, Sonnet) auf allen 95 Losen; Z0 94/95, Z1 77/80, Z3 75/80 und 67/72, Z4 10/10, Z2 14/15 (bei einheitlichem Maßstab 11/15). Leser nicht unabhängig, nicht von Menschen bestätigt; neue Fehlerarten (Lose ohne Zuschlag, Regel 6, „3 Jahre mit Option“) bleiben offene Grenzen. Keine weitere Iteration.
Iteration 9 ist abgeschlossen (Entscheidung: weiter, Projektabschluss, eingeschränkt formuliert): Regeln 6 bis 10, neue Stichprobe (Seed 20261109), KI-Leser ohne Projektkontext, Kommilitone an 15 Losen. V1 66/70 = 94,3 %, V2 28/30, V3 66 gegen 65 (alt), V5 110/110, V6 14/15; V4 und V7 verfehlt, V8 teilweise. Prototyp = Fassung der Iteration 9 (Liste 9.325 Lose), Höchstende nur Hinweis. Keine weitere Iteration.
Iteration 10/10b ist abgeschlossen (Entscheidung: weiter, Projektabschluss, eingeschränkt formuliert; Tag iteration-10): Der Dozent verlangt mehr Business Understanding und Competitive Edge. Konkurrenz Vergabeweiser (kostenlos, API) und AusschreibungsRadar (0 bis 149 €/Monat): Annahme A2 widerlegt, die Liste als eigenes Produkt trägt nicht. Der Vorsprung der Liste ist ein Merkmalsunterschied (Ende je Los, Grundlaufzeit statt Höchstende, ca. 10 % der Lose), kein belegter Qualitätsvorteil. Paket B: 26,7 % der Oberpfälzer Reinigungsverfahren stehen nicht auf TED.
Business-Case-Auswahl (docs/business_case_auswahl.md): kein Kandidat erreicht 8 Punkte, Ergebnis „kein tragfähiger Business Case“; Test K-A nach Vorprüfung abgebrochen (23 von 52 Paaren, Schwelle 30). Sicht eines Betriebs (Make or Buy, Export-Schema 1.1): docs/business.md §9, reports/make_or_buy.md. Hypothesen H1/H2 (A21/A22) ungeprüft; Wizard-of-Oz-Blatt (docs/wizard_of_oz_blatt.md) vorbereitet, nicht durchgeführt.
Demo (docs/demo_push.md, src/demo/): Profil-Match mit KI-Stufe und Push-Nachrichten für die Oberpfalz, offline reproduzierbar, nichts gesendet; nur Veranschaulichung der Datenübergabe, kein Business Case (K7=0).
Kundenkontakt: drei Telefongespräche (n = 3, 2026-11-05, durch den Nutzer); keine Kaltakquise. Projekt ist LN B (Zweierteam Manuel Strobel, Ludwig Richthammer, mit dem Dozenten besprochen). Webseite-Prototyp: docs/prototyp/vertragsliste.html; Vortrag: docs/vortrag/; Lab-Log: docs/lab_log.md/.pdf (aus docs/lab_log_vorlage.md erzeugt). Übergabe an den Kommilitonen: docs/mitarbeit_uebergabe.md.
Bewertung als Leistungsnachweis: docs/bewertung_LN.md; Quellen: docs/quellen.md; Reproduzierbarkeit: docs/reproduzierbarkeit.md.
Daten: TED-API ab Okt. 2016; vor eForms Laufzeit über REF_NOTICE.
Details: docs/iterationen.md, reports/evaluation_iteration5.md, reports/evaluation_iteration6.md, reports/evaluation_iteration7.md, reports/evaluation_iteration8.md, reports/evaluation_iteration9.md, reports/evaluation_iteration10*.md

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
