# Phase 4: Modeling

> **Ziel:** Das erwartete Datum der Neuausschreibung prognostizieren (Stufen: Baseline-Regel → Verlängerungen →
> Auftraggeber-Historie → ggf. ML).
> **Zurück zu Phase 3, wenn:** Das Modell zusätzliche oder anders aufbereitete Merkmale braucht.
> Details: [CRISP-DM.md](../CRISP-DM.md#4-modeling)
>
> **Artefakte laut CRISP-DM.md:** Skripte in `src/model/` (fehlen)

---

## Aktueller Stand

_Stand: Iteration 5 (Abschluss), 2026-11-04. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Baseline getestet und verfehlt.** Stufe 1 und eine Variante von Stufe 2 aus `docs/CRISP-DM.md` sind gelaufen; weitere Stufen sind nicht begründet, solange die Frage nach Nutzen und Prognoseziel offen ist.

Quellen: **[BT5]** [backtest_iteration5.md](../../reports/backtest_iteration5.md) · **[E5]** [evaluation_iteration5.md](../../reports/evaluation_iteration5.md) · **[ZP]** [gt_pruefung_iteration5_auswertung.md](../../reports/gt_pruefung_iteration5_auswertung.md) · **[AN]** [backtest_analysen_iteration5.md](../../reports/backtest_analysen_iteration5.md) · **[VL]** [vertragsliste_iteration5.md](../../reports/vertragsliste_iteration5.md) · **[VP]** [verlaengerung_praxis_iteration5.md](../../reports/verlaengerung_praxis_iteration5.md) · **[HP]** [hoechstende_pruefung_iteration5_test.md](../../reports/hoechstende_pruefung_iteration5_test.md).

### Fakten (aus den Daten)

- Regeln in `src/model/baseline.py` (vor dem ersten Lauf committet): R0 = Ende der Grundlaufzeit − 6 Monate, R1 = Höchstende − 6 Monate (bei unbestimmbarem Höchstende wie R0); Treffer ±3 Monate; keine Parameterschätzung aus den Paaren.
- Ergebnis auf 52 Paaren: R0 17,3 %, R1 28,8 % (Wilson 18,3–42,3); bei belegter Verlängerung (24 Paare) R1 10/24 gegenüber R0 4/24; ohne belegte Verlängerung beide 5/28 [BT5].
- Kein Vorlauf-Parameter rettet das Ergebnis (Streuung zu breit) [E5].

### Interpretation

- Eine feste Vorlaufzeit auf Höchstende oder Grundlaufzeit reicht nicht. Verlängerungstext hilft (datum_text 7/14 gegenüber 1/14), löst aber das Problem nicht.
- Offen: Vorlauf je Auftraggeber (z. B. Bayern 0/5, Bundesanstalt für Immobilienaufgaben 3/4), nur sinnvoll mit Daten zur Ausübung von Optionen.

## Offene Fragen

- [ ] Wie viele Monate vor Vertragsende wird typischerweise neu ausgeschrieben? Das ist der Parameter der Baseline (Annahme A8).
- [ ] Wie gehen wir mit Verlängerungen um: mit oder ohne Ausübung oder beides als Zeitfenster?
- [ ] Wie behandeln wir unbefristete Verträge (BT-538 UNLIMITED, 4,2 %)?

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| – | – | Noch keine Entscheidungen | – |
| 2026-11-04 | 5 | Keine weitere Modellstufe in Iteration 5; Baseline R0/R1 eingefroren und verworfen als Terminprognose (28,8 % < 40 %) | Vorab festgelegte Folge, reports/evaluation_iteration5.md. Entscheidung des Nutzers. |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

_Noch keine Einträge._

### Iteration 5 – 2026-11-04

- **Was gemacht:** Baseline R0/R1 in `src/model/baseline.py` eingefroren, vor dem Lauf committet, dann Backtest auf 52 Paaren.
- **Erkenntnisse – Fakten:** R1 15/52 = 28,8 %, R0 9/52 = 17,3 % (reports/backtest_iteration5.md).
- **Erkenntnisse – Interpretation:** Eine einfache Regel trägt nicht; Verlängerungstext verbessert etwas.
- **Übergabe an die nächste Phase:** Kein Modell für den Prototyp nötig (Liste mit Enddaten). Falls Iteration 6 Prognose weiterverfolgt: Auftraggeber-Verhalten und Optionsausübung.
