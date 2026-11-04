"""Iteration 8, Schritt 2: Antworten der Leser (je 4 Teilläufe) zu einer CSV je Leser zusammenführen; nur Format, kein Inhalt.

Rohantworten unverändert in reports/zweitlesung_iteration8_roh/leser_{a,b}_teil{1-4}.txt (Schlussantwort der Subagenten, Codeblock-Zeilen plus HINWEIS-Zeile).
Formatregel (festgelegt nach dem Eintreffen, bevor eine Antwort mit der Liste verglichen wurde): Einige Leser schrieben Semikolons ins Zitat.
Deshalb gilt: Feld 1 bis 3 = Nr, ende_grundlaufzeit, hoechstende; letztes Feld = gebaeudereinigung; alles dazwischen = Zitat (Semikolons darin werden zu Kommas).
Zeilen ab „HINWEIS:“ und Folgezeilen gehen nicht in die CSV, sondern in reports/zweitlesung_iteration8_hinweise.md.
Außerdem: Prüfung der Subagenten-Protokolle (benutzte Werkzeuge, URLs außerhalb von ted.europa.eu) → in dieselbe Datei.

Aufruf:  .venv\\Scripts\\python -I src/prepare/zweitlesung_iteration8_zusammenfuehren.py [Ordner der Subagenten-Protokolle]
"""

import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ROH = ROOT / "reports" / "zweitlesung_iteration8_roh"
HINWEISE = ROOT / "reports" / "zweitlesung_iteration8_hinweise.md"
ERWARTET = [f"L{i}" for i in range(1, 96)] + ["K1", "K2", "K3"]
FELDER = ["Nr", "ende_grundlaufzeit", "hoechstende", "zitat", "gebaeudereinigung"]
# Teillauf → Agenten-ID (für die Prüfung der Protokolle)
AGENTEN = {"A1": "a45eeccfb4d68c9f2", "A2": "a014717c9e0719b8a", "A3": "a66f828daa2538a5c", "A4": "ab4851b628d4c2064",
           "B1": "a8e92166bff79c2e2", "B2": "ad9c43833f575569f", "B3": "ad76eafe94e8c82bc", "B4": "a03a396caf55b1e9e"}


def zerlegen(zeile: str) -> dict:
    t = [x.strip() for x in zeile.split(";")]
    assert len(t) >= 5, zeile
    return dict(zip(FELDER, [t[0], t[1], t[2], ", ".join(t[3:-1]), t[-1]]))


def protokolle(ordner: Path) -> list[str]:
    out = ["", "## Prüfung der Subagenten-Protokolle", "", "| Teillauf | Modell | Werkzeuge | URLs außerhalb ted.europa.eu |", "|---|---|---|---|"]
    for teil, aid in AGENTEN.items():
        c, fremd, modell = Counter(), set(), "?"
        for line in (ordner / f"agent-{aid}.jsonl").open(encoding="utf-8"):
            msg = json.loads(line).get("message", {})
            if not isinstance(msg, dict):
                continue
            modell = msg.get("model", modell)
            for b in msg.get("content") if isinstance(msg.get("content"), list) else []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    c[b["name"]] += 1
                    url = b.get("input", {}).get("url", "")
                    if url and "ted.europa.eu" not in url:
                        fremd.add(url)
        out.append(f"| {teil} | {modell} | {', '.join(f'{k} {v}' for k, v in sorted(c.items()))} | {', '.join(sorted(fremd)) or '–'} |")
    return out


def main() -> None:
    hinweise = ["# Hinweise der Leser und Prüfung der Protokolle (Iteration 8)", "",
                "_Erzeugt mit `src/prepare/zweitlesung_iteration8_zusammenfuehren.py`. Die Hinweise sind die Schlusszeilen der Leser, unverändert._"]
    for leser in "ab":
        zeilen, hw = [], []
        for teil in range(1, 5):
            text = (ROH / f"leser_{leser}_teil{teil}.txt").read_text(encoding="utf-8").splitlines()
            i = next((k for k, z in enumerate(text) if z.startswith("HINWEIS")), len(text))
            zeilen += [zerlegen(z) for z in text[:i] if z.strip()]
            hw += [f"- **Teil {teil}:** " + " ".join(text[i:]).strip()] if i < len(text) else []
        assert [z["Nr"] for z in zeilen] == ERWARTET, f"Leser {leser}: Nummern unvollständig oder in falscher Reihenfolge"
        with (ROOT / "reports" / f"zweitlesung_iteration8_leser_{leser}.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FELDER, delimiter=";")
            w.writeheader()
            w.writerows(zeilen)
        hinweise += ["", f"## Leser {leser.upper()} ({'Opus' if leser == 'a' else 'Sonnet'})", "", *hw]
    if len(sys.argv) > 1:
        hinweise += protokolle(Path(sys.argv[1]))
    HINWEISE.write_text("\n".join(hinweise) + "\n", encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main()
