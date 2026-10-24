# Urteilsregeln für die Blindprüfung der Zuordnung

**Version 1.1, 2026-10-24.** Gilt für die Blindprüfung in Iteration 3 (20 Paare aus Zuschlag und möglicher Neuausschreibung).
Vor dem ersten echten Urteil committen. Danach werden die Regeln nicht mehr geändert (siehe Spielregel 1).

## Zweck

Ein Mensch beurteilt, ob zwei Bekanntmachungen **dasselbe Objekt** betreffen. Das Urteil soll nachvollziehbar sein und
von der Prognose selbst unabhängig bleiben. Damit lässt sich später belegen, wie zuverlässig die automatische Zuordnung
(Annahme A9) ist.

## Spielregeln

1. **Diese Regeln stehen vor dem ersten echten Paar fest** und sind committet. Wer sie danach ändern will, legt eine neue
   Version mit Datum und Grund an und beurteilt **alle** Paare neu.
2. Es werden **nur die beiden Bekanntmachungen** eines Paares geöffnet. Keine anderen Reports von Iteration 3, kein Lösungsschlüssel.
3. **Zeitabstand, Vertragsende und Laufzeiten werden nicht berücksichtigt**, auch nicht für die Tendenz. Dass die zweite
   Ausschreibung zeitlich passt, ist genau das, was das Projekt erst belegen will. Als Argument entstünde ein Zirkelschluss.
4. **Jedes Urteil bekommt eine Begründung** mit Feld und Wert (ein Satz).
5. **„Unklar“ ist ein gültiges Urteil.** Nicht raten, um eine klare Zahl zu erhalten.
6. Bei Unsicherheit zwischen zwei Urteilen gilt das **vorsichtigere** (siehe Rangfolge).
7. Beurteilt werden Bekanntmachungen als Ganzes. Bei mehreren Losen wird in der Begründung vermerkt, **welche Lose** Überschneidungen haben.

## Schritt 1: Merkmale vergleichen

| Stufe | Merkmale | Aussagekraft |
|---|---|---|
| **A: Identität** | Adresse oder Objektliste, Gebäudename, Fläche in m², Anzahl Gebäude, Geschosse oder Gebäudeteile | Legen ein Objekt eindeutig fest. Nur hier ist ein sicheres Urteil möglich. |
| **B: Objektraum** | Stadtteil oder Gebiet, Objektart, Leistungsart (Unterhalt, Glas, Grund) | Grenzen das Objekt ein, machen es aber nicht eindeutig. |
| **C: Stütze** | Auftraggeber, CPV-Code, Titel, Kennungsschema, **Losstruktur**, Zuschlagskriterien, Optionstext | Reichen allein nie. Sie machen ein Urteil nur plausibler. |
| **Nicht verwenden** | Zeitabstand, Vertragsende, Laufzeit, Auftragswert | Würde das Projektziel selbst voraussetzen oder ist oft Platzhalter. |

### Definitionen und Klarstellungen

**Stufe C**
- Ein abweichender Wert in Stufe C (CPV, Auftraggebername, Titel, Losstruktur) ist **kein Widerspruch**.
- Eine Übereinstimmung in Stufe C **gleicht keinen Widerspruch** in Stufe A oder B aus. Auch wenn Auftraggeber, Titel, CPV und
  Kriterien wortgleich sind: Der Auftraggeber schreibt Schwesterverfahren oft nach demselben Muster aus.
- Eine abweichende Anschrift des Beschaffers bei gleicher Körperschaft (z. B. Zentrale in einer anderen Stadt) ist kein Widerspruch.
- Ein anderer Losschnitt (andere Zahl oder Art der Lose) ist kein Widerspruch zum Objekt.

**Fläche**
- Eine Fläche zählt nur beim Vergleich **gleicher Flächenarten** (Reinigungsfläche mit Reinigungsfläche, Glasfläche mit Glasfläche).
  Vermischen die Angaben beider Seiten die Arten, werden beide Lesarten geprüft. Gibt es keine eindeutige, gilt die Fläche als
  **mehrdeutig**: weder Übereinstimmung noch Widerspruch.
- Bis **2 %** Abweichung gilt eine Fläche als gleich, darüber als **abweichend**. Abweichend ist kein Widerspruch, schließt aber
  „objektgleich (hoch)“ aus. Die Abweichung wird in der Begründung genannt.

**Einzelstandorte** (Hochschule, Museum, Verwaltungssitz, einzelne Dienststelle)
- Die Adresse allein zählt nicht als Merkmal aus Stufe A, weil jeder Vertrag dieses Auftraggebers sie nennen würde.
  Für „hoch“ sind zwei weitere A-Merkmale nötig (z. B. Fläche, Geschosse, Gebäudeteile).

**Erkennbarkeit von Stufe B**
- Die **Objektart** gilt als erkennbar, wenn sie im Text steht **oder** sich zweifelsfrei aus Auftraggeber oder Standort ergibt
  (Hochschule, Museum, Polizeiinspektion). „Diverse Gebäude“ oder „verschiedene Objekte“ eines Auftraggebers mit vielen Gebäudearten
  (Stadt, Kreis, Land) ist **nicht** erkennbar.
- Stufe B ist **nicht erkennbar**, wenn Objektart oder Gebiet auf mindestens einer Seite nicht erkennbar sind.
- Eine fehlende oder unspezifische **Objektliste** (Stufe A) macht Stufe B nicht unerkennbar. Sie führt höchstens zu „mittel“.

**Überschneidung von Objektlisten**
- Maßgeblich ist der Anteil der Objekte, die **auf beiden Seiten belegt** sind, bezogen auf die Objekte der kürzeren Seite
  und auf die der längeren Seite.
- Nur namentlich oder adressmäßig belegte Objekte zählen. Eine „mögliche“ Entsprechung (z. B. Schulgebäude gegenüber zugehöriger
  Sporthalle) wird in der Begründung vermerkt, zählt aber nicht.

## Schritt 2: Urteil ableiten

| Urteil | Bedingung | Sicherheit |
|---|---|---|
| **objektgleich** | Stufe B erkennbar und übereinstimmend. Kein Widerspruch in A oder B. Objektlisten (soweit vorhanden) nahezu deckungsgleich oder auf einer Seite nicht aufgeführt. | **hoch:** mindestens zwei A-Merkmale stimmen überein (Regeln zu Einzelstandort und Fläche beachten). **mittel:** sonst. |
| **teilmenge** | Die kürzere Objektliste ist zu mindestens **50 %** auch auf der längeren belegt, die längere enthält weitere Objekte, und die kürzere Seite schließt nichts ausdrücklich aus. | – |
| **nicht objektgleich** | Mindestens ein klarer Widerspruch in A oder B: andere Adresse, anderer Stadtteil, andere Objektart, andere Leistungsart, **oder** gemeinsame Objekte machen weniger als **20 %** der Objekte jeder Seite aus. | – |
| **unklar** | Stufe B ist auf mindestens einer Seite nicht erkennbar, **oder** die Überschneidung der Objektlisten liegt zwischen 20 % und 50 % ohne klare Teilmenge. Sind beide Seiten unspezifisch („diverse Objekte“), ist „unklar“ das höchste erreichbare Urteil. | – |

**Rangfolge bei Zweifel (vorsichtig vor weniger vorsichtig):** nicht objektgleich, dann unklar, dann teilmenge, dann
objektgleich (mittel), dann objektgleich (hoch).

Begründungen:
- **Andere Leistungsart gilt als Widerspruch.** Dasselbe Gebäude mit Glasreinigung statt Unterhaltsreinigung ist ein anderer Vertrag.
- **Teilmenge ist ein eigenes Urteil**, weil für die Prognose zählt, ob dasselbe Objekt wiederkehrt. Ein Teil davon ist nicht dasselbe wie das Ganze.
- **Die Sicherheitsstufe zeigt, wie viel ein Urteil trägt.** „Objektgleich (mittel)“ beruht auf Gebiet, Objektart und Leistung, aber nicht auf belegter Identität.

## Schritt 3: Tendenz bei „unklar“

Bei jedem Urteil „unklar“ wird zusätzlich eine **Tendenz** notiert: **eher dafür** (dasselbe Objekt), **eher dagegen** oder **keine**.
- Grundlage sind dieselben inhaltlichen Merkmale (A bis C), **nie der Zeitabstand**.
- Die Tendenz ersetzt das Urteil nicht und fließt nicht in die Hauptquote ein.
- Sie wird in einem Satz begründet.

## Schritt 4: Begründung notieren

Ein Satz mit Feld und Wert. Beispiel:

> Beide: Wuppertal-Uellendahl, Schulen/Kitas/Sporthallen/Verwaltung, Fenster- und Innenglasreinigung, CPV 90911300.
> Umfang nur 2022 genannt (32 Liegenschaften) → objektgleich, mittel.

## Schritt 5: Auswertung als Spanne

| Variante | Zählt als Treffer | Zählt als Fehler | Ausgeschlossen |
|---|---|---|---|
| **streng** | objektgleich (hoch) | alles andere, auch unklar | – |
| **breit** | objektgleich (hoch und mittel) und teilmenge | nicht objektgleich | unklar |
| **Zusatz mit Tendenz** | breit, plus „unklar, eher dafür“ | nicht objektgleich und „unklar, eher dagegen“ | „unklar, keine Tendenz“ |

Liegen streng und breit nah beieinander, ist das Ergebnis belastbar. Weichen sie stark ab, hängt die Aussage an den Zweifelsfällen.
Zusätzlich berichten: Anzahl je Urteil, Anzahl „unklar“ mit Tendenz. Die Variante mit Tendenz ist eine Zusatzinformation und
nicht die Hauptaussage.

## Urteilsvorlage je Paar

```
Paar: <Nr>
Alt:  <Link>       Neu: <Link>
A (Identität):  <übereinstimmend / widersprüchlich / abweichend / mehrdeutig / nicht vergleichbar>  Details: ...
B (Objektraum): <erkennbar und übereinstimmend / widersprüchlich / nicht erkennbar>               Details: ...
C (Stütze):     Auftraggeber <ja/nein>, CPV <ja/nein>, Titel <ähnlich/anders>, Losstruktur <gleich/anders>
Überschneidung der Objekte: <x von y gemeinsam, bezogen auf die kürzere Seite> (falls Listen vorhanden)
Lose mit Überschneidung: <Nummern> (falls mehrere Lose)
Urteil: <objektgleich | teilmenge | nicht objektgleich | unklar>   Sicherheit: <hoch | mittel | –>
Tendenz (nur bei unklar): <eher dafür | eher dagegen | keine>
Begründung: ...
```

## Kalibrierungsbeispiele (zählen nicht zur Prüfung)

Acht Paare, an denen die Regeln entstanden sind. Sie gehören nicht zur Blindprüfung. Sollte eines davon unter den 20 Prüfpaaren
sein, wird es dort **nicht** gezählt, weil das Urteil nicht mehr unabhängig wäre. Zwei Beispiele (Wuppertal, Berlin) wurden anhand
von Screenshots eingestuft, die übrigen anhand des kopierten Textes. Die Originale wurden nicht noch einmal geprüft.

| Paar | Alt (Zuschlag oder frühere Bekanntmachung) | Neu | Urteil | Was der Fall lehrt |
|---|---|---|---|---|
| Wuppertal | 202519-2022 | 530979-2026 | objektgleich, mittel | Identität nur über Stufe B belegt, Umfang nur auf einer Seite |
| Berlin (BGW) | 509902-2022 | 574953-2026 | objektgleich, hoch | Teilflächen auf zwei Nachkommastellen gleich, Geschosse gleich; Tippfehler von 1 m² ist kein Widerspruch |
| Stade/Harburg | 306431-2026 | 656958-2026 | nicht objektgleich | Stufe C komplett gleich, aber Standort, Landkreis, Nebenliegenschaften und Fläche widersprechen |
| Stralsund | 569523-2019 | 599457-2026 | teilmenge | Eine Seite zählt sieben Objekte auf, die andere nur eines, das darin vorkommt |
| Düsseldorf | 327439-2022 | 457874-2026 | objektgleich, mittel | Einzelstandort: Die Adresse allein trägt kein „hoch“ |
| Esslingen | 436672-2026 | 595492-2026 | unklar, Tendenz eher dagegen | Wortgleiche Verfahrenstexte, Flächen weichen ab, Objektart einseitig erkennbar, Losschnitt anders |
| Saarbrücken | 442059-2026 | 644509-2026 | nicht objektgleich | Identische Verfahrenstexte, aber höchstens ein Objekt gemeinsam |
| Springe | 390156-2023 | 623928-2026 | unklar, Tendenz eher dafür | Beide Seiten „diverse Objekte“, Fläche mehrdeutig, Los- und Kriterienschnitt ähnlich |

Kurz zu drei Fällen:

**Berlin (objektgleich, hoch).** Beide: Spichernstraße 2-3, Erdgeschoss bis 3. Obergeschoss, HNF/NNF/VF identisch (2.456,32 /
972,18 / 1.031,34 m²), Unterhalts-, Grund- und einseitige Glasreinigung. Die Adresse zählt bei diesem Einzelstandort nicht als eigenes
Merkmal. Fläche und Geschosse sind trotzdem zwei übereinstimmende A-Merkmale. Der CPV-Code weicht ab (90919200 gegenüber 90911200),
das ist Stufe C und kein Widerspruch.

**Stralsund (teilmenge).** 2019: sieben Objekte (Meeresmuseum, Ozeaneum, Nautineum, Natureum, Burmeisterhaus, Neue Badenstraße 4,
Türmchenspeicher) und zehn Leistungen. 2026: nur das Ozeaneum (Hafenstraße 11) und vier Leistungen. Die kürzere Seite ist zu 100 %
in der längeren enthalten, nichts wird ausdrücklich ausgeschlossen. Alternative Lesart: objektgleich (mittel), falls 2026 nur den
Hauptstandort nennt. Bei Zweifel gilt nach der Rangfolge das vorsichtigere Urteil.

**Springe (unklar, eher dafür).** Beide: Stadt Springe, „diverse Objekte“ ohne Liste, Unterhalts-, Grund- und Glasreinigung.
Fläche mehrdeutig (Reinigung 52.500 gegenüber 63.400 m²; mit Glas 62.500 oder 60.500 gegenüber 63.400 m²), Losstruktur 7
gegenüber 3 (Stufe C). Weil beide Seiten unspezifisch sind, ist „unklar“ das höchste erreichbare Urteil. Die inhaltlichen Hinweise
(gleiche Stadt, gleicher Beschaffungsdienstleister, gleiche Optionsformel, fast gleiche Kriterien, Gesamtfläche mit Glas 1,4 %
auseinander) sprechen eher dafür.

## Hinweise für Phase 3 (kein Teil der Urteilsregeln)

Beobachtungen aus der Kalibrierung. Sie sind Interpretationen und nicht Teil der Urteilsregeln.

- **Stufe-C-Merkmale trennen Schwesterverfahren nicht.** Auftraggeber, Titel, CPV, Optionstext und Zuschlagskriterien sind bei
  Stade/Harburg, Esslingen und Saarbrücken identisch, obwohl es verschiedene Vorhaben sind. Ein Score darf sich nicht darauf stützen.
- **Objekte, Adressen und Flächen sind die tragenden Merkmale.** Sie stehen meist nur im Freitext der Losbeschreibungen und müssen
  extrahiert werden (Objektlisten als Mengen, Flächen mit Toleranz, Zuordnung auf Los-Ebene).
- **Der Zeitabstand ist höchstens ein grober Ausschluss** (die neue Ausschreibung darf nicht lange vor dem Ende des Vorgängers
  liegen), nie ein Score-Merkmal. Sonst misst der Backtest später nur, was der Matcher vorgegeben hat.
- **Ältere Bekanntmachungen enthalten Verweise auf frühere Verfahren** (z. B. unter IV.2.1). Das kann als Verbindungsschlüssel
  dienen (A9, A11).
- **Ist der Vorgänger eine Auftragsbekanntmachung**, sollte die zugehörige Zuschlagsbekanntmachung gesucht werden. Sonst beruhen
  Laufzeit und Verlängerung auf einem Plan und nicht auf dem tatsächlichen Vertrag.
- **Mit Platzhaltern ist zu rechnen:** Auftragswert 1,00 EUR, „nicht veröffentlicht“, „Beliebiger Ort“ als Erfüllungsort.

## Grenzen

- Ein klares Urteil bezieht sich auf **zwei Texte**, nicht auf die Wirklichkeit. Dass zwei Bekanntmachungen dasselbe Objekt
  beschreiben, heißt nicht zwingend, dass es sich um denselben Nachfolgevertrag handelt.
- **20 Paare sind wenig.** Bei 16 richtigen von 20 (80 %) reicht das 95-%-Intervall grob von 58 bis 92 %. Die Quote ist ein Hinweis, kein Beweis.
- Ein zweiter Beurteiler mit denselben Regeln (Kommilitone, Bekannter) erhöht die Aussagekraft. Aus der Übereinstimmung beider
  Urteile lässt sich ablesen, ob die Regeln eindeutig genug sind. Wo sie abweichen, liegt es meist an den Regeln und nicht an einer Person.
- Die Schwellen (2 % Fläche, 20 % und 50 % Überschneidung) sind begründete Setzungen und nicht aus Daten abgeleitet. Sie wurden an
  acht Paaren kalibriert. Randfälle werden als „unklar“ oder „teilmenge“ notiert und in der Auswertung genannt, nicht nachträglich umdefiniert.

## Änderungsprotokoll

**Version 1.1 (2026-10-24), vor der ersten echten Beurteilung.** Gegenüber Version 1 neu:
- Stufe C: abweichende Werte sind kein Widerspruch, Übereinstimmung gleicht keinen Widerspruch aus (Stade/Harburg)
- Abweichende Anschrift des Beschaffers bei gleicher Körperschaft ist kein Widerspruch (Berlin)
- Teilmenge bei Objektlisten (Stralsund), mit Schwellen von 50 % und 20 % zur Abgrenzung (Saarbrücken)
- Einzelstandorte: Adresse allein zählt nicht als Merkmal (Düsseldorf)
- Fläche: 2-%-Toleranz, abweichend ist kein Widerspruch (Esslingen); gleiche Flächenart, Mehrdeutigkeit (Springe)
- Erkennbarkeit von Stufe B und unspezifische Beschreibung (Esslingen, Springe)
- Losstruktur gehört in Stufe C (Springe); mehrere Lose werden in der Begründung vermerkt (Saarbrücken)
- Tendenz bei „unklar“ als Zusatzspalte (Springe); Auswertung mit Zusatzzeile
- „Geschosse oder Gebäudeteile“ als A-Merkmal (Berlin); Laufzeiten und Auftragswert stehen unter „Nicht verwenden“
- Acht Kalibrierungsbeispiele statt einem
