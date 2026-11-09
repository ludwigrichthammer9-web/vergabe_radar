# Video „Franz und die Glaskugel“

## Zweck
Zusammenfassung des Projekts Vergabe-Radar für den Vortrag und das Lab-Log: im Vortrag die gekürzte Fassung mit 3:32 Minuten (`franz_video_ton_kurz.mp4`, 212,49 s), vollständig 4:28 Minuten (`franz_video_ton.mp4`, 267,76 s); beide 1280 x 720. Inhalt: von der Idee (Prognose von Vertragsenden) über die gescheiterte Punktprognose und die Vertragsliste bis zur Entscheidung „Selbst bauen? Nein.“ Erzählt wird mit erfundenen Figuren (Franz, Bit, Prüfi). Das Video ist eine Veranschaulichung, kein zusätzlicher Beleg. (Frühere Fassungen v1 bis v4: 170,5 s; HTML-Live-Fassung 276 s, siehe unten.)

## Aktuelle Fassung (2026-11-09): Manuels Fassung mit ElevenLabs-Stimmen
_Fakten nach Angabe des Teams (2026-11-09) und eigener Messung mit ffmpeg aus `imageio-ffmpeg` (`.venv-video`)._
- **Vollständige Fassung:** `franz_video_ton.mp4`, erstellt von Manuel Strobel (Angabe des Teams). Gemessen: 267,76 s (4:28), 1280 x 720, H.264 (High, 25 fps), AAC 48 kHz Stereo. Abspann (Standbild bei 266 s gesehen): „Stimmen KI-generiert (ElevenLabs)“, dazu „Gespräche: n = 3, nachgestellt und verändert. Alle Figuren sind erfunden.“
- **Vortragsfassung:** `franz_video_ton_kurz.mp4`, gekürzt von Claude Code (2026-11-09). Gemessen: 212,49 s (3:32), 1280 x 720, H.264 (25 fps), AAC 48 kHz Stereo. Herausgeschnitten ist Runde 4 (kostenlose Liste, Vergleich 230 Verträge, Waage Selbstbauen/kostenlos, Oberpfalz, Bauplan; Videozeit ca. 3:18 bis 4:14), weil die Folien diese Inhalte direkt danach zeigen. Das Original `franz_video_ton.mp4` bleibt unverändert.
- **Schnitt (Neuschnitt 2026-11-09, ersetzt den ersten Schnitt):** bei 198,62 s und 253,9 s der Datei `franz_video_ton.mp4`, beide Punkte in gemessenen Sprechpausen (Sprechende „… nicht fehlerfrei“ bei ca. 198,36 s, Stille 198,40–198,65 s; Einsatz „Vorhersagen?“ bei ca. 254,55 s, Stille davor). Die Blenden liegen damit ganz in der Stille (Ton: Ausblende 198,40–198,62 s, Einblende 0,1 s ab 253,9 s; Bild: Ab-/Aufblende 0,4 s). Länge 198,62 + (267,76 − 253,9) = 212,48 s, gemessen 212,49 s (3:32). Neu kodiert mit libx264, CRF 20, AAC 160 kbit/s. Aufruf:
```
ffmpeg -i franz_video_ton.mp4 -filter_complex "[0:v]trim=0:198.62,setpts=PTS-STARTPTS,fade=t=out:st=198.2:d=0.42[v1];[0:a]atrim=0:198.62,asetpts=PTS-STARTPTS,afade=t=out:st=198.40:d=0.22[a1];[0:v]trim=253.9,setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.4[v2];[0:a]atrim=253.9,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.1[a2];[v1][a1][v2][a2]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -preset medium -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart franz_video_ton_kurz.mp4
```
  Erster Schnitt (frühere Fassung derselben Datei): 198,4 s und 254,3 s, 211,85 s; dabei lagen Teile der Blenden in der Sprache (siehe Prüfung unten).
- **Im Vortrag:** Videofolie rund 4:15 Minuten (Einleitung, 3:32 Video, Quizfrage, Überleitung; Angabe des Teams).
- **Lizenz und Stimmen:** Die Stimmen sind über ElevenLabs erzeugt; es gelten die Bedingungen von ElevenLabs. Die Nennung im Abspann ist vorhanden. **Offen:** Tarif und Konto laufen über Manuel; ob der Tarif die Nutzung und Weitergabe abdeckt, konnten wir nicht prüfen. Darum bleibt das Video ohne Freigabe (README im Wurzelordner, „Lizenzen“). Der ElevenLabs-Zweig in `src/report/video_vertonung.py` (unten) ist im Repo nicht eingerichtet (`stimmen.json` enthält weiter nur Platzhalter statt Voice-IDs), wurde für diese Fassung also nach Stand des Repos nicht benutzt; wie Manuel Bild und Ton erzeugt hat, ist nicht im Repo dokumentiert (offen).
- **Grenzen** wie bisher: Figuren erfunden, Gespräche nachgestellt (es gab drei echte, n = 3), vereinfacht (Runden statt zehn Iterationen). Die Zahlen der neuen Fassung haben wir nicht erneut Satz für Satz gegen die Belege geprüft; gesehen haben wir nur die Standbilder bei 120 bis 150 s (28,8 % gegen 17,3 %, Ziel 60 %, 52 geprüfte Fälle) und den Abspann.
- Das Standbild im Lab-Log (`docs/lab_log_bilder/video_standbild.png`) stammt jetzt aus `franz_video_ton_kurz.mp4` bei 135 s (ffmpeg, ein Bild). Achtung: `src/report/lab_log_bilder.py` erzeugt das Standbild noch aus der HTML-Animation und würde es beim nächsten Lauf überschreiben.

## Prüfung der Fassung franz_video_ton gegen die Belege (2026-11-09)
_Geprüft von Claude Code im Auftrag des Nutzers. Dieser Abschnitt ergänzt den Satz unter „Grenzen“ oben („nicht erneut Satz für Satz geprüft“); jener Satz bleibt als Stand vor dieser Prüfung stehen._

**Methode (Fakten).**
- Geprüft wurde die **Langfassung** `franz_video_ton.mp4` (267,76 s), damit auch Runde 4 erfasst ist. Die Kurzfassung `franz_video_ton_kurz.mp4` ist Teil 0 bis 198,4 s plus Teil 254,3 s bis Ende; Zeiten nach der Naht liegen in der Kurzfassung um 55,9 s früher. Herausgeschnitten sind die Zeilen 33 bis 40 der Tabelle (Runde 4).
- **Den Ton haben wir nicht gehört.** Gelesen wurden die eingebrannten Untertitel (Sprecher-Etikett und Text) und die Bildtexte: Einzelbilder mit ffmpeg aus `imageio-ffmpeg` (`.venv-video`), ein Bild je 2 s als Kontaktbögen (8 Bilder je Bogen, 640 px breit), dazu Untertitelwechsel per Szenenerkennung im Untertitelbereich (4 Bilder/s; Wechsel bei rund 0,5 / 6,5 / 9,5 / 12,75 / 20,5 / 24,5 / 29,5 / 37,75 / 42,25 / 53,5 / 61,5 / 68,5 / 73,5 / 80,75 / 89,25 / 97,25 / 104 / 113,25 / 133 / 139,5 / 142 / 150,5 / 158,25 / 164,75 / 175,25 / 183 / 190,25 / 200,75 / 208 / 219 / 230,75 / 236,5 / 242,5 / 254,5 s). Zeitangaben deshalb auf etwa ±1 s genau. Hilfsdateien liegen außerhalb des Repos (Scratch-Ordner), nicht eingecheckt.
- **Ob der gesprochene Text den Untertiteln entspricht, muss das Team beim Anhören prüfen.** `sprechertext.json` gehört zur früheren HTML-Fassung und passt nicht zu dieser Fassung.
- Belege: `docs/lab_log.md`, `docs/iterationen.md`, `reports/backtest_iteration5.md`, `reports/evaluation_iteration3.md`, `reports/evaluation_iteration5.md`, `reports/evaluation_iteration10b.md`, `reports/optionsanalyse.md`, `reports/wettbewerbsbild_oberpfalz.md`, `reports/make_or_buy.md`, `docs/business.md` §7.1, §8.1 bis §8.3, §8.9, §9.4.
- Urteile: **korrekt** (deckt sich mit dem Beleg, Vereinfachung vermerkt), **ungenau** (Zahl stimmt oder Kern stimmt, aber die Formulierung behauptet mehr oder etwas anderes; mit Vorschlag), **falsch** (widerspricht dem Beleg), **nicht prüfbar** (Fiktion der Figuren oder kein Beleg im Repo).

**Ergebnis je Aussage.** Spalte „Kurz“: in `franz_video_ton_kurz.mp4` enthalten. Erz. = Erzähler.

| Nr | Zeit lang (s) | Kurz | Sprecher | Aussage (Untertitel bzw. „Bild:“ = Bildtext) | Urteil | Beleg / Vorschlag |
|---|---|---|---|---|---|---|
| 1 | 0–6 | ja | Bild | Titel „Franz und die Glaskugel“; Steckbrief Franz, Firma „Franz putzt.“, putzt Schulen, Rathäuser, Ämter; „Alle Figuren und Firmen erfunden.“ | korrekt | Fiktion von Anfang an gekennzeichnet |
| 2 | 0,5–12 | ja | Erz. | „Das ist Franz. Er hat einen Reinigungsbetrieb und putzt Schulen, Rathäuser und Ämter.“ / „Superkraft: findet jeden Fleck.“ / „Schwäche: erfährt alles zu spät.“ | nicht prüfbar (Fiktion) | gekennzeichnet (Nr. 1); „zu spät“ passt zu Gespräch 1 (Meldung 28 Tage vor Abgabe, `docs/business.md` §8.9) |
| 3 | 12,75 | ja | Erz. | „Wenn ein Rathaus putzen lässt, darf es nicht irgendwen anrufen. Es muss den Auftrag in der Regel ausschreiben.“ | nicht prüfbar | kein eigener Beleg im Repo; als Grundsatz des Vergaberechts üblich, „in der Regel“ lässt Ausnahmen offen |
| 4 | 20,5 | ja | Erz. | „Betriebe geben Angebote ab, einer bekommt den Vertrag.“ (Bild: „Öffentlich ausgeschrieben“, Putzauftrag, Bieter A/B/C) | korrekt | vereinfacht (Lose); Oberpfalz: 0 von 130 Losen mit mehreren Gewinnern (`reports/wettbewerbsbild_oberpfalz.md` §2) |
| 5 | 24,5 | ja | Erz. | „Der Vertrag läuft einige Jahre, oft mit Verlängerung.“ (Bild: Grundlaufzeit, „Verlängerung?“) | korrekt | Vergabestelle: meist 2 Jahre fest plus 1 Jahr Option (§8.9); Option belegt bei 24 von 52 Backtest-Paaren (`reports/optionsanalyse.md`) |
| 6 | 29,5 | ja | Erz. | „Danach wird neu ausgeschrieben. Nur: Ob verlängert wird, weiß vorher keiner.“ (Bild: „Neuausschreibung: wann?“) | ungenau | Die Vergabestelle weiß es, sie entscheidet; nicht lesbar ist es aus den TED-Daten (`reports/evaluation_iteration5.md`, Alternative Erklärungen; `docs/lab_log.md` §1 „steht nicht in den TED-Daten“). Vorschlag: „Ob verlängert wird, steht in keinen öffentlichen Daten.“ |
| 7 | 37,75 | ja | Franz | „Eine Ausschreibung? Schon wieder erfahre ich das als Letzter!“ (Bild: „Unterhaltsreinigung Grundschule, Angebotsfrist: in wenigen Wochen“) | nicht prüfbar (Fiktion) | passt zu Gespräch 1 (28 Tage, Kalkulation nachts, §8.9) |
| 8 | 42,25 | ja | Erz. | „Die Konkurrenz hat ihr Angebot längst fertig. Franz fängt gerade erst an.“ (Bild: „Konkurrenz: Angebot fertig ✓“) | ungenau | Zuspitzung, vom Erzähler als Tatsache gesprochen. Beleg nur dafür, dass ein Betrieb das Ende **eigener** (oder knapp verlorener) Verträge kennt, sonst „Blackbox“ (§8.9, Gespräch 1). Dass die Konkurrenz allgemein früher fertig ist, ist nicht belegt. Vorschlag (mündlich): „zugespitzt; der bisherige Auftragnehmer kennt sein Vertragsende, Franz nicht“ |
| 9 | 48–53 | ja | Bild | „Unsere Projektfrage: Kann man aus öffentlichen Daten vorhersagen, wann welcher Auftrag neu ausgeschrieben wird? Vergabe-Radar, Projekt im Modul Big Data Analytics“ | korrekt | `CLAUDE.md` (Idee), `docs/lab_log.md` §0 |
| 10 | 53,5 | ja | Franz | „Ich hab's! Ich baue mir eine Glaskugel, die mir sagt, wann neu ausgeschrieben wird.“ | nicht prüfbar (Fiktion) | – |
| 11 | 61,5 | ja | Erz. | „Die Daten sind öffentlich: Größere Aufträge stehen mit ihrem Zuschlag im EU-Amtsblatt TED.“ (Bild: „TED, Amtsblatt der EU – Zuschläge oberhalb der EU-Schwelle“) | korrekt | `docs/business.md` §8.1, §8.3 (Schwelle 216.000 € für Kommunen und Länder seit 2026; TED nur oberhalb) |
| 12 | 68,5 | ja | Bit (KI) | „Hallo, ich bin Bit, die KI. Das klappt hundertprozentig!“ | nicht prüfbar (Fiktion) | erkennbar übertriebene Figur, später widerlegt (Nr. 15, 21) |
| 13 | 73,5 | ja | Erz. | „Gearbeitet wird nach CRISP-DM: sechs Schritte im Kreis. Jede Runde endet mit einer Entscheidung.“ (Bild: Rad mit sechs Phasen, ab hier „Runde 1“ bis „Runde 4“) | korrekt | `docs/CRISP-DM.md`; je Iteration eine Entscheidung (`docs/iterationen.md`). Vereinfachung: vier Runden statt zehn Iterationen (wie bisher) |
| 14 | 80,75 | ja | Bit (KI) | „Runde 1: Ich finde zu jedem neuen Auftrag seinen Vorgänger. Meine Vorschläge sind fast alle plausibel!“ | korrekt | Selbsteinschätzung der KI: auf Entwicklungsdaten „10–11 von 12“ plausibel (`reports/evaluation_iteration3.md`; `docs/lab_log.md` Irrwege 2026-10-25). „Runde 1“ = Iteration 3 |
| 15 | 89,25 | ja | Erz. | „Geprüft wird an neuen Testdaten. Ergebnis: Nur 11 von 24 Zuordnungen stimmen.“ (Bild: „Test mit neuen Daten: 11 von 24 richtig“) | korrekt | V2 Präzision 11/24 = 45,8 % der **Vorschläge** (Ziel ≥ 80 %), `docs/iterationen.md` Iteration 3. Gesagt wird „Zuordnungen stimmen“, nicht „gefunden“; das passt. Nicht gezeigt: Iteration 4 (17/19, aber nur 19 Vorschläge) |
| 16 | 97,25 | ja | Erz. | „Runde gescheitert. Festhalten, was schiefging, und zurück an den Anfang.“ | korrekt | vereinfacht: nach Iteration 3 „in Phase 2/3 bleiben“, erst nach Iteration 4 „Idee anpassen“ (`docs/iterationen.md`) |
| 17 | 104 | ja | Erz. | „Runde 2: eine einfache Regel. Neuausschreibung gleich Vertragsende mit allen Verlängerungen, minus sechs Monate.“ (Bild: Kugel „Vertragsende − 6 Monate“; „Vertragsende mit allen Verlängerungen. Treffer: auf ±3 Monate genau.“) | korrekt | R1 = Höchstende − 6 Monate, Fenster ±3 Monate (`reports/backtest_iteration5.md`) |
| 18 | 113,25 | ja | Erz. | „Treffer heißt: auf drei Monate genau. Das Ziel steht vorher fest: 60 Prozent.“ (Bild: „Ziel, vorher festgelegt: 60 %“) | korrekt | festgelegt 2026-10-30 vor jeder Berechnung (`docs/business.md` §7.1); Evaluator: Vorab-Festlegung „erfüllt, mit Vorbehalt“ (`reports/evaluation_iteration5.md`) |
| 19 | 120–125 | ja | Bild | „Was schätzt ihr: Wie oft lag die Regel richtig? Ziel waren 60 Prozent.“ | korrekt | wie Nr. 18 |
| 20 | 126–138 | ja | Bild | Balken „simple Vergleichsregel 17,3 %“, „unsere Regel 28,8 %“, „Ziel 60 %“, „52 geprüfte Fälle“ | korrekt | R0 (Grundlaufzeit − 6) 9/52 = 17,3 %, R1 15/52 = 28,8 % (Wilson 18,3–42,3), `reports/evaluation_iteration5.md`. Mündlich ggf.: Vergleichsregel = Ende der Grundlaufzeit − 6 Monate |
| 21 | 133 | ja | Erz. | „28,8 Prozent bei 52 geprüften Fällen. Ziel klar verfehlt.“ | korrekt | wie Nr. 20 |
| 22 | 139,5 | ja | Franz | „… und wieder zu spät.“ | nicht prüfbar (Fiktion) | – |
| 23 | 142 | ja | Erz. / Bild | „Die Vergabestelle sagt sinngemäß: Steht eine Option im Vertrag, wird meist verlängert.“ (Bild: „Vergabestelle (Gespräch, sinngemäß): …“) | korrekt | Notiz: „Fast immer, wenn eine Verlängerungsoption im Vertrag steht“ (§8.9, n = 1); „meist“ ist schwächer als die Notiz, „sinngemäß“ ist gekennzeichnet. Zeitlich vereinfacht: das Gespräch war am 2026-11-05, nach Iteration 5 |
| 24 | 142 | ja | Erz. | „Das passt zu unserem Ergebnis.“ | ungenau | Deutung von Claude aus einem Gespräch (n = 1), kein Beleg (§8.9 Interpretation 4; `reports/optionsanalyse.md`: „Hinweis, kein Beleg“; `docs/iterationen.md` Paket F: „fast immer verlängert“ damit nicht prüfbar). Die frühere Fassung trug diese Einschränkung, diese nicht. Zudem gestreut nach beiden Seiten (20 früher, 17 später). Vorschlag: „Ein Hinweis aus einem Gespräch, kein Beleg: Das Vertragsende ist kein fester Termin.“ |
| 25 | 150,5 | ja | Franz | „Dann eben keine Glaskugel, sondern eine Liste: Welcher Vertrag endet wann?“ | korrekt | Entscheidung Iteration 5 „Idee anpassen“, Vertragsliste ohne Terminprognose (`docs/iterationen.md`) |
| 26 | 150–172 | ja | Bild | „Vertragsliste – über 9.000 Lose, Gebäudereinigung, Deutschland“; Zeilen „Rathaus endet 03/2027“, „Grundschule Nord 09/2027“, „Landratsamt 12/2026“ usw. | korrekt | 9.915 bzw. 9.325 Lose (Iteration 9). Die Zeilen sind erfundene Beispiele, nicht als solche gekennzeichnet (gering) |
| 27 | 158,25 | ja | Bit (KI) | „Liste fertig! Über 9.000 Lose. Da stimmt bestimmt alles!“ | korrekt | Zahl stimmt für beide Fassungen; die Übertreibung gehört der Figur und wird sofort widerlegt (Nr. 28). Die frühere Vereinfachung („9.325“ vor der Korrektur) ist damit behoben |
| 28 | 164,75 | ja | Prüfi (Kontrolle) | „Moment. Hier ist das Ende schon das Datum mit allen Verlängerungen. ‚Bestimmt‘ ist keine Prüfmethode.“ (Bild: „Fehler: Dieses Ende enthält schon alle Verlängerungen.“) | korrekt | Fehlertyp der Iteration 6 („Enddatum ist manchmal schon das Höchstende“, `docs/iterationen.md`, `reports/evaluation_iteration6.md`) |
| 29 | 175,25 | ja | Erz. | „Also zurück: Regeln nachbessern, eine neue Zufallsstichprobe ziehen und die Lösung vorher versiegeln.“ (Bild: „neue Zufallsstichprobe“, „Lösung vorher versiegelt“) | korrekt | vereinfacht für Iterationen 7 bis 9: Regel 1b, Regeln 6 bis 10, Seed 20261109, Skripte und Schlüssel vor dem Lauf committet (`docs/iterationen.md` Iteration 9) |
| 30 | 183 | ja | Erz. / Bild | „Zwei KI-Prüfer lesen dieselben Fälle: Bei 66 von 70 stimmt die Liste mit ihnen überein.“ (Bild: „66 von 70 stimmen mit zwei KI-Prüfern überein (nicht unabhängig)“) | korrekt | V1 66/70 = 94,3 % gleich dem Vergleichswert zweier KI-Leser (`docs/iterationen.md`, zulässige Aussage). „Nicht unabhängig“ steht im Bild; es fehlt „Vergleichswert teils zirkulär“ (mündlich ergänzen). Kein „korrekt“ behauptet |
| 31 | 190,25 | ja | Erz. / Bild | „Ein Mensch prüft 15 und bestätigt 14.“ (Bild: „Ein Mensch prüft 15 Fälle: 14 stimmen.“) | ungenau | V6: Teammitglied Manuel Strobel, nicht unabhängig, verglichen mit dem **Vergleichswert** der KI-Leser, nicht mit der Liste; 15 Lose, dünn (`docs/lab_log.md` §1 Grenzen, §4 Iteration 9). „Bestätigt“ klingt nach unabhängiger Bestätigung. Vorschlag: „Ein Teammitglied liest 15 Fälle selbst nach: 14 stimmen mit den KI-Lesern überein.“ |
| 32 | 190,25 | ja | Erz. / Bild | „Die Liste hat jetzt 9.325 Lose. Gut, aber nicht fehlerfrei.“ (Bild: „Liste nach allen Korrekturen: 9.325 Lose“) | korrekt | 9.325 statt 9.915 Lose (Iteration 9); „nicht fehlerfrei“: V4 und V7 verfehlt, Paket C 12 Lose mit Fehlertyp (`docs/iterationen.md`) |
| 33 | 198–200 | nein | Bild | „kostenloser Online-Dienst – Auslaufende Verträge – 0 €“ | korrekt | Vergabeweiser kostenlos, A2 widerlegt (`docs/business.md` §8.2, Iteration 10) |
| 34 | 200,75 | nein | Franz | „Moment … so eine Liste gibt es ja schon. Kostenlos!“ | korrekt | wie Nr. 33 |
| 35 | 208 | nein | Bild | „230 verglichene Verträge – 23 davon (rund 10 %): anderes Ende“ | korrekt | 23/230 = 10,0 % gepoolt aus n = 70 und n = 160 (`reports/evaluation_iteration10b.md`, Gesamtbild). Genauer: Lose, und „anderes Ende“ = Vergabeweiser weicht ab, die Liste trifft den Vergleichswert |
| 36 | 208 | nein | Erz. / Bild | „Unterschied bei rund 10 Prozent: Unsere Liste zeigt das Ende je Los, also je Teilauftrag, etwa je Gebäude, statt je Ausschreibung.“ | ungenau | Die Losebene erklärt nur einen Teil: in W1 (8 Fälle) 4 Losebene, 2 Höchstende; in 10b (15) 4 Losebene, 7 Höchstende, 4 sonstige; zusammen etwa 8 Losebene, 9 Höchstende, 6 sonstige (`docs/iterationen.md` Paket-Nachtrag W1; `reports/evaluation_iteration10b.md`). Es fehlt „ein Qualitätsvorsprung ist nicht belegt“. Vorschlag: „… meist ein anderes Datum (Höchstende statt Grundlaufzeit) oder das Ende je Los; ein Qualitätsvorsprung ist nicht belegt.“ |
| 37 | 219 | nein | Erz. / Bild | „Im Kostenmodell, mit unseren Annahmen, ist Selbstbauen gegen einen kostenlosen Dienst nie günstiger.“ (Bild: „Was kostet mehr? (Modell)“, „Kostenmodell mit Annahmen, keine Messung“) | korrekt | gilt für das **Basismodell** (Modellkonstruktion, `reports/make_or_buy.md`, `docs/business.md` §9.4). Hinweis: In der symmetrischen Variante ist Eigenbau „Niedrig“ gegen einen kostenlosen Dienst mit eigenem Import nicht teurer, gegen Übernahme von Hand nach 4 bis 12 Jahren günstiger |
| 38 | 230,75 | nein | Erz. / Bild | „Wer den Vertrag hat, steht in der Oberpfalz fast immer drin: 99 Prozent.“ (Bild: „Oberpfalz: 130 Lose (Teilaufträge)“, „Wer hat den Vertrag? 99 %“, „Quelle: TED-Bekanntmachungen, eigene Auswertung“) | korrekt | 129/130 = 99,2 % (`reports/wettbewerbsbild_oberpfalz.md` §2) |
| 39 | 236,5 | nein | Erz. / Bild | „Den Auftragswert, also ungefähr den Preis, gibt es nur bei 48 Prozent.“ (Bild: „48 %, knapp die Hälfte“) | korrekt | Wert über 1 € bei 62/130 = 47,7 % (ebd.). Es ist der Wert des Gewinnerangebots, kein Stunden- oder Einheitspreis (`docs/business.md` §8.9 Präzisierung) |
| 40 | 242,5 | nein | Franz | „Ich baue keine eigene Plattform. Ich nutze, was es gibt, und schaue mir die Konkurrenz genauer an.“ (Bild: „Bauplan eigene Plattform“, durchgestrichen) | korrekt | Empfehlung „kostenlosen Alarm nutzen … nicht selbst bauen“ (`docs/lab_log.md` §7); Wettbewerbsdaten als einziger Zahlungswunsch (§8.9, Gespräch 1) |
| 41 | 254 | ja | Bild | „Franz gibt es nicht. Die Daten schon.“ | korrekt | Fiktion aufgelöst |
| 42 | 254,5 | ja | Erz. | „Vorhersagen? Mit unserer einfachen Regel nicht.“ | korrekt | 28,8 % gegen Ziel 60 % (Nr. 21) |
| 43 | 254,5 | ja | Erz. | „Selbst bauen? Lohnt sich nach unserem Modell nicht.“ | ungenau | Das Modell vergleicht nur Kosten; belegt ist „im Basismodell gegen kostenlose Dienste nie günstiger“, „der Preis ist kein Vorteil des Eigenbaus“, nicht „lohnt sich nicht“ (Nutzen nicht gemessen; `reports/make_or_buy.md`). In der **Kurzfassung** fehlt die Modellszene (Nr. 37); der Satz steht dort ohne Herleitung. Vorschlag (mündlich): „rechnet sich im Modell gegen kostenlose Dienste nicht“ und direkt die Make-or-Buy-Folie zeigen |
| 44 | 254,5 | ja | Erz. | „Wie sicher wir uns sind und wo nicht, zeigen wir euch jetzt.“ | korrekt | Überleitung zu den Folien |
| 45 | 254–267 | ja | Bild (Abspann) | „Daten: TED, Amt für Veröffentlichungen der EU; eigene Auswertung.“ | korrekt | `docs/lab_log.md` §0, `docs/quellen.md` |
| 46 | 254–267 | ja | Bild (Abspann) | „Gespräche: n = 3, nachgestellt und verändert. Alle Figuren sind erfunden.“ | korrekt | drei Gespräche am 2026-11-05 (§8.9) |
| 47 | 254–267 | ja | Bild (Abspann) | „Projekt Vergabe-Radar, Modul Big Data Analytics, OTH Amberg-Weiden.“ | korrekt | `docs/lab_log.md` Kopf |
| 48 | 254–267 | ja | Bild (Abspann) | „Stimmen KI-generiert (ElevenLabs).“ | nicht prüfbar | Angabe des Teams; im Repo kein Beleg (`stimmen.json` nur Platzhalter, siehe oben). Hinweis: Der Abspann nennt weder Autoren noch, dass die Animation KI-gestützt erstellt wurde (die frühere Fassung nannte die Autoren) |

**Zählung (Fakten aus der Tabelle).** 48 Zeilen: **35 korrekt, 6 ungenau (Nr. 6, 8, 24, 31, 36, 43), 0 falsch, 7 nicht prüfbar** (Nr. 2, 3, 7, 10, 12, 22: Fiktion bzw. kein Repo-Beleg; Nr. 48: Angabe des Teams). Kurzfassung (40 Zeilen, ohne Nr. 33 bis 40): 29 korrekt, 5 ungenau (Nr. 6, 8, 24, 31, 43), 0 falsch, 6 nicht prüfbar. Alle Zahlen im Bild und im Untertitel (11 von 24, ±3 Monate, 60 %, 17,3 %, 28,8 %, 52, über 9.000, 66 von 70, 15/14, 9.325, 230/23/rund 10 %, 130 Lose, 99 %, 48 %, n = 3) stimmen mit den Belegen überein.

**Ton an den Nähten (gemessen, nicht gehört).** Stillesuche (−40 dB, ≥ 0,15 s) in der Langfassung: Vor der ersten Naht endet das Sprechen bei etwa 198,36 s, die Ausblende läuft ab 198,0 s; das Ende von „… nicht fehlerfrei“ liegt also in der Ausblende. Nach der zweiten Naht setzt der Erzähler bei etwa 254,6 s ein, die Einblende (ab 254,3 s, 0,5 s) reicht bis 254,8 s; der Anfang von „Vorhersagen?“ wird also leicht eingeblendet. Beides beim Anhören prüfen. **Nachtrag (Neuschnitt):** Beide Nähte wurden danach in die Stille verlegt (198,62 s und 253,9 s, siehe oben); gemessen in der neuen Kurzfassung: Sprache endet vor der Blende, die Stille an der Naht dauert ca. 0,9 s. Anhören bleibt Aufgabe des Teams.

**Deutung (Interpretation).**
- Das Video enthält keine falsche Zahl. Die sechs ungenauen Stellen sind Formulierungen, die mehr sagen als die Belege: zwei zur Einordnung der Ergebnisse (Nr. 24 „passt zu unserem Ergebnis“ ohne „n = 1, Hinweis“; Nr. 31 „ein Mensch bestätigt“ ohne „Teammitglied, nicht unabhängig, gegen den Vergleichswert“), eine zur Ursache des Unterschieds zu Vergabeweiser (Nr. 36, nur Langfassung), eine zum Kostenmodell (Nr. 43) und zwei zugespitzte Erzählersätze im Einstieg (Nr. 6, Nr. 8).
- Gegenüber den früheren HTML-Fassungen fehlen einige der damals eingefügten Einschränkungen wieder (Vergabestelle „Hinweis, kein Beleg“; „Vergleichswert teils zirkulär“; „Qualitätsvorsprung nicht belegt“). Die Langfassung ist dafür bei 9.325 genauer als die frühere Fassung.
- **Empfehlung:** Vor dem Vortrag muss im Video nichts geändert werden, ein mündlicher Hinweis genügt, weil keine Aussage falsch ist, die Einschränkungen auf den Folien und im Lab-Log stehen und eine Änderung Bild und Ton (ElevenLabs, Konto bei Manuel) neu erzeugen müsste. Vorschlag für die Einleitung oder Überleitung, ein Satz: „Das Video vereinfacht: Der Mensch, der 15 Fälle prüfte, ist Manuel aus unserem Team, also nicht unabhängig; die Vergabestelle ist ein einziges Gespräch, ein Hinweis, kein Beleg; und ‚selbst bauen lohnt nicht‘ heißt: im Kostenmodell mit Annahmen nie günstiger als ein kostenloser Dienst.“ Wenn das Video ohnehin neu geschnitten wird, zuerst Nr. 31 und Nr. 24 im Untertitel und Sprechtext ändern (Vorschläge in der Tabelle), dann Nr. 43; für die Weitergabe der Langfassung zusätzlich Nr. 36.

## Frühere Fassungen v1 bis v4 (HTML-Animation, Export 170,5 s)
_Die folgenden Abschnitte beschreiben die früheren Fassungen; sie bleiben unverändert im Repo._

## Herkunft
- Die HTML/SVG-Animation hat Manuel Strobel **KI-gestützt** erstellt (Original: `Franz_und_die_Glaskugel_live.html`, nicht im Repo, Original unverändert). Ludwig Richthammer und Manuel Strobel haben sie abwechselnd gemeinsam überarbeitet (Angabe des Nutzers, 2026-11-09).
- Diese Fassung `franz_und_die_glaskugel.html` ist **korrigiert und erweitert** (siehe unten). Autorenzeile im Abspann.
- **Stand vor der Fassung von Manuel (2026-11-09, inzwischen überholt, siehe „Aktuelle Fassung“ oben):** Fassung v4 (`franz_und_die_glaskugel_szenen_0-5_v4.mp4`) mit Microsoft-Neuralstimmen über edge-tts (Commit b87088c). Manuel optimiert das Video weiter; eine Fassung nach v4 folgt (offen).

## Was gegenüber dem Original geändert wurde (Fakten)
Nur Texte und Technik, **keine Zahlen**:
1. Schlusssatz: „Genau das haben uns die Daten gezeigt“ ersetzt durch „Das zeigt unsere Rechnung mit Annahmen und der Blick auf kostenlose Dienste.“
2. Szene 7: Untertitel „Im Modell, mit unseren Annahmen und nicht als Messung: Selbstbauen ist gegen einen kostenlosen Dienst nie günstiger.“ (die Waage trägt schon „Kostenmodell mit Annahmen, keine Messung“).
3. Szene 6: „rund 10 Prozent“ ergänzt um „meist anderes Datum für das Höchstende statt der Grundlaufzeit, teils Losebene; ein Qualitätsvorsprung ist nicht belegt“ (Untertitel und Karte).
4. Szene 5: Einschränkung „Die zwei KI-Leser sind nicht unabhängig, der Vergleichswert ist teils zirkulär; der Mensch prüfte 15 Fälle: 14 stimmen“ (Untertitel und Karte).
5. Szene 4: Die Aussage der Vergabestelle ist als „sinngemäß, Hinweis aus einem Gespräch und einer Optionsanalyse (70,8 %, n = 24)“ gekennzeichnet (Untertitel und Karte, „kein Beleg“).
6. Szene 2: Karte „Daten: TED, Gebäudereinigung, Deutschland, ab 2016“.
7. Abspann: „Autoren: Manuel Strobel, Ludwig Richthammer. Stimme: synthetisch (Piper, Thorsten-Voice).“ (v1: Windows SAPI; seit v4: „Stimmen: synthetisch (Microsoft Neural-Stimmen ueber edge-tts)“)
8. Technik: Abspielbereich per URL (`?von=8&bis=186`), Sprecherstimme (WAV je Untertitel, jetzt Piper; Text aus `sprechertext.json`), Stumm-Schalter, Startbildschirm. Caption-Fenster angepasst, wo die Texte länger wurden oder die Stimme Platz brauchte: Untertitel 4 und 5 (Szene 2, Grenze 51 s auf 50,8 s, „Hallo!“ gestrichen), Untertitel in Szene 6 (186,6 bis 193,2; 193,4 bis 204,6; 204,8 bis 215). Die Szenen-Zeitleiste `B` ist **nicht** geändert; kein Fenster überlappt (geprüft).

## Fassung v3 (Synchronität geprüft, Schluss-Einordnung)
Anlass: Der Nutzer bemerkte, dass Ton und Bild manchmal nicht ganz zusammenpassen und dass am Ende (Ende Szene 5) eine Einordnung fehlt. Fassung v3 = `franz_und_die_glaskugel_szenen_0-5_v3.mp4`; v1 und v2 bleiben unverändert.

**Messmethode (Fakten).** Aus der MP4 wird die Tonspur per ffmpeg (imageio-ffmpeg) als Mono-WAV mit 44,1 kHz extrahiert; je Sprechstück wird der erste Abtastwert über -40 dBFS in einem Suchfenster (Soll - 0,5 s bis Soll + 1,5 s, nicht vor dem Ende des vorigen Stücks) als Einsatz gesucht und mit dem Soll verglichen. Soll = Untertitelbeginn im Videozeitmaß (+ gemessene Anfangsstille der WAV); Videozeit = Quellzeit - 8 s, nach der Quizpause (Quelle 116 s) Quellzeit - 8 s - 7,5 s (Quelle 105 bis 116 s entfällt, im Video 3,5 s Standbild). Ergebnis an v2: alle 20 Sprechstücke (Index 0 bis 19, auch die Quizfrage und alle nach der Quizpause) setzen auf +-0,005 s genau am Soll ein; die Enden liegen 0,03 bis 0,2 s vor dem Soll (Ausklang unter -40 dBFS): **kein Drift, kein Versatz** im Mux (`adelay` in ganzen Millisekunden, Tonspur mit `apad`, Dauer 170,5 s Bild und Ton gleich). Die Schwäche lag also nicht im Zusammenbau, sondern in der Lage einzelner Bildereignisse zum gesprochenen Wort (siehe unten). Die Wiedergabe im Browser (HTML) startet jedes Sprechstück am Untertitelbeginn und korrigiert bei mehr als 0,35 s Abweichung; das wurde nicht gemessen, nur im Code gelesen.

**Abgleich Sprechbeginn mit Bildereignis.** Wortlagen im Sprechstück wurden aus den Sprechpausen der WAV-Dateien (Stille >= 120 ms) geschätzt, nicht per Spracherkennung; Genauigkeit etwa +-0,2 s.

| Untertitel | Wort im Sprechtext (v2-Zeit) | Bildereignis (v2) | Abweichung v2 | v3 |
|---|---|---|---|---|
| 8 (71,0) | „Nur elf von vierundzwanzig“ ab 73,7 | Stempel „11 von 24 richtig“ 71,2 | Bild 2,5 s zu früh | Stempel 73,6 bis 73,9, Mimik von Franz/Bit ab 73,7 |
| 10 (88,6) | „Runde zwei“ 88,7 | Radbeschriftung „Runde 2“ ab 84 | Rad 4,6 s zu früh | Umschaltung bei 88 (Szenengrenze) |
| 11 (97,0) | „Das Ziel steht vorher fest“ 99,3; „Sechzig Prozent“ 101,1 | Karte „Ziel 60 %“ ab 97,5 | 1,8 bis 3,6 s zu früh | Karte ab 99,2 |
| 13 (121,5) | „Achtundzwanzig Komma acht Prozent“ bis ca. 123,4 | Balken/Zähler fertig 122,5 | ca. 0,9 s zu früh | Balken fertig 123,2 |
| 19 (alt 173,0) | „Ergebnis“ 173,0 | Tafel „66 von 70“ 173,4 | ok (0,4 s) | Tafel jetzt 167,8 bis 168,6 mit dem neuen Fenster (siehe unten) |
| 2 (24,0) | „Wann laufen die Verträge der Konkurrenz aus?“ 24,0 bis 26,5 | Kiste mit der Frage 24,4 | ok (die Kiste zeigt die Frage); „Blackbox“ erst 27,6 | unverändert |
| 17 (152,5) | „Moment mal“ 152,5 | Auftritt Prüfi 151,8 bis 152,7 | ok (0,2 s) | unverändert |
| 14 (127,0) | „Sinngemäß hieß es im Gespräch“ 127,0 | Sprechblase 127,3 | ok | unverändert |
| 18 (161,0) | „versiegeln“ ca. 166,2 | Siegel 166,5 | ok | unverändert |
| 3, 4, 5, 6, 7, 9, 10 (Rad), 15 | Auftritt Glühbirne, Daten, Bit, Rad, Linien, Klemmbrett | Bildereignis innerhalb ca. 0,5 s vom Wort (Schätzung) | ok | unverändert |
| 1 (15,0), 16 (146,0) | „Vier Wochen“ 16,6; „Liste fertig, 9.325 Verträge“ | Karte 16,4; kein eigenes Bildereignis für „Liste fertig“ | ok bzw. nicht prüfbar | unverändert |

Kein Sprechstück reicht in einen Wischer (+-0,6 s um 8, 36, 62, 88, 138, 186 s); spätestes Ende vor einer Grenze: Untertitel 14 bei ca. 137,1 s (Wischer ab 137,4 s).

**Schluss-Einordnung (neu).** Das letzte Fenster (173 bis 185,5 s, 11,2 s Sprechzeit) ließ keinen Platz. Darum liegen Ergebnistafel und Untertitel 19 jetzt früher (167,9 bis 179,1 s; Untertitel 18 endet 167,7 s, Sprechende bei ca. 166,8 s; Briefumschläge blenden um 167,8 bis 168,2 aus) und ein neuer Untertitel 20 (179,2 bis 185,35 s) enthält die Einordnung. Die Tempostufen des Sprechers (`length_scale`) stehen im Manifest. Szenengrenzen `B` und Zeiten der Szenen 6 bis 8 sind nicht verändert; die CAPS-Indizes ab 20 sind um 1 verschoben (alter 20 = neuer 21 usw.), `sprechertext.json` und die WAV-Namen folgen.
- Untertitel: „Einordnung: Das Vertragsende lässt sich meist lesen. Den Termin der Neuausschreibung sagt es nicht voraus. Ob daraus ein Geschäft wird, ist offen.“
- Sprechtext (kürzer wegen der Zeit): „Das Vertragsende lässt sich meist lesen. Den Termin sagt es nicht voraus. Ob daraus ein Geschäft wird, ist offen.“
- Bildkarte „Einordnung“: Vertragsende: lesbar · Termin: nicht vorhersagbar · Geschäft: offen (Einblendung mit dem Satzbeginn).
- Belege der Formulierung (Interpretation, nicht stärker als die Zahlen): „meist lesen“ = 66 von 70 gleich mit dem Vergleichswert zweier nicht unabhängiger KI-Leser, Vergleichswert teils zirkulär, Mensch 14 von 15; „Termin nicht voraus“ = Trefferquote 28,8 % gegenüber dem Ziel 60 % (`reports/evaluation_iteration5.md`); „Geschäft offen“ = Business-Case-Prüfung ohne tragfähigen Case, Hypothesen ungeprüft (`docs/business_case_auswahl.md`).
- Weitere Zeitänderungen in der Animation: Rad „Prüfen“ 168,0 (vorher 173), „Einsetzen“ 179,4 (vorher 181), Jubel von Franz nur zum Satz „vierzehn stimmen“ (ab 177,7 s).
- Alle WAV-Dateien wurden für v3 neu erzeugt; Piper ist nicht bitgenau reproduzierbar, Sprechdauern schwanken um einige Zehntelsekunden zwischen Läufen (v2-Ton liegt nur in der MP4).
- Die Einordnung ist **nicht** Teil der Belege der Iterationen, sondern eine Zusammenfassung der Aussagen im Video.

## Quellen der Zahlen im Video
| Zahl im Video | Quelle |
|---|---|
| 11 von 24 Zuordnungen richtig (Runde 1) | `docs/iterationen.md` (Iteration 3), `reports/evaluation_iteration3.md` |
| 28,8 % bei 52 geprüften Paaren; naive Regel 17,3 %; Ziel 60 % | `docs/iterationen.md` (Iteration 5), `reports/evaluation_iteration5.md` |
| 9.325 Verträge (Lose) der Liste | `docs/iterationen.md` (Iteration 9, Liste Fassung 9) |
| 66 von 70 gleich mit dem Vergleichswert zweier KI-Leser; 14 von 15 beim Menschen (Kommilitone) | `docs/iterationen.md` (Iteration 9, V1, V6), `reports/evaluation_iteration9.md` |
| 230 verglichene Lose, 23 davon (10,0 %) nur bei der Liste richtig; Ursachen der 15 abweichenden Lose in 10b: 7 Höchstende, 4 Losebene, 4 sonstige | `reports/evaluation_iteration10b.md` (Tabelle „Gesamtbild“, „Einordnung der 15 diskordanten Lose“; Stichproben n = 70 und n = 160 gepoolt) |
| Optionsanalyse 70,8 %, n = 24 | `reports/optionsanalyse.md`, `docs/lab_log.md` |
| 130 Oberpfalz-Lose; Auftragnehmer genannt 99,2 % („99 %“); Wert über 1 € 47,7 % („48 %“) | `reports/wettbewerbsbild_oberpfalz.md` §2 |
| „nie günstiger“ gegen kostenlose Dienste | `reports/make_or_buy.md`, `docs/business.md` §9 (Modellkonstruktion, keine Messung) |
| n = 3 Gespräche; Aussagen der Figuren (Wettbewerbsdaten statt Enddaten; Formblätter) | `docs/business.md` §8.9 |
| Daten ab 2016 | TED Search API ab Ende Oktober 2016, `docs/phasen/02_data_understanding.md` und `docs/iterationen.md` |

Abweichungen bei der Prüfung: keine falschen Zahlen gefunden. Zwei Vereinfachungen bleiben stehen: (a) „Liste fertig! 9.325 Verträge“ steht vor der Korrektur, die Zahl gehört zur späteren Fassung der Iteration 9 (vorher 9.915); (b) das CRISP-DM-Rad zeigt vier „Runden“, das Projekt hatte zehn Iterationen. Die Reihenfolge „Runde 4 / Geschäft verstehen“ in Szene 6 ist eine Dramaturgie, keine Zählung aus `docs/iterationen.md`. Eintrag in `docs/ki_irrwege.md`.

## Abspielen (Browser)
`docs/video/franz_und_die_glaskugel.html` im Browser öffnen (Edge/Chrome); Ton liegt in `docs/video/audio/` (Ordner mitnehmen).
- Standard ohne Parameter: ganze Fassung (0 bis 276 s). Nur Szenen 1 bis 5: `…html?von=8&bis=186`. (Hinweis: 8 s ist das Ende des Titelbilds; für Titel mit: `?von=0&bis=186`.)
- Start per Klick oder Leertaste (nötig, damit der Browser den Ton erlaubt).
- Leertaste oder Klick: Pause/weiter; Pfeil links/rechts: 5 s zurück/vor; **M**: Ton stumm/an; **R**: Neustart.
- Quizpause bei 105 s: Die Quizfrage wird zu Ende gesprochen; Leertaste löst auf.
- `?render` schaltet das Abspielen ab und stellt `window.render(t)` bereit (für den Export).
- Schriftart Inter ist nicht überall installiert; dann greifen Helvetica Neue oder Arial (Zeilenumbrüche können minimal abweichen).

## Sprecherstimme
`src/report/video_vertonung.py` erzeugt je Untertitel (Index in `CAPS`) eine Datei `audio/cap_NN.wav` im Caption-Fenster und `audio/manifest.json` (Dauer, Spitzenpegel, Stille am Anfang, Einstellung). Gesprochen wird der **Sprechertext** aus `docs/video/sprechertext.json` (Index -> Text), nicht der Untertitel: fürs Hören geschrieben (kurze Sätze, Zahlen und Kürzel ausgeschrieben, z. B. „achtundzwanzig Komma acht Prozent“, „K I“, „T E D“, „elf von vierundzwanzig“). Einschränkungen des Untertitels (nicht unabhängig, Hinweis, nachgestellt, synthetisch) bleiben im Sprechtext erhalten. Alle Stimmen sind **synthetisch**.

Der Schalter `--stimme` wählt den Weg:
| Weg | Aufruf | Eigenschaften |
|---|---|---|
| **piper** (Standard) | `.venv-video\Scripts\python.exe -I src\report\video_vertonung.py` | offline, kostenlos, Modell `de_DE-thorsten-high` |
| piper-mehrstimmig | `... --stimme piper-mehrstimmig` | offline, eigenes Modell je Figur (siehe unten) |
| edge | `... --stimme edge` | Cloud (Microsoft, inoffiziell), Texte verlassen den Rechner |
| elevenlabs | `... --stimme elevenlabs` (Plan ohne Netz: `--trocken`) | Cloud, braucht Konto und Schlüssel |
| sapi | `... --stimme sapi` | frühere Fassung v1 (Windows Hedda), Ausgabe in `audio_sapi/` |

### Piper (Standard)
- Paket `piper-tts` (Version in `requirements-video.txt`), Modell `de_DE-thorsten-high` (Fallback `-medium`) von Hugging Face (`rhasspy/piper-voices`, Pfad `de/de_DE/thorsten/high/`). Ablage **außerhalb des Repos**: `%LOCALAPPDATA%\piper_models\de_DE-thorsten-high.onnx` und `.onnx.json`; anderer Ort per `--modell PFAD.onnx`.
- Lizenz: Die Stimme „Thorsten“ (Thorsten-Voice, Thorsten Müller) steht laut Modellkarte unter CC0 (gemeinfrei). Piper selbst: MIT-Lizenz; Sprachausgabe nutzt eSpeak-NG-Daten im Paket (GPL-3-Lizenz der eSpeak-NG-Daten, bei Weitergabe des Pakets beachten; das Video enthält nur die erzeugte Audiodatei).
- Das Modell hat **einen** Sprecher. Die Figuren werden über Tonhöhe und Tempo unterschieden (ffmpeg): Franz etwas höher und flotter, Bit (KI) deutlich höher mit leichtem Tremolo (robotisch), Prüfi tiefer, Erzähler unverändert. Das Tempo (`length_scale`) wird je Untertitel nur erhöht, wenn die Dauer sonst nicht ins Fenster passt (Dauer <= Fenster - 0,3 s). Aufnahmen werden vorne von Stille befreit und auf -3 dBFS Spitze normiert.
- Ob „T E D“ oder „Ted“ besser klingt, wurde **nicht gehört**; im Sprechtext steht „T E D“ (Buchstabieren), änderbar in `sprechertext.json`.

### Mehrstimmig: piper-mehrstimmig und edge (gewählt: edge, Fassung v4)
Anlass: Der Nutzer wollte eine menschlichere Stimme und Stimmvorlagen. _Nachtrag 2026-11-09:_ Gewählt wurde **edge**; die Fassung v4 ist damit erzeugt (Commit b87088c, Abspann „Microsoft Neural-Stimmen ueber edge-tts“). Der folgende Text beschreibt den Stand vor der Wahl; die Videos v1 bis v3 sind unverändert. Die Zuordnung Figur -> Stimme steht in `docs/video/stimmen.json` (Abschnitte `piper_mehrstimmig` und `edge`, jeweils mit Feld `abspann`).

**Hörproben** (5 Sätze: Erzähler, Franz, Bit, Prüfi, Erzähler): `docs/video/stimmproben/probe_piper-mehrstimmig.wav` und `probe_edge.wav`. Neu erzeugen: `.venv-video\Scripts\python.exe -I src\report\video_vertonung.py --stimme piper-mehrstimmig --probe` (bzw. `--stimme edge --probe`). `--probe` schreibt nur dorthin, nicht nach `audio/`, und ändert die HTML nicht.

**Nach der Wahl genügen zwei Befehle** (Beispiel für Piper mehrstimmig; für Edge `--stimme edge`):
```
.venv-video\Scripts\python.exe -I src\report\video_vertonung.py --stimme piper-mehrstimmig
.venv-video\Scripts\python.exe src\report\video_export.py --out docs\video\franz_und_die_glaskugel_szenen_0-5_v4.mp4
```
Der erste Befehl erzeugt alle `audio/cap_NN.wav` und `manifest.json` neu (überschreibt die jetzigen WAVs; die v3-Töne stecken weiter in der v3-MP4) und setzt den Stimmennamen im Abspann und auf dem Startbildschirm der HTML aus dem Feld `abspann` der `stimmen.json` (nur diese zwei Textstellen, der Szenenablauf bleibt unverändert). Das Tempo je Untertitel wird wie bei Piper automatisch angepasst (Dauer <= Fenster - 0,3 s). Zurück zur alten Stimme: `--stimme piper` (setzt den Abspann **nicht** zurück; dort `Stimmen: synthetisch (...)` von Hand oder aus Git wiederherstellen).

**Piper mehrstimmig** (offline). Modelle liegen außerhalb des Repos in `%LOCALAPPDATA%\piper_models`. Geprüfte Liste (Hugging Face `rhasspy/piper-voices`, `de/de_DE`, Modellkarten am 2026-11-09 gelesen):
| Modell | Qualität | Lizenz laut Modellkarte | Entscheidung |
|---|---|---|---|
| thorsten (high/medium/low) | 22 kHz | CC0 | benutzt: Erzähler (high), Bit (medium) |
| thorsten_emotional (medium, 8 Sprecher: amused, angry, disgusted, drunk, neutral, sleepy, surprised, whisper) | 22 kHz | CC0 | benutzt: Franz (Sprecher `amused`) |
| kerstin (low) | 16 kHz | CC0 | benutzt: Prüfi (weibliche Stimme; die Karte nennt kein Geschlecht, nach dem Namen angenommen) |
| mls (medium, 236 Sprecher) | 22 kHz | CC-BY 4.0 (OpenSLR 94, Namensnennung nötig) | heruntergeladen, **nicht benutzt** (Geschlecht und Klang der Sprecher-IDs ohne Hören nicht wählbar) |
| karlsson, ramona (low), eva_k (x_low) | 16 kHz | Karte nur „See URL“ (M-AILABS, caito.de); die Seite war nicht erreichbar | **nicht benutzt** (Lizenz nicht geprüft) |
| pavoque (low) | 16 kHz | CC BY-NC-SA 4.0 | **nicht benutzt** (Weitergabe nur nichtkommerziell und unter gleichen Bedingungen) |
Die niedrige Qualität von kerstin (16 kHz) klingt vermutlich dumpfer als Thorsten-high; ungehört.
Bit bleibt leicht robotisch (Tonhöhe x1,14 und Tremolo per ffmpeg). Ein Modell je Figur lädt die Datei einmal; erster Aufruf mit allen Modellen braucht zusätzlich Speicher (rund 300 MB Modelle gesamt). Zusätzlich geladen: `de_DE-kerstin-low`, `de_DE-thorsten_emotional-medium`, `de_DE-mls-medium` (je `.onnx` und `.onnx.json` von `https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/<name>/<qualität>/`).

**Edge (Microsoft-Neuralstimmen)**, Paket `edge-tts==7.3.1` in `requirements-video.txt` (Installation: `.venv-video\Scripts\python.exe -m pip install -r requirements-video.txt`). Stimmenliste: `.venv-video\Scripts\edge-tts.exe --list-voices` (deutsch: Amala, Conrad, FlorianMultilingual, Katja, Killian, SeraphinaMultilingual). Zuordnung: Erzähler Florian (Multilingual), Franz Conrad, Bit Killian (Tonhöhe +25 Hz plus Tremolo), Prüfi Katja, Frage ans Publikum Seraphina. `rate` und `pitch` je Figur in `stimmen.json` als Basis; das Skript erhöht die Rate in 5-Prozent-Schritten (bis +35 Prozent über der Basis), bis die Dauer ins Fenster passt. Aufnahmen werden wie bei Piper von Stille befreit und auf -3 dBFS normiert.
- **Prüfung der Fenster (2026-11-09, Trockenlauf in ein Temp-Verzeichnis, nicht nach `audio/`):** Alle 29 Untertitel passen bei beiden Wegen (Dauer <= Fenster - 0,3 s), Spitze -3 dBFS, keine Klipps, Anfangsstille <= 0,05 s. Piper mehrstimmig brauchte nur Tempo 0,90 bis 1,00. Edge ist langsamer als die Fenster: der Erzähler Florian braucht oft +5 bis +20 Prozent Rate, bei Untertitel 20 (Einordnung) +35 Prozent (Grenze der Automatik), Untertitel 0, 6, 14, 19 +20 Prozent. Das klingt dort vermutlich gehetzt (ungehört); Abhilfe: Sprechtext in `sprechertext.json` kürzen oder den Erzähler auf eine andere Stimme setzen.
- **Datenabfluss und Status:** Die Sprechtexte (öffentliche Projektfakten, keine personenbezogenen Daten) werden an einen Microsoft-Dienst gesendet. `edge-tts` nutzt den Online-Dienst des Edge-Browsers über einen **inoffiziellen** Zugang, ohne Vertrag, ohne Zusicherung der Verfügbarkeit und ohne klare Nutzungsbedingungen für Dritte; für ein Studienprojekt vom Nutzer ausdrücklich gewünscht. Das Ergebnis (WAV im Video) ist reproduzierbar nur, solange der Dienst die Stimmen unverändert anbietet; Netz ist zur Erzeugung nötig, danach nicht mehr.
- Die Lizenzlage der erzeugten Audiodaten ist nicht geklärt; vor einer Veröffentlichung außerhalb des Studienprojekts prüfen.

### ElevenLabs (optional, nicht getestet)
- Voraussetzung: eigenes ElevenLabs-Konto, Umgebungsvariable `ELEVENLABS_API_KEY` (**nie in Dateien schreiben**), echte `voice_id` je Sprecher in `docs/video/stimmen.json` (dort stehen Platzhalter `HIER_VOICE_ID_EINTRAGEN`, keine erfundenen IDs). Modell `eleven_multilingual_v2`, Ausgabe `pcm_22050`.
- **Datenabfluss:** Die Sprechtexte werden an ElevenLabs gesendet (Cloud). **Kosten** und Kontingent laufen über das Konto des Nutzers (hier rund 4.500 Zeichen je Durchlauf, Zahl steht im Trockenlauf).
- Aufruf: `$env:ELEVENLABS_API_KEY="..."` setzen, dann `.venv-video\Scripts\python.exe -I src\report\video_vertonung.py --stimme elevenlabs`. Vorher mit `--trocken` prüfen (kein Netz, nichts gesendet).
- Die API-Nutzung (`ElevenLabs(api_key=...)`, `client.text_to_speech.convert(voice_id=..., text=..., model_id=..., output_format=...)`, liefert Byte-Blöcke) folgt der aktuellen Python-SDK (Version 2.77.0, Doku github.com/elevenlabs/elevenlabs-python). **Der Zweig wurde nie gegen die API ausgeführt**, nur der Trockenlauf wurde geprüft. Der Stimmenwechsel macht die Namensangabe im Abspann (Zeile „Stimme: synthetisch (Piper, Thorsten-Voice)“ in der HTML) falsch; dann anpassen.
- Ein einziger Gesamttext über das ganze Video wird bewusst nicht benutzt: Untertitel und Animation hängen an festen Sekunden, ein Gesamttext verliert den Gleichlauf.

## MP4-Export
`src/report/video_export.py` (eigene venv `.venv-video`, in `.gitignore`; Versionen in `requirements-video.txt`: playwright, imageio-ffmpeg). Browser: installiertes Edge (`channel="msedge"`), kein Download; ffmpeg kommt aus `imageio-ffmpeg`.
```
python -m venv .venv-video
.venv-video\Scripts\python.exe -m pip install -r requirements-video.txt
.venv-video\Scripts\python.exe src\report\video_export.py            # Standard: 8 bis 186 s, 30 fps
.venv-video\Scripts\python.exe src\report\video_export.py --von 0 --bis 186 --out mein.mp4
```
Ergebnis (Stand der Erzeugung von v3): `docs/video/franz_und_die_glaskugel_szenen_0-5_v3.mp4` (**danach v4** mit Edge-Stimmen; aktuell ist inzwischen `franz_video_ton.mp4`, siehe oben; gleiche Länge 170,5 s; v2 = Piper-Stimme ohne Einordnung und mit den alten Bildzeiten; die erste Fassung mit SAPI-Stimme `franz_und_die_glaskugel_szenen_0-5.mp4` bleibt als v1 erhalten, ältere WAVs in `audio_sapi/`; Ordner mit anderen WAVs per `--audio DIR`) (H.264, AAC, yuv420p, 1280 x 720, 30 fps; der Dateiname folgt der Auftragsvorgabe, der Standardbereich 8 bis 186 s umfasst die Szenen 1 bis 5 der Zeitleiste `B`, das Titelbild 0 bis 8 s ist nicht enthalten).
**Quizphase im Export:** Das Quizbild (Live-Zeit 105 s) steht 3 s still (danach 0,5 s) mit dem Hinweis „Auflösung folgt …“; die Zeit 105 bis 116 s der Live-Fassung entfällt, das Video läuft bei 116 s weiter. Die Quizfrage wird in diesen Sekunden gesprochen. Die Standbilder werden bei 30 fps per `window.render(t)` aufgenommen und direkt an ffmpeg gegeben (keine Zwischendateien); die Tonspur wird aus den WAVs mit `adelay` an den Untertitel-Anfängen gemischt.

## Grenzen
_Grenzen der früheren Fassungen v1 bis v4; für die aktuelle Fassung siehe oben._
- Stimmen **synthetisch**: v4 nutzt Microsoft-Neuralstimmen über edge-tts, einen **inoffiziellen** Zugang ohne Vertrag; die Lizenzlage der erzeugten Audiodaten ist ungeklärt (v2 und v3: Piper, Thorsten-Voice, CC0). Betonung maschinell. **Die Klangqualität wurde vom Bearbeiter (KI) nicht gehört**, nur Dauer, Pegel und Anfangsstille wurden gemessen. Offener Punkt: Eine Hörprobe der Fassung v4 ist nicht dokumentiert.
- Alle **Figuren sind erfunden**; die Gespräche im Video sind **nachgestellt** und verändert, es gab nur **drei** echte Telefongespräche (n = 3, Hinweise, keine Statistik, `docs/business.md` §8.9).
- Das Video ist eine Vereinfachung des Projektverlaufs (vier Runden statt zehn Iterationen); Belege und Grenzen stehen in `docs/iterationen.md`, `docs/lab_log.md` und den Evaluationsberichten.
- Nicht belegt bleibt: Qualitätsvorsprung der Liste gegenüber kostenlosen Diensten, Nachfrage, Zahlungsbereitschaft. „Nie günstiger“ folgt aus der Modellkonstruktion mit Annahmen.
- Der Export wurde nur mit Edge unter Windows geprüft. Die Untertitel sind im Bild eingebrannt, nicht als eigene Spur.
