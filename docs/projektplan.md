# Projektplan Vergabe-Radar

Grobplanung für das Gesamtprojekt, aufgeteilt in Aufgaben (A) und Unteraufgaben (A.1, A.2 …).
Die Detailplanung je Iteration (Hypothese, Erfolgskriterium mit Schwelle, Zeitrahmen) entsteht weiterhin mit
`/iteration-start` und steht in `docs/iterationen.md`. Dieser Plan gibt nur die Richtung und die Abhängigkeiten vor.

**Stand:** 2026-10-25. Iteration 3 abgeschlossen (Entscheidung: in Phase 2/3 bleiben, letzter Verbesserungsversuch der Zuordnung).
Nächster Schritt: Iteration 4 mit `/iteration-start`.
**Zeitangaben** sind grobe Schätzungen für Arbeit neben dem Studium und werden in `/iteration-start` konkretisiert.
**Schwellenwerte** in diesem Plan sind Vorschläge. Verbindlich werden sie erst, wenn sie **vor** der Arbeit in
`docs/iterationen.md` stehen.

## Überblick

Das Projekt hat drei parallele Stränge:

| Strang | Frage | Wo im Prozess |
|---|---|---|
| **T: Technik und Daten** | Lässt sich die Neuausschreibung aus TED-Daten zuverlässig vorhersagen? | CRISP-DM-Phasen 2 bis 5 |
| **G: Geschäft** | Zahlt jemand dafür, und wer genau? | CRISP-DM-Phase 1 und 6 |
| **P: Prozess und Rahmen** | Bleibt das Projekt nachvollziehbar, sauber und rechtlich unbedenklich? | laufend |

| Iteration | Fokus | Phasen | Grobe Dauer | Status |
|---|---|---|---|---|
| 1 | Machbarkeit der Daten | 1 → 2 | 1 Tag | **abgeschlossen** |
| 2 | Zielereignis sichtbar und zuordenbar? | 2 (→ 3) | 1 Tag | **abgeschlossen** (Idee anpassen) |
| 3 | Sichtbarkeit der Vorgänger und Zuordnung über das Objekt | 2 (→ 3) | 2 Tage | **abgeschlossen** (in Phase 2/3 bleiben) |
| 4 | Letzter Verbesserungsversuch der Objekt-Zuordnung (neue Testdaten) | 2/3 | 2 bis 3 Wochen | nächster Schritt |
| 5 | Erste Prognose und Backtest | 3 → 4 → 5 | 2 bis 3 Wochen | geplant |
| 6 | Verbesserung der Prognose | 3 → 4 → 5 | 2 bis 3 Wochen | geplant |
| 7 | Erster Kundentest | 6 → 1 | 2 bis 4 Wochen | geplant |
| 8+ | Ausbau oder Neuausrichtung | je nach Ergebnis | offen | geplant |

_Geändert am 2026-10-23 nach Iteration 2: Iteration 3 (Phase 2) eingeschoben; die Abschnitte T3–T6 unten gelten jetzt für die
Iterationen 4–7. Ihre Nummern bleiben zur Nachvollziehbarkeit unverändert._
_Geändert am 2026-10-25 nach Iteration 3: Iteration 4 (T2c) eingeschoben; die Abschnitte T3–T6 gelten jetzt für die Iterationen 5–8._

Der Strang G läuft von Anfang an mit und wartet nicht auf die technischen Ergebnisse.

---

## Strang T: Technik und Daten

### T1 Iteration 1: Machbarkeit der Daten (abgeschlossen)
- [x] T1.1 TED Search API recherchieren, Zuschläge für Deutschland laden (15.706 Notices)
- [x] T1.2 Datenqualitätsreport erstellen
- [x] T1.3 Parsing per Stichprobe gegen die Original-XML prüfen (15 Notices)
- [x] T1.4 Laufzeit aus Beginn und Ende nachberechnen
- [x] T1.5 Evaluation durch den Subagenten `evaluator`
- [x] T1.6 Entscheidung: Gebäudereinigung als vorläufige Arbeitsnische, zurück zu Phase 2

### T2 Iteration 2: Zielereignis sichtbar und zuordenbar? (Phase 2)

**Ziel:** Klären, ob Neuausschreibungen auf TED erscheinen, wie weit die Daten zurückreichen und ob sich alte Zuschläge
und neue Ausschreibungen zuordnen lassen. Das sind die riskantesten offenen Annahmen (A3, A9, A10, A11).

- [x] **T2.1 Iteration planen**
  - [x] T2.1.1 `/iteration-start` ausführen
  - [x] T2.1.2 Hypothese, Erfolgskriterien mit Zahlen und Abbruchregeln vorab in `docs/iterationen.md` eintragen
    _(2026-10-23: K1–K5; K2 und K5 am selben Tag vor Ergebnissen an das Entscheidungstor unten angeglichen)_
- [ ] **T2.2 Auftragsbekanntmachungen (competition) für CPV 909 laden**
  - [x] T2.2.1 Passende `form-type`- und `notice-type`-Werte in der API-Doku klären
    _(2026-10-23: `form-type=competition`, `notice-type` z. B. `cn-standard`; Filter `main-classification-proc=909*`)_
  - [x] T2.2.2 `src/ted_download.py` erweitern, Rohdaten unverändert nach `data/raw`
    _(2026-10-23: Parameter `--form-type`, `--cpv`, `--cpv-field`; 710 Ausschreibungen Q2 2026, davon 551 Original-Verfahren)_
  - [x] T2.2.3 Anzahl pro Jahr bestimmen (Basisrate des Prognoseziels)
    _(2026-10-23: `reports/rueckreichweite_909.md`; 2024/2025 je ca. 2.560–2.780 Ausschreibungs-Notices, davon ca. 16 % Änderungen)_
  - [x] T2.2.4 Prüfen, ob Vorinformationen (PIN) als Frühsignal existieren und wie häufig sie sind
    _(2026-10-23: 5 PIN mit Haupt-CPV 909 in Q2 2026, praktisch bedeutungslos)_
- [ ] **T2.3 Rückreichweite klären (A10, A11)**
  - [x] T2.3.1 Zuschläge für CPV 909 seit Ende Oktober 2023 laden
    _(2026-10-23: sogar seit Okt. 2016, 15.361 Notices, davon 4.905 eForms mit Haupt-CPV 909)_
  - [x] T2.3.2 Verteilung der Enddaten auswerten: Wie viele Verträge sind bis heute ausgelaufen?
    _(2026-10-23: 629 abgelaufen, aber Median-Laufzeit nur 12 Monate; `reports/kennzahlen_iteration2.md`)_
  - [ ] T2.3.3 Prüfen, ob Daten vor eForms (alte TED-Formulare) Laufzeiten enthalten und wie sie abrufbar sind
    _(teilweise, 2026-10-23: Such-API ab Ende Okt. 2016, vor eForms ohne Laufzeit; in der XML alter Ausschreibungen (F02)
    vorhanden, alte Zuschläge (F03) ohne Laufzeit, bisher 1 Fall)_
  - [ ] T2.3.4 Entscheiden, ob die eForms-Historie für einen Backtest reicht oder ältere Daten nötig sind
- [x] **T2.4 Erste Zuordnung Zuschlag zu Neuausschreibung (A9)**
  - [x] T2.4.1 Merkmale für die Zuordnung festlegen (Auftraggeber, CPV, Ort, Titel, Beschreibung, Kennungen)
    _(2026-10-23: erste Fassung nur Auftraggebername und -kennung; Ort/Titel nur zur Auswahl unter Kandidaten)_
  - [x] T2.4.2 Einfachen Score bauen (nachvollziehbar vor komplex)
    _(2026-10-23: `src/zuordnung_prototyp.py`, Regel statt Score; K1 83,7 %, `reports/zuordnung_iteration2.md`)_
  - [x] T2.4.3 30 Paare aus allen Score-Bereichen **von Hand prüfen** und Trefferquote festhalten
    _(2026-10-23: Zufallsauswahl statt Score-Bereiche; geprüft von Claude auf Wunsch des Nutzers; K2 = 5/30 = 16,7 %,
    `reports/k2_pruefliste.md`; Evaluator in 29/30 einig)_
  - [x] T2.4.4 Typische Fehlerfälle dokumentieren (Losaufteilung, Fusion von Auftraggebern, neuer Zuschnitt)
    _(2026-10-23, `reports/ergebnis_iteration2.md`: große Auftraggeber mit vielen Parallelverträgen, zu grobe Kennungen,
    abweichende Namensschreibweisen, Neuzuschnitt, vorzeitige Neuvergabe, Nicht-Reinigung unter CPV 909)_
- [x] **T2.5 Replikation der 80-%-Quote (A13)**
  - [x] T2.5.1 Ein unabhängiges Quartal wählen (z. B. Frühjahr 2025), Definition und Schwelle vorab festlegen
  - [x] T2.5.2 Quote „Laufzeitende bestimmbar“ berechnen, Konfidenzintervall angeben
    _(2026-10-23: Q2 2025 82,1 %, KI 77,9–85,5 %; aber 2024 nur 70,1 %)_
- [ ] **T2.6 Fehlende Laufzeiten verstehen**
  - [ ] T2.6.1 Etwa 20 der 84 nicht bestimmbaren Notices von Hand prüfen
  - [ ] T2.6.2 Ursachen einteilen (Freitext, unbefristet, falsches Formular, echte Lücke)
    _Verschoben am 2026-10-23 nach Iteration 3 (T3.1): für das Entscheidungstor nach Iteration 2 nicht nötig, Zeitrahmen knapp._
    _Nachtrag 2026-10-23: T3.1 ist jetzt Teil von T4 (Iteration 4), siehe unten._
  - [ ] T2.6.3 Klären, ob BT-36/536/537 die Laufzeit mit oder ohne Verlängerungen meinen (eForms-Doku)
    _(teilweise, 2026-10-23: BT-36 laut Definition mit Optionen und Verlängerungen, BT-537 ohne Aussage; Praxis ungeprüft)_
- [ ] **T2.7 Abschluss**
  - [x] T2.7.1 Report `reports/` mit Fakten und Interpretation getrennt _(2026-10-23: `reports/ergebnis_iteration2.md`)_
  - [x] T2.7.2 Evaluator prüfen lassen _(2026-10-23: `reports/evaluation_iteration2.md`; Empfehlung: Idee anpassen)_
  - [ ] T2.7.3 `/iteration-ende`, Commit, Tag `iteration-2`
    _(2026-10-23: `/iteration-ende` erledigt, Entscheidung „Idee anpassen“; Commit und Tag durch den Nutzer)_

**Entscheidungstor nach Iteration 2 (Vorschläge, vorab verbindlich festzulegen):**
_Verbindlich festgelegt am 2026-10-23 als K1–K5 in `docs/iterationen.md` (K2 ≥ 80 %, K5 ≥ 100 abgelaufene eForms-Verträge)._
**Ergebnis 2026-10-23: nicht bestanden** (K2 = 16,7 %). Entscheidung: Idee anpassen, weitere Phase-2-Iteration mit Zuordnung über das
Objekt (als Abweichung dokumentiert in `docs/iterationen.md`).
- Zuordnung: mindestens 80 % von 30 geprüften Paaren korrekt, **und** genug zuordenbare Paare für einen Backtest
  (Richtwert: mindestens 100 abgelaufene Verträge)
  → weiter mit Iteration 3.
- Zuordnung gut, aber Historie zu kurz → ältere TED-Daten erschließen (A11), bevor Iteration 3 beginnt.
- Zuordnung unter 50 % oder Neuausschreibungen erscheinen kaum auf TED → Idee anpassen: andere Nische, andere Datenquelle
  (zusätzlich nationale Vergabeplattformen, A3) oder Projektziel neu bewerten.

### T2b Iteration 3: Sichtbarkeit der Vorgänger und Zuordnung über das Objekt (Phase 2)

_Neu am 2026-10-23 nach dem Entscheidungstor von Iteration 2. Vorschläge aus `reports/evaluation_iteration2.md`; verbindlich erst nach
`/iteration-start`._

- [x] **T2b.1** Iteration planen: Kriterien V1–V6 und Abbruchregel vorab festlegen und committen
- [x] **T2b.2** Population enger fassen (90911/90919, Ausschlussliste, anderes Quartal, höchstens 2 Ausschreibungen je Auftraggeber)
- [x] **T2b.3** Sichtbarkeit messen: Zufallsstichprobe, Handsuche mit Protokoll unter Zuschlägen **und** früheren Ausschreibungen
  _(V1 = 63,3 %)_
- [x] **T2b.4** Zuordnung über das Objekt (Adresse, Liegenschaft, Titel), auf Entwicklungsdaten bauen und auf Testdaten messen
  (1:1-Zuordnung, kein Zeitfenster als Auswahlkriterium) _(V2 = 45,8 %, V3 = 28,9 %, verfehlt)_
- [x] **T2b.5** Zweitprüfung: Der Nutzer beurteilt mindestens 20 Paare blind _(V4 = 17/20, mit Abweichungen vom Plan)_
- [x] **T2b.6** A11 repräsentativ: 30 zufällige Zuschläge vor eForms auf REF_NOTICE und Laufzeit prüfen _(V6 = 25/30)_
- [x] **T2b.7** Zuordenbare Paare mit bekanntem Vorgänger-Ende zählen und den Anteil vorzeitiger Neuvergaben messen (A16)
  _(V5 = 328/Jahr, vorzeitig 2/36)_
- [x] **T2b.8** Abschluss: Report, Evaluator, `/iteration-ende`, Tag `iteration-3`
  _(2026-10-25: Evaluator `reports/evaluation_iteration3.md`, Dokumente aktualisiert; Commit b3c3475, Tag `iteration-3`)_

**Ergebnis 2026-10-25:** V1 knapp erfüllt, V2/V3 verfehlt. Entscheidung: in Phase 2/3 bleiben, ein letzter Verbesserungsversuch (T2c).

### T2c Iteration 4: Letzter Verbesserungsversuch der Objekt-Zuordnung (Phase 2/3)

_Neu am 2026-10-25 nach Iteration 3. Vorschläge aus `reports/evaluation_iteration3.md`; verbindlich erst nach `/iteration-start`._

- [x] **T2c.1** Iteration planen: Kriterien, Stichprobenumfang (etwa 60–70 Testfälle) und Abbruchkriterium vorab festlegen
  _(2026-10-25: W1–W6, 70 Testfälle, in `docs/iterationen.md`)_
- [x] **T2c.2** Aufräumen aus Iteration 3: Vorgänger-Enddaten T26, T56, T18 korrigieren; Belegstärke T18–T30 in `gt.csv` nachtragen;
  Originaldatei der Nutzerurteile ins Repo _(2026-10-25; dazu Rechercheur auf Regeln 1.1, Population Iteration 4)_
- [x] **T2c.3** Objekt- und Leistungsart-Merkmale auf Los-Ebene, auch vor eForms (XML, Volltextsuche `FT`)
- [x] **T2c.4** Regel verbessern auf Q2 + Q3 2026 (jetzt Entwicklungsdaten): Leistungsart hart prüfen, Geschwisterverfahren über
  Objektlisten und Flächen trennen, **kein Zeitfenster**; einfrieren per Commit
- [x] **T2c.5** Neue Testdaten Q1 2026: Testprobe ziehen, Handsuche nach Urteilsregeln 1.1 **vor** dem Regel-Lauf
  _(2026-10-26: 70 Fälle, Handsuche in 5 Teilen, Ground Truth d43c547; Regel-Lauf ec4733e)_
- [ ] **T2c.6** Zweitprüfung mit frischen Paaren (vorher nicht angesehen), gezielt schwach belegte Treffer und „kein Vorgänger“-Fälle
- [x] **T2c.7** Saisonalität prüfen: Populationsgröße je Quartal (Hochrechnung V5)
  _(2026-10-26: Q4 2025 381, Q1 538, Q2 488, Q3 486 = 1.893 pro Jahr)_
- [ ] **T2c.8** Parallel (Strang G): Produkt mit manueller Prüfung bewerten (Prüfaufwand je Fall, Preis)
- [ ] **T2c.9** Abschluss: Report, Evaluator, `/iteration-ende`, Tag `iteration-4`

### T3 Iteration 3: Erste Prognose und Backtest (Phasen 3, 4, 5)
_Jetzt Iteration 4 (geändert am 2026-10-23)._

**Ziel:** Eine einfache Regel liefert nachweislich brauchbare Prognosen, gemessen an echten Neuausschreibungen.

- [ ] **T3.1 Datenaufbereitung (Phase 3)**
  - [ ] T3.1.1 Tabelle auf Los-Ebene bauen (eine Zeile pro Vertrag oder Los)
  - [ ] T3.1.2 Laufzeitende vereinheitlichen und mit Herkunft kennzeichnen (direkt, Beginn plus Dauer, unbekannt)
  - [ ] T3.1.3 Auftraggebernamen normalisieren, wenn möglich über Kennungen
  - [ ] T3.1.4 Zuordnung Zuschlag zu Neuausschreibung als Tabelle festschreiben
  - [ ] T3.1.5 Skripte nach `src/prepare/` und `src/ingest/` ordnen, Bereinigungsregeln dokumentieren
- [ ] **T3.2 Baseline-Modell (Phase 4)**
  - [ ] T3.2.1 Vorlaufzeit aus bestätigten Paaren schätzen (Abstand Veröffentlichung Neuausschreibung zu Vertragsende)
  - [ ] T3.2.2 Regel: erwartete Neuausschreibung = Laufzeitende minus Vorlaufzeit
  - [ ] T3.2.3 Zwei Varianten: ohne Verlängerung und mit voll ausgeschöpften Verlängerungen
  - [ ] T3.2.4 Umgang mit unbefristeten Verträgen festlegen
- [ ] **T3.3 Backtest (Phase 5)**
  - [ ] T3.3.1 Nur Verträge verwenden, deren prognostizierter Termin in der Vergangenheit liegt (keine Zensierungsfehler)
  - [ ] T3.3.2 Kennzahlen: Trefferquote im Fenster ±3 Monate, Präzision, durchschnittlicher Vorlauf
  - [ ] T3.3.3 Verzerrungen offenlegen (kurze Verträge überrepräsentiert, Verträge ohne Verlängerung)
  - [ ] T3.3.4 Vergleich mit einer naiven Referenz (z. B. immer „Laufzeitende minus 6 Monate“)
- [ ] **T3.4 Abschluss:** Report, Evaluator, `/iteration-ende`, Tag `iteration-3`

**Entscheidungstor (Vorschläge):**
- Trefferquote ±3 Monate mindestens 60 % und besser als die naive Referenz → weiter mit Iteration 4 (Verbesserung).
- 40 bis 60 % → Verbesserungen in Iteration 4 gezielt auf die häufigsten Fehlerursachen ausrichten.
- Unter 40 % → zurück zu Phase 1 oder 2: Eignet sich die Nische, oder ist das Prognoseziel falsch gewählt?

### T4 Iteration 4: Verbesserung der Prognose (Phasen 3, 4, 5)

- [ ] **T4.1 Verlängerungen aus Freitext extrahieren**
  - [ ] T4.1.1 Texte aus BT-54 und BT-57 sichten, typische Formulierungen sammeln
  - [ ] T4.1.2 Regelbasierte Extraktion bauen (Anzahl, Dauer je Verlängerung, Ausübungsfrist)
  - [ ] T4.1.3 Erfassungsquote an 30 handgeprüften Fällen messen
- [ ] **T4.2 Verhalten der Auftraggeber nutzen**
  - [ ] T4.2.1 Historische Ausschreibungszyklen je Auftraggeber auswerten
  - [ ] T4.2.2 Vorlaufzeit je Auftraggeber statt global schätzen
  - [ ] T4.2.3 Vertragsänderungen (can-modif) auswerten: Zeigen sie ausgeübte Verlängerungen?
- [ ] **T4.3 Prognose als Zeitfenster statt Einzeldatum**
  - [ ] T4.3.1 Wahrscheinlichstes Fenster und Unsicherheit je Vertrag angeben
  - [ ] T4.3.2 Dem Kunden verständlich darstellen (z. B. „Neuausschreibung wahrscheinlich Q2 2027“)
- [ ] **T4.4 Modellerweiterung nur bei Bedarf**
  - [ ] T4.4.1 Statistisches oder ML-Modell nur, wenn Regeln nachweislich an Grenzen stoßen
  - [ ] T4.4.2 Vergleich gegen die Regel-Baseline im selben Backtest
- [ ] **T4.5 Weitere Nischen testen (optional)**
  - [ ] T4.5.1 Sicherheitsdienste und Winterdienst mit derselben Pipeline prüfen (Facility-Services-Radar)
  - [ ] T4.5.2 Winterdienst über mehrere Quartale prüfen (Saisonalität)
- [ ] **T4.6 Abschluss:** Report, Evaluator, `/iteration-ende`, Tag `iteration-4`

### T5 Iteration 5: Erster Kundentest (Phase 6, dann Phase 1)

- [ ] **T5.1 Erstes Produkt als manuelle Liste**
  - [ ] T5.1.1 Format festlegen (Tabelle oder PDF: Auftraggeber, Objekt, voraussichtliches Fenster, Quelle, Sicherheit)
  - [ ] T5.1.2 Liste für eine Region erzeugen, Stichprobe der Einträge von Hand gegenprüfen
  - [ ] T5.1.3 Quellenangabe und Hinweis auf Unsicherheit je Eintrag
- [ ] **T5.2 Testkunden gewinnen** (siehe Strang G, G4)
- [ ] **T5.3 Pipeline automatisieren**
  - [ ] T5.3.1 Ablauf von Datenabruf bis Liste in einem Skript bündeln
  - [ ] T5.3.2 Monatlicher Lauf, Protokoll, Fehlerbehandlung
  - [ ] T5.3.3 Versand per E-Mail (zunächst manuell auslösbar)
- [ ] **T5.4 Feedback auswerten**
  - [ ] T5.4.1 Wurde die Liste gelesen und genutzt?
  - [ ] T5.4.2 Welche Einträge waren nützlich, welche falsch?
  - [ ] T5.4.3 Preisreaktion festhalten
- [ ] **T5.5 Abschluss:** Report, Evaluator, `/iteration-ende`, Tag `iteration-5`, Feedback in Phase 1 einarbeiten

### T6 Ausbau oder Neuausrichtung (je nach Ergebnis)
- [ ] T6.1 Weitere Nischen oder Regionen
- [ ] T6.2 Dashboard nur, wenn zahlende Kunden es verlangen
- [ ] T6.3 Zusätzliche Datenquellen (nationale Vergabeplattformen, Vorinformationen) bei Abdeckungslücken (A3)
- [ ] T6.4 Abbruch oder Umbau, falls die Entscheidungstore nicht bestanden werden. Das ist ein gültiges Ergebnis.

---

## Strang G: Geschäft

### G1 Wettbewerb und Markt prüfen (A2, A3)
- [ ] G1.1 Ausschreibungsdienste sichten (z. B. DTAD, Vergabeportale, kommerzielle Anbieter): Bieten sie Prognosen?
- [ ] G1.2 Funktionen und Preise festhalten, Lücken benennen
- [ ] G1.3 Marktgröße abschätzen: Anzahl Reinigungsfirmen im Zielbereich, Anteil der öffentlichen Aufträge
- [ ] G1.4 Abdeckung durch TED abschätzen: Welcher Teil der Reinigungsaufträge liegt über den EU-Schwellenwerten? (A3)

### G2 Kundengespräche (A1, A15)
- [x] G2.1 Zielgruppe festlegen (Größe, Region, Rolle: Geschäftsführung, Vertrieb, Ausschreibungsverantwortliche)
  _(2026-10-23: Oberpfalz; 71 Firmen mit TED-Zuschlägen als Startliste, dazu kleine lokale Firmen; `docs/business.md`)_
- [x] G2.2 Gesprächsleitfaden schreiben (offene Fragen zum heutigen Vorgehen, kein Verkaufsgespräch)
  _(2026-10-23: `docs/business.md`, Abschnitt 3)_
- [ ] G2.3 Fünf bis zehn Gespräche führen, jeweils kurz protokollieren
- [ ] G2.4 Auswerten: Wie finden Firmen heute Ausschreibungen? Was würde ein früherer Hinweis wert sein? Wie viele Monate Vorlauf bräuchten sie?
- [ ] G2.5 Ergebnisse in `docs/annahmen.md` (A1, A15) und Phase 1 eintragen

### G3 Angebot und Preis
- [ ] G3.1 Nutzenversprechen in einem Satz formulieren und mit Gesprächspartnern testen
- [ ] G3.2 Preishypothese testen (zunächst grob, etwa monatliches Abo je Firma)
- [ ] G3.3 Zahlungsbereitschaft als Aussage festhalten, nicht als Zusage werten

### G4 Pilotkunden
- [ ] G4.1 Zwei bis drei Firmen für den Kundentest in Iteration 5 gewinnen
- [ ] G4.2 Erwartungen klären (Testphase, Feedback, Vertraulichkeit)
- [ ] G4.3 Nach dem Test nachfragen: Würde die Firma weiterzahlen, und zu welchem Preis?

**Entscheidungstor (Vorschläge):**
- Nach G2: Zeigt mindestens ein Teil der Gesprächspartner ein konkretes Problem und Interesse an einer Testliste → Pilot.
  Sagt niemand, dass früheres Wissen hilft, ist das ein ernstes Warnsignal, unabhängig von der Prognosegüte.
- Nach G4: Mindestens eine Firma ist bereit zu zahlen → weiterbauen. Sonst Ausrichtung ändern oder Projekt beenden.

---

## Strang P: Prozess und Rahmen

### P1 Dokumentation und Versionierung
- [ ] P1.1 Nach jeder Iteration `/iteration-ende`, Commit und Tag
- [ ] P1.2 `git push` und `git push origin <tag>` nach jedem Abschluss
- [ ] P1.3 Annahmen in `docs/annahmen.md` nur mit Nachweis ändern
- [ ] P1.4 Skriptordner an die Struktur in `docs/CRISP-DM.md` anpassen (`src/ingest/`, `src/prepare/`, `src/model/`, `src/report/`)

### P2 Qualitätssicherung
- [ ] P2.1 Vor jeder Auswertung Stichprobe gegen das Original (TED-Webansicht oder XML)
- [ ] P2.2 Erfolgskriterien und Schwellen vor der Arbeit festlegen
- [ ] P2.3 Evaluator am Ende jeder Iteration, seine Kritik unverändert dokumentieren
- [ ] P2.4 Ergebnisse in neuen Zeitfenstern replizieren, bevor Annahmen als bestätigt gelten

### P3 Rechtliches und Organisatorisches (vor dem ersten Verkauf klären)
- [ ] P3.1 Nutzungsbedingungen der TED-Daten prüfen (Weiterverwendung, Quellenangabe)
- [ ] P3.2 Datenschutz prüfen: Auftraggeber sind meist Behörden, Ansprechpersonen in Bekanntmachungen sind personenbezogene Daten
- [ ] P3.3 Gewerbeanmeldung und Steuerfragen vor dem ersten Geld klären
- [ ] P3.4 Haftungs- und Hinweistext für Prognosen (keine Zusicherung, Quelle öffentlich)
- [ ] P3.5 Vertragslage bei Nebentätigkeit neben Arbeit oder Studium prüfen

Hinweis: Dieser Plan ersetzt keine Rechts- oder Steuerberatung. Für P3 empfiehlt sich eine Beratung, etwa über die
Gründungsberatung der Hochschule oder die IHK.

### P4 Technische Hygiene
- [ ] P4.1 `requirements.txt` aktuell halten
- [ ] P4.2 Rohdaten unverändert lassen, Auswertungen per Skript reproduzierbar machen
- [ ] P4.3 Projekt aus OneDrive in einen lokalen Ordner verschieben, falls Synchronisationsprobleme auftreten
- [ ] P4.4 Sicherung von `data/` (liegt nicht in Git) und bei Bedarf Neu-Download dokumentieren

---

## Abhängigkeiten und kritischer Pfad

```
T2 (Zuordnung und Historie) ──► T3 (Baseline und Backtest) ──► T4 (Verbesserung) ──► T5 (Kundentest)
        │                                                                               ▲
G1 + G2 (Wettbewerb, Gespräche) ───────────────────────────────────────────────────► G4 (Pilotkunden)
```

- Iteration 3 beginnt erst, wenn das Entscheidungstor nach Iteration 2 bestanden ist.
  _Nachtrag 2026-10-23: Tor nicht bestanden; die erste Prognose (jetzt Iteration 4) beginnt erst, wenn Iteration 3 eine tragfähige
  Zuordnung über das Objekt zeigt._
- Die Kundengespräche (G2) laufen ab sofort parallel und sind unabhängig von der Technik.
- P3 (Rechtliches) muss vor dem ersten bezahlten Angebot erledigt sein, nicht vor dem Pilot mit kostenloser Testliste.

## Größte Risiken (nach Annahmen)

| Risiko | Annahme | Gegenmaßnahme im Plan |
|---|---|---|
| Neuausschreibungen erscheinen kaum auf TED (unter dem Schwellenwert) | A3 | T2.2, G1.4, ggf. T6.3 |
| Zuordnung von Zuschlag und Neuausschreibung scheitert | A9 | T2.4 |
| eForms-Historie reicht nicht für einen Backtest | A10, A11 | T2.3 |
| Vorlaufzeit schwankt stark, Prognose zu ungenau | A8 | T3.2, T4.2, T4.3 |
| Niemand zahlt für den Hinweis | A1, A15 | G2, G3, G4 |
| Bestehende Anbieter decken das Feld ab | A2 | G1 |

## Fortschritt pflegen

- Erledigte Aufgaben in diesem Dokument abhaken (`- [x]`).
- Verschobene oder geänderte Aufgaben nicht löschen, sondern mit Datum und Grund direkt darunter vermerken.
- Neue Aufgaben aus Iterationen hier ergänzen, damit der Plan aktuell bleibt.
