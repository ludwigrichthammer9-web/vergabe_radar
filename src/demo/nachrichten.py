"""Demo Profil-Match: Nachrichten erzeugen (Teams-Adaptive-Card als JSON, E-Mail als .eml). Es wird nichts gesendet."""

import json
import re
from datetime import datetime, timezone, timedelta
from email.message import EmailMessage
from email.policy import default as mail_policy
from html import escape

from daten import norm_ws
from stufen import NUTS3_PUNKTE, eignung_block, naechster_bezugspunkt, orte_im_text

HINWEIS = ("Demo zur Veranschaulichung der Datenübergabe. Kein Rechtsrat, keine Aussage zu Gewinnchancen. "
           "Bitte die Bekanntmachung selbst lesen.")
QUELLE = "Quelle: TED (Tenders Electronic Daily), Auftragsbekanntmachung; Quellenangabe: © Europäische Union, https://ted.europa.eu"


def _de(d):
    return d.strftime("%d.%m.%Y")


_LZ_SATZ = re.compile(r"Laufzeit|Vertragsdauer|verl.ngert|Verl.ngerung|Option|bis zum \d{1,2}\.\d{1,2}\.\d{4}|endet|in Kraft", re.I)


def laufzeit_im_text(b, max_saetze=3, max_zeichen=230):
    """Sätze aus Option, Verlängerung und Beschreibungen, die eine Laufzeit oder Option nennen (einfache Textsuche)."""
    saetze = []
    for q in [*b["option"], *b["verlaengerung"], b["beschreibung_verfahren"], *b["beschreibung_lose"]]:
        for s in re.split(r"(?<=[.!?])\s+", norm_ws(q)):
            if _LZ_SATZ.search(s) and s not in saetze:
                saetze.append(s)
    return [s if len(s) <= max_zeichen else s[:max_zeichen].rstrip() + " …" for s in saetze[:max_saetze]]


def _iso_de(s):
    return datetime.strptime(s, "%Y-%m-%d").strftime("%d.%m.%Y")


def _md_sicher(s):
    """Teams rendert Markdown in TextBlocks; '](' wird entschärft, damit Fremdtext keinen Link bildet."""
    return s.replace("](", "] (") if isinstance(s, str) else s


def inhalt(profil, b, urteil, regel, vorgaenger, stichtag):
    """Sammelt Fakten (aus der Bekanntmachung) und Deutung (KI/Regel) getrennt."""
    nuts = ", ".join(f"{n} {NUTS3_PUNKTE[n][0]}" if n in NUTS3_PUNKTE else n for n in b["nuts"])
    text_orte = orte_im_text(b)
    # Leistungsort: nur Datenfeld "Ort" (der Sitz des Auftraggebers ist nicht der Leistungsort)
    if b["orte"] and text_orte:
        ort = f"{', '.join(b['orte'])} (Datenfeld); zusätzlich im Text, nicht im Datenfeld: {', '.join(text_orte)}"
    elif b["orte"]:
        ort = f"{', '.join(b['orte'])} (Datenfeld)"
    elif text_orte:
        ort = f"Ort im Text, nicht im Datenfeld: {', '.join(text_orte)}"
    else:
        ort = "Ort weder im Datenfeld noch im Text gefunden (einfache Ortssuche)"
    ort += f"; Region laut Datenfeld: {nuts or 'NUTS nicht angegeben'}"
    if text_orte:
        ort += "; die Orte im Text weichen vom Datenfeld ab, einzelne Objekte können weit außerhalb der Region liegen"
    bezug = naechster_bezugspunkt(profil, b)
    if bezug:
        code, km = bezug
        name = NUTS3_PUNKTE[code][0]
        gerundet = int(round(km / 5.0) * 5)
        zahl = f"ca. {gerundet} km" if gerundet else "unter 5 km"
        entfernung = (f"Näherung: {zahl} Luftlinie von {profil['sitz']['ort']} zum Bezugspunkt {code} "
                      f"({name}), nicht zum Objekt")
    else:
        entfernung = "nicht berechenbar"
    if b["fristen"]:
        fr = max(b["fristen"])
        frist = f"{_de(fr)} (noch {(fr - stichtag).days} Tage ab {_de(stichtag)})"
    else:
        frist = "nicht angegeben"
    # Laufzeit: Datenfeld und Text getrennt
    dauer = f"{max(b['laufzeit_monate']):g} Monate" if b["laufzeit_monate"] else "nicht angegeben"
    lz = f"Datenfeld Dauer: {dauer}"
    if b["laufzeit_beginn"] or b["laufzeit_ende"]:
        lz += "; Datenfeld Datum: " + ", ".join(
            x for x in (f"Beginn {_iso_de(b['laufzeit_beginn'][0])}" if b["laufzeit_beginn"] else "",
                        f"Ende {_iso_de(b['laufzeit_ende'][-1])}" if b["laufzeit_ende"] else "") if x)
    lz_text = laufzeit_im_text(b)
    if lz_text:
        marke = "im Text, nicht im Datenfeld" if not b["laufzeit_monate"] else "Verlängerung/Option im Text"
        lz += f"; {marke}: " + " ".join(f"„{s}“" for s in lz_text)
    else:
        lz += "; im Text keine Laufzeitangabe gefunden (einfache Textsuche)"
    wert = b["wert_verfahren"] or b["wert_lose"]
    wert_s = f"{max(wert):,.0f} EUR (geschätzt, laut Bekanntmachung)".replace(",", ".") if wert else "nicht angegeben"
    n_lose = max(len(b["titel_lose"]), len(b["beschreibung_lose"]), 1)
    zitate = [k for k in urteil["kriterien"] if k["zitat"]][:2]
    ist_ki = str(urteil.get("quelle", "")).startswith("KI")
    deutung = (f"KI-Deutung ({urteil['quelle'][4:-1]}; vom Sprachmodell erzeugt, nicht Fakt, Begründung nicht geprüft)" if ist_ki
               else "Platzhalter-Deutung (Stichwortregel, keine KI, nicht Fakt)")
    nicht_ablesbar = [k["kriterium"] for k in urteil["kriterien"] if k["status"] == "nicht ablesbar"]
    e = eignung_block(b)
    return {
        "nr": b["nr"], "titel": b["titel"], "auftraggeber": b["auftraggeber"], "ort": ort, "entfernung": entfernung, "deutung": deutung, "frist": frist, "laufzeit": lz,
        "wert": wert_s, "lose": f"{n_lose} Los(e)", "link": b["link"], "veroeffentlicht": _de(b["veroeffentlicht"]),
        "urteil": urteil["urteil"], "begruendung": urteil["begruendung"], "quelle_urteil": urteil.get("quelle", ""),
        "regel": regel, "zitate": [(k["kriterium"], k["zitat"]) for k in zitate], "nicht_ablesbar": nicht_ablesbar,
        "eignung": "; ".join(e["arten"]) if e["arten"] else "keine Eignungskriterien als Code angegeben",
        "eignung_hinweis": e["hinweis"], "vorgaenger": vorgaenger, "profil_name": profil["name"], "profil_id": profil["id"],
    }


def _zitat_kurz(z, n=220):
    z = " ".join(z.split())
    return z if len(z) <= n else z[:n].rstrip() + " …"


KI_HINWEIS = ("Der KI lagen Titel, Beschreibungen, Eignungs-Freitext und einige Datenfelder vor (nicht Beginn-/Ende-Datum, nicht die Vergabeunterlagen). "
              "Geprüft wird nur, dass Zitate wörtlich im Text stehen; die Begründung selbst wird nicht geprüft.")
_DATENFELD_ZEILE = re.compile(r"^[^:]{0,60}\(Datenfeld[^)]*\):")


def zitat_zeilen(c):
    """Zitate der KI; Zeilen, die wir selbst aus Datenfeldern in den KI-Text eingefügt haben, sind als solche gekennzeichnet."""
    out = []
    for kriterium, z in c["zitate"]:
        art = "Datenfeld-Zeile (von uns eingefügt, kein Bekanntmachungstext)" if _DATENFELD_ZEILE.match(z) else "Zitat aus dem Text (wörtlich geprüft)"
        out.append(f"{art} zu „{kriterium}“: „{_zitat_kurz(z)}“")
    return out


def adaptive_card(c):
    farbe = {"passt": "Good", "unklar": "Warning", "passt nicht": "Attention"}[c["urteil"]]
    fakten = [("Auftraggeber", c["auftraggeber"]), ("Ort", c["ort"]), ("Entfernung", c["entfernung"]), ("Abgabefrist", c["frist"]),
              ("Laufzeit", c["laufzeit"]), ("Wert", c["wert"]), ("Umfang", c["lose"]), ("Veröffentlicht", c["veroeffentlicht"])]
    body = [
        {"type": "TextBlock", "text": f"Neue Ausschreibung: {c['titel']}", "weight": "Bolder", "size": "Medium", "wrap": True},
        {"type": "TextBlock", "text": f"Profil: {c['profil_name']}", "isSubtle": True, "spacing": "None", "wrap": True},
        {"type": "TextBlock", "text": "Fakten aus der Bekanntmachung", "weight": "Bolder", "spacing": "Medium"},
        {"type": "FactSet", "facts": [{"title": k, "value": v} for k, v in fakten]},
        {"type": "TextBlock", "text": "Verlangt laut Bekanntmachung (Eignung, Art der Nachweise)", "weight": "Bolder", "spacing": "Medium"},
        {"type": "TextBlock", "text": f"{c['eignung']}. {c['eignung_hinweis']}", "wrap": True},
        {"type": "TextBlock", "text": f"{c['deutung']}: {c['urteil']}", "weight": "Bolder", "color": farbe, "spacing": "Medium", "wrap": True},
        {"type": "TextBlock", "text": c["begruendung"], "wrap": True},
    ]
    for zeile in zitat_zeilen(c):
        body.append({"type": "TextBlock", "text": zeile, "wrap": True, "isSubtle": True})
    body.append({"type": "TextBlock", "text": "Nicht ablesbar: " + ", ".join(c["nicht_ablesbar"]), "wrap": True})
    body.append({"type": "TextBlock", "text": KI_HINWEIS, "wrap": True, "size": "Small", "isSubtle": True})
    if c["vorgaenger"]:
        v = c["vorgaenger"]
        body.append({"type": "TextBlock", "wrap": True, "text": f"Vorgänger laut Vertragsliste (Prototyp, eindeutiger Titeltreffer): {v['los_titel']}, "
                                                               f"Ende der Grundlaufzeit {v['ende_grundlaufzeit']} (Herkunft: {v['ende_herkunft']})."})
    body.append({"type": "TextBlock", "text": f"{HINWEIS} {QUELLE}", "wrap": True, "size": "Small", "isSubtle": True, "spacing": "Medium"})
    karte = {"$schema": "http://adaptivecards.io/schemas/adaptive-card.json", "type": "AdaptiveCard", "version": "1.2", "body": body,
             "actions": [{"type": "Action.OpenUrl", "title": "Bekanntmachung auf TED", "url": c["link"]}]}
    for blk in karte["body"]:  # Markdown-Links aus Fremdtext entschärfen
        if "text" in blk:
            blk["text"] = _md_sicher(blk["text"])
        for f in blk.get("facts", []):
            f["value"] = _md_sicher(f["value"])
    return {"type": "message", "attachments": [{"contentType": "application/vnd.microsoft.card.adaptive", "contentUrl": None, "content": karte}]}


def mail_text(c):
    z = [f"Neue Ausschreibung: {c['titel']}", f"Profil: {c['profil_name']}", "", "FAKTEN AUS DER BEKANNTMACHUNG",
         f"Auftraggeber: {c['auftraggeber']}", f"Ort: {c['ort']}", f"Entfernung: {c['entfernung']}", f"Abgabefrist: {c['frist']}",
         f"Laufzeit: {c['laufzeit']}",
         f"Wert: {c['wert']}", f"Umfang: {c['lose']}", f"Veröffentlicht: {c['veroeffentlicht']}", f"Bekanntmachung: {c['link']}", "",
         "VERLANGT LAUT BEKANNTMACHUNG (EIGNUNG, ART DER NACHWEISE)", f"{c['eignung']}. {c['eignung_hinweis']}", "",
         f"{c['deutung'].upper()}: {c['urteil']}", c["begruendung"]]
    z += zitat_zeilen(c)
    z.append("Nicht ablesbar: " + ", ".join(c["nicht_ablesbar"]))
    z.append(KI_HINWEIS)
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
         zeile("Auftraggeber", c["auftraggeber"]), zeile("Ort", c["ort"]), zeile("Entfernung", c["entfernung"]),
         zeile("Abgabefrist", c["frist"]), zeile("Laufzeit", c["laufzeit"]), zeile("Wert", c["wert"]), zeile("Umfang", c["lose"]),
         zeile("Veröffentlicht", c["veroeffentlicht"]), "</table>",
         f"<p><a href='{escape(c['link'])}'>Bekanntmachung auf TED</a></p>",
         f"<p><b>Verlangt laut Bekanntmachung (Eignung, Art der Nachweise)</b><br>{escape(c['eignung'])}. {escape(c['eignung_hinweis'])}</p>",
         f"<p><b>{escape(c['deutung'])}: {escape(c['urteil'])}</b><br>{escape(c['begruendung'])}"]
    for zeile_ in zitat_zeilen(c):
        h.append(f"<br><span style='color:#555'>{escape(zeile_)}</span>")
    h.append(f"<br>Nicht ablesbar: {escape(', '.join(c['nicht_ablesbar']))}<br><small>{escape(KI_HINWEIS)}</small></p>")
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
