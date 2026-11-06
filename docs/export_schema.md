# Export-Schema der Vertragsliste, Version 1.1

_Stand der Beispieldaten: 04.11.2026. Version 1.1 (06.11.2026) ergänzt Version 1.0 nur additiv (siehe Änderungsverlauf in Abschnitt 5). Erzeugt von `src/report/export_vertragsliste.py`; die Skript-Validierung prüft die Dateien gegen dieses Schema. Fakten (mit Quelle) und Deutung sind getrennt; Aussagen zur Nachfrage nach dem Export sind **nicht geprüft** (siehe Abschnitt 9)._

## 1. Zweck und Dateien

Der Export übergibt die Vertragsliste (Los für Los) als Datei an ein Verwaltungssystem (Excel, ERP, CRM, Kalkulationssoftware). Die Webseite `docs/prototyp/vertragsliste.html` stellt dieselben Daten nur dar (Demo); ihre Schaltfläche „Auswahl als CSV“ liefert die gefilterte Auswahl mit **denselben Spalten** wie dieses Schema.

| Datei | Format | Verwendung |
|---|---|---|
| `docs/prototyp/export/vertragsliste_v1.csv` | CSV nach RFC 4180, Trennzeichen Komma, UTF-8 **ohne** Byte-Order-Mark (BOM), Zeilenende CRLF | Programme, Skripte, Import in Systeme |
| `docs/prototyp/export/vertragsliste_v1_de.csv` | CSV, Trennzeichen Semikolon, UTF-8 **mit** BOM, Zeilenende CRLF | Doppelklick in deutschem Excel |
| `docs/prototyp/export/vertragsliste_v1.json` | JSON, Objekt mit `meta` und `eintraege`; `region_nuts3` und `region_name` als Arrays | Programme, Schnittstellen |
| `docs/prototyp/export/vertragsliste_v1_ohne_auftragnehmer.csv`, `..._de.csv`, `....json` | wie oben, **ohne das Feld `auftragnehmer`** (25 statt 26 Felder); im JSON-`meta` steht `"variante": "ohne_auftragnehmer"` | Weitergabe ohne Namen der Auftragnehmer (siehe Abschnitt 8); erzeugt mit der Option `--ohne-auftragnehmer` |

Inhalt der drei Hauptdateien ist gleich: 130 Lose (64 Bekanntmachungen) der Oberpfalz-Liste (Fassung der Iteration 9, Haupt-CPV 90910/90911/90919), 26 Felder (Version 1.1). Die Variante ohne Auftragnehmer hat dieselben Zeilen und 25 Felder (alle außer `auftragnehmer`, Reihenfolge unverändert); sie ist ein eigener Dateisatz derselben Schema-Version und wird vom Skript ebenfalls validiert.

**Konstante Spalten.** `schema_version`, `stand_daten` und `quelle` haben in allen Zeilen denselben Wert. Im JSON stehen sie auch in `meta`. In der CSV bleiben sie als Spalten, weil eine CSV-Datei kein `meta` hat und jede Zeile für sich beschrieben sein soll (Selbstbeschreibung, auch nach Filtern und Zusammenführen); die Wiederholung kostet Platz, ist aber gewollt. Ein Import kann sie ignorieren.

## 2. Felder

Typen: Text, Datum (ISO 8601), ganze Zahl, Dezimalzahl (Punkt), Wahrheitswert (`true`/`false`). Pflicht = in jeder Zeile gefüllt; optional = darf leer sein. Herkunft: **Liste** = `reports/beispiel_liste_oberpfalz.csv`, **Wettbewerbsbild** = `reports/wettbewerbsbild_oberpfalz.csv` (eForms-XML der Zuschlagsbekanntmachung), **Export** = vom Export gesetzt.

| Feld | Typ | Pflicht | Bedeutung | Erlaubte Werte | Herkunft | Beispiel |
|---|---|---|---|---|---|---|
| `schema_version` | Text | ja | Version dieses Schemas (konstant; auch in `meta` des JSON) | `1.1` | Export | `1.1` |
| `stand_daten` | Datum | ja | Stand der Liste (Datenstand, nicht Erzeugungsdatum; konstant; auch in `meta`) | ISO-Datum | Export (aus `reports/beispiel_liste.md`) | `2026-11-04` |
| `bekanntmachung` | Text | ja | Nummer der TED-Zuschlagsbekanntmachung; mit `los_kennung` der Schlüssel | `Nummer-Jahr` | Liste (`notice`) | `383677-2024` |
| `ted_link` | Text | ja | Link zur Bekanntmachung auf TED | URL | Liste | `https://ted.europa.eu/de/notice/-/detail/383677-2024` |
| `veroeffentlicht` | Datum | ja | Veröffentlichungsdatum der Bekanntmachung | ISO-Datum | Liste | `2024-06-28` |
| `los` | ganze Zahl | ja | Laufnummer in der Liste (n-tes Los der Bekanntmachung); bleibt zur Rückwärtskompatibilität. **Stabiler Schlüssel ist `los_kennung`** | ≥ 1 | Liste | `1` |
| `los_titel` | Text | ja | Titel des Loses | frei | Liste | `24 E 028 - Los 1 Gebäudereinigung` |
| `auftraggeber` | Text | ja | Name des Auftraggebers | frei | Liste | `Stadt Regensburg` |
| `region_nuts3` | Text (JSON: Array von Text) | ja | NUTS-3-Code(s) des Leistungsorts. **CSV:** mehrere mit `\|` getrennt. **JSON:** Array, z. B. `["DE232","DE236"]` | z. B. `DE232`, `DE232\|DE236` | Liste (`nuts`) | `DE232` |
| `region_name` | Text (JSON: Array von Text) | ja | Name(n) zu `region_nuts3`, gleiche Reihenfolge und Länge. **CSV:** `\|` getrennt. **JSON:** Array | Namen der Oberpfälzer Codes DE231 bis DE23A; andere Codes bleiben als Code stehen | Export | `Regensburg (Stadt)` |
| `leistungsort_auch_ausserhalb` | Wahrheitswert | ja | Leistungsort liegt auch außerhalb der Oberpfalz | `true`, `false` | Liste (`auch_ausserhalb`) | `false` |
| `beginn` | Datum | nein | Vertragsbeginn laut Bekanntmachung | ISO-Datum | Liste | `2024-07-01` |
| `ende_grundlaufzeit` | Datum | nein | **Ende der Grundlaufzeit laut Bekanntmachung, kein Termin der Neuausschreibung.** Leer bei Stufe F (kein Ende bekannt) | ISO-Datum | Liste (`gl_ende`; bei Stufe E die Schätzung) | `2025-06-30` |
| `ende_herkunft` | Text | ja | Woher das Ende stammt | `enddatum` (Datumsfeld), `text_zunaechst` („zunächst bis …“ im Text), `text_festlaufzeit` („Festlaufzeit …“ im Text), `beginn_plus_dauer` (Beginn plus Dauerfeld), `geschaetzt` (Veröffentlichung plus Dauer, ungeprüft, Stufe E), `unbekannt` | Liste (`gl_herkunft`) | `enddatum` |
| `hoechstende_hinweis` | Datum | nein | Höchstende mit allen Verlängerungen. **Nur Hinweis, nicht für Fristen.** Ist `hoechstende_herkunft` gleich `keine_angabe` oder `keine_verlaengerung` (32 von 130 Losen), steht hier **ersatzweise das Ende der Grundlaufzeit** (kein Hinweis auf eine Verlängerung; geprüft: in diesen Losen gleich `ende_grundlaufzeit`). Sonst ist es ein Hinweis aus der Bekanntmachung, oft zu hoch (auf den Zufallslosen stimmte das Höchstende zu 87,1 %, Schwelle 90 % verfehlt). Leer bei `unbestimmbar` und `keine_grundlaufzeit` | ISO-Datum | Liste (`hoechstende`) | `2025-06-30` |
| `hoechstende_herkunft` | Text | ja | Woher das Höchstende stammt oder warum es fehlt | `datum_text`, `enddatum_ist_hoechstende`, `anzahl_x_laenge`, `hoechstlaufzeit_text`, `keine_verlaengerung`, `keine_angabe`, `unbestimmbar`, `keine_grundlaufzeit` | Liste (`hoechstende_herkunft`) | `keine_angabe` |
| `stufe` | Text | ja | Stufe der Herkunft, **nicht** der Verlässlichkeit (A: Höchstende ausdrücklich; B: berechnet; C: keine Angabe zur Verlängerung; D: Verlängerung erwähnt, Länge fehlt; E: Ende geschätzt; F: kein Ende) | `A` bis `F` | Liste | `C` |
| `status_stand` | Text | ja | Status des Loses **zum Datenstand** (`stand_daten`), nicht zum Abrufdatum | `Grundlaufzeit läuft`, `Grundlaufzeit läuft (geschätzt)`, `Verlängerungszeit möglich`, `Verlängerung offen`, `abgelaufen`, `kein Ende bekannt` | Liste (`status`) | `abgelaufen` |
| `auftragnehmer` | Text | nein | Name des Gewinners (genau ein Gewinner je Los); leer, wenn nicht genannt oder mehrere Gewinner | frei | Wettbewerbsbild (`gewinner`) | `Götz-Gebäudemanagement RSL GmbH` |
| `wert_eur` | Dezimalzahl | nein | Zuschlagswert des Loses in Euro, **nur Werte über 1 €**, Punkt als Dezimalzeichen, ohne Tausendertrenner | > 1, höchstens 2 Nachkommastellen | Wettbewerbsbild (`wert_eur`) | `79352.71` |
| `wert_status` | Text | ja | Erklärt, warum `wert_eur` gefüllt oder leer ist | `angegeben`; `platzhalter` (Angabe ≤ 1 €, nicht als Wert übernommen); `fehlt` (Angabe fehlt im Gewinnerangebot); `zurueckgehalten` (Auftraggeber hat die Veröffentlichung ausdrücklich ausgesetzt, hat Vorrang vor `platzhalter`/`fehlt`); `kein_gewinnergebot`; `gemeinsam_mehrere_lose` und `angegeben_mehrere_gewinner` (beide in den 130 Losen nicht vorgekommen, Wert wird dann nicht je Los zugeteilt) | Wettbewerbsbild (`wert_status`, `wert_zurueckgehalten`) | `angegeben` |
| `angebote_gesamt` | ganze Zahl | nein | Gesamtzahl der eingegangenen Angebote (≥ 1), wenn in der Bekanntmachung angegeben | ≥ 1 | Wettbewerbsbild (`angebote`) | `3` (Bekanntmachung 62258-2025, Los 5) |
| `angebote_untergrenze` | ganze Zahl | nein | Nur wenn die Bekanntmachung bloß die **elektronisch** eingegangenen Angebote nennt: Zahl der Angebote ist **mindestens** so hoch. Nie zugleich mit `angebote_gesamt` gefüllt | ≥ 1 | Wettbewerbsbild (`angebote_elektronisch`) | `6` (383677-2024, Los 1) |
| `hinweis` | Text | nein | Bekannter Fehler oder Besonderheit des Loses | frei; derzeit 3 Lose (siehe Abschnitt 6) | Export | `Interimsvergabe: Dauerfeld enthält die Option; Grundlaufzeit vermutlich bis 31.01.2027` |
| `quelle` | Text | ja | Quellenangabe (TED; konstant; auch in `meta`) | fester Text | Export | `TED (Tenders Electronic Daily), Zuschlagsbekanntmachung; …` |
| `los_kennung` | Text | nein (in den 130 Losen immer gefüllt) | **Seit 1.1.** Kennung des Loses in der TED-Bekanntmachung (Los-ID im eForms-XML). **Stabiler Schlüssel** zusammen mit `bekanntmachung`; stabiler als `los`, weil sie nicht von der Sortierung der Liste abhängt | Format `LOT-0000` (vier Ziffern; `LOT-0000` kommt vor) | Wettbewerbsbild (`los_zugeordnet`) | `LOT-0002` |

`los_kennung` steht als 26. Feld am Ende (Änderungsregel für Nebenversionen, Abschnitt 5), nicht neben `los`. In 117 der 130 Zeilen ist die Zahl in `los_kennung` gleich `los`, in 13 weicht sie ab (zum Beispiel `los` 1 bis 4 bei `LOT-0003` bis `LOT-0006` in Bekanntmachung 207816-2024; `los` 1 bei `LOT-0000` in 514969-2024; Ursache nicht untersucht, vermutlich steht nicht jedes Los der Bekanntmachung in der Liste); deshalb ist `los` kein verlässlicher Verweis auf die Bekanntmachung.

Beispielzeile (CSV, Auszug): `1.1,2026-11-04,383677-2024,https://ted.europa.eu/de/notice/-/detail/383677-2024,2024-06-28,1,…,Stadt Regensburg,DE232,Regensburg (Stadt),false,2024-07-01,2025-06-30,enddatum,2025-06-30,keine_angabe,C,abgelaufen,…`

Verteilung in den 130 Losen (Fakt, aus den erzeugten Dateien): `stufe` A 54, B 2, C 27, D 9, E 5, F 33; `ende_herkunft` enddatum 76, text_zunaechst 8, text_festlaufzeit 5, beginn_plus_dauer 3, geschaetzt 5, unbekannt 33; `wert_status` angegeben 62, platzhalter 39, fehlt 20, zurueckgehalten 8, kein_gewinnergebot 1; Auftragnehmer genannt 129, Gesamtzahl der Angebote 79, nur Untergrenze 51.

## 3. Regeln für leere Werte

- Ein fehlender Wert ist **leer** (CSV: leeres Feld; JSON: `null`). Nie „–“, „n/a“, „NA“, „null“ oder „0“ als Ersatz. Die Validierung weist solche Platzhaltertexte zurück.
- **Platzhalterwerte ≤ 1 € sind nie ein Wert:** `wert_eur` bleibt leer, `wert_status` erklärt den Grund (`platzhalter`, `fehlt`, `zurueckgehalten`, `kein_gewinnergebot`). Leer heißt „nicht veröffentlicht oder nicht angegeben“, nicht „null Euro“ und nicht „unbekannt, aber klein“.
- Pflichtfelder sind in jeder Zeile gefüllt. Für `ende_grundlaufzeit` gilt: leer genau dann, wenn Stufe F.
- `0` in den Angebotsfeldern kommt nicht vor; fehlt die Angabe, sind beide Felder leer.

## 4. Formate

- **Datum:** ISO 8601, `JJJJ-MM-TT` (z. B. `2025-06-30`). Keine Uhrzeit, keine Zeitzone.
- **Zahlen:** Dezimalpunkt, kein Tausendertrenner, kein Währungszeichen (`79352.71`). Ganze Zahlen ohne Nachkommastellen.
- **Wahrheitswerte:** `true` und `false` (klein), im JSON als Wahrheitswerte.
- **Listen in einem Feld** (`region_nuts3`, `region_name`): **CSV:** mit senkrechtem Strich `|` getrennt, gleiche Reihenfolge. **JSON (seit 1.1):** Arrays von Text gleicher Länge (z. B. `["DE232","DE236"]`; bei einem Ort ein Array mit einem Element).
- **Codierung:** UTF-8. Zeilenende CRLF. Erste Zeile ist die Kopfzeile mit den Feldnamen aus Abschnitt 2 in dieser Reihenfolge.
- **Trennzeichen und Anführungszeichen:** Ein Feld wird in doppelte Anführungszeichen gesetzt, wenn es das Trennzeichen, ein Anführungszeichen oder einen Zeilenumbruch enthält; ein Anführungszeichen im Feld wird verdoppelt (RFC 4180).
- **Komma-Datei (`vertragsliste_v1.csv`):** ohne BOM, wie von Programmen erwartet. Excel erkennt UTF-8 ohne BOM beim Doppelklick oft nicht (Umlaute werden falsch dargestellt); dafür gibt es die deutsche Datei oder den Import über „Daten > Aus Text/CSV“ mit Dateiursprung „65001: Unicode (UTF-8)“.
- **Semikolon-Datei (`vertragsliste_v1_de.csv`):** mit BOM (`EF BB BF` am Dateianfang), damit deutsches Excel UTF-8 und das Semikolon erkennt. Programme, die das BOM nicht entfernen, sehen es als Teil des ersten Feldnamens; in Python mit `encoding="utf-8-sig"` lesen.
- **Dezimalpunkt in deutschem Excel:** Die Datei behält den Punkt. Deutsches Excel kann `79352.71` beim Doppelklick als Text oder, je nach Einstellung, falsch als Datum oder Zahl deuten. Zuverlässig ist der Import über „Daten > Aus Text/CSV“ mit Spalte `wert_eur` als Text oder mit Gebietsschema „Englisch (USA)“ für diese Spalte. **Nicht in Excel getestet** (nur Laden in Python mit `csv` und `pandas` geprüft); vor der Zusage an einen Betrieb im Gespräch gezeigt zu prüfen.

## 5. Schlüssel und Versionierung

- **Eindeutiger Schlüssel (seit 1.1):** `bekanntmachung` + `los_kennung`. `los_kennung` ist der stabilere Schlüssel (Kennung aus der TED-Bekanntmachung). `los` bleibt zur Rückwärtskompatibilität und ist weiterhin zusammen mit `bekanntmachung` eindeutig; die Validierung prüft beide Paare in den 130 Zeilen. Die Zahl `los` ist die Laufnummer der Liste (n-tes Los der Bekanntmachung nach sortierter Los-Kennung), nicht unbedingt die im Titel stehende Zahl und nicht immer gleich der Zahl in `los_kennung`. Neue Importe sollten `los_kennung` verwenden.
- **Version:** Jede Zeile und das JSON-`meta` tragen `schema_version` (Format `Hauptversion.Nebenversion`). Der Dateiname enthält die Hauptversion (`_v1`).
- **Änderungsregeln:**
  - *Nebenversion (1.1, 1.2, …):* nur **neue optionale Felder am Ende**; vorhandene Felder bleiben in Name, Typ, Bedeutung und Reihenfolge unverändert; neue erlaubte Werte nur bei Textfeldern mit Aufzählung (der Leser muss unbekannte Werte tolerieren).
  - *Hauptversion (2.0):* Umbenennen oder Löschen von Feldern, Änderung von Typ, Bedeutung, Format oder Schlüssel. Neue Dateinamen (`_v2`), die alte Version bleibt bis zur Abkündigung weiter erzeugbar.
  - Jede Änderung wird in diesem Dokument im Abschnitt „Änderungsverlauf“ mit Datum festgehalten.
- **Änderungsverlauf:** 1.0 (06.11.2026): erste Fassung, 25 Felder. 1.1 (06.11.2026): neues optionales Feld `los_kennung` am Ende (26 Felder), Schlüssel `bekanntmachung` + `los_kennung`; im JSON `region_nuts3` und `region_name` als Arrays statt Text mit `|` (die CSV bleibt unverändert); Dokumentation zu `hoechstende_hinweis` (ersatzweise Ende der Grundlaufzeit bei `keine_angabe`/`keine_verlaengerung`) und zu den konstanten Spalten; Variante ohne Auftragnehmer (`--ohne-auftragnehmer`). **Hinweis:** Die Änderung der JSON-Typen von `region_nuts3`/`region_name` ist streng genommen eine Typänderung (nach der eigenen Regel eine Hauptversion); sie wurde als 1.1 geführt, weil das Schema vor jeder Nutzung durch Dritte geändert wurde und keine Abnehmer kennt. Leser eines 1.0-JSON müssen `region_nuts3` als Text behandeln.

## 6. Zuordnungshinweise für ERP, CRM und Kalkulation

Vorschläge, **nicht an einem realen System erprobt**. Welche Felder ein Betrieb braucht, ist offen (Fragen im Wizard-of-Oz-Blatt).

| Feld | Mögliches Ziel im System | Anmerkung |
|---|---|---|
| `auftraggeber` | Kunde / Lead / Organisation | Name nicht normalisiert; Dubletten durch Schreibweisen möglich |
| `ende_grundlaufzeit` | Wiedervorlage-Datum (Aufgabe, Erinnerung) | **kein Termin der Neuausschreibung**; als „Vertrag beobachten“, nicht als Frist |
| `hoechstende_hinweis` | Notizfeld | nur Hinweis, nicht für Fristen |
| `bekanntmachung` + `los_kennung` | externe ID des Datensatzes (Upsert-Schlüssel) | gemeinsam eindeutig (`los` bleibt zur Rückwärtskompatibilität); beim Wiederimport aktualisieren statt neu anlegen |
| `ted_link` | Link / Dokumentenverweis | vor Entscheidung lesen |
| `los_titel` | Betreff / Titel der Gelegenheit | |
| `region_nuts3`, `region_name` | Region / Einsatzgebiet | Filter für Entfernung zum Betriebssitz muss das System selbst leisten |
| `auftragnehmer` | Wettbewerber (aktueller Auftragnehmer) | leer bei 1 von 130 Losen |
| `wert_eur` | Auftragswert / Kalkulationsgrundlage | nur bei 62 von 130 Losen; Zuschlagswert des Loses (Gewinnerangebot), kein Jahreswert |
| `angebote_gesamt`, `angebote_untergrenze` | Bieterzahl | `angebote_untergrenze` ist ein Mindestwert |
| `stufe`, `ende_herkunft`, `status_stand` | Qualitätsangabe / Statusfeld | Stufe nennt Herkunft, nicht Verlässlichkeit |
| `hinweis` | Bemerkung | enthält bekannte Fehler |

## 7. Grenzen (Fakten mit Quelle)

- **Das Ende der Grundlaufzeit ist kein Termin der Neuausschreibung.** Der Backtest einer Punktprognose traf ±3 Monate nur zu 28,8 % (Schwelle 60 %; `reports/evaluation_iteration5.md`). Der Export enthält keine Prognose.
- **Höchstende nur Hinweis** (Zufallslose 87,1 % richtig, Schwelle 90 % verfehlt; `reports/beispiel_liste.md`).
- **Nur TED-Lose oberhalb der EU-Schwelle.** Verfahren, die nicht auf TED stehen, fehlen (rund ein Viertel der Oberpfälzer Reinigungsverfahren laut Hinweis aus Paket B, nicht als Schwelle gemessen).
- **Fehlerart „Dauerfeld enthält die Option“:** Bei der Herkunft `beginn_plus_dauer` kann das Dauerfeld die Option schon enthalten, dann liegt `ende_grundlaufzeit` zu spät (12 von 9.325 Losen der Gesamtliste, 0,13 %; Paket C, `reports/stufe_f_fehlertyp.csv`). In den 130 Oberpfalz-Losen sind es 3 Lose (527230-2026 Los 1 und 2, 533946-2026 Los 1); sie tragen einen `hinweis`, der Wert in `ende_grundlaufzeit` bleibt unverändert (Liste eingefroren). Weitere Fehler sind möglich: Das Ende stimmte zu 94,3 % mit zwei KI-Lesern überein (n = 70, ganz Deutschland, keine Fehlerquote, nicht für die Oberpfalz gemessen).
- **Wettbewerbsfelder unvollständig:** Auftragnehmer 129 von 130, Zuschlagswert über 1 € 62 von 130, Gesamtzahl der Angebote 79 von 130 (`reports/wettbewerbsbild_oberpfalz.md`).
- **Stand der Daten:** `stand_daten` (04.11.2026). `status_stand` ist der Status zu diesem Stand; wer die Datei später liest, muss ihn neu aus `ende_grundlaufzeit` ableiten.
- **Gebäudereinigung, Oberpfalz, eine Momentaufnahme.** Es gibt keine laufende Aktualisierung; jeder Stand ist ein neuer Lauf des Skripts.

## 8. Quelle und Lizenz

- Quelle: TED (Tenders Electronic Daily), Zuschlagsbekanntmachungen; Wettbewerbsfelder aus dem eForms-XML derselben Bekanntmachungen. Bei Weitergabe ist TED als Quelle anzugeben (Feld `quelle`, `ted_link`).
- Lizenz: Laut TED-Rechtsseite frei wiederverwendbar, auch kommerziell (Beschluss 2011/833/EU; identifizierbare Privatpersonen ausgenommen). **Vor Abgabe zu bestätigen.**
- **Namen der Auftragnehmer (Datenschutz-Vorprüfung, 2026-11-06).** Methode: Der Exportlauf (`namenpruefung` in `src/report/export_vertragsliste.py`, gibt nur Zahlen aus) zählt in den 129 Losen mit Namen die verschiedenen Namen und sucht per Textmuster nach einer erkennbaren Rechtsform (GmbH, mbH, AG, KG, OHG, GbR, UG, SE, e. V., eG, „& Co.“, Anstalt, Körperschaft, KGaA, e. K.). **Ergebnis (Fakten):** 47 verschiedene Namen; 43 mit erkennbarer Rechtsform (darunter 1 e. K., also ein Einzelunternehmen); 4 ohne erkennbare Rechtsform (zusammen 9 Lose). Die Namen stehen hier bewusst nicht (eine einmalige Vorprüfung am 2026-11-06 zeigte sie nur in der Konsole). **Grenzen:** Eine Rechtsform schließt nicht aus, dass der Name eine Privatperson enthält (zum Beispiel „Vorname Nachname GmbH“; ein e. K. ist ein Einzelkaufmann, der Name ist dann oft der einer Person); umgekehrt ist ein Name ohne Rechtsform nicht notwendig eine Person. Die Prüfung ist nicht abschließend (Textmuster, keine Einzelfallprüfung, keine Rechtsprüfung). Laut TED-Rechtsseite sind identifizierbare Privatpersonen von der freien Wiederverwendung ausgenommen. **Empfehlung vor Weitergabe an Dritte:** das Feld `auftragnehmer` auf Wunsch entfernen, dafür gibt es die Variante `vertragsliste_v1_ohne_auftragnehmer*` (Option `--ohne-auftragnehmer`; Schema-Variante: dieselben Felder ohne `auftragnehmer`, 25 Felder, im JSON `meta.variante = "ohne_auftragnehmer"`); in dieser Variante entfällt das Wettbewerbsfeld, die übrigen Felder bleiben unverändert.

## 9. Was dieses Schema nicht belegt

- Es belegt **keine Nachfrage:** Ob ein Betrieb die Datei in ein System lädt, ist ungeprüft (Annahmen A1/A15, Fragen im Blatt `docs/wizard_of_oz_blatt.md`).
- Die technische Übergabe einer CSV ist einfach; neu ist hier nur das dokumentierte, versionierte Schema. Kostenlose Wege (TED-Suchprofil, Bekanntmachungsservice, Vergabeweiser) bestehen daneben; „keine Abo-Kosten“ ist deshalb kein Vorteil an sich.
- Es ist keine Aussage, dass die Daten besser, vollständiger oder exklusiver sind als bei anderen Angeboten.
