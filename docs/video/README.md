# Video „Franz und die Glaskugel“

## Zweck
Zusammenfassung des Projekts Vergabe-Radar in rund 4,5 Minuten (276 s Live-Fassung, 1280 x 720) für den Vortrag und das Lab-Log: von der Idee (Prognose von Vertragsenden) über die gescheiterte Punktprognose und die Vertragsliste bis zur Entscheidung „Selbst bauen? Nein.“ Erzählt wird mit erfundenen Figuren (Franz, Bit, Prüfi). Das Video ist eine Veranschaulichung, kein zusätzlicher Beleg.

## Herkunft
- Die HTML/SVG-Animation wurde von einem Kollegen **KI-gestützt** erstellt (Original: `Franz_und_die_Glaskugel_live.html`, nicht im Repo, Original unverändert).
- Diese Fassung `franz_und_die_glaskugel.html` ist von uns (Manuel Strobel, Ludwig Richthammer) **korrigiert und erweitert** (siehe unten). Autorenzeile im Abspann.

## Was gegenüber dem Original geändert wurde (Fakten)
Nur Texte und Technik, **keine Zahlen**:
1. Schlusssatz: „Genau das haben uns die Daten gezeigt“ ersetzt durch „Das zeigt unsere Rechnung mit Annahmen und der Blick auf kostenlose Dienste.“
2. Szene 7: Untertitel „Im Modell, mit unseren Annahmen und nicht als Messung: Selbstbauen ist gegen einen kostenlosen Dienst nie günstiger.“ (die Waage trägt schon „Kostenmodell mit Annahmen, keine Messung“).
3. Szene 6: „rund 10 Prozent“ ergänzt um „meist anderes Datum für das Höchstende statt der Grundlaufzeit, teils Losebene; ein Qualitätsvorsprung ist nicht belegt“ (Untertitel und Karte).
4. Szene 5: Einschränkung „Die zwei KI-Leser sind nicht unabhängig, der Vergleichswert ist teils zirkulär; der Mensch prüfte 15 Fälle: 14 stimmen“ (Untertitel und Karte).
5. Szene 4: Die Aussage der Vergabestelle ist als „sinngemäß, Hinweis aus einem Gespräch und einer Optionsanalyse (70,8 %, n = 24)“ gekennzeichnet (Untertitel und Karte, „kein Beleg“).
6. Szene 2: Karte „Daten: TED, Gebäudereinigung, Deutschland, ab 2016“.
7. Abspann: „Autoren: Manuel Strobel, Ludwig Richthammer. Stimme: synthetisch (Piper, Thorsten-Voice).“ (v1: Windows SAPI)
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

### Mehrstimmig: piper-mehrstimmig und edge (Wahl steht aus)
Anlass: Der Nutzer wollte eine menschlichere Stimme und Stimmvorlagen. Beide Wege sind **vorbereitet, aber noch nicht als Standard erzeugt**; `docs/video/audio/` und die Videos v1 bis v3 sind unverändert. Die Zuordnung Figur -> Stimme steht in `docs/video/stimmen.json` (Abschnitte `piper_mehrstimmig` und `edge`, jeweils mit Feld `abspann`).

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
Ergebnis: `docs/video/franz_und_die_glaskugel_szenen_0-5_v3.mp4` (aktuelle Fassung; v2 = Piper-Stimme ohne Einordnung und mit den alten Bildzeiten; die erste Fassung mit SAPI-Stimme `franz_und_die_glaskugel_szenen_0-5.mp4` bleibt als v1 erhalten, ältere WAVs in `audio_sapi/`; Ordner mit anderen WAVs per `--audio DIR`) (H.264, AAC, yuv420p, 1280 x 720, 30 fps; der Dateiname folgt der Auftragsvorgabe, der Standardbereich 8 bis 186 s umfasst die Szenen 1 bis 5 der Zeitleiste `B`, das Titelbild 0 bis 8 s ist nicht enthalten).
**Quizphase im Export:** Das Quizbild (Live-Zeit 105 s) steht 3 s still (danach 0,5 s) mit dem Hinweis „Auflösung folgt …“; die Zeit 105 bis 116 s der Live-Fassung entfällt, das Video läuft bei 116 s weiter. Die Quizfrage wird in diesen Sekunden gesprochen. Die Standbilder werden bei 30 fps per `window.render(t)` aufgenommen und direkt an ffmpeg gegeben (keine Zwischendateien); die Tonspur wird aus den WAVs mit `adelay` an den Untertitel-Anfängen gemischt.

## Grenzen
- Stimme **synthetisch** (Piper, Thorsten-Voice), ein Modell für alle Figuren (nur Tonhöhe und Tempo unterscheiden sie), Betonung maschinell. **Die Klangqualität wurde vom Bearbeiter (KI) nicht gehört**, nur Dauer, Pegel und Anfangsstille wurden gemessen; Hörprobe durch den Nutzer steht aus.
- Alle **Figuren sind erfunden**; die Gespräche im Video sind **nachgestellt** und verändert, es gab nur **drei** echte Telefongespräche (n = 3, Hinweise, keine Statistik, `docs/business.md` §8.9).
- Das Video ist eine Vereinfachung des Projektverlaufs (vier Runden statt zehn Iterationen); Belege und Grenzen stehen in `docs/iterationen.md`, `docs/lab_log.md` und den Evaluationsberichten.
- Nicht belegt bleibt: Qualitätsvorsprung der Liste gegenüber kostenlosen Diensten, Nachfrage, Zahlungsbereitschaft. „Nie günstiger“ folgt aus der Modellkonstruktion mit Annahmen.
- Der Export wurde nur mit Edge unter Windows geprüft. Die Untertitel sind im Bild eingebrannt, nicht als eigene Spur.
