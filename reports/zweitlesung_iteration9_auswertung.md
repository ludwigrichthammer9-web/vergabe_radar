# Auswertung der KI-Lesung (Iteration 9, V1 bis V8)

_Erzeugt mit `src/prepare/auswertung_iteration9.py`. Schlüssel-SHA-256 `9dbf5c1a…8753`. Vergleichswert nach der neutralen Definition im Kopf des Skripts. Leser A = Opus, Leser B = Sonnet, je 5 Teile in eigenen Sitzungen ohne Projektkontext._

## Fakten

- **V5 (Leser A = B beim Ende der Grundlaufzeit, 110 Lose): 110/110 = 100,0 % (Wilson 96,6–100,0)** (Schwelle ≥ 90 %). Höchstende einig: 108/110.
- Kontrolle des Evaluators (Seed 20261110): N25, N43, N53, N67, N80, N92, N94, N101, N102, N103.
- **V1 (Liste = Vergleichswert, Z-Lose, ohne „nicht tagesgenau“): 66/70 = 94,3 % (Wilson 86,2–97,8)** (Schwelle ≥ 63/70 = 90 %).
- **V2 (R- und M-Lose): 28/30 = 93,3 % (Wilson 78,7–98,2)** (Schwelle ≥ 24/30 = 80 %).
- **V3 (neue Fassung nicht schlechter als die alte, Z-Lose):** neu 66/70, alt 65/70 → erfüllt.
- **V4 (Höchstende, Z-Lose): 61/70 = 87,1 % (Wilson 77,3–93,1)** (Schwelle ≥ 90 %); **nur behauptetes Höchstende: 52/61 = 85,2 % (Wilson 74,3–92,0)** (Schwelle ≥ 85 %); streng ohne „unbestimmbar = korrekt“: 52/70 = 74,3 % (Wilson 63,0–83,1).
- **V7 (V-Lose, für die ein Leser „kein Zuschlag“ meldet): 1 von 100** (Schwelle 0): N51.
- Lose mit „nicht tagesgenau“ (aus Zähler und Nenner genommen): –.
- **V6 (Kommilitone = Vergleichswert, 15 Lose): 14/15** (Schwelle ≥ 13/15). Abweichend: N48 (Mensch 31.12.2030, Vergleichswert 2027-12-31).
- Kontrolle durch den Evaluator (beschreibend): Ende der Grundlaufzeit stimmt mit dem Vergleichswert bei 10/10 Losen.

### Beschreibend (ohne Schwelle)

- Regel-6-Lose (S, 10): Der Vergleichswert ist bestimmbar bei 8; die Liste nennt bei allen kein Ende (Abdeckungsverlust: 8/10).
- Von mindestens einem Leser als „keine Gebäudereinigung“ eingestuft: N54, N62, N93.
- Zuordnung des Loses von mindestens einem Leser als unsicher gemeldet: –.
- Herkunft des Endes in der Liste (V-Lose): {'enddatum': 94, 'text_zunaechst': 2, 'text_laufzeit_option': 3, 'beginn_plus_dauer': 1}.

### Abweichungen der Liste vom Vergleichswert (V-Lose)

| N | Gruppe | Herkunft | Liste GL | Vergleichswert GL | Leser A | Leser B | Liste Höchstende | Vergleichswert Höchstende |
|---|---|---|---|---|---|---|---|---|
| N7 | Z | enddatum | 2028-07-31 ✗ | 2027-07-31 | 2027-07-31 | 2027-07-31 | 2028-07-31 | 2028-07-31 |
| N18 | Z | enddatum | 2029-07-31 | 2029-07-31 | 2029-07-31 | 2029-07-31 | 2030-07-31 ✗ | 2029-07-31 |
| N25 | Z | enddatum | 2031-04-30 | 2031-04-30 | 2031-04-30 | 2031-04-30 | 2033-04-30 ✗ | 2032-12-31 |
| N32 | Z | enddatum | 2029-12-31 ✗ | 2029-11-30 | 2029-11-30 | 2029-11-30 | 2029-12-31 ✗ | 2029-11-30 |
| N35 | Z | enddatum | 2027-09-30 | 2027-09-30 | 2027-09-30 | 2027-09-30 | 2027-09-30 ✗ | 2029-09-30 |
| N39 | Z | enddatum | 2028-02-28 ✗ | 2028-03-25 | 2028-03-25 | 2028-03-25 | 2030-02-28 ✗ | 2030-03-25 |
| N49 | Z | enddatum | 2029-07-31 | 2029-07-31 | 2029-07-31 | 2029-07-31 | 2030-07-31 ✗ | 2029-07-31 |
| N57 | Z | enddatum | 2029-12-31 | 2029-12-31 | 2029-12-31 | 2029-12-31 | 2031-12-31 ✗ | unbestimmbar |
| N67 | Z | enddatum | 2028-07-09 | 2028-07-09 | 2028-07-09 | 2028-07-09 | 2030-07-09 ✗ | 2030-06-23 |
| N97 | Z | enddatum | 2034-02-28 | 2034-02-28 | 2034-02-28 | 2034-02-28 | 2042-02-28 ✗ | unbestimmbar |
| N108 | Z | enddatum | 2030-06-30 ✗ | 2028-06-30 | 2028-06-30 | 2028-06-30 | 2030-06-30 | 2030-06-30 |
| N5 | M | enddatum | 2026-08-31 ✗ | 2027-05-31 | 2027-05-31 | 2027-05-31 | unbestimmbar | unbestimmbar |
| N28 | M | enddatum | 2029-12-31 | 2029-12-31 | 2029-12-31 | 2029-12-31 | 2031-12-31 ✗ | 2030-12-31 |
| N79 | M | enddatum | 2030-07-31 ✗ | 2028-07-31 | 2028-07-31 | 2028-07-31 | 2032-07-31 ✗ | 2030-07-31 |
