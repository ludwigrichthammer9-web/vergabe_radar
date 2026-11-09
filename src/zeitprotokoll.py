"""Zeitprotokoll aus der Git-Historie (Bewertung LN C, Teil 5: Arbeitsschritte mit Zeitaufwand).

Methode wie in src/dashboard_daten.py: Commits mit höchstens 90 Minuten Abstand bilden eine Arbeitssitzung; Dauer = Zeit vom ersten bis
zum letzten Commit plus 30 Minuten Vorlauf; eine Sitzung wird am Iterationstag geteilt. Iteration = Zeitraum bis zum jeweiligen Git-Tag `iteration-N`. Untergrenze: Arbeit ohne Commit
(Lesen, Prüfen von Hand, Recherche) fehlt; die Zeit, in der Claude rechnet, ist enthalten.

Aufruf:  python -I src/zeitprotokoll.py      Ausgabe: docs/zeitprotokoll.md
"""

import subprocess
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "zeitprotokoll.md"
GAP, LEAD = timedelta(minutes=90), timedelta(minutes=30)


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout.strip()


def main() -> None:
    commits = [(datetime.fromisoformat(d), s) for d, s in
               (line.split("|", 1) for line in git("log", "--reverse", "--format=%ad|%s", "--date=iso-strict").splitlines())]
    ends = [(datetime.fromisoformat(git("log", "-1", "--format=%ad", "--date=iso-strict", f"iteration-{i}")), i)
            for i in range(1, 12) if git("tag", "-l", f"iteration-{i}")]

    def iteration(d: datetime) -> int:
        return next((i for end, i in ends if d <= end), len(ends) + 1)

    sessions: list[list[tuple[datetime, str]]] = []
    for c in commits:
        if sessions and c[0] - sessions[-1][-1][0] <= GAP and iteration(c[0]) == iteration(sessions[-1][-1][0]):
            sessions[-1].append(c)
        else:
            sessions.append([c])

    rows, total = {}, {}
    for s in sessions:
        h = (s[-1][0] - s[0][0] + LEAD).total_seconds() / 3600
        it = iteration(s[0][0])
        rows.setdefault(it, []).append((s, h))
        total[it] = total.get(it, 0) + h

    out = ["# Zeitprotokoll (aus der Git-Historie)", "",
           f"_Erzeugt mit `src/zeitprotokoll.py` am {datetime.now():%Y-%m-%d}. Methode: Commits mit höchstens 90 min Abstand = eine "
           "Sitzung; Dauer = erster bis letzter Commit + 30 min Vorlauf. **Untergrenze:** Arbeit ohne Commit (Lesen, Handprüfung, "
           "Recherche, Gespräche) fehlt; die Rechenzeit von Claude ist enthalten. Beiträge anderer Personen (Kommilitone) stehen nicht "
           "im Git und werden unten von Hand ergänzt._", "",
           "| Iteration | Sitzungen | Commits | Stunden (Untergrenze) |", "|---|---|---|---|"]
    for it in sorted(rows):
        out.append(f"| {it} | {len(rows[it])} | {sum(len(s) for s, _ in rows[it])} | {total[it]:.1f} |")
    out.append(f"| **Summe** | {sum(len(r) for r in rows.values())} | {len(commits)} | **{sum(total.values()):.1f}** |")
    out.append("")
    for it in sorted(rows):
        out += [f"## Iteration {it}", "", "| Tag | Zeit | Commits | Std. | Erster / letzter Commit |", "|---|---|---|---|---|"]
        for s, h in rows[it]:
            a, b = s[0], s[-1]
            first, last = a[1][:70], b[1][:70]
            out.append(f"| {a[0]:%Y-%m-%d} | {a[0]:%H:%M}–{b[0]:%H:%M} | {len(s)} | {h:.1f} | {first}" +
                       (f" / {last}" if len(s) > 1 else "") + " |")
        out.append("")
    out += ["## Ergänzungen von Hand (nicht im Git)", "",
            "| Datum | Person | Tätigkeit | Std. |", "|---|---|---|---|",
            "| 2026-11-05 | Nutzer | Gespräche Iteration 10 (W5): Vorbereitung, 9 Anrufe, Abtippen (business.md §8.9) | 1.75 |",
            "| 2026-11-05 | Kommilitone (Manuel Strobel) | Lesen von 15 Losen im TED-Original (Iteration 9, V6) | offen |",
            "| 2026-11-03 | Kommilitone (Manuel Strobel) | Zweitprüfung P14–P71 (Iteration 5; Angabe des Nutzers) | offen |",
            "| | Kommilitone (Manuel Strobel) | Präsentation/Umsetzung der Folien (Angabe des Nutzers, 2026-11-03) | offen |",
            "| 2026-11-08 | Kommilitone (Manuel Strobel) | Erstellung der Video-Animation „Franz und die Glaskugel“ (KI-gestützt), danach Überarbeitung abwechselnd mit dem Nutzer (Angabe des Nutzers, 2026-11-09) | offen (laut Nutzer in den rund 30 Stunden je Person enthalten) |",
            "| | | weitere Handarbeit (Zweitprüfungen, Handprüfungen der Iterationen 5 bis 7) | offen |", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(sessions)} Sitzungen, {sum(total.values()):.1f} h; {OUT}")


if __name__ == "__main__":
    main()
