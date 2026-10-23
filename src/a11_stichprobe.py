"""Kriterium V6 (Iteration 3): Ist die Laufzeit bei Zuschlägen vor eForms über REF_NOTICE erreichbar? (Annahme A11)

Stichprobe: 30 zufällige Zuschläge (form-type=result) mit CPV 909 in der CPV-Liste, Auftraggeber DEU, veröffentlicht 01.01.2018 bis
24.10.2023 (vor eForms, ohne Haupt-CPV in der API). Seed 20261024.

Je Zuschlag: Original-XML laden, Verweis auf die frühere Bekanntmachung lesen (`REF_NOTICE`, ersatzweise `NOTICE_NUMBER_OJ`), diese
laden und prüfen, ob ein Laufzeitende bestimmbar ist (Definition wie Iteration 1: Enddatum, oder Beginn + Dauer). Zusätzlich wird
ausgewiesen, ob schon der Zuschlag selbst eine Laufzeit enthält und ob nur eine Dauer ohne Beginn vorliegt.
XML unverändert in data/raw/ted_xml/a11_20261023/.

Ergebnis: reports/a11_stichprobe.md
"""

import random
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

from analyze_completeness import RAW_SEARCH_DIR, load_notices
from kennzahlen_iteration2 import wilson

SEED = 20261024
N = 30
POOL_RUN = "DEU_result_cpv909_20161001_20260930"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
XML_DIR = PROJECT_ROOT / "data" / "raw" / "ted_xml" / "a11_20261023"
REPORT = PROJECT_ROOT / "reports" / "a11_stichprobe.md"
XML_URL = "https://ted.europa.eu/en/notice/{}/xml"


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def fetch(pub: str) -> ET.Element | None:
    path = XML_DIR / f"{pub}.xml"
    if not path.exists():
        for attempt in range(4):
            resp = requests.get(XML_URL.format(pub), timeout=60)
            if resp.status_code == 200:
                path.write_bytes(resp.content)  # unverändert speichern
                break
            time.sleep(2 ** (attempt + 1))
        else:
            return None
        time.sleep(0.5)
    try:
        return ET.fromstring(path.read_bytes())
    except ET.ParseError:
        return None


def first(root: ET.Element, name: str) -> ET.Element | None:
    return next((e for e in root.iter() if local(e.tag) == name), None)


def text(el: ET.Element | None) -> str:
    return re.sub(r"\s+", " ", " ".join(el.itertext())).strip() if el is not None else ""


def duration_info(root: ET.Element) -> dict:
    """Laufzeitangaben im ersten Los: Enddatum, Beginn, Dauer."""
    descr = first(root, "OBJECT_DESCR")
    scope = descr if descr is not None else root
    end, start, dur = first(scope, "DATE_END"), first(scope, "DATE_START"), first(scope, "DURATION")
    return {"end": text(end), "start": text(start), "duration": (text(dur) + " " + dur.get("TYPE", "")).strip() if dur is not None else ""}


def determinable(d: dict) -> bool:
    return bool(d["end"]) or bool(d["start"] and d["duration"])


def ref_pub(root: ET.Element) -> str | None:
    ref = first(root, "REF_NOTICE")
    if ref is None:
        ref = first(root, "NOTICE_NUMBER_OJ")
    m = re.search(r"(\d{4})/S \d+-(\d+)", text(ref)) if ref is not None else None
    return f"{int(m.group(2))}-{m.group(1)}" if m else None


def form_name(root: ET.Element) -> str:
    form = next((e for e in root.iter() if re.fullmatch(r"F\d\d_2014|[A-Z_]+_2014", local(e.tag))), None)
    return local(form.tag) if form is not None else local(root.tag)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    XML_DIR.mkdir(parents=True, exist_ok=True)
    pool = [n for n in load_notices(RAW_SEARCH_DIR / POOL_RUN)
            if "2018-01-01" <= str(n["publication-date"])[:10] <= "2023-10-24" and not n.get("main-classification-proc")]
    pool.sort(key=lambda n: n["publication-number"])
    sample = random.Random(SEED).sample(pool, N)

    rows = []
    for n in sample:
        pub = n["publication-number"]
        root = fetch(pub)
        row = {"pub": pub, "date": str(n["publication-date"])[:10], "form": "", "own": False, "ref": None, "ref_form": "",
               "ref_det": False, "ref_info": {}, "status": ""}
        if root is None:
            row["status"] = "Zuschlag-XML nicht ladbar"
            rows.append(row)
            continue
        row["form"] = form_name(root)
        row["own"] = determinable(duration_info(root))
        row["ref"] = ref_pub(root)
        if row["ref"]:
            ref_root = fetch(row["ref"])
            if ref_root is None:
                row["status"] = "Referenz-XML nicht ladbar"
            else:
                row["ref_form"] = form_name(ref_root)
                row["ref_info"] = duration_info(ref_root)
                row["ref_det"] = determinable(row["ref_info"])
                row["status"] = "bestimmbar" if row["ref_det"] else (
                    "nur Dauer" if row["ref_info"]["duration"] else "keine Laufzeit in Referenz")
        else:
            row["status"] = "kein Verweis"
        rows.append(row)
        print(pub, row["form"], row["ref"], row["ref_form"], row["status"])

    k = sum(r["ref_det"] for r in rows)
    lo, hi = wilson(k, N)
    out = ["# Stichprobe A11: Laufzeit bei Zuschlägen vor eForms (Iteration 3, Kriterium V6)", "",
           f"Erzeugt mit `src/a11_stichprobe.py`. {N} zufällige Zuschläge (Seed {SEED}) aus `data/raw/ted_search/{POOL_RUN}/`, "
           f"veröffentlicht 01.01.2018–24.10.2023, ohne Haupt-CPV in der API (Format vor eForms); Grundgesamtheit {len(pool)}. "
           f"XML in `{XML_DIR.relative_to(PROJECT_ROOT).as_posix()}/`.", "",
           "„Bestimmbar“ wie in Iteration 1: Enddatum, oder Beginn und Dauer (erstes Los der referenzierten Bekanntmachung).", "",
           f"**Ergebnis V6:** Laufzeitende über `REF_NOTICE` bestimmbar bei **{k} von {N} = {k / N * 100:.1f} %** ".replace(".", ",")
           + f"(Wilson {lo * 100:.1f}–{hi * 100:.1f} %). ".replace(".", ",", 2)
           + f"Schwelle ≥ 80 %: **{'erfüllt' if k / N >= 0.8 else 'nicht erfüllt'}**.",
           "", "| Status | Anzahl |", "|---|---|"]
    for s in sorted({r["status"] for r in rows}):
        out.append(f"| {s} | {sum(r['status'] == s for r in rows)} |")
    out.append(f"\nZuschläge, die selbst eine bestimmbare Laufzeit enthalten: {sum(r['own'] for r in rows)} von {N}.\n")
    out += ["| Zuschlag | Datum | Formular | Verweis | Formular Verweis | Beginn | Ende | Dauer | Status |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        i = r["ref_info"]
        out.append(f"| {r['pub']} | {r['date']} | {r['form']} | {r['ref'] or '–'} | {r['ref_form'] or '–'} | {i.get('start', '')} | "
                   f"{i.get('end', '')} | {i.get('duration', '')} | {r['status']} |")
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\n{k}/{N} bestimmbar. Report: {REPORT}")


if __name__ == "__main__":
    main()
