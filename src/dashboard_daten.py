"""Daten für das Dashboard „Vergabe-Radar Projektstand“ aus den Projektdokumenten.

Schreibt JSON-Dateien (Liste von Zeilen) nach data/processed/dashboard/:
- aufgaben.json     aus docs/projektplan.md: Aufgaben erster Ebene der Stränge T und G mit Haken (Strang P sind Daueraufgaben)
- annahmen.json     aus docs/annahmen.md: ID, Kurztext, Risiko, Status
- iterationen.json  Iterationen 1–8 mit Status und Entscheidung (docs/iterationen.md, Übersicht)
- schritte_it4.json Plan der laufenden Iteration 4 (docs/iterationen.md, Abschnitt Iteration 4)
- kriterien_it4.json W1–W6 (reports/zuordnung_iteration4.md, sichtbarkeit_iteration4_gt.csv)
- verlauf.json      Zuordnung über die Iterationen (ergebnis/evaluation der Iterationen 2–4)
- phasen.json       Stand der CRISP-DM-Phasen (docs/phasen/01–06)
- zeit_ist.json     Arbeitssitzungen je Iteration aus den Commit-Zeiten (git log, Untergrenze)
- zeit_rest.json    Schätzung der verbleibenden Stunden je Block, mit Grundlage

Aufruf:
    python -I src/dashboard_daten.py
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
                   "T3": "Iteration 5: Erste Prognose und Backtest", "T4": "Iteration 6: Verbesserung der Prognose",
                   "T5": "Iteration 7: Prototyp der Vertragsliste", "T6": "Iteration 8: Ausbau oder Neuausrichtung",
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


ITERATIONEN = [  # docs/iterationen.md, Übersicht (Stand 2026-10-28)
    {"nr": 1, "fokus": "Machbarkeit der Daten", "status": "abgeschlossen", "entscheidung": "Gebäudereinigung als Arbeitsnische, zurück zu Phase 2"},
    {"nr": 2, "fokus": "Neuausschreibungen zuordenbar über den Auftraggeber?", "status": "abgeschlossen", "entscheidung": "Idee anpassen: Zuordnung über das Objekt"},
    {"nr": 3, "fokus": "Sichtbarkeit und Zuordnung über das Objekt", "status": "abgeschlossen", "entscheidung": "In Phase 2/3 bleiben, letzter Verbesserungsversuch"},
    {"nr": 4, "fokus": "Letzter Verbesserungsversuch der Zuordnung", "status": "läuft", "entscheidung": "offen (Blindprüfung W4 fehlt)"},
    {"nr": 5, "fokus": "Erste Prognose und Backtest", "status": "geplant", "entscheidung": "–"},
    {"nr": 6, "fokus": "Verbesserung der Prognose", "status": "geplant", "entscheidung": "–"},
    {"nr": 7, "fokus": "Prototyp der Vertragsliste", "status": "geplant", "entscheidung": "–"},
    {"nr": 8, "fokus": "Ausbau oder Neuausrichtung", "status": "geplant", "entscheidung": "–"},
]

SCHRITTE_IT4 = [  # docs/iterationen.md, Iteration 4, Plan
    {"nr": 1, "schritt": "Aufräumen, Population, Rechercheur auf Regeln 1.1", "status": "erledigt", "commit": "71e5d57"},
    {"nr": 2, "schritt": "Merkmale je Los (auch vor eForms)", "status": "erledigt", "commit": "98909dd"},
    {"nr": 3, "schritt": "Regel verbessern und einfrieren", "status": "erledigt", "commit": "1d0e060"},
    {"nr": 4, "schritt": "Testprobe Q1 2026 und Handsuche (70 Fälle)", "status": "erledigt", "commit": "d43c547"},
    {"nr": 5, "schritt": "Regel auf Testdaten, Paarbeurteilung", "status": "erledigt", "commit": "ec4733e"},
    {"nr": 6, "schritt": "Blindprüfung W4 durch dich (20 Paare, Prüfzeit)", "status": "in Arbeit", "commit": ""},
    {"nr": 7, "schritt": "Report, Evaluator, /iteration-ende", "status": "offen", "commit": ""},
]

KRITERIEN_IT4 = [  # reports/zuordnung_iteration4.md (ec4733e); Anteile 0–1, W5 Anzahl pro Jahr
    {"id": "W1", "name": "Sichtbarkeit", "wert": 30 / 70, "schwelle": 0.50, "max": 1, "einheit": "Anteil", "anzeige": "30 von 70",
     "status": "verfehlt", "hinweis": "Fälle mit objektgleichem Vorgänger oder Teilmenge auf TED"},
    {"id": "W2", "name": "Präzision", "wert": 17 / 19, "schwelle": 0.80, "max": 1, "einheit": "Anteil", "anzeige": "17 von 19",
     "status": "knapp", "hinweis": "Quote erfüllt, aber nur 19 statt mindestens 25 Vorschläge"},
    {"id": "W3", "name": "Trefferquote", "wert": 17 / 30, "schwelle": 0.60, "max": 1, "einheit": "Anteil", "anzeige": "17 von 30",
     "status": "verfehlt", "hinweis": "Vorgänger, die die Regel korrekt findet"},
    {"id": "W4", "name": "Zweitprüfung", "wert": None, "schwelle": 0.85, "max": 1, "einheit": "Anteil", "anzeige": "steht aus",
     "status": "offen", "hinweis": "Deine Blindprüfung, 20 Paare"},
    {"id": "W5", "name": "Backtest-Basis", "wert": 189, "schwelle": 100, "max": 400, "einheit": "pro Jahr", "anzeige": "189 pro Jahr",
     "status": "erfüllt", "hinweis": "Korrekte Paare mit Vertragsende, auf 1.893 Verfahren pro Jahr hochgerechnet"},
    {"id": "W6", "name": "Kandidatenliste", "wert": 22 / 30, "schwelle": 0.70, "max": 1, "einheit": "Anteil", "anzeige": "22 von 30",
     "status": "erfüllt", "hinweis": "Vorgänger unter den drei besten Kandidaten"},
]

VERLAUF = [  # Iteration 2: reports/ergebnis_iteration2.md (K2); 3: zuordnung_iteration3.md; 4: zuordnung_iteration4.md
    {"iteration": 2, "kennzahl": "Präzision der Zuordnung", "wert": 5 / 30},
    {"iteration": 3, "kennzahl": "Präzision der Zuordnung", "wert": 11 / 24},
    {"iteration": 4, "kennzahl": "Präzision der Zuordnung", "wert": 17 / 19},
    {"iteration": 3, "kennzahl": "Trefferquote", "wert": 11 / 38},
    {"iteration": 4, "kennzahl": "Trefferquote", "wert": 17 / 30},
    {"iteration": 3, "kennzahl": "Sichtbarkeit der Vorgänger", "wert": 38 / 60},
    {"iteration": 4, "kennzahl": "Sichtbarkeit der Vorgänger", "wert": 30 / 70},
]

PHASEN = [  # docs/phasen/01–06, Aktueller Stand
    {"nr": 1, "phase": "Business Understanding", "stand": "begonnen", "kurz": "Nische vorläufig, Recherche ohne Kundenkontakt"},
    {"nr": 2, "phase": "Data Understanding", "stand": "aktiv", "kurz": "Sichtbarkeit und Zuordnung gemessen"},
    {"nr": 3, "phase": "Data Preparation", "stand": "aktiv", "kurz": "Merkmale je Los, Regel eingefroren"},
    {"nr": 4, "phase": "Modeling", "stand": "nicht begonnen", "kurz": "Erste Prognose in Iteration 5"},
    {"nr": 5, "phase": "Evaluation", "stand": "nicht begonnen", "kurz": "Backtest in Iteration 5"},
    {"nr": 6, "phase": "Deployment", "stand": "nicht begonnen", "kurz": "Prototyp in Iteration 7"},
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
        if sessions and d - sessions[-1][-1] <= SESSION_GAP:
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


ZEIT_REST = [  # Schätzung der verbleibenden Stunden (Spanne); Grundlage je Zeile, Stand 2026-10-29 (ohne Kundenkontakt)
    {"block": "Iteration 4: Blindprüfung W4", "min": 1.5, "max": 2, "grundlage": "Planwert in docs/iterationen.md (etwa 1,5 Stunden)"},
    {"block": "Iteration 4: Abschluss", "min": 1, "max": 2, "grundlage": "Abschluss Iteration 3 (Report, Evaluator, Dokumente)"},
    {"block": "Iteration 5: Prognose und Backtest", "min": 4, "max": 10, "grundlage": "Iterationen 2–4 laut Git 3,8–4,8 h (Untergrenze); obere Grenze geschätzt"},
    {"block": "Iteration 6: Verbesserung", "min": 4, "max": 10, "grundlage": "wie Iteration 5"},
    {"block": "Iteration 7: Prototyp", "min": 4, "max": 10, "grundlage": "wie Iteration 5; Liste bauen und gegen den Backtest prüfen"},
    {"block": "Markt, Angebot und Preis", "min": 4, "max": 8, "grundlage": "Annahme für G1 und G3 im Projektplan (Schreibtisch-Recherche)"},
]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    data = {"aufgaben": aufgaben(), "annahmen": annahmen(), "iterationen": ITERATIONEN, "schritte_it4": SCHRITTE_IT4,
            "kriterien_it4": KRITERIEN_IT4, "verlauf": VERLAUF, "phasen": PHASEN, "zeit_ist": zeit_ist(), "zeit_rest": ZEIT_REST}
    for name, rows in data.items():
        (OUT / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    a = data["aufgaben"]
    print(f"Aufgaben {sum(r['erledigt'] for r in a)}/{len(a)} erledigt; Annahmen {len(data['annahmen'])}")


if __name__ == "__main__":
    main()
