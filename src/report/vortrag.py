"""Foliengerüst für den Vortrag (LN B: 15 min, höchstens 12 Folien) mit Sprechernotizen.

Stand nach Iteration 10 und 10b (Business Understanding mit Konkurrenz, Gesprächen und Vergleich mit Vergabeweiser).
Zahlen aus docs/iterationen.md, docs/business.md §8, reports/evaluation_iteration5.md bis 10b, reports/wettbewerbsbild_oberpfalz.md.
Jede Folie hat Notizen: ZEIT, KERNAUSSAGE, ZEIG-MIR-WO (Summe der Zeiten 15:00).
Aufruf:  .venv\\Scripts\\python.exe -I src/report/vortrag.py      Ausgabe: docs/vortrag/vortrag_vergabe_radar.pptx
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
    """Textfeld. paras: str oder Liste von Absätzen; ein Absatz ist str oder Liste von (Text, {bold, color})."""
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
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = HEAD, Pt(28), True, DARK
    box(s, 9.1, 5.2, 0.5, 0.3, str(_nr[0]), size=10, color=SOFT if dark else GREY, align=PP_ALIGN.RIGHT, name="Foliennummer")
    s.notes_slide.notes_text_frame.text = notes
    return s


def stat(s, x, y, w, zahl, label, farbe, name, h=1.5, zsize=34, lsize=13):
    rect(s, x, y, w, h, PALE, name=name + " Karte")
    box(s, x + 0.15, y + 0.08, w - 0.3, 0.6, zahl, size=zsize, bold=True, color=farbe, font=HEAD, name=name + " Zahl")
    box(s, x + 0.15, y + 0.72, w - 0.3, h - 0.78, label, size=lsize, name=name + " Text")


def balken(s, x, y, w, h, kategorien, werte, farben, name, maximum=118, fmt='0.0" %"'):
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
    dl.number_format, dl.number_format_is_linked = fmt, False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.size, dl.font.bold, dl.font.color.rgb = Pt(14), True, INK
    for i, f in enumerate(farben):
        pt = plot.series[0].points[i]
        pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = f


# 1 Titel -------------------------------------------------------------------------------------------
s = new_slide("", "ZEIT 0:45. KERNAUSSAGE: Eine Reinigungsfirma will früh wissen, wann ein öffentlicher Vertrag endet und neu ausgeschrieben wird. Wir zeigen, was TED-Daten dazu hergeben "
              "(eine Liste der Vertragsenden), was nicht (eine Terminprognose), und was an der Idee gegenüber der kostenlosen Konkurrenz übrig bleibt. "
              "Ablauf in einem Satz: Frage, zwei Irrwege, eine Liste, ihre Genauigkeit, dann der Rücksprung zur Frage, ob jemand das braucht und ob es das schon gibt. "
              "Kernbotschaft schon jetzt nennen: Die Liste lässt sich aus TED lesen, ein eigenes Produkt ist sie nicht, und ein Qualitätsvorsprung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/iterationen.md (Übersicht und Ergebnis Iteration 10 und 10b).", dark=True)
box(s, 0.6, 1.5, 6.2, 1.0, "Vergabe-Radar", size=48, bold=True, color=WHITE, font=HEAD, name="Titel")
box(s, 0.6, 2.6, 6.0, 1.2, "Wann laufen öffentliche Aufträge aus, und wer weiß es schon? Was TED-Daten verraten, wer mitspielt und was bleibt", size=20, color=SOFT, name="Untertitel")
box(s, 0.6, 4.7, 7.5, 0.4, "Big Data Analytics · Leistungsnachweis B · [Namen eintragen]", size=12, color=SOFT, name="Autoren")
rect(s, 7.2, 1.4, 2.2, 2.2, TEAL, MSO_SHAPE.OVAL, "Fragezeichen Kreis")
box(s, 7.2, 1.4, 2.2, 2.2, "?", size=96, bold=True, color=WHITE, font=HEAD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, name="Fragezeichen")

# 2 Frage, Kriterium, Daten ----------------------------------------------------------------------------
s = new_slide("Frage, Erfolgskriterium, Daten",
              "ZEIT 1:15. KERNAUSSAGE: Die Frage hatte eine Entscheidung (auf welche Ausschreibung bereite ich mich vor?) und eine vorab festgelegte Schwelle. "
              "Zielgruppe: Reinigungsfirmen im Mittelstand, Nische Gebäudereinigung (Haupt-CPV 90910/90911/90919). Annahme: Wer früh weiß, wann ein Vertrag endet, kann Personal und Angebot vorbereiten (A1, A15). "
              "Erfolgskriterium vor dem Backtest festgelegt (docs/business.md 7.1): Treffer = Neuausschreibung im Fenster ±3 Monate um die Prognose, Schwelle 60 %; Baseline R0 = naive Regel 17,3 %. "
              "Daten: TED Search API, eForms-Zuschläge ab Okt. 2023, Rohdaten unverändert in data/raw (nicht im Git, Abruf-Skript und Parameter in docs/reproduzierbarkeit.md). "
              "9.325 Lose aus 4.011 Zuschlägen, im Richtwert von 200 bis 10.000 Zeilen; jedes Los ist ein Vertrag. "
              "Laufzeitende bei 90,0 % der Zuschläge bestimmbar (großzügig); Verlängerungsoptionen nur bei 18,9 % im Feld BT-58, der Rest im Freitext (Annahme A5 widerlegt). "
              "Die Zuordnung und die Datenqualität sind hier verdichtet; Details bei Rückfragen. Ehrlich: Zu diesem Zeitpunkt gab es keinen Kundenkontakt; das holen wir auf Folie 6 nach. "
              "ZEIG-MIR-WO: docs/business.md Abschnitt 7.1, reports/datenqualitaet_DEU_20260722_20261021.md, docs/quellen.md.")
box(s, 0.5, 1.1, 9, 0.9, "Reinigungsfirmen wollen sich früh auf Neuausschreibungen vorbereiten. Entscheidung: Auf welche Ausschreibung stelle ich Personal und Angebot ein?", size=17)
stat(s, 0.5, 2.1, 2.8, "60 %", "Mindest-Trefferquote der Terminprognose, Fenster ±3 Monate (vorab festgelegt)", TEAL, "Schwelle")
stat(s, 3.6, 2.1, 2.8, "17,3 %", "naive Vergleichsregel R0 (Baseline)", GREY, "Baseline")
stat(s, 6.7, 2.1, 2.8, "9.325", "Lose aus 4.011 TED-Zuschlägen der Gebäudereinigung (eForms ab Okt. 2023)", TEAL, "Daten")
box(s, 0.5, 3.8, 9, 0.8, "Laufzeitende steht bei 90,0 % der Zuschläge im Feld; Verlängerungsoptionen nur bei 18,9 % strukturiert, der Rest im Freitext. Annahme „früher wissen hilft“ war noch ungeprüft.", size=14, color=GREY)
box(s, 0.5, 4.85, 8, 0.3, "Quelle: TED Search API v3 (docs/quellen.md), Zuschläge mit Veröffentlichung Q4 2025 bis Q3 2026", size=10, color=GREY)

# 3 Irrwege Zuordnung und Terminprognose ----------------------------------------------------------------
s = new_slide("Irrwege: Zuordnung, Terminprognose",
              "ZEIT 1:45. KERNAUSSAGE: Zwei Ideen sind an vorab festgelegten Schwellen gescheitert, und das haben wir so berichtet. "
              "PUBLIKUMSFRAGE (vorher, bevor jemand den vierten Balken erklärt bekommt; Folie 2 offen lassen, dann klicken): „Wie oft trifft die einfache Regel ‚Höchstende minus 6 Monate‘ den Neuausschreibungstermin im Fenster ±3 Monate? Schätzt: unter 20 %, 20–40 %, 40–60 % oder über 60 %?“ 20 Sekunden, Handzeichen. Antwort: 28,8 %. "
              "IRRWEG 1 (Iteration 2 bis 4): Jede Neuausschreibung dem Vorgängervertrag zuordnen. Auftraggeber + CPV 16,7 % (Schwelle 80 %), weil große Auftraggeber viele Verträge parallel vergeben; Objekt-Regel (Adresse, Titel) 28,9 % (Schwelle 60 %); letzter Versuch auf neuen Testdaten 56,7 % (Schwelle 60 %), die Zweitprüfung durch den Nutzer 65 %. Lernpunkt Trennung Entwicklung/Test: Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 richtig. "
              "IRRWEG 2 (Iteration 5, Backtest): R1 = Höchstende − 6 Monate auf 52 von Hand bestätigten Paaren: 28,8 %; R0 17,3 %; Schwelle 60 %. 20 Neuausschreibungen kamen mehr als 3 Monate früher, 15 im Fenster, 17 später; der Termin streut zweigipflig. Entscheidung: Idee anpassen, keine Terminprognose. Grenzen: Paare aus einer Rückwärtssuche (nur auffindbare Vorgänger), Zweitprüfung KI-unterstützt. "
              "FRAGE-VORBEREITUNG Methodenfrage („Warum ±3 Monate, warum diese Baseline?“): Das Fenster wurde vor der Rechnung gesetzt, weil ein Betrieb für Personal und Angebot grob ein Vierteljahr Spielraum braucht; die naive Regel R0 zeigt, was Zufall und Streuung allein schaffen; die Schwelle 60 % war eine Setzung ohne Kundenkontakt. Alternative wäre ein Fenster ±6 Monate, das wäre aber für die Entscheidung zu unscharf. "
              "ZEIG-MIR-WO: reports/zuordnung_iteration3.md, reports/evaluation_iteration4.md, reports/backtest_iteration5.md, reports/evaluation_iteration5.md.")
balken(s, 0.5, 1.15, 5.8, 3.2, ["Zuordnung: Auftraggeber + CPV", "Zuordnung: Objekt-Regel", "Zuordnung: letzter Versuch", "Terminprognose R1 (Backtest)"],
       [16.7, 28.9, 56.7, 28.8], [RED, RED, AMBER, RED], "Trefferquote gegen Schwelle")
box(s, 0.5, 4.4, 5.8, 0.5, "Schwellen vorab: 80 %, 60 %, 60 %, 60 %. Baseline der Prognose R0: 17,3 %", size=12, color=GREY)
rect(s, 6.5, 1.3, 3.0, 3.0, DARK, name="Publikumsfrage Karte")
box(s, 6.7, 1.5, 2.6, 2.6, [[("Frage an euch", {"bold": True, "color": AMBER})], [("Wie oft trifft „Höchstende − 6 Monate“ den Neuausschreibungstermin im Fenster ±3 Monate?", {"color": WHITE})], [("Schätzt: unter 20 %, 20–40 %, 40–60 %, über 60 %", {"color": SOFT, "size": 13})]], size=16, space=8, name="Publikumsfrage")

# 4 Wende: Liste der Vertragsenden ---------------------------------------------------------------------------
s = new_slide("Neue Frage: Wann endet ein Vertrag?",
              "ZEIT 1:00. KERNAUSSAGE: Aus dem Rückschlag wird eine andere Frage: nicht „wann wird neu ausgeschrieben?“, sondern „wann endet ein Vertrag laut Bekanntmachung?“. "
              "Die Liste zeigt je Los das Ende der Grundlaufzeit, das Höchstende nur als Hinweis, den Auftraggeber, einen TED-Link und eine Stufe A bis F (woher die Angabe stammt; F = kein Ende bestimmbar). "
              "Die Liste (Fassung der Iteration 9) hat 9.325 Lose; ein Datum liefert sie für 79,4 % der Lose (2.783 von 3.503, Zuschläge 10/2025 bis 9/2026; Schwelle 80 % knapp verfehlt). Prototyp Oberpfalz: 130 Lose, davon 33 ohne Ende (Stufe F, keine Laufzeitfelder im XML). "
              "Streifen unten: vier Zyklen CRISP-DM, jeder endete mit einer Entscheidung gegen vorab festgelegte Schwellen: Zuordnung (Iteration 1 bis 4), Prognose (5), Qualität der Liste (6 bis 9), Business Understanding (10 und 10b). Zyklus 4 ist der Rücksprung in Phase 1. "
              "ZEIG-MIR-WO: reports/beispiel_liste.md, reports/beispiel_liste_oberpfalz.csv, src/report/beispiel_liste.py, docs/iterationen.md Übersichtstabelle.")
zeilen = [("Ende Grundlaufzeit (laut Bekanntmachung)", "Höchstende (nur Hinweis)", "Auftraggeber", "Stufe", "Quelle"),
          ("14.09.2027", "14.09.2029", "Stadt Regensburg", "A", "570596-2025"),
          ("31.08.2028", "31.08.2030", "REWAG Regensburg", "A", "622498-2025")]
tbl = s.shapes.add_table(3, 5, Inches(0.5), Inches(1.15), Inches(9), Inches(1.2))
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
stat(s, 0.5, 2.55, 2.8, "9.325", "Lose in der Liste (Fassung 9)", TEAL, "Lose", h=1.4, zsize=34, lsize=12)
stat(s, 3.6, 2.55, 2.8, "79,4 %", "der Lose mit Datum (2.783 von 3.503)", TEAL, "Abdeckung", h=1.4, zsize=34, lsize=12)
stat(s, 6.7, 2.55, 2.8, "A–F", "Stufe je Eintrag: woher stammt die Angabe", AMBER, "Stufe", h=1.4, zsize=34, lsize=12)
for t, x, w, f in (("Zyklus 1: Zuordnung (It. 1–4)", 0.5, 3.2, TEAL), ("Zyklus 2: Prognose (It. 5)", 3.75, 1.4, AMBER),
                   ("Zyklus 3: Qualität der Liste (It. 6–9)", 5.2, 2.5, GREEN), ("Zyklus 4: Business (It. 10)", 7.75, 1.75, RED)):
    rect(s, x, 4.25, w - 0.05, 0.6, f, name=t)
    box(s, x + 0.06, 4.25, w - 0.17, 0.6, t, size=10, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)

# 5 Genauigkeit ------------------------------------------------------------------------------------------
s = new_slide("Wie genau ist die Liste?",
              "ZEIT 1:15. KERNAUSSAGE: Vier Messungen messen vier verschiedene Dinge; keine ist eine belastbare Fehlerquote. "
              "Iteration 6: Handprüfung von 60 Zufallslosen, aber die Vorlage zeigte den Listenwert (Verankerung): 88,3 %. Iteration 7: Handprüfung ohne Listenwerte, Nachprüfung im Original: 76,6 %, ein Mischmaß aus Listen- und Prüfungsfehlern (Felder abgeschrieben). "
              "Iteration 8: zwei KI-Leser (Opus, Sonnet) auf allen 95 Losen: 77 von 80 = 96,2 %, Leser nicht unabhängig. Iteration 9: neue Stichprobe (Seed 20261109), Rohtext ohne Projektkontext, überarbeitete Liste: 66 von 70 = 94,3 %, Kommilitone 14 von 15; Höchstende 87,1 % (Schwelle 90 % verfehlt). "
              "Alle Schwellen standen vorab fest; der Vergleichswert ist teilweise zirkulär (Liste und Vergleich nutzen dasselbe TED-Feld). Die alte Fassung der Liste erreicht auf denselben Losen 65 von 70: Der Nutzen der neuen Regeln ist kaum gesichert. "
              "FRAGE-VORBEREITUNG Methodenfrage („Warum Übereinstimmung mit KI-Lesern als Maß, was wäre die Alternative?“): Es gibt keine Wahrheitsquelle außer dem Bekanntmachungstext; Handprüfung ist teuer und hatte Verankerung (It. 6) und Abschreibefehler (It. 7), deshalb zusätzlich KI-Leser mit neutraler Definition „erste feste Laufzeit ohne Optionen“. Alternative: mehr Menschen als Leser; fehlt noch. "
              "ZEIG-MIR-WO: reports/evaluation_iteration6.md, 7, 8, 9.")
balken(s, 0.5, 1.15, 5.7, 3.0, ["Iteration 6: Hand, Listenwert sichtbar", "Iteration 7: Hand, ohne Listenwert", "Iteration 8: zwei KI-Leser", "Iteration 9: KI-Leser, neue Stichprobe"],
       [88.3, 76.6, 96.2, 94.3], [AMBER, RED, TEAL, TEAL], "Ende der Grundlaufzeit stimmt")
rect(s, 6.4, 1.3, 3.1, 3.3, PALE, name="Schwächen Karte")
box(s, 6.6, 1.45, 2.7, 3.0, [[("Jede Messung hat eine Schwäche", {"bold": True})], "6: verankert", "7: Mischmaß aus Listen- und Prüffehlern", "8: Leser nicht unabhängig", "9: Vergleichswert teils zirkulär, Mensch nur 14/15", "", [("Eine belastbare Fehlerquote bleibt offen", {"bold": True})]], size=13, space=3, name="Schwächen")
box(s, 0.5, 4.3, 5.7, 0.5, "Schwelle jeweils 90 %; Iteration 7 mit gekürzter Stichprobe (47 Lose); Iteration 9: 70 Zufallslose", size=11, color=GREY)

# 6 Business: Wettbewerb und Gespräche -----------------------------------------------------------------
s = new_slide("Zurück zur Frage: Wer macht das?",
              "ZEIT 1:45. KERNAUSSAGE: Wir kehren ins Business Understanding zurück, das wir zu knapp behandelt hatten: Wie finden Betriebe Aufträge, wer bietet die Funktion schon an, wofür würde jemand zahlen? "
              "WETTBEWERB (Fakten, von uns am 2026-11-05 nachgelesen): Vergabeweiser, kostenlos, listet 1.005 Gebäudereinigungs-Verträge, die in 12 Monaten enden, mit Zuschlagsempfänger, Zahl der Angebote und Verlängerungsoptionen, ober- und unterschwellig. AusschreibungsRadar: 0 bis 149 € im Monat, mit geschätztem Ausschreibungsmonat. Beide schreiben selbst, dass der Auftraggeber über die Neuausschreibung entscheidet. "
              "DREI GESPRÄCHE (Nutzer, 9 Anrufe, 3 erreicht, 105 Minuten; Notizen ohne Namen; n = 3, Hinweise, keine Belege): Betrieb mit etwa 120 Beschäftigten nutzt ein Portal-Abo (knapp 1.500 € im Jahr), Entscheidung zum Mitbieten „hauptsächlich Entfernung und Personal“, Vertragsenden „eine Blackbox“; würde zahlen für alte Preise und aktuellen Auftragnehmer, Enddaten seien „nett für die Planung“. Kleinbetrieb (15 Beschäftigte): sucht auf Webseiten und in der Zeitung, zahlt „für gar nichts in dem Bereich“, kennt Vergabeweiser nicht. Vergabestelle (Landratsamt): Verlängern „fast immer, wenn eine Option im Vertrag steht“; „sehr oft“ unterhalb der EU-Schwelle (also nicht auf TED); zuletzt nur zwei Bieter. "
              "EHRLICH: Die Suche am 24.10. fand die Konkurrenz nicht; das war ein Versäumnis im Business Understanding (docs/ki_irrwege.md), die Iterationen 5 bis 9 arbeiteten an etwas, das es kostenlos schon gibt. Grenze: Zielgruppe „Mittelstand“ ist enger als gedacht, die Aussagen stammen von einem Betrieb mit Abo, einem Kleinbetrieb, einer Vergabestelle. "
              "TRANSFERFRAGE „Warum nicht einfach Vergabeweiser nutzen?“ Antwort: Doch, für die Suche nach Vertragsenden spricht vieles dafür: kostenlos, mehr Abdeckung (auch unterhalb der EU-Schwelle), Zuschlagsempfänger und Bieterzahl. Unsere Liste ist als eigenes Produkt nicht tragfähig; was bleibt, steht auf Folie 8. "
              "ZEIG-MIR-WO: docs/business.md §8.2 (Wettbewerber), §8.8 (Leitfaden), §8.9 (Gespräche), reports/nebentest_ausschreibungsradar.md, docs/annahmen.md (A1, A2, A15).")
spalten = (("So gehen Betriebe vor", TEAL, ["Suche: Portal-Abo (knapp 1.500 € im Jahr) oder Webseiten und Zeitung", "Mitbieten? „Hauptsächlich Entfernung und Personal“", "Vertragsenden: „eine Blackbox“"]),
           ("Wettbewerb gibt es", RED, ["Vergabeweiser: kostenlos, 1.005 Reinigungsverträge mit Ende, Zuschlagsempfänger, Bieterzahl", "AusschreibungsRadar: 0–149 € im Monat", "Beide Betriebe: kaum bekannt, nicht genutzt"]),
           ("Zahlungsbereitschaft", AMBER, ["Gesucht: alte Preise und aktueller Auftragnehmer", "Enddaten: „nett für die Planung“", "Kleinbetrieb: „für gar nichts“"]))
for i, (h, f, pts) in enumerate(spalten):
    x = 0.5 + i * 3.1
    rect(s, x, 1.15, 2.9, 2.95, PALE, name=h + " Karte")
    rect(s, x, 1.15, 2.9, 0.08, f, name=h + " Streifen")
    box(s, x + 0.15, 1.3, 2.6, 0.4, h, size=16, bold=True, color=DARK)
    box(s, x + 0.15, 1.8, 2.6, 2.25, ["• " + p for p in pts], size=12, space=5, name=h + " Text")
rect(s, 0.5, 4.25, 9.0, 0.75, DARK, name="Banner")
box(s, 0.65, 4.25, 8.7, 0.75, [[("Ehrlich: ", {"bold": True, "color": AMBER}), ("Die Konkurrenz sahen wir erst in Iteration 10 (die Suche vom 24.10. fand sie nicht). n = 3 Gespräche: Hinweise, keine Belege.", {"color": WHITE})]], size=13, anchor=MSO_ANCHOR.MIDDLE, name="Banner Text")

# 7 Vergleich mit Vergabeweiser -------------------------------------------------------------------------
s = new_slide("Vergleich mit Vergabeweiser",
              "ZEIT 1:45. KERNAUSSAGE: Wir haben vorab festgelegt und dann geprüft, ob unsere Liste das Ende der Grundlaufzeit häufiger trifft als Vergabeweiser. Ergebnis: Es gibt einen Unterschied in rund 10 % der Lose, aber er ist überwiegend eine Frage der Definition und der Losebene, kein belegter Qualitätsvorteil. "
              "ITERATION 10 (70 Zufallslose der Iteration 9): Liste 66/70, Vergabeweiser 58/70, Differenz +8 (Schwelle ≥ 5), exakter Test p = 0,0078, formal erfüllt. Ursachen der 8: Losebene 4, Höchstende statt Grundlaufzeit 2, fehlender Wert 1, 2 Tage 1. "
              "ITERATION 10b (neue Stichprobe, 160 Lose, Seed 20261112): Vergabeweiser hat alle 160, 145 gleich, 15 diskordant. Zwei KI-Leser (Opus, Sonnet) lesen ohne Quellenangabe und stimmen bei 15 von 15 überein; die Liste entspricht ihrem Wert in 15 von 15. Einordnung des Evaluators: Höchstende 7 (alle mit derselben Textvorlage, effektiv ein Mechanismus), Losebene 4, Zuordnungsfehler unserer Pipeline 1, Abweichung bei Vergabeweiser mit offener Ursache 2, mehrdeutig 1. "
              "VORAB-KRITERIEN OFFEN: W8a (Vorsprung ≥ 16 Lose) war rechnerisch unerreichbar, weil nur 15 Lose diskordant waren; das war unser Fehler bei der Festlegung (docs/ki_irrwege.md). Er wurde nicht nachträglich geändert; W8a gilt als formal verfehlt. W8b (Losebene als richtig für Vergabeweiser, ≥ 8 Lose) ist erfüllt (+10, p = 0,002). Sensitivität: Zählt auch das Höchstende als richtig für Vergabeweiser, bleiben 3 zu 0 (p = 0,25), also nichts Belegtes. "
              "Zusammen: nur die Liste richtig bei 23 von 230 = 10,0 % (Wilson etwa 6,8–14,6 %). "
              "ZULÄSSIGER SATZ: „Auf zwei Stichproben weicht Vergabeweisers Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt; in 10b waren 11 von 15 dieser Fälle Höchstende oder Losebene.“ NICHT sagen: „genauer“, „Vergabeweiser liest falsch“, „kein Unterschied“. "
              "GRENZEN: Liste und Vergabeweiser nutzen dasselbe TED-Feld, gemeinsame Fehler sind unsichtbar (bei einem von 10 übereinstimmenden Losen lagen beide falsch); Leser und Regeln aus derselben Modellfamilie; keine menschliche Gegenlesung der 15; nur Lose oberhalb der EU-Schwelle. "
              "FRAGE-VORBEREITUNG Methodenfrage: „Warum nur die diskordanten Lose lesen?“ Weil die übereinstimmenden die Differenz nicht ändern; absolute Genauigkeit der Liste ist damit nicht belegt. "
              "ZEIG-MIR-WO: reports/vergleich_iteration10.md, reports/vergleich_iteration10b.md, reports/evaluation_iteration10b.md, src/prepare/vergleich_iteration10b.py.")
stat(s, 0.5, 1.15, 2.9, "66 : 58", "n = 70 (It. 10): richtiges Ende, Liste : Vergabeweiser", TEAL, "Iteration 10", h=1.25, zsize=28, lsize=12)
stat(s, 0.5, 2.5, 2.9, "15 von 160", "n = 160 (It. 10b): Liste und Vergabeweiser weichen ab", TEAL, "Iteration 10b", h=1.25, zsize=28, lsize=12)
stat(s, 0.5, 3.85, 2.9, "≈ 10 %", "der Lose: nur die Liste richtig (23 von 230)", AMBER, "Zusammen", h=1.25, zsize=28, lsize=12)
box(s, 3.7, 1.1, 5.8, 0.35, "Die 15 abweichenden Lose in 10b (Einordnung des Evaluators)", size=13, bold=True, color=DARK)
balken(s, 3.6, 1.45, 5.9, 2.5, ["Höchstende statt Grundlaufzeit", "Losebene", "Abweichung, Ursache offen", "Zuordnungsfehler (unsere Pipeline)", "mehrdeutig"],
       [7, 4, 2, 1, 1], [AMBER, AMBER, GREY, GREY, GREY], "Ursachen der 15 abweichenden Lose", maximum=10, fmt='0')
box(s, 3.7, 4.05, 5.8, 1.0, [[("Kein Beleg für bessere Lesequalität: ", {"bold": True}), ("gleiche TED-Quelle, Leser aus einer Modellfamilie, kein Mensch. Vorab-Schwelle W8a (≥ 16 Lose) war bei 15 abweichenden Losen unerreichbar: unser Fehler, offen berichtet.", {})]], size=12, name="Grenzen Vergleich")

# 8 Competitive Edge und Positionierung ---------------------------------------------------------------------
s = new_slide("Competitive Edge: Was bleibt?",
              "ZEIT 1:30. KERNAUSSAGE: Von der Idee bleibt ein Merkmalsunterschied, kein belegter Vorsprung und kein belegter Markt. "
              "WAS BLEIBT (Fakten): (1) Das Ende je Los und das Ende der Grundlaufzeit statt des Höchstendes; in rund 10 % der Lose unterscheidet sich Vergabeweisers Datum davon (Folie 7). (2) Der Backtest: Ein fester Abstand sagt den Termin nicht voraus (28,8 %); Optionsanalyse an 52 Paaren: Bei belegter Option kam die Neuausschreibung in 70,8 % zwischen Ende der Grundlaufzeit und Höchstende (n = 24, Hinweis). (3) Ein dokumentiertes Prüfverfahren mit Seeds, Hashes und Evaluator; bei den geprüften Anbietern fanden wir keine Angabe zur Genauigkeit ihrer Vertragsenden. "
              "WETTBEWERBSBILD AUS TED (Paket A, 130 Oberpfalz-Lose): Auftragnehmer genannt bei 99,2 %, Zuschlagswert über 1 € nur bei 47,7 %, Zahl der Angebote bei 60,8 %, alle drei Felder zusammen bei 24,6 %. Das, wofür Gesprächspartner zahlen würden (alte Preise, Gegner), ist aus TED also nur zur Hälfte vollständig zu haben; Vergabeweiser zeigt Zuschlagsempfänger, Bieterzahl und Zuschlagssummen schon. "
              "NICHT BELEGT: Qualitätsvorteil beim Lesen; Nachfrage und Zahlungsbereitschaft (n = 3, nur für Wettbewerbsdaten, die es schon gibt); Abdeckung (unsere Liste nur TED und etwa 80 % der Lose, Vergabeweiser auch unterhalb der EU-Schwelle); der Vertriebskanal. "
              "POSITIONIERUNG (Hypothese, ungeprüft): Nische Gebäudereinigung, Datenqualität als Zulieferung für bestehende Dienste oder Beratung über Innung oder Kammer; der Kanal wäre der Vorteil, nicht die Technik, denn die Daten sind offen (CC0). Eine Liste als eigenes Produkt ist nicht tragfähig. "
              "TRANSFERFRAGE „Anderer Standort, andere Nische, doppeltes Volumen?“: Pipeline und Prüfverfahren übertragbar, Lese-Regeln neu testen (nur an eForms-Texten entwickelt, vor 2023 fehlen die meisten Vorgänger); doppeltes Volumen: Abruf skaliert, die menschliche Prüfung nicht. "
              "ZEIG-MIR-WO: docs/business.md §8.5 (Positionierung), reports/wettbewerbsbild_oberpfalz.md, reports/optionsanalyse.md, docs/annahmen.md.")
stat(s, 0.5, 1.15, 2.9, "≈ 10 %", "der Lose: Ende der Grundlaufzeit trifft nur die Liste (zwei Stichproben, n = 70 und 160)", TEAL, "Edge Unterschied", h=1.4, zsize=26, lsize=11)
stat(s, 3.6, 1.15, 2.9, "47,7 %", "der Oberpfalz-Lose mit Zuschlagswert über 1 € in TED; Zahl der Angebote 60,8 %", AMBER, "Edge Wettbewerbsbild", h=1.4, zsize=26, lsize=11)
stat(s, 6.7, 1.15, 2.8, "n = 3", "Gespräche: Zahlung nur für Wettbewerbsdaten, die es schon gibt", RED, "Edge Gespräche", h=1.4, zsize=26, lsize=11)
rect(s, 0.5, 2.65, 4.45, 2.4, PALE, name="Bleibt Karte")
rect(s, 0.5, 2.65, 4.45, 0.08, GREEN, name="Bleibt Streifen")
box(s, 0.65, 2.8, 4.2, 2.2, [[("Was bleibt", {"bold": True, "size": 15, "color": DARK})], "• Ende je Los, Grundlaufzeit statt Höchstende: rund 10 % der Lose", "• Backtest: fester Abstand trägt nicht (28,8 %)", "• Prüfverfahren dokumentiert; Genauigkeit der Anbieter nicht angegeben", "• Hypothese: Nische, Datenqualität als Zulieferung; Kanal (Innung) ungeprüft"], size=12, space=4, name="Bleibt Text")
rect(s, 5.05, 2.65, 4.45, 2.4, PALE, name="Nicht belegt Karte")
rect(s, 5.05, 2.65, 4.45, 0.08, RED, name="Nicht belegt Streifen")
box(s, 5.2, 2.8, 4.2, 2.2, [[("Nicht belegt", {"bold": True, "size": 15, "color": DARK})], "• bessere Lesequalität (gleiche Quelle, kein Mensch)", "• Nachfrage und Zahlungsbereitschaft", "• Abdeckung: nur TED, etwa 80 % der Lose; Vergabeweiser mehr", "• Eigenes Produkt: Liste allein nicht tragfähig"], size=12, space=4, name="Nicht belegt Text")

# 9 KI-Irrwege ---------------------------------------------------------------------------------------------
s = new_slide("KI-Irrwege, die wir gefunden haben",
              "ZEIT 1:00. KERNAUSSAGE: Claude Code hat Regeln, Stichproben und Auswertungen mitgebaut; jeder dieser Fehler wurde von einem getrennten Evaluator, im Test oder vom Nutzer gefunden, nicht von der Hand, die ihn gemacht hat. "
              "Vier von 27 Einträgen in docs/ki_irrwege.md: (1) Entwicklung 10–11 von 12 plausibel, im Test 11 von 24 richtig (Iteration 3): Regel verworfen. (2) „Blind“ war nicht blind: Leser der Iteration 8 hatten die Projektbeschreibung im Kontext (CLAUDE.md), gefunden vom Evaluator, im Ergebnis offen genannt. "
              "(3) Konkurrenz übersehen: Die Suche vom 24.10. fand keinen deutschen Dienst, tatsächlich gibt es zwei; gefunden vom Recherche-Agenten nach dem Hinweis des Dozenten. (4) Schwelle W8a unerreichbar: Claude übernahm die Diskordanzrate von 17 % aus Iteration 10 für 160 Lose, es waren 9,4 %; gefunden vor den Leserantworten, nicht nachträglich geändert. "
              "Weitere (nicht auf der Folie): Prüfer und Regel von derselben Hand (Iteration 2), versteckte Felder (65 von 95 „unbekannt“, Iteration 7), Dauerfeld enthält die Option schon (12 Lose, 0,13 % der Liste). Kernpunkt: Ein eigener Subagent (Evaluator) prüft jede Iteration kritisch. "
              "ZEIG-MIR-WO: docs/ki_irrwege.md, reports/evaluation_iteration10b.md.")
items = [("Entwicklung gut, Test schlecht", "10–11 von 12 plausibel, im Test 11 von 24 richtig (It. 3). Folge: Regel verworfen."),
         ("„Blind“ war nicht blind", "Leser hatten die Projektbeschreibung im Kontext (It. 8). Folge: offen berichtet."),
         ("Konkurrenz übersehen", "Suche vom 24.10. fand keinen deutschen Dienst; es gibt zwei (It. 10). Folge: Business Understanding neu."),
         ("Schwelle unerreichbar", "W8a: ≥ 16 von höchstens 15 Losen (It. 10b). Folge: nicht geändert, offen berichtet.")]
for i, (h, t) in enumerate(items):
    x, y = 0.5 + (i % 2) * 4.6, 1.2 + (i // 2) * 1.85
    rect(s, x, y, 4.4, 1.7, PALE, name=f"Irrweg {i + 1}")
    box(s, x + 0.2, y + 0.12, 4.0, 0.4, h, size=16, bold=True, color=DARK)
    box(s, x + 0.2, y + 0.6, 4.0, 1.0, t, size=13)
box(s, 0.5, 4.95, 8.5, 0.3, "4 von 27 Einträgen; gefunden vom Evaluator, im Test oder vom Nutzer: docs/ki_irrwege.md", size=10, color=GREY)

# 10 Trennung Entwicklung/Test (Live-Nachweis) ---------------------------------------------------------
s = new_slide("Trennung von Entwicklung und Test",
              "ZEIT 1:00. KERNAUSSAGE: Regeln, Seeds und Kriterien stehen im Git, bevor die Stichprobe gezogen oder die Antworten gelesen werden; das ist der Nachweis, dass Test und Entwicklung getrennt sind. "
              "LIVE-NACHWEIS (Fragerunde vorbereiten): im Terminal `git log --format=\"%h %ad %s\" --date=iso`. Iteration 10b: 4f50436 (Hypothese, Kriterien, Skript und Seed 20261112 vorab), 9d63c59 (Stichprobe gezogen, SHA-256 des Schlüssels 2cd00206…3e33; Schlüsseldatei lokal, nicht im Git: data/processed/stichprobe_iteration10b_schluessel.csv), 6b7e8d8 (Paket und Leseskript vor den Antworten), 69917ff (Antworten der Leser unverändert), f6583cc (Auswertung). "
              "Iteration 9 genauso: Regeln a03a4a8, Seed und Skript 4521952, Stichprobe und Auswertungsskript b3b1471, Antworten erst e1726e7. Entwicklungsfälle sind aus der Stichprobe ausgeschlossen (reports/entwicklung_iteration9_notices.txt). "
              "Ehrliche Lücken: das Lauf-Skript der Iteration-9-Leser wurde erst mit den Antworten committet; in Iteration 8 kannten die Leser den Fehlertyp; in 10b liegt das Protokoll der Leserläufe außerhalb des Repos. Der 10b-Fehler (W8a unerreichbar) wurde vor den Leserantworten bemerkt und offengelegt, aber nicht mehr geändert. "
              "FRAGE-VORBEREITUNG: „Parameter ändern, Wirkung erklären“: z. B. Seed ändern und Stichprobe neu ziehen (src/prepare/stichprobe_iteration10b.py) oder eine Regel in src/prepare/vertragsliste.py zeigen; Erwartung: Zahlen ändern sich leicht, die Aussagen bleiben, da die Stichprobe nur 70 bzw. 160 Lose hat. „Fehlwerte zeigen“: 33 der 130 Oberpfalz-Lose ohne Ende (Stufe F), keine Laufzeitfelder im XML. "
              "ZEIG-MIR-WO: git log, src/prepare/stichprobe_iteration10b.py, docs/reproduzierbarkeit.md.")
for i, (h, c) in enumerate((("Regel, Seed, Kriterien committen", "4f50436 (Iteration 10b)"), ("Stichprobe ziehen", "9d63c59, Hash des Schlüssels"), ("Lesen ohne Listenwerte", "6b7e8d8, Antworten 69917ff"), ("Auswerten gegen vorab Schwellen", "f6583cc, W8a–W11"))):
    x = 0.5 + i * 2.3
    rect(s, x, 1.4, 2.1, 2.5, PALE, name=f"Schritt {i + 1}")
    rect(s, x + 0.15, 1.55, 0.5, 0.5, TEAL, MSO_SHAPE.OVAL, f"Nummer {i + 1}")
    box(s, x + 0.15, 1.55, 0.5, 0.5, str(i + 1), size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.15, 2.2, 1.8, 0.9, h, size=14, bold=True)
    box(s, x + 0.15, 3.25, 1.8, 0.55, c, size=11, color=GREY)
box(s, 0.5, 4.2, 9, 0.7, "Nachweis in der Fragenrunde: git log und die Reihenfolge der Commits. Lücke: Leseprotokoll der Iteration 10b liegt außerhalb des Repos.", size=14, color=GREY)

# 11 Empfehlung und Grenzen ----------------------------------------------------------------------------------
s = new_slide("Empfehlung und Grenzen",
              "ZEIT 1:15. KERNAUSSAGE: Ampel statt Fazit-Text. GRÜN: Die Liste ist als Ausgangspunkt nutzbar, immer mit Blick in die verlinkte Bekanntmachung: 94,3 % der Zufallslose der Iteration 9 stimmen mit zwei KI-Lesungen überein (Mensch 14 von 15); Merkmal Ende je Los und Grundlaufzeit. Für Betriebe heißt das praktisch: Vertragsenden bei Vergabeweiser nachsehen (kostenlos) und das Enddatum in der Bekanntmachung prüfen, ob Grundlaufzeit oder Höchstende gemeint ist. "
              "GELB: Höchstende nur Hinweis (87,1 %); Abdeckung nur TED und etwa 80 % der Lose; Listenfehler offen (Dauerfeld enthält die Option: 12 von 9.325 Losen; Textmuster „läuft vom … bis … und verlängert sich“); Gespräche n = 3; Leser nicht unabhängig, keine Menschenprüfung der 15 Lose aus 10b. "
              "ROT: Terminprognose (28,8 %); „die Liste ist korrekt“; „genauer als Vergabeweiser“; Nachfrage und Zahlungsbereitschaft nicht belegt. "
              "TRANSFERFRAGE „Würdet ihr das Produkt bauen?“: Nein, nicht als Liste allein. Wenn weiter, dann ein Gespräch mit mehr größeren Betrieben und Vergabestellen, eine menschliche Gegenlesung und ein Maß, das Definition und Losebene trennt. Neuer Standort oder andere Nische: Pipeline übertragbar, Lese-Regeln neu testen. Doppeltes Volumen: Abruf skaliert, die menschliche Prüfung nicht. "
              "ZEIG-MIR-WO: docs/annahmen.md, reports/evaluation_iteration9.md, reports/evaluation_iteration10b.md, docs/business.md §8.9.")
ampel = (("Ja", GREEN, ["Liste „laut Bekanntmachung“ als Ausgangspunkt, Link prüfen", "Ende je Los, Grundlaufzeit statt Höchstende", "94,3 % wie zwei KI-Leser, Mensch 14/15"]),
         ("Mit Vorsicht", AMBER, ["Höchstende nur als Hinweis", "Nur TED, etwa 80 % der Lose", "Offene Listenfehler (12 von 9.325 Lose)", "Gespräche n = 3"]),
         ("Nein", RED, ["Terminprognose", "„Die Liste ist korrekt“", "Qualitätsvorsprung vor Vergabeweiser (nicht belegt)", "Nachfrage, Zahlungsbereitschaft (nicht belegt)"]))
for i, (h, f, pts) in enumerate(ampel):
    x = 0.5 + i * 3.1
    rect(s, x, 1.2, 2.9, 3.5, PALE, name=h + " Karte")
    rect(s, x + 0.2, 1.35, 0.4, 0.4, f, MSO_SHAPE.OVAL, h + " Signal")
    box(s, x + 0.75, 1.35, 2.05, 0.4, h, size=16, bold=True, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 2.0, 2.55, 2.6, ["• " + p for p in pts], size=13, space=7)
box(s, 0.5, 4.85, 8.5, 0.3, "Quellen: reports/evaluation_iteration9.md und 10b, docs/business.md §8", size=10, color=GREY)

# 12 Fazit ------------------------------------------------------------------------------------------------
s = new_slide("", "ZEIT 0:45. KERNAUSSAGE in einem Satz wiederholen, dann Brücke zur Fragenrunde. Gesamtzeit: 15:00 (Ziel ±30 Sekunden); Zeitbudget je Folie: 0:45 / 1:15 / 1:45 / 1:00 / 1:15 / 1:45 / 1:45 / 1:30 / 1:00 / 1:00 / 1:15 / 0:45. "
              "Satz zum Mitnehmen: Den Termin einer Neuausschreibung sagen TED-Daten nicht vorher; eine Liste der Vertragsenden lässt sich lesen, ist aber kein eigenes Produkt, solange Vergabeweiser sie kostenlos bietet. "
              "FRAGENRUNDE vorbereiten: (1) Methodenfrage: warum ±3 Monate, warum diese Baseline, warum KI-Leser als Maß, warum nur diskordante Lose (Folien 3, 5, 7). (2) Live-Nachweis: git log und die Reihenfolge der Commits zeigen, Seed und Schlüssel-Hash (Folie 10), Regel in src/prepare/vertragsliste.py öffnen, Fehlwerte (Stufe F) in reports/beispiel_liste_oberpfalz.csv zeigen. "
              "(3) Transferfrage: „Warum nicht Vergabeweiser nutzen?“ (Folie 6/8), anderer Standort, andere Nische, doppeltes Volumen (Folie 8/11). Nicht sagen: „genauer als Vergabeweiser“, „Vorsprung belegt“, „kein Unterschied“.", dark=True)
box(s, 0.6, 0.5, 8.8, 0.8, "Fazit", size=36, bold=True, color=AMBER, font=HEAD, name="Fazit Titel")
box(s, 0.6, 1.4, 8.8, 2.4, "TED-Daten sagen den Termin einer Neuausschreibung nicht vorher (28,8 % statt 60 %). Eine Liste der Vertragsenden lässt sich daraus lesen: 94,3 % Übereinstimmung mit zwei KI-Lesern. "
    "Ein eigenes Produkt ist sie nicht, denn Vergabeweiser bietet sie kostenlos. Ein Unterschied bleibt (Ende je Los, Grundlaufzeit statt Höchstende, rund 10 % der Lose); "
    "bessere Lesequalität ist nicht belegt, Nachfrage und Zahlungsbereitschaft sind offen.", size=19, color=WHITE, name="Kernbotschaft")
box(s, 0.6, 4.0, 8.8, 1.0, [[("Nächster Schritt: ", {"bold": True, "color": AMBER}), ("menschliche Gegenlesung der 15 Lose und mehr Gespräche mit größeren Betrieben und Vergabestellen", {"color": SOFT})]], size=16, name="Nächster Schritt")

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(len(prs.slides), "Folien;", OUT)
