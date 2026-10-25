# Evaluation Iteration 3

Kritische Prüfung durch den Subagenten `evaluator` am 2026-10-25 (nur Lesezugriff), im Rahmen von `/iteration-ende`.
Bericht unverändert übernommen.

Grundlage: `docs/iterationen.md` (Abschnitt „Iteration 3“), `reports/zuordnung_iteration3.md`, `reports/sichtbarkeit_iteration3_gt.csv`, `reports/sichtbarkeit_iteration3_teil1–4.md`, `reports/zuordnung_iteration3_urteile.csv`, `reports/blindpruefung_iteration3*.md`, `reports/urteilsregeln_blindpruefung.md`, `reports/a11_stichprobe.md`, `reports/regel_entwicklung_iteration3.md`, `src/blindpruefung_iteration3.py`, `src/auswertung_iteration3.py`, Schlüssel `data/processed/blindpruefung_iteration3_schluessel*.csv`. Wenn ich selbst gerechnet habe, steht „(eigene Rechnung)“ dabei. Für die Wilson-Intervalle habe ich z = 1,96 verwendet.

## Urteil je Kriterium

| Kriterium | Urteil | Beleg (Quelle) |
|---|---|---|
| Kriterium vorab festgelegt | **erfüllt für die Schwellen, teilweise für das Verfahren.** | Hypothese, Begriffe, V1–V6 und Folgen stehen vor Schritt 1 fest (iterationen.md, „vorab festgelegt am 2026-10-23“). Danach wurde aber das Messverfahren geändert: in der Handsuche (Teil 2 und Teil 4 mit „Ergänzender Auslegung“) und in V4 (Urteilsregeln erst nach Ansicht der Paare, P1–P8 ausgeschlossen, P21–P28 nachgezogen). |
| V1 Sichtbarkeit ≥ 50 % | **formal erfüllt, aber knapp und abhängig von der Definition.** | 38/60 = 63,3 % (Wilson 50,7–74,4), zuordnung_iteration3.md. Nachgezählt aus gt.csv: 29 objektgleich, **9 teilmenge** (T6, T10, T14, T18, T33, T34, T52, T53, T59), 14 kein_vorgaenger, 8 unklar. Nur objektgleich: **29/60 = 48,3 % (Wilson 36,2–60,7)**, also unter 50 % (eigene Rechnung). |
| V2 Präzision ≥ 80 %, Untergrenze ≥ 60 % | **klar verfehlt** | 11/24 = 45,8 % (27,9–64,9). Bei jeder Lesart liegt V2 zwischen 10/24 und 12/24, höchstens 50 %. Ohne Teilmengen 6/24 = 25 % (eigene Rechnung). |
| V3 Trefferquote ≥ 60 % | **klar verfehlt** | 11/38 = 28,9 % (17,0–44,8). Ohne Teilmengen 6/29 = 20,7 % (eigene Rechnung). |
| V4 Zweitprüfung ≥ 85 % | **formal erfüllt (17/20 genau auf der Schwelle), als Beleg nicht tragfähig** | Gegen die Schlüssel nachgezählt: Abweichungen P16, P18, P28, also 17/20 = 85 %. **Wilson 64,0–94,8 %**, Cohens κ ≈ 0,70 bei 11 „gefunden“ und 9 „nicht“ im Schlüssel (eigene Rechnung). Verfahrensabweichungen siehe unten. |
| V5 Backtest-Basis ≥ 100/Jahr | **formal erfüllt, inhaltlich überschätzt** | 10/60 × 492 × 4 = 328 stimmt rechnerisch. Davon sind 2–3 Enddaten fragwürdig (T26, T56, T18, siehe unten). Robust etwa 7/60, also ≈ 230/Jahr (Wilson 114–437). Nur mit eForms-Vorgängern 3–4/60, also ≈ 98–131/Jahr (eigene Rechnung). |
| V6 A11 ≥ 80 % | **erfüllt, knapp, mit engem Geltungsbereich** | 25/30 = 83,3 % (66,4–92,7), a11_stichprobe.md. Nachgezählt: 25 bestimmbar, 2 ohne Verweis, 3 nur Dauer. Schon 23/30 = 76,7 % würde die Schwelle verfehlen. |
| Explorativ: vorzeitige Neuvergaben > 30 % | **nicht ausgelöst** | Zähler: T18 (nur Lose 8/9, teil2 Z. 112) und T32 (teil3 Z. 400 und 429), also 2. Nenner: 36 von 38 gefundenen Paaren, bei denen sich die Grundlaufzeit gegen den Testfall-Beginn entscheiden lässt. Nicht entscheidbar ist T13 (Beginn fehlt). T10 ist nur geschätzt und nicht mitgezählt. Ergebnis **2/36 = 5,6 % (Wilson 1,5–18,1 %)**, nur objektgleich 1/28 = 3,6 % (eigene Rechnung aus teil1–4). |

## Schwächen (nach Schwere)

**Kritisch**

- **V4 ist methodisch nicht mehr die vorab geplante Prüfung.**
  - Die Urteilsregeln entstanden *nach* der Ansicht aller 20 Paare. Auch P9–P20 hatte der Nutzer schon gesehen. Unabhängig sind nur P21–P28, dort ist die Übereinstimmung 7/8.
  - Die Kalibrierung entstand teilweise nach Kenntnis der Grenzfall-Hinweise des Subagenten (iterationen.md, Nachtrag „Urteilsregeln“).
  - Die pauschale erste Einschätzung „alle passen oder unsicher“ wurde nicht paarweise erfasst und ist deshalb nicht prüfbar. Grob abgeschätzt: Hätte der Nutzer nach diesem Eindruck alle Paare als „gefunden“ gewertet, wäre die Übereinstimmung nahe dem Anteil der „gefunden“-Paare im Schlüssel gewesen, etwa 50 %. Die 85 % entstehen also erst durch Regeln, die an denselben Paaren entwickelt wurden.
  - Die Ersatzpaare sind leichter als die ersetzten. Unter P1–P8 waren ein schwach belegter Fall (T4), eine Teilmenge (T14) und zwei unklare (Esslingen, Springe). Die vier „gefunden“-Ersatzpaare P21, P22, P24, P27 haben alle Belegstärke „stark“ (gt.csv: T41, T13, T56, T45). Die vier „nicht“-Ersatzpaare sind Geschwisterverfahren, die oft schon am Titel als verschieden erkennbar sind (P23, P25, P26).
  - Der eigentliche Zweck von V4, die schwach belegten Treffer zu prüfen (`src/blindpruefung_iteration3.py` Z. 4: T4, T10, T11), ist nur noch mit zwei Fällen abgedeckt: P17 stimmt überein, P18 nicht. Die übrigen Treffer mit Belegstärke „mittel“ (T21, T30 aus Teil 2, T40) wurden nie geprüft. T40 landete zufällig in der Kalibrierung (P5).
  - Eine einzige Abweichung mehr ergibt 16/20 = 80 % und löst „V1–V3 gelten nicht“ aus. P28 ist ein Wackelfall in beide Richtungen. Der Nutzer urteilt „objektgleich“, obwohl beide Seiten nur „diverse“ Objekte bzw. Standorte nennen. Nach der eigenen Regel V1.1 („Sind beide Seiten unspezifisch …, ist ‚unklar‘ das höchste erreichbare Urteil“) wäre das „unklar“, und V4 stiege auf 18/20. Bei P17 würde dieselbe strenge Lesart wie beim Agenten („unklar“) eine neue Abweichung erzeugen. Netto sind es also 17 ± 1.
- **Richtung der Abweichungen:** Nutzer und Agent haben unabhängig voneinander bei P16 und P18 dieselbe Abweichung vom Schlüssel. Der Schlüssel (Handsuche und Claudes Einzelurteile) ist damit systematisch großzügiger als Regel V1.1. Das betrifft V1 direkt: Die Definition des Rechercheurs lässt für „teilmenge“ schon ein gemeinsames Objekt genügen (`.claude/agents/rechercheur.md` Z. 25). V1.1 verlangt mindestens 50 % der kürzeren Liste.
- **V1 hängt an den Teilmengen.** Ohne die 9 Teilmengen läge V1 bei 48,3 %, das wäre nach Vorab-Regel „V1 30–50 % → Idee anpassen“. Der Vorab-Plan zählt Teilmengen zwar ausdrücklich als „gefunden“, das formale Urteil steht also. Die Strenge-Prüfung der Urteilsregeln (Schritt 5) zeigt aber selbst, dass das Ergebnis nicht robust ist: Der Agent vergibt 0 von 20 Paaren „objektgleich (hoch)“ (`blindpruefung_iteration3_agent_v1_1.md`, „Spanne“), der Nutzer 2 (P10, P27).

**Mittel**

- **Die Definition hat sich während der Handsuche verschoben.**
  - Teil 2 führt neu ein, dass „objektgleich (mittel)“ auch ohne Objektnamen gilt, wenn Kennzahlen übereinstimmen (T21, T30; teil2 Z. 32–35).
  - Teil 4 ergänzt eine weitere Regel für „unklar“ (T46; teil4 Z. 35).
  - Die Fälle wurden also nicht durchgehend mit derselben Regel eingestuft.
  - In gt.csv fehlt die Belegstärke für T18–T30, obwohl Teil 2 sie angibt (z. B. T21 und T30 „mittel“). Das ist ein Übertragungsfehler, der die Auswahl der schwachen Fälle für V4 beeinflusst hat.
- **Die Population ist nicht sauber abgegrenzt.** T16 ist eine Bauzwischen- und Bauendreinigung. Sie fällt sachlich aus der Population, weil die Stichwortliste nur den Titel prüft (teil2 Z. 393), steht aber im Nenner von V1 und V3. Ohne T16 ergibt sich V1 = 38/59 = 64,4 %, die Wirkung ist also klein.
- **„Objektgleicher Vorgänger auf TED“ heißt oft nicht „direkter Vorgänger auf TED“.** Zwischen dem Ende des gefundenen Vorgängers und dem Testfall liegt eine Lücke bei mindestens T1, T8, T14, T15, T23, T24, T26 (Interim), T34, T38 und T40, das sind ≥ 10 der 38 (teil1 Z. 371, teil2 Z. 391, teil3 Z. 427). Für eine Prognose der Kette ist V1 deshalb optimistischer, als die Zahl wirkt.
- **Vorgänger-Enddaten in V5 sind fragwürdig.**
  - T26: Als Ende steht 2031-10-31. Das ist die geplante Laufzeit des *aufgehobenen* Verfahrens 462151-2026 desselben Objekts, nicht das Ende des Vorgängervertrags. Dieses war 2026-03-31 (95743-2021 bzw. 557850-2020, teil2 Z. 261–266).
  - T56: Eingetragen ist 2023-12-31, das Ende der Grundlaufzeit. Laut Handsuche verlängert sich der Vertrag danach jährlich, das Vertragsende ist „unbekannt“ (teil4 Z. 263, 384).
  - T18: Das Ende gilt nur für die Lose 8/9.
  - `auswertung_iteration3.py` nimmt das Grundlaufzeit-Ende des *vorgeschlagenen* Notice, ungeprüft.
- **V5 setzt voraus, dass korrekte Vorschläge erkennbar sind.** Bei V2 = 45,8 % lassen sich die 10 korrekten Paare im Betrieb nicht von den 11 falschen und 2 unklaren unterscheiden. 328/Jahr beschreibt daher eine Basis *mit* manueller Prüfung, keine automatische.
- **Hochrechnung in V5:**
  - Die Hochrechnung „× 4“ unterstellt, dass Q3 für das ganze Jahr steht. Viele Testfälle beginnen am 01.01.2027, Q3 ist also vermutlich ein Saisonhoch. Das ist nicht prüfbar ohne Populationszahlen anderer Quartale.
  - Die Stichprobe hat höchstens 2 Fälle je Auftraggeber, die Hochrechnung bezieht sich aber auf alle 492 Verfahren. Große Auftraggeber mit vielen Geschwisterverfahren, bei denen die Regel am häufigsten danebenliegt, sind damit unterrepräsentiert.
- **Entwicklungsdaten wirkten viel besser als der Test.** Auf den Entwicklungsdaten hielt Claude „etwa 10–11 von 12“ Vorschlägen für plausibel (regel_entwicklung_iteration3.md, Lauf 3), ohne Handsuche als Vergleich. Im Test sind es 11/24. Die Bewertung der Entwicklungsdaten war also deutlich zu optimistisch, wie der Report selbst einräumt.

**Gering**

- Die Urteile des Nutzers hat Claude „kompakt übertragen“ (`blindpruefung_iteration3_nutzer.md` Z. 3–4). Das Original „pruefung_auftraege_md.md“ liegt nicht im Repo. Die Übertragung ist deshalb nicht prüfbar.
- Die Kategorien selbst sind nur zu 70 % stabil. Nutzer und Agent stimmen bei objektgleich/teilmenge in 14 von 20 Paaren überein (abweichend: P14, P17, P20, P21, P22, P28; eigene Rechnung). Die getrennte Ausweisung der Teilmengen in V1 ist deshalb unzuverlässig.
- V4 prüft keinen einzigen „kein_vorgaenger“-Fall der Handsuche (14 Fälle). Ob die Handsuche Vorgänger übersehen hat, bleibt offen. Das würde V1 eher unterschätzen.
- In iterationen.md stehen „Ergebnis: offen“ und „Entscheidung: offen“. Die Ergebnisse sind dort und in `docs/phasen/02_data_understanding.md` noch nicht eingetragen. Das ist kein Widerspruch, aber unvollständig.

## V2/V3: Fehlertypen (eigene Auszählung aus zuordnung_iteration3.md und zuordnung_iteration3_urteile.csv)

- **Falsche Vorschläge (11):**
  - 9 sind **Geschwisterverfahren desselben Auftraggebers**: T1, T7, T8, T21, T23, T24, T43, T46, T58.
  - 2 betreffen **dasselbe Objekt mit anderer Leistungsart**: T31 (Baureinigung), T54 (Unterhalts- statt Glasreinigung).
  - **Alle 11 falschen Vorschläge sind Notices aus 2025/2026.**
  - Unklar sind zusätzlich T36 (2026) und T60.
- **Nach Stufe:** B 6 von 14 korrekt, A 3 von 6, T 2 von 4 (eigene Rechnung).
- **Trefferquote:** Von den 38 gefundenen Fällen gibt die Regel bei 19 gar keinen Vorschlag ab, bei 8 einen falschen oder unklaren. Laut Handsuche hängen die meisten Vorgänger an Bekanntmachungen vor eForms, die in den lokalen Rohdaten weder Titel noch Ort haben. Gefunden wurden sie nur über die Volltextsuche `FT` und die XML (teil1 Z. 359–361, teil2 Z. 381–382). Die schwache Trefferquote liegt also wahrscheinlich eher am Datenzugang und an der Merkmalsextraktion als an der Vergleichslogik.
- **Warnung, nur nachträglich beobachtet und ausdrücklich kein Ergebnis:** Ein Ausschluss von Kandidaten jünger als etwa 12 Monate hätte alle 11 falschen Vorschläge entfernt. Er hätte aber genau die korrekten Paare T18, T26 und T32 gekostet, darunter **beide vorzeitigen Neuvergaben**. Ein solches Zeitfenster würde A16 in die Regel einbauen und den Backtest zirkulär machen. Davor warnt urteilsregeln_blindpruefung.md, „Hinweise für Phase 3“, selbst.
- **Ist ein letzter Verbesserungsversuch realistisch?** Er braucht drei Dinge:
  1. Objekt- und Leistungsart-Merkmale auf Los-Ebene, auch für Bekanntmachungen vor eForms (XML bzw. `FT`).
  2. Eine harte Prüfung der Leistungsart.
  3. Eine Trennung von Geschwisterverfahren über Objektlisten und Flächen statt über Stufe-C-Merkmale.

  Methodisch sauber geht das nur so:
  - Q3 2026 wird jetzt Entwicklungsdatum.
  - **Neue Testdaten aus einem unbenutzten Zeitraum**, z. B. Q1 2026 oder Q4 2025. Q4 2026 ist erst nach dem 31.12. vollständig.
  - Die Handsuche läuft *vor* dem Regel-Lauf unter den bereits committeten Regeln V1.1.
  - V4 wird mit frischen Paaren wiederholt, ohne vorheriges Ansehen.
  - Ein Abbruchkriterium wird vorab festgelegt.
  - Zum Stichprobenumfang: Für 80 % Präzision mit Wilson-Untergrenze ≥ 60 % braucht es mindestens etwa 25 Vorschläge (20/25 → Untergrenze 60,9 %; eigene Rechnung). Bei rund 40 % Vorschlagsquote sind das etwa 60–70 Testfälle.

## Alternative Erklärungen

- **V4 = 85 %** kann ebenso bedeuten, dass sich Nutzer und Regeln an denselben Paaren aufeinander eingestellt haben. Das ist kein Beleg für eindeutige Definitionen. Dafür spricht, dass der erste, regelfreie Eindruck („alle passen“) stark abwich.
- **P16 (T33)** muss kein Fehler im Schlüssel sein. Claude hat den Zuschlag 582425-2019 über das zugehörige Verfahren 250469-2019 bewertet (urteile.csv). Der Nutzer durfte nur die beiden Texte des Paares öffnen (Spielregel 2), und im Zuschlagstext steht das Kundenzentrum nicht namentlich. Die Abweichung kann also eine Folge des Prüfverfahrens sein.
- **V1 = 63 %** kann auch eine großzügige Auslegung abbilden: Teilmenge ab einem gemeinsamen Objekt, „mittel“ ohne Objektnamen. Eine echte Sichtbarkeit dieser Größe ist damit nicht gezeigt. Unter V1.1 und nur mit objektgleich läge V1 bei etwa 48 %.
- **Geringe Trefferquote:** Das Verfahren ist nicht unbedingt ungeeignet. Die Merkmale fehlen vor eForms in den Rohdaten (siehe oben).
- **2/36 vorzeitig** passt auch zu einer Auswahlverzerrung. Gezählt werden nur Paare, bei denen Neuausschreibung *und* Vorgänger auf TED sichtbar sind. Außerdem misst die Definition nur gegen die Grundlaufzeit. Neuvergaben vor dem Höchstende kommen häufiger vor: mindestens T6, T11, T21, T30, T48, T57 (teil1 Z. 376, teil2 Z. 169 und 336, teil4 Z. 102 und 282). Iteration 2 hatte 3 von 6 vorzeitig, mit anderer Auswahl über den Auftraggeber. Die beiden Werte lassen sich nicht vergleichen.
- **V6:** 3 Fälle „nur Dauer“ ließen sich mit dem Zuschlagsdatum näherungsweise bestimmen (dann 28/30). Umgekehrt sind alle Enddaten *geplante* Daten der Ausschreibung, nicht tatsächliche Vertragsenden.

## Fakten vs. Interpretation

- `reports/zuordnung_iteration3.md`, Spalte „Status“: „korrekt (Einzelurteil)“ und „falsch (Einzelurteil)“ sind Urteile von Claude, werden aber in der Kennzahl wie Ground Truth gezählt. P16 zeigt, dass mindestens ein solches Urteil strittig ist.
- `reports/zuordnung_iteration3.md`, Spalte „Vorgänger-Ende“: T26 2031-10-31 und T56 2023-12-31 stehen da wie Fakten, sind als Vertragsende aber falsch bzw. unbekannt (siehe oben).
- `reports/sichtbarkeit_iteration3_teil4.md`, „Kategorien (Fakten aus dem Protokoll)“: Die Kategorien sind Einstufungen nach Auslegung, keine Fakten. Teil 2 und Teil 4 ergänzen die Auslegung während der Messung.
- `reports/a11_stichprobe.md`: „Laufzeitende … bestimmbar“ meint das geplante Ende der Grundlaufzeit der referenzierten Ausschreibung, erstes Los. Das steht nur indirekt da.
- `docs/iterationen.md`, Nachtrag V4: „wird … als Hinweis auf eine zu unscharfe Ausgangsdefinition berichtet“ ist eine Interpretation. Sie ist als Plan formuliert und daher vertretbar, muss im Ergebnis aber getrennt stehen.
- Gut getrennt sind: „Einschätzungen (keine Fakten)“ in teil1–4 und die Einschätzung in regel_entwicklung_iteration3.md.

## Betroffene Annahmen (Vorschläge für docs/annahmen.md)

- **A3:** bleibt **ungeprüft**, Nachweis ergänzen.
  - Fakten: Unter Q3-2026-Ausschreibungen (Haupt-CPV 90910/90911/90919, DEU, n = 60, höchstens 2 je Auftraggeber) haben 38/60 = 63,3 % einen objektgleichen *oder teilmengengleichen* Vorgänger auf TED (Wilson 50,7–74,4), nur objektgleich 29/60 = 48,3 %. Bei ≥ 10 der 38 fehlt das Glied direkt davor auf TED (Lücke).
  - Geltungsbereich: Sichtbarkeit unter Ausschreibungen, die bereits auf TED stehen. Der Marktanteil ist nicht gemessen. Definition des Rechercheurs, nicht V1.1.
- **A9b:** **widerlegt (Variante: eingefrorene Regel, Commit 4497743)**, analog zu A9.
  - V2 11/24 = 45,8 % (27,9–64,9), V3 11/38 = 28,9 %. Hauptursachen: Geschwisterverfahren desselben Auftraggebers (9/11 Fehler) und fehlende Merkmale vor eForms.
  - Die allgemeine Annahme (Zuordnung über das Objekt ist grundsätzlich möglich) bleibt **ungeprüft** bis zum letzten Versuch auf neuen Testdaten. Gegebenenfalls als A9c führen.
- **A11:** **ungeprüft → bestätigt (enger Geltungsbereich)**, oder vorsichtiger: „vorläufig gestützt“ beibehalten, weil die Untergrenze bei 66 % liegt.
  - Fakten: V6 25/30 = 83,3 % (Wilson 66,4–92,7), Schwelle 80 % vorab (a11_stichprobe.md). 2 Zuschläge ohne `REF_NOTICE`, 3 mit nur Dauer.
  - Geltungsbereich: Zuschläge mit Haupt-CPV 909 (gesamt, nicht eng), DEU, veröffentlicht 01.01.2018–24.10.2023, F03/F06. Laufzeit = *geplante* Grundlaufzeit des ersten Loses der referenzierten Ausschreibung. Ausdrücklich **nicht** abgedeckt: 2016–2017, tatsächliche Vertragsenden, gezogene Verlängerungen.
- **A16:** bleibt **ungeprüft**, mit Gegenbeleg zum Warnsignal aus Iteration 2.
  - Fakten: Vorzeitig nach Definition (Beginn ≥ 3 Monate vor Ende der Grundlaufzeit) sind 2/36 = 5,6 % (Wilson 1,5–18,1; T18 Lose 8/9, T32). Neuvergabe nach der Grundlaufzeit, aber vor dem Höchstende bei mindestens 6 Paaren (T6, T11, T21, T30, T48, T57).
  - Geltungsbereich: Paare aus der Handsuche in Q3 2026, geplante Enddaten. Die zweite Hälfte der Annahme („zum regulären Vertragsende“) ist wegen der Lücken und der unbekannten Verlängerungen nicht belegt. Eine Bestätigung wäre deshalb verfrüht.
- **A8:** bleibt **ungeprüft**. Die Vorlaufzeit (Abstand zwischen neuer Ausschreibung und Vorgänger-Ende) wurde in Iteration 3 nicht ausgewertet. Als Hinweis eintragen: Bei einem Teil der Paare schließt der neue Vertrag nahtlos an, bei ≥ 10 von 38 klafft eine Lücke. Offen ist, auf welches Ende sich die Prognose bezieht (Grundlaufzeit oder Höchstende).
- **A10:** bleibt **ungeprüft, Warnsignal ergänzen.**
  - Fakten: Nur etwa 5 der 38 gefundenen Vorgänger sind eForms-Verträge (T18, T32, T36, T48, T53; eigene Auszählung aus teil1–4). Unter den 10 V5-Paaren sind es 3–4, hochgerechnet ≈ 98–131/Jahr.
  - Interpretation: Ein Backtest nur mit eForms-Daten läge an oder unter der Grenze von V5. A11-Daten werden praktisch nötig.
- **A12:** bleibt **ungeprüft**, Nachweis ergänzen.
  - Fakten: Trotz Haupt-CPV-Filter und Stichwortliste ist 1 von 60 Testfällen sachfremd (T16, Bauendreinigung). Die Leistungsart (Unterhalts-, Glas- oder Baureinigung desselben Objekts) entscheidet über „objektgleich“ (T31, T54). Die Abgrenzung muss deshalb auf Los-Ebene über die Leistungsart erfolgen, nicht nur über die Haupt-CPV.

## Welche vorab festgelegte Folge greift

- V4 liegt formal bei ≥ 85 %, also gelten V1–V3.
- V1 ≥ 50 %, aber V2 und V3 sind verfehlt. Damit greift: **„in Phase 2/3 bleiben: ein letzter Verbesserungsversuch der Regel, alternativ Produkt mit manueller Prüfung“.**
- V6 ≥ 80 %: A11 ist nicht widerlegt.
- Die explorative Folge (> 30 % vorzeitig → Phase 1) ist nicht ausgelöst.
- Wichtig: Wäre V4 bei 80 % (eine Abweichung mehr) oder würde V1 nur objektgleich zählen (48,3 %), griffe „Definition schärfen, V1–V3 gelten nicht“ bzw. „V1 30–50 % → Idee anpassen“. An der Aussage zu V2/V3 (Regel unzureichend) ändert das in keinem Fall etwas.

## Was für ein belastbares Urteil fehlt

- Eine Zweitprüfung mit Regeln, die **vor** dem ersten Ansehen feststehen, auf frischen Paaren. Dabei gezielt alle Handsuche-Treffer mit Belegstärke „mittel“ (T4, T10, T11, T21, T30, T40) und eine Stichprobe der „kein_vorgaenger“-Fälle prüfen.
- Eine erneute Einstufung der 38 V1-Fälle nach V1.1, zumindest der 9 Teilmengen und der 6 Fälle mit „mittel“, um V1 unter einer einheitlichen Definition zu kennen.
- Korrigierte Enddaten für V5 (T26, T56, T18) und eine Prüfung der Saisonalität über die Populationsgrößen anderer Quartale.
- Das Original der Nutzerurteile („pruefung_auftraege_md.md“) im Repo.
- Für A16 und A8: Vorlaufzeit und tatsächliches Vertragsende statt geplanter Daten.

## Empfehlung

**In Phase 2/3 bleiben (vorab festgelegte Folge), mit dem ausdrücklichen Vermerk, dass V1 und V4 nur knapp und definitionsabhängig erfüllt sind.** V2 und V3 sind so deutlich verfehlt, dass keine Lesart der Zweifelsfälle sie rettet. Ein letzter Verbesserungsversuch ist nur sinnvoll, wenn er die Merkmale vor eForms erschließt, Geschwisterverfahren über Objektlisten und Flächen trennt (nicht über ein Zeitfenster) und auf neuen, unbenutzten Testdaten mit vorab festgelegter Handsuche und Zweitprüfung nach V1.1 gemessen wird. Parallel sollte die Alternative „Produkt mit manueller Prüfung“ in Phase 1 bewertet werden: Die Regel liefert dann nur Kandidaten, und die 328/Jahr sind als Obergrenze mit manuellem Aufwand zu lesen. Die Entscheidung trifft der Nutzer.
