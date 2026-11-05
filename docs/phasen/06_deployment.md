# Phase 6: Deployment

> _Seit 2026-10-29: im Projekt nur als Prototyp der Vertragsliste, ohne Kunden (Iteration 7)._
> **Ziel:** Ergebnisse so bereitstellen, dass echte Kunden sie nutzen und Feedback geben (Stufen: manuelle Liste →
> monatliche E-Mail → Dashboard).
> **Danach:** Feedback fließt in die nächste Iteration von Phase 1.
> Details: [CRISP-DM.md](../CRISP-DM.md#6-deployment)
>
> **Artefakte laut CRISP-DM.md:** Skripte in `src/report/` (`beispiel_liste.py`), `reports/beispiel_liste.md` (vorhanden seit Iteration 6, wird nach Phase 3 neu erzeugt)

---

## Aktueller Stand

_Stand: Iteration 9 (Abschluss), 2026-11-05. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Prototyp der Vertragsliste (Oberpfalz) wird mit der Fassung der Iteration 9 neu erzeugt** (`src/report/beispiel_liste.py`). Genauigkeitshinweis: Ende der Grundlaufzeit 94,3 % Übereinstimmung mit dem Vergleichswert zweier KI-Leser (Stichprobe aus ganz Deutschland, 14/15 durch einen Menschen bestätigt), Höchstende nur Hinweis. Keine Kunden, keine Terminprognose.

Quellen: **[BL]** [beispiel_liste.md](../../reports/beispiel_liste.md) · **[E6]** [evaluation_iteration6.md](../../reports/evaluation_iteration6.md) · **[LA6]** [liste_auswertung_iteration6.md](../../reports/liste_auswertung_iteration6.md).
Iteration 7: **[LA7]** [liste_auswertung_iteration7.md](../../reports/liste_auswertung_iteration7.md) · **[E7]** [evaluation_iteration7.md](../../reports/evaluation_iteration7.md) · **[AC7]** [abschreibecheck_iteration7.md](../../reports/abschreibecheck_iteration7.md) · **[BL]** [beispiel_liste.md](../../reports/beispiel_liste.md).
Iteration 8: **[ZA8]** [zweitlesung_iteration8_auswertung.md](../../reports/zweitlesung_iteration8_auswertung.md) · **[E8]** [evaluation_iteration8.md](../../reports/evaluation_iteration8.md).
Iteration 9: **[ZA9]** [zweitlesung_iteration9_auswertung.md](../../reports/zweitlesung_iteration9_auswertung.md) · **[E9]** [evaluation_iteration9.md](../../reports/evaluation_iteration9.md) · **[VL9]** [vertragsliste_iteration9.md](../../reports/vertragsliste_iteration9.md).

### Fakten (aus den Daten)

- **Iteration 9:** Liste ohne Lose ohne Zuschlag (9.325 Lose bundesweit); der Prototyp wird neu erzeugt und im Bericht auf die Zahlen der Iteration 9 umgestellt [ZA9], [VL9].
- Prototyp neu erzeugt (2026-11-05): Oberpfalz 130 Lose (vorher 146), Stufen A 54, B 2, C 27, D 9, E 5, F 33, Region je Los überall eindeutig (9 Bekanntmachungen über das XML), 87 Lose laufen [BL]. Korrektur im Skript: Die Region-Zuordnung rechnete mit der Zahl der Lose der Liste; seit Regel 7 fehlen Lose ohne Zuschlag, daher zählt jetzt die Zahl aller Lose (API-Feld oder XML).
- Idee des Nutzers (nach Iteration 9, noch nicht umgesetzt): statische Seite mit Filtern (Region, Zeitraum des Vertragsendes) auf Oberpfalz-Daten; Bewerbungsfristen stammen aus Auftragsbekanntmachungen, nicht aus den Zuschlagsdaten.
- _Frühere Iterationen (weiter gültig):_
- 146 Lose, Stufen A 64, B 2, C 33, D 9, E 5, F 33 (unverändert) [BL].
- Kontroll-Lose 143100-2026 Lose 8, 9, 14: Ende der Grundlaufzeit 31.03.2030, Höchstende 31.03.2031; beide KI-Leser lasen dasselbe [ZA8].
- Bekannte Fehlerarten der Liste: Lose ohne Zuschlag, Regel 6 (Einzelwert auf andere Lose), „3 Jahre mit Option“, „um 3 Jahre“, Datumsformat mit Monatsnamen [E8].

### Interpretation

- Die Seite wäre nur eine andere Darstellung derselben Liste; ein Filter auf einen „prognostizierten Ausschreibungszeitraum“ wäre nicht belegt (Iteration 5), gefiltert werden darf nur nach Vertragsende und Höchstende.
- Der Prototyp zeigt die Form eines möglichen Produkts; seine Genauigkeit ist nur durch KI-Lesung gestützt. Ob eine Liste ohne Terminprognose für Mittelständler nützlich ist, ist nicht geprüft (A1, A15 außerhalb des Projektumfangs).

## Offene Fragen

- [ ] _(neu, Iteration 7)_ Stimmen die Stufe-A-Einträge aus Regel 1b (z. B. 143100-2026 Lose 9, 14)? Ungeprüft.
- [ ] Welche Felder braucht ein Kunde in der Liste mindestens? _(Stand Iteration 6: Prototyp zeigt Auftraggeber, Los, Ende der Grundlaufzeit, Höchstende, Status, Herkunft, Stufe, TED-Link; ohne Kundentest nicht beantwortbar.)_
- [ ] _(neu, Iteration 6)_ Wie werden Lose, die nur teilweise in der Region liegen (Leistungsorte auch außerhalb), und sachfremde Lose (Haupt-CPV 909, aber keine Gebäudereinigung) in der Liste behandelt?

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| – | – | Noch keine Entscheidungen | – |
| 2026-11-04 | 6 | Prototyp der Vertragsliste als Markdown und CSV je Region, mit Stufe A–F je Eintrag und ohne Terminprognose; Neuerzeugung nach Phase 3 | Entscheidung „Idee anpassen“ nach Iteration 5; Abschluss Iteration 6 (reports/evaluation_iteration6.md) |
| 2026-11-04 | 7 | Prototyp mit Regel 1b neu erzeugt; Spalten „Ende Grundlaufzeit (laut Bekanntmachung)“ und „Höchstende (nur Hinweis)“; Aussage „Stufe A ist die sicherste“ zurückgenommen | Abschluss Iteration 7, Evaluator (reports/evaluation_iteration7.md). Entscheidung des Nutzers. |
| 2026-11-05 | 8 | Prototyp bleibt unverändert; im Bericht stehen die KI-Zweitlesung und ihre Grenzen | Abschluss Iteration 8 (reports/evaluation_iteration8.md). Entscheidung des Nutzers. |
| 2026-11-05 | 9 | Weiter (Projektabschluss), eingeschränkt formuliert: Die Fassung der Iteration 9 (Regeln 1 bis 10) wird der Prototyp; das Höchstende bleibt Hinweis; V4, V7 und V8 werden offen als verfehlt bzw. teilweise berichtet; keine weitere Iteration | V1 66/70, V2 28/30, V3 66 gegen 65 (erfüllt), V5 110/110, V6 14/15; V4 verfehlt, V7 verfehlt (Ursache in der Anweisung, nicht im Filter), V8 teilweise ([ZA9], [E9]). Entscheidung des Nutzers nach dem Vorschlag und der Gesamtprüfung des Evaluators. |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

_Noch keine Einträge._

### Iteration 6 – 2026-11-04

- **Was gemacht:** Prototyp der Vertragsliste für die Oberpfalz (NUTS DE23) gebaut (`src/report/beispiel_liste.py`): Region je Los über API-Feld oder eForms-XML, Status zum Stichtag, Unsicherheitsstufe A–F, Quellen-Links.
- **Erkenntnisse – Fakten:** 146 Lose, 108 mit Ende der Grundlaufzeit aus den Feldern; bekannte Fehler bei 143100-2026 und sachfremde Lose (reports/beispiel_liste.md, reports/evaluation_iteration6.md).
- **Erkenntnisse – Interpretation:** Y4 formal erfüllt; der Prototyp ist wegen der Fehler der Lese-Regel und der kleinen Stichprobe je Stufe nur vorläufig.
- **Übergabe an die nächste Phase:** Nach Phase 3 (Regel erweitern) die Liste neu erzeugen und mit einer neuen Stichprobe prüfen (Phase 5).

### Iteration 7 – 2026-11-04

- **Was gemacht:** Prototyp der Oberpfalz-Liste mit Regel 1b und vorab definierten Stufen neu erzeugt (Commit a93785e); beim Abschluss Kennzeichnung „laut Bekanntmachung“/„nur Hinweis“ ergänzt und die Aussage zu Stufe A korrigiert.
- **Erkenntnisse – Fakten:** 146 Lose, Fehler 143100-2026 (Lose 8, 9, 14) behoben, Los 8 an TED bestätigt (reports/beispiel_liste.md, reports/evaluation_iteration7.md).
- **Erkenntnisse – Interpretation:** Y4 teilweise erfüllt; die Genauigkeitsangaben je Stufe beruhen auf kleinen Zahlen und belegen Stufe A nicht.
- **Übergabe an die nächste Phase:** Liste bleibt eingefroren; eine KI-Zweitlesung (Iteration 8) kann die Genauigkeitsangabe ergänzen, ändert den Prototyp aber nicht.

### Iteration 8 – 2026-11-05

- **Was gemacht:** Nur der Genauigkeitshinweis im Prototyp ergänzt; Liste und Regeln unverändert.
- **Erkenntnisse – Fakten:** Kontroll-Lose 8, 9, 14 von beiden Lesern wie in der Liste gelesen; neue Fehlerarten bekannt (reports/evaluation_iteration8.md).
- **Erkenntnisse – Interpretation:** Y4 bleibt teilweise; Aussagen zur Genauigkeit nur mit Vorbehalt.
- **Übergabe an die nächste Phase:** Projektabschluss.

### Iteration 9 – 2026-11-05

- **Was gemacht:** Prototyp mit der Fassung der Iteration 9 neu erzeugt bzw. zur Neuerzeugung vorgesehen; Genauigkeitshinweis auf Iteration 9 umgestellt.
- **Erkenntnisse – Fakten:** Liste um 590 Lose ohne Zuschlag kleiner; Ende der Grundlaufzeit 94,3 % (reports/zweitlesung_iteration9_auswertung.md).
- **Erkenntnisse – Interpretation:** Der Prototyp zeigt die Form eines möglichen Produkts; seine Genauigkeit ist KI-gelesen und nur an 15 Losen von einem Menschen bestätigt.
- **Übergabe an die nächste Phase:** Projektabschluss (Lab-Log, Vortrag); Webseite und Dashboard sind Ideen des Nutzers außerhalb der Bewertung.
