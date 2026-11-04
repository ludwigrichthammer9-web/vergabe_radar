# Vertragsliste aus Zuschlägen (Iteration 5, Schritt 3)

_Erzeugt mit `src/prepare/vertragsliste.py`; Regeln im Kopf des Skripts und in `docs/business.md` §7.1._

## Fakten

- Datenbasis: eForms-Zuschläge `DEU_result_cpv909_20231025_20260930_lostext`; Population wie Iteration 4 (`population_iteration4.exclusion_reason`), 1006 Notices ausgeschlossen.
- Tabelle: 9915 Lose aus 4209 Zuschlägen (`data/processed/vertragsliste_909.csv`, nicht im Git).
- Lose mit nicht eindeutig zuordenbarer Feldliste: 28.

### X4 Abdeckung (Lose aus Zuschlägen, veröffentlicht 2025-10-01 bis 2026-09-30)

**R1 liefert ein Datum: 2924/3668 = 79,7 % (Wilson 78,4–81,0)** (Schwelle ≥ 80 %, vorab festgelegt).

Zusätzlich (Iteration 6, nur Hinweis, zählt nicht für X4/Y3): mit **geschätztem** Ende (Veröffentlichung + Dauer, wenn nur die Dauer vorliegt) 3207/3668 = 87,4 % (Wilson 86,3–88,5).

| Herkunft Ende der Grundlaufzeit | Lose |
|---|---|
| enddatum | 2794/3668 = 76,2 % |
| unbekannt | 735/3668 = 20,0 % |
| text_zunaechst | 77/3668 = 2,1 % |
| beginn_plus_dauer | 53/3668 = 1,4 % |
| unplausibel | 9/3668 = 0,2 % |

### Herkunft des Höchstendes (alle Lose mit Ende der Grundlaufzeit)

| Herkunft | Lose |
|---|---|
| keine_angabe | 2354/7284 = 32,3 % |
| anzahl_x_laenge | 1600/7284 = 22,0 % |
| datum_text | 1291/7284 = 17,7 % |
| unbestimmbar | 966/7284 = 13,3 % |
| hoechstlaufzeit_text | 638/7284 = 8,8 % |
| enddatum_ist_hoechstende | 325/7284 = 4,5 % |
| keine_verlaengerung | 104/7284 = 1,4 % |
| bt36_laenger | 6/7284 = 0,1 % |

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
