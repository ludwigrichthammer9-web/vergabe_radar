"""Lab-Log (Bewertung Teil 5): fügt Zeitprotokoll und KI-Irrwege in die Vorlage ein.

Eingaben: docs/lab_log_vorlage.md (Platzhalter {{ZEIT}}, {{KI_IRRWEGE}}), docs/zeitprotokoll.md (Übersichtstabelle), docs/ki_irrwege.md (Tabelle).
Aufruf:  .venv\\Scripts\\python -I src/report/lab_log.py      Ausgabe: docs/lab_log.md
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DOCS = ROOT / "docs"


def tabelle(text: str, ab: int = 0) -> str:
    """Erste zusammenhängende Markdown-Tabelle nach Zeile `ab`."""
    zeilen = text.splitlines()
    start = next(i for i in range(ab, len(zeilen)) if zeilen[i].startswith("|"))
    ende = start
    while ende < len(zeilen) and zeilen[ende].startswith("|"):
        ende += 1
    return "\n".join(zeilen[start:ende])


def main() -> None:
    vorlage = (DOCS / "lab_log_vorlage.md").read_text(encoding="utf-8")
    zeit = tabelle((DOCS / "zeitprotokoll.md").read_text(encoding="utf-8"))
    irrwege = tabelle((DOCS / "ki_irrwege.md").read_text(encoding="utf-8"))
    out = vorlage.replace("{{ZEIT}}", zeit).replace("{{KI_IRRWEGE}}", irrwege)
    (DOCS / "lab_log.md").write_text(out, encoding="utf-8")
    print(f"{len(out.split())} Wörter; {len(irrwege.splitlines()) - 2} Irrwege; docs/lab_log.md")


if __name__ == "__main__":
    main()
