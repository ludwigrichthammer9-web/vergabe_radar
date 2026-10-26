"""Überträgt die Übersichtstabellen der Handsuche (reports/sichtbarkeit_iteration4_teil1–5.md) in eine Ground-Truth-Tabelle.

Ergebnis: reports/sichtbarkeit_iteration4_gt.csv (Semikolon), eine Zeile je Testfall U1–U70:
    U;notice;kategorie;tendenz;vorgaenger;kandidat_unklar;vertrag;ende;herkunft;vorzeitig
- vorgaenger: alle Notices desselben Vorgängers (nur bei objektgleich_*/teilmenge), durch Leerzeichen getrennt
- kandidat_unklar: bei „unklar“ der beste Kandidat (nur informativ, zählt nicht als Vorgänger)
Prüft, dass Reihenfolge und Notice-Nummern mit reports/testfaelle_iteration4.txt übereinstimmen.

Aufruf:
    python -I src/gt_iteration4.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
NOTICE = re.compile(r"\b\d{1,6}-20\d\d\b")
KATEGORIEN = ("objektgleich_hoch", "objektgleich_mittel", "teilmenge", "unklar", "kein_vorgaenger")


def rows(path: Path) -> list[list[str]]:
    text = path.read_text(encoding="utf-8")
    table = text.split("## Übersichtstabelle", 1)[1].split("\n## ", 1)[0]
    out = []
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"\**U\d+\**", cells[0]):
            out.append(cells)
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    expected = (REPORTS / "testfaelle_iteration4.txt").read_text(encoding="utf-8").split()
    lines = ["U;notice;kategorie;tendenz;vorgaenger;kandidat_unklar;vertrag;ende;herkunft;vorzeitig"]
    counts: dict[str, int] = {}
    for i in range(1, 6):
        for c in rows(REPORTS / f"sichtbarkeit_iteration4_teil{i}.md"):
            u = c[0].strip("*")
            nr = int(u[1:])
            notice = NOTICE.search(c[1]).group(0)
            if expected[nr - 1] != notice:
                sys.exit(f"{u}: {notice} passt nicht zu testfaelle_iteration4.txt ({expected[nr - 1]})")
            kat = next((k for k in KATEGORIEN if k in c[2].replace("*", "")), None)
            if kat is None:
                sys.exit(f"{u}: unbekannte Kategorie „{c[2]}“")
            preds = " ".join(dict.fromkeys(NOTICE.findall(c[4] + " " + c[5])))
            found = kat != "unklar" and kat != "kein_vorgaenger"
            clean = [re.sub(r"[;\n]", ",", x) for x in c[3:10]]
            lines.append(";".join([u, notice, kat, clean[0], preds if found else "", preds if kat == "unklar" else ""]
                                  + [" ".join(NOTICE.findall(c[6])) or "–", clean[4], clean[5], clean[6]]))
            counts[kat] = counts.get(kat, 0) + 1
    if len(lines) - 1 != len(expected):
        sys.exit(f"{len(lines) - 1} Zeilen statt {len(expected)}")
    (REPORTS / "sichtbarkeit_iteration4_gt.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(lines) - 1} Fälle übertragen:", counts)


if __name__ == "__main__":
    main()
