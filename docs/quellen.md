# Quellenliste

_Für die Abgabe (Bewertung: Daten, Verfahren und Abbildungen brauchen Quellen). Stand 2026-11-09 (zuerst 2026-11-03). Abrufdaten: Dokumentation und Daten im
Zeitraum 2026-10-22 bis 2026-10-30._

## Daten
| Quelle | Verwendung | Hinweis |
|---|---|---|
| TED (Tenders Electronic Daily), Amt für Veröffentlichungen der EU: Bekanntmachungen, abgerufen über die [TED Search API v3](https://api.ted.europa.eu/v3/notices/search) | alle Zuschläge und Ausschreibungen (Auftraggeber in Deutschland, CPV 909), 2016–2026 | Abfragen je Datensatz in `docs/reproduzierbarkeit.md` und in `request_meta.json` jedes Laufs |
| TED-Bekanntmachungen als XML (`https://ted.europa.eu/en/notice/<Nr>/xml`) | Felder, die die API vor eForms nicht liefert (Laufzeit, Verweise `REF_NOTICE`, Lose) | je Notice einzeln, unverändert gespeichert |
| CPV-Codeliste (`codelists/cpv.gc`) aus dem [eForms SDK](https://github.com/OP-TED/eForms-SDK) | Bezeichnungen der CPV-Codes | |
| Lizenz der TED-Daten | – | Laut TED-Rechtsseite ([ted.europa.eu/en/legal-notice](https://ted.europa.eu/en/legal-notice), am 2026-11-05 von einem Agenten, am 2026-11-06 von Claude per WebFetch gelesen; Wortlaut am 2026-11-06 erneut gelesen: Bekanntmachungen „can be freely reused, for commercial or non-commercial purposes“; Redaktionsinhalt der TED-Seiten unter CC BY 4.0, Bedingung „appropriate credit is given and any changes made are indicated“; deshalb Quellenangabe „TED, Publications Office of the European Union“ und Hinweis auf eigene Auswertung) sind Bekanntmachungen nach dem Beschluss 2011/833/EU frei wiederverwendbar, auch kommerziell („Unless otherwise noted“); für Inhalte mit identifizierbaren Privatpersonen können zusätzliche Rechte zu klären sein, diese sind ausgenommen. Dieser Wortlaut (gelesen 2026-11-06) gilt für alle Lizenzhinweise im Projekt |
| Vergabeweiser-API ([vergabeweiser.de](https://vergabeweiser.de/)), Abruf 2026-11-05 | Vergleich Liste gegen Vergabeweiser (Iteration 10, 10b); Rohantworten unverändert in `data/raw/vergabeweiser_20261105/` | Lizenz CC BY 4.0, Namensnennung „Vergabeweiser“ (vergabeweiser.de) ([vergleich_iteration10.md](../reports/vergleich_iteration10.md)) |
| Bekanntmachungsservice (Datenservice Öffentlicher Einkauf), OCDS-Jahresdateien 2024 bis 2026 über die [Open Contracting Partnership, Veröffentlichung 136](https://data.open-contracting.org/en/publication/136) | Paket B, Abdeckung unterhalb von TED (Oberpfalz) | Lizenz CC0 1.0 ([oeffentlichevergabe_test.md](../reports/oeffentlichevergabe_test.md)) |

**Personenbezug.** Alle Angaben stammen aus öffentlichen TED-Bekanntmachungen. Bei Einzelunternehmern kann der Firmenname des Auftragnehmers einen Personennamen enthalten (Vertragsliste, Webseite, Wettbewerbsbild; Vorprüfung: 4 von 47 Namen ohne erkennbare Rechtsform, 1 e. K.; `docs/export_schema.md` §8). Unverändert übernommene TED-Texte (z. B. `reports/zweitlesung_iteration9/rohtext/`) enthalten die dort veröffentlichten Kontaktdaten der Auftraggeber. Eine Fassung ohne Auftragnehmer liegt unter `docs/prototyp/export/vertragsliste_v1_ohne_auftragnehmer.csv`. Die Telefonnotizen (`docs/business.md` §8.9) enthalten keine Namen.

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

## Kandidat K-J: Push in Teams, Outlook, Planner (Nachtrag 2026-11-09, Lesedatum aller Seiten 2026-11-06)
_Verwendung: `docs/business_case_auswahl.md`, Nachtrag K-J. Die Aussagen stehen „laut Seite“ so in der Recherche; wir haben sie nicht erneut abgerufen. Eigenangaben der Anbieter; Preise und Bedingungen ändern sich._

| Quelle | Laut Seite |
|---|---|
| [Power Automate, Deep dive licenses](https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/deep-dive-on-specific-license) (ms.date 2026-10-17) | Microsoft-365-Lizenzen erlauben Standard-Konnektoren; Premium ist nicht enthalten |
| [Flows mit Dienstprinzipal, Lizenz zuweisen](https://learn.microsoft.com/en-us/power-automate/assign-user-license-service-principal-flow) (ms.date 2026-08-14) | Eine Microsoft-365-Lizenz („seeded license“) deckt Premium-Funktionen wie HTTP-Aktionen nicht ab (indirekte Aussage in einem Artikel über Flows mit Dienstprinzipal) |
| [Power Automate Licensing FAQs](https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/faqs) (Stand 2026-09-22) | Bei geplanten Flows braucht der Besitzer Premium |
| [Preise Power Automate](https://www.microsoft.com/de-de/power-platform/products/power-automate/pricing) | Premium 13,00 € je Nutzer und Monat, jährliche Abrechnung, zuzüglich MwSt. |
| Standard-Konnektoren: [Referenz](https://learn.microsoft.com/en-us/connectors/connector-reference/connector-reference-standard-connectors), [Outlook](https://learn.microsoft.com/en-us/connectors/office365/), [Teams](https://learn.microsoft.com/en-us/connectors/teams/), [Planner](https://learn.microsoft.com/en-us/connectors/planner/), [RSS](https://learn.microsoft.com/en-us/connectors/rss/) | Outlook, Teams, Planner und RSS sind Standard-Konnektoren |
| [Incoming Webhooks mit Workflows für Teams](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498) | Teams-Webhooks über Workflows ohne Premium |
| [Abschaltung der Office-365-Konnektoren in Teams](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) (Stand 2026-04-14) | Abschaltung 18. bis 22.05.2026 |
| Planner: [Graph API „planner-post-tasks“](https://learn.microsoft.com/en-us/graph/api/planner-post-tasks?view=graph-rest-1.0), [Planner für Admins](https://learn.microsoft.com/en-us/planner/planner-for-admins) | Aufgaben per Graph oder Konnektor anlegbar |
| TED: [About TED](https://ted.europa.eu/en/about-ted), [My dashboard](https://ted.europa.eu/en/help/my-dashboard), [TED account](https://ted.europa.eu/en/help/ted-account) | Gespeicherte Suchen und Alarme (bis 25), E-Mail, RSS |
| [service.bund.de, Ausschreibungssuche](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html) | Suche mit RSS und Newsletter |
| [Vergabeweiser](https://vergabeweiser.de/) | Alerts (gespeicherte Suchen, E-Mail-Benachrichtigung) |
| [AusschreibungsRadar, Preise](https://ausschreibungsradar.com/preise/) | Watchlist 9 €, Starter 29 €, Business 79 €, Professional 149 € (netto) |
| [subreport, Produktübersicht](https://subreport.de/ausschreibungen/produktuebersicht/) | Preise |

## Werkzeuge
Python mit `requests`, `pandas`, `tabulate` (`requirements.txt`); KI-Assistenz: Claude Code (Anthropic), Einsatz und Irrwege in
`docs/ki_irrwege.md`.
