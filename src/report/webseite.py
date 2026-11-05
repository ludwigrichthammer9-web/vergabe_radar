"""Phase 6: Prototyp-Webseite der Vertragsliste (eine statische HTML-Datei mit Filtern, ohne Server).

Eingabe:  reports/beispiel_liste_oberpfalz.csv (aus src/report/beispiel_liste.py, Fassung der Iteration 9)
Aufruf:   .venv\\Scripts\\python -I src/report/webseite.py      Ausgabe: docs/prototyp/vertragsliste.html
Keine Terminprognose (Iteration 5): gefiltert wird nach dem Ende der Grundlaufzeit laut Bekanntmachung; das Höchstende ist nur Hinweis.
"""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CSV = ROOT / "reports" / "beispiel_liste_oberpfalz.csv"
OUT = ROOT / "docs" / "prototyp" / "vertragsliste.html"
# NUTS-3-Namen der Oberpfalz (NUTS 2021) – aus dem Gedächtnis eingetragen, vor Abgabe gegen Eurostat prüfen
NUTS = {"DE231": "Amberg (Stadt)", "DE232": "Regensburg (Stadt)", "DE233": "Weiden i. d. OPf. (Stadt)", "DE234": "Amberg-Sulzbach",
        "DE235": "Cham", "DE236": "Neumarkt i. d. OPf.", "DE237": "Neustadt a. d. Waldnaab", "DE238": "Regensburg (Landkreis)",
        "DE239": "Schwandorf", "DE23A": "Tirschenreuth"}
STUFEN = {"A": "Höchstende steht ausdrücklich in Text oder Feld, oder das Ende wurde aus dem Text berichtigt",
          "B": "Höchstende berechnet (Anzahl × Länge der Verlängerungen); das Enddatum kann schon das Höchstende sein",
          "C": "keine Angabe zur Verlängerung; Höchstende = Grundlaufzeit angenommen",
          "D": "Verlängerung erwähnt, Länge oder Anzahl fehlt; Höchstende unbestimmbar",
          "E": "Ende nur geschätzt (Veröffentlichung + Dauer, ungeprüft)", "F": "kein Ende bekannt"}


def lade() -> list[dict]:
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    out = []
    for r in rows:
        codes = r["nuts"].split()
        out.append({"n": r["notice"], "u": r["ted_link"], "v": r["veroeffentlicht"], "a": r["auftraggeber"], "l": r["los"], "t": r["los_titel"],
                    "r": [NUTS.get(c, c) for c in codes], "b": r["beginn"], "e": r["gl_ende"] or r["gl_geschaetzt"], "g": r["gl_herkunft"], "h": r["hoechstende"],
                    "hh": r["hoechstende_herkunft"], "s": r["stufe"], "st": r["status"], "ge": not r["gl_ende"] and bool(r["gl_geschaetzt"]),
                    "x": r["auch_ausserhalb"] == "True"})
    return out


SEITE = r"""<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vertragsliste Gebäudereinigung Oberpfalz (Prototyp)</title>
<style>
:root{--dark:#0b3c49;--teal:#1c7293;--pale:#eaf3f5;--ink:#1b2a33;--grey:#6c7a89;--amber:#f2a541}
*{box-sizing:border-box}body{font:15px/1.45 Calibri,Segoe UI,Arial,sans-serif;color:var(--ink);margin:0;background:#fff}
header{background:var(--dark);color:#fff;padding:18px 24px}h1{margin:0 0 4px;font:700 24px Cambria,Georgia,serif}header p{margin:0;color:#8fb8c4}
main{padding:16px 24px;max-width:1500px;margin:auto}
.hinweis{background:#fff6e5;border-left:4px solid var(--amber);padding:10px 14px;margin:0 0 14px}
.filter{display:flex;flex-wrap:wrap;gap:10px;align-items:end;background:var(--pale);padding:12px;border-radius:6px}
label{display:flex;flex-direction:column;font-size:12px;color:var(--grey);gap:2px}
input,select,button{font:inherit;padding:5px 7px;border:1px solid #b8c7cc;border-radius:4px;background:#fff}button{cursor:pointer;background:var(--teal);color:#fff;border-color:var(--teal)}button.sek{background:#fff;color:var(--teal)}
.zeile{margin:10px 0;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
table{border-collapse:collapse;width:100%;font-size:13.5px}th,td{border-bottom:1px solid #dfe8ea;padding:6px 8px;text-align:left;vertical-align:top}
th{background:var(--pale);position:sticky;top:0;cursor:pointer;white-space:nowrap}th:hover{background:#d9eaee}
.st{display:inline-block;padding:1px 7px;border-radius:10px;font-size:12px;background:#e3edf0}.st.abgelaufen{background:#f3d9d2}.st.laeuft{background:#dcefe3}.st.offen{background:#fbe9c6}
.sf{font-weight:700;color:var(--teal)}.grau{color:var(--grey)}details{margin-top:18px}footer{color:var(--grey);font-size:12px;margin:24px 0}
</style></head><body>
<header><h1>Vertragsliste Gebäudereinigung · Oberpfalz</h1><p>Prototyp · Stand der Daten: __STAND__ · __N__ Lose aus __NN__ Bekanntmachungen</p></header>
<main>
<p class="hinweis"><b>Keine Prognose.</b> Die Liste zeigt, wann die feste Laufzeit laut Bekanntmachung endet. Wann neu ausgeschrieben wird, sagt sie nicht (Backtest: Treffer ±3 Monate nur 28,8 %).
Das Höchstende ist nur ein Hinweis (oft zu hoch). Das Ende der Grundlaufzeit stimmte auf einer Stichprobe aus ganz Deutschland zu 94,3 % mit dem Vergleichswert zweier KI-Leser überein; „die Liste ist korrekt“ ist damit nicht belegt. <b>Vor einer Entscheidung immer die verlinkte Bekanntmachung lesen.</b></p>
<div class="filter">
<label>Suche (Auftraggeber, Titel, Nr.)<input id="q" type="search" size="26"></label>
<label>Region<select id="reg"><option value="">alle</option></select></label>
<label>Status<select id="stat"><option value="">alle</option></select></label>
<label>Stufe<select id="stufe"><option value="">alle</option></select></label>
<label>Ende Grundlaufzeit ab<input id="von" type="date"></label>
<label>bis<input id="bis" type="date"></label>
<label style="flex-direction:row;align-items:center;gap:5px"><input id="nurEnde" type="checkbox"> nur mit bekanntem Ende</label>
<button class="sek" id="reset">Zurücksetzen</button>
</div>
<div class="zeile"><span id="anz"></span><button id="csv">Auswahl als CSV</button></div>
<table><thead><tr id="kopf"></tr></thead><tbody id="tb"></tbody></table>
<details><summary>Stufen A bis F: woher stammt die Angabe?</summary><ul id="legende"></ul></details>
<footer>Quelle: TED (Tenders Electronic Daily), Zuschlagsbekanntmachungen, Haupt-CPV 90910/90911/90919, Leistungsort Oberpfalz (NUTS DE23). Erzeugt mit src/report/webseite.py; Daten: reports/beispiel_liste_oberpfalz.csv.
Lose mit mehreren Regionen erscheinen mit allen; „*“ = Leistungsort auch außerhalb der Oberpfalz. Prototyp ohne Kundentest.</footer>
</main>
<script>
const D=__DATA__, STUFEN=__STUFEN__;
const SPALTEN=[["e","Ende Grundlaufzeit"],["h","Höchstende (Hinweis)"],["a","Auftraggeber"],["t","Los"],["rs","Region"],["st","Status"],["s","Stufe"],["n","Bekanntmachung"]];
D.forEach(d=>{d.rs=d.r.join(", ")+(d.x?" *":"")});
let sort=["e",1];const $=id=>document.getElementById(id);
const uniq=k=>[...new Set(D.flatMap(d=>k==="r"?d.r:[d[k]]))].sort();
for(const [id,k] of [["reg","r"],["stat","st"],["stufe","s"]])uniq(k).forEach(v=>$(id).add(new Option(v,v)));
$("kopf").innerHTML=SPALTEN.map(([k,n])=>`<th data-k="${k}">${n}</th>`).join("");
$("legende").innerHTML=Object.entries(STUFEN).map(([k,v])=>`<li><b>${k}</b>: ${v}</li>`).join("");
const fmt=s=>s?s.split("-").reverse().join("."):"";
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function auswahl(){const q=$("q").value.toLowerCase(),reg=$("reg").value,st=$("stat").value,sf=$("stufe").value,von=$("von").value,bis=$("bis").value,ne=$("nurEnde").checked;
 let r=D.filter(d=>(!q||(d.a+" "+d.t+" "+d.n).toLowerCase().includes(q))&&(!reg||d.r.includes(reg))&&(!st||d.st===st)&&(!sf||d.s===sf)&&(!ne||d.e)&&(!von||(d.e&&d.e>=von))&&(!bis||(d.e&&d.e<=bis)));
 const [k,rich]=sort;r.sort((x,y)=>{const a=x[k]||"",b=y[k]||"";if(!a&&b)return 1;if(a&&!b)return -1;return (a<b?-1:a>b?1:0)*rich});return r}
function zeige(){const r=auswahl();$("anz").textContent=r.length+" von "+D.length+" Losen";
 $("tb").innerHTML=r.map(d=>{const c=d.st.startsWith("abgel")?"abgelaufen":d.st.includes("offen")||d.st.includes("möglich")?"offen":d.st.startsWith("Grundlaufzeit")?"laeuft":"";
 return `<tr><td>${d.e?fmt(d.e)+(d.ge?' <span class="grau" title="geschätzt">(geschätzt)</span>':""):'<span class="grau">unbekannt</span>'}</td><td class="grau">${d.h?fmt(d.h):"–"}</td><td>${esc(d.a)}</td><td>${esc(d.t)}</td><td>${esc(d.rs)}</td><td><span class="st ${c}">${esc(d.st)}</span></td><td class="sf" title="${esc(STUFEN[d.s]||"")}">${d.s}</td><td><a href="${esc(d.u)}" target="_blank" rel="noopener">${esc(d.n)}</a></td></tr>`}).join("")}
function csv(){const k=["n","u","a","t","rs","e","h","hh","g","s","st"],h=["Bekanntmachung","TED-Link","Auftraggeber","Los","Region","Ende Grundlaufzeit","Höchstende (Hinweis)","Herkunft Höchstende","Herkunft Ende","Stufe","Status"];
 const q=v=>'"'+String(v??"").replace(/"/g,'""')+'"';const t=[h.map(q).join(";"),...auswahl().map(d=>k.map(x=>q(d[x])).join(";"))].join("\r\n");
 const a=document.createElement("a");a.href=URL.createObjectURL(new Blob(["﻿"+t],{type:"text/csv;charset=utf-8"}));a.download="vertragsliste_auswahl.csv";a.click()}
document.querySelectorAll(".filter input,.filter select").forEach(e=>e.addEventListener("input",zeige));
$("reset").onclick=()=>{document.querySelectorAll(".filter input,.filter select").forEach(e=>e.type==="checkbox"?e.checked=false:e.value="");zeige()};
$("csv").onclick=csv;
$("kopf").onclick=e=>{const k=e.target.dataset.k;if(!k)return;sort=[k,sort[0]===k?-sort[1]:1];zeige()};
zeige();
</script></body></html>"""


def main() -> None:
    d = lade()
    stand = re.search(r"Stand (\d{2}\.\d{2}\.\d{4})", (ROOT / "reports" / "beispiel_liste.md").read_text(encoding="utf-8")).group(1)
    html = (SEITE.replace("__DATA__", json.dumps(d, ensure_ascii=False)).replace("__STUFEN__", json.dumps(STUFEN, ensure_ascii=False))
            .replace("__STAND__", stand).replace("__N__", str(len(d))).replace("__NN__", str(len({x["n"] for x in d}))))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(len(d), "Lose;", OUT)


if __name__ == "__main__":
    main()
