# Evaluation Iteration 10b (Gesamtprüfung durch den Subagenten `evaluator`, 2026-11-05)

_Gekürzte Wiedergabe des Berichts des Evaluators (nur Lesezugriff, keine Skriptläufe; Wilson-Intervalle und Tests von Hand gerechnet; die Stichprobe der 10 übereinstimmenden Lose ist systematisch statt zufällig, weil der Seed nicht ausgeführt werden konnte). Urteile stammen vom Evaluator; Einordnungen des Projekts stehen in `docs/iterationen.md` (Ergebnis Iteration 10 und 10b)._

## Urteil je Kriterium
| Kriterium | Urteil | Beleg |
|---|---|---|
| W8a (≥ 16 Lose und p < 0,05) | **nicht erfüllt, rechnerisch unerreichbar** (nur 15 diskordante Lose) | Differenz +15, p = 2·(½)^15 = 6,1·10⁻⁵ nachgerechnet |
| W8b (≥ 8 Lose und p < 0,05) | erfüllt, nur schwach aussagekräftig | +10, p = 2/1024 = 0,00195 nachgerechnet |
| W9 Ursachenklassen | gemessen, Klassifikation von M7 fehlerhaft | a 5, b 6, e 4 |
| W10 Abdeckung | gemessen, aber zirkulär | 160/160; beide Seiten stammen aus TED |
| W11 Verfahren | im Wesentlichen erfüllt | Commit-Reihenfolge stimmt; Unerreichbarkeit von W8a vor den Leserantworten offengelegt |
| Hypothese „über die Granularität hinaus“ | **nicht belegt** | siehe Sensitivitätstest |

## Einordnung der 15 diskordanten Lose (Evaluator, je Los am Rohtext)
- **Höchstende statt Grundlaufzeit (Definition): 7** (M7, M33, M34, M37, M52, M63, M67), alle mit derselben Textvorlage („tritt … in Kraft und gilt zunächst bis … endet spätestens“), also effektiv **ein** Mechanismus.
- **Losebene (Granularität): 4** (M42, M116, M132, M159).
- **Zuordnungsfehler der Pipeline: 1** (M54: der Vergabeweiser-Eintrag gehört zu einer anderen Ausschreibung, Vreden statt Lengerich; Weg 2). Gehört nicht zu „Vergabeweiser liest falsch“.
- **Abweichung bei Vergabeweiser, Ursache offen: 2** (M3: 24 statt 48 Monate; M22: April statt Juni; möglicherweise Stand der Ausschreibung statt des Zuschlags, nicht geprüft).
- **Mehrdeutig: 1** (M49: Titel „ab 01.05.2025“ erlaubt die Deutung von Vergabeweiser).
- M7 wurde nach der vorab festgelegten Reihenfolge der Klassen als (a) geführt, ist aber ein Höchstende-Fall; die Einordnung als (a) entstand, weil die Liste bei Los 3 derselben Bekanntmachung selbst falsch liegt. Mit M7 als (b) stünde W8b bei +11 statt +10.
- Echte Lesefehler von Vergabeweiser: höchstens 2 bis 3, nicht belegt.

## Zirkularität und Blindheit
- Der Vergleichswert ist bei 12 von 15 Losen durch ausdrückliche Textangaben gedeckt (`feste_ende`, `feste_dauer`); bei M22, M54, M159 greift er auf das Feld EndDate zurück (dieselbe Basisregel wie die Liste). Die Aufgabe fragt ausdrücklich nach der ersten festen Laufzeit ohne Optionen.
- Keine Verankerung erkennbar (keine Listen- oder Vergabeweiser-Werte im Paket). 15 von 15 Übereinstimmungen der Leser sind **kein Zeichen von Unabhängigkeit** (gleiche Familie, gleiche Anweisung, ausdrücklicher Text). Eine menschliche Gegenlesung fehlt. Das Protokoll der Leserläufe liegt außerhalb des Repos (`C:\leser10b`).

## Die 145 übereinstimmenden Lose (10, systematisch gezogen: M9, M24, M41, M59, M75, M89, M103, M118, M133, M147)
6 richtig, 2 konsistent (kein Optionstext gefunden), 1 nicht sicher prüfbar, **1 beide falsch (M59**: „Der Vertrag läuft vom 01.07.2024 bis 30.06.2027 und verlängert sich um 12 weitere Monate … endet spätestens am 30.06.2028“; Liste und Vergabeweiser geben das Höchstende). 1 von 10, Wilson etwa 1,8–40,4 %: ein Hinweis, keine Rate. Die Differenz bleibt unverändert, die absolute Genauigkeit der Liste ist aber nicht belegt, weil beide Quellen dasselbe TED-Feld nutzen.

## Gesamtbild beider Stichproben (von Hand gerechnet)
| | Diskordanzrate | nur Liste richtig | Wilson 95 % |
|---|---|---|---|
| Iteration 10 (n = 70) | 12/70 = 17,1 % | 8/70 = 11,4 % | etwa 5,9–21,0 % |
| Iteration 10b (n = 160) | 15/160 = 9,4 % | 15/160 = 9,4 % | 5,8–14,9 % |
| zusammen, roh gepoolt | 27/230 | 23/230 = 10,0 % | etwa 6,8–14,6 % |

**Sensitivitätstest:** Zählt man das Höchstende (Definition) auch als „richtig für Vergabeweiser“, bleiben nach Abzug des Zuordnungsfehlers M54 die Fälle M3, M22, M49: 3 : 0, exakter zweiseitiger Test p = 0,25 (ohne M49: 2 : 0, p = 0,5). Der Vorsprung über Granularität und Definition hinaus ist **nicht belegt**.

## Zulässig und nicht zulässig
- **Zulässig:** „Auf zwei Stichproben (n = 70 und n = 160) weicht das Datum von Vergabeweiser in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt; in 10b waren 11 von 15 dieser Fälle Höchstende oder Losebene, höchstens 3 sind Abweichungen anderer Art.“
- **Nicht zulässig:** „Die Liste ist genauer als Vergabeweiser“; „Vorsprung belegt“ ohne den Zusatz „auf Los- und Definitionsebene“; „Vergabeweiser liest falsch“; jede Gleichheitsaussage („kein Vorteil“, „mindestens gleich gut“).

## Schwächen nach Gewicht
**Kritisch:** (1) Gemeinsame Quelle und gemeinsame Fehler: gemessen ist nur der Unterschied dort, wo die Quellen abweichen. (2) Der Test misst überwiegend Definition und Granularität, nicht Lesequalität; W8b entlastet Vergabeweiser nur bei der Losebene, nicht beim Höchstende. (3) Die Vorab-Folge für „W8a verfehlt“ („Aussage ‚kein Vorteil‘ gilt weiter“) widerspricht der gemessenen Richtung; für „W8a verfehlt und W8b erfüllt“ gibt es keine Regel.
**Mittel:** Zuordnungsfehler bei Weg 2 (M54); zusätzliche Listenfehler außerhalb der Stichprobe (12853-2024 Los 3, M59: Textmuster „gilt bis … ohne ‚zunächst‘“ und „läuft vom … bis … und verlängert sich“ werden nicht gefangen); Leser nicht unabhängig, keine Menschenprüfung; Clustering (7 Fälle eine Textvorlage); Auswahlverzerrung (nur Lose mit Listenende, 5.754 von 9.325 Losen; Lose ohne Listenende, etwa 20 %, gehen nicht ein); Klassifikation M7.
**Gering:** Der Satz „Abweichungen von der Vorab-Festlegung: keine“ steht fest im Skript (`vergleich_iteration10b.py` Z. 391) und verschweigt die Unerreichbarkeit von W8a; Stichprobe der 145 nur n = 10 und nicht zufällig; Protokoll außerhalb des Repos.

## Betroffene Annahmen
A2 bleibt widerlegt; A3 ungeprüft (W10 zirkulär); A4 bleibt bestätigt, kein neuer Beleg zur Qualität; A15 ungeprüft. **Business-Aussage „kein Vorteil gegenüber Vergabeweiser“:** auf Losebene und bei der Definition nicht mehr haltbar; ein Merkmalsvorteil (Los, Grundlaufzeit statt Höchstende) liegt vor, ein Qualitätsvorteil beim Lesen ist nicht belegt. „Liste als Produkt nicht tragfähig“ bleibt unwiderlegt (Zahlungsbereitschaft offen, Abdeckung etwa 80 % gegen 100 %).

## Gesamturteil
Weiter (Projektabschluss), eingeschränkt formuliert. Vorschlag des Evaluators für die Entscheidung: W1 (Iteration 10) formal erfüllt, als Qualitätsvorteil eingeschränkt; W8a formal verfehlt wegen eines Fehlers der Vorab-Schwelle (+15 von höchstens 15), W8b erfüllt; nach der Vorab-Regel „kein belegter Vorteil im definierten Maß“, die Aussage „kein Vorteil“ nicht als Gleichheit lesen; Befund: Merkmalsunterschied, kein belegter Qualitätsvorteil, Nachfrage offen. Neu gefundene Listenfehler und der Zuordnungsfehler kommen als offene Grenzen ins Lab-Log. Was fehlt: ein vorab festgelegtes Maß, das Definition und Granularität trennt; menschliche Gegenlesung der 15 Lose und eine zufällige größere Prüfung der übereinstimmenden Lose; Klärung, ob Vergabeweiser Ausschreibungs- oder Zuschlagsstand zeigt (M3, M22, M49); Prüfung der Zuordnung bei allen 160 Losen; Häufigkeit der Listenfehler vom Typ M59 und 12853-2024/Los 3; Vergleich bei Losen ohne Listenende.
