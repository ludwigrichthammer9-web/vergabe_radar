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

_Stand: Iteration 6 (Abschluss), 2026-11-04. Dieser Abschnitt wird in jeder Iteration neu geschrieben._

**Prototyp der Vertragsliste vorhanden** (Region Oberpfalz, Stichtag 04.11.2026), ohne Kunden und ohne Terminprognose. Er enthält bekannte Fehler und wird nach der Rückkehr in Phase 3 neu erzeugt.

Quellen: **[BL]** [beispiel_liste.md](../../reports/beispiel_liste.md) · **[E6]** [evaluation_iteration6.md](../../reports/evaluation_iteration6.md) · **[LA6]** [liste_auswertung_iteration6.md](../../reports/liste_auswertung_iteration6.md).

### Fakten (aus den Daten)

- Für eine Kundenliste wären Auftraggeber (100 %) und CPV (100 %) immer vorhanden. Ein plausibler Auftragswert fehlt bei
  rund 41 % der Notices. [Report §2]
- **Iteration 6:** `src/report/beispiel_liste.py` erzeugt aus der Vertragsliste und dem Abruf mit Leistungsort DE23* eine Liste mit 146 Losen aus 67 Zuschlägen: TED-Link, Auftraggeber, Los, Ende der Grundlaufzeit, Höchstende, Status zum Stichtag, Herkunft, Unsicherheitsstufe A–F, Hinweise [BL]. Das Ende der Grundlaufzeit kommt bei 108 Losen (74,0 %) aus den Feldern, bei 5 ist es geschätzt, bei 33 fehlt es.
- Die Region je Los ließ sich bei 9 Bekanntmachungen nur über das eForms-XML bestimmen (die Such-API liefert die Orte als flache Liste); die Zuordnung XML-Los zu Listen-Los läuft über den Titel, sonst über die Reihenfolge (ungeprüft) [BL], [E6].
- Bekannte Fehler im Prototyp: Bei 143100-2026 (Lose 8, 9, 14) ist das Enddatum laut Evaluator ein Jahr zu spät (Stufe B); sachfremde Lose wie 556275-2026 (Kesselreinigung) stehen drin [E6].

### Interpretation

- Eine Liste nach Auftragswert zu sortieren, wäre lückenhaft. Gegebenenfalls nach Laufzeitende sortieren und den Wert
  nur ergänzend zeigen.
- Die Unsicherheitsstufen sind nach Kenntnis der Prüfergebnisse eingeteilt und stützen sich auf kleine Zahlen je Stufe aus der bundesweiten Stichprobe; sie helfen beim Lesen, ersetzen aber keine Prüfung der Oberpfalz-Einträge (nur 1 Los aus der Stichprobe liegt dort) [BL], [E6].
- Ob eine Liste ohne Terminprognose für Mittelständler nützlich ist, ist nicht geprüft (A1, A15 außerhalb des Projektumfangs).

## Offene Fragen

- [ ] Welche Felder braucht ein Kunde in der Liste mindestens? _(Stand Iteration 6: Prototyp zeigt Auftraggeber, Los, Ende der Grundlaufzeit, Höchstende, Status, Herkunft, Stufe, TED-Link; ohne Kundentest nicht beantwortbar.)_
- [ ] _(neu, Iteration 6)_ Wie werden Lose, die nur teilweise in der Region liegen (Leistungsorte auch außerhalb), und sachfremde Lose (Haupt-CPV 909, aber keine Gebäudereinigung) in der Liste behandelt?

## Entscheidungen

_Nur ergänzen. Überholte Entscheidungen bleiben stehen und werden durch eine neue Zeile ersetzt._

| Datum | Iteration | Entscheidung | Begründung |
|---|---|---|---|
| – | – | Noch keine Entscheidungen | – |
| 2026-11-04 | 6 | Prototyp der Vertragsliste als Markdown und CSV je Region, mit Stufe A–F je Eintrag und ohne Terminprognose; Neuerzeugung nach Phase 3 | Entscheidung „Idee anpassen“ nach Iteration 5; Abschluss Iteration 6 (reports/evaluation_iteration6.md) |

## Iterationslog

<!-- Nur ergänzen, nie überschreiben. Neueste Einträge unten. -->

_Noch keine Einträge._

### Iteration 6 – 2026-11-04

- **Was gemacht:** Prototyp der Vertragsliste für die Oberpfalz (NUTS DE23) gebaut (`src/report/beispiel_liste.py`): Region je Los über API-Feld oder eForms-XML, Status zum Stichtag, Unsicherheitsstufe A–F, Quellen-Links.
- **Erkenntnisse – Fakten:** 146 Lose, 108 mit Ende der Grundlaufzeit aus den Feldern; bekannte Fehler bei 143100-2026 und sachfremde Lose (reports/beispiel_liste.md, reports/evaluation_iteration6.md).
- **Erkenntnisse – Interpretation:** Y4 formal erfüllt; der Prototyp ist wegen der Fehler der Lese-Regel und der kleinen Stichprobe je Stufe nur vorläufig.
- **Übergabe an die nächste Phase:** Nach Phase 3 (Regel erweitern) die Liste neu erzeugen und mit einer neuen Stichprobe prüfen (Phase 5).

