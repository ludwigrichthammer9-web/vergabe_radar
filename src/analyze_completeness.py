"""Wertet die Rohdaten aus ted_download.py aus: Befüllungsgrad der Kernfelder und häufigste CPV-Bereiche.

Ergebnis:
    data/processed/notices_<lauf>.csv      eine Zeile pro Bekanntmachung (bereinigt)
    reports/datenqualitaet_<lauf>.md       Markdown-Report

Aufruf:
    .venv\\Scripts\\python src/analyze_completeness.py                 # neuester Lauf in data/raw/ted_search
    .venv\\Scripts\\python src/analyze_completeness.py --run DEU_20260722_20261021
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date
from pathlib import Path

import pandas as pd
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_SEARCH_DIR = PROJECT_ROOT / "data" / "raw" / "ted_search"
CPV_FILE = PROJECT_ROOT / "data" / "raw" / "cpv" / "cpv.gc"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_DIR = PROJECT_ROOT / "reports"

# Offizielle CPV-2008-Codeliste (Publications Office, eForms SDK) mit Bezeichnungen in allen EU-Sprachen
CPV_URL = "https://raw.githubusercontent.com/OP-TED/eForms-SDK/develop/codelists/cpv.gc"

# Kategorie -> Felder. Eine Kategorie gilt als befüllt, wenn mindestens eines ihrer Felder befüllt ist.
CATEGORIES = {
    "Vertragslaufzeit": [
        "contract-duration-period-lot",
        "contract-duration-start-date-lot",
        "contract-duration-end-date-lot",
        "contract-duration-period-oth-lot",
    ],
    "Verlängerungsoptionen": [
        "renewal-maximum-lot",
        "renewal-description-lot",
        "option-description-lot",
    ],
    "CPV-Code": [
        "main-classification-proc",
        "main-classification-lot",
        "classification-cpv",
    ],
    "Auftraggeber": ["buyer-name"],
    "Auftragswert": [
        "total-value",
        "result-value-lot",
        "tender-value",
        "estimated-value-proc",
        "estimated-value-lot",
        "framework-maximum-value-lot",
    ],
}

FIELD_LABELS = {
    "contract-duration-period-lot": "BT-36 Laufzeit (Dauer)",
    "contract-duration-start-date-lot": "BT-536 Laufzeitbeginn",
    "contract-duration-end-date-lot": "BT-537 Laufzeitende",
    "contract-duration-period-oth-lot": "BT-538 Laufzeit sonstige (z. B. unbefristet)",
    "renewal-maximum-lot": "BT-58 max. Anzahl Verlängerungen",
    "renewal-description-lot": "BT-57 Beschreibung Verlängerung",
    "option-description-lot": "BT-54 Beschreibung Optionen",
    "main-classification-proc": "BT-262 Haupt-CPV (Verfahren)",
    "main-classification-lot": "BT-262 Haupt-CPV (Los)",
    "classification-cpv": "alle CPV-Codes",
    "buyer-name": "BT-500 Name Auftraggeber",
    # Kein reines BT-161: TED berechnet den Wert auch, wenn BT-161 fehlt (Stichprobe 573266-2026)
    "total-value": "Gesamtwert, von TED berechnet (BT-161, sonst abgeleitet)",
    "result-value-lot": "BT-709 Höchstwert Rahmenvertrag (Los)",
    "tender-value": "BT-720 Wert des Zuschlagsangebots",
    "estimated-value-proc": "BT-27 geschätzter Wert (Verfahren)",
    "estimated-value-lot": "BT-27 geschätzter Wert (Los)",
    "framework-maximum-value-lot": "Höchstwert Rahmenvereinbarung (Los)",
}

VALUE_FIELDS = CATEGORIES["Auftragswert"]

# Beispiel-Nischen aus CLAUDE.md, über Präfix des Haupt-CPV-Codes
NICHES = {
    "Gebäudereinigung (CPV 909…)": ["909"],
    "Winterdienst (CPV 90620000, 90630000)": ["9062", "9063"],
    "IT-Dienste (CPV 72…)": ["72"],
    "IT-Wartung/Support (CPV 503…, 7225…, 72267…)": ["503", "7225", "72267"],
    "Sicherheitsdienste (CPV 7971…)": ["7971"],
}

UNIT_TO_MONTHS = {"DAY": 1 / 30.44, "WEEK": 7 / 30.44, "MONTH": 1, "YEAR": 12}


# ---------------------------------------------------------------- Hilfsfunktionen


def is_filled(value) -> bool:
    """True, wenn ein echter Wert vorhanden ist. "-1" gilt als Platzhalter (nicht veröffentlicht)."""
    if value is None:
        return False
    if isinstance(value, (list, tuple)):
        return any(is_filled(v) for v in value)
    if isinstance(value, dict):
        return any(is_filled(v) for v in value.values())
    if isinstance(value, (int, float)):
        return value != -1
    text = str(value).strip()
    return text != "" and text != "-1"


def contains_minus_one(value) -> bool:
    if isinstance(value, (list, tuple)):
        return any(contains_minus_one(v) for v in value)
    return str(value).strip() == "-1" or value == -1


def flatten(value) -> list:
    """Verschachtelte Listen/Dicts zu einer flachen Liste von Werten."""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [x for v in value for x in flatten(v)]
    if isinstance(value, dict):
        return [x for v in value.values() for x in flatten(v)]
    return [value]


def first_text(value, prefer_lang="deu") -> str:
    if isinstance(value, dict) and value.get(prefer_lang):
        value = value[prefer_lang]
    vals = flatten(value)
    return str(vals[0]) if vals else ""


def first_number(value):
    for v in flatten(value):
        try:
            num = float(v)
        except (TypeError, ValueError):
            continue
        if num != -1:
            return num
    return None


def max_number(value):
    nums = []
    for v in flatten(value):
        try:
            nums.append(float(v))
        except (TypeError, ValueError):
            continue
    return max(nums, default=None)


def duration_months(period) -> float | None:
    """BT-36 kommt als [{"value": "12", "unit": "MONTH"}]; wir nehmen das erste Los."""
    for item in period or []:
        if isinstance(item, dict) and item.get("unit") in UNIT_TO_MONTHS:
            try:
                return float(item["value"]) * UNIT_TO_MONTHS[item["unit"]]
            except (TypeError, ValueError):
                continue
    return None


MAX_PLAUSIBLE_MONTHS = 240


def months_between(start: str, end: str) -> float | None:
    """Laufzeit in Monaten aus BT-536/BT-537 (inklusive Endtag); None, wenn ein Datum fehlt oder ungültig ist."""
    try:
        days = (date.fromisoformat(end) - date.fromisoformat(start)).days + 1
    except ValueError:
        return None
    return days / 30.44


def pct(part, total) -> str:
    return f"{100 * part / total:.1f} %".replace(".", ",") if total else "–"


def num(x) -> str:
    """Deutsche Tausenderpunkte: 15706 -> 15.706"""
    return f"{x:,}".replace(",", ".")


def fmt_date(yyyymmdd: str) -> str:
    return f"{yyyymmdd[6:8]}.{yyyymmdd[4:6]}.{yyyymmdd[:4]}"


# ---------------------------------------------------------------- CPV-Bezeichnungen


def load_cpv_labels() -> dict[str, str]:
    if not CPV_FILE.exists():
        print(f"Lade CPV-Codeliste von {CPV_URL} ...")
        resp = requests.get(CPV_URL, timeout=300)
        resp.raise_for_status()
        CPV_FILE.parent.mkdir(parents=True, exist_ok=True)
        CPV_FILE.write_bytes(resp.content)  # roh und unverändert speichern
    labels = {}
    for _, row in ET.iterparse(CPV_FILE):
        if row.tag != "Row":
            continue
        cols = {v.get("ColumnRef"): v.findtext("SimpleValue") for v in row.findall("Value")}
        if cols.get("code"):
            labels[cols["code"]] = cols.get("deu_label") or cols.get("Name") or ""
        row.clear()
    return labels


def cpv_label(labels: dict, prefix: str) -> str:
    """Bezeichnung für Abteilung (2 Stellen) oder Gruppe (3 Stellen): Code mit Nullen auffüllen."""
    return labels.get(prefix.ljust(8, "0"), "(unbekannt)")


# ---------------------------------------------------------------- Daten laden


def load_notices(run_dir: Path) -> list[dict]:
    notices = []
    for page_file in sorted(run_dir.glob("page_*.json")):
        data = json.loads(page_file.read_bytes().decode("utf-8"))
        notices.extend(data.get("notices", []))
    return notices


def build_table(notices: list[dict]) -> pd.DataFrame:
    rows = []
    for n in notices:
        main_cpv = first_text(n.get("main-classification-proc")) or first_text(
            n.get("main-classification-lot")
        ) or first_text(n.get("classification-cpv"))
        row = {
            "publication_number": n.get("publication-number"),
            "publication_date": str(n.get("publication-date", ""))[:10],
            "notice_type": first_text(n.get("notice-type")),
            "contract_nature": first_text(n.get("contract-nature-main-proc")),
            "procedure_type": first_text(n.get("procedure-type")),
            "buyer_name": first_text(n.get("buyer-name")),
            "main_cpv": main_cpv,
            "cpv_division": main_cpv[:2],
            "cpv_group": main_cpv[:3],
            "duration_months_lot1": duration_months(n.get("contract-duration-period-lot")),
            "start_date_lot1": first_text(n.get("contract-duration-start-date-lot"))[:10],
            "end_date_lot1": first_text(n.get("contract-duration-end-date-lot"))[:10],
            "renewal_max": max((int(v) for v in flatten(n.get("renewal-maximum-lot")) if str(v).isdigit()), default=None),
            "total_value": first_number(n.get("total-value")),
            "tender_value": first_number(n.get("tender-value")),
            "estimated_value": first_number(n.get("estimated-value-proc")) or first_number(n.get("estimated-value-lot")),
            "lots": max(len(n.get("main-classification-lot") or []), 1),
        }
        for fields in CATEGORIES.values():
            for f in fields:
                row[f"filled:{f}"] = is_filled(n.get(f))
        for f in VALUE_FIELDS:
            row[f"minus1:{f}"] = contains_minus_one(n.get(f)) if f in n else False
        for cat, fields in CATEGORIES.items():
            row[f"cat:{cat}"] = any(row[f"filled:{f}"] for f in fields)
        # Platzhalter wie 0 oder 0.01 € sind häufig: "plausibel" = mindestens ein Wertfeld > 1 €
        row["value_plausible"] = any((max_number(n.get(f)) or 0) > 1 for f in VALUE_FIELDS)
        row["renewal_gt0"] = (row["renewal_max"] or 0) > 0
        row["end_or_duration"] = row["filled:contract-duration-end-date-lot"] or row["filled:contract-duration-period-lot"]
        # Strenger: ein Enddatum liegt vor oder lässt sich aus Beginn + Dauer berechnen
        row["end_determinable"] = row["filled:contract-duration-end-date-lot"] or (
            row["filled:contract-duration-start-date-lot"] and row["filled:contract-duration-period-lot"]
        )
        months = months_between(row["start_date_lot1"], row["end_date_lot1"])
        row["duration_dates_implausible"] = months is not None and not 0 < months <= MAX_PLAUSIBLE_MONTHS
        row["duration_dates_months_lot1"] = None if row["duration_dates_implausible"] else months
        rows.append(row)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- Report


def md_table(df: pd.DataFrame) -> str:
    return df.to_markdown(index=False)


def build_report(df: pd.DataFrame, meta: dict, labels: dict) -> str:
    total = len(df)
    out = []
    out.append(f"# Datenqualität TED-Zuschlagsbekanntmachungen {meta.get('country', '')}")
    out.append("")
    out.append(
        f"Zeitraum (Veröffentlichung): **{fmt_date(meta['date_from'])} – {fmt_date(meta['date_to'])}** · "
        f"Bekanntmachungen: **{num(total)}** ·Download: {meta.get('downloaded_at', '?')[:16]} UTC"
    )
    out.append("")
    out.append(f"Query: `{meta['query']}`")

    # 1. Überblick
    out.append("\n## 1. Überblick\n")
    nt = df["notice_type"].value_counts().rename_axis("Notice-Typ").reset_index(name="Anzahl")
    nt["Anteil"] = [pct(c, total) for c in nt["Anzahl"]]
    out.append(md_table(nt))
    out.append("")
    cn = df["contract_nature"].replace("", "(leer)").value_counts().rename_axis("Vertragsart").reset_index(name="Anzahl")
    cn["Anteil"] = [pct(c, total) for c in cn["Anzahl"]]
    out.append(md_table(cn))
    multi = (df["lots"] > 1).sum()
    out.append(f"\n{num(multi)} Bekanntmachungen ({pct(multi, total)}) haben mehr als ein Los.")

    # 2. Befüllungsgrad je Kategorie
    out.append("\n## 2. Befüllungsgrad der Kernkategorien\n")
    out.append("Eine Kategorie gilt als befüllt, wenn mindestens eines ihrer Felder in mindestens einem Los "
               "einen echten Wert hat (`-1` zählt nicht).\n")
    cat_rows = [{"Kategorie": c, "befüllt": pct(df[f"cat:{c}"].sum(), total), "Anzahl": int(df[f"cat:{c}"].sum())}
                for c in CATEGORIES]
    out.append(md_table(pd.DataFrame(cat_rows)))

    out.append("\n### Einzelfelder\n")
    field_rows = []
    for cat, fields in CATEGORIES.items():
        for f in fields:
            r = {"Kategorie": cat, "Feld": f"`{f}`", "Bedeutung": FIELD_LABELS.get(f, ""),
                 "befüllt": pct(df[f"filled:{f}"].sum(), total)}
            r["enthält `-1`"] = pct(df[f"minus1:{f}"].sum(), total) if f in VALUE_FIELDS else ""
            field_rows.append(r)
    out.append(md_table(pd.DataFrame(field_rows)))

    # Zusatzkennzahlen
    out.append("\n### Zusatzkennzahlen für die Prognose\n")
    dur = df["duration_months_lot1"].dropna()
    unlimited = df["filled:contract-duration-period-oth-lot"].sum()
    any_minus1 = df[[f"minus1:{f}" for f in VALUE_FIELDS]].any(axis=1).sum()
    extras = [
        ("Laufzeitende (BT-537) **oder** Dauer (BT-36) vorhanden", pct(df["end_or_duration"].sum(), total)),
        ("Beginn **und** Ende vorhanden", pct((df["filled:contract-duration-start-date-lot"]
                                               & df["filled:contract-duration-end-date-lot"]).sum(), total)),
        ("Laufzeit „sonstige“ (meist UNLIMITED/UNKNOWN)", pct(unlimited, total)),
        ("BT-58 vorhanden (auch `0`)", pct(df["filled:renewal-maximum-lot"].sum(), total)),
        ("BT-58 > 0 (mind. eine Verlängerung möglich)", pct(df["renewal_gt0"].sum(), total)),
        ("mind. ein Wertfeld enthält `-1` (Wert nicht veröffentlicht)", pct(any_minus1, total)),
        ("**plausibler Auftragswert** (mind. ein Wertfeld > 1 €)", pct(df["value_plausible"].sum(), total)),
    ]
    out.append(md_table(pd.DataFrame(extras, columns=["Kennzahl", "Anteil"])))
    if len(dur):
        out.append(
            f"\nLaufzeit laut BT-36 (erstes Los, n = {num(len(dur))}): Median **{dur.median():.0f} Monate**, "
            f"25 %-Quantil {dur.quantile(.25):.0f}, 75 %-Quantil {dur.quantile(.75):.0f} Monate."
        )

    # 3. CPV
    out.append("\n## 3. Häufigste CPV-Bereiche (Haupt-CPV der Bekanntmachung)\n")
    out.append("### CPV-Abteilungen (2-stellig), Top 20\n")
    div = df["cpv_division"].value_counts().head(20)
    out.append(md_table(pd.DataFrame({
        "Abteilung": div.index,
        "Bezeichnung": [cpv_label(labels, d) for d in div.index],
        "Anzahl": div.values,
        "Anteil": [pct(c, total) for c in div.values],
    })))
    out.append("\n### CPV-Gruppen (3-stellig), Top 25\n")
    grp = df["cpv_group"].value_counts().head(25)
    out.append(md_table(pd.DataFrame({
        "Gruppe": grp.index,
        "Bezeichnung": [cpv_label(labels, g) for g in grp.index],
        "Anzahl": grp.values,
        "Anteil": [pct(c, total) for c in grp.values],
    })))

    # 4. Befüllungsgrad je CPV-Abteilung
    out.append("\n## 4. Befüllungsgrad je CPV-Abteilung (Top 15)\n")
    out.append("Beantwortet: Welche Kategorien sind häufig **und** gut befüllt?\n")
    rows = []
    for d in df["cpv_division"].value_counts().head(15).index:
        sub = df[df["cpv_division"] == d]
        rows.append({
            "Abt.": d,
            "Bezeichnung": cpv_label(labels, d)[:60],
            "Anzahl": len(sub),
            "Laufzeit": pct(sub["cat:Vertragslaufzeit"].sum(), len(sub)),
            "Ende/Dauer": pct(sub["end_or_duration"].sum(), len(sub)),
            "Verlängerung": pct(sub["cat:Verlängerungsoptionen"].sum(), len(sub)),
            "BT-58 > 0": pct(sub["renewal_gt0"].sum(), len(sub)),
            "Wert": pct(sub["cat:Auftragswert"].sum(), len(sub)),
            "Wert > 1 €": pct(sub["value_plausible"].sum(), len(sub)),
        })
    out.append(md_table(pd.DataFrame(rows)))

    out.append("\n### Beispiel-Nischen aus CLAUDE.md\n")
    rows = []
    for name, prefixes in NICHES.items():
        sub = df[df["main_cpv"].str.startswith(tuple(prefixes))]
        n = len(sub)
        rows.append({
            "Nische": name,
            "Anzahl (3 Monate)": n,
            "Laufzeit": pct(sub["cat:Vertragslaufzeit"].sum(), n),
            "Ende/Dauer": pct(sub["end_or_duration"].sum(), n),
            "Verlängerung": pct(sub["cat:Verlängerungsoptionen"].sum(), n),
            "BT-58 > 0": pct(sub["renewal_gt0"].sum(), n),
            "Wert": pct(sub["cat:Auftragswert"].sum(), n),
            "Wert > 1 €": pct(sub["value_plausible"].sum(), n),
            "Median-Laufzeit BT-36 (Mon.)": f"{sub['duration_months_lot1'].median():.0f}" if sub["duration_months_lot1"].notna().any() else "–",
        })
    out.append(md_table(pd.DataFrame(rows)))

    # 5. Laufzeit aus Beginn und Ende
    out.append("\n## 5. Laufzeit aus Beginn und Ende (BT-536/BT-537)\n")
    out.append(
        "BT-36 (Dauer) ist nur bei rund 21 % befüllt. Hier wird die Laufzeit zusätzlich aus Beginn und Ende des ersten Loses "
        f"berechnet (Ende − Beginn + 1 Tag, in Monaten à 30,44 Tage). Werte ≤ 0 oder > {MAX_PLAUSIBLE_MONTHS} Monate gelten als "
        "unplausibel und werden ausgeschlossen.\n\n"
        "**Laufzeitende bestimmbar** heißt: Enddatum (BT-537) vorhanden **oder** Beginn (BT-536) und Dauer (BT-36) vorhanden. "
        "Das ist strenger als „Ende/Dauer“ in Abschnitt 2 und 4, wo eine Dauer ohne Beginn mitzählt.\n"
    )
    dates = df["duration_dates_months_lot1"].dropna()
    bt36 = df["duration_months_lot1"].dropna()

    def stats(s: pd.Series) -> dict:
        if s.empty:
            return {"n": 0, "Median": "–", "25 %": "–", "75 %": "–"}
        return {"n": num(len(s)), "Median": f"{s.median():.0f}", "25 %": f"{s.quantile(.25):.0f}",
                "75 %": f"{s.quantile(.75):.0f}"}

    out.append("### Gesamt (Monate)\n")
    out.append(md_table(pd.DataFrame([
        {"Quelle": "BT-36 Dauer", "Anteil": pct(len(bt36), total), **stats(bt36)},
        {"Quelle": "Ende − Beginn", "Anteil": pct(len(dates), total), **stats(dates)},
    ])))
    both = df.dropna(subset=["duration_months_lot1", "duration_dates_months_lot1"])
    agree = ((both["duration_months_lot1"] - both["duration_dates_months_lot1"]).abs() <= 1).sum()
    out.append(
        f"\nLaufzeitende bestimmbar: **{pct(df['end_determinable'].sum(), total)}** aller Notices. "
        f"Unplausible Datumspaare ausgeschlossen: {num(int(df['duration_dates_implausible'].sum()))}. "
        f"Notices mit BT-36 **und** Datumspaar: {num(len(both))}, davon stimmen {pct(agree, len(both))} auf ±1 Monat überein."
    )

    out.append("\n### Je Beispielnische (Monate)\n")
    rows = []
    for name, prefixes in NICHES.items():
        sub = df[df["main_cpv"].str.startswith(tuple(prefixes))]
        s36, sdat = stats(sub["duration_months_lot1"].dropna()), stats(sub["duration_dates_months_lot1"].dropna())
        rows.append({
            "Nische": name,
            "n": len(sub),
            "Ende bestimmbar": pct(sub["end_determinable"].sum(), len(sub)),
            "BT-36: n": s36["n"], "BT-36: Median": s36["Median"],
            "Datum: n": sdat["n"], "Datum: Median": sdat["Median"], "Datum: 25 %": sdat["25 %"], "Datum: 75 %": sdat["75 %"],
        })
    out.append(md_table(pd.DataFrame(rows)))

    # 6. Methodik
    out.append("\n## 6. Methodische Hinweise\n")
    out.append(
        "- **Ebene:** Ausgewertet wird pro Bekanntmachung. Lot-Felder sind Listen; „befüllt“ heißt: mindestens ein Los hat einen Wert. "
        "Ob *alle* Lose befüllt sind, ist hier nicht geprüft.\n"
        "- **`-1`:** Wertfelder enthalten oft `-1`. Wir werten das als Platzhalter für „nicht veröffentlicht“ "
        "und zählen es als nicht befüllt.\n"
        "- **Platzhalterwerte:** Zusätzlich tragen viele Vergabestellen `0` oder `0,01 €` ein (z. B. 505084-2026: "
        "Gesamtwert 0,00 €, Angebot 0,01 €). Diese zählen in Abschnitt 2 als „befüllt“. Realistischer ist die Kennzahl "
        "„plausibler Auftragswert (> 1 €)“.\n"
        "- **`total-value` ist nicht BT-161:** TED berechnet dieses Feld auch, wenn die Bekanntmachung keinen Gesamtwert (BT-161) "
        "enthält (Stichprobe 573266-2026, siehe reports/stichprobe_iteration1.md). Seine Befüllungsquote überschätzt daher, wie oft "
        "Vergabestellen selbst einen Gesamtwert angeben.\n"
        "- **Verlängerungen oft nur als Freitext:** In 505084-2026 stehen zwei Verlängerungsjahre nur in BT-54 "
        "(Optionen-Text), BT-58 ist leer. Für die Prognose müssen Verlängerungen also aus dem Text extrahiert werden.\n"
        "- **Verlängerungen:** Ein fehlendes Verlängerungsfeld kann eine Datenlücke sein, aber auch „es gibt keine Verlängerung“ bedeuten. "
        "Der Befüllungsgrad ist hier also keine reine Datenqualitätskennzahl. Ein vorhandenes BT-58 = `0` bedeutet ausdrücklich „keine Verlängerung“.\n"
        "- **Haupt-CPV:** `main-classification-proc`, ersatzweise das erste Los. Bei Bekanntmachungen mit vielen Losen "
        "verschiedener Branchen wird nur der Haupt-Code gezählt.\n"
        "- **Auswahl:** `form-type=result` (can-standard, can-social, can-desg, can-tran). Vertragsänderungen (can-modif) "
        "und Ex-ante-Transparenz (veat) sind nicht enthalten.\n"
        f"- **CPV-Bezeichnungen:** offizielle CPV-2008-Liste aus dem eForms SDK ({CPV_URL})."
    )
    return "\n".join(out) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run", help="Unterordner in data/raw/ted_search (Standard: neuester)")
    args = parser.parse_args()

    if args.run:
        run_dir = RAW_SEARCH_DIR / args.run
    else:
        runs = sorted((p for p in RAW_SEARCH_DIR.iterdir() if p.is_dir()), key=lambda p: p.stat().st_mtime)
        if not runs:
            sys.exit("Keine Rohdaten gefunden. Erst src/ted_download.py ausführen.")
        run_dir = runs[-1]
    meta = json.loads((run_dir / "request_meta.json").read_text(encoding="utf-8"))
    print(f"Lauf: {run_dir.name}")

    notices = load_notices(run_dir)
    print(f"{len(notices):,} Notices geladen")
    df = build_table(notices)
    dupes = df["publication_number"].duplicated().sum()
    if dupes:
        print(f"WARNUNG: {dupes} doppelte publication-numbers, werden entfernt")
        df = df.drop_duplicates("publication_number")

    labels = load_cpv_labels()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = PROCESSED_DIR / f"notices_{run_dir.name}.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")  # utf-8-sig: Excel erkennt Umlaute

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"datenqualitaet_{run_dir.name}.md"
    report_path.write_text(build_report(df, meta, labels), encoding="utf-8")
    print(f"CSV:    {csv_path}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
