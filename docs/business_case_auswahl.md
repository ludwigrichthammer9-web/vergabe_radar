# Auswahl eines tragfähigen Business Case (Nachtrag zu Paket D, 2026-11-06)

_Kriterien vorab festgelegt am 2026-11-06, bevor die Kandidaten bewertet werden. Anlass: Stand nach Iteration 10 ist, dass die Vertragsliste als eigenes Produkt nicht trägt (Vergabeweiser kostenlos, AusschreibungsRadar ab 0 €, aufträge.io mit Pipeline endender Verträge) und die Make-or-Buy-Perspektive „keine Abo-Kosten“ nicht trägt. Fünf Recherche-Agenten haben aus je einem Blickwinkel Kandidaten gesucht (Probleme der Betriebe; weiße Flecken im Wettbewerb; andere Kundengruppen; lokale Daten; Geschäftsmodell und Bewertbarkeit). Hier steht nur die Bewertungsvorschrift; Kandidaten und Ergebnis folgen darunter._

## Was ein „nutzbarer Business Case“ hier ist
Nach `docs/bewertung_LN.md` muss das Projekt kein Geld verdienen. Verlangt sind: Frage mit Entscheidungsbezug, fachliches Kriterium mit Nutzen und Schwelle, Risiken, im Verlauf geschärft, Empfehlung mit Grenzen. Ein nutzbarer Business Case ist deshalb eine **vorab festgelegte Entscheidungsvorlage**, die auch mit „Nein“ enden darf, **und** eine Kernthese, die einen billigen Test hat. „Tragfähig“ heißt hier: Es gibt eine Kundengruppe, ein belegtes Problem, einen belegbaren Unterschied zur Konkurrenz und eine Spur von Zahlungsbereitschaft; fehlt eines davon, wird es offen als fehlend ausgewiesen.

## Kriterien (je 0, 1 oder 2 Punkte; Belegstand zählt, nicht Plausibilität)
| | Kriterium | 0 | 1 | 2 |
|---|---|---|---|---|
| K1 | **Problem belegt** | nur Annahme | eine Quelle oder ein Gespräch (n = 1) | mehrere unabhängige Quellen oder mindestens zwei Gespräche |
| K2 | **Unterschied zur Konkurrenz belegt** | gleiche Funktion kostenlos vorhanden oder nicht geprüft | Funktion bei Konkurrenz nicht gefunden (kein Beleg für Nichtexistenz) | von uns gemessen oder in einem Anbietervergleich belegt |
| K3 | **Zahlungsspur** | keine | Preisanker aus Quelle oder Gespräch (Aussage, keine Zusage) | mehrere Anker oder ein konkreter Betrag aus einem Gespräch |
| K4 | **Daten tragen** | Felder fehlen (< 40 % vollständig) oder nicht ehrlich lieferbar | 40–80 % vollständig, mit Einschränkung | über 80 % vollständig oder Auswertung belastbar (Nenner, Intervall) |
| K5 | **Zeigbar in höchstens 3 Arbeitstagen** | mehr als 3 Tage oder Produktbau nötig | 2–3 Tage | höchstens 1–2 Tage |
| K6 | **Billiger Test mit Abbruchkriterium** | kein Test | Test ohne Schwelle | Test mit vorab festgelegter Schwelle |
| K7 | **Passung zum Bogen und zur ehrlichen Geschichte** (Business Understanding, Aussagekraft, Dramaturgie, keine Überziehung) | schwächt die Geschichte | neutral | stärkt (Erkenntnis steuert nächsten Schritt) |

Höchstens 14 Punkte. **Ausschluss:** K4 = 0 oder K7 = 0 schließt einen Kandidaten als Kern aus (er darf als Ausblick genannt werden). **Entscheidung:** Der Kandidat mit der höchsten Summe wird Kernthese; bei Gleichstand gilt K3, dann K2. Liegt die höchste Summe unter 8, lautet das Ergebnis „kein tragfähiger Case; Empfehlung X mit Test“. Die Bewertung nennt je Punktzahl den Beleg (Datei oder Quelle), Annahmen zählen nicht als Beleg.

## Grenzen (vorab)
Die Recherche der Agenten stützt sich teils auf Eigenangaben der Anbieter, Suchzusammenfassungen und Drittseiten; „nicht gefunden“ heißt nicht „existiert nicht“. Zahlungsbereitschaft ist in den drei Gesprächen (n = 3) nur als Aussage vorhanden. Die Bewertung ist eine Einschätzung und keine Messung.

## Ergebnis der Bewertung (Evaluator, 2026-11-06)
_Die Kriterien wurden festgelegt, nachdem die fünf Recherche-Berichte vorlagen (Bestätigungsgefahr, offen genannt); die Punktzahl ist eine Einschätzung mit Belegen, die Berichte der Agenten sind Eigenangaben und nicht Teil des Repos._

| Kandidat | K1 | K2 | K3 | K4 | K5 | K6 | K7 | Summe |
|---|---|---|---|---|---|---|---|---|
| K-A Amtsinhaber-Quote und Wettbewerbsblatt | 1 | 1 | 1 | 1 | 0 | 1 | 2 | **7** |
| K-C Klausel-Auswertung | 1 | 1 | 0 | **0** | 2 | 2 | 1 | 7, ausgeschlossen (K4 = 0) |
| K-D Vertragsbestand für Käufer | 0 | 1 | 0 | 1 | 2 | 1 | 1 | 6 |
| K-F Datenqualität als Dienst | 0 | 1 | 0 | 2 | 2 | 0 | 1 | 6 |
| K-G Datenübergabe/Export | 0 | 0 | 0 | 1 | 2 | 2 | 1 | 6 |
| K-B Auftraggeber-Dossier | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 5 |
| K-E Regionalbericht Verband/Vergabestelle | 1 | 0 | 0 | 1 | 2 | 0 | 1 | 5 |
| K-H Anonymer Preis-Benchmark | 1 | 0 | 1 | **0** | 0 | 0 | 0 | 2, ausgeschlossen (K4 = 0, K7 = 0) |

**Nach der vorab festgelegten Entscheidungsregel (höchste Summe unter 8): kein tragfähiger Business Case.** Die höchste zulässige Summe ist 7 (K-A), einen Punkt unter der Schwelle. K-A bleibt als **Testhypothese**: „Größere Reinigungsbetriebe, die für Kommunen bieten, entscheiden Bieten oder Nicht-Bieten besser, wenn sie wissen, wie oft der bisherige Auftragnehmer eine Neuvergabe gewinnt“ (nicht belegt).

**Testplan K-A (rund 24 Stunden, 3 Arbeitstage):** (1) Vorprüfung des Nenners aus den 52 Paaren (3 Std.; Abbruch bei weniger als 30 verwertbaren Paaren); (2) Handprüfung der Namensidentität im Rechercheur-Verfahren mit Wilson-Intervall und vorab festgelegter Intervallbreite (10 Std.); (3) Klauseltest K-C nur als Ausblick (2 Std.; Abbruch unter 10 % mit Klauselangabe); (4) Nachfragetest: Gespräch 1 und mindestens 2 weitere größere Betriebe, Schwelle vorab „mindestens 2 von 3 Ja“ (4 Std.); (5) Auswertung und Lab-Log-Text (4 Std.).

**Grenzen der Quote (Evaluator):** Selektionsbias der Backtest-Paare (nur Neuausschreibungen, nur auf TED auffindbar; verlängerte Verträge fehlen; 52 Paare von 40 Auftraggebern, nicht unabhängig); der Nachfolger-Zuschlag liegt oft noch nicht vor; die Betriebsfrage nach „18 € pro Stunde“ beantwortet eine Quote nicht (Preise je Einheit gibt TED nicht her).

**Neue Befunde, die in den Dokumenten zu korrigieren sind:** (a) aufträge.io zeigt laut Seite Lieferant, Wert, Single-Bid-Rate und Insider/Outsider und enthält auch Verfahren unterhalb der Schwelle (`docs/business.md` §8.2 ergänzen); (b) das OCDS-Feld `numberOfTenderers` ist keine Zahl der Angebote (Beispiel 1 gegen 9 in der TED-XML), echte Bieterzahlen nur in TED; (c) die Aussage „Bieterzahl sinkt“ stützt sich auf ein Gespräch (n = 1); in TED (eForms, Gebäudereinigung) liegt der Median bei 7 Angeboten, höchstens zwei bei 12,5 % (Angaben des Daten-Agenten, nicht nachgerechnet; die Meldeform „nur elektronisch eingegangene Angebote“ verzerrt den Jahresvergleich); (d) die Median-Zahl 7 bei Vergabeweiser gilt für EU-weite Verfahren (die Seite schließt nationale aus); (e) der Median-Jahreswert 167.404 € und die Wettbewerbsbild-Anteile gelten nur für TED-Lose mit plausiblem Wert bzw. eForms in der Oberpfalz.

**Empfehlung für die Gesamtgeschichte:** Kein Produkt bauen. Das Ergebnis „kein tragfähiger Case, offene Hypothese K-A“ ist bewertbar, weil Kriterien und Entscheidungsregel vor der Bewertung feststanden. Wert der Arbeit: geprüftes Lesen der Enden, Prüfverfahren, ehrliche Marktprüfung; Lücke: Preise je Einheit, Mengen und Vertragsklauseln stehen nicht in öffentlichen Daten.

## Nachtrag 2026-11-06 (abends): Kandidat K-I (Push-Matching) und Vorprüfung K-A

**K-I „Push-Matching / automatisierte Auftragssammlung“** (Idee des Nutzers; kam nach der Bewertung der Kandidaten K-A bis K-H, Bestätigungsgefahr). Bewertung des Evaluators nach K1 bis K7: K1 = 1, K2 = 0, K3 = 1, K4 = 1, K5 = 2 (Schätzung), K6 = 1, K7 = 0, Summe 6. **Korrektur durch den Nutzer-Gegencheck (WebFetch, vergabeweiser.de, 2026-11-06):** Die Behauptung, Vergabeweiser biete „Benachrichtigungen per E-Mail, Teams, Slack oder Webhook“, ist nicht bestätigt; die Startseite nennt nur „gespeicherte Suchen und E-Mail-Benachrichtigungen“ (Konto nötig, kostenlos). Damit wäre K2 = 1 (Teams bei Anbietern nicht gefunden; Jorpex nennt Slack; AusschreibungsRadar laut Preisseite nur E-Mail) und die Summe 7. **Das Ergebnis ändert sich nicht:** K7 = 0 (zusätzlicher Produktbau am Projektende wiederholt „erst bauen, dann prüfen“; Kandidat nach der Bewertung eingebracht), K4 ist durch die Matching-Felder begrenzt (Zertifikate und Kapazität stehen in den Vergabeunterlagen, nicht in der Bekanntmachung), und ein Push verkürzt nicht den Vorlauf (28 Tage Meldung vor Abgabe, Frist setzt der Auftraggeber). K-I ist **als Kern ausgeschlossen, als Ausblick zulässig**; eine kleine Demo „Treffer landen im Kanal“ wäre eine Veranschaulichung der Datenübergabe (Paket D) ohne Business-Case-Anspruch. Noch offen: Der Kanal Teams wurde in den Gesprächen nie erfragt.

**Test K-A, Schritt 1 (Vorprüfung des Nenners; Regel vorab im Testplan oben: Abbruch bei weniger als 30 verwertbaren Paaren), Skript `src/report/ka_vorpruefung.py`:** Von den 52 Paaren der Backtest-Basis (`data/processed/x1_paare_iteration5.txt`) haben **23** einen Zuschlag des Nachfolgers in den lokalen TED-Abfragen (Verknüpfung über die Verfahrenskennung der Auftragsbekanntmachung 2026; Abfragestand bis 2026-10-22). Das sind weniger als 30. **Nach der vorab festgelegten Regel ist der Test K-A mit den vorhandenen Paaren abzubrechen.** Zusätzlich gilt: Der Vorgänger-Auftragnehmer liegt nur bei einem Teil der Paare vor (43 von 68 Vorgängern im Alt-XML), verwertbar für eine Quote sind also höchstens die 23 Paare, bei denen beide Seiten vorliegen (nicht gezählt). Eine Amtsinhaber-Quote hätte damit ein breites Intervall (bei 23 Paaren etwa ±20 Prozentpunkte) und bliebe eine **Fallserie**, keine belastbare Rate. Grenzen: Verlängerte Verträge fehlen (Überlebensverzerrung), die Paare stammen von 40 Auftraggebern und sind nicht unabhängig, Nachfolger-Zuschläge von Ausschreibungen 2026 liegen vielfach noch nicht vor.

## Nachtrag 2026-11-09: Kandidat K-J (Push in Teams, Outlook, Planner per Power Automate)

**Kandidat (Idee des Nutzers).** Treffer zu einem Betriebsprofil landen als Nachricht in Teams, Outlook oder Planner, ausgelöst über einen Power-Automate-Ablauf. Evaluation und Recherche vom 2026-11-08/09; die Quellen wurden am 2026-11-06 gelesen. Die einzelnen Punkte je Kriterium K1 bis K7 sind in dieser Quelle nicht festgehalten, nur die Summen.

**Fakten (Stand der Recherche, Eigenangaben der Anbieter, nicht von uns nachgeprüft):**
- Den Ablauf „Alarm auf neue Ausschreibung, Weiterleitung in den Arbeitsplatz“ gibt es bereits kostenlos: TED-Suchprofile mit E-Mail-Alarm und RSS (ted.europa.eu, Seiten „About TED“ und „My dashboard“), gespeicherte Suchen mit E-Mail-Benachrichtigung bei Vergabeweiser (vergabeweiser.de), AusschreibungsRadar ab 29 € mit Suchprofilen und Alerts (ausschreibungsradar.com/preise). Die Weiterleitung einer E-Mail nach Teams oder Planner läuft mit einem Standard-Flow.
- In Power Automate ist die HTTP-Aktion eine Premium-Funktion (13 € je Nutzer und Monat; learn.microsoft.com, Seite zu den Power-Automate-Lizenzen).
- Das Problem „Suchaufwand“ wurde in den drei Gesprächen (n = 3) nicht belegt; der Kanal Teams wurde nie erfragt.
- Im Datensatz der Live-Demo ergeben sich rund 13 bis 19 Treffer pro Jahr und erfundenem Profil (Stufe nach dem Radius, vor dem Fristfilter; `docs/demo_push.md` Abschnitt 11, drei Profile mit 13, 13 und 19). Die Profile sind erfunden, die Zahl ist keine Marktaussage.

**Bewertung nach dem Auswahlbogen:** streng 5, wohlwollend 7 von 14 Punkten; K7 = 0. **Das Ergebnis ändert sich nicht:** K-J ist als Kern ausgeschlossen, als Ausblick zulässig; es bleibt bei „kein tragfähiger Business Case“.

**Billiger Test (vorbereitet, nicht durchgeführt):** (1) eine Stunde: TED-Suchprofil mit E-Mail-Alarm anlegen und per Standard-Flow nach Teams weiterleiten; (2) drei Anrufe mit einer vorab festgelegten Schwelle, ob der Betrieb diesen Weg schon nutzt oder braucht. Der Wert der Schwelle steht in den vorliegenden Dateien nicht: **offen**.

**Grenzen / offen:** Die genauen Unterseiten der Quellen (Microsoft, TED) sind von der Recherche nicht festgehalten und vor Abgabe nachzutragen; Preise und Lizenzbedingungen ändern sich; die Punktzahl ist eine Einschätzung, keine Messung.
