"""Daten für das Dashboard „Vergabe-Radar Projektstand“ aus den Projektdokumenten.

Schreibt JSON-Dateien (Liste von Zeilen) nach data/processed/dashboard/:
- aufgaben.json     aus docs/projektplan.md: Aufgaben erster Ebene der Stränge T und G mit Haken (Strang P sind Daueraufgaben)
- annahmen.json     aus docs/annahmen.md: ID, Kurztext, Risiko, Status
- iterationen.json  Iterationen 1–8 mit Status und Entscheidung (docs/iterationen.md, Übersicht)
- schritte_it6.json Plan der laufenden Iteration 6 (docs/iterationen.md, Abschnitt Iteration 6)
- kriterien_it5.json X1–X4 der Iteration 5 (reports/gt_pruefung_iteration5_auswertung.md, backtest_iteration5.md, vertragsliste_iteration5.md)
- backtest.json     Treffer von R0 und R1 im Backtest (aus src/model/baseline.py, data/processed)
- backtest_lage.json Lage der Neuausschreibung relativ zur R1-Prognose (wie backtest.json)
- verlauf.json      Zuordnung über die Iterationen (ergebnis/evaluation der Iterationen 2–4)
- phasen.json       Stand der CRISP-DM-Phasen (docs/phasen/01–06)
- zeit_ist.json     Arbeitssitzungen je Iteration aus den Commit-Zeiten (git log, Untergrenze)
- zeit_rest.json    Schätzung der verbleibenden Stunden je Block, mit Grundlage

Aufruf (Backtest-Teil liest data/processed, daher mit der Projektumgebung):
    .venv\\Scripts\\python src/dashboard_daten.py
"""

import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "processed" / "dashboard"


# Abschnitte des Projektplans tragen die Nummern von vor den eingeschobenen Iterationen (projektplan.md, Überblick)
ABSCHNITT_LABEL = {"T1": "Iteration 1: Machbarkeit", "T2": "Iteration 2: Zuordnung über den Auftraggeber",
                   "T2b": "Iteration 3: Zuordnung über das Objekt", "T2c": "Iteration 4: Letzter Verbesserungsversuch",
                   "T3": "Iteration 5: Erste Prognose und Backtest", "T4": "Verbesserung der Prognose (zurückgestellt)",
                   "T5": "Iteration 6: Prototyp der Vertragsliste", "T6": "Ausbau oder Neuausrichtung",
                   "G1": "Wettbewerb und Markt", "G2": "Kundengespräche (eingestellt)", "G3": "Angebot und Preis (Recherche)", "G4": "Pilotkunden (entfällt)"}


def aufgaben() -> list[dict]:
    rows, strang, abschnitt = [], None, None
    for line in (ROOT / "docs" / "projektplan.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## Strang "):
            strang = line.split()[2].rstrip(":")
        elif line.startswith("## "):
            strang = None
        elif line.startswith("### ") and strang:
            code = line[4:].split()[0]
            abschnitt = ABSCHNITT_LABEL.get(code, re.sub(r"\s*\(.*\)$", "", line[4:]).strip())
        m = re.match(r"- \[([ x])\] (.*)", line)
        if m and strang in ("T", "G"):
            text = re.sub(r"\*\*|`", "", m.group(2))
            nr = re.match(r"(T\d+[a-z]?\.\d+|G\d+\.\d+)", text)
            rows.append({"strang": "Technik und Daten" if strang == "T" else "Geschäft", "abschnitt": abschnitt,
                         "nr": nr.group(1) if nr else text[:6], "aufgabe": re.sub(r"^\S+\s+", "", text)[:110],
                         "erledigt": 1 if m.group(1) == "x" else 0})
    return rows


def annahmen() -> list[dict]:
    rows = []
    for line in (ROOT / "docs" / "annahmen.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and re.fullmatch(r"A\d+[a-z]?", cells[0]):
            text = re.split(r"(?<=[.!?])\s", cells[1])[0]
            status = re.sub(r"\*\*", "", cells[3])
            kurz = ("widerlegt" if "widerlegt" in status else "bestätigt" if "bestätigt" in status
                    else "vorläufig gestützt" if "gestützt" in status else "ungeprüft")
            rows.append({"id": cells[0], "annahme": text[:120], "risiko": cells[2], "status": kurz,
                         "status_detail": status[:80]})
    return rows


ITERATIONEN = [  # docs/iterationen.md, Übersicht (Stand 2026-11-04)
    {"nr": 1, "fokus": "Machbarkeit der Daten", "status": "abgeschlossen", "entscheidung": "Gebäudereinigung als Arbeitsnische, zurück zu Phase 2"},
    {"nr": 2, "fokus": "Neuausschreibungen zuordenbar über den Auftraggeber?", "status": "abgeschlossen", "entscheidung": "Idee anpassen: Zuordnung über das Objekt"},
    {"nr": 3, "fokus": "Sichtbarkeit und Zuordnung über das Objekt", "status": "abgeschlossen", "entscheidung": "In Phase 2/3 bleiben, letzter Verbesserungsversuch"},
    {"nr": 4, "fokus": "Letzter Verbesserungsversuch der Zuordnung", "status": "abgeschlossen", "entscheidung": "Idee anpassen: Zuordnung nicht weiter verbessern, Vertragsliste aus Zuschlägen"},
    {"nr": 5, "fokus": "Vertragsliste aus Zuschlägen: Prognoseziel, Prognose, Backtest", "status": "abgeschlossen", "entscheidung": "Idee anpassen: Terminprognose verworfen (28,8 %), Vertragsliste mit Enddaten als Kern"},
    {"nr": 6, "fokus": "Prototyp der Vertragsliste und Qualität der Enddaten", "status": "läuft", "entscheidung": "–"},
    {"nr": 7, "fokus": "Prototyp der Vertragsliste", "status": "entfällt", "entscheidung": "In Iteration 6 aufgegangen"},
    {"nr": 8, "fokus": "Ausbau oder Neuausrichtung", "status": "geplant", "entscheidung": "–"},
]

SCHRITTE_IT6 = [  # docs/iterationen.md, Iteration 6, Plan und Fortschritt
    {"nr": 1, "schritt": "Abdeckung prüfen, Regeln vorab committen", "status": "erledigt", "commit": "6baaab5"},
    {"nr": 2, "schritt": "Stichprobe ziehen (60 Lose, 10 Paare), Schlüssel-Hash", "status": "erledigt", "commit": "3e01407"},
    {"nr": 3, "schritt": "Prüfung durch dich, ohne KI-Hilfe", "status": "in Arbeit", "commit": ""},
    {"nr": 4, "schritt": "Auswertung Y1 bis Y3", "status": "offen", "commit": ""},
    {"nr": 5, "schritt": "Prototyp der Liste für eine Region", "status": "offen", "commit": ""},
    {"nr": 6, "schritt": "Selbstbewertung, Evaluator, /iteration-ende", "status": "offen", "commit": ""},
]

KRITERIEN_IT5 = [  # Iteration 5: reports/gt_pruefung_iteration5_auswertung.md, backtest_iteration5.md, vertragsliste_iteration5.md
    {"id": "X1", "name": "Backtest-Basis", "wert": 52, "schwelle": 30, "max": 70, "einheit": "Paare", "anzeige": "52 Paare",
     "status": "nur formal", "hinweis": "Von Handsuche und Zweitprüfung bestätigte Paare; Zweitprüfung KI-unterstützt"},
    {"id": "X2", "name": "Zweitprüfung", "wert": 61 / 67, "schwelle": 0.85, "max": 1, "einheit": "Anteil", "anzeige": "61 von 67",
     "status": "nur formal", "hinweis": "KI-unterstützt; blindes Bestätigen hätte schon 85,1 % ergeben"},
    {"id": "X3", "name": "Trefferquote R1", "wert": 15 / 52, "schwelle": 0.60, "max": 1, "einheit": "Anteil", "anzeige": "15 von 52",
     "status": "verfehlt", "hinweis": "Höchstende − 6 Monate, Fenster ±3 Monate; naive Referenz R0: 9 von 52"},
    {"id": "X4", "name": "Abdeckung der Liste", "wert": 2924 / 3668, "schwelle": 0.80, "max": 1, "einheit": "Anteil", "anzeige": "2.924 von 3.668",
     "status": "verfehlt", "hinweis": "Knapp verfehlt (Wilson 78,4–81,0 %); 20 % der Lose ohne Laufzeitangabe"},
]


def backtest() -> tuple[list[dict], list[dict]]:
    """Treffer von R0/R1 und Lage der Veröffentlichung relativ zur R1-Prognose, aus den eingefrorenen Regeln (src/model/baseline.py)."""
    sys.path.insert(0, str(ROOT / "src" / "model"))
    from baseline import FENSTER_MONATE, lade
    rows = lade()
    n = len(rows)
    treffer = [{"regel": "R0: Ende der Grundlaufzeit − 6 Monate", "treffer": sum(r["t0"] for r in rows), "paare": n},
               {"regel": "R1: Höchstende − 6 Monate", "treffer": sum(r["t1"] for r in rows), "paare": n}]
    lage = [{"lage": f"mehr als {FENSTER_MONATE} Monate früher", "paare": sum(r["d1"] < -FENSTER_MONATE for r in rows)},
            {"lage": f"im Fenster ±{FENSTER_MONATE} Monate", "paare": sum(abs(r["d1"]) <= FENSTER_MONATE for r in rows)},
            {"lage": f"mehr als {FENSTER_MONATE} Monate später", "paare": sum(r["d1"] > FENSTER_MONATE for r in rows)}]
    return treffer, lage


VERLAUF = [  # Iteration 2: reports/ergebnis_iteration2.md (K2); 3: zuordnung_iteration3.md; 4: zuordnung_iteration4.md
    {"iteration": 2, "kennzahl": "Präzision der Zuordnung", "wert": 5 / 30},
    {"iteration": 3, "kennzahl": "Präzision der Zuordnung", "wert": 11 / 24},
    {"iteration": 4, "kennzahl": "Präzision der Zuordnung", "wert": 17 / 19},
    {"iteration": 3, "kennzahl": "Trefferquote", "wert": 11 / 38},
    {"iteration": 4, "kennzahl": "Trefferquote", "wert": 17 / 30},
    {"iteration": 3, "kennzahl": "Sichtbarkeit der Vorgänger", "wert": 38 / 60},
    {"iteration": 4, "kennzahl": "Sichtbarkeit der Vorgänger", "wert": 30 / 70},
]

PHASEN = [  # docs/phasen/01–06, Aktueller Stand (Iteration 5, Abschluss; Iteration 6 läuft)
    {"nr": 1, "phase": "Business Understanding", "stand": "begonnen", "kurz": "Idee angepasst: Vertragsliste mit Enddaten, ohne Terminprognose"},
    {"nr": 2, "phase": "Data Understanding", "stand": "begonnen", "kurz": "Laufzeitfelder verstanden; Höchstende nur im Freitext"},
    {"nr": 3, "phase": "Data Preparation", "stand": "aktiv", "kurz": "Vertragsliste je Los, Abdeckung 79,7 %"},
    {"nr": 4, "phase": "Modeling", "stand": "begonnen", "kurz": "Baseline R0/R1 getestet und verworfen"},
    {"nr": 5, "phase": "Evaluation", "stand": "aktiv", "kurz": "Backtest 28,8 %; Stichprobe der Liste in Prüfung"},
    {"nr": 6, "phase": "Deployment", "stand": "nicht begonnen", "kurz": "Prototyp der Liste in Iteration 6"},
]


SESSION_GAP = timedelta(minutes=90)  # Commits mit größerem Abstand gehören zu verschiedenen Arbeitssitzungen
SESSION_LEAD = timedelta(minutes=30)  # Arbeit vor dem ersten Commit einer Sitzung


def zeit_ist() -> list[dict]:
    """Arbeitssitzungen je Iteration aus den Commit-Zeiten (Untergrenze: Arbeit ohne Commit fehlt)."""
    def git(*args: str) -> str:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout.strip()
    dates = [datetime.fromisoformat(d) for d in git("log", "--reverse", "--format=%ad", "--date=iso-strict").splitlines()]
    ends = [(datetime.fromisoformat(git("log", "-1", "--format=%ad", "--date=iso-strict", f"iteration-{i}")), i)
            for i in range(1, 9) if git("tag", "-l", f"iteration-{i}")]
    def iteration(d: datetime) -> int:
        return next((i for end, i in ends if d <= end), len(ends) + 1)
    sessions: list[list[datetime]] = []
    for d in dates:
        if sessions and d - sessions[-1][-1] <= SESSION_GAP and iteration(d) == iteration(sessions[-1][-1]):  # wie src/zeitprotokoll.py
            sessions[-1].append(d)
        else:
            sessions.append([d])
    rows: dict[int, dict] = {}
    for s in sessions:
        r = rows.setdefault(iteration(s[0]), {"sitzungen": 0, "stunden": 0.0, "commits": 0})
        r["sitzungen"] += 1
        r["commits"] += len(s)
        r["stunden"] += (s[-1] - s[0] + SESSION_LEAD).total_seconds() / 3600
    return [{"iteration": i, "block": f"Iteration {i}", **{k: round(v, 1) if k == "stunden" else v for k, v in r.items()}}
            for i, r in sorted(rows.items())]


ZEIT_REST = [  # Schätzung der verbleibenden Stunden (Spanne); Grundlage je Zeile, Stand 2026-11-04 (ohne Kundenkontakt)
    {"block": "Iteration 6: Prüfung, Prototyp, Abschluss", "min": 5, "max": 10, "grundlage": "Plan der Iteration 6: etwa 2 Stunden Prüfung ohne KI-Hilfe, 3 bis 4 Sitzungen; Iteration 5 laut Git 4 bis 5 Stunden (Untergrenze)"},
    {"block": "Lab-Log, Folien und Fragenrunde", "min": 8, "max": 14, "grundlage": "Bewertungsbogen: Lab-Log 15 %, Vortrag 10 oder 15 Minuten, Fragenrunde; Inhalte liegen in den Iterationsdokumenten, Aufbereitung geschätzt"},
    {"block": "Markt, Angebot und Preis", "min": 2, "max": 6, "grundlage": "Offene Recherche-Aufgaben G1 und G3 im Projektplan; Grundlage aus docs/business.md §6 vorhanden"},
]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    treffer, lage = backtest()
    data = {"aufgaben": aufgaben(), "annahmen": annahmen(), "iterationen": ITERATIONEN, "schritte_it6": SCHRITTE_IT6,
            "kriterien_it5": KRITERIEN_IT5, "backtest": treffer, "backtest_lage": lage, "verlauf": VERLAUF, "phasen": PHASEN,
            "zeit_ist": zeit_ist(), "zeit_rest": ZEIT_REST}
    for name, rows in data.items():
        (OUT / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    a = data["aufgaben"]
    print(f"Aufgaben {sum(r['erledigt'] for r in a)}/{len(a)} erledigt; Annahmen {len(data['annahmen'])}")


if __name__ == "__main__":
    main()
