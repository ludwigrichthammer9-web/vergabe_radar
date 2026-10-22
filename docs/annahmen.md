# Annahmen

Annahmen, auf denen das Vergabe-Radar beruht. Die riskantesten ungeprüften Annahmen sollten zuerst geprüft werden.

- **Risiko:** Wie stark schadet es dem Projekt, wenn die Annahme falsch ist? (hoch / mittel / niedrig)
- **Status:** ungeprüft / bestätigt / widerlegt. Der Status ändert sich nur mit Nachweis.
- **Nachweis:** Quelle wie Report, Datei, Notice-Nummer oder Gesprächsnotiz. Wo der Nachweis nur für einen Teil gilt,
  wird der Geltungsbereich genannt (z. B. Zeitraum).
- Bei Statusänderungen den alten Nachweis nicht löschen, sondern unter „Verlauf“ ergänzen.

Quellen: **[R]** = `reports/datenqualitaet_DEU_20260722_20261021.md`, **[S]** = `reports/stichprobe_iteration1.md`,
**[E]** = `reports/evaluation_iteration1.md`.

| ID | Annahme | Risiko | Status | Nachweis | Phase | zuletzt geprüft |
|---|---|---|---|---|---|---|
| A1 | Mittelständler wollen frühzeitig von Neuausschreibungen wissen und zahlen dafür. | hoch | ungeprüft | Noch keine Kundengespräche. Für die Arbeitsnische konkretisiert in A15. | 1 | – |
| A2 | Bestehende Ausschreibungsdienste (z. B. DTAD) bieten keine solchen Prognosen an. | hoch | ungeprüft | – | 1 | – |
| A3 | TED bildet einen relevanten Teil des Markts der Nische ab. Pflicht zur EU-weiten Veröffentlichung besteht nur oberhalb der EU-Schwellenwerte, kleinere Aufträge fehlen. | hoch | ungeprüft | Nicht untersucht. Laut [E] ist das Risiko für Gebäudereinigung eher gestiegen, weil Nachfolgeaufträge unter dem Schwellenwert nicht auf TED erscheinen. | 1, 2 | 2026-10-22 |
| A4 | Zuschläge in Dienstleistungsnischen enthalten meist ein Vertragsende oder eine Laufzeit. | mittel | bestätigt | Großzügige Definition (Ende oder Dauer): Gebäudereinigung 90,0 %, Winterdienst 93,0 %, Sicherheit 93,4 %, IT-Wartung 83,0 % ([R §4]). Streng „Ende bestimmbar“: 80,9 % / 84,5 % / 83,9 %, IT-Dienste nur 33,7 % ([R §5]). Gilt für 5 Nischen, Haupt-CPV, Notice-Ebene, Veröffentlichung 22.07.–21.10.2026. | 2 | 2026-10-22 |
| A5 | Verlängerungsoptionen lassen sich überwiegend aus dem strukturierten Feld BT-58 ablesen. | mittel | widerlegt | BT-58 nur bei 18,9 % vorhanden, > 0 bei 14,7 % ([R §2]); in Gebäudereinigung > 0 bei 42,0 % ([R §4]), also höher, aber nicht überwiegend. In 505084-2026 steht die Verlängerung nur im Freitext BT-54. | 2, 3 | 2026-10-22 |
| A6 | Angegebene Auftragswerte sind echte Beträge. | niedrig | widerlegt | Platzhalter im Original belegt: 505084-2026 (0,00 € / 0,01 €), 561098-2026 (0,01 €), 702922-2026 (Gesamtwert 0 €) ([S]). Die Quote „2.276 von 10.775 ≤ 1 €“ beruht auf `total-value`, das TED selbst berechnet (kein BT-161, [S]). Sie zeigt also nicht direkt, wie oft Vergabestellen Platzhalter eintragen. | 2 | 2026-10-22 |
| A7 | `-1` in Wertfeldern bedeutet „Wert nicht veröffentlicht“. | niedrig | bestätigt | 684689-2026: `-1` in der XML mit `efac:FieldsPrivacy`, die Website zeigt „Nicht veröffentlicht“. 636832-2026: `-1` ebenfalls in der XML ([S]). Geltungsbereich: 2 Fälle, Wertfelder. Ob jedes `-1` einen FieldsPrivacy-Block hat, ist nicht geprüft. | 2 | 2026-10-22 |
| A8 | Eine Neuausschreibung erscheint ungefähr zum Vertragsende minus einer typischen Vorlaufzeit. | hoch | ungeprüft | – (ohne competition-Daten nicht prüfbar) | 4, 5 | – |
| A9 | Neuausschreibungen lassen sich zuverlässig dem ursprünglichen Vertrag zuordnen (z. B. über Auftraggeber + CPV). | hoch | ungeprüft | Noch kein Paar aus Zuschlag und Neuausschreibung gesucht. Laut [E] ist das die riskanteste und am leichtesten prüfbare Annahme. | 2, 3, 5 | 2026-10-22 |
| A10 | Die eForms-Historie seit Herbst 2023 reicht für einen aussagekräftigen Backtest. | hoch | ungeprüft | Fakt: Gebäudereinigung hat einen Median von 36 Monaten (Quartile 24/48, n = 350, aus Beginn/Ende, [R §5]), BT-58 > 0 bei 42,0 % ([R §4]). Interpretation: Seit Herbst 2023 sind vor allem kurze Verträge ohne Verlängerung vollständig beobachtbar, mit Zensierungsverzerrung ([E]). | 2, 5 | 2026-10-22 |
| A11 | TED-Daten vor eForms (vor Herbst 2023) sind für Laufzeiten brauchbar. | hoch | ungeprüft | – (nicht untersucht; wichtiger geworden, falls A10 nicht trägt, [E]) | 2 | – |
| A12 | Der Haupt-CPV-Code der Bekanntmachung reicht, um sie einer Nische zuzuordnen. | mittel | ungeprüft | 15,3 % der Notices haben mehrere Lose ([R §1]). Teilbeleg: 91,8 % der 909-Notices tragen Reinigungs-Codes 90910/90911/90919, 8 nutzen das Formular `can-desg` ([E]). Reinigungslose unter anderem Haupt-CPV sind nicht geprüft. | 2, 3 | 2026-10-22 |
| A13 | TED-Daten liefern für mindestens eine wiederkehrende Dienstleistungsnische bei ≥ 80 % der Zuschläge ein bestimmbares Laufzeitende (Enddatum, oder Beginn + Dauer). | mittel | ungeprüft | **Vorläufig gestützt, nicht bestätigt:** Gebäudereinigung 80,9 % (95-%-KI 77,0–84,3 %), Winterdienst 84,5 %, Sicherheit 83,9 % ([R §5], [E]). Schwelle nachträglich gesetzt, Notice-Ebene, nur 22.07.–21.10.2026. Bestätigen durch Replikation in einem unabhängigen Zeitfenster mit vorab festgelegter Schwelle. | 2 | 2026-10-22 |
| A14 | TED-Daten reichen für eine brauchbare Prognose der Neuausschreibung in mindestens einer Nische. | hoch | ungeprüft | Oberbegriff aus A3, A8, A9 und A10 ([E]). Prüfbar erst mit messbarem Kriterium, z. B. Trefferquote im ±3-Monats-Fenster. | 2–5 | – |
| A15 | Reinigungsfirmen zahlen für Vorabinformationen über auslaufende Verträge. | hoch | ungeprüft | Noch keine Gespräche mit Reinigungsfirmen. | 1 | – |

## Verlauf

<!-- Nur ergänzen: Datum, ID, alter Status → neuer Status, Grund. -->

- 2026-10-22, A4: ungeprüft → bestätigt (Iteration 1, Vollständigkeitsanalyse)
- 2026-10-22, A5: ungeprüft → widerlegt (Iteration 1, Vollständigkeitsanalyse und Stichprobe 505084-2026)
- 2026-10-22, A6: ungeprüft → widerlegt (Iteration 1, Platzhalterwerte ≤ 1 €)
- 2026-10-22, A7: ungeprüft → bestätigt (Iteration 1 Abschluss, Parsing-Stichprobe: FieldsPrivacy bei 684689-2026; Geltungsbereich 2 Fälle)
- 2026-10-22, A4, A5, A6: Status unverändert, Nachweis präzisiert bzw. korrigiert (`total-value` ist kein BT-161; strenge Quote ergänzt)
- 2026-10-22, A9: neu formuliert („zuverlässig dem ursprünglichen Vertrag zuordnen“), Status ungeprüft, Risiko hoch
- 2026-10-22, A10: Nachweis ersetzt. Vorher Gesamt-Median 24 Monate, laut [E] die falsche Bezugsgröße; jetzt Gebäudereinigung 36 Monate aus Beginn/Ende.
- 2026-10-22, A11: Risiko mittel → hoch (wird wichtig, falls die eForms-Historie für den Backtest nicht reicht)
- 2026-10-22, A13: neu, ungeprüft (vorläufig gestützt; Evaluator rät von „bestätigt“ ab, Entscheidung des Nutzers)
- 2026-10-22, A14: neu, ungeprüft, Risiko hoch
- 2026-10-22, A15: neu, ungeprüft, Risiko hoch
