# Prüfung der Lese-Regeln für das Höchstende (Iteration 5, Schritt 3, test)

_Erzeugt mit `src/prepare/pruefung_hoechstende.py test`, Seed 20261031, je Herkunft 10 Lose, ohne Notices der Handsuche. Urteil von Hand: **richtig**, **falsch** (mit richtigem Wert) oder **unklar**._

## Auswertung (Test, Urteile von Claude, 2026-10-30)

Geprüfte Fassung: `src/prepare/vertragsliste.py` aus Commit a0aa419 (eingefroren vor dem Ziehen dieser Stichprobe).
Bewertet wird das **Höchstende**; Urteile von Claude allein (keine Zweitprüfung).

| Herkunft | richtig | falsch | unklar | Anteil an allen Losen mit GL |
|---|---|---|---|---|
| datum_text | 10 | 0 | 0 | 17,7 % |
| anzahl_x_laenge | 10 | 0 | 0 | 22,0 % |
| hoechstlaufzeit_text | 10 | 0 | 0 | 8,8 % |
| enddatum_ist_hoechstende | 10 | 0 | 0 | 4,5 % |
| keine_angabe | 10 | 0 | 0 | 32,3 % |
| unbestimmbar | 3 | 6 | 1 | 13,3 % |
| zusammen (ungewichtet) | 53/60 | 6 | 1 | |

Gewichtet mit den Anteilen der Herkunft (keine_verlaengerung und bt36_laenger, zusammen 1,5 %, ungeprüft und hier als richtig
gezählt): etwa **91 %** der Lose mit richtigem Höchstende (85,3 % aus den fünf fehlerfreien Arten + 13,3 % × 0,3 + 1,5 % = 90,8 %).
Mit nur 10 Losen je Art ist das eine grobe Schätzung (z. B. 10/10 schließt eine Fehlerquote bis etwa 28 % je Art nicht aus).
Die Fehler betreffen fast nur „unbestimmbar“. Folge: R1 fällt dort auf die Grundlaufzeit zurück und liegt eher zu früh.

Nebenbefund zur **Grundlaufzeit**: Bei „enddatum_ist_hoechstende“ wurde das frühere Ende der Grundlaufzeit in 0 von 10 Fällen erkannt
(häufigster Wortlaut „gilt zunächst bis zum …“, der Satz fiel durch den Satzfilter). Dort fallen R0 und R1 zusammen.

## H1: 333888-2025 Los 7 (datum_text)

- Beginn 2026-01-01, Ende Grundlaufzeit 2029-12-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2031-12-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis verlängert sich jeweils um ein weiteres Jahr, sofern die Auftraggeberin einer Fortsetzung nicht mit einer Frist von sechs Monaten vor Ablauf der Vertragsdauer widerspricht. Die Widerspruchsfrist für die Auftragnehmerin beträgt neun Monate vor Ablauf der Vertragslaufzeit. Der Widerspruch muss schriftlich erfolgen. Der Vertrag endet spätestens am 31.12.2031, ohne dass es einer …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H2: 110255-2025 Los 1 (datum_text)

- Beginn 2025-05-15, Ende Grundlaufzeit 2027-05-14 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2029-05-14**
- BT-57: 
- BT-54: Der Vertrag verlängert sich zweimal um jeweils ein Jahr, wenn dieser nicht mit einer Frist von 6 Monaten zum Vertragsende von Seiten des AN oder des AG gekündigt wird. Der Vertrag endet somit spätestens, ohne dass es einer Kündigung bedarf, zum 14.05.2029.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H3: 565762-2025 Los 2 (datum_text)

- Beginn 2025-10-01, Ende Grundlaufzeit 2027-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-09-30**
- BT-57: 
- BT-54: Die Vertragslaufzeit verlängert sich jeweils um ein weiteres Jahr, wenn der Vertrag nicht spätestens bis 31.03.2027 bzw. bis 31.03.2028 schriftlich gekündigt wird. Er endet in jedem Fall automatisch nach 4 Jahren am 30.09.2029. Es bedarf keiner gesonderten Kündigung.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H4: 197597-2024 Los 1 (datum_text)

- Beginn 2024-08-01, Ende Grundlaufzeit 2026-07-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2028-07-31**
- BT-57: Der Auftragnehmer verpflichtet sich, erforderliche Zusatzaufträge (Regieleistungen), auch kurzfristiger Art z. B. nach einem Wasserrohrbruch sowie nach größeren Umbau- oder Handwerksarbeiten zu übernehmen. Die erforderlichen Arbeiten sind schriftlich zu beauftragen und werden zu den jeweiligen Einzelpreisen aus der Angebotskalkulation unter Vorlage sorgsam und nachvollziehbar geführter sowie durch …
- BT-54: Dieser Vertrag wird für die Dauer von 2 Jahren geschlossen und tritt am 01.08.2024 in Kraft. Die Vertragslaufzeit verlängert sich jeweils um ein weiteres Jahr, wenn der Vertrag nicht spätestens zum 30.04.2026, bzw. zum 30.04.2027, vom Auftraggeber schriftlich gekündigt wird. Er endet in jedem Fall automatisch nach vier Schuljahren am 31.07.2028.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H5: 151114-2026 Los 1 (datum_text)

- Beginn 2026-04-01, Ende Grundlaufzeit 2028-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2032-12-31**
- BT-57: 
- BT-54: Verlängerung um jeweils 2 Jahre, maximal bis 31.12.2032
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H6: 51019-2024 Los 3 (datum_text)

- Beginn 2023-12-31, Ende Grundlaufzeit 2026-12-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-12-31**
- BT-57: 
- BT-54: Der Vertrag verlängert sich jeweils um ein weiteres Jahr, sofern er nicht von einem der Vertragspartner schriftlich mit einer Frist von sechs Monaten zum jeweiligen Jahresende gekündigt wird. Der Vertrag endet jedoch spätestens mit Ablauf des 31.12.2028, ohne dass es einer Kündigung bedarf.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H7: 780685-2024 Los 1 (datum_text)

- Beginn 2025-02-01, Ende Grundlaufzeit 2027-01-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2029-03-31**
- BT-57: 
- BT-54: Der Vertrag verlängert sich jeweils um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten gekündigt wird, er endet jedoch spätestens mit Ablauf des 31. März 2029
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Glasreinigung an Objekten der Stadt Fürth im Zeitraum vom 01.04.2025 bis 31.03.2027 mit jährlicher Option der Verlängerung bis maximal 31.03.2029.
- Urteil: richtig

## H8: 151886-2025 Los 1 (datum_text)

- Beginn 2025-03-03, Ende Grundlaufzeit 2028-06-30 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2029-07-13**
- BT-57: 
- BT-54: Der Auftraggeber behält sich die Option vor, den Vertrag um bis zu zwölf Monate, längstens bis zum 13.07.2029 (Ende Schuljahr 2028/2029), zu gleichen Bedingungen zu verlängern. Dies muss der Auftraggeber spätestens drei Monat vor Ablauf des Vertrags schriftlich gegenüber dem Auftragnehmer kenntlich machen.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Text nennt 31.03.2029 als spätestes Ende; Beginn/Ende-Felder weichen vom Text ab)

## H9: 15546-2026 Los 3 (datum_text)

- Beginn 2026-01-01, Ende Grundlaufzeit 2027-12-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2029-12-31**
- BT-57: 
- BT-54: Die Laufzeit beträgt 24 Monate (2 Jahre). Der Vertrag kann zweimal zu den bestehenden Bedingungen um jeweils ein weiteres Jahr verlängert werden. Bei der Option handelt es sich um ein einseitiges Gestaltungsrecht des Auftraggebers. Der Auftragnehmer hat keinen Anspruch auf Ausübung der Option. Das verlängerte Vertragsverhältnis kann vom Auftraggeber mit einer Frist von drei Monaten jeweils zum End …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H10: 36889-2025 Los 1 (datum_text)

- Beginn 2025-01-01, Ende Grundlaufzeit 2028-12-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2030-12-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis verlängert sich jeweils um ein weiteres Jahr, sofern die Auftraggeberin einer Fortsetzung nicht mit einer Frist von sechs Monaten vor Ablauf der Vertragsdauer widerspricht. Die Widerspruchsfrist für die Auftragnehmerin beträgt neun Monate vor Ablauf der Vertragslaufzeit. Der Widerspruch muss schriftlich erfolgen. Der Vertrag endet spätestens am 31.12.2030, ohne dass es einer …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H11: 368710-2026 Los 4 (anzahl_x_laenge)

- Beginn 2026-07-01, Ende Grundlaufzeit 2028-06-30 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2030-06-30**
- BT-57: Das Vertragsverhältnis kann maximal zweimal um jeweils ein weiteres Jahr verlängert werden.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H12: 665767-2024 Los 5 (anzahl_x_laenge)

- Beginn 2025-01-01, Ende Grundlaufzeit 2026-12-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2028-12-31**
- BT-57: Das Vertragsverhältnis verlängert sich maximal zweimal um jeweils ein weiteres Jahr, wenn es nicht zuvor mit einer Frist von 6 Monaten schriftlich von einer der Vertragsparteien gekündigt wird.
- BT-54: Die Talschule (Los 2) erhält voraussichtlich 2027 ein neues Gebäude, um das Los 2 mit Nutzungsbeginn dann erweitert wird.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H13: 403037-2024 Los 4 (anzahl_x_laenge)

- Beginn 2024-09-01, Ende Grundlaufzeit 2028-08-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2030-08-31**
- BT-57: 
- BT-54: Der AG kann den Vertrag je Los bis fünf Monate vor Ablauf durch schriftliche Erklärung um ein Jahr verlängern. Eine Verlängerung ist höchstens 2-mal bis zum Leistungsende 31.08.20930 möglich.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H14: 157480-2026 Los 4 (anzahl_x_laenge)

- Beginn 2026-03-01, Ende Grundlaufzeit 2030-02-28 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2033-02-28**
- BT-57: 
- BT-54: Verlängerungsoption um weitere 3 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H15: 649053-2026 Los 1 (anzahl_x_laenge)

- Beginn 2026-10-01, Ende Grundlaufzeit 2027-09-30 (enddatum), BT-58 3
- **Extrahiert: Höchstende 2030-09-30**
- BT-57: Es werden keine weiteren Optionen eingeräumt
- BT-54: Die Laufzeit der Beauftragung beträgt ein Jahr mit der Option zur dreimaligen Verlängerung um jeweils ein weiteres Jahr. Sofern vom Auftragsgeber nicht spätestens bis sechs Monate vor Ablauf des jeweiligen Jahres erklärt wird, die Option nicht ziehen zu wollen, verlängert sich die Beauftragung automatisch um jeweils ein weiteres Jahr. Nach maximal vier Jahren endet der Vertrag automatisch.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H16: 657664-2026 Los 11 (anzahl_x_laenge)

- Beginn 2026-11-01, Ende Grundlaufzeit 2029-10-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2031-10-31**
- BT-57: 
- BT-54: Der Auftraggeber ist berechtigt, die Laufzeit der Rahmenvereinbarung einseitig zweimal, um jeweils ein weiteres Jahr, zu verlängern. Die Verlängerung erfolgt durch schriftliche Mitteilung des Auftraggebers an den Auftragnehmer spätestens drei Monate vor Ablauf der jeweiligen Vertragslaufzeit. Der Auftragnehmer hat keinen Anspruch auf eine Verlängerung.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H17: 219899-2026 Los 1 (anzahl_x_laenge)

- Beginn 2026-05-01, Ende Grundlaufzeit 2029-04-30 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2030-04-30**
- BT-57: Der Vertrag verlängert sich um jeweils ein weiteres Jahr, sofern er nicht 3 Monate vor Vertragsende von einer der Parteien durch eigeschriebenen Brief gekündigt wird.
- BT-54: Optional Gebäudeinnenreinigung Haus 4 (Verwaltungsgebäude) sowie weitere Büroräume in den Häusern 7 und 8
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (rollierend, Höchstzahl 1 aus BT-58)

## H18: 97524-2024 Los 1 (anzahl_x_laenge)

- Beginn 2024-04-02, Ende Grundlaufzeit 2026-03-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-03-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis verlängert sich danach maximal dreimal automatisch um jeweils ein weiteres Jahr, sofern nicht eine der Parteien zuvor mit einer Frist von 6 Monaten zum Monatsende gekündigt hat.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H19: 274102-2025 Los 3 (anzahl_x_laenge)

- Beginn 2025-06-01, Ende Grundlaufzeit 2029-05-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2030-05-31**
- BT-57: 
- BT-54: Es besteht die einmalige Option durch die Auftraggeberin auf Verlängerung um ein Jahr.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H20: 143678-2025 Los 3 (anzahl_x_laenge)

- Beginn 2025-04-01, Ende Grundlaufzeit 2029-03-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2031-03-31**
- BT-57: Zweimalige Verlängerungsoption für je 12 Monate
- BT-54: Zweimalige Verlängerungsoption für je 12 Monate
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H21: 292650-2024 Los 1 (hoechstlaufzeit_text)

- Beginn 2024-06-01, Ende Grundlaufzeit 2025-05-31 (enddatum), BT-58 6
- **Extrahiert: Höchstende 2031-05-31**
- BT-57: Die maximale Vertragslaufzeit beträgt sieben Jahre. Der Vertrag kann mit einer Frist von drei Monaten erstmals zu dem im Auftragsschreiben genannten frühesten Ende der Ausführungsfrist gekündigt werden. Wird der Vertrag nicht zum vorgenannten frühesten Ende der Ausführungsfrist gekündigt, läuft er weiter und kann dann mit einer Frist von drei Monaten zum Ende eines jeden Monats gekündigt werden.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H22: 239610-2025 Los 1 (hoechstlaufzeit_text)

- Beginn 2025-08-01, Ende Grundlaufzeit 2029-07-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2031-07-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis wird zunächst für die Dauer von 4 Jahren bis zum 31.07.2029 abgeschlossen. Es verlängert sich, sofern nicht die Auftraggeberin mit einer Frist von 6 Monaten vor Ablauf der Vertragslaufzeit schriftlich widerspricht, jeweils um ein weiteres Jahr. Die entsprechende Widerspruchsfrist für den Auftragnehmer beträgt 9 Monate vor Ablauf der Vertragslaufzeit. Das verlängerte Vertrags …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (voller Text: „maximale Vertragsdauer beträgt 6 Jahre (bis 31.07.2031)“)

## H23: 524944-2026 Los 1 (hoechstlaufzeit_text)

- Beginn 2026-11-01, Ende Grundlaufzeit 2029-10-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2033-10-31**
- BT-57: 
- BT-54: Der Vetrag wird zunächst für eine Vertragslaufzeit von 3 Jahren geschlossen. Es besteht die Option der viermaligen Verlängerung um je ein Jahr. Die maximale Vertragslaufzeit beträgt 7 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H24: 229376-2026 Los 2 (hoechstlaufzeit_text)

- Beginn 2026-06-01, Ende Grundlaufzeit 2030-05-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2032-05-31**
- BT-57: 
- BT-54: Die erstmalige Leistungserbringung erfolgt zum 01.06.2026. Das Vertragsverhältnis wird zunächst für die Dauer von 4 Jahren bis zum 31.05.2030 abgeschlossen. Es verlängert sich, sofern nicht die Auftraggeberin mit einer Frist von 6 Monaten vor Ablauf der Vertragslaufzeit schriftlich widerspricht, jeweils um ein weiteres Jahr. Die entsprechende Widerspruchsfrist für den Auftragnehmer beträgt 9 Monat …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Außenjalousien: Die Reinigung der Außenjalousien umfasst insgesamt 2.031,96 m² (einseitig gemessen, allseitig zu reinigen), die Reinigung findet einmal während der Vertragslaufzeit statt.
- Urteil: richtig

## H25: 756565-2024 Los 1 (hoechstlaufzeit_text)

- Beginn 2025-01-01, Ende Grundlaufzeit 2025-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-12-31**
- BT-57: 
- BT-54: Wird der Vertrag nicht fristgerecht gekündigt, verlängert sich die Laufzeit um je ein weiteres Jahr, höchstens jedoch auf eine Gesamtlaufzeit von vier Jahren.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H26: 782681-2025 Los 10 (hoechstlaufzeit_text)

- Beginn 2025-10-01, Ende Grundlaufzeit 2027-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-09-30**
- BT-57: 
- BT-54: Es besteht die Möglichkeit, 2x um je 1 Jahr zu verlängern = maximale Gesamtlaufzeit 4 Jahre
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H27: 757804-2025 Los 3 (hoechstlaufzeit_text)

- Beginn 2025-08-01, Ende Grundlaufzeit 2027-07-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2029-07-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis verlängert sich um jeweils ein weiteres Jahr, wenn der Vertrag nicht mit einer Frist von drei Monaten zum Ende der jeweiligen Laufzeit von einem der Vertragspartner gekündigt wird, maximal jedoch bis zum 31.07.2029. Der Auftraggeber strebt eine längerfristige Zusammenarbeit an. Nach längstens vier Jahren muss erneut ausgeschrieben werden.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H28: 314137-2025 Los 3 (hoechstlaufzeit_text)

- Beginn 2025-06-01, Ende Grundlaufzeit 2029-05-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende 2031-05-31**
- BT-57: 
- BT-54: Das Vertragsverhältnis wird zunächst für die Dauer von 4 Jahren bis zum 31.05.2029 abgeschlossen. Es verlängert sich, sofern nicht die Auftraggeberin mit einer Frist von 6 Monaten vor Ablauf der Vertragslaufzeit schriftlich widerspricht, jeweils um ein weiteres Jahr. Die entsprechende Widerspruchsfrist für den Auftragnehmer beträgt 9 Monate vor Ablauf der Vertragslaufzeit. Das verlängerte Vertrags …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H29: 432273-2024 Los 1 (hoechstlaufzeit_text)

- Beginn 2025-02-01, Ende Grundlaufzeit 2028-01-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2032-01-31**
- BT-57: 
- BT-54: Die Vertragslaufzeit beginnt am 01.02.2025. Der Vertrag wird zunächst für eine Vertragslaufzeit von 3 Jahren geschlossen. Es besteht die Option der viermaligen Verlängerung um je ein Jahr. Die maximale Vertragslaufzeit beträgt 7 Jahre.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Zum weiteren Leistungsumfang gehört die optionale Durchführung der Sonderreinigung des 24 Stunden-Bereiches an Samstagen, Sonntagen und Feiertagen.
- Urteil: richtig

## H30: 107194-2024 Los 1 (hoechstlaufzeit_text)

- Beginn 2024-01-01, Ende Grundlaufzeit 2025-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2027-12-31**
- BT-57: Der Vertrag verlängert sich um jeweils 1 Jahr wenn er nicht 6 Monate vor Ablauf der Vertragszeit von einer Partei gekündigt wird. Die maximale Gesamtlaufzeit beträgt 4 Jahre.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H31: 228059-2025 Los 1 (unbestimmbar)

- Beginn 2025-01-01, Ende Grundlaufzeit 2026-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Es werden keine weiteren Optionen eingeräumt
- BT-54: Die Vertragslaufzeit beträgt zwei Jahre mit der Option zur Verlängerung für zwei weitere Jahre. Sofern vom Auftragsgeber kein Widerspruch der Option auf Verlängerung bekanntgegeben wird, verlängert sich der Vertrag automatisch um zwei weiteren Jahre. Der Bieter hat keinen Anspruch auf Vertragsverlängerung. Sollte die Option auf Wunsch des Bieters nicht ausgeübt werden, so hat dieser uns dies minde …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „Option zur Verlängerung für zwei weitere Jahre“ (einmal); richtig wäre 2028-12-31

## H32: 279353-2024 Los 10 (unbestimmbar)

- Beginn 2024-06-01, Ende Grundlaufzeit 2028-05-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Es besteht eine einmalige Option der Verlängerung um maximal 1 Jahr
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „einmalige Option der Verlängerung um maximal 1 Jahr“ (Länge nach „maximal“ nicht erkannt); richtig wäre 2029-05-31

## H33: 745490-2025 Los 1 (unbestimmbar)

- Beginn 2026-01-01, Ende Grundlaufzeit 2028-12-31 (enddatum), BT-58 1
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (BT-58 = 1 ohne Text, Länge unbekannt)

## H34: 196137-2025 Los 3 (unbestimmbar)

- Beginn 2025-06-01, Ende Grundlaufzeit 2028-05-31 (enddatum), BT-58 2
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (BT-58 = 2 ohne Text, Länge unbekannt)

## H35: 396304-2025 Los 1 (unbestimmbar)

- Beginn 2025-08-01, Ende Grundlaufzeit 2027-07-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: Die Laufzeit des Vertrags verlängert sich um jeweils ein weiteres Jahr, wenn er nicht vom Auftraggeber mit einer Frist von drei (3) Monaten zum Ende der laufenden Vertragslaufzeit gekündigt wird. Die Laufzeit des Vertrags endet spätestens vier (4) Jahre nach Beginn des Regelbetriebs.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „endet spätestens vier (4) Jahre nach Beginn“ nicht erkannt; richtig wäre 2029-07-31

## H36: 436533-2025 Los 3 (unbestimmbar)

- Beginn 2024-08-01, Ende Grundlaufzeit 2027-07-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: Nach vier Jahren die Option der Verlängerung um jeweils ein weiteres Jahr (hier zusätzlich 4 Jahre).
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **unklar** – „Nach vier Jahren … um jeweils ein weiteres Jahr (hier zusätzlich 4 Jahre)“, aber Grundlaufzeit laut Feldern 3 Jahre

## H37: 781010-2024 Los 1 (unbestimmbar)

- Beginn 2025-01-01, Ende Grundlaufzeit 2025-12-31 (enddatum), BT-58 3
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Option der Verlängerung bis maximal 4 Jahre (48 Monate) Vertragslaufzeit
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „bis maximal 4 Jahre (48 Monate) Vertragslaufzeit“ nicht erkannt; richtig wäre 2028-12-31

## H38: 300034-2025 Los 2 (unbestimmbar)

- Beginn 2025-06-30, Ende Grundlaufzeit 2028-07-21 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: Eine Verlängerung um zweimal ein Jahr ist möglich, wenn er nicht sechs Monate vor Ablauf der jeweiligen Vertragslaufzeit gekündigt wird.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „um zweimal ein Jahr“ nicht erkannt; richtig wäre 2030-07-21

## H39: 72791-2025 Los 4 (unbestimmbar)

- Beginn 2025-01-01, Ende Grundlaufzeit 2025-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: 
- BT-54: Der Vertrag beginnt am 01.01.2025 und läuft zunächst fest bis zum 31.12.2025. Er verlängert sich automatisch jeweils um ein weiteres Jahr, sofern der Verlängerung des Vertrages weder durch den Auftraggeber noch durch den Auftragnehmer bis spätestens sechs (6) Monate vor Ablauf des jeweiligen Vertragsjahres mit eingeschriebenen Brief widersprochen wird. Für die Fristwahrung ist der Zugang der vorge …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (rollierend ohne Höchstdauer)

## H40: 145945-2025 Los 1 (unbestimmbar)

- Beginn 2025-03-01, Ende Grundlaufzeit 2027-02-28 (enddatum), BT-58 1
- **Extrahiert: Höchstende unbestimmbar**
- BT-57: Eine Verlängerung erfolgt entsprechend den Bestimmungen der Besonderen Vertragsbedingungen einmalig um maximal 12 Monate.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: **falsch** – „einmalig um maximal 12 Monate“ (wie H32); richtig wäre 2028-02-29

## H41: 639270-2025 Los 2 (enddatum_ist_hoechstende)

- Beginn 2026-01-01, Ende Grundlaufzeit 2031-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2031-12-31**
- BT-57: 
- BT-54: Der Vertrag tritt am 01.01.2026 in Kraft und gilt zunächst bis zum 31.12.2028. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 31.12.2031.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H42: 757726-2025 Los 1 (enddatum_ist_hoechstende)

- Beginn 2026-01-01, Ende Grundlaufzeit 2029-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-12-31**
- BT-57: 
- BT-54: Leistungszeitraum/Vertragsdauer Dieser Vertrag tritt am 01.01.2026 in Kraft. Er läuft zunächst 6 – sechs – Monate auf Probe und kann während dieser Zeit von beiden Vertragspartnern mit einer Frist von 12 Wochen zum Monatsende gekündigt werden. Wird der Vertrag seitens des AN innerhalb der Probezeit gekündigt, trägt der AN den Aufwand für eine Neuausschreibung in Höhe von 5% der Jahresnettoangebots …
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (voller Text: „endet spätestens am 31.12.2029“) (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H43: 600964-2025 Los 6 (enddatum_ist_hoechstende)

- Beginn 2025-09-01, Ende Grundlaufzeit 2029-08-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-08-31**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Die Grundfläche in Quadratmetern (m2), die im Rahmen der wiederkehrenden Unterhaltsreinigung zu reinigen ist, beträgt ca. bei: Los 1 13.000,00 m2 Los 2 19.000,00 m2 Los 3 17.000,00 m2 Los 4 11.500,00 m2 Los 5 19.000,00 m2 Los 6 3.000,00 m2 Die Rahmenvereinbarung wird für 1 Jahr mit der Option der dreimaligen Verlängerung um ein weiteres Jahr geschlossen. Der Leistungszeitraum beginnt am 01.09.2025 …
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H44: 516032-2024 Los 2 (enddatum_ist_hoechstende)

- Beginn 2025-01-01, Ende Grundlaufzeit 2030-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2030-12-31**
- BT-57: Der Vertrag tritt am 01.01.2025 in Kraft und gilt zunächst bis zum 31.12.2027. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 31.12.2030.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H45: 434620-2026 Los 1 (enddatum_ist_hoechstende)

- Beginn 2026-08-01, Ende Grundlaufzeit 2030-07-31 (enddatum), BT-58 3
- **Extrahiert: Höchstende 2030-07-31**
- BT-57: Nach Ablauf der Probezeit endet der Vertrag am 31.07.2027 und verlängert sich danach jeweils um 1 Jahr (maximal 3 Verlängerungen), wenn er nicht mit einer Frist von 4 Monaten gekündigt wurde. Der Vertrag endet spätestens am 31.07.2030, ohne dass es einer Kündigung bedarf.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H46: 237415-2025 Los 3 (enddatum_ist_hoechstende)

- Beginn 2025-10-01, Ende Grundlaufzeit 2031-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2031-09-30**
- BT-57: 
- BT-54: Der Vertrag tritt am 01.10.2025 in Kraft und gilt zunächst bis zum 30.09.2028. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 30.09.2031.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H47: 718892-2024 Los 2 (enddatum_ist_hoechstende)

- Beginn 2025-02-01, Ende Grundlaufzeit 2031-01-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2031-01-31**
- BT-57: 
- BT-54: Der Vertrag tritt am 01.02.2025 in Kraft und gilt zunächst bis zum 31.01.2028. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 31.01.2031.
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H48: 258456-2024 Los 1 (enddatum_ist_hoechstende)

- Beginn 2024-10-01, Ende Grundlaufzeit 2030-09-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2030-09-30**
- BT-57: Der Vertrag tritt am 01.10.2024 in Kraft und gilt zunächst bis zum 30.09.2027. Der Vertrag verlängert sich je um ein weiteres Jahr, wenn er nicht mit einer Frist von sechs Monaten vor Vertragsende gekündigt wird und endet spätestens mit Ablauf des 30.09.2030.
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H49: 50133-2026 Los 7 (enddatum_ist_hoechstende)

- Beginn 2026-03-01, Ende Grundlaufzeit 2029-07-01 (enddatum), BT-58 1
- **Extrahiert: Höchstende 2029-07-01**
- BT-57: 01.03.2026 bis 19.07.2026 mit der Option der jährlichen Verlängerung, längstens bis zum 01.07.2029
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H50: 372335-2024 Los 2 (enddatum_ist_hoechstende)

- Beginn 2024-07-01, Ende Grundlaufzeit 2028-06-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-06-30**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Los 2: Glas- und Rahmenreinigung Gesundheitsamt für das Gesundheitsamt Chemnitz Gesamte Vertragslaufzeit: 01.07.2024 bis 30.06.2028 Der Vertrag läuft vom 01.07.2024 bis 30.06.2027 und verlängert sich um 12 weitere Monate, wenn er, durch den AG, nicht 3 Monate vor dem Vertragsende (30.06.2027) gekündigt wird. Er endet spätestens am 30.06.2028.
- Urteil: richtig (Höchstende richtig; das frühere Ende der Grundlaufzeit wurde nicht erkannt, GL bleibt = Enddatum)

## H51: 351382-2025 Los 1 (keine_angabe)

- Beginn 2025-07-01, Ende Grundlaufzeit 2029-06-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-06-30**
- BT-57: 
- BT-54: Optionen gemäß § 132 Abs. 2 Nr. 1 GWB
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig (Optionen nach § 132 GWB, keine Verlängerung)

## H52: 750900-2025 Los 2 (keine_angabe)

- Beginn 2025-11-01, Ende Grundlaufzeit 2029-10-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-10-31**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Rahmenvereinbarung über maximal 48 Monate
- Urteil: richtig (Rahmenvereinbarung max. 48 Monate = Grundlaufzeit)

## H53: 332495-2024 Los 1 (keine_angabe)

- Beginn 2024-08-01, Ende Grundlaufzeit 2026-07-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2026-07-31**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H54: 94596-2025 Los 1 (keine_angabe)

- Beginn 2025-03-01, Ende Grundlaufzeit 2030-02-28 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2030-02-28**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): Gegenstand der Leistung ist die Gewährleistung der Sauberkeit in den gesamten Einrichtungen des Saarländischen Staatstheaters, insbesondere in den folgenden Räumlichkeiten: - Großen Haus des Saarländischen Staatstheaters (Schillerpl. 1, 66111 Saarbrücken) - Alte Feuerwache (Landwehrplatz 1, 66111 Saarbrücken) - Verwaltung und Werkstätten des Saarländischen Staatstheaters (Heinrich-Böcking-Straße 2 …
- Urteil: richtig (voller Text: Laufzeit 5 Jahre, keine Verlängerung)

## H55: 706637-2024 Los 4 (keine_angabe)

- Beginn 2025-01-01, Ende Grundlaufzeit 2028-12-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-12-31**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H56: 404789-2024 Los 3 (keine_angabe)

- Beginn 2024-09-16, Ende Grundlaufzeit 2028-09-15 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-09-15**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H57: 364422-2024 Los 3 (keine_angabe)

- Beginn 2024-07-15, Ende Grundlaufzeit 2028-06-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-06-30**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H58: 608695-2026 Los 1 (keine_angabe)

- Beginn 2026-10-01, Ende Grundlaufzeit 2028-01-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2028-01-31**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H59: 719821-2024 Los 5 (keine_angabe)

- Beginn 2024-11-01, Ende Grundlaufzeit 2031-10-31 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2031-10-31**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig

## H60: 218463-2024 Los 1 (keine_angabe)

- Beginn 2024-05-01, Ende Grundlaufzeit 2029-04-30 (enddatum), BT-58 –
- **Extrahiert: Höchstende 2029-04-30**
- BT-57: 
- BT-54: 
- BT-24 (nur Sätze zu Laufzeit/Verlängerung): 
- Urteil: richtig
