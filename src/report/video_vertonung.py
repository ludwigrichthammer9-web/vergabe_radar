r"""Erzeugt die Sprecherstimme für das Video "Franz und die Glaskugel".

Liest die Untertitel (Konstante CAPS) aus docs/video/franz_und_die_glaskugel.html und
erzeugt je Untertitel eine WAV-Datei cap_NN.wav (NN = Index in CAPS) im Caption-Fenster.
Gesprochen wird der Sprechtext aus docs/video/sprechertext.json (eigenständig vom Untertitel,
fürs Hören geschrieben); fehlt ein Eintrag, wird der Untertitel mit Aussprachehilfen genommen.
Alle Stimmen sind SYNTHETISCH und werden in Dokumentation und Video so benannt.

Stimmen (Schalter --stimme):
  piper       (Standard) offline, kostenlos, Modell de_DE-thorsten-high (Thorsten-Voice, CC0),
              Ausgabe docs/video/audio/. Sprecher werden über Tonhöhe/Tempo unterschieden,
              Bit (KI) leicht robotisch (ffmpeg-Filter).
  elevenlabs  Cloud (ElevenLabs), nur mit Umgebungsvariable ELEVENLABS_API_KEY und echten
              voice_id in docs/video/stimmen.json. Die Texte VERLASSEN den Rechner, Kosten
              laufen über das eigene Konto. Ausgabe docs/video/audio/. Mit --trocken nur Plan,
              kein Netz, kein Schlüssel nötig. NICHT getestet.
  sapi        Windows SAPI (Hedda), offline; Ausgabe docs/video/audio_sapi/ (frühere Fassung v1).

Das Tempo wird je Untertitel so gewählt, dass die Dauer <= Fenster - 0,3 s ist; passt es
nicht, wird gemeldet (Text kürzen oder Fenster verlängern).
Ergebnis: manifest.json im Ausgabeordner (Index, Start, Ende, Sprecher, Datei, Dauer, Spitze).

Aufruf (Windows):
    .venv-video\Scripts\python.exe -I src\report\video_vertonung.py [--stimme piper|elevenlabs|sapi]
        [--trocken] [--modell PFAD.onnx]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIDEO = ROOT / "docs" / "video"
HTML = VIDEO / "franz_und_die_glaskugel.html"
SPRECHTEXT = VIDEO / "sprechertext.json"
STIMMEN = VIDEO / "stimmen.json"
OUT_NEU = VIDEO / "audio"
OUT_SAPI = VIDEO / "audio_sapi"
LEAD_OUT = 0.3          # Reserve am Fensterende in Sekunden
SR = 22050
PEAK_ZIEL = 0.708       # -3 dBFS
PLATZHALTER = "HIER_VOICE_ID_EINTRAGEN"

# ---- Piper ----
PIPER_MODELLE = [r"%LOCALAPPDATA%\piper_models\de_DE-thorsten-high.onnx",
                 r"%LOCALAPPDATA%\piper_models\de_DE-thorsten-medium.onnx"]
# Sprecher -> (Basis-length_scale, Tonhöhenfaktor, zusätzlicher ffmpeg-Filter)
PIPER_SPRECHER = {
    "E": (1.00, 1.00, ""),
    "F": (0.95, 1.06, ""),
    "B": (0.95, 1.12, "tremolo=f=35:d=0.12"),   # leicht robotisch
    "P": (1.00, 0.93, ""),
    "Q": (1.00, 1.04, ""),
}
PIPER_FAKTOREN = [1.0, 0.95, 0.90, 0.85, 0.80]   # length_scale-Faktoren (schneller)

# ---- SAPI (frühere Fassung) ----
VOICE = "Microsoft Hedda Desktop"
MAX_RATE = 4
AUSSPRACHE = [
    ("CRISP-DM", "Krisp D M"), ("EU-Amtsblatt", "E U Amtsblatt"), ("KI-Leser", "K I Leser"),
    ("KI", "K I"), ("TED", "Ted"), ("9.325", "9325"), ("n = 24", "n gleich 24"),
    ("…", ","), ("„", ""), ("“", ""), ("’", "'"),
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
""" % (SR, VOICE)


def lese_caps():
    html = HTML.read_text(encoding="utf-8")
    block = re.search(r"const CAPS = \[(.*?)\n\];", html, re.S).group(1)
    caps = []
    for m in re.finditer(r"\[([\d.]+),([\d.]+),'(\w)','(.*?)'\],?\s*$", block, re.M):
        caps.append((float(m.group(1)), float(m.group(2)), m.group(3), m.group(4)))
    return caps


def sprechtexte(caps):
    """Index -> Sprechtext (Sprechertext-Datei, sonst Untertitel mit Aussprachehilfen)."""
    spr = {}
    if SPRECHTEXT.exists():
        spr = json.loads(SPRECHTEXT.read_text(encoding="utf-8"))
    out = {}
    for i, c in enumerate(caps):
        t = spr.get(str(i))
        if not t:
            t = c[3]
            for a, b in AUSSPRACHE:
                t = t.replace(a, b)
        out[i] = t
    return out


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def lies_wav(p):
    import numpy as np
    with wave.open(str(p), "rb") as w:
        n, sr = w.getnframes(), w.getframerate()
        x = np.frombuffer(w.readframes(n), dtype="<i2").astype("float32") / 32768
    return x, sr


def schreibe_wav(p, x, sr):
    import numpy as np
    with wave.open(str(p), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())


def nachbearbeiten(src, dst, filt=""):
    """Stille am Anfang kürzen, Filter anwenden, auf Mono/22050 Hz, Spitze auf -3 dBFS."""
    import numpy as np
    kette = ["silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05"]
    if filt:
        kette.append(filt)
    tmp = Path(str(dst) + ".tmp.wav")
    r = subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-i", str(src), "-af", ",".join(kette),
                        "-ar", str(SR), "-ac", "1", "-c:a", "pcm_s16le", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("ffmpeg-Fehler: " + r.stderr)
    x, sr = lies_wav(tmp)
    tmp.unlink()
    pk = float(np.abs(x).max()) if len(x) else 0.0
    if pk > 0:
        x = x * (PEAK_ZIEL / pk)
    schreibe_wav(dst, x, sr)
    return len(x) / sr


def pitch_filter(f):
    if abs(f - 1) < 1e-6:
        return ""
    return f"asetrate={SR*f:.0f},aresample={SR},atempo={1/f:.5f}"


def messen(wav):
    import numpy as np
    x, sr = lies_wav(wav)
    peak = float(np.abs(x).max())
    lead = 0.0
    idx = np.nonzero(np.abs(x) > 10 ** (-40 / 20))[0]
    if len(idx):
        lead = idx[0] / sr
    return {"dauer": round(len(x) / sr, 2), "spitze_dbfs": round(20 * np.log10(peak + 1e-12), 2),
            "stille_anfang": round(lead, 2), "klipps": int((np.abs(x) >= 0.999).sum())}


# ---------------- Piper ----------------
def lauf_piper(caps, texte, out, modell):
    from piper import PiperVoice, SynthesisConfig
    pfad = None
    if modell:
        pfad = Path(modell)
    else:
        for m in PIPER_MODELLE:
            if Path(os.path.expandvars(m)).exists():
                pfad = Path(os.path.expandvars(m)); break
    if not pfad or not pfad.exists():
        sys.exit("Piper-Modell nicht gefunden (siehe docs/video/README.md, Abschnitt Piper).")
    print("Piper-Modell:", pfad.name)
    voice = PiperVoice.load(pfad)
    ergebnis = {}
    with tempfile.TemporaryDirectory() as tmp:
        for i, (start, ende, wer, _) in enumerate(caps):
            basis, pf, extra = PIPER_SPRECHER.get(wer, PIPER_SPRECHER["E"])
            filt = ",".join(x for x in (pitch_filter(pf), extra) if x)
            fenster = ende - start - LEAD_OUT
            for f in PIPER_FAKTOREN:
                roh = Path(tmp) / f"roh_{i}.wav"
                with wave.open(str(roh), "wb") as w:
                    voice.synthesize_wav(texte[i], w, SynthesisConfig(length_scale=basis * f))
                d = nachbearbeiten(roh, out / f"cap_{i:02d}.wav", filt)
                if d <= fenster:
                    break
            ergebnis[i] = f"length_scale {basis*f:.2f}, Tonhoehe x{pf}"
    return ergebnis


# ---------------- ElevenLabs ----------------
def lauf_elevenlabs(caps, texte, out, trocken):
    cfg = json.loads(STIMMEN.read_text(encoding="utf-8"))
    modell, fmt = cfg.get("model_id", "eleven_multilingual_v2"), cfg.get("output_format", "pcm_22050")
    sprecher = cfg["sprecher"]
    key = os.environ.get("ELEVENLABS_API_KEY", "")
    zeichen = sum(len(texte[i]) for i in range(len(caps)))
    print(f"ElevenLabs: Modell {modell}, Format {fmt}, {len(caps)} Aufrufe, {zeichen} Zeichen (Kontingent/Kosten beim Konto)")
    fehlen = sorted({w for _, _, w, _ in caps if sprecher.get(w, {}).get("voice_id", PLATZHALTER) == PLATZHALTER})
    for i, (start, ende, wer, _) in enumerate(caps):
        s = sprecher.get(wer, {})
        print(f"  {i:02d} {wer} voice_id={'(Platzhalter)' if s.get('voice_id', PLATZHALTER) == PLATZHALTER else s['voice_id'][:6] + '...'}"
              f" speed={s.get('speed', 1.0)} fenster={ende-start:.1f}s zeichen={len(texte[i])}")
    if trocken:
        print("Trockenlauf: kein Netz, nichts gesendet. Fehlende voice_id fuer Sprecher:", fehlen or "keine",
              "| API-Schluessel gesetzt:", "ja" if key else "nein")
        return None
    if not key:
        sys.exit("ELEVENLABS_API_KEY ist nicht gesetzt (Umgebungsvariable). Abbruch, nichts gesendet.")
    if fehlen:
        sys.exit(f"voice_id fehlt fuer Sprecher {fehlen} in docs/video/stimmen.json. Abbruch, nichts gesendet.")
    if not fmt.startswith("pcm_"):
        sys.exit("Nur pcm_* als output_format unterstuetzt (rohes 16-Bit-PCM, Mono).")
    from elevenlabs.client import ElevenLabs
    from elevenlabs import VoiceSettings
    client = ElevenLabs(api_key=key)
    sr_in = int(fmt.split("_")[1])
    ergebnis = {}
    with tempfile.TemporaryDirectory() as tmp:
        for i, (start, ende, wer, _) in enumerate(caps):
            s = sprecher[wer]
            audio = client.text_to_speech.convert(
                voice_id=s["voice_id"], text=texte[i], model_id=modell, output_format=fmt,
                voice_settings=VoiceSettings(speed=float(s.get("speed", 1.0))))
            roh = Path(tmp) / f"roh_{i}.wav"
            with wave.open(str(roh), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr_in)
                w.writeframes(b"".join(audio))
            # Passt es nicht ins Fenster, mit atempo (max. 1,15) beschleunigen.
            d = nachbearbeiten(roh, out / f"cap_{i:02d}.wav")
            fenster = ende - start - LEAD_OUT
            if d > fenster:
                faktor = min(1.15, d / fenster + 0.01)
                d = nachbearbeiten(roh, out / f"cap_{i:02d}.wav", f"atempo={faktor:.3f}")
            ergebnis[i] = f"ElevenLabs {modell}"
    return ergebnis


# ---------------- SAPI ----------------
def lauf_sapi(caps, texte, out):
    def synth(jobs):
        with tempfile.TemporaryDirectory() as tmp:
            jf, pf = Path(tmp) / "jobs.json", Path(tmp) / "speak.ps1"
            jf.write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8-sig")
            pf.write_text(PS, encoding="utf-8-sig")
            r = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                                "-File", str(pf), str(jf)], capture_output=True, text=True)
            if r.returncode != 0:
                sys.exit("SAPI-Fehler: " + r.stderr)
    offen, ergebnis = list(range(len(caps))), {}
    for rate in range(0, MAX_RATE + 1):
        synth([{"text": texte[i], "wav": str(out / f"cap_{i:02d}.wav"), "rate": rate} for i in offen])
        neu = []
        for i in offen:
            with wave.open(str(out / f"cap_{i:02d}.wav"), "rb") as w:
                d = w.getnframes() / w.getframerate()
            ergebnis[i] = f"SAPI Rate {rate}"
            if d > caps[i][1] - caps[i][0] - LEAD_OUT:
                neu.append(i)
        offen = neu
        if not offen:
            break
    return ergebnis


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stimme", choices=["piper", "elevenlabs", "sapi"], default="piper")
    ap.add_argument("--trocken", action="store_true", help="nur Plan zeigen (elevenlabs: kein Netz)")
    ap.add_argument("--modell", default=None, help="Pfad zum Piper-Modell (.onnx)")
    a = ap.parse_args()
    caps = lese_caps()
    if not caps:
        sys.exit("Keine Untertitel gefunden")
    texte = sprechtexte(caps) if a.stimme != "sapi" else {i: t for i, t in sprechtexte_sapi(caps).items()}
    out = OUT_SAPI if a.stimme == "sapi" else OUT_NEU
    if a.stimme == "elevenlabs" and a.trocken:
        lauf_elevenlabs(caps, texte, out, True)
        return
    out.mkdir(parents=True, exist_ok=True)
    if a.stimme == "piper":
        info = lauf_piper(caps, texte, out, a.modell)
    elif a.stimme == "elevenlabs":
        info = lauf_elevenlabs(caps, texte, out, False)
    else:
        info = lauf_sapi(caps, texte, out)
    manifest, schlecht = [], []
    for i, (start, ende, wer, text) in enumerate(caps):
        m = messen(out / f"cap_{i:02d}.wav")
        passt = m["dauer"] <= ende - start - LEAD_OUT
        if not passt:
            schlecht.append(i)
        manifest.append({"index": i, "start": start, "ende": ende, "sprecher": wer, "datei": f"cap_{i:02d}.wav",
                         "dauer": m["dauer"], "spitze_dbfs": m["spitze_dbfs"], "stille_anfang": m["stille_anfang"],
                         "klipps": m["klipps"], "einstellung": info[i], "stimme": a.stimme, "passt": passt,
                         "text": text, "sprechtext": texte[i]})
        print(f"{i:02d} {wer} {start:6.1f}-{ende:6.1f} fenster {ende-start:5.1f}s dauer {m['dauer']:5.2f}s "
              f"spitze {m['spitze_dbfs']:6.2f} dBFS stille {m['stille_anfang']:.2f}s {info[i]}"
              f"{'' if passt else '  <-- PASST NICHT'}")
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    if schlecht:
        print("Nicht passend:", schlecht)


def sprechtexte_sapi(caps):
    """SAPI (v1) spricht wie früher den Untertitel mit Aussprachehilfen."""
    out = {}
    for i, c in enumerate(caps):
        t = c[3]
        for a, b in AUSSPRACHE:
            t = t.replace(a, b)
        out[i] = t
    return out


if __name__ == "__main__":
    main()
