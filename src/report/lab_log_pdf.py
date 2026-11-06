"""Lab-Log als PDF: docs/lab_log.md -> HTML (markdown) -> PDF (Microsoft Edge oder Chrome, headless).

Aufruf:  python -I src/report/lab_log_pdf.py      Ausgabe: docs/lab_log.pdf
Relative Links (../reports/...) bleiben im PDF Text bzw. führen ins Repo; die HTML-Zwischendatei liegt neben dem PDF und wird gelöscht.
"""

import subprocess
import sys
import tempfile
import time
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent.parent
MD, HTML, PDF = ROOT / "docs" / "lab_log.md", ROOT / "docs" / "_lab_log.html", ROOT / "docs" / "lab_log.pdf"
BROWSER = [Path(p) for p in (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                             r"C:\Program Files\Google\Chrome\Application\chrome.exe")]
PROFIL = Path(tempfile.gettempdir()) / "lab_log_pdf_profil"  # eigenes Profil, damit ein laufender Browser den Aufruf nicht schluckt
CSS = """
/* Gestaltung nach Apple Human Interface Guidelines (Klarheit, Zurückhaltung, Tiefe); nur Light-Mode, da Druck. 8-Punkt-Raster. */
@page { size: A4; margin: 14mm 13mm; }
:root { --text: #1C1C1E; --grau: #8E8E93; --flaeche: #F2F2F7; --linie: #E5E5EA; --blau: #007AFF; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", system-ui, "Segoe UI", sans-serif;
       font-size: 9.2pt; line-height: 1.4; color: var(--text); }
h1 { font-size: 24pt; line-height: 1.12; font-weight: 700; letter-spacing: -.02em; margin: 0 0 16px; }
h2 { font-size: 15pt; line-height: 1.2; font-weight: 700; letter-spacing: -.01em; margin: 16px 0 8px; padding-bottom: 4px;
     border-bottom: 1px solid var(--linie); break-after: avoid; }
h3 { font-size: 11pt; font-weight: 600; color: var(--blau); margin: 12px 0 4px; break-after: avoid; }
h4 { font-size: 9.5pt; font-weight: 600; margin: 12px 0 4px; break-after: avoid; }
p, li { margin: 0 0 4px; } ul, ol { margin: 0 0 8px; padding-left: 20px; } li::marker { color: var(--grau); }
a { color: var(--blau); text-decoration: none; }
strong { font-weight: 600; }
hr { border: 0; border-top: 1px solid var(--linie); margin: 16px 0; }
table { border-collapse: separate; border-spacing: 0; width: 100%; margin: 8px 0 12px; font-size: 8pt; line-height: 1.3;
        border: 1px solid var(--linie); border-radius: 12px; overflow: hidden; }
th, td { padding: 3px 8px; vertical-align: top; text-align: left; border: 0; border-bottom: 1px solid var(--linie); }
th { background: var(--flaeche); color: #636366; font-weight: 600; font-size: 8pt; }
tr:last-child td { border-bottom: 0; }
tbody tr:nth-child(even) td { background: #FAFAFC; }
tr { break-inside: avoid; }
blockquote { margin: 8px 0 12px; padding: 8px 16px; background: var(--flaeche); border-radius: 12px; border-left: 3px solid var(--blau); color: #3A3A3C; }
blockquote p:last-child { margin-bottom: 0; }
code { font-family: "SF Mono", ui-monospace, Menlo, Consolas, monospace; font-size: 8.3pt; background: var(--flaeche); padding: 1px 4px; border-radius: 4px; }
pre { background: var(--flaeche); border-radius: 12px; padding: 8px 16px; overflow: hidden; white-space: pre-wrap; break-inside: avoid; }
pre code { background: none; padding: 0; }
"""


def main() -> None:
    browser = next((b for b in BROWSER if b.exists()), None)
    if browser is None:
        sys.exit("Weder Edge noch Chrome gefunden.")
    body = markdown.markdown(MD.read_text(encoding="utf-8"), extensions=["tables", "sane_lists"])
    HTML.write_text(f'<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Lab-Log Vergabe-Radar</title><style>{CSS}</style></head><body>{body}</body></html>', encoding="utf-8")
    PDF.unlink(missing_ok=True)
    try:
        subprocess.run([str(browser), "--headless", "--disable-gpu", f"--user-data-dir={PROFIL}", "--no-pdf-header-footer", f"--print-to-pdf={PDF}", HTML.as_uri()],
                       check=True, timeout=120)
    finally:
        for _ in range(60):  # Edge schreibt die Datei teils erst nach Rückkehr des Aufrufs
            if PDF.exists() and PDF.stat().st_size > 0:
                break
            time.sleep(0.5)
        HTML.unlink(missing_ok=True)
    print(PDF, PDF.stat().st_size, "Bytes")


if __name__ == "__main__":
    main()
