# Phase 5: Evaluation

> **Ziel:** Prüfen, ob die Prognosen gut genug für den geschäftlichen Zweck sind (Backtest).
> **Entscheidung:** gut genug → Phase 6; nicht gut genug → zurück zu Phase 1, 3 oder 4; nicht tragfähig → Idee verwerfen
> oder umbauen.
> Details: [CRISP-DM.md](../CRISP-DM.md#5-evaluation)
>
> **Artefakte laut CRISP-DM.md:** `reports/backtest_iterationN.md` (fehlt)

---

## Aktueller Stand

_Stand: Iteration 1, 2026-10-22. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Noch nicht begonnen.** Die Kennzahlen (Trefferquote, Präzision, Vorlauf) sind in CRISP-DM.md vorgeschlagen, aber noch
nicht festgelegt.

### Fakten (aus den Daten)

- Bisher gibt es nur Daten aus 3 Monaten (22.07.–21.10.2026). Ein Backtest ist damit nicht möglich. [request_meta.json]
- Median-Laufzeit 24 Monate, 75 %-Quantil 48 Monate (BT-36). [Report §2]

### Interpretation

- Ein Backtest braucht Verträge, deren Laufzeit inzwischen abgelaufen ist und die neu ausgeschrieben wurden. Mit
  eForms-Daten seit Herbst 2023 kommen dafür vor allem kurze Verträge (≤ 2–3 Jahre) in Frage. Längere Verträge
  wären unterrepräsentiert, was den Backtest verzerren kann (Annahme A10).

## Offene Fragen

- [ ] Welches Zeitfenster gilt als Treffer (z. B. ±3 Monate)? Das wird in Phase 1 festgelegt.
- [ ] Reicht die eForms-Historie für einen aussagekräftigen Backtest, oder brauchen wir ältere TED-Daten (Annahme A10, A11)?
- [ ] Wie gehen wir mit Verträgen um, die nicht neu ausgeschrieben wurden (Verlängerung, Wegfall, nationale Vergabe)?
- [ ] _(aus Iteration 1)_ Wie vermeiden wir Zensierungsverzerrung? Bei Gebäudereinigung (Median 36 Monate) sind seit Herbst 2023
  überwiegend kurze Verträge vollständig beobachtbar. Eine noch nicht erschienene Neuausschreibung darf nicht als Fehlprognose zählen.
  (reports/evaluation_iteration1.md, Schwäche 3)

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| – | – | Noch keine Entscheidungen | – |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

_Noch keine Einträge._
