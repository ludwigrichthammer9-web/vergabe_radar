"""Demo Profil-Match: eigenständige Vorschauseite (HTML, ohne Skripte, ohne externe Ressourcen)."""

from html import escape

from nachrichten import HINWEIS, KI_HINWEIS, QUELLE, mail_html_fragment, zitat_zeilen

CSS = """
:root{color-scheme:light dark;--bg:#F2F2F7;--card:#fff;--ink:#1C1C1E;--grey:#6C6C70;--blue:#007AFF;--green:#34C759;--orange:#FF9500;--red:#FF3B30;--sep:rgba(60,60,67,.16);
--fill:rgba(120,120,128,.12);--inner:#F2F2F7;--glass:rgba(242,242,247,.78);--shadow:0 1px 2px rgba(0,0,0,.04),0 8px 24px rgba(0,0,0,.06);--ease:cubic-bezier(.2,.8,.2,1);--accent:#5856D6;--tagg:#1E7B3A;--tago:#A15C00;--tagr:#C0261C}
@media (prefers-color-scheme:dark){:root{--bg:#000;--card:#1C1C1E;--ink:#F2F2F7;--grey:#AEAEB2;--blue:#0A84FF;--sep:rgba(235,235,245,.16);--fill:rgba(120,120,128,.24);--inner:#2C2C2E;
--glass:rgba(28,28,30,.72);--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.5);--accent:#7D7AFF;--tagg:#30D158;--tago:#FFB340;--tagr:#FF6961}}
*{box-sizing:border-box}
body{font:15px/1.47 -apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display",system-ui,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;margin:0;background:var(--bg);color:var(--ink)}
a{color:var(--blue)}
.banner{position:sticky;top:0;z-index:20;background:var(--glass);-webkit-backdrop-filter:blur(20px) saturate(180%);backdrop-filter:blur(20px) saturate(180%);border-bottom:1px solid var(--sep);color:var(--red);padding:12px 24px;font-weight:600;font-size:14px}
h1{font:700 34px/1.12 -apple-system,BlinkMacSystemFont,"SF Pro Display",system-ui,"Segoe UI",sans-serif;letter-spacing:-.02em;margin:32px 24px 8px}
h2{font-size:22px;font-weight:700;letter-spacing:-.01em;margin:0 0 16px} h3{letter-spacing:-.005em}
.sub{margin:0 24px 16px;color:var(--grey);font-size:13px}
section.profil{margin:24px;padding:24px;background:var(--card);border-radius:22px;box-shadow:var(--shadow)}
.grid{display:grid;grid-template-columns:260px 300px 1fr 1fr;gap:16px;align-items:start}
@media(max-width:1300px){.grid{grid-template-columns:1fr 1fr}}
@media(max-width:700px){.grid{grid-template-columns:1fr}h1{font-size:28px}}
.box{border-radius:18px;padding:16px;background:var(--inner);font-size:13px}
.box h3{margin:0 0 8px;font-size:15px}
dl{margin:0} dt{font-weight:600;margin-top:8px} dd{margin:0}
.stufe{margin:8px 0} .bar{height:8px;margin-top:4px;background:var(--accent);border-radius:999px;min-width:2px}
.stufe small{color:var(--grey);display:block}
.teams{background:var(--inner)} .card{background:var(--card);border-left:4px solid var(--accent);border-radius:14px;box-shadow:var(--shadow);padding:16px;margin:12px 0;font-size:13px}
.card.passt{border-left-color:var(--green)}.card.unklar{border-left-color:var(--orange)}
.card .kopf{font-weight:700;font-size:15px} .card .klein{font-size:12px;color:var(--grey)}
.card table{font-size:12px;border-collapse:collapse;margin:8px 0} .card td{padding:2px 12px 2px 0;vertical-align:top}
.card a.knopf{display:inline-flex;align-items:center;min-height:44px;background:var(--fill);color:var(--blue);padding:8px 16px;border-radius:12px;text-decoration:none;font-weight:600;margin-top:8px;transition:background-color .2s var(--ease),transform .15s var(--ease)}
.card a.knopf:hover{background:var(--sep)} .card a.knopf:active{transform:scale(.97)}
:focus-visible{outline:3px solid var(--blue);outline-offset:2px;border-radius:8px}
details{background:var(--card);border-radius:14px;box-shadow:var(--shadow);margin:8px 0;padding:0 16px 8px}
summary{cursor:pointer;font-weight:600;min-height:44px;display:flex;align-items:center;transition:color .2s var(--ease)} summary:hover{color:var(--blue)}
.mail{background:#fff;color:#1C1C1E;border-radius:12px;padding:16px;margin-top:4px} .mail a{color:#0066CC}
table.v{border-collapse:separate;border-spacing:0;font-size:12px;width:100%} table.v td,table.v th{border-bottom:1px solid var(--sep);padding:8px 12px;text-align:left;vertical-align:top}
table.v th{color:var(--grey);font-weight:600}
table.v tbody tr:hover,table.v tr:hover td{background:var(--fill)}
footer{margin:24px;font-size:12px;color:var(--grey)}
.tag{display:inline-block;padding:2px 10px;border-radius:999px;font-size:11px;font-weight:600}
.tag.passt{background:rgba(52,199,89,.16);color:var(--tagg)}.tag.unklar{background:rgba(255,149,0,.16);color:var(--tago)}.tag.pn{background:rgba(255,59,48,.14);color:var(--tagr)}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
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
        mails = "".join(f"<details><summary>{escape(betreff)}</summary><div class='mail'>{mail_html_fragment(c)}</div></details>" for betreff, c in p["mails"])
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
