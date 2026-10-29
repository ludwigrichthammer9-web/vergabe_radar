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

## 7. Erfolgskriterien (offen)

_Stand 2026-10-29: ohne Gespräche werden die Erfolgskriterien aus Recherche und Backtest abgeleitet (z. B. Treffer im Zeitfenster);
der folgende ursprüngliche Plan ist Archiv._

Geschäftliche und technische Erfolgskriterien werden nach den ersten Gesprächen festgelegt, zum Beispiel der Vorlauf, den Kunden
brauchen, und das daraus folgende Trefferfenster für den Backtest. Entscheidungstor laut [projektplan.md](projektplan.md), Strang G:
Zeigt mindestens ein Teil der Gesprächspartner ein konkretes Problem und Interesse an einer Testliste, folgt ein Pilot. Sagt niemand,
dass früheres Wissen hilft, ist das ein ernstes Warnsignal.
