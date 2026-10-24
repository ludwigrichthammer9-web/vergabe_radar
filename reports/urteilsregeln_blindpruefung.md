# Urteilsregeln für die Blindprüfung der Zuordnung

**Version 2, 2026-10-24.** Gilt für die Blindprüfung in Iteration 3 (20 Paare aus Zuschlag und möglicher Neuausschreibung).

_Änderung gegenüber Version 1 (Entscheidung des Nutzers, vor dem ersten eingetragenen Urteil des Nutzers):_ Zwei Klarstellungen
unter „Hinweise zum Vergleich“ (Stufe C ist weder Widerspruch noch Ausgleich; abweichende Anschrift des Beschaffers). Grund: Ein
abweichender CPV, Name oder Titel sollte nicht als Widerspruch gelten, und eine Übereinstimmung in Stufe C darf einen Widerspruch in
A oder B nicht aufwiegen. Version 1 ist in Git erhalten (Commit eff8f55). Der Subagent hat die 20 Paare nach Version 1 beurteilt
(`blindpruefung_iteration3_agent.md`); die neuen Zeilen präzisieren nur, sie ändern keine Urteilsstufe.

## Zweck

Ein Mensch beurteilt, ob zwei Bekanntmachungen **dasselbe Objekt** betreffen. Das Urteil soll nachvollziehbar sein
und von der Prognose selbst unabhängig bleiben. Damit lässt sich später belegen, wie zuverlässig die automatische
Zuordnung (Annahme A9) ist.

## Spielregeln

1. **Diese Regeln stehen vor dem ersten echten Paar fest** und werden committet. Nach dem ersten Urteil werden sie nicht mehr
   geändert. Wer sie ändern will, legt eine neue Version mit Datum und Grund an und beurteilt **alle** Paare neu.
2. Es werden **nur die beiden Bekanntmachungen** der Paare geöffnet. Keine anderen Reports von Iteration 3, kein Lösungsschlüssel.
3. **Zeitabstand und Vertragsende werden nicht berücksichtigt.** Dass die zweite Ausschreibung zeitlich passt, ist genau das,
   was das Projekt erst belegen will. Als Argument würde es einen Zirkelschluss erzeugen.
4. **Jedes Urteil bekommt eine Begründung** mit Feld und Wert (ein Satz).
5. **„Unklar“ ist ein gültiges Urteil.** Nicht raten, um eine klare Zahl zu erhalten.
6. Bei Unsicherheit zwischen zwei Urteilen gilt das **vorsichtigere** (siehe Rangfolge unten).

## Schritt 1: Merkmale vergleichen

| Stufe | Merkmale | Aussagekraft |
|---|---|---|
| **A: Identität** | Adresse oder Liegenschaftsliste, Gebäudename, Fläche in m², Anzahl Gebäude | Legen ein Objekt eindeutig fest. Nur hier ist ein sicheres Urteil möglich. |
| **B: Objektraum** | Stadtteil oder Gebiet, Objektarten (z. B. Schulen, Verwaltung), Leistungsart (Unterhalt, Glas, Grund) | Grenzen das Objekt ein, machen es aber nicht eindeutig. |
| **C: Stütze** | gleicher Auftraggeber, gleicher CPV-Code, ähnlicher Titel | Reichen allein nie. Sie machen ein Urteil nur plausibler. |
| **Nicht verwenden** | Zeitabstand, Vertragsende, Verlängerungsoption | Würde das Projektziel selbst voraussetzen. |

Hinweise zum Vergleich:
- Abweichende Namen desselben Auftraggebers (andere Abteilung, andere Schreibweise) sind **kein** Widerspruch, solange die Stadt
  oder Körperschaft dieselbe ist.
- Eine andere **Vertragsform** (Einzelvertrag gegenüber Rahmenvereinbarung) ist kein Widerspruch zum Objekt.
- Ein abweichender Wert in **Stufe C** (CPV, Name, Titel) ist kein Widerspruch. Eine Übereinstimmung in Stufe C gleicht einen
  Widerspruch in Stufe A oder B nicht aus.
- Eine abweichende **Anschrift des Beschaffers** (Sitz der Vergabestelle) bei gleicher Körperschaft ist kein Widerspruch.
  Maßgeblich ist der Ort der Leistung, nicht die Adresse des Auftraggebers.
- Details, die nur in **Anlagen** stehen (Flächenverzeichnis, Leistungsverzeichnis), die man nicht einsehen kann, zählen als nicht vergleichbar.

## Schritt 2: Urteil ableiten

| Urteil | Bedingung | Sicherheit |
|---|---|---|
| **objektgleich** | Stufe B stimmt vollständig überein, und weder in A noch in B gibt es einen Widerspruch | **hoch:** mindestens 2 Merkmale aus A stimmen überein. **mittel:** A fehlt oder ist nicht vergleichbar, nur B stimmt. |
| **teilmenge** | Eine Seite beschreibt erkennbar mehr oder weniger Objekte (andere Zahl Liegenschaften, Teilgebiet, einzelne Lose), und die Schnittmenge ist belegbar | – |
| **nicht objektgleich** | Mindestens ein Merkmal aus A oder B widerspricht klar: andere Adresse, anderer Stadtteil, andere Objektart, andere Leistungsart | – |
| **unklar** | Stufe B ist nicht vollständig erkennbar (z. B. nur „Gebäudereinigung für das Landratsamt“), oder die Objektangaben stehen nur in Anlagen | – |

**Rangfolge bei Zweifel (vorsichtig nach vorsichtiger):** nicht objektgleich vor teilmenge vor objektgleich (mittel) vor
objektgleich (hoch). „Unklar“ gilt, wenn weder ein Widerspruch noch eine Übereinstimmung der Stufe B belegbar ist.

Begründungen zu den Urteilen:
- **Andere Leistungsart gilt als Widerspruch.** Dasselbe Gebäude mit Glasreinigung statt Unterhaltsreinigung ist ein anderer Vertrag.
- **Teilmenge ist ein eigenes Urteil**, weil für die Prognose zählt, ob dasselbe Objekt wiederkehrt. Ein Teil davon ist nicht dasselbe wie das Ganze.
- **Die Sicherheitsstufe zeigt, wie viel ein Urteil trägt.** „Objektgleich (mittel)“ beruht auf Gebiet und Leistung, aber nicht auf belegter Identität.

## Schritt 3: Begründung notieren

Ein Satz mit Feld und Wert. Beispiel:

> Beide: Wuppertal-Uellendahl, Schulen/Kitas/Sporthallen/Verwaltung, Fenster- und Innenglasreinigung, CPV 90911300.
> Umfang nur in der Bekanntmachung von 2022 genannt (32 Liegenschaften) → objektgleich, mittel.

## Schritt 4: Quote als Spanne berichten

| Variante | Zählt als Treffer | Zählt als Fehler | Ausgeschlossen |
|---|---|---|---|
| **streng** | objektgleich (hoch) | alles andere, auch unklar | – |
| **breit** | objektgleich (hoch und mittel) und teilmenge | nicht objektgleich | unklar |

Liegen beide Werte nah beieinander, ist das Ergebnis belastbar. Weichen sie stark ab, hängt die Aussage an den Zweifelsfällen.
Zusätzlich berichten: Anzahl je Urteil, davon unklar.

## Urteilsvorlage je Paar

```
Paar: <Nr>
Alt:  <Link>       Neu: <Link>
A (Identität):  <übereinstimmend / widersprüchlich / nicht vergleichbar>  Details: ...
B (Objektraum): <übereinstimmend / widersprüchlich / teils>               Details: ...
C (Stütze):     Auftraggeber <ja/nein>, CPV <ja/nein>, Titel <ähnlich/anders>
Urteil: <objektgleich | teilmenge | nicht objektgleich | unklar>   Sicherheit: <hoch | mittel | –>
Begründung: ...
```

## Kalibrierungsbeispiel (zählt nicht zur Prüfung)

Zur Einordnung der Regeln an einem Fall, der nicht zu den 20 Paaren gehören muss. Eingestuft anhand von Screenshots,
nicht anhand der Originale.

| Merkmal | 202519-2022 (Fenster- und Glasreinigung Uellendahl) | 530979-2026 (Rahmenvereinbarung Fenster- und Innenglasreinigung Uellendahl) | Befund |
|---|---|---|---|
| Auftraggeber | Stadt Wuppertal, Gebäudemanagement | Stadt Wuppertal (Beschaffer), Zentrale Vergabestelle | gleiche Stadt, andere Abteilung |
| Titel | Fenster- und Glasreinigung in Wuppertal-Uellendahl | Rahmenvereinbarung Fenster- und Innenglasreinigung in Wuppertal Uellendahl | fast wortgleich |
| CPV | 90911300 | 90911300 | gleich |
| Gebiet | Wuppertal-Uellendahl | Wuppertal-Uellendahl, PLZ 42285 | gleich |
| Objektarten | Schulen, Tagesstätten, Sporthallen, Verwaltungen | Verwaltungen, Schulen, Kitas, Sporthallen | gleich |
| Leistung | Fenster- und Innenglasflächen | Fenster- und Innenglasreinigung | gleich |
| Umfang | 32 Liegenschaften, ca. 22 Tsd. m² Glasfläche | nicht angegeben (nur Höchstwert 290.000 €) | nicht vergleichbar |
| Vertragsform | Einzelvertrag, 3 Jahre, Option +12 Monate | Rahmenvereinbarung, 36 Monate, 1 Verlängerung | anders, kein Widerspruch |

**Urteil: objektgleich, Sicherheit mittel.** Stufe B stimmt überein, nichts widerspricht, Stufe A ist nicht vergleichbar, weil das
Flächenverzeichnis eine Anlage ist. Unter der strengen Variante wäre das ein Fehler, unter der breiten ein Treffer.

## Grenzen

- Ein klares Urteil bezieht sich auf **zwei Texte**, nicht auf die Wirklichkeit. Dass zwei Bekanntmachungen dasselbe Objekt
  beschreiben, heißt nicht zwingend, dass es sich um denselben Nachfolgevertrag handelt.
- **20 Paare sind wenig.** Bei 16 richtigen von 20 (80 %) reicht das 95-%-Intervall grob von 58 bis 92 %. Die Quote ist ein Hinweis, kein Beweis.
- Ein zweiter Beurteiler mit denselben Regeln (Kommilitone, Bekannter) erhöht die Aussagekraft. Aus der Übereinstimmung der beiden
  Urteile lässt sich ablesen, ob die Regeln eindeutig genug sind. Wo sie abweichen, liegt es meist an den Regeln und nicht an einer Person.
- Die Regeln können in Randfällen (Fusion von Auftraggebern, geänderter Zuschnitt der Lose) an Grenzen stoßen. Solche Fälle werden
  als „unklar“ oder „teilmenge“ notiert und in der Auswertung genannt, nicht nachträglich umdefiniert.
