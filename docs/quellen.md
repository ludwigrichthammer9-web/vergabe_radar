# Quellenliste

_Für die Abgabe (Bewertung: Daten, Verfahren und Abbildungen brauchen Quellen). Stand 2026-11-03. Abrufdaten: Dokumentation und Daten im
Zeitraum 2026-10-22 bis 2026-10-30._

## Daten
| Quelle | Verwendung | Hinweis |
|---|---|---|
| TED (Tenders Electronic Daily), Amt für Veröffentlichungen der EU: Bekanntmachungen, abgerufen über die [TED Search API v3](https://api.ted.europa.eu/v3/notices/search) | alle Zuschläge und Ausschreibungen (Auftraggeber in Deutschland, CPV 909), 2016–2026 | Abfragen je Datensatz in `docs/reproduzierbarkeit.md` und in `request_meta.json` jedes Laufs |
| TED-Bekanntmachungen als XML (`https://ted.europa.eu/en/notice/<Nr>/xml`) | Felder, die die API vor eForms nicht liefert (Laufzeit, Verweise `REF_NOTICE`, Lose) | je Notice einzeln, unverändert gespeichert |
| CPV-Codeliste (`codelists/cpv.gc`) aus dem [eForms SDK](https://github.com/OP-TED/eForms-SDK) | Bezeichnungen der CPV-Codes | |
| Lizenz der TED-Daten | – | Laut TED-Rechtsseite ([ted.europa.eu/en/legal-notice](https://ted.europa.eu/en/legal-notice), am 2026-11-05 von einem Agenten, am 2026-11-06 von Claude per WebFetch gelesen; Wortlaut am 2026-11-06 erneut gelesen: Bekanntmachungen „can be freely reused, for commercial or non-commercial purposes“; Redaktionsinhalt der TED-Seiten unter CC BY 4.0, Bedingung „appropriate credit is given and any changes made are indicated“; deshalb Quellenangabe „TED, Publications Office of the European Union“ und Hinweis auf eigene Auswertung) sind Bekanntmachungen nach dem Beschluss 2011/833/EU frei wiederverwendbar, auch kommerziell („Unless otherwise noted“); für Inhalte mit identifizierbaren Privatpersonen können zusätzliche Rechte zu klären sein, diese sind ausgenommen |

Es werden keine personenbezogenen Daten ausgewertet; Bekanntmachungen nennen Auftraggeber und Auftragnehmer als Organisationen.

## Dokumentation und Verfahren
| Quelle | Verwendung |
|---|---|
| [TED API Dokumentation (Search)](https://docs.ted.europa.eu/api/latest/search.html), [OpenAPI-Spezifikation](https://ted.europa.eu/docs/v3), [Feldliste](https://docs.ted.europa.eu/ODS/latest/reuse/field-list.html) | Abfragen, Felder, Grenzen der API |
| [eForms SDK](https://github.com/OP-TED/eForms-SDK), `translations/business-term_de.xml` (develop, abgerufen 2026-10-30) | Definitionen BT-36, BT-536, BT-537, BT-538, BT-54, BT-57, BT-58 |
| [TED Developer Documentation, eForms Business Terms](https://docs.ted.europa.eu/eforms/1.4/reference/business-terms/BT-57.html) | Felder zu Verlängerungen |
| [TED-Schemata-Archiv (R2.0.9)](https://op.europa.eu/en/web/eu-vocabularies/e-procurement/tedschemas-archive) | Aufbau der Formulare F02/F03/F05/F06 vor eForms (`DATE_END`, `DURATION`, `RENEWAL`, `RENEWAL_DESCR`, `REF_NOTICE`) |
| CRISP-DM (Chapman et al., 2000: *CRISP-DM 1.0 – Step-by-step data mining guide*) | Vorgehensmodell, `docs/CRISP-DM.md` |
| Wilson-Intervall für Anteile (E. B. Wilson, 1927; Funktion `wilson` in `src/kennzahlen_iteration2.py`) | Konfidenzintervalle |
| Cohen's κ (Cohen, 1960) | Übereinstimmung in Zweitprüfungen |

## Markt und Wettbewerb (Recherche)
Siehe `docs/business.md` §6 (Schreibtisch-Recherche, 2026-10-24) mit den dort genannten Quellen (u. a. britischer Dienst Stotles).
Die Zahlen dort sind Fakten aus den TED-Daten oder Recherche, keine Kundenaussagen.

## Werkzeuge
Python mit `requests`, `pandas`, `tabulate` (`requirements.txt`); KI-Assistenz: Claude Code (Anthropic), Einsatz und Irrwege in
`docs/ki_irrwege.md`.
