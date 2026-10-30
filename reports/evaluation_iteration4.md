# Evaluation Iteration 4

Kritische Prüfung durch den Subagenten `evaluator` am 2026-10-30 (nur Lesezugriff), im Rahmen von `/iteration-ende`. Bericht unverändert
übernommen. Nachtrag Claude: Den SHA-256 des Schlüssels hat der Evaluator nicht prüfen können; Claude hat ihn geprüft
(`45aff7a4eb2399d0aafd3ff74c330016b858026e89d8f3738df3de966dbe9bcc`, stimmt mit `docs/iterationen.md` überein).

Nachgerechnet habe ich aus `reports/sichtbarkeit_iteration4_gt.csv`, `reports/zuordnung_iteration4.md`, dem Schlüssel `data/processed/blindpruefung_iteration4_schluessel.csv` und `reports/blindpruefung_iteration4.md`. Die Reihenfolge der Commits habe ich in `.git/logs/HEAD` geprüft. Den SHA-256 des Schlüssels konnte ich nicht prüfen, weil ich keine Shell habe. Der Inhalt passt aber zur Erzeugungslogik in `src/blindpruefung_iteration4.py`: Ich habe die Gruppen A bis D gegen gt.csv, `zuordnung_iteration4_lauf.json` und `paarbeurteilung_iteration4.md` abgeglichen.

## Urteil je Kriterium

| Kriterium | Urteil | Beleg (Quelle) |
|---|---|---|
| Vorab festgelegt | erfüllt | Hypothese, W1–W6 und Folgen sind auf 2026-10-25 datiert (iterationen.md, Abschnitt Iteration 4). Reihenfolge laut Reflog: „Iteration 4 angelegt“ → 1d0e060 (Regel eingefroren) → e2223ea (Testprobe, 5 Min später) → Handsuche Teil 1–5 → d43c547 (Ground Truth) → ec4733e (Regel-Lauf) → ba607e5 (W4-Schlüssel) → 078d2c1 (Urteile). Den Inhalt des Commits „angelegt“ habe ich nicht geöffnet. |
| W1 Sichtbarkeit ≥ 50 % | nicht erfüllt | 30/70 = 42,9 % (Wilson 31,9–54,5), nachgezählt: 18 objektgleich_mittel, 12 teilmenge, **0 objektgleich_hoch**, 18 unklar, 22 kein Vorgänger. Mit „unklar, eher dafür“ (10 Fälle) wären es 40/70 = 57,1 %. Die Schwelle liegt also im Bereich der Definitionsfrage. |
| W2 Präzision | nicht erfüllt (formal), nur Hinweis | 17/19 = 89,5 %, Wilson 68,6–97,1 (nachgerechnet). **Die Mindestzahl von 25 Vorschlägen ist verfehlt.** Nur objektgleich korrekt: 9/19. Zählt man U35 nicht (älterer Vorgänger 517331-2019 statt 325959-2023): 16/19 = 84,2 %. |
| W3 Trefferquote ≥ 60 % | nicht erfüllt (knapp) | 17/30 = 56,7 % (Wilson 39,2–72,6). Mit 18/30 wäre die Schwelle erreicht. Ohne U35: 16/30 = 53,3 %. |
| W4 Zweitprüfung ≥ 85 % | nicht erfüllt | Nachgezählt 13/20 = 65 % (Wilson 43,3–81,9, die Obergrenze liegt also unter 85 %), Cohen's κ ≈ 0,29. Nach Gruppe: A 4/6, B 5/6, C 0/4, D 4/4. Abweichungen: P5, P7, P9, P11, P12, P18, P19. |
| W5 Backtest-Basis ≥ 100/Jahr | erfüllt (Punktwert) | 7/70 × 1893 = 189. Das Wilson-Intervall von 7/70, hochgerechnet, reicht von 93 bis 364. Der Parser zählt zu wenig (siehe Schwächen), mit U2, U6, U13 und U14 wären es 11/70, also etwa 297. |
| W6 Kandidatenliste ≥ 70 % | erfüllt (knapp), nur Hinweis | 22/30 = 73,3 % (Wilson 55,6–85,8). Zwei Fälle weniger, und die Schwelle wäre verfehlt. |
| Prüfzeit (explorativ) | Median 2 Min | Nachgerechnet: 3× 1, 8× 2, 6× 3, 3× 4 Minuten, zusammen 49 Minuten (geplant waren rund 1,5 Stunden). Selbst notiert. |
| **Hypothese (80/60)** | **nicht bestätigt** | W2 hat die Mindestzahl nicht erreicht, W3 liegt unter der Schwelle, W4 auch. |

## Welche vorab festgelegte Folge greift

1. **W4 < 85 % greift.** W2, W3 und W6 gelten nur als Hinweis. Es gibt keinen weiteren Regelversuch, die Entscheidung fällt in Phase 1 („Idee anpassen“).
2. W1 < 30 % greift nicht: Der Punktwert liegt bei 42,9 %, die Wilson-Untergrenze bei 31,9 %, also knapp darüber. Für W1 zwischen 30 und 50 % ist keine Folge festgelegt. Das ist eine Lücke, aber sie ändert am Ergebnis nichts.
3. „Weiter zu Phase 3“ greift nicht, weil W2 (Mindestzahl), W3 und W4 verfehlt sind.
4. Die Folge „Produkt mit manueller Prüfung“ (W6 ≥ 70 %, Median ≤ 5 Min) ist **zahlenmäßig erfüllt, inhaltlich aber nicht gedeckt**. W6 ist laut Folge 1 nur ein Hinweis. Die Prüfzeit von 2 Minuten stammt genau aus der Prüfung, die nur zu 65 % übereinstimmte. Belegt ist damit „schnell“, aber nicht „schnell und zuverlässig“.
5. **Robust:** Alle Wege führen zu Phase 1 / „Idee anpassen“. Auch wenn man die Urteile des Nutzers für die 7 strittigen Paare übernimmt, bleibt W3 verfehlt (eigene Rechnung, übrige 63 Fälle unverändert): W1 31/70, W3 15/31 = 48,4 %, und W2 fiele auf 15/19 = 78,9 %.

## Schwächen (nach Schwere)

**Kritisch**
- **Die Ground Truth ist nicht unabhängig bestätigt.** Alle W-Werte beruhen auf der Handsuche des Subagenten. Rechercheur, Regelbau und Paarurteil laufen auf derselben Modellfamilie, blinde Flecken können also gemeinsam sein. Die einzige menschliche Prüfung (W4) bestätigt die Ground Truth nicht. W5 ist von der Regel „nur Hinweis“ nicht erfasst, hängt aber genauso an der Ground Truth.
- **W4 misst hier vor allem, wie sorgfältig und regelkonform die Zweitprüfung war, und kaum, wie eindeutig die Definition ist.** Belege:
  - Bei den drei Fällen, in denen der Nutzer strenger urteilte, standen die entscheidenden A-Merkmale im Text, den der Nutzer vorliegen hatte (`ted_paare_inhalt.txt`):
    - P7: „Bahnhofstraße 8 99706 Sondershausen“ in 272214-2020, Los 2 und Los 4 (Zeilen 7155–7181).
    - P11: die Objekte Oedeme und Bleckede in 79802-2023 (Zeilen 8738–8755).
    - P19: „Trakt 1 - 3“ und „Trakt 4 - 10, MZ, UBZ“ in 362257-2022 (Zeilen 13228–13239).
  - In Gruppe C widersprechen die Begründungen des Nutzers selbst den Regeln 1.1:
    - P5 nennt eine andere Leistungsart (Glas gegenüber Gebäudereinigung). Das wäre ein Widerspruch, das Urteil lautet trotzdem „teilmenge“.
    - P9 argumentiert mit der Zeit, was Spielregel 3 verbietet, und äußert selbst Zweifel. Nach der Rangfolge wäre das vorsichtigere Urteil fällig gewesen.
    - P12 vergibt „hoch“ allein wegen der Leistungsart. Stufe B ist nicht erkennbar („verschiedene städtische Gebäude“).
    - P18 begründet mit „wahrscheinlich Sammlung“. Eine Teilmenge setzt aber belegte gemeinsame Objekte voraus.
  - Auch mehrere Übereinstimmungen sind schwach begründet: P3 und P4 haben wortgleiche Begründungen, und P4 betrifft eine Fachhochschule, keine Schulen; P20 „In Berlin, ähnliche Aufgaben“; P1 „selber Auftrag etc.“.
  - Gerecht formuliert: Ein Durchfallen von W4 belegt weder, dass die Definition unklar ist, noch, dass die Ground Truth falsch ist.
- **Die Prämisse „Produkt mit manueller Prüfung“ ist nicht belegt.** Die einzige gemessene Handprüfung (Median 2 Min) erreicht 65 %. Positiv ist, dass Gruppe D (die Kandidaten der Regel bei „kein Vorgänger“ verwerfen) mit 4/4 gelingt. Falsch angenommen wurden dagegen alle 4 „unklar“-Kandidaten.

**Mittel**
- **W2 beruht auf einer leichten Teilmenge.** Die Regel macht nur bei 19 von 70 Fällen einen Vorschlag. 8 der 17 korrekten Vorschläge sind Teilmengen. Bei U35 schlägt die Regel einen Vorgänger von 2019 vor, obwohl 2023 ein Verfahren dazwischen lag; die Paarbeurteilung vermerkt selbst einen möglichen Zwischenvertrag. Die Hypothese spricht von „dem objektgleichen Vorgänger“.
- **W1 hängt an der Definition.** Streng (nur „hoch“) ergibt 0/70, breit 30/70. Die Urteilsregeln selbst (Schritt 5) sagen, dass die Aussage bei einem solchen Abstand an den Zweifelsfällen hängt. Die Grenze „nahezu deckungsgleich“ hat keine feste Schwelle: U37 mit 14/16 gilt als objektgleich, U47 mit 12/14 bzw. 12/15 als teilmenge. Das betrifft nur die Angabe „nur objektgleich“, nicht den Binärwert.
- **Auffällige Unterschiede zwischen den Teilen der Handsuche.** Gefundene Vorgänger je Teil: 5, 4, 5, 8, 8. Teil 1–3 kommen auf 14/42, Teil 4–5 auf 16/28. Die Aufteilung habe ich nachträglich gewählt; Zufall ist möglich. Mögliche Ursachen sind der Hinweis zur FT-Syntax erst ab Teil 2 und lokale Suchen ohne Budget, also ungleiche Suchtiefe.
- **Die Lesehilfe ist nicht dokumentiert.** Für `data/processed/ted_paare_inhalt.txt` gibt es kein Skript und keinen Verweis im Repo. Die Datei enthält rohe XML-Textknoten ohne Feldnamen und viele mehrsprachige Zeilen, Regel 4 verlangt aber „Feld und Wert“. Auch der erste, zurückgewiesene Satz von Urteilen steht nicht im Repo. Ob er den zweiten Satz beeinflusst hat, ist nicht prüfbar.
- **W5 hat einen Parser-Fehler.** `src/auswertung_iteration4.py`, Zeile 108, prüft `herkunft == "grundlaufzeit"` exakt. Damit fallen U2, U6, U13 und U14 heraus (Herkunft „grundlaufzeit, hoechstende“), W5 ist zu niedrig. Umgekehrt zählt U65 mit, obwohl laut Handsuche ein Zwischenvertrag nicht auf TED steht; das Ende gehört also nicht zum ersetzten Vertrag.
- **Zeitpunkt der Entscheidung „kein Kundenkontakt“.** Sie fiel am 2026-10-29 (cc8d301), nachdem W2, W3 und W6 bekannt waren (ec4733e, 2026-10-26). Damit entfällt genau der Input aus Phase 1 für die jetzt ausgelöste Folge. Die Kriterien blieben unverändert, eine Manipulation liegt also nicht vor.
- **Entwicklung und Test nutzen verschiedene Definitionen.** Die Regel wurde auf Q3 gegen die großzügigere Ground Truth aus Iteration 3 abgestimmt. Testdaten gibt es nur aus einem Quartal (Q1), Saisonalität ist also nicht geprüft.

**Gering**
- In `zuordnung_iteration4.md` steht „vorzeitig: U16, U20, U66, U70 (von 30 Fällen mit Vorgänger)“. U20 gehört zur Kategorie „unklar“. Korrekt sind 3/30 (Ursache: Zeile 117 filtert nicht auf W1). Dazu ein kosmetischer Fehler: „68,6%,“ mit Komma am Ende.
- Die W4-Zusammensetzung weicht von Plan-Schritt 6 ab („Zufall“ und „schwach belegt“ wurden durch die Gruppen B und C ersetzt). Das war vor den Urteilen festgelegt.
- Bei P1, P2 und P10 fehlt die Sicherheit. Auf die Binärzählung hat das keinen Einfluss.
- CLAUDE.md nennt noch „63 %“, und die Stand-Zeile in projektplan.md ist veraltet.

## Alternative Erklärungen

- **W4 = 65 %:**
  - (a) Zeitdruck oder geringe Sorgfalt (2 Minuten, Begründungen über Stufe B und C).
  - (b) Unlesbare Lesehilfe.
  - (c) Unschärfe an der Grenze zu „unklar“: 6 der 7 Abweichungen haben auf einer Seite „unklar“, nur P11 ist ein harter Widerspruch.
  - (d) Fehler in der Ground Truth. Meine Lektüre von P7, P11 und P19 stützt das nicht, für die übrigen Paare ist es nicht ausgeschlossen.
  - (e) Verankerung durch den ersten Urteilssatz (nicht prüfbar).
  - Nachträgliche Varianten, **nicht als Ersatz zu verwenden:** mit Tendenz 15/18 = 83 %; „breit“, also Paare mit „unklar“ auf einer Seite ausgeschlossen, 13/14 = 93 %. Nur die großzügigste nachträgliche Variante läge über 85 %.
- **W1 von 63 % auf 43 %:** Das kann an der strengeren Definition 1.1 liegen, an Vorgängern nur mit CPV 909 (U21), am anderen Quartal oder an Unterschieden zwischen den Teilen der Handsuche. Es heißt nicht zwingend, dass weniger Vorgänger sichtbar sind.
- **W2 hoch:** Die Regel ist zurückhaltend und schlägt nur in klaren Fällen etwas vor. Die strengere Ground Truth enthält zudem weniger zweifelhafte Positive.
- **W6:** Bei Auftraggebern mit wenigen Verfahren landet der Vorgänger fast automatisch unter den Top 3. Nicht geprüft; `n_candidates` in der Lauf-JSON würde es zeigen.
- **Vorlaufzeit (Median 0,3 Monate):** Entweder werden Verlängerungen gezogen, oder der Vorgänger auf TED ist nicht der unmittelbare (U65).

## Fakten vs. Interpretation

- iterationen.md, Nachtrag 2026-10-29: „Die Folge ‚Produkt mit manueller Prüfung‘ bleibt bewertbar über W6 und die Prüfzeit“ ist eine Interpretation. W6 und die Prüfzeit messen Abdeckung und Tempo, nicht ob die Prüfung zuverlässig ist und ob das Produkt trägt.
- zuordnung_iteration4.md, „Explorativ“: Die Liste der vorzeitigen Neuvergaben ist sachlich falsch (U20). Die Vorlaufzeiten werden ohne Hinweis auf die Lücke bei U65 genannt.
- CLAUDE.md: „Objektgleiche Vorgänger sind auf TED oft sichtbar“. „Oft“ ist eine Wertung, und die Zahl ist durch Iteration 4 überholt.
- Die Teile der Handsuche und die Paarbeurteilung kennzeichnen ihre Einschätzungen sauber, z. B. U54, U47 und Q2 „Einschätzung (nicht geprüft)“. Das ist gut.

## Betroffene Annahmen (Vorschläge für annahmen.md)

- **A3:** Status bleibt „ungeprüft“. Ergänzen: Iteration 4, W1 30/70 = 42,9 % (Wilson 31,9–54,5), nur objektgleich 18/70 = 25,7 %, „hoch“ 0/70, mit „eher dafür“ 40/70. Geltungsbereich: Ausschreibungen Q1 2026, Haupt-CPV 90910/90911/90919, DEU, höchstens 2 je Auftraggeber, Urteilsregeln 1.1, Vorgänger nur CPV 909 auf TED ab Oktober 2016, Ground Truth nicht menschlich bestätigt (W4 65 %). Mit Iteration 3 nicht direkt vergleichbar. Gemessen ist weiterhin nicht der Marktanteil von TED. Vorschlag: A3b neu anlegen, „≥ 50 % der Ausschreibungen haben einen sichtbaren objektgleichen Vorgänger“, ungeprüft mit Warnsignal.
- **A9c:** ungeprüft → widerlegt **für die Variante** `src/zuordnung_los.py` @1d0e060 (Schwellen 80/60, ≥ 25 Vorschläge). Begründung: W3 ist unter beiden Lesarten verfehlt (56,7 % bzw. 48,4 %), die Mindestzahl für W2 ebenfalls. Vermerk: Die Präzision von 89,5 % auf 19 Vorschlägen ist ein Hinweis, die Ground Truth ist unbestätigt, W3 knapp. Wer vorsichtiger sein will: Status „ungeprüft“ mit Vermerk „Kriterium verfehlt, kein weiterer Versuch“. Die Entscheidung liegt beim Nutzer.
- **A8:** bleibt ungeprüft. Explorativ, 7 Paare: Vorlaufzeit bis zum Ende der Grundlaufzeit von −18,3 bis +26,3 Monaten, Median 0,3 Monate. 3 von 7 Ausschreibungen erschienen erst nach dem Ende der Grundlaufzeit. Interpretation: Das Ende der Grundlaufzeit allein ist kein brauchbarer Ankerpunkt. Das Prognoseziel muss vor Iteration 5 festgelegt werden. Geltungsbereich: Treffer der Regel mit Herkunft exakt „grundlaufzeit“ (Parser), Q1 2026.
- **A10:** bleibt ungeprüft, Warnsignal bestätigt. Mindestens 4 der 7 Paare in W5 haben Vorgänger vor eForms (U47, U56, U64, U65). W5 ergibt 189 pro Jahr, die Hochrechnung des Intervalls reicht von 93 bis 364.
- **A11:** unverändert „vorläufig gestützt“. Die Handsuche bestimmte die Laufzeiten vor eForms mehrfach über die zugehörige Ausschreibung (U47, U56, U65). Das war keine Zufallsstichprobe.
- **A12:** bleibt ungeprüft. Ergänzen: Die Population enthält weiterhin Kanalreinigung (U21) und Arbeitnehmerüberlassung (U50). Der Fehlvorschlag bei U66 betraf Schriftgutvernichtung (CPV 90918000), weil „fachfremd“ nur im Titel geprüft wird. Die Leistungsart je Los entscheidet. Ausgezählt ist das nicht, deshalb keine Statusänderung.
- **A16:** bleibt ungeprüft. Iteration 4: 3/30 = 10 % „ja“ (Wilson 3,5–25,6; U16, U66, U70), 7 unklar, 20 nein. Gestützt ist nur „selten vorzeitig“, nicht „zum regulären Ende“. Geltungsbereich: Handsuche Q1 2026, geplante Enddaten.
- **A1/A15:** unverändert. Vermerk: Die Entscheidung in Phase 1 („Idee anpassen“) fällt ohne Belege zur Nachfrage.
- **Neu A17:** „Ein Mensch kann Kandidatenpaare in ≤ 5 Minuten zuverlässig (≥ 85 %) bestätigen oder verwerfen.“ Risiko hoch, ungeprüft mit Warnsignal: W4 13/20 bei Median 2 Minuten, κ ≈ 0,29, Gruppe D 4/4, Gruppe C 0/4. Geltungsbereich: ein Prüfer, Textauszug ohne Feldnamen, Q1 2026, Regeln 1.1.
- **Neu A18:** „Die Ground Truth der Handsuche (rechercheur, Regeln 1.1) ist korrekt.“ Risiko hoch, ungeprüft. W4 bestätigt sie nicht. Stichproben zu P7, P11 und P19 sprechen für die Ground Truth, aber es gibt keinen unabhängigen Nachweis.

## Was für ein belastbares Urteil fehlt

- Eine unabhängige, vorab festgelegte Prüfung der Ground Truth: Urteilsvorlage je Paar, lesbare Ansicht (TED-HTML oder Auszug mit Feldnamen), keine Zeitgrenze. Sie dient der Backtest-Basis in Iteration 5 und **nicht** dazu, W4 nachträglich zu retten.
- Der SHA-256 des Schlüssels: `Get-FileHash` gegen `45aff7a4…9bcc`.
- Dokumentation des zurückgewiesenen ersten Urteilssatzes und der Herkunft der Lesehilfe.
- W5 mit korrigiertem Parser und nur unmittelbaren Vorgängern.
- Die Vorlaufzeit auf allen 30 Paaren der Ground Truth statt nur auf 7.
- W6 getrennt nach Anzahl der Kandidaten.

## Empfehlung

**Idee anpassen (Phase 1).** Das ist die vorab festgelegte Folge von W4 < 85 %. Sie wird zusätzlich dadurch gestützt, dass W3 unter beiden Lesarten verfehlt ist. Ein weiterer Regelversuch ist ausgeschlossen. W4 nachträglich umzudeuten (z. B. die Variante „breit“ mit 93 %), um doch „weiter“ zu wählen, wäre Bestätigungsgefahr.

Phase 1 müsste entscheiden:
1. **Rolle der Zuordnung:** Ist sie ein Produktmerkmal oder nur ein Werkzeug zur Validierung? Die einfachste Anpassung wäre eine Vertragsliste aus Zuschlägen (gestützt durch A4 und A13) als Prototyp. Der Backtest würde dann auf handgeprüften Paaren laufen, deren Ground Truth zuerst bestätigt wird.
2. **Produkt mit manueller Prüfung:** Kommt es noch in Frage? Dann nur mit strukturierter Prüfung, einer realistischen Prüfzeit und einem neuen Zuverlässigkeitstest, der vorab festgelegt wird.
3. **Abdeckung offen benennen:** In Q1 2026 haben etwa 43 % der Fälle einen sichtbaren Vorgänger, bei 31 % (22/70) steht er unter den Top 3. Außerdem muss das Prognoseziel festgelegt werden: Ende der Grundlaufzeit oder Höchstende.

Die Entscheidung trifft der Nutzer.
