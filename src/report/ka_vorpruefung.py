"""Test K-A, Schritt 1 (Vorprüfung des Nenners): Für wie viele der 52 Backtest-Paare (data/processed/x1_paare_iteration5.txt, Paare aus backtest_paare_iteration5.csv) liegt lokal ein Zuschlag des Nachfolgers (Testfall = Auftragsbekanntmachung 2026) vor?

Regel (vorab, docs/business_case_auswahl.md): Abbruch, wenn weniger als 30 Paare verwertbar sind. Verknüpfung über die Verfahrenskennung (procedure-identifier) der lokal gespeicherten TED-Abfragen (data/raw/ted_search/*competition* und *result*).
Aufruf:  .venv\Scripts\python -I src/report/ka_vorpruefung.py
"""

import csv,glob,json,sys
sys.stdout.reconfigure(encoding='utf-8')
x1=[l.strip() for l in open('data/processed/x1_paare_iteration5.txt',encoding='utf-8') if l.strip()]
pairs={r['pid']:r for r in csv.DictReader(open('data/processed/backtest_paare_iteration5.csv',encoding='utf-8'),delimiter=';')}
print(len(x1),len(pairs)); r0=pairs[x1[0]]; print(r0)
# Index: procedure-identifier -> notices by type, from all local searches
def load(pat):
    out=[]
    for f in glob.glob(pat):
        try: out+=json.load(open(f,encoding='utf-8')).get('notices',[])
        except Exception: pass
    return out
comp=load('data/raw/ted_search/*competition*/*.json'); res=load('data/raw/ted_search/*result*/*.json')
print(len(comp),len(res))
def pid(n):
    p=n.get('procedure-identifier'); return p if isinstance(p,str) else (p[0] if p else None)
comp_by_num={n['publication-number']:n for n in comp}
res_by_proc={}
for n in res:
    p=pid(n)
    if p: res_by_proc.setdefault(p,[]).append(n['publication-number'])
tot=0;hit=0;nolookup=0
rows=[]
for k in x1:
    r=pairs.get(k)
    if not r: continue
    t=r['testfall']; tot+=1
    n=comp_by_num.get(t)
    if not n or not pid(n): nolookup+=1; rows.append((k,t,'kein Verfahrensschluessel')); continue
    z=res_by_proc.get(pid(n))
    if z: hit+=1; rows.append((k,t,'Zuschlag '+','.join(z)))
    else: rows.append((k,t,'kein Zuschlag lokal'))
print('Paare',tot,'ohne Schluessel',nolookup,'mit Zuschlag des Nachfolgers',hit)
for x in rows[:12]: print(x)
