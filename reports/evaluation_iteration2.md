# Evaluation Iteration 2

> Erstellt am 2026-10-23 vom Subagenten `evaluator` (nur Lesezugriff, keine Dateien geändert).
> **Eingaben:** Hypothese, Kriterien K1–K5 und alle datierten Änderungen in `docs/iterationen.md` (Abschnitt Iteration 2); Iterationsreport `reports/ergebnis_iteration2.md`; Quellreports, Skripte, Phasendokumente und Annahmen (vollständige Liste am Ende).
> **Eigene Prüfungen:** Nachrechnungen (Summen, Wilson-Intervalle), Grep in `data/processed/zuordnung_q2_2026.csv` [CSV-Z], `data/processed/k5_vertraege.csv` [CSV-K5], im Vorgänger-Pool `data/raw/ted_search/DEU_result_cpv909_20161001_20261022/` [Pool] und in der Original-XML `data/raw/ted_xml/k2_20261023/` [XML]. Dazu zwei Webstichproben auf ted.europa.eu (775273-2024, 441725-2026). Die Webstichproben liefen über ein Zusammenfassungswerkzeug und sind deshalb weniger streng als ein XML-Abgleich.

> **Nachtrag von Claude (2026-10-23), außerhalb des Evaluator-Texts:** Der Bericht ist unten unverändert wiedergegeben. Zum offenen
> Punkt „Git-Beleg der Reihenfolge“: `git show 3fa8418:docs/iterationen.md` enthält bereits K2 „≥ 80 % (angepasst 2026-10-23)“,
> die Zeile K5 und den Block „Anpassung an den Projektplan“. Commit 3fa8418 entstand um 09:26 MESZ, vor allen Downloads und
> Auswertungen, die in 2b212e3 (11:01 MESZ) eingingen.

---

## Evaluation Iteration 2

Quellenkürzel wie im Report: [Z] `reports/zuordnung_iteration2.md`, [K] `reports/kennzahlen_iteration2.md`, [RR] `reports/rueckreichweite_909.md`, [P] `reports/k2_pruefliste.md`, [X] `reports/k2_auszuege.md`, [V] `reports/k2_vorbewertung.md`, [DU] `docs/phasen/02_data_understanding.md`, [IT] `docs/iterationen.md`, [PP] `docs/projektplan.md`, [E] `reports/ergebnis_iteration2.md`.

### Gesamturteil

- **Die Zahlen im Report stimmen.** Alle Summen und Intervalle, die ich nachgerechnet habe, passen zu den Quellen (Einzelheiten unten).
- **Die Hypothese ist im Wortlaut bestätigt (K1), sagt aber wenig aus.** Das räumt der Report selbst ein.
- **Das entscheidende Kriterium K2 ist deutlich und robust verfehlt.** Gemessen sind 5 von 30, also 16,7 %. Auch bei meiner großzügigsten eigenen Wertung sind es höchstens 7 von 30 (23,3 %; Wilson 11,8–40,9 %). Die Obergrenze liegt damit unter 50 %.
- **Die vorab festgelegte Regel ist ausgelöst:** „K2 < 50 % → Idee anpassen / zurück zu Phase 1“. Das Entscheidungstor in [PP] ist nicht bestanden.
- **K4 ist sauber erfüllt.** Gilt aber, wie [K] selbst zeigt, nur für die Zeit ab 2025.
- **K5 ist formal erfüllt, aber ein schwaches Kriterium.** Es zählt abgelaufene Verträge, nicht „zuordenbare Paare“, wie es der Projektplan verlangt.
- **Die Schwäche liegt in der Deutung, nicht in den Zahlen.** Der Report sagt, die Ursache sei „methodisch, nicht Datensichtbarkeit“. Das ist nicht belegt, denn die Sichtbarkeit (Recall) wurde nicht gemessen. Einige Befunde stützen die methodische Erklärung, darunter ein neuer Fund von mir (A30). Andere sprechen ebenso für Lücken in der Sichtbarkeit.
- **Positiv:**
  - Änderungen sind datiert und begründet.
  - Die Stichprobe ist zufällig und hat einen festen Seed.
  - Die Urteile sind mit XML belegt.
  - Die Grenzen sind offen genannt (Selbstprüfung, Nachträglichkeit, Zirkularität des Vorlaufs).
  - Ein Ergebnis gegen die eigene Hypothese wird ehrlich berichtet.

### Urteil je Kriterium

| Kriterium | Urteil | Beleg (Quelle) |
|---|---|---|
| **Hypothese** (Mehrheit der Q2-2026-Ausschreibungen hat einen früheren 909-Zuschlag desselben Auftraggebers) | erfüllt im Wortlaut, wenig aussagekräftig | Siehe K1. Bei großen Auftraggebern ist ein früherer Zuschlag fast sicher: 248 von 461 Treffern haben mehr als 10 Kandidaten [Z]. |
| **K1** ≥ 50 % mit automatisch gefundenem Vorgänger | **erfüllt (robust, aber trivial)** | 461/551 = 83,7 %, Wilson 80,3–86,5 % [Z]. Nachgerechnet: 56+39+70+48+126+122 = 461 Kandidaten-Klassen, Stufen 236+188+37 = 461, Jahre der Vorgänger summieren sich auf 461. Nur über den Namen: 441/551 = 80,0 % [Z]. Sensitivität (eigene Rechnung, [CSV-Z]): 18 der 273 gewählten eForms-Vorgänger haben eine Haupt-CPV außerhalb von 909, zum Beispiel 45450000, 45300000, 80000000. Unter der ursprünglichen Definition (Haupt-CPV 909 für eForms-Vorgänger) läge K1 daher bei mindestens (461−18)/551 = 80,4 %. 58 gewählte Vorgänger stammen aus 2026 [Z]. Sie können kaum Vorgänger eines Vertrags sein, der 2026 neu ausgeschrieben wird. |
| **K2** ≥ 80 % plausibel dieselbe Leistung (30 zufällige Treffer) | **nicht erfüllt (robust)** | 5/30 = 16,7 %, Wilson 7,3–33,6 % (nachgerechnet: 7,34–33,56 %) [P]. Meine eigene Nachprüfung: 29 von 30 Urteilen gleich, A4 Grenzfall (siehe unten). Bester Fall mit beiden „unklar“ als „ja“: 7/30 = 23,3 %, Wilson 11,8–40,9 %. Auch die Schwelle 50 % der Entscheidungsregel wird damit sicher verfehlt. |
| **K3** Anteil bestätigter Vorgänger im eForms-Format (Messwert) | Messwert vorhanden, **nicht interpretierbar** | 2/5 (A8, A24) [P]. Das n ist zu klein. Der Wert hängt außerdem an der Auswahlregel: Stufe 2 bevorzugt Vorgänger vor eForms vor eForms-Kandidaten, deren Ende außerhalb des Fensters liegt. Mit meinem Fund A30 (eForms-Vorgänger 775273-2024, siehe unten) wären es 3/6. |
| **K4** Replikation ≥ 80 % und KI-Untergrenze ≥ 75 % (Q2 2025) | **erfüllt** | 320/390 = 82,1 %, Wilson 77,9–85,5 % (nachgerechnet 77,93–85,54 %) [K]. Die Gegenprobe ergibt wieder 440/356 und reproduziert Iteration 1 [K]. Einschränkung (nachträglich, aber großes n): 2024 sind es 70,1 % (KI 67,8–72,2 %), 2023 ab 25.10. 70,7 % [K]. |
| **K5** ≥ 100 abgelaufene eForms-Verträge | **formal erfüllt, inhaltlich schwach** | 629 [K], per Grep bestätigt (629 Zeilen mit `expired=True` in [CSV-K5]). Eigene Auszählung: 187 der 629 (29,7 %) haben `renewal_max ≥ 1`, sind also womöglich verlängert und nicht ausgelaufen. Ohne diese bleiben 442. Weitere Befunde: Median-Laufzeit 12 Monate, Quartile 12/24, n = 622 [K]. 410 der 629 wurden 2024 veröffentlicht [K], also im Jahr mit nur ca. 70 % bestimmbarem Ende. Die Stadt Frankfurt am Main stellt 39 der 629 (6,2 %, Grep [CSV-K5]). |
| **Entscheidungsregel** | **ausgelöst** | K2 < 50 % → „Idee anpassen / zurück zu Phase 1“ [IT]. In [PP] lautet die Regel ohne Ursachenangabe: „Zuordnung unter 50 % … → Idee anpassen“. |

---

### Unabhängige Nachprüfung der K2-Urteile

**Vorgehen.** Ich habe [X] gelesen und eigene Urteile gebildet, bevor ich [P] und [V] geöffnet habe. Drei Angaben, die über den gekürzten Auszug hinausgehen, habe ich in der Voll-XML nachgeprüft. A30 habe ich zusätzlich im Web nachgesehen. Einschränkung: Meine Grundlage stammt aus denselben, von Claude erzeugten Auszügen (350 Zeichen). Eine wirklich unabhängige Zweitprüfung ist das daher nicht.

| Fall | Mein Urteil | Urteil [P] | Begründung / Abweichung |
|---|---|---|---|
| A2 Wenden | ja, mit Vorbehalt | ja | Dieselbe Gemeinde, dieselbe Leistungsart. Alt waren 7 Objekte mit ca. 27.700 m² Unterhaltsreinigung plus Glas; neu sind es 6 Lose. [XML 147163-2017]: „Option der mehrmaligen Vertragsverlängerung um jeweils ein weiteres Jahr“, die Angabe in [P] ist also gedeckt. **Vorbehalt:** Zwischen 2021 und 2026 kann es einen Zwischenvertrag gegeben haben, etwa national oder unter einem anderen Namen. Dann wäre 264073-2017 nicht der direkte Vorgänger. [V] nannte diesen Vorbehalt noch, [P] nicht mehr. |
| A4 Traunreut | ja (Neuzuschnitt, Teilmenge) bis unklar | unklar | [XML 529954-2022]: „2 x je um ein Jahr“, also bestätigt. Die beiden Kitas waren Teil des alten Loses 1 „Kitas und Friedhof“. **Abweichung in der Begründung:** [P] führt bei A4 den Zeitpunkt als Argument an („Zeitpunkt passt nicht sauber“). Bei A8 und A24 werden vorzeitige Neuvergaben dagegen als „ja“ gewertet. Der Zeitpunkt ist nicht Teil der K2-Definition („Objekt/Liegenschaft, Umfang“). Ein verkleinerter Umfang wird als „unklar“ gewertet (A4), ein erweiterter als „ja“ (A8). Das ist uneinheitlich, ändert aber das Ergebnis nicht. |
| A8 DPMA | ja | ja | Dieselben Gebäude, neu kommt eines hinzu. Neuvergabe lange vor Ablauf der 48 Monate. |
| A13 Bezirk Oberbayern | ja (eindeutigster Fall) | ja | Gleiche Standorte. Alt 01.10.2022–30.09.2026 ohne Verlängerung, neu ab 01.10.2026. |
| A16 WZB | ja (wahrscheinlich) | ja | Identischer Titel und identischer Hinweis auf die Pflichtbesichtigung. [XML 315851-2022]: „max. Vertragslaufzeit 48 Monate“, also bestätigt. Eine Objektadresse fehlt in den Auszügen (nur „Berlin“). |
| A24 Polizeirevier Ost Kassel | ja | ja | Gleiche Adresse Forstbachweg 80, gleiche Vertragsstruktur (3 Jahre + 4 × 1). Vorzeitig neu vergeben. |
| A25 Wupperverband | unklar | unklar | Gleicher Standort, aber andere Hausnummer (37 statt 45) und andere Leistung (Labor/Spüldienst statt Unterhalts- und Glasreinigung). |

**„Nein“-Fälle:** Ich habe alle 23 geprüft, unter anderem A1, A3, A5, A6, A9, A11, A12, A17, A19, A21, A22, A26, A27, A28, A29 und A30. Bei allen 23 komme ich zum selben Ergebnis. Die Begründungen in [P] sind zutreffend: anderes Objekt bzw. anderer Standort oder andere Leistung (Schädlingsbekämpfung, Feuerfest-Reinigung, Bauendreinigung).

**Zusätzliche Befunde, die [P] nicht enthält:**
1. **A30: Der objektgleiche Vorgänger war unter den Kandidaten und wurde nicht gewählt.**
   - Im Pool steht 775273-2024 „Unterhaltsreinigung JKI Quedlinburg“, Auftraggeber „Julius Kühn-Institut (JKI)“, Haupt-CPV 90911000, veröffentlicht 18.12.2024 [Pool, page_0049.json].
   - Laufzeit 01.01.2025–31.12.2028 [CSV-K5, Zeile 1824].
   - Laut Webansicht betreffen beide Bekanntmachungen die „Gebäudeunterhaltsreinigung in den Räumen der Liegenschaft“ Erwin-Baur-Straße 27, 06484 Quedlinburg (775273-2024 und 441725-2026, Webstichprobe).
   - Die Regel wählte stattdessen 669822-2022 (Siebeldingen). Grund: Das Ende von 775273-2024 liegt etwa 30 Monate nach der Ausschreibung, also außerhalb des Fensters von −3 bis +18 Monaten. Danach bevorzugt Stufe 2 Kandidaten vor eForms (`pick()` in `src/zuordnung_prototyp.py`, Z. 113–120).
   - Das „nein“ für das gewählte Paar ist korrekt. Der Fall zeigt aber zweierlei: Erstens versagt hier die Methode, nicht die Datenlage. Zweitens ist es die dritte vorzeitige Neuvergabe unter den objektgleichen Paaren.
2. **In [P] wurde nur das gewählte Paar geprüft, nicht die Kandidatenliste.** Ob in den 23 „nein“-Fällen ein richtiger Vorgänger unter den Kandidaten oder überhaupt auf TED existiert, ist offen. Stichprobe per Grep in den eForms-Titeln des Pools:
   - Für Schillerschule und Niddaschule (A3, A19) gibt es keinen früheren Zuschlag, nur den Zuschlag zur Ausschreibung selbst (639060-2026).
   - Ebenso für Naußlitz (A20), Lettenwald (A23), Fürstenwalde (A1), Michendorf (A5) und LBM Diez (A7).
   - Kandidaten vor eForms haben in der API keinen Titel. Für sie ist diese Suche also blind.
3. **Ein Vorgänger kann für viele Ausschreibungen gewählt werden (keine 1:1-Zuordnung)** [CSV-Z]:
   - 229946-2025 (Ebelfeldschule) ist Vorgänger von 10 Ausschreibungen,
   - 401251-2025 (Dom-Veranstaltungen) von 6,
   - 428234-2025 (PWC Westfalen) von 3.
   - In der Stichprobe stecken deshalb Klumpen (A3/A19, A1/A5). Die effektive Zahl unabhängiger Beobachtungen liegt unter 30.

---

### Forking paths und Nachträglichkeit

| Änderung (alle 2026-10-23) | Vor Kenntnis welcher Ergebnisse? | Einfluss auf das Ergebnis | Bewertung |
|---|---|---|---|
| K1: Vorgänger-Pool über `classification-cpv=909*` für **alle** Jahre | Laut [IT] nach der API-Prüfung, vor Ergebnissen. Die Begründung (keine Haupt-CPV vor eForms) ist in [DU] belegt. | Für die Zeit vor eForms war die Änderung nötig, für eForms nicht: Dort gibt es eine Haupt-CPV. Folge: 18 gewählte eForms-Vorgänger mit Haupt-CPV außerhalb von 909 [CSV-Z]. Davon 2 in der K2-Stichprobe: A21 (45300000) und A26 (45214600), beide „nein“. K1 bleibt ≥ 80,4 %. | Dokumentiert und begründet. Die Ausweitung auf eForms war nicht nötig. Sie erhöht K1 etwas und senkt K2 etwas, wirkt also nicht zugunsten des Tors. |
| K1-Nenner: Verfahren statt Notices | Nach Schritt 2, vor der Zuordnung | 551 Originale mit 551 verschiedenen `procedure-identifier` [DU]. Der Code filtert nur Änderungen heraus (`zuordnung_prototyp.py` Z. 128). Die Gleichheit ist in [DU] festgehalten. | Sachgerecht, neutral. |
| K2: 70 % → 80 % | Laut [IT] vor Schritt 2 | Keiner: 16,7 % liegt unter beiden Schwellen. | Unkritisch. |
| K5 neu (≥ 100) | Laut [IT] vor Schritt 2 | Die Schwelle 100 bei 4.905 eForms-Zuschlägen [RR] war fast sicher zu erreichen. | Kein Ergebnis-Tuning erkennbar, aber das Kriterium ist kaum riskant und anders als [PP] („zuordenbare Paare“). |
| Kandidatenauswahl nach dem ersten Lauf | Nach Gesamtzahlen (K1, Vorlauf-Median), vor jedem K2-Urteil | Die Stichprobe zieht mit Seed 20261023 aus denselben 461 Treffern (`write_checklist`, Z. 254–257). Logisch ergibt das dieselben 30 Ausschreibungen. Eine Auswahl günstiger Fälle ist dadurch ausgeschlossen, sofern Seed und Code unverändert blieben (nicht prüfbar, die erste Liste und die erste CSV sind überschrieben). Die neue Stufe 1 trifft 1 von 16, Stufe 2 3 von 10 [P]. Die Änderung hat K2 vermutlich gesenkt. | Kein Hinweis auf zielgerichtete Anpassung. Nicht prüfbar ist die Aussage „auch die erste Regel hätte viele falsche Vorgänger gewählt“ [E §5]. |
| Prüfung vollständig an Claude übertragen | – | Die Urteile fallen gegen die eigene Regel aus, und meine Nachprüfung stimmt weitgehend überein. Ein Bias zugunsten eines hohen K2 ist nicht erkennbar. | Das Risiko verlagert sich auf die **Deutung** (siehe Schwäche 2). |

**Zeitliche Reihenfolge:** `.git/logs/HEAD` zeigt am 23.10. zwei Commits: 3fa8418 um 09:26 MESZ („Iteration 2 gestartet …“) und 2b212e3 um 11:01 MESZ („Download, K4/K5, Zuordnungs-Prototyp und K2-Prüfung“). Ob K2 = 80 % und K5 schon in 3fa8418 standen, kann ich ohne Git-Befehl nicht prüfen. Das ist nachholbar mit `git show 3fa8418:docs/iterationen.md`. Bis dahin ist „vor Kenntnis der Ergebnisse“ nur durch die Selbstauskunft in [IT] belegt.

**Fazit:** Auf Ebene der Zahlen gibt es keine Forking-Path-Probleme, die das Urteil ändern. Der eigentliche Pfad, der sich verzweigt, liegt in der nachträglichen Auslegung der ausgelösten Regel.

---

### Schwächen (nach Schwere)

**Kritisch**

1. **Die Sichtbarkeit der Vorgänger (Recall) wurde nicht gemessen. Die Aussage „das Problem ist methodisch, nicht die Datensichtbarkeit“ [E §4] ist deshalb nicht belegt.** K2 misst nur die Präzision der Top-1-Auswahl. Die Befunde zeigen in beide Richtungen.
   - *Für die Methode als Ursache:*
     - Gefälle nach Kandidatenzahl: 1–2 Kandidaten 3 von 6 „ja“, mehr als 10 Kandidaten 1 von 15 [P], nachgezählt.
     - Die typischen Fehler sind „gleicher Auftraggeber, anderes Objekt“.
     - Bei A30 war ein objektgleicher Kandidat vorhanden.
   - *Für Lücken in der Sichtbarkeit:*
     - Auch bei nur 1–2 Kandidaten, wo die Auswahlregel kaum Spielraum hat, stimmt nur die Hälfte (3/6; Wilson 18,8–81,2 %). A7 und A22 haben offenbar keinen passenden Vorgänger im Pool.
     - Bei den Ausschreibungen ohne Treffer haben 6 von 15 keinen früheren Zuschlag unter ähnlichem Namen [P, B-Teil].
     - Für Frankfurter Einzelschulen findet sich in den eForms-Titeln kein früherer Zuschlag (Grep).
     - Es gibt mehr Ausschreibungen als Zuschläge (1,6 pro Zuschlag seit eForms [RR]). Das ist ungeklärt und kann bedeuten, dass Zuschläge auf TED fehlen.
   - Belegt ist nur: **Die Zuordnung auf Ebene des Auftraggebers taugt nicht.** Offen bleibt, ob eine Zuordnung auf Objektebene genug Vorgänger auf TED *findet*.
2. **Die ausgelöste Entscheidungsregel wird umgedeutet.** Der Report liest den Klammerzusatz („Nachfolger auf TED kaum sichtbar“) als Ursache, die nicht zutreffe [E §4].
   - [PP] formuliert dieselbe Regel ohne Ursache: „Zuordnung unter 50 % … → Idee anpassen“.
   - Vorab genannte Optionen waren: Facility-Services-Radar, Prognose aus Auftraggeber-Zyklen, nationale Quellen [IT].
   - Die vom Report bevorzugte Auslegung 1 (Objektebene) steht nicht auf dieser Liste. Inhaltlich entspricht sie dem Zweig „K2 50–80 % → in Phase 2 bleiben“, der für bessere Ergebnisse vorgesehen war.
   - Option 3 (nationale Quellen) wird als „durch den Befund nicht nahegelegt“ verworfen [E §4]. Das ist angesichts von Schwäche 1 verfrüht.
   - Die Umdeutung ist nicht unbegründet: Die Regel hat Präzision der Methode und Sichtbarkeit der Daten vermengt, das ist ein Konstruktionsfehler der Vorab-Festlegung. Er muss aber als **Abweichung** dokumentiert werden und darf nicht als „Regel passt nicht“ erscheinen.
3. **Die Belege zum Vorlauf sind dünn und teils zirkulär.** „Drei davon zeigen einen Vorlauf von 4–5 Monaten“ [E §3]:
   - Bei A2 wurde die Zahl der Verlängerungen (5) *aus dem Datum der neuen Ausschreibung* erschlossen. Bei A16 wurde die Ausschöpfung aller Verlängerungen angenommen.
   - Unabhängig gemessen ist nur A13 (5,1 Monate).
   - Unter den nun 6 objektgleichen Paaren (5 aus [P] plus A30) sind 3 vorzeitige Neuvergaben (A8, A24, A30). Das spricht eher gegen eine einfache Regel „Ende minus Vorlauf“ (A8) als für sie (n = 6, nur ein Hinweis).

**Mittel**

4. **K1 ist kaum trennscharf.** Es zählt jeden früheren 909-Zuschlag desselben Auftraggebers, auch 58 aus 2026 [Z] und 18 mit Haupt-CPV außerhalb von 909 [CSV-Z]. Für große Auftraggeber ist K1 fast immer erfüllt.
5. **K5 misst nicht, was das Entscheidungstor verlangt.** [PP] verlangt „genug **zuordenbare Paare** … (Richtwert: mindestens 100 abgelaufene Verträge)“. K5 zählt abgelaufene Verträge ohne Prüfung, ob ein Nachfolger auffindbar ist.
   - Eigene grobe Hochrechnung: Bei K1 × K2 ≈ 0,837 × 0,167 bekäme die jetzige Regel nur etwa 14 % der Ausschreibungen richtig zugeordnet (etwa 6–28 %, ohne Unsicherheit von K1).
   - Dazu kommen die Verzerrungen aus der Tabelle (Median 12 Monate, 29,7 % mit Verlängerungsoption, 410/629 aus 2024).
6. **Selbstprüfung, kein zweiter Prüfer.** Regel, Auszüge und Urteile stammen von Claude [IT, Nachtrag]. Meine Nachprüfung bestätigt die Urteile, nutzt aber dieselben Auszüge. Eine Übereinstimmung zwischen zwei Prüfern (z. B. Nutzer gegen Claude) fehlt. Für K2 ist das unkritisch, weil das Ergebnis eindeutig ist. Für die nächste Iteration, in der eine Schwelle knapp werden kann, ist es kritisch.
7. **Stichprobe:**
   - nur ein Quartal (Q2; Schulreinigung zum Schuljahresbeginn ist vermutlich überrepräsentiert);
   - Klumpen (A1/A5, A3/A19 mit demselben Vorgänger);
   - Teilzellen nach Stufe bzw. Kandidatenzahl mit n = 4 bis 16, also nur beschreibend.
8. **Die Nische „Haupt-CPV 909“ ist nicht nur wiederkehrende Gebäudereinigung.**
   - In der Stichprobe: A6 und A22 (Schädlingsbekämpfung), B4 (Fahrzeugreinigung), B15 (Industriereinigung im Müllheizkraftwerk), B1/B7/B12 (einmalige Bau-, Schimmel- und Bauendreinigung) [X].
   - Das sind 2 von 30 Treffern und 5 von 15 Fällen ohne Treffer.
   - Diese Fälle verzerren sowohl K1 als auch die Gründe für fehlende Treffer.
9. **Die Auswahlregel prägt K3 und den Vorlauf strukturell.**
   - Das Fenster von −3 bis +18 Monaten schließt vorzeitige Neuvergaben aus (A30).
   - Stufe 2 bevorzugt Notices vor eForms gegenüber eForms-Kandidaten mit bekanntem Ende außerhalb des Fensters.
   - Eine 1:1-Bedingung fehlt (Befund 3 oben).

**Gering**

10. „Eine Prognose nur aus der Grundlaufzeit hätte um 3–5 Jahre danebengelegen“ [E §3]: Nachgerechnet sind es bei A16 etwa 2,7 Jahre (31.08.2023 → 04.05.2026) und bei A2 etwa 4,7 Jahre (31.07.2021 → 01.04.2026). Bei A2 gilt das nur, wenn es keinen Zwischenvertrag gab.
11. Die Basisrate in [RR] rechnet mit 16 % Änderungen. Tatsächlich sind es 159/710 = 22,4 % [DU]. Damit ergeben sich grob 1.990–2.160 Verfahren pro Jahr statt 2.150–2.350 (eigene Rechnung aus 2.560 bzw. 2.780 × 0,776).
12. Die Dokumente sind nicht synchron: [PP] T2.4.4 sagt noch „Prüfung durch den Nutzer steht aus“, T2.4.3 ist offen. Dazu ein Unterschied von einer Notice zwischen der Jahrestabelle (3.772 bestimmbar, „mindestens ein Los“) und K5 (3.764 + 7 verworfen, „erstes Los“) [K]. Für das Ergebnis unerheblich.
13. Zu A2 schreibt [P] „Gleiche Leistung (Unterhalts- und Glasreinigung …)“. Die neue Ausschreibung nennt im Auszug aber „Unterhalts-, Grund- und Sonderreinigung“ in 6 Losen, Glas ist nicht sichtbar. Der Vorbehalt „Zwischenvertrag nicht ausgeschlossen“ aus [V] fehlt in [P].

---

### Alternative Erklärungen

- **Vorgänger existiert, aber nur als Ausschreibung, nicht als Zuschlag auf TED.** Seit eForms gibt es etwa 1,6 Ausschreibungs-Notices pro Zuschlag [RR], nach Abzug der Änderungen grob 1,2. Gesucht wurde nur unter Zuschlägen. Ein Abgleich mit früheren Ausschreibungen (F02 bzw. eForms competition) könnte Vorgänger finden. Diese enthalten zudem Titel, Ort und geplante Laufzeit.
- **Vorgänger unter dem Schwellenwert oder nur national veröffentlicht (A3).** Ein Beispiel könnten Frankfurter Einzelschul-Verträge mit 1 Jahr + 3 Verlängerungen sein (A3, A19). Nicht geprüft.
- **Andere Vergabestelle, anderer Name, andere CPV.** Zentrale Beschaffer (BImA, Finanzbehörde Hamburg, Beschaffungsamt des BMI, Land Hessen HCC) vergeben für viele Bedarfsträger. Namen ändern sich (B4, B5, B11, B13, B14). Vorgänger können unter Facility-Management-CPVs liegen oder nur mit 909 als Los-CPV.
- **Neuzuschnitt statt Neuausschreibung.** Lose werden neu gebündelt (A4, A8, A27). Dann gibt es gar keinen eindeutigen Vorgänger. „Dieselbe Leistung“ ist für solche Fälle nicht klar definiert.
- **Vorzeitige Neuvergabe** nach Kündigung, Insolvenz oder Umbau (A8, A24, A30). Das ist kein Zuordnungsfehler, sondern ein anderer Mechanismus für das Zielereignis.
- **Die 5 bestätigten Paare sind leichte Fälle.** 3 von 5 haben höchstens 2 Kandidaten [P]. Dass sich das Zielereignis „auf Objektebene zuordnen“ lässt [E §3], ist damit für große Auftraggeber nicht gezeigt.

---

### Fakten vs. Interpretation

- **[E §2 „Fakten“], B-Fälle:** „5 mit Vorgänger unter abweichendem Namen“ und „6 ohne früheren Zuschlag auf TED“.
  - Zum ersten Teil sagt [V]: „Ob die Treffer bei abweichendem Namen inhaltlich passen, ist nicht geprüft.“ Faktisch: 5 mit *früherem 909-Zuschlag* unter abweichendem Namen, Inhalt ungeprüft.
  - Zum zweiten Teil: Faktisch wurde *im 909-Pool per Namenssuche kein früherer Zuschlag gefunden*. Das ist nicht dasselbe wie „kein früherer Zuschlag auf TED“.
- **[E §2], „Bestätigte Paare“:** Bestätigt hat sie dieselbe Hand, die die Regel gebaut hat. Genauer wäre „von Claude als plausibel beurteilt“.
- **[E §3], Überschrift „Das Zielereignis selbst ist sichtbar und zuordenbar, wenn man auf das Objekt schaut“:** Eine Verallgemeinerung aus 5 Paaren, die eine ungenaue Regel gefunden hat. Eine Zuordnung auf Objektebene wurde nicht gemessen.
- **[E §3], „Drei davon zeigen einen Vorlauf von 4–5 Monaten … einschließlich Verlängerungen“:** Zwei der drei Werte beruhen auf erschlossenen bzw. angenommenen Verlängerungen (Schwäche 3). Die Tabelle markiert A2 zu Recht mit „angenommen“, der Fließtext nicht.
- **[E §4]:** „Nachfolger sind sichtbar (K1, bestätigte Paare), die **Methode** der Zuordnung ist zu grob“ und Option 3 „durch den Befund nicht nahegelegt, weil das Problem methodisch ist“. Das sind Interpretationen im Ton eines Befunds. K1 belegt keine Sichtbarkeit auf Objektebene.
- **[E §3], A11:** „dafür sind die Angaben in der Stichprobe vollständig“. Faktisch richtig (10 von 10 mit DATE_START/DATE_END, nachgezählt in [X]; 5 von 10 mit Verlängerung). Die Stichprobe ist aber durch die Auswahlregel bestimmt (jüngster Zuschlag vor eForms bei Treffern) und nicht zufällig.
- **Positiv:**
  - [E §5 „Grenzen“] und [Z] („Zirkulär für Stufe 1“) benennen die eigenen Schwächen offen.
  - [DU] trennt sauber und hält fest: „Für A13 heißt das: ab 2025 repliziert, für 2024 nicht“.

---

### Betroffene Annahmen

- **A3** (TED bildet relevanten Teil des Markts ab): **ungeprüft lassen, Risiko hoch.**
  - Es gibt Hinweise auf Lücken: 6 von 15 Fällen ohne Treffer ohne früheren Zuschlag im Pool; in der Gruppe mit 1–2 Kandidaten 2–3 von 6 ohne passenden Vorgänger [P]; ungeklärtes Verhältnis Ausschreibungen zu Zuschlägen [RR].
  - Weder bestätigt noch widerlegt. Nachweis entsprechend ergänzen.
- **A8** (Neuausschreibung ≈ Vertragsende minus Vorlauf): **ungeprüft lassen.**
  - Nachweis ergänzen: Unter 6 objektgleichen Paaren (A2, A8, A13, A16, A24 aus [P]; A30 aus dieser Evaluation) sind 3 vorzeitige Neuvergaben. 2 passen nur, wenn alle Verlängerungen ausgeschöpft wurden (erschlossen). 1 ist unabhängig gemessen (A13: 5,1 Monate).
  - Das ist eher ein Warnsignal als eine Stütze. „Stützt A8 nur teilweise“ [E] ist zu wohlwollend.
- **A9** (zuverlässige Zuordnung, „z. B. über Auftraggeber + CPV“): **für die Variante Auftraggeber + CPV → widerlegt.**
  - Geltungsbereich: Haupt-CPV 909, Ausschreibungen Q2 2026, Top-1-Regel aus `src/zuordnung_prototyp.py`.
  - Nachweis: K2 = 5/30 = 16,7 %, Wilson 7,3–33,6 %; auch im besten Fall höchstens 23,3 % (KI-Obergrenze 40,9 %).
  - Die Zuordnung auf Objektebene bleibt **ungeprüft**. Ich empfehle, sie als eigene Annahme zu führen (z. B. A9b), statt A9 stillschweigend umzudeuten.
- **A10** (eForms-Historie reicht für aussagekräftigen Backtest): **ungeprüft lassen, Nachweis ergänzen. Nicht „bestätigt“.**
  - Die Anzahl ist erfüllt: 629, ohne strukturierte Verlängerungsoption noch 442 [CSV-K5].
  - Die Fälle sind aber kaum repräsentativ: Median 12 statt 36 Monate, 410 von 629 aus 2024 [K].
  - Zuordenbare Paare sind nicht gezählt.
  - Dazu der vorab festgelegte Hinweis: K3 < 50 % → Formate vor eForms nötig [IT]. Bei n = 5 ist das nur ein Indiz.
- **A11** (Daten vor eForms für Laufzeiten brauchbar): **ungeprüft, mit Vermerk „vorläufig gestützt“** (analog zu A13 in Iteration 1). Nicht „bestätigt“, weil die Annahme ein hohes Risiko trägt und die Stichprobe nicht zufällig ist.
  - Nachweis: 10 von 10 Zuschlägen vor eForms (F03/F06) verweisen über REF_NOTICE auf F02/F05 mit DATE_START/DATE_END, 5 von 10 mit Verlängerung [X], nachgezählt.
  - Geltungsbereich: Vorgänger, die die Regel gewählt hat (2017–2023), keine Zufallsstichprobe. Wie oft F03 ganz ohne REF_NOTICE vorkommen (etwa bei Verfahren ohne vorherige Bekanntmachung), ist offen.
- **A12** (Haupt-CPV reicht für die Nische): **ungeprüft lassen, Nachweis ergänzen.** Haupt-CPV 909 enthält Schädlingsbekämpfung (A6, A22), Fahrzeug- und Industriereinigung (B4, B15) und einmalige Bau- bzw. Sonderreinigung (B1, B7, B12) [X].
- **A13** (≥ 80 % bestimmbares Laufzeitende): **ungeprüft → bestätigt, mit engem Geltungsbereich.** Das ist durch die vorab festgelegte Replikation gedeckt.
  - Gilt für: Haupt-CPV 909, Notice-Ebene, Veröffentlichung Q2 2025 (82,1 %, KI 77,9–85,5 %, Schwelle vorab) und Q3 2026 (80,9 %).
  - Gilt **nicht** für 2023/2024: 70,7 % bzw. 70,1 % (KI 67,8–72,2 %) [K]. Diese Jahresauswertung war nachträglich, hat aber ein großes n.
  - Weil die Backtest-Fälle überwiegend aus 2024 stammen, gehört diese Einschränkung ausdrücklich in den Nachweis.
- **A14:** **ungeprüft**, Risiko unverändert hoch. A9 (in der geprüften Variante) und A10 tragen derzeit nicht.

---

### Was für ein belastbares Urteil fehlt

1. **Eine Messung der Sichtbarkeit:** Für eine Zufallsstichprobe von Ausschreibungen von Hand und mit Suchprotokoll prüfen, ob es überhaupt einen objektgleichen Vorgänger auf TED gibt. Gesucht wird unter Zuschlägen **und** früheren Ausschreibungen, in allen Formaten seit 2016. Erst damit lässt sich „Methode“ von „Sichtbarkeit“ trennen.
2. **Ein zweiter, unabhängiger Prüfer** für mindestens einen Teil der Urteile, mit Übereinstimmungsmaß.
3. **Kontrolle der Kandidatenlisten** der 23 „nein“-Fälle auf einen objektgleichen Kandidaten. A30 zeigt, dass es solche Fälle gibt.
4. **Git-Beleg der Reihenfolge:** `git show 3fa8418:docs/iterationen.md` (enthält es K2 = 80 % und K5?).
5. **Ein zweites Quartal** (z. B. Q3/Q4) wegen Saisonalität und Schulreinigung.
6. **Repräsentative Prüfung von A11:** Zufallsstichprobe von Zuschlägen vor eForms (z. B. 30 aus 2018–2023) auf REF_NOTICE und Laufzeit.
7. **Belege für Verlängerungen:** Vertragsänderungen (can-modif, im Pool nicht enthalten) könnten gezogene Verlängerungen zeigen. Das würde die Zirkularität bei A2/A16 auflösen.

---

### Empfehlung

**Idee anpassen, wie es die vorab festgelegte Regel verlangt. Nicht weiter zu Phase 3.** Konkret empfehle ich eine weitere Data-Understanding-Iteration, in der „Zuordnung auf Objektebene“ und „Sichtbarkeit der Vorgänger“ **getrennt** gemessen werden. Sie braucht neue, vorab committete Kriterien und eine harte Abbruchregel zu den vorab genannten Optionen (nationale Quellen, Prognose aus Auftraggeber-Zyklen).

Diese Wahl ist als **Abweichung** von der Optionsliste in [IT] zu dokumentieren. Die Begründung muss belegt sein: Die Regel vermengte Präzision der Methode und Sichtbarkeit der Daten, und A30 zeigt mindestens einen Fall, in dem die Methode versagte, obwohl die Daten da waren. Die Begründung darf nicht „die Regel passt nicht“ lauten. Option 3 (nationale Quellen, A3) sollte nicht verworfen, sondern als Ausweg vorab festgelegt werden, falls die Sichtbarkeit zu niedrig ausfällt.

Die Entscheidung trifft der Nutzer.

---

### Empfehlungen für Iteration 3 (vorab festzulegen und vor Beginn zu committen)

1. **Population vorab abgrenzen:**
   - Haupt-CPV 90911/90919 (ggf. 90910).
   - Ausschluss nach vorab festgelegter Stichwortliste: Bau-, Bauend-, Schimmel-, Fahrzeug- und Industriereinigung, Schädlingsbekämpfung.
   - Ein anderes Quartal als Q2 2026.
   - Höchstens 2 Ausschreibungen je Auftraggeber.
2. **Getrennte Datensätze:** Die Regeln für die Objektebene werden auf einem Entwicklungsdatensatz gebaut (z. B. die 30 K2-Paare plus Q1 2026). Gemessen wird nur auf einem neuen Testdatensatz. Sonst passt man die Regel an die 30 bekannten Fälle an.
3. **Vorab-Kriterien (Vorschlag, Zahlen sind Diskussionsgrundlage):**
   - **V1 Sichtbarkeit:**
     - Stichprobe: n = 60 zufällige Original-Ausschreibungen.
     - Vorgehen: Handsuche je Fall mit festem Zeitbudget und Suchprotokoll, unter Zuschlägen und früheren Ausschreibungen.
     - Gemessen: Anteil mit objektgleichem Vorgänger auf TED.
     - „Objektgleich“ vorab definieren: gleiche Adresse oder gleicher Liegenschaftsname **und** überschneidende Leistungsart. Neuzuschnitt bzw. Teilmenge ist eine eigene Kategorie. Der Zeitpunkt gehört nicht zur Definition.
     - Regel: ≥ 50 % → weiter. 30–50 % → nur Teilsegment (z. B. Auftraggeber mit wenigen Verträgen). < 30 % → zurück zu Phase 1 (nationale Quellen oder Auftraggeber-Zyklen).
   - **V2 Präzision der Objektzuordnung** auf dem Testdatensatz: ≥ 80 % **und** Wilson-Untergrenze ≥ 60 %.
   - **V3 Recall:** Anteil der in V1 gefundenen Vorgänger, die der Algorithmus findet: ≥ 60 %.
   - **V4 Zweitprüfung:** Der Nutzer beurteilt mindestens 20 Paare blind, ohne Claudes Urteil zu sehen. Übereinstimmung ≥ 85 % (oder Cohens κ ≥ 0,6), sonst Definition schärfen, bevor V2 zählt.
   - **V5 Backtest-Basis:** Hochgerechnete Zahl objektgleicher, zuordenbarer Paare mit bestimmbarem Vertragsende des Vorgängers ≥ 100. So verlangt es [PP], im Unterschied zu K5.
   - **V6 A11, repräsentativ:** Zufallsstichprobe von 30 Zuschlägen vor eForms aus 2018–2023. Anteil mit über REF_NOTICE erreichbarer Laufzeit ≥ 80 %.
   - **Explorativ, mit vorab genannter Folge:** Anteil vorzeitiger Neuvergaben unter den objektgleichen Paaren. Liegt er über etwa 30 %, wird das Prognoseziel „Ende minus Vorlauf“ in Phase 1 neu bewertet (A8).
4. **Regeldesign:**
   - 1:1-Bedingung (ein Vorgänger nur einmal je Objekt).
   - Kein Zeitfenster als Auswahlkriterium (vermeidet Zirkularität beim Vorlauf).
   - Frühere Ausschreibungen als Vorgängerquelle einbeziehen.
   - Für eForms Haupt-CPV statt CPV-Liste.
   - Erste Läufe und Prüflisten versionieren, statt sie zu überschreiben.
5. **Dokumentation:**
   - In [E] die Formulierungen aus „Fakten vs. Interpretation“ korrigieren.
   - In [RR] die Basisrate mit 22,4 % Änderungen neu angeben.
   - [PP] T2.4.3/T2.4.4 aktualisieren.
   - Die Zeile „Iteration 3 = Erste Prognose und Backtest“ in [IT] und [PP] erst ändern, wenn der Nutzer entschieden hat.

---

### Geprüfte Dateien (absolute Pfade)

- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\docs\iterationen.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\ergebnis_iteration2.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\zuordnung_iteration2.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\kennzahlen_iteration2.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\rueckreichweite_909.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\k2_pruefliste.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\k2_auszuege.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\k2_vorbewertung.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\reports\evaluation_iteration1.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\src\zuordnung_prototyp.py
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\src\kennzahlen_iteration2.py
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\src\k2_xml_auszug.py (nur Grep der Kernstellen)
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\src\ted_counts.py (nur Grep der Abfragen)
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\docs\phasen\02_data_understanding.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\docs\annahmen.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\docs\projektplan.md
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\data\processed\zuordnung_q2_2026.csv
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\data\processed\k5_vertraege.csv
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\data\raw\ted_search\DEU_result_cpv909_20161001_20261022\ (page_0049.json, page_0061.json u. a. per Grep)
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\data\raw\ted_xml\k2_20261023\147163-2017.xml, 315851-2022.xml, 529954-2022.xml
- c:\Users\ludwi\OneDrive\Dokumente\GitHub\vergabe_radar\.git\logs\HEAD
- Web: https://ted.europa.eu/de/notice/775273-2024/html, https://ted.europa.eu/de/notice/441725-2026/html
