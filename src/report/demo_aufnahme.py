r"""Bildschirmaufnahme der Live-Demo (docs/demo/live_demo.html) als MP4, ohne Ton.

Voraussetzungen wie src/report/video_export.py (.venv-video: playwright, imageio-ffmpeg; Browser: installiertes Edge).
Aufruf:
    .venv-video\Scripts\python.exe src\report\demo_aufnahme.py [--out docs/video/live_demo_aufnahme.mp4]
        [--poster docs/vortrag/poster_live_demo.png] [--stills DIR] [--breite 1280 --hoehe 720]

Ablauf (ca. 55 s, alles Klicks mit sichtbarem, dezentem Mauszeiger): Seite (hell) -> Großer Datensatz -> Beispielfirma
Cham 50 km (Frist-Filter an) -> Filterung starten (Trichter läuft, ca. 8 s) -> Trefferliste -> Klick auf Treffer
-> Teams-Karte -> E-Mail -> Frist-Filter aus (Hinweis „nur zur Veranschaulichung“) -> Ergebnis.
Aufnahme über das Chrome-DevTools-Protokoll (Page.startScreencast, JPEG-Bilder mit Zeitstempel; Playwrights record_video
braucht einen Zusatz-Download und wird nicht benutzt); ffmpeg setzt die Bilder zeitgenau zu H.264/MP4 mit 30 fps zusammen. Konsolenfehler und Seitenfehler werden gemeldet.
Nichts wird gesendet; die Seite ist offline (file://).
"""
import argparse
import base64
import subprocess
import sys
import tempfile
from pathlib import Path

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "docs" / "demo" / "live_demo.html"

CURSOR_JS = """
(() => {
  const css = `
  #__cur{position:fixed;left:0;top:0;width:22px;height:22px;margin:-3px 0 0 -3px;z-index:2147483647;pointer-events:none;
    transition:none}
  #__cur svg{display:block;filter:drop-shadow(0 1px 2px rgba(0,0,0,.45))}
  .__ring{position:fixed;z-index:2147483646;pointer-events:none;width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;
    border:3px solid rgba(255,159,10,.95);background:rgba(255,159,10,.25);animation:__r .6s ease-out forwards}
  @keyframes __r{to{transform:scale(3.2);opacity:0}}`;
  const add = () => {
    if (document.getElementById('__cur')) return;
    const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    const c = document.createElement('div'); c.id = '__cur';
    c.innerHTML = '<svg width="22" height="22" viewBox="0 0 22 22"><path d="M3 2 L3 17 L7 13.5 L9.8 19.5 L12.2 18.4 L9.5 12.6 L15 12.6 Z" fill="#fff" stroke="#1c1c1e" stroke-width="1.4" stroke-linejoin="round"/></svg>';
    document.body.appendChild(c);
    c.style.transform = 'translate(-60px,-60px)';
    document.addEventListener('mousemove', e => { c.style.transform = `translate(${e.clientX}px,${e.clientY}px)`; }, true);
    document.addEventListener('mousedown', e => {
      const r = document.createElement('div'); r.className = '__ring';
      r.style.left = e.clientX + 'px'; r.style.top = e.clientY + 'px'; document.body.appendChild(r);
      setTimeout(() => r.remove(), 700);
    }, true);
  };
  if (document.body) add(); else document.addEventListener('DOMContentLoaded', add);
})();
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "docs" / "video" / "live_demo_aufnahme.mp4"))
    ap.add_argument("--poster", default=str(ROOT / "docs" / "vortrag" / "poster_live_demo.png"))
    ap.add_argument("--stills", default=None, help="Ordner für Kontrollbilder aus dem Ablauf (PNG)")
    ap.add_argument("--breite", type=int, default=1280)
    ap.add_argument("--hoehe", type=int, default=720)
    a = ap.parse_args()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    stills = Path(a.stills) if a.stills else None
    if stills:
        stills.mkdir(parents=True, exist_ok=True)
    fehler = []
    tmp = Path(tempfile.mkdtemp(prefix="demo_aufnahme_"))
    size = {"width": a.breite, "height": a.hoehe}

    with sync_playwright() as pw:
        br = pw.chromium.launch(channel="msedge", headless=True)
        ctx = br.new_context(viewport=size, color_scheme="light", reduced_motion="no-preference", locale="de-DE")
        ctx.add_init_script(CURSOR_JS)
        page = ctx.new_page()
        frames = []   # (Zeitstempel, Dateipfad)
        cdp = ctx.new_cdp_session(page)

        def on_frame(ev):
            f = tmp / ("f%06d.jpg" % len(frames))
            f.write_bytes(base64.b64decode(ev["data"]))
            frames.append((ev["metadata"]["timestamp"], f))
            cdp.send("Page.screencastFrameAck", {"sessionId": ev["sessionId"]})

        cdp.on("Page.screencastFrame", on_frame)
        page.on("console", lambda m: fehler.append("console." + m.type + ": " + m.text) if m.type in ("error", "warning") else None)
        page.on("pageerror", lambda e: fehler.append("pageerror: " + str(e)))
        page.on("requestfailed", lambda r: fehler.append("requestfailed: " + r.url))

        def foto(name):
            if stills:
                page.screenshot(path=str(stills / (name + ".png")))

        def zu(sel, pause=0.9, steps=35):
            """Mauszeiger langsam zum Element, kurz warten, klicken."""
            el = page.locator(sel).first
            el.scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            b = el.bounding_box()
            page.mouse.move(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2, steps=steps)
            page.wait_for_timeout(int(pause * 1000))
            page.mouse.down()
            page.wait_for_timeout(90)
            page.mouse.up()

        def warte(s):
            page.wait_for_timeout(int(s * 1000))

        def scrolle_zu(sel, rand=84, dauer=1.4):
            """Seite gleichmäßig (Mausrad-Schritte) so scrollen, dass das Element knapp unter der Kopfleiste steht."""
            ziel = page.evaluate("(s)=>document.querySelector(s).getBoundingClientRect().top - %d" % rand, sel)
            n = max(1, int(dauer * 25))
            for _ in range(n):
                page.mouse.wheel(0, ziel / n)
                page.wait_for_timeout(40)
            page.wait_for_timeout(300)

        page.goto(HTML.as_uri())
        cdp.send("Page.startScreencast", {"format": "jpeg", "quality": 92, "maxWidth": a.breite, "maxHeight": a.hoehe, "everyNthFrame": 1})
        page.mouse.move(900, 500)
        warte(3.0)                                    # 1 Seite, hell
        foto("01_seite")
        zu('button[data-set="bayern"]')               # 2 Großer Datensatz
        warte(1.5)
        zu('button[data-frei="DE235,50,12"]')         # 3 Beispielfirma Cham 50 km
        warte(1.2)
        scrolle_zu("#setwahl", rand=100, dauer=0.8)   # Datensatz, Zeitraum, Frist-Filter (an) im Bild
        warte(2.5)
        foto("02_formular")
        c = page.locator("#nuroffen").bounding_box()
        page.mouse.move(c["x"] + 10, c["y"] + 10, steps=25)
        warte(2.0)
        zu("#start1", pause=1.0)                      # 4 Filterung starten
        warte(2.8)                                    # Punktfeld mit großer Zahl und Erklärzeile
        foto("03_filterlauf_punkte")
        scrolle_zu("#trichter", rand=84, dauer=1.4)   # Trichter mit den Zahlen je Stufe
        warte(3.4)
        foto("04_filterlauf_trichter")
        warte(2.4)                                    # Lauf ca. 8 s, dann Ergebnis
        scrolle_zu("#ergebnis", rand=84, dauer=1.0)
        warte(1.5)
        foto("05_trefferliste")
        Path(a.poster).parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=a.poster)                # Posterbild für die Folie (Trefferliste)
        warte(1.5)
        zu("#treffer button.tcard", pause=1.2)        # 5 Treffer anklicken -> Teams-Karte
        warte(3.0)
        foto("06_teams")
        scrolle_zu("#vorschau", rand=84, dauer=0.5)
        warte(0.5)
        for _ in range(30):
            page.mouse.wheel(0, 9)
            page.wait_for_timeout(40)
        warte(1.8)
        foto("07_teams_ki")
        scrolle_zu("#schritt3", rand=84, dauer=0.8)
        zu('.kanalzeile button[data-k="mail"]', pause=1.0)   # 6 E-Mail
        warte(3.5)
        foto("08_mail")
        # 7 Frist-Filter AUS
        scrolle_zu("#schritt1", rand=84, dauer=1.0)
        zu("#nuroffen", pause=1.0)
        warte(3.5)
        foto("09_filter_aus")
        zu("#start1", pause=0.8)                      # 8 neu starten, sofort anzeigen
        warte(2.0)
        zu("#sofort", pause=0.8)
        warte(1.0)
        scrolle_zu("#ergebnis", rand=84, dauer=0.8)
        warte(4.0)
        foto("10_filter_aus_ergebnis")
        warte(1.0)
        cdp.send("Page.stopScreencast")
        warte(0.3)
        ctx.close()
        br.close()

    ff = imageio_ffmpeg.get_ffmpeg_exe()
    liste = tmp / "liste.txt"
    zeilen = []
    for i, (t, f) in enumerate(frames):
        d = (frames[i + 1][0] - t) if i + 1 < len(frames) else 1.0
        zeilen.append("file '%s'" % f.as_posix())
        zeilen.append("duration %.4f" % max(d, 0.001))
    zeilen.append("file '%s'" % frames[-1][1].as_posix())
    liste.write_text("\n".join(zeilen), encoding="utf-8")
    print("Bilder:", len(frames), "Dauer: %.1f s" % (frames[-1][0] - frames[0][0]))
    subprocess.run([ff, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(liste), "-an", "-vf", "fps=30,scale=%d:%d" % (a.breite, a.hoehe),
                    "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)], check=True)
    mb = out.stat().st_size / 1e6
    print("MP4:", out, "%.1f MB" % mb)
    print("Konsole/Seitenfehler:", fehler if fehler else "keine")
    if mb >= 25:
        print("WARNUNG: Datei >= 25 MB")
        sys.exit(1)


if __name__ == "__main__":
    main()
