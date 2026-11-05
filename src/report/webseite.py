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
from datetime import date
from pathlib import Path

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
SONDER = {"527230-2026": "Interimsvergabe: Dauerfeld enthält die Option; Grundlaufzeit vermutlich bis 31.01.2027"}


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
    out = []
    for r in rows:
        codes = r["nuts"].split()
        w = wb.get((r["notice"], int(r["los"])), {})
        out.append({"n": r["notice"], "u": r["ted_link"], "v": r["veroeffentlicht"], "a": r["auftraggeber"], "l": r["los"], "t": r["los_titel"],
                    "r": [NUTS.get(c, c) for c in codes], "b": r["beginn"], "e": r["gl_ende"] or r["gl_geschaetzt"], "g": r["gl_herkunft"], "h": r["hoechstende"],
                    "hh": r["hoechstende_herkunft"], "s": r["stufe"], "st": r["status"], "ge": not r["gl_ende"] and bool(r["gl_geschaetzt"]),
                    "x": r["auch_ausserhalb"] == "True", "w": w.get("w"), "wv": w.get("wv"), "wz": w.get("wz", False),
                    "ang": w.get("ang"), "am": w.get("am", False), "wb": bool(w), "mg": w.get("mg", False), "so": SONDER.get(r["notice"], "")})
    return out


SEITE = r"""<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vertragsliste Gebäudereinigung Oberpfalz (Prototyp)</title>
<style>
:root{--dark:#0b3c49;--teal:#14607e;--pale:#eaf3f5;--ink:#1b2a33;--grey:#4f5d68;--amber:#f2a541}
*{box-sizing:border-box}body{font:15px/1.45 Calibri,Segoe UI,Arial,sans-serif;color:var(--ink);margin:0;background:#fff}
header{background:var(--dark);color:#fff;padding:18px 24px}h1{margin:0 0 4px;font:700 24px Cambria,Georgia,serif}header p{margin:0;color:#c5dde3}
main{padding:16px 24px;max-width:1600px;margin:auto}
.hinweis{background:#fff6e5;border-left:4px solid #b36b00;padding:10px 14px;margin:0 0 14px}.hinweis ul{margin:6px 0 4px;padding-left:20px}
.filter{display:flex;flex-wrap:wrap;gap:10px;align-items:end;background:var(--pale);padding:12px;border-radius:6px}
label{display:flex;flex-direction:column;font-size:13px;color:var(--grey);gap:2px}label.cb{flex-direction:row;align-items:center;gap:5px}
input,select,button{font:inherit;padding:5px 7px;border:1px solid #7f93a0;border-radius:4px;background:#fff;color:var(--ink)}
button{cursor:pointer;background:var(--teal);color:#fff;border-color:var(--teal)}button.sek{background:#fff;color:var(--teal)}
:focus-visible{outline:3px solid #1a73e8;outline-offset:1px}
.zeile{margin:10px 0;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:13.5px;min-width:1100px}th,td{border-bottom:1px solid #dfe8ea;padding:6px 8px;text-align:left;vertical-align:top}
th{background:var(--pale);position:sticky;top:0;cursor:pointer;white-space:nowrap}th:hover{background:#d9eaee}th small{font-weight:400;color:var(--grey)}
.st{display:inline-block;padding:1px 7px;border-radius:10px;font-size:12px;background:#e3edf0}.st.abgelaufen{background:#f3d9d2}.st.laeuft{background:#dcefe3}.st.offen{background:#fbe9c6}
.sf{font-weight:700;color:var(--teal)}.grau{color:var(--grey)}.so{display:block;margin-top:3px;font-size:12px;background:#fff6e5;border-left:3px solid #b36b00;padding:2px 6px}
.num{text-align:right;white-space:nowrap}details{margin-top:18px}footer{color:var(--grey);font-size:12.5px;margin:24px 0}footer p{margin:6px 0}
@media (max-width:700px){main{padding:12px}header{padding:14px 12px}h1{font-size:20px}.filter label{flex:1 1 140px}}
</style></head><body>
<header><h1>Vertragsliste Gebäudereinigung · Oberpfalz</h1><p>Prototyp · Stand der Daten: __STAND__ · __N__ Lose aus __NN__ Bekanntmachungen · Seite erzeugt am __ERZ__</p></header>
<main>
<div class="hinweis" role="note"><p style="margin:0 0 8px"><b>Das Ende der Grundlaufzeit ist kein Termin der Neuausschreibung.</b></p><b>Was diese Liste ist und was nicht.</b> Sie zeigt je <b>Los</b>, wann die feste Laufzeit (Grundlaufzeit) laut Bekanntmachung endet, das <b>Höchstende</b> (mit Verlängerungen) getrennt davon, die Herkunft der Angabe (Stufe A bis F) und, soweit in TED veröffentlicht, Auftragnehmer, Zuschlagswert und Zahl der Angebote.
<ul>
<li><b>Voreinstellung der Ansicht:</b> angezeigt werden laufende und noch verlängerbare Verträge (Status „Grundlaufzeit läuft“, „Verlängerungszeit möglich“, „Verlängerung offen“); abgelaufene Lose (auch das Höchstende ist vorbei) sind ausgeblendet, Lose ohne bekanntes Ende stehen am Schluss. Der Schalter „auch abgelaufene“ zeigt alle Lose. Lose, deren Grundlaufzeit vorbei ist, bleiben sichtbar, weil dort eine Verlängerung möglich ist; in der Optionsanalyse kam bei belegter Option die Neuausschreibung in 17 von 24 Fällen (70,8 %) zwischen Ende der Grundlaufzeit und Höchstende (kleine Stichprobe, nur Hinweis).</li>
<li><b>Keine Terminprognose:</b> Wann neu ausgeschrieben wird, sagt die Liste nicht (Backtest: Treffer ±3 Monate nur 28,8 %).</li>
<li><b>Höchstende nur Hinweis</b> (oft zu hoch, nicht geprüft).</li>
<li><b>Nur Lose aus TED oberhalb der EU-Schwelle;</b> Aufträge unterhalb der Schwelle fehlen.</li>
<li><b>Die Liste hat Fehler.</b> Beispiel: Das Dauerfeld enthält die Option schon (12 von 9.325 Losen der Gesamtliste bekannt). Das Ende der Grundlaufzeit stimmte zu 94,3 % mit zwei KI-Lesern überein (Stichprobe aus ganz Deutschland, n = 70). Das ist eine Übereinstimmung, keine Fehlerquote, und sie wurde nicht für die Oberpfalz gemessen; „die Liste ist korrekt“ ist damit nicht belegt.</li>
<li><b>Wettbewerbsbild unvollständig:</b> Auftragnehmer in 99 % der Lose, Zuschlagswert über 1 € in 48 %, Gesamtzahl der Angebote in 61 %, alle drei zusammen in 25 % (130 Lose). Platzhalterwerte (höchstens 1 €) werden nicht als Wert gezeigt.</li>
<li><b>Vergleich:</b> <a href="https://vergabeweiser.de" target="_blank" rel="noopener">Vergabeweiser</a> ist eine kostenlose Alternative mit Ende je Verfahren und mehr Abdeckung (auch unterhalb der EU-Schwelle). Auf zwei Stichproben (n = 70 und n = 160) weicht dessen Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt, auf Los- und Definitionsebene; das sind überwiegend Unterschiede der Definition (Höchstende) und der Ebene (Verfahren statt Los). Kein Beleg für bessere Lesequalität.</li>
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
<div class="tw"><table><caption class="grau" style="text-align:left;caption-side:bottom;padding-top:6px">Voreinstellung: laufende und noch verlängerbare Verträge, nach Ende der Grundlaufzeit aufsteigend. „auch abgelaufene“ zeigt alle Lose. Spaltenkopf anklicken (oder Eingabetaste) sortiert.</caption><thead><tr id="kopf"></tr></thead><tbody id="tb"></tbody></table></div>
<details><summary>Stufen A bis F: woher stammt die Angabe?</summary><p class="grau">Die Stufe nennt die Herkunft der Angabe, nicht ihre Verlässlichkeit. Stufe A ist nicht „am sichersten“.</p><ul id="legende"></ul></details>
<footer>
<p><b>Quelle:</b> TED (Tenders Electronic Daily), Zuschlagsbekanntmachungen, Haupt-CPV 90910/90911/90919, Leistungsort Oberpfalz (NUTS DE23); Auftragnehmer, Zuschlagswert und Angebote aus dem eForms-XML derselben Bekanntmachungen (nur ab eForms, soweit der Auftraggeber sie veröffentlicht hat). Stand der Daten: __STAND__. Seite erzeugt am __ERZ__ mit src/report/webseite.py; Daten: reports/beispiel_liste_oberpfalz.csv, reports/wettbewerbsbild_oberpfalz.csv.</p>
<p>Hintergrund: Lab-Log (docs/lab_log.pdf).</p>
<p><b>Lizenz:</b> TED-Daten sind öffentliche Bekanntmachungen der EU; bei Weitergabe ist TED als Quelle anzugeben. Die genauen Nutzungsbedingungen sind vor Abgabe zu prüfen (noch nicht geprüft).</p>
<p><b>Lesehilfe:</b> „*“ = Leistungsort auch außerhalb der Oberpfalz; Lose mit mehreren Regionen erscheinen mit allen. „≥ n“ bei Angeboten = nur die elektronisch eingegangenen Angebote sind veröffentlicht, die Gesamtzahl ist mindestens n. „nicht veröffentlicht“ = Auftraggeber hat den Wert ausdrücklich nicht veröffentlicht; „in TED nicht angegeben“ = Angabe fehlt in der Bekanntmachung (nicht: Wert unbekannt oder null). Prototyp ohne Kundentest.</p>
</footer>
</main>
<script>
const D=__DATA__, STUFEN=__STUFEN__;
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
function csv(){const k=["n","u","a","t","rs","e","h","hh","g","s","st","w","wv","ang","am"],h=["Bekanntmachung","TED-Link","Auftraggeber","Los","Region","Ende Grundlaufzeit","Höchstende (Hinweis)","Herkunft Höchstende","Herkunft Ende","Stufe","Status","Auftragnehmer","Zuschlagswert EUR (nur > 1 EUR)","Angebote","Angebote nur Untergrenze (elektronisch)"];
 const q=v=>'"'+String(v??"").replace(/"/g,'""')+'"';const t=[h.map(q).join(";"),...auswahl().map(d=>k.map(x=>q(d[x])).join(";"))].join("\r\n");
 const a=document.createElement("a");a.href=URL.createObjectURL(new Blob(["﻿"+t],{type:"text/csv;charset=utf-8"}));a.download="vertragsliste_auswahl.csv";a.click()}
document.querySelectorAll(".filter input,.filter select").forEach(e=>e.addEventListener("input",zeige));
$("reset").onclick=()=>{document.querySelectorAll(".filter input,.filter select").forEach(e=>e.type==="checkbox"?e.checked=false:e.value="");sort=["e",1];zeige()};
$("csv").onclick=csv;
const kopfKlick=e=>{const th=e.target.closest("th");const k=th&&th.dataset.k;if(!k)return;sort=[k,sort[0]===k?-sort[1]:1];zeige()};
$("kopf").onclick=kopfKlick;$("kopf").onkeydown=e=>{if(e.key==="Enter")kopfKlick(e)};
zeige();
</script>__TEST__</body></html>"""


def main(test: str = "", out: Path = OUT) -> None:
    d = lade()
    stand = re.search(r"Stand (\d{2}\.\d{2}\.\d{4})", (ROOT / "reports" / "beispiel_liste.md").read_text(encoding="utf-8")).group(1)
    html = (SEITE.replace("__DATA__", json.dumps(d, ensure_ascii=False)).replace("__STUFEN__", json.dumps(STUFEN, ensure_ascii=False))
            .replace("__STAND__", stand).replace("__N__", str(len(d))).replace("__NN__", str(len({x["n"] for x in d})))
            .replace("__ERZ__", date.today().strftime("%d.%m.%Y")).replace("__TEST__", test))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(len(d), "Lose;", out)


if __name__ == "__main__":
    main()
