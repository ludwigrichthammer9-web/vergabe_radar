# Bewertung des Projekts (Leistungsnachweis, Big Data Analytics, OTH Amberg-Weiden)

_Kurzfassung der Bewertungsbögen LN A/B/C (Stand 2026-11-03, Quelle: PDFs des Nutzers, Originale nicht im Repo). Gilt als Maßstab für
Projektablauf und Dokumentation. Es gilt **LN B** (Zweierteam, mit dem Dozenten besprochen; Stand 2026-11-09)._

## Welcher Bogen
- **LN A** Lehrvortrag über einen Algorithmus: für dieses Projekt nicht relevant.
- **LN B (gilt für dieses Projekt)** Datenanalyseprojekt, Zweierteam: 15 min Vortrag (≤ 12 Folien) + 5 min Fragen.
- **LN C** (gilt nicht; nur zum Vergleich) Datenanalyseprojekt, Einzelarbeit: **10 min Vortrag (≤ 8 Folien) + 5 min Fragen**, Datensatz Richtwert 200–10.000 Zeilen,
  ≤ 15 Merkmale (unser Datensatz ist größer: begründen), Lab-Log 4–8 Seiten-Äquivalent **mit Zeitprotokoll je Arbeitsschritt**.

## Gemeinsam (B und C)
- CRISP-DM iterativ, **≥ 2 vollständige Zyklen** (bei C darf der 2. sich auf eine Phase konzentrieren, Rücksprünge dokumentieren).
- Abgabe: **Lab-Log** (PDF/Web-App), **Code/Workflow**, **Daten(link)**, **Folien**. Vorab beim Dozenten angemeldet.
- KI frei nutzbar, kein Nachweis nötig. Bewertet wird, was im Raum geschieht. Fehlerfrei, aber reproduziert = 2,0; 1,0 braucht
  sichtbares eigenes Verständnis.
- Note: gewichteter Mittelwert der Stufen 1–5, gerundet auf Drittelnoten; K.-o. deckelt auf 4,0.

## Gewichte und Anforderungen (1,0 = Kernpunkt)
| Nr | Teil | % | Was für 1,0 / 2,0 zählt |
|---|---|---|---|
| 1 | Business Understanding | 8 | Frage mit Entscheidungsbezug; Erfolgskriterium **fachlich (Nutzen, Schwelle) und analytisch**; Risiken; im Verlauf geschärft |
| 2 | Data Understanding/Preparation | 12 | Qualität systematisch geprüft, jeder Schritt begründet, **Leakage bedacht**, eigene Merkmale mit fachlicher Begründung |
| 3 | Modeling/Evaluation | 12 | Wahl begründet, **Baseline**, saubere Trennung Training/Test, passende Maße, Ergebnis gegen Erfolgskriterium und Alternativen kritisch geprüft |
| 4 | Iteratives Vorgehen | 8 | ≥ 2 Zyklen, Erkenntnis steuert den nächsten, verworfene Wege und Rücksprünge dokumentiert |
| 5 | Lab-Log | 15 | chronologisch, alle Phasen je Zyklus, Entscheidungen begründet, reproduzierbar, **Zeitaufwand je Schritt (C)**, **KI-Irrwege und deren Prüfung** |
| 6 | Aussagekraft | 12 | eine Kernbotschaft, Antwort auf die Geschäftsfrage, Empfehlung **mit Grenzen und Unsicherheit**, Zahlen richtig eingeordnet, Irrwege ehrlich |
| 7 | Dramaturgie | 13 | Erzählbogen Frage → Irrwege → Erkenntnis, Visualisierung trägt, Publikum aktiviert, frei vortragen, Zeit ± 30 s |
| 8–10 | Fragenrunde (3 Fragen: Methode, Live-Nachweis, Entscheidung/Transfer) | 7/7/6 | Methodenfrage (warum Verfahren/Maß/Aufbereitung, Alternative); **Live-Nachweis im Werkzeug** (Trennung Training/Test, Fehlwerte zeigen, Parameter ändern, Wirkung erklären); Entscheidungs-/Transferfrage (Empfehlung, neuer Standort, doppeltes Volumen) |

## K.-o. (Deckel 4,0)
- CRISP-DM-Phasen nicht erkennbar oder nur ein Durchlauf.
- Vortragsdauer: B unter 10/über 20 min, **C unter 7/über 14 min**.
- Personenbezogene Daten ohne Freigabe oder **Datensatz ohne Quellenangabe**.
- Code/Workflow nicht abgegeben (nicht reproduzierbar). Kein Lab-Log.

## Folgen für das Vergabe-Radar (Abgleich, 2026-11-03)
- `docs/iterationen.md` + Phasendokumente entsprechen im Kern dem Lab-Log (chronologisch, Entscheidungen, verworfene Wege). Daraus
  das Lab-Log ableiten, nicht neu erfinden.
- **Zeitprotokoll je Arbeitsschritt (C):** Dashboard „Zeit (Git-Sitzungen)“ reicht grob; Schritte der Iterationen mit Zeit notieren.
- **KI-Irrwege dokumentieren** (Abschnitt im Lab-Log): z. B. K2 und Regel-Urteile aus derselben Hand, kalibrierte Paare in der
  Zweitprüfung nicht ausgeschlossen, Lese-Regeln nur an eForms getestet. Laufend in `docs/ki_irrwege.md` sammeln.
- **Fachliches Erfolgskriterium** (Nutzen, Schwelle) fehlt noch; ohne Kundenkontakt als begründete Setzung formulieren (Phase 1).
- **Reproduzierbarkeit:** `data/raw` ist nicht im Git; vor Abgabe Datenlink oder Download-Skript mit Parametern bereitstellen.
- **Quellenangaben** für TED-Daten und eForms-SDK in einer Quellenliste führen.
- **Leakage und Trennung Training/Test:** Entwicklungs-/Testdaten (Iteration 3/4) und eingefrorene Regeln vor Test sind der
  Live-Nachweis; im Vortrag/Lab-Log ausdrücklich zeigen. Baseline = R0.
- **Datensatzgröße (C):** 200–10.000 Zeilen, ≤ 15 Merkmale ist ein Richtwert; Auswahl der Merkmale und Teilmenge begründen.
- **Vortrag:** Erzählbogen Frage → Irrwege (Auftraggeber-Zuordnung verworfen, Objekt-Zuordnung verworfen) → Erkenntnis
  (Vertragsliste, Höchstende aus Freitext) mit Empfehlung und Grenzen.
- LN B (Zweierteam) ist mit dem Dozenten besprochen (Angabe des Nutzers, 2026-11-06). Offen: Abgabefrist (Moodle, nicht bekannt).
