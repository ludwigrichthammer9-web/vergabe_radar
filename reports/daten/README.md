# Daten zum Nachrechnen (Analysetabelle, Backtest-Paare, Lösungsschlüssel)

_Stand 2026-11-09. Byte-gleiche Kopien aus `data/processed/` (lokal, nicht im Git); mit `cmp` gegen die Originale geprüft, 0 Abweichungen.
Alle Blindprüfungen und Stichproben, zu denen diese Schlüssel gehören, sind abgeschlossen; die Schlüssel sind deshalb kein Prüfgeheimnis mehr.
Zusammen 11 Dateien, 1.849.004 Bytes (rund 1,8 MB). Nachrechnen: `docs/reproduzierbarkeit.md`, Abschnitt „Nachrechnen ohne TED-Abruf“._

**Inhalt und Datenschutz (geprüft 2026-11-09).** Spalten je Datei angesehen: Es gibt **keine Spalte mit Auftragnehmern** und keine mit
Namen von Prüfern. Enthalten sind TED-Nummern, Los-Nummern, Los-Titel, Daten, Herkunftsangaben der Regeln und (in der Vertragsliste und im
Schlüssel 10b) der Name des **Auftraggebers** (öffentliche Stellen laut TED). Die Spalte `mensch` im Schlüssel der Iteration 9 enthält nur
„ja“ (Los gehört zur menschlichen Kontrolle), keinen Namen; die Spalte `claude` im Schlüssel der Iteration 3 nur den Status „gefunden“.
Eine Textsuche nach den Namen des Teams fand nur Ortsnamen (z. B. „Ludwigsburg“). Quelle der Inhalte: TED, frei wiederverwendbar mit
Quellenangabe (`docs/quellen.md`).

## Hash-Prüfung

Fakten: SHA-256 am 2026-11-09 mit `sha256sum` berechnet und mit dem Wert verglichen, der **vor** der jeweiligen Prüfung dokumentiert wurde
(`docs/iterationen.md`, Commits, Lab-Log Anhang A). „Zeilen“ = Datenzeilen ohne Kopfzeile.

| Datei | Inhalt | Zeilen | SHA-256 | Dokumentierter Hash stimmt | Herkunftsskript |
|---|---|---|---|---|---|
| `vertragsliste_909.csv` | Analysetabelle: Vertragsliste Fassung 9, je Los (16 Spalten, ohne Auftragnehmer) | 9.325 | `5ec733643f88ed8bd51e83617d471bead6b52a95ea4da305a0bd3a6f6d64f2b5` | ja (`docs/iterationen.md`, Iteration 9, Nachtrag Schritt 1) | `src/prepare/vertragsliste.py` |
| `backtest_paare_iteration5.csv` | 68 Backtest-Paare (Vorgänger-Ende nur aus den Bekanntmachungen des Vorgängers) | 68 | `c97e7fbda21f855cd2e22ddcb9b1649225ae7f90b04cf77ed941d0b88599adb4` | kein Hash dokumentiert | `src/prepare/backtest_paare.py` |
| `x1_paare_iteration5.txt` | Kennungen der 52 bestätigten Paare (X1), Backtest-Basis | 52 | `c336ea5848a21bed1d8df0dfb175596d9e0b7122998740386b6bc3eee02c4b9d` | kein Hash dokumentiert | kein erzeugendes Skript im Repo gefunden; Inhalt = X1 aus `reports/gt_pruefung_iteration5_auswertung.md` |
| `blindpruefung_iteration3_schluessel.csv` | Schlüssel Blindprüfung Iteration 3 (P1–P20) | 20 | `c45d448c11ab1d2296e63581ec1a0ca258a735d8b6e34757d5dc37556e319eaf` | ja (`docs/iterationen.md`, Iteration 3) | `src/blindpruefung_iteration3.py` |
| `blindpruefung_iteration3_schluessel_ergaenzung.csv` | Ergänzung Iteration 3 (P21–P28, Seed 20261025) | 8 | `59672f7ece76b5f6e8c54f3c7e43d653197cda4f23939bf3daf66778727ab4f2` | ja (`docs/iterationen.md`, Iteration 3) | `src/blindpruefung_iteration3.py --ergaenzen` |
| `blindpruefung_iteration4_schluessel.csv` | Schlüssel Blindprüfung Iteration 4 (W4, P1–P20) | 20 | `45aff7a4eb2399d0aafd3ff74c330016b858026e89d8f3738df3de966dbe9bcc` | ja (`docs/iterationen.md`, Iteration 4) | `src/blindpruefung_iteration4.py` |
| `gt_pruefung_iteration5_schluessel.csv` | Schlüssel Zweitprüfung Iteration 5 (71 Paare inkl. Köder) | 71 | `05abddc9a8e450dd2fa9706bfaf06e507740ab3f0fb507d8836c340043df0b8c` | ja (`docs/iterationen.md`, Iteration 5) | `src/prepare/backtest_paare.py` |
| `liste_pruefung_iteration6_schluessel.csv` | Schlüssel Prüfung der Liste Iteration 6 (60 Lose + 10 Paare) | 70 | `3de3e81270ee2488f8b8b2f60c42d4f7271eb196bfcf7e8aa92809a0ba689d0e` | ja (`docs/iterationen.md`, Iteration 6) | `src/prepare/stichprobe_iteration6.py` (Seed 20261105) |
| `liste_pruefung_iteration7_schluessel.csv` | Schlüssel Iteration 7 (95 Lose, auch Grundlage der Iteration 8) | 95 | `eade66c033ab13d541dda2f7af3f5b074f1b5a4587e711f6a29e0ba1916ddf9b` | ja (`docs/iterationen.md`, Iteration 7; Lab-Log Anhang A) | `src/prepare/stichprobe_iteration7.py` (Seed 20261106) |
| `stichprobe_iteration9_schluessel.csv` | Schlüssel Iteration 9 (110 Lose, Gruppen Z, M, R, S) | 110 | `9dbf5c1a1b30256fa70d8f16759c9c613edf41cb54102c76c50b5440bbdc8753` | ja (`docs/iterationen.md`, Iteration 9; Lab-Log Anhang A) | `src/prepare/stichprobe_iteration9.py` (Seed 20261109) |
| `stichprobe_iteration10b_schluessel.csv` | Schlüssel Iteration 10b (160 Lose) | 160 | `2cd0020634582a77e46155375cb655db9f0bc04f186bc5e6bbc6b446633a6e33` | ja (voller Wert in `src/prepare/vergleich_iteration10b.py`, Präfix `2cd00206…` in Lab-Log Anhang A); die Commit-Nachricht `9d63c59` nennt als Ende „…3e33“ statt „…6e33“ (Tippfehler in der Nachricht, Präfix stimmt) | `src/prepare/stichprobe_iteration10b.py` (Seed 20261112) |

**Ergebnis:** Bei allen 9 Dateien mit dokumentiertem Hash stimmt der Wert; für die beiden Paardateien der Iteration 5 war kein Hash dokumentiert.

## Nachgerechnet (2026-11-09, temporäre Kopie des Repos, nicht in `data/processed`)

Fakten: In einer Kopie des Stands `131804e` (ohne `data/`) wurden nur diese Dateien nach `data/processed/` gelegt und die Skripte ohne
TED-Abruf ausgeführt.

| Skript | Ergebnis |
|---|---|
| `src/model/baseline.py` | R0 9/52, R1 15/52 = 28,8 %; `reports/backtest_iteration5.md` byte-gleich |
| `src/report/optionsanalyse.py` | `reports/optionsanalyse.md` byte-gleich |
| `src/model/sensitivitaet_backtest.py` | `reports/sensitivitaet_iteration5.md` byte-gleich |
| `src/prepare/auswertung_iteration6.py` | Y1 54/60; Bericht byte-gleich |
| `src/prepare/auswertung_iteration7.py` | Y1 36/47, Y1r 8/15; Bericht gleich bis auf eine beschreibende Zeile („nach Losen gewichtet“ 80,5 statt 80,2 %) |
| `src/prepare/auswertung_iteration8.py` | Z0 94/95, Z1 77/80, Z2 14/15, Z3 75/80 und 67/72, Z4 10/10; gleich bis auf „Z1 nach Losen gewichtet“ (98,6 statt 98,0 %) |
| `src/prepare/auswertung_iteration9.py` | V1 66/70, V2 28/30, V5 110/110; Bericht byte-gleich |
| `src/prepare/stichprobe_iteration10b.py` | zieht mit Seed 20261112 dieselben 160 Lose; Schlüssel-Hash `2cd00206…6e33` identisch |
| `src/prepare/stichprobe_iteration9.py` | läuft **nicht**: braucht zusätzlich die alte Fassung `vertragsliste_909_iteration8.csv` (nicht veröffentlicht) |

_Deutung:_ Die beiden abweichenden Zeilen gewichten nach der Zahl der Lose in der aktuellen Liste (`src/prepare/vertragsliste.py`,
Fenster X4); zum Zeitpunkt der Iterationen 7 und 8 galt eine ältere Fassung der Liste. Die Kriterien (Zähler und Nenner) ändern sich nicht.
