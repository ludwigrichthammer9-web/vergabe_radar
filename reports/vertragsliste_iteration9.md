# Vertragsliste aus Zuschlägen (Iteration 5, Schritt 3)

_Erzeugt mit `src/prepare/vertragsliste.py`; Regeln im Kopf des Skripts und in `docs/business.md` §7.1._

## Fakten

- Datenbasis: eForms-Zuschläge `DEU_result_cpv909_20231025_20260930_lostext`; Population wie Iteration 4 (`population_iteration4.exclusion_reason`), 1006 Notices ausgeschlossen.
- Tabelle: 9325 Lose aus 4011 Zuschlägen (`data/processed/vertragsliste_909.csv`, nicht im Git).
- Lose mit nicht eindeutig zuordenbarer Feldliste: 101.
- Regel 7 (Iteration 9): 590 Lose ohne Zuschlag aus der Liste genommen; Status unbekannt bei 79 Losen.

### X4 Abdeckung (Lose aus Zuschlägen, veröffentlicht 2025-10-01 bis 2026-09-30)

**R1 liefert ein Datum: 2783/3503 = 79,4 % (Wilson 78,1–80,8)** (Schwelle ≥ 80 %, vorab festgelegt).

Zusätzlich (Iteration 6, nur Hinweis, zählt nicht für X4/Y3): mit **geschätztem** Ende (Veröffentlichung + Dauer, wenn nur die Dauer vorliegt) 3044/3503 = 86,9 % (Wilson 85,7–88,0).

| Herkunft Ende der Grundlaufzeit | Lose |
|---|---|
| enddatum | 2565/3503 = 73,2 % |
| unbekannt | 711/3503 = 20,3 % |
| text_festlaufzeit | 90/3503 = 2,6 % |
| text_zunaechst | 77/3503 = 2,2 % |
| beginn_plus_dauer | 26/3503 = 0,7 % |
| text_laufzeit_option | 25/3503 = 0,7 % |
| unplausibel | 9/3503 = 0,3 % |

### Herkunft des Höchstendes (alle Lose mit Ende der Grundlaufzeit)

| Herkunft | Lose |
|---|---|
| keine_angabe | 2185/6803 = 32,1 % |
| datum_text | 1344/6803 = 19,8 % |
| anzahl_x_laenge | 1342/6803 = 19,7 % |
| unbestimmbar | 832/6803 = 12,2 % |
| hoechstlaufzeit_text | 606/6803 = 8,9 % |
| enddatum_ist_hoechstende | 378/6803 = 5,6 % |
| keine_verlaengerung | 101/6803 = 1,5 % |
| gesamt_verlaengerung_text | 11/6803 = 0,2 % |
| bt36_laenger | 4/6803 = 0,1 % |

### Genauigkeit der Lese-Regeln

- Entwicklungsstichprobe (40 Lose, vor Regel 1a): 30 richtig; Fehler führten zu Regel 1a und weiteren Mustern
  ([hoechstende_pruefung_iteration5_entwicklung.md](hoechstende_pruefung_iteration5_entwicklung.md)).
- Teststichprobe (60 Lose, nach dem Einfrieren gezogen, Fassung a0aa419): Höchstende 53/60 richtig, gewichtet etwa 91 %;
  Fehler fast nur bei „unbestimmbar“ ([hoechstende_pruefung_iteration5_test.md](hoechstende_pruefung_iteration5_test.md)).
  Urteile von Claude allein.

## Interpretation

- X4 liegt knapp unter der Schwelle von 80 %. Ursache ist fast nur, dass bei etwa 20 % der Lose gar keine Laufzeit angegeben ist;
  das Höchstende spielt für X4 keine Rolle (R1 fällt auf die Grundlaufzeit zurück). Laut Vorab-Regel kein Abbruch, die
  Abdeckung wird im Prototyp genannt.
- Wo eine Laufzeit vorliegt, ist das Höchstende meist lesbar. Bleibt es unbestimmbar, liegt R1 eher zu früh.
