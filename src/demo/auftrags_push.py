"""Demo: Profil-Match mit KI-Stufe und Push-Nachrichten (Veranschaulichung der Datenübergabe, KEIN Business Case).

Standardlauf: offline, aus dem lokalen Schnappschuss data/raw/demo_push_<Datum>/, festes „heute“, KI-Antworten aus dem Cache.
Es wird nichts gesendet. Siehe docs/demo_push.md.

Aufrufe (im Projektordner):
  .venv\\Scripts\\python.exe -I src\\demo\\auftrags_push.py                       # offline, KI aus Cache (reproduzierbar)
  .venv\\Scripts\\python.exe -I src\\demo\\auftrags_push.py --ki claude           # echte KI-Aufrufe (höchstens 20), Cache wird gefüllt
  .venv\\Scripts\\python.exe -I src\\demo\\auftrags_push.py --ki platzhalter      # ohne KI
  .venv\\Scripts\\python.exe -I src\\demo\\auftrags_push.py --modus live          # holt neue Bekanntmachungen von TED (heute, 14 Tage)
  Versand (vom Nutzer mit eigenem Webhook/Postfach auszuführen, in dieser Demo NICHT ausgeführt):
  ... --senden-teams (URL aus Umgebungsvariable TEAMS_WEBHOOK_URL)     ... --senden-mail --smtp-host H --smtp-user U --mail-an A   (Passwort: Umgebungsvariable DEMO_SMTP_PASSWORD)
"""

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # nötig wegen python -I

import daten as D  # noqa: E402
import ki_stufe as K  # noqa: E402
import nachrichten as N  # noqa: E402
import stufen as S  # noqa: E402
import vorschau as V  # noqa: E402

AUSGABE = D.PROJECT_ROOT / "docs" / "demo"


def pipeline(args):
    stichtag = date.fromisoformat(args.stichtag)
    if args.modus == "live":
        stichtag = date.today()
        ordner = D.RAW_DIR / f"demo_push_{stichtag:%Y%m%d}"
        print(f"Live-Abruf nach {ordner} (nur Veröffentlichungen ab {stichtag - timedelta(days=args.fenster_tage)}) ...")
        D.live_abruf(f"{stichtag - timedelta(days=args.fenster_tage):%Y%m%d}", ordner)
    else:
        ordner = Path(args.daten) if args.daten else D.standard_quelle()  # zuerst docs/demo/daten, sonst data/raw
    meta, alle = D.lade_schnappschuss(ordner)
    quelle_name = meta["quelle_name"]
    profile = json.loads((AUSGABE / "profil_beispiel.json").read_text(encoding="utf-8"))["profile"]

    von = stichtag - timedelta(days=args.fenster_tage)
    fenster = [b for b in alle if von <= b["veroeffentlicht"] <= stichtag]
    dedupliziert = S.dedupe(fenster)
    gemeinsam = [
        {"name": "Alle Bekanntmachungen Deutschland, CPV 909* (im Schnappschuss)", "anzahl": meta["anzahl_gesamt"], "notiz": quelle_name},
        {"name": f"veröffentlicht {von:%d.%m.} bis {stichtag:%d.%m.%Y}", "anzahl": len(fenster), "notiz": ""},
        {"name": "ohne Mehrfachveröffentlichung (gleicher Auftraggeber + Titel)", "anzahl": len(dedupliziert), "notiz": ""},
    ]

    # Vergleichsmenge: gleiche Filter ohne Frist, längeres Fenster (nur für den KI-gegen-Regel-Vergleich)
    # (ganzer Schnappschuss, auch Veröffentlichungen nach dem Stichtag: es geht nur um den Inhaltsvergleich, nicht um Nachrichten)
    v_dedup = S.dedupe(alle)

    treffer, stufen_je, vergleich_je = {}, {}, {}
    for p in profile:
        stufen_je[p["id"]], treffer[p["id"]] = S.trichter(p, dedupliziert, stichtag)
        _, vergleich_je[p["id"]] = S.trichter(p, v_dedup, stichtag, ohne_frist=True, ohne_radius=True)

    # KI-Stufe: pro Bekanntmachung ein Aufruf, beide Profile; Entfernung je Profil im Profil-JSON der KI
    eingabe = {}
    for p in profile:
        eingabe[p["id"]] = {b["nr"]: b for b in treffer[p["id"]] + vergleich_je[p["id"]]}
    liste_je_profil = {pid: list(m.values()) for pid, m in eingabe.items()}
    urteile, ki_protokoll = K.ki_stufe(liste_je_profil, profile, args.ki, args.max_aufrufe)

    liste = S.lade_liste()
    nachr_dir = AUSGABE / "nachrichten"
    nachr_dir.mkdir(parents=True, exist_ok=True)
    for f in list(nachr_dir.glob("*.json")) + list(nachr_dir.glob("*.eml")):
        f.unlink()
    vorschau_profile, alle_cards, ergebnis_profile = [], [], []
    for p in profile:
        karten, mails, treffer_info = [], [], []
        n_vorg = 0
        for b in treffer[p["id"]]:
            u = urteile[p["id"]][b["nr"]]
            regel = S.regel_urteil(p, b)
            if u["urteil"] != "passt nicht":
                b["_entfernung"] = S.entfernung_km(p, b)
                vg = S.vorgaenger_hinweis(b, liste)
                n_vorg += 1 if vg else 0
                c = N.inhalt(p, b, u, f"{regel[0]}: {regel[1]}", vg, stichtag)
                stamm = f"{p['id']}_{b['nr']}"
                (nachr_dir / f"{stamm}.json").write_text(N.card_json(c), encoding="utf-8")
                (nachr_dir / f"{stamm}.eml").write_bytes(N.eml(c, stichtag))
                karten.append(c)
                mails.append((f"[Demo] {c['urteil'].capitalize()}: {c['titel'][:80]}", c))
                alle_cards.append((p["id"], b["nr"], N.adaptive_card(c), N.eml(c, stichtag)))
            treffer_info.append({"nr": b["nr"], "titel": b["titel"], "ki": u["urteil"], "ki_quelle": u["quelle"],
                                 "regel": regel[0], "begruendung": u["begruendung"], "nachricht": u["urteil"] != "passt nicht",
                                 "pruefhinweise": u["pruefhinweise"]})
        stufen = stufen_je[p["id"]] + [
            {"name": "KI-Urteil: passt / unklar / passt nicht",
             "anzahl": len(treffer[p["id"]]),
             "notiz": " / ".join(str(sum(1 for t in treffer_info if t["ki"] == k)) for k in K.URTEILE)},
            {"name": "Nachrichten erzeugt (passt + unklar)", "anzahl": len(karten), "notiz": ""},
            {"name": "davon mit Vorgänger-Hinweis (Vertragsliste, eindeutig)", "anzahl": n_vorg,
             "notiz": f"bei {len(karten) - n_vorg} von {len(karten)} Nachrichten kein eindeutiger Treffer"},
        ]
        vorschau_profile.append({"profil": p, "stufen": stufen, "karten": karten, "mails": mails})
        ergebnis_profile.append({"profil_id": p["id"], "stufen": stufen, "treffer": treffer_info})

    paare = []
    for p in profile:
        for b in vergleich_je[p["id"]]:
            u, r = urteile[p["id"]][b["nr"]], S.regel_urteil(p, b)
            paare.append({"profil": p["id"], "nr": b["nr"], "titel": b["titel"], "ki": u["urteil"], "regel": r[0],
                          "gleich": u["urteil"] == r[0], "ki_begruendung": u["begruendung"], "regel_begruendung": r[1],
                          "ki_quelle": u["quelle"]})
    vergleich = {"n": len(paare), "gleich": sum(p["gleich"] for p in paare), "paare": paare,
                 "modus": ("KI " + K.MODELL) if ki_protokoll["modus"] != "platzhalter" and all(p["ki_quelle"].startswith("KI") for p in paare)
                 else "enthält Platzhalter-Urteile statt KI"}
    vorschau = {"stichtag": f"{stichtag:%d.%m.%Y}", "fenster": args.fenster_tage, "quelle": quelle_name, "gemeinsam": gemeinsam,
                "profile": vorschau_profile, "vergleich": vergleich}
    (AUSGABE / "push_demo.html").write_text(V.baue(vorschau), encoding="utf-8")
    (AUSGABE / "ergebnis_lauf.json").write_text(json.dumps(
        {"stichtag": str(stichtag), "fenster_tage": args.fenster_tage, "vergleichsmenge": "ganzer Schnappschuss, CPV + Oberpfalz + Laufzeit, ohne Frist- und Radiusfilter (Radius steckt im Regelurteil)",
         "schnappschuss": quelle_name, "gemeinsam": gemeinsam, "profile": ergebnis_profile, "vergleich": vergleich,
         "ki_protokoll": ki_protokoll}, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"Stichtag {stichtag}, Schnappschuss {quelle_name} (gelesen aus {ordner})")
    for g in gemeinsam:
        print(f"  {g['anzahl']:4d}  {g['name']}")
    for pp in vorschau_profile:
        print(f"Profil {pp['profil']['id']}:")
        for s in pp["stufen"]:
            print(f"  {s['anzahl']:4d}  {s['name']}  {s['notiz']}")
    print(f"Vergleich KI/Regel: {vergleich['gleich']} von {vergleich['n']} gleich ({vergleich['modus']}); "
          "5 Fälle trivial (gleiche Entfernung), kein inhaltlicher Ablehnungsfall, keine Referenz durch einen Menschen")
    print("KI-Protokoll:", ki_protokoll)
    return alle_cards


def senden(alle_cards, args):
    """NUR auf ausdrücklichen Wunsch des Nutzers, mit eigenem Webhook/Postfach. In dieser Demo nicht ausgeführt."""
    import os
    if args.senden_teams:
        import requests
        url = os.environ.get("TEAMS_WEBHOOK_URL")
        if not url and args.senden_teams != "ENV":
            url = args.senden_teams
            print("WARNUNG: Webhook-URL über die Kommandozeile gegeben; sie landet in der Shell-History. Besser: Umgebungsvariable TEAMS_WEBHOOK_URL.")
        if not url:
            sys.exit("Fehler: Umgebungsvariable TEAMS_WEBHOOK_URL fehlt (oder URL hinter --senden-teams angeben).")
        for pid, nr, karte, _ in alle_cards:
            r = requests.post(url, json=karte, timeout=30)
            print(f"Teams {pid} {nr}: HTTP {r.status_code}")
    if args.senden_mail:
        import smtplib
        import ssl
        from email import message_from_bytes
        from email.policy import default
        fehlt = [n for n, w in (("--smtp-host", args.smtp_host), ("--smtp-user", args.smtp_user), ("--mail-an", args.mail_an)) if not w]
        if fehlt:
            sys.exit(f"Fehler: für --senden-mail fehlt {', '.join(fehlt)} (Passwort: Umgebungsvariable DEMO_SMTP_PASSWORD).")
        if "DEMO_SMTP_PASSWORD" not in os.environ:
            sys.exit("Fehler: Umgebungsvariable DEMO_SMTP_PASSWORD fehlt.")
        with smtplib.SMTP(args.smtp_host, args.smtp_port) as s:
            s.starttls(context=ssl.create_default_context())
            s.login(args.smtp_user, os.environ["DEMO_SMTP_PASSWORD"])
            for pid, nr, _, eml in alle_cards:
                m = message_from_bytes(eml, policy=default)
                del m["To"]
                m["To"] = args.mail_an
                del m["From"]
                m["From"] = args.smtp_user
                s.send_message(m)
                print(f"Mail {pid} {nr} an {args.mail_an}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--modus", choices=["offline", "live"], default="offline")
    ap.add_argument("--stichtag", default="2026-10-16", help="festes „heute“ im Offline-Modus (JJJJ-MM-TT)")
    ap.add_argument("--fenster-tage", type=int, default=14)
    ap.add_argument("--daten", help="Schnappschuss-Ordner oder JSON-Kopie (Standard: docs/demo/daten/schnappschuss_demo.json, sonst neuester data/raw/demo_push_*)")
    ap.add_argument("--ki", choices=["cache", "claude", "platzhalter"], default="cache")
    ap.add_argument("--max-aufrufe", type=int, default=20)
    ap.add_argument("--senden-teams", nargs="?", const="ENV", metavar="URL",
                    help="Teams-Workflow-URL aus Umgebungsvariable TEAMS_WEBHOOK_URL (empfohlen); URL hier nur als Rückfall (Shell-History!)")
    ap.add_argument("--senden-mail", action="store_true")
    ap.add_argument("--smtp-host"); ap.add_argument("--smtp-port", type=int, default=587)
    ap.add_argument("--smtp-user"); ap.add_argument("--mail-an")
    args = ap.parse_args()
    karten = pipeline(args)
    if args.senden_teams or args.senden_mail:
        senden(karten, args)
    else:
        print("Es wurde nichts gesendet.")


if __name__ == "__main__":
    main()
