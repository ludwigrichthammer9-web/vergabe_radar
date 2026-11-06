"""Demo Profil-Match: eigenständige Vorschauseite (HTML, ohne Skripte, ohne externe Ressourcen)."""

from html import escape

from nachrichten import HINWEIS, KI_HINWEIS, QUELLE, mail_html_fragment, zitat_zeilen

CSS = """
body{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f3f2f1;color:#201f1e}
.banner{background:#8a1c1c;color:#fff;padding:10px 20px;font-weight:600}
h1{font-size:20px;margin:16px 20px 4px} h2{font-size:17px;margin:0 0 8px}
.sub{margin:0 20px 8px;color:#555;font-size:13px}
section.profil{margin:16px 20px;padding:12px;background:#fff;border:1px solid #d2d0ce;border-radius:6px}
.grid{display:grid;grid-template-columns:260px 300px 1fr 1fr;gap:12px;align-items:start}
@media(max-width:1300px){.grid{grid-template-columns:1fr 1fr}}
.box{border:1px solid #d2d0ce;border-radius:6px;padding:10px;background:#faf9f8;font-size:13px}
.box h3{margin:0 0 6px;font-size:14px}
dl{margin:0} dt{font-weight:600;margin-top:6px} dd{margin:0}
.stufe{margin:6px 0} .bar{height:14px;background:#5b5fc7;border-radius:3px;min-width:2px}
.stufe small{color:#605e5c;display:block}
.teams{background:#ebebf5} .card{background:#fff;border-left:4px solid #5b5fc7;border-radius:4px;padding:8px;margin:8px 0;font-size:13px}
.card.passt{border-left-color:#107c10}.card.unklar{border-left-color:#c19c00}
.card .kopf{font-weight:700;font-size:14px} .card .klein{font-size:11px;color:#605e5c}
.card table{font-size:12px;border-collapse:collapse} .card td{padding:1px 8px 1px 0;vertical-align:top}
.card a.knopf{display:inline-block;border:1px solid #5b5fc7;color:#5b5fc7;padding:3px 8px;border-radius:3px;text-decoration:none;margin-top:4px}
details{background:#fff;border:1px solid #d2d0ce;border-radius:4px;margin:6px 0;padding:6px 8px}
summary{cursor:pointer;font-weight:600}
table.v{border-collapse:collapse;font-size:12px;width:100%} table.v td,table.v th{border:1px solid #d2d0ce;padding:3px 6px;text-align:left;vertical-align:top}
footer{margin:16px 20px;font-size:12px;color:#605e5c}
.tag{display:inline-block;padding:0 6px;border-radius:8px;font-size:11px;color:#fff}.tag.passt{background:#107c10}.tag.unklar{background:#9a7b00}.tag.pn{background:#a4262c}
"""


def _tag(u):
    return f"<span class='tag {'pn' if u == 'passt nicht' else u}'>{escape(u)}</span>"


def _card_html(c):
    fakt = [("Auftraggeber", c["auftraggeber"]), ("Ort", c["ort"]), ("Entfernung", c["entfernung"]), ("Abgabefrist", c["frist"]),
            ("Laufzeit", c["laufzeit"]), ("Wert", c["wert"]), ("Umfang", c["lose"])]
    z = "".join(f"<div class='klein'>{escape(zeile)}</div>" for zeile in zitat_zeilen(c))
    vg = ""
    if c["vorgaenger"]:
        vg = (f"<div class='klein'>Vorgänger laut Vertragsliste (Prototyp): {escape(c['vorgaenger']['los_titel'])}, "
              f"Ende der Grundlaufzeit {escape(c['vorgaenger']['ende_grundlaufzeit'])}</div>")
    return (f"<div class='card {'unklar' if c['urteil'] == 'unklar' else 'passt'}'><div class='kopf'>Neue Ausschreibung: {escape(c['titel'])}</div>"
            f"<div class='klein'>Profil: {escape(c['profil_name'])}</div>"
            f"<table>{''.join(f'<tr><td>{escape(k)}</td><td>{escape(v)}</td></tr>' for k, v in fakt)}</table>"
            f"<div><b>Verlangt (Eignung, Art):</b> {escape(c['eignung'])}. <span class='klein'>{escape(c['eignung_hinweis'])}</span></div>"
            f"<div><b>{escape(c['deutung'])}:</b> {_tag(c['urteil'])} {escape(c['begruendung'])}</div>{z}"
            f"<div><b>Nicht ablesbar:</b> {escape(', '.join(c['nicht_ablesbar']))}</div>"
            f"<div class='klein'>{escape(KI_HINWEIS)}</div>{vg}"
            f"<a class='knopf' href='{escape(c['link'])}'>Bekanntmachung auf TED</a>"
            f"<div class='klein'>{escape(HINWEIS)}</div></div>")


def _profil_html(profil):
    zert = ", ".join(profil["zertifikate"]) or "keine"
    return (f"<div class='box'><h3>Profil (erfunden)</h3><b>{escape(profil['name'])}</b><dl>"
            f"<dt>Sitz / Radius</dt><dd>{escape(profil['sitz']['ort'])}, {profil['radius_km']} km</dd>"
            f"<dt>Leistungen</dt><dd>{escape(', '.join(profil['leistungen']))}</dd>"
            f"<dt>Objektarten</dt><dd>{escape(', '.join(profil['objektarten']))}</dd>"
            f"<dt>Wert (nur Anzeige)</dt><dd>{profil['wert_min_eur']:,} bis {profil['wert_max_eur']:,} EUR".replace(",", ".") + "</dd>"
            f"<dt>Mindestlaufzeit</dt><dd>{profil['laufzeit_min_monate']} Monate</dd>"
            f"<dt>Nicht aus Bekanntmachung ablesbar</dt><dd>Zertifikate ({escape(zert)}), "
            f"max. {profil['max_neue_objekte_gleichzeitig']} neue Objekte gleichzeitig (Kapazität), Personal, Tarifbindung</dd></dl></div>")


def _trichter_html(gemeinsam, stufen):
    alle = gemeinsam + stufen
    maxi = max(s["anzahl"] for s in alle) or 1
    teile = []
    for s in alle:
        breite = max(2, int(100 * s["anzahl"] / maxi))
        teile.append(f"<div class='stufe'><b>{s['anzahl']}</b> {escape(s['name'])}<div class='bar' style='width:{breite}%'></div>"
                     f"{'<small>' + escape(s['notiz']) + '</small>' if s.get('notiz') else ''}</div>")
    return "<div class='box'><h3>Trichter (Anzahl Bekanntmachungen)</h3>" + "".join(teile) + "</div>"


def baue(daten):
    """daten: dict mit stichtag, fenster, quelle, gemeinsam, profile=[{profil, stufen, karten(list c), mails(list (betreff, c))}], vergleich."""
    teile = [f"<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'><title>Demo Profil-Match mit KI-Stufe</title><style>{CSS}</style></head><body>",
             "<div class='banner'>Demo zur Veranschaulichung der Datenübergabe; kein Produkt, keine Nachfrage belegt.</div>",
             "<h1>Profil-Match mit KI-Stufe: Treffer landen im Arbeitswerkzeug (Demo)</h1>",
             f"<p class='sub'>Wiedergabe aus lokalen TED-Daten (Schnappschuss {escape(daten['quelle'])}), festes „heute“: {escape(daten['stichtag'])}, "
             f"Veröffentlichungen der letzten {daten['fenster']} Tage. Nichts wurde gesendet. Erfundene Profile, öffentliche Auftraggeber.</p>"]
    for p in daten["profile"]:
        teile.append(f"<section class='profil'><h2>Profil {escape(p['profil']['id'])}: {escape(p['profil']['name'])}</h2><div class='grid'>")
        teile.append(_profil_html(p["profil"]))
        teile.append(_trichter_html(daten["gemeinsam"], p["stufen"]))
        teile.append("<div class='box teams'><h3>Teams-Kanal (Vorschau der Adaptive Cards)</h3>" +
                     ("".join(_card_html(c) for c in p["karten"]) or "<i>keine Nachricht</i>") + "</div>")
        mails = "".join(f"<details><summary>{escape(betreff)}</summary>{mail_html_fragment(c)}</details>" for betreff, c in p["mails"])
        teile.append("<div class='box'><h3>Posteingang (Vorschau der E-Mails)</h3>" + (mails or "<i>keine Nachricht</i>") + "</div>")
        teile.append("</div></section>")
    v = daten["vergleich"]
    zeilen = "".join(f"<tr><td>{escape(r['profil'])}</td><td>{escape(r['nr'])}</td><td>{escape(r['titel'][:70])}</td><td>{escape(r['ki'])}</td>"
                     f"<td>{escape(r['regel'])}</td><td>{'ja' if r['gleich'] else '<b>nein</b>'}</td></tr>" for r in v["paare"])
    triv = sum(1 for r in v["paare"] if r["regel"] == "passt nicht" and r["gleich"] and r["regel_begruendung"].startswith("Entfernung"))
    teile.append("<section class='profil'><h2>KI-Urteil gegen regelbasiertes Urteil (Vergleich, keine Genauigkeitsaussage)</h2>"
                 f"<p class='sub' style='margin:0 0 6px'>{v['gleich']} von {v['n']} Fällen gleich ({escape(v['modus'])}); {triv} Fälle trivial "
                 "(gleiche Entfernung), kein inhaltlicher Ablehnungsfall: Ob die KI fachlich ablehnen kann, ist ungetestet. "
                 "Keine Referenz durch einen Menschen; beide Urteile können falsch sein.</p>"
                 "<table class='v'><tr><th>Profil</th><th>Bekanntmachung</th><th>Titel</th><th>KI</th><th>Regel</th><th>gleich</th></tr>" + zeilen + "</table></section>")
    teile.append(f"<footer>{escape(QUELLE)}. Lizenz: TED-Daten sind laut Rechtshinweis der TED-Seite frei wiederverwendbar mit Quellenangabe "
                 "(Wortlaut selbst prüfen). Hinweis: " + escape(HINWEIS) + "</footer></body></html>")
    return "\n".join(teile)
