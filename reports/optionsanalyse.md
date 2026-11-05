# Optionsanalyse (Paket F, Nachtrag zu Iteration 10)

_Erzeugt mit `src/report/optionsanalyse.py` (liest nur, ändert keine Daten). Eingaben: `data/processed/backtest_paare_iteration5.csv`, `data/processed/x1_paare_iteration5.txt` (die 52 Paare, dieselbe Auswahl wie `src/model/baseline.py`), `reports/backtest_iteration5.md`, `reports/backtest_analysen_iteration5.md`. Nachträgliche, explorative Auswertung; keine Schwelle, keine Änderung an den Iterationen 1 bis 10._

**Ausdrücklich: 52 Paare, Hinweis, kein Beleg für die Aussage der Vergabestelle (gestützt auf ein einziges Gespräch, n = 1).**

## 1. Frage und Aussage der Vergabestelle

- Fakt (Gespräch, `docs/business.md` §8.9, n = 1): „Fast immer [verlängern wir], wenn eine Verlängerungsoption im Vertrag steht.“ Meist 2 Jahre fest plus 1 Jahr Option. Planung etwa 9 Monate vor Vertragsende, Veröffentlichung „meist 3 bis 4 Monate vor Start“.
- Fakt (Iteration 5, `reports/backtest_iteration5.md`): Die Veröffentlichung der Neuausschreibung streut zweigipflig um „Höchstende − 6 Monate“: 20 Paare früher als −3 Monate, 17 später als +3, 15 im Fenster.
- Frage hier: Wo liegt die Veröffentlichung relativ zum Ende der Grundlaufzeit (GL) und zum Höchstende, und passt das zu „fast immer verlängert“?

## 2. Daten und Definitionen

- Fakt: 52 Paare (Vorgänger-Zuschlag → Neuausschreibung); je Paar sind bekannt: Ende der Grundlaufzeit (`gl_ende`), Höchstende (`hoechstende`, mit Herkunft), Veröffentlichungsdatum der Neuausschreibung (`testfall_datum`). Das Zuschlagsdatum des Vorgängers und der Beginn der Neuausschreibung stehen in dieser Datei nicht (die Spalte `beginn` ist der Beginn des Vorgängers). Es wird nur verwendet, was dort steht.
- Monate = Tage / 30,4375 (wie in `src/model/baseline.py`). d = Veröffentlichung − GL-Ende (positiv: nach dem GL-Ende).
- (a) Veröffentlichung < GL-Ende. (b) GL-Ende ≤ Veröffentlichung ≤ Höchstende. (c) Veröffentlichung > Höchstende. Ist das Höchstende unbestimmbar, lassen sich (b) und (c) nicht trennen.
- Gruppen nach Datenlage im Vorgänger (nicht nach tatsächlichem Vertragsverlauf):
  - G1 Höchstende bekannt, Option belegt (Höchstende > GL-Ende): n = 24.
  - G2 Höchstende = GL-Ende, ausdrücklich „keine Verlängerung“: n = 10.
  - G3 Höchstende = GL-Ende, Herkunft „keine_angabe“ oder „enddatum_ist_hoechstende“ (Option unklar): n = 5.
  - G4 Höchstende unbestimmbar: n = 13.
- Wilson-Intervalle: 95 %, in Klammern in Prozent. Nenner steht immer dabei.

## 3. Fakten: Lage der Neuausschreibung

Anteile mit Nenner und Wilson-Intervall (95 %); Rechenweg: Zahl der Paare in der Lage / Zahl der Paare der Gruppe.

| Gruppe | n | (a) vor GL-Ende | (b) GL-Ende bis Höchstende | (c) nach Höchstende | ab GL-Ende (b und c nicht trennbar) |
|---|---|---|---|---|---|
| alle 52 Paare | 52 | 19/52 = 36,5 % (24,8–50,1) | 17/52 = 32,7 % (21,5–46,2) | 7/52 = 13,5 % (6,7–25,3) | 9/52 = 17,3 % (9,4–29,7) |
| bekannt, Option belegt | 24 | 6/24 = 25,0 % (12,0–44,9) | 17/24 = 70,8 % (50,8–85,1) | 1/24 = 4,2 % (0,7–20,2) | – |
| bekannt, ohne Option | 10 | 4/10 = 40,0 % (16,8–68,7) | 0/10 = 0,0 % (0,0–27,8) | 6/10 = 60,0 % (31,3–83,2) | – |
| bekannt, Option unklar | 5 | 5/5 = 100,0 % (56,6–100,0) | 0/5 = 0,0 % (0,0–43,4) | 0/5 = 0,0 % (0,0–43,4) | – |
| unbekannt | 13 | 4/13 = 30,8 % (12,7–57,6) | 0/13 = 0,0 % (0,0–22,8) | 0/13 = 0,0 % (0,0–22,8) | 9/13 = 69,2 % (42,4–87,3) |
| Höchstende bekannt (G1–G3) | 39 | 15/39 = 38,5 % (24,9–54,1) | 17/39 = 43,6 % (29,3–59,0) | 7/39 = 17,9 % (9,0–32,7) | – |

- Fakt: Über alle 52 Paare lag die Veröffentlichung in 19/52 = 36,5 % (24,8–50,1) der Fälle vor dem GL-Ende (a) und in 33/52 = 63,5 % (49,9–75,2) ab dem GL-Ende.
- Fakt (G1, Option belegt, n = 24): (a) 6/24 = 25,0 % (12,0–44,9); (b) 17/24 = 70,8 % (50,8–85,1); (c) 1/24 = 4,2 % (0,7–20,2).
- Fakt: Bei den 39 Paaren mit bekanntem Höchstende lag die Veröffentlichung in 32/39 = 82,1 % (67,3–91,0) vor dem Höchstende (bei G2 und G3 ist Höchstende = GL-Ende, dort fällt das mit (a) zusammen).

### Sensitivität: Wie viel Vorlauf wäre bei voll gezogener Option normal?

Eine Veröffentlichung vor dem Höchstende ist noch kein Hinweis auf eine nicht gezogene Option, denn auch bei voll genutzter Option wird vorher ausgeschrieben (Vergabestelle: Planung etwa 9 Monate, Veröffentlichung 3 bis 4 Monate vor Start). Anteil der G1-Paare, die **mehr als V Monate vor dem Höchstende** veröffentlicht wurden (dann spricht mehr für „Option nicht voll genutzt“; V ist hier eine Setzung zur Sensitivität, nicht aus den Paaren geschätzt):

| V (Monate vor Höchstende) | G1: Veröffentlichung früher als Höchstende − V |
|---|---|
| 0 | 23/24 = 95,8 % (79,8–99,3) |
| 3 | 23/24 = 95,8 % (79,8–99,3) |
| 6 | 16/24 = 66,7 % (46,7–82,0) |
| 9 | 13/24 = 54,2 % (35,1–72,1) |
| 12 | 13/24 = 54,2 % (35,1–72,1) |
| 18 | 6/24 = 25,0 % (12,0–44,9) |

## 4. Fakten: Verteilung von d = Veröffentlichung − GL-Ende (Monate)

Zahl der Paare je Klasse (Klasse unten ≤ d < oben):

| Gruppe | n | < −24 | −24 bis −12 | −12 bis −6 | −6 bis 0 | 0 bis 6 | 6 bis 12 | 12 bis 24 | 24 bis 48 | ≥ 48 |
|---|---|---|---|---|---|---|---|---|---|---|
| alle 52 Paare | 52 | 4 | 4 | 2 | 9 | 1 | 10 | 8 | 7 | 7 |
| bekannt, Option belegt | 24 | 0 | 1 | 2 | 3 | 0 | 7 | 7 | 2 | 2 |
| bekannt, ohne Option | 10 | 0 | 0 | 0 | 4 | 1 | 1 | 1 | 1 | 2 |
| bekannt, Option unklar | 5 | 2 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| unbekannt | 13 | 2 | 1 | 0 | 1 | 0 | 2 | 0 | 4 | 3 |
| Höchstende bekannt (G1–G3) | 39 | 2 | 3 | 2 | 8 | 1 | 8 | 8 | 3 | 4 |
| mit belegter Option (G1) | 24 | 0 | 1 | 2 | 3 | 0 | 7 | 7 | 2 | 2 |
| ohne belegte Option (G2+G3+G4) | 28 | 4 | 3 | 0 | 6 | 1 | 3 | 1 | 5 | 5 |

Textbalken, alle 52 Paare (je # ein Paar):

```
       < −24 | #### 4
 −24 bis −12 | #### 4
  −12 bis −6 | ## 2
    −6 bis 0 | ######### 9
     0 bis 6 | # 1
    6 bis 12 | ########## 10
   12 bis 24 | ######## 8
   24 bis 48 | ####### 7
        ≥ 48 | ####### 7
```

Textbalken, G1 (Option belegt):

```
       < −24 |  0
 −24 bis −12 | # 1
  −12 bis −6 | ## 2
    −6 bis 0 | ### 3
     0 bis 6 |  0
    6 bis 12 | ####### 7
   12 bis 24 | ####### 7
   24 bis 48 | ## 2
        ≥ 48 | ## 2
```

Textbalken, G2+G3+G4 (keine belegte Option):

```
       < −24 | #### 4
 −24 bis −12 | ### 3
  −12 bis −6 |  0
    −6 bis 0 | ###### 6
     0 bis 6 | # 1
    6 bis 12 | ### 3
   12 bis 24 | # 1
   24 bis 48 | ##### 5
        ≥ 48 | ##### 5
```

- Fakt: Median d: alle 52 Paare 8,0 Monate; G1 10,8; G2 6,5; G3 -20,7; G4 31,4.
- Fakt: In G1 liegt d zwischen -16,2 und 66,5 Monaten; in G4 (Höchstende unbestimmbar) zwischen -44,4 und 89,0.

Zum Vergleich: Abstand Veröffentlichung − **Höchstende** (dh, nur G1 bis G3, in Monaten):

| Gruppe | n | < −24 | −24 bis −12 | −12 bis −6 | −6 bis −3 | −3 bis 0 | 0 bis 12 | ≥ 12 |
|---|---|---|---|---|---|---|---|---|
| alle 52 Paare | 39 | 8 | 9 | 3 | 11 | 1 | 2 | 5 |
| bekannt, Option belegt | 24 | 6 | 7 | 3 | 7 | 0 | 0 | 1 |
| bekannt, ohne Option | 10 | 0 | 0 | 0 | 3 | 1 | 2 | 4 |
| bekannt, Option unklar | 5 | 2 | 2 | 0 | 1 | 0 | 0 | 0 |
| unbekannt | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Höchstende bekannt (G1–G3) | 39 | 8 | 9 | 3 | 11 | 1 | 2 | 5 |
| mit belegter Option (G1) | 24 | 6 | 7 | 3 | 7 | 0 | 0 | 1 |
| ohne belegte Option (G2+G3+G4) | 15 | 2 | 2 | 0 | 4 | 1 | 2 | 4 |

(Die Zeilen G4 und „ohne belegte Option“ enthalten hier nur Paare mit bekanntem Höchstende; G4 ist leer.)

## 5. Fakten: Vorlauf

Vorlauf = Vertragsende − Veröffentlichung der Neuausschreibung (Monate; positiv: vor dem Ende veröffentlicht; negativ: nach dem Ende). Vertragsende = Höchstende, wenn bekannt, sonst GL-Ende. Der Beginn des Folgevertrags steht nicht in den Daten; „3 bis 4 Monate vor Start“ lässt sich deshalb nur näherungsweise (Start ≈ Vertragsende des Vorgängers) prüfen.

| Menge | n | < 0 (nach Ende) | 0 bis 3 | 3 bis 6 | 6 bis 9 | 9 bis 12 | 12 bis 24 | ≥ 24 | Median |
|---|---|---|---|---|---|---|---|---|---|
| alle 52 Paare (Vertragsende = Höchstende, sonst GL-Ende) | 52 | 16 | 1 | 12 | 3 | 0 | 10 | 10 | 5,5 |
| G1 Option belegt, bezogen auf Höchstende | 24 | 1 | 0 | 7 | 3 | 0 | 7 | 6 | 14,1 |
| G2 ohne Option | 10 | 6 | 1 | 3 | 0 | 0 | 0 | 0 | -6,5 |
| G3 Option unklar | 5 | 0 | 0 | 1 | 0 | 0 | 2 | 2 | 20,7 |
| G4 Höchstende unbekannt (GL-Ende) | 13 | 9 | 0 | 1 | 0 | 0 | 1 | 2 | -31,4 |

- Fakt: Vorlauf zwischen 2,5 und 4,5 Monaten („3 bis 4 Monate“ der Vergabestelle, grob): 5/52 = 9,6 % (4,2–20,6). Vorlauf 0 bis 12 Monate: 16/52 = 30,8 % (19,9–44,3). Veröffentlichung erst nach dem Vertragsende (Vorlauf < 0): 16/52 = 30,8 % (19,9–44,3).
- Fakt (G1): Vorlauf zum Höchstende 0 bis 12 Monate bei 10/24 = 41,7 % (24,5–61,2); Median 14,1 Monate.
- Fakt: Median des Vorlaufs zum Vertragsende (alle Paare) 5,5 Monate; zum GL-Ende (alle Paare) -8,0 Monate.

## 6. Deutung (getrennt von den Fakten)

1. **Zweigipfligkeit.** Ein Teil der Neuausschreibungen kommt vor dem GL-Ende, ein anderer deutlich danach (siehe Textbalken). Das passt zu zwei Fällen: Verträge ohne gezogene Option (kurzer Vorlauf vor dem GL-Ende) und Verträge mit gezogener Option (Veröffentlichung nach dem GL-Ende). Die Daten trennen diese Fälle nicht, weil die tatsächliche Ausübung der Option in keiner Bekanntmachung der Paare steht.
2. **Option belegt (G1, n = 24).** 17 von 24 Veröffentlichungen liegen zwischen GL-Ende und Höchstende, nur 6 vor dem GL-Ende und 1 nach dem Höchstende. Das ist mit „Option wird in der Regel gezogen, ausgeschrieben wird gegen Ende der Optionszeit“ vereinbar. Es ist aber auch mit anderen Vorgängen vereinbar (Übergangsverlängerung, vorzeitige Ausschreibung vor Ablauf der Option, eine Option, die nur teilweise genutzt wurde). Wie viel davon „Option gezogen“ ist, lässt sich aus den Daten nicht sagen.
3. **Vorlauf.** Der Vorlauf streut breit; der Wert „3 bis 4 Monate vor Start“ ist nur ein Teil der Fälle (siehe oben). Die Angabe „Planung 9 Monate vorher“ betrifft interne Arbeit und ist an einer Veröffentlichung nicht ablesbar. Ein Vorlauf von mehreren Monaten ist mit einer voll genutzten Option verträglich; wo die Veröffentlichung 12 Monate und mehr vor dem Höchstende liegt (Sensitivitätstabelle), spricht mehr für eine nicht voll genutzte Option oder eine Zuordnung, die nicht das gleiche Los trifft.
4. **Zeitpunkt relativ zum Höchstende (G1).** Läge bei jedem Vertrag mit Option die Option voll bis zum Höchstende, wäre bei „Veröffentlichung 3 bis 4 Monate vor Start“ ein Vorlauf zum Höchstende von etwa 3 bis 6 Monaten zu erwarten. Tatsächlich liegen 16/24 = 66,7 % (46,7–82,0) der G1-Veröffentlichungen mehr als 6 Monate vor dem Höchstende. Das ist ein Hinweis, dass bei den später doch neu ausgeschriebenen Verträgen mit Option die Option oft nicht bis zum Ende lief (oder nur teilweise gezogen wurde, z. B. 2 Jahre fest plus 1 Jahr Option, davon nur ein Teil); es ist kein Beleg, weil Höchstende und GL-Ende vor eForms teils aus Freitext stammen und die Auswahl nur Neuausschreibungen enthält.
5. **Lange Lücken nach dem Ende** (G2 und G4 mit d über 24 Monaten): Die Analysen der Iteration 5 (`reports/backtest_analysen_iteration5.md`, 12 Paare mit Lücke über 24 Monaten) belegen keinen Zwischenvertrag; es sind mehrere Erklärungen möglich (nicht in der Bekanntmachung stehende Verlängerung, Zwischenvertrag, falsche Zuordnung). Bei G4 fehlt das Höchstende, ein spätes d ist dort deshalb nicht auswertbar.

## 7. Grenzen

- **Nur Neuausschreibungen sind erfasst.** Die Paare entstanden durch Rückwärtssuche vom Testfall (Neuausschreibung 2026) zum auffindbaren Vorgänger. Verträge, die verlängert wurden und (noch) nicht neu ausgeschrieben sind, fehlen vollständig. Für „fast immer verlängert, wenn Option vorhanden“ wäre der Nenner alle Verträge mit Option am Ende der Grundlaufzeit; der steht in den Daten nicht (Überlebens- bzw. Auswahlverzerrung).
- **Kleine Zahlen.** 52 Paare, davon nur 24 mit belegter Option; die Wilson-Intervalle sind breit (oft über 30 Prozentpunkte).
- **Zeitfenster der Testfälle:** Neuausschreibungen aus Q1 und Q3 2026 (Iteration 4 und 3); Verträge, deren Option bis nach 2026 läuft, können nur vorzeitig ausgeschrieben worden sein (Rechtszensierung zugunsten von (a)/(b)).
- **Datenherkunft der Enden:** 41 von 52 Vorgängern liegen vor eForms (XML), 11 im eForms-Format; (in der Rohdatei mit 68 Vorgängern sind es 55 vor eForms, 13 eForms). Das Höchstende ist vor eForms nur teilweise und aus Freitext bestimmbar (Herkunft `datum_text`, `anzahl_x_laenge`, `hoechstlaufzeit_text`); bei `enddatum_ist_hoechstende` (n = 4) ist das GL-Ende selbst unsicher.
- **Zuordnung und Prüfung:** 37 Paare „objektgleich“, 15 „Teilmenge“ laut Handsuche; die Ground Truth ist nicht unabhängig bestätigt (A18); die Zweitprüfung war KI-gestützt (`docs/ki_irrwege.md`, `reports/gt_pruefung_iteration5_auswertung.md`).
- **Veröffentlichungsdatum ist nicht Vergabestart.** Der Beginn der Neuausschreibung steht nicht in den Daten; „Vorlauf zum Vertragsende“ ist eine Näherung für „Vorlauf zum Start“.
- **Eine Quelle für die Aussage** (n = 1, eine Vergabestelle). Gespräche sind Hinweise, keine Stichprobe.
- **Auftraggeber-Cluster:** 52 Paare, 40 Auftraggeber, 6 mit mehr als einem Paar (`reports/backtest_analysen_iteration5.md`); die Paare sind nicht unabhängig.
- **Nicht auswertbar:** Wie oft eine Option tatsächlich gezogen wurde; Verlängerung ohne Neuausschreibung; Dauer der Verlängerung.

## 8. Urteil zur Aussage „fast immer verlängert“

**Die Daten können die Aussage „fast immer verlängert“ nicht prüfen** (kein Beleg dafür und keiner dagegen). Begründung: Die 52 Paare sind per Konstruktion Verträge, die neu ausgeschrieben wurden; eine Quote „verlängert / nicht verlängert“ braucht auch die Verträge, die verlängert und (noch) nicht neu ausgeschrieben wurden. Als schwache Nebenbeobachtung: Bei den 24 Paaren mit belegter Option wurde 18/24 = 75,0 % (55,1–88,0) ab dem GL-Ende veröffentlicht (mit Verlängerung vereinbar), aber 16/24 = 66,7 % (46,7–82,0) mehr als 6 Monate vor dem Höchstende (spricht eher gegen „Option wird bis zum Höchstende ausgeschöpft“, ohne die Aussage zu widerlegen, denn eine Verlängerung um nur einen Teil der Option bleibt möglich). Belastbar prüfen ließe sich die Aussage nur mit einer Vorwärtsbetrachtung (alle Verträge mit Option, deren Grundlaufzeit endete, und was danach geschah) und mehr als einer Vergabestelle.

