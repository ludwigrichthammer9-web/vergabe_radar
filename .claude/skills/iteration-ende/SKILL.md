---
name: iteration-ende
description: Schließt die laufende CRISP-DM-Iteration im Vergabe-Radar ab. Lässt das Ergebnis vom evaluator prüfen, aktualisiert Phasendokumente, Logs, Annahmen und iterationen.md und schlägt Commit-Nachricht und Git-Tag vor.
disable-model-invocation: true
argument-hint: "[Iterationsnummer, optional]"
---

# Iteration abschließen

Iteration laut Nutzer (leer = die laufende aus `docs/iterationen.md`): $ARGUMENTS

## Git-Kontext

Status:
!`git status --short || true`

Vorhandene Iterations-Tags:
!`git tag --list "iteration-*" || true`

Commits seit dem letzten Iterations-Tag (ohne Tag: die letzten 15):
!`t=$(git describe --tags --match "iteration-*" --abbrev=0 2>/dev/null); if [ -n "$t" ]; then git log --oneline "$t"..HEAD; else git log --oneline -15; fi || true`

## Vorgehen

1. **Einlesen:** Iteration in `docs/iterationen.md` finden und ihre Hypothese und ihr Erfolgskriterium wörtlich notieren.
   Dazu alle Dateien in `docs/phasen/`, `docs/annahmen.md` und die in dieser Iteration entstandenen Reports und Skripte
   lesen (siehe Git-Kontext). Wenn das Erfolgskriterium keine konkrete Schwelle hat, zuerst den Nutzer bitten, sie
   festzulegen, und das als nachträglich markieren.

2. **Kritisch prüfen lassen:** Den Subagenten `evaluator` beauftragen. Mitgeben: Iterationsnummer, Hypothese und
   Erfolgskriterium wörtlich, Liste der relevanten Dateien. Sein Urteil nicht abschwächen, sondern vollständig berichten.

3. **Entscheidung vorschlagen:** weiter / zurück zu Phase X / Idee anpassen, mit Begründung.
   - Dabei Ergebnis und Evaluator-Befund dem Erfolgskriterium gegenüberstellen.
   - **Die Entscheidung trifft der Nutzer.** Vorschlag zeigen und auf Bestätigung oder Änderung warten.
   - Vor der Bestätigung keine Datei ändern.

4. **Nach Bestätigung die Dokumente aktualisieren:**
   - **Phasendokumente** (`docs/phasen/`, nur die betroffenen Phasen):
     - „Aktueller Stand“ neu schreiben, mit neuer Stand-Zeile (Iteration, Datum).
     - Fakten (mit Quelle) und Interpretation trennen.
     - „Offene Fragen“ abhaken oder ergänzen.
     - „Entscheidungen“: neue Zeilen **anhängen**.
     - „Iterationslog“: einen neuen Eintrag **unten anhängen** mit Iteration, Datum, Was gemacht,
       Erkenntnisse – Fakten, Erkenntnisse – Interpretation und Übergabe an die nächste Phase.
     - Bestehende Log-Einträge und Entscheidungszeilen **niemals ändern oder löschen**.
       Korrekturen kommen als neuer Eintrag dazu.
   - **`docs/annahmen.md`:** Status und Nachweis nur mit Beleg ändern, Geltungsbereich nennen, Änderung unter „Verlauf“ anhängen.
     Neue Annahmen, die in der Iteration sichtbar wurden, ergänzen.
   - **`docs/iterationen.md`:** Ergebnis (Fakten/Interpretation) und Entscheidung im Abschnitt der Iteration eintragen,
     Status auf „abgeschlossen“ setzen, Übersichtstabelle aktualisieren. Abschnitte anderer Iterationen nicht ändern.
   - Falls sich die aktuelle Phase ändert, die Angabe in `CLAUDE.md` kurz anpassen.

5. **Commit und Tag vorschlagen, nicht ausführen:**
   - Commit-Nachricht auf Deutsch: Betreff (≤ 60 Zeichen), Leerzeile, 2 bis 4 Stichpunkte zu Ergebnis und Entscheidung.
   - Annotiertes Tag `iteration-N`, z. B.
     `git tag -a iteration-1 -m "Iteration 1: Machbarkeit der Daten – Entscheidung: weiter"`
   - Die Befehle als Codeblock ausgeben. Der Nutzer führt sie selbst aus oder bittet ausdrücklich darum.
