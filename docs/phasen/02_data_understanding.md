# Phase 2: Data Understanding

> **Ziel:** Verstehen, welche Daten es gibt, wie gut sie sind und was sie hergeben.
> **Weiter, wenn:** Für die gewählte Nische genug Datensätze mit verwertbarer Laufzeit vorliegen.
> **Zurück zu Phase 1, wenn:** Die Daten für die Nische nicht reichen.
> Details: [CRISP-DM.md](../CRISP-DM.md#2-data-understanding)
>
> **Artefakte laut CRISP-DM.md:**
> - Datenqualitätsreport: vorhanden als [reports/datenqualitaet_DEU_20260722_20261021.md](../../reports/datenqualitaet_DEU_20260722_20261021.md)
> - Skripte in `src/ingest/`: liegen derzeit direkt in `src/` ([ted_download.py](../../src/ted_download.py), [analyze_completeness.py](../../src/analyze_completeness.py))

---

## Aktueller Stand

_Stand: Iteration 1 (Abschluss), 2026-10-22. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

Abkürzungen für Quellen: **[R]** = Report `reports/datenqualitaet_DEU_20260722_20261021.md`,
**[S]** = `reports/stichprobe_iteration1.md`, **[E]** = `reports/evaluation_iteration1.md`,
**[M]** = `data/raw/ted_search/DEU_20260722_20261021/request_meta.json`,
**[A]** = Probeabfragen an die API vom 22.10.2026 (nicht gespeichert),
**[Sp]** = OpenAPI-Spezifikation https://ted.europa.eu/docs/v3.

### Fakten (aus den Daten)

**Datenquelle und Datensatz**
- TED Search API v3: `POST https://api.ted.europa.eu/v3/notices/search`, kein API-Key. Maximal 250 Notices pro Seite,
  im Seitennummern-Modus höchstens 15.000 Treffer, im ITERATION-Modus unbegrenzt. [Sp]
- Geladen sind **nur Zuschläge** (`form-type=result`) mit deutschem Auftraggeber, veröffentlicht vom 22.07. bis 21.10.2026:
  15.706 Notices, vollständig laut API, keine Duplikate. [M]
- Nicht geladen: Auftragsbekanntmachungen (competition), Vorinformationen, can-modif (2.673 im Zeitraum), veat (302). [A]
- Bau (CPV 45) und Architektur/Ingenieure (CPV 71) machen zusammen 52,4 % aller Notices aus. [R §3], [E]

**Parsing-Prüfung** [S]
- 15 zufällige Notices (Seed 20261022, davon 5 aus CPV 909) gegen die Original-XML geprüft.
- Beginn, Ende, Dauer, Verlängerung und Haupt-CPV stimmen in 15 von 15 Fällen. Kein Fehler in unserem Code.
- Bei 2 Auftraggebernamen weicht nur der Leerraum ab.
- `total-value` ist **nicht** BT-161, sondern ein von TED berechneter Wert. Belegt durch 573266-2026, im Report korrigiert.
- `-1` geht mit `efac:FieldsPrivacy` einher, die Website zeigt „Nicht veröffentlicht“ (684689-2026).

**Laufzeit** [R §2, §5]
- Alle Notices: BT-36 bei 21,3 % (Median 24 Monate); Beginn und Ende bei 60,2 % (Median 16 Monate).
  „Laufzeitende bestimmbar“ (Ende, oder Beginn + Dauer) bei 61,7 %.
- Nur 10 Notices haben BT-36 und Beginn/Ende zugleich. Davon stimmen 40 % auf ±1 Monat überein.

| Nische | n | Ende bestimmbar | Ende oder Dauer | Median aus Beginn/Ende (Quartile, n) | Median BT-36 (n) | BT-58 > 0 | Wert > 1 € |
|---|---|---|---|---|---|---|---|
| Gebäudereinigung (909) | 440 | 80,9 % | 90,0 % | 36 (24/48, n = 350) | 24 (n = 45) | 42,0 % | 51,4 % |
| Winterdienst (9062, 9063) | 129 | 84,5 % | 93,0 % | 36 (17/47, n = 109) | 48 (n = 11) | 33,3 % | 51,9 % |
| Sicherheitsdienste (7971) | 137 | 83,9 % | 93,4 % | 24 (13/48, n = 115) | 24 (n = 13) | 42,3 % | 32,8 % |
| IT-Dienste (72) | 575 | 33,7 % | 78,6 % | 36 (18/48, n = 185) | 48 (n = 264) | 34,3 % | 52,7 % |
| IT-Wartung/Support | 47 | 29,8 % | 83,0 % | 44 (25/48, n = 14) | 36 (n = 25) | 29,8 % | 53,2 % |

**Gebäudereinigung im Detail** [E, nachgerechnet]
- 95-%-KI für „Ende bestimmbar“: 77,0–84,3 %.
- 40 Notices haben nur eine Dauer ohne Beginn, 8 sind als `can-desg` veröffentlicht.
- 91,8 % tragen Reinigungs-Codes 90910/90911/90919.
- Die größten Auftraggeber sind BImA (26) und Stadt Frankfurt am Main (24), zusammen 11,4 %.

### Interpretation

- Das Laufzeitende ist in den Facility-Nischen meist bestimmbar. Die 80-%-Schwelle wurde aber nachträglich gesetzt und ist für
  Gebäudereinigung statistisch nicht sicher überschritten. [E]
- Die Median-Laufzeit von 24 Monaten aus Iteration 1 war für Gebäudereinigung zu kurz, weil sie nur auf 45 BT-36-Werten beruhte.
  Aus Beginn und Ende ergeben sich 36 Monate. Ein Backtest nur mit eForms-Daten (seit Herbst 2023) würde dadurch vor allem kurze
  Verträge ohne Verlängerung sehen, mit Zensierungs- und Selektionsverzerrung. [E]
- Die eigentliche Zielgröße ist noch nicht untersucht: ob und wann Neuausschreibungen auf TED erscheinen und ob sie sich zuordnen lassen.
- Die Gesamtkennzahlen sind wegen des hohen Anteils an Bau- und Ingenieurprojekten für das Radar wenig aussagekräftig.
  Sinnvolle Bezugsgröße ist die Nische.

## Offene Fragen

- [ ] Wie weit zurück sind die Daten brauchbar? Zahl der 909-Zuschläge seit Ende Oktober 2023 und Verteilung ihrer Enddaten. Enthalten die Formate vor eForms Laufzeiten (A10, A11)?
- [ ] Erscheinen Neuausschreibungen für CPV 909 als Auftragsbekanntmachungen (competition) auf TED, und wie viele pro Jahr? Gibt es Vorinformationen (PIN) als Frühsignal?
- [ ] Lassen sich Zuschlag und Neuausschreibung zuordnen, z. B. über Auftraggeber und CPV (A9)?
- [ ] Meinen BT-36/BT-536/BT-537 die Laufzeit mit oder ohne Verlängerungen? (eForms-Dokumentation prüfen)
- [ ] Warum ist bei 84 von 440 Gebäudereinigungs-Notices kein Laufzeitende bestimmbar? Stichprobe von etwa 20 Fällen.
- [ ] Hält die Quote in einem unabhängigen Zeitfenster (z. B. ein Frühjahrsquartal 2025), mit vorab festgelegter Schwelle (A13)?
- [ ] Wie sieht die Befüllung auf Los-Ebene aus statt auf Notice-Ebene?
- [x] Bedeutet `-1` „nicht veröffentlicht“? Teilweise belegt durch 2 Fälle mit FieldsPrivacy [S] (A7).
- [ ] Wie oft stehen Verlängerungen nur im Freitext (quantifizieren statt aus einem Einzelfall verallgemeinern)?
- [ ] Wie häufig ist Kantinenbetrieb, und wie gut ist er befüllt?
- [ ] Zeigen Vertragsänderungen (can-modif) ausgeübte Verlängerungen?
- [x] Wie viele Datensätze mit verwertbarer Laufzeit gelten als „genug“? Nachträglich: ≥ 80 % bestimmbares Laufzeitende (siehe iterationen.md).

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| 2026-10-22 | 1 | Abfrage mit `form-type=result`, ohne can-modif und veat | Nur echte Zuschläge sind neue Verträge |
| 2026-10-22 | 1 | Download im ITERATION-Modus | Mehr als 15.000 Treffer |
| 2026-10-22 | 1 | Rohantworten byteweise unverändert in `data/raw/`, `data/` nicht in Git | CLAUDE.md-Regel; 77 MB, jederzeit reproduzierbar |
| 2026-10-22 | 1 | Auswertung auf Notice-Ebene (befüllt = mindestens ein Los) | Einfach zuerst; Los-Ebene als offene Frage |
| 2026-10-22 | 1 | `-1` gilt als nicht befüllt; zusätzlich Kennzahl „plausibler Wert > 1 €“ | Platzhalter verfälschen sonst die Quote |
| 2026-10-22 | 1 | CPV-Bezeichnungen aus der offiziellen Liste im eForms SDK | Offizielle Quelle mit deutschen Labels |
| 2026-10-22 | 1 | „Laufzeitende bestimmbar“ = Enddatum, oder Beginn + Dauer; „Ende oder Dauer“ wird nur ergänzend ausgewiesen | Eine Dauer ohne Beginn ergibt kein Enddatum |
| 2026-10-22 | 1 | Laufzeit zusätzlich aus Beginn/Ende berechnen; Werte ≤ 0 oder > 240 Monate verwerfen | BT-36 nur bei 21 % befüllt, Median dadurch verzerrt |
| 2026-10-22 | 1 | `total-value` als „von TED berechnet“ kennzeichnen, nicht als BT-161 | Parsing-Stichprobe 573266-2026 |
| 2026-10-22 | 1 | Iteration 2 beginnt in Phase 2 mit competition-Daten, Rückreichweite und erster Zuordnung (CPV 909), erst danach Phase 3 | Evaluation: Zielereignis und Backtest-Machbarkeit sind ungeprüft |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

### Iteration 1 – 2026-10-22

- **Was gemacht:** TED Search API v3 recherchiert (Doku, OpenAPI-Spezifikation, Probeabfragen). Alle deutschen
  Zuschlagsbekanntmachungen vom 22.07. bis 21.10.2026 geladen (`src/ted_download.py`). Vollständigkeitsanalyse mit Report
  erstellt (`src/analyze_completeness.py`). Eine Notice manuell mit der TED-Website verglichen.
- **Erkenntnisse – Fakten:** 15.706 Notices. Laufzeit (Ende oder Dauer) 82,0 %, in den Dienstleistungsnischen 90–93 %.
  BT-58 > 0 nur 14,7 %. Plausibler Wert nur 58,8 %. Etwa 21 % der Gesamtwerte ≤ 1 €. In 505084-2026 steht die
  Verlängerung nur im Freitext.
- **Erkenntnisse – Interpretation:** Die Laufzeit trägt eine Baseline. Verlängerungen brauchen Textextraktion. Der Wert
  ist nur eingeschränkt nutzbar.
- **Übergabe an die nächste Phase:** An Phase 3 gehen die Feldliste und Fallstricke (`-1`, Platzhalterwerte, Listen je Los,
  mehrsprachige Namen, Verlängerung im Freitext). An Phase 1 geht die Häufigkeit und Befüllung je Nische als Grundlage
  für die Nischenwahl. Vor Phase 3 noch offen: Rückreichweite der Daten.

### Iteration 1 (Abschluss) – 2026-10-22

- **Was gemacht:**
  - Parsing-Stichprobe mit 15 Notices gegen die Original-XML ([S], `src/stichprobe_parsing.py`)
  - Laufzeit aus Beginn/Ende nachberechnet und Kennzahl „Laufzeitende bestimmbar“ eingeführt ([R §5])
  - Kritische Prüfung durch den Evaluator ([E])
- **Erkenntnisse – Fakten:**
  - Kein Parsing-Fehler in 15 von 15 Fällen. `total-value` ist nicht BT-161.
  - Gebäudereinigung: Ende bestimmbar 80,9 % (KI 77,0–84,3 %), Median-Laufzeit 36 Monate aus Beginn/Ende (BT-36: 24, n = 45).
  - Winterdienst 84,5 %, Sicherheit 83,9 %, IT-Dienste 33,7 %.
- **Erkenntnisse – Interpretation:**
  - Die Datenbasis trägt eine vorläufige Arbeitsnische.
  - Ob ein Backtest nur mit eForms-Daten gelingt und ob Neuausschreibungen sich zuordnen lassen, ist offen und eher kritisch.
- **Übergabe an die nächste Phase:** Iteration 2 bleibt zunächst in Phase 2:
  - Auftragsbekanntmachungen (competition) für CPV 909 laden
  - Rückreichweite klären
  - erste Zuordnung von Zuschlag und Neuausschreibung versuchen

  Danach geht an Phase 3:
  - Laufzeit aus Beginn/Ende nutzen
  - Verlängerungen aus BT-54/BT-57 extrahieren
  - Zuordnung alter und neuer Ausschreibungen aufbauen
