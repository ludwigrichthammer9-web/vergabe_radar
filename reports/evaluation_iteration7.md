# Evaluation Iteration 7 (Subagent `evaluator`, 2026-11-04)

_Bericht des Evaluators, ungekürzt übernommen (ab „Evaluation Iteration 7“). Der Abschnitt „Nachprüfung durch Claude und Entscheidung“ am Ende stammt von Claude und vom Nutzer._

Ich habe alle Zahlen aus den CSV-Dateien und dem Schlüssel nachgerechnet. Zwei Stichproben habe ich bei TED nachgesehen: 650531-2026 Los 2 und 143100-2026 Los 8. Prüfen konnte ich nicht, ob die Commits vor dem Ziehen liegen, außer über `.git/logs/HEAD` (Zeitstempel).

### Urteil je Kriterium

| Kriterium | Urteil | Beleg (Quelle) |
|---|---|---|
| Hypothese/Kriterien vorab festgelegt | erfüllt | Commit "Hypothese und Kriterien festgelegt (vor Regeländerung)", `.git/logs/HEAD` Z. 71. Regel 1b (Z. 72) und Seed (Z. 73) liegen vor dem Ziehen (Z. 74). |
| Y1 ≥ 90 % (Ende der Grundlaufzeit) | **nicht erfüllt** (formal 36/47 = 76,6 %). Inhaltlich zu großen Teilen **nicht prüfbar**. | `reports/liste_auswertung_iteration7.md`, Nachrechnung unten |
| Y1r ≥ 12/15 | **nicht erfüllt** (8/15 = 53,3 %), als Test der Regel **kaum aussagekräftig** | gleiche Datei, Schlüssel, beide Abgaben |
| Y2 ≥ 90 % | nicht erfüllt (29/47 = 61,7 %). Der Wert 29/32 = 90,6 % ist selektiv. | gleiche Datei |
| Y2b ≥ 85 % | nicht erfüllt (24/42 = 57,1 %). Der Wert 24/27 = 88,9 % ist selektiv. | gleiche Datei |
| Y3 Verfahren | **teilweise / nicht erfüllt** (Hilfsmittel der Nachprüfung fehlen) | siehe (c) |
| Y4 Prototyp | **teilweise erfüllt** | siehe (d) |

### (a) Rechnerische Prüfung

**Y1 stimmt: 36/47.** Es gibt 47 Lose des Typs Y in L1 bis L50 (L3, L7, L49 sind Typ R).
- Die 11 Abweichungen sind L16, L18, L24, L25, L26, L27, L30, L31, L32, L38 und L44.
- Davon sind 6 „unbekannt“ (L24, L25, L27, L31, L38, L44) und 5 Datumsabweichungen (L16, L18, L26, L30, L32). Das entspricht dem Report.

**Y1r stimmt: 8/15.**
- Die 7 Abweichungen sind L3, L7, L49, L57, L62, L65, L88.
- Richtig sind L55, L73, L74, L75, L77, L80, L84 und L87, alle aus Prüfer-Einträgen mit Quelle „Text“ und Hilfsmittel „Kalender“.

**Y2 und Y2b stimmen.**
- Y2 hat 18 Abweichungen, davon 15 „veraltet“ (Nachprüfung mit Eintrag, Höchstende nicht neu eingetragen) und 3 ohne Nachprüfung (L27, L31, L38).
- Y2b hat 42 als Nenner, weil 5 Lose in der Liste „unbestimmbar“ sind (L4, L19, L22, L40, L48).
- Diese 5 zählen bei Y2 automatisch als „korrekt“ (`auswertung_iteration7.py`, `if hh == "unbestimmbar": ok2 = True`). Das bläht Y2 gegenüber Y2b leicht auf.

**Die Kürzung auf L1 bis L50 ist statistisch vertretbar.**
- Die Nummern entstehen per `random.Random(seed).shuffle` (`stichprobe_iteration7.py`), L1 bis L50 sind also eine Zufallsteilmenge.
- Die Wilson-Obergrenze 86,4 % liegt unter 90 %. Allein aus der Stichprobengröße lässt sich das Verfehlen also nicht wegerklären.
- Zwei Vorbehalte:
  - Der Abbruch richtete sich nach dem Aufwand des Prüfers. Er war zum Zeitpunkt der Festlegung (Commit 0cca980) bereits bis L50 fertig. Das ist nicht prüfbar, aber plausibel unabhängig vom Ergebnis.
  - Der Plan sah 80 Lose vor, Y1 ist also kein „72/80“-Test mehr.
- Die Cluster sind nicht berücksichtigt. Die Lose stammen aus höchstens 2 je Zuschlag, aber 787336-2025 (L18, L38) und 291266-2026 erscheinen mehrfach. Die Wilson-Intervalle nehmen unabhängige Lose an.

### (b) Belastbarkeit von Y1

**Kritisch 1: Y1 misst für die meisten Lose nicht, was die Hypothese behauptet.**
- Die Hypothese betrifft die Frage, ob das Enddatum ein Höchstende ist, obwohl der Text eine kürzere feste Laufzeit nennt.
- Die Nachprüfungsvorlage zeigt nur Link und Titel (`liste_nachpruefung_iteration7.md`, Z. 5 bis 12). Der Prüfer sollte Beginn, Ende und Dauer aus den Feldern abschreiben.
- In `liste_nachpruefung_iteration7_urteile.csv` ist „Ende der Grundlaufzeit“ (`gl_nach`) fast überall identisch mit `ende_feld`. Die Ausnahmen sind L18 (Tippfehler), L24 und L44 (unbekannt) sowie L48 (Jahr korrigiert).
- Die Liste verwendet für 45 von 47 Losen selbst das Feld BT-537 (Herkunft „enddatum“). Dann vergleicht Y1 dieselbe Rohquelle mit ihrer Abschrift.
- Wenn im Text ein früheres Ende steht, das der Prüfer nicht liest, bleibt der Fehler, den Regel 1b finden soll, unsichtbar.
- Echte Inhaltsprüfung gibt es nur bei den 12 Losen mit Quelle „Text“ (L1, L2, L6, L8, L9, L15, L19, L28, L29, L36, L39, L47): 12/12. Das ist gut belegt, aber das ist eine ausgewählte Teilmenge. Der Prüfer las dort den Text so gründlich, dass er ein Datum daraus entnahm.
- Die 76,6 % sind deshalb weder eine Unter- noch eine Obergrenze der wahren Genauigkeit.
- In Iteration 6 wurden mit Textlesen etwa 10 % Fehler gefunden. Dass diese Fehlerart hier bei den roughly 35 nur aus Feldern abgeschriebenen Losen ebenfalls auftritt, ist nicht ausgeschlossen.

**Kritisch 2: Die Abweichungen sind überwiegend Mess- und Lesefehler, keine belegten Listenfehler.**
- 6 „unbekannt“:
  - 4 leere Nachprüfungen (L25, L27, L31, L38).
  - L24 und L44, bei denen der Prüfer „unbekannt“ eintrug, obwohl er Beginn und Dauer (L24) bzw. Ende (L44) abgeschrieben hat. In der Auswertung zählen beide gegen die Liste.
- 5 Datumsabweichungen:
  - L26 bestätigte ich bei TED: Los 2 hat Beginn 01/10/2026 und Ende 30/09/2029. Das entspricht der Liste, der Prüfer schrieb 01.01.2026 und 31.12.2029 ab.
  - L16, L30, L32 sind nicht unabhängig geprüft. Der Abschreibe-Check (`abschreibecheck_iteration7.md`) vergleicht nur mit denselben Rohdaten, aus denen die Liste stammt. Dass „Liste = Rohdaten“ richtig ist, wurde nur bei L26 an TED bestätigt.
  - L18 ist ein Tippfehler (31.10. statt 31.12.2029).
- Die 11 Abweichungen führen nicht zu der Aussage „Liste falsch“. Bei keiner einzigen ist ein Listenfehler belegt.
- Rechenbeispiel, ausdrücklich nur illustrativ und kein Ersatz für eine Nachprüfung durch den Prüfer: Zählt man L16, L18, L26, L30, L32, L24 und L44 als Prüferfehler, wären es 43/47 = 91,5 %. Ob das stimmt, könnte nur der Prüfer klären.

**Y1 liegt also zwischen 36/47 und 47/47, je nach Auflösung der Prüferfehler.** Das ist rechtlich nach den Vorab-Regeln ein Fehlschlag, inhaltlich aber nicht aussagekräftig.

**Ersetzungsregel und Hinweise an den Prüfer verfälschen das Ergebnis.**
- Nach den Regeln „Nachprüfung ersetzt die erste Abgabe“ und „Feld übernehmen, wenn der Text nicht widerspricht“ ist der Prüfer in der Nachprüfung systematisch beim Feldwert geblieben. Der Feldwert ist bei Typ R genau der Wert, den Regel 1b als falsch ansieht.
- Alle 7 Typ-R-Abweichungen stehen in Losen, die nachgeprüft wurden (L3, L7, L49, L57, L62, L65, L88). Alle 8 Treffer stehen in Losen, die nicht nachgeprüft wurden.
- Besonders deutlich: 267775-2025 (L74, L84) und 360180-2025 (L65, L88) haben dieselben Daten (Liste 29.06.2026, Höchstende 22.07.2029).
  - L74 und L84 wurden nicht nachgeprüft und zählen als korrekt.
  - L65 und L88 wurden nachgeprüft und zählen als falsch.
  - Dieselbe Sachlage führt je nach Verfahrensweg zu gegensätzlichen Urteilen.
- In der früheren Abgabe (`liste_pruefung_iteration7_urteile_abgabe1.csv`) standen bei L65 und L88 29.06.2026 mit Quelle „Text“. Hätte man die frühere Datei genommen, wäre Y1r 10/15. Die Korrektur auf die frühere Datei wäre aber ebenfalls nachträglich.
- Die Aussage in `docs/ki_irrwege.md`, die Nachprüfung habe „einen zuvor richtigen Texteintrag“ verschlechtert, gilt nur für die unfertige Abgabe 1. In der maßgeblichen zweiten Abgabe steht dort „unbekannt“.
- Die Regelwirkungs-Lose sind zudem nur 9 Zuschlagsnummern, nicht 15 unabhängige Fälle. Die Zahlen 8 und 7 sind nach Zuschlag geclustert.
- Der Prüfer wusste außerdem, dass L57, L62, L65, L88 Regelwirkungs-Lose sind (`iterationen.md`, Zeile 1059). Seine Blindheit war damit nicht mehr vollständig.

### (c) Y3 Verfahren

**Eingehalten (Faktenlage):**
- Regel, Seed und Skript wurden vor dem Ziehen committet (Commits 7d42a55, c7fb0c0 vor a87dc1f).
- Die Vorlage der ersten Prüfung zeigt keine Listenwerte (dokumentiert; nicht neu verifiziert).
- Der Schlüssel-Hash ist dokumentiert und im Skript eingebaut.
- Die Hilfsmittel der ersten Abgabe sind in allen 95 Zeilen eingetragen („keine“ 79, „Kalenderberechnung“ 16).

**Nicht eingehalten oder geschwächt:**
- **Hilfsmittel der Nachprüfung fehlen komplett:** In `liste_nachpruefung_iteration7.md` ist bei allen 38 Einträgen das Feld Hilfsmittel leer (Suche nach „- Hilfsmittel: \S“ ohne Treffer). Y3 verlangt „Hilfsmittel je Eintrag vermerkt“, das gilt also nicht für den Teil, der Y1 entscheidet. Die Auswertung bildet das nicht ab. Dort ist nur von „79 keine / 16 Kalenderberechnung“ die Rede, die aus der ersten Abgabe stammt.
- **Die Quelle der Nachprüfung wurde nicht vom Prüfer vergeben.** Im Markdown steht nur einmal „ted“ (L3). Alle übrigen sind leer, und `quelle_ableiten()` in `auswertung_iteration7.py` setzt sie nachträglich per Regel von Claude. Der Auswertungsbericht schreibt trotzdem „Quelle laut Prüfer“.
- **Keine Sitzungstabellen** (Start/Ende), weder in der ersten Abgabe noch in der Nachprüfung. Das war als Pflicht angekündigt (`iterationen.md`, Prüfung). A17 (Prüfzeit mit Zeitprotokoll) ist damit nicht belegt. Mediane von 1 Minute bei der ersten Abgabe sind kaum plausibel für ein Lesen des Originals.
- **Die Hilfsmittel stützen sich nur auf die Aussage des Prüfers.** Unabhängig belegen lässt sich „ohne KI-Hilfe“ nicht. Dass die erste Abgabe eine unfertige Datei war, die dann ersetzt wurde, ist dokumentiert, aber ebenfalls nur über die Aussage des Prüfers.
- **Unabhängigkeit:** Claude kennt die Listenwerte, hat der Nachprüfung Hinweise zur Vorgehensweise gegeben („Feld übernehmen“, „selbst ausrechnen“, Auswahl der Regelwirkungs-Lose) und die Quelle selbst abgeleitet. Das ist offen dokumentiert, aber es ist keine saubere Trennung zwischen Messung und Auswertung.
- **Die Kürzung und die Nachprüfung der 68 „unbekannt“-Lose waren Abweichungen vom Plan,** nach Kenntnis der Rohwerte der ersten Abgabe (Y1 zunächst 25 %). Die Festlegung der Nachprüfung kam also nach Kenntnis eines schlechten Ergebnisses. Das ist keine Bestätigungsverzerrung zugunsten der Hypothese, aber die Wahl der Lose („unbekannt“) war nicht blind, und die Kriterien selbst blieben unverändert.

### (d) Y4 Prototyp

**Teilweise erfüllt:**
- Der Prototyp wurde neu erzeugt (Commit a93785e), die Stufen A bis F stehen vorab in `src/report/beispiel_liste.py` (Funktion `stufe`).
- Die Fehler in 143100-2026 sind für Lose 8, 9, 14 behoben: Die Liste zeigt Ende Grundlaufzeit 31.03.2030 und Höchstende 31.03.2031. Für Los 8 stimmt das mit TED überein („Festlaufzeit von 01.01.2026-31.03.2030“, Verlängerung um ein Jahr bis 31.03.2031). Für Lose 9 und 14 habe ich nicht nachgesehen. Dass sie wie Los 8 gelesen wurden, ist plausibel, aber nur an Los 8 bestätigt.

**Aussagen zur Genauigkeit sind nur zum Teil gedeckt:**
- **Stufe A ist als „die sicherste“ bezeichnet (`beispiel_liste.md`, „Interpretation“), die Zahlen stützen das nicht.**
  - Stufe A umfasst per Definition alle Lose, deren Ende aus dem Text berichtigt wurde (`TEXT_GL`), also genau die Lose mit Regel 1b. Diese Lose schnitten in der Prüfung mit 8/15 ab.
  - Die in der Tabelle ausgewiesene Stufe-A-Quote (11/12) stammt nur aus Typ-Y-Losen und enthält keine Regel-1b-Lose.
  - Die Quote bei Stufe A ist also für den Teil, der die Regel betrifft, nicht belegt. Die Datei räumt zwar ein, dass der Typ „Festlaufzeit-Datum“ ungetestet ist, die Gesamtaussage „sicherste“ bleibt aber stehen.
- Die „Genauigkeit insgesamt“ (76,6 %, „Wilson 62,8–86,4 %“) ist in `beispiel_liste.md` offen mit Vorbehalten genannt (Kürzung, 4 leere Nachprüfungen, 5 Abschreibefehler). Das ist fair. Sie beschreibt aber ein Mischmaß aus Listenfehlern und Prüfungsfehlern und gilt für ganz Deutschland, nicht für die Oberpfalz.
- Die Stufentabelle beruht auf sehr kleinen Zahlen (Stufe D: 5 Lose, per Definition immer „korrekt“; Stufe C: 12 Lose). Das ist in der Datei vermerkt.
- Die Aussage „Zwei Fehler der Liste … 557125-2026 und 707425-2025“ (Zeile 192) stützt sich auf L72 und L82 aus L51 bis L95, also außerhalb der ausgewerteten Teilmenge, und auf die Eintragungen aus der ersten Abgabe. Ob der Text wirklich 31.08.2031 bzw. 31.10.2030 nennt, wurde nicht unabhängig geprüft.

### Schwächen (nach Schwere)

**Kritisch**
- Y1 misst für ca. 35 von 47 Losen die Abschrift des Feldes gegen das Feld und nicht die Grundlaufzeit (siehe (b)). Die Hypothese (Text nennt kürzere Laufzeit) ist nur an 12 Losen mit Quelle „Text“ (12/12) und an den nicht nachgeprüften R-Losen (8/8) inhaltlich getestet.
- Y1r ist durch das Verfahren verzerrt: alle Abweichungen kommen aus nachgeprüften Losen mit Feldübernahme. Gleiche Fälle (L74/L84 gegen L65/L88) werden verschieden bewertet (`liste_auswertung_iteration7.md`, Tabelle der Abweichungen).
- Hilfsmittel fehlen bei allen 38 Nachprüfungs-Einträgen (`liste_nachpruefung_iteration7.md`). Quelle wurde nachträglich abgeleitet (`auswertung_iteration7.py`, `quelle_ableiten`). Y3 ist damit nicht erfüllt.
- Stufe A wird als „sicherste“ bezeichnet, obwohl die Regel-1b-Lose (Stufe A per Definition) in der Prüfung nur 8/15 erreichten (`src/report/beispiel_liste.py`, `reports/beispiel_liste.md`).

**Mittel**
- Y2/Y2b: Die „bereinigten“ Werte (29/32, 24/27) schließen genau die 15 Lose aus, bei denen die Höchstende-Behauptung nicht geprüft wurde. Das sind Lose mit Herkunft „anzahl_x_laenge“. Die Höchstende-Angaben aus Anzahl × Länge sind damit praktisch ungeprüft. In `beispiel_liste.md` zeigt Stufe B nur 2/5 (12–77 %).
- 4 leere Nachprüfungen (L25, L27, L31, L38), 5 abgeschriebene Feldwerte, die von den Rohdaten abweichen (L16, L26, L30, L32, L48), und 2 „unbekannt“-Einträge trotz abgeschriebener Felder (L24, L44). Diese Prüferfehler sollen laut `iterationen.md` (Z. 1058) vom Prüfer noch korrigiert werden. Wenn das nach Kenntnis der Folgen („90 %-Schwelle fast erreichbar“) passiert, besteht Bestätigungsgefahr.
- Der Prüfer kennt die Regelwirkungs-Lose L57, L62, L65, L88. Die „Blindheit“ ist damit teilweise aufgehoben.
- Y1r hat nur 9 unabhängige Zuschläge (15 Lose), die Regeltreffer sind eng gefasst (alle vom Typ „text_laufzeit_option“, der Typ „text_festlaufzeit“ ist ungetestet).
- Die Wilson-Intervalle ignorieren das Clustern nach Zuschlag.

**Gering**
- Der Report schreibt „Quelle laut Prüfer“, obwohl ein Teil per Regel von Claude abgeleitet wurde.
- Die Wilson-Intervalle in `beispiel_liste.md` sind kaum zu prüfen (z. B. „65–99 %“ für 11/12), sie stimmen aber ungefähr mit Wilson überein.
- Die Hauptstichprobe enthielt kein einziges Regel-1b-Los (`iterationen.md`, Zeile 1028); das wurde offen ergänzt.

### Alternative Erklärungen
- **Y1 niedrig wegen Messdesign, nicht wegen schlechter Regel:** „Feld übernehmen, wenn der Text nicht widerspricht“ und die Nachprüfung ohne Textauszüge erzeugen Feldübernahmen. Alle Treffer in R stammen aus Text-Lesen, alle Fehler aus Feldübernahme. Das ist auch mit „die Regel ist richtig“ vereinbar, genauso gut aber mit „die Regel ist falsch, nur der Prüfer hat bei den Text-Losen anders gelesen“. Die Daten unterscheiden das nicht.
- **Y1 hoch bei Feld-Losen, weil trivial:** Liste und Prüfer lesen dasselbe Feld. Die 35 Treffer bei Herkunft „enddatum“ beweisen nur, dass das Feld korrekt abgeschrieben wurde.
- **Das Enddatum im Feld ist tatsächlich das Höchstende, und der Prüfer hat recht, das Feld zu übernehmen:** Dann wäre Regel 1b bei den 7 R-Losen falsch. Die Daten schließen das nicht aus, solange die Originale nicht von einem zweiten, unabhängigen Prüfer gelesen wurden.
- **Fehlende Angabe heißt „es gibt keine“ statt Lücke:** Bei Stufe C (keine Angabe zur Verlängerung, Höchstende = Grundlaufzeit angenommen) zählt „keine Verlängerung“ des Prüfers als korrekt, wenn der Prüfer im Auszug nichts fand. Im Volltext kann trotzdem eine Option stehen (so auch in der Stufenbeschreibung).
- **Cluster:** 360180-2025 und 267775-2025 (jeweils zwei R-Lose) sowie mehrere Lose derselben Zuschläge ziehen Y1r um ganze Zuschläge nach oben oder unten.

### Fakten vs. Interpretation
- `docs/iterationen.md`, Fortschrittsnotiz zur Nachprüfung (Z. 1056): „Die 4 Y-Abweichungen … gehen darauf zurück, dass der abgeschriebene Feldwert von den Rohdaten abweicht (Liste = Rohdaten)“ ist als Tatsache formuliert. Bestätigt habe ich es nur bei L26. Bei L16, L30, L32 ist es eine Annahme.
- `iterationen.md` Z. 1057: „Der Prüfer übernahm das Enddatum des Feldes“ als Ursache der R-Abweichungen ist plausibel, aber die Ursache (Prüferfehler statt Listenfehler) ist Interpretation.
- `reports/liste_auswertung_iteration7.md`: „Quelle laut Prüfer“ ist teilweise eine Ableitung von Claude.
- `reports/beispiel_liste.md`, „Interpretation“: „Stufe A … ist die sicherste“ ist eine Interpretation, die durch 8/15 bei Regel-1b-Losen nicht gedeckt ist.
- `reports/beispiel_liste.md` Z. 13: „bei den 15 Losen, die Regel 1b ändert, stimmten nur 8 mit dem Prüfer überein (der Prüfer übernahm dort das Enddatum des Feldes …)“ trennt Beobachtung und Deutung gut, die Deutung ist aber Behauptung.
- `docs/ki_irrwege.md` (Eintrag zur Ersetzungsregel): „verschlechterte einen zuvor richtigen Texteintrag“ gilt nur für die unfertige erste Datei.

### Betroffene Annahmen
(`docs/annahmen.md` enthält keinen Iteration-7-Eintrag; die Statusänderungen sind noch zu schreiben.)
- **A4 und A13 (Los-Ebene, Enddatum = Grundlaufzeit?):** Status „bleibt offen / teilweise gestützt“. Gestützt ist nur: Bei Losen, deren Text ein Datum nennt, stimmt das Enddatum der Liste (12/12). Keine Aussage ist möglich über den Anteil der Lose, bei denen das Feld das Höchstende ist.
- **A12 (Höchstende nur als Hinweis):** bestätigt die Einstufung „nur Hinweis“. Y2 und Y2b verfehlt, die bereinigten Werte sind selektiv.
- **A17 (Prüfzeit mit Zeitprotokoll):** nicht geprüft/belegt, weil Sitzungstabellen fehlen und der Median bei 1 Minute liegt.
- **A18:** laut Plan in dieser Iteration nicht geprüft, bleibt offen.
- **A1, A15:** außerhalb des Projektumfangs, ungeprüft.

### Was für ein belastbares Urteil fehlt
- Eine unabhängige Lesung der Originale (Text + Feld) für die Lose, die nur über Feldübernahme bewertet wurden. Mindestens für eine Zufallsauswahl, z. B. die 35 Feld-Lose, mit der Frage „nennt der Text eine kürzere feste Laufzeit?“.
- Für die 4 leeren Nachprüfungen sowie L16, L18, L24, L26, L30, L32, L44, L48 eine nochmalige Prüfung durch den Prüfer. Dabei besteht aber Bestätigungsgefahr, da das Ergebnis jetzt bekannt ist; besser wäre ein zweiter Prüfer.
- Hilfsmittel und Sitzungszeiten für die Nachprüfung (nachträglich nicht herstellbar).
- Eine Prüfung der Regel 1b an Losen vom Typ „text_festlaufzeit“ (nur L8 aus 143100-2026 von mir an TED bestätigt) und an mehr als 9 Zuschlägen.
- Eine Prüfung des Höchstendes (Herkunft „anzahl_x_laenge“) durch tatsächliches Lesen des Textes.

### Empfehlung

**Folge nach den vorab festgelegten Regeln (`iterationen.md`, „Was folgt aus welchem Ergebnis“):**
- Y1 liegt mit 76,6 % im Bereich 70 bis 90 %. Damit folgt: kein dritter Regelversuch, die Liste führt das Ende als „laut Bekanntmachung“, die Fehlerquote wird offen genannt, das Projekt wird mit diesem Stand abgeschlossen.
- „Weiter“ ist ausgeschlossen: Y1, Y1r, Y2, Y2b sind verfehlt, Y3 ist wegen der fehlenden Hilfsmittel der Nachprüfung nicht erfüllt.
- „Idee anpassen“ (Y1 < 70 %) greift nicht, die Untergrenze 70 % wird mit 76,6 % nicht unterschritten.

**Meine Einschätzung:** Die Regel „Abschluss mit diesem Stand“ ist formal richtig. Das Ergebnis darf aber nicht als „Regel 1b ist belegt“ oder „Regel 1b ist widerlegt“ gelesen werden. Es sagt nur: Mit diesem Verfahren war die Hypothese nicht nachweisbar. Der Abschluss sollte den Typ „text_festlaufzeit“ als ungetestet benennen, Y1 als Mischmaß aus Listenfehlern und Prüfungsfehlern beschreiben und die Aussage „Stufe A ist die sicherste“ zurücknehmen oder umformulieren. Die Entscheidung trifft der Nutzer.

Relevante Dateien (alle unter `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\`): `docs\iterationen.md`, `reports\liste_auswertung_iteration7.md`, `reports\abschreibecheck_iteration7.md`, `reports\liste_pruefung_iteration7_urteile.csv`, `reports\liste_pruefung_iteration7_urteile_abgabe1.csv`, `reports\liste_nachpruefung_iteration7.md`, `reports\liste_nachpruefung_iteration7_urteile.csv`, `data\processed\liste_pruefung_iteration7_schluessel.csv`, `src\prepare\auswertung_iteration7.py`, `src\prepare\vertragsliste.py`, `src\report\beispiel_liste.py`, `reports\beispiel_liste.md`, `docs\ki_irrwege.md`.
---

### Nachprüfung durch Claude und Entscheidung (2026-11-04)

**Nachgeprüft (Fakten):**
- L65 und L88: In der maßgeblichen zweiten Abgabe (`reports/liste_pruefung_iteration7_urteile.csv`) steht „unbekannt“, nur in der unfertigen ersten Datei (`…_abgabe1.csv`) 29.06.2026 mit Quelle „Text“. Die Aussagen in `docs/ki_irrwege.md` und `docs/iterationen.md` (Fortschrittsnotiz zur Nachprüfung, Befund 3), die Nachprüfung habe einen zuvor richtigen Texteintrag ersetzt, sind deshalb falsch; Korrekturen als Nachtrag.
- Hilfsmittel der Nachprüfung: Das Feld ist bei allen 38 Einträgen leer. Der Prüfer gab im Gespräch an, keine Hilfsmittel benutzt zu haben; das ist nur eine Selbstangabe und wird so vermerkt.
- „Quelle laut Prüfer“ in `reports/liste_auswertung_iteration7.md` und „Stufe A ist die sicherste“ in `reports/beispiel_liste.md` sind umformuliert (Skripte geändert, Berichte neu erzeugt, Zahlen unverändert).

**Entscheidung des Nutzers:** Abschluss mit diesem Stand nach der vorab festgelegten Folge „Y1 zwischen 70 % und 90 %“: kein dritter Regelversuch, die Liste führt das Ende der Grundlaufzeit als „laut Bekanntmachung“, das Höchstende nur als Hinweis, die Fehlerquote wird offen genannt.
Die Prüfer-Einträge (4 leere Lose, abgeschriebene Feldwerte) werden nicht nachträglich korrigiert (Bestätigungsgefahr). Als nächster Schritt folgt eine getrennte Messung (Iteration 8, KI-Zweitlesung), die das Ergebnis von Iteration 7 nicht ersetzt.
