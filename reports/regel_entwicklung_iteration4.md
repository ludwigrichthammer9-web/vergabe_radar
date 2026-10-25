# Regelentwicklung Iteration 4 (nur Entwicklungsdaten Q2 und Q3 2026)

Stand: 2026-10-25. Code: [src/zuordnung_los.py](../src/zuordnung_los.py), [src/los_merkmale.py](../src/los_merkmale.py),
[src/population_iteration4.py](../src/population_iteration4.py). Läufe: [Q3](regel_entwicklung_iteration4_lauf_q3.txt) (gegen die Handsuche
aus Iteration 3), [Q2](regel_entwicklung_iteration4_lauf_q2.txt) (40 Zufallsfälle, Seed 20261025, ohne Maßstab).

**Die Testdaten (Q1 2026) wurden bis zum Einfrieren nicht angesehen.** Der Kandidatenpool enthält Q1-2026-Ausschreibungen als mögliche
Vorgänger. 20 davon erschienen in den Entwicklungsläufen als Kandidat oder Vorschlag und stehen in
[dev_gesehene_q1_notices.txt](dev_gesehene_q1_notices.txt). Sie werden nicht als Testfall gezogen (Festlegung in `docs/iterationen.md`).

## Eingefrorene Regel

**Merkmale je Los** (`los_merkmale.py`): Leistungsart (aus Lostitel, sonst Verfahrenstitel, sonst Beschreibung ohne „fachfremd“, sonst
CPV des Loses), Flächen mit Art (Boden/Glas), Adressen (Straße + Hausnummer), Objektnamen (Typwort + großgeschriebener Eigenname,
zusammengesetzte Namen mit eigener Vorsilbe, Einzelobjekte wie Rathaus). eForms aus den API-Feldern mit Los-Texten (BT-21, BT-24, BT-728),
vor eForms aus der XML (OBJECT_DESCR).

**Kandidaten**: Auftraggeber ähnlich (wie Iteration 3), gleiche PLZ, ein seltenes gemeinsames Namenswort (≤ 50 Pool-Notices) oder Treffer
der Volltextsuche (bis zu 6 Namen/Adressen, `FT~"…"`, CPV 909, vor dem Fall). Vor eForms höchstens 40 XML je Fall.

**Vergleich** (Logik der Urteilsregeln 1.1, kein Zeitabstand):

| Prüfung | Regel |
|---|---|
| Widerspruch | Kernarten (Unterhalt, Glas, Treppenhaus, Bau) ohne Schnittmenge; Kandidat nur Bau; „fachfremd“ im Titel des Kandidaten (Schädlinge, Fahrzeuge, Wäsche, Winterdienst); PLZ beider Seiten disjunkt (je ≤ 2) |
| Identität | Objektnamen ∪ Adressen; bei ≥ 15 Kandidaten ohne Merkmale, die bei ≥ 4 und ≥ 40 % der Kandidaten vorkommen |
| Ortsbezug | Auftraggeber ähnlich, gemeinsame PLZ oder Orte, oder gemeinsamer Name, dessen Eigenname einen Ort des Falls nennt |
| „objekt“ | kein Widerspruch, Ortsbezug, gemeinsame Identität ≥ 50 % der kürzeren Seite |
| „geschwister“ | Auftraggeber ähnlich, beide mit Objekten, Überschneidung < 20 % beider Seiten, keine gleiche Fläche |
| Rangliste (W6) | „objekt“ und „unklar“ nach Punkten (3·r_kurz + r_lang + 1,5·Fläche + 0,5·Straße + 0,7·Auftraggeber + 0,5·Titelwörter + 1·Volltext, −1 ohne Ortsbezug), höchstens 3 |
| Vorschlag (W2/W3) | jüngster „objekt“-Kandidat mit höchstens 1,5 Punkten unter dem besten |

## Entwicklungsverlauf auf Q3 (Fakten)

Maßstab: Handsuche aus Iteration 3 (alte, großzügigere Definition; 38 Fälle mit Vorgänger, T16 jetzt außerhalb der Population).
„Unbekannt“ = Vorschlag, den die Handsuche nicht nennt.

| Lauf | Änderung | Vorschläge (korrekt / falsch bekannt / unbekannt) | Trefferquote | Top 3 |
|---|---|---|---|---|
| 1 | erste Fassung | 32 (19 / 2 / 11) | 19/38 = 50,0 % | 24/38 = 63,2 % |
| 2 | Ortsbezug Pflicht; Gebietswiderspruch (PLZ); fachfremde Leistungen; Häufigkeitsfilter; allgemeine Vorsilben; jüngster starker Treffer | 22 (18 / 0 / 4) | 47,4 % | 63,2 % |
| 3 | Häufigkeitsfilter nur ab 15 Kandidaten (Einzelstandorte); Ortsbezug über Namen | 24 (20 / 0 / 4) | 52,6 % | 63,2 % |
| 4 | Muster für Fahrzeugreinigung; Leistungsart aus Verfahrenstitel | unverändert | 52,6 % | 63,2 % |
| 5 | „fachfremd“ nur aus Titeln; „Gebäudereinigung“ = Unterhalt; Volltexttreffer in der Rangliste | 25 (20 / 0 / 5) | 52,6 % | 68,4 % |
| 6 | Ortsbezug über Namen nur mit Ortswort des Falls | 25 (21 / 0 / 4) | 55,3 % | 68,4 % |
| 7 | „Bad“ kein Typwort; fachfremd im Titel schließt immer aus; Vorsilben Ein-/Zwei-/Drei-/Vierfeld | unverändert | 55,3 % | 68,4 % |
| 8 | mehr Kandidaten (40 XML, 6 Suchbegriffe, seltene Namenswörter) | 25 (21 / 0 / 4) | 55,3 % | 68,4 % |

Lauf 8 = eingefrorene Fassung. Präzision auf Q3: **untere Grenze 84,0 %** (unbekannt = falsch), obere 100 %. Die 4 unbekannten Vorschläge
(T2 Freiburg Mozartstraße 58, T11 WISTA, T32 Ludwigslust 2020, T53 Leipzig 2022) sind nach Einschätzung von Claude eher objektgleiche ältere
Verfahren bzw. Teilmengen; T11 ist unsicher.

Verbleibende Lücken auf Q3 (Lauf 8): 6 Vorgänger sind gar nicht unter den Kandidaten (T4, T21, T41, T55, T57; T23 teilweise), 4 werden
fälschlich ausgeschlossen (T23, T37 als Geschwister, T55 ohne Objekte und mit Namenswechsel), 5 Fälle nennen auf einer Seite keine Objekte
(T10, T12, T19, T34, T42; nach den Urteilsregeln höchstens „unklar“).

## Prüfung auf Q2 (40 Zufallsfälle, Urteil Claude)

Lauf 1 (Stand Lauf 6 auf Q3): 22 Vorschläge, davon nach Einschätzung 15 korrekt, 5 falsch, 2 unklar. Die Fehler „Bad“ als Typwort (2),
Fahrzeugreinigung (1) und „Dreifeldsporthalle“ (1, unklar) führten zu Lauf 7. Eingefrorene Fassung (Lauf 3 auf Q2):

| Urteil (Claude) | Anzahl | Fälle |
|---|---|---|
| eher korrekt | 14 | u. a. Grundschule Pölling, Martin-Luther-Schule Marburg, FA Würzburg, NDR Rothenbaum, Rathaus Neukölln, Kasinoschule, Polizei Bamberg, Neuenkirchen-Vörden, Goldsteinschule (2017), Behördenzentrum Lüneburg |
| falsch | 2 | Klinikum Nürnberg Süd (Neubau Kinderklinikum gegenüber Großküche, gleicher Standortname); Polizeipräsidium Einsatz Göppingen gegenüber Mainz (gleicher Behördenname, keine PLZ im Fall) |
| unklar | 1 | BImA Ober-/Niederbayern (gemeinsame Adressen, Leistungsart des Kandidaten unsicher) |

Damit etwa **14/17 = 82 %**. Bad Frankenhausen (zuvor korrekt) fällt in der eingefrorenen Fassung weg.

## Einschätzung (Interpretation)

- Die Regel ist auf Q3 abgestimmt; die Zahlen dort sind **optimistisch**. Q2 deutet auf eine Präzision um 80 % hin, mit großer
  Unsicherheit (n = 17, Urteil von Claude, keine Handsuche).
- Die **Trefferquote** liegt auf den Entwicklungsdaten bei 55 % und damit unter der Schwelle von W3 (60 %). Die Rangliste (W6) liegt mit
  68 % knapp unter 70 %. Für den Test ist eher weniger zu erwarten. Die verbleibenden Lücken liegen vor allem in der Kandidatensuche
  (Namenswechsel, große Auftraggeber) und bei Fällen ohne Objektangaben, die nach den Urteilsregeln ohnehin höchstens „unklar“ sind.
- Weitere Änderungen brachten zuletzt keine Verbesserung (Läufe 7 und 8). Die Abstimmung auf Q3 gilt als ausgereizt.
- Bekannte Grenzen: Beispielobjekte, die nur in Feldern außerhalb der API stehen (Hürth); gleiche Behörden- oder Standortnamen in
  verschiedenen Städten ohne PLZ im Fall (Göppingen/Mainz); Objekte innerhalb eines großen Standorts (Klinikum).
