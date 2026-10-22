---
name: iteration-start
description: Startet eine neue CRISP-DM-Iteration im Vergabe-Radar. Liest Phasendokumente, Iterationen und Annahmen, fasst den Stand zusammen und schlägt Hypothese, Erfolgskriterium und Plan für die nächste Iteration vor, ohne etwas umzusetzen.
disable-model-invocation: true
argument-hint: "[optionaler Fokus, z. B. Gebäudereinigung]"
allowed-tools: Read Grep Glob
---

# Iteration starten

Optionaler Fokus des Nutzers: $ARGUMENTS

## Git-Kontext

Status:
!`git status --short || true`

Vorhandene Iterations-Tags:
!`git tag --list "iteration-*" || true`

Letzte Commits:
!`git log --oneline -10 || true`

## Vorgehen

**Setze in diesem Schritt nichts um.** Kein Code, keine Downloads, keine Änderungen an Dateien, bis der Nutzer
den Vorschlag bestätigt hat (siehe Schritt 4).

1. **Lesen:** `docs/CRISP-DM.md`, alle Dateien in `docs/phasen/` (01 bis 06), `docs/iterationen.md` und
   `docs/annahmen.md`. Wenn dort Reports oder Skripte zitiert werden, die für den Vorschlag wichtig sind, diese ebenfalls lesen.

2. **Stand zusammenfassen** (kurz, auf Deutsch, Fakten und Interpretation getrennt):
   - Letzte Iteration: Hypothese, Ergebnis, Entscheidung. Falls noch eine Iteration läuft, darauf hinweisen und
     fragen, ob sie zuerst mit `/iteration-ende` abgeschlossen werden soll.
   - Stand je Phase in einem Satz.
   - Die wichtigsten offenen Fragen.
   - Die riskantesten **ungeprüften** Annahmen aus `annahmen.md` (Risiko hoch zuerst).

3. **Nächste Iteration vorschlagen:**
   - **Fokus und Phasen.** Am Iterationsplan in CRISP-DM.md orientieren und begründen, falls davon abgewichen wird.
     Rücksprünge in frühere Phasen sind normal.
   - **Hypothese:** eine Aussage, die durch das Ergebnis widerlegt werden kann.
   - **Erfolgskriterium:** messbar mit konkreter Schwelle, **jetzt** festgelegt, bevor Ergebnisse vorliegen.
     Dazu sagen, welches Ergebnis zu „weiter“, „zurück zu Phase X“ oder „Idee anpassen“ führen würde.
   - **Zeitrahmen:** realistisch für einen Studenten neben dem Studium.
   - **Plan:** 3 bis 7 konkrete Schritte mit Artefakten (Dateien, Reports) und den betroffenen Phasen.
   - **Geprüfte Annahmen:** welche IDs aus `annahmen.md` diese Iteration prüft.
   - Einfache Lösungen zuerst (Arbeitsregel aus CRISP-DM.md).
   - Den optionalen Fokus des Nutzers berücksichtigen, falls angegeben.

4. **Abschluss:** Fragen, ob die Iteration so in `docs/iterationen.md` angelegt werden soll. Erst nach Bestätigung
   genau diesen Eintrag schreiben: neue Zeile in der Übersicht und neuer Abschnitt mit Hypothese, Erfolgskriterium,
   Zeitrahmen, Ergebnis „offen“ und Entscheidung „offen“. Bestehende Einträge nicht verändern.
