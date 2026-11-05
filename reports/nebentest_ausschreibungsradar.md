# Nebentest AusschreibungsRadar (Iteration 10, W7)

_Erzeugt von Hand mit `src/prepare/nebentest_ausschreibungsradar.py` (Ziehung, Seed 20261111, Commit `2002ac8` vor dem Nachsehen) und `src/prepare/nebentest_ausschreibungsradar_abruf.py` (Liste, Detailseiten, Prüfung). Rohseiten unverändert in `data/raw/ausschreibungsradar_20261105/` (nicht im Git). Quelle: ausschreibungsradar.com, Abruf 2026-11-05; nur Pfade, die `robots.txt` erlaubt. Rein beschreibend, ohne Schwelle (W7)._

## Fakten

- **Stichprobe:** 15 Z-Lose (N7, N10, N19, N21, N25, N27, N35, N49, N55, N63, N68, N73, N93, N95, N106).
- **Liste bei AusschreibungsRadar:** `/vertragsende/?cpv=90&sort=frist`, 2.153 Aufträge mit Laufzeitende in 1 bis 18 Monaten (Gesamtliste aller Branchen: 26.319), 36 Seiten à 60 Einträge, alle geladen.
- **Seitenabrufe per Skript:** 5 zur Erkundung des Filters, 37 Listenseiten (die 37. leer), 10 Detailseiten = 52 (Grenze 60, Pause ≥ 2,5 s). Dazu kamen vier Einzelabrufe der Preis-, Listen-, Detailseite und `robots.txt` über das Lesewerkzeug.
- **Kandidatensuche:** Stichwortsuche nach Auftraggeber in den Einträgen, danach Auswahl von 10 Kandidaten (7 Lose) nach Titelähnlichkeit von Hand (`KANDIDATEN` im Skript). Für N21, N25, N27, N49, N63, N68, N73, N93 gab es keinen plausiblen Kandidaten.
- **Anerkennung nur über die Kennung:** Die Detailseite verlinkt auf `oeffentlichevergabe.de/ui/de/notices/<UUID>`; diese UUID ist die Adresse des Eintrags. Anerkannt wird, wenn sie der `notice-id` der Zuschlagsbekanntmachung, der `ContractFolderID` oder einer Auftragsbekanntmachung desselben Verfahrens (BT-701) entspricht.

| N | Bekanntmachung | Los | Eintrag bei AusschreibungsRadar | Laufzeit bei AusschreibungsRadar | Vergleichswert (Iteration 9) | Liste | AR richtig | Liste richtig |
|---|---|---|---|---|---|---|---|---|
| N35 | 657794-2025 | 3 | `2c2f75fb…` (4 Lose in einem Eintrag) | 01.10.2025 – 30.09.2027 | 30.09.2027 | 30.09.2027 | ja | ja |
| N95 | 120111-2026 | 1 | `019bea24…` | 01.02.2026 – 31.01.2027 | 31.01.2027 | 31.01.2027 | ja | ja |
| übrige 13 | – | – | nicht gefunden (7 Lose: nur andere Verfahren desselben Auftraggebers gefunden, 8 Lose: kein Kandidat) | – | – | – | – | – |

- **Gefunden und bestätigt: 2 von 15 Losen** (13,3 %); beide stimmen mit dem Vergleichswert und mit der Liste überein.
- Bei den 7 Losen mit Kandidaten zeigte jede der 8 geprüften Detailseiten auf eine andere Bekanntmachung desselben Auftraggebers (kein Treffer).
- Das Laufzeitende steht bei AusschreibungsRadar je Eintrag (Verfahren), ohne Los-Feld; bei N35 gilt es für die vier Lose.

## Interpretation (vorläufig)

- **Nur ein Hinweis, kein Maß:** Zwei bestätigte Treffer reichen für keine Aussage über die Genauigkeit von AusschreibungsRadar. Sie sagen nur: Wo ein Eintrag sicher zuzuordnen war, stimmte sein Laufzeitende mit dem Vergleichswert überein.
- **Abdeckung:** Die Liste zeigt nur Aufträge mit Ende in 1 bis 18 Monaten. Viele der 15 Lose enden später (Enden der Z-Lose reichen bis 2030) oder sind abgelaufen; das erklärt einen Teil der 13 „nicht gefunden“. Dass AusschreibungsRadar ein Los nicht führt, ist daraus nicht zu schließen.
- **Zuordnung ohne API:** Sicher zuordnen lässt sich nur über die Kennung im Link der Detailseite; ohne Bekanntmachungsnummer in der Liste ist das Suchen aufwendig (hier etwa zwei Stunden für 15 Lose). Für einen größeren Vergleich wäre ein Massenabruf nötig, den wir nicht machen.
