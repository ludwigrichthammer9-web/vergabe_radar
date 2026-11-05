# Paket C: Ursachen der Stufe F und Fehlertyp „Dauerfeld = Gesamtdauer einschließlich Option“

Stand 2026-11-05. Erzeugt mit `src/report/stufe_f_ursachen.py` (Aufruf im Kopf), Tabellen in `reports/stufe_f_ursachen.csv` (Teil 1) und `reports/stufe_f_fehlertyp.csv` (Teil 2). Die Liste (Fassung 9) wurde nicht geändert. Rohdaten: `data/raw/ted_search/DEU_result_cpv909_20231025_20260930_lostext`; TED-XML der 21 Bekanntmachungen neu geladen nach `data/raw/ted_xml/stufe_f_20261105/`.

## Teil 1: Warum haben 33 Lose kein Ende?

### Fakten

Stufe F heißt (`src/report/beispiel_liste.py`, Regel 2): kein Ende der Grundlaufzeit und keine Schätzung. In `reports/beispiel_liste_oberpfalz.csv` sind das 33 von 130 Losen (25,4 %) in 21 Bekanntmachungen. Bei allen 33 sind `contract-duration-start-date-lot`, `-end-date-lot`, `-period-lot` und `-period-oth-lot` leer; im XML fehlt jedes Element PlannedPeriod, DurationMeasure, StartDate, EndDate (vom Skript geprüft, sonst Abbruch). Jedes Los hat genau eine Ursache; Vorrang bei mehreren Gründen: 5, 3, 4, 2, 1.

| Ursache | Lose | Bekanntmachungen (Lose) |
|---|---|---|
| 1a kein Laufzeitfeld, im Text nur eine Verlängerung | 10 | 266771-2024 (2), 267158-2024 (2), 446124-2025 (2), 420740-2026 (2), 480569-2026 (2) |
| 1b kein Laufzeitfeld, im Text weder Laufzeit noch Verlängerung | 8 | 788951-2023 (2), 437343-2024 (2; Los 5, 10), 555698-2024 (1), 685373-2025 (2), 420148-2026 (1) |
| 2 Dauer oder Datum nur im Freitext, von der Regel nicht gelesen | 14 | 33610-2024 (1), 683177-2024 (2; Los 3, 4), 226358-2025 (3), 503542-2025 (2), 722107-2025 (1), 722423-2025 (1), 215440-2026 (1), 454420-2026 (1), 579178-2026 (1), 580747-2026 (1) |
| 3 Rahmenvereinbarung ohne feste Laufzeit | 0 | – |
| 4 „unbestimmt“/„bis auf Weiteres“ | 0 | – |
| 5 keine Gebäudereinigung | 1 | 556275-2026 (1) |
| 6 Zuordnung Los zu Feld unklar | 0 | – |
| 7 andere | 0 | – |
| **Summe** | **33** | 21 Bekanntmachungen |

Wörtliche Beispiele (Feld: Text):
- 1a, 266771-2024, `renewal-description-lot`: „Verlängerung des Vertrages von 2 x 1 Jahr möglich“. 480569-2026: „… verlängert er sich jeweils um ein weiteres Jahr (siehe Punkt 1.28 der Vorbemerkungen/Vorgaben).“ Die Grundlaufzeit steht nur in den Vergabeunterlagen.
- 1b, 420148-2026, `description-lot`: „Für 22 verschiedene Objekte der Stadt Regensburg wird die Glasreinigung ausgeschrieben.“ Bei 437343-2024 und 555698-2024 steht im XML `framework-agreement = none`, es ist also keine Rahmenvereinbarung.
- 2, 722107-2025, `renewal-description-lot`: „Der Vertrag beginnt am 01.01.2026 und endet am 31.12.2028.“ 683177-2024, `option-description-lot`: „Beginn der Leistung: 01.01.2025 Der Vertrag wird auf die Dauer von 1 Jahr geschlossen … Der Vertrag endet spätestens am 31.12.2028“. 226358-2025, `description-lot`: „Der Vertrag wird auf 5 Jahre befristet …“ (ohne Beginn). 33610-2024: „… endet spätestens mit Ablauf des 31.03.2030.“ (Vertragsende nur als „31.03. des jeweiligen Jahres“).
- 5, 556275-2026: Titel „Kesselreinigungsarbeiten an der Ofenlinie 1 und 4 inkl. Strahlentrostungsarbeiten“, Haupt-CPV 90910000, „Rahmenvereinbarung zur Durchführung von Kesselreinigungsarbeiten“. Der Text nennt zusätzlich „Vertragsende (31.12.2027)“ und „endet spätestens mit Ablauf des 31.12.2029“.

### Schätzung: Was könnte eine einfache Zusatzregel „Datum/Dauer aus dem Freitext“ lesen?

Nur Schätzung; Regex-Regel im Skript (`zusatzregel`), Ergebnis stimmt mit meiner Handlesung überein, nicht an Stichproben geprüft, Liste unverändert.

| Art | Lose | Lose (Bekanntmachung) |
|---|---|---|
| A Enddatum steht im Text | 4 | 722107-2025, 722423-2025, 215440-2026, 454420-2026 |
| B Beginn + Dauer | 4 | 579178-2026, 580747-2026, 683177-2024 (2) |
| C Rückrechnung: „endet spätestens 31.08.2029“ minus 2 × 12 Monate | 2 | 503542-2025 (2) |
| E nur Dauer ohne Beginn (Veröffentlichung + 5 Jahre, nur geschätzt) | 3 | 226358-2025 |
| nur Höchstende lesbar | 1 | 33610-2024 |
| nichts lesbar (Ursache 1) | 18 | – |
| Ursache 5: Ende lesbar, aber keine Gebäudereinigung | 1 | 556275-2026 |

Damit hätten bis zu 10 der 33 Lose ein Ende der Grundlaufzeit (30,3 %), 3 weitere ein geschätztes; 18 (54,5 %) blieben ohne Ende, weil die Bekanntmachung nichts enthält. In der Oberpfalz-Liste sänke Stufe F von 33 auf höchstens 20 Lose.

### Deutung (Interpretation, nicht belegt)

- Mehr als die Hälfte der Lose ohne Ende (18 von 33) ließe sich auch mit besserer Regel nicht lesen; das ist eine Grenze der Quelle, kein Regelfehler. Das stützt die Aussage, dass die Liste Lücken lässt und der Blick in die Bekanntmachung bleibt.
- Auffällig: Neumarkt i.d.OPf. (6 der 14 Fälle der Ursache 2) und Amberg-Sulzbach (Ursache 1a) schreiben die Laufzeit in Freitext bzw. gar nicht; hier könnte ein Auftraggeber-Muster vorliegen (nur aus diesen 21 Bekanntmachungen, nicht verallgemeinerbar).
- Die Ursachen 3, 4, 6 kommen nicht vor; die Rahmenvereinbarungs-Vermutung trifft für diese 33 nicht zu.
- Ob 556275-2026 als „keine Gebäudereinigung“ zählt, ist eine Einschätzung (Kesselreinigung, CPV 90910000 allgemein).

## Teil 2: Fehlertyp „Dauerfeld enthält die Gesamtdauer einschließlich Option“

### Geprüfte Menge (Fakten)

Alle Lose in `data/processed/vertragsliste_909.csv` (9.325 Lose) mit `gl_herkunft` = beginn_plus_dauer (49 Lose, 24 Bekanntmachungen), text_laufzeit_option (49 Lose, 22), text_festlaufzeit (102 Lose, 9) und text_zunaechst (207 Lose, 116). Zusammen **407 Lose in 171 Bekanntmachungen**. Prüfung durch KI-Lesung (keine zweite Person, nicht unabhängig): beginn_plus_dauer, text_laufzeit_option und text_festlaufzeit Satz für Satz; bei text_zunaechst nur der Satz mit dem Datum des Listenwerts (alle 116 Zeilen gelesen), nicht der gesamte Text. Die vollständige Liste der Bekanntmachungen mit Urteil und Beleg steht in `reports/stufe_f_fehlertyp.csv`.

| Herkunft | Bek. | Lose | Fehler | unklar | kein Fehler |
|---|---|---|---|---|---|
| beginn_plus_dauer | 24 | 49 | **12 Lose / 5 Bek.** | 2 / 2 | 35 / 17 |
| text_laufzeit_option | 22 | 49 | 0 | 3 / 1 | 46 |
| text_festlaufzeit | 9 | 102 | 0 | 1 / 1 | 101 |
| text_zunaechst | 116 | 207 | 0 | 0 | 207 |
| **zusammen** | 171 | 407 | **12 Lose / 5 Bek.** | **6 Lose / 4 Bek.** | 389 Lose |

Bei den Textherkünften ist das Datum aus dem Text gelesen, das Dauerfeld spielt für den Listenwert keine Rolle; dort kann der Typ nicht in der gleichen Form auftreten.

### Fehler und unklare Fälle (beginn_plus_dauer, Listenwert gegen Text)

| Bekanntmachung | Los | Listenwert (Ende GL) | Text-Befund | Urteil | wörtlicher Beleg |
|---|---|---|---|---|---|
| 119677-2025 (Stadt Kaarst) | 1 | 31.12.2029 (5 Jahre ab 01.01.2025) | GL wäre 31.12.2026 | **Fehler** | `option-description-lot`: „1. Januar 2025 bis 31. Dezember 2026 mit Verlängerungsoption (bei unterlassener Kündigung) bis maximal 31. Dezember 2029“ |
| 122700-2025 (Stadt Kaarst) | 1–7 | 31.12.2029 | Los 4–7: 31.12.2026; Los 1–3: 31.08.2027 (Zuordnung über den Beginn, zwei Textblöcke für sieben Lose) | **Fehler** (7 Lose) | „1. Januar 2025 bis 31.Dezember 2026 mit Verlängerungsoption … bis maximal 31. Dezember 2029“; „optionale Verschiebung … auf 1. September 2025 bis 31. August 2027 …“ |
| 495440-2026 (Europäische Kommission, JRC Karlsruhe) | 1 | 31.07.2030 (48 Monate) | GL wäre 31.07.2027 (Länge der Verlängerung nicht genannt, 12 + 3 × 12 = 48 passt) | **Fehler** | `renewal-description-lot`: „Der Vertrag wird für einen Anfangszeitraum von 12 (zwölf) Monate, verlängerbar 3 (drei) geschlossen.“ |
| 527230-2026 (Universität Regensburg) | 1, 2 | 31.07.2027 (10 Monate) | GL wäre 31.01.2027 | **Fehler** (bekannt) | `description-proc`: „Interimsvergabe aufgrund Dringlichkeit 01.10.26 - 31.01.27 mit 6 Monaten Option“ |
| 533946-2026 (Universität Regensburg) | 1 | 30.09.2031 (5 Jahre) | GL wäre 30.09.2028 | **Fehler** | `option-description-lot`: „2 Jahre Festlaufzeit + 3x1 Jahr Option“ |
| 495951-2025, 496173-2025 (Land Schleswig-Holstein) | je 1 | 31.10.2031 (72 Monate) | Vertrag ohne feste Grundlaufzeit | unklar (anderer Typ) | „Der Vertrag beginnt am 01.11.2025 und läuft auf unbestimmte Zeit. Aus vergaberechtlichen Gründen ist der Auftraggeber grundsätzlich gehalten, die Vertragsleistung nach 6 Jahren neu zu vergeben.“ |
| 612313-2026 (Polizeiinspektion, Sachsen-Anhalt) | 1–3 | 31.08.2029 | Text „3 Jahren (01.09.2025 bis 31.08.2028)“, Feld Beginn 01.09.2026 | unklar | Textjahr vermutlich Übernahmefehler; Option nicht in der Dauer |
| 758702-2025 (Wiesbaden Congress) | 2 | 30.09.2027 | Feldbeginn 01.12.2025, Text „beginnend am 01.10.2025 und endet am 30.09.2027“ | unklar | Listenwert und Höchstende (30.11.2029) passen nicht zusammen |

Kein Fehler: 17 von 24 Bekanntmachungen der Herkunft beginn_plus_dauer. Davon 11 mit bestätigender Textstelle (z. B. 697344-2025: „vom 1.1.2026 bis 31.12.2027 mit zweimaliger Verlängerungsoption“; 199184-2026: Dauer 24 Monate, „zwei Mal um jeweils 12 Monate, bis max. zum 30.03.2030“), 4 ohne Widerspruch, aber ohne Bestätigung (109604-2026, 325419-2024, 409547-2026, 9955-2026), 2 ohne Text, also nicht prüfbar (755291-2023, 779220-2024). Einzelbelege je Bekanntmachung: CSV.

### Deutung (nicht belegt)

- Der Fehlertyp ist häufiger als im Nachtrag zu 527230-2026 angenommen: dort stand, nur diese Bekanntmachung zeige den Widerspruch; hier sind es 5 von 24 (12 von 49 Losen), also vier weitere Bekanntmachungen (10 weitere Lose) in der Gruppe beginn_plus_dauer. Die grobe Textprüfung damals hat sie nicht erfasst (Formulierungen „bis maximal“, „2 Jahre Festlaufzeit + 3x1 Jahr Option“, „Anfangszeitraum von 12 Monate, verlängerbar 3“).
- Mögliche Ursache (nur Codelesung, nicht getestet): In `laufzeit()` in `src/prepare/vertragsliste.py` greift Regel 1b nur bei `gl_h == "enddatum"`; bei Herkunft beginn_plus_dauer wird sie nicht angewendet. Bei 122700-2025 kam der Text zusätzlich nicht an, weil zwei Textblöcke für sieben Lose nicht eindeutig zugeordnet werden.
- Folge für die Liste: In den 5 Bekanntmachungen ist das Ende der Grundlaufzeit zu spät (um 2 bis 4 Jahre), das Höchstende bleibt meist richtig. Auswirkung auf die Messungen der Iterationen 6 bis 10 nicht geprüft (nur 12 von 9.325 Losen, 0,13 %).

### Grenzen

- Nur die vier Herkünfte wurden geprüft. Das Dauerfeld kann auch bei Herkunft `enddatum` die Gesamtdauer sein (Enddatum = Höchstende); das ist der Fehlertyp der Iteration 6 und hier nicht untersucht. Keine Hochrechnung auf alle Lose.
- Eine Lesung durch die KI, keine Gegenprüfung; Texte mit anderen Formulierungen können übersehen sein. text_zunaechst nur satzweise geprüft.
- Zuordnung Textblock zu Los bei 122700-2025 über den Beginn, bei 495440-2026 Länge der Verlängerung angenommen.
- Teil 1: Ursachenzuordnung ist Handlesung der Rohtexte; die Schätzung der Zusatzregel ist ungeprüft an der Wirklichkeit.
