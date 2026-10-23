# Annahmen

Annahmen, auf denen das Vergabe-Radar beruht. Die riskantesten ungeprüften Annahmen sollten zuerst geprüft werden.

- **Risiko:** Wie stark schadet es dem Projekt, wenn die Annahme falsch ist? (hoch / mittel / niedrig)
- **Status:** ungeprüft / bestätigt / widerlegt. Der Status ändert sich nur mit Nachweis.
- **Nachweis:** Quelle wie Report, Datei, Notice-Nummer oder Gesprächsnotiz. Wo der Nachweis nur für einen Teil gilt,
  wird der Geltungsbereich genannt (z. B. Zeitraum).
- Bei Statusänderungen den alten Nachweis nicht löschen, sondern unter „Verlauf“ ergänzen.

Quellen: **[R]** = `reports/datenqualitaet_DEU_20260722_20261021.md`, **[S]** = `reports/stichprobe_iteration1.md`,
**[E]** = `reports/evaluation_iteration1.md`.
Iteration 2: **[RR]** = `reports/rueckreichweite_909.md`, **[K]** = `reports/kennzahlen_iteration2.md`, **[P]** = `reports/k2_pruefliste.md`, **[X]** = `reports/k2_auszuege.md`, **[Erg]** = `reports/ergebnis_iteration2.md`, **[E2]** = `reports/evaluation_iteration2.md`, **[DU]** = `docs/phasen/02_data_understanding.md`.

| ID | Annahme | Risiko | Status | Nachweis | Phase | zuletzt geprüft |
|---|---|---|---|---|---|---|
| A1 | Mittelständler wollen frühzeitig von Neuausschreibungen wissen und zahlen dafür. | hoch | ungeprüft | Noch keine Kundengespräche. Für die Arbeitsnische konkretisiert in A15. | 1 | – |
| A2 | Bestehende Ausschreibungsdienste (z. B. DTAD) bieten keine solchen Prognosen an. | hoch | ungeprüft | – | 1 | – |
| A3 | TED bildet einen relevanten Teil des Markts der Nische ab. Pflicht zur EU-weiten Veröffentlichung besteht nur oberhalb der EU-Schwellenwerte, kleinere Aufträge fehlen. | hoch | ungeprüft | Nicht untersucht. Laut [E] ist das Risiko für Gebäudereinigung eher gestiegen, weil Nachfolgeaufträge unter dem Schwellenwert nicht auf TED erscheinen. **Iteration 2:** Hinweise in beide Richtungen, Sichtbarkeit nicht gemessen. Für Lücken sprechen: 6 von 15 Ausschreibungen ohne Treffer haben per Namenssuche keinen früheren 909-Zuschlag im Pool [P]; in der Gruppe mit 1–2 Kandidaten fehlt 2–3 von 6 ein passender Vorgänger [E2]; seit eForms gibt es ca. 1,6 Ausschreibungs-Notices pro Zuschlag, ungeklärt [RR]. Dagegen spricht A30: Der objektgleiche Vorgänger war vorhanden [E2]. | 1, 2 | 2026-10-23 |
| A4 | Zuschläge in Dienstleistungsnischen enthalten meist ein Vertragsende oder eine Laufzeit. | mittel | bestätigt | Großzügige Definition (Ende oder Dauer): Gebäudereinigung 90,0 %, Winterdienst 93,0 %, Sicherheit 93,4 %, IT-Wartung 83,0 % ([R §4]). Streng „Ende bestimmbar“: 80,9 % / 84,5 % / 83,9 %, IT-Dienste nur 33,7 % ([R §5]). Gilt für 5 Nischen, Haupt-CPV, Notice-Ebene, Veröffentlichung 22.07.–21.10.2026. | 2 | 2026-10-22 |
| A5 | Verlängerungsoptionen lassen sich überwiegend aus dem strukturierten Feld BT-58 ablesen. | mittel | widerlegt | BT-58 nur bei 18,9 % vorhanden, > 0 bei 14,7 % ([R §2]); in Gebäudereinigung > 0 bei 42,0 % ([R §4]), also höher, aber nicht überwiegend. In 505084-2026 steht die Verlängerung nur im Freitext BT-54. | 2, 3 | 2026-10-22 |
| A6 | Angegebene Auftragswerte sind echte Beträge. | niedrig | widerlegt | Platzhalter im Original belegt: 505084-2026 (0,00 € / 0,01 €), 561098-2026 (0,01 €), 702922-2026 (Gesamtwert 0 €) ([S]). Die Quote „2.276 von 10.775 ≤ 1 €“ beruht auf `total-value`, das TED selbst berechnet (kein BT-161, [S]). Sie zeigt also nicht direkt, wie oft Vergabestellen Platzhalter eintragen. | 2 | 2026-10-22 |
| A7 | `-1` in Wertfeldern bedeutet „Wert nicht veröffentlicht“. | niedrig | bestätigt | 684689-2026: `-1` in der XML mit `efac:FieldsPrivacy`, die Website zeigt „Nicht veröffentlicht“. 636832-2026: `-1` ebenfalls in der XML ([S]). Geltungsbereich: 2 Fälle, Wertfelder. Ob jedes `-1` einen FieldsPrivacy-Block hat, ist nicht geprüft. | 2 | 2026-10-22 |
| A8 | Eine Neuausschreibung erscheint ungefähr zum Vertragsende minus einer typischen Vorlaufzeit. | hoch | ungeprüft | **Iteration 2 (n = 6 objektgleiche Paare, Warnsignal):** 3 vorzeitige Neuvergaben (A8, A24, A30). 2 passen nur, wenn alle Verlängerungen ausgeschöpft wurden (A2, A16; das wurde aus dem Datum der neuen Ausschreibung erschlossen, also zirkulär). Nur A13 unabhängig gemessen: 5,1 Monate vor Vertragsende [Erg], [E2]. | 4, 5 | 2026-10-23 |
| A9 | Neuausschreibungen lassen sich zuverlässig dem ursprünglichen Vertrag zuordnen (z. B. über Auftraggeber + CPV). | hoch | **widerlegt** (Variante Auftraggeber + CPV) | K2 = 5/30 = 16,7 % (Wilson 7,3–33,6 %), Schwelle 80 % vorab; im besten Fall 7/30 = 23,3 % [P], [E2]. Geltungsbereich: Haupt-CPV 909, Ausschreibungen Q2 2026, Regel aus `src/zuordnung_prototyp.py` (Name oder Kennung, Top-1-Auswahl). Ursache: Große Auftraggeber vergeben viele Verträge parallel. Die Zuordnung über das Objekt wird als A9b geführt. | 2, 3, 5 | 2026-10-23 |
| A10 | Die eForms-Historie seit Herbst 2023 reicht für einen aussagekräftigen Backtest. | hoch | ungeprüft | Fakt: Gebäudereinigung hat einen Median von 36 Monaten (Quartile 24/48, n = 350, aus Beginn/Ende, [R §5]), BT-58 > 0 bei 42,0 % ([R §4]). Interpretation: Seit Herbst 2023 sind vor allem kurze Verträge ohne Verlängerung vollständig beobachtbar, mit Zensierungsverzerrung ([E]). **Iteration 2:** 629 abgelaufene eForms-Verträge (K5 ≥ 100 erfüllt), davon 187 mit Verlängerungsoption, Median-Laufzeit 12 Monate, 410 aus 2024 [K], [E2]. Zuordenbare Paare nicht gezählt. Anzahl reicht, Repräsentativität nicht. | 2, 5 | 2026-10-23 |
| A11 | TED-Daten vor eForms (vor Herbst 2023) sind für Laufzeiten brauchbar. | hoch | ungeprüft (vorläufig gestützt) | **Iteration 2:** Die Such-API liefert vor eForms keine Laufzeit [DU]. 10 von 10 Zuschlägen vor eForms (F03/F06) verweisen über `REF_NOTICE` auf eine alte Ausschreibung (F02/F05) mit `DATE_START`/`DATE_END`, 5 von 10 mit Verlängerung [X]. Geltungsbereich: von der Auswahlregel gewählte Vorgänger 2017–2023, keine Zufallsstichprobe. Offen: Zuschläge ohne `REF_NOTICE`. | 2 | 2026-10-23 |
| A12 | Der Haupt-CPV-Code der Bekanntmachung reicht, um sie einer Nische zuzuordnen. | mittel | ungeprüft | 15,3 % der Notices haben mehrere Lose ([R §1]). Teilbeleg: 91,8 % der 909-Notices tragen Reinigungs-Codes 90910/90911/90919, 8 nutzen das Formular `can-desg` ([E]). Reinigungslose unter anderem Haupt-CPV sind nicht geprüft. **Iteration 2:** Haupt-CPV 909 enthält auch Schädlingsbekämpfung (A6, A22), Fahrzeug- und Industriereinigung (B4, B15) und einmalige Bau- bzw. Sonderreinigung (B1, B7, B12) [X], [E2]. | 2, 3 | 2026-10-23 |
| A13 | TED-Daten liefern für mindestens eine wiederkehrende Dienstleistungsnische bei ≥ 80 % der Zuschläge ein bestimmbares Laufzeitende (Enddatum, oder Beginn + Dauer). | mittel | **bestätigt** (enger Geltungsbereich) | Replikation mit vorab festgelegter Schwelle: Q2 2025 82,1 % (Wilson 77,9–85,5 %, n = 390) [K]; dazu Q3 2026 80,9 % (KI 77,0–84,3 %) [R §5], [E]. Geltungsbereich: Haupt-CPV 909, Notice-Ebene, Veröffentlichung **ab 2025**. **Gilt nicht** für 2023 (70,7 %) und 2024 (70,1 %, KI 67,8–72,2 %; nachträglich ausgewertet, großes n) [K]. | 2 | 2026-10-23 |
| A14 | TED-Daten reichen für eine brauchbare Prognose der Neuausschreibung in mindestens einer Nische. | hoch | ungeprüft | Oberbegriff aus A3, A8, A9 und A10 ([E]). Prüfbar erst mit messbarem Kriterium, z. B. Trefferquote im ±3-Monats-Fenster. | 2–5 | – |
| A15 | Reinigungsfirmen zahlen für Vorabinformationen über auslaufende Verträge. | hoch | ungeprüft | Noch keine Gespräche mit Reinigungsfirmen. | 1 | – |
| A9b | Neuausschreibungen lassen sich über das Objekt (Adresse, Liegenschaftsname, Titel) automatisch dem Vorgängervertrag zuordnen, auch bei großen Auftraggebern. | hoch | ungeprüft | Neu nach Iteration 2. Hinweise: In 5 plausiblen Paaren und bei A30 stimmen Objekt und Titel überein; 3 der 5 Paare haben höchstens 2 Kandidaten, sind also leichte Fälle [P], [E2]. | 2, 3, 5 | 2026-10-23 |
| A16 | Neuausschreibungen erfolgen überwiegend zum regulären Vertragsende (inkl. Verlängerungen), nicht vorzeitig. | hoch | ungeprüft | Neu nach Iteration 2. Warnsignal: 3 von 6 objektgleichen Paaren vorzeitig neu vergeben (A8, A24, A30) [Erg], [E2]. | 1, 4, 5 | 2026-10-23 |

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
- 2026-10-23, A9: ungeprüft → widerlegt für die Variante Auftraggeber + CPV (Iteration 2, K2 = 16,7 %); Objektebene als A9b neu
- 2026-10-23, A13: ungeprüft → bestätigt mit engem Geltungsbereich (ab 2025; Replikation Q2 2025 mit Vorab-Schwelle; nicht für 2023/2024)
- 2026-10-23, A11: Status ungeprüft, Vermerk „vorläufig gestützt“ (10/10 nicht zufällig, REF_NOTICE → F02/F05)
- 2026-10-23, A3, A8, A10, A12: Status unverändert, Nachweis aus Iteration 2 ergänzt
- 2026-10-23, A9b: neu, ungeprüft, Risiko hoch
- 2026-10-23, A16: neu, ungeprüft, Risiko hoch
