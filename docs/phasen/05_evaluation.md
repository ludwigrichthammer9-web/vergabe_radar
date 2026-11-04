# Phase 5: Evaluation

> **Ziel:** Prüfen, ob die Prognosen gut genug für den geschäftlichen Zweck sind (Backtest).
> **Entscheidung:** gut genug → Phase 6; nicht gut genug → zurück zu Phase 1, 3 oder 4; nicht tragfähig → Idee verwerfen
> oder umbauen.
> Details: [CRISP-DM.md](../CRISP-DM.md#5-evaluation)
>
> **Artefakte laut CRISP-DM.md:** `reports/backtest_iterationN.md` (fehlt)

---

## Aktueller Stand

_Stand: Iteration 5 (Abschluss), 2026-11-04. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Erster Backtest durchgeführt.** Kennzahl Trefferquote im Fenster ±3 Monate; Referenz R0; Evaluator-Prüfung liegt vor.

Quellen: **[BT5]** [backtest_iteration5.md](../../reports/backtest_iteration5.md) · **[E5]** [evaluation_iteration5.md](../../reports/evaluation_iteration5.md) · **[ZP]** [gt_pruefung_iteration5_auswertung.md](../../reports/gt_pruefung_iteration5_auswertung.md) · **[AN]** [backtest_analysen_iteration5.md](../../reports/backtest_analysen_iteration5.md) · **[VL]** [vertragsliste_iteration5.md](../../reports/vertragsliste_iteration5.md) · **[VP]** [verlaengerung_praxis_iteration5.md](../../reports/verlaengerung_praxis_iteration5.md) · **[HP]** [hoechstende_pruefung_iteration5_test.md](../../reports/hoechstende_pruefung_iteration5_test.md).

### Fakten (aus den Daten)

- Backtest-Basis: 52 von Rechercheur und Prüfer bestätigte Paare (X1), Zweitprüfung 61/67 = 91,0 % (KI-unterstützt, nicht unabhängig) [ZP].
- Trefferquote R1 28,8 %, R0 17,3 %, Median-Abweichung R1 +0,6 Monate bei zweigipfliger Verteilung (20 früher, 17 später) [BT5].
- Robustheit: 35,9 % ohne unbestimmbare Höchstenden, 41,7 % ohne lange Lücken, 27,5 % mit einem Paar je Auftraggeber [E5], [AN].

### Interpretation

- Verzerrungen: Rückwärtssuche (nur auffindbare Vorgänger), Rechtszensierung, zwei kurze Beobachtungsfenster; die Quote ist keine Präzision eines späteren Produkts.
- Der Median täuscht (Zweigipfligkeit). Die Paare messen Objektidentität, nicht den direkten Vorgänger.

## Offene Fragen

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
