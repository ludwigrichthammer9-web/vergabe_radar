"""Lesehilfe zur Blindprüfung Iteration 4 (W4): lädt die XML der 20 Paare von TED und schreibt den reinen Text nach
data/processed/ted_paare_inhalt.txt.

Vom Nutzer vorgeschlagenes Skript, am 2026-10-29 von Claude mit zwei Änderungen ausgeführt (Ausgabe in data/processed statt im
Projektstamm, 0,5 s Pause und ein zweiter Versuch je Abruf). Arbeitshilfe zum Lesen, kein Rohdatensatz: Der Text enthält keine
Feldnamen und keine Losstruktur. Ergebnis 2026-10-29: 40 von 40 Abrufen ohne Fehler.

Aufruf:
    python -I src/lesehilfe_blindpruefung_iteration4.py
"""
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "processed" / "ted_paare_inhalt.txt"

PAARE = [
    ('P1', '209315-2019', '100442-2026'), ('P2', '38758-2022', '52190-2026'),
    ('P3', '347828-2022', '183269-2026'), ('P4', '328497-2023', '134081-2026'),
    ('P5', '662197-2021', '108283-2026'), ('P6', '316381-2022', '21073-2026'),
    ('P7', '272214-2020', '14788-2026'), ('P8', '448916-2023', '84590-2026'),
    ('P9', '289728-2022', '87147-2026'), ('P10', '540553-2025', '198259-2026'),
    ('P11', '79802-2023', '93751-2026'), ('P12', '477144-2023', '62104-2026'),
    ('P13', '37979-2026', '78859-2026'), ('P14', '789489-2024', '153719-2026'),
    ('P15', '181605-2024', '122844-2026'), ('P16', '552382-2019', '54141-2026'),
    ('P17', '765145-2025', '139668-2026'), ('P18', '326187-2022', '45854-2026'),
    ('P19', '362257-2022', '134489-2026'), ('P20', '325959-2023', '195060-2026'),
]


def fetch_ted_text(notice_id):
    url = f"https://ted.europa.eu/de/notice/{notice_id}/xml"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    last = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                xml_bytes = resp.read()
            root = ET.fromstring(xml_bytes)
            lines = [t.strip() for t in root.itertext() if t.strip()]
            time.sleep(0.5)
            return "\n".join(lines)
        except Exception as e:
            last = e
            time.sleep(2)
    return f"FEHLER bei {notice_id}: {last}"


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fehler = 0
    with open(OUT, "w", encoding="utf-8") as out:
        for pid, alt, neu in PAARE:
            print(f"Lade {pid} ({alt} / {neu})...", flush=True)
            a, n = fetch_ted_text(alt), fetch_ted_text(neu)
            fehler += a.startswith("FEHLER") + n.startswith("FEHLER")
            out.write(f"==================== {pid} ====================\n")
            out.write(f"--- ALT: {alt} ---\n{a}\n\n")
            out.write(f"--- NEU: {neu} ---\n{n}\n\n")
    print(f"Fertig: {OUT} ({fehler} Fehler von 40)")
