"""Prüfung der Live-Demo: Selbsttest (docs/demo/live_demo.html#selftest) in Edge headless ausführen und auswerten.

(a) P1/P2 mit dem Beispiel-Schnappschuss: Trichter (Name, Anzahl, Notiz) = docs/demo/ergebnis_lauf.json, Teams-Karten =
    docs/demo/nachrichten/*.json, keine JS-Fehler.
(b) Großer Datensatz: Zahlen je Stufe für drei eigene Profile; jede Trefferkarte wird gegen die unveränderten Rohdaten
    (data/raw/demo_live_20261106, falls vorhanden) geprüft: Ort (NUTS DE23*), Frist, CPV 90910/90911/90919.
Kein Netz, keine KI. Ausgabe: Text auf der Konsole, Rohergebnis als JSON (Pfad als Argument, Standard: nicht gespeichert).

Aufruf: .venv\\Scripts\\python.exe -I src\\demo\\live_demo_pruefung.py [ausgabe.json]
"""

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # nötig wegen python -I

import daten as D  # noqa: E402

EDGE = [Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe")]
HTML = D.PROJECT_ROOT / "docs" / "demo" / "live_demo.html"
BERICHT = D.PROJECT_ROOT / "reports" / "demo_live_pruefung.txt"
_ZEILEN = []


def log(*a):
    s = " ".join(str(x) for x in a)
    _ZEILEN.append(s)
    print(s)


def selbsttest():
    edge = next((p for p in EDGE if p.exists()), None)
    if edge is None:
        sys.exit("Microsoft Edge nicht gefunden (gesucht: " + "; ".join(map(str, EDGE)) + "). Selbsttest nicht ausgeführt.")
    url = HTML.resolve().as_uri() + "#selftest"
    r = subprocess.run([str(edge), "--headless=new", "--disable-gpu", "--no-first-run", "--virtual-time-budget=20000",
                        "--dump-dom", url], capture_output=True, timeout=180)
    dom = r.stdout.decode("utf-8", "replace")
    a = dom.index('<pre id="selftest">') + len('<pre id="selftest">')
    import html as H
    return json.loads(H.unescape(dom[a:dom.index("</pre>", a)]))


def main():
    out = selbsttest()
    fehler = []
    log("JS-Fehler:", out.get("errors"), "| Ausnahme:", out.get("fehler", "keine"))
    if out.get("errors") or out.get("fehler"):
        fehler.append("JS-Fehler")
    erg = json.loads((D.PROJECT_ROOT / "docs" / "demo" / "ergebnis_lauf.json").read_text(encoding="utf-8"))
    gem_soll = erg["gemeinsam"]
    for p in erg["profile"]:
        pid = p["profil_id"]
        ist = out[pid]
        g = ist["gemeinsam"] == gem_soll
        s = ist["stufen"] == p["stufen"]
        k_ok = True
        for k in ist["karten"]:
            soll = json.loads((D.PROJECT_ROOT / "docs" / "demo" / "nachrichten" / f"{pid}_{k['nr']}.json").read_text(encoding="utf-8"))
            k_ok &= soll == k["card"]
        n_dateien = len(list((D.PROJECT_ROOT / "docs" / "demo" / "nachrichten").glob(f"{pid}_*.json")))
        log(f"(a) {pid}: gemeinsam gleich={g}, Stufen gleich={s}, Karten {len(ist['karten'])}/{n_dateien} identisch={k_ok}, "
              f"Animation {ist['zeit_ms'] / 1000:.1f} s, ausgeschieden je Zeile={ist['raus']}")
        if not (g and s and k_ok and len(ist["karten"]) == n_dateien):
            fehler.append(f"{pid} weicht ab")
        if "bayern_14t" in ist:
            ab_op = [x for x in ist["bayern_14t"]["stufen"] if not x["name"].startswith("Gebäudereinigungs")]
            soll_ab_op = [x for x in p["stufen"] if not x["name"].startswith("Gebäudereinigungs")]
            gleich = ab_op == soll_ab_op
            log(f"    Gegenprobe großer Datensatz, 14 Tage bis 16.10.2026: Stufen ab Oberpfalz gleich={gleich}, "
                  f"Treffer {[(k['nr'], k['urteil'], k['ki']) for k in ist['bayern_14t']['karten']]}")
            if not gleich:
                fehler.append(f"{pid} Gegenprobe Bayern weicht ab")
    # (b) Großer Datensatz
    roh = {}
    ordner = D.RAW_DIR / "demo_live_20261106"
    if not ordner.exists():
        log("Rohdatenabgleich nicht ausgeführt (data/raw/demo_live_20261106 fehlt)")
    if ordner.exists():
        _, alle = D.lade_schnappschuss(ordner)
        roh = {b["nr"]: b for b in alle}
    for key, c in out.get("bayern", {}).items():
        log(f"(b) {key}: Animation {c['zeit_ms'] / 1000:.1f} s, abgelaufen unter Treffern {c['abgelaufen']}")
        for z in c["zeilen"]:
            log("      ", z)
        frist_aus = key.lower().endswith("true")  # Schlüssel: <Sitz>_<Radius>_<Laufzeit>|<Stichtag>_<Zeitraum>_<ohneFrist>
        stichtag = key.split("|")[1].split("_")[0]
        for k in c["karten"]:
            b = roh.get(k["nr"])
            if not b:
                continue
            ok_ort = any(n.startswith("DE23") for n in b["nuts"]) and b["nuts"] == k["nuts"]
            ok_cpv = any(x.startswith(("90910", "90911", "90919")) for x in b["cpv"]) and b["cpv"] == k["cpv"]
            fr = max(b["fristen"]).isoformat() if b["fristen"] else None
            ok_frist = fr == k["frist"] and (frist_aus or fr is None or fr >= stichtag)
            if not (ok_ort and ok_cpv and ok_frist):
                fehler.append(f"{key} {k['nr']}: Ort {ok_ort}, CPV {ok_cpv}, Frist {ok_frist}")
        log(f"      Treffer gegen Rohdaten geprüft: {len([k for k in c['karten'] if k['nr'] in roh])} von {len(c['karten'])}")
    log("anim_ok:", out.get("anim_ok"))
    if roh:
        geprueft = sum(1 for c in out.get("bayern", {}).values() for k in c["karten"] if k["nr"] in roh)
        log(f"Rohdatenabgleich: {geprueft} Trefferkarten gegen Rohdaten geprüft")
    ergebnis = ("(a) gleich" + (", (b) gegen Rohdaten ok" if roh else ", (b) Rohdatenabgleich NICHT ausgeführt")) if not fehler else fehler
    log("ERGEBNIS:", ergebnis)
    BERICHT.parent.mkdir(exist_ok=True)
    kopf = "Ausgabe von src/demo/live_demo_pruefung.py (Edge headless), Lauf 2026-11-06"
    BERICHT.write_text("\n".join([kopf, *_ZEILEN]) + "\n", encoding="utf-8")
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not fehler else 1


if __name__ == "__main__":
    sys.exit(main())
