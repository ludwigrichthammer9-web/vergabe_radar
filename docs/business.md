# Business Understanding: Zielgruppe, Gespräche, Erfolgskriterien

Artefakt laut [CRISP-DM.md](CRISP-DM.md#1-business-understanding) (Phase 1). Angelegt am 2026-10-23.
Prüft vor allem die Annahmen A1, A15 (Zahlungsbereitschaft) und A2 (Wettbewerb), siehe [annahmen.md](annahmen.md).

## 1. Zielgruppe (vorläufig)

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

## 2. Vorgehen bei den Gesprächen

- **Ziel:** 5 Gespräche bis Mitte November 2026. Davon etwa 3 mit Firmen aus der TED-Liste und 2 mit kleineren lokalen Firmen
  (z. B. über eine Suche nach „Gebäudereinigung“ und Landkreis).
- **Kontaktweg:** Telefonzentrale oder Kontaktformular der Firma. Weitere Zugänge sind die IHK Regensburg für Oberpfalz/Kelheim,
  die Innung des Gebäudereiniger-Handwerks in Bayern und die Gründungsberatung der Hochschule.
- **Rahmen:** 15–20 Minuten, telefonisch oder vor Ort. Ausdrücklich **kein Verkaufsgespräch**, sondern ein studentisches Projekt.
- **Kurzvorstellung (Vorschlag):**
  > „Ich bin Student und untersuche in einem Projekt, wie Reinigungsfirmen öffentliche Ausschreibungen finden und sich darauf
  > vorbereiten. Hätten Sie 15 Minuten für ein paar Fragen? Ich verkaufe nichts. Die Antworten verwende ich nur anonymisiert.“

## 3. Gesprächsleitfaden

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

## 4. Notizvorlage je Gespräch

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

## 5. Gesprächsnotizen

_Noch keine Gespräche (Stand 2026-10-23)._

## 6. Erfolgskriterien (offen)

Geschäftliche und technische Erfolgskriterien werden nach den ersten Gesprächen festgelegt, zum Beispiel der Vorlauf, den Kunden
brauchen, und das daraus folgende Trefferfenster für den Backtest. Entscheidungstor laut [projektplan.md](projektplan.md), Strang G:
Zeigt mindestens ein Teil der Gesprächspartner ein konkretes Problem und Interesse an einer Testliste, folgt ein Pilot. Sagt niemand,
dass früheres Wissen hilft, ist das ein ernstes Warnsignal.
