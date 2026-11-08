"""Erzeugt die Sprecherstimme für das Video "Franz und die Glaskugel".

Liest die Untertitel (Konstante CAPS) aus docs/video/franz_und_die_glaskugel.html und
erzeugt je Untertitel eine WAV-Datei docs/video/audio/cap_NN.wav (NN = Index in CAPS).
Stimme: Windows SAPI (System.Speech), "Microsoft Hedda Desktop", offline, keine Cloud.
Die Stimme ist SYNTHETISCH und wird in Dokumentation und Video so benannt.

Das Sprechtempo (Rate, -10 bis +10) wird je Untertitel so gewählt, dass die Dauer in das
Caption-Fenster passt (Dauer <= Fenster - 0,3 s). Beginnt bei Rate 0 und erhöht schrittweise
bis MAX_RATE. Passt es dann nicht, wird gemeldet (Text kürzen oder Fenster verlängern).
Ergebnis: docs/video/audio/manifest.json (Index, Start, Ende, Sprecher, Datei, Dauer, Rate).

Aufruf (Windows, PowerShell nötig):
    .venv\\Scripts\\python.exe -I src\\report\\video_vertonung.py
"""
import json
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "docs" / "video" / "franz_und_die_glaskugel.html"
OUT = ROOT / "docs" / "video" / "audio"
VOICE = "Microsoft Hedda Desktop"
MAX_RATE = 4
LEAD_OUT = 0.3  # Reserve am Fensterende in Sekunden
SAMPLE_RATE = 22050

# Aussprachehilfen: Anzeigetext -> Sprechtext (nur für die Stimme, der Untertitel bleibt gleich)
AUSSPRACHE = [
    ("CRISP-DM", "Krisp D M"),
    ("EU-Amtsblatt", "E U Amtsblatt"),
    ("KI-Leser", "K I Leser"),
    ("KI", "K I"),
    ("TED", "Ted"),
    ("9.325", "9325"),
    ("n = 24", "n gleich 24"),
    ("…", ","),
    ("„", ""),
    ("“", ""),
    ("’", "'"),
]

PS = r"""
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$jobs = Get-Content -LiteralPath $args[0] -Raw -Encoding UTF8 | ConvertFrom-Json
$fmt = New-Object System.Speech.AudioFormat.SpeechAudioFormatInfo(%d, [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen, [System.Speech.AudioFormat.AudioChannel]::Mono)
foreach ($j in $jobs) {
  $s = New-Object System.Speech.Synthesis.SpeechSynthesizer
  $s.SelectVoice('%s')
  $s.Rate = [int]$j.rate
  $s.Volume = 100
  $s.SetOutputToWaveFile($j.wav, $fmt)
  $s.Speak([string]$j.text)
  $s.Dispose()
}
""" % (SAMPLE_RATE, VOICE)


def lese_caps():
    html = HTML.read_text(encoding="utf-8")
    block = re.search(r"const CAPS = \[(.*?)\n\];", html, re.S).group(1)
    caps = []
    for m in re.finditer(r"\[([\d.]+),([\d.]+),'(\w)','(.*?)'\],?\s*$", block, re.M):
        caps.append((float(m.group(1)), float(m.group(2)), m.group(3), m.group(4)))
    return caps


def sprechtext(text):
    for a, b in AUSSPRACHE:
        text = text.replace(a, b)
    return text


def dauer(wav):
    with wave.open(str(wav), "rb") as w:
        return w.getnframes() / w.getframerate()


def synth(jobs):
    """jobs: Liste von dict(text, wav, rate). Eine PowerShell-Sitzung für alle."""
    if not jobs:
        return
    with tempfile.TemporaryDirectory() as tmp:
        jf = Path(tmp) / "jobs.json"
        pf = Path(tmp) / "speak.ps1"
        jf.write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8-sig")
        pf.write_text(PS, encoding="utf-8-sig")
        r = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
             "-File", str(pf), str(jf)], capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("SAPI-Fehler: " + r.stderr)


def main():
    caps = lese_caps()
    if not caps:
        sys.exit("Keine Untertitel gefunden")
    OUT.mkdir(parents=True, exist_ok=True)
    stand = {}
    offen = list(range(len(caps)))
    for rate in range(0, MAX_RATE + 1):
        jobs = []
        for i in offen:
            wav = OUT / f"cap_{i:02d}.wav"
            jobs.append({"text": sprechtext(caps[i][3]), "wav": str(wav), "rate": rate})
        synth(jobs)
        neu = []
        for i in offen:
            d = dauer(OUT / f"cap_{i:02d}.wav")
            start, ende = caps[i][0], caps[i][1]
            stand[i] = (d, rate)
            if d > ende - start - LEAD_OUT:
                neu.append(i)
        offen = neu
        if not offen:
            break
    manifest = []
    for i, (start, ende, wer, text) in enumerate(caps):
        d, rate = stand[i]
        manifest.append({"index": i, "start": start, "ende": ende, "sprecher": wer,
                         "datei": f"cap_{i:02d}.wav", "dauer": round(d, 2), "rate": rate,
                         "passt": d <= ende - start - LEAD_OUT, "text": text})
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1),
                                       encoding="utf-8")
    for m in manifest:
        flag = "" if m["passt"] else "  <-- PASST NICHT"
        print(f"{m['index']:02d} {m['start']:6.1f}-{m['ende']:6.1f} fenster {m['ende']-m['start']:5.1f}s"
              f" dauer {m['dauer']:5.2f}s rate {m['rate']}{flag}")
    if offen:
        print("Nicht passend:", offen)


if __name__ == "__main__":
    main()
