# Business Understanding: Zielgruppe, Gespräche, Erfolgskriterien

Artefakt laut [CRISP-DM.md](CRISP-DM.md#1-business-understanding) (Phase 1). Angelegt am 2026-10-23.
Prüft vor allem die Annahmen A1, A15 (Zahlungsbereitschaft) und A2 (Wettbewerb), siehe [annahmen.md](annahmen.md).

> **Stand 2026-10-29 (Entscheidung des Nutzers):** Das Projekt läuft ohne Kundenkontakt. Die Abschnitte 1 bis 5 (Zielgruppe,
> Gespräche, Leitfaden, Notizvorlage, Notizen) sind **Archiv**: nicht weiterverfolgt, aber erhalten. Aktiv bleiben Abschnitt 6
> (Markt und Preise als Schreibtisch-Recherche) und Abschnitt 7. A1 und A15 bleiben ungeprüft.

## 1. Zielgruppe (vorläufig) – Archiv

- **Branche:** Gebäudereinigung (Unterhalts-, Grund-, Glasreinigung), die sich an öffentlichen Ausschreibungen beteiligt.
- **Region:** Oberpfalz (NUTS DE23), Region des Nutzers.
- **Ansprechpartner:** Geschäftsführung, Vertrieb oder die Person, die Ausschreibungen bearbeitet.

### Fakten aus TED (Quelle: `src/zielgruppe_oberpfalz.py`, Rohdaten `data/raw/ted_search/zielgruppe_oberpfalz_20261023/`)

- Gebäudereinigungs-Zuschläge (Haupt-CPV 9091…) mit Leistungsort Oberpfalz seit eForms (25.10.2023 bis 23.10.2026): **70**,
  davon 6 ohne Firmennamen.
- Darin genannte Auftragnehmer: **71 Firmen**, 21 davon mit mehr als einem Zuschlag. Die Firmen sitzen in der Oberpfalz und außerhalb
  (z. B. Nürnberg, München, Hessen).
- Die Firmenliste liegt in `data/processed/zielgruppe_oberpfalz.csv` und ist **bewusst nicht in Git**, weil Firmennamen von
  Einzelunternehmen Personennamen enthalten können.

### Einschätzung

- Firmen mit TED-Zuschlägen sind die naheliegende Zielgruppe, weil sie EU-weite Ausschreibungen bereits bearbeiten.
- Kleine Firmen, die nur national oder unterhalb der EU-Schwellenwerte anbieten, fehlen in dieser Liste. Sie sind für A3 wichtig
  (Wie viel des Markts sieht TED?) und sollten ebenfalls befragt werden.

## 2. Vorgehen bei den Gesprächen – Archiv

- **Ziel:** 5 Gespräche bis Mitte November 2026. Davon etwa 3 mit Firmen aus der TED-Liste und 2 mit kleineren lokalen Firmen
  (z. B. über eine Suche nach „Gebäudereinigung“ und Landkreis).
- **Kontaktweg:** Telefonzentrale oder Kontaktformular der Firma. Weitere Zugänge sind die IHK Regensburg für Oberpfalz/Kelheim,
  die Innung des Gebäudereiniger-Handwerks in Bayern und die Gründungsberatung der Hochschule.
- **Rahmen:** 15–20 Minuten, telefonisch oder vor Ort. Ausdrücklich **kein Verkaufsgespräch**, sondern ein studentisches Projekt.
- **Kurzvorstellung (Vorschlag):**
  > „Ich bin Student und untersuche in einem Projekt, wie Reinigungsfirmen öffentliche Ausschreibungen finden und sich darauf
  > vorbereiten. Hätten Sie 15 Minuten für ein paar Fragen? Ich verkaufe nichts. Die Antworten verwende ich nur anonymisiert.“

## 3. Gesprächsleitfaden – Archiv

Grundregel: nach **vergangenem, konkretem Verhalten** fragen, nicht nach Meinungen zu einer Idee. Erst am Ende die Idee kurz nennen.
Antworten möglichst wörtlich notieren.

**A. Heute**
1. Wie erfahren Sie heute von öffentlichen Ausschreibungen? Welche Portale oder Dienste nutzen Sie (z. B. DTAD, Vergabeportale, TED)?
   Was kosten die?
2. Erzählen Sie von der letzten Ausschreibung, an der Sie teilgenommen haben. Wann haben Sie davon erfahren, und wie viel Zeit blieb bis zur Abgabe?
3. Was passiert zwischen Bekanntmachung und Abgabe (Begehung, Kalkulation, Personalplanung)? Wo wird es eng?
4. Gab es eine Ausschreibung, die Sie verpasst haben oder zu spät gesehen haben? Was ist passiert?

**B. Wissen über auslaufende Verträge**
5. Wissen Sie heute, wann bei öffentlichen Auftraggebern in Ihrer Region Reinigungsverträge auslaufen? Woher?
6. Verfolgen Sie Verträge von Mitbewerbern oder Objekte, die Sie früher hatten? Wie?

**C. Wert eines frühen Hinweises** (erst jetzt die Idee nennen)
7. Angenommen, Sie wüssten 6–12 Monate vorher, dass Objekt X neu ausgeschrieben wird: Was würden Sie konkret anders machen?
8. Reicht es Ihnen zu wissen, *dass* ein Auftraggeber bald wieder Reinigung ausschreibt, oder brauchen Sie das konkrete Objekt?
9. Wie viele Monate Vorlauf wären nützlich?
10. Was geben Sie heute für Ausschreibungsinformationen aus, und wer entscheidet darüber?

**D. Abschluss**
11. Dürfte ich Ihnen in ein paar Wochen eine kostenlose Testliste für die Oberpfalz zeigen?
12. Wen sollte ich noch fragen?

## 4. Notizvorlage je Gespräch – Archiv

```
### Gespräch <Nr> – <Datum>
- Firma (anonymisiert, z. B. „Reinigungsfirma, ~50 MA, Landkreis Cham“), Rolle der Person:
- Heutige Quellen für Ausschreibungen und Kosten:
- Letzte Ausschreibung (Zeitpunkt, Vorlauf, Engpässe):
- Wissen über auslaufende Verträge:
- Reaktion auf die Idee (wörtliche Zitate):
- Objekt- oder Auftraggeber-Ebene? Gewünschter Vorlauf:
- Zahlungsbereitschaft (Aussage, keine Zusage):
- Testliste gewünscht? ja/nein · Empfehlungen für weitere Gespräche:
- Bezug zu Annahmen: A1 / A2 / A15 / A3 (stützt / schwächt / neutral, Begründung)
```

## 5. Gesprächsnotizen – Archiv

_Noch keine Gespräche (Stand 2026-10-23)._

## 6. Markt und Preise (Schreibtisch-Recherche, 2026-10-24)

Ersatz bzw. Ergänzung für Kundengespräche, falls diese nicht stattfinden. Prüft vor allem A2 (Wettbewerb).

### Fakten

**Wert der Aufträge** ([reports/auftragswerte_909.md](../reports/auftragswerte_909.md), eigene TED-Auswertung, Zuschläge 2024–2025)
- 2.952 Zuschläge Gebäudereinigung (DEU), davon 1.321 (45 %) mit plausiblem Wert.
- Median-Auftragswert über die Gesamtlaufzeit **421.713 €**, Quartile 209.033 € / 954.876 €. Pro Jahr im Median **167.404 €**
  (Quartile 80.367 € / 422.744 €, n = 957 mit bekannter Laufzeit).

**Lohn- und Preisniveau der Branche**
- Branchenmindestlohn Gebäudereinigung Lohngruppe 1 (Innen- und Unterhaltsreinigung) ab 01.01.2026: **15,00 €/Std.**,
  Lohngruppe 6: 18,40 €; die Verordnung gilt bis 31.12.2026. ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/tvmindestlohngeb_ude_2024/BJNR0160B0025.html),
  [Deutsche Handwerks Zeitung](https://www.deutsche-handwerks-zeitung.de/tariflohn-gebaeudereinigung-2025-2026-337962/))
- Stundenverrechnungssätze werden nicht amtlich veröffentlicht. Ein Verbraucherratgeber nennt 25–38 € netto je Stunde
  ([meister-job.de](https://meister-job.de/was-kosten-treppenhaus-reinigen/)). Das ist eine Größenordnung, keine Statistik.

**Ausschreibungsdienste in Deutschland**
- DTAD: keine öffentlichen Preise, Angebot über den Vertrieb, 12 Monate Laufzeit, Zahlung im Voraus. Quellen sind Vergleichsseiten
  von Wettbewerbern ([jorpex.com](https://jorpex.com/de/compare/), [ki-syndikat.de](https://www.ki-syndikat.de/tools/dtad/)).
- subreport: laut Wettbewerber-Vergleich 84–198 € pro Monat zzgl. MwSt., Mindestlaufzeit 12 Monate
  ([jorpex.com](https://jorpex.com/de/compare/subreport-alternative/)). Nicht auf der Seite von subreport selbst geprüft.
- Einen deutschen Dienst, der **auslaufende Verträge** oder **künftige Neuausschreibungen** anzeigt, habe ich in zwei Suchen nicht
  gefunden. Das ist kein Beleg dafür, dass es keinen gibt.

**Ausland (Vergleich)**
- Großbritannien: Stotles bewirbt „expiring contracts“ (auslaufende öffentliche Verträge), laut eigener Preisseite ab 50 £ pro Nutzer
  und Monat (ein Drittanbieter nennt 75 £). Tussell: öffentliche Vertragsdatenbank, Preise nur auf Anfrage
  ([stotles.com](https://www.stotles.com/competitors/tussell), [itqlick.com](https://www.itqlick.com/Products/21420)).

### Interpretation

- Ein einzelner gewonnener Auftrag (Median etwa 167.000 € Umsatz pro Jahr) ist für eine Reinigungsfirma um Größenordnungen mehr
  wert als ein Informationsdienst für 50–200 € im Monat. Wenn ein früher Hinweis die Gewinnchance auch nur gering erhöht, kann sich
  das rechnen. Ob er das tut, ist ohne Kundengespräche nicht belegt (A1, A15).
- Dass es in Großbritannien bezahlte Dienste für auslaufende Verträge gibt, deutet auf eine Zahlungsbereitschaft für diese Art
  Information hin. Das ist allerdings ein anderer Markt mit anderer Datenlage (A2).
- Preis-Hypothese für das Projekt (ungeprüft): 50–150 € pro Monat und Region, also im Bereich bestehender Ausschreibungsdienste.

## 7. Erfolgskriterien

### 7.1 Prognoseziel und Backtest-Regeln (Iteration 5, festgelegt am 2026-10-30, vor jeder Berechnung)

Grundlage: Hypothese und Kriterien X1–X4 in [iterationen.md](iterationen.md) (Iteration 5, Commit 25f7dd3). Hier stehen die Regeln, nach
denen gerechnet wird. Was davon im Produkt nützt, ist ohne Kundengespräche nicht belegt (A1, A15).

**Prognoseziel** _(Entscheidung des Nutzers)_
- Vorhergesagt wird das Datum, an dem die Neuausschreibung veröffentlicht wird. Anker ist das **Höchstende** des Vorgängervertrags,
  also das Ende einschließlich aller Verlängerungsoptionen.
- Begründung: In Iteration 4 erschien die Neuausschreibung meist erst nach dem Ende der Grundlaufzeit (Median etwa 6 Monate danach,
  Streuung −32 bis +26 Monate, 11 Paare; [zuordnung_iteration4.md](../reports/zuordnung_iteration4.md)). In Iteration 3 lagen mindestens
  6 Paare zwischen Grundlaufzeit und Höchstende ([evaluation_iteration3.md](../reports/evaluation_iteration3.md)).
  _Vorbehalt:_ Diese Werte stammen aus denselben Paaren, auf denen jetzt getestet wird.

**Regeln**

| | Regel | Datum |
|---|---|---|
| R1 (Hauptregel) | Höchstende − 6 Kalendermonate; ist das Höchstende nicht bestimmbar: Ende der Grundlaufzeit − 6 Kalendermonate | sonst keine Prognose |
| R0 (naive Referenz) | Ende der Grundlaufzeit − 6 Kalendermonate | sonst keine Prognose |

**Festlegungen**
1. **Nur Wissen zum Zeitpunkt des Vorgänger-Zuschlags.** Quellen sind die Ausschreibung und der Zuschlag des Vorgängers. Vor eForms wird
   die über `REF_NOTICE` verknüpfte Ausschreibung genutzt. Nicht verwendet werden spätere Bekanntmachungen wie Vertragsänderungen
   (can-modif), die neue Ausschreibung selbst und Angaben der Handsuche über tatsächlich ausgeübte Verlängerungen (z. B. U19
   „verlängert bis“). Begründung: Sonst flösse Wissen aus der Zukunft in die Prognose ein.
2. **Ende der Grundlaufzeit:** Enddatum, oder Beginn + Dauer der Grundlaufzeit (Definition „bestimmbar“ wie seit Iteration 1).
3. **Höchstende:** Ein ausdrücklich genanntes spätestes Ende oder eine Gesamthöchstlaufzeit hat Vorrang. Sonst gilt das Ende der
   Grundlaufzeit plus alle möglichen Verlängerungen, wenn deren Dauer angegeben ist (strukturiert oder im Freitext). Gibt es keine
   Verlängerungsoption, ist das Höchstende gleich dem Ende der Grundlaufzeit.
   Wie die einzelnen Felder (BT-36, BT-57, BT-58 u. a.; vor eForms F02/F05) gelesen werden, legt Schritt 3 nach der Prüfung der
   Dokumentation (Schritt 2) fest. Die Regeln werden committet, bevor R0 und R1 eingefroren werden (Schritt 6).
   _Präzisierung 2026-10-30 (Schritt 3, vor jeder Prognose auf Backtest-Paaren):_ Die Lese-Regeln stehen im Kopf von
   `src/prepare/vertragsliste.py`. Zwei Abweichungen vom Wortlaut oben: (a) Statt „ausdrückliches Ende hat Vorrang“ gilt der
   **späteste plausible Kandidat**, weil im Text auch Kündigungstermine nach der Grundlaufzeit stehen. (b) Nennt der Text das
   Enddatum selbst als spätestes Ende, ist das Enddatum das Höchstende und die Grundlaufzeit endet früher (Regel 1a). Gelesen
   werden BT-57, BT-54 und BT-24. Genauigkeit in einer Teststichprobe etwa 91 % ([Bericht](../reports/hoechstende_pruefung_iteration5_test.md)).
4. **Höchstende nicht bestimmbar** (Option ohne Dauer, rollierende Verlängerung ohne Höchstdauer): R1 nimmt das Ende der Grundlaufzeit.
   Herkunft wird je Paar gekennzeichnet, Treffer werden getrennt nach Herkunft berichtet.
5. **Unbefristete Verträge** ohne Ende der Grundlaufzeit: keine Prognose. In X4 zählen sie als nicht abgedeckt. In X3 kommen sie nicht
   vor, weil X1 ein bestimmbares Ende der Grundlaufzeit verlangt.
6. **Mehrere Lose:** Maßgeblich sind die Lose des Vorgängers, die laut Handsuche zum Objekt gehören. Haben sie verschiedene Enden, gilt
   das früheste. Ist keine Zuordnung möglich, gilt das früheste Ende aller Lose (gekennzeichnet).
7. **Treffer:** Veröffentlichungsdatum des Testfalls (erste Bekanntmachung des neuen Verfahrens) liegt im Bereich
   Prognose − 3 Kalendermonate bis Prognose + 3 Kalendermonate, Grenzen eingeschlossen. Zusätzlich ohne Schwelle: ±6 Monate und die
   Abweichung in Monaten.
8. **Objektgleich und Teilmenge** zählen gleich, werden aber getrennt ausgewiesen.

**Kennzahlen und Schwellen:** X1–X4 wie in [iterationen.md](iterationen.md); technisches Erfolgskriterium ist X3 (R1 ≥ 60 % Treffer
±3 Monate und mindestens 10 Prozentpunkte über R0).

**Fachliches Erfolgskriterium** _(festgelegt 2026-11-04, vor dem Backtest-Lauf; Vorschlag von Claude, bestätigt vom Nutzer)_
- **Nutzen:** Ein Eintrag der Vertragsliste hilft einem Reinigungsbetrieb, wenn die Neuausschreibung im Fenster von **±3 Monaten** um das
  prognostizierte Datum erscheint: Der Betrieb kann Angebot, Referenzen und Personal gezielt vorbereiten, statt Bekanntmachungen
  dauernd zu beobachten.
- **Schwelle:** Die Liste gilt als brauchbar, wenn R1 in **mindestens 60 %** der Fälle im Fenster trifft **und** mindestens **10 Prozentpunkte
  besser** ist als die naive Referenz R0. Unter 40 % taugt sie nicht als Terminprognose; die Liste bliebe dann ein Verzeichnis mit Enddaten.
- **Setzung, nicht belegt:** Das Fenster von ±3 Monaten stammt aus dem Projektplan; ohne Kundengespräche (A1, A15) ist nicht belegt, welches
  Fenster und welche Quote ein Betrieb braucht. Der Wert der Liste bleibt eine Annahme.
- Gilt zusammen mit den technischen Kriterien X1–X4 (`docs/iterationen.md`, Iteration 5).

**Grenzen der Messung**
- Gemessen wird nur, wie oft eine Neuausschreibung im prognostizierten Fenster liegt, **wenn** sie auf TED erscheint (Trefferquote). Wie
  viele Prognosen ins Leere gehen (Präzision), misst Iteration 5 nicht.
- Die Paare wurden rückwärts gesucht, also von der Ausschreibung zum Vorgänger. Ob sie für die Verträge einer Vertragsliste typisch sind,
  ist offen.
- Ein geschäftliches Kriterium (welcher Vorlauf und welches Fenster einem Kunden reichen) ist ohne Gespräche nicht festlegbar. Das
  ±3-Monats-Fenster stammt aus dem Projektplan und ist eine Setzung.

### 7.2 Ursprünglicher Plan (Archiv)

_Stand 2026-10-29: ohne Gespräche werden die Erfolgskriterien aus Recherche und Backtest abgeleitet (z. B. Treffer im Zeitfenster);
der folgende ursprüngliche Plan ist Archiv._

Geschäftliche und technische Erfolgskriterien werden nach den ersten Gesprächen festgelegt, zum Beispiel der Vorlauf, den Kunden
brauchen, und das daraus folgende Trefferfenster für den Backtest. Entscheidungstor laut [projektplan.md](projektplan.md), Strang G:
Zeigt mindestens ein Teil der Gesprächspartner ein konkretes Problem und Interesse an einer Testliste, folgt ein Pilot. Sagt niemand,
dass früheres Wissen hilft, ist das ein ernstes Warnsignal.

## 8. Markt, Wettbewerb und Positionierung (Nachtrag nach Iteration 9, 2026-11-05)

_Anlass: Der Dozent verlangt mehr Gewicht auf Business Understanding. Grundlage: Web-Recherche eines Recherche-Agenten und ein kritisches Gutachten eines zweiten Agenten aus BWL-Sicht (beide 2026-11-05, ohne Kundenkontakt).
Angaben mit **(geprüft)** hat Claude am 2026-11-05 selbst auf der Seite nachgelesen; alle anderen stammen aus der Recherche des Agenten und sind nicht einzeln nachgeprüft. Abschnitt 6 bleibt als früherer Stand stehen; seine Aussage „keinen deutschen Dienst für auslaufende Verträge gefunden“ ist überholt._

### 8.1 Fakten: Wie Reinigungsfirmen heute an öffentliche Aufträge kommen

- **Kostenlos:** Bekanntmachungsservice [oeffentlichevergabe.de](https://www.oeffentlichevergabe.de) (Datenservice Öffentlicher Einkauf, BeschA; ober- und unterschwellig, Suchvorlagen mit ELSTER-Konto, Open Data als eForms-DE, OCDS und CSV, [BeschA](https://www.bescha.bund.de/DE/E-Beschaffung/Datenservice/Oeffentlicher-Einkauf_node.html)); Suchprofile mit E-Mail-Alarm auf TED; IHK-Ausschreibungsdienste.
- **Kostenpflichtig:** Ausschreibungsdienste wie subreport (84–198 € pro Monat zzgl. USt., [Produktübersicht](https://subreport.de/ausschreibungen/produktuebersicht/)), DTAD (nur über den Vertrieb), evergabe.de (83 € pro Monat).
- **Eignung:** Präqualifikation über das AVPQ der IHKs, gültig 1 Jahr, z. B. 90 € bei der IHK Stuttgart ([IHK Stuttgart](https://www.ihk.de/stuttgart/fuer-unternehmen/oe-ausschreibungen/service-unternehmen/pq-vol-verfahren-avpq-678374)).
- **Zuschlagskriterien:** Der BIV empfiehlt Preis und Qualität je 50 %, Objektbesichtigung und mindestens 30 Tage Angebotsfrist ([BIV-Empfehlungen Mai 2026](https://www.die-gebaeudedienstleister.de/wp-content/uploads/2026/05/BIV_Vergabe-Empfehlungen_oeffentlVergabe_Mai26.pdf)); vergeben werde in der Praxis „überwiegend nach dem günstigsten Preis“ ([Vergabeblog 28.01.2026](https://vergabeblog.de/2026-01-28/reinigungsdienste-bundesinnungsverband-veroeffentlicht-empfehlungen-zur-oeffentlichen-vergabe/)). Laut Vergabestatistik 2024 wurden 63 % aller Vergaben nur nach Preis entschieden ([cosinex, Zusammenfassung des BMWE-Berichts](https://blog.cosinex.de/2026/08/27/vergabestatistik-bericht-2024/)).
- **Umfrage KOINNO 2025** (n = 62 KMU und Start-ups, alle Branchen; nur die Zusammenfassung gelesen, [cosinex](https://blog.cosinex.de/2025/07/07/startups-und-kmu-in-der-oeffentlichen-beschaffung/)): Knapp die Hälfte findet selten passende Ausschreibungen; 56 % wurden schon vor einer Ausschreibung vom Auftraggeber kontaktiert (Markterkundung).
- **Branche:** rund 35.000 Betriebe, 658.000 Beschäftigte, 27,5 Mrd. € Umsatz (BIV-Branchenreport 2025 über [DHZ](https://www.deutsche-handwerks-zeitung.de/?p=364247)). BIV-Konjunkturumfrage Frühjahr 2026 (n = 250): 16 % erwarten ein positives Jahr, 49 % haben Kunden oder Aufträge verloren ([BIV](https://www.die-gebaeudedienstleister.de/wp-content/uploads/2026/04/260414_Deutschlands-personalintensivstes-Handwerk-im-Stimmungstief-1.pdf)). Den Anteil öffentlicher Auftraggeber am Branchenumsatz hat die Recherche nicht gefunden.
- **Abdeckung durch TED:** EU-Schwellenwert für Dienstleistungen 2026/2027: 216.000 € (Kommunen, Länder), 140.000 € (oberste Bundesbehörden) ([Vergabeblog 21.01.2026](https://vergabeblog.de/2026-01-21/eu-schwellenwerte-wurden-zum-01-01-2026-angepasst/)). Über alle Branchen lagen 2024 88 % der Vergaben unter der Schwelle (cosinex, s. o.); für Reinigung allein nicht gefunden.

### 8.2 Fakten: Wettbewerber mit Funktion „auslaufende Verträge“

| Anbieter | Land | Was er zeigt | Preis | Quelle |
|---|---|---|---|---|
| **Vergabeweiser** | DE | 10.265 Verträge, die in 12 Monaten enden, davon **1.005 Gebäudereinigung**; je Vertrag Zuschlagsempfänger, Zahl der Angebote, Verlängerungsoptionen, Erinnerung per E-Mail; Daten ober- und unterschwellig seit 12/2022 | kostenlos | [vergabeweiser.de/geplant](https://vergabeweiser.de/geplant) **(geprüft)** |
| **AusschreibungsRadar** | DE/AT | rund 26.000 Aufträge mit Laufzeitende in 1 bis 18 Monaten, „verlängerbar“ markiert, geschätzter Ausschreibungsmonat („Median 111 Tage vor Vertragsbeginn“, mit Fragezeichen) | 0–149 € pro Monat | [Vertragsende](https://ausschreibungsradar.com/vertragsende/) **(geprüft)**, [Preise](https://ausschreibungsradar.com/preise/) |
| aufträge.io | DACH | 43.373 Verträge mit Ende in 12 Monaten, Analyse der bisherigen Gewinner | auf Anfrage | [auftraege.io](https://www.auftraege.io/) |
| TenderRender | DE | Vorhersage auslaufender Verträge (6/12/24 Monate) | ab 300 € pro Monat (Eigenangabe) | [Blog](https://www.tenderrender.com/de/blog/ausschreibungen-verwalten-software) |
| Stotles | UK | „expiring contracts“ mit Prognose; Series A rund 10 Mio. £ (2025) | ab etwa 50 £ pro Monat | [stotles.com/pricing](https://www.stotles.com/pricing) |
| Tussell | UK | Vertragsdaten, Wettbewerber; über 300 Firmenkunden (Eigenangabe) | Behördenverträge 18.000–29.000 £ pro Jahr | [Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/871b5dc1-ab3f-4d0d-a884-da4f997cae6a) |
| GovSpend | US | Modul „Expiring Contracts“ | geschätzt 11.600–15.000 USD pro Jahr (Angabe eines Wettbewerbers) | [GovSpend](https://govspend.com/?p=17171) |

Beide geprüften deutschen Anbieter schreiben ausdrücklich, dass der Auftraggeber entscheidet, ob und wann neu ausgeschrieben wird.

### 8.3 Fakten aus dem eigenen Projekt, die für die Bewertung zählen

- Die Liste nutzt nur TED (oberhalb der EU-Schwelle) und nur eForms-Zuschläge ab Oktober 2023 (9.325 Lose, [vertragsliste_iteration9.md](../reports/vertragsliste_iteration9.md)).
- Die meisten Vorgänger heutiger Neuausschreibungen stammen aus der Zeit vor eForms: 55 von 68 Backtest-Vorgängern ([ki_irrwege.md](ki_irrwege.md)), nur etwa 5 von 38 Vorgängern in Iteration 3 (A10). Einen objektgleichen Vorgänger auf TED hatten 63,3 % (A3).
- Die Liste enthält weder Zuschlagsempfänger noch Wert noch Zahl der Angebote (Kopfzeile von [beispiel_liste_oberpfalz.csv](../reports/beispiel_liste_oberpfalz.csv)); die Rohdaten enthalten diese Felder.
- Terminprognose ±3 Monate 28,8 % (Iteration 5); Ende der Grundlaufzeit zu 94,3 % wie zwei KI-Leser, Höchstende nur Hinweis (Iteration 9).

### 8.4 Interpretation: Was aus Unternehmersicht keinen Sinn ergibt

1. **Das Kernprodukt gibt es schon, kostenlos und mit mehr Abdeckung** (kritisch). Vergabeweiser zeigt Vertragsenden in der Gebäudereinigung samt Zuschlagsempfänger und Bieterzahl, ober- und unterschwellig. Unsere Liste ist enger (nur TED) und hat weniger Felder. Ein Markteintritt mit der Liste allein ergibt keinen Sinn.
2. **Das Kundenproblem ist eine Setzung** (kritisch). Neuausschreibungen sind öffentlich, mit mindestens 30 Tagen Frist, und Suchdienste dafür gibt es kostenlos. Der Engpass der Betriebe liegt nach den Quellen eher beim Preis (Vergabe überwiegend nach Preis), bei Personal und Eignung und bei der Frage, wo sich ein Angebot lohnt. Ob „früher wissen“ hilft, ist ohne Gespräche nicht belegt (A1, A15).
3. **Die Liste sieht die nahe Zukunft kaum** (kritisch). Die Verträge, die in den nächsten 6 bis 18 Monaten neu ausgeschrieben werden, wurden meist vor eForms vergeben und fehlen; die Lücke schließt sich erst über die Jahre.
4. **Vertragsende ist kein Termin** (mittel). Verlängerungen, Kündigungsfristen und Eigenreinigung verschieben die Neuausschreibung. Das betrifft alle Anbieter gleich; die Wettbewerber weisen es ebenso aus.
5. **Marktgröße** (mittel; grobe Schätzung des Gutachtens, Annahmen offen): Bei 3.000 bis 6.000 Betrieben, die öffentlich bieten (Annahme 10–20 % von rund 30.000), und 1.200 € pro Jahr läge das gesamte Potenzial bei 3,6–7,2 Mio. €; für ein Zweierteam ohne Vertrieb realistisch 40 bis 200 Kunden (50.000–240.000 € pro Jahr). Gegen kostenlose Konkurrenz ist auch das fraglich.
6. **Kundenbindung** (mittel). Die Liste ändert sich langsam; nach dem ersten Blick gibt es wenig Grund, monatlich zu zahlen.

### 8.5 Interpretation: Mehrwert und mögliche Positionierung

- **Was vom Mehrwert bleibt:** (a) gemessene Lesequalität auf Losebene (Ende der Grundlaufzeit, Regel 1b „Enddatum ist schon Höchstende“, Lose ohne Zuschlag); keiner der geprüften Wettbewerber veröffentlicht, wie genau seine Vertragsenden sind. (b) Der Backtest-Beleg, dass ein fester Abstand den Termin nicht vorhersagt (28,8 %). (c) Ein sauber dokumentiertes Prüfverfahren (Seeds, Hashes, Evaluator). Das ist ein Mehrwert für das Studium und für einen Datenanbieter, kaum direkt für einen Reinigungsbetrieb.
- **Positionierungen im Vergleich** (Bewertung des Gutachtens, ergänzt um die Wettbewerbslage):

| Richtung | Einschätzung |
|---|---|
| Liste der Vertragsenden als eigenes Produkt | nicht tragfähig: kostenlos vorhanden (Vergabeweiser) |
| Wettbewerbsbild für die Entscheidung „bieten oder nicht, zu welchem Preis“ (Amtsinhaber, Jahreswert, Bieterzahl, Fenster frühestens bis spätestens) | inhaltlich am stärksten, aber Vergabeweiser zeigt Amtsinhaber und Bieterzahl schon; ein Vorsprung bliebe nur bei Preis-Benchmarks (Jahreswert je Auftraggeber; nur 45 % der Zuschläge mit plausiblem Wert) |
| Datenqualität als Zulieferung (Lese-Regeln, Prüfverfahren) für bestehende Dienste | realistischster Weg; kleiner Markt, Käufer können nachbauen |
| Beratung oder Jahresreport für Reinigungsbetriebe über Innung oder Auftragsberatung | der Kanal wäre der Vorteil, nicht die Technik; Zahlungsbereitschaft offen |
| Benchmark für Vergabestellen (Auftragswertschätzung) | denkbarer Zweitmarkt, kleine Budgets |

- **Was einen vom Markt abheben könnte:** nicht die Daten (offen, CC0), sondern Branchentiefe in einer Nische (z. B. Objektart, Leistungsumfang, Jahreswert je Auftraggeber), nachgewiesene Datenqualität und ein Vertriebskanal über Verband oder Kammer. Keiner dieser Punkte ist im Projekt geprüft.

### 8.6 Folgen für das Projekt

- **A2 widerlegt** (siehe `docs/annahmen.md`): Deutsche Dienste zeigen auslaufende Verträge, einer schätzt auch den Ausschreibungstermin.
- Die Sichtung der Wettbewerber (Projektplan G1.1) war früh geplant und ist erst jetzt erfolgt; die Suche vom 2026-10-24 (Abschnitt 6) fand die deutschen Anbieter nicht. Das ist ein Versäumnis im Business Understanding und wird im Lab-Log offen genannt.
- **Ehrliche Einordnung:** Das Projekt zeigt, wie genau sich Vertragsenden aus TED lesen lassen und dass sich der Termin der Neuausschreibung mit einem festen Abstand nicht vorhersagen lässt. Ein eigenständiges Geschäftsmodell für die Liste lässt sich daraus nicht ableiten.
- **Was in der Restzeit noch möglich wäre** (Entscheidung beim Nutzer): (1) drei bis fünf kurze Gespräche mit Reinigungsbetrieben aus der Oberpfalz-Liste, einer Vergabestelle und der Auftragsberatung Bayern, mit der Frage, ob sie Vergabeweiser oder AusschreibungsRadar kennen und was ihnen fehlt; (2) eine Stichprobe: für 10 bis 20 Lose der Oberpfalz-Liste das Vertragsende bei Vergabeweiser nachsehen und vergleichen (zeigt, ob unsere Lesequalität einen Unterschied macht).

_Nachtrag 2026-11-05:_ Beides wird in Iteration 10 umgesetzt (`docs/iterationen.md`); der Vergleich (2) läuft per Skript über die API von Vergabeweiser an den 70 Zufallslosen der Iteration 9 statt an der Oberpfalz-Liste, weil es dort schon einen festen Vergleichswert gibt.

### 8.7 Nachtrag: Marktzahlen bei Vergabeweiser (Fakt, 2026-11-05)

Die API von Vergabeweiser liefert kostenlos auch Marktzahlen je Gewerk und Region (`/market`, Rohantwort `data/raw/vergabeweiser_20261105/market_gebaeudereinigung_bayern.json`). Für Gebäudereinigung in Bayern: 470 Ausschreibungen in 12 Monaten; 1.805 vergebene Lose mit Angebotszahl, im Median 7 Angebote, 77 Lose mit nur einem Angebot; Zuschlagssummen (n = 594) im Median 129.050 €, Quartile 30.748 € / 438.459 €; dazu eine Liste der Firmen mit den meisten Zuschlägen.
**Interpretation:** Auch das „Wettbewerbsbild“ (Amtsinhaber, Bieterzahl, Zuschlagswerte), das das BWL-Gutachten als beste Positionierung empfahl (§8.5), gibt es dort schon kostenlos. Die Zeile in §8.5 ist damit noch schwächer als dort beschrieben.

### 8.8 Kurzleitfaden für Telefonate (Iteration 10, W5)

_Vorab festgelegt am 2026-11-05. Zwei bis drei Gespräche à etwa 10 Minuten: Reinigungsbetriebe aus der Oberpfalz-Liste (Gewinner in `reports/beispiel_liste_oberpfalz.csv` stehen nicht in der Liste; Betriebe über die Webseite der Auftraggeber oder die Innung finden) oder eine Vergabestelle (z. B. Stadt Regensburg). Kein Verkaufsgespräch, Kurzvorstellung wie in Abschnitt 2. Notizen ohne Namen von Personen; Firmen nur beschreibend („Reinigungsfirma, ~50 Beschäftigte, Landkreis Cham“)._

**An Reinigungsbetriebe**
1. Wie erfahren Sie heute von öffentlichen Ausschreibungen? Welche Dienste oder Portale nutzen Sie, was zahlen Sie dafür?
2. Erzählen Sie von der letzten öffentlichen Ausschreibung, bei der Sie mitgeboten haben: Wann haben Sie davon erfahren, wo wurde es eng?
3. Woran entscheiden Sie, ob Sie mitbieten? (Preis, Gegner, Objektgröße, Personal, Entfernung)
4. Wissen Sie, wann Reinigungsverträge bei Auftraggebern in Ihrer Region auslaufen? Woher?
5. Kennen Sie Vergabeweiser oder AusschreibungsRadar? Falls ja: Nutzen Sie die Liste auslaufender Verträge, und was fehlt Ihnen dort?
6. Hätte Ihnen ein früherer Hinweis (6–12 Monate) bei einem konkreten Auftrag etwas gebracht? Was hätten Sie anders gemacht?
7. Wofür würden Sie zahlen, wenn überhaupt: genauere Enddaten je Los, Gegner und Preise der letzten Vergabe, Hilfe bei der Kalkulation, nichts davon?

**An eine Vergabestelle**
1. Wie planen Sie die Neuausschreibung eines Reinigungsvertrags: Wie viele Monate vor Vertragsende fangen Sie an?
2. Wie oft verlängern Sie statt neu auszuschreiben, und wovon hängt das ab?
3. Bekommen Sie zu wenige Angebote? Würden Sie es begrüßen, wenn Firmen früher wüssten, dass ein Vertrag ausläuft?

**Notiz je Gespräch:** Wer (beschreibend), Datum, Antworten möglichst wörtlich, Bezug zu A1/A15 (stützt, schwächt, neutral). Ablage: `docs/business.md` §8.9.

### 8.9 Ergebnisse der Gespräche (Iteration 10, W5; geführt vom Nutzer am 2026-11-05, Notizen von ihm, hier übertragen)

_Fakten sind die Aussagen der Gesprächspartner, Zitate wörtlich nach den Notizen des Nutzers; es sind **drei** Gespräche, keine Stichprobe. Namen von Personen und Firmen wurden nicht notiert (eine empfohlene Firma ist hier bewusst nicht genannt). Die Einordnung zu A1, A15, A3 im Anschluss stammt von Claude, nicht von den Gesprächspartnern._

**Fakten**

| | Gespräch 1 | Gespräch 2 | Gespräch 3 |
|---|---|---|---|
| Wer | Reinigungsbetrieb, ca. 120 Beschäftigte, Landkreis Schwandorf; Vertriebsleitung/Kalkulator; 14 Min. | Reinigungsbetrieb, 15 Beschäftigte, Stadt Amberg; Inhaberin; 8 Min. | Landratsamt (mittelgroß), Oberpfalz; Leitung Vergabestelle; 12 Min. |
| Wie sie Ausschreibungen finden | DTAD (knapp 1.500 € pro Jahr, Suchprofile), gelegentlich Bayerisches Vergabeportal | Webseiten von Stadt und Landkreis alle paar Wochen, Lokalteil der Zeitung; „zahlen für keine Portale“ | – |
| Letzte Ausschreibung | Berufsschule vor drei Wochen; Meldung 28 Tage vor Abgabe; eng bei der Objektbegehung (ein Termin, bester Vorarbeiter krank), Kalkulation nachts | Kindergarten im Vorjahr; „tausend Eigenerklärungen“, ein Wochenende | – |
| Entscheidung mitzubieten | „Hauptsächlich Entfernung und Personal“ (über 40 km nicht; Kräfte für Früh-/Abendzeiten nötig) | Kapazität des Teams, kein Einstellen für unsicheren Auftrag, direkter Umkreis | – |
| Wissen über Vertragsenden | „Nur bei denen, die wir selbst haben oder … knapp verloren haben. Ansonsten ist das eine Blackbox.“ | „Nein“, nur Flurfunk | – |
| Vergabeweiser / AusschreibungsRadar | „vom Hörensagen“, nicht abonniert; im DTAD kennt er keine Listen auslaufender Verträge | „Nie gehört“ | – |
| Früherer Hinweis (6–12 Monate) | „Absolut“: Personal in der Zielregion früher suchen (Social Media, Aushänge); nach Zuschlag „schwitzt man Blut und Wasser“ | „Eigentlich nicht“: Kapazitäten in 6 Monaten nicht planbar (Schwangerschaft, Kündigung) | Gewünscht: Bei der letzten Unterhaltsreinigung für ein Gymnasium genau zwei Bieter, vor fünf Jahren fünf bis sechs; mehr Bieter halte die Preise realistisch |
| Wofür Zahlung | Alte Preise und aktueller Auftragnehmer („wenn der aktuelle Dienstleister bei 18 Euro pro Stunde lag, brauche ich gar nicht erst mitbieten“); Enddaten „nett für die Planung“; Aufpreis beim Portal, klang nach etwa 50–100 € pro Monat extra (Einschätzung des Nutzers, kein genannter Betrag) | „Für gar nichts in dem Bereich“; braucht Hilfe bei den Formblättern, nicht beim Finden | – |
| Vergabestelle: Planung | – | – | Fachbereich beginnt etwa 9 Monate vor Vertragsende mit dem Leistungsverzeichnis; Veröffentlichung „meist 3 bis 4 Monate vor Start“ |
| Vergabestelle: Verlängern | – | – | „Fast immer, wenn eine Verlängerungsoption im Vertrag steht“; meist 2 Jahre fest plus 1 Jahr Option; „Neu ausschreiben ist ein enormer Aufwand“ |
| Vergabestelle: Schwelle | – | – | „Sehr oft“ national vergeben („alles unter 221.000 Euro“), vor allem Außenstellen, Jugendzentren, kleinere Schulen als Einzellose, um den regionalen Mittelstand zu fördern |

Anrufe: 9, erreicht 3 (Gespräche 3), Absagen 2; Zeitaufwand 105 Minuten (Vorbereitung, Anrufe, Abtippen). _Berichtigung des Nutzers 2026-11-05:_ „4 erreicht“ in den Notizen war ein Tippfehler.
_Hinweis zur Schwelle:_ In den Notizen steht als Aussage der Vergabestelle „alles unter 221.000 Euro“. Der Nutzer hält das für einen Versprecher; der Schwellenwert für Dienstleistungen von Kommunen und Ländern beträgt seit 01.01.2026 216.000 € (Vergabeblog, §8.1). Die Aussage („sehr oft“ unterschwellig) bleibt davon unberührt; der Betrag wird nicht verwendet.

**Interpretation (Claude; n = 3, Hinweise, keine Belege)**

1. **A1/A15 gespalten, nach Betriebsgröße:** Der größere Betrieb (120 Beschäftigte) sieht Nutzen in früher Information (Personalsuche), zahlen würde er aber eher für Wettbewerbsdaten als für Enddaten. Der Kleinbetrieb (15 Beschäftigte) hätte von sechs bis zwölf Monaten Vorlauf nichts und will für Informationen nichts zahlen; sein Engpass ist die Bürokratie. Die Zielgruppe „Mittelstand“ ist damit enger als gedacht (größere Betriebe, die für Kommunen und Behörden bieten).
2. **Was der Kunde bezahlen würde, ist nicht die Liste, sondern das Wettbewerbsbild** (aktueller Auftragnehmer, alte Preise). Das stützt die Richtung aus dem BWL-Gutachten (§8.5). Genau das zeigen Vergabeweiser (Zuschlagsempfänger, Zahl der Angebote, Zuschlagssummen) und AusschreibungsRadar (Zuschlagsempfänger, Wettbewerber-Tracking in Business ab 79 € pro Monat) schon.
3. **Bekanntheit statt Funktion?** Keiner der beiden Betriebe nutzt einen der Dienste; einer kennt sie vom Hörensagen, die andere gar nicht. Der Betrieb mit Abo nutzt DTAD. Das deutet eher auf ein Vertriebs- und Bekanntheitsproblem der Konkurrenz als auf eine Lücke im Angebot. Das ist eine Hypothese; die Zahl der Gespräche trägt keinen Schluss.
4. **Die Vergabestelle bestätigt die Grenze der Terminprognose:** Verlängerung ist der Normalfall (zwei Jahre plus Option), das Vertragsende ist also kein Neuausschreibungstermin; geplant wird etwa 9 Monate vor Vertragsende, veröffentlicht meist 3 bis 4 Monate vor Start. Das passt zu Iteration 5 (28,8 %) und zeigt, warum das **Höchstende** (nicht das Ende der Grundlaufzeit) für die Planung zählt, das die Liste nur als Hinweis führt.
5. **Aus Sicht der Auftraggeber gibt es einen Bedarf:** Bieterzahl sinkt (zwei statt fünf bis sechs). Das stützt einen zweiten Markt (Vergabestellen oder Bietermarketing), auf den die Recherche schon hinwies (§8.5, Benchmark für Vergabestellen). Die Aussage stammt von einer einzigen Stelle.
6. **A3:** Die Vergabestelle vergibt Reinigung „sehr oft“ unterhalb der EU-Schwelle (Einzellose), also nicht auf TED. Das stützt die Lücke unserer Datenbasis (Kleinaufträge fehlen) und spricht für Vergabeweiser, das auch unterschwellige Bekanntmachungen führt.
7. **Folgerung für die Positionierung (Entwurf, abhängig von W1):** Eine reine Liste der Vertragsenden trägt nicht. Der Nutzen liegt eher bei größeren Betrieben (Personal- und Kalkulationsplanung) und bei Vergabestellen; Zahlungsbereitschaft zeigt sich nur für Wettbewerbsdaten, die es bereits gibt.
