# Demo: Profil-Match mit KI-Stufe und Push-Nachrichten

Stand: 2026-11-06. Die Abnahmekriterien wurden vor dem Bau festgelegt (Abschnitt 2); die Ergebnisse je Kriterium stehen in Abschnitt 6.

## 1. Zweck und Rahmen

Fakt: Die Demo zeigt, wie Treffer aus öffentlichen TED-Auftragsbekanntmachungen (Gebäudereinigung, Oberpfalz) zu einem Betriebsprofil passen und als Teams-Karte und als E-Mail im Arbeitswerkzeug eines Betriebs landen könnten (Paket D der Datenübergabe).

Die Demo ist **kein Business Case**. Der Auswahlbogen (`docs/business_case_auswahl.md`) hat keinen tragfähigen Case ergeben; K-I (Push-Matching) ist dort nur Ausblick. Die Demo ändert das nicht. Sie belegt keine Nachfrage, keine Kunden und keinen Vorteil gegenüber bestehenden Angeboten.

Fakt (Eigenangaben der Anbieter, Stand der Recherche vom 2026-11-06, nicht von uns geprüft): Vergabeweiser bietet gespeicherte Suchen mit E-Mail-Benachrichtigung kostenlos, AusschreibungsRadar Suchprofile und Alerts per E-Mail (ab 29 €) sowie KI-Eignungsanalyse und Match-Score (ab 79 €), TED selbst hat Suchprofile mit E-Mail-Alarm. Einen Eignungsabgleich mit dem Firmenprofil nennen laut Anbieter- und Vergleichsseiten auch TendiGo (Premium), Patterno und Bidfix. Ein Teams-Kanal ist bei keinem deutschen Dienst belegt (Jorpex nennt Teams „soon“, Slack ist vorhanden). Ein KI-Eignungsabgleich existiert also bei Wettbewerbern; **die Demo beansprucht kein Alleinstellungsmerkmal.** Ob ein Betrieb Teams als Zielort nutzt, wurde in den drei Gesprächen nie erfragt.

## 2. Abnahmekriterien (vorab festgelegt, vor dem Bau)

- A1 Läuft reproduzierbar offline (Wiedergabe aus lokalen Daten, festes „heute“) und optional live (TED Search API v3 für neue Auftragsbekanntmachungen).
- A2 Filtert auf die Oberpfalz und Gebäudereinigung und zeigt, wie viele Bekanntmachungen jede Stufe durchlaufen (Trichter mit Zahlen).
- A3 Erzeugt mindestens 3 Beispielnachrichten je Kanal (Teams-Adaptive-Card-JSON, E-Mail als .eml) und eine eigenständige Vorschauseite `docs/demo/push_demo.html` (ohne externe Skripte, wie ein Teams-Kanal und ein Posteingang).
- A4 Die KI-Stufe urteilt je Treffer „passt / unklar / passt nicht“ nur mit Zitat aus dem Bekanntmachungstext, markiert nicht ablesbare Kriterien als „nicht ablesbar“ und gibt eine kurze Begründung. Die KI-Urteile werden an mindestens 10 Fällen mit dem regelbasierten Urteil verglichen (Übereinstimmung, Abweichungen aufgelistet, keine Genauigkeitsbehauptung).
- A5 Es wird nichts gesendet. `--senden-teams <URL>` und `--senden-mail` dürfen implementiert sein, werden aber nicht ausgeführt.
- A6 Keine echten Firmen-/Personendaten im Profil; Auftraggeber sind öffentliche Stellen.
- A7 Grenzen dokumentiert; Fakten und Deutung getrennt.

## 3. Aufruf

Im Projektordner (Windows, `-I` wie im übrigen Projekt):

```
.venv\Scripts\python.exe -I src\demo\auftrags_push.py                 # offline, KI-Antworten aus dem Cache (reproduzierbar, kein Netz)
.venv\Scripts\python.exe -I src\demo\auftrags_push.py --ki platzhalter # ohne KI (regelbasierte Begründung, gekennzeichnet)
.venv\Scripts\python.exe -I src\demo\auftrags_push.py --ki claude      # neue KI-Aufrufe (höchstens 20), füllt docs\demo\ki_urteile.json
.venv\Scripts\python.exe -I src\demo\auftrags_push.py --modus live     # holt Bekanntmachungen der letzten 14 Tage von TED nach data\raw\demo_push_<Datum>\
```

Dateien:

| Datei | Inhalt |
|---|---|
| `src/demo/auftrags_push.py` | Ablauf und Kommandozeile, Versandfunktionen (nicht ausgeführt) |
| `src/demo/daten.py` | TED-Abruf (Wartezeit und Wiederholung bei HTTP 429/5xx), Einlesen, Vereinheitlichen |
| `src/demo/stufen.py` | harte Filter, Entfernung, Regelurteil, Eignungs-Block, Vorgänger-Hinweis |
| `src/demo/ki_stufe.py` | KI-Stufe (`claude -p`), Zitatprüfung, Cache, Platzhalter |
| `src/demo/nachrichten.py`, `vorschau.py` | Adaptive Card, .eml, Vorschauseite |
| `docs/demo/profil_beispiel.json` | zwei erfundene Profile (P1 mittlerer Betrieb, Schwandorf, 60 km; P2 Kleinbetrieb, Amberg, 25 km) |
| `docs/demo/nachrichten/*.json, *.eml` | 6 Karten und 6 E-Mails |
| `docs/demo/push_demo.html` | Vorschauseite |
| `docs/demo/ergebnis_lauf.json` | Zahlen des Laufs (Trichter, Vergleich) |
| `docs/demo/ki_urteile.json` | unveränderte Roh-Antworten der KI (Cache für die Wiedergabe) |
| `data/raw/demo_push_20261106/` | unveränderte TED-Antworten (Schnappschuss, 621 Bekanntmachungen) |

Fakt zu den Daten: Die älteren lokalen Abfragen (`data/raw/ted_search/DEU_competition_*_lostext`) enthalten weder die Abgabefrist (`deadline-receipt-tender-date-lot`) noch den NUTS-Ort (`place-of-performance-subdiv-lot`) noch die Eignungsfelder (`selection-criterion-lot`, `selection-criterion-description-lot`). Deshalb wurde **einmal live** abgefragt (TED Search API v3, `POST https://api.ted.europa.eu/v3/notices/search`, anonym; Abfrage `buyer-country=DEU AND form-type=competition AND classification-cpv=909* AND publication-date>=20260901`, 3 Seiten à 250; zuvor 4 kleine Testabfragen mit je 1 bis 5 Treffern, deren Antworten nicht gespeichert wurden) und unverändert abgelegt. Der Offline-Modus spielt diesen Schnappschuss ab. Das ist eine Abweichung vom Vorschlag „Offline aus den älteren Abfragen“ (siehe Abschnitt 6). Die Feldnamen wurden an den Antworten bestätigt; die Doku-Seite https://docs.ted.europa.eu/api/latest/search.html nennt Endpunkt und anonymen Zugang, aber keine Feldliste (Feldliste: https://docs.ted.europa.eu/ODS/latest/reuse/field-list.html, in `src/ted_download.py` bereits verwendet).

Festes „heute“: **2026-10-16**, Wiedergabe der Veröffentlichungen der 14 Tage davor (02.10.–16.10.2026). Gewählt, weil an diesem Tag mehrere Oberpfalz-Bekanntmachungen noch offen waren (der tatsächliche Tag 2026-11-06 hätte im 14-Tage-Fenster nur 2 Treffer ergeben). Veröffentlichungen nach dem Stichtag werden für die Nachrichten ignoriert.

## 4. Stufen

(a) Harte Filter: CPV-Präfix des Profils (90910/90911/90919 auf alle CPV-Felder der Bekanntmachung); Oberpfalz = NUTS-Code beginnt mit DE23 (ersatzweise PLZ 92/93, wenn kein NUTS angegeben); Radius = Luftlinie vom Firmensitz zu einem Punkt je NUTS-3-Region.
(b) Frist noch offen (Frist am Stichtag oder später) und Laufzeit mindestens Profil-Minimum. Fehlt eine Angabe, bleibt die Bekanntmachung im Trichter und wird als „nicht angegeben“ markiert.
**Kein harter Wertfilter:** Wertfelder sind selten gefüllt; der Wert wird nur angezeigt („nicht angegeben“), die Grenze steht im Trichter.
(c) KI-Stufe: je Bekanntmachung ein Aufruf von `claude -p --model claude-sonnet-5-5` in einem leeren temporären Ordner außerhalb des Repos (`--tools "Read,Write"`, `--disable-slash-commands --strict-mcp-config --no-session-persistence`, vorher Prüfung, dass in keinem übergeordneten Ordner eine CLAUDE.md liegt). Die KI bekommt nur Profil(e) und den Bekanntmachungstext (Titel, Beschreibung, Optionen, Eignungs-Freitext, einige Datenfelder als Textzeilen). Ausgabe: Gesamturteil, Begründung, Urteil je Kriterium (Leistung, Objektart, Ort/Entfernung, Laufzeit, Wert, Frist, Losgröße, Zertifikate, Kapazität, Personal, Tarifbindung) mit wörtlichem Zitat oder „nicht ablesbar“. **Das Programm prüft jedes Zitat wörtlich gegen den Text**; ohne belegtes Zitat wird das Kriterium auf „unklar“ zurückgestuft, ein „passt“ ohne belegtes Leistungs-Zitat und ein „passt nicht“ ohne belegtes Gegenargument werden zu „unklar“. Ohne `claude`-Binary läuft ein Platzhalter (Stichwortregel, in der Begründung als „Platzhalter, keine KI“ gekennzeichnet).
(d) Nachrichten: für „passt“ und „unklar“; „passt nicht“ erzeugt keine Nachricht.

**Eignungs-Block** (aus `selection-criterion-lot`, Codes): Die Nachricht nennt die Art der verlangten Nachweise (z. B. Referenzen, Versicherung, Berufsregister, Beschäftigtenzahl, Umsatz). Die deutschen Bezeichnungen sind von uns aus den Codes abgeleitet, die Codeliste wurde nicht Eintrag für Eintrag geprüft. Befund aus dem Schnappschuss (621 Bekanntmachungen): Eignungscodes stehen bei 535, Freitext (`selection-criterion-description-lot`) ebenfalls bei 535; häufigste Codes slc-abil-ref-services (390), slc-stand-ins (300), slc-stand-other (273), slc-suit-reg-trade (210), slc-suit-reg-prof (202). Abweichend von der Erwartung „Schwellen stehen meist in den Vergabeunterlagen“ enthält der Freitext teils konkrete Schwellen (Beispiel 691173-2026: Referenzen mit Mindestgrundfläche); er wird deshalb an die KI gegeben. Zertifikate wie ISO 9001 oder RAL-GZ 902 des Profils lassen sich nur ablesen, wenn der Text sie nennt; sonst „nicht ablesbar“.

**Vorgänger-Hinweis (optional):** Gleicher Auftraggeber (normalisiert) und genau ein Los der Prototyp-Liste mit Titelähnlichkeit ≥ 0,6 und ≥ 0,15 Abstand zum zweitbesten; sonst kein Hinweis. Genutzt wird `docs/prototyp/export/vertragsliste_v1_ohne_auftragnehmer.csv`.

## 5. Ergebnisse (Lauf vom 2026-11-06, Stichtag 2026-10-16)

### Trichter (Anzahl Bekanntmachungen; Fakt aus dem Lauf, `docs/demo/ergebnis_lauf.json`)

| Stufe | P1 (Schwandorf, 60 km) | P2 (Amberg, 25 km) |
|---|---|---|
| Alle Bekanntmachungen DE, CPV 909*, im Schnappschuss (ab 01.09.2026) | 621 | 621 |
| veröffentlicht 02.–16.10.2026 | 145 | 145 |
| ohne Mehrfachveröffentlichung (gleicher Auftraggeber + Titel) | 131 | 131 |
| Gebäudereinigungs-CPV | 125 | 125 |
| Oberpfalz (DE23*) | 4 | 4 |
| Radius | 4 | 2 |
| Frist offen | 4 | 2 |
| Laufzeit ≥ 12 Monate | 4 (bei 3 Laufzeit nicht im Datenfeld) | 2 (bei 2 nicht im Datenfeld) |
| Wert angegeben (Info, kein Filter) | 0 von 4 | 0 von 2 |
| KI: passt / unklar / passt nicht | 3 / 1 / 0 | 1 / 1 / 0 |
| Nachrichten | 4 | 2 |
| davon mit Vorgänger-Hinweis | 0 | 0 |

Der Vorgänger-Hinweis gelang bei **0 von 6** Nachrichten. Ein Funktionstest mit einem erfundenen Eingabe-Titel („Stadt Amberg, Unterhalts- und Grundreinigung Erasmus-Gymnasium“) lieferte den erwarteten Treffer; an den echten Bekanntmachungen wurde nie ein eindeutiger Treffer gefunden (Beispiel: Amberg schreibt 10 Objekte in einer Bekanntmachung aus, mehrere Lose der Liste sind ähnlich). Die Funktion ist damit nur am Beispiel getestet, nicht an echten Treffern.

Randbefund aus dem ganzen Schnappschuss (Fakt): Von 621 Bekanntmachungen haben 21 keinen NUTS-Ort, 30 keine Abgabefrist; Wert je Verfahren oder Los ist bei 75 angegeben (12 %); Laufzeit im Datenfeld bei 89 (14 %).

### KI-Urteil gegen regelbasiertes Urteil (14 Fälle: 7 Bekanntmachungen × 2 Profile)

Vergleichsmenge: alle Bekanntmachungen des Schnappschusses mit CPV und Oberpfalz und Laufzeit-Filter, ohne Fristfilter und ohne Radiusfilter (der Radius steckt im Regelurteil). Das ist größer als der Treffer-Trichter, damit mindestens 10 Fälle zusammenkommen (der Trichter allein ergibt nur 6 Profil-Treffer). Die KI bekam die Entfernung als Hinweis. Sieben KI-Aufrufe (eine Sitzung je Bekanntmachung, beide Profile).

- Übereinstimmung: 13 von 14 Fällen. Davon sind 5 „passt nicht“ allein wegen der Entfernung (P2, Radius 25 km); hier stimmen KI und Regel trivial überein, weil beide denselben Entfernungswert nutzen. Ohne diese 5 bleiben 9 Fälle mit 8 Übereinstimmungen.
- Abweichung (1): P2 / 691173-2026 (Finanzamt Schwandorf, Unterhalts- sowie Glas- und Rahmenreinigung). KI: „unklar“ (Glas- und Rahmenreinigung gehört nicht zum Angebot von P2, Teilangebote je Los nicht ablesbar). Regel: „passt“ (Stichwort „unterhaltsreinigung“ gefunden). Fachlich ist die KI-Begründung plausibel, ein menschliches Urteil liegt nicht vor.
- Regelschwäche (Fakt): Beim Regelurteil für 691173-2026 stammt die „Objektart schule“ aus dem Eignungs-Freitext („Schulen oder Kindergärten“ als vergleichbare Referenzen), nicht aus dem Leistungsobjekt. Das Regelurteil ist also kein zuverlässiger Maßstab.
- Deutung: Die Zahlen sind **keine Genauigkeit**. Es gibt keine menschlich geprüfte Referenz; KI und Regel können beide falsch liegen, die Regel ist ein einfacher Stichwortvergleich, der Vergleich ist klein (n = 14, 7 Bekanntmachungen) und nicht unabhängig (gleiche Entfernungsangabe).

KI-Aufrufe insgesamt: **7 von höchstens 20** (ein Lauf `--ki claude`, 0 Fehler, 0 Wiederholungen). Alle übrigen Läufe nutzen den Cache.

## 6. Abnahmekriterien: Ergebnis

| Kriterium | Ergebnis | Anmerkung |
|---|---|---|
| A1 offline reproduzierbar, optional live | erfüllt mit Abweichung | Zwei aufeinanderfolgende Offline-Läufe lieferten identische Karten-JSON und HTML (MD5 verglichen). Offline-Quelle ist ein Schnappschuss, der einmal live geholt wurde, nicht die älteren Abfragen (diese haben keine Frist/NUTS). Der Live-Modus (`--modus live`) wurde nur als Abfrage des Schnappschusses getestet, nicht als eigener Lauf. |
| A2 Filter und Trichter | erfüllt | Zahlen in Abschnitt 5. |
| A3 ≥ 3 Nachrichten je Kanal und Vorschau | erfüllt | 6 Karten (.json), 6 E-Mails (.eml, Text und HTML; Parsing mit Python geprüft), `push_demo.html` ohne `<script>`, ohne `src=`; 15 Fundstellen von `http(s)://` sind Links und Quellenangaben, keine geladenen Ressourcen. Nicht in Teams oder einem Mailprogramm angezeigt; die Vorschauseite ist eine Nachbildung und wurde nicht in einem Browser angesehen. |
| A4 KI-Stufe, Vergleich ≥ 10 Fälle | erfüllt | 14 Fälle; Zitate werden maschinell geprüft; keine Genauigkeitsbehauptung. |
| A5 nichts gesendet | erfüllt | Kein Aufruf von Teams oder Mail. Netzzugriffe: nur TED-Abfragen beim Schnappschuss und die KI-Aufrufe über `claude -p`. Versandoptionen sind implementiert, nicht ausgeführt, nicht getestet. |
| A6 keine echten Firmen-/Personendaten | erfüllt | Profile erfunden; Absender/Empfänger `example.invalid`. Auftraggeber sind öffentliche Stellen. Ein Auftraggeber (IKK classic) ist eine Körperschaft des öffentlichen Rechts. Die Bekanntmachungstexte können Namen von Ansprechpersonen enthalten; die Nachrichten übernehmen sie nicht, die Roh-Antworten in `data/raw` und `ki_urteile.json` enthalten die Texte. |
| A7 Grenzen, Fakten/Deutung getrennt | erfüllt | Abschnitte 7 bis 9; Nachrichten trennen „Fakten aus der Bekanntmachung“ von „Einordnung (Deutung)“. |

## 7. Anbindung für den späteren echten Versand (vom Nutzer auszuführen, mit eigenem Webhook/Postfach; von uns nicht getestet)

**Teams.** Fakt laut Microsoft (Seite „Create an Incoming Webhook – Teams“, Seitenstand 2026-10-26, gelesen am 2026-11-06, https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook; Ankündigung https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/): Office-365-Connectoren einschließlich Incoming Webhooks wurden im Mai 2026 abgeschaltet. Ersatz ist die Workflows-App (Power Automate) mit dem Auslöser „When a Teams webhook request is received“ bzw. einer Vorlage wie „Send webhook alerts to a channel“. Der Workflow liefert eine URL; an sie schickt man per HTTP POST ein JSON `{"type": "message", "attachments": [{"contentType": "application/vnd.microsoft.card.adaptive", "contentUrl": null, "content": {...}}]}`. Genau dieses Format erzeugt die Demo (Karten-Version 1.2). Grenzen laut Seite: Nachrichten bis 28 KB (unsere Karten ca. 3 KB), Drosselung bei mehr als 4 Anfragen pro Sekunde, Workflows gehören einem Nutzer (Co-Owner einrichten, sonst „verwaiste“ Flows), Lizenzvoraussetzung im Zielmandanten prüfen. Aufruf: `... --senden-teams <Workflow-URL>`. Die Webhook-URL ist ein Geheimnis und gehört nicht ins Repository. **Nicht getestet:** weder das Rendern der Karten in Teams noch der Workflow.

**E-Mail.** `... --senden-mail --smtp-host <Host> --smtp-user <Benutzer> --mail-an <eigene Adresse>`, Passwort in der Umgebungsvariable `DEMO_SMTP_PASSWORD`. Die Funktion ersetzt Absender und Empfänger der .eml-Dateien. **Nicht getestet.** Für einen echten Betrieb bräuchte es einen Versanddienst mit SPF/DKIM; nicht Teil der Demo.

## 8. Datenschutz und UWG (Hinweise, keine Rechtsberatung)

- Die Demo verarbeitet nur öffentliche Bekanntmachungen und erfundene Profile; sie versendet nichts und speichert keine Daten Dritter.
- Deutung (nicht geprüft, juristisch zu klären): Eine von einem Betrieb **bestellte** Benachrichtigung (Anmeldung mit Bestätigung, Abmeldung jederzeit) unterscheidet sich von unverlangter Werbung. Unaufgeforderte Werbe-E-Mails an Gewerbetreibende sind nach § 7 UWG regelmäßig unzulässig; Nachrichten an Betriebe, die sich nicht angemeldet haben, wären deshalb nicht Teil eines späteren Angebots. Bei einem echten Versand an Personen (Teams-Kanal, E-Mail-Adressen) kämen DSGVO-Pflichten hinzu (Rechtsgrundlage, Auftragsverarbeitung bei Cloud-Diensten, Löschfristen).
- TED-Daten: Quellenangabe, Wiederverwendung laut TED-Rechtshinweis (siehe `docs/quellen.md`; Wortlaut vor Abgabe selbst bestätigen). Die Nachrichten und die Vorschauseite tragen die Quellenangabe.

## 9. Grenzen und was die Demo nicht zeigt

Grenzen (Fakt):
- Datenbasis: ein Schnappschuss von 621 Bekanntmachungen (01.09.–06.11.2026); im Wiedergabefenster 4 (P1) und 2 (P2) Treffer. Die Zahlen sind Beispiele, keine Marktaussage.
- Region: Entfernung ist Luftlinie zu einem Punkt je NUTS-3-Region (Kreisstadt, nicht Kreismittelpunkt); Fehler bis etwa 20 km bei großen Landkreisen. Bei Bekanntmachungen mit mehreren Orten zählt der nächste. Bundesweite Ausschreibungen mit Leistungsort in der Oberpfalz (z. B. mehrere Standorte) werden nur über die NUTS-Angabe erfasst.
- Mehrfachveröffentlichungen werden über gleichen Auftraggeber und Titel zusammengefasst; Änderungsbekanntmachungen mit anderem Titel erscheinen doppelt, gleichnamige Neuausschreibungen könnten fälschlich verschmelzen.
- Laufzeit, Wert und Frist fehlen oft im Datenfeld; die KI liest nur den mitgelieferten Text.
- Die KI-Urteile sind nicht menschlich geprüft; sie kann Entfernungen und Losgrößen falsch deuten. Das Programm sichert nur ab, dass Zitate wörtlich im Text stehen, nicht dass das Urteil stimmt. Eine Bekanntmachung wurde mit dem Modell `claude-sonnet-5-5` je einmal bewertet, ohne Wiederholung (keine Aussage zur Stabilität).
- Der Eignungs-Block zeigt die Art der Nachweise; die Beschriftung der Codes ist von uns abgeleitet.

Was die Demo **nicht** zeigt:
- Nachfrage: ob ein Betrieb solche Nachrichten haben will, bezahlen würde oder Teams als Zielort nutzt (in den drei Gesprächen nicht erfragt).
- Eignung nach Zertifikaten, Kapazität und Personal: Diese Kriterien sind aus der Bekanntmachung nicht ablesbar; die Demo weist sie als „nicht ablesbar“ aus und bewertet sie nicht. Die Entscheidung der Gesprächspartner (Entfernung, Personal/Kapazität) wird damit nur teilweise abgebildet.
- Wettbewerbsvorteil: Vergleichbare Dienste existieren (Abschnitt 1); die Demo wurde nicht gegen sie gemessen.
- Genauigkeit der KI: kein Maßstab, keine Stichprobe mit menschlichem Urteil. Der Vergleich mit dem Regelurteil ist ein Hinweis auf Abweichungen, keine Güte.
- Gewinnchancen: Keine Aussage, dass ein Auftrag „gewinnbar“ ist.
- Zeitvorsprung: Die Demo zeigt keinen früheren Hinweis als TED oder Wettbewerber; sie nutzt die Veröffentlichung selbst (Gespräche: Meldung kam 28 Tage vor Abgabe).
