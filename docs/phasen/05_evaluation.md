# Phase 5: Evaluation

> **Ziel:** Prüfen, ob die Prognosen gut genug für den geschäftlichen Zweck sind (Backtest).
> **Entscheidung:** gut genug → Phase 6; nicht gut genug → zurück zu Phase 1, 3 oder 4; nicht tragfähig → Idee verwerfen
> oder umbauen.
> Details: [CRISP-DM.md](../CRISP-DM.md#5-evaluation)
>
> **Artefakte laut CRISP-DM.md:** `reports/backtest_iterationN.md` (fehlt)

---

## Aktueller Stand

_Stand: Iteration 6 (Abschluss), 2026-11-04. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Zwei Messungen liegen vor:** der Backtest der Terminprognose (Iteration 5, verworfen) und die Handprüfung der Vertragsliste an 60 Zufallslosen (Iteration 6, Y1 bis Y4). Beide wurden vom Evaluator geprüft; die Liste muss nach der Evaluation zurück in Phase 3.

Quellen: **[BT5]** [backtest_iteration5.md](../../reports/backtest_iteration5.md) · **[E5]** [evaluation_iteration5.md](../../reports/evaluation_iteration5.md) · **[ZP]** [gt_pruefung_iteration5_auswertung.md](../../reports/gt_pruefung_iteration5_auswertung.md) · **[AN]** [backtest_analysen_iteration5.md](../../reports/backtest_analysen_iteration5.md) · **[VL]** [vertragsliste_iteration5.md](../../reports/vertragsliste_iteration5.md) · **[VP]** [verlaengerung_praxis_iteration5.md](../../reports/verlaengerung_praxis_iteration5.md) · **[HP]** [hoechstende_pruefung_iteration5_test.md](../../reports/hoechstende_pruefung_iteration5_test.md).
Iteration 6: **[LA6]** [liste_auswertung_iteration6.md](../../reports/liste_auswertung_iteration6.md) · **[E6]** [evaluation_iteration6.md](../../reports/evaluation_iteration6.md) · **[BL]** [beispiel_liste.md](../../reports/beispiel_liste.md) · **[XP6]** [explorativ_iteration6.md](../../reports/explorativ_iteration6.md).

### Fakten (aus den Daten)

- Backtest-Basis: 52 von Rechercheur und Prüfer bestätigte Paare (X1), Zweitprüfung 61/67 = 91,0 % (KI-unterstützt, nicht unabhängig) [ZP].
- Trefferquote R1 28,8 %, R0 17,3 %, Median-Abweichung R1 +0,6 Monate bei zweigipfliger Verteilung (20 früher, 17 später) [BT5].
- Robustheit: 35,9 % ohne unbestimmbare Höchstenden, 41,7 % ohne lange Lücken, 27,5 % mit einem Paar je Auftraggeber [E5], [AN].
- **Iteration 6 (Qualität der Liste, 60 Zufallslose, Prüfer ohne KI-Hilfe laut eigener Angabe):** Y1 Ende der Grundlaufzeit 54/60 = 90,0 % laut Auswertung, **53/60 = 88,3 %** (Wilson 77,8–94,2) nach dem Fehler L60; Y2 Höchstende 55/60 = 91,7 % (nur auf die 51 Lose mit behauptetem Höchstende bezogen: 46/51 = 90,2 %); Y3 Abdeckung 79,7 %; Y4 Prototyp vorhanden [LA6], [E6], [VL], [BL].
- Explorativ: bundesweit 1.368 Lose mit Ende der Grundlaufzeit in den nächsten 12 Monaten, 3.024 in 24 Monaten; 32/52 Backtest-Paare im Fenster „GL − 12 bis Höchstende + 12 Monate“ (Regel für unbestimmbare Höchstenden nicht vorab festgelegt) [XP6].

### Interpretation

- Verzerrungen: Rückwärtssuche (nur auffindbare Vorgänger), Rechtszensierung, zwei kurze Beobachtungsfenster; die Quote ist keine Präzision eines späteren Produkts.
- Der Median täuscht (Zweigipfligkeit). Die Paare messen Objektidentität, nicht den direkten Vorgänger.
- **Iteration 6:** Y1 ist nicht belastbar: Die Vorlage zeigte das Enddatum der Liste (bei 59 von 60 Losen der Wert der Liste), die Stichprobe enthält 0 Lose vor eForms, große Bekanntmachungen sind untergewichtet, und das Feld „Hilfsmittel“ blieb leer. Die Quote ist eher eine Untergrenze der Fehler. Y2 profitiert von der Kategorie „unbestimmbar“. Eine Prüfung der Unabhängigkeit (A18) hat Teil B wegen eines Aufbaufehlers nicht geleistet.

## Offene Fragen

- [ ] _(neu, Iteration 6)_ Wie wird die Genauigkeit der Liste ohne Verankerung gemessen (Vorlage ohne Listenwerte), mit Vor-eForms-Losen und mit nach Losen gewichteten großen Bekanntmachungen?
- [ ] _(neu, Iteration 6)_ Wie wird A18 wirklich unabhängig geprüft (Paare, die der Prüfer noch nicht kennt)?
- [ ] Welches Zeitfenster gilt als Treffer (z. B. ±3 Monate)? Das wird in Phase 1 festgelegt.
- [ ] Reicht die eForms-Historie für einen aussagekräftigen Backtest, oder brauchen wir ältere TED-Daten (Annahme A10, A11)?
- [ ] Wie gehen wir mit Verträgen um, die nicht neu ausgeschrieben wurden (Verlängerung, Wegfall, nationale Vergabe)?
- [ ] _(neu, Iteration 2)_ Wie werden vorzeitige Neuvergaben im Backtest gewertet (eigene Kategorie, nicht Fehlprognose)?
  3 von 6 objektgleichen Paaren waren vorzeitig (A16).
- [ ] _(neu, Iteration 2)_ Wie viele **zuordenbare** Paare mit bekanntem Vorgänger-Ende gibt es (Backtest-Basis laut Projektplan,
  statt nur abgelaufener Verträge wie in K5)?
- [ ] _(aus Iteration 1)_ Wie vermeiden wir Zensierungsverzerrung? Bei Gebäudereinigung (Median 36 Monate) sind seit Herbst 2023
  überwiegend kurze Verträge vollständig beobachtbar. Eine noch nicht erschienene Neuausschreibung darf nicht als Fehlprognose zählen.
  (reports/evaluation_iteration1.md, Schwäche 3)

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| – | – | Noch keine Entscheidungen | – |
| 2026-10-23 | 2 | Backtest erst nach belegter Zuordnung über das Objekt; vorzeitige Neuvergaben werden später als eigene Kategorie geführt | K2 = 16,7 %, 3 von 6 objektgleichen Paaren vorzeitig (reports/evaluation_iteration2.md) |
| 2026-11-04 | 5 | Trefferdefinition ±3 Monate um R0/R1; Backtest nur auf von zwei Prüfern bestätigten Paaren; Köder zur Kontrolle der Prüfung; Median nicht als Stützung werten | Vorab festgelegt (docs/business.md §7.1); Evaluator (reports/evaluation_iteration5.md) |
| 2026-11-04 | 6 | Y1 gilt nach der Korrektur um L60 als verfehlt (53/60 = 88,3 %); Y2 formal erfüllt; Y3 knapp verfehlt; die Prüfung wird mit Vorlage ohne Listenwerte wiederholt | Evaluator (reports/evaluation_iteration6.md); Entscheidung des Nutzers „zurück zu Phase 3“ |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

_Noch keine Einträge._

### Iteration 2 – 2026-10-23

- **Was gemacht:** Kein Backtest. Backtest-Basis (K5) und erste objektgleiche Paare aus Phase 2 ausgewertet.
- **Erkenntnisse – Fakten:**
  - 629 abgelaufene eForms-Verträge, Median-Laufzeit 12 Monate.
  - 3 von 6 objektgleichen Paaren vorzeitig neu vergeben.
  - Vorlauf unabhängig gemessen nur einmal: 5,1 Monate (A13).

  Quellen: [K], [Erg], [E2].
- **Erkenntnisse – Interpretation:** Die eForms-Daten allein ergeben keine unverzerrte Backtest-Basis. Das Prognoseziel muss
  vorzeitige Neuvergaben und Verlängerungen berücksichtigen.
- **Übergabe an die nächste Phase:** Iteration 3 (Phase 2) zählt zuordenbare Paare mit bekanntem Vorgänger-Ende und den Anteil
  vorzeitiger Neuvergaben.

### Iteration 5 – 2026-11-04

- **Was gemacht:** Backtest R0/R1 auf 52 Paaren (`reports/backtest_iteration5.md`), nachträgliche Analysen (`reports/backtest_analysen_iteration5.md`), Evaluator.
- **Erkenntnisse – Fakten:** R1 28,8 %, R0 17,3 %, X3 verfehlt; Ergebnis robust gegen Ausreißer, Vorlauf und Auftraggeber-Gewichtung (reports/evaluation_iteration5.md).
- **Erkenntnisse – Interpretation:** Die Terminprognose „Höchstende − 6 Monate“ wird verworfen; Selektion und nicht direkte Vorgänger verzerren die Quote in unbekannter Richtung.
- **Übergabe an die nächste Phase:** Backtest-Kennzahlen für spätere Varianten bleiben vergleichbar (gleiche Paare, gleiche Definition). Für den Prototyp: Prüfung der Liste selbst gegen den Backtest.

### Iteration 6 – 2026-11-04

- **Was gemacht:** Handprüfung der Vertragsliste an 60 Zufallslosen ausgewertet (Y1, Y2), Abdeckung Y3 aus Iteration 5 übernommen, Prototyp bewertet (Y4), Evaluator; explorative Kennzahlen als Skript (`src/prepare/explorativ_iteration6.py`).
- **Erkenntnisse – Fakten:** Y1 54/60 = 90,0 % laut Auswertung und 53/60 = 88,3 % nach L60; Y2 55/60 = 91,7 %; Y3 79,7 %; Y4 erfüllt mit bekannten Fehlern im Prototyp. Hypothese und Kriterien seit 6baaab5 unverändert (reports/liste_auswertung_iteration6.md, reports/evaluation_iteration6.md).
- **Erkenntnisse – Interpretation:** Die Hypothese ist nicht bestätigt. Y1 ist durch Verankerung und fehlende Vor-eForms-Lose nicht belastbar, Y2 durch „unbestimmbar“ begünstigt. Ob eine Liste ohne Prognose Nutzen hat, bleibt offen (A1, A15 außerhalb des Projektumfangs).
- **Übergabe an die nächste Phase:** Zurück zu Phase 3 (Regel erweitern, neue Stichprobe ohne Listenwerte); danach erneute Evaluation mit denselben Kriterien Y1 bis Y3 an neuen Losen.
