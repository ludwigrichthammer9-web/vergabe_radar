"""Foliengerüst für den Vortrag (LN B: 15 min, höchstens 12 Folien) mit Sprechernotizen.

Zahlen aus docs/iterationen.md und reports/evaluation_iteration5.md bis 8. Jede Folie hat Notizen: Zeit, Kernaussage, „Zeig-mir-wo“.
Aufruf:  .venv\\Scripts\\python -I src/report/vortrag.py      Ausgabe: docs/vortrag/vortrag_vergabe_radar.pptx
"""

from pathlib import Path

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "docs" / "vortrag" / "vortrag_vergabe_radar.pptx"

DARK, TEAL, AMBER, RED, GREEN, GREY, PALE, INK, WHITE, SOFT = (RGBColor.from_string(h) for h in
    ("0B3C49", "1C7293", "F2A541", "C8553D", "4C956C", "6C7A89", "EAF3F5", "1B2A33", "FFFFFF", "8FB8C4"))
HEAD, BODY = "Cambria", "Calibri"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(10), Inches(5.625)
LAYOUT_TITLE_ONLY = prs.slide_layouts[5]
LAYOUT_BLANK = prs.slide_layouts[6]
_nr = [0]


def box(s, x, y, w, h, paras, size=14, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font=BODY, name=None, space=0):
    """Textfeld. paras: str oder Liste von Absätzen; ein Absatz ist str oder Liste von (Text, {bold, color}) oder dict(bullet=...)."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    paras = [paras] if isinstance(paras, str) else paras
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        if space:
            para.space_after = Pt(space)
        runs = [(p, {})] if isinstance(p, str) else p
        for text, o in runs:
            r = para.add_run()
            r.text = text
            r.font.name = o.get("font", font)
            r.font.size = Pt(o.get("size", size))
            r.font.bold = o.get("bold", bold)
            r.font.color.rgb = o.get("color", color)
    return tb


def rect(s, x, y, w, h, fill, shape=MSO_SHAPE.RECTANGLE, name=None):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.fill.background()
    sh.shadow.inherit = False
    if name:
        sh.name = name
    return sh


def new_slide(titel, notes, dark=False):
    s = prs.slides.add_slide(LAYOUT_BLANK if dark else LAYOUT_TITLE_ONLY)
    _nr[0] += 1
    if dark:
        s.background.fill.solid()
        s.background.fill.fore_color.rgb = DARK
    else:
        t = s.shapes.title
        t.left, t.top, t.width, t.height = Inches(0.5), Inches(0.3), Inches(9), Inches(0.75)
        tf = t.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run()
        r.text = titel
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = HEAD, Pt(30), True, DARK
    box(s, 9.1, 5.2, 0.5, 0.3, str(_nr[0]), size=10, color=SOFT if dark else GREY, align=PP_ALIGN.RIGHT, name="Foliennummer")
    s.notes_slide.notes_text_frame.text = notes
    return s


def stat(s, x, y, w, zahl, label, farbe, name):
    rect(s, x, y, w, 1.5, PALE, name=name + " Karte")
    box(s, x + 0.15, y + 0.1, w - 0.3, 0.7, zahl, size=38, bold=True, color=farbe, font=HEAD, name=name + " Zahl")
    box(s, x + 0.15, y + 0.85, w - 0.3, 0.6, label, size=13, name=name + " Text")


def balken(s, x, y, w, h, kategorien, werte, farben, name, maximum=118):
    cd = CategoryChartData()
    cd.categories = kategorien
    cd.add_series(name, werte)
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf.name = name
    ch = gf.chart
    ch.has_legend = False
    ch.has_title = False
    ch.font.size, ch.font.name, ch.font.color.rgb = Pt(12), BODY, INK
    ca, va = ch.category_axis, ch.value_axis
    ca.reverse_order = True
    ca.format.line.fill.background()
    ca.has_major_gridlines = False
    va.visible = False
    va.has_major_gridlines = False
    va.minimum_scale, va.maximum_scale = 0, maximum
    plot = ch.plots[0]
    plot.gap_width = 60
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.number_format, dl.number_format_is_linked = '0.0" %"', False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.size, dl.font.bold, dl.font.color.rgb = Pt(14), True, INK
    for i, f in enumerate(farben):
        pt = plot.series[0].points[i]
        pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = f


# 1 Titel
s = new_slide("", "ZEIT 0:45. Einstieg mit der Frage: Eine Reinigungsfirma will wissen, wann der Vertrag der Stadt X endet und neu ausgeschrieben wird. Wer es früh weiß, kann sich vorbereiten. "
              "Kernbotschaft schon jetzt nennen: Wir zeigen, was geht (Liste mit Vertragsenden) und was nicht (Terminprognose), und wie sicher wir uns bei der Liste sind.", dark=True)
box(s, 0.6, 1.5, 6.2, 1.0, "Vergabe-Radar", size=48, bold=True, color=WHITE, font=HEAD, name="Titel")
box(s, 0.6, 2.6, 6.0, 1.0, "Wann laufen öffentliche Aufträge aus? Was TED-Daten verraten und was nicht", size=20, color=SOFT, name="Untertitel")
box(s, 0.6, 4.7, 7.5, 0.4, "Big Data Analytics · Leistungsnachweis B · [Namen eintragen]", size=12, color=SOFT, name="Autoren")
rect(s, 7.2, 1.4, 2.2, 2.2, TEAL, MSO_SHAPE.OVAL, "Fragezeichen Kreis")
box(s, 7.2, 1.4, 2.2, 2.2, "?", size=96, bold=True, color=WHITE, font=HEAD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, name="Fragezeichen")

# 2 Business
s = new_slide("Frage und Erfolgskriterium",
              "ZEIT 1:15. Zielgruppe: Reinigungsfirmen im Mittelstand. Entscheidung: Auf welche Ausschreibung bereite ich mich vor? Erfolgskriterium vor dem Backtest festgelegt "
              "(docs/business.md 7.1, Commit 25f7dd3): Treffer = Neuausschreibung im Fenster ±3 Monate um die Prognose, Schwelle 60 %. Baseline R0 = naive Regel. Ehrlich: Kein Kundenkontakt "
              "(Entscheidung 2026-10-29), Nachfrage und Zahlungsbereitschaft (A1, A15) sind ungeprüft. ZEIG-MIR-WO: docs/business.md Abschnitt 7.1.")
box(s, 0.5, 1.2, 9, 0.8, "Reinigungsfirmen wollen sich früh auf Neuausschreibungen vorbereiten. Eine Prognose würde ihnen Wochen Vorlauf geben.", size=18)
stat(s, 0.5, 2.2, 2.8, "60 %", "Mindest-Trefferquote im Fenster ±3 Monate (vorab festgelegt)", TEAL, "Schwelle")
stat(s, 3.6, 2.2, 2.8, "17,3 %", "naive Vergleichsregel R0 (Baseline)", GREY, "Baseline")
stat(s, 6.7, 2.2, 2.8, "0", "Kundengespräche: Nachfrage bleibt ungeprüft", RED, "Kunden")
box(s, 0.5, 4.1, 9, 0.5, "Nische: Gebäudereinigung (Haupt-CPV 90910/90911/90919), TED-Zuschläge in Deutschland", size=14, color=GREY)

# 3 Daten
s = new_slide("Daten: TED, Laufzeit oft vorhanden",
              "ZEIT 1:15. TED veröffentlicht Zuschläge der EU-weiten Vergaben. Wir nutzen eForms ab Herbst 2023 über die Search-API; Rohdaten unverändert in data/raw. Fakten: Laufzeitende bei 90,0 % der "
              "Zuschläge der Gebäudereinigung (großzügig), streng bestimmbar 80,9 %. Verlängerungsoptionen stehen aber nur bei 18,9 % im strukturierten Feld BT-58 (Annahme A5 widerlegt), der Rest im Freitext. "
              "Datensatz: 9.915 Lose, bewusst größer als der Richtwert, weil jedes Los ein Vertrag ist. QUELLE: docs/quellen.md. ZEIG-MIR-WO: reports/datenqualitaet_DEU_20260722_20261021.md.")
balken(s, 0.5, 1.2, 5.7, 3.4, ["Laufzeitende bestimmbar (großzügig)", "Laufzeitende streng bestimmbar", "Verlängerung im Feld BT-58"], [90.0, 80.9, 18.9], [TEAL, TEAL, RED], "Befüllung der Felder")
rect(s, 6.4, 1.3, 3.1, 3.2, PALE, name="Merkkasten")
box(s, 6.6, 1.5, 2.7, 2.8, [[("9.915 Lose", {"bold": True})], "aus 4.209 Zuschlägen, eForms ab 2023", "", [("Verlängerungen stehen meist im Freitext", {"bold": True})], "Lese-Regeln nötig, geprüft nur an eForms"], size=14, name="Merktext")
box(s, 0.5, 4.8, 7, 0.3, "Quelle: TED Search API v3, Stichprobe Q4 2025 bis Q3 2026", size=10, color=GREY)

# 4 Verlauf
s = new_slide("Acht Iterationen, drei Zyklen",
              "ZEIT 1:00. CRISP-DM nicht einmal linear: acht Iterationen in drei Zyklen mit Rücksprüngen. Jede endete mit einer Entscheidung gegen vorab festgelegte Schwellen: weiter, zurück zu Phase X "
              "oder Idee anpassen. Fünfmal wurde die Idee angepasst oder zurückgesprungen. ZEIG-MIR-WO: docs/iterationen.md Übersichtstabelle; Zeitaufwand 29,4 Stunden (Untergrenze, docs/zeitprotokoll.md).")
for t, x, w, f in (("Zyklus 1: Zuordnung zum Vorgänger", 0.5, 4.5, TEAL), ("Zyklus 2: Prognose", 5.1, 1.1, AMBER), ("Zyklus 3: Qualität der Liste", 6.3, 3.2, GREEN)):
    rect(s, x, 1.3, w, 0.55, f, name=t)
    box(s, x + 0.08, 1.3, w - 0.12, 0.55, t, size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
its = [("1", "Machbarkeit"), ("2", "Auftraggeber + CPV"), ("3", "Objekt-Regel"), ("4", "Letzter Versuch"), ("5", "Backtest"), ("6", "Erste Handprüfung"), ("7", "Regel 1b"), ("8", "KI-Zweitlesung")]
for i, (n, l) in enumerate(its):
    x = 0.5 + i * 1.13
    rect(s, x + 0.25, 2.2, 0.6, 0.6, TEAL, MSO_SHAPE.OVAL, "Iteration " + n)
    box(s, x + 0.25, 2.2, 0.6, 0.6, n, size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x, 2.95, 1.1, 0.6, l, size=12, align=PP_ALIGN.CENTER)
box(s, 0.5, 3.9, 9, 0.7, "Idee angepasst nach Iteration 1, 2, 4, 5; zurück zu Phase 3 nach Iteration 6; Abschluss mit Einschränkung nach 7 und 8", size=14, color=GREY)

# 5 Irrweg Zuordnung
s = new_slide("Irrweg: Neuausschreibung zuordnen",
              "ZEIT 1:30. Erster Irrweg: Wir wollten jede Neuausschreibung ihrem Vorgängervertrag zuordnen. Auftraggeber + CPV: 16,7 % (Schwelle 80 %), weil große Auftraggeber viele Verträge parallel vergeben. "
              "Objekt-Regel (Adresse, Titel): 28,9 % (Schwelle 60 %). Letzter Versuch auf neuen Testdaten: 56,7 % (Schwelle 60 %), Zweitprüfung durch den Nutzer nur 65 %. LERNPUNKT Trennung Entwicklung/Test: "
              "Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 richtig. Publikumsfrage stellen, 20 Sekunden Antworten sammeln. "
              "ZEIG-MIR-WO: reports/zuordnung_iteration3.md, reports/evaluation_iteration4.md.")
balken(s, 0.5, 1.2, 5.8, 2.9, ["Iteration 2: Auftraggeber + CPV", "Iteration 3: Objekt-Regel", "Iteration 4: letzter Versuch"], [16.7, 28.9, 56.7], [RED, RED, AMBER], "Trefferquote der Zuordnung")
box(s, 0.5, 4.15, 5.8, 0.3, "Schwellen: 80 %, 60 %, 60 %", size=12, color=GREY)
rect(s, 6.5, 1.3, 3.0, 3.0, DARK, name="Publikumsfrage Karte")
box(s, 6.7, 1.5, 2.6, 2.6, [[("Frage an euch", {"bold": True, "color": AMBER})], [("Wie oft trifft eine einfache Regel („Ende − 6 Monate“) das Fenster ±3 Monate?", {"color": WHITE})]], size=16, space=8, name="Publikumsfrage")

# 6 Backtest
s = new_slide("Backtest: die Prognose trägt nicht",
              "ZEIT 1:30. Antwort auf die Publikumsfrage: 28,8 %. Regel R1 = Höchstende − 6 Monate, getestet auf 52 von Hand bestätigten Paaren; Baseline R0 17,3 %; Schwelle 60 % vorab festgelegt. "
              "20 Neuausschreibungen kamen mehr als 3 Monate früher, 17 später: Der Termin streut zweigipflig, ein fester Abstand trägt nicht. Robust gegen Ausreißer und Vorlauf. Entscheidung: Idee anpassen, "
              "keine Terminprognose. Grenze: Paare stammen aus einer Rückwärtssuche (nur auffindbare Vorgänger), Zweitprüfung war KI-unterstützt. ZEIG-MIR-WO: reports/backtest_iteration5.md, reports/evaluation_iteration5.md.")
balken(s, 0.5, 1.2, 5.8, 2.9, ["R0: naive Referenz", "R1: Höchstende − 6 Monate", "Schwelle (vorab)"], [17.3, 28.8, 60.0], [GREY, RED, TEAL], "Trefferquote im Fenster ±3 Monate")
rect(s, 6.5, 1.3, 3.0, 3.0, PALE, name="Befund Karte")
box(s, 6.7, 1.5, 2.6, 2.6, [[("52 geprüfte Paare", {"bold": True})], "20 früher, 15 im Fenster, 17 später", "", [("Entscheidung: keine Terminprognose", {"bold": True})]], size=14, name="Befund")

# 7 Wende
s = new_slide("Neue Frage: Wann endet ein Vertrag?",
              "ZEIT 1:15. Aus dem Rückschlag wird ein anderes Produkt: Statt den Neuausschreibungstermin vorherzusagen, zeigen wir, wann ein Vertrag laut Bekanntmachung endet (Ende der Grundlaufzeit) und wie "
              "lange er höchstens verlängert werden kann. Die Liste deckt 79,7 % der Lose ab. Prototyp für die Oberpfalz: 146 Lose. Jeder Eintrag hat einen TED-Link und eine Stufe A bis F (Herkunft der Angabe). "
              "Keine Prognose. ZEIG-MIR-WO: reports/beispiel_liste.md, src/report/beispiel_liste.py.")
zeilen = [("Ende Grundlaufzeit (laut Bekanntmachung)", "Höchstende (nur Hinweis)", "Auftraggeber", "Stufe", "Quelle"),
          ("31.07.2027", "31.07.2029", "Stadt Regensburg", "A", "271497-2025"),
          ("14.09.2027", "14.09.2029", "Stadt Regensburg", "A", "570596-2025")]
tbl = s.shapes.add_table(3, 5, Inches(0.5), Inches(1.3), Inches(9), Inches(1.4))
tbl.name = "Beispielliste"
for c, w in enumerate((2.6, 2.0, 1.9, 0.7, 1.8)):
    tbl.table.columns[c].width = Inches(w)
for r, zeile in enumerate(zeilen):
    for c, wert in enumerate(zeile):
        cell = tbl.table.cell(r, c)
        cell.text = wert
        para = cell.text_frame.paragraphs[0]
        para.runs[0].font.size, para.runs[0].font.name = Pt(12), BODY
        para.runs[0].font.bold = r == 0
        para.runs[0].font.color.rgb = WHITE if r == 0 else INK
        cell.fill.solid()
        cell.fill.fore_color.rgb = TEAL if r == 0 else PALE
stat(s, 0.5, 3.1, 2.8, "79,7 %", "der Lose mit bestimmbarem Ende", TEAL, "Abdeckung")
stat(s, 3.6, 3.1, 2.8, "146", "Lose im Prototyp (Oberpfalz)", TEAL, "Lose")
stat(s, 6.7, 3.1, 2.8, "A–F", "Stufe je Eintrag: woher stammt die Angabe", AMBER, "Stufe")

# 8 Qualität messen
s = new_slide("Wie genau ist die Liste? Drei Messungen",
              "ZEIT 1:45. Wichtigste Folie zur Einordnung. Drei Messungen, drei verschiedene Dinge: Iteration 6, Handprüfung von 60 Zufallslosen, aber die Vorlage zeigte den Listenwert (Verankerung): 88,3 %. "
              "Iteration 7, Handprüfung ohne Listenwerte, Nachprüfung im Original: 76,6 %, ein Mischmaß aus Listenfehlern und Prüfungsfehlern (Felder abgeschrieben). Iteration 8, zwei KI-Leser (Opus, Sonnet): "
              "77 von 80, 96,2 %. Wichtig: Die Zahlen sind NICHT vergleichbar und keine davon ist eine belastbare Fehlerquote. Alle Schwellen standen vorab fest. "
              "ZEIG-MIR-WO: reports/evaluation_iteration6.md, 7, 8.")
balken(s, 0.5, 1.2, 5.7, 3.0, ["Iteration 6: Hand, Listenwert sichtbar", "Iteration 7: Hand, ohne Listenwert", "Iteration 8: zwei KI-Leser"], [88.3, 76.6, 96.2], [AMBER, RED, TEAL], "Ende der Grundlaufzeit stimmt")
rect(s, 6.4, 1.3, 3.1, 3.3, PALE, name="Schwächen Karte")
box(s, 6.6, 1.5, 2.7, 3.0, [[("Jede Messung hat eine Schwäche", {"bold": True})], "6: verankert", "7: Mischmaß aus Listen- und Prüffehlern", "8: Leser nicht unabhängig", "", [("Eine belastbare Fehlerquote bleibt offen", {"bold": True})]], size=14, space=4, name="Schwächen")
box(s, 0.5, 4.4, 5.7, 0.3, "Schwelle jeweils 90 %; Iteration 7 mit gekürzter Stichprobe (47 Lose)", size=11, color=GREY)

# 9 KI-Irrwege
s = new_slide("KI-Irrwege, die wir gefunden haben",
              "ZEIT 1:30. Claude Code hat Regeln, Stichproben und Auswertungen mitgebaut. Vier Beispiele aus docs/ki_irrwege.md (19 Einträge): (1) Prüfer und Regel stammen von derselben Hand: gefunden vom Evaluator "
              "in Iteration 2, Folge: Handsuche durch getrennten Subagenten. (2) Entwicklung 10–11 von 12 plausibel, im Test 11 von 24: gefunden im Test, Folge: Regel verworfen. (3) Felder in der Vorlage versteckt, "
              "damit nichts verankert; dadurch 65 von 95 Einträge „unbekannt“ (Y1 zunächst 25 %): gefunden in der Auswertung, Folge: Nachprüfung im Original. (4) Leser „blind“ genannt, hatten aber die "
              "Projektbeschreibung im Kontext: gefunden vom Evaluator, Folge: offen im Ergebnis genannt. Kernpunkt: Ein eigener Subagent (Evaluator) prüft jede Iteration kritisch. ZEIG-MIR-WO: docs/ki_irrwege.md.")
items = [("Prüfer und Regel von derselben Hand", "Gefunden vom Evaluator (It. 2). Folge: Handsuche durch getrennten Agenten."),
         ("Entwicklung gut, Test schlecht", "10–11 von 12 plausibel, im Test 11 von 24 richtig (It. 3). Folge: Regel verworfen."),
         ("Versteckte Felder", "65 von 95 Einträge „unbekannt“, Y1 zunächst 25 % (It. 7). Folge: Nachprüfung im Original."),
         ("„Blind“ war nicht blind", "Leser hatten die Projektbeschreibung im Kontext (It. 8). Folge: offen berichtet.")]
for i, (h, t) in enumerate(items):
    x, y = 0.5 + (i % 2) * 4.6, 1.3 + (i // 2) * 1.8
    rect(s, x, y, 4.4, 1.6, PALE, name=f"Irrweg {i + 1}")
    box(s, x + 0.2, y + 0.12, 4.0, 0.4, h, size=16, bold=True, color=DARK)
    box(s, x + 0.2, y + 0.6, 4.0, 0.9, t, size=14)

# 10 Trennung Entwicklung/Test
s = new_slide("Trennung von Entwicklung und Test",
              "ZEIT 1:00. LIVE-NACHWEIS (Fragenrunde vorbereiten): Regel 1b und der Seed 20261106 wurden VOR dem Ziehen der Stichprobe committet (Commits 7d42a55, c7fb0c0, dann a87dc1f). Der Schlüssel der "
              "Stichprobe liegt lokal, sein SHA-256 steht im Commit (eade66c0…). Entwicklungsfälle (L1, L42, L43, L60) und angesehene Bekanntmachungen sind aus der Stichprobe ausgeschlossen. Kriterien Z0 bis Z4 "
              "der Iteration 8 vor dem Lauf committet (6fe4e38), Auswertungsskript vor den Antworten (9645fa8). ZEIG-MIR-WO: git log --oneline, .git/logs/HEAD, src/prepare/stichprobe_iteration7.py. "
              "Ehrlich: Die Leser kannten den Fehlertyp.")
for i, (h, c) in enumerate((("Regel und Seed committen", "7d42a55, c7fb0c0"), ("Stichprobe ziehen", "a87dc1f, Hash des Schlüssels"), ("Prüfen ohne Listenwerte", "Vorlage ohne Ende-Spalte"), ("Auswerten gegen vorab Schwellen", "Y1–Y4, Z0–Z4"))):
    x = 0.5 + i * 2.3
    rect(s, x, 1.5, 2.1, 2.3, PALE, name=f"Schritt {i + 1}")
    rect(s, x + 0.15, 1.65, 0.5, 0.5, TEAL, MSO_SHAPE.OVAL, f"Nummer {i + 1}")
    box(s, x + 0.15, 1.65, 0.5, 0.5, str(i + 1), size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.15, 2.3, 1.8, 0.8, h, size=14, bold=True)
    box(s, x + 0.15, 3.2, 1.8, 0.5, c, size=11, color=GREY)
box(s, 0.5, 4.2, 9, 0.4, "Nachweis in der Fragenrunde: git log und die Reihenfolge der Commits", size=14, color=GREY)

# 11 Empfehlung und Grenzen
s = new_slide("Empfehlung und Grenzen",
              "ZEIT 1:15. Ampel statt Fazit-Folie voller Text. GRÜN: Die Liste ist als Ausgangspunkt nutzbar, immer mit Blick in die verlinkte Bekanntmachung; 77 von 80 Zufallslosen stimmen mit zwei KI-Lesungen "
              "überein. GELB: Höchstende nur Hinweis; Schuljahres-Verträge (Landkreis Börde) nicht tagesgenau; Lose ohne Zuschlag (L69, L72) und Übertragung von Einzelwerten auf andere Lose (L81) stecken in der Liste; "
              "Leser nicht unabhängig. ROT: Terminprognose, „die Liste ist korrekt“, Nachfrage und Zahlungsbereitschaft. Transferfrage vorbereiten: andere Nische = gleiche Pipeline, aber Lese-Regeln neu testen; "
              "doppeltes Volumen = Abruf und Prüfung skalieren, menschliche Prüfung nicht. ZEIG-MIR-WO: docs/annahmen.md, reports/evaluation_iteration8.md.")
ampel = (("Ja", GREEN, ["Liste „laut Bekanntmachung“ als Ausgangspunkt", "Link zur Bekanntmachung prüfen", "77 von 80 durch KI-Lesung gestützt"]),
         ("Mit Vorsicht", AMBER, ["Höchstende nur als Hinweis", "Schuljahres-Verträge nicht tagesgenau", "Lose ohne Zuschlag, Zuordnungsfehler"]),
         ("Nein", RED, ["Terminprognose", "„Die Liste ist korrekt“", "Nachfrage und Preis (nicht geprüft)"]))
for i, (h, f, pts) in enumerate(ampel):
    x = 0.5 + i * 3.1
    rect(s, x, 1.3, 2.9, 3.3, PALE, name=h + " Karte")
    rect(s, x + 0.2, 1.45, 0.4, 0.4, f, MSO_SHAPE.OVAL, h + " Signal")
    box(s, x + 0.75, 1.45, 2.0, 0.4, h, size=18, bold=True, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 2.1, 2.5, 2.3, ["• " + p for p in pts], size=14, space=8)

# 12 Fazit
s = new_slide("", "ZEIT 0:45. Kernbotschaft in einem Satz wiederholen, dann Brücke zur Fragenrunde. Gesamtzeit: 15:00 (Ziel ±30 Sekunden). Fragenrunde: Methodenfrage (warum ±3 Monate, warum diese Baseline), "
              "Live-Nachweis (git log, Regel in src/prepare/vertragsliste.py öffnen), Transferfrage (andere Nische, doppeltes Volumen).", dark=True)
box(s, 0.6, 0.6, 8.8, 0.8, "Fazit", size=36, bold=True, color=AMBER, font=HEAD, name="Fazit Titel")
box(s, 0.6, 1.6, 8.6, 1.9, "Den Termin einer Neuausschreibung sagen TED-Daten nicht vorher (28,8 % statt 60 %). Brauchbar ist eine Liste, wann Verträge laut Bekanntmachung enden. "
    "Wie genau sie ist, bleibt offen: Hand- und KI-Prüfung stützen sie, ohne sie zu beweisen.", size=22, color=WHITE, name="Kernbotschaft")
box(s, 0.6, 3.9, 8.6, 0.9, [[("Nächster Schritt: ", {"bold": True, "color": AMBER}), ("menschliche Zweitlesung der Problemgruppen und ein Gespräch mit zwei bis drei Reinigungsfirmen", {"color": SOFT})]], size=16, name="Nächster Schritt")

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(len(prs.slides), "Folien;", OUT)
