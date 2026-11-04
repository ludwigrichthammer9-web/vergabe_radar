# Evaluation Iteration 5 (Subagent `evaluator`, 2026-11-04)

_Gekürzte, sinngemäße Wiedergabe des Berichts des Evaluators (nur Lesezugriff). Eigene Nachrechnungen des Evaluators sind als solche gekennzeichnet.
Die Entscheidung trifft der Nutzer._

## Kernaussage
X3 ist klar verfehlt und das Ergebnis robust. Zwei Befunde wiegen schwerer als die Ampel: (1) Die Zweitprüfung (X1/X2) bestätigt die Ground
Truth wahrscheinlich nicht unabhängig, nicht nur beim Kommilitonen. (2) Die Folge „Idee anpassen“ trägt formal, belegt aber nicht, dass eine
Vertragsliste ohne Terminprognose Nutzen hat.

## Urteil je Kriterium
| Kriterium | Urteil | Beleg |
|---|---|---|
| Vorab-Festlegung | erfüllt, mit Vorbehalt | Prognoseziel „Höchstende“ nach Kenntnis der Vorlaufzeiten derselben Paare gewählt; begünstigt R1, stärkt also das negative Ergebnis |
| X1 ≥ 30 | nur formal erfüllt | 52 Paare; hängt an der Unabhängigkeit der Prüfung (A18); 41 von 52 Vorgängern vor eForms |
| X2 ≥ 85 % | nur formal erfüllt, kaum aussagekräftig | 61/67 = 91,0 %. **Wer alle 57 echten Paare bestätigt und die 10 Köder ablehnt, kommt auf 57/67 = 85,1 %** (Nachrechnung des Evaluators); die Schwelle trennt nicht von blindem Bestätigen |
| X3 | **nicht erfüllt** | R1 15/52 = 28,8 % (Wilson 18,3–42,3), R0 9/52 = 17,3 %, Abstand +11,5 Prozentpunkte; nachgerechnet |
| X4 ≥ 80 % | nicht erfüllt (knapp) | 2.924/3.668 = 79,7 % (Wilson 78,4–81,0); Schwelle nicht nachjustiert |
| Fachliches Kriterium | nicht erfüllt, nur formal | gleiche Schwelle wie X3, belegt keinen Nutzen (A1/A15 ungeprüft) |

## Schwächen
**Kritisch**
1. **Unabhängigkeit der Zweitprüfung (A18) wahrscheinlich nicht gegeben, auch für P1–P13.** Begründungen und Detailtiefe (z. B. P13 mit
   57 vs. 55 Objekten und Prozentwerten bei „2 Minuten“, einheitliches „Beide: …“) ähneln den Texten der Handsuche. Beim Kommilitonen
   (84 % der Wertung) fehlen die Minuten. Ob und wie KI genutzt wurde, ist nicht prüfbar. Fehlt: Angabe der Nutzung beider Prüfer und eine
   kleine Stichprobe (5–10 Paare), garantiert ohne Hilfsmittel. Bis dahin ist X1 = 52 „konsistent mit dem Rechercheur“, nicht „menschlich bestätigt“.
2. **Der Backtest misst Objektidentität, nicht „direkter Vorgänger“.** Paare mit Veröffentlichung 37 bis 95 Monate nach der Prognose
   (T56, T37, U54, T38, U19, T33, T24, T8, T23, T34) deuten auf Zwischenverträge außerhalb TED, stillschweigende Verlängerung oder einen
   falschen „jüngsten Vorgänger“. Wie viel des Ergebnisses daher kommt, ist offen.

**Mittel**
3. Selektion durch Rückwärtssuche (nur Fälle mit auffindbarem Vorgänger; Rechtszensierung; zwei kurze Fenster Q1 und Q3 2026).
4. Lese-Regeln nicht für den Einsatzbereich getestet: Test an eForms-Losen (Urteile von Claude allein), im Backtest 41/52 Vorgänger vor eForms;
   „keine_verlaengerung“ (10 von 52 Paaren) ungeprüft, „unbestimmbar“ (13 von 52) im Test mit 6/10 Fehlern.
5. Nur Paare mit bestimmbarer Grundlaufzeit (61 von 68); für die rund 20 % Lose ohne Laufzeit ist die Aussage nicht prüfbar.
6. Köder schwach: zehn Fälle, selbst von der Handsuche als „unklar“ eingestuft, gleiche Quelle wie die Paare; Wilson 59,6–98,2 %.
7. Kalibrierungsbeispiele: P11, P12, P60, P62 ausgeschlossen, P27, P51, P64 gezählt (offen ausgewiesen, Einfluss gering). Prüferwechsel nach
   Beginn (ab P14): X2 ist kein Vergleich Nutzer–Rechercheur mehr, wie in X1 definiert.

**Gering**
8. Mehrfachlose: nur 4 von 68 Paaren mit unterschiedlichen Enden (T5, U35, U65, U70); Einfluss klein.
9. Der Median +0,6 Monate täuscht (zweigipflig: 20 früher, 17 später).
10. Fehlerrichtung im Report nicht ausgewiesen (38,5 % früher, 32,7 % später, 28,8 % im Fenster).

## Robustheit des negativen Ergebnisses (Nachrechnungen des Evaluators, aus der Tabelle)
- Ohne die 13 Paare „unbestimmbar“: 14/39 = 35,9 %.
- Ohne die 16 Paare mit Abweichung über 24 Monate: 15/36 = 41,7 %.
- Kein Vorlauf-Parameter rettet X3: Die Abweichungen streuen so breit, dass ein ±3-Fenster höchstens etwa 15–16 Paare fängt (Handsicht).
- Auch ohne Unsicherheit beim Höchstende („keine_verlaengerung“, n = 10) trifft R1 nur 3/10.
- Ein nachträglich definierter Korridor „GL − 9 bis Höchstende − 3 Monate“ käme auf etwa 26/52 = 50 % (explorativ, nicht als Kriterium verwenden).

## Alternative Erklärungen
- Option nicht gezogen oder Neuvergabe zwischen Grundlaufzeit und Höchstende (viele der 20 „zu frühen“ Fälle liegen zwischen R0 und R1);
  die Ausübung ist aus dem Vorgänger-Zuschlag nicht lesbar.
- Verlängerung, Notverlängerung oder Zwischenvertrag (17 „zu späte“ Fälle, besonders die mit über 37 Monaten).
- Falscher oder nicht direkter Vorgänger laut Handsuche.
- Laufzeitfelder: BT-537/DATE_END als Grundlaufzeit ist eine Mustererkennung, keine Definition.
- Heterogene Auftraggeber: Es fehlt eine Auswertung nach Auftraggeber (mehrere Paare derselben Häuser, z. B. IKK classic).

## Stellen, an denen Fakt und Interpretation vermischt sind
- Auswertung Zweitprüfung: „eher eine Untergrenze der echten Paare“ folgt aus n = 6 und ist nur eine Vermutung; „‚Alles bestätigen‘ ist
  ausgeschlossen“ stimmt rechnerisch nicht (85,1 %), nur über die 9/10 Köder.
- „53/60, gewichtet etwa 91 %“ steht als Fakt, stammt aber von Claude allein, gilt nur für eForms, „keine_verlaengerung“ nicht geprüft.
- „Verlängerung belegt“ heißt „im Text genannt“, nicht „gezogen“.
- „Vertragsliste ohne Terminprognose“ ist die vorab festgelegte Folge, ihr Nutzen ist nicht belegt.

## Statusvorschläge für Annahmen
- **A8:** „widerlegt für die geprüfte Operationalisierung“ (Höchstende − 6, ±3 Monate, 52 Paare); „im Mittel +0,6“ nicht als Stützung eintragen.
- **A10:** „widerlegt (Variante nur eForms-Vorgänger)“: 11 von 52 Backtest-Vorgängern sind eForms; Daten vor eForms waren nötig.
- **A11:** „vorläufig gestützt“ beibehalten, nur für die Bestimmbarkeit der Grundlaufzeit (61/68); Höchstende vor eForms ungeprüft.
- **A16:** bleibt „ungeprüft“, Warnsignal verstärkt (15 im Fenster, 20 früher, 17 später); nicht definitionsgleich mit früheren Zahlen.
- **A18:** bleibt „ungeprüft“; auch P1–P13 zeigen das Muster; X2 ohne Köderaussage schwach (85,1 %).
- **A3b:** unberührt; lange Lücken sind ein indirektes Indiz für nicht-direkte Vorgänger.
- **A4/A13:** X4 auf Los-Ebene 79,7 % als eigener Hinweis eintragen, keine Statusänderung.
- **A14:** „widerlegt (Variante R0/R1, Backtest Iteration 5)“ oder mindestens „ungeprüft, starkes Warnsignal“.

## Was für ein belastbares Urteil fehlt
- Angabe zur Hilfsmittel- und KI-Nutzung beider Prüfer und eine kleine, wirklich unabhängige Handprüfung (z. B. 10 Paare).
- Auswertung nach Auftraggeber und Prüfung der Paare mit Lücken über 24 Monate (späterer Zwischenvertrag?).
- Test der Lese-Regeln an Vorgängern vor eForms, besonders „keine_verlaengerung“ und „unbestimmbar“, mit unabhängigem Urteil.
- Verlängerungsrealität (wie oft Optionen gezogen werden); Vorwärtsstichprobe zur Schätzung von Selektion und Präzision.

## Empfehlung
**Idee anpassen (Phase 1), mit Auflagen.** Die vorab festgelegte Folge ist ausgelöst und trägt als Abbruch der Punktprognose „Höchstende − 6 Monate“,
nicht als Beleg für den Nutzen einer Vertragsliste mit Enddaten. Vor der Entscheidung zu klären: die KI-Nutzung bei beiden Prüfern und die
Frage, ob die langen Lücken echte Neuausschreibungen oder falsche Vorgänger sind.
