# Auswertung der Zweitprüfung (Iteration 5, Schritt 5: X1 und X2)

_Stand 2026-11-04. Urteile: [gt_pruefung_iteration5_urteile.csv](gt_pruefung_iteration5_urteile.csv) (aus dem ausgefüllten PDF des Nutzers
übertragen; Originaltexte im PDF `Iteration5_Blindpruefung_ausgefuellt.pdf`). Schlüssel lokal; SHA-256 vor dem Öffnen geprüft:
`05abddc9…0b8c` = vorab festgehaltener Wert._

## Fakten
- 71 Paare vorgelegt (61 Paare der Handsuche mit bestimmbarem Ende der Grundlaufzeit, 10 Köder). **4 nicht beurteilt** (P11, P12, P60,
  P62: Kalibrierungsbeispiele der Urteilsregeln). Gewertet: **67 Paare** (57 Paare, 10 Köder).
- Prüfer: P1–P13 der Nutzer (11 gewertet), P14–P71 ein Kommilitone des Nutzers (56 gewertet). Minuten nur für P1–P13 angegeben.
- Zählweise binär wie W4: „gefunden“ = objektgleich oder teilmenge; „nicht gefunden“ = nicht objektgleich oder unklar. Gegenüber dem
  Urteil der Handsuche (Rechercheur, Urteilsregeln 1.1; Köder zählen als „nicht gefunden“).

| Kennzahl | Ergebnis | Schwelle (vorab) | Status |
|---|---|---|---|
| **X2** Übereinstimmung, alle gewerteten Paare | **61/67 = 91,0 %** (Wilson 81,8–95,8), κ = 0,70 | ≥ 85 % | erfüllt (Punktwert; Untergrenze des Intervalls knapp unter 85 %) |
| – nur echte Paare | 52/57 = 91,2 % (81,1–96,2) | | |
| – nur Köder | 9/10 = 90,0 % (59,6–98,2) | | |
| – Nutzer (P1–P13) | 10/11 = 90,9 % | | |
| – Kommilitone (P14–P71) | 51/56 = 91,1 % | | |
| – in W4 schon gesehen (12 Paare, davon 1 nicht beurteilt) | 11/12 | | |
| **X1** Paare, die Rechercheur **und** Prüfer bestätigen, Ende bestimmbar | **52** von 57 | ≥ 30 | erfüllt |

- Abweichungen (6 von 67): P9, P30, P35, P43, P59 (Handsuche „gefunden“, Prüfer „unklar“) und P25 (Köder, Prüfer „objektgleich, mittel“).
  In 5 von 6 Fällen war der Prüfer vorsichtiger als die Handsuche.
- Urteile im Detail (nach Handsuche): objektgleich → 30 objektgleich, 7 teilmenge, 3 unklar; teilmenge → 13 teilmenge, 2 objektgleich,
  2 unklar; Köder („unklar“) → 8 unklar, 1 nicht objektgleich, 1 objektgleich. Die Prüfer vergaben 10-mal „objektgleich, hoch“, die
  Handsuche kennt in Iteration 4 kein „hoch“.

## Interpretation (Vorbehalte)
- X1 und X2 sind formal erfüllt. Die 52 bestätigten Paare sind die Backtest-Basis für Schritt 6.
- **Die Übereinstimmung ist deutlich höher als in W4 (65 %)** bei gleicher Methodik und gleichen Regeln. Mögliche Erklärungen, nicht
  entscheidbar mit diesen Daten: (a) die Ground Truth ist für diese Paare eindeutiger (die Handsuche-Paare sind nach 1.1 meist
  „objektgleich/teilmenge“, es gab weniger schwierige Köder), (b) sorgfältigere Prüfung mit Lesehilfe und ohne Zeitgrenze, (c) die
  Prüfer teilen Gewohnheiten oder Hilfsmittel mit der Handsuche. Zu (c): Die Begründungen von P14–P71 sind einheitlich formatiert („Beide: …“,
  „x von y = 50 %, Grenzfall“) und die Minuten fehlen. **Ob der Kommilitone Hilfsmittel (auch KI) verwendet hat, ist offen und muss geklärt
  werden.** Geht die Prüfung auf dieselbe Modellfamilie wie die Handsuche zurück, bestätigt X2 die Ground Truth (A18) **nicht unabhängig**.
- Köder: 9 von 10 richtig erkannt (nur P25 als „objektgleich“). „Alles bestätigen“ ist damit ausgeschlossen.
- Die Prüfer waren häufiger vorsichtiger als die Handsuche (5 von 6 Abweichungen); die Backtest-Paare sind daher eher eine
  Untergrenze der „echten“ Paare als eine Übertreibung.
- Auswahl: 7 Paare teilen die neue Bekanntmachung mit Kalibrierungsbeispielen (P27, P51, P64 gewertet), siehe `docs/iterationen.md`.

## Folgen für A18 (Status)
A18 bleibt **ungeprüft, mit gestütztem Hinweis**: X2 = 91 % bei zwei Prüfern, Unabhängigkeit des Kommilitonen nicht belegt.
Aus dem Ergebnis folgt keine Statusänderung ohne die Klärung oben.

## Nachtrag 2026-11-04: Hilfsmittel bei der Zweitprüfung
Angabe des Nutzers auf Nachfrage: Die Prüfung wurde **durch KI unterstützt**; die KI hat die Urteile und Begründungen nach Angabe des Nutzers
„nur noch etwas schärfen“ lassen. Für beide Prüfer (Nutzer P1–P13, Kommilitone P14–P71) ist damit nicht ausgeschlossen, dass die Formulierungen
und Details von einem Modell stammen. Der Anteil der KI an den Urteilen selbst ist nicht belegt. Folge: X2 = 91 % gilt als **nicht unabhängige**
Bestätigung der Handsuche (A18 bleibt „ungeprüft“); X1 = 52 bleibt die Backtest-Basis, mit diesem Vorbehalt.

