# Phase 5: Evaluation

> **Ziel:** Prüfen, ob die Prognosen gut genug für den geschäftlichen Zweck sind (Backtest).
> **Entscheidung:** gut genug → Phase 6; nicht gut genug → zurück zu Phase 1, 3 oder 4; nicht tragfähig → Idee verwerfen
> oder umbauen.
> Details: [CRISP-DM.md](../CRISP-DM.md#5-evaluation)
>
> **Artefakte laut CRISP-DM.md:** `reports/backtest_iterationN.md` (fehlt)

---

## Aktueller Stand

_Stand: Iteration 2 (Abschluss), 2026-10-23. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Noch nicht begonnen.** Die Kennzahlen (Trefferquote, Präzision, Vorlauf) sind in CRISP-DM.md vorgeschlagen, aber noch
nicht festgelegt. Iteration 2 liefert erste Hinweise zur Backtest-Basis.

### Fakten (aus den Daten)

Quellen: **[K]** [kennzahlen_iteration2.md](../../reports/kennzahlen_iteration2.md), **[Erg]** [ergebnis_iteration2.md](../../reports/ergebnis_iteration2.md),
**[E2]** [evaluation_iteration2.md](../../reports/evaluation_iteration2.md).

- 629 eForms-Zuschläge (Gebäudereinigung) haben ein Laufzeitende bis 23.10.2026. Ihre Median-Laufzeit liegt bei 12 Monaten,
  über alle eForms-Zuschläge bei 36. 410 der 629 stammen aus 2024. 187 haben eine Verlängerungsoption. [K], [E2]
- Die Zuordnung zum Nachfolger gelang über den Auftraggeber nur in 5 von 30 Fällen. [Erg]
- Unter 6 objektgleichen Paaren sind 3 vorzeitige Neuvergaben. Nur bei A13 ist der Vorlauf unabhängig gemessen: 5,1 Monate. [Erg], [E2]
- Bei A2 und A16 lag das Ende der Grundlaufzeit 4,7 bzw. 2,7 Jahre vor der Neuausschreibung (Verlängerungen). [Erg]

### Interpretation

- Ein Backtest nur mit eForms-Daten würde vor allem Einjahresverträge prüfen und wäre stark verzerrt (A10). Daten vor eForms über die
  XML sind voraussichtlich nötig (A11).
- Für den Backtest zählen nur **zuordenbare** Paare. Deren Zahl ist noch unbekannt (Iteration 3).
- Vorzeitige Neuvergaben und Verlängerungen müssen im Backtest eigene Kategorien bekommen, sonst werden sie als Fehlprognose gezählt.

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
