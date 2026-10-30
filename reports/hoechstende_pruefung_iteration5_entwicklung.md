# Prüfung der Lese-Regeln für das Höchstende (Iteration 5, Schritt 3)

_Erzeugt mit `src/prepare/pruefung_hoechstende.py`, Seed 20261030, je Herkunft 10 Lose, ohne Notices der Handsuche. Urteil von Hand: **richtig**, **falsch** (mit richtigem Wert) oder **unklar**._

## Auswertung (Entwicklung, Urteile von Claude, 2026-10-30)

| Herkunft | richtig | falsch | Wert richtig, Herkunft falsch |
|---|---|---|---|
| datum_text | 10 | 0 | 0 |
| anzahl_x_laenge | 8 | 2 (H17, H18) | 0 |
| hoechstlaufzeit_text | 10 | 0 | 0 |
| unbestimmbar | 2 | 5 (H31, H33, H34, H36, H37) | 3 (H32, H35, H38) |

Folgen für `src/prepare/vertragsliste.py` (vor dem Testdurchgang): Regel 1a (Enddatum = Höchstende, wenn der Text es als spätestes
Ende nennt; GL dann aus „zunächst … bis“), Einheiten „Vertragsjahr/Leistungsjahr“, Höchstlaufzeit auch bei „auf max.“,
„Verlängerung maximal“ und „maximal bis zu einer Laufzeit von“. Diese Stichprobe ist damit Entwicklungsdaten; die Genauigkeit
misst der Testdurchgang (`hoechstende_pruefung_iteration5_test.md`).

## H1: 220298-2026 Los 2 (datum_text)

- Beginn 2026-04-01, Ende Grundlaufzeit 2028-04-30 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2030-04-30**
- BT-57: Der Vertrag kommt mit Erteilung des Zuschlags zustande. Die Leistungspflicht beginnt mit Zuschlag, nicht jedoch vor dem 01.05.2026. Der Vertrag verlängert sich um – Verlängerungsoption 1) ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und um – Verlängerungsoption 2) ebenfalls ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor  …
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H2: 7607-2025 Los 1 (datum_text)

- Beginn 2025-01-01, Ende Grundlaufzeit 2026-12-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2028-12-31**
- BT-57: Das Vertragsverhältnis kann danach seitens der AG durch einfaches Schreiben um jeweils ein weiteres Jahr verlängert werden. Die Möglichkeit der Verlängerung kann maximal zwei Mal wahrgenommen werden. Die maximal mögliche Vertragslaufzeit ist somit begrenzt bis zum 31.12.2028.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H3: 306431-2026 Los 2 (datum_text)

- Beginn 2026-05-01, Ende Grundlaufzeit 2027-04-30 (enddatum), BT-58 6
- **Extrahiert: Höchstende 2033-04-30**
- BT-57: Verlängerung maximal 7 Jahre (bis zum 30.04.2033)
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H4: 361736-2025 Los 16 (datum_text)

- Beginn 2025-04-01, Ende Grundlaufzeit 2025-11-28 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2026-10-30**
- BT-57: Verlängerungsoption für 2026: Ausführungszeitraum 02.03.2026 - 30.10.2026
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H5: 629836-2025 Los 2 (datum_text)

- Beginn 2025-10-01, Ende Grundlaufzeit 2028-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2030-09-30**
- BT-57: 
- BT-54: Das Vertragsverhältnis verlängert sich jeweils um ein weiteres Jahr, es sei denn der Auftraggeber erklärt a) bis zum 31.05.2028 für das Optionsjahr 2028/2029 und b) bis zum 31.05.2029 für das Optionsjahr 2029/2030 die Verlängerungsoption nicht ausüben zu wollen. Soweit nichts anderes geregelt ist, enden die Verträge hiernach, ohne dass es einer Kündigung bedarf, spätestens am 30.09.2030. Eine weit …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H6: 46066-2024 Los 6 (datum_text)

- Beginn 2024-01-01, Ende Grundlaufzeit 2028-03-31 (enddatum), BT-58 3
- **Extrahiert: Höchstende 2031-03-31**
- BT-57: 3-malige Verlängerungsoption um jeweils 1 Jahr. Vertrags-/Leistungsende spätestens (inkl. Verlängerungsoptionen): 31.03.2031
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H7: 120866-2026 Los 3 (datum_text)

- Beginn 2026-04-01, Ende Grundlaufzeit 2027-03-31 (enddatum), BT-58 4
- **Extrahiert: Höchstende 2031-03-31**
- BT-57: 
- BT-54: Der AG hat das Recht die Geltungsdauer des Vertrages durch Ausübung einer Option um ein Jahr (Vertragsende 31.03.2028) und letztlich bis zum 31.03.2031, zu verlängern. Der AN hat keinen Anspruch auf eine Optionsausübung durch den AG.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H8: 413340-2026 Los 4 (datum_text)

- Beginn 2026-07-01, Ende Grundlaufzeit 2027-06-30 (enddatum), BT-58 6
- **Extrahiert: Höchstende 2033-06-30**
- BT-57: Spätestes Vertragsende 30.06.2033
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H9: 178552-2025 Los 7 (datum_text)

- Beginn 2025-04-16, Ende Grundlaufzeit 2028-07-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2030-07-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis endet am 31.07.2028. Wird der Vertrag nicht bis neun Monate vor Vertragsbeendigung von einer der Parteien, in Textform gekündigt, so verlängert er sich automatisch jeweils um ein weiteres Jahr, ohne dass es diesbezüglich einer gesonderten Erklärung der Parteien bedarf. Das Vertragsverhältnis kann maximal um insgesamt 2 Jahre stillschweigend verlängert werden, so dass es spät …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Los 6 Glasreinigung: Glas- und Rahmenreinigung sowie optionale Sonderreinigung auf Abruf in 16 Gebäuden mit einer Grundfläche von ca. 13.000 qm und einer Jahresreinigungsfläche von ca. 13.000 qm.
- Urteil: richtig

## H10: 582428-2026 Los 1 (datum_text)

- Beginn 2026-09-01, Ende Grundlaufzeit 2027-08-31 (enddatum), BT-58 6
- **Extrahiert: Höchstende 2033-08-31**
- BT-57: Verlängerung maximal 7 Jahre (bis zum 31.08.2033)
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H11: 261451-2025 Los 3 (anzahl_x_laenge)

- Beginn 2025-07-01, Ende Grundlaufzeit 2029-06-30 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2031-06-30**
- BT-57: Laufzeit von 4 Jahren mit der Option auf Verlängerung um weitere 2 Jahre sofern der Vertrag nicht durch den Auftraggeber bis zum 31.03.2029 schriftlich gekündigt wird.
- BT-54: Option auf Verlängerung um weitere 2 Jahre sofern der Vertrag nicht durch den Auftraggeber bis zum 31.03.2029 schriftlich gekündigt wird.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H12: 473201-2024 Los 2 (anzahl_x_laenge)

- Beginn 2024-09-01, Ende Grundlaufzeit 2026-08-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-08-31**
- BT-57: 
- BT-54: Die Vertragslaufzeit verlängert sich maximal 2mal um 1 Jahr, wenn diese spätestens drei Monate vor Ablauf schriftlich verlängert wird und die Verlängerung von beiden Vertragsparteien rechtsverbindlich unterzeichnet wird.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H13: 479557-2025 Los 2 (anzahl_x_laenge)

- Beginn 2025-09-01, Ende Grundlaufzeit 2027-08-31 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2028-08-31**
- BT-57: Der AG behält sich vor, im Rahmen der gesetzlichen Vorgaben dem jeweiligen Bedarf entsprechend jederzeit einzelne Positionen der Leistungsbeschreibung und Preisblätter auszuklammern sowie die Anzahl der Reinigungen zu erhöhen oder zu vermindern. Des Weiteren behält sich der AG vor, einzelne Positionen der Leistungsbeschreibung und Preisblätter zu anderen Zeiten ausführen zu lassen. 2. Der AG kann  …
- BT-54: Das Vertragsverhältnis verlängert sich danach einmalig automatisch um ein weiteres Jahr, sofern nicht eine der Parteien zuvor mit einer Frist von 6 Monaten zum Monatsende gekündigt hat.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H14: 327163-2025 Los 9 (anzahl_x_laenge)

- Beginn 2025-09-01, Ende Grundlaufzeit 2029-08-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2031-08-31**
- BT-57: 
- BT-54: Option um zweimalige Verlängerung um jeweils ein Jahr.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H15: 730430-2025 Los 2 (anzahl_x_laenge)

- Beginn 2025-11-01, Ende Grundlaufzeit 2028-10-31 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2029-10-31**
- BT-57: Das Vertragsverhältnis verlängert sich danach maximal einmal automatisch um jeweils ein weiteres Jahr, sofern nicht eine der Parteien zuvor mit einer Frist von 6 Monaten zum Monatsende gekündigt hat.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Die Flächen sind in unterschiedlichen Intervallen maximal dreimal jährlich zu reinigen.
- Urteil: richtig

## H16: 560641-2024 Los 1 (anzahl_x_laenge)

- Beginn 2024-10-01, Ende Grundlaufzeit 2027-09-30 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2029-09-30**
- BT-57: Optional kann der Vertrag, mit Ablauf der regulären 36 monatigen Vertragslaufzeit, maximal zweimal um jeweils 12 weitere Monaten verlängert werden. Dieser optionalen Vertragsverlängerung müssen die Vertragsparteien spätestens 3 Monate vor Ende der jeweiligen Laufzeit zustimmen.
- BT-54: Für den Fall, dass der Auftragnehmer vor vollständiger Leistungserbringung wegen Kündigung oder Insolvenz ausfällt, behält sich der Auftraggeber vor, die verbleibenden Arbeiten den übrigen Bietern in der Reihenfolge des Ausschreibungsergebnisses anzutragen (§ 132 Abs. 2 Nr. 1 GWB)
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Ziel der Vergabe ist es, einen Dienstleistungspartner zu finden, der in der Lage ist, die qualitativen Anforderungen des UKA kombiniert mit den maximal möglichen wirtschaftlichen Effekten zu erfüllen.
- Urteil: richtig

## H17: 392341-2026 Los 1 (anzahl_x_laenge)

- Beginn 2026-07-01, Ende Grundlaufzeit 2030-06-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2033-06-30**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Jährliche Reinigungsfläche: ca. 2.473.310 m² Der Vertrag beginnt am 01.07.2026 und endet zunächst am 30.06.2028. Der Auftraggeber hat die Option, den Vertrag zwei Mal um je ein weiteres Jahr zu verlängern. Der Vertrag hat inklusive der Verlängerungsoptionen eine Laufzeit von maximal 4 Jahren und endet spätestens am 30.06.2030. Für den Standort Berlin Charlottenburg gilt abweichend eine Laufzeit vo …
- Urteil: **falsch** – Enddatum 2030-06-30 ist laut Text schon das Höchstende („endet spätestens am 30.06.2030“, zunächst bis 30.06.2028); richtig wäre Höchstende 2030-06-30

## H18: 578613-2024 Los 1 (anzahl_x_laenge)

- Beginn 2024-10-01, Ende Grundlaufzeit 2029-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2033-09-30**
- BT-57: Die Vertragslaufzeit beläuft sich auf ein Jahr ab Vertragsbeginn (01.10.2024 bis 30.09.2025), mit der Option seitens der AG auf eine viermalige Verlängerung um jeweils ein Jahr, längstens bis zum 30.09.2029. Der Vertrag verlängert sich stillschweigend, soweit der Vertrag nicht fristgerecht gekün-digt wird oder aufgrund des Eintritts einer auflösenden Bedingung endet.
- BT-54: ja
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – Enddatum 2029-09-30 ist laut Text das Höchstende („längstens bis zum 30.09.2029“); richtig wäre 2029-09-30

## H19: 670771-2024 Los 1 (anzahl_x_laenge)

- Beginn 2025-01-16, Ende Grundlaufzeit 2028-01-15 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2030-01-15**
- BT-57: 2-malige optionale Verlängerung um jeweils 1 Jahr
- BT-54: 2-malige optionale Verlängerung um jeweils 1 Jahr
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H20: 338444-2024 Los 1 (anzahl_x_laenge)

- Beginn 2024-08-01, Ende Grundlaufzeit 2028-07-31 (enddatum), BT-58 3
- **Extrahiert: Höchstende 2029-01-31**
- BT-57: Der Vertrag kann in beiderseitigem Einverständnis maximal 3x für jeweils 2 Monate verlängert werden.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H21: 769069-2023 Los 1 (hoechstlaufzeit_text)

- Beginn 2024-04-01, Ende Grundlaufzeit 2027-03-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2031-03-31**
- BT-57: 
- BT-54: Die Vertragslaufzeit beginnt am 01.04.2024. Der Vertrag wird zunächst für eine Vertragslaufzeit von 3 Jahren geschlossen. Es besteht die Option der viermaligen Verlängerung um je ein Jahr. Die maximale Vertragslaufzeit beträgt 7 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Optionale Leistungen: Sonderreinigung 24 Stunden-Bereich an Sonn- und Feiertagen
- Urteil: richtig

## H22: 710188-2024 Los 1 (hoechstlaufzeit_text)

- Beginn 2025-01-01, Ende Grundlaufzeit 2025-12-31 (enddatum), BT-58 3
- **Extrahiert: Höchstende 2028-12-31**
- BT-57: 
- BT-54: Die Laufzeit des Vertrages beträgt 1 Jahr. Der Vertrag enthält die Option der dreimaligen Verlängerung um jeweils 1 Jahr. Die maximale Laufzeit des Vertrages beträgt 4 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H23: 314536-2024 Los 2 (hoechstlaufzeit_text)

- Beginn 2024-09-01, Ende Grundlaufzeit 2027-08-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2031-08-31**
- BT-57: 
- BT-54: Der Vertrag wird zunächst für eine Vertragslaufzeit von drei Jahren geschlossen. Es besteht die Option der viermaligen Verlängerung um je ein Jahr. Die maximale Vertragslaufzeit beträgt 7 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H24: 101643-2026 Los 4 (hoechstlaufzeit_text)

- Beginn 2026-05-01, Ende Grundlaufzeit 2030-04-30 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2032-04-30**
- BT-57: 
- BT-54: Die erstmalige Leistungserbringung erfolgt zum 01.05.2026. Das Vertragsverhältnis wird zunächst für die Dauer von 4 Jahren bis zum 30.04.2030 abgeschlossen. Es verlängert sich, sofern nicht die Auftraggeberin mit einer Frist von 6 Monaten vor Ablauf der Vertragslaufzeit schriftlich widerspricht, jeweils um ein weiteres Jahr. Die entsprechende Widerspruchsfrist für den Auftragnehmer beträgt 9 Monat …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H25: 141011-2025 Los 3 (hoechstlaufzeit_text)

- Beginn 2025-02-01, Ende Grundlaufzeit 2026-01-31 (enddatum), BT-58 3
- **Extrahiert: Höchstende 2029-01-31**
- BT-57: 
- BT-54: Eine Verlängerung der Vertragslaufzeit um jeweils 12 Monate kann bis zu drei Mal (auf insgesamt maximal 48 Monate) optional (einseitiges Optionsrecht) durch den Auftraggeber drei Monate vor Ablauf des Vertrages erklärt werden. In jedem Fall endet der Vertrag spätestens am 31.01.2029, ohne dass es einer besonderen Kündigung bedarf.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H26: 574666-2026 Los 3 (hoechstlaufzeit_text)

- Beginn 2026-10-01, Ende Grundlaufzeit 2030-09-30 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2032-09-30**
- BT-57: 
- BT-54: Die erstmalige Leistungserbringung erfolgt zum 01.10.2026. Das Vertragsverhältnis wird zunächst für die Dauer von 4 Jahren bis zum 30.09.2030 abgeschlossen. Es ver-längert sich, sofern nicht die Auftraggeberin mit einer Frist von 6 Monaten vor Ablauf der Vertragslaufzeit schriftlich widerspricht, jeweils um ein weiteres Jahr. Die entsprechende Widerspruchsfrist für den Auftrag-nehmer beträgt 9 Mon …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H27: 175729-2026 Los 4 (hoechstlaufzeit_text)

- Beginn 2026-04-01, Ende Grundlaufzeit 2028-03-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2030-03-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis wird für die Dauer von 2 Jahren abgeschlossen. Es verlängert sich um ein weiteres Jahr, wenn es seitens des Auftraggebers nicht fristgemäß gekündigt wird. Es kann mit einer Frist von 6 Monaten vor Ablauf der jeweiligen Vertragslaufzeit gekündigt werden. Die maximale Laufzeit des Vertrages beträgt 4 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H28: 411254-2025 Los 2 (hoechstlaufzeit_text)

- Beginn 2025-10-01, Ende Grundlaufzeit 2027-09-30 (enddatum), BT-58 3
- **Extrahiert: Höchstende 2030-09-30**
- BT-57: 
- BT-54: Der Vertrag verlängert sich danach jeweils um ein Jahr, wenn er nicht durch den Auftraggeber mit einer Frist von 12 Wochen zum Ende der jeweiligen Laufzeit gekündigt wird. Der Vertrag endet jedoch spätestens nach einer Gesamtlaufzeit von 5 Jahren zum 30.09.2030 ohne dass es einer Kündigung bedarf.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H29: 663107-2025 Los 6 (hoechstlaufzeit_text)

- Beginn 2025-10-01, Ende Grundlaufzeit 2026-10-01 (enddatum), BT-58 6
- **Extrahiert: Höchstende 2032-09-30**
- BT-57: Die maximale Vertragslaufzeit beträgt sieben Jahre. Der Vertrag kann mit einer Frist von drei Monaten erstmals zu dem im Auftragsschreiben genannten frühesten Ende der Ausführungsfrist gekündigt werden. Wird der Vertrag nicht zum vorgenannten frühesten Ende der Ausführungsfrist gekündigt, läuft er weiter und kann dann mit einer Frist von drei Monaten zum Ende eines jeden Monats gekündigt werden. D …
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H30: 338060-2025 Los 1 (hoechstlaufzeit_text)

- Beginn 2025-06-01, Ende Grundlaufzeit 2028-05-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2032-05-31**
- BT-57: 
- BT-54: Die Vertragslaufzeit beginnt am 01.03.2025. Der Vertrag wirdzunächst für eine Vertragslaufzeit von 3 Jahren geschlossen. Es besteht die Option der viermaligen Verlängerung um je ein Jahr. Die maximale Vertragslaufzeit beträgt 7 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H31: 373984-2025 Los 3 (unbestimmbar)

- Beginn 2025-07-01, Ende Grundlaufzeit 2027-06-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: Verlängerung erfolgt automatisch um jeweils ein Jahr, maximal bis zu einer Laufzeit von vier Jahren, sofern er nicht mit einer Frist von drei Monaten zum Ende des jeweiligen Vertragsjahres gekündigt wird.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „maximal bis zu einer Laufzeit von vier Jahren“ nicht erkannt; richtig wäre 2029-06-30

## H32: 257331-2024 Los 1 (unbestimmbar)

- Beginn 2024-07-01, Ende Grundlaufzeit 2030-06-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Der Vertrag tritt am 01.07.2024 in Kraft und gilt zunächst bis zum 30.06.2027. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 30.06.2030.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **Wert richtig, Herkunft falsch** – Enddatum ist das Höchstende („endet spätestens mit Ablauf des 30.06.2030“); R1 trifft über den Rückfall auf GL zufällig das richtige Datum

## H33: 135610-2024 Los 5 (unbestimmbar)

- Beginn 2024-04-01, Ende Grundlaufzeit 2026-03-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Das Vertragsverhältnis verlängert sich stillschweigend jeweils um ein weiteres Vertragsjahr (01.04. bis 31.03), maximal zweimal, sollte es nicht mit einer Frist von 3 Monaten zum Ende des jeweiligen Vertragsjahres durch den AG gekündigt werden. Mit Ablauf der zweiten Verlängerung endet, ohne dass es einer gesonderten Kündigung bedarf, das Vertragsverhältnis automatisch.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „Vertragsjahr“ nicht als Einheit erkannt; richtig wäre 2028-03-31 (2 × 1 Jahr)

## H34: 62179-2026 Los 1 (unbestimmbar)

- Beginn 2026-02-01, Ende Grundlaufzeit 2027-01-31 (enddatum), BT-58 4
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Option der Verlängerung auf max. 5 Jahre
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „auf max. 5 Jahre“ nicht erkannt; richtig wäre 2031-01-31

## H35: 412095-2025 Los 1 (unbestimmbar)

- Beginn 2025-08-01, Ende Grundlaufzeit 2030-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: Der Vertrag tritt am 01.08.2025 in Kraft und gilt zunächst bis zum 30.09.2027. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 30.09.2030.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **Wert richtig, Herkunft falsch** – wie H32 (spätestens 30.09.2030 = Enddatum)

## H36: 541478-2025 Los 3 (unbestimmbar)

- Beginn 2025-09-01, Ende Grundlaufzeit 2026-08-31 (enddatum), BT-58 6
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Verlängerung maximal 7 Jahre
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „Verlängerung maximal 7 Jahre“ (Gesamtlaufzeit, vgl. H3) nicht erkannt; richtig wäre 2032-08-31

## H37: 137884-2026 Los 5 (unbestimmbar)

- Beginn 2026-07-01, Ende Grundlaufzeit 2027-06-30 (enddatum), BT-58 6
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Verlängerung maximal 7 Jahre
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – wie H36; richtig wäre 2033-06-30

## H38: 610301-2024 Los 2 (unbestimmbar)

- Beginn 2024-12-01, Ende Grundlaufzeit 2030-11-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: Der Vertrag tritt am 01.12.2024 in Kraft und gilt zunächst bis zum 30.11.2024. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 30.11.2030.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **Wert richtig, Herkunft falsch** – wie H32 (spätestens 30.11.2030 = Enddatum)

## H39: 537921-2026 Los 4 (unbestimmbar)

- Beginn 2026-10-01, Ende Grundlaufzeit 2030-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: V Allgemeine Vertragsbedingungen Nr. 4 Der Auftragsstart ist für Los I - Los IV der 01. Oktober 2026. Der Reinigungsvertrag wird für die Dauer von 4 Jahren ab Auftragsstart abgeschlossen und kann erstmals zum Ablauf des vierten Jahres mit einer Frist von 3 Monaten gekündigt werden. Nach Ablauf des 4. Jahres kann der Vertrag mit einer Frist von 3 Monaten zum Monatsende gekündigt werden. Der Vertrag …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig – nach 4 Jahren monatlich kündbar, kein Höchstende

## H40: 24281-2025 Los 7 (unbestimmbar)

- Beginn 2025-01-01, Ende Grundlaufzeit 2028-12-31 (enddatum), BT-58 1
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig – BT-58 = 1 ohne Text, Länge unbekannt
