# Evaluation Iteration 10 (Gesamtprüfung durch den Subagenten `evaluator`, 2026-11-05)

_Gekürzte Wiedergabe des Berichts des Evaluators (Lesezugriff, kein Code, keine API-Abrufe; Rechnungen von Hand aus den vorhandenen Dateien). Urteile stammen vom Evaluator; Einordnungen des Projekts stehen in `docs/iterationen.md` (Ergebnis Iteration 10)._

## Urteil je Kriterium
| Kriterium | Urteil | Beleg |
|---|---|---|
| W1 Vorsprung ≥ 5 bei ≥ 40 gemeinsamen Losen | formal **erfüllt**, als „Qualitätsvorteil“ nur eingeschränkt belastbar | 66/70 gegen 58/70, +8; Auswertung entspricht der vorab festgelegten Regel |
| W2 Abdeckung | gemessen, wenig aussagekräftig | 70/70; gleiche Quelle (Bekanntmachungsservice), erwartbar |
| W3 Fehltreffer mit verschiedenen Losenden | Zählung stimmt | 4 von 12 (N25, N40, N69, N98), am TED-XML bestätigt |
| W4 Abdeckung unterhalb der EU-Schwelle | **nicht aussagekräftig** | API liefert nur die 50 frühesten Verträge; 0 von 100 nicht EU-weit |
| W6 Verfahren | überwiegend ja, Abweichungen offen zu nennen | Weg 2 nach dem Trockenlauf ergänzt; Abruf-Skript nach erstem Lauf angepasst; W7 nach Beginn des Abrufs aufgenommen (ohne Schwelle, Ziehung vor dem Nachsehen) |
| W7 Nebentest AusschreibungsRadar | als Hinweis korrekt | 2 von 15 bestätigt; 56 Seitenabrufe |

## Einordnung der 8 Fälle (Vorsprung der Liste)
- **Verfahrens- statt Losebene: 4** (N25, N40, N69, N98): Vergabeweiser zeigt das Ende des ersten Loses des Verfahrens; unsere Liste und der Vergleichswert gelten je Los.
- **Höchstende statt Grundlaufzeit: 2** (N9, N11): `EndDate` ist dort das Höchstende (Text: „endet spätestens 31.08.2032“), obwohl die Beschriftung „ohne Verlängerungen“ lautet.
- **Echte Leselücke: 1** (N23: bei Vergabeweiser kein Wert, Dauer steht im XML).
- **Toleranz/Quelle: 1** (N70: 2 Tage Abweichung).
- Reine Lesefehler von Vergabeweiser: 1, höchstens 2 von 8.

## Dritte Messlatte (Basisregel „Feld EndDate“)
Liste 66/70 (94,3 %), Basisregel 63/70 (90,0 %), Vergabeweiser 58/70 (82,9 %, Wilson etwa 72,4–89,9). Liste gegen Basisregel +3 (N9, N11, N23; exakt p = 0,25); Basisregel gegen Vergabeweiser +5 (p = 0,0625). Vergabeweiser verhält sich wie die Basisregel plus Verfahrensebene.

## Unsicherheit der Differenz +8
Exakter McNemar-Test 8 zu 0 diskordante Paare: p zweiseitig = 0,0078. Wald-Näherung: etwa +4 % bis +19 % (rund +3 bis +13 Lose); die untere Grenze liegt unter der Schwelle 5. Sensitivität: ohne N70 +7; ohne N9 und N11 +6 auf 68 Losen; ohne die drei BImA-Lose (N25, N40, N69) +5; gilt Vergabeweisers Verfahrensdatum als richtig, wenn es dem Ende irgendeines Loses entspricht, liegt der Vorsprung bei +4 (kein gesicherter Vorteil).

## Zulässig und nicht zulässig
- **Zulässig:** „Auf 70 Zufallslosen der eigenen TED-Liste stimmt unser Ende der Grundlaufzeit bei 66/70 mit dem Vergleichswert zweier KI-Leser überein, das Verfahrensdatum aus der API von Vergabeweiser bei 58/70. Alle 8 abweichenden Fälle gehen zugunsten der Liste; die vorab festgelegte Schwelle (≥ 5) ist erreicht. Ursachen: Losebene (4), Höchstende statt Grundlaufzeit (2), fehlender Wert (1), 2 Tage (1).“
- **Nicht zulässig:** „Die Liste ist genauer als Vergabeweiser“; „Vergabeweiser liest schlechter“; Aussagen über die Unterschwelle oder andere Anbieter; Aussagen zu Nachfrage oder Marktvorteil; Aussagen zum Höchstende.

## Schwächen nach Gewicht
**Kritisch:** (1) Maßstab und Befund fallen zusammen: 6 von 8 Fällen sind Granularitäts- oder Begriffsunterschiede. (2) Vergleichswert aus derselben Modellfamilie wie die Regeln (vorab benannt).
**Mittel:** Häufung bei BImA (3 von 8); eine Stichprobe, eine Messung, nur TED-Lose oberhalb der Schwelle; W4 nicht aussagekräftig; Setzungen im Vergleichswert (N32, N39).
**Gering:** W7 nur 2 Lose; Schwelle 5 ohne Unsicherheitsbezug; N70 knapp außerhalb der Toleranz.

## Alternative Erklärungen
Gleiche Rohquelle mit unterschiedlicher Verarbeitung; Vergabeweisers Höchstende kann für die Planung sinnvoller sein, wenn Verlängerung „fast immer“ erfolgt (Gespräch 3); Auftraggeber-Cluster; Quellenunterschied bei N70.

## Betroffene Annahmen
A2 bleibt widerlegt (Existenz); A3 und A15 bleiben ungeprüft; A4 nur Hinweis. Die Aussage „Liste als eigenes Produkt nicht tragfähig“ (business.md §8.4 bis §8.6) bleibt bestehen; „Vergabeweiser ist mindestens gleich gut“ wäre nach W1 nicht mehr haltbar.

## Gesamturteil
Weiter, Projektabschluss, eingeschränkt formuliert. Kein Beleg für einen Marktvorteil. Was für ein belastbares Urteil fehlt: größere Stichprobe (mindestens 150 Lose, mehrere Auftraggeber) mit getrennter Ausweisung von Los- und Verfahrensebene, ein von Menschen bestätigter Vergleichswert, Klärung von N70 und des Mehrlos-Verhaltens von `/expiring`, für W4 eine Zufallsziehung statt der 50 frühesten.
