"""Abgrenzung der Population für Iteration 3 (siehe docs/iterationen.md, Abschnitt Iteration 3, „Begriffe“).

Festgelegt am 2026-10-23 anhand der Entwicklungsdaten (Q2 2026), bevor die Testdaten (Q3 2026) geladen wurden.

Population = Ausschreibung (competition), Auftraggeber DEU, Haupt-CPV beginnt mit 90910, 90911 oder 90919, keine
Änderungsbekanntmachung, und der Verfahrenstitel enthält keinen Begriff aus EXCLUDE_TERMS.

Bekannte Grenze: Einmalige Reinigungen ohne Ausschlussbegriff im Titel (z. B. „Neubau … – Grundreinigung“) bleiben drin.
"""

from analyze_completeness import flatten

CPV_PREFIXES = ("90910", "90911", "90919")

# Teilzeichenketten, Groß-/Kleinschreibung egal. Bewusst eng: „bau“ allein träfe z. B. „Montabaur“ oder „Unterhaltsreinigung Neubau“.
EXCLUDE_TERMS = (
    "baureinigung", "bauendreinigung", "baufeinreinigung", "bauschlussreinigung", "baugrobreinigung", "bauzwischenreinigung",
    "endreinigung",
    "schimmel",
    "fahrzeug",
    "industriereinigung",
    "schädling", "ratten",
)


def title(notice: dict) -> str:
    t = notice.get("title-proc") or {}
    if isinstance(t, dict) and t.get("deu"):
        return str(t["deu"])
    vals = flatten(t)
    return str(vals[0]) if vals else ""


def main_cpv(notice: dict) -> str:
    vals = flatten(notice.get("main-classification-proc"))
    return str(vals[0]) if vals else ""


def exclusion_reason(notice: dict) -> str | None:
    """None, wenn die Notice zur Population gehört, sonst der Grund."""
    if notice.get("change-notice-version-identifier"):
        return "Änderungsbekanntmachung"
    if not main_cpv(notice).startswith(CPV_PREFIXES):
        return f"Haupt-CPV {main_cpv(notice)[:5] or '(leer)'}"
    low = title(notice).lower()
    hit = next((term for term in EXCLUDE_TERMS if term in low), None)
    return f"Titel enthält „{hit}“" if hit else None
