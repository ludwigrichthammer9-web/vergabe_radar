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
| elevenlabs | `... --stimme elevenlabs` (Plan ohne Netz: `--trocken`) | Cloud, braucht Konto und Schlüssel |
| sapi | `... --stimme sapi` | frühere Fassung v1 (Windows Hedda), Ausgabe in `audio_sapi/` |

### Piper (Standard)
- Paket `piper-tts` (Version in `requirements-video.txt`), Modell `de_DE-thorsten-high` (Fallback `-medium`) von Hugging Face (`rhasspy/piper-voices`, Pfad `de/de_DE/thorsten/high/`). Ablage **außerhalb des Repos**: `%LOCALAPPDATA%\piper_models\de_DE-thorsten-high.onnx` und `.onnx.json`; anderer Ort per `--modell PFAD.onnx`.
- Lizenz: Die Stimme „Thorsten“ (Thorsten-Voice, Thorsten Müller) steht laut Modellkarte unter CC0 (gemeinfrei). Piper selbst: MIT-Lizenz; Sprachausgabe nutzt eSpeak-NG-Daten im Paket (GPL-3-Lizenz der eSpeak-NG-Daten, bei Weitergabe des Pakets beachten; das Video enthält nur die erzeugte Audiodatei).
- Das Modell hat **einen** Sprecher. Die Figuren werden über Tonhöhe und Tempo unterschieden (ffmpeg): Franz etwas höher und flotter, Bit (KI) deutlich höher mit leichtem Tremolo (robotisch), Prüfi tiefer, Erzähler unverändert. Das Tempo (`length_scale`) wird je Untertitel nur erhöht, wenn die Dauer sonst nicht ins Fenster passt (Dauer <= Fenster - 0,3 s). Aufnahmen werden vorne von Stille befreit und auf -3 dBFS Spitze normiert.
- Ob „T E D“ oder „Ted“ besser klingt, wurde **nicht gehört**; im Sprechtext steht „T E D“ (Buchstabieren), änderbar in `sprechertext.json`.

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
Ergebnis: `docs/video/franz_und_die_glaskugel_szenen_0-5_v2.mp4` (Piper-Stimme; die erste Fassung mit SAPI-Stimme `franz_und_die_glaskugel_szenen_0-5.mp4` bleibt als v1 erhalten, ältere WAVs in `audio_sapi/`; Ordner mit anderen WAVs per `--audio DIR`) (H.264, AAC, yuv420p, 1280 x 720, 30 fps; der Dateiname folgt der Auftragsvorgabe, der Standardbereich 8 bis 186 s umfasst die Szenen 1 bis 5 der Zeitleiste `B`, das Titelbild 0 bis 8 s ist nicht enthalten).
**Quizphase im Export:** Das Quizbild (Live-Zeit 105 s) steht 3 s still, in den letzten 0,5 s mit dem Hinweis „Auflösung folgt …“; die Zeit 105 bis 116 s der Live-Fassung entfällt, das Video läuft bei 116 s weiter. Die Quizfrage wird in diesen Sekunden gesprochen. Die Standbilder werden bei 30 fps per `window.render(t)` aufgenommen und direkt an ffmpeg gegeben (keine Zwischendateien); die Tonspur wird aus den WAVs mit `adelay` an den Untertitel-Anfängen gemischt.

## Grenzen
- Stimme **synthetisch** (Piper, Thorsten-Voice), ein Modell für alle Figuren (nur Tonhöhe und Tempo unterscheiden sie), Betonung maschinell. **Die Klangqualität wurde vom Bearbeiter (KI) nicht gehört**, nur Dauer, Pegel und Anfangsstille wurden gemessen; Hörprobe durch den Nutzer steht aus.
- Alle **Figuren sind erfunden**; die Gespräche im Video sind **nachgestellt** und verändert, es gab nur **drei** echte Telefongespräche (n = 3, Hinweise, keine Statistik, `docs/business.md` §8.9).
- Das Video ist eine Vereinfachung des Projektverlaufs (vier Runden statt zehn Iterationen); Belege und Grenzen stehen in `docs/iterationen.md`, `docs/lab_log.md` und den Evaluationsberichten.
- Nicht belegt bleibt: Qualitätsvorsprung der Liste gegenüber kostenlosen Diensten, Nachfrage, Zahlungsbereitschaft. „Nie günstiger“ folgt aus der Modellkonstruktion mit Annahmen.
- Der Export wurde nur mit Edge unter Windows geprüft. Die Untertitel sind im Bild eingebrannt, nicht als eigene Spur.
