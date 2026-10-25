"""Abgrenzung der Population für Iteration 4 (siehe docs/iterationen.md, Abschnitt Iteration 4, „Begriffe“).

Festgelegt am 2026-10-25 anhand der Entwicklungsdaten (Q2 und Q3 2026), bevor die Testdaten (Q1 2026) geladen wurden.

Population = Regel aus Iteration 3 (competition, Auftraggeber DEU, Haupt-CPV 90910/90911/90919, keine Änderungsbekanntmachung,
kein Begriff aus EXCLUDE_TERMS im Verfahrenstitel) und zusätzlich:
- Lose: Enthält **jeder** Los-Titel einen Begriff aus EXCLUDE_TERMS, ist die Bekanntmachung ausgeschlossen. Einzelne Lose
  (z. B. ein Los „Fahrzeugreinigung“ neben Unterhaltsreinigung) schließen nicht aus.
- Bauprojekt: Der Verfahrenstitel enthält einen Begriff aus BAU_TERMS und weder Verfahrenstitel noch Los-Titel enthalten einen
  Begriff aus RECURRING_TERMS (Anlass: T16 „Umbau und Sanierung der Nikolaikirche …“, Los „Gebäudereinigung“).

Wirkung auf den Entwicklungsdaten (Q2 + Q3 2026): 6 zusätzliche Ausschlüsse (508745, 534873, 559458 = T16, 567616, 580419,
586704-2026), alle einmalige Reinigungen in Bauprojekten. Bekannte Grenze: Beschreibungen (BT-24) sind nicht in den Rohdaten;
Grenzfälle wie „Neubau … – Grundreinigung“ bleiben drin.

Außerdem für die Testprobe: KNOWN_FILE listet alle Notices mit Jahr 2026, die bis zum Commit dieser Datei in reports/ oder docs/
vorkommen. Sie werden nicht als Testfall gezogen (Q1-2026-Notices waren in Iteration 2/3 teils Vorgänger-Kandidaten).

Aufruf (schreibt KNOWN_FILE einmalig, danach nicht mehr ändern):
    python -I src/population_iteration4.py --bekannte-notices
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWN_FILE = PROJECT_ROOT / "reports" / "bekannte_notices_iteration4.txt"

TEST_FROM, TEST_TO = "20260101", "20260331"
TEST_SIZE = 70
TEST_SEED = 20261026
MAX_PER_BUYER = 2

CPV_PREFIXES = ("90910", "90911", "90919")

# Wie Iteration 3 (src/population_iteration3.py), Teilzeichenketten, Groß-/Kleinschreibung egal.
EXCLUDE_TERMS = (
    "baureinigung", "bauendreinigung", "baufeinreinigung", "bauschlussreinigung", "baugrobreinigung", "bauzwischenreinigung",
    "endreinigung",
    "schimmel",
    "fahrzeug",
    "industriereinigung",
    "schädling", "ratten",
)
BAU_TERMS = ("umbau", "neubau", "sanierung", "erweiterung", "rohbau", "modernisierung")
RECURRING_TERMS = ("unterhalt", "uhr", "glas", "grundreinigung", "fenster", "rahmenvertrag", "rahmenvereinbarung", "jährlich",
                   "laufend")


def flatten(value) -> list:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [x for v in value for x in flatten(v)]
    if isinstance(value, dict):
        return [x for v in value.values() for x in flatten(v)]
    return [value]


def _deu(value) -> list[str]:
    if isinstance(value, dict) and value.get("deu"):
        value = value["deu"]
    return [str(x) for x in flatten(value)]


def title(notice: dict) -> str:
    vals = _deu(notice.get("title-proc"))
    return vals[0] if vals else ""


def lot_titles(notice: dict) -> list[str]:
    return _deu(notice.get("title-lot"))


def main_cpv(notice: dict) -> str:
    vals = flatten(notice.get("main-classification-proc"))
    return str(vals[0]) if vals else ""


def _hit(text: str, terms: tuple[str, ...]) -> str | None:
    low = text.lower()
    return next((t for t in terms if t in low), None)


def exclusion_reason(notice: dict) -> str | None:
    """None, wenn die Notice zur Population gehört, sonst der Grund."""
    if notice.get("change-notice-version-identifier"):
        return "Änderungsbekanntmachung"
    if not main_cpv(notice).startswith(CPV_PREFIXES):
        return f"Haupt-CPV {main_cpv(notice)[:5] or '(leer)'}"
    if hit := _hit(title(notice), EXCLUDE_TERMS):
        return f"Titel enthält „{hit}“"
    lots = lot_titles(notice)
    if lots and all(_hit(lot, EXCLUDE_TERMS) for lot in lots):
        return f"alle Los-Titel mit Ausschlussbegriff („{_hit(lots[0], EXCLUDE_TERMS)}“)"
    if (bau := _hit(title(notice), BAU_TERMS)) and not _hit(" ".join([title(notice)] + lots), RECURRING_TERMS):
        return f"Bauprojekt („{bau}“) ohne wiederkehrende Reinigung"
    return None


def write_known() -> None:
    if KNOWN_FILE.exists():
        sys.exit(f"{KNOWN_FILE} existiert bereits und wird nicht überschrieben.")
    found = set()
    for folder in ("reports", "docs"):
        for f in (PROJECT_ROOT / folder).rglob("*"):
            if f.is_file() and f.suffix in (".md", ".csv", ".txt"):
                found |= set(re.findall(r"(?<![\w-])(\d{1,6}-2026)(?!\d)", f.read_text(encoding="utf-8", errors="ignore")))
    numbers = sorted(found, key=lambda s: int(s.split("-")[0]))
    KNOWN_FILE.write_text("\n".join(numbers) + "\n", encoding="utf-8")
    print(f"{len(numbers)} Notices mit Jahr 2026 nach {KNOWN_FILE.relative_to(PROJECT_ROOT)} geschrieben")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--bekannte-notices", action="store_true", help="Liste bekannter 2026-Notices einmalig schreiben")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if args.bekannte_notices:
        write_known()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
