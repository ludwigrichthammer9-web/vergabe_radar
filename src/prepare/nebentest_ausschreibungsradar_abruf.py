"""Iteration 10, W7: Suche der 15 Nebentest-Lose bei AusschreibungsRadar (docs/iterationen.md).

Rahmen aus W7: nur Pfade, die robots.txt erlaubt (/vertragsende/?cpv=90&page=N, /ausschreibung/<uuid>/), Pause ≥ 2 s, höchstens 60 Seitenabrufe insgesamt
(5 Abrufe zur Erkundung des Filters sind schon verbraucht, siehe Protokoll in reports/nebentest_ausschreibungsradar.md). Seiten unverändert nach
data/raw/ausschreibungsradar_20261105/. Quelle: ausschreibungsradar.com, Abruf 2026-11-05.

Schritt 1 (--liste): Seiten 1 bis N der Liste (cpv=90, sort=frist) laden, bis keine Einträge mehr kommen.
Schritt 2 (ohne Argument): Einträge nach Auftraggeber/Titel der 15 Lose durchsuchen (nur Kandidatenfindung), Detailseiten der Kandidaten laden,
Treffer nur anerkennen, wenn die noticeId im Link zu oeffentlichevergabe.de einer notice-id aus dem TED-XML der Bekanntmachung (Auftrag oder Zuschlag) entspricht.
"""

import csv
import re
import sys
import time
import html
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent.parent
D = ROOT / "data" / "raw" / "ausschreibungsradar_20261105"
BASE = "https://ausschreibungsradar.com"
HEADERS = {"User-Agent": "vergabe-radar-studienprojekt"}
PAUSE = 2.5


def lade(url: str, ziel: Path) -> str:
    if ziel.exists():
        return ziel.read_text(encoding="utf-8")
    time.sleep(PAUSE)
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    ziel.write_bytes(r.content)  # unverändert
    return r.text


def text(t: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))


def eintraege(seite: str) -> list[dict]:
    """Einträge der Listenseite: Link, Klartext (Titel, Auftraggeber, Zuschlagsempfänger, Laufzeitende)."""
    out = []
    for m in re.finditer(r'<a[^>]+href="(/ausschreibung/[0-9a-f-]{36}/)"[^>]*>(.*?)</a>', seite, re.S):
        out.append({"url": m.group(1), "text": text(m.group(2))})
    return out


# Von Hand nach Titelähnlichkeit gewählte Kandidaten aus der Liste (Stichwortsuche nach Auftraggeber, Ausgabe von main). Anerkannt wird ein Treffer nur über die noticeId.
# Für N27, N63, N73 und N25 (nur Fremdtitel) fand die Stichwortsuche keinen plausiblen Kandidaten in der Liste (Ende des Loses vermutlich später als 18 Monate oder nicht gelistet).
KANDIDATEN = {
    "N7": ["5f896802-7cdf-4b2b-8343-7c58201c2047", "9ff4cb6b-233d-4929-a5c6-152fa4b14057"],
    "N10": ["2865d1fe-77b8-4b5d-bf77-e3ec7020da28"],
    "N19": ["0d16d8d4-fa24-45c3-8fb6-e60b63c60771"],
    "N35": ["2c2f75fb-b19a-426d-a829-f8df35067e4f"],
    "N55": ["5987ab0f-25ac-49bd-95b6-6e583b59c26b"],
    "N95": ["019bea24-5c7e-4c4e-a113-349723ece16f"],
    "N106": ["e8f33c22-4b53-4edd-8f83-9e0e303de78f", "a02d05a8-1fae-4f26-ba2e-58a8cfc81206", "ce51b24f-cd91-4f2a-88ca-e4a70637c3f0"],
}


def ids_der_bekanntmachung(pub: str) -> set[str]:
    """notice-id der Zuschlagsbekanntmachung, ContractFolderID und notice-identifier der Auftragsbekanntmachungen mit derselben Verfahrenskennung."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import vergleich_iteration10 as v10
    refs, folder, eigen = v10.referenzen(pub)
    ids = {eigen, folder} | set(v10.verfahrensindex().get(folder, []))
    for ref in refs:
        if (v10.XML10 / f"{ref}.xml").exists():
            ids.add(v10.notice_id(ref, False))
    return {i.lower() for i in ids if i}


def pruefe() -> None:
    lose = {r["N"]: r for r in csv.DictReader((ROOT / "reports" / "nebentest_ausschreibungsradar_lose.csv").open(encoding="utf-8"), delimiter=";")}
    for n, urls in KANDIDATEN.items():
        ids = ids_der_bekanntmachung(lose[n]["notice"])
        for u in urls:
            seite = lade(f"{BASE}/ausschreibung/{u}/", D / f"ausschreibung_{u}.html")
            nid = re.findall(r"oeffentlichevergabe.de/ui/de/notices/([0-9a-fA-F-]{36})", seite)
            laufzeit = re.search(r"Laufzeit\s*([0-9.]+\s*[–-]\s*[0-9.]+)", text(seite))
            print(n, lose[n]["notice"], u[:8], "noticeId", nid[:1], "→", "TREFFER" if any(x.lower() in ids for x in nid) else "kein Treffer", "| Laufzeit", laufzeit.group(1) if laufzeit else "–")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    if "--pruefe" in sys.argv:
        pruefe()
        return
    if "--liste" in sys.argv:
        n = 1
        while n <= 40:
            t = lade(f"{BASE}/vertragsende/?cpv=90&sort=frist&page={n}", D / f"vertragsende_cpv90_p{n}.html")
            e = eintraege(t)
            print(f"Seite {n}: {len(e)} Einträge")
            if not e:
                break
            n += 1
        return

    lose = list(csv.DictReader((ROOT / "reports" / "nebentest_ausschreibungsradar_lose.csv").open(encoding="utf-8"), delimiter=";"))
    liste = {}
    for r in csv.DictReader((ROOT / "data" / "processed" / "vertragsliste_909.csv").open(encoding="utf-8-sig"), delimiter=";"):
        liste[(r["notice"], r["los"])] = r
    alle = []
    for p in sorted(D.glob("vertragsende_cpv90_p*.html"), key=lambda x: int(re.search(r"p(\d+)", x.name).group(1))):
        alle += eintraege(p.read_text(encoding="utf-8"))
    print(len(alle), "Einträge in der Liste")
    for r in lose:
        l = liste[(r["notice"], r["los"])]
        schluessel = [w.lower() for w in re.findall(r"[A-Za-zÄÖÜäöüß]{5,}", l["auftraggeber"])][:3]
        kand = [e for e in alle if all(s in e["text"].lower() for s in schluessel[:2])] if schluessel else []
        print(r["N"], r["notice"], l["auftraggeber"][:50], "|", l["los_titel"][:40], "→", len(kand), "Kandidaten")
        for e in kand[:6]:
            print("    ", e["url"], e["text"][:140])


if __name__ == "__main__":
    main()
