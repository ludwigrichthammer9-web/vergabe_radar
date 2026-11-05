# Evaluation Iteration 9 (Gesamtprüfung durch den Subagenten `evaluator`, 2026-11-05)

_Gekürzte Wiedergabe des Berichts des Evaluators (Lesezugriff, kein Git). Die Urteile stammen vom Evaluator; Einordnungen des Projekts stehen in `docs/iterationen.md` (Nachtrag und Ergebnis Iteration 9)._

Gelesen: Kriterien in `docs/iterationen.md`, Auswertung, Auswertungsskript, Rohantworten, Protokolle, Entscheide, Evaluator-Lesung, Blatt des Kommilitonen, Aufgabe Teil 1, Lauf-Skript, `pruefung_rohtext.md`, `.git/logs/HEAD`.

## Urteil je Kriterium
| Kriterium | Urteil | Beleg |
|---|---|---|
| V1 Ende GL, 70 Z-Lose, ≥ 63/70 | erfüllt, mit Vorbehalt | 66/70 = 94,3 %; Abweichungen N7, N32, N39, N108 |
| V2 R und M, 30 Lose, ≥ 24/30 | erfüllt (R nur 2 Lose statt 10) | 28/30 = 93,3 %; Abweichungen N5, N79 |
| V3 neue Fassung nicht schlechter | formal erfüllt, kaum aussagekräftig | 66/70 gegen 65/70 |
| V4 Höchstende ≥ 90 % und ≥ 85 % | **verfehlt** (erste Schwelle); zweite knapp erfüllt | 61/70 = 87,1 %; 52/61 = 85,2 % |
| V5 Einigkeit A und B ≥ 90 % | erfüllt, geringe Aussagekraft | 110/110 |
| V6 Kommilitone ≥ 13/15 | erfüllt, statistisch dünn | 14/15; Abweichung N48 |
| V7 kein Los ohne Zuschlag | **verfehlt (formal)** | N51, Leser B meldet „kein Zuschlag“ |
| V8 Verfahren | nicht beurteilbar bis teilweise erfüllt („im Kern ja, mit dokumentierten Lücken“) | siehe unten |

## V8
Belegt: Commit-Reihenfolge (Regeln a03a4a8, Seed und Skript 4521952, Stichprobe, Rohtexte, Anweisung, Auswertungsskript b3b1471 vor den Antworten e1726e7); Schlüssel-Hash im Commit; Kriterium nicht nachträglich geändert.
Nicht belegt oder abweichend: Lauf-Skript wahrscheinlich nicht vor den Antworten committet; Abweichung vom Plan (Skriptläufe statt Sitzungen im Fenster) nicht in `iterationen.md`; für Teil 1 und 2 von Leser A kein Nachweis im Repo; Protokoll prüft nur Eltern-Ordner, nicht `~/.claude`; Pakete (ZIP) nicht versioniert; Bedingungen der Teile unterschiedlich (interaktiv gegen Skript, `--effort high`).
Nach den vorab festgelegten Folgen hieße V8 „nein“: Schritt wiederholen. Das wäre unverhältnismäßig, bevor die Lücken benannt sind.
_Nachtrag des Projekts (bff5b6e):_ Abweichung, V4, V7, N57 und die Paketprüfung (230 Dateien byte-gleich) sind in `docs/iterationen.md` nachgetragen; die ZIP-Pakete liegen im Git.

## Schwerpunkte
- **V7 und N51:** Formal ein Treffer (Präzisierung: „kein Los, für das ein Leser ‚kein Zuschlag erteilt‘ meldet“). Die Einstufung als Lesefehler ist nicht eindeutig: Die Anweisung definiert „kein Zuschlag“ als „Bekanntmachung nennt keinen Zuschlag“; im Rohtext steht bei allen 10 Losen `TenderResultCode: unpublished`. Nicht vertretbar wäre, V7 als erfüllt zu zählen. _(Projekt: `unpublished` bedeutet laut XML `FieldsPrivacy` „geschäftliche Interessen“ nicht veröffentlicht, nicht „kein Zuschlag“.)_
- **V4:** Zwei Schwellen ohne Verknüpfung, keine Folge in „Was folgt“; ehrlich ist „verfehlt“, die Lücke liegt in der Vorab-Festlegung. Die Höchstende-Spalte ist meist zu hoch (7 von 11 Z-Fällen Überschätzung).
- **N57:** Entscheid „unbestimmbar“ folgt der Definition, ist aber eine Härte gegen die Liste. Bei anderer Wertung 62/70 = 88,6 % und 53/61 = 86,9 %; erste Schwelle bleibt verfehlt. N97 geht in die Gegenrichtung (8 Verlängerungen ohne Länge, Liste 2042).
- **V5 = 110/110:** Eher Gleichförmigkeit (gleiche Familie, gleiche Anweisung, Rohtexte mit vorab geschnittenem `EndDate`; 94 von 100 Listenwerten mit Herkunft „enddatum“) als echte Einigkeit. Der Vergleich nutzt das Ergebnis der neutralen Definition, nicht die Rohfakten.
- **V6:** Der Fehlbefund N48 liegt beim Kommilitonen (Text: „Laufzeit ein Jahr“).
- **Alternative Erklärungen V1/V2:** Auswahl leicht (Lose mit Ende, höchstens 2 je Bekanntmachung); die neutrale Definition teilt die Standardannahme „Feld = Ende der Grundlaufzeit“ mit der Liste (teilweise zirkulär; Fehlertyp aus Iteration 6 und 7 in Z kaum prüfbar, z. B. N97); bei N32 und N39 bevorzugt die Definition die Textdauer (Setzung; sonst 68/70); kein Basisvergleich auf Z (nachträglich berechnet: Feld allein 63/70).
- **Prototyp:** „V1 bis V8 erfüllt → weiter“ greift nicht. Die Folge „V7 verfehlt → Filter nachbessern“ und „V8 nicht erfüllt → wiederholen“ gelten wörtlich; für V4 gibt es keine Folge. Die neue Fassung kann als Prototyp gelten (V1 bis V3 erfüllt), darf aber nicht als „V1–V8 erfüllt“ bezeichnet werden; das Höchstende bleibt Hinweis.

## Schwächen nach Gewicht
**Kritisch:** (1) V3: alte Fassung 65/70 = 92,9 % erreicht dieselbe Schwelle, der Nutzen der Regeländerung ist nicht gezeigt, die Stichprobe trennt die Fassungen kaum (7 Regelwirkungs-Lose in 3 Bekanntmachungen). (2) Der Vergleichswert ist teilweise zirkulär. (3) V8-Lücken.
**Mittel:** (4) V7 an einer einzigen Bekanntmachung mit 10 Losen; Bedeutung von `unpublished` ungeklärt. (5) V4 zwei Schwellen ohne Folge, zweite nur 0,2 Punkte über der Schwelle. (6) V5 und Evaluator nicht unabhängig. (7) V6 mit 15 Losen. (8) R hat nur 2 statt 10 Lose, S zählt nicht.
**Gering:** (9) unterschiedliche Bedingungen der Teile; (10) Zeichensatzfehler in Protokollen; (11) keine Prüfung auf Häufung je Auftraggeber.

## Betroffene Annahmen
A4 und A13: bedingt gestützt; Statusänderung auf „gestützt“ nicht gedeckt. A19: nur bedingt gestützt (gleiche Familie, V6 dünn), Statusänderung nicht gedeckt. A20: offen (ein Treffer, `unpublished` ungeklärt; 590 von 9.915 = 6,0 % ist ein Statusfeld-Wert). A12: nur beschreibend (N54, N62, N93 von mindestens einem Leser als „keine Gebäudereinigung“).

## Gesamturteil
**Weiter mit Einschränkung, nicht „V1–V8 erfüllt“.** V1 bis V3 formal erfüllt; der Messaufbau ist ordentlich (Seed, Hashes, blinde Kontrolle, beide Messungen offen berichtet). Gedeckt ist: „Die neue Fassung ist auf dieser Stichprobe mit dem Vergleichswert zu 94,3 % identisch, die alte zu 92,9 %.“ Nicht gedeckt: „Fehlerarten behoben, Stichprobe bestätigt“. Vorschlag des Evaluators (Entscheidung beim Nutzer): neue Fassung als Prototyp nur mit offen ausgewiesenen V7 und V8, Höchstende als Hinweis; sonst „Abschluss mit a93785e als Prototyp, neue Fassung als Ausblick“.
Was für ein belastbares Urteil fehlt: Commit-Zeitpunkt des Skripts, Nachweise für A Teil 1 und 2, Klärung von `unpublished`, Basisregel auf Z, mehr R-Lose, Klarstellung V4, zweite Familie oder mehr menschliche Kontrolle.
