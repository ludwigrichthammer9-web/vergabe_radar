"""Demo Profil-Match: Nachrichten erzeugen (Teams-Adaptive-Card als JSON, E-Mail als .eml). Es wird nichts gesendet."""

import json
from datetime import datetime, timezone, timedelta
from email.message import EmailMessage
from email.policy import default as mail_policy
from html import escape

from stufen import NUTS3_PUNKTE, eignung_block

HINWEIS = ("Demo zur Veranschaulichung der Datenübergabe. Kein Rechtsrat, keine Aussage zu Gewinnchancen. "
           "Bitte die Bekanntmachung selbst lesen.")
QUELLE = "Quelle: TED (Tenders Electronic Daily), Auftragsbekanntmachung; Quellenangabe: © Europäische Union, https://ted.europa.eu"


def _de(d):
    return d.strftime("%d.%m.%Y")


def inhalt(profil, b, urteil, regel, vorgaenger, stichtag):
    """Sammelt Fakten (aus der Bekanntmachung) und Deutung (KI/Regel) getrennt."""
    ort_teile = b["orte"]  # nur Leistungsort; der Sitz des Auftraggebers (buyer-city) ist nicht der Leistungsort
    nuts = ", ".join(f"{n} {NUTS3_PUNKTE[n][0]}" if n in NUTS3_PUNKTE else n for n in b["nuts"])
    entf = b.get("_entfernung")
    ort = (f"{', '.join(t for t in ort_teile if t)} " if ort_teile else "Ort nicht genannt ") + f"({nuts or 'NUTS nicht angegeben'})"
    ort += f"; Luftlinie ca. {entf:.0f} km von {profil['sitz']['ort']} (Näherung)" if entf is not None else "; Entfernung nicht berechenbar"
    if b["fristen"]:
        fr = max(b["fristen"])
        frist = f"{_de(fr)} (noch {(fr - stichtag).days} Tage ab {_de(stichtag)})"
    else:
        frist = "nicht angegeben"
    if b["laufzeit_monate"]:
        lz = f"{max(b['laufzeit_monate']):g} Monate"
        if b["laufzeit_beginn"]:
            lz += f", Beginn {', '.join(b['laufzeit_beginn'][:1])}"
    else:
        lz = "im Datenfeld nicht angegeben (ggf. im Text)"
    wert = b["wert_verfahren"] or b["wert_lose"]
    wert_s = f"{max(wert):,.0f} EUR (geschätzt, laut Bekanntmachung)".replace(",", ".") if wert else "nicht angegeben"
    n_lose = max(len(b["titel_lose"]), len(b["beschreibung_lose"]), 1)
    zitate = [k for k in urteil["kriterien"] if k["zitat"]][:2]
    nicht_ablesbar = [k["kriterium"] for k in urteil["kriterien"] if k["status"] == "nicht ablesbar"]
    e = eignung_block(b)
    return {
        "nr": b["nr"], "titel": b["titel"], "auftraggeber": b["auftraggeber"], "ort": ort, "frist": frist, "laufzeit": lz,
        "wert": wert_s, "lose": f"{n_lose} Los(e)", "link": b["link"], "veroeffentlicht": _de(b["veroeffentlicht"]),
        "urteil": urteil["urteil"], "begruendung": urteil["begruendung"], "quelle_urteil": urteil.get("quelle", ""),
        "regel": regel, "zitate": [(k["kriterium"], k["zitat"]) for k in zitate], "nicht_ablesbar": nicht_ablesbar,
        "eignung": "; ".join(e["arten"]) if e["arten"] else "keine Eignungskriterien als Code angegeben",
        "eignung_hinweis": e["hinweis"], "vorgaenger": vorgaenger, "profil_name": profil["name"], "profil_id": profil["id"],
    }


def _zitat_kurz(z, n=220):
    z = " ".join(z.split())
    return z if len(z) <= n else z[:n].rstrip() + " …"


def adaptive_card(c):
    farbe = {"passt": "Good", "unklar": "Warning", "passt nicht": "Attention"}[c["urteil"]]
    fakten = [("Auftraggeber", c["auftraggeber"]), ("Ort", c["ort"]), ("Abgabefrist", c["frist"]), ("Laufzeit", c["laufzeit"]),
              ("Wert", c["wert"]), ("Umfang", c["lose"]), ("Veröffentlicht", c["veroeffentlicht"])]
    body = [
        {"type": "TextBlock", "text": f"Neue Ausschreibung: {c['titel']}", "weight": "Bolder", "size": "Medium", "wrap": True},
        {"type": "TextBlock", "text": f"Profil: {c['profil_name']}", "isSubtle": True, "spacing": "None", "wrap": True},
        {"type": "TextBlock", "text": "Fakten aus der Bekanntmachung", "weight": "Bolder", "spacing": "Medium"},
        {"type": "FactSet", "facts": [{"title": k, "value": v} for k, v in fakten]},
        {"type": "TextBlock", "text": "Verlangt laut Bekanntmachung (Eignung, Art der Nachweise)", "weight": "Bolder", "spacing": "Medium"},
        {"type": "TextBlock", "text": f"{c['eignung']}. {c['eignung_hinweis']}", "wrap": True},
        {"type": "TextBlock", "text": f"Einordnung (Deutung, nicht Fakt): {c['urteil']}", "weight": "Bolder", "color": farbe, "spacing": "Medium"},
        {"type": "TextBlock", "text": f"{c['begruendung']} ({c['quelle_urteil']})", "wrap": True},
    ]
    for kriterium, z in c["zitate"]:
        body.append({"type": "TextBlock", "text": f"Zitat zu „{kriterium}“: „{_zitat_kurz(z)}“", "wrap": True, "isSubtle": True})
    body.append({"type": "TextBlock", "text": "Nicht ablesbar: " + ", ".join(c["nicht_ablesbar"]), "wrap": True})
    if c["vorgaenger"]:
        v = c["vorgaenger"]
        body.append({"type": "TextBlock", "wrap": True, "text": f"Vorgänger laut Vertragsliste (Prototyp, eindeutiger Titeltreffer): {v['los_titel']}, "
                                                               f"Ende der Grundlaufzeit {v['ende_grundlaufzeit']} (Herkunft: {v['ende_herkunft']})."})
    body.append({"type": "TextBlock", "text": f"{HINWEIS} {QUELLE}", "wrap": True, "size": "Small", "isSubtle": True, "spacing": "Medium"})
    karte = {"$schema": "http://adaptivecards.io/schemas/adaptive-card.json", "type": "AdaptiveCard", "version": "1.2", "body": body,
             "actions": [{"type": "Action.OpenUrl", "title": "Bekanntmachung auf TED", "url": c["link"]}]}
    return {"type": "message", "attachments": [{"contentType": "application/vnd.microsoft.card.adaptive", "contentUrl": None, "content": karte}]}


def mail_text(c):
    z = [f"Neue Ausschreibung: {c['titel']}", f"Profil: {c['profil_name']}", "", "FAKTEN AUS DER BEKANNTMACHUNG",
         f"Auftraggeber: {c['auftraggeber']}", f"Ort: {c['ort']}", f"Abgabefrist: {c['frist']}", f"Laufzeit: {c['laufzeit']}",
         f"Wert: {c['wert']}", f"Umfang: {c['lose']}", f"Veröffentlicht: {c['veroeffentlicht']}", f"Bekanntmachung: {c['link']}", "",
         "VERLANGT LAUT BEKANNTMACHUNG (EIGNUNG, ART DER NACHWEISE)", f"{c['eignung']}. {c['eignung_hinweis']}", "",
         f"EINORDNUNG (DEUTUNG, NICHT FAKT): {c['urteil']}", f"{c['begruendung']} ({c['quelle_urteil']})"]
    for kriterium, q in c["zitate"]:
        z.append(f"Zitat zu {kriterium}: \"{_zitat_kurz(q)}\"")
    z.append("Nicht ablesbar: " + ", ".join(c["nicht_ablesbar"]))
    if c["vorgaenger"]:
        v = c["vorgaenger"]
        z.append(f"Vorgänger laut Vertragsliste (Prototyp): {v['los_titel']}, Ende der Grundlaufzeit {v['ende_grundlaufzeit']}.")
    z += ["", "---", HINWEIS, QUELLE]
    return "\n".join(z)


def mail_html_fragment(c):
    def zeile(k, v):
        return f"<tr><td style='padding:2px 10px 2px 0;color:#555;vertical-align:top'>{escape(k)}</td><td>{escape(v)}</td></tr>"
    h = [f"<h3 style='margin:0 0 4px'>Neue Ausschreibung: {escape(c['titel'])}</h3>",
         f"<div style='color:#666;margin-bottom:8px'>Profil: {escape(c['profil_name'])}</div>",
         "<b>Fakten aus der Bekanntmachung</b><table style='font-size:14px'>",
         zeile("Auftraggeber", c["auftraggeber"]), zeile("Ort", c["ort"]), zeile("Abgabefrist", c["frist"]),
         zeile("Laufzeit", c["laufzeit"]), zeile("Wert", c["wert"]), zeile("Umfang", c["lose"]),
         zeile("Veröffentlicht", c["veroeffentlicht"]), "</table>",
         f"<p><a href='{escape(c['link'])}'>Bekanntmachung auf TED</a></p>",
         f"<p><b>Verlangt laut Bekanntmachung (Eignung, Art der Nachweise)</b><br>{escape(c['eignung'])}. {escape(c['eignung_hinweis'])}</p>",
         f"<p><b>Einordnung (Deutung, nicht Fakt): {escape(c['urteil'])}</b><br>{escape(c['begruendung'])} <i>({escape(c['quelle_urteil'])})</i>"]
    for kriterium, q in c["zitate"]:
        h.append(f"<br><span style='color:#555'>Zitat zu {escape(kriterium)}: „{escape(_zitat_kurz(q))}“</span>")
    h.append(f"<br>Nicht ablesbar: {escape(', '.join(c['nicht_ablesbar']))}</p>")
    if c["vorgaenger"]:
        v = c["vorgaenger"]
        h.append(f"<p>Vorgänger laut Vertragsliste (Prototyp): {escape(v['los_titel'])}, Ende der Grundlaufzeit {escape(v['ende_grundlaufzeit'])}.</p>")
    h.append(f"<p style='font-size:12px;color:#666'>{escape(HINWEIS)}<br>{escape(QUELLE)}</p>")
    return "\n".join(h)


def eml(c, stichtag):
    m = EmailMessage(policy=mail_policy)
    m["From"] = "Vergabe-Radar Demo <demo-radar@example.invalid>"
    m["To"] = "Beispielbetrieb <betrieb@example.invalid>"
    m["Subject"] = f"[Demo] {c['urteil'].capitalize()}: {c['titel'][:90]} (Frist {c['frist'].split(' (')[0]})"
    m["Date"] = datetime(stichtag.year, stichtag.month, stichtag.day, 8, 0, tzinfo=timezone(timedelta(hours=2 if 4 <= stichtag.month <= 10 else 1)))
    m["Message-ID"] = f"<demo-{c['profil_id']}-{c['nr']}@example.invalid>"
    m["X-Demo"] = "Veranschaulichung, nicht gesendet"
    m.set_content(mail_text(c))
    m.add_alternative(f"<html><body style='font-family:Segoe UI,Arial,sans-serif;font-size:14px'>{mail_html_fragment(c)}</body></html>", subtype="html")
    return m.as_bytes()


def card_json(c):
    return json.dumps(adaptive_card(c), ensure_ascii=False, indent=2)
