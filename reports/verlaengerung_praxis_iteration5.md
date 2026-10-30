# Laufzeit und Verlängerungen in der Praxis (Iteration 5, Schritt 2)

_Erzeugt mit `src/verlaengerung_praxis.py`. Grobe Textmuster, Größenordnungen; Fakten und Interpretation getrennt._

## Definition laut eForms SDK

Quelle: `translations/business-term_de.xml` im [eForms SDK](https://github.com/OP-TED/eForms-SDK) (Branch develop, abgerufen 2026-10-30).

- **BT-36 Laufzeit:** „… vom Beginn bis zum Ende. Dies umfasst etwaige Optionen und Verlängerungen.“
- **BT-537 Ende der Laufzeit:** „Angaben zum (voraussichtlichen) Ende der Laufzeit …“, ohne Aussage zu Verlängerungen.
- **BT-538:** „Laufzeit unbekannt, unbegrenzt, usw.“
- **BT-58 Höchstzahl der Verlängerungen:** „Die maximale Zahl der Vertragsverlängerungen …“, ohne Länge je Verlängerung.
- **BT-57:** „Sonstige Informationen über die Verlängerung(en).“ (Freitext); **BT-54:** „Die Beschreibung der Optionen.“
- Vor eForms (Formular F02/F05, Abschnitt II.2.7): Beginn/Ende oder Dauer, „verlängerbar ja/nein“ (`RENEWAL`/`NO_RENEWAL`) und
  Freitext `RENEWAL_DESCR`. Eine Definition, ob die Laufzeit Verlängerungen einschließt, wurde im Schema nicht gefunden.

## Fakten: eForms-Zuschläge

Population: eForms-Zuschläge, Haupt-CPV 90910/90911/90919, nur Originale, veröffentlicht 25.10.2023–30.09.2026: **4307**.

| | Anzahl |
|---|---|
| Enddatum BT-537 vorhanden | 3235/4307 = 75,1 % |
| kein Enddatum, aber Beginn + Dauer (BT-536 + BT-36) | 44/4307 = 1,0 % |
| nur BT-538 (unbekannt/unbegrenzt) | 62/4307 = 1,4 % |
| keine verwertbare Laufzeit | 966/4307 = 22,4 % |

Unter den 3279 Zuschlägen mit bestimmbarem Ende:

| | Anzahl |
|---|---|
| BT-58 > 0 (Verlängerung möglich) | 1048/3279 = 32,0 % (Wilson 30,4–33,6) |
| BT-58 = 0 | 41/3279 = 1,3 % |
| BT-58 fehlt | 2190/3279 = 66,8 % |
| BT-58 = 0 oder fehlt, aber „verläng…“ im Text BT-57/BT-54 | 947/2231 = 42,4 % |

Unter den 1048 Zuschlägen mit BT-58 > 0 (Text = BT-57 und BT-54 zusammen):

| | Anzahl |
|---|---|
| BT-57 nicht leer | 569/1048 = 54,3 % |
| Text nennt Länge je Verlängerung („um jeweils ein Jahr“) | 784/1048 = 74,8 % |
| Text nennt Höchstlaufzeit („maximale Laufzeit 4 Jahre“) | 141/1048 = 13,5 % |
| Text nennt ein Datum | 487/1048 = 46,5 % |
| mindestens eine dieser Angaben | 869/1048 = 82,9 % (Wilson 80,5–85,1) |

**Bedeutet das Feld die Grundlaufzeit oder das Höchstende?** Vergleich mit der im Text genannten Höchstlaufzeit (±1 Monat = gleich):

| Feld | n | Feld kürzer als Höchstlaufzeit | gleich | länger |
|---|---|---|---|---|
| Beginn bis BT-537 | 289 | 274/289 = 94,8 % (Wilson 91,6–96,8) | 11 | 4 |
| BT-36 | 3 | 3/3 = 100,0 % (Wilson 43,8–100,0) | 0 | 0 |

„Länger“ entsteht vor allem, wenn das Muster eine Höchstdauer **je Verlängerung** greift („maximal 12 Monate“).

**BT-36 neben Beginn und Ende** (beide angegeben, n = 37): BT-36 gleich der Datumsspanne (±1 Monat) 27/37 = 73,0 % (Wilson 57,0–84,6), BT-36 länger 7/37 = 18,9 % (Wilson 9,5–34,2), BT-36 kürzer 3/37 = 8,1 %.

Beispiele (BT-58 > 0, erste 8 in Dateireihenfolge):

| Notice | Beginn | Ende | BT-36 (Mon.) | BT-58 | BT-57 (Auszug) |
|---|---|---|---|---|---|
| 657984-2023 | 2024-04-01 | 2025-07-31 | 40 | 2 | 2-fache Vertragsverlängerung um jeweils ein Schuljahr (01.08. bis einschließlich 31.07.); pro Schuljahr können im Rahmen der Unterhaltsreinigung Regieleistungen im Wert von max. 16.200,00 Euro brutto  |
| 711588-2023 | 2024-02-01 | 2028-01-31 | – | 1 | Die Laufzeit dieses Vertrages verlängert sich einmalig um zwei weitere Jahre, sofern die Auftraggeberin der Fortsetzung des Vertragsverhältnisses nicht mit einer Frist von sechs Monaten vor Ablauf der |
| 727372-2023 | 2024-01-01 | 2025-12-31 | – | 2 | Die Leistungszeit beginnt am 01. Januar 2024 und endet am 31. Dezember 2025. Der Vertrag kann jeweils um 1 Jahr verlängert werden, endet ohne Kündigung jedoch spätestens zum 31.12.2027. |
| 742247-2023 | 2024-01-01 | 2025-08-31 | – | 2 | Verlängerungsoption: 2 x 12 Monate bis 31.08.2027. Die Vertragslaufzeit beträgt 20 Monate. Sie verlängert sich 2-mal um weitere 12 Monate, wenn er nicht 6 Monate vor Vertragsende durch den AG gekündig |
| 783383-2023 | 2023-12-18 | 2025-11-30 | – | 2 | Es besteht zweimal eine einjährige Verlängerungsoption, sodass die maximale Laufzeit am 30.11.2027 erreicht ist. Der Vertrag verlängert sich automatisch um die einjährige Verlängerungsoption, wenn er  |
| 794901-2023 | 2024-01-01 | 2024-12-31 | – | 3 | Der Auftrag kann sich maximal 3 mal um je ein weiteres Jahr verlängern. |
| 38887-2024 | 2023-12-01 | 2028-02-29 | – | 3 | 3-malige Verlängerungsoption um jeweils 1 Jahr. Vertrags-/Leistungsende spätestens (inkl. Verlängerungsoptionen): 28.02.2031 3-malige Verlängerungsoption um jeweils 1 Jahr. Vertrags-/Leistungsende spä |
| 46066-2024 | 2024-01-01 | 2028-03-31 | – | 3 | 3-malige Verlängerungsoption um jeweils 1 Jahr. Vertrags-/Leistungsende spätestens (inkl. Verlängerungsoptionen): 31.03.2031 3-malige Verlängerungsoption um jeweils 1 Jahr. Vertrags-/Leistungsende spä |

## Fakten: vor eForms (A11-Zufallsstichprobe)

Referenzierte Ausschreibungen F02/F05 der 30 zufälligen Zuschläge 2018–2023 aus Iteration 3: **28** Dateien.

| | Anzahl |
|---|---|
| `RENEWAL` (verlängerbar) | 17/28 = 60,7 % |
| `NO_RENEWAL` | 11/28 = 39,3 % |
| keine Angabe | 0/28 = 0,0 % |
| bei `RENEWAL`: `RENEWAL_DESCR` vorhanden | 17/17 = 100,0 % |
| bei `RENEWAL`: Text nennt Länge, Höchstlaufzeit oder Datum | 12/17 = 70,6 % |
| Beginn bis DATE_END kürzer als genannte Höchstlaufzeit | 1/1 = 100,0 % (gleich 0, länger 0) |

Beispiele:

| Notice | DATE_START | DATE_END | RENEWAL_DESCR (Auszug) |
|---|---|---|---|
| 124768-2019 | 2019-07-04 | 2023-07-03 | Eine Verlängerung erfolgt entsprechend den Bestimmungen der Besonderen Vertragsbedingungen um ein Jahr. |
| 212554-2022 | 2022-10-01 | 2023-09-30 | Dieser Vertrag tritt am 01.10.2022 in Kraft und hat eine Laufzeit bis zum 30.09.2023. Eine Verlängerung der Vertragslaufzeit um jeweils 12 Monate kann bis zu drei Mal (auf insgesamt maximal 48 Monate) |
| 306400-2020 | 2020-11-01 | 2022-10-31 | Optional kann die Vertragslaufzeit durch den AG zweimal jeweils um ein Jahr verlängert werden. Diese Option kann einseitig vom AG bis 3 Monate vor Ende der Vertragslaufzeit gezogen werden. Der AG teil |
| 3426-2019 | 2019-09-01 | 2023-08-31 | Max. einmal um 1 Jahr |
| 342694-2019 |  |  | Der AG hat das Recht die Geltungsdauer des Vertrages durch Ausübung einer Option zweimalig jeweils um ein Jahr bis zum 31.12.2022 und letztmalig bis zum 31.12.2023 zu verlängern. Der AN hat keinen Ans |
| 354765-2022 | 2022-10-01 | 2025-09-30 | Der Vertrag verlängert sich um jeweils 12 Monate, sofern nicht gekündigt wird. Der Vertrag läuft längstens bis zum 30.09.2027 und wird automatisch beendet. |

## Interpretation

- In der Praxis bezeichnet BT-537 das **Ende der Grundlaufzeit**; das gilt auch für `DATE_END` vor eForms. Für die Regeln in
  `docs/business.md` §7.1 heißt das: „Ende der Grundlaufzeit“ = BT-537; das Höchstende muss aus BT-58 und dem Freitext
  (BT-57, BT-54; vor eForms `RENEWAL_DESCR`) gewonnen werden.
- BT-36 ist uneinheitlich (siehe Vergleich mit der Datumsspanne): teils Grundlaufzeit, teils Laufzeit mit Verlängerungen wie in
  der Definition. Ist BT-36 länger als die Datumsspanne, ist das ein Hinweis auf das Höchstende. „Beginn + BT-36“ als Ende der
  Grundlaufzeit betrifft nur wenige Zuschläge ohne Enddatum, ist aber unsicher.
- BT-58 allein reicht nicht: Es nennt nur die Zahl der Verlängerungen, nicht ihre Länge. Die Länge steht meist im Freitext.
- Verlängerungen kommen auch ohne BT-58 > 0 vor (Text erwähnt „verläng…“; Obergrenze, weil auch „keine Verlängerung“ mitzählt).
  Die Regel muss den Text daher auch dort lesen.
- Die Zahlen beruhen auf groben Mustern. Wie gut eine Extraktion des Höchstendes wirklich ist, misst erst Schritt 3 an Beispielen.
