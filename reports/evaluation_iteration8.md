# Evaluation Iteration 8 (Subagent `evaluator`, 2026-11-05)

_Bericht des Evaluators, ungekürzt übernommen. Der Abschnitt „Nachprüfung durch Claude und Entscheidung“ am Ende stammt von Claude und vom Nutzer._

## Gesamtprüfung Schritt 4 (KI-Zweitlesung)

**Formal sind alle fünf Kriterien erfüllt. Inhaltlich trägt das Ergebnis weniger, als die Zahlen nahelegen.**
- Die Übereinstimmung der Leser (Z0) und die Kontrolle (Z4) messen vor allem, wie einheitlich dasselbe Verfahren liest, nicht, ob es richtig liest.
- Z2 (14/15) hängt an einer Rechenkonvention, die die Vorlage den Lesern ausdrücklich vorgegeben hat. Wendet man den Maßstab, den der Evaluator bei L7 angelegt hat, gleich auf alle betroffenen Lose an, sind es 11/15. Die Schwelle (12) wäre dann verfehlt.
- Neu gefunden habe ich zwei Fehlerarten der Liste, die keines der Kriterien erfasst:
  - Lose ohne Zuschlag stehen in der Liste (L69, L72).
  - Ein Wert von Los 1 wird auf andere Lose übertragen (L81).

**Was ich selbst geprüft habe**
- Alle Zahlen von Z0 bis Z3 und den Dreiervergleich habe ich Los für Los aus beiden Leser-CSV-Dateien und dem Schlüssel nachgerechnet.
- 12 Bekanntmachungen mit 16 Losen habe ich an der HTML-Fassung bei TED angesehen. Einschränkung: Ich habe dafür dasselbe WebFetch-Hilfsmodell benutzt wie die Leser und gehöre zur selben Modellfamilie. Meine Kontrolle ist also nicht unabhängig.
- Die Rohdaten der API zu L81 habe ich in `data/raw/.../page_0017.json` gelesen.
- Nicht prüfbar: Python-Ausführung (Seed-Ziehung für Z4, Prüfung des Schlüssel-Hashes) und die Inhalte älterer Commits.

### Urteil je Kriterium

| Kriterium | Urteil | Beleg (Quelle) |
|---|---|---|
| Verfahren (vorab, blind, getrennt, nur Format korrigiert) | **teilweise erfüllt** | `.git/logs/HEAD` Z. 83–86: Kriterien und Vorlage (6fe4e38), dann Auswertungsskript (9645fa8, 5:18 min später), dann Antworten (74f95d0, weitere 5:30 min), dann Entscheide (3e9178b). Die Reihenfolge stimmt. Ob das Skript vor dem *Start* der Leser committet war, lässt sich nicht prüfen; laut Plan war nur „vor den Antworten“ verlangt. Die Formatkorrektur betrifft nur Leser B und nur Semikolons im Zitat (Grep in `zweitlesung_iteration8_roh/`: 70 Zeilen, alle `leser_b_*`); die Felder 1–3 und das letzte Feld sind unverändert. Die Vorlage enthält keine Listenwerte. **Aber:** Die Vorlage gibt Regel 1b als Leseanweisung vor (siehe Schwächen). Der genaue Auftragstext an die Leser ist nicht im Repository abgelegt. |
| Z0 Leser A = B beim Ende der Grundlaufzeit ≥ 90 % | **erfüllt** (94/95 nachgerechnet; einzige Uneinigkeit L7). Aussagekraft begrenzt | Leser-CSV-Dateien. Das Höchstende ist ebenfalls bei 94/95 einig (nur L33 uneinig) |
| Z1 Liste = Vergleichswert ≥ 72/80 | **erfüllt** (77/80 nachgerechnet) | Abweichungen L5, L33, L81. L5 und L81 habe ich am Original als echte Listenfehler bestätigt. Bei L33 widerspricht sich die Quelle selbst |
| Z2 Regelwirkungs-Lose ≥ 12/15 | **formal erfüllt (14/15), inhaltlich nur teilweise** | Mit einheitlichem Maßstab 11/15. 8 der 15 Lose stammen von einem einzigen Auftraggeber (Landkreis Börde) |
| Z3 ≥ 90 % / ≥ 85 % | **erfüllt** (75/80 und 67/72 nachgerechnet) | Ohne die Regel „Liste unbestimmbar = korrekt“ wären es 69/80 = 86,3 %, also unter 90 % (siehe unten) |
| Z4 ≥ 9/10 vom Evaluator bestätigt | **formal erfüllt (10/10), schwach belegt** | `zweitlesung_iteration8_z4.csv`. Wilson-Untergrenze bei 10/10 etwa 72 %. Der Evaluator kannte die Werte der Leser und benutzte dasselbe Hilfsmodell. 9 der 10 Lose sind einfache Fälle mit Enddatum-Feld, keines gehört zur Problemgruppe „Schuljahr“ |

### Abweichungen am TED-Original (Frage 4)

| Los | Bekanntmachung | Befund am Original | Einordnung |
|---|---|---|---|
| L5 | 538350-2026 LOT-0003 | Beginn 01/09/2026, „Enddatum der Laufzeit: 31/08/2031“, „3 Jahre mit Option für eine zweimalige Verlängerung von je einem Jahr“, Max. Verlängerungen 2 | **Echter Listenfehler**, genau der Typ „Enddatum ist schon Höchstende“. Regel 1b greift nicht, weil „3 Jahre mit Option“ kein Schlüsselwort wie „Laufzeit“ oder „Vertragsdauer“ vor der Dauer hat (`RE_BASIS_DAUER` in `vertragsliste.py`). Das Höchstende 2033 ist dadurch ebenfalls falsch |
| L33 | 112593-2026 | Ende 31/03/2030, aber „zunächst für eine Vertragslaufzeit von drei Jahren“, „zweimaligen Verlängerung um je ein Jahr“, „maximale Vertragslaufzeit beträgt 7 Jahre“ | **Die Quelle widerspricht sich.** Nach der Definition „erste feste Laufzeit“ ist 31.03.2029 wahrscheinlicher, die Liste folgt dem Feld. Eher Listenfehler, aber nicht belegbar. Das Höchstende ist zu Recht „unklar“ |
| L81 | 10154-2026 LOT-0002 | Los 2 hat weder Beginn noch Ende, nur „2 Jahre“ und 2 × 12 Monate. Los 1 hat 01/12/2025 bis 30/11/2027 | **Echter Listenfehler durch falsche Los-Zuordnung.** In den Rohdaten (`page_0017.json`) hat die Bekanntmachung zwei Lostitel, aber `contract-duration-end-date-lot":["2027-11-30…"]` mit nur **einem** Wert. Regel 6 („kürzer und alle Werte gleich → gilt für alle Lose“) überträgt dann den Wert von Los 1 auf Los 2. Ein einzelner Wert gilt dabei immer als „alle gleich“. Der Fehler ist also systematisch, kein Einzelfall. Wie oft er vorkommt, ist nicht gezählt |
| L72 | 557125-2026 LOT-0001 | „maximal um 3 Jahre stillschweigend verlängert … spätestens am 31.08.2031“. **„Es wurde kein Wettbewerbsgewinner ermittelt“** (21 Angebote, Gewinner nur in LOT-0002) | Doppelter Fehler: (1) Das Höchstende 2037 entsteht, weil „um 3 Jahre“ als Länge je Verlängerung gelesen und mit 3 (Feld BT-58) multipliziert wird. (2) **Für das Los gibt es gar keinen Vertrag.** Leser B hat das gemeldet (`hinweise.md`, B Teil 3). Weder Auswertung noch Evaluator (Z4: „Höchstende stimmt“) haben es aufgegriffen |
| L69 | 506823-2026 | „kein Wettbewerbsgewinner … keine Angebote“, „Anzahl der eingegangenen Angebote: 0“ | Ebenfalls ein Los ohne Vertrag. In Z1 und Z3 zählt es als „korrekt“ |
| L82 | 707425-2025 | „36 Monate“ ab 01/11/2025, Max. Verlängerungen 1, „jeweils um ein weiteres Jahr“, „endet jedoch spätestens mit Ablauf des 31. Oktober 2030“ | Wahrscheinlich ein Listenfehler. Die Quelle ist widersprüchlich (1 Verlängerung gegen ausdrückliches Ende 2030), aber das ausdrücklich genannte späteste Ende ist maßgeblich. Die Liste verpasst das Datum, weil `RE_DATUM` nur Daten wie „31.10.2030“ erkennt, nicht „31. Oktober 2030“ |
| L74, L84 | 267775-2025 | Feld 22/07/2029, Text „spätestes Vertragsende ist der 20.07.2029“ | Feld und Text widersprechen sich um 2 Tage. Kein inhaltlicher Listenfehler. Zählt nicht für Z3, weil es Typ-R-Lose sind |

### Weitere Übereinstimmungen am Original (Frage 5)

- **Eindeutig richtig** (Liste und Leser stimmen, der Text nennt die Grunddauer ausdrücklich):
  - L73/L77 (574881-2025): „Vertragsdauer von 3 Jahren (01.09.2025 bis 31.08.2028)“ plus 2 × 12 Monate, das Feld 31/08/2030 ist das Höchstende.
  - L3 (108370-2024): „Laufzeit von 12 Monaten“ plus 3 × 12 Monate, Feld 31/12/2027.
  - Regel 1b ist hier richtig angewandt.
- **Schuljahres-Muster:** L7, L57 (340183-2026), L74, L84 (267775-2025), L65, L88 (360180-2025), L55, L80 (284267-2024).
  - Alle stammen vom **Landkreis Börde, Zentrale Vergabestelle**.
  - Wortlaut: „ein Jahr zum Schuljahresende“ (L7/L57, L74/L84) bzw. „ein Jahr mit Verlängerungsoption“.
  - Die Bekanntmachungen zeigen selbst, dass der Auftraggeber in Schuljahren rechnet und nicht in Kalenderjahren:
    - 284267-2024: „Vertragsende ist der 21.07.2028 (letzter Schultag vor den Sommerferien)“.
    - Die Höchstenden 12.07.2030 und 20./22.07.2029 sind nicht „Beginn + 4 Jahre − 1 Tag“.
  - Das Ende des ersten Jahres ist also der letzte Schultag vor den Sommerferien des Folgejahres. Dieses Datum nennt keine der Bekanntmachungen tagesgenau.
  - „Beginn + 1 Jahr − 1 Tag“ (29.06.2026 bzw. 03.07.2027) ist eine **gemeinsame Konvention**. Die Vorlage gibt sie wörtlich vor („Ende = Beginn + Dauer − 1 Tag“, `zweitlesung_iteration8_vorlage.md` Z. 10), und die Regel setzt „Schuljahr = 12 Monate“ (`vertragsliste.py`, Regel 3d). Eine unabhängige Bestätigung ist das nicht.
  - Ob das Datum innerhalb von ±1 Tag liegt, ist mit TED allein nicht prüfbar; dafür braucht es den Ferienkalender Sachsen-Anhalt. Ich vermute eine Abweichung von einigen Tagen bis Wochen. Das ist eine Interpretation.
  - Praktisch ist eine solche Abweichung für die Vorbereitung auf eine Neuausschreibung belanglos. Für das vorab gesetzte ±1-Tag-Kriterium ist sie nicht belanglos.

### Schwächen

**Kritisch**
1. **Der Maßstab für Z2 ist uneinheitlich.**
   - Der Evaluator hat L7 als „unklar“ entschieden: „Tagesgenaues Datum fehlt … 03.07.2027 ist gerechnet und übergeht ‚zum Schuljahresende‘“ (`entscheide.csv`).
   - L57 hat denselben Text in derselben Bekanntmachung und zählt trotzdem als richtig, nur weil Leser B dort gerechnet hat und bei L7 nicht. Für L74 und L84 gilt dasselbe.
   - Mit einheitlichem Maßstab ergibt sich **11/15 = 73,3 %, Schwelle verfehlt.** Rechnet man auch L55/L80/L65/L88 als „nicht tagesgenau belegt“, sind es 7/15.
   - Nachträglich umwerten wäre selbst eine Abweichung vom Vorab-Verfahren. Beide Zahlen sollten deshalb nebeneinander berichtet werden.
2. **Vorlage und Regel teilen dieselbe Lesart.**
   - Die Vorlage schreibt den Lesern Regel 1b als Anweisung vor: „Nennt der Text eine kürzere feste Laufzeit als das Enddatum-Feld …, gilt die kürzere“ und „selbst ausrechnen (Ende = Beginn + Dauer − 1 Tag)“.
   - Damit prüft Z2 teilweise, ob die Leser der Anweisung gefolgt sind, und nicht, ob die Regel stimmt.
   - Für die Aussage „Regel 1b gestützt“ ist das ein Zirkelschluss.
3. **Die Leser sind getrennt, aber nicht unabhängig.** Leser, Regel, Vorlage und Evaluator stammen aus derselben Modellfamilie, und alle lesen TED über dasselbe WebFetch-Hilfsmodell. Das Hilfsmodell kürzt und fasst zusammen (Hinweise A2, A3, B1–B4; Evaluator 4a). Folgen:
   - **Z0** misst, wie einheitlich das Verfahren liest. Übersieht das Hilfsmodell eine Optionsklausel, irren beide Leser gleich.
   - **Z4** kann genau diesen Fehler nicht aufdecken; der Evaluator sagt das selbst (`hinweise.md`, Schlussbemerkung). Er prüfte außerdem nicht blind, sondern bestätigte bekannte Werte. Aussagen wie „kommt in der ganzen Bekanntmachung nicht vor“ (Z4, L30) stützen sich allein auf das Hilfsmodell.
   - **Gesamtaussage:** Die Hypothese verlangt „voneinander unabhängige“ Leser. Diese Voraussetzung ist nur eingeschränkt erfüllt.

**Mittel**
4. **Lose ohne Vertrag stehen in der Liste** (L69, L72, am Original bestätigt). `vertragsliste.py` filtert nicht nach dem Ergebnis je Los. Kein Kriterium erfasst das, und die Vorlage hat nicht danach gefragt. Der Anteil ist mindestens 2/95 und wurde nicht gemessen.
5. **Die Los-Zuordnung nach Regel 6 ist systematisch fehleranfällig** (L81). Sie betrifft vermutlich alle Bekanntmachungen, in denen nur ein Teil der Lose Laufzeitfelder hat. Die Abdeckung von 79,7 % kann dadurch leicht zu hoch sein; das Ausmaß ist unbekannt.
6. **Z1 ist zum großen Teil eine Feldabschrift.**
   - Bei 76 der 80 Y-Lose übernimmt die Liste das Enddatum-Feld (Herkunft „enddatum“, Schlüssel).
   - Inhaltlich aussagekräftig ist vor allem, dass die Leser bei 2 dieser 76 Lose (L5, L33) eine kürzere Grunddauer im Text gefunden haben.
   - Ob es weitere solche Fälle gibt, die das Hilfsmodell nicht wiedergegeben hat, bleibt offen.
7. **Z3: „Liste unbestimmbar = korrekt“ zählt mit.**
   - Bei 6 der 8 „unbestimmbar“-Lose fanden beide Leser einen Wert: L4, L19, L48, L83, L91 mit Datum, L40 mit „keine Angabe“.
   - Streng gezählt ergibt Z3a 69/80 = 86,3 % (Schwelle 90 %).
   - Die Regel war vorab festgelegt. Z3b mit 67/72 ist das sauberere Maß und erfüllt.
   - „Unbestimmbar“ bedeutet „nicht falsch“, nicht „korrekt“.
8. **Klumpung.** Die 15 R-Lose stammen aus 9 Bekanntmachungen, 8 davon aus 4 Bekanntmachungen eines Auftraggebers (Börde). L3, L49 und L62 haben wortgleiche Texte, vermutlich ebenfalls ein Auftraggeber (nicht geprüft). Die Wilson-Intervalle unterstellen unabhängige Lose.
9. **Vermutlich vorgeprägter Kontext.** Ich habe als Subagent `CLAUDE.md` automatisch im Kontext erhalten. Dort steht: „Fehlertyp: Das Enddatum der Bekanntmachung ist manchmal schon das Höchstende.“ Wenn das auch für die Leser galt, kannten sie die Richtung der Hypothese, wenn auch keine Listenwerte. Prüfbar ist das in den Subagenten-Protokollen; die liegen nicht im Repository.

**Gering**
10. Der Auftragstext an die Leser und die Protokolle (`agent-*.jsonl`) liegen nicht im Repository. Die Protokollprüfung (nur WebFetch, ToolSearch, Handback; keine Zugriffe auf Projektdateien) ist nur über die Skriptausgabe in `hinweise.md` nachvollziehbar.
11. In `auswertung.md` heißt es „Antworten unverändert“. Genauer wäre „unverändert bis auf Semikolons → Kommas im Zitat (Leser B)“.
12. `docs/iterationen.md` (Iteration 8) hat noch keine Fortschrittsnotizen zu den Schritten 2–4.
13. Leser B war innerhalb seiner Teilläufe uneinheitlich (L7 „unbekannt“ in Teil 1, L57 gerechnet in Teil 3). Die Einigkeit bei den Börde-Losen ist also nicht stabil.

### Alternative Erklärungen
- **Hohe Einigkeit (Z0) und hohes Z2 durch gemeinsame Anweisung und gemeinsames Hilfsmodell** statt durch richtiges Lesen. Beides passt gleich gut zu den Daten.
- **Z1 hoch, weil das Feld meist trivial abzuschreiben ist.** Die schwierige Fehlerart (Enddatum = Höchstende) kommt in Y-Losen selten vor (2/76). Ob sie selten *ist* oder selten *gefunden wird*, lässt sich nicht trennen.
- **Iteration 7, Dreiervergleich:**
  - In allen 11 Abweichungen von Iteration 7 (L16, L18, L24, L25, L26, L27, L30, L31, L32, L38, L44) steht die KI-Lesung auf der Seite der Liste.
  - Bei den 5 Datumsabweichungen ist ein Abschreibfehler des Prüfers die plausibelste Erklärung. Ein Leser, der das HTML-Feld liest, trifft das Feld, und die Liste kommt aus demselben Feld.
  - Bei den 6 „unbekannt“ hat Iteration 7 schlicht nichts gemessen.
  - Bei L5 und L33 folgte der Prüfer dem Feld, die KI der Anweisung „kürzere gilt“. Bei L5 ist der Text eindeutig, bei L33 nicht.
- **L33:** Das Feld 31.03.2030 könnte die gewollte Grundlaufzeit sein, und der Freitext ist veraltet. Belegbar ist keine der beiden Lesarten.

### Fakten vs. Interpretation
- `reports/zweitlesung_iteration8_auswertung.md`: Der Abschnitt „Abweichungen der Liste vom Vergleichswert“ steht unter „Fakten“, und die ✗ legen „Liste falsch“ nahe. Fakt ist nur die Abweichung von einer KI-Lesung. Ob ein Fehler vorliegt, ist Deutung (siehe L33, L74, L84).
- `docs/iterationen.md`, Hypothese: „voneinander unabhängige KI-Leser“ ist eine Annahme über das Verfahren, kein Befund.
- `docs/iterationen.md`, „Was folgt“: „Regel 1b … als gestützt“ geht über die Belege hinaus (Schwächen 1 und 2).
- `zweitlesung_iteration8_z4.csv` (L30): „kommen … nicht vor“ ist eine Aussage des Hilfsmodells. Abwesenheit kann es nicht belegen.
- `zweitlesung_iteration8_hinweise.md`: Die Fakten „L69, L72 kein Zuschlag“ (Leser B, von mir bestätigt) fehlen in Auswertung und Entscheiden.

### Betroffene Annahmen
- **A4:** Status bleibt **bestätigt** (betrifft die Abdeckung). Hinweis ergänzen:
  - Laut zwei KI-Lesungen ist bei 74 von 76 Y-Losen mit Herkunft „enddatum“ das Feld das Ende der Grundlaufzeit (Ausnahmen L5, am Original bestätigt, und L33 mit widersprüchlicher Quelle).
  - Zusätzlich: Regel 6 überträgt Einzelwerte auf andere Lose (L81).
  - Geltungsbereich: eForms, Haupt-CPV 909, KI-Lesung derselben Modellfamilie, nicht von Menschen bestätigt.
- **A13:** Status unverändert; die Abdeckung wurde nicht neu gemessen. Zwei Vorbehalte, Ausmaß unbekannt: Lose ohne Zuschlag (L69, L72) und Regel-6-Übertragungen können die 79,7 % leicht überhöhen.
- **A12:** Status bleibt **ungeprüft**. Die Leser stuften 95/95 als „Gebäudereinigung ja“ ein, aber ungeprüft (Z4 prüft das nicht). Kein Beleg in eine Richtung.
- **A19 (neu):** höchstens **„ungeprüft (vorläufig gestützt)“**, nicht „bestätigt“.
  - Dafür spricht: Z0 94/95. Die Leser fanden echte Listenfehler (L5, L81, L72-Höchstende, L82), die ich am Original bestätigt habe, und klärten die Prüferfehler von Iteration 7 auf.
  - Dagegen spricht: Es gibt keine menschliche Referenz, und Z4 ist nicht unabhängig.
  - Die Leser sind bei gleichem Text uneinheitlich (L7/L57). Leser A hat das fehlende Gewinner-Los nicht gemeldet; Leser B hat es gemeldet, aber nicht als Abweichung eingetragen (danach war allerdings nicht gefragt).
- **Vorschlag neue Annahme:** „Jedes Los einer Zuschlagsbekanntmachung hat einen Vertrag.“ Widerlegt durch 506823-2026 und 557125-2026 LOT-0001. Der Anteil ist nicht gemessen.

### Was für ein belastbares Urteil fehlt
- Eine menschliche Lesung mindestens der Problemgruppen: die 8 Börde-Lose mit Ferienkalender Sachsen-Anhalt, L33, und eine kleine Zufallsauswahl von Übereinstimmungen. Alternativ eine Prüfung, die nicht über das Hilfsmodell läuft, z. B. direkter Blick in die XML-Felder für Optionstexte bei den „keine Angabe“-Losen.
- Eine Auszählung, wie viele Lose der Liste keinen Zuschlag haben und wie viele von Regel 6 betroffen sind.
- Ablage von Auftragstext und Subagenten-Protokollen, damit Blindheit und Kontext (CLAUDE.md) nachprüfbar sind.
- Ein einheitlicher, vorab festgelegter Umgang mit nicht tagesgenau bestimmbaren Grundlaufzeiten.

### Welche Aussagen zulässig sind (Frage 7)

**Zulässig:**
- „Das Ende der Grundlaufzeit der Liste stimmt bei 77/80 Zufallslosen mit zwei getrennten KI-Lesungen derselben Modellfamilie überein (Wilson 89,5–98,7, ohne Berücksichtigung der Klumpung); nicht von Menschen bestätigt.“
- „Die Abweichungen der Iteration 7 sind überwiegend mit Prüferfehlern vereinbar.“
- „Regel 1b liest Fälle mit ausdrücklich genannter Grunddauer richtig (L3, L73, L77 am Original).“

**Nicht zulässig:**
- „Die Liste ist korrekt.“
- „Regel 1b ist belegt.“
- „A19 bestätigt.“
- „Iteration 7 lag in Wahrheit bei 96 %.“ Iteration 8 ersetzt Iteration 7 nicht, so wie vorab festgelegt.
- „Unabhängig geprüft.“

### Empfehlung
**Weiter (Projektabschluss) mit eingeschränkter Formulierung.** Nach den Vorab-Regeln folgt aus Z0 bis Z4 „weiter“, und Z1 ist auch nach meiner Prüfung tragfähig; ein Zurück wäre durch die vorab festgelegten Regeln nicht gedeckt.

Die Folge „Regel 1b gestützt“ würde ich aber nur für Fälle mit ausdrücklicher Grunddauer übernehmen. Z2 sollte mit beiden Zahlen berichtet werden: 14/15 nach Regel, 11/15 bei einheitlichem Maßstab. Die neu gefundenen Fehlerarten gehören als offene Grenzen ins Lab-Log, ohne Regeländerung in dieser Iteration: Lose ohne Zuschlag, Übertragung nach Regel 6, Monatsnamen-Daten, „um 3 Jahre“.

Die Entscheidung trifft der Nutzer.

**Relevante Dateien:**
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\docs\iterationen.md`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_vorlage.md`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_leser_a.csv`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_leser_b.csv`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_roh\`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_hinweise.md`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_entscheide.csv`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_z4.csv`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zweitlesung_iteration8_auswertung.md`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\src\prepare\auswertung_iteration8.py`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\src\prepare\zweitlesung_iteration8_zusammenfuehren.py`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\src\prepare\vertragsliste.py` (Regel 6 in `je_los`, `RE_DATUM`, `RE_BASIS_DAUER`)
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\data\processed\liste_pruefung_iteration7_schluessel.csv`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\data\raw\ted_search\DEU_result_cpv909_20231025_20260930_lostext\page_0017.json`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\docs\annahmen.md`
- `C:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\.git\logs\HEAD`

---

### Nachprüfung durch Claude und Entscheidung (2026-11-05)

**Nachgeprüft (Fakten):** In den Protokollen von Leser A (Teil 1) und Leser B (Teil 1) steht der Satz aus `CLAUDE.md` („Das Enddatum der Bekanntmachung ist manchmal schon das Höchstende“): Die Leser hatten ihn automatisch im Kontext, Listenwerte kannten sie nicht. Das ist in `docs/iterationen.md` und `docs/ki_irrwege.md` vermerkt.
**Entscheidung des Nutzers:** Weiter (Projektabschluss), eingeschränkt formuliert; keine weitere Iteration. Z2 wird mit beiden Zahlen berichtet (14/15 und 11/15).
