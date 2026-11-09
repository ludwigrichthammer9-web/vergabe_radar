# Spickzettel Fragenrunde (5 Minuten)

_Stand 2026-11-09. Laut Bewertungsbogen (`docs/bewertung_LN.md`, Zeile 29) gibt es drei Fragen: eine **Methodenfrage**, einen **Live-Nachweis im Werkzeug** und eine **Entscheidungs- oder Transferfrage**. Die Fragen gehen an das Teammitglied, das den Teil **nicht** präsentiert hat. Quellen der Fragen: Notizen „FRAGE – ANTWORT“ und „ZEIG-MIR-WO“ in `src/report/vortrag.py`, `docs/bewertung_LN.md`, Beispielfragen des Bewertungsbogens 5 („Beispielfragen für die Fragenrunde“, LN B und LN C), typische Prüferfragen._

_Folien (Stand: Kopf und `TITEL` in `src/report/vortrag.py`, 2026-11-09): 11 sichtbar._

| Nr. | Folie | Sprecher | Fragen dazu beantwortet |
|---|---|---|---|
| 1 | Titel | Ludwig | Manuel |
| 2 | Video „Franz und die Glaskugel“ (Kurzfilm 3:32; **Quizfrage jetzt vor dem Video**) | Ludwig | Manuel |
| 3 | Betriebe heute und unsere Idee | Manuel | Ludwig |
| 4 | Konkurrenz: Vertragsenden kostenlos bei Vergabeweiser | Manuel | Ludwig |
| 5 | Vergleich mit Vergabeweiser | Ludwig | Manuel |
| 6 | Make or Buy aus Sicht des Betriebs | Ludwig | Manuel |
| 7 | Demo als Zielbild | Ludwig | Manuel |
| 8 | Technik: Pipeline und Prognoseregel im Code (`src/model/baseline.py`) | Manuel | Ludwig |
| 9 | KI-Irrwege und Trennung von Entwicklung und Test | Ludwig | Manuel |
| 10 | Empfehlung und Grenzen | Manuel | Ludwig |
| 11 | Fazit (mit QR-Code zum Repo) | Manuel | Ludwig |

_Ausgeblendeter Anhang: 12 Vier Versuche, vier verfehlte Schwellen · 13 Frage/Kriterium/Daten · 14 Trefferquote je Vorlauf · 15 Liste und Genauigkeit · 16–17 Sicherung „Falls die Technik streikt“ (Live-Nachweise als Bild). Die Folientitel im Vortrag sind Aussagesätze (z. B. Folie 8: „So funktioniert es technisch: von der TED-Abfrage zur geprüften Liste“); oben stehen Kurznamen. Vor dem Vortrag in `docs/vortrag/` abgleichen._

**Einheitliche Zahlen (so sagen, überall gleich):**
- Laufzeitende bestimmbar (Gebäudereinigung, Iteration 1): **80,9 % (90,0 %, wenn eine Dauer ohne Beginn mitzählt)**; n = 440 Zuschläge in 3 Monaten (`docs/iterationen.md`, Zeilen 85 und 107).
- BT-58 (höchste Zahl der Verlängerungen) immer mit Bezugsmenge: **vorhanden bei 18,9 %, > 0 bei 14,7 % der 15.706 deutschen Zuschlagsbekanntmachungen** vom 22.07. bis 21.10.2026 (alle Branchen); in der Gebäudereinigung > 0 bei 42,0 % von 440 (`reports/datenqualitaet_DEU_20260722_20261021.md`, Zeilen 3, 65–66 und 155).
- Folie 2, Runde 1: **„11 von 24 Vorschlägen richtig“** (Präzision V2, 45,8 %), nicht „Vorgänger gefunden“; gefunden wurden 11 von 38 = 28,9 % (Trefferquote V3; `docs/iterationen.md`, Zeilen 407–408).
- Folie 9: Auf Entwicklungsdaten **hielt die KI 10–11 von 12 Vorschläge für plausibel**, im Test waren 11 von 24 richtig (`docs/iterationen.md`, Zeile 420).
- Arbeit nach Iteration 10 heißt **„Nachträge nach Iteration 10“**, nicht „Iteration 11“.
- „Nutzer“ (so in Lab-Log und Iterationslog) heißt im Gespräch „wir“ (gemeinsam im Call, rund 90 %) oder „Ludwig“, wenn `docs/beitraege.md` es ihm einzeln zuordnet.

**Regel für jede Antwort:** erst die Zahl, dann die Grenze, dann die Datei. Fakten und Deutung trennen („Gemessen ist …; wir deuten das als …“). Auf den Folien heißt das Höchstende „spätestes Vertragsende“; in Code, Lab-Log und hier „Höchstende“.

---

## Teil A: Live-Nachweise (vorbereitet)

Alle Befehle im Wurzelordner des Repos, PowerShell. (a) bis (c) und (e) laufen ohne lokale Daten; (d) braucht die Zwischentabellen in `data/processed/`. Ausgaben unten sind am 2026-11-09 mit `.venv\Scripts\python.exe -I` erzeugt und unverändert abgeschrieben (Dezimalpunkt wie im Skript).

> **Hinweis Zeichensatz:** Im Mitschnitt unseres Werkzeugs erschienen „±“, „–“ und Umlaute als Ersatzzeichen. Vor dem Vortrag im echten Terminal testen; falls nötig vorher `chcp 65001` ausführen.

### (a) Parameter ändern und Wirkung erklären

Skript: `src/model/sensitivitaet_backtest.py`. Es liest die 52 Paare aus `reports/backtest_iteration5.md` (im Git). Mit Argumenten schreibt es nichts, es zeigt nur eine Variante. **Wichtig sagen:** Das ist nachträglich und kein neuer Test; die Regel war vorab eingefroren (Vorlauf 6, Fenster ±3, Schwelle 60 %).

**Kontrolle (vorab festgelegte Regel):**
```
.venv\Scripts\python.exe -I src\model\sensitivitaet_backtest.py --vorlauf 6 --fenster 3
R0: Vorlauf 6 Monate, Fenster ±3: 9 von 52 = 17.3 % (Wilson 9.4–29.7 %)
R1: Vorlauf 6 Monate, Fenster ±3: 15 von 52 = 28.8 % (Wilson 18.3–42.3 %)
Vorab festgelegt: Vorlauf 6, Fenster ±3, Schwelle 60 %.
```

**Variante 1: mehr Vorlauf, engeres Fenster** (Beispiel aus dem Skriptkopf)
```
.venv\Scripts\python.exe -I src\model\sensitivitaet_backtest.py --vorlauf 9 --fenster 2
R0: Vorlauf 9 Monate, Fenster ±2: 1 von 52 = 1.9 % (Wilson 0.3–10.1 %)
R1: Vorlauf 9 Monate, Fenster ±2: 2 von 52 = 3.8 % (Wilson 1.1–13.0 %)
```
Wirkung: Die Prognose rückt 3 Monate früher, das Fenster wird schmaler. Fast alle Treffer fallen weg.

**Variante 2: gleicher Vorlauf, doppelt so breites Fenster**
```
.venv\Scripts\python.exe -I src\model\sensitivitaet_backtest.py --vorlauf 6 --fenster 6
R0: Vorlauf 6 Monate, Fenster ±6: 11 von 52 = 21.2 % (Wilson 12.2–34.0 %)
R1: Vorlauf 6 Monate, Fenster ±6: 16 von 52 = 30.8 % (Wilson 19.9–44.3 %)
```
Wirkung: Ein Jahr Unsicherheit statt eines halben bringt nur 1 Treffer mehr. Die Termine streuen weit (20 Neuausschreibungen kamen mehr als 3 Monate früher, 17 später; `docs/iterationen.md`, Zeile 788).

**Variante 3: ein Jahr Vorlauf, Fenster ±6**
```
.venv\Scripts\python.exe -I src\model\sensitivitaet_backtest.py --vorlauf 12 --fenster 6
R0: Vorlauf 12 Monate, Fenster ±6: 5 von 52 = 9.6 % (Wilson 4.2–20.6 %)
R1: Vorlauf 12 Monate, Fenster ±6: 12 von 52 = 23.1 % (Wilson 13.7–36.1 %)
```
Wirkung: So viel Vorlauf, wie ein Betrieb für die Personalsuche gern hätte, trifft seltener.

**Satz dazu:** Keine Variante kommt in die Nähe von 32 Treffern (60 %). Die volle Tabelle (Vorlauf 0 bis 24, Fenster ±1 bis ±12) steht in `reports/sensitivitaet_iteration5.md`; bester Vorlauf ist 6 mit 28,8 %, erst ±12 Monate erreicht 50 %. Ohne Argumente erzeugt das Skript diesen Bericht neu; am 2026-11-09 geprüft: die Datei bleibt byte-gleich (`git status` danach leer).

### (b) Trennung von Entwicklung und Test

**Schritt 1: Überschneidung Entwicklungsfälle gegen Stichprobe der Iteration 9.** Spalten vorher angesehen: `reports/stichprobe_iteration9_lose.csv` hat `N;notice;los;los_titel` (Semikolon), `reports/entwicklung_iteration9_notices.txt` hat eine Bekanntmachung je Zeile, Kommentare mit `#`.
```
.venv\Scripts\python.exe -I -c "import csv;e={z.strip() for z in open('reports/entwicklung_iteration9_notices.txt',encoding='utf-8') if z.strip() and not z.startswith('#')};s={r['notice'] for r in csv.DictReader(open('reports/stichprobe_iteration9_lose.csv',encoding='utf-8'),delimiter=';')};print(len(e),'Entwicklung,',len(s),'Stichprobe, Ueberschneidung:',len(e&s))"
7 Entwicklung, 104 Stichprobe, Ueberschneidung: 0
```
Mit beiden Entwicklungslisten (Iteration 7 und 9; im Einzeiler `open(...)` über beide Dateien `reports/entwicklung_iteration7_notices.txt` und `reports/entwicklung_iteration9_notices.txt`): `27 Entwicklung (It. 7 und 9), 104 Stichprobe, Ueberschneidung: 0`. Die Stichprobe hat 110 Lose aus 104 Bekanntmachungen.

**Schritt 1b: Lose der Iteration 7 gegen Stichprobe 9.** Der Schlüssel der Iteration 7 liegt jetzt als Kopie in `reports/daten/` (Spalten `L`, `notice`).
```
.venv\Scripts\python.exe -I -c "import csv;it7={r['notice'] for r in csv.DictReader(open('reports/daten/liste_pruefung_iteration7_schluessel.csv',encoding='utf-8'),delimiter=';') if r['L'].startswith('L')};s={r['notice'] for r in csv.DictReader(open('reports/stichprobe_iteration9_lose.csv',encoding='utf-8'),delimiter=';')};print(len(it7),'Iteration 7,',len(s),'Stichprobe 9, Ueberschneidung:',len(it7&s))"
85 Iteration 7, 104 Stichprobe 9, Ueberschneidung: 0
```
_Grenze:_ Das Stichprobenskript schließt zusätzlich die Bekanntmachungen der Handsuche aus (`src/prepare/stichprobe_iteration9.py`, Zeilen 69–73; angewendet in Zeile 78).

**Schritt 2: Reihenfolge der Commits** (Kriterien vor Stichprobe, Stichprobe vor Antworten).
```
git log --oneline --reverse 4f50436^..f6583cc
```
Ergebnis (gekürzt, älteste zuerst): `4f50436` Hypothese, Kriterien, Seed vorab → `9d63c59` Stichprobe gezogen (Seed 20261112, 160 Lose) → `d6e2335` Paket F → `49bb198` Skript für Abruf und Auswertung vor dem Abruf → `ea5ebfb` Paket A → `79fd0df` Paket C → `64a23e3` Abruf abgeschlossen → `6b7e8d8` Paket für die Leser vor den Antworten → `69917ff` Antworten der Leser unverändert → `f6583cc` Auswertung.
Iteration 9 genauso: `git log --oneline --reverse a03a4a8^..e1726e7` zeigt `a03a4a8` Regeln 6 bis 10 → `4521952` Seed vor dem Ziehen → `b3b1471` Stichprobe und Auswertungsskript → `3dd84bd` Nachtrag Pfad → `e1726e7` Antworten.
_Grenzen (ehrlich sagen):_ Die Commit-Zeiten setzen wir selbst; belegt ist die Reihenfolge in der Git-Kette, kein Zeitstempel einer dritten Stelle. `4f50436` und `9d63c59` liegen in derselben Minute (17:50). Das Lauf-Skript der Leser in Iteration 9 kam erst mit den Antworten ins Git; das Leseprotokoll der Iteration 10b liegt außerhalb des Repos (`docs/ki_irrwege.md`).

### (c) Fehlwerte zeigen

Datei: `reports/beispiel_liste_oberpfalz.csv` (130 Lose der Oberpfalz, Semikolon, UTF-8 mit BOM). Spalte `stufe` sagt, woher das Ende stammt.
```
.venv\Scripts\python.exe -I -c "import csv,collections as c;r=list(csv.DictReader(open('reports/beispiel_liste_oberpfalz.csv',encoding='utf-8-sig'),delimiter=';'));print(len(r),'Lose; Stufen:',sorted(c.Counter(x['stufe'] for x in r).items()));print('gl_ende leer:',sum(not x['gl_ende'] for x in r),'nach Stufe:',sorted(c.Counter(x['stufe'] for x in r if not x['gl_ende']).items()))"
130 Lose; Stufen: [('A', 54), ('B', 2), ('C', 27), ('D', 9), ('E', 5), ('F', 33)]
gl_ende leer: 38 nach Stufe: [('E', 5), ('F', 33)]
```
**Erklärung der 38 leeren `gl_ende`:**
- **33 Lose Stufe F:** kein Ende in der Bekanntmachung. Bei allen 33 fehlen die Laufzeitfelder im XML; 14 davon nennen Dauer oder Datum nur im Freitext, den die Regel nicht liest (`reports/stufe_f_ursachen.md`, Zeilen 9 und 15).
- **5 Lose Stufe E:** Es gibt kein Datum und keinen Beginn, nur eine Dauer. Das Ende ist **geschätzt** (Veröffentlichung + Dauer) und steht deshalb in der Spalte `gl_geschaetzt`, nicht in `gl_ende`. Es zählt nicht für die Abdeckung und ist ungeprüft (`reports/beispiel_liste.md`, Zeile 26; `src/prepare/vertragsliste.py`, Zeilen 397–400; Einteilung E/F in `src/report/beispiel_liste.py`, Zeilen 74–78).
- **Wirkung:** 33 von 130 = 25,4 % der Oberpfalz-Lose haben kein Ende. Über alle 9.325 Lose fehlt es bei 27,0 %, im letzten Jahr bei 20,6 % (Lab-Log §4). Wir füllen diese Lücke nicht mit einer Schätzung auf, sondern zeigen sie als Stufe F.

**Umstellen wie im Bogen („Fehlwerte anders behandeln, Wirkung erklären“): geschätzte Enden mitzählen.**
```
.venv\Scripts\python.exe -I -c "import csv;r=list(csv.DictReader(open('reports/beispiel_liste_oberpfalz.csv',encoding='utf-8-sig'),delimiter=';'));a=sum(1 for x in r if x['gl_ende']);b=sum(1 for x in r if x['gl_ende'] or x['gl_geschaetzt']);print(len(r),'Lose; Ende laut Bekanntmachung:',a,'; mit geschaetztem Ende (Stufe E):',b)"
130 Lose; Ende laut Bekanntmachung: 92 ; mit geschaetztem Ende (Stufe E): 97
```
Wirkung: Oberpfalz 92 → 97 von 130 Losen mit Ende (70,8 % → 74,6 %). Über alle Lose des letzten Jahres stiege die Abdeckung X4 von 2.783/3.503 = 79,4 % auf 3.044/3.503 = 86,9 % und läge damit über der Schwelle von 80 % (`reports/vertragsliste_iteration9.md`, Zeile 16). **Genau deshalb zählen wir sie nicht:** Die Schätzung ist ungeprüft, und das Kriterium würde nur durch eine andere Zählweise erfüllt. Der Export (`docs/prototyp/export/`) führt die 5 Enden mit `ende_herkunft = geschaetzt`, die Webseite mit dem Status „Grundlaufzeit läuft (geschätzt)“.

Ergänzend auf der Webseite: `docs/prototyp/vertragsliste.html` lokal öffnen, Filter „Stufe“ auf F setzen.

### (d) Seed zeigen und Ziehung wiederholen

**Wo:** `src/prepare/stichprobe_iteration9.py`, Zeile 33 (`SEED = 20261109`); benutzt in Zeile 68 (`seed = 1 if trocken else SEED`), Zeile 79 (Ziehung), Zeile 91 (Mischen, `seed + 2`) und Zeile 93 (15 Lose für die Menschenprüfung, `seed + 3`). Andere Seeds: Iteration 10b `src/prepare/stichprobe_iteration10b.py`, Zeile 19 (20261112); Zweitprüfung Iteration 5 `src/prepare/backtest_paare.py`, Zeile 61 (20261101); Liste aller Seeds und Hashes: Lab-Log Anhang A.

**Trockenlauf** (laut Docstring: anderer Seed, schreibt nichts):
```
.venv\Scripts\python.exe -I src\prepare\stichprobe_iteration9.py --trockenlauf
Pool Fenster 2376 Lose aus 1140 Bekanntmachungen; ausgeschlossene Bekanntmachungen 429
Z 70 | R 4 (Pool 4) | M 26 (Pool 1216) | S 10 (Pool 37) | Mensch 15
Trockenlauf: nichts geschrieben.
```
Mit dem echten Seed (Lauf am 2026-11-09 in einen Ordner außerhalb des Repos umgeleitet, damit nichts überschrieben wird) kamen `Z 70 | R 2 (Pool 4) | M 28 (Pool 1216) | S 10 (Pool 37) | Mensch 15` und `Schlüssel SHA-256: 9dbf5c1a…`. Beide Dateien waren byte-gleich mit `reports/stichprobe_iteration9_lose.csv` und `data/processed/stichprobe_iteration9_schluessel.csv`; der Hash steht seit Iteration 9 in `docs/iterationen.md`. Mit Seed 1 statt 20261109 hatten die beiden Ziehungen nur 10 von 110 Losen gemeinsam.

**Ohne lokale Daten?** Nur eingeschränkt. Das Skript liest fest aus `data/processed/`: `vertragsliste_909.csv` und `liste_pruefung_iteration7_schluessel.csv` liegen als Kopie in `reports/daten/` und müssten dorthin kopiert werden. Die alte Fassung `vertragsliste_909_iteration8.csv` liegt dort nicht (Stand 2026-11-09). Ohne sie bricht das Skript ab. Ohne lokale Daten also besser die Stelle im Code zeigen und den Hash im Commit nennen.

### (e) Diagramme erzeugen

```
.venv\Scripts\python.exe -I src\report\diagramme.py
diagramm_abweichung.png: 15/52 im Fenster, Median +0.6; diagramm_vorlauf.png: bestes R1 28.8 %
```
Liest nur `reports/backtest_iteration5.md` (im Git), braucht `matplotlib`. Schreibt `docs/lab_log_bilder/diagramm_abweichung.png` und `diagramm_vorlauf.png`; am 2026-11-09 geprüft: beide byte-gleich (`git status` danach leer). Danach das Bild öffnen und M8 (Median gegen Streuung) daran erklären.

---

## Teil B: Wahrscheinliche Fragen

Kategorien: **M** = Methodenfrage, **L** = Live-Nachweis, **E** = Entscheidungs- oder Transferfrage.

### Methodenfragen

**M1. Warum ±3 Monate und warum 60 %?**
Kurzantwort: Fenster und Schwelle haben wir am 2026-10-30 vor jeder Rechnung festgelegt, als Setzung ohne Kundenkontakt. Die Idee: Ein Betrieb braucht etwa ein Vierteljahr Spielraum für Personal und Angebot; mehr als ±3 Monate hilft bei der Planung kaum. Ob ein Betrieb genau das braucht, ist nicht belegt; das steht so in den Unterlagen.
Zeig mir wo: `docs/business.md` §7.1, Zeilen 179–186 („Setzung, nicht belegt“); `docs/iterationen.md`, Zeilen 651–662 (Hypothese vorab).

**M2. Sind 28,8 % gegen 17,3 % mehr als Zufall?**
Kurzantwort: Nicht gesichert. Auf denselben 52 Paaren trifft nur R1 in 10 Fällen, nur R0 in 4 Fällen; der exakte McNemar-Test ergibt p = 0,18. Entscheidend ist ohnehin, dass beide weit unter 60 % liegen.
Zeig mir wo: `reports/sensitivitaet_iteration5.md`, Zeile 11.

**M3. Habt ihr die 6 Monate nicht nach Ansicht der Daten gewählt?**
Kurzantwort, ehrlich: Teilweise ja. „Minus 6 Monate“ stammt aus dem Projektplan (naive Referenz T3.3.4); eine Schätzung des Vorlaufs aus den Paaren (T3.2.1) haben wir bewusst gestrichen. Den Anker „Höchstende“ haben wir aber gewählt, nachdem wir einen Teil derselben Paare in Iteration 3 und 4 explorativ angesehen hatten; dieser Vorbehalt steht vorab im Protokoll. Die Sensitivität zeigt, dass die Wahl am Ergebnis nichts ändert: Kein Vorlauf von 0 bis 24 Monaten kommt über 28,8 %.
Zeig mir wo: `docs/iterationen.md`, Zeilen 660 und 666–669; `docs/projektplan.md`, Zeilen 186 und 194; Live-Nachweis (a).

**M4. Welche Baseline habt ihr, und warum diese?**
Kurzantwort: Für die Terminprognose R0 = Ende der Grundlaufzeit − 6 Monate (17,3 %); sie zeigt, was die einfachste Regel schafft. Für die Vertragsliste die Basisregel „Feld EndDate übernehmen“: 63 von 70, gegen 66 von 70 für unsere Liste und 65 von 70 für die alte Fassung. Der Zugewinn der Leseregeln ist also klein und kaum gesichert.
Zeig mir wo: `docs/business.md` §7.1, Zeilen 144–147; Lab-Log §4 und §5 (Tabelle W1).

**M5. Die KI-Leser stammen aus derselben Modellfamilie wie eure Regeln. Warum ist 66 von 70 trotzdem aussagekräftig?**
Kurzantwort: Nur eingeschränkt, und so formulieren wir es auch („übereinstimmend“, nicht „korrekt“). Für die Aussagekraft spricht: neue Zufallsstichprobe (Seed 20261109, vorab committet), zwei Leser lasen den Rohtext ohne Projektkontext nach einer neutralen Definition, und die Liste konnte abweichen (sie tat es 4-mal). Ein Teammitglied (Manuel) las 15 Lose im TED-Original: 14 von 15 stimmen. Dagegen spricht: gleiche Modellfamilie, der Vergleichswert nutzt teils dasselbe Feld (teilweise zirkulär), gemeinsame Fehler bleiben unsichtbar, und der menschliche Leser ist nicht unabhängig.
Zeig mir wo: Lab-Log §4 (Iteration 9, Deutung); `reports/evaluation_iteration9.md`; `reports/zweitlesung_iteration9_mensch.csv`.

**M6. Warum habt ihr in Iteration 10b nur die 15 abweichenden Lose lesen lassen?**
Kurzantwort: Die 145 übereinstimmenden Lose ändern die Differenz zwischen Liste und Vergabeweiser nicht. Die absolute Genauigkeit belegt das nicht; bei 1 von 10 übereinstimmenden Losen lagen sogar beide falsch. Von den 15 sind 7 Höchstende statt Grundlaufzeit und 4 Losebene, also vor allem Definitionsfragen.
Zeig mir wo: Lab-Log §5 (Einordnung der 15 Lose); `reports/evaluation_iteration10b.md`.

**M7. Wie habt ihr Leakage im Backtest vermieden?**
Kurzantwort: Die Prognose nutzt nur Wissen zum Zeitpunkt des Vorgänger-Zuschlags (Ausschreibung und Zuschlag des Vorgängers). Spätere Vertragsänderungen und Angaben aus der Handsuche wie „verlängert bis“ sind ausgeschlossen. Die Regeln wurden in `src/model/baseline.py` eingefroren, bevor sie auf die Paare liefen.
Zeig mir wo: `docs/business.md` §7.1, Festlegung 1, Zeilen 150–153; `docs/iterationen.md`, Zeile 663.

**M8. Ihr berichtet die Trefferquote im Fenster. Welches Maß hätte mehr gezeigt?** (Bogen: „Welches Maß hätte Ihr Erfolgskriterium besser abgebildet?“)
Kurzantwort: Die Abweichung in Monaten samt Streuung. Der Median allein täuscht: Bei R1 liegt er bei +0,6 Monaten, also fast perfekt; bei R0 bei +14,0 Monaten (`reports/backtest_iteration5.md`, Zeile 12–13). Die Streuung von R1 ist aber riesig: mittleres Quartil −10,8 bis +14,3 Monate, Spanne −38,3 bis +95,0 Monate, 20 Fälle mehr als 3 Monate zu früh, 17 zu spät (Quartile am 2026-11-09 aus der Spalte „Abw. R1“ nachgerechnet, Python `statistics.quantiles`). Gute Lage im Mittel, aber für den einzelnen Vertrag unbrauchbar; genau das misst die Trefferquote im Fenster. Ein Betrieb plant mit dem einzelnen Vertrag, deshalb passt das Fenster als Kriterium. Ergänzend wäre der Median des Betrags der Abweichung gewesen (12,0 Monate, ebenfalls nachgerechnet).
Zeig mir wo: `docs/lab_log_bilder/diagramm_abweichung.png` (Live-Nachweis e); `reports/backtest_iteration5.md`, Tabelle „Alle Paare“ und „Lage der Veröffentlichung“.

**M9. Warum eine feste Regel und kein gelerntes Modell (Klassifikation, Überlebenszeitmodell)?** (Bogen: „Warum dieses Verfahren und nicht die Alternative?“)
Kurzantwort: Unser Vorgehen hieß „einfach vor komplex“; ein Modell nur, wenn die Regeln klar an Grenzen stoßen. Mit 52 Paaren reicht es nicht für Training und getrennten Test. Wichtiger: Ein Modell hätte dieselben Merkmale wie die Regel. Ob eine Verlängerungsoption gezogen wird, steht nicht im Zuschlag des Vorgängers. Selbst der nachträglich beste Vorlauf bleibt bei 28,8 %. Eine feste Regel ist für einen Betrieb außerdem nachvollziehbar.
Zeig mir wo: Lab-Log §3, „Warum eine feste Regel und kein gelerntes Modell?“; `docs/CRISP-DM.md`, Phase 4.

**M10. Habt ihr Ausreißer entfernt? Was ging dabei verloren?**
Kurzantwort: Ja, eine Plausibilitätsregel seit Iteration 1. Laufzeiten ≤ 0 oder über 240 Monate gelten als unplausibel, das Ende bleibt leer. In der Liste betrifft das 19 von 9.325 Losen (`gl_herkunft = unplausibel`, am 2026-11-09 in `reports/daten/vertragsliste_909.csv` gezählt), davon 9 von 3.503 bei den Zuschlägen 10/2025 bis 9/2026 (Tabelle X4 in `reports/vertragsliste_iteration9.md`; diese Zahl steht im Lab-Log neben der 19). Verloren gehen könnten echte lange Verträge oder Tippfehler, die man von Hand retten könnte; geprüft haben wir diese 19 nicht. Beim Höchstende zählen Kandidaten nur bis 10 Jahre nach der Grundlaufzeit.
Zeig mir wo: `src/prepare/vertragsliste.py`, Zeilen 164–173 (`grundlaufzeit`), Zeile 78 (`MAX_MONATE = 240`).

**M11. Im zweiten Zyklus habt ihr das Ziel gewechselt (Prognose → Liste). Was hat das ausgelöst?**
Kurzantwort: Die vorab festgelegte Folge. Bei R1 < 40 % hieß es „Idee anpassen: Vertragsliste ohne Terminprognose“; R1 lag bei 28,8 %. Die Daten zeigen den Grund: Die Neuausschreibungen streuen zu weit um das Vertragsende (M8). Statt das Ziel zu wechseln, hätten wir neue Merkmale suchen können, etwa ausgeübte Verlängerungen oder Vorinformationen (PIN). Das steht als Ausblick im Lab-Log §7, nicht als Ergebnis.
Zeig mir wo: `docs/iterationen.md`, Zeilen 690–695; Lab-Log §3 und §7.

### Live-Nachweise

**L1. „Ändert bitte einen Parameter und erklärt die Wirkung.“** → Teil A (a). Erst Kontrolle 6/3 zeigen, dann 9/2 oder 6/6.

**L2. „Zeigt uns die Trennung von Training und Test.“** → Teil A (b). Einzeiler (Überschneidung 0), dann `git log --oneline --reverse 4f50436^..f6583cc`.

**L3. „Wo sind die Fehlwerte, und wie geht ihr damit um? Stellt die Behandlung um.“** → Teil A (c). Stufe F = 33 von 130; 38 leere `gl_ende` = 33 F + 5 E (geschätzt, eigene Spalte). Umgestellt: mit Stufe E 97 statt 92 von 130; X4 würde 86,9 % statt 79,4 %, deshalb zählen wir E nicht.

**L4. „Wo wird der Seed gesetzt? Was wäre ohne Seed nicht reproduzierbar?“** → Teil A (d). Zeile 33 zeigen, dann `--trockenlauf`. Ohne festen Seed wären nicht reproduzierbar: welche 110 Lose in der Stichprobe der Iteration 9 stehen, damit V1 66/70 und V6 14/15, der Vergleich mit Vergabeweiser auf denselben 70 Losen (Iteration 10) und die SHA-256-Werte im Lab-Log (Anhang A). Mit Seed 1 statt 20261109 hatten die Ziehungen nur 10 von 110 Losen gemeinsam. Grenze: Der Seed garantiert dieselbe Ziehung nur mit derselben Liste. Ein neuer TED-Abruf ändert den Pool (`README.md`, Abschnitt „Daten“).

**L5. „Erzeugt das Diagramm neu.“** → Teil A (e).

### Entscheidungs- und Transferfragen

**E1. Warum habt ihr die Demo gebaut, nachdem der Auswahlbogen Nein gesagt hatte?**
Kurzantwort: Wir haben sie auf eigenen Wunsch nach dem Auswahlbogen gebaut (`docs/beitraege.md`: Wunsch nach Demo, gemeinsam), als Veranschaulichung der Datenübergabe, ausdrücklich ohne Business-Case-Anspruch. Der Bogen hatte die Idee (K-I) mit K7 = 0 ausgeschlossen, gerade weil „erst bauen, dann prüfen“ der Fehler aus dem Marktgate war; das sagen wir offen. Die Demo belegt keine Nachfrage und keine KI-Genauigkeit; den Vorgänger-Hinweis haben wir im großen Datensatz abgeschaltet (3 von 3 Auslösungen falsch).
Zeig mir wo: `docs/business_case_auswahl.md`, Zeile 50; `docs/demo_push.md`; Lab-Log §6 und §8.

**E2. Was soll ein Reinigungsbetrieb morgen konkret tun?**
Kurzantwort, unsere Empfehlung im Wortlaut: **Kostenlosen Alarm nutzen · Abo nur, wenn eine Funktion fehlt – vorher testen · nicht selbst bauen, solange niemand Treffer von Hand ins eigene System überträgt.** Kostenlos heißt: TED-Suchprofil mit E-Mail-Alarm, bei Vergabeweiser die Vertragsenden nachsehen. Vor jeder Entscheidung die Bekanntmachung selbst lesen (Grundlaufzeit oder spätestes Vertragsende?). Im Gespräch fehlte eine Funktion nur dem größeren Betrieb: Wettbewerbsdaten. Das Selbstbauen rechnet sich im Modell gegen kostenlose Dienste nicht (Annahmen, keine Messung).
Zeig mir wo: `docs/entscheidungsvorlage_betrieb.md`; Lab-Log §7.

**E3. Wie belastbar sind drei Gespräche?**
Kurzantwort: Nicht belastbar, es sind Hinweise. Neun Anrufe, drei erreicht (zwei Betriebe, eine Vergabestelle), Antworten gespalten: Der größere Betrieb würde eher für Wettbewerbsdaten zahlen, der Kleinbetrieb für nichts. Deshalb behaupten wir weder Nachfrage noch Zahlungsbereitschaft; der nächste Test hat eine vorab festgelegte Schwelle (mindestens 2 von 3), ist aber nicht durchgeführt.
Zeig mir wo: `docs/business.md` §8.9, Zeilen 314–343; `docs/business_case_auswahl.md`, Zeile 77.

**E4. Würde das in einer anderen Nische funktionieren, etwa Winterdienst, oder an einem anderen Standort?**
Kurzantwort: Die Pipeline ist übertragbar (CPV und Region sind Parameter von `src/ted_download.py`); die Leseregeln müsste man neu testen. Winterdienst hatte in Iteration 1 eine ähnliche Datenqualität (Laufzeitende bestimmbar bei 84,5 % gegen 80,9 %, Intervalle überlappen; 93,0 % gegen 90,0 %, wenn eine Dauer ohne Beginn mitzählt), aber nur 129 statt 440 Zuschläge in drei Monaten und ein Saisonmuster. Vor allem gilt die Lehre: zuerst prüfen, ob es die Liste schon gibt (Marktgate).
Zeig mir wo: `docs/iterationen.md`, Zeilen 83–107; Werte mit Dauer: `reports/datenqualitaet_DEU_20260722_20261021.md`, Zeilen 155–156.

**E5. Was ist mit Aufträgen unterhalb der EU-Schwelle?**
Kurzantwort: Die fehlen in TED. Im Bekanntmachungsservice standen 32 von 120 Oberpfälzer Reinigungsverfahren nicht auf TED, also 26,7 % (Wilson 19,6–35,2 %); die Vorab-Schwelle von 33 % ist damit nicht entscheidbar. Die erste Auswertung ergab 0 von 84, das war ein Filterfehler; wir haben die Null geprüft statt sie zu berichten. Die Vergabestelle sagte, sie vergebe „sehr oft“ national (n = 1).
Zeig mir wo: Lab-Log §5, Paket B; `reports/oeffentlichevergabe_robustheit.md`.

**E6. Was passiert bei doppeltem Datenvolumen?**
Kurzantwort: Abruf und Aufbereitung skalieren, das sind Skripte gegen eine öffentliche API; die Liste hat heute 9.325 Lose. Was nicht skaliert, ist die Prüfung: Handprüfung, KI-Leser und Evaluator kosten je Stichprobe Zeit, und mit mehr Daten kommen neue Fehlerarten. Gemessen haben wir das nicht.
Zeig mir wo: `docs/reproduzierbarkeit.md`; Notiz zur Transferfrage in `src/report/vortrag.py` (Folie 10 „Empfehlung und Grenzen“).

**E7. Warum habt ihr die Konkurrenz erst so spät gesehen?**
Kurzantwort: Ein Prozessfehler. Die Sichtung der Wettbewerber (Plan G1.1) war früh geplant und blieb offen; zwei Suchen am 2026-10-24 fanden keinen deutschen Dienst; am 2026-10-29 fiel die Entscheidung gegen Kundenkontakt. Erst am 2026-11-05 fand ein Recherche-Agent Vergabeweiser und AusschreibungsRadar. Kosten: Die Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos gibt. Lehre: ein Marktgate vor der Modellierung.
Zeig mir wo: Lab-Log §1, „Lernpunkt: Die Konkurrenz wurde erst spät gesehen“; `docs/business.md` §8.6.

**E8. Was hat die KI falsch gemacht, und was habt ihr selbst bemerkt?**
Kurzantwort: KI-Fehler (Auswahl): Auf Entwicklungsdaten hielt die KI 10–11 von 12 Vorschläge für plausibel, im Test waren 11 von 24 richtig (Folie 9); die „blinden“ Leser der Iteration 8 kannten die Projektbeschreibung; die Schwelle W8a war rechnerisch unerreichbar. Selbst bemerkt haben wir unter anderem: Ludwig beim Ausfüllen seiner Zweitprüfung die kalibrierten Paare (P11, P12; laut `docs/beitraege.md` beurteilte er P1–P13) und beim Ausfüllen der Iteration 6 (Prüfung laut `docs/beitraege.md` bei Ludwig), dass Teil B dieselben Paare noch einmal vorlegte; wir (im Call) den Fall 527230-2026 (Dauerfeld enthält die Option schon; Paket C fand dann 12 Lose) und dass die Angabe des Evaluators, Vergabeweiser benachrichtige auch per Teams, Slack oder Webhook, nicht stimmt (Startseite nennt nur gespeicherte Suchen und E-Mail; Gegencheck 2026-11-06). In `docs/ki_irrwege.md` steht dafür „Nutzer“; wer von uns beiden es jeweils war, ist dort nicht festgehalten. Vieles fand der Evaluator, ein getrennter Subagent.
Zeig mir wo: Lab-Log §8; `docs/ki_irrwege.md` (Spalte „Bemerkt durch“).

**E9. Was war Manuels Beitrag?** (keine eigene Kategorie im Bogen; Bezug: Beiträge beider sichtbar)
Kurzantwort, **am besten von Manuel selbst.** Laut `docs/beitraege.md` (Angabe beider, 2026-11-09, nicht aus Git belegbar): Rund 90 % der Zeit haben wir gemeinsam im Call gearbeitet; Claude Code lief über Ludwigs Rechner und Konto, darum steht im Git nur Ludwig. Einzeln belegt sind bei Manuel:
- Zweitprüfung Iteration 5: Paare P14–P71 (Angabe, 2026-11-03).
- Iteration 9: 15 Lose im TED-Original gelesen (V6: 14/15).
- Kritische Business-Case-Prüfung mit dem Subagenten `evaluator` (2026-11-07): Kandidaten bewertet, Kernbotschaft entschärft, keine weitere Iteration (nur Nachträge nach Iteration 10), Liste „Das dürfen wir NICHT behaupten“.
- Reproduzierbarkeitsprüfung auf macOS (2026-11-07): Repo frisch geklont, Berichts-Skripte neu erzeugt und verglichen, Befunde zu Windows-Pfaden und `zeitprotokoll.py`.
- Video: Animation KI-gestützt erstellt, abwechselnd mit Ludwig überarbeitet; neue Fassung mit ElevenLabs-Stimmen (`franz_video_ton.mp4`, 2026-11-09).
- Folien und Vortrag: Präsentation/Umsetzung (Angabe, 2026-11-03); Präsentation gemeinsam.
- Gespräche: bei Manuel „offen“ (die neun Anrufe stehen bei Ludwig).

Verteilung ca. 50:50, von beiden bestätigt. Stunden (Selbstangabe beider, nicht gemessen): je rund 35 bis zur Abgabe am 10.11., dazu je 2–3 h am 11.11. geplant. Nicht mehr sagen, als dort steht.
Zeig mir wo: `docs/beitraege.md` (Tabelle mit Spalte „Gemeinsam (im Call)“); Lab-Log §9 und §10.

**E10. Würdet ihr das Produkt bauen? Warum nicht einfach Vergabeweiser nutzen?**
Kurzantwort: Als Liste allein nein. Vergabeweiser zeigt 1.005 auslaufende Reinigungsverträge kostenlos, mit Auftragnehmer und Zahl der Angebote. Belegt ist bei uns nur ein Merkmalsunterschied (Ende je Los, Grundlaufzeit statt Höchstende) in rund 10 % der Lose, kein Qualitätsvorteil. Der Auswahlbogen ergab höchstens 7 von 14 Punkten (Schwelle 8): kein tragfähiger Business Case.
Zeig mir wo: `docs/business_case_auswahl.md`, Zeilen 27–38; `docs/business.md` §8.2 und §8.4.

**E11. Wer würde zahlen?**
Kurzantwort: Belegt ist das nicht. Der größere Betrieb (rund 120 Beschäftigte, zahlt knapp 1.500 € im Jahr für DTAD) würde eher für alte Preise und den aktuellen Auftragnehmer zahlen; einen Betrag hat er nicht genannt. Der Kleinbetrieb zahlt „für gar nichts in dem Bereich“. Preise je Einheit (etwa 18 € pro Stunde) stehen nicht in TED.
Zeig mir wo: `docs/business.md` §8.9, Zeile 327; `docs/business_case_auswahl.md`, Zeile 42.

**E12. Ihr lagt knapp unter dem Kriterium. Einführung, weiterer Zyklus oder Abbruch?** (Beispielfrage im Bogen 5)
Kurzantwort: Zwei Fälle, je mit Entscheidung:
- **Abdeckung X4:** 79,4 % bei Schwelle 80 % (Wilson 78,1–80,8, die Schwelle liegt im Intervall). Die Folge war vorab festgelegt: „X4 < 80 % → kein Abbruch, Abdeckung offen nennen“. Das haben wir getan. Wir haben die Lücke nicht mit geschätzten Enden geschlossen, obwohl das 86,9 % ergäbe (L3).
- **Höchstende V4:** 87,1 % bei Schwelle 90 %. Für V4 war vorab keine Folge festgelegt, das ist eine Lücke unserer Planung. Entscheidung am 2026-11-05: Fassung 9 wird Prototyp, das Höchstende bleibt nur Hinweis, keine weitere Iteration.

Begründung gegenüber dem Management: Ein weiterer Zyklus würde an der Genauigkeit feilen. Der Engpass liegt aber im Markt: Die Liste gibt es kostenlos (Vergabeweiser). Für die Terminprognose (28,8 % gegen 60 %) gilt nicht „knapp“, dort haben wir die Idee angepasst.
Zeig mir wo: Lab-Log §4 (Abdeckung, Tabelle Iteration 9); `docs/iterationen.md`, Zeilen 695, 1291 und 1333–1334.

**E13. Angenommen, ihr hättet zehnmal so viele Daten. Welche Entscheidung würdet ihr revidieren?** (Beispielfrage im Bogen 5)
Kurzantwort, ehrlich: Die Kernentscheidung „keine Terminprognose“ nicht. Sie scheitert an einem fehlenden Merkmal, nicht an der Menge: Ob eine Option gezogen wird, steht nicht im Zuschlag; selbst ±12 Monate treffen nur 50 %. Was sich ändern würde:
- Die Intervalle würden enger. 28,8 % bei 520 statt 52 Paaren hätte das Wilson-Intervall 25,1–32,9 % statt 18,3–42,3 % (nachgerechnet mit `wilson` aus `src/model/baseline.py`). Auch R1 gegen R0 (heute 10 zu 4, p ≈ 0,18) ließe sich entscheiden.
- Ein gelerntes Modell (M9) würde erst sinnvoll, wenn auch Merkmale zur Verlängerungsentscheidung dazukommen: ausgeübte Verlängerungen, Haushaltspläne, Vorinformationen.
- Zehnmal mehr Prüflose würden die Quoten je Stufe A–F und die Menschenprüfung (heute 15 Lose) belastbar machen.

Grenze: Mehr TED-Daten gibt es kaum, die API reicht nur bis Oktober 2016; mehr Paare kosten vor allem Handsuche.
Zeig mir wo: Lab-Log §3 („Warum eine feste Regel …“) und §7 („Lohnt eine weitere Prognose-Iteration?“).

**E14. Ab welcher Trefferquote hätte sich die Prognose für einen Betrieb gelohnt?** (Bogentyp Kosten und Nutzen)
Kurzantwort: Das haben wir nicht gerechnet. Die 60 % waren eine Setzung ohne Kosten je Fehlalarm oder verpasster Ausschreibung (M1). Für eine Rechnung bräuchte man die Kosten eines zu frühen Vorbereitens und den Deckungsbeitrag eines gewonnenen Auftrags. Den Deckungsbeitrag haben wir nur als Modellgröße (25.110 € je Auftrag, Lab-Log §5, Annahmen), nicht gemessen. Ehrlich sagen: offen.
Zeig mir wo: `docs/business.md` §7.1; Lab-Log §5 (Make or Buy, Deutung).


**E15. Wer hat das Video gemacht, und warum ist es gekürzt?**
Kurzantwort: Die Animation hat Manuel KI-gestützt erstellt; wir haben sie abwechselnd gemeinsam überarbeitet. Die aktuelle Fassung mit Ton ist von Manuel (4:28), die Stimmen sind KI-generiert (ElevenLabs, steht im Abspann). Für den Vortrag hat Claude Code Runde 4 herausgeschnitten (kostenlose Liste, Vergleich 230 Verträge, Waage Selbstbauen/kostenlos, Oberpfalz, Bauplan; ca. 3:18 bis 4:14), weil die Folien danach diese Inhalte zeigen (Konkurrenz, Vergleich mit Vergabeweiser, Make or Buy); so bleiben 3:32. Schnitt in Sprechpausen, Original unverändert. Grenze: Figuren erfunden, Gespräche nachgestellt (es gab drei echte); das Video ist Veranschaulichung, kein Beleg. Tarif und Bedingungen von ElevenLabs haben wir nicht geprüft, darum ist das Video ohne Freigabe.
Zeig mir wo: `docs/video/README.md`, Abschnitt „Aktuelle Fassung (2026-11-09)“; `docs/beitraege.md`, Zeile Video; Lab-Log §6.

**E16. Was würdet ihr mit drei Monaten mehr Zeit tun?** (Bogentyp Transfer; Folie 11)
Kurzantwort, in dieser Reihenfolge:
1. **Zuerst die Nachfrage prüfen**, denn dort liegt der Engpass. Der Test ist vorbereitet, nicht durchgeführt: TED-Alarm nach Teams weiterleiten, dann drei Anrufe, Schwelle vorab festgelegt „mindestens 2 von 3 Betrieben“ nutzen Teams oder Planner, nennen mindestens 1 Stunde pro Woche und übertragen heute von Hand (K-J). Dazu das Wizard-of-Oz-Blatt mit 3 bis 5 Betrieben (eigene Schwelle: Gründe bei mindestens 3 von 5 Aufträgen ablesbar).
2. **Die Liste unabhängig prüfen:** Menschen außerhalb des Teams lesen die 15 abweichenden Lose und 30 zufällige Lose; dazu ein Leser aus einer zweiten Modellfamilie. Heute fehlen beide (Lab-Log §1 Risiken und §7 „Offene Grenzen“). Die Zahl 30 ist unsere Setzung für den Plan, nicht belegt.
3. **Eine Prognose nur mit neuen Merkmalen:** Vorinformationen (PIN, laut Iteration 2 etwa 30 pro Jahr in CPV 909) und ausgeübte Verlängerungen, geprüft als Vorwärtstest ab dem Zuschlag statt Rückwärtssuche (Lab-Log §7, „Lohnt eine weitere Prognose-Iteration?“).
4. **Unterschwellige Verfahren erst, wenn (1) trägt:** 26,7 % der Oberpfälzer Reinigungsverfahren stehen nicht auf TED (Paket B), aber eine größere Datenbasis hilft nur, wenn jemand die Liste nutzt.

Ausdrücklich **nicht:** weitere Leseregeln. Die Genauigkeit ist nicht der Engpass, die Liste gibt es kostenlos (E10, E12).
Zeig mir wo: `docs/business_case_auswahl.md`, Nachtrag K-J, Zeile 77; `docs/wizard_of_oz_blatt.md`, Zeilen 5–7; Lab-Log §1 (Tabelle Risiken, Zeile „KI-Methode“), §5 (Paket B) und §7.

---

## Teil C: Wer antwortet worauf (festgelegt)

**Aufteilung (festgelegt):** Ludwig spricht Folien 1, 2, 5, 6, 7, 9; Manuel spricht Folien 3, 4, 8, 10, 11. Laut Bewertungsbogen gehen die Fragen an das Teammitglied, das den Teil **nicht** präsentiert hat (`docs/bewertung_LN.md`, Zeile 29). Also: **Fragen zu Ludwigs Folien beantwortet Manuel, Fragen zu Manuels Folien beantwortet Ludwig.** Maßgeblich ist die Folie, auf die sich die Frage bezieht (Zuordnung unten; die Notiz der Folie 11 in `src/report/vortrag.py` nennt dieselben Folien für die Transferfragen). Passt eine Frage auf zwei Folien, gilt die erstgenannte; der andere ergänzt höchstens einen Satz.

| Frage | Bezug (Folie) | antwortet |
|---|---|---|
| M1 Warum ±3 Monate und 60 %? | 2 (Kriterium in der Einleitung), Anhang 13 | **Manuel** |
| M2 28,8 % gegen 17,3 % mehr als Zufall? | 8 (McNemar in der Notiz), Anhang 14 | **Ludwig** |
| M3 6 Monate nach Ansicht der Daten? | 8, Anhang 14 | **Ludwig** |
| M4 Welche Baseline? | 8 (R0 und R1 im Code), Anhang 15 | **Ludwig** |
| M5 KI-Leser derselben Modellfamilie | 9, Anhang 15 | **Manuel** |
| M6 Nur die 15 abweichenden Lose? | 5 | **Manuel** |
| M7 Leakage im Backtest | 8 (Regel vor dem Lauf eingefroren) | **Ludwig** |
| M8 Besseres Maß als die Trefferquote? | 8, Anhang 14 | **Ludwig** |
| M9 Feste Regel statt gelerntes Modell | 8 | **Ludwig** |
| M10 Ausreißer | 8 (Pipeline, Aufbereitung) | **Ludwig** |
| M11 Zielwechsel Prognose → Liste | 2 (Video Runde 2 und 3), Anhang 12 | **Manuel** |
| L1 Parameter ändern | 8 (Prognoseregel im Code) | **Ludwig** |
| L2 Trennung von Entwicklung und Test | 9 | **Manuel** |
| L3 Fehlwerte umstellen | 8 (Liste mit Stufen A–F) | **Ludwig** |
| L4 Seed zeigen | 9 (Stichproben mit Seed) | **Manuel** |
| L5 Diagramm erzeugen | 8, Anhang 14 | **Ludwig** |
| E1 Demo nach dem Nein | 7 | **Manuel** |
| E2 Was soll ein Betrieb morgen tun? | 10 | **Ludwig** |
| E3 Wie belastbar sind drei Gespräche? | 3 | **Ludwig** |
| E4 Andere Nische, anderer Standort | 10 (Notiz Folie 11: „Folien 6 und 10“) | **Ludwig** |
| E5 Unterhalb der EU-Schwelle (Paket B) | 9 (die Null), Ausblick auf 6 | **Manuel** |
| E6 Doppeltes Datenvolumen | 10 | **Ludwig** |
| E7 Konkurrenz so spät gesehen | 9 (laut Notiz Folie 11), Bezug 4 | **Manuel** |
| E8 KI-Fehler, selbst bemerkt | 9 | **Manuel** |
| E9 Manuels Beitrag | – | **jeder für sich** (eigene Angaben, nichts annehmen) |
| E10 Warum nicht einfach Vergabeweiser? | 4 | **Ludwig** |
| E11 Wer würde zahlen? | 3 (Gespräche); falls an Folie 6 gestellt: Manuel | **Ludwig** |
| E12 Knapp unter dem Kriterium | 10 (Grenzen), Anhang 15 | **Ludwig** |
| E13 Zehnmal so viele Daten | 8 | **Ludwig** |
| E14 Ab welcher Trefferquote lohnt es? | 6 (Deckungsbeitrag im Make-or-Buy-Modell) | **Manuel** |
| E15 Video | 2 | **Manuel** |
| E16 Drei Monate mehr Zeit | 11 | **Ludwig** |

Ergebnis: Manuel 12 Fragen (M1, M5, M6, M11, L2, L4, E1, E5, E7, E8, E14, E15), Ludwig 19 (M2–M4, M7–M10, L1, L3, L5, E2–E4, E6, E10–E13, E16), E9 jeder für sich. Ludwig hat mehr, weil die Technikfolie 8 bei Manuel liegt.

**Was jeder dafür vorbereiten muss (nicht mehr der eigene Teil, sondern der des anderen):**
- **Manuel** (Folien 1, 2, 5, 6, 7, 9):
  - Folie 9: Live-Nachweis L2 selbst ausführen können (Einzeiler Überschneidung 0, dann `git log --oneline --reverse 4f50436^..f6583cc`, Teil A (b)) und die Grenzen dazu sagen (Commit-Zeiten setzen wir selbst). Dazu L4 (Seed, Teil A (d)) und E8 (`docs/ki_irrwege.md`, Spalte „Bemerkt durch“).
  - Folie 5: M6 (15 abweichende Lose: 7 Höchstende statt Grundlaufzeit, 4 Losebene) und M5 (KI-Leser; eigene Lesung der 15 Lose, 14/15, aber als Teammitglied nicht unabhängig).
  - Folie 6: Make or Buy in `reports/make_or_buy.md` und Lab-Log §5 lesen; Kernsatz: Eigenbau gegen kostenlose Dienste im Basismodell nie günstiger, das ist eine Modellkonstruktion, keine Messung (Lab-Log §1, Zeile 137). E14 (Deckungsbeitrag nur als Modellgröße).
  - Folien 2 und 7: M1, M11, E1, E15 (eigene Angaben zum Video).
- **Ludwig** (Folien 3, 4, 8, 10, 11):
  - Folie 8: Code-Nachweis L1 (Parameter ändern, Teil A (a)), dazu L3, L5 und M2–M4, M7–M10. Die Regel steht in `src/model/baseline.py`; die Varianten sind nachträglich, kein neuer Test.
  - Folie 3: E3 und E11 (Gespräche; Ludwig hat die neun Anrufe geführt, `docs/beitraege.md`; Notizen in `docs/business.md` §8.9).
  - Folien 4, 10, 11: E2, E4, E6, E10, E12, E13, E16.

## Übungsplan Kreuzverhör (20 min)

Ziel: Jeder übt genau die Fragen, die er im Vortrag beantworten muss, also die zu den Folien des **anderen**.

**Vorbereitung (vor dem Start, nicht in den 20 min):** Ludwigs Windows-Laptop, PowerShell im Wurzelordner des Repos, vorher `chcp 65001` (sonst erscheinen „±“, „–“ und Umlaute als Ersatzzeichen, Hinweis in Teil A), Schriftgröße im Terminal mindestens 20 pt. Die Befehle aus Teil A (a) bis (e) in eine Textdatei zum Kopieren legen (außerhalb des Repos, z. B. auf dem Desktop), damit nichts abgetippt wird.

| Zeit | Was | Wer |
|---|---|---|
| 0:00–6:00 | Manuel führt L1, L2 und L3 einmal selbst auf Ludwigs Laptop aus (Befehle aus der Textdatei) und vergleicht die Ausgabe mit Teil A. L1 und L3 beantwortet im Vortrag zwar Ludwig, Manuel soll sie aber im Notfall zeigen können. | Manuel tippt, Ludwig schaut zu |
| 6:00–12:00 | **Runde 1:** Manuel zieht je eine M-, L- und E-Frage aus seiner Spalte in Teil C (Folien 1, 2, 5, 6, 7, 9). Ludwig stellt sie und stoppt die Zeit; danach je 30 s Rückmeldung. | Manuel antwortet |
| 12:00–18:00 | **Runde 2:** Ludwig zieht je eine M-, L- und E-Frage aus seiner Spalte (Folien 3, 4, 8, 10, 11). Manuel stellt sie und stoppt. | Ludwig antwortet |
| 18:00–20:00 | Notieren, welche Antwort länger als 45 s war oder ohne Datei blieb; diese Frage beim nächsten Durchgang zuerst ziehen. | beide |

**Regeln für jede Antwort:** höchstens 45 Sekunden, nach dem Muster **Zahl – Grenze – Datei** (z. B. „28,8 % statt 60 % · 52 Paare, Rückwärtssuche · `reports/backtest_iteration5.md`“). Bei L-Fragen zählt die Zeit ab dem ersten Tastendruck. Eine Fangbehauptung aus Teil D pro Runde einstreuen.

## Teil D: Fangbehauptungen

Der Bogen 5 nennt den Typ „Falschbehauptung: erwartet wird Widerspruch mit Begründung“. Auf diese Sätze freundlich widersprechen, mit Zahl und Quelle.

| Behauptung (mögliche Falle) | Richtig ist | Quelle |
|---|---|---|
| „28,8 % schlägt die Baseline signifikant.“ | Nein. Nur R1 trifft 10-mal, nur R0 4-mal; exakter McNemar-Test p ≈ 0,18. Beide liegen weit unter 60 %. | `reports/sensitivitaet_iteration5.md`, Zeile 11; Lab-Log §3 |
| „66 von 70 heißt, die Liste ist zu 94 % korrekt.“ | Nein. Gemessen ist Übereinstimmung mit dem Vergleichswert zweier KI-Leser derselben Modellfamilie, teilweise zirkulär (gleiches Feld). Menschliche Prüfung nur 15 Lose durch ein Teammitglied (14/15). | Lab-Log §4 und §7 („Zulässige Aussagen“) |
| „26,7 % der Verfahren liegen unter der EU-Schwelle.“ | Nein. 32 von 120 Oberpfälzer Reinigungsverfahren wurden **nicht auf TED gefunden**. Der Datensatz hat kein Schwellenfeld, den Wert haben wir nicht geprüft. B1 (33 %) ist nicht entscheidbar (Wilson 19,6–35,2 %). | `reports/oeffentlichevergabe_robustheit.md`, Zeilen 128 und 143 |
| „Vergabeweiser ist schlechter als eure Liste.“ | Nein, nicht belegt. Abweichung bei 27 von 230 Losen (11,7 %), meist andere Zählweise: Vergabeweiser nennt ein Ende je Verfahren, nicht je Los; von den 15 Abweichungen in 10b sind 7 Höchstende statt Grundlaufzeit und 4 Losebene. Zählt das Höchstende als richtig, bleibt 3 : 0, p = 0,25. | Lab-Log §0 und §5 |
| „Die 6 Monate habt ihr aus den Daten optimiert.“ | Nein. Der Vorlauf war gesetzt (Projektplan T3.3.4; Schätzung aus den Paaren, T3.2.1, bewusst gestrichen) und vor dem Lauf in `src/model/baseline.py` eingefroren. Nachträglich ist 6 trotzdem der beste Vorlauf (28,8 %). Das zeigt die Sensitivität, ist aber kein neuer Test. Ehrlich dazu: Der Anker Höchstende wurde nach Ansicht eines Teils der Paare gewählt (M3). | `docs/projektplan.md`, Zeilen 186 und 194; `reports/sensitivitaet_iteration5.md` |
| „Ihr habt 11 von 24 Vorgängern gefunden.“ (Folie 2) | Nein. 11 von 24 **Vorschlägen** waren richtig (Präzision 45,8 %); gefunden wurden 11 von 38 Vorgängern = 28,9 % (Trefferquote). Beide Schwellen verfehlt. | `docs/iterationen.md`, Zeilen 407–408 |
| „Der Median der Abweichung ist +0,6 Monate, die Prognose liegt also richtig.“ | Nein. Die Lage stimmt im Mittel, die Streuung ist riesig (mittleres Quartil −10,8 bis +14,3 Monate); nur 15 von 52 im Fenster. | M8; `docs/lab_log_bilder/diagramm_abweichung.png` |

**Außerdem nicht sagen:**
- „Vergabeweiser liest falsch“, „kein Unterschied“, „Vorsprung belegt“ ohne den Zusatz „auf Los- und Definitionsebene“.
- „Die Liste ist korrekt“, „fehlerfrei“, „V1 bis V8 erfüllt“.
- „Selbst bauen ist teuer“ (das Modell zeigt nur: Der Preis ist kein Vorteil des Eigenbaus).
- „Betriebe wollen das“ oder „würden zahlen“ (n = 3).
- „0 %“ oder „genau 27 %“ für Paket B.
- „Iteration 11“ (richtig: Nachträge nach Iteration 10).

## Technik-Checkliste

- Eigener Laptop (Ludwigs Windows-Laptop) und Adapter für den Beamer mitnehmen; Anschluss vorher testen.
- Ton testen: Video auf Folie 2 im Raum kurz anspielen, Lautstärke einstellen.
- USB-Stick: `docs/vortrag/vortrag_vergabe_radar.pptx`, beide MP4 (`docs/video/franz_video_ton_kurz.mp4`, 3:32; `docs/video/franz_video_ton.mp4`, 4:28) und eine Kopie des Repos.
- `docs/demo/live_demo.html` vor dem Vortrag im Browser öffnen (Folie 7); PowerShell mit `chcp 65001` und großer Schrift offen lassen (Teil A).
- Ausgeblendete Folien 12 bis 17 in der Bildschirmpräsentation über **Nummer + Enter** aufrufen; vorher einmal testen (z. B. `16` + Enter für die Sicherung).
- Probedurchlauf mit Stoppuhr, **Ziel 14:30** (Puffer 30 s gegen 15:00). Zwischenzeiten laut Zeitbudget in der Notiz der Folie 11: **4:45** Ende Folie 2 (Wechsel zu Manuel) · **7:30** Ende Folie 4 (Wechsel zu Ludwig) · **10:45** Ende Folie 7 (Wechsel zu Manuel) · **13:00** Ende Folie 9 (Wechsel zu Manuel für Folien 10 und 11).
