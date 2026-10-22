# Phase 4: Modeling

> **Ziel:** Das erwartete Datum der Neuausschreibung prognostizieren (Stufen: Baseline-Regel → Verlängerungen →
> Auftraggeber-Historie → ggf. ML).
> **Zurück zu Phase 3, wenn:** Das Modell zusätzliche oder anders aufbereitete Merkmale braucht.
> Details: [CRISP-DM.md](../CRISP-DM.md#4-modeling)
>
> **Artefakte laut CRISP-DM.md:** Skripte in `src/model/` (fehlen)

---

## Aktueller Stand

_Stand: Iteration 1, 2026-10-22. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Noch nicht begonnen.**

### Fakten (aus den Daten)

- Median-Laufzeit laut BT-36: 24 Monate (n = 3.349), Quartile 8 bzw. 48 Monate. [Report §2]
- Für die Baseline-Regel (Beginn + Laufzeit − Vorlaufzeit) ist Ende oder Dauer bei 82,0 % aller Notices vorhanden,
  in Dienstleistungsnischen bei 90–93 %. [Report §2, §4]

### Interpretation

- Die Baseline-Regel ist von der Datenlage her umsetzbar. Die Vorlaufzeit ist unbekannt.

## Offene Fragen

- [ ] Wie viele Monate vor Vertragsende wird typischerweise neu ausgeschrieben? Das ist der Parameter der Baseline (Annahme A8).
- [ ] Wie gehen wir mit Verlängerungen um: mit oder ohne Ausübung oder beides als Zeitfenster?
- [ ] Wie behandeln wir unbefristete Verträge (BT-538 UNLIMITED, 4,2 %)?

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| – | – | Noch keine Entscheidungen | – |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

_Noch keine Einträge._
