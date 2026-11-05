# Vergleich Liste gegen Vergabeweiser, größere Stichprobe (Iteration 10b)

_Erzeugt mit `src/prepare/vergleich_iteration10b.py`. Kriterien vorab in `docs/iterationen.md` (Iteration 10b), Skript im Kopf mit den Definitionen. Schlüssel-SHA-256 `2cd00206…6e33` (stimmt mit dem Commit überein). Daten von Vergabeweiser: CC BY 4.0, Quelle „Vergabeweiser“ (vergabeweiser.de), Abruf 2026-11-05 ff., Rohdaten unverändert in `data/raw/vergabeweiser_20261105/`. In diesem Bericht stehen keine Datumswerte je Los (Leser bleiben blind); sie stehen in `data/processed/vergleich_iteration10b_voll.csv` (lokal)._

## Fakten

- Stichprobe: 160 Lose aus 154 Bekanntmachungen.
- **W10 Abdeckung:** Vergabeweiser hat einen Eintrag für 160/160 Lose (160/160 = 100,0 % (Wilson 97,7–100,0)); Bekanntmachungen zugeordnet 154/154 (Weg 1/2/3: 10/125/19). Unvollständig (TED-XML fehlt oder Abfrage vorläufig): 0 Bekanntmachungen (0 Lose) – diese gelten bis zu einem erneuten Lauf als „kein Eintrag“.
- Von 160 Losen mit Eintrag: Liste und Vergabeweiser gleich (± 1 Tag) bei 145; **diskordant 15** (an die Leser: `reports/vergleich_iteration10b_diskordant.csv`).
- Art des Werts von Vergabeweiser bei Losen mit Eintrag: {'datum': 160}.
- **W9 Ursachenverteilung der 15 diskordanten Lose:** (a) 5 = 33,3 %, (b) 6 = 40,0 %, (c) 0 = 0,0 %, (d) 0 = 0,0 %, (e) 4 = 26,7 %. Klassen: (a) Losebene, (b) Höchstende bzw. `renewals`, (c) fehlendes Datum, (d) Abweichung 2 bis 5 Tage, (e) andere.

### Ergebnis nach dem Vergleichswert der Leser

- Diskordante Lose 15; davon „nicht tagesgenau“ (aus der Zählung genommen): –; gezählt 15. Leser A = B beim Ende der Grundlaufzeit: 15/15 = 100,0 % (Wilson 79,6–100,0); übrige Lose durch Evaluator entschieden. Lose mit „kein Zuschlag“ bei einem Leser: –.

| | beide richtig | nur Liste richtig | nur Vergabeweiser richtig | beide falsch | Differenz (Liste − VW) | McNemar exakt p |
|---|---|---|---|---|---|---|
| W8a (Vergabeweiser wie gelesen) | 0 | 15 | 0 | 0 | +15 | 0,0001 |
| W8b (Klasse (a) zählt für Vergabeweiser als richtig) | 5 | 10 | 0 | 0 | +10 | 0,0020 |

- Treffer je Quelle gegen den Vergleichswert (diskordante Lose, n = 15): Liste 15, Vergabeweiser 0, Vergabeweiser nach W8b 5.
- **W8a:** Differenz +15 (Schwelle ≥ 16 = 10 % der Stichprobe), p = 0,0001 → **verfehlt**.
- **W8b:** Differenz +10 (Schwelle ≥ 8 = 5 % der Stichprobe), p = 0,0020 → **erfüllt**.
- Ursachen der Fehltreffer von Vergabeweiser (diskordante, gezählte Lose): {'e': 4, 'a': 5, 'b': 6}; der Liste: {}.
- Nur Liste richtig: M3, M7, M22, M33, M34, M37, M42, M49, M52, M54, M63, M67, M116, M132, M159; nur Vergabeweiser richtig: –.

## Deutung (Interpretation, nicht Messung)

- Nach den vorab festgelegten Folgen: W8a verfehlt: kein belegter Vorteil, die Aussage „kein Vorteil gegenüber Vergabeweiser“ gilt weiter (mit Einschränkung der Stichprobengröße).
- Die Differenz stützt sich nur auf diskordante Lose und setzt voraus, dass bei übereinstimmenden Losen beide Quellen gleich liegen (vorab benannte Grenze). Leser und Regeln stammen aus derselben Modellfamilie; die Wahl der Losebene in W8a ist nicht neutral, deshalb W8b.
- Lose ohne Eintrag bei Vergabeweiser (W10) gehen in W8 nicht ein; würde man sie als Fehltreffer von Vergabeweiser werten, wäre das ein anderes Maß (Abdeckung statt Genauigkeit).

## Verfahren (W11, Hinweis)

- Seed, Skript und Kriterien lagen vor dem Ziehen im Commit; Rohantworten von Vergabeweiser und TED-XML werden unverändert gespeichert. Abweichungen von der Vorab-Festlegung: keine; Festlegungen, die dort offen waren (Behandlung von Losen ohne Eintrag, Reihenfolge der Ursachenklassen, Schwelle „später als +5 Tage“ bei `renewals`), stehen im Kopf dieses Skripts.
