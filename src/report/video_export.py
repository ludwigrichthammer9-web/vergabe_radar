r"""MP4-Export für "Franz und die Glaskugel" (Standbilder per Playwright/Edge + Tonspur + ffmpeg).

Voraussetzungen (eigene venv, nichts im Haupt-Projekt):
    python -m venv .venv-video
    .venv-video\Scripts\python.exe -m pip install -r requirements-video.txt
    (Browser: installiertes Microsoft Edge über channel="msedge", kein Download;
     ffmpeg-Binary kommt aus dem Paket imageio-ffmpeg.)
Vorher die WAV-Dateien erzeugen: src/report/video_vertonung.py (Piper, ElevenLabs oder --stimme sapi; synthetisch).

Aufruf:
    .venv-video\Scripts\python.exe src\report\video_export.py [--von 8] [--bis 186] [--fps 30]
        [--out docs/video/franz_und_die_glaskugel_szenen_0-5_v3.mp4] [--audio DIR] [--stills DIR]

Ablauf: Die Seite wird mit ?render geladen; window.render(t) zeichnet das Bild zur Zeit t.
Jedes Bild wird als PNG aufgenommen und direkt an ffmpeg gegeben (keine Zwischendateien).
Quizpause (Quiz bei 104 bis 116 s): Im Video bleibt das Quizbild bei t = 105 s drei Sekunden
stehen, die letzten 0,5 s mit dem Hinweis "Auflösung folgt"; danach geht es bei t = 116 s weiter
(die Zeit 105 bis 116 s der Live-Fassung entfällt). Die Quizfrage wird in den ersten Sekunden
gesprochen (Beginn bei 104 s). Untertitel im Bild, Ton aus audio/cap_NN.wav an den Offsets der
Untertitel-Anfänge (adelay), alles als H.264/AAC, yuv420p, 1280x720.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
VIDEO = ROOT / "docs" / "video"
HTML = VIDEO / "franz_und_die_glaskugel.html"
AUDIO = VIDEO / "audio"
QUIZ_T = 105.0      # Quizpause in der Live-Fassung
QUIZ_WEITER = 116.0
HOLD_S = 3.0
HINT_S = 0.5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--von", type=float, default=8)
    ap.add_argument("--bis", type=float, default=186)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--out", default=str(VIDEO / "franz_und_die_glaskugel_szenen_0-5_v3.mp4"))
    ap.add_argument("--audio", default=str(AUDIO), help="Ordner mit cap_NN.wav und manifest.json")
    ap.add_argument("--stills", default=None, help="Ordner: Standbilder bei ausgewählten Zeiten speichern")
    a = ap.parse_args()
    fps = a.fps
    mit_quiz = a.von < QUIZ_T < a.bis

    # Zeitplan: Liste (Quellzeit, Modus); Modus 0 normal, 1 Quiz-Halt, 2 Quiz-Halt mit Hinweis
    plan = []
    n = int(round((min(a.bis, QUIZ_T if mit_quiz else a.bis) - a.von) * fps))
    plan += [(a.von + i / fps, 0) for i in range(n)]
    if mit_quiz:
        plan += [(QUIZ_T, 1)] * int(HOLD_S * fps) + [(QUIZ_T, 2)] * int(HINT_S * fps)
        m = int(round((a.bis - QUIZ_WEITER) * fps))
        plan += [(QUIZ_WEITER + i / fps, 0) for i in range(m)]
    dauer = len(plan) / fps

    def out_offset(t):
        if mit_quiz and t >= QUIZ_WEITER:
            return (QUIZ_T - a.von) + HOLD_S + HINT_S + (t - QUIZ_WEITER)
        return t - a.von

    audio = Path(a.audio)
    manifest = json.loads((audio / "manifest.json").read_text(encoding="utf-8"))
    spuren = []
    for m in manifest:
        s, e = m["start"], m["ende"]
        if s < a.von or s >= a.bis:
            continue
        if mit_quiz and QUIZ_T < s < QUIZ_WEITER:
            continue
        spuren.append((audio / m["datei"], out_offset(s)))

    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps), "-c:v", "png", "-i", "-"]
    for f, _ in spuren:
        cmd += ["-i", str(f)]
    fc = []
    for k, (_, off) in enumerate(spuren, start=1):
        ms = int(round(off * 1000))
        fc.append(f"[{k}:a]adelay={ms}|{ms}[a{k}]")
    labels = "".join(f"[a{k}]" for k in range(1, len(spuren) + 1))
    fc.append(f"{labels}amix=inputs={len(spuren)}:normalize=0:duration=longest,apad[aout]")
    cmd += ["-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
            "-r", str(fps), "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            "-t", f"{dauer:.3f}", "-movflags", "+faststart", a.out]
    print(f"Bilder: {len(plan)} ({dauer:.1f} s), Tonspuren: {len(spuren)}")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    stills = Path(a.stills) if a.stills else None
    if stills:
        stills.mkdir(parents=True, exist_ok=True)
    marken = {round(t * fps) for t in (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 105, 120, 130, 150, 160, 170, 180)}

    with sync_playwright() as pw:
        br = pw.chromium.launch(channel="msedge", headless=True)
        pg = br.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
        pg.goto(HTML.as_uri() + "?render")
        pg.wait_for_function("typeof window.render === 'function'")
        pg.evaluate("document.fonts.ready")
        cache = None
        for i, (t, modus) in enumerate(plan):
            if modus == 1 and cache is not None and plan[i - 1][1] == 1:
                png = cache
            else:
                if modus == 2:
                    pg.evaluate("t=>{window.render(t); document.getElementById('qs').textContent='Auflösung folgt …';}", t)
                else:
                    pg.evaluate("t=>{document.getElementById('qs').textContent='Ziel waren 60 Prozent.'; window.render(t);}", t)
                png = pg.screenshot(type="png")
                cache = png if modus else None
            proc.stdin.write(png)
            if stills and (i in {round((x - a.von) * fps) for x in (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130, 150, 160, 170, 180)}
                           or (modus == 1 and plan[i - 1][1] == 0) or (modus == 2 and plan[i - 1][1] == 1)):
                (stills / f"t{i:05d}_{t:06.2f}_m{modus}.png").write_bytes(png)
            if i % 300 == 0:
                print(f"  {i}/{len(plan)}", flush=True)
        br.close()
    proc.stdin.close()
    if proc.wait() != 0:
        sys.exit("ffmpeg-Fehler")
    print("fertig:", a.out)


if __name__ == "__main__":
    main()
