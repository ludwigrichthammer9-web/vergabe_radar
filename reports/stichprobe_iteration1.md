# Stichprobe Iteration 1: Prüfung des Parsings

Stand: 2026-10-22 · Skript: [src/stichprobe_parsing.py](../src/stichprobe_parsing.py) ·
Vergleichsdaten: `data/processed/stichprobe_iteration1.csv` · Original-XML: `data/raw/ted_xml/<nr>.xml`

## Frage

Liest unsere Pipeline (Search API → `src/analyze_completeness.py` → `data/processed/notices_DEU_20260722_20261021.csv`)
die Felder Laufzeitbeginn, Laufzeitende, Dauer, Verlängerungen, Auftraggeber, Haupt-CPV und Auftragswert korrekt?

## Methode

- **Auswahl:** zufällig mit Seed `20261022`. 5 Notices mit Haupt-CPV `909…` (Gebäudereinigung) und 10 aus allen übrigen,
  gezogen aus den 15.706 Notices vom 22.07. bis 21.10.2026.
- **Referenz:** die Original-eForms-XML jeder Notice (`https://ted.europa.eu/en/notice/<nr>/xml`), unverändert gespeichert.
  Ausgelesen mit eigenen XPaths aus dem eForms SDK (`fields/fields.json`), also unabhängig von der Search API:

  | Merkmal | Feld | XML-Pfad (gekürzt) |
  |---|---|---|
  | Beginn | BT-536 | `ProcurementProjectLot/ProcurementProject/PlannedPeriod/StartDate` |
  | Ende | BT-537 | `…/PlannedPeriod/EndDate` |
  | Dauer | BT-36 | `…/PlannedPeriod/DurationMeasure` (+ `unitCode`) |
  | Verlängerung | BT-58 / BT-57 / BT-54 | `…/ContractExtension/MaximumNumberNumeric`, `…/Renewal/Period/Description`, `…/OptionsDescription` |
  | Auftraggeber | BT-500 über OPT-300 | `ContractingParty/Party/PartyIdentification/ID` → `Organizations/…/PartyName/Name` |
  | Haupt-CPV | BT-262 (Verfahren) | `ProcurementProject/MainCommodityClassification/ItemClassificationCode` |
  | Wert | BT-161 / BT-720 / BT-27 | `NoticeResult/TotalAmount`, `LotTender/…/PayableAmount`, `RequestedTenderTotal/EstimatedOverallContractAmount` |

- **Vergleichsregeln:**
  - Beginn, Ende und Dauer: erstes Los, wie in unserer Tabelle.
  - Verlängerung: höchster BT-58-Wert über alle Lose; dazu, ob es in irgendeinem Los einen BT-57- oder BT-54-Text gibt.
  - Wert: erster Wert ungleich `-1`.
  - Ob sich weitere Lose unterscheiden, wird zusätzlich geprüft.
- **Gegenprobe in der TED-Webansicht** (`/de/notice/<nr>/html`) für 560887-2026 (19 Lose), 573266-2026 und 684689-2026.
- **Ursachen für Abweichungen:**
  - (a) Parsing-Fehler in unserem Code
  - (b) Search API liefert etwas anderes als die XML
  - (c) Definitions- oder Beschriftungsunterschied
  - (d) Original fehlerhaft oder unplausibel
- **STOPP-Regel** (vorab festgelegt): Die Iteration wird nicht abgeschlossen, wenn
  - ein Fehler der Ursache (a) bei ≥ 2 Notices auftritt oder
  - ein Fehler der Ursache (a) beim Laufzeitende auftritt.

## Ergebnis

✓ = gleich · ✗ = abweichend · – = in Tabelle und XML leer

| Notice | Nische | Haupt-CPV | Lose | Beginn | Ende | Dauer | Verlängerung | Auftraggeber | CPV | Wert |
|:--|:--|--:|--:|:--|:--|:--|:--|:--|:--|:--|
| 560887-2026 | 909 | 90910000 | 19 | ✓ | ✓ | – | ✓ | ✓ | ✓ | ✓ |
| 587627-2026 | 909 | 90911200 | 1 | ✓ | ✓ | – | ✓ | ✓ | ✓ | ✓ |
| 528933-2026 | 909 | 90910000 | 1 | ✓ | ✓ | – | ✓ | ✗ (c) | ✓ | ✓ |
| 637022-2026 | 909 | 90911200 | 2 | ✓ | ✓ | – | ✓ | ✓ | ✓ | ✓ |
| 637113-2026 | 909 | 90911200 | 3 | ✓ | ✓ | – | ✓ | ✓ | ✓ | ✓ |
| 702922-2026 | andere | 34144213 | 3 | – | – | – | ✓ | ✓ | ✓ | ✓ |
| 636832-2026 | andere | 79952000 | 2 | ✓ | ✓ | – | ✓ | ✓ | ✓ | – |
| 561098-2026 | andere | 71000000 | 1 | – | – | – | ✓ | ✓ | ✓ | ✓ |
| 675850-2026 | andere | 35111520 | 1 | ✓ | ✓ | – | ✓ | ✓ | ✓ | – |
| 682493-2026 | andere | 71000000 | 1 | ✓ | ✓ | – | ✓ | ✓ | ✓ | ✓ |
| 684689-2026 | andere | 71000000 | 1 | – | – | ✓ | ✓ | ✓ | ✓ | – |
| 676896-2026 | andere | 45000000 | 1 | ✓ | ✓ | – | ✓ | ✗ (c) | ✓ | ✓ |
| 559053-2026 | andere | 80000000 | 2 | ✓ | ✓ | – | ✓ | ✓ | ✓ | – |
| 573266-2026 | andere | 35330000 | 1 | – | – | – | ✓ | ✓ | ✓ | ✗ (c) |
| 528698-2026 | andere | 71221000 | 1 | – | – | ✓ | ✓ | ✓ | ✓ | ✓ |

### Laufzeit und Verlängerung im Detail

| Notice | Beginn (Tabelle \| XML) | Ende (Tabelle \| XML) | Dauer Monate (Tabelle \| XML) | BT-58 / BT-57-Text / BT-54-Text (Tabelle \| XML) |
|:--|:--|:--|:--|:--|
| 560887-2026 | 2026-12-01 \| 2026-12-01 | 2032-09-30 \| 2032-09-30 | – | 2 / ja / nein \| 2 / ja / nein |
| 587627-2026 | 2027-01-01 \| 2027-01-01 | 2028-12-31 \| 2028-12-31 | – | 1 / ja / nein \| 1 / ja / nein |
| 528933-2026 | 2026-07-06 \| 2026-07-06 | 2027-07-05 \| 2027-07-05 | – | – / nein / ja \| – / nein / ja |
| 637022-2026 | 2027-01-01 \| 2027-01-01 | 2028-12-31 \| 2028-12-31 | – | 1 / ja / nein \| 1 / ja / nein |
| 637113-2026 | 2026-10-17 \| 2026-10-17 | 2029-07-01 \| 2029-07-01 | – | – / nein / ja \| – / nein / ja |
| 702922-2026 | – | – | – | – / nein / nein (beide) |
| 636832-2026 | 2026-06-17 \| 2026-06-17 | 2026-11-30 \| 2026-11-30 | – | – / nein / nein (beide) |
| 561098-2026 | – | – | – | – / nein / nein (beide) |
| 675850-2026 | 2026-10-15 \| 2026-10-15 | 2030-10-14 \| 2030-10-14 | – | – / nein / nein (beide) |
| 682493-2026 | 2026-07-01 \| 2026-07-01 | 2028-08-31 \| 2028-08-31 | – | – / nein / nein (beide) |
| 684689-2026 | – | – | 21 \| 21 | – / nein / nein (beide) |
| 676896-2026 | 2026-10-02 \| 2026-10-02 | 2028-06-02 \| 2028-06-02 | – | – / nein / nein (beide) |
| 559053-2026 | 2026-10-01 \| 2026-10-01 | 2027-09-30 \| 2027-09-30 | – | – / nein / ja \| – / nein / ja |
| 573266-2026 | – | – | – | 2 / ja / nein \| 2 / ja / nein |
| 528698-2026 | – | – | 24 \| 24 | – / nein / nein (beide) |

Bei allen 7 Notices mit mehreren Losen ist die Losanzahl in Tabelle und XML gleich. Innerhalb dieser Notices haben alle Lose
dieselbe Laufzeit, die Beschränkung unserer Tabelle auf das 1. Los verfälscht hier also nichts.

### Abweichungen

| Notice | Merkmal | Tabelle | Original | Ursache | Bewertung |
|---|---|---|---|---|---|
| 528933-2026 | Auftraggeber | „Landratsamt Erzgebirgskreis Abteilung 2, Referat 23000 …“ | gleicher Text mit Zeilenumbrüchen | (c) | Inhaltlich gleich. Die Search API ersetzt Zeilenumbrüche durch Leerzeichen. |
| 676896-2026 | Auftraggeber | „Land Rheinland-Pfalz vertreten durch …“ | gleicher Text mit doppelten Leerzeichen | (c) | Inhaltlich gleich, nur der Leerraum unterscheidet sich. |
| 573266-2026 | Wert (`total-value`) | 1.921.425 € | **kein** `TotalAmount` (BT-161) in der XML; Angebotswert BT-720 = 1.921.425 € | (c) | Das API-Feld `total-value` ist nicht BT-161, sondern ein von TED berechneter Wert. Der Report beschriftet es fälschlich als BT-161. |

### Weitere Beobachtungen

- **`-1` heißt „nicht veröffentlicht“:**
  - 684689-2026 hat in der XML `PayableAmount = -1` und einen `efac:FieldsPrivacy`-Block.
  - Die Webansicht zeigt „Nicht veröffentlicht, Geschäftliche Interessen eines Wirtschaftsteilnehmers“.
  - Bei 636832-2026 steht `-1` ebenfalls so in der XML.
  - Das stützt Annahme A7.
- **Platzhalterwerte stehen auch im Original:** 561098-2026 hat 0,01 € als Gesamt- und Angebotswert, 702922-2026 hat Gesamtwert 0 € bei
  Angebotswerten von 444.719 € u. a. Das sind keine Parsing-Fehler.
- **Laufzeit nur im Freitext:** 573266-2026 ist eine Rahmenvereinbarung mit 2 Verlängerungen. Die Laufzeit („maximal 48 Monate“) steht nur
  im Freitext und weder als Datum noch als BT-36. Für Rahmenvereinbarungen fehlt das Laufzeitende also möglicherweise öfter
  strukturiert. Das ist eine Beobachtung aus einem Fall.
- **Zuschlagsdatum als Platzhalter:** 505084-2026 (Stichprobe aus der ersten Runde) enthält `AwardDate 2000-01-01`, ein Platzhalterdatum (d).

## Fazit

- **Laufzeit (Beginn, Ende, Dauer), Verlängerungsangaben und Haupt-CPV:** 15 von 15 ohne Abweichung, in den 5 Fällen aus
  Gebäudereinigung jeweils mit Beginn und Ende.
- **Kein Fehler der Ursache (a). Die STOPP-Regel greift nicht.**
- **Zu korrigieren:** Die Beschriftung von `total-value` im Datenqualitätsreport („BT-161“) ist falsch. Die Zahlen zum
  Auftragswert sind dadurch etwas zu günstig dargestellt, weil `total-value` auch dann befüllt ist, wenn BT-161 fehlt. Die
  Laufzeitaussagen sind davon nicht betroffen.
- **Grenzen:**
  - 15 Notices sind eine kleine Stichprobe. Seltene Fehler (< 10 %) würden damit wahrscheinlich nicht auffallen.
  - Geprüft wurde nur das 1. Los. Nur 7 Notices hatten mehrere Lose.
  - Die Gegenprobe in der Webansicht lief über ein Zusammenfassungswerkzeug und ist weniger streng als der XML-Vergleich.
