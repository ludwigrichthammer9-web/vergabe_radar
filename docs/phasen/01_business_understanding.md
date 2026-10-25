# Phase 1: Business Understanding

> **Ziel:** Klären, welches Problem für wen gelöst wird und woran Erfolg gemessen wird.
> **Weiter, wenn:** Nische und messbare Erfolgskriterien schriftlich feststehen.
> Details: [CRISP-DM.md](../CRISP-DM.md#1-business-understanding)
>
> **Artefakte laut CRISP-DM.md:** [`docs/business.md`](../business.md) (angelegt 2026-10-23: Zielgruppe Oberpfalz, Leitfaden, Notizvorlage)

---

## Aktueller Stand

_Stand: Iteration 3 (Abschluss), 2026-10-25. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Arbeitsnische (vorläufig): Gebäudereinigung, Haupt-CPV 90910/90911/90919.** Die Prognose soll sich auf das Objekt (Liegenschaft)
beziehen. Iteration 3 zeigt: Vorgänger sind auf TED oft sichtbar, eine einfache automatische Zuordnung gelingt aber nicht. Deshalb
kommt eine zweite Produktvariante ins Spiel, das **Produkt mit manueller Prüfung** (Kandidaten automatisch, Prüfung von Hand). Das
Phase-1-Gate aus CRISP-DM.md ist weiterhin nicht erfüllt: Kundensicht und geschäftliche Erfolgskriterien fehlen.

### Fakten (aus den Daten)

Quellen: **[R]** = [Datenqualitätsreport](../../reports/datenqualitaet_DEU_20260722_20261021.md),
**[E]** = [Evaluation Iteration 1](../../reports/evaluation_iteration1.md), **[RR]** = [rueckreichweite_909.md](../../reports/rueckreichweite_909.md),
**[Erg]** = [ergebnis_iteration2.md](../../reports/ergebnis_iteration2.md), **[E2]** = [evaluation_iteration2.md](../../reports/evaluation_iteration2.md),
**[Z3]** = [zuordnung_iteration3.md](../../reports/zuordnung_iteration3.md), **[E3]** = [evaluation_iteration3.md](../../reports/evaluation_iteration3.md),
**[B]** = [business.md](../business.md), **[AW]** = [auftragswerte_909.md](../../reports/auftragswerte_909.md).

| Nische (Haupt-CPV) | Zuschläge in 3 Monaten | Laufzeitende bestimmbar¹ | 95-%-KI | Median-Laufzeit aus Beginn/Ende | BT-58 > 0 |
|---|---|---|---|---|---|
| Gebäudereinigung (909) | 440 | 80,9 % | 77,0–84,3 % | 36 Mon. (n = 350) | 42,0 % |
| Winterdienst (9062, 9063) | 129 | 84,5 % | 77,3–89,7 % | 36 Mon. (n = 109) | 33,3 % |
| Sicherheitsdienste (7971) | 137 | 83,9 % | 76,9–89,2 % | 24 Mon. (n = 115) | 42,3 % |
| IT-Dienste (72) | 575 | 33,7 % | – | 36 Mon. (n = 185) | 34,3 % |
| IT-Wartung/Support (503, 7225, 72267) | 47 | 29,8 % | – | 44 Mon. (n = 14) | 29,8 % |

¹ Enddatum vorhanden oder Beginn und Dauer vorhanden; Zeitraum 22.07.–21.10.2026. Quelle: [R §5]; KI aus [E].

- Gebäudereinigung auf TED (DEU): 1.250–1.750 Zuschläge und grob 1.990–2.160 ausgeschriebene Verfahren pro Jahr. [RR]
  Population Q3 2026 (eng abgegrenzt): 492 Ausschreibungsverfahren. [Z3]
- **Sichtbarkeit:** 63,3 % der Ausschreibungen haben einen objektgleichen Vorgänger oder einen mit gemeinsamem Objekt auf TED, nur
  objektgleich 48,3 %. **Automatische Zuordnung:** Präzision 45,8 %, Trefferquote 28,9 %. [Z3], [E3]
- Unter den gefundenen Paaren sind vorzeitige Neuvergaben selten (2/36); Neuvergaben nach der Grundlaufzeit, aber vor dem Höchstende,
  kommen öfter vor (mindestens 6). [E3]
- Auftragswerte (eForms-Zuschläge 2024–2025, plausible Werte): Median 421.713 € je Auftrag, 167.404 € pro Jahr. [AW]
- Zielgruppe Oberpfalz: 70 TED-Zuschläge seit eForms, 71 Firmen. Gesprächsleitfaden liegt vor. [B]
- Ausschreibungsdienste DTAD und subreport (laut Vergleichsseiten 84–198 €/Monat); ein deutscher Dienst für auslaufende Verträge wurde
  in zwei Suchen nicht gefunden; in Großbritannien bewirbt Stotles „expiring contracts“ ab 50 £ pro Nutzer und Monat. [B]
- Kundengespräche: 0.

### Interpretation

- Für Kunden zählt vermutlich, *welcher* Vertrag ausläuft (Objekt, Umfang, Termin). Ungeprüft, das sollen Gespräche klären (A15).
- **Ein Produkt mit manueller Prüfung ist eine ernsthafte Alternative.** Bei 46 % Präzision liefert die Regel Kandidaten, die ein
  Mensch prüfen muss. Offen ist, wie viel Prüfaufwand je Fall entsteht und ob ein Kunde das Ergebnis dann noch günstig genug bekommt.
- Eine Variante auf Ebene des Auftraggebers („Stadt X schreibt bald wieder aus“) bleibt Ausweichoption.
- Das Warnsignal zu vorzeitigen Neuvergaben aus Iteration 2 hat sich nicht bestätigt; die Frage verschiebt sich zu „Grundlaufzeit
  oder Höchstende?“ (A8, A16).
- Der Wert eines Auftrags (etwa 167.000 € pro Jahr) ist groß gegenüber einem Dienst für 50–200 € im Monat. Ob ein früher Hinweis die
  Gewinnchance erhöht, ist ohne Gespräche nicht belegt.

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
- [ ] _(neu, Iteration 2)_ Brauchen Kunden die Prognose auf Objektebene (welche Liegenschaft, welcher Umfang), oder reicht
  „Auftraggeber X schreibt bald wieder aus“? In Gesprächen klären (A15).
- [ ] _(neu, Iteration 2)_ Wie eng wird die Nische gefasst (nur wiederkehrende Unterhalts- und Glasreinigung, ohne
  Schädlingsbekämpfung, Bau- und Sonderreinigung)? (A12)
- [ ] _(neu, Iteration 2)_ Ist ein Prognoseziel „Vertragsende minus Vorlauf“ tragfähig, wenn vorzeitige Neuvergaben häufig sind (A8, A16)?
  _Stand Iteration 3:_ Vorzeitig gegen die Grundlaufzeit nur 2/36 (Folge „> 30 % → neu bewerten“ nicht ausgelöst); offen bleibt, ob
  das Prognoseziel die Grundlaufzeit oder das Höchstende sein soll [E3].
- [ ] _(neu, Iteration 3)_ Trägt ein **Produkt mit manueller Prüfung** (Regel liefert Kandidaten, Prüfung von Hand)? Prüfaufwand je
  Fall, Kosten und Zahlungsbereitschaft abschätzen, auch in den Gesprächen fragen (A1, A15).

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| 2026-10-22 | 1 | Gebäudereinigung (Haupt-CPV 909…) wird **vorläufige Arbeitsnische** | Häufigste Kandidaten-Nische (440 Zuschläge in 3 Monaten). Laufzeitende bei 80,9 % bestimmbar (KI 77–84 %), vergleichbar mit Winterdienst und Sicherheit. Rein datengetrieben, Kundensicht fehlt. Siehe reports/evaluation_iteration1.md |
| 2026-10-23 | 2 | **Idee anpassen:** Prognose auf Objektebene (Liegenschaft) statt auf Auftraggeber-Ebene; Gebäudereinigung bleibt vorläufige Nische, wird aber enger abgegrenzt. Ausweichoptionen (Auftraggeber-Zyklen, nationale Quellen) bleiben bestehen. | Zuordnung über den Auftraggeber K2 = 16,7 %; siehe reports/ergebnis_iteration2.md und reports/evaluation_iteration2.md. Entscheidung des Nutzers. |
| 2026-10-25 | 3 | Objekt-Ebene bleibt Ziel; **parallel** wird die Alternative „Produkt mit manueller Prüfung“ bewertet. Nische enger: Haupt-CPV 90910/90911/90919, Leistungsart künftig auf Los-Ebene prüfen | Zuordnung über das Objekt: Präzision 45,8 %, Trefferquote 28,9 % bei Sichtbarkeit 63,3 % ([Z3], [E3]); vorab festgelegte Folge „in Phase 2/3 bleiben, alternativ Produkt mit manueller Prüfung“. Entscheidung des Nutzers. |

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

### Iteration 2 – 2026-10-23

- **Was gemacht:** Keine eigene Arbeit mit Kunden oder Wettbewerb. Ergebnisse aus Phase 2 für die Ausrichtung ausgewertet.
- **Erkenntnisse – Fakten:**
  - Zuordnung über den Auftraggeber: 5 von 30 richtig.
  - 3 von 6 objektgleichen Paaren sind vorzeitige Neuvergaben.
  - Haupt-CPV 909 ist breiter als wiederkehrende Gebäudereinigung.

  Quellen: [Erg], [E2].
- **Erkenntnisse – Interpretation:** Das Produkt muss vermutlich auf Objektebene prognostizieren. Ob TED dafür reicht und ob Kunden
  das brauchen, ist offen.
- **Übergabe an die nächste Phase:** Phase 2 (Iteration 3) misst Sichtbarkeit und Zuordnung über das Objekt. Parallel in Phase 1:
  erste Gespräche mit Reinigungsfirmen (A15), dabei auch fragen, ob Auftraggeber-Ebene reichen würde.

### Iteration 3 – 2026-10-25

- **Was gemacht:**
  - Zielgruppe Oberpfalz aus TED bestimmt, Gesprächsleitfaden und Notizvorlage angelegt ([B], `src/zielgruppe_oberpfalz.py`)
  - Schreibtisch-Recherche zu Markt und Preisen, Auftragswerte aus TED ([B] §6, [AW], `src/auftragswerte.py`)
  - Ergebnisse aus Phase 2 für die Ausrichtung ausgewertet ([Z3], [E3])
  - Keine Kundengespräche.
- **Erkenntnisse – Fakten:**
  - 70 Zuschläge und 71 Firmen in der Oberpfalz seit eForms.
  - Median-Auftragswert 167.404 € pro Jahr.
  - Kein deutscher Dienst für auslaufende Verträge gefunden; in Großbritannien gibt es einen (Stotles).
  - Sichtbarkeit 63,3 %, automatische Zuordnung Präzision 45,8 %.
- **Erkenntnisse – Interpretation:**
  - Ein vollautomatisches Radar auf Objektebene ist mit der bisherigen Regel nicht machbar; ein Produkt mit manueller Prüfung ist
    die naheliegende Alternative.
  - Der Wert eines Auftrags spricht für Zahlungsbereitschaft, belegt ist sie nicht.
- **Übergabe an die nächste Phase:** Phase 2/3 (Iteration 4) unternimmt den letzten Verbesserungsversuch der Zuordnung. Parallel in
  Phase 1: erste Gespräche führen (Ziel 5 bis Mitte November) und das Produkt mit manueller Prüfung grob bewerten (Prüfaufwand je
  Fall, Preis).
