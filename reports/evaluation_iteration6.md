# Evaluation Iteration 6 (Subagent `evaluator`, 2026-11-04)

_Bericht des Evaluators, ungekürzt übernommen (Abschnitte 1 bis 6). Abschnitt 7 stammt von Claude (Nachprüfung) und vom Nutzer (Antworten)._

Grundlage des Evaluators: nur gelesene Dateien, die Git-Reflog-Datei `.git/logs/HEAD` und 7 Stichproben auf ted.europa.eu (392720-2026, 430737-2026, 750900-2025, 832634-2025, 520078-2026, 402160-2026, 143100-2026). Git-Befehle konnte er nicht ausführen; Diffs von Commits sind deshalb von ihm nicht geprüft (siehe Abschnitt 7).

## 1. Urteil je Kriterium

| Kriterium | Urteil | Beleg |
|---|---|---|
| Y1 Ende der Grundlaufzeit (GL) ≥ 90 % | **formal erfüllt (54/60 = 90,0 %), aber nicht belastbar** | `reports/liste_auswertung_iteration6.md` Z. 7. Nachgerechnet 54/60. Gründe gegen die Belastbarkeit: Verankerung (59/60), unbelegte Unabhängigkeit und ein versteckter Fehler bei L60. Mit L60: 53/60 = 88,3 % (Wilson 77,8–94,2). |
| Y2 Höchstende ≥ 90 % | **erfüllt** (55/60 = 91,7 %, eher unterschätzt) | Auswertung Z. 8. L56 ist laut Stichprobe des Evaluators wohl ein Fehler des Prüfers, nicht der Liste (dann 56/60 = 93,3 %). 9/60 Einträge stehen auf „unbestimmbar“ und zählen automatisch als korrekt. |
| Y3 Abdeckung ≥ 80 % | **verfehlt (knapp)**, Folge vorab festgelegt: kein Abbruch | `reports/vertragsliste_iteration5.md` Z. 13: 2924/3668 = 79,7 % (nachgerechnet 79,72 %), dieselbe Zahl wie X4 aus Iteration 5; in Iteration 6 kam nichts Neues hinzu. |
| Y4 Prototyp | **erfüllt** (Ja/Nein-Kriterium, niedrige Hürde), mit inhaltlichen Mängeln | `reports/beispiel_liste.md`: jeder Eintrag mit TED-Link, Herkunft und Stufe; 146 Lose, Status und Stufen summieren sich zu 146. |

## 2. Schwächen nach Schwere

**Kritisch**

- **Verankerung macht Y1 fast zu einer Abschreibe-Prüfung.** Laut Schlüssel stammt die GL der Liste in 59 von 60 Fällen aus `gl_herkunft = enddatum`, nur L54 aus `text_zunaechst`. Die Vorlage zeigt in der Zeile „Felder: … Ende …“ genau dieses Datum. Der Prüfer sah bei 59/60 die Antwort der Liste. Y1 misst damit nur, wie oft dem Prüfer ein Widerspruch im Text auffiel; es ist eine Untergrenze der Fehlerzahl, keine Genauigkeit.
- **Versteckter Fehler L60 (392720-2026, Los 1).** Laut Original Laufzeit 01.07.2026–30.06.2030, dazu: „Die Vertragsdauer beträgt zwei Jahre mit einer zusätzlichen Option einer Verlängerung von zweimal ein Jahr. (2+1+1)“. Richtig: GL 30.06.2028, Höchstende 30.06.2030. Liste und Prüfer nennen GL 30.06.2030, der Prüfer als Höchstende 30.06.2032 (1 Minute Prüfzeit). Derselbe Fehlertyp wie L1/L42, unentdeckt. Nach der vorab festgelegten Definition ein Fehler; Y1 läge unter der Schwelle, die vorab festgelegte Folge wäre „zurück zu Phase 3“.
- **Unabhängigkeit „ohne KI-Hilfe“ ist nicht belegt, gehört aber zur Hypothese.** Feld Hilfsmittel in 60/60 Einträgen leer. Teil B im selben PDF stimmt wörtlich mit der KI-unterstützten Zweitprüfung aus Iteration 5 überein, was auch Zweifel an Teil A begründet. Das PDF lag nicht im Repo, die Übertragung in die Urteils-CSV war nicht prüfbar.

**Mittel**

- **Zeitlinie widerspricht der Prüfzeit.** Vorlage mit Commit 3e01407 bei 13:07 MEZ, Auswertung mit Commit 67fc28b bei 15:15, dazwischen etwa 128 Minuten; allein Teil A soll 163 Minuten gedauert haben (Summe nachgerechnet: 163). Dazu kommen Teil B und die Übertragung.
- **Die Commit-Reihenfolge belegt die Vorab-Festlegung nur schwach.** ac1424e und 6baaab5 tragen denselben Zeitstempel; 3e01407 (Stichprobe, Seed, Hash) folgt 15 Sekunden später. Der Seed 20261105 wurde im selben Commit wie die Stichprobe festgehalten. Der Hash schützt nur den Schlüssel, der ohnehin aus der Liste reproduzierbar ist, nicht die Urteile. Ob Hypothese und Kriterium nach 6baaab5 geändert wurden, konnte er nicht prüfen.
- **Gewichtung durch höchstens 2 Lose je Zuschlag.** Große Bekanntmachungen sind untergewichtet, z. B. 143100-2026 (Autobahn GmbH, mindestens 56 Lose). Dort steht in allen geprüften Losen „Festlaufzeit von 01.01.2026-31.03.2030“, während BT-537 den 31.03.2031 nennt (= L1), systematisch über die ganze Bekanntmachung. Nach Losen gewichtet kann die Fehlerquote über 10 % liegen.
- **Der Prototyp enthält bekannte Fehler.** In der Oberpfalz stehen bei 143100-2026 die Lose 8, 9 und 14 mit GL 31.03.2031 und Höchstende 31.03.2032; laut Original GL 31.03.2030, Höchstende 31.03.2031. Mindestens 3 der 6 B-Einträge sind falsch, obwohl der Fehler seit L1 bekannt war. Stufe B warnt nur.
- **Die Stufenquoten sind teils zirkulär oder überschätzt.** In Stufe D ist „Höchstende korrekt 9/9“ per Definition garantiert (`auswertung_iteration6.py` Z. 66–67); D „GL 9/9“ enthält L60, korrekt wäre 8/9. Die Stufen wurden nachträglich gebildet und sind auch so gekennzeichnet; die Quoten sind trotzdem nicht prüfend.
- **Die Aussage „kein Eintrag der Oberpfalz geprüft“ ist falsch.** L6 = 617709-2026 Los 3 steht in der Oberpfalz-Liste (DE232). Betroffen: `docs/iterationen.md` und `beispiel_liste.md`.

**Gering**

- Der Median der Prüfzeit ist 2,5 statt 3 Minuten (das Skript nimmt den oberen Median). Verteilung: 18× 1, 12× 2, 11× 3, 7× 4, 12× 5.
- „Es fehlen 12 Lose (2.936)“ (`iterationen.md`): Für 80 % reichen 2.935 Lose, es fehlen 11.
- Die Interpretation zu L43 trifft nicht zu: Das Feld 14.08.2028 ist weder GL (Text: 14.07.2028) noch Höchstende (Sommerferien 2030).
- Die Interpretation zu L56 („Verlängerung steht nur im Originaltext“) ist durch seine Stichprobe nicht gedeckt: Laut Abruf kommen in 832634-2025 weder „2030“ noch „verlänger…“ vor, alle 13 Lose enden am 31.12.2028. Vorbehalt: Abruf über eine Zusammenfassung.
- Die Region wird bei XML-Losen ersatzweise über die Reihenfolge zugeordnet (`beispiel_liste.py`); diese Zuordnung ist ungeprüft (16 CSV-Zeilen mit `xml`).
- Der Prototyp lässt sich nur mit dem lokalen Schlüssel neu erzeugen: `bewertung()` prüft dessen Hash per `assert`.

## 3. Alternative Erklärungen

- **Hohe Y1-Quote durch Abschreiben statt Prüfen:** Bei etwa 14 Losen ohne jeden Laufzeittext in den Auszügen (z. B. L5, L10, L25, L33, L37, L41, L44, L57) gibt es nur eine mögliche Quelle, das angezeigte Feld. Die „Korrektheit“ ist dort tautologisch. Ob BT-537 GL oder Höchstende ist, lässt sich nicht feststellen (vgl. L1, L42, L60).
- **Die „unbekannt“-Fälle sind eher uneinheitliches Prüferverhalten als Listenfehler.** L48 (430737-2026) enthält laut Original keinerlei Optionsangabe, so wie 12 andere Lose, bei denen der Prüfer das Feld übernahm. Umgekehrt ist L8 („Rahmenvereinbarung über maximal 48 Monate“) mit gutem Grund als Höchstende lesbar, und die Liste dort möglicherweise wirklich falsch. Die Lesart 95 % ist nicht neutral.
- **Y2 hoch durch die Kategorie „unbestimmbar“:** Bei 8 der 9 als unbestimmbar markierten Lose gab der Prüfer ein Datum an (L2, L3, L21, L22, L31, L38, L59, L60). Die Liste ist dort vorsichtig, aber nicht informativ. Bezogen nur auf die 51 Lose, bei denen die Liste ein Höchstende behauptet: 46/51 = 90,2 %.
- **Exploratives Fenster:** „GL − 12 bis Höchstende + 12“ umfasst oft vier Jahre und mehr; 32/52 sagt ohne Referenz wenig. Die Regel für unbestimmbare Höchstenden (GL + 12) war nicht vorab festgelegt. Umgekehrt: 20/52 liegen sogar außerhalb dieses breiten Fensters.

## 4. Fakten und Interpretation

- `beispiel_liste.md`, „Fakten“: 90,0 % und 91,7 % standen dort als Genauigkeit; der Vorbehalt (Hilfsmittel leer) stand erst unter „Interpretation“ und gehört an die Zahl.
- „Fehler … traten nur in Stufe B auf“ gilt nur für die Fehler, die der Prüfer fand (L60 ist Stufe D).
- `liste_auswertung_iteration6.md`, „Interpretation“: L56 als „echter Fehler der Liste“ und L43 als „Enddatum ist Höchstende“ sind Deutungen, die die Stichprobe nicht stützt.
- Die explorativen Zahlen (1.368/9.915, 3.024, 32/52) waren nicht prüfbar, weil das Scratch-Skript nicht im Repo lag. Sie durften nicht als Fakten in den Abschluss.

## 5. Betroffene Annahmen

- **A4, A13:** Status unverändert. Y3 bringt keine neue Messung (gleiche 79,7 %). Neu ist der Hinweis, dass BT-537 bei manchen Auftraggebern schon das Höchstende ist (L1, L42, L60, 143100-2026 systematisch); ein „bestimmbares Ende“ ist also nicht immer das Ende der GL.
- **A11:** unverändert und **nicht geprüft**; die Stichprobe enthält 0 Lose vor eForms, obwohl die Kriterientabelle A11 unter Y1 führt.
- **A12:** unverändert, Hinweis ergänzen: L58 (851303-2025, Mietkleidung) in der Stichprobe, in der Oberpfalz 556275-2026 (Kesselreinigung Müllkraftwerk), beide trotz Haupt-CPV 909xx.
- **A17:** unverändert; die Prüfzeit betrifft eine andere Aufgabe (Enddaten lesen statt Paare beurteilen) und ist durch die Zeitlinie fraglich.
- **A18:** unverändert ungeprüft; Teil B nicht unabhängig.
- **A1, A15:** unverändert, außerhalb des Projektumfangs.

## 6. Was für ein belastbares Urteil fehlte, und Empfehlung

Fehlte: Angabe des Nutzers zu den Hilfsmitteln und das abgegebene PDF im Repo; Nachprüfung der 60 Lose mit einer Vorlage ohne die Zeile „Felder: Ende“ (oder wenigstens der etwa 44 Lose mit Verlängerungstext); Klärung der Zeitlinie und `git diff 6baaab5 HEAD -- docs/iterationen.md`; die explorativen Berechnungen als Skript im Repo; eine nach Losen gewichtete Abschätzung des Fehlertyps aus L1.

**Empfehlung des Evaluators:** Formal deckt die Vorab-Regel „weiter“, inhaltlich ist „Hypothese bestätigt“ nicht gedeckt. Y1 liegt genau auf der Schwelle, ist durch die Verankerung kaum aussagekräftig, und die Prüfung „ohne KI-Hilfe“ ist nicht belegt. Mit L60 läge Y1 unter 90 %, die vorab festgelegte Folge wäre „zurück zu Phase 3“. Im Abschluss sollte Y1 als „an der Schwelle, nicht belastbar“ stehen, nicht als erfüllt. Offen zu benennen: Unabhängigkeit, Verankerung, L60/L56, die bekannten Fehler im Prototyp (143100-2026 Lose 8, 9, 14), Y3 79,7 % und ungeprüfte Annahmen (A11, A17, A18, A1, A15). Die Entscheidung trifft der Nutzer.

## 7. Nachprüfung durch Claude und Antworten des Nutzers (2026-11-04)

Von Claude nachgeprüft:
- **Hypothese und Kriterien unverändert** seit 6baaab5 (`git diff 6baaab5 HEAD -- docs/iterationen.md` enthält nur Fortschrittseinträge, keine Änderung an Hypothese, Begriffen oder Kriterien).
- **L60** bestätigt: Schon der Auszug in der Vorlage enthält „(2+1+1)“, GL 30.06.2030 in Liste und Prüfer-Eintrag; richtig wäre 30.06.2028 (Beginn 01.07.2026, zwei Jahre).
- **L6** (617709-2026, Los 3) steht in der Oberpfalz-Liste (Quelle API, DE232): Die Aussage „kein Eintrag der Oberpfalz geprüft“ war falsch.
- **Zeitlinie** bestätigt (3e01407 um 13:07:28, 67fc28b um 15:15:14, Zeitzone +01:00).
- **Übertragung PDF → CSV:** Alle 60 Einträge (Grundlaufzeit, Höchstende, Minuten) der Datei `liste_pruefung_iteration6_urteile.csv` stimmen mit dem PDF überein; keine Übertragungsfehler. Das PDF liegt jetzt als `reports/liste_pruefung_iteration6_abgabe.pdf` im Repo (SHA-256 `D55BF513EAD082CFC1F40559413E9253FAD31D3A40D9506444E5BDD428EEFBD7`).
- Nicht selbst nachgeprüft (nur Aussage des Evaluators): L56, 143100-2026 Lose 8, 9, 14, die Stichproben auf ted.europa.eu, die Aufteilung der 9 „unbestimmbar“-Einträge.

Angaben des Nutzers (2026-11-04, auf Rückfrage):
1. Entscheidung: zurück zu Phase 3.
2. Teil A (60 Lose) wurde **ohne KI-Hilfe** geprüft (mündliche Angabe; im Feld „Hilfsmittel“ nicht vermerkt).
3. Teil B: Die Einträge wurden aus der Zweitprüfung Iteration 5 übernommen, weil die 10 Paare dieselben waren. **Ursache war ein Fehler im Aufbau (Schritt 2):** Die 10 Paare wurden aus den 57 Paaren der Zweitprüfung gezogen, die der Prüfer schon kannte. Teil B konnte nie ein unabhängiger Test von A18 sein.
4. Prüfzeit, auf die Frage, ob schon vor dem Commit um 13:07 an der Vorlage gearbeitet wurde: „Habe davor schon gearbeitet, aber nicht durchgängig.“ Der Commit-Zeitpunkt begrenzt den Beginn der Prüfung also nicht, und der Widerspruch zu den 163 Minuten ist damit erklärt. Die Angabe der Minuten je Los bleibt eine Selbstangabe.
5. Das PDF darf ins Repo (erledigt).
