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
@page { size: A4; margin: 16mm 14mm; }
body { font-family: Calibri, Arial, sans-serif; font-size: 10pt; line-height: 1.4; color: #1b2a33; }
h1 { font-size: 20pt; color: #0b3c49; } h2 { font-size: 14pt; color: #0b3c49; border-bottom: 1px solid #8fb8c4; margin-top: 1.4em; }
h3 { font-size: 11.5pt; color: #1c7293; margin-bottom: .3em; }
table { border-collapse: collapse; width: 100%; margin: .6em 0; font-size: 8.5pt; }
th, td { border: 1px solid #b8c7cc; padding: 3px 5px; vertical-align: top; } th { background: #eaf3f5; }
tr { page-break-inside: avoid; } code { font-size: 8.5pt; background: #f2f5f6; }
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
