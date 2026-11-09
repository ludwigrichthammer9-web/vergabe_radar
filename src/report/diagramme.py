"""Zwei Diagramme zur Terminprognose (Iteration 5) für Lab-Log und Folien.

1. docs/lab_log_bilder/diagramm_abweichung.png: Abweichung der Prognose R1 (Höchstende − 6 Monate) von der tatsächlichen
   Veröffentlichung der Neuausschreibung, 52 Paare, mit dem Trefferfenster ±3 Monate.
2. docs/lab_log_bilder/diagramm_vorlauf.png: Trefferquote von R1 und R0 für Vorlauf 0 bis 24 Monate (Fenster ±3), mit der
   vorab festgelegten Schwelle 60 %. Nachträgliche Darstellung (Sensitivität), kein neuer Test.

Daten: Tabelle „Alle Paare“ in reports/backtest_iteration5.md (im Git); Rechnung wie src/model/sensitivitaet_backtest.py.
Abhängigkeit: matplotlib (requirements.txt).
Aufruf:  .venv\\Scripts\\python.exe -I src/report/diagramme.py
"""

import re
import statistics
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src" / "model"))
from sensitivitaet_backtest import QUELLE, lade_paare, treffer  # noqa: E402

AUS = ROOT / "docs" / "lab_log_bilder"
BLAU, GRAU, ROT, GRUEN, TEXT, LINIE = "#007AFF", "#8E8E93", "#FF3B30", "#34C759", "#1C1C1E", "#D1D1D6"
plt.rcParams.update({"font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 12, "axes.edgecolor": LINIE,
                     "axes.labelcolor": TEXT, "xtick.color": TEXT, "ytick.color": TEXT, "axes.spines.top": False,
                     "axes.spines.right": False})


def abweichungen():
    """Spalte „Abw. R1 (Mon.)“ der Tabelle „Alle Paare“ (positiv = Ausschreibung kam später als die Prognose)."""
    werte = []
    for zeile in QUELLE.read_text(encoding="utf-8").splitlines():
        teile = [t.strip() for t in zeile.strip().strip("|").split("|")]
        if len(teile) == 10 and re.match(r"^[A-Z]\d+$", teile[0]):
            werte.append(float(teile[7]))
    return werte


def diagramm_abweichung():
    w = abweichungen()
    assert len(w) == 52, len(w)
    im_fenster = sum(-3 <= x <= 3 for x in w)
    fig, ax = plt.subplots(figsize=(9, 3.6), dpi=200)
    grenzen = list(range(-42, 97, 3))   # alle 52 Paare (Minimum −38,3, Maximum +95,0 Monate)
    ax.axvspan(-3, 3, color=GRUEN, alpha=0.15, lw=0)
    ax.hist([x for x in w if -3 <= x <= 3], bins=grenzen, color=GRUEN, edgecolor="white")
    ax.hist([x for x in w if not -3 <= x <= 3], bins=grenzen, color=GRAU, edgecolor="white")
    ax.set_xlabel("Abweichung der Prognose in Monaten (negativ = Ausschreibung kam früher)")
    ax.set_ylabel("Zahl der Paare")
    ax.set_xlim(-42, 96)
    ax.text(5, ax.get_ylim()[1] * 0.9, f"grün = Treffer (±3 Monate): {im_fenster} von {len(w)}", ha="left", color=TEXT,
            fontsize=11, fontweight="bold")
    ax.set_title(f"Im Mittel fast richtig (Median {statistics.median(w):+.1f} Monate), im Einzelfall Jahre daneben".replace(".", ","),
                 loc="left", fontsize=12, color=TEXT)
    fig.tight_layout()
    fig.savefig(AUS / "diagramm_abweichung.png")
    plt.close(fig)
    return im_fenster, statistics.median(w)


def diagramm_vorlauf():
    paare = lade_paare()
    n = len(paare)
    v = list(range(25))
    r1 = [100 * sum(treffer(paare, "R1", x, 3)) / n for x in v]
    r0 = [100 * sum(treffer(paare, "R0", x, 3)) / n for x in v]
    fig, ax = plt.subplots(figsize=(8, 3.6), dpi=200)
    ax.axhline(60, color=ROT, lw=1.5, ls="--")
    ax.text(24, 61.5, "Schwelle 60 % (vorab festgelegt)", ha="right", color=ROT, fontsize=11)
    ax.plot(v, r1, color=BLAU, lw=2.2, marker="o", ms=4, label="R1: spätestes Vertragsende − Vorlauf")
    ax.plot(v, r0, color=GRAU, lw=1.8, marker="o", ms=3, label="R0: Ende der Grundlaufzeit − Vorlauf")
    ax.scatter([6], [r1[6]], s=90, color=BLAU, zorder=5)
    ax.annotate(f"6 Monate (vorab): {r1[6]:.1f} %".replace(".", ","), (6, r1[6]), xytext=(9, r1[6] + 9), color=TEXT, fontsize=11,
                arrowprops={"arrowstyle": "-", "color": GRAU})
    ax.set_xlabel("Vorlauf in Monaten (Trefferfenster ±3 Monate)")
    ax.set_ylabel("Treffer in %")
    ax.set_ylim(0, 70)
    ax.set_xlim(-0.5, 24.5)
    ax.legend(loc="upper right", bbox_to_anchor=(1, 0.88), frameon=False, fontsize=10)
    ax.set_title("Kein Vorlauf erreicht die Schwelle (nachträglich auf denselben 52 Paaren)", loc="left",
                 fontsize=12, color=TEXT)
    fig.tight_layout()
    fig.savefig(AUS / "diagramm_vorlauf.png")
    plt.close(fig)
    return max(r1)


if __name__ == "__main__":
    k, med = diagramm_abweichung()
    best = diagramm_vorlauf()
    print(f"diagramm_abweichung.png: {k}/52 im Fenster, Median {med:+.1f}; diagramm_vorlauf.png: bestes R1 {best:.1f} %")
