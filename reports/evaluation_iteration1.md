# Evaluation Iteration 1

> Erstellt am 2026-10-22 vom Subagenten `evaluator` (`.claude/agents/evaluator.md`, nur Lesezugriff).
> **Eingaben:**
> - Hypothese (nachträglich formuliert) und Definition „Laufzeitende bestimmbar“
> - geplante Nischenentscheidung samt Begründung und bekannten Korrekturen
> - Prüfpunkte: Saisonalität, Bau/Architektur/Ingenieure, fehlende Auftragsbekanntmachungen, Backtest-Machbarkeit, statistische Unsicherheit, Parsing-Stichprobe, Annahmen
>
> Der Text zwischen den Trennlinien ist die **unveränderte** Antwort des Evaluators. Anmerkungen von Claude (Hauptsitzung) stehen getrennt am Ende.

---

## Evaluation Iteration 1

Stand: 2026-10-22 · Evaluator (nur Lesezugriff) · Geprüft: `reports/datenqualitaet_DEU_20260722_20261021.md` (im Folgenden [R]), `reports/stichprobe_iteration1.md` ([S]), `src/analyze_completeness.py`, `src/ted_download.py`, `src/stichprobe_parsing.py`, `data/raw/ted_search/DEU_20260722_20261021/request_meta.json` ([M]), `docs/iterationen.md`, `docs/phasen/01_business_understanding.md`, `docs/phasen/02_data_understanding.md`, `docs/annahmen.md`, `docs/CRISP-DM.md`, `CLAUDE.md`. Eigene Nachzählungen per Grep in `data/processed/notices_DEU_20260722_20261021.csv` ([CSV]) und zwei Web-Stichproben auf ted.europa.eu.

**Geprüfte Hypothese (nachträglich formuliert):** „Für mindestens eine wiederkehrende Dienstleistungsnische lässt sich bei mindestens 80 % der Zuschläge ein Laufzeitende bestimmen.“ „Bestimmbar“ heißt: BT-537 vorhanden oder BT-536 und BT-36 vorhanden, jeweils in irgendeinem Los, gezählt auf Notice-Ebene.

---

### Urteil je Kriterium

| Kriterium | Urteil | Beleg (Quelle) |
|---|---|---|
| **K1** Mind. eine Nische mit ≥ 80 % „Laufzeitende bestimmbar“ (strenge Definition) | **teilweise** | Punktschätzer: Gebäudereinigung 80,9 % (356/440), Winterdienst 84,5 % (109/129), Sicherheitsdienste 83,9 % (115/137) [R §5]. Eigene Rechnung (Wilson, 95 %): Gebäudereinigung 77,0–84,3 %, Winterdienst 77,3–89,7 %, Sicherheit 76,9–89,2 %. Bei allen drei Nischen schließt das Intervall Werte unter 80 % ein. Gebäudereinigung liegt 0,9 Prozentpunkte über der Schwelle. Ein einseitiger Test gegen 80 % ergibt z ≈ 0,48 (p ≈ 0,32). Die Schwelle wurde erst nach Kenntnis der Daten gesetzt. |
| **K1a** Großzügige Variante „Ende oder Dauer“ ≥ 80 % | erfüllt, aber für den Zweck zu großzügig | Gebäudereinigung 90,0 % (396/440; Wilson 86,8–92,5 %) [R §4]. Eine Dauer ohne Beginn ergibt aber kein Enddatum. Das betrifft 40 Notices in dieser Nische (396 − 356; per Grep bestätigt: 40 Zeilen mit BT-36 im 1. Los ohne Beginn und Ende [CSV]). |
| **K2** Zahl solcher Notices pro Jahr ≥ N (laut `docs/iterationen.md`) | nicht prüfbar | N wurde nie festgelegt. Es gibt nur 3 Monate Daten. Eine Hochrechnung (440 × 4 ≈ 1.760 pro Jahr) ist wegen unbekannter Saisonalität nicht belastbar. |
| **K3** Daten reichen zeitlich weit genug zurück für einen Backtest (laut `docs/iterationen.md` und `CLAUDE.md` Z. 14) | nicht prüfbar (nicht untersucht) | Es wurden keine Daten vor dem 22.07.2026 geladen [M]. Die Rückreichweite steht in `docs/iterationen.md` selbst als „noch offen“. Die neue Hypothese lässt dieses Teilkriterium stillschweigend weg. |
| **K4** Parsing korrekt (STOPP-Regel, laut [S] vorab festgelegt) | erfüllt, mit geringer Trennschärfe | 0 Fehler der Ursache (a) in 15 Notices [S, Fazit]. Eigene Rechnung: Die 95-%-Obergrenze der Fehlerrate liegt bei ca. 18 % (0/15), für die Nische allein bei ca. 45 % (0/5). Damit sind nur grobe Fehler ausgeschlossen. |
| **K5** Ergebnis laut Iterationsplan: „Entscheidung für eine Nische“ (`docs/CRISP-DM.md`, Iterationsplan) | teilweise | Aus Datensicht lässt sich die Wahl begründen (s. u.). Das Phase-1-Gate „Nische **und** messbare Erfolgskriterien“ (`docs/CRISP-DM.md` §1) ist aber nicht erfüllt: 0 Kundengespräche, kein Wettbewerbs-Check, keine geschäftlichen Erfolgskriterien (`docs/phasen/01_business_understanding.md`). |

---

### Schwächen (nach Schwere)

**Kritisch**

1. **Kriterium und Schwelle stehen nachträglich fest und liegen knapp unter dem Ergebnis.** `docs/iterationen.md` hält fest: „Schwelle noch offen … Bestätigungsgefahr“. Die nun gesetzten 80 % liegen 0,9 Prozentpunkte unter dem Wert der bevorzugten Nische (80,9 %). Das Ergebnis hängt stark von Schwelle und Definition ab:
   - Bei 85 % (streng) besteht keine der fünf Nischen; das Maximum ist 84,5 %.
   - Mit der großzügigen Definition bestehen vier von fünf Nischen [R §4].
   - Hinzu kommt Mehrfachtesten: 5 Kandidaten-Nischen und 2 Definitionen, gesucht war nur „mindestens eine“. Die Chance, eine Nische knapp über einer nachträglich gesetzten Schwelle zu finden, ist dadurch hoch.
   - Außerdem wurde die Hypothese gegenüber `docs/iterationen.md` verengt. Die Teilkriterien N/Jahr und Rückreichweite fehlen jetzt. Auch das ist eine nachträgliche Änderung und muss als solche dokumentiert werden.

2. **„Laufzeitende bestimmbar“ ist eine notwendige, aber keine hinreichende Bedingung für das Radar. Die eigentliche Zielgröße wurde nicht angefasst.** Geladen wurden nur `form-type=result` [M]. Damit ist **nicht** gezeigt:
   - (a) dass Nachfolgeaufträge überhaupt wieder auf TED erscheinen. Sie könnten unter dem EU-Schwellenwert liegen, nur national veröffentlicht werden, inhouse vergeben oder über Rahmenverträge zentraler Beschaffer abgerufen werden (A3);
   - (b) dass sie sich den Vorgängern zuordnen lassen (A9);
   - (c) welche Vorlaufzeit zwischen Laufzeitende und Neuausschreibung liegt (A8);
   - (d) wie viele Auftragsbekanntmachungen (competition) es in CPV 909 pro Jahr gibt, also die Basisrate des Prognoseziels;
   - (e) ob das Enddatum im Zuschlag die Basislaufzeit ohne Verlängerungen meint. Das ist ungeklärt; siehe den Befund aus [R §5]: Nur 10 Notices haben BT-36 und ein Datumspaar, davon stimmen nur 40 % auf ±1 Monat überein.

3. **Ein Backtest „allein mit eForms-Daten“ ist nicht belegt und bei den gemessenen Laufzeiten eher unwahrscheinlich.** Für Gebäudereinigung gilt laut Datumsangaben: Median 36 Monate, Quartile 24/48 (n = 350) [R §5]. eForms ist seit Ende Oktober 2023 Pflicht. Bis heute sind das rund 36 Monate Beobachtungsfenster. Ein Vertrag mit Median-Laufzeit, der im November 2023 vergeben wurde, endet etwa Ende 2026. Seine Neuausschreibung liegt je nach Vorlaufzeit gerade jetzt oder noch in der Zukunft.
   - Beobachtbar sind also fast nur die kürzeren Verträge (etwa unteres Quartil, ≤ 24 Monate) aus dem ersten eForms-Jahr. Dazu kommen nur Verträge, deren Verlängerungsoptionen nicht gezogen wurden. Das ist relevant, weil 42,0 % BT-58 > 0 haben [R §4].
   - Die Folge wäre eine systematische Verzerrung zugunsten kurzer Verträge, Verträge ohne Verlängerung und Auftraggeber, die schnell und EU-weit neu ausschreiben. Eine „noch nicht erschienene“ Neuausschreibung ist rechtszensiert und darf nicht als Fehlprognose zählen.
   - Die ursprüngliche Begründung „Median ca. 24 Monate, daher Backtest allein mit eForms möglich“ beruht auf BT-36 mit n = 45. Sie ist in beiden Teilen nicht haltbar.

**Mittel**

4. **Das 3-Monats-Fenster (22.07.–21.10.2026) ist nicht repräsentativ belegt.**
   - **Winterdienst** zeigt ein typisches Saisonmuster: 52 Zuschläge vom 22.07. bis 31.08. (ca. 1,3 pro Tag) und 77 vom 01.09. bis 21.10. (ca. 1,5 pro Tag) [CSV, Grep auf Haupt-CPV 9062/9063]. Die Fallzahl dieses Fensters (129) dürfte über dem Jahresdurchschnitt liegen. Winterdienst stellt hier 129 von 164 Zuschlägen der CPV-Gruppe 906 [R §3]. Belegen lässt sich der Saisoneffekt ohne andere Monate aber nicht.
   - **Gebäudereinigung** ist über die Monate recht gleichmäßig verteilt: Juli (ab 22.) 58, August 151, September 153, Oktober (bis 21.) 78 [CSV]. Die Zusammensetzung kann trotzdem saisonal sein. In der Liste der Enddaten 2026/2027 dominieren Starts zum 01.10. und 01.01. mit 12-Monats-Laufzeit [CSV, 64 von 352 Notices mit Enddatum bis Ende 2027]. Das passt zu Haushaltsjahr-Verträgen, die im Herbst vergeben werden. Zuschläge im Frühjahr, etwa Schulreinigung zum Schuljahresbeginn, könnten andere Laufzeiten und Befüllungsquoten haben.
   - Haushalts- und Jahresendeffekte (Q4) und die Ferienzeit (Juli/August) liegen im Fenster, der Jahresendspurt im November/Dezember nicht.

5. **Bezugsgröße der Gesamtzahlen.** Bau (CPV 45: 5.538) und Architektur/Ingenieure (CPV 71: 2.699) machen zusammen 8.237 von 15.706 Notices aus, also 52,4 % [R §3]. Bei diesen Leistungen ist die „Laufzeit“ meist eine Projekt- oder Bauzeit ohne Wiederkehr. Alle Gesamtkennzahlen sind daher für das Radar kaum aussagekräftig: 86,4 % Laufzeit, 82,0 % Ende/Dauer, 61,7 % bestimmbar, Median 24 bzw. 16 Monate [R §2, §5].
   - A10 stützt sich ausdrücklich auf den Gesamt-Median von 24 Monaten [R §2], also auf eine falsche Bezugsgröße.
   - Sinnvoll wäre als Nenner „wiederkehrende Dienstleistungen“: eine vorab definierte CPV-Liste ohne 45/71 oder wenigstens `contract_nature = services` ohne 71.

6. **Notice- statt Vertrags- bzw. Losebene, keine unabhängigen Beobachtungen.**
   - Die Hypothese spricht von „Zuschlägen“, gemessen wurden Notices. Ein Los mit Enddatum reicht, damit die ganze Notice als „bestimmbar“ zählt (`end_determinable` in `src/analyze_completeness.py`, Z. 268–270). Beginn und Dauer dürfen dabei sogar aus verschiedenen Losen stammen.
   - Es gibt Häufungen. Universität Stuttgart veröffentlichte am 21.09.2026 vier Notices (648512, 649561, 649891, 650172-2026), alle ohne Laufzeit. Weitere Beispiele: BImA mit 26 von 440 Notices (5,9 %), Stadt Mannheim 9 [CSV]. Die effektive Stichprobe ist dadurch kleiner als 440, die Unsicherheit größer als oben berechnet.
   - Eine vollständige Konzentrationsanalyse (Top-10-Auftraggeber) liegt nicht vor.

7. **Was die fehlenden 19 % in Gebäudereinigung sind, ist ungeklärt.** Aufschlüsselung [R §4/§5, CSV]:
   - 40 Notices haben nur BT-36 ohne Beginn.
   - 30 Notices haben im 1. Los weder Dauer noch Beginn noch Ende; davon sind 8 als `can-desg` (Wettbewerbsergebnis) veröffentlicht.
   - Der Rest hat nur den Beginn, BT-538 oder Angaben in anderen Losen.
   - Keine der 5 Gebäudereinigungs-Notices der Parsing-Stichprobe stammt aus diesen 84 Fällen. Die Seite „nicht bestimmbar“ ist für die gewählte Nische also gar nicht validiert.
   - Zwei eigene Web-Stichproben (über ein Zusammenfassungswerkzeug, daher weniger streng):
     - 648512-2026 (Glasreinigung, Uni Stuttgart): keine Grundlaufzeit, aber „Maximale Verlängerungen: 2, jeweils für 2 Jahre“ und ein Vertragsabschlussdatum 31.08.2026.
     - 603205-2026 (Unterhaltsreinigung, BIM Berlin): als „Wettbewerbsergebnis“ veröffentlicht, keine Laufzeit, nur Vertragsabschluss 20.07.2026.
   - Beides sind echte Lücken in der Quelle, keine Parsing-Fehler.

8. **Die Nischenabgrenzung „909…“ ist nicht rein Gebäudereinigung.** Zusammensetzung [CSV]:
   - 404 von 440 (91,8 %) tragen 90910/90911/90919 (Reinigung, Gebäude- und Fensterreinigung, Büro/Schulen).
   - 23 tragen den generischen Code 90900000.
   - 9 tragen 9092… (Hygiene/Schädlingsbekämpfung).
   - 4 tragen 90915/90917/90918 (Schornstein-, Fahrzeug-, Mülltonnenreinigung).
   - Der Fehler ist klein, aber das Etikett ist ungenau. Zudem zählt nur der Haupt-CPV; Mehrfach-Los-Notices mit Reinigungslosen unter anderem Haupt-CPV fehlen (A12).

9. **Die Parsing-Stichprobe ist methodisch sauber, aber klein und prüft nur die Weiterleitung, nicht die Bedeutung.**
   - Positiv: Seed, Schichtung (5/10), XPaths aus dem SDK, vorab benannte STOPP-Regel, Ursachenklassen (a) bis (d), offen benannte Grenzen [S].
   - Grenzen:
     - XML und Search API stammen aus derselben Quelle. Geprüft wird die Zuordnung API → CSV, nicht die inhaltliche Richtigkeit der Angaben der Vergabestellen.
     - Nur 7 Notices hatten mehrere Lose.
     - Die Gegenprobe in der Webansicht lief über ein Zusammenfassungswerkzeug.
     - Die 5 Fälle aus der Nische enthalten keinen Negativfall (s. Punkt 7).
     - Dass die STOPP-Regel vorab festgelegt wurde, ist nur durch die Aussage in [S] belegt, nicht durch einen Zeitstempel.
   - Der Befund „`total-value` ist nicht BT-161“ (573266-2026: keine `TotalAmount` in der XML, Wert = BT-720) ist ein guter, gut belegter Fund. Der Report hat die Beschriftung korrigiert [R §2, §6].
   - Folgen sind aber noch nicht umgesetzt:
     - Die Kategorie „Auftragswert befüllt 70,8 %“ [R §2] und der Nachweis zu A6 (2.276 von 10.775 Werten ≤ 1 €) beruhen weiter auf `total-value`.
     - Ein Teil dieser „Platzhalter“ könnte aus der TED-Ableitung stammen, z. B. aus Angebotswerten von 0,01 €, und nicht direkt aus einem Gesamtwert der Vergabestelle.

**Gering**

10. `end_determinable` prüft Enddaten nicht auf Plausibilität. Nur die Laufzeitstatistik schließt Werte ≤ 0 bzw. > 240 Monate aus (`src/analyze_completeness.py`, Z. 268–273). In CPV 909 gibt es kein Enddatum ab 2040 [CSV]. Der Effekt ist hier also null, gesamt mindestens 12 Notices mit Enddatum ≥ 2050 im 1. Los [CSV].
11. Die Laufzeit-Mediane beruhen nur auf dem 1. Los. Die Monatsumrechnung mit 30,44 Tagen ist für Mediane unkritisch.
12. Die Phasendokumente sind nicht synchron:
    - `docs/phasen/02_data_understanding.md` nennt noch „Manuelle Stichprobe (1 Notice)“. Die 15er-Stichprobe fehlt.
    - Die Nischentabelle dort führt nur den BT-36-Median (24 Monate, ohne n = 45).
    - Dort steht „> 90 % Ende oder Dauer“ für Gebäudereinigung, tatsächlich sind es genau 90,0 %.
    - `docs/iterationen.md` zitiert nur die großzügige Variante (90,0 %) und eine andere Hypothese als die jetzt geprüfte.
13. Die geplante Begründung „höchster Anteil strukturierter Verlängerungsangaben“ ist falsch, wie bereits bekannt. Die Werte sind praktisch gleich: 42,0 % (185/440) gegenüber 42,3 % (58/137) [R §4, nachgerechnet]. Bei „irgendein Verlängerungsfeld“ liegt Sicherheit mit 77,4 % klar vor Gebäudereinigung mit 65,2 %.
    - Zudem ist ein hoher Anteil an Verlängerungsoptionen für die Prognose zweischneidig: Er macht das tatsächliche Ende unsicherer, nicht sicherer.

---

### Alternative Erklärungen

- **Fehlendes Laufzeitende bedeutet nicht zwingend eine Datenlücke.** Mögliche Gründe:
  - unbefristete Verträge (BT-538 „UNLIMITED“; Anteil in 909 nicht ausgewertet);
  - Laufzeit nur im Freitext (573266-2026 [S]);
  - falsches Formular (8 von 440 Notices in 909 als `can-desg` [CSV]; 603205-2026);
  - Angabe nur als Dauer ohne Beginn (40 Fälle).

  Im letzten Fall ließe sich der Beginn näherungsweise schätzen, etwa über das Vertragsabschlussdatum. Das ist bei beiden Web-Stichproben vorhanden, wurde aber nicht heruntergeladen. Die 80,9 % sind daher eher eine Untergrenze dessen, was mit Zusatzannahmen erreichbar ist. Umgekehrt sind die 90,0 % eine Obergrenze, die Unschärfe in Kauf nimmt.
- **Die Unterschiede zwischen den Nischen sind mit Zufall vereinbar.** Gebäudereinigung (80,9 %), Sicherheit (83,9 %) und Winterdienst (84,5 %) haben stark überlappende Konfidenzintervalle. Eine Rangfolge nach Befüllung ist nicht belegt.
- **Die gute Befüllung kann ein Fenster-Effekt sein.** Im Herbst vergebene Jahres- und Mehrjahresverträge mit festen Stichtagen (01.10., 01.01.) haben naturgemäß klare Daten. In anderen Quartalen kann der Anteil anders sein.
- **Die Laufzeit-Verteilung ist eine Momentaufnahme der Vergaben von 2026.** Sie muss nicht auf die Verträge von 2023/24 zutreffen, die ein Backtest nutzen würde.
- **Die hohe Zahl in 909 kann teils aus Losaufteilung entstehen.** Ein Beispiel sind mehrere Notices eines Auftraggebers am selben Tag (Uni Stuttgart). In dem Fall ist die Zahl unabhängiger Vertragsbeziehungen kleiner als die Notice-Zahl.
- **Die Nichtübereinstimmung BT-36 gegen Datumsangaben (4 von 10 übereinstimmend [R §5]) lässt mehrere Deutungen zu.** Eine Quelle könnte Verlängerungen einschließen und die andere nicht. Oder die Vergabestellen füllen die Felder uneinheitlich. Bei n = 10 ist keine Deutung belegt.

---

### Fakten vs. Interpretation

- **Geplante Begründung der Nischenentscheidung** (Vorgabe des Nutzers):
  - „größte **wiederkehrende** Dienstleistungsnische“: Größe ist Fakt (440 gegenüber 137/129/47 unter den Kandidaten [R §4]); „wiederkehrend“ ist Annahme.
  - „sodass ein Backtest allein mit eForms-Daten möglich ist“ ist eine Interpretation, die als Folgerung auftritt und durch keine Auswertung gedeckt ist (s. Schwäche 3).
- **`docs/phasen/02_data_understanding.md`, „Interpretation“:** „Eine Baseline-Prognose aus Laufzeitende erscheint machbar“. Das ist als Interpretation gekennzeichnet (gut). Es stützt sich aber auf die großzügige Definition und blendet aus, dass Zielereignis und Zuordnung nicht untersucht sind.
- **`docs/phasen/02_data_understanding.md`, Nischentabelle unter „Fakten“:** „Median-Laufzeit BT-36 24 Mon.“ für Gebäudereinigung ist formal richtig, ohne n = 45 und ohne den Datumsmedian (36, n = 350) aber irreführend.
- **[R §6]:** „Für die Prognose müssen Verlängerungen also aus dem Text extrahiert werden“ ist eine Verallgemeinerung aus einer Notice (505084-2026), formuliert als Tatsache. Auch „oft nur als Freitext“ ist nicht quantifiziert.
- **[R §2]:** „Laufzeit ‚sonstige‘ (meist UNLIMITED/UNKNOWN)“: Das „meist“ ist im Report nicht ausgezählt.
- **`docs/annahmen.md`, A10, Spalte Nachweis:** Hier steht eine Interpretation auf Basis der falschen Bezugsgröße (Gesamtmedian 24 Monate). Das ist kein Nachweis.
- **`docs/annahmen.md`, A4:** Bestätigt wird „Dienstleistungsnischen“ allgemein. Gemessen sind 5 Nischen in einem Fenster, und IT-Dienste liegt streng bei nur 33,7 % [R §5].
- **`docs/iterationen.md`, Ergebnis:** Fakten und Interpretation sind sauber getrennt (gut). Die „Fakten“ zeigen aber nur die großzügige Quote; die strenge fehlt.
- **Positiv:** [S] trennt sauber zwischen Befund, Ursache und Grenzen („Das ist eine Beobachtung aus einem Fall“).

---

### Betroffene Annahmen

- **A3** (TED bildet relevanten Marktanteil ab): **ungeprüft, Risiko eher höher.** Gerade Reinigungsverträge liegen oft nahe am oder unter dem Schwellenwert, sodass Nachfolger womöglich nicht auf TED erscheinen. Der Projekterfolg hängt direkt daran.
- **A4:** **bestätigt lassen, Nachweis präzisieren.** Ergänzen: „großzügige Definition (Ende oder Dauer); streng bestimmbar: Gebäudereinigung 80,9 %, Winterdienst 84,5 %, Sicherheit 83,9 %, IT-Dienste 33,7 % [R §5]; Notice-Ebene, Haupt-CPV, Veröffentlichung 22.07.–21.10.2026“. Die Formulierung „Dienstleistungsnischen“ allgemein ist durch 5 Nischen nur begrenzt gedeckt.
- **A5:** **widerlegt lassen.** Ergänzen, dass in 909 BT-58 > 0 bei 42,0 % liegt [R §4], also höher als gesamt (14,7 %) und dennoch nicht „überwiegend“.
- **A6:** **widerlegt lassen, Nachweis korrigieren.** `total-value` ist ein von TED berechneter Wert, nicht BT-161 [S]. „Gesamtwert ≤ 1 €“ ist deshalb nicht dasselbe wie „Vergabestelle trägt Platzhalter ein“. Ein Platzhalter im Original ist durch 505084-, 561098- und 702922-2026 belegt [S].
- **A7:** **Nachweis ergänzen.**
  - Teilbeleg: 684689-2026 hat `-1` zusammen mit dem Block `efac:FieldsPrivacy`, und die Webansicht zeigt „Nicht veröffentlicht“. Bei 636832-2026 steht `-1` ebenfalls in der XML [S].
  - Ein Statuswechsel auf „bestätigt“ ist bei niedrigem Risiko vertretbar, aber nur mit dem Geltungsbereich „2 Fälle, Wertfelder“.
  - Ob jedes `-1` einen FieldsPrivacy-Block hat, ist nicht geprüft.
- **A8:** **ungeprüft.** Nichts dazu untersucht; ohne competition-Daten nicht prüfbar.
- **A9:** **ungeprüft, jetzt riskanteste und am leichtesten prüfbare Annahme.** Es wurde kein einziges Zuschlag-Neuausschreibungs-Paar gesucht.
- **A10:** **ungeprüft lassen, Nachweis ersetzen, Risiko gestiegen.** Neue Grundlage: Gebäudereinigung hat laut Datumsangaben einen Median von 36 Monaten (Quartile 24/48, n = 350) [R §5], bei 42 % mit Verlängerungsoption [R §4]. Bei rund 36 Monaten eForms-Historie sind überwiegend nur kurze Verträge ohne Verlängerung vollständig beobachtbar, mit Zensierungs- und Selektionsverzerrung. „Widerlegt“ ist A10 noch nicht: Zensierungsgerechte Verfahren oder A11 könnten helfen.
- **A11:** **ungeprüft, an Bedeutung gestiegen.** Davon hängt ab, ob ein Backtest über volle Zyklen möglich ist. Ob die Formate vor eForms in Zuschlags- oder Auftragsbekanntmachungen Laufzeiten enthalten, ist zu prüfen und nicht aus dem Gedächtnis anzunehmen.
- **A12:** **ungeprüft, Teilbeleg ergänzen.** 91,8 % der 909-Notices tragen Reinigungs-Codes (90910/90911/90919), der Rest Hygiene, Schädlingsbekämpfung oder generische Codes [CSV]. 8 Notices nutzen das falsche Formular `can-desg`. Ob Reinigungslose unter anderem Haupt-CPV versteckt sind, ist nicht geprüft.
- **A13 (neu, geplant „bestätigt“):** **Vorschlag: ungeprüft (vorläufig gestützt), nicht bestätigt.**
  - Der Punktschätzer liegt 0,9 Prozentpunkte über einer nachträglich gesetzten Schwelle. Das 95-%-Intervall (77,0–84,3 %) schließt Werte unter 80 % ein.
  - Der Beleg stammt aus genau den Daten, aus denen die Schwelle abgeleitet wurde.
  - Gemessen wurde auf Notice-Ebene, die Annahme spricht von „Zuschlägen“.
  - Bestätigen ließe sich A13 ehrlich durch eine vorab festgelegte Replikation in einem unabhängigen Zeitfenster, etwa einem Quartal aus 2024 oder 2025 mit gleicher Definition und Schwelle.
  - Wird A13 trotzdem auf „bestätigt“ gesetzt, muss der Nachweis Konfidenzintervall, nachträgliche Schwelle, Notice-Ebene und Zeitfenster ausdrücklich nennen.
- **A14 (neu, „ungeprüft“):** Status korrekt. Hinweis: A14 ist ein Oberbegriff, der in A3, A8, A9 und A10 zerfällt. Ohne messbare Fassung (z. B. Trefferquote im ±3-Monats-Fenster, siehe Phase-1-Fragen) ist A14 nicht prüfbar.

---

### Was für ein belastbares Urteil fehlt

1. **Replikation in einem unabhängigen Zeitfenster** mit vorab fixierter Definition und Schwelle, idealerweise ein Frühjahrs- und ein Vorjahresquartal. Das deckt Saisonalität und Bestätigungsgefahr zugleich ab.
2. **Auftragsbekanntmachungen (competition) für CPV 909**, z. B. 3 bis 12 Monate. Daraus ergeben sich Basisrate, Erscheinen auf TED und ein erster Zuordnungsversuch zu früheren Zuschlägen über Auftraggeber und CPV (A9). Dazu ein Blick auf Vorinformationen (PIN) als mögliches Frühsignal.
3. **Rückreichweite:** Anzahl der 909-Zuschläge seit Ende Oktober 2023 und Verteilung ihrer Enddaten. Daraus folgt, wie viele Verträge bis heute ausgelaufen sein sollten. Außerdem eine Prüfung, ob TED-Daten vor eForms Laufzeiten enthalten (A11).
4. **Stichprobe der 84 nicht bestimmbaren 909-Notices**, z. B. 20: Freitext, unbefristet, falsches Formular oder echte Lücke?
5. **Klärung in der eForms-Dokumentation**, ob BT-36/BT-536/BT-537 die Laufzeit mit oder ohne Verlängerungen meinen. Davon hängt die Bedeutung von „Laufzeitende“ für die Prognose ab.
6. **Auswertung auf Losebene** und eine Konzentrationsanalyse nach Auftraggebern (Top 10 und Anteil) für 909.
7. **Messbare geschäftliche Erfolgskriterien und erste Kundengespräche** (Phase-1-Gate), damit die Nischenwahl nicht allein datengetrieben ist.

---

### Empfehlung

**Zurück zu Phase 2, bevor Phase 3 beginnt. Gebäudereinigung (CPV 909) bleibt dabei vorläufige Arbeitsnische.**

Die Entscheidung für Gebäudereinigung ist als pragmatische Arbeitsnische tragfähig: Sie hat unter den Kandidaten mit Abstand die meisten Fälle, und ihre Datenqualität ist vergleichbar mit Winterdienst und Sicherheitsdiensten. Winterdienst ist zudem vermutlich saisonal überzeichnet. Nicht tragfähig sind die Behauptungen „Kriterium klar erfüllt“, „höchster Verlängerungsanteil“ und „Backtest allein mit eForms möglich“. Die riskantesten Annahmen (A9, A10, A3) und das Teilkriterium Rückreichweite sind ungeprüft und lassen sich mit wenig Aufwand in Phase 2 prüfen. Das sollte vor dem Bau einer Baseline geschehen.

Eine ehrliche Begründung könnte etwa lauten:

> „Wir arbeiten vorläufig mit Gebäudereinigung (Haupt-CPV 909…, davon 92 % Reinigungs-Codes). Sie ist unter den geprüften Kandidaten die häufigste Dienstleistungsnische: 440 Zuschläge vom 22.07. bis 21.10.2026. Bei 80,9 % lässt sich ein Laufzeitende bestimmen (95-%-KI ca. 77–84 %; 90,0 %, wenn Dauer ohne Beginn mitzählt). Das liegt im Rahmen von Winterdienst und Sicherheitsdiensten, die Schwelle von 80 % wurde nachträglich gesetzt. Die Laufzeit liegt im Median bei 36 Monaten (Quartile 24/48, n = 350). 42 % der Zuschläge haben mindestens eine strukturierte Verlängerungsoption, die das tatsächliche Ende offenlässt. Offen und für die Machbarkeit entscheidend sind: ob Nachfolgeaufträge auf TED erscheinen und sich zuordnen lassen und ob die eForms-Historie seit Herbst 2023 für einen Backtest reicht. Bei 36 Monaten Median ist das fraglich. Kundensicht und Wettbewerb sind nicht geprüft.“

Die Entscheidung trifft der Nutzer.

---

## Anmerkungen von Claude (Hauptsitzung)

- **Nachgerechnet** mit `data/processed/notices_DEU_20260722_20261021.csv` und bestätigt:
  - 356/440 = 80,9 %, Wilson-95-%-Intervall 77,0–84,3 %
  - 396/440 „Ende oder Dauer“
  - 40 Notices mit BT-36 im 1. Los ohne Beginn und Ende
  - 404/440 mit Reinigungs-Codes 90910/90911/90919
  - 8 × `can-desg`
- **Ergänzung zur Konzentration (Schwäche 6):** Zweitgrößter Auftraggeber in CPV 909 ist die Stadt Frankfurt am Main, Amt für Bau
  und Immobilien, mit 24 Notices. Zusammen mit der BImA (26) stammen damit 50 von 440 Notices (11,4 %) von zwei Auftraggebern.
- Die übrigen Zählungen des Evaluators habe ich nicht einzeln nachgeprüft: Monatsverteilung, Enddaten ≥ 2050 und die Web-Stichproben 648512/603205-2026.
