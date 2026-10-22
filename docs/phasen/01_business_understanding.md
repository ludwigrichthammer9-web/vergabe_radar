# Phase 1: Business Understanding

> **Ziel:** Klären, welches Problem für wen gelöst wird und woran Erfolg gemessen wird.
> **Weiter, wenn:** Nische und messbare Erfolgskriterien schriftlich feststehen.
> Details: [CRISP-DM.md](../CRISP-DM.md#1-business-understanding)
>
> **Artefakte laut CRISP-DM.md:** `docs/business.md` (fehlt noch)

---

## Aktueller Stand

_Stand: Iteration 1 (Abschluss), 2026-10-22. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Arbeitsnische (vorläufig): Gebäudereinigung, Haupt-CPV 909….** Die Wahl beruht nur auf Daten. Kundensicht, Wettbewerb und
geschäftliche Erfolgskriterien fehlen noch, das Phase-1-Gate aus CRISP-DM.md ist also nicht erfüllt.

### Fakten (aus den Daten)

Quellen: **[R]** = [Datenqualitätsreport](../../reports/datenqualitaet_DEU_20260722_20261021.md),
**[E]** = [Evaluation](../../reports/evaluation_iteration1.md). Zeitraum der Daten: Zuschläge vom 22.07. bis 21.10.2026.

| Nische (Haupt-CPV) | Zuschläge in 3 Monaten | Laufzeitende bestimmbar¹ | 95-%-KI | Median-Laufzeit aus Beginn/Ende | BT-58 > 0 |
|---|---|---|---|---|---|
| Gebäudereinigung (909) | 440 | 80,9 % | 77,0–84,3 % | 36 Mon. (n = 350) | 42,0 % |
| Winterdienst (9062, 9063) | 129 | 84,5 % | 77,3–89,7 % | 36 Mon. (n = 109) | 33,3 % |
| Sicherheitsdienste (7971) | 137 | 83,9 % | 76,9–89,2 % | 24 Mon. (n = 115) | 42,3 % |
| IT-Dienste (72) | 575 | 33,7 % | – | 36 Mon. (n = 185) | 34,3 % |
| IT-Wartung/Support (503, 7225, 72267) | 47 | 29,8 % | – | 44 Mon. (n = 14) | 29,8 % |
| Kantinenbetrieb | nicht ausgewertet | | | | |

¹ Enddatum vorhanden oder Beginn und Dauer vorhanden. Quelle: [R §5]; KI aus [E]; BT-58: [R §4].

- 91,8 % der 909-Notices tragen Reinigungs-Codes 90910/90911/90919. [E]
- Kundengespräche: 0. Wettbewerberprüfung: nicht begonnen.

### Interpretation

- Gebäudereinigung ist die häufigste Kandidaten-Nische, rund 3-mal so häufig wie Winterdienst oder Sicherheitsdienste.
  Bei der Datenqualität unterscheidet sie sich nicht erkennbar von diesen beiden, die Intervalle überlappen. [E]
- Winterdienst ist im Herbstfenster vermutlich saisonal überzeichnet. [E]
- IT-Dienste und IT-Wartung geben die Laufzeit meist nur als Dauer ohne Beginn an. Für eine Prognose sind sie ohne Zusatzannahmen
  ungeeignet.
- Ob die Nische geschäftlich trägt, also Zahlungsbereitschaft vorhanden ist und Nachfolgeaufträge auf TED sichtbar sind, ist offen.

## Ideen für später

- **Facility-Services-Radar:** Gebäudereinigung, Sicherheitsdienste und Winterdienst gemeinsam abdecken. Bei diesen Leistungen sind oft
  dieselben Auftraggeber (z. B. Liegenschaftsverwaltungen) und dieselben Anbieter aktiv. Die Datenlage ist in allen drei ähnlich
  ([R §5]). _Idee, nicht geprüft; notiert am 2026-10-22._

## Offene Fragen

- [x] Welche Nische wählen wir? Vorläufig Gebäudereinigung (Entscheidung vom 2026-10-22).
- [ ] Wer genau ist der Kunde (Branche, Größe, Region)?
- [ ] Wie viele Monate Vorlauf braucht ein Kunde, damit die Prognose nützt?
- [ ] Was ist ein Kunde bereit zu zahlen?
- [ ] Bieten Ausschreibungsdienste (z. B. DTAD) bereits Prognosen an?
- [ ] Welche geschäftlichen und technischen Erfolgskriterien gelten (z. B. Trefferquote im ±3-Monats-Fenster)?
- [ ] Wie häufig ist Kantinenbetrieb auf TED (CPV noch abzugrenzen)?
- [ ] Zahlen Reinigungsfirmen für Vorabinformationen über auslaufende Verträge (Annahme A15)? Erste Gespräche mit Reinigungsfirmen.
- [ ] Liegen Reinigungsaufträge oft unter dem EU-Schwellenwert, sodass Nachfolger nicht auf TED erscheinen (A3)?

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| 2026-10-22 | 1 | Gebäudereinigung (Haupt-CPV 909…) wird **vorläufige Arbeitsnische** | Häufigste Kandidaten-Nische (440 Zuschläge in 3 Monaten). Laufzeitende bei 80,9 % bestimmbar (KI 77–84 %), vergleichbar mit Winterdienst und Sicherheit. Rein datengetrieben, Kundensicht fehlt. Siehe reports/evaluation_iteration1.md |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

### Iteration 1 – 2026-10-22

- **Was gemacht:** Nur datenseitige Vorarbeit für die Nischenwahl. Die Häufigkeit der Kandidaten-Nischen wurde in den
  TED-Daten der letzten 3 Monate gezählt. Keine Kundengespräche, keine Wettbewerberprüfung.
- **Erkenntnisse – Fakten:** Gebäudereinigung 440, Winterdienst 129, IT-Wartung/Support 47 Zuschläge in 3 Monaten
  (Report, Abschnitt 4).
- **Erkenntnisse – Interpretation:** Gebäudereinigung und Winterdienst haben datenseitig genug Volumen für einen ersten Versuch.
  Bei IT-Wartung hängt das stark von der CPV-Abgrenzung ab.
- **Übergabe an die nächste Phase:** Phase 2 prüft die Datenqualität je Nische. Die Nischenentscheidung bleibt in Phase 1 offen.

### Iteration 1 (Abschluss) – 2026-10-22

- **Was gemacht:** Auf Basis der Phase-2-Ergebnisse und der Evaluation wurde eine vorläufige Arbeitsnische gewählt.
  Die Idee „Facility-Services-Radar“ ist notiert. Kundengespräche gab es weiterhin keine.
- **Erkenntnisse – Fakten:** Gebäudereinigung 440 Zuschläge, Laufzeitende bestimmbar 80,9 % (KI 77,0–84,3 %), Median 36 Monate
  aus Beginn/Ende. Winterdienst 84,5 % und Sicherheitsdienste 83,9 % liegen gleichauf. ([R §5], [E])
- **Erkenntnisse – Interpretation:** Gebäudereinigung ist datenseitig eine vertretbare Arbeitsnische, weil sie die meisten Fälle hat
  und keine schlechtere Qualität. Sie ist aber nicht klar überlegen. Die Wahl ist vorläufig, bis Kundensicht und Sichtbarkeit
  der Nachfolgeaufträge auf TED geprüft sind.
- **Übergabe an die nächste Phase:** Phase 2 lädt in Iteration 2 Auftragsbekanntmachungen (competition) für CPV 909, klärt die
  Rückreichweite und versucht eine erste Zuordnung von Zuschlag und Neuausschreibung. Parallel in Phase 1: erste Gespräche
  mit Reinigungsfirmen (A15).
