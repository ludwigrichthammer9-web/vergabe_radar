"""Foliengerüst für den Vortrag (LN B: 15 min, höchstens 12 Folien) mit Sprechernotizen.

Stand nach Iteration 10 und 10b, überarbeitet nach Kritik des Evaluators: Methodik auf Folien 2 bis 4 verdichtet,
Business Understanding auf Folien 5 bis 8 (6:15 von 15:00), Publikumsfrage mit Business-Bezug, Live-Nachweis auf Folie 10.
Zahlen aus docs/iterationen.md, docs/business.md §8, reports/evaluation_iteration5.md bis 10b, reports/wettbewerbsbild_oberpfalz.md.
Jede Folie hat Notizen: ZEIT, KERNAUSSAGE, FRAGE – ANTWORT, ZEIG-MIR-WO (Summe der Zeiten 15:00).
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


def stat(s, x, y, w, zahl, label, farbe, name, h=1.5, zsize=34, lsize=13, zoff=0.72):
    rect(s, x, y, w, h, PALE, name=name + " Karte")
    box(s, x + 0.15, y + 0.05, w - 0.3, zoff - 0.05, zahl, size=zsize, bold=True, color=farbe, font=HEAD, name=name + " Zahl")
    box(s, x + 0.15, y + zoff, w - 0.3, h - zoff - 0.06, label, size=lsize, name=name + " Text")


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
s = new_slide("", "ZEIT 0:30. KERNAUSSAGE: Eine Reinigungsfirma will früh wissen, wann ein öffentlicher Vertrag endet und neu ausgeschrieben wird. Wir zeigen, was TED-Daten dazu hergeben "
              "(eine Liste der Vertragsenden), was nicht (eine Terminprognose), und was an der Idee gegenüber der kostenlosen Konkurrenz übrig bleibt. "
              "Ablauf in einem Satz: Frage, zwei Irrwege, eine Liste samt Genauigkeit (kurz, vier Folien), dann der längere Teil: Wie arbeiten Betriebe, wer bietet es schon, was bleibt. "
              "Kernbotschaft schon jetzt nennen: Die Liste lässt sich aus TED lesen, ein eigenes Produkt ist sie nicht, und ein Qualitätsvorsprung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/iterationen.md (Übersicht und Ergebnis Iteration 10 und 10b).", dark=True)
box(s, 0.6, 1.5, 6.2, 1.0, "Vergabe-Radar", size=48, bold=True, color=WHITE, font=HEAD, name="Titel")
box(s, 0.6, 2.6, 6.0, 1.2, "Wann laufen öffentliche Aufträge aus, und wer weiß es schon? Was TED-Daten verraten, wer mitspielt und was bleibt", size=20, color=SOFT, name="Untertitel")
box(s, 0.6, 4.7, 7.5, 0.4, "Big Data Analytics · Leistungsnachweis B · [Namen eintragen]", size=12, color=SOFT, name="Autoren")
rect(s, 7.2, 1.4, 2.2, 2.2, TEAL, MSO_SHAPE.OVAL, "Fragezeichen Kreis")
box(s, 7.2, 1.4, 2.2, 2.2, "?", size=96, bold=True, color=WHITE, font=HEAD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, name="Fragezeichen")

# 2 Frage, Kriterium, Daten, Zyklen (Methodik verdichtet 1/3) -------------------------------------------
s = new_slide("Frage, Kriterium, Daten",
              "ZEIT 1:00. KERNAUSSAGE: Die Frage hatte eine Entscheidung (auf welche Ausschreibung bereite ich mich vor?) und eine vorab festgelegte Schwelle. "
              "Zielgruppe: Reinigungsfirmen im Mittelstand, Nische Gebäudereinigung (Haupt-CPV 90910/90911/90919). Annahme: Wer früh weiß, wann ein Vertrag endet, kann Personal und Angebot vorbereiten (A1, A15); diese Annahme war zu diesem Zeitpunkt ungeprüft, ein Kundengespräch gab es nicht. "
              "Erfolgskriterium vor dem Backtest festgelegt (docs/business.md 7.1): Treffer = Neuausschreibung im Fenster ±3 Monate um die Prognose, Schwelle 60 %; Baseline R0 = naive Regel 17,3 %. "
              "Daten: TED Search API, eForms-Zuschläge ab Okt. 2023, Rohdaten unverändert in data/raw (nicht im Git, Abruf-Skript in docs/reproduzierbarkeit.md). 9.325 Lose aus 4.011 Zuschlägen, im Richtwert von 200 bis 10.000 Zeilen. "
              "Laufzeitende bei 90,0 % der Zuschläge bestimmbar; Verlängerungsoptionen nur bei 18,9 % im Feld BT-58, der Rest im Freitext. "
              "Streifen unten: vier Zyklen CRISP-DM, jeder endete mit einer Entscheidung gegen vorab festgelegte Schwellen. Zyklus 4 ist der Rücksprung in Phase 1; er bekommt in diesem Vortrag den größten Teil der Zeit (Folien 5 bis 8, 6:15 von 15:00). "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1: Befüllungsquote etwa 90 %, Laufzeitende bestimmbar, Haupt-CPV klar abgrenzbar. Eine Geschäftsbegründung ist das nicht; sie wurde nicht belegt. "
              "ZEIG-MIR-WO: docs/business.md Abschnitt 7.1, reports/datenqualitaet_DEU_20260722_20261021.md, docs/quellen.md.")
box(s, 0.5, 1.1, 9, 0.7, "Reinigungsfirmen wollen sich früh auf Neuausschreibungen vorbereiten. Entscheidung: Auf welche Ausschreibung stelle ich Personal und Angebot ein?", size=16)
stat(s, 0.5, 1.95, 2.8, "60 %", "Mindest-Trefferquote der Terminprognose, ±3 Monate (vorab festgelegt)", TEAL, "Schwelle", h=1.45, zsize=30)
stat(s, 3.6, 1.95, 2.8, "17,3 %", "naive Vergleichsregel R0 (Baseline)", GREY, "Baseline", h=1.45, zsize=30)
stat(s, 6.7, 1.95, 2.8, "9.325", "Lose aus 4.011 TED-Zuschlägen der Gebäudereinigung (ab Okt. 2023)", TEAL, "Daten", h=1.45, zsize=30)
box(s, 0.5, 3.6, 9, 0.35, "Vier Zyklen, jeder mit Entscheidung gegen vorab festgelegte Schwellen", size=13, bold=True, color=DARK)
for t, x, w, f in (("1 Zuordnung (It. 1–4)", 0.5, 2.3, TEAL), ("2 Prognose (It. 5)", 2.85, 2.1, AMBER),
                   ("3 Qualität der Liste (It. 6–9)", 5.0, 2.45, GREEN), ("4 Business (It. 10)", 7.5, 2.0, RED)):
    rect(s, x, 4.0, w - 0.05, 0.6, f, name=t)
    box(s, x + 0.08, 4.0, w - 0.2, 0.6, t, size=12, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
box(s, 0.5, 4.85, 8, 0.3, "Quelle: TED Search API v3 (docs/quellen.md), Zuschläge mit Veröffentlichung Q4 2025 bis Q3 2026", size=10, color=GREY)

# 3 Irrwege Zuordnung und Terminprognose (Methodik 2/3) -------------------------------------------------
s = new_slide("Irrwege: Zuordnung, Terminprognose",
              "ZEIT 1:15. KERNAUSSAGE: Zwei Ideen sind an vorab festgelegten Schwellen gescheitert, und das haben wir so berichtet. "
              "IRRWEG 1 (Iteration 2 bis 4): Jede Neuausschreibung dem Vorgängervertrag zuordnen. Auftraggeber + CPV 16,7 % (Schwelle 80 %), weil große Auftraggeber viele Verträge parallel vergeben; Objekt-Regel (Adresse, Titel) 28,9 % (Schwelle 60 %); letzter Versuch auf neuen Testdaten 56,7 % (Schwelle 60 %), die Zweitprüfung durch den Nutzer 65 %. Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 richtig. "
              "IRRWEG 2 (Iteration 5, Backtest): R1 = Höchstende − 6 Monate auf 52 von Hand bestätigten Paaren: 28,8 %; R0 17,3 %; Schwelle 60 %. 20 Neuausschreibungen kamen mehr als 3 Monate früher, 15 im Fenster, 17 später. Entscheidung: Idee anpassen, keine Terminprognose. Grenzen: Paare aus einer Rückwärtssuche (nur auffindbare Vorgänger), Zweitprüfung KI-unterstützt. "
              "OPTIONALE BACKTEST-FRAGE (nur wenn Zeit, sonst weglassen; die Publikumsfrage des Vortrags steht auf Folie 5): „Wie oft trifft ‚Höchstende − 6 Monate‘ den Termin im Fenster ±3 Monate?“ Antwort: 28,8 %. "
              "FRAGE – ANTWORT: „Warum ±3 Monate, warum diese Baseline?“ Das Fenster wurde vor der Rechnung gesetzt, weil ein Betrieb für Personal und Angebot grob ein Vierteljahr Spielraum braucht; die naive Regel R0 zeigt, was Zufall und Streuung allein schaffen; die Schwelle 60 % war eine Setzung ohne Kundenkontakt. Ein Fenster ±6 Monate wäre für die Entscheidung zu unscharf. "
              "ZEIG-MIR-WO: reports/zuordnung_iteration3.md, reports/evaluation_iteration4.md, reports/backtest_iteration5.md, reports/evaluation_iteration5.md.")
balken(s, 0.5, 1.15, 5.8, 3.4, ["Zuordnung: Auftraggeber + CPV", "Zuordnung: Objekt-Regel", "Zuordnung: letzter Versuch", "Terminprognose R1 (Backtest)"],
       [16.7, 28.9, 56.7, 28.8], [RED, RED, AMBER, RED], "Trefferquote gegen Schwelle")
box(s, 0.5, 4.6, 5.8, 0.5, "Schwellen vorab: 80 %, 60 %, 60 %, 60 %. Baseline der Prognose R0: 17,3 %", size=12, color=GREY)
rect(s, 6.5, 1.3, 3.0, 3.3, PALE, name="Lehre Karte")
rect(s, 6.5, 1.3, 3.0, 0.08, TEAL, name="Lehre Streifen")
box(s, 6.65, 1.5, 2.7, 3.0, [[("Was wir mitnehmen", {"bold": True, "size": 15, "color": DARK})], "• Schwellen vorab: Rückschläge zählen als Ergebnis", "• Entwicklung ≠ Test: 10–11 von 12 plausibel, im Test 11 von 24", "• Entscheidung: keine Terminprognose, sondern eine Liste der Vertragsenden"], size=13, space=6, name="Lehre Text")

# 4 Liste und Genauigkeit (Methodik 3/3) ------------------------------------------------------------------
s = new_slide("Die Liste und ihre Genauigkeit",
              "ZEIT 1:15. KERNAUSSAGE: Aus dem Rückschlag wird eine andere Frage: nicht „wann wird neu ausgeschrieben?“, sondern „wann endet ein Vertrag laut Bekanntmachung?“. Vier Messungen messen vier verschiedene Dinge; keine ist eine belastbare Fehlerquote. "
              "Die Liste (Fassung der Iteration 9) hat 9.325 Lose; je Los das Ende der Grundlaufzeit, das Höchstende nur als Hinweis, Auftraggeber, TED-Link und eine Stufe A bis F (woher die Angabe stammt). Ein Datum liefert sie für 79,4 % der Lose (2.783 von 3.503; Schwelle 80 % knapp verfehlt). Prototyp Oberpfalz: 130 Lose, davon 33 ohne Ende (Stufe F, keine Laufzeitfelder im XML). "
              "Iteration 6: Handprüfung von 60 Zufallslosen, aber die Vorlage zeigte den Listenwert (Verankerung): 88,3 %. Iteration 7: Handprüfung ohne Listenwerte, Nachprüfung im Original: 76,6 %, ein Mischmaß aus Listen- und Prüfungsfehlern. "
              "Iteration 8: zwei KI-Leser (Opus, Sonnet) auf allen 95 Losen: 77 von 80 = 96,2 %, Leser nicht unabhängig. Iteration 9: neue Stichprobe (Seed 20261109), Rohtext ohne Projektkontext, überarbeitete Liste: 66 von 70 = 94,3 %, Kommilitone 14 von 15; Höchstende 87,1 % (Schwelle 90 % verfehlt). "
              "Die alte Fassung der Liste erreicht auf denselben Losen 65 von 70: Der Nutzen der neuen Regeln ist kaum gesichert. "
              "FRAGE – ANTWORT: „Warum Übereinstimmung mit KI-Lesern als Maß, was wäre die Alternative?“ Es gibt keine Wahrheitsquelle außer dem Bekanntmachungstext; Handprüfung ist teuer und hatte Verankerung (It. 6) und Abschreibefehler (It. 7), deshalb zusätzlich KI-Leser mit neutraler Definition „erste feste Laufzeit ohne Optionen“. Alternative: mehr Menschen als Leser; fehlt noch. "
              "FRAGE – ANTWORT: „Was brachten Iteration 6 bis 9?“ Eine Basisregel (Feld EndDate) trifft 63 von 70; die Fassung mit den Regeln 6 bis 10 trifft 66 von 70 (alte Fassung 65): ein kleiner, kaum gesicherter Zugewinn, dafür bekannte Fehlerarten behoben und Lose ohne Zuschlag entfernt (590). "
              "ZEIG-MIR-WO: reports/beispiel_liste.md, reports/beispiel_liste_oberpfalz.csv, reports/evaluation_iteration6.md bis 9.")
stat(s, 0.5, 1.1, 2.9, "9.325", "Lose in der Liste (Fassung 9)", TEAL, "Lose", h=1.0, zsize=26, lsize=12, zoff=0.5)
stat(s, 3.6, 1.1, 2.9, "79,4 %", "der Lose mit Datum (2.783 von 3.503)", TEAL, "Abdeckung", h=1.0, zsize=26, lsize=12, zoff=0.5)
stat(s, 6.7, 1.1, 2.8, "A–F", "Stufe je Eintrag: woher die Angabe stammt", AMBER, "Stufe", h=1.0, zsize=26, lsize=12, zoff=0.5)
balken(s, 0.5, 2.3, 5.7, 2.55, ["It. 6: Hand, Listenwert sichtbar", "It. 7: Hand, ohne Listenwert", "It. 8: zwei KI-Leser", "It. 9: KI-Leser, neue Stichprobe"],
       [88.3, 76.6, 96.2, 94.3], [AMBER, RED, TEAL, TEAL], "Ende der Grundlaufzeit stimmt")
rect(s, 6.4, 2.35, 3.1, 2.5, PALE, name="Schwächen Karte")
box(s, 6.55, 2.45, 2.8, 2.35, [[("Jede Messung hat eine Schwäche", {"bold": True})], "• 6: verankert; 7: Mischmaß aus Listen- und Prüffehlern", "• 8: Leser nicht unabhängig", "• 9: Vergleichswert teils zirkulär, Mensch nur 14/15", [("Keine belastbare Fehlerquote", {"bold": True})]], size=12, space=4, name="Schwächen")
box(s, 0.5, 4.9, 5.7, 0.3, "Schwelle jeweils 90 %; It. 7: 47 Lose; It. 9: 70 Zufallslose", size=10, color=GREY)

# 5 Business: Wie gehen Betriebe heute vor? (mit Publikumsfrage) ---------------------------------------
s = new_slide("Wie gehen Betriebe heute vor?",
              "ZEIT 1:30. KERNAUSSAGE: Ab hier der Teil, den wir zu knapp behandelt hatten: das Business Understanding (Folien 5 bis 8, zusammen 6:15 = 42 % der Zeit). Zuerst der Prozess aus Sicht der Betriebe, dann die Konkurrenz. "
              "PUBLIKUMSFRAGE (gleich zu Beginn der Folie, bevor Folie 6 aufgelöst wird; 20 Sekunden, Handzeichen): „Gibt es kostenlos eine Liste auslaufender öffentlicher Verträge?“ Ja / nein / weiß nicht. Auflösung auf Folie 6: Ja, Vergabeweiser. "
              "PROZESS (Fakten, drei Gespräche des Nutzers am 2026-11-05; 9 Anrufe, 3 erreicht, 105 Minuten; Notizen ohne Namen; n = 3, Hinweise, keine Belege): Betrieb mittlerer Größe: Meldung der Ausschreibung 28 Tage vor Abgabe; eng bei der Objektbegehung (ein Termin, der beste Vorarbeiter krank); Kalkulation nachts; Entscheidung mitzubieten „hauptsächlich Entfernung und Personal“; Vertragsenden bei anderen „eine Blackbox“. Kleinbetrieb: Entscheidung nach Kapazität des Teams; die Bürokratie (viele Eigenerklärungen) ist der Engpass; sucht auf Webseiten und in der Zeitung. Vergabestelle: plant etwa 9 Monate vor Vertragsende, verlängert „fast immer, wenn eine Option im Vertrag steht“, vergibt „sehr oft“ unterhalb der EU-Schwelle (also nicht auf TED). "
              "KOSTEN der Suche: Portal-Abo des mittleren Betriebs knapp 1.500 € im Jahr (Suchprofile); Dienste wie subreport 84–198 € im Monat (Produktübersicht, Recherche, nicht einzeln nachgeprüft). Der Kleinbetrieb zahlt für nichts in dem Bereich. "
              "FRAGE – ANTWORT: „Wer zahlt?“ Gespräche n = 3: Der größere Betrieb würde für den aktuellen Auftragnehmer und alte Preise zahlen, die Enddaten nannte er „nett für die Planung“; der Kleinbetrieb für nichts. Ein Betrag wurde nicht genannt. Aus TED ist das nur teilweise lieferbar (Folie 6). Preisanker der Konkurrenz: 0 bis 200 € im Monat. Ehrlich: Zahlungsbereitschaft ist nicht belegt. "
              "FRAGE – ANTWORT: „Sind die Gespräche anonym?“ Ja. Es gibt keine Namen von Personen oder Firmen, die Betriebe sind nur beschrieben (Betrieb mittlerer Größe, Kleinbetrieb, Vergabestelle). "
              "ZEIG-MIR-WO: docs/business.md §8.1 (wie Betriebe an Aufträge kommen) und §8.9 (Gespräche), docs/annahmen.md (A1, A15).")
for i, (h, t) in enumerate((("1 Meldung", "Hinweis kommt 28 Tage vor Abgabe"), ("2 Begehung", "Ein Termin; fällt der beste Vorarbeiter aus, wird es eng"),
                            ("3 Kalkulation", "Unter Zeitdruck, nachts"), ("4 Entscheidung", "Entfernung und Personal bzw. Kapazität; Bürokratie"))):
    x = 0.5 + i * 2.3
    rect(s, x, 1.15, 2.1, 1.65, PALE, name=h + " Karte")
    rect(s, x, 1.15, 2.1, 0.08, TEAL, name=h + " Streifen")
    box(s, x + 0.12, 1.32, 1.9, 0.35, h, size=15, bold=True, color=DARK)
    box(s, x + 0.12, 1.75, 1.9, 1.0, t, size=13)
rect(s, 0.5, 3.0, 5.4, 1.9, PALE, name="Suche Karte")
box(s, 0.65, 3.08, 5.1, 1.8, [[("Womit sie suchen, was es kostet", {"bold": True, "color": DARK, "size": 14})],
    "• Portal-Abo: knapp 1.500 € im Jahr (Betrieb mittlerer Größe)", "• Dienste wie subreport: 84–198 € im Monat", "• Kleinbetrieb: Webseiten, Zeitung, zahlt nichts; Vertragsenden „eine Blackbox“"], size=12, space=4, name="Suche Text")
rect(s, 6.1, 3.0, 3.4, 1.9, DARK, name="Publikumsfrage Karte")
box(s, 6.25, 3.1, 3.1, 1.7, [[("Frage an euch", {"bold": True, "color": AMBER})], [("Gibt es kostenlos eine Liste auslaufender öffentlicher Verträge?", {"color": WHITE})], [("Handzeichen: ja, nein, weiß nicht", {"color": SOFT, "size": 12})]], size=15, space=6, name="Publikumsfrage")
box(s, 0.5, 5.0, 8.5, 0.3, "Quelle: drei Gespräche (n = 3: Betrieb mittlerer Größe, Kleinbetrieb, Vergabestelle), docs/business.md §8.1, §8.9", size=10, color=GREY)

# 6 Business: Konkurrenz ----------------------------------------------------------------------------------
s = new_slide("Auflösung: Wer bietet es schon?",
              "ZEIT 1:45. KERNAUSSAGE: Auflösung der Publikumsfrage: Ja, es gibt sie kostenlos. Vergabeweiser listet 1.005 Gebäudereinigungs-Verträge, die in 12 Monaten enden, mit Zuschlagsempfänger, Zahl der Angebote und Verlängerungsoptionen, ober- und unterschwellig. "
              "TABELLE (Prüfstand): Vergabeweiser und die Vertragsende-Seite von AusschreibungsRadar hat Claude am 2026-11-05 selbst nachgelesen; AusschreibungsRadar: 0 bis 149 € im Monat, KI-Eignungsanalyse ab 29 €, Bid/No-Bid-Check mit Match-Score ab 79 € (Preise aus der Recherche); aufträge.io (43.373 Verträge mit Ende in 12 Monaten, auf Anfrage) und subreport (84–198 € im Monat) stammen aus der Recherche eines Agenten und sind nicht einzeln nachgeprüft; DTAD nach Aussage des Betriebs mittlerer Größe: knapp 1.500 € im Jahr, eine Liste auslaufender Verträge kenne er dort nicht. Beide geprüften deutschen Anbieter schreiben selbst, dass der Auftraggeber über die Neuausschreibung entscheidet. "
              "HINWEIS (Fakt, Paket A, 130 Oberpfalz-Lose): Auftragnehmer genannt bei 99,2 %, Zuschlagswert über 1 € nur bei 47,7 %, Zahl der Angebote bei 60,8 %. TED-Daten allein reichen für Preisbenchmarks also nur zur Hälfte. "
              "Beobachtung (Hypothese, n = 3): Zwei Betriebe nutzen keinen der Dienste, einer kannte sie vom Hörensagen, die andere gar nicht: eher ein Bekanntheits- als ein Angebotsproblem der Konkurrenz. "
              "FRAGE – ANTWORT: „Warum nicht einfach Vergabeweiser nutzen?“ Doch, für die Suche nach Vertragsenden spricht vieles dafür: kostenlos, mehr Abdeckung (auch unterhalb der EU-Schwelle), Zuschlagsempfänger und Bieterzahl. Unsere Liste ist als eigenes Produkt nicht tragfähig; was bleibt, steht auf Folie 8. "
              "ZEIG-MIR-WO: docs/business.md §8.2 (Wettbewerber), §8.7 (Marktzahlen), reports/nebentest_ausschreibungsradar.md, reports/wettbewerbsbild_oberpfalz.md.")
zeilen = [("Anbieter", "Funktion", "Preis", "Prüfstand"),
          ("Vergabeweiser", "Ende, Zuschlagsempfänger, Bieterzahl; ober- und unterschwellig; 1.005 Reinigungsverträge", "kostenlos", "nachgelesen"),
          ("AusschreibungsRadar", "Laufzeitende, geschätzter Ausschreibungsmonat", "0–149 € im Monat; KI-Eignungsanalyse ab 29 €; Bid/No-Bid-Check mit Match-Score ab 79 €", "Funktion nachgelesen, Preise Recherche"),
          ("aufträge.io", "43.373 Verträge mit Ende in 12 Monaten, Analyse bisheriger Gewinner", "auf Anfrage", "Recherche"),
          ("subreport", "Ausschreibungsdienst (Suche, Alarm)", "84–198 € im Monat", "Recherche"),
          ("DTAD", "Portal-Abo mit Suchprofilen; keine Liste auslaufender Verträge bekannt", "knapp 1.500 € im Jahr", "Gespräch")]
tbl = s.shapes.add_table(len(zeilen), 4, Inches(0.5), Inches(1.1), Inches(9), Inches(3.1))
tbl.name = "Konkurrenz Tabelle"
for c, w in enumerate((1.6, 3.4, 2.6, 1.4)):
    tbl.table.columns[c].width = Inches(w)
for r, h in enumerate((0.3, 0.6, 0.85, 0.6, 0.45, 0.6)):
    tbl.table.rows[r].height = Inches(h)
for r, zeile in enumerate(zeilen):
    for c, wert in enumerate(zeile):
        cell = tbl.table.cell(r, c)
        cell.text = wert
        run = cell.text_frame.paragraphs[0].runs[0]
        run.font.size, run.font.name = Pt(12), BODY
        run.font.bold = r == 0 or c == 0
        run.font.color.rgb = WHITE if r == 0 else INK
        cell.fill.solid()
        cell.fill.fore_color.rgb = TEAL if r == 0 else PALE
        cell.margin_top = cell.margin_bottom = Inches(0.03)
rect(s, 0.5, 4.45, 9.0, 0.55, DARK, name="Hinweis Banner")
box(s, 0.65, 4.45, 8.7, 0.55, [[("Hinweis: ", {"bold": True, "color": AMBER}), ("TED-Daten allein reichen für Preisbenchmarks nur zur Hälfte (Wert über 1 € bei 47,7 % der Oberpfalz-Lose).", {"color": WHITE})]], size=13, anchor=MSO_ANCHOR.MIDDLE, name="Hinweis Text")

# 7 Business: Vergleich mit Vergabeweiser -------------------------------------------------------------------
s = new_slide("Vergleich mit Vergabeweiser",
              "ZEIT 1:30. KERNAUSSAGE: Wir haben vorab festgelegt und dann geprüft, ob unsere Liste das Ende der Grundlaufzeit häufiger trifft als Vergabeweiser. Ergebnis: Es gibt einen Unterschied in rund 10 % der Lose, aber er ist überwiegend eine Frage der Definition und der Losebene, kein belegter Qualitätsvorteil. "
              "ITERATION 10 (70 Zufallslose der Iteration 9): Liste 66/70, Vergabeweiser 58/70, Differenz +8 (Schwelle ≥ 5), exakter Test p = 0,0078, formal erfüllt, auf Los- und Definitionsebene. Die Basisregel „Feld EndDate“ allein trifft 63/70. Ursachen der 8: Losebene 4, Höchstende statt Grundlaufzeit 2, fehlender Wert 1, 2 Tage 1. "
              "ITERATION 10b (neue Stichprobe, 160 Lose, Seed 20261112): Vergabeweiser hat alle 160, 145 gleich, 15 diskordant. Zwei KI-Leser (Opus, Sonnet) lesen ohne Quellenangabe und stimmen bei 15 von 15 überein; die Liste entspricht ihrem Wert in 15 von 15. Einordnung des Evaluators: Höchstende 7 (alle mit derselben Textvorlage, effektiv ein Mechanismus), Losebene 4, Zuordnungsfehler unserer Pipeline 1, Abweichung bei Vergabeweiser mit offener Ursache 2, mehrdeutig 1. "
              "VORAB-KRITERIEN: Die Vorab-Schwelle für den Vorsprung (≥ 16 Lose) war bei nur 15 abweichenden Losen rechnerisch unerreichbar; das war unser Fehler bei der Festlegung (docs/ki_irrwege.md). Sie wurde nicht nachträglich geändert und gilt als formal verfehlt. Das zweite Kriterium (Losebene als richtig für Vergabeweiser, ≥ 8 Lose) ist erfüllt. Sensitivität: Zählt auch das Höchstende als richtig für Vergabeweiser, bleiben 3 zu 0 (p = 0,25), also nichts Belegtes. Zusammen: nur die Liste richtig bei 23 von 230 = 10,0 % (Wilson etwa 6,8–14,6 %). "
              "ZULÄSSIGER SATZ: „Auf zwei Stichproben weicht Vergabeweisers Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt; in 10b waren 11 von 15 dieser Fälle Höchstende oder Losebene.“ NICHT sagen: „genauer“, „Vergabeweiser liest falsch“, „kein Unterschied“. "
              "GRENZEN: Liste und Vergabeweiser nutzen dasselbe TED-Feld, gemeinsame Fehler sind unsichtbar (bei einem von 10 übereinstimmenden Losen lagen beide falsch); Leser und Regeln aus derselben Modellfamilie; keine menschliche Gegenlesung der 15; nur Lose oberhalb der EU-Schwelle. "
              "FRAGE – ANTWORT: „Warum ist W8a verfehlt?“ Die Vorab-Schwelle (≥ 16 Lose) war bei 15 diskordanten Losen rechnerisch unerreichbar. Gemessen: Differenz +15 von 15, p = 0,0001, aber überwiegend Definition und Losebene, deshalb kein Beleg für bessere Lesequalität. Kriterium nicht geändert, offen berichtet. "
              "FRAGE – ANTWORT: „Warum nur die diskordanten Lose lesen?“ Weil die übereinstimmenden die Differenz nicht ändern; absolute Genauigkeit der Liste ist damit nicht belegt. "
              "ZEIG-MIR-WO: reports/vergleich_iteration10.md, reports/vergleich_iteration10b.md, reports/evaluation_iteration10b.md, src/prepare/vergleich_iteration10b.py.")
rect(s, 0.5, 1.15, 4.4, 2.35, PALE, name="Vergleich Karte")
box(s, 0.65, 1.22, 4.1, 0.6, "66 : 58", size=34, bold=True, color=TEAL, font=HEAD, name="Vergleich Zahl")
box(s, 0.65, 1.88, 4.1, 1.6, "richtiges Ende der Grundlaufzeit, Liste : Vergabeweiser, n = 70, auf Los- und Definitionsebene. Basisregel Feld EndDate: 63/70. Kein Beleg für bessere Lesequalität.", size=13, name="Vergleich Text")
stat(s, 0.5, 3.65, 4.4, "15 von 160", "weichen ab (It. 10b); 11 davon Höchstende oder Losebene", AMBER, "Iteration 10b", h=1.3, zsize=26, lsize=12, zoff=0.55)
box(s, 5.1, 1.1, 4.4, 0.35, "Die 15 abweichenden Lose in 10b", size=14, bold=True, color=DARK)
balken(s, 5.0, 1.45, 4.5, 2.45, ["Höchstende", "Losebene", "Ursache offen", "Zuordnung (Pipeline)", "mehrdeutig"],
       [7, 4, 2, 1, 1], [AMBER, AMBER, GREY, GREY, GREY], "Ursachen der 15 abweichenden Lose", maximum=10, fmt='0')
box(s, 5.1, 4.0, 4.4, 1.0, [[("Vorab-Schwelle (≥ 16 Lose) bei 15 abweichenden Losen rechnerisch unerreichbar: ", {"bold": True}), ("unser Fehler, offen berichtet. Gleiche TED-Quelle, Leser aus einer Modellfamilie, kein Mensch.", {})]], size=12, name="Grenzen Vergleich")

# 8 Business: Competitive Edge und Positionierung ------------------------------------------------------------
s = new_slide("Competitive Edge: Was bleibt?",
              "ZEIT 1:30. KERNAUSSAGE: Aus Unternehmersicht ergibt die Liste als eigenes Produkt keinen Sinn. Von der Idee bleibt ein Merkmalsunterschied, kein belegter Vorsprung und kein belegter Markt. "
              "WAS KEINEN SINN ERGIBT (Interpretation, docs/business.md §8.4): (1) Das Kernprodukt gibt es schon, kostenlos und mit mehr Abdeckung. (2) Das Kundenproblem ist eine Setzung: Der Engpass liegt nach den Quellen eher bei Preis (63 % der Vergaben nur nach Preis), Personal und Bürokratie; ob „früher wissen“ hilft, ist offen (A1, A15). (3) Die nahe Zukunft fehlt: Die Vorgänger heutiger Neuausschreibungen stammen meist aus der Zeit vor eForms (55 von 68 Backtest-Vorgängern). (4) Vertragsende ist kein Termin: Verlängerung ist der Normalfall, Backtest 28,8 %; das gilt für alle Anbieter. (5) Markt klein: grobe Schätzung des Gutachtens 3,6–7,2 Mio. € Gesamtpotenzial bei offenen Annahmen, gegen kostenlose Konkurrenz fraglich. "
              "WAS BLEIBT (Fakten): (1) Ende je Los und Ende der Grundlaufzeit statt Höchstende; in rund 10 % der Lose weicht Vergabeweisers Datum davon ab, auf Los- und Definitionsebene (Folie 7). (2) Ein dokumentiertes Prüfverfahren mit Seeds, Hashes und Evaluator; bei den geprüften Anbietern fanden wir keine Angabe zur Genauigkeit ihrer Vertragsenden. Optionsanalyse an 52 Paaren: Bei belegter Option kam die Neuausschreibung in 70,8 % zwischen Ende der Grundlaufzeit und Höchstende (n = 24, Hinweis). (3) Die Nische als Hypothese: Gebäudereinigung, Datenqualität als Zulieferung für bestehende Dienste oder Beratung über Innung oder Kammer; der Kanal wäre der Vorteil, nicht die Technik, denn die Daten sind offen (CC0). Nichts davon ist im Projekt geprüft. "
              "NICHT BELEGT: Qualitätsvorteil beim Lesen; Nachfrage und Zahlungsbereitschaft; Abdeckung (unsere Liste nur TED, etwa 80 % der Lose, Vergabeweiser auch unterhalb der EU-Schwelle); der Vertriebskanal. "
              "TRANSFERFRAGE „Anderer Standort, andere Nische, doppeltes Volumen?“: Pipeline und Prüfverfahren übertragbar, Lese-Regeln neu testen (nur an eForms-Texten entwickelt, vor 2023 fehlen die meisten Vorgänger); doppeltes Volumen: Abruf skaliert, die menschliche Prüfung nicht. "
              "ZEIG-MIR-WO: docs/business.md §8.4 (Interpretation), §8.5 (Positionierung), reports/wettbewerbsbild_oberpfalz.md, reports/optionsanalyse.md, docs/annahmen.md.")
box(s, 0.5, 1.05, 9, 0.3, "Aus Unternehmersicht ergibt die Liste als eigenes Produkt keinen Sinn, weil …", size=13, bold=True, color=DARK)
for i, (h, t) in enumerate((("1 Kernprodukt kostenlos", "Vergabeweiser zeigt Enden, Bieterzahl, Zuschlagsempfänger"), ("2 Problem eine Setzung", "Engpass eher Preis, Personal, Bürokratie; Nutzen offen"),
                            ("3 Nahe Zukunft fehlt", "Vorgänger meist vor eForms (55 von 68)"), ("4 Ende ist kein Termin", "Verlängerung ist Normalfall; Backtest 28,8 %"),
                            ("5 Markt klein", "grob 3,6–7,2 Mio. € Potenzial, Annahmen offen"))):
    x = 0.5 + i * 1.82
    rect(s, x, 1.4, 1.74, 1.75, PALE, name=h + " Karte")
    rect(s, x, 1.4, 1.74, 0.07, RED, name=h + " Streifen")
    box(s, x + 0.08, 1.52, 1.6, 0.5, h, size=12, bold=True, color=DARK)
    box(s, x + 0.08, 2.05, 1.6, 1.05, t, size=12)
rect(s, 0.5, 3.3, 4.45, 1.7, PALE, name="Bleibt Karte")
rect(s, 0.5, 3.3, 4.45, 0.07, GREEN, name="Bleibt Streifen")
box(s, 0.65, 3.4, 4.2, 1.6, [[("Was bleibt", {"bold": True, "size": 14, "color": DARK})], "• Merkmalsunterschied: Grundlaufzeit statt Höchstende, auf Los- und Definitionsebene (≈ 10 %)", "• Dokumentiertes Prüfverfahren", "• Nische als Hypothese: Datenqualität, Kanal Innung"], size=12, space=3, name="Bleibt Text")
rect(s, 5.05, 3.3, 4.45, 1.7, PALE, name="Nicht belegt Karte")
rect(s, 5.05, 3.3, 4.45, 0.07, AMBER, name="Nicht belegt Streifen")
box(s, 5.2, 3.4, 4.2, 1.6, [[("Nicht belegt", {"bold": True, "size": 14, "color": DARK})], "• Bessere Lesequalität (gleiche Quelle, kein Mensch)", "• Nachfrage und Zahlungsbereitschaft (n = 3)", "• Abdeckung: nur TED, etwa 80 % der Lose"], size=12, space=3, name="Nicht belegt Text")

# 9 KI-Irrwege und Prozessfehler -----------------------------------------------------------------------------
s = new_slide("KI-Irrwege und ein Prozessfehler",
              "ZEIT 1:15. KERNAUSSAGE: Claude Code hat Regeln, Stichproben und Auswertungen mitgebaut; jeder dieser Fehler wurde von einem getrennten Evaluator, im Test oder vom Nutzer gefunden, nicht von der Hand, die ihn gemacht hat. "
              "Vier von 27 Einträgen in docs/ki_irrwege.md: (1) Entwicklung 10–11 von 12 plausibel, im Test 11 von 24 richtig (Iteration 3): Regel verworfen. (2) „Blind“ war nicht blind: Leser der Iteration 8 hatten die Projektbeschreibung im Kontext (CLAUDE.md), gefunden vom Evaluator, offen genannt. "
              "(3) Konkurrenz übersehen: Die Suche vom 24.10. fand keinen deutschen Dienst, tatsächlich gibt es zwei; gefunden vom Recherche-Agenten nach dem Hinweis des Dozenten. (4) Schwelle unerreichbar: Claude übernahm die Diskordanzrate von 17 % aus Iteration 10 für 160 Lose, es waren 9,4 %; gefunden vor den Leserantworten, nicht nachträglich geändert. "
              "LERNPUNKT STATT SCHWÄCHE: „Konkurrenz erst in Iteration 10 gesehen“ ist ein Prozessfehler, kein Pech. Plan G1.1 (Wettbewerber sichten) blieb offen; die Entscheidung gegen Kundenkontakt fiel am 2026-10-29. Kosten: Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos gibt. Lehre: ein Marktgate in Phase 1, vor der Modellierung (Gibt es das schon? Wer zahlt dafür? Nach Gesprächen, nicht nach Annahmen). "
              "FRAGE – ANTWORT: „Warum erst jetzt die Konkurrenz?“ Weil die Sichtung (G1.1) offen blieb und die Suche am 24.10. die Dienste nicht fand; die Suche war zu eng. Das ist ein Prozessfehler im Business Understanding. Er hat Zeit gekostet (Iterationen 5 bis 9), aber das Ergebnis geändert: Wir sagen heute, dass die Liste kein eigenes Produkt ist. "
              "Weitere (nicht auf der Folie): Prüfer und Regel von derselben Hand (Iteration 2), versteckte Felder (65 von 95 „unbekannt“, Iteration 7), Dauerfeld enthält die Option schon (12 Lose, 0,13 % der Liste). Ein eigener Subagent (Evaluator) prüft jede Iteration kritisch. "
              "ZEIG-MIR-WO: docs/ki_irrwege.md, docs/projektplan.md (G1.1), reports/evaluation_iteration10b.md.")
items = [("Entwicklung gut, Test schlecht", "10–11 von 12 plausibel, im Test 11 von 24 richtig (It. 3). Folge: Regel verworfen."),
         ("„Blind“ war nicht blind", "Leser hatten die Projektbeschreibung im Kontext (It. 8). Folge: offen berichtet."),
         ("Konkurrenz übersehen", "Suche vom 24.10. fand keinen deutschen Dienst; es gibt zwei (It. 10). Folge: Business Understanding neu."),
         ("Schwelle unerreichbar", "≥ 16 von höchstens 15 Losen (It. 10b). Folge: nicht geändert, offen berichtet.")]
for i, (h, t) in enumerate(items):
    x, y = 0.5 + (i % 2) * 4.6, 1.15 + (i // 2) * 1.3
    rect(s, x, y, 4.4, 1.2, PALE, name=f"Irrweg {i + 1}")
    box(s, x + 0.2, y + 0.08, 4.0, 0.35, h, size=15, bold=True, color=DARK)
    box(s, x + 0.2, y + 0.48, 4.0, 0.7, t, size=12)
rect(s, 0.5, 3.85, 9.0, 1.1, DARK, name="Lernpunkt Banner")
box(s, 0.7, 3.9, 8.6, 1.0, [[("Lernpunkt, ein Prozessfehler: ", {"bold": True, "color": AMBER}), ("Plan G1.1 (Wettbewerber sichten) blieb offen, am 2026-10-29 fiel die Entscheidung gegen Kundenkontakt. Kosten: Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos gibt. Lehre: Marktgate in Phase 1, vor der Modellierung.", {"color": WHITE})]], size=13, anchor=MSO_ANCHOR.MIDDLE, name="Lernpunkt Text")

# 10 Trennung Entwicklung/Test (Live-Nachweis) ---------------------------------------------------------------
s = new_slide("Trennung von Entwicklung und Test",
              "ZEIT 1:15. KERNAUSSAGE: Hypothese, Kriterien und Seed stehen im Git, bevor die Stichprobe gezogen und die Antworten gelesen werden; die Commit-Reihenfolge ist der Nachweis, dass Test und Entwicklung getrennt sind. Die Folie zeigt die Reihenfolge der Iteration 10b (Kurzfassung der Commit-Nachrichten, im Terminal von unten nach oben lesen). "
              "WAS IN DER FRAGERUNDE LIVE GEZEIGT WIRD: (1) Im Terminal `git log --oneline`: 4f50436 (Hypothese, Kriterien, Skript und Seed 20261112 vorab), 9d63c59 (Stichprobe gezogen, SHA-256 des Schlüssels 2cd00206…3e33; Schlüsseldatei lokal, nicht im Git: data/processed/stichprobe_iteration10b_schluessel.csv), 49bb198 (Skript für Abruf und Auswertung vor dem Abruf), 6b7e8d8 (Paket und Leseskript vor den Antworten), 69917ff (Antworten der Leser unverändert), f6583cc (Auswertung). "
              "(2) Eine Regel in src/prepare/vertragsliste.py öffnen und einen Parameter ändern (z. B. Seed in src/prepare/stichprobe_iteration10b.py): Erwartung: Zahlen ändern sich leicht, die Aussagen bleiben, da die Stichprobe nur 70 bzw. 160 Lose hat. (3) Fehlwerte zeigen: 33 der 130 Oberpfalz-Lose ohne Ende (Stufe F), keine Laufzeitfelder im XML (reports/beispiel_liste_oberpfalz.csv). "
              "Iteration 9 genauso: Regeln a03a4a8, Seed und Skript 4521952, Stichprobe und Auswertungsskript b3b1471, Antworten erst e1726e7. Entwicklungsfälle sind aus der Stichprobe ausgeschlossen (reports/entwicklung_iteration9_notices.txt). "
              "EHRLICHE LÜCKEN: das Lauf-Skript der Iteration-9-Leser wurde erst mit den Antworten committet; in Iteration 8 kannten die Leser den Fehlertyp; in 10b liegt das Protokoll der Leserläufe außerhalb des Repos. Der 10b-Fehler (Schwelle unerreichbar) wurde vor den Leserantworten bemerkt und offengelegt, aber nicht mehr geändert. "
              "ZEIG-MIR-WO: git log, src/prepare/stichprobe_iteration10b.py, docs/reproduzierbarkeit.md.")
rect(s, 0.5, 1.15, 5.9, 2.6, INK, name="Terminal")
box(s, 0.7, 1.25, 5.6, 2.45, [[("$ git log --oneline", {"color": AMBER})],
    "f6583cc Auswertung nach den Lesern", "69917ff Antworten der Leser, unverändert", "6b7e8d8 Paket und Leseskript vor den Antworten",
    "49bb198 Skript für Abruf und Auswertung", "9d63c59 Stichprobe gezogen, Schlüssel-Hash", "4f50436 Hypothese, Kriterien, Seed vorab"],
    size=12, color=WHITE, font="Consolas", space=5, name="Terminal Text")
box(s, 0.5, 3.85, 5.9, 0.5, "Iteration 10b, Kurzfassung der Nachrichten; von unten nach oben lesen", size=12, color=GREY)
rect(s, 6.6, 1.15, 2.9, 2.6, PALE, name="Reihenfolge Karte")
box(s, 6.75, 1.25, 2.6, 2.45, [[("Was die Reihenfolge zeigt", {"bold": True, "color": DARK, "size": 14})], "• Kriterien und Seed vor der Stichprobe", "• Skript vor dem Abruf, Paket vor den Antworten", "• Antworten unverändert, Auswertung zuletzt"], size=12, space=5, name="Reihenfolge Text")
rect(s, 0.5, 4.4, 9.0, 0.6, DARK, name="Live Banner")
box(s, 0.65, 4.4, 8.7, 0.6, [[("In der Fragerunde live: ", {"bold": True, "color": AMBER}), ("git log, Regel in vertragsliste.py ändern, Fehlwerte (Stufe F) zeigen. Lücke: Leseprotokoll von 10b liegt außerhalb des Repos.", {"color": WHITE})]], size=13, anchor=MSO_ANCHOR.MIDDLE, name="Live Text")

# 11 Empfehlung und Grenzen ----------------------------------------------------------------------------------
s = new_slide("Empfehlung und Grenzen",
              "ZEIT 1:30. KERNAUSSAGE: Ampel statt Fazit-Text. GRÜN: Die Liste ist als Ausgangspunkt nutzbar, immer mit Blick in die verlinkte Bekanntmachung: 94,3 % der Zufallslose der Iteration 9 stimmen mit zwei KI-Lesungen überein (Mensch 14 von 15); Merkmal Ende je Los und Grundlaufzeit. Für Betriebe heißt das praktisch: Vertragsenden bei Vergabeweiser nachsehen (kostenlos) und das Enddatum in der Bekanntmachung prüfen, ob Grundlaufzeit oder Höchstende gemeint ist. "
              "GELB: Höchstende nur Hinweis (87,1 %); Abdeckung nur TED und etwa 80 % der Lose; Listenfehler offen (Dauerfeld enthält die Option: 12 von 9.325 Losen; Textmuster „läuft vom … bis … und verlängert sich“); Gespräche n = 3; Leser nicht unabhängig, keine Menschenprüfung der 15 Lose aus 10b. "
              "ROT: Terminprognose (28,8 %); die Liste als eigenes Produkt; Nachfrage, Zahlungsbereitschaft und Qualitätsvorsprung nicht belegt. "
              "TRANSFERFRAGE „Würdet ihr das Produkt bauen?“: Nein, nicht als Liste allein. Wenn weiter, dann ein Gespräch mit mehr größeren Betrieben und Vergabestellen, eine menschliche Gegenlesung und ein Maß, das Definition und Losebene trennt. Neuer Standort oder andere Nische: Pipeline übertragbar, Lese-Regeln neu testen. Doppeltes Volumen: Abruf skaliert, die menschliche Prüfung nicht. "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1 (Befüllungsquote 90 %, Laufzeitende bestimmbar); eine Geschäftsbegründung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/annahmen.md, reports/evaluation_iteration9.md, reports/evaluation_iteration10b.md, docs/business.md §8.9.")
ampel = (("Ja", GREEN, ["Liste „laut Bekanntmachung“ als Ausgangspunkt, Link prüfen", "Ende je Los, Grundlaufzeit statt Höchstende", "94,3 % Übereinstimmung mit zwei KI-Lesern"]),
         ("Mit Vorsicht", AMBER, ["Höchstende nur Hinweis; offene Listenfehler (12 von 9.325)", "Nur TED, etwa 80 % der Lose", "Gespräche n = 3"]),
         ("Nein", RED, ["Terminprognose", "Liste als eigenes Produkt", "Nachfrage, Zahlungsbereitschaft, Qualitätsvorsprung: nicht belegt"]))
for i, (h, f, pts) in enumerate(ampel):
    x = 0.5 + i * 3.1
    rect(s, x, 1.2, 2.9, 3.5, PALE, name=h + " Karte")
    rect(s, x + 0.2, 1.35, 0.4, 0.4, f, MSO_SHAPE.OVAL, h + " Signal")
    box(s, x + 0.75, 1.35, 2.05, 0.4, h, size=16, bold=True, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 2.0, 2.55, 2.6, ["• " + p for p in pts], size=13, space=8)
box(s, 0.5, 4.85, 8.5, 0.3, "Quellen: reports/evaluation_iteration9.md und 10b, docs/business.md §8", size=10, color=GREY)

# 12 Fazit ------------------------------------------------------------------------------------------------
s = new_slide("", "ZEIT 0:45. KERNAUSSAGE in einem Satz wiederholen, dann Brücke zur Fragenrunde. Gesamtzeit: 15:00 (Ziel ±30 Sekunden); Zeitbudget je Folie: 0:30 / 1:00 / 1:15 / 1:15 / 1:30 / 1:45 / 1:30 / 1:30 / 1:15 / 1:15 / 1:30 / 0:45 (Business Understanding Folien 5 bis 8: 6:15 = 42 %). "
              "Satz zum Mitnehmen: Den Termin einer Neuausschreibung sagen TED-Daten nicht vorher; eine Liste der Vertragsenden lässt sich lesen, ist aber kein eigenes Produkt, solange Vergabeweiser sie kostenlos bietet. Lehre: Marktgate in Phase 1, vor der Modellierung. "
              "FRAGENRUNDE vorbereiten: (1) Methodenfrage: warum ±3 Monate, warum diese Baseline, warum KI-Leser als Maß, warum nur diskordante Lose (Folien 3, 4, 7). (2) Live-Nachweis: git log und die Reihenfolge der Commits zeigen, Seed und Schlüssel-Hash (Folie 10), Regel in src/prepare/vertragsliste.py öffnen, Fehlwerte (Stufe F) in reports/beispiel_liste_oberpfalz.csv zeigen. "
              "(3) Transferfrage: „Warum nicht Vergabeweiser nutzen?“ (Folie 6), „Warum erst jetzt die Konkurrenz?“ (Folie 9), „Wer zahlt?“ (Folie 5), „Warum ist W8a verfehlt?“ (Folie 7), anderer Standort, andere Nische, doppeltes Volumen (Folie 8 und 11). Nicht sagen: „genauer als Vergabeweiser“, „Vorsprung belegt“ ohne den Zusatz „auf Los- und Definitionsebene“, „kein Unterschied“.", dark=True)
box(s, 0.6, 0.5, 8.8, 0.8, "Fazit", size=36, bold=True, color=AMBER, font=HEAD, name="Fazit Titel")
box(s, 0.6, 1.4, 8.8, 2.5, "TED-Daten sagen den Termin einer Neuausschreibung nicht vorher (28,8 % statt 60 %). Eine Liste der Vertragsenden lässt sich daraus lesen: 94,3 % Übereinstimmung mit zwei KI-Lesern. "
    "Ein eigenes Produkt ist sie nicht, denn Vergabeweiser bietet sie kostenlos. Ein Unterschied bleibt auf Los- und Definitionsebene (Grundlaufzeit statt Höchstende, rund 10 % der Lose); "
    "bessere Lesequalität ist nicht belegt, Nachfrage und Zahlungsbereitschaft sind offen. Lehre: Marktgate in Phase 1, vor der Modellierung.", size=18, color=WHITE, name="Kernbotschaft")
box(s, 0.6, 4.0, 8.8, 1.0, [[("Nächster Schritt: ", {"bold": True, "color": AMBER}), ("menschliche Gegenlesung der 15 Lose und mehr Gespräche mit größeren Betrieben und Vergabestellen", {"color": SOFT})]], size=16, name="Nächster Schritt")

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(len(prs.slides), "Folien;", OUT)
