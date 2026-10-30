# Phase 1: Business Understanding

> **Ziel:** Klären, welches Problem für wen gelöst wird und woran Erfolg gemessen wird.
> **Weiter, wenn:** Nische und messbare Erfolgskriterien schriftlich feststehen.
> Details: [CRISP-DM.md](../CRISP-DM.md#1-business-understanding)
>
> **Artefakte laut CRISP-DM.md:** [`docs/business.md`](../business.md) (angelegt 2026-10-23: Zielgruppe Oberpfalz, Leitfaden, Notizvorlage)

---

## Aktueller Stand

_Stand: Iteration 4 (Abschluss), 2026-10-30. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Arbeitsnische (vorläufig): Gebäudereinigung, Haupt-CPV 90910/90911/90919.** Nach Iteration 4 lautet die Entscheidung **Idee anpassen**:
Die automatische Zuordnung von Ausschreibung und Vorgänger über das Objekt wird nicht weiter verbessert. Iteration 5 baut stattdessen eine
**Vertragsliste aus Zuschlägen** (Laufzeitende meist bestimmbar) und prüft sie mit einem Backtest auf handgeprüften Paaren. Das Projekt
läuft ohne Kundenkontakt (Entscheidung 2026-10-29); Phase 1 stützt sich auf Recherche. Das Phase-1-Gate aus CRISP-DM.md ist nicht erfüllt:
Geschäftliche Erfolgskriterien und Prognoseziel fehlen noch.

### Fakten (aus den Daten)

Quellen: **[Z4]** [zuordnung_iteration4.md](../../reports/zuordnung_iteration4.md) und [zuordnung_iteration4_korrektur.md](../../reports/zuordnung_iteration4_korrektur.md) · **[GT4]** [sichtbarkeit_iteration4_gt.csv](../../reports/sichtbarkeit_iteration4_gt.csv) · **[BP4]** [blindpruefung_iteration4.md](../../reports/blindpruefung_iteration4.md) · **[RE4]** [regel_entwicklung_iteration4.md](../../reports/regel_entwicklung_iteration4.md) · **[E4]** [evaluation_iteration4.md](../../reports/evaluation_iteration4.md). Ältere Quellen siehe Iterationslog.

- Zuordnung über das Objekt (eingefrorene Regel, Testdaten Q1 2026): Präzision 17/19 = 89,5 % bei nur 19 Vorschlägen, Trefferquote
  17/30 = 56,7 %, Vorgänger unter den Top 3 in 22/30 Fällen [Z4].
- Sichtbarkeit nach Urteilsregeln 1.1: 30/70 = 42,9 % der Ausschreibungen haben einen objektgleichen Vorgänger oder eine Teilmenge auf TED [GT4].
- Zweitprüfung durch den Nutzer: 13/20 = 65 % Übereinstimmung bei Median 2 Minuten je Paar [BP4].
- Vorzeitige Neuvergaben 3/30; Vorlaufzeit bis Ende der Grundlaufzeit streut von −32 bis +26 Monaten [Z4].
- Population Gebäudereinigung (eng): 1.893 Ausschreibungsverfahren in den letzten 4 Quartalen [Z4].
- Markt und Preise aus der Recherche: Median-Auftragswert 167.404 € pro Jahr; Dienste für auslaufende Verträge gibt es in Großbritannien,
  in Deutschland in zwei Suchen keinen gefunden (`docs/business.md` §6).
- Kundengespräche: keine, und im Projekt nicht vorgesehen.

### Interpretation

- Ein Radar, das zu jeder Ausschreibung automatisch den Vorgänger findet, ist mit TED-Daten und einer einfachen Regel nicht erreichbar.
- Eine Liste auslaufender Verträge aus Zuschlägen braucht diese Zuordnung nicht. Sie ist der einfachere Weg und nutzt, was die Daten gut
  hergeben (Laufzeitende bei rund 80 % bestimmbar).
- Ein Produkt mit manueller Prüfung ist nicht belegt: schnell, aber in der einzigen Messung nicht zuverlässig (A17).
- Vor Iteration 5 muss das Prognoseziel feststehen: Ende der Grundlaufzeit oder Höchstende. Die Vorlaufzeiten zeigen, dass die
  Grundlaufzeit allein nicht trägt (A8).
- Ob jemand für die Liste zahlt (A1, A15), bleibt ohne Kundenkontakt offen und wird als Grenze genannt.

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
  _Stand 2026-10-29:_ im Projekt nicht prüfbar (kein Kundenkontakt); nur indirekte Hinweise aus der Recherche.
- [ ] Liegen Reinigungsaufträge oft unter dem EU-Schwellenwert, sodass Nachfolger nicht auf TED erscheinen (A3)?
- [ ] _(neu, Iteration 2)_ Brauchen Kunden die Prognose auf Objektebene (welche Liegenschaft, welcher Umfang), oder reicht
  „Auftraggeber X schreibt bald wieder aus“? In Gesprächen klären (A15).
  _Stand 2026-10-29:_ ohne Gespräche nicht zu klären; der Prototyp (Iteration 7) arbeitet auf Objektebene.
- [ ] _(neu, Iteration 2)_ Wie eng wird die Nische gefasst (nur wiederkehrende Unterhalts- und Glasreinigung, ohne
  Schädlingsbekämpfung, Bau- und Sonderreinigung)? (A12)
- [ ] _(neu, Iteration 2)_ Ist ein Prognoseziel „Vertragsende minus Vorlauf“ tragfähig, wenn vorzeitige Neuvergaben häufig sind (A8, A16)?
  _Stand Iteration 3:_ Vorzeitig gegen die Grundlaufzeit nur 2/36 (Folge „> 30 % → neu bewerten“ nicht ausgelöst); offen bleibt, ob
  das Prognoseziel die Grundlaufzeit oder das Höchstende sein soll [E3].
- [ ] _(neu, Iteration 4)_ Welches Prognoseziel gilt (Ende der Grundlaufzeit, Höchstende oder ein Zeitfenster dazwischen)? (A8)
- [ ] _(neu, Iteration 3)_ Trägt ein **Produkt mit manueller Prüfung** (Regel liefert Kandidaten, Prüfung von Hand)? Prüfaufwand je
  Fall, Kosten und Zahlungsbereitschaft abschätzen, auch in den Gesprächen fragen (A1, A15).
  _Stand 2026-10-29:_ Prüfaufwand über die Prüfzeit in W4, Kosten über Recherche; Zahlungsbereitschaft nicht prüfbar.

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| 2026-10-22 | 1 | Gebäudereinigung (Haupt-CPV 909…) wird **vorläufige Arbeitsnische** | Häufigste Kandidaten-Nische (440 Zuschläge in 3 Monaten). Laufzeitende bei 80,9 % bestimmbar (KI 77–84 %), vergleichbar mit Winterdienst und Sicherheit. Rein datengetrieben, Kundensicht fehlt. Siehe reports/evaluation_iteration1.md |
| 2026-10-23 | 2 | **Idee anpassen:** Prognose auf Objektebene (Liegenschaft) statt auf Auftraggeber-Ebene; Gebäudereinigung bleibt vorläufige Nische, wird aber enger abgegrenzt. Ausweichoptionen (Auftraggeber-Zyklen, nationale Quellen) bleiben bestehen. | Zuordnung über den Auftraggeber K2 = 16,7 %; siehe reports/ergebnis_iteration2.md und reports/evaluation_iteration2.md. Entscheidung des Nutzers. |
| 2026-10-29 | 4 | **Kein Kundenkontakt im Projekt.** Gespräche (G2.3–G2.5) und Pilotkunden (G4) entfallen; Markt, Wettbewerb, Angebot und Preis nur als Schreibtisch-Recherche; Iteration 7 wird Prototyp statt Kundentest; A1 und A15 bleiben ungeprüft | Studienprojekt; Kundenkontakt gehört nicht zum Projektumfang. Entscheidung des Nutzers. |
| 2026-10-25 | 3 | Objekt-Ebene bleibt Ziel; **parallel** wird die Alternative „Produkt mit manueller Prüfung“ bewertet. Nische enger: Haupt-CPV 90910/90911/90919, Leistungsart künftig auf Los-Ebene prüfen | Zuordnung über das Objekt: Präzision 45,8 %, Trefferquote 28,9 % bei Sichtbarkeit 63,3 % ([Z3], [E3]); vorab festgelegte Folge „in Phase 2/3 bleiben, alternativ Produkt mit manueller Prüfung“. Entscheidung des Nutzers. |
| 2026-10-30 | 4 | **Idee anpassen:** Keine weitere automatische Objekt-Zuordnung; Iteration 5 baut eine Vertragsliste aus Zuschlägen, Zuordnung nur als Werkzeug für einen Backtest auf handgeprüften Paaren; Prognoseziel vorher festlegen | Vorab festgelegte Folge „W4 < 85 %“ (W4 65 %); W3 56,7 %, W2-Mindestzahl verfehlt; reports/evaluation_iteration4.md. Entscheidung des Nutzers. |

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

### Iteration 4 – 2026-10-30

- **Was gemacht:** Keine Kundengespräche (seit 2026-10-29 nicht mehr vorgesehen). Ergebnisse aus Phase 2/3 für die Ausrichtung
  ausgewertet; Strang G auf Schreibtisch-Recherche umgestellt; Iteration 7 als Prototyp statt Kundentest geplant.
- **Erkenntnisse – Fakten:**
  - Zuordnung über das Objekt: Präzision 89,5 % bei 19 Vorschlägen, Trefferquote 56,7 %, Top 3 73,3 % [Z4].
  - Sichtbarkeit 42,9 %, Zweitprüfung 65 % bei 2 Minuten je Paar [GT4], [BP4].
  - Vorlaufzeit streut stark, vorzeitige Neuvergaben selten (3/30) [Z4].
- **Erkenntnisse – Interpretation:**
  - Das Produkt soll nicht mehr an einer automatischen Nachfolger-Zuordnung hängen.
  - Eine Vertragsliste aus Zuschlägen ist der naheliegende Kern; die Prognose braucht ein klar definiertes Ziel.
- **Übergabe an die nächste Phase:** Iteration 5 beginnt in Phase 1: Prognoseziel festlegen (Grundlaufzeit oder Höchstende, Zeitfenster),
  Abdeckung offen benennen, dann Phase 3 (Tabelle der Zuschläge mit Laufzeitende), Phase 4 (einfache Regel) und Phase 5 (Backtest auf
  handgeprüften Paaren, deren Ground Truth vorab unabhängig geprüft wird).
