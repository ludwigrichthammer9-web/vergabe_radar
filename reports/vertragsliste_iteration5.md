# Vertragsliste aus Zuschlägen (Iteration 5, Schritt 3)

_Erzeugt mit `src/prepare/vertragsliste.py`; Regeln im Kopf des Skripts und in `docs/business.md` §7.1._

## Fakten

- Datenbasis: eForms-Zuschläge `DEU_result_cpv909_20231025_20260930_lostext`; Population wie Iteration 4 (`population_iteration4.exclusion_reason`), 1006 Notices ausgeschlossen.
- Tabelle: 9915 Lose aus 4209 Zuschlägen (`data/processed/vertragsliste_909.csv`, nicht im Git).
- Lose mit nicht eindeutig zuordenbarer Feldliste: 28.

### X4 Abdeckung (Lose aus Zuschlägen, veröffentlicht 2025-10-01 bis 2026-09-30)

**R1 liefert ein Datum: 2924/3668 = 79,7 % (Wilson 78,4–81,0)** (Schwelle ≥ 80 %, vorab festgelegt).

| Herkunft Ende der Grundlaufzeit | Lose |
|---|---|
| enddatum | 2861/3668 = 78,0 % |
| unbekannt | 735/3668 = 20,0 % |
| beginn_plus_dauer | 53/3668 = 1,4 % |
| text_zunaechst | 10/3668 = 0,3 % |
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
