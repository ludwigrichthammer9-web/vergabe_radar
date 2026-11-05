# Vergleich Liste gegen Vergabeweiser, größere Stichprobe (Iteration 10b)

_Erzeugt mit `src/prepare/vergleich_iteration10b.py`. Kriterien vorab in `docs/iterationen.md` (Iteration 10b), Skript im Kopf mit den Definitionen. Schlüssel-SHA-256 `2cd00206…6e33` (stimmt mit dem Commit überein). Daten von Vergabeweiser: CC BY 4.0, Quelle „Vergabeweiser“ (vergabeweiser.de), Abruf 2026-11-05 ff., Rohdaten unverändert in `data/raw/vergabeweiser_20261105/`. In diesem Bericht stehen keine Datumswerte je Los (Leser bleiben blind); sie stehen in `data/processed/vergleich_iteration10b_voll.csv` (lokal)._

## Fakten

- Stichprobe: 160 Lose aus 154 Bekanntmachungen.
- **W10 Abdeckung:** Vergabeweiser hat einen Eintrag für 160/160 Lose (160/160 = 100,0 % (Wilson 97,7–100,0)); Bekanntmachungen zugeordnet 154/154 (Weg 1/2/3: 10/125/19). Unvollständig (TED-XML fehlt oder Abfrage vorläufig): 0 Bekanntmachungen (0 Lose) – diese gelten bis zu einem erneuten Lauf als „kein Eintrag“.
- Von 160 Losen mit Eintrag: Liste und Vergabeweiser gleich (± 1 Tag) bei 145; **diskordant 15** (an die Leser: `reports/vergleich_iteration10b_diskordant.csv`).
- Art des Werts von Vergabeweiser bei Losen mit Eintrag: {'datum': 160}.
- **W9 Ursachenverteilung der 15 diskordanten Lose:** (a) 5 = 33,3 %, (b) 6 = 40,0 %, (c) 0 = 0,0 %, (d) 0 = 0,0 %, (e) 4 = 26,7 %. Klassen: (a) Losebene, (b) Höchstende bzw. `renewals`, (c) fehlendes Datum, (d) Abweichung 2 bis 5 Tage, (e) andere.

## Deutung (Interpretation, nicht Messung)

- Erst nach dem Vergleichswert der Leser (Modus `--ergebnis`) lässt sich sagen, welche Quelle bei den diskordanten Losen richtig liegt. Die Ursachenverteilung zeigt nur, wie die Abweichungen zustande kommen, nicht wer recht hat (Klasse (a) und (b) sind Verdachtsfälle für Verfahrens- statt Losebene bzw. Höchstende).

## Verfahren (W11, Hinweis)

- Seed, Skript und Kriterien lagen vor dem Ziehen im Commit; Rohantworten von Vergabeweiser und TED-XML werden unverändert gespeichert. Abweichungen von der Vorab-Festlegung: keine; Festlegungen, die dort offen waren (Behandlung von Losen ohne Eintrag, Reihenfolge der Ursachenklassen, Schwelle „später als +5 Tage“ bei `renewals`), stehen im Kopf dieses Skripts.
