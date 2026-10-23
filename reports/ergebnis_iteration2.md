# Ergebnis Iteration 2: Neuausschreibungen sichtbar und zuordenbar?

Stand: 2026-10-23. Hypothese, Kriterien und alle Präzisierungen: [docs/iterationen.md](../docs/iterationen.md), Abschnitt Iteration 2.

> **Korrigiert nach der Evaluation** ([evaluation_iteration2.md](evaluation_iteration2.md)), 2026-10-23: Formulierungen in §2–§4
> an die Trennung von Fakten und Interpretation angepasst, Befund A30 ergänzt, Zahlen zur Grundlaufzeit korrigiert. Die Kriterien
> und die Urteile zu K1–K5 sind unverändert.

**Hypothese (vorab):** „Für die Mehrheit der deutschen Gebäudereinigungs-Ausschreibungen (competition, Haupt-CPV 909) aus Q2 2026
gibt es auf TED einen früheren CPV-909-Zuschlag desselben Auftraggebers.“

**Quellen**
- **[RR]** [rueckreichweite_909.md](rueckreichweite_909.md): Trefferzahlen je Quartal, Formatwechsel
- **[K]** [kennzahlen_iteration2.md](kennzahlen_iteration2.md): K4, K5 (`src/kennzahlen_iteration2.py`)
- **[Z]** [zuordnung_iteration2.md](zuordnung_iteration2.md): K1, Auswahlstufen (`src/zuordnung_prototyp.py`)
- **[P]** [k2_pruefliste.md](k2_pruefliste.md): K2-Urteile, Gründe ohne Treffer
- **[X]** [k2_auszuege.md](k2_auszuege.md): Auszüge aus der Original-XML (`src/k2_xml_auszug.py`)
- **[DU]** [02_data_understanding.md](../docs/phasen/02_data_understanding.md): API-Prüfung (Schritt 1)

---

## 1. Kriterien im Überblick

| | Kriterium | Ergebnis | Schwelle | Status |
|---|---|---|---|---|
| K1 | Ausschreibungen mit früherem Zuschlag desselben Auftraggebers | 461 / 551 = **83,7 %** (Wilson 80,3–86,5 %) [Z] | ≥ 50 % | erfüllt |
| K2 | Davon plausibel dieselbe Leistung (30 zufällige Treffer) | 5 / 30 = **16,7 %** (Wilson 7,3–33,6 %); 2 unklar, 23 nein [P] | ≥ 80 % | **nicht erfüllt** |
| K3 | Bestätigte Vorgänger im eForms-Format | 2 / 5 (A8, A24) [P] | Messwert | – |
| K4 | Laufzeitende bestimmbar, Q2 2025 | 320 / 390 = **82,1 %** (Wilson 77,9–85,5 %) [K] | ≥ 80 % und KI-Untergrenze ≥ 75 % | erfüllt |
| K5 | Abgelaufene eForms-Verträge (Ende ≤ 23.10.2026) | **629** [K] | ≥ 100 | erfüllt |

## 2. Fakten

### Daten und Rückreichweite
- Die Such-API enthält Notices ab Ende Oktober 2016. Vor eForms (bis 24.10.2023) liefert sie nur Auftraggebername, Ort, CPV-Liste,
  Datum und Formulartyp, also keine Laufzeit, keine Haupt-CPV und keine Kennung. [DU]
- 15.361 Zuschläge mit CPV 909 (DEU) seit Okt. 2016, stabil 1.250–1.750 pro Jahr. 710 Ausschreibungs-Notices in Q2 2026, davon
  159 Änderungsbekanntmachungen. Es bleiben 551 Verfahren. [RR], [DU]
- Vorinformationen: etwa 30 pro Jahr. [RR]

### K1 und K2: Zuordnung
- Regel: gleicher normalisierter Auftraggebername oder gleiche Kennung, Zuschlag vor der Ausschreibung. Auswahl unter mehreren
  Kandidaten in drei Stufen (Präzisierung vom 23.10. in iterationen.md). [Z]
- Treffer haben oft sehr viele Kandidaten: Bei 248 von 461 Ausschreibungen sind es mehr als 10. [Z]
- K2 nach Anzahl der Kandidaten: 1–2 Kandidaten 3 von 6 „ja“ (1 unklar), 3–10 Kandidaten 1 von 9 (1 unklar), mehr als 10
  Kandidaten 1 von 15. [P]
- Typische Fehlzuordnung: gleicher Auftraggeber, anderes Objekt. Beispiele: Frankfurt Schillerschule → Ebelfeldschule (A3),
  Autobahn GmbH NL Nordost → NL Westfalen über gemeinsame Kennung (A1, A5), andere Leistung wie Schädlingsbekämpfung statt
  Reinigung (A6, A22). [P]
- Von Claude als plausibel beurteilte Paare (keine unabhängige Prüfung): A2 (Gemeinde Wenden), A8 (DPMA München),
  A13 (Bezirk Oberbayern), A16 (WZB Berlin), A24 (Polizeirevier Ost Kassel). [P]
- **A30 (Befund des Evaluators):** Der objektgleiche Vorgänger 775273-2024 („Unterhaltsreinigung JKI Quedlinburg“, Laufzeit
  01.01.2025–31.12.2028) war unter den Kandidaten. Gewählt wurde aber 669822-2022 (Siebeldingen), weil das Ende außerhalb des
  Fensters von −3 bis +18 Monaten lag. [Evaluation]
- Ein Vorgänger wurde teils für mehrere Ausschreibungen gewählt (z. B. 229946-2025 für 10). Die Stichprobe enthält deshalb
  Klumpen (A1/A5, A3/A19). [Evaluation]
- 15 Ausschreibungen ohne Treffer: 5 mit früherem 909-Zuschlag unter abweichendem Namen (z. B. „Hansestadt Demmin“ statt
  „Hansestadt Demmin – Der Bürgermeister“; inhaltlich nicht geprüft), 3 einmalige Leistungen (Bau- oder Schimmelreinigung),
  6 ohne früheren Zuschlag im 909-Pool per Namenssuche (nicht dasselbe wie „keiner auf TED“), 1 unklar. [P]

### Laufzeit vor eForms (A11)
- Alle 10 Vorgänger vor eForms in der Stichprobe verweisen über `REF_NOTICE` auf eine frühere Bekanntmachung (9 × F02, 1 × F05).
  In allen 10 stehen Beginn und Ende, in 5 eine Verlängerungsoption. Die Zuschläge selbst (F03/F06) enthalten keine Laufzeit. [X]

### Vorlauf in den als plausibel beurteilten Paaren (explorativ, n = 5; dazu A30 vorzeitig)

| Fall | Ausschreibung | Vertragsende Vorgänger | Vorlauf |
|---|---|---|---|
| A13 | 27.04.2026 | 30.09.2026 | 5,1 Monate |
| A16 | 04.05.2026 | 31.08.2026 nur mit allen Verlängerungen (Grundlaufzeit bis 31.08.2023) | 3,9 Monate |
| A2 | 01.04.2026 | 31.07.2026 mit 5 Verlängerungen (angenommen; Grundlaufzeit bis 31.07.2021) | 4,0 Monate |
| A24 | 22.05.2026 | 31.03.2027 (Grundlaufzeit), neuer Vertrag ab 01.11.2026 | vorzeitige Neuvergabe |
| A8 | 22.04.2026 | etwa Herbst 2028 (48 Monate ab Okt. 2024) | vorzeitige Neuvergabe |

### K4 und K5
- Gegenprobe: Der Pool ergibt für das Fenster aus Iteration 1 wieder 440 Notices, davon 356 mit bestimmbarem Ende. [K]
- „Laufzeitende bestimmbar“ je Jahr: 2023 (ab 25.10.) 70,7 %, 2024 70,1 %, 2025 79,7 %, 2026 82,5 %. [K]
- Die 629 abgelaufenen eForms-Verträge haben eine Median-Laufzeit von 12 Monaten (alle eForms-Zuschläge: 36). [K]

## 3. Interpretation

- **Die Hypothese ist im Wortlaut bestätigt, sagt aber zu wenig aus.** Fast jede Ausschreibung hat einen früheren Zuschlag desselben
  Auftraggebers (K1). Bei großen Auftraggebern ist das aber trivial, weil sie dauernd Reinigung vergeben.
- **Die Zuordnung auf Ebene des Auftraggebers taugt nicht für das Radar (K2 = 17 %).** Sie erkennt, *dass* ein Auftraggeber
  wieder ausschreibt, nicht *welcher* Vertrag ausläuft. Die Auswahl über ein passendes Vertragsende (Stufe 1) hilft nicht, weil große
  Auftraggeber fast immer irgendeinen passenden Vertrag haben.
- **Es gibt Fälle, in denen das Zielereignis über das Objekt zuordenbar ist.** In den 5 plausiblen Paaren und bei A30 stimmen
  Adresse bzw. Liegenschaft und Titel überein. Ob das allgemein gilt, ist nicht gemessen. 3 der 5 Paare stammen von Auftraggebern
  mit höchstens 2 Kandidaten, sind also leichte Fälle. Für große Auftraggeber ist eine Zuordnung über das Objekt nicht gezeigt.
- **Vorlauf und Verlängerungen:** Unabhängig gemessen ist nur A13 (5,1 Monate vor Vertragsende). Bei A2 und A16 passen 4 Monate nur,
  wenn alle Verlängerungen gezogen wurden. Das wurde aus dem Datum der neuen Ausschreibung erschlossen und ist damit zirkulär. Wäre
  nur die Grundlaufzeit verwendet worden, läge die Prognose 4,7 Jahre (A2) bzw. 2,7 Jahre (A16) daneben. **3 von 6 objektgleichen
  Paaren sind vorzeitige Neuvergaben** (A8, A24, A30). Das ist für A8 eher ein Warnsignal als eine Stütze (n = 6).
- **Daten vor eForms scheinen nutzbar (A11),** aber nur über die XML der alten Ausschreibung. In der Stichprobe hatten alle 10 eine
  Laufzeit. Die Stichprobe ist allerdings durch die Auswahlregel bestimmt und nicht zufällig. Weil die abgelaufenen eForms-Verträge
  fast nur kurze Verträge sind (K5), wird diese Quelle für einen unverzerrten Backtest wohl nötig sein.
- **Ob die Vorgänger überhaupt auf TED stehen, wurde nicht gemessen.** K2 misst nur, ob der gewählte Kandidat stimmt. Hinweise gibt es
  in beide Richtungen: A30 (Vorgänger vorhanden, Methode versagt) gegenüber 6 Fällen ohne Treffer ohne Vorgänger im Pool, Fällen
  mit 1–2 Kandidaten ohne passenden Vorgänger (A7, A22) und dem ungeklärten Verhältnis von 1,6 Ausschreibungen pro Zuschlag.
- **Exakte Namensgleichheit ist zu streng und zu grob zugleich.** Sie verpasst Vorgänger unter anderer Schreibweise und trennt nicht
  zwischen Objekten desselben Auftraggebers.

## 4. Was die vorab festgelegte Entscheidungsregel sagt

Laut iterationen.md gilt „K1 < 25 % oder K2 < 50 % → **Idee anpassen / zurück zu Phase 1** (Nachfolger auf TED kaum sichtbar, A3)“.
K2 liegt mit 16,7 % unter 50 %, **die Regel ist also ausgelöst** und das Entscheidungstor im Projektplan nicht bestanden.

Die Regel nennt als Ursache „Nachfolger kaum sichtbar“. Belegt ist aber nur, dass die **Zuordnung über den Auftraggeber** nicht
taugt. Ob die Vorgänger auf TED sichtbar sind, wurde nicht gemessen. Die Regel hat also zwei Dinge vermengt: Wie gut die Methode
trifft (Präzision) und ob die Daten den Vorgänger überhaupt enthalten (Sichtbarkeit). Wer davon abweicht, muss das als **Abweichung**
dokumentieren. „Die Regel passt nicht“ ist keine ausreichende Begründung.

Mögliche Auslegungen (Entscheidung des Nutzers bei `/iteration-ende`):
1. **Idee anpassen über eine weitere Phase-2-Iteration:** Sichtbarkeit der Vorgänger und Zuordnung über das Objekt (Adresse,
   Liegenschaft, Titel; auch frühere Ausschreibungen als Quelle) **getrennt** messen, mit neuen, vorab committeten Kriterien. Dazu
   eine harte Abbruchregel zu den vorab genannten Optionen. Diese Auslegung stand nicht auf der vorab genannten Optionsliste und ist
   deshalb eine Abweichung (Empfehlung des Evaluators).
2. **Prognose aus Auftraggeber-Zyklen** (vorab genannte Option): Das Produkt sagt nur „Auftraggeber X schreibt voraussichtlich bald
   wieder Reinigung aus“. Das ginge mit den jetzigen Daten, wäre aber vermutlich weniger wertvoll für Kunden (A1, A15 ungeprüft).
3. **Nationale Quellen oder andere Nische** (vorab genannte Optionen): bleiben als Ausweg, falls die Sichtbarkeit auf TED zu niedrig ist
   (A3). Sie sind durch die Befunde nicht widerlegt.

## 5. Grenzen

- **Regel und Prüfung aus derselben Hand:** Der Nutzer hat die K2-Prüfung an Claude übertragen. Der Evaluator kam in 29 von 30
  Fällen zum selben Urteil (A4 Grenzfall), allerdings mit denselben XML-Auszügen. Eine wirklich unabhängige zweite Prüfung fehlt.
- **Nur das gewählte Paar wurde geprüft,** nicht die ganze Kandidatenliste (siehe A30).
- **Die Nische „Haupt-CPV 909“ ist breiter als wiederkehrende Gebäudereinigung:** Sie enthält auch Schädlingsbekämpfung,
  Fahrzeug- und Industriereinigung sowie einmalige Bau- bzw. Sonderreinigung (A6, A22, B1, B4, B7, B12, B15).
- **Kleine Stichproben:** K2 n = 30, bestätigte Paare n = 5, A11 n = 10, Fälle ohne Treffer n = 15.
- **Nur ein Quartal Ausschreibungen** (Q2 2026). Saisoneffekte sind nicht geprüft.
- **Grundlage sind XML-Auszüge**, die TED-Webansicht wurde nicht geöffnet. Die Auszüge kürzen Beschreibungen auf 350 Zeichen.
- **Die Auswahlregel wurde nach dem ersten Lauf geändert** (vor jeder Paarbeurteilung, dokumentiert). Auch die erste Regel hätte
  laut Diagnose viele falsche Vorgänger gewählt.
- **K1 ist durch die Präzisierungen vom 23.10. beeinflusst:** CPV-Liste statt Haupt-CPV für Vorgänger vor eForms, Verfahren statt Notices.
