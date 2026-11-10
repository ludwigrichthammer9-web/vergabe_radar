"""Phase 6: Prototyp-Webseite der Vertragsliste (eine statische HTML-Datei mit Filtern, ohne Server, ohne externe Skripte/Schriften).

Eingaben: reports/beispiel_liste_oberpfalz.csv (aus src/report/beispiel_liste.py, Fassung der Iteration 9)
          reports/wettbewerbsbild_oberpfalz.csv (Paket A: Auftragnehmer, Zuschlagswert, Zahl der Angebote aus dem eForms-XML)
Aufruf:   .venv\\Scripts\\python -I src/report/webseite.py      Ausgabe: docs/prototyp/vertragsliste.html
Keine Terminprognose (Iteration 5): gefiltert wird nach dem Ende der Grundlaufzeit laut Bekanntmachung; das Höchstende ist nur Hinweis.

NUTS-Namen: geprüft am 05.11.2026 gegen die Tabelle „NUTS statistical regions of Germany“ (Wikipedia, nennt Verordnung (EU) 2016/2066;
Eurostat-Seite selbst nicht abgerufen) und gegen die Daten der Liste (z. B. DE234 = Landkreis Amberg-Sulzbach, DE23A = Landkreis Tirschenreuth,
DE231 = Stadt Amberg, DE236 = Stadt Neumarkt i. d. OPf.). Die Namen aus dem Gedächtnis stimmten; geändert wurde nur die Schreibweise
(„Regensburg (Landkreis)“ bleibt, Quelle schreibt „Regensburg, Landkreis“). Die Schreibweise der Quelle sagt nichts über Stand NUTS 2021 aus;
die Codes DE231 bis DE23A sind seit NUTS 2016 unverändert (nicht selbst gegen Eurostat belegt).
"""

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # für den Import von export_vertragsliste (Schema-Spalten der Auswahl-CSV)
ROOT = Path(__file__).resolve().parent.parent.parent
CSV = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
CSV_W = ROOT / "reports" / "wettbewerbsbild_oberpfalz.csv"
OUT = ROOT / "docs" / "prototyp" / "vertragsliste.html"
NUTS = {"DE231": "Amberg (Stadt)", "DE232": "Regensburg (Stadt)", "DE233": "Weiden i. d. OPf. (Stadt)", "DE234": "Amberg-Sulzbach",
        "DE235": "Cham", "DE236": "Neumarkt i. d. OPf.", "DE237": "Neustadt a. d. Waldnaab", "DE238": "Regensburg (Landkreis)",
        "DE239": "Schwandorf", "DE23A": "Tirschenreuth"}
STUFEN = {"A": "Höchstende steht ausdrücklich in Text oder Feld, oder das Ende wurde aus dem Text berichtigt. Herkunft der Angabe, nicht Verlässlichkeit: bei den Losen, die Regel 1b ändert, stimmten 8 von 15 mit dem Prüfer überein (Prüfung der Iteration 7, ältere Regelfassung)",
          "B": "Höchstende berechnet (Anzahl × Länge der Verlängerungen); das Enddatum kann schon das Höchstende sein",
          "C": "keine Angabe zur Verlängerung; Höchstende = Grundlaufzeit angenommen",
          "D": "Verlängerung erwähnt, Länge oder Anzahl fehlt; Höchstende unbestimmbar",
          "E": "Ende nur geschätzt (Veröffentlichung + Dauer, ungeprüft)", "F": "kein Ende bekannt"}
# Sonderfall aus docs/iterationen.md (Nachtrag zu 527230-2026): Listenwert bleibt unverändert, nur Hinweis
SONDER = {"527230-2026": "Interimsvergabe: Dauerfeld enthält die Option; Grundlaufzeit vermutlich bis 31.01.2027",
          "533946-2026": "Dauerfeld enthält die Option: Text nennt 2 Jahre Festlaufzeit + 3x1 Jahr Option; Grundlaufzeit vermutlich bis 30.09.2028"}  # Paket C (Fehlertyp „Dauerfeld = Gesamtdauer“)


def num(s: str):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def lade_wettbewerb() -> dict:
    """Schlüssel (Bekanntmachung, Los als int) -> belegte Wettbewerbsfelder; fehlt etwas, bleibt None."""
    with CSV_W.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    out = {}
    for r in rows:
        wert = num(r["wert_eur"]) if r["wert_status"] == "angegeben" else None
        if wert is not None and wert <= 1:  # Platzhalter nie als Wert zeigen
            wert = None
        if r["angebote_status"] == "angegeben":
            ang, mind = num(r["angebote"]), False
        elif r["angebote_status"] == "nur_elektronisch":
            ang, mind = num(r["angebote_elektronisch"]), True
        else:
            ang, mind = None, False
        out[(r["notice"], int(r["los"]))] = {
            "w": r["gewinner"] if r["gewinner"] and r["mehrfachgewinner"] != "True" else None, "mg": r["mehrfachgewinner"] == "True",
            "wv": wert, "wz": r["wert_zurueckgehalten"] == "True",
            "ang": int(ang) if ang is not None else None, "am": mind}
    return out


def lade() -> list[dict]:
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    wb = lade_wettbewerb()
    from export_vertragsliste import NAMEN, baue_zeilen  # erst hier, weil der Export seinerseits NUTS/SONDER aus dieser Datei lädt
    ex = {(z["bekanntmachung"], z["los"]): [z[k] or "" for k in NAMEN] for z in baue_zeilen()}  # Zeilen im Spaltenschema des Exports (docs/export_schema.md)
    out = []
    for r in rows:
        codes = r["nuts"].split()
        w = wb.get((r["notice"], int(r["los"])), {})
        out.append({"n": r["notice"], "u": r["ted_link"], "v": r["veroeffentlicht"], "a": r["auftraggeber"], "l": r["los"], "t": r["los_titel"],
                    "r": [NUTS.get(c, c) for c in codes], "b": r["beginn"], "e": r["gl_ende"] or r["gl_geschaetzt"], "g": r["gl_herkunft"], "h": r["hoechstende"],
                    "hh": r["hoechstende_herkunft"], "s": r["stufe"], "st": r["status"], "ge": not r["gl_ende"] and bool(r["gl_geschaetzt"]),
                    "x": r["auch_ausserhalb"] == "True", "w": w.get("w"), "wv": w.get("wv"), "wz": w.get("wz", False),
                    "ang": w.get("ang"), "am": w.get("am", False), "wb": bool(w), "mg": w.get("mg", False), "so": SONDER.get(r["notice"], ""),
                    "ex": ex[(r["notice"], str(int(r["los"])))]})
    return out


SEITE = r"""<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark"><script>try{var t=localStorage.getItem("vr-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>
<title>Vertragsliste Gebäudereinigung Oberpfalz (Prototyp)</title>
<style>
:root{color-scheme:light dark;--bg:#F2F2F7;--card:#fff;--ink:#1C1C1E;--grey:#6C6C70;--blue:#34618F;--green:#34C759;--orange:#FF9500;--red:#FF3B30;--onblue:#fff;--sep:rgba(60,60,67,.16);--glass:rgba(242,242,247,.78);--fill:rgba(120,120,128,.12);--field:#fff;--shadow:0 1px 2px rgba(0,0,0,.04),0 8px 24px rgba(0,0,0,.06);--note:rgba(255,149,0,.12);--notebar:#C93400;--link:#2F5A86;--rbg:rgba(255,59,48,.14);--gbg:rgba(52,199,89,.16);--obg:rgba(255,149,0,.16);--rt:#C0261C;--gt:#1E7B3A;--ot:#A15C00;--ease:cubic-bezier(.2,.8,.2,1)}
:root[data-theme=light]{color-scheme:light}
:root[data-theme=dark]{color-scheme:dark;--bg:#000;--card:#1C1C1E;--ink:#F2F2F7;--grey:#AEAEB2;--blue:#5A84B3;--green:#30D158;--orange:#FF9F0A;--red:#FF453A;--onblue:#fff;--sep:rgba(235,235,245,.16);--glass:rgba(28,28,30,.72);--fill:rgba(120,120,128,.24);--field:#2C2C2E;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.5);--note:rgba(255,159,10,.16);--notebar:#FF9F0A;--link:#8FB0D6;--rbg:rgba(255,69,58,.2);--gbg:rgba(48,209,88,.2);--obg:rgba(255,159,10,.2);--rt:#FF6961;--gt:#4CD964;--ot:#FFB340}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#000;--card:#1C1C1E;--ink:#F2F2F7;--grey:#AEAEB2;--blue:#5A84B3;--green:#30D158;--orange:#FF9F0A;--red:#FF453A;--onblue:#fff;--sep:rgba(235,235,245,.16);--glass:rgba(28,28,30,.72);--fill:rgba(120,120,128,.24);--field:#2C2C2E;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.5);--note:rgba(255,159,10,.16);--notebar:#FF9F0A;--link:#8FB0D6;--rbg:rgba(255,69,58,.2);--gbg:rgba(48,209,88,.2);--obg:rgba(255,159,10,.2);--rt:#FF6961;--gt:#4CD964;--ot:#FFB340}}
*{box-sizing:border-box}
body{font:15px/1.47 -apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display",system-ui,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;color:var(--ink);margin:0;background:var(--bg)}
a{color:var(--link)}
header{position:sticky;top:0;z-index:20;background:var(--glass);-webkit-backdrop-filter:blur(20px) saturate(180%);backdrop-filter:blur(20px) saturate(180%);border-bottom:1px solid var(--sep);padding:16px 24px}
h1{margin:0 0 4px;font:700 34px/1.12 -apple-system,BlinkMacSystemFont,"SF Pro Display",system-ui,"Segoe UI",sans-serif;letter-spacing:-.02em}
header{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px}header>div:first-child{min-width:0;flex:1 1 400px}
header p{margin:0;color:var(--grey);font-size:13px}
.theme{display:inline-flex;gap:2px;padding:2px;background:var(--fill);border:1px solid var(--sep);border-radius:12px;font-weight:500}
.theme button{min-height:44px;padding:0 14px;border:0;border-radius:10px;background:transparent;color:var(--ink);font:inherit;font-weight:500;font-size:14px;cursor:pointer;filter:none;transform:none}
.theme button:hover{background:var(--sep);filter:none}
.theme button[aria-checked=true]{background:var(--ink);color:var(--bg);font-weight:600;box-shadow:var(--shadow)}
main{padding:24px;max-width:1600px;margin:auto}
.hinweis{background:var(--card);border-radius:18px;box-shadow:var(--shadow);border-left:6px solid var(--orange);padding:16px 24px;margin:0 0 24px}.hinweis ul{margin:8px 0 8px;padding-left:24px}.hinweis li{margin:4px 0}
code{font:13px ui-monospace,"SF Mono",Menlo,Consolas,monospace;background:var(--fill);padding:1px 6px;border-radius:6px}
.filter{display:flex;flex-wrap:wrap;gap:16px;align-items:end;background:var(--card);box-shadow:var(--shadow);padding:16px;border-radius:18px}
label{display:flex;flex-direction:column;font-size:13px;font-weight:500;color:var(--grey);gap:4px}label.cb{flex-direction:row;align-items:center;gap:8px;min-height:44px;font-size:15px;color:var(--ink);font-weight:400}
label.cb input{width:22px;height:22px;min-height:0;padding:0;accent-color:var(--blue)}
input,select,button{font:inherit;min-height:44px;padding:8px 12px;border:1px solid transparent;border-radius:12px;background:var(--fill);color:var(--ink);transition:background-color .2s var(--ease),box-shadow .2s var(--ease),transform .15s var(--ease)}
input:hover,select:hover{background:var(--sep)}
input:focus,select:focus{background:var(--field);border-color:var(--blue)}
button{cursor:pointer;background:var(--blue);color:var(--onblue);font-weight:600;padding:8px 20px}
button:hover{filter:brightness(1.08)}button:active{transform:scale(.97);filter:brightness(.92)}
button.sek{background:var(--fill);color:var(--blue)}button.sek:hover{background:var(--sep);filter:none}
:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
.zeile{margin:16px 0;display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}#anz{font-weight:600}
.tw{overflow:auto;max-height:72vh;background:var(--card);border-radius:18px;box-shadow:var(--shadow)}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:13.5px;min-width:1100px}th,td{border-bottom:1px solid var(--sep);padding:12px 16px;text-align:left;vertical-align:top}
tbody tr{transition:background-color .2s var(--ease)}tbody tr:hover{background:var(--fill)}tbody tr:last-child td{border-bottom:0}
th{background:var(--glass);-webkit-backdrop-filter:blur(20px) saturate(180%);backdrop-filter:blur(20px) saturate(180%);position:sticky;top:0;z-index:2;cursor:pointer;white-space:nowrap;font-size:12px;font-weight:600;color:var(--grey);min-height:44px;transition:background-color .2s var(--ease),color .2s var(--ease)}
th:hover{background:var(--fill);color:var(--ink)}th:active{background:var(--sep)}th small{font-weight:400;color:var(--grey)}
.st{display:inline-block;padding:2px 10px;border-radius:999px;font-size:12px;font-weight:600;background:var(--fill);color:var(--ink)}
.st.abgelaufen{background:var(--rbg);color:var(--rt)}.st.laeuft{background:var(--gbg);color:var(--gt)}.st.offen{background:var(--obg);color:var(--ot)}
.sf{font-weight:700;color:var(--blue)}.grau{color:var(--grey)}.so{display:block;margin-top:4px;font-size:12px;background:var(--note);border-left:3px solid var(--notebar);border-radius:6px;padding:4px 8px}
.num{text-align:right;white-space:nowrap}
details{margin-top:24px;background:var(--card);border-radius:18px;box-shadow:var(--shadow);padding:0 24px 8px}summary{cursor:pointer;min-height:44px;display:flex;align-items:center;font-weight:600}
footer{color:var(--grey);font-size:12.5px;margin:32px 0}footer p{margin:8px 0}
@media (max-width:700px){main{padding:16px}header{padding:12px 16px}h1{font-size:28px}.filter label{flex:1 1 140px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
</style></head><body>
<header><div><h1>Vertragsliste Gebäudereinigung · Oberpfalz</h1><p>Prototyp, Darstellung (Demo) · Stand der Daten: __STAND__ · __N__ Lose aus __NN__ Bekanntmachungen · Seite erzeugt am __ERZ__</p></div><div class="theme" role="radiogroup" aria-label="Darstellung"><button type="button" role="radio" aria-checked="true" data-t="auto">Automatisch</button><button type="button" role="radio" aria-checked="false" data-t="light">Hell</button><button type="button" role="radio" aria-checked="false" data-t="dark">Dunkel</button></div></header>
<main>
<div class="hinweis" role="note"><p style="margin:0 0 8px"><b>Das Ende der Grundlaufzeit ist kein Termin der Neuausschreibung.</b></p><p style="margin:0 0 8px"><b>Diese Seite stellt die Daten dar (Demo).</b> Für die Übernahme in ein Verwaltungssystem gibt es einen Datei-Export mit festem Schema (Version 1.1): <a href="export/vertragsliste_v1.csv">CSV (Komma)</a>, <a href="export/vertragsliste_v1_de.csv">CSV (Semikolon, für deutsches Excel)</a>, <a href="export/vertragsliste_v1.json">JSON</a>; Beschreibung der Felder: <code>docs/export_schema.md</code>. Die Schaltfläche „Auswahl als CSV“ liefert die gefilterte Auswahl mit denselben Spalten (Semikolon).</p><b>Was diese Liste ist und was nicht.</b> Sie zeigt je <b>Los</b>, wann die feste Laufzeit (Grundlaufzeit) laut Bekanntmachung endet, das <b>Höchstende</b> (mit Verlängerungen) getrennt davon, die Herkunft der Angabe (Stufe A bis F) und, soweit in TED veröffentlicht, Auftragnehmer, Zuschlagswert und Zahl der Angebote.
<ul>
<li><b>Voreinstellung der Ansicht:</b> angezeigt werden laufende und noch verlängerbare Verträge (Status „Grundlaufzeit läuft“, „Verlängerungszeit möglich“, „Verlängerung offen“); abgelaufene Lose (auch das Höchstende ist vorbei) sind ausgeblendet, Lose ohne bekanntes Ende stehen am Schluss. Der Schalter „auch abgelaufene“ zeigt alle Lose. Lose, deren Grundlaufzeit vorbei ist, bleiben sichtbar, weil dort eine Verlängerung möglich ist; in der Optionsanalyse kam bei belegter Option die Neuausschreibung in 17 von 24 Fällen (70,8 %) zwischen Ende der Grundlaufzeit und Höchstende (kleine Stichprobe, nur Hinweis).</li>
<li><b>Keine Terminprognose:</b> Wann neu ausgeschrieben wird, sagt die Liste nicht (Backtest: Treffer ±3 Monate nur 28,8 %).</li>
<li><b>Höchstende nur Hinweis</b> (oft zu hoch, nicht geprüft).</li>
<li><b>Nur Lose aus TED oberhalb der EU-Schwelle;</b> Verfahren, die nicht auf TED stehen, fehlen (rund ein Viertel der Oberpfälzer Reinigungsverfahren im Bekanntmachungsservice laut Hinweis, nicht als Schwelle gemessen).</li>
<li><b>Die Liste hat Fehler.</b> Beispiel: Das Dauerfeld enthält die Option schon (12 von 9.325 Losen der Gesamtliste bekannt). Das Ende der Grundlaufzeit stimmte zu 94,3 % mit zwei KI-Lesern überein (Stichprobe aus ganz Deutschland, n = 70). Das ist eine Übereinstimmung, keine Fehlerquote, und sie wurde nicht für die Oberpfalz gemessen; „die Liste ist korrekt“ ist damit nicht belegt.</li>
<li><b>Wettbewerbsbild unvollständig:</b> Auftragnehmer in 99 % der Lose, Zuschlagswert über 1 € in 48 %, Gesamtzahl der Angebote in 61 %, alle drei zusammen in 25 % (130 Lose). Platzhalterwerte (höchstens 1 €) werden nicht als Wert gezeigt.</li>
<li><b>Vergleich:</b> <a href="https://vergabeweiser.de" target="_blank" rel="noopener">Vergabeweiser</a> ist eine kostenlose Alternative mit Ende je Verfahren, nach eigener Angabe auch unterhalb der EU-Schwelle (wir haben das nicht gemessen). Auf zwei Stichproben (n = 70 und n = 160) weicht dessen Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt, auf Los- und Definitionsebene; das sind überwiegend Unterschiede der Definition (Höchstende) und der Ebene (Verfahren statt Los). Kein Beleg für bessere Lesequalität.</li>
</ul>
<b>Vor einer Entscheidung immer die verlinkte Bekanntmachung lesen.</b></div>
<div class="filter" role="search">
<label>Suche (Auftraggeber, Titel, Nr.)<input id="q" type="search" size="24"></label>
<label>Auftragnehmer<input id="aufn" type="search" size="20" placeholder="Name enthält …"></label>
<label>Region<select id="reg"><option value="">alle</option></select></label>
<label>Status<select id="stat"><option value="">alle</option></select></label>
<label>Stufe<select id="stufe"><option value="">alle</option></select></label>
<label>Ende Grundlaufzeit ab<input id="von" type="date"></label>
<label>bis<input id="bis" type="date"></label>
<label class="cb"><input id="altE" type="checkbox"> auch abgelaufene (alle Lose)</label>
<label class="cb"><input id="nurEnde" type="checkbox"> nur mit bekanntem Ende</label>
<label class="cb"><input id="nurWb" type="checkbox"> nur mit Auftragnehmer</label>
<button class="sek" id="reset">Zurücksetzen</button>
</div>
<div class="zeile"><span id="anz" aria-live="polite"></span><span id="vor" class="grau"></span><button id="csv">Auswahl als CSV</button></div>
<div class="tw"><table><caption class="grau" style="text-align:left;caption-side:bottom;padding:8px 16px">Voreinstellung: laufende und noch verlängerbare Verträge, nach Ende der Grundlaufzeit aufsteigend. „auch abgelaufene“ zeigt alle Lose. Spaltenkopf anklicken (oder Eingabetaste) sortiert.</caption><thead><tr id="kopf"></tr></thead><tbody id="tb"></tbody></table></div>
<details><summary>Stufen A bis F: woher stammt die Angabe?</summary><p class="grau">Die Stufe nennt die Herkunft der Angabe, nicht ihre Verlässlichkeit. Stufe A ist nicht „am sichersten“.</p><ul id="legende"></ul></details>
<footer>
<p><b>Quelle:</b> TED (Tenders Electronic Daily), Zuschlagsbekanntmachungen, Haupt-CPV 90910/90911/90919, Leistungsort Oberpfalz (NUTS DE23); Auftragnehmer, Zuschlagswert und Angebote aus dem eForms-XML derselben Bekanntmachungen (nur ab eForms, soweit der Auftraggeber sie veröffentlicht hat). Stand der Daten: __STAND__. Seite erzeugt am __ERZ__ mit src/report/webseite.py; Daten: reports/beispiel_liste_oberpfalz.csv, reports/wettbewerbsbild_oberpfalz.csv.</p>
<p>Hintergrund: Lab-Log (docs/lab_log.pdf).</p>
<p><b>Lizenz:</b> TED-Daten sind öffentliche Bekanntmachungen der EU; bei Weitergabe ist TED als Quelle anzugeben. Laut TED-Rechtsseite frei wiederverwendbar, auch kommerziell (Beschluss 2011/833/EU; identifizierbare Privatpersonen ausgenommen); Wortlaut am 06.11.2026 gelesen (docs/quellen.md).</p>
<p><b>Lesehilfe:</b> „*“ = Leistungsort auch außerhalb der Oberpfalz; Lose mit mehreren Regionen erscheinen mit allen. „≥ n“ bei Angeboten = nur die elektronisch eingegangenen Angebote sind veröffentlicht, die Gesamtzahl ist mindestens n. „nicht veröffentlicht“ = Auftraggeber hat den Wert ausdrücklich nicht veröffentlicht; „in TED nicht angegeben“ = Angabe fehlt in der Bekanntmachung (nicht: Wert unbekannt oder null). Prototyp ohne Kundentest.</p>
</footer>
</main>
<script>
const D=__DATA__, STUFEN=__STUFEN__, SCHEMA=__SCHEMA__;
const SPALTEN=[["e","Ende Grundlaufzeit<br><small>je Los</small>"],["h","Höchstende<br><small>nur Hinweis</small>"],["a","Auftraggeber"],["t","Los"],["rs","Region"],["w","Auftragnehmer"],["wv","Zuschlagswert"],["ang","Angebote"],["st","Status"],["s","Stufe"],["n","Bekanntmachung"]];
D.forEach(d=>{d.rs=d.r.join(", ")+(d.x?" *":"")});
const $=id=>document.getElementById(id);
const HEUTE=new Date().toISOString().slice(0,10);
let sort=["e",1];
const uniq=k=>[...new Set(D.flatMap(d=>k==="r"?d.r:[d[k]]))].sort();
for(const [id,k] of [["reg","r"],["stat","st"],["stufe","s"]])uniq(k).forEach(v=>$(id).add(new Option(v,v)));
$("kopf").innerHTML=SPALTEN.map(([k,n])=>`<th scope="col" tabindex="0" data-k="${k}">${n}</th>`).join("");
$("legende").innerHTML=Object.entries(STUFEN).map(([k,v])=>`<li><b>${k}</b>: ${v}</li>`).join("");
const fmt=s=>s?s.split("-").reverse().join("."):"";
const eur=v=>v.toLocaleString("de-DE",{maximumFractionDigits:0})+" €";
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
// abgelaufen = Status „abgelaufen“, oder Grundlaufzeit vorbei und kein Höchstende in der Zukunft; Status „Verlängerungszeit möglich/offen“ bleibt sichtbar
const vergangen=(d,heute)=>d.st.startsWith("abgel")||(!!d.e&&d.e<heute&&!(d.h&&d.h>=heute)&&!d.st.includes("offen")&&!d.st.includes("möglich"));
function filtere(D,o){const q=(o.q||"").toLowerCase(),an=(o.aufn||"").toLowerCase();
 return D.filter(d=>(!q||(d.a+" "+d.t+" "+d.n).toLowerCase().includes(q))&&(!an||(d.w||"").toLowerCase().includes(an))&&(!o.reg||d.r.includes(o.reg))&&(!o.st||d.st===o.st)&&(!o.sf||d.s===o.sf)
  &&(!o.ne||d.e)&&(!o.nw||d.w)&&(o.alt||!vergangen(d,o.heute))&&(!o.von||(d.e&&d.e>=o.von))&&(!o.bis||(d.e&&d.e<=o.bis)))}
function sortiere(r,k,rich){return r.slice().sort((x,y)=>{const a=x[k]??"",b=y[k]??"";if(a===""&&b!=="")return 1;if(a!==""&&b==="")return -1;return (a<b?-1:a>b?1:0)*rich})}
function auswahl(){return sortiere(filtere(D,{q:$("q").value,aufn:$("aufn").value,reg:$("reg").value,st:$("stat").value,sf:$("stufe").value,von:$("von").value,bis:$("bis").value,
 ne:$("nurEnde").checked,nw:$("nurWb").checked,alt:$("altE").checked,heute:HEUTE}),sort[0],sort[1])}
const wertTxt=d=>d.wv!=null?eur(d.wv):(d.wz?'<span class="grau">nicht veröffentlicht</span>':'<span class="grau">in TED nicht angegeben</span>');
const angTxt=d=>d.ang!=null?(d.am?"≥ ":"")+d.ang:'<span class="grau">in TED nicht angegeben</span>';
function zeige(){const r=auswahl();$("anz").textContent=r.length+" von "+D.length+" Losen";$("vor").textContent=$("altE").checked?"Angezeigt: alle Lose, auch abgelaufene":"Angezeigt: laufende und noch verlängerbare Verträge; abgelaufene ausgeblendet";
 $("tb").innerHTML=r.map(d=>{const c=d.st.startsWith("abgel")?"abgelaufen":d.st.includes("offen")||d.st.includes("möglich")?"offen":d.st.startsWith("Grundlaufzeit")?"laeuft":"";
 const so=d.so?`<span class="so">${esc(d.so)}</span>`:"";
 return `<tr><td>${d.e?fmt(d.e)+(d.ge?' <span class="grau">(geschätzt)</span>':""):'<span class="grau">in TED nicht angegeben</span>'}${so}</td><td class="grau">${d.h?fmt(d.h):"–"}</td><td>${esc(d.a)}</td><td>${esc(d.t)}</td><td>${esc(d.rs)}</td><td>${d.w?esc(d.w):'<span class="grau">'+(d.mg?"mehrere Auftragnehmer":"in TED nicht angegeben")+"</span>"}</td><td class="num">${wertTxt(d)}</td><td class="num">${angTxt(d)}</td><td><span class="st ${c}">${esc(d.st)}</span></td><td class="sf" title="${esc(STUFEN[d.s]||"")}">${d.s}</td><td><a href="${esc(d.u)}" target="_blank" rel="noopener">${esc(d.n)}</a></td></tr>`}).join("")}
function csv(){// Spalten und Werte wie docs/export_schema.md (Version 1.1), Semikolon wie vertragsliste_v1_de.csv, mit BOM
 const q=v=>{const s=String(v??"");return /[;"\r\n]/.test(s)?'"'+s.replace(/"/g,'""')+'"':s};const t=[SCHEMA.map(q).join(";"),...auswahl().map(d=>d.ex.map(q).join(";"))].join("\r\n")+"\r\n";
 const a=document.createElement("a");a.href=URL.createObjectURL(new Blob(["﻿"+t],{type:"text/csv;charset=utf-8"}));a.download="vertragsliste_auswahl.csv";a.click()}
document.querySelectorAll(".filter input,.filter select").forEach(e=>e.addEventListener("input",zeige));
$("reset").onclick=()=>{document.querySelectorAll(".filter input,.filter select").forEach(e=>e.type==="checkbox"?e.checked=false:e.value="");sort=["e",1];zeige()};
$("csv").onclick=csv;
const kopfKlick=e=>{const th=e.target.closest("th");const k=th&&th.dataset.k;if(!k)return;sort=[k,sort[0]===k?-sort[1]:1];zeige()};
$("kopf").onclick=kopfKlick;$("kopf").onkeydown=e=>{if(e.key==="Enter")kopfKlick(e)};
zeige();
</script><script>(function(){var r=document.documentElement,bs=document.querySelectorAll(".theme button");function m(){var t=r.getAttribute("data-theme")||"auto";bs.forEach(function(b){b.setAttribute("aria-checked",b.dataset.t===t?"true":"false")})}bs.forEach(function(b){b.addEventListener("click",function(){var t=b.dataset.t;if(t==="auto")r.removeAttribute("data-theme");else r.setAttribute("data-theme",t);try{if(t==="auto")localStorage.removeItem("vr-theme");else localStorage.setItem("vr-theme",t)}catch(e){}m()})});m()})()</script>__TEST__</body></html>"""


def main(test: str = "", out: Path = OUT) -> None:
    from export_vertragsliste import NAMEN
    d = lade()
    stand = re.search(r"Stand (\d{2}\.\d{2}\.\d{4})", (ROOT / "reports" / "beispiel_liste.md").read_text(encoding="utf-8")).group(1)
    html = (SEITE.replace("__DATA__", json.dumps(d, ensure_ascii=False)).replace("__STUFEN__", json.dumps(STUFEN, ensure_ascii=False)).replace("__SCHEMA__", json.dumps(NAMEN))
            .replace("__STAND__", stand).replace("__N__", str(len(d))).replace("__NN__", str(len({x["n"] for x in d})))
            .replace("__ERZ__", date.today().strftime("%d.%m.%Y")).replace("__TEST__", test))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(len(d), "Lose;", out)


if __name__ == "__main__":
    main()
