# Regelentwicklung Iteration 3 (nur Entwicklungsdaten Q2 2026)

Stand: 2026-10-23. Code: `src/objekt_merkmale.py`, `src/zuordnung_objekt.py`, `src/population_iteration3.py`.
Letzter Entwicklungslauf: [regel_entwicklung_iteration3_lauf.txt](regel_entwicklung_iteration3_lauf.txt)
(`zuordnung_objekt.py --dev`, 40 Zufallsfälle mit Seed 20261023 plus 9 bekannte Fälle aus Iteration 2).

**Die Testdaten (Q3 2026) wurden bis zum Einfrieren nur geladen und nicht angesehen.**

## Eingefrorene Parameter

- Kandidaten: Auftraggeber ähnlich (gleicher Name, Jaccard der Namenswörter ≥ 0,6 oder Überlappung ≥ 0,8 bei mindestens 2 Wörtern)
  oder (eForms) gleiche PLZ und gemeinsame Straße oder gemeinsames Wort. Vor eForms höchstens 25 Kandidaten mit XML (bevorzugt gleicher
  Ort, dann jüngste).
- Objektwörter: Titel- und Ortswörter ohne Allerweltswörter (`GENERIC`, alle Wörter mit „reinigung“) und ohne Namen und Sitz des
  Auftraggebers.
- Stufe T: Auftraggeber ähnlich und wortgleicher Titel. Stufe A: gleiche Straße und gleiche PLZ und ≥ 1 gemeinsames Objektwort.
  Stufe B: Auftraggeber ähnlich und (≥ 2 gemeinsame Objektwörter oder Jaccard ≥ 0,67). Rangfolge T > A > B > Wortähnlichkeit > jünger.
  1:1-Zuordnung, kein Zeitfenster.

## Entwicklungsverlauf (Fakten)

| Lauf | Änderung | Beobachtung auf den Entwicklungsdaten (Urteil Claude) |
|---|---|---|
| 1 | erste Fassung | Viele Fehlzuordnungen über Typwörter (UHR, Grundschule), Namen/Sitz des Auftraggebers (Neumarkt, München), lange Straßen (Gutleutstraße) |
| 2 | Typwörter allgemein; Auftraggebername/-sitz aus dem Vergleich; Stufe A braucht PLZ und Wort; Stufe T; Überlappungsmaß für Namen | Frankfurter Schulverwechslungen weg; Fehler LfF München → LfF Augsburg, JKI Quedlinburg → JKI Braunschweig |
| 3 | Wortähnlichkeit ≥ 0,67; Wörter mit „reinigung“ und Justiz-Organisationswörter allgemein | 12 von 40 Zufallsfällen zugeordnet, davon nach Einschätzung etwa 10–11 plausibel; 1 unklar (Mayen-Koblenz, wortgleicher allgemeiner Titel) |

Bekannte Fälle aus Iteration 2 (Lauf 3): gefunden A2 Wenden, A13 Bezirk Oberbayern, A16 WZB, A24 Polizeirevier Ost; nicht gefunden
A8 DPMA (Auftraggebername geändert) und A30 JKI Quedlinburg (Ort = Sitz des Auftraggebers wird herausgefiltert). Bei A3/A19
(Frankfurter Schulen) kein Vorschlag.

## Einschätzung

- Die Regel ist bewusst vorsichtig: lieber kein Vorschlag als ein falscher. Die Trefferquote (V3) ist deshalb das größere Risiko.
- Die Urteile auf den Entwicklungsdaten stammen von Claude und sind auf diese Fälle hin abgestimmt, also optimistisch. Maßgeblich
  sind nur die Testdaten.
