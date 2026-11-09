"""Foliengerüst für den Vortrag (LN B: 15 min Vortrag + 5 min Fragen, höchstens 12 Inhaltsfolien) mit Sprechernotizen.

Stand nach Iteration 10/10b, Business-Case-Prüfung und Nachtrag Sensitivität (2026-11-09). Gestaltung im Apple-/Keynote-Stil: Titel als Aussagesatz
(höchstens 2 Zeilen), viel Weißraum, weiße Karten auf hellgrauem Grund (F2F2F7), Systemfarben mit fester Bedeutung (Grün = erfüllt/gut,
Rot = verfehlt, Orange = Vorsicht, Blau = neutral/Hervorhebung; dunkle Karte nur für die Publikumsfrage auf Folie 3), Schrift Segoe UI.
Text mindestens 14 pt; Fußnoten und Abschnittszeile 11 pt, Fußnoten einzeilig, ohne Dateipfade (Pfade stehen in den Notizen).
Oben auf jeder Inhaltsfolie eine graue Abschnittszeile (Idee · Betriebe · Markt · Produkt · Prüfung · Fazit), der aktuelle Abschnitt blau.
Unten der Kasten „Kurz gesagt:“ mit der Folgerung für Laien. Notizen je Folie: ZEIT, KERNAUSSAGE, FRAGE – ANTWORT, ZEIG-MIR-WO, KURZ GESAGT.
Summe der Zeiten der sichtbaren Folien: 15:00.

Folien (11 sichtbar, 3 ausgeblendet):
   1 Titel (0:30)
   2 Video „Franz und die Glaskugel“ (3:30, Video ca. 3 Minuten mit Quizfrage)
   3 Betriebe heute und unsere Idee (1:45, mit Publikumsfrage)
   4 Konkurrenz: Vergabeweiser kostenlos (1:15)
   5 Vergleich mit Vergabeweiser (1:15)
   6 Make or Buy aus Sicht des Betriebs (1:30)
   7 Demo als Zielbild (1:00, Bildschirmaufnahme)
   8 So funktioniert es technisch: Pipeline und Prognoseregel (1:00)
   9 KI-Irrwege und Trennung von Entwicklung und Test (1:15)
  10 Empfehlung und Grenzen (1:15)
  11 Fazit (0:45)
  12–14 ausgeblendeter Anhang für die Fragerunde (Frage/Kriterium/Daten, Irrwege, Liste und Genauigkeit)
Option --ohne-anhang lässt den Anhang weg. Das Video wird eingebettet, sobald docs/video/franz_und_die_glaskugel_szenen_0-5_v4.mp4 existiert
(Rückfall v3, v2, v1). Zahlen aus docs/iterationen.md, docs/business.md §7 bis §9, docs/business_case_auswahl.md, docs/demo_push.md,
reports/evaluation_iteration5.md bis 10b, reports/sensitivitaet_iteration5.md, docs/lab_log.md.
Aufruf:  .venv\\Scripts\\python.exe -I src/report/vortrag.py [--ohne-anhang] [Ausgabepfad]      Ausgabe: docs/vortrag/vortrag_vergabe_radar.pptx
"""

import sys
from pathlib import Path

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "docs" / "vortrag" / "vortrag_vergabe_radar.pptx"

# Apple Human Interface Guidelines: Systemfarben, ruhige Flächen, runde Karten, Systemschrift
DARK, BLUE, AMBER, RED, GREEN, GREY, PALE, INK, WHITE, SOFT, LBLUE, DBLUE, LINE = (RGBColor.from_string(h) for h in
    ("1C1C1E", "007AFF", "FF9F0A", "FF3B30", "34C759", "6E6E73", "F2F2F7", "1C1C1E", "FFFFFF", "AEAEB2", "E5F1FF", "0062CC", "D1D1D6"))
DAMBER = RGBColor.from_string("B25E00")   # Orange als Schrift (lesbar auf Weiß)
DGREEN = RGBColor.from_string("248A3D")   # Grün als Schrift (lesbar auf Weiß)
HEAD, BODY, MONO = "Segoe UI Semibold", "Segoe UI", "Consolas"   # Ersatz für San Francisco unter Windows

ABSCHNITTE = ("Idee", "Betriebe", "Markt", "Produkt", "Prüfung", "Fazit")

# Kernaussage je Folie (Titel als Aussagesatz, höchstens 2 Zeilen)
TITEL = [None,
    "",
    "Video: Was TED vorhersagt und was nicht",
    "Ein Betrieb hatte nur 28 Tage für sein Angebot; wir wollten Monate daraus machen",
    "Eine solche Liste gibt es schon, kostenlos bei Vergabeweiser",
    "Bei 27 von 230 Losen weichen wir von Vergabeweiser ab, meist wegen der Zählweise",
    "Im Modell lohnt Selbstbauen nicht; offen ist nur, ob Betriebe die Daten im eigenen System brauchen",
    "So hätte das Produkt aussehen sollen: passende Hinweise direkt an die Firma",
    "So funktioniert es technisch: von der TED-Abfrage zur geprüften Liste",
    "Die KI machte Fehler; gefunden wurden sie durch getrennte Prüfung",
    "Nutzbar als Ausgangspunkt, aber nicht als eigenes Produkt",
    "",
    # ausgeblendeter Anhang (Folien 12 bis 14)
    "Wer früh weiß, wann ein Auftrag endet, kann sich besser vorbereiten",
    "Den Termin der Neuausschreibung kann TED nicht vorhersagen",
    "Das Vertragsende lässt sich meist lesen: 66 von 70 wie zwei KI-Leser",
]

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(10), Inches(5.625)
LAYOUT_TITLE_ONLY = prs.slide_layouts[5]
LAYOUT_BLANK = prs.slide_layouts[6]
_nr = [0]


def box(s, x, y, w, h, paras, size=14, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font=BODY, name=None, space=0):
    """Textfeld. paras: str oder Liste von Absätzen; ein Absatz ist str oder Liste von (Text, {bold, color, size, font})."""
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


def rect(s, x, y, w, h, fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, name=None, radius=0.16):
    """Fläche; Rechtecke werden zu Karten mit runden Ecken."""
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = min(radius / min(w, h), 0.5)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.fill.background()
    sh.shadow.inherit = False
    if name:
        sh.name = name
    return sh


def kreis(s, x, y, d, fill, text="", size=16, color=WHITE, name=None):
    rect(s, x, y, d, d, fill, MSO_SHAPE.OVAL, name)
    if text:
        box(s, x, y, d, d, text, size=size, bold=True, color=color, font=HEAD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def pfeil(s, x, y, w=0.22, h=0.22, richtung="rechts", farbe=SOFT, name="Pfeil"):
    form = {"rechts": MSO_SHAPE.RIGHT_ARROW, "links": MSO_SHAPE.LEFT_ARROW, "unten": MSO_SHAPE.DOWN_ARROW}[richtung]
    rect(s, x, y, w, h, farbe, form, name)


def abschnitt(s, aktiv):
    """Graue Abschnittszeile oben; der aktuelle Abschnitt fett und blau (aktiv = None: Anhang)."""
    if aktiv is None:
        box(s, 0.6, 0.1, 8.8, 0.22, [[("Anhang für die Fragerunde", {"color": GREY})]], size=11, name="Abschnitt")
        return
    runs = []
    for i, a in enumerate(ABSCHNITTE):
        if i:
            runs.append(("  ·  ", {"color": SOFT}))
        runs.append((a, {"color": BLUE, "bold": True} if a == aktiv else {"color": GREY}))
    box(s, 0.6, 0.1, 8.8, 0.22, [runs], size=11, name="Abschnitt")


def new_slide(notes, dark=False, teil="anhang"):
    s = prs.slides.add_slide(LAYOUT_BLANK if dark else LAYOUT_TITLE_ONLY)
    _nr[0] += 1
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = PALE   # alle Folien hell (einheitlich); dark=True nur noch: Folie ohne Titelplatzhalter
    if not dark:
        t = s.shapes.title
        t.left, t.top, t.width, t.height = Inches(0.6), Inches(0.4), Inches(8.8), Inches(0.9)
        tf = t.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.TOP
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run()
        r.text = TITEL[_nr[0]]
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = HEAD, Pt(26), False, DARK
    if teil != "titel":
        abschnitt(s, None if teil == "anhang" else teil)
    box(s, 9.0, 5.25, 0.5, 0.25, str(_nr[0]), size=11, color=GREY, align=PP_ALIGN.RIGHT, name="Foliennummer")
    s.notes_slide.notes_text_frame.text = notes
    return s


def kurz(s, text, x=0.6, y=4.3, w=8.8, h=0.55):
    """Kasten „Kurz gesagt:“ mit der Folgerung für Laien; derselbe Satz kommt in die Notizen."""
    rect(s, x, y, w, h, LBLUE, radius=min(0.275, h / 2), name="Kurz gesagt Pille")
    box(s, x + 0.25, y, w - 0.45, h, [[("Kurz gesagt: ", {"bold": True, "color": DBLUE}), (text, {"color": DBLUE})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Kurz gesagt Satz")
    tf = s.notes_slide.notes_text_frame
    tf.text = tf.text + " KURZ GESAGT (für Laien, steht auf der Folie): " + text


def fuss(s, text):
    """Fußnote, einzeilig, ohne Dateipfade."""
    box(s, 0.6, 4.97, 8.3, 0.25, text, size=11, color=GREY, name="Fußnote")


def tile(s, x, y, w, h, zahl, label, farbe, name, zsize=32):
    rect(s, x, y, w, h, WHITE, name=name + " Karte")
    box(s, x + 0.2, y + 0.1, w - 0.4, 0.62, zahl, size=zsize, color=farbe, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name=name + " Zahl")
    box(s, x + 0.2, y + 0.76, w - 0.4, h - 0.8, label, size=14, name=name + " Text")


def balken(s, x, y, w, h, kategorien, werte, farben, name, maximum=118, fmt='0.0" %"'):
    cd = CategoryChartData()
    cd.categories = kategorien
    cd.add_series(name, werte)
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf.name = name
    ch = gf.chart
    ch.has_legend = False
    ch.has_title = False
    ch.font.size, ch.font.name, ch.font.color.rgb = Pt(14), BODY, INK
    ca, va = ch.category_axis, ch.value_axis
    ca.reverse_order = True
    ca.format.line.fill.background()
    ca.has_major_gridlines = False
    va.visible = False
    va.has_major_gridlines = False
    va.minimum_scale, va.maximum_scale = 0, maximum
    plot = ch.plots[0]
    plot.gap_width = 55
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.number_format, dl.number_format_is_linked = fmt, False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.size, dl.font.bold, dl.font.color.rgb = Pt(14), True, INK
    for i, f in enumerate(farben):
        pt = plot.series[0].points[i]
        pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = f



# Folie 1: Titel ------------------------------------------------------------
s = new_slide("ZEIT 0:30. KERNAUSSAGE: Eine Reinigungsfirma will früh wissen, wann ein öffentlicher Vertrag endet und neu ausgeschrieben wird. Wir zeigen, was TED-Daten dazu hergeben "
              "(eine Liste der Vertragsenden), was nicht (eine Terminprognose), und was an der Idee gegenüber der kostenlosen Konkurrenz übrig bleibt. "
              "Ablauf in einem Satz: ein Video von ca. 3 Minuten (Franz und die Glaskugel: Frage, zwei Irrwege, Liste samt Genauigkeit), dann der längere Teil aus Sicht eines Betriebs: "
              "Wie arbeiten Betriebe, was war unsere Idee, wer bietet es schon, was hätte das Produkt sein sollen, wie funktioniert es technisch, was bleibt. "
              "Kernbotschaft schon jetzt nennen: Die Liste lässt sich aus TED lesen, ein eigenes Produkt ist sie nicht, und ein Qualitätsvorsprung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/iterationen.md (Übersicht und Ergebnis Iteration 10 und 10b), docs/lab_log.md Abschnitt 0.", dark=True, teil="titel")

# Radar-Grafik: Kreise um einen Mittelpunkt
rect(s, 6.1, 0.9, 3.4, 3.4, RGBColor.from_string("DCEBFF"), MSO_SHAPE.OVAL, "Radar außen")
rect(s, 6.6, 1.4, 2.4, 2.4, RGBColor.from_string("B3D4FF"), MSO_SHAPE.OVAL, "Radar mitte")
rect(s, 7.1, 1.9, 1.4, 1.4, BLUE, MSO_SHAPE.OVAL, "Radar innen")
rect(s, 8.15, 1.55, 0.3, 0.3, AMBER, MSO_SHAPE.OVAL, "Radar Punkt")
box(s, 0.6, 1.35, 5.2, 1.0, "Vergabe-Radar", size=48, color=INK, font=HEAD, name="Titel")
box(s, 0.6, 2.4, 5.1, 1.2, "Wann endet ein öffentlicher Auftrag, und wer weiß es schon?", size=24, color=GREY, name="Untertitel")
box(s, 0.6, 3.75, 5.1, 0.6, "Was die EU-Plattform TED verrät und was nicht", size=16, color=BLUE, name="Zusatz")
box(s, 0.6, 4.65, 8.4, 0.3, "Manuel Strobel · Ludwig Richthammer", size=16, color=INK, font=HEAD, name="Namen")
box(s, 0.6, 5.0, 8.0, 0.3, "Big Data Analytics · Leistungsnachweis B", size=14, color=GREY, name="Autoren")
s.notes_slide.notes_text_frame.text += " KURZ GESAGT (für Laien): Wir haben geprüft, ob man aus öffentlichen Daten vorhersagen kann, wann ein Reinigungsauftrag neu ausgeschrieben wird."

# Folie 2: Video ---------------------------------------------------------
VIDEO = ROOT / "docs" / "video" / "franz_und_die_glaskugel_szenen_0-5_v4.mp4"   # v4: Edge-Stimmen (Microsoft Neural), sonst wie v3
if not VIDEO.exists():
    VIDEO = ROOT / "docs" / "video" / "franz_und_die_glaskugel_szenen_0-5_v3.mp4"
if not VIDEO.exists():  # Fallback auf v2 (Piper-Stimme), dann v1 (SAPI-Stimme)
    VIDEO = ROOT / "docs" / "video" / "franz_und_die_glaskugel_szenen_0-5_v2.mp4"
if not VIDEO.exists():
    VIDEO = ROOT / "docs" / "video" / "franz_und_die_glaskugel_szenen_0-5.mp4"
POSTER = ROOT / "docs" / "vortrag" / "poster_franz_und_die_glaskugel.png"


def poster_erzeugen(pfad):
    """Posterbild 1600x900 aus der Foliengestaltung (dunkle Fläche, Glaskugel, Abspielzeichen)."""
    from PIL import Image, ImageDraw, ImageFont
    w, h = 1600, 900
    im = Image.new("RGB", (w, h), (28, 28, 30))
    d = ImageDraw.Draw(im)
    d.ellipse((1000, 160, 1480, 640), fill=(44, 44, 46))
    d.ellipse((1080, 240, 1400, 560), fill=(58, 58, 60))
    d.ellipse((1160, 320, 1320, 480), fill=(0, 122, 255))
    d.ellipse((1290, 270, 1340, 320), fill=(255, 159, 10))
    try:
        f1 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 92)
        f2 = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 44)
    except OSError:
        f1 = f2 = ImageFont.load_default()
    d.text((100, 300), "Franz und", font=f1, fill=(255, 255, 255))
    d.text((100, 410), "die Glaskugel", font=f1, fill=(255, 255, 255))
    d.text((100, 560), "Szenen 0 bis 5 · ca. 3 Minuten", font=f2, fill=(174, 174, 178))
    d.polygon([(100, 700), (100, 790), (180, 745)], fill=(0, 122, 255))
    d.text((210, 715), "Abspielen", font=f2, fill=(0, 122, 255))
    pfad.parent.mkdir(parents=True, exist_ok=True)
    im.save(pfad)


s = new_slide("ZEIT 3:30 (Video ca. 3 Minuten inklusive Pause für die Quizfrage; dazu Einleitung und Überleitung etwa 0:30; das Video wird noch optimiert, die Länge kann sich leicht ändern). "
              "KERNAUSSAGE: Das Video „Franz und die Glaskugel“ erzählt die ersten Zyklen des Projekts in drei Runden: "
              "Problem (Franz, Gebäudereiniger, erfährt zu spät, wann Verträge enden), Idee (TED-Daten), Runde 1: Vorgänger finden, 11 von 24 (Schwelle verfehlt), "
              "Runde 2: die Glaskugel „spätestes Vertragsende minus 6 Monate“ (Regel R1: Höchstende, also Ende mit allen Verlängerungen, minus 6 Monate), 28,8 % statt der geforderten 60 %, "
              "Runde 3: die Vertragsliste, 66 von 70 Stichproben mit gleichem Enddatum wie zwei KI-Leser. Es ersetzt die Folien Frage/Kriterium/Daten, Irrwege, Liste und Genauigkeit (ausgeblendet am Ende, Folien 12 bis 14). "
              "ABLAUF: (1) Einleitung 15 Sekunden: „Drei Minuten Video, in der Mitte eine Frage an euch.“ Daten und Kriterium in einem Satz sagen: TED, Gebäudereinigung, Deutschland, Daten ab Okt. 2016 (Liste: eForms ab Okt. 2023), "
              "Treffer = Neuausschreibung im Fenster ±3 Monate, Schwelle 60 % vorab festgelegt; einfache Vergleichsregel R0 „Ende der Grundlaufzeit minus 6 Monate“ schafft 17,3 %. "
              "(2) Video starten (Folie anklicken, Wiedergabe). (3) QUIZFRAGE LIVE in der Mitte, Video anhalten: „Wie oft lag die Regel ‚spätestes Vertragsende minus 6 Monate‘ richtig? Ziel waren 60 %.“ "
              "Handzeichen oder Zuruf, 20 Sekunden; dann Video weiter: Auflösung 28,8 %. "
              "(4) Überleitung nach dem Video, 15 Sekunden: „Franz hat also eine Liste statt einer Glaskugel. Schauen wir, wie Betriebe heute arbeiten und was wir ihnen bieten wollten.“ "
              "SICHERUNG, falls das Video nicht läuft: die drei Karten rechts nennen die Kernzahlen (11 von 24 · 28,8 % statt 60 % · 66 von 70); die Geschichte in 60 Sekunden frei erzählen, Quizfrage trotzdem stellen. Details in den ausgeblendeten Folien 12 bis 14. "
              "HINWEISE: Die Animation hat Manuel Strobel KI-gestützt erstellt; Ludwig Richthammer und Manuel Strobel haben sie abwechselnd überarbeitet (Zahlen gegen Belege geprüft, zu starke Sätze eingeschränkt). Stimmen synthetisch, Figuren erfunden. Das im Vortrag offen sagen. "
              "EHRLICHE EINSCHRÄNKUNGEN (bei Nachfrage oder in einem Satz am Ende): Die Figuren (Franz) sind erfunden, die Gespräche sind im Video nachgestellt (die drei echten Telefongespräche, n = 3, sind nur Hinweise, keine Belege). "
              "Die 66 von 70 heißen nur: gleiches Enddatum wie der Vergleichswert zweier KI-Leser; die Leser sind nicht unabhängig (gleiche Modellfamilie), und ihr Vergleichswert ist teils zirkulär (er nutzt wie die Liste das Feld als Ende der Grundlaufzeit); "
              "dazu prüfte ein Kommilitone 15 Lose, 14 stimmen. Der Vergleichswert 17,3 % der Terminprognose ist dagegen die einfache Regel R0 auf denselben 52 Paaren; die Paare stammen aus einer Rückwärtssuche. "
              "Ein Qualitätsvorsprung gegenüber der Konkurrenz ist nicht belegt (Folien 4 und 5). "
              "FRAGE – ANTWORT: „Warum ±3 Monate, warum 60 %?“ Das Fenster und die Schwelle wurden vor der Rechnung gesetzt, ohne Kundenkontakt, begründete Setzung (Anhang Folie 12). "
              "Nachträglich, kein neuer Test: Auch mit dem im Nachhinein besten Vorlauf bleibt R1 bei 28,8 % (Folie 8). "
              "„Waren die 66 von 70 nicht vom Entwickler selbst bewertet?“ Nein, neue Stichprobe, Rohtext ohne Projektkontext, aber KI-Leser nicht unabhängig (Folie 9, Anhang Folie 14). "
              "ZEIG-MIR-WO: docs/video/franz_und_die_glaskugel_szenen_0-5_v4.mp4, docs/video/README.md (Korrekturen), docs/iterationen.md, reports/backtest_iteration5.md, reports/evaluation_iteration3.md bis 9, Anhang Folien 12 bis 14.",
              teil="Idee")
if VIDEO.exists():
    poster_erzeugen(POSTER)
    s.shapes.add_movie(str(VIDEO), Inches(0.6), Inches(1.4), Inches(4.97), Inches(2.8), poster_frame_image=str(POSTER), mime_type="video/mp4").name = "Video Franz und die Glaskugel"
    VIDEO_STATUS = "eingebettet"
else:
    rect(s, 0.6, 1.4, 4.97, 2.8, DARK, name="Video Platzhalter")
    box(s, 0.85, 1.6, 4.5, 2.4, [[("Video hier einbetten", {"bold": True, "color": AMBER, "size": 20, "font": HEAD})],
        [("Datei noch nicht vorhanden. Skript erneut ausführen, dann wird das Video automatisch eingebettet.", {"color": SOFT, "size": 14})]],
        space=10, anchor=MSO_ANCHOR.MIDDLE, name="Video Platzhalter Text")
    VIDEO_STATUS = "Platzhalter"
for i, (zahl, text, f) in enumerate((("11 von 24", "Vorgänger gefunden: Runde 1 verfehlt", RED),
                                      ("28,8 % statt 60 %", "„Spätestes Vertragsende − 6 Monate“", RED),
                                      ("66 von 70", "gleiches Enddatum wie zwei KI-Leser", GREEN))):
    y = 1.4 + i * 0.955
    rect(s, 5.77, y, 3.63, 0.89, WHITE, name=f"Kernzahl {i + 1} Karte")
    box(s, 5.97, y + 0.06, 3.3, 0.45, zahl, size=22, color=f, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name=f"Kernzahl {i + 1} Zahl")
    box(s, 5.97, y + 0.52, 3.3, 0.33, text, size=14, name=f"Kernzahl {i + 1} Text")
kurz(s, "Wann neu ausgeschrieben wird, sagt niemand voraus; wann ein Vertrag endet, lässt sich meist lesen.")
fuss(s, "Animation: Manuel Strobel (KI-gestützt), gemeinsam überarbeitet; Stimmen synthetisch, Figuren erfunden.")


# Folie 3: Betriebe heute und unsere Idee ----------------------------------------
s = new_slide("ZEIT 1:45. KERNAUSSAGE: Ab hier der Teil, den wir zu knapp behandelt hatten: das Business Understanding aus Sicht eines Gebäudereinigers (Folien 3 bis 7, zusammen 6:45 = 45 % der Zeit). "
              "Zuerst, wie Betriebe heute vorgehen und was unsere Idee für sie war, dann die Konkurrenz. "
              "OBERE REIHE, PROZESS (Fakten, drei Gespräche des Nutzers am 2026-11-05; 9 Anrufe, 3 erreicht, 105 Minuten; Notizen ohne Namen; n = 3, Hinweise, keine Belege): Betrieb mittlerer Größe (rund 120 Beschäftigte): "
              "Meldung der Ausschreibung 28 Tage vor Abgabe; eng bei der Objektbegehung (ein Termin, der beste Vorarbeiter krank); Kalkulation nachts; Entscheidung mitzubieten „hauptsächlich Entfernung und Personal“; "
              "Vertragsenden bei anderen „eine Blackbox“. Kleinbetrieb (rund 15 Beschäftigte): Entscheidung nach Kapazität des Teams; die Bürokratie (viele Eigenerklärungen) ist der Engpass. "
              "Vergabestelle: plant etwa 9 Monate vor Vertragsende, verlängert „fast immer, wenn eine Option im Vertrag steht“, vergibt „sehr oft“ unterhalb der EU-Schwelle (also nicht auf TED). "
              "MITTLERE KARTE, UNSERE IDEE (so steht es in den Quellen): (1) Zuschläge enthalten meist ein Vertragsende oder eine Laufzeit (Annahme A4, bestätigt: Gebäudereinigung 90,0 %). "
              "(2) Also ist das Vertragsende bekannt. (3) Annahme A8: „Eine Neuausschreibung erscheint ungefähr zum Vertragsende minus einer typischen Vorlaufzeit.“ "
              "(4) Nutzen laut fachlichem Kriterium (docs/business.md §7.1): „Der Betrieb kann Angebot, Referenzen und Personal gezielt vorbereiten, statt Bekanntmachungen dauernd zu beobachten.“ "
              "Also statt rund 28 Tagen ab Meldung Monate für Begehung, Kalkulation, Personal und Referenzen. Gespräch 1 bestätigt den Wunsch („Absolut“: Personal in der Zielregion früher suchen), der Kleinbetrieb nicht („Eigentlich nicht“). "
              "Ehrlich: A8 wurde in Iteration 5 widerlegt (28,8 %, Video); A1 und A15 (Betriebe wollen früh wissen und zahlen dafür) sind ungeprüft. "
              "PUBLIKUMSFRAGE (dunkle Karte, am Ende der Folie; 20 Sekunden, Handzeichen): „Gibt es kostenlos eine Liste auslaufender öffentlicher Verträge?“ Ja / nein / weiß nicht. Auflösung auf Folie 4: Ja, Vergabeweiser. "
              "Zwischenstand: 4:00 nach Folie 2, 5:45 nach Folie 3; liegt ihr hinten, die Frage als Satz überspringen und direkt auf Folie 4 auflösen. "
              "KOSTEN der Suche (nicht auf der Folie): Portal-Abo des mittleren Betriebs knapp 1.500 € im Jahr (DTAD, Suchprofile); Dienste wie subreport 84–198 € im Monat (Recherche, nicht einzeln nachgeprüft). Der Kleinbetrieb zahlt für nichts in dem Bereich. "
              "FRAGE – ANTWORT: „Wer zahlt?“ Gespräche n = 3: Der größere Betrieb würde für den aktuellen Auftragnehmer und alte Preise zahlen, die Enddaten nannte er „nett für die Planung“; der Kleinbetrieb für nichts. "
              "Ein Betrag wurde nicht genannt. Preisanker der Konkurrenz: 0 bis 200 € im Monat. Ehrlich: Zahlungsbereitschaft ist nicht belegt (Folie 6). "
              "„Sind die Gespräche anonym?“ Ja. Keine Namen von Personen oder Firmen, die Betriebe sind nur beschrieben. "
              "ZEIG-MIR-WO: docs/business.md §7.1 (Nutzen und Schwelle), §8.1 (wie Betriebe an Aufträge kommen), §8.9 (Gespräche), docs/annahmen.md (A1, A4, A8, A15).",
              teil="Betriebe")

schritte = (("Meldung", "Hinweis kommt 28 Tage vor Abgabe"), ("Begehung", "Nur ein Termin vor Ort"),
            ("Kalkulation", "Nachts, unter Zeitdruck"), ("Entscheidung", "Entfernung, Personal, Bürokratie"))
for i, (h, t) in enumerate(schritte):
    x = 0.6 + i * (2.1 + 0.4 / 3)
    rect(s, x, 1.4, 2.1, 1.08, WHITE, name=h + " Karte")
    kreis(s, x + 0.15, 1.5, 0.36, GREY, str(i + 1), size=13)
    box(s, x + 0.6, 1.5, 1.4, 0.36, h, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.15, 1.92, 1.85, 0.52, t, size=14)
# Unsere Idee: Kette mit Pfeilen
rect(s, 0.6, 2.58, 8.8, 1.02, WHITE, name="Idee Karte")
box(s, 0.8, 2.63, 8.4, 0.28, [[("Unsere Idee ", {"bold": True, "color": BLUE}), ("(warum wir eine Prognose für möglich hielten)", {"color": GREY})]], size=14, name="Idee Kopf")
kette = ("Der Zuschlag nennt die Laufzeit", "Also ist das Ende bekannt","Ausschreibung ≈ Ende minus Vorlauf", "Monate Vorlauf statt 28 Tage")
bw, gap = 1.92, 0.24
for i, t in enumerate(kette):
    x = 0.8 + i * (bw + gap)
    letzte = i == len(kette) - 1
    rect(s, x, 2.96, bw, 0.56, BLUE if letzte else LBLUE, radius=0.1, name=f"Idee Schritt {i + 1}")
    box(s, x + 0.08, 2.96, bw - 0.16, 0.56, t, size=14, bold=letzte, color=WHITE if letzte else DBLUE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if not letzte:
        pfeil(s, x + bw + 0.03, 3.13, 0.18, 0.22, name=f"Idee Pfeil {i + 1}")
rect(s, 0.6, 3.7, 8.8, 0.5, DARK, name="Publikumsfrage Karte")
box(s, 0.85, 3.7, 8.4, 0.5, [[("Frage an euch: ", {"bold": True, "color": AMBER}), ("Gibt es kostenlos eine Liste auslaufender öffentlicher Verträge?", {"color": WHITE})]],
    size=14, anchor=MSO_ANCHOR.MIDDLE, name="Publikumsfrage")
kurz(s, "Mehr Vorlauf hieße Zeit für Begehung, Kalkulation und Personal (Annahme).")
fuss(s, "Drei Telefongespräche (n = 3: mittlerer Betrieb, Kleinbetrieb, Vergabestelle): Hinweise, keine Belege.")

# Folie 4: Konkurrenz ------------------------------------------------------------
s = new_slide("ZEIT 1:15. KERNAUSSAGE: Auflösung der Publikumsfrage: Ja, es gibt sie kostenlos. Vergabeweiser listet 1.005 Gebäudereinigungs-Verträge, die in 12 Monaten enden, mit Zuschlagsempfänger, Zahl der Angebote und Verlängerungsoptionen, "
              "nach eigener Angabe auch unterhalb der EU-Schwelle (von uns nicht gemessen). "
              "TABELLE (Prüfstand): Vergabeweiser und die Vertragsende-Seite von AusschreibungsRadar hat Claude am 2026-11-05 selbst nachgelesen; AusschreibungsRadar: 0 bis 149 € im Monat, KI-Eignungsanalyse ab 29 €, Bid/No-Bid-Check mit Match-Score ab 79 € (Preise aus der Recherche); "
              "aufträge.io (43.373 Verträge mit Ende in 12 Monaten, auf Anfrage) und subreport (84–198 € im Monat) stammen aus der Recherche eines Agenten und sind nicht einzeln nachgeprüft; "
              "DTAD nach Aussage des Betriebs mittlerer Größe: knapp 1.500 € im Jahr, eine Liste auslaufender Verträge kenne er dort nicht. Beide geprüften deutschen Anbieter schreiben selbst, dass der Auftraggeber über die Neuausschreibung entscheidet. "
              "HINWEIS (Fakt, Paket A, 130 Oberpfalz-Lose): Auftragnehmer genannt bei 99,2 %, Zuschlagswert über 1 € nur bei 47,7 %, Zahl der Angebote bei 60,8 %. TED-Daten allein reichen für Preisbenchmarks also nur zur Hälfte. "
              "Beobachtung (Hypothese, n = 3): Zwei Betriebe nutzen keinen der Dienste, einer kannte sie vom Hörensagen, die andere gar nicht: eher ein Bekanntheits- als ein Angebotsproblem der Konkurrenz. "
              "FRAGE – ANTWORT: „Warum nicht einfach Vergabeweiser nutzen?“ Doch, für die Suche nach Vertragsenden spricht vieles dafür: kostenlos, nach eigener Angabe auch unterschwellige Verfahren, Zuschlagsempfänger und Bieterzahl. "
              "Unsere Liste ist als eigenes Produkt nicht tragfähig; die Sicht des Betriebs (selbst bauen) steht auf Folie 6. "
              "ZEIG-MIR-WO: docs/business.md §8.2 (Wettbewerber), §8.7 (Marktzahlen), reports/nebentest_ausschreibungsradar.md, reports/wettbewerbsbild_oberpfalz.md.",
              teil="Markt")

box(s, 0.6, 1.42, 8.8, 0.5, [[("Vergabeweiser: ", {"bold": True}), ("1.005 Reinigungsverträge enden in den nächsten 12 Monaten, mit Auftragnehmer und Zahl der Angebote.", {})]], size=14, name="Vergabeweiser Satz")
zeilen = (("Vergabeweiser", "kostenlos", "nachgelesen"), ("AusschreibungsRadar", "0–149 € im Monat", "Funktion nachgelesen"),
          ("subreport", "84–198 € im Monat", "Recherche"), ("DTAD", "rund 1.500 € im Jahr", "Gespräch"),
          ("aufträge.io", "auf Anfrage", "Recherche"))
for i, (n, p, t) in enumerate(zeilen):
    y = 1.95 + i * 0.45
    rect(s, 0.6, y, 8.8, 0.4, WHITE, radius=0.12, name=n + " Zeile")
    box(s, 0.8, y, 2.6, 0.4, n, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 3.5, y, 3.0, 0.4, p, size=14, bold=(i == 0), color=BLUE if i == 0 else INK, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 6.6, y, 2.7, 0.4, t, size=14, color=GREY, anchor=MSO_ANCHOR.MIDDLE)
kurz(s, "Wer nur Vertragsenden sucht, braucht kein Abo.")
fuss(s, "nachgelesen = Anbieterseite selbst gelesen · Recherche = nicht einzeln geprüft · Gespräch = Aussage eines Betriebs")

# Folie 5: Vergleich mit Vergabeweiser ------------------------------------------------------------
s = new_slide("ZEIT 1:15. KERNAUSSAGE: Wir haben vorab festgelegt und dann geprüft, ob unsere Liste das Ende der Grundlaufzeit häufiger trifft als Vergabeweiser. "
              "Ergebnis: Auf zwei Stichproben weichen beide bei 27 von 230 Losen voneinander ab (11,7 %); nur unsere Liste richtig ist bei 23 von 230 Losen (10,0 %, Wilson etwa 6,8–14,6 %). "
              "Meist zählen wir anders, nicht besser: Höchstende statt Grundlaufzeit und Ende je Los statt je Verfahren. Ein Qualitätsvorsprung ist nicht belegt. "
              "ITERATION 10 (70 Zufallslose der Iteration 9): Liste 66 von 70, Vergabeweiser 58 von 70 gleich mit dem Vergleichswert der KI-Leser; Differenz +8 (Schwelle ≥ 5), exakter Test p = 0,0078, formal erfüllt. "
              "Die Basisregel „Feld EndDate“ allein trifft 63 von 70. Abweichend waren 12 von 70; Ursachen der 8 Fälle „nur Liste richtig“: Losebene 4, Höchstende statt Grundlaufzeit 2, fehlender Wert 1, 2 Tage 1. "
              "ITERATION 10b (neue Stichprobe, 160 Lose, Seed 20261112): Vergabeweiser hat alle 160, 145 gleich, 15 abweichend. Zwei KI-Leser (Opus, Sonnet) lesen ohne Quellenangabe und stimmen bei 15 von 15 überein; die Liste entspricht ihrem Wert in 15 von 15. "
              "Einordnung des Evaluators (Balken rechts): Höchstende 7 (alle mit derselben Textvorlage, effektiv ein Mechanismus), Losebene 4, Abweichung bei Vergabeweiser mit offener Ursache 2, Zuordnungsfehler unserer Pipeline 1, mehrdeutig 1. "
              "VORAB-KRITERIEN: Die Vorab-Schwelle für den Vorsprung (≥ 16 Lose) war bei nur 15 abweichenden Losen rechnerisch unerreichbar; das war unser Fehler bei der Festlegung (docs/ki_irrwege.md). "
              "Sie wurde nicht nachträglich geändert und gilt als formal verfehlt. Das zweite Kriterium (Losebene als richtig für Vergabeweiser, ≥ 8 Lose) ist erfüllt. Sensitivität: Zählt auch das Höchstende als richtig für Vergabeweiser, bleiben 3 zu 0 (p = 0,25), also nichts Belegtes. "
              "ZULÄSSIGER SATZ: „Auf zwei Stichproben weicht Vergabeweisers Datum in rund 10 % der Lose vom Ende der Grundlaufzeit nach neutraler Definition ab, wo die Liste richtig liegt; in 10b waren 11 von 15 dieser Fälle Höchstende oder Losebene.“ "
              "NICHT sagen: „genauer“, „Vergabeweiser liest falsch“, „kein Unterschied“. "
              "GRENZEN: Liste und Vergabeweiser nutzen dasselbe TED-Feld, gemeinsame Fehler sind unsichtbar (bei einem von 10 übereinstimmenden Losen lagen beide falsch); Leser und Regeln aus derselben Modellfamilie; keine menschliche Gegenlesung der 15; nur Lose oberhalb der EU-Schwelle. "
              "FRAGE – ANTWORT: „Warum ist W8a verfehlt?“ Die Vorab-Schwelle (≥ 16 Lose) war bei 15 abweichenden Losen rechnerisch unerreichbar. Gemessen: Differenz +15 von 15, p = 0,0001, aber überwiegend Zählweise (Definition und Losebene), deshalb kein Beleg für bessere Lesequalität. Kriterium nicht geändert, offen berichtet. "
              "„Warum nur die abweichenden Lose lesen?“ Weil die übereinstimmenden die Differenz nicht ändern; absolute Genauigkeit der Liste ist damit nicht belegt. "
              "ZEIG-MIR-WO: reports/vergleich_iteration10.md, reports/vergleich_iteration10b.md, reports/evaluation_iteration10b.md (Tabelle „Gesamtbild beider Stichproben“), src/prepare/vergleich_iteration10b.py.",
              teil="Markt")

rect(s, 0.6, 1.4, 4.3, 2.8, WHITE, name="Vergleich Karte")
box(s, 0.8, 1.48, 3.9, 0.3, "Gleiches Enddatum wie zwei KI-Leser", size=14, bold=True, color=GREY, name="Vergleich Kopf")
box(s, 0.8, 1.82, 1.9, 0.5, "66 von 70", size=28, color=BLUE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name="Vergleich Liste Zahl")
box(s, 0.8, 2.32, 1.9, 0.3, "bei uns", size=14, name="Vergleich Liste Text")
box(s, 2.8, 1.82, 1.95, 0.5, "58 von 70", size=28, color=GREY, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name="Vergleich VW Zahl")
box(s, 2.8, 2.32, 1.95, 0.3, "bei Vergabeweiser", size=14, name="Vergleich VW Text")
box(s, 0.8, 2.75, 3.95, 1.4, [[("Abweichung: ", {"bold": True}), ("27 von 230 Losen (11,7 %)", {})],
                             [("Nur unsere Liste richtig: ", {"bold": True}), ("23 von 230 (10 %)", {})],
                             [("Meist zählen wir anders, nicht besser.", {"bold": True, "color": BLUE})]], size=14, space=6, name="Vergleich Text")
rect(s, 5.05, 1.4, 4.35, 2.8, WHITE, name="Ursachen Karte")
box(s, 5.25, 1.48, 4.0, 0.3, "Warum 15 von 160 Losen abweichen", size=14, bold=True, color=GREY)
balken(s, 5.1, 1.8, 4.25, 2.35, ["Höchstende gemeint", "Teilauftrag (Los)", "Ursache offen", "Fehler bei uns", "mehrdeutig"],
       [7, 4, 2, 1, 1], [BLUE, BLUE, GREY, GREY, GREY], "Ursachen der 15 abweichenden Lose", maximum=9, fmt='0')
kurz(s, "Beide Listen sind brauchbar; das Datum in der Bekanntmachung selbst nachlesen.")
fuss(s, "Vorab-Schwelle (mindestens 16 Lose) war bei 15 abweichenden Losen unerreichbar: unser Fehler, offen berichtet.")

# Folie 6: Make or Buy ------------------------------------------------------------
s = new_slide("ZEIT 1:30. KERNAUSSAGE: Aus Sicht eines Betriebs, der seine Aufträge selbst filtern könnte (Make or Buy): Im Modell rechnet sich Selbstbauen gegen kostenlose Dienste nicht; "
              "offen ist nur, ob Betriebe die Daten in ihrem eigenen System brauchen. Als eigenes Produkt ergibt die Liste keinen Sinn. "
              "BALKEN LINKS (Paket D, Quelle reports/make_or_buy.md, docs/business.md §9.4; ALLE Kosten sind Annahmen): Rechnung bei 100 € pro Stunde: Niedrig (20 h einmalig, 5 h im Jahr) 3.500 € in drei Jahren, Mittel (60 h, 20 h) 12.000 €, Hoch (120 h, 50 h) 27.000 €. "
              "Break-even im Basismodell: gegen DTAD (knapp 1.500 € im Jahr, Gespräch) nur im Szenario Niedrig, nach 2,0 Jahren; gegen AusschreibungsRadar Starter und gegen Vergabeweiser nie. "
              "KARTE 1: Dieses „nie“ ist eine Folge der Modellkonstruktion (Abos und kostenlose Dienste ohne Eigenaufwand gerechnet, Eigenbau mit Stunden), keine Messung. "
              "SYMMETRISCHE VARIANTE (Annahmen): Rechnet man auch für Abo und kostenlose Dienste Nutzungsstunden (10 / 30 / 60 Stunden im Jahr), liegt der Break-even gegen DTAD bei 1,0 / 2,4 / 4,8 Jahren und gegen einen kostenlosen Dienst mit Übernahme von Hand bei 4,0 / 6,0 / 12,0 Jahren. "
              "KARTE 2 (docs/business.md §9.4): Die Kosten der ersten drei Jahre entsprechen 0,14 bis 1,08 zusätzlichen Aufträgen (Marge 5 %, Median-Jahresumsatz 167.404 €, Deckungsbeitrag 25.110 € je Auftrag ohne Angebotsaufwand und Zuschlagswahrscheinlichkeit); "
              "eine Rechengröße, kein Nutzenbeleg. Nicht die Kostenfrage entscheidet, sondern ob ein früher Hinweis überhaupt einen Auftrag bringt (nicht belegt). "
              "KARTE 3 (docs/business.md §8.9, docs/business_case_auswahl.md): Gezahlt hätte im Gespräch nur der größere Betrieb, und zwar für alte Preise und den aktuellen Auftragnehmer („wenn der aktuelle Dienstleister bei 18 Euro pro Stunde lag, brauche ich gar nicht erst mitbieten“). "
              "Preise je Einheit, Mengen und Vertragsklauseln stehen nicht in öffentlichen Daten; den Zuschlagswert als Gesamtsumme nennt TED nur bei knapp der Hälfte der Lose (47,7 %). "
              "BUSINESS-CASE-PRÜFUNG (docs/business_case_auswahl.md): Acht Kandidaten nach sieben vorab festgelegten Kriterien, höchste Summe 7 unter der Schwelle 8: kein tragfähiger Business Case; Test K-A nach Vorprüfung abgebrochen (23 von 52 Paaren, Schwelle 30). "
              "OFFENE HYPOTHESEN (ungeprüft): Daten ins eigene System mit dokumentiertem Schema (Export Schema 1.1, 26 Felder), Anreicherung (Ende je Los, Herkunft je Feld). Zielgruppe nur Betriebe mit Branchensoftware: rund ein Drittel laut einem sekundär zitierten Branchenartikel (Original nicht geprüft). "
              "Die Perspektive des Betriebs wurde in den drei Gesprächen NICHT erfragt; der Kurztest ist vorbereitet (Wizard-of-Oz-Blatt), nicht durchgeführt. "
              "AUSBLICK (Paket B, Oberpfalz): Im Bekanntmachungsservice stehen 32 von 120 Reinigungsverfahren (26,7 %, Intervall 19,6–35,2 %) nicht auf TED. Hinweis auf eine Lücke der TED-Basis, kein belegter Vorsprung. "
              "FRAGE – ANTWORT: „Ist ‚nie günstiger‘ nicht trivial?“ Ja, es ist eine Modellkonstruktion; deshalb die symmetrische Variante. Die Aussage ist, dass der Preis kein Vorteil ist, nicht dass Eigenbau teuer wäre. "
              "„Warum selbst bauen statt Vergabeweiser nutzen?“ Gar nicht, wenn es nur um das Finden geht. Selbst bauen wäre nur sinnvoll, wenn der Betrieb Daten mit festem Schema in sein eigenes System braucht; ob er das braucht, ist nicht geprüft. "
              "„Welches Verwaltungssystem haben Betriebe?“ Nicht erfragt. „Wer pflegt das?“ Der Betrieb oder ein Integrator; im Modell 5 bis 50 Stunden im Jahr (Annahme). "
              "„Warum nicht gleich die Daten von bund.de einbauen?“ Geprüft haben wir den Bekanntmachungsservice (oeffentlichevergabe.de, CC0); ohne belegte Nachfrage wäre es Aufwand ohne Ziel, deshalb Ausblick. "
              "TRANSFERFRAGE „Anderer Standort, andere Nische, doppeltes Volumen?“: Pipeline und Prüfverfahren übertragbar, Lese-Regeln neu testen; Abruf skaliert, die menschliche Prüfung nicht. "
              "ZEIG-MIR-WO: reports/make_or_buy.md, src/report/make_or_buy.py, docs/business.md §8.4, §8.9, §9, docs/business_case_auswahl.md, docs/export_schema.md, docs/prototyp/export/vertragsliste_v1_de.csv.",
              teil="Markt")

rect(s, 0.6, 1.4, 4.4, 2.8, WHITE, name="Kosten Karte")
box(s, 0.8, 1.48, 4.0, 0.3, "Eigenbau: Kosten in 3 Jahren (Annahmen)", size=14, bold=True, color=GREY)
balken(s, 0.7, 1.85, 4.2, 2.3, ["Niedrig", "Mittel", "Hoch"], [3500, 12000, 27000], [BLUE, BLUE, BLUE], "Eigenbau Kosten", maximum=36000, fmt='#,##0')
karten = ([("„Nie günstiger“ ", {"bold": True}), ("als kostenlose Dienste folgt aus der Rechnung, nicht aus einer Messung.", {})],
          [("Die Kosten entsprechen ", {}), ("0,14 bis 1,08", {"bold": True, "color": BLUE}), (" zusätzlichen Aufträgen.", {})],
          [("Gezahlt würde für alte Stundenpreise ", {"bold": True}), ("(ein Gespräch) – die stehen in keinen offenen Daten.", {})])
for i, k in enumerate(karten):
    y = 1.4 + i * 0.97
    rect(s, 5.2, y, 4.2, 0.86, WHITE, name=f"Make or Buy Karte {i + 1}")
    box(s, 5.4, y, 3.85, 0.86, [k], size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Make or Buy Text {i + 1}")
kurz(s, "Für die Suche kostenlose Dienste nutzen; selbst bauen nur, wenn ein eigenes System gefüttert werden soll.")
fuss(s, "Annahmen: 100 € je Stunde; Niedrig 20 h einmalig + 5 h im Jahr, Mittel 60 + 20, Hoch 120 + 50; Marge 5 %.")

# Folie 7: Demo als Zielbild ------------------------------------------------------------
DEMO_VIDEO = ROOT / "docs" / "video" / "live_demo_aufnahme.mp4"      # erzeugt von src/report/demo_aufnahme.py
DEMO_POSTER = ROOT / "docs" / "vortrag" / "poster_live_demo.png"
DEMO_NOTIZEN = (
    "ZEIT 1:00 (nur etwa eine Minute der Bildschirmaufnahme zeigen, live dazu sprechen; die Live-Demo im Browser NUR in der Fragenrunde). "
    "KERNAUSSAGE (Zielbild): So hätte das Produkt aussehen sollen: Passende Hinweise kommen direkt bei der Firma an, als Teams-Karte oder E-Mail. Mit einer Terminprognose wären diese Hinweise Monate vor der Ausschreibung gekommen. "
    "Ohne Prognose bleiben nur Ausschreibungen, die heute erscheinen: im großen Datensatz rund 1 bis 2 Treffer im Monat je erfundener Firma (13, 13 und 19 in 12 Monaten für drei erfundene Profile, Stufe nach dem Radius, vor dem Frist-Filter; docs/business_case_auswahl.md, Nachtrag K-J; docs/demo_push.md Abschnitt 11). "
    "Dafür reicht ein kostenloser Alarm (TED-Suchprofil mit E-Mail-Alarm, Vergabeweiser-Alerts, Weiterleitung per Standard-Flow); ein Push verkürzt den Vorlauf nicht (28 Tage Meldung vor Abgabe, die Frist setzt der Auftraggeber). "
    "WAS DIE AUFNAHME ZEIGT (Fakt, docs/demo_push.md §11): echte, öffentliche TED-Bekanntmachungen (590 Ausschreibungen mit Leistungsort Bayern, 16.10.2025 bis 06.11.2026), erfundene Firma „Cham, 50 km“, Trichter 590 → 562 → 428 → 405 → 37 → 19 → 2 "
    "(Zeitraum, Mehrfachveröffentlichung, Reinigungs-CPV, Oberpfalz, Radius, Frist); Ergebnis 2 Treffer, dann Teams-Karte und E-Mail-Vorschau. Nichts wird gesendet, alles läuft offline im Browser. "
    "EINORDNUNG (immer sagen): Firma erfunden, nichts gesendet, Treffer sind kein Befund über den Markt; Veranschaulichung der Datenübergabe, kein Business Case (Auswahlbogen: K-I und K-J mit K7 = 0, nur Ausblick). "
    "Ein KI-Urteil gibt es nur für zwei gespeicherte Beispielprofile, bei jeder anderen Firma gilt eine Stichwortregel. KI gegen Regel 13 von 14 gleich, davon 5 trivial, ohne Referenz durch einen Menschen. "
    "Der Vorgänger-Hinweis wurde im großen Datensatz 3-mal ausgelöst (alte Fassung 2, neue Fassung 1), alle 3 falsch; deshalb ist er dort abgeschaltet (docs/demo_push.md §11, Befund Vorgänger-Hinweis). Teams-Anzeige und Versand wurden nie getestet. "
    "FRAGE – ANTWORT (Prüferfrage): „Warum habt ihr nach dem Nein noch eine Demo gebaut?“ Sie entstand auf Wunsch nach dem Auswahlbogen, als Zielbild und als Veranschaulichung der Datenübergabe, nicht als Business Case. "
    "Sie hat das Nein eher bestätigt: Sie zeigt, dass ohne Prognose kein Zeitvorsprung entsteht und ein kostenloser Alarm dasselbe leistet. Gemessen haben wir damit nichts über Nachfrage; der Test mit Betrieben ist vorbereitet, nicht durchgeführt (Folie 11). "
    "„Wo ist der Unterschied zu AusschreibungsRadar?“ Keiner belegt: Eignungsabgleich und Alerts gibt es dort laut Anbieterseite schon (Match-Score ab 79 €). "
    "LIVE-DEMO IN DER FRAGENRUNDE (Datei docs/demo/live_demo.html, Doppelklick, kein Netz): (1) gelben Hinweis vorlesen; (2) „Großer Datensatz (Bayern, 12 Monate)“; (3) Schnellknopf „Cham, 50 km“, Frist-Filter AN; "
    "(4) „Filterung starten“ (etwa 8 Sekunden); (5) 2 Treffer; (6) Treffer anklicken: Teams-Karte, Fakten getrennt von Deutung; (7) Kanal „E-Mail“; (8) Frist-Filter AUS: 16 statt 2, 14 davon mit abgelaufener Frist, nur zur Veranschaulichung. "
    "ZEIG-MIR-WO: docs/demo_push.md (Abschnitte 9 bis 11), docs/demo/live_demo.html, docs/demo/push_demo.html, docs/demo/nachrichten/, Aufnahme docs/video/live_demo_aufnahme.mp4 (Skript src/report/demo_aufnahme.py), docs/business_case_auswahl.md (K-I, K-J). ")

s = new_slide(DEMO_NOTIZEN, teil="Produkt")

if DEMO_VIDEO.exists() and DEMO_POSTER.exists():
    # Bildschirmaufnahme der Live-Demo (ohne Ton) links, groß; Einordnung rechts
    s.shapes.add_movie(str(DEMO_VIDEO), Inches(0.6), Inches(1.4), Inches(5.6), Inches(3.15), poster_frame_image=str(DEMO_POSTER), mime_type="video/mp4").name = "Aufnahme Live-Demo"
    DEMO_STATUS = "Aufnahme eingebettet"
else:
    rect(s, 0.6, 1.4, 5.6, 3.15, WHITE, name="Aufnahme Platzhalter")
    box(s, 0.8, 1.4, 5.2, 3.15, "Bildschirmaufnahme der Demo fehlt (Skript erneut ausführen).", size=14, color=GREY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    DEMO_STATUS = "Platzhalter ohne Aufnahme"
rect(s, 6.4, 1.4, 3.0, 0.95, WHITE, name="Mit Prognose Karte")
box(s, 6.6, 1.4, 2.65, 0.95, [[("Mit Prognose: ", {"bold": True, "color": BLUE}), ("Hinweis Monate vor der Ausschreibung.", {})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Mit Prognose Text")
rect(s, 6.4, 2.45, 3.0, 1.35, WHITE, name="Ohne Prognose Karte")
box(s, 6.6, 2.45, 2.65, 1.35, [[("Ohne Prognose: ", {"bold": True}), ("nur heutige Ausschreibungen, rund 1 bis 2 Treffer im Monat je Firma (13 bis 19 in 12 Monaten).", {})]],
    size=14, anchor=MSO_ANCHOR.MIDDLE, name="Ohne Prognose Text")
kurz(s, "Dafür reicht ein kostenloser Alarm.", x=6.4, y=3.9, w=3.0, h=0.65)
fuss(s, "Firma erfunden, nichts gesendet. Bildschirmaufnahme der Demo mit echten TED-Bekanntmachungen, ohne Ton.")

# Folie 8: So funktioniert es technisch ------------------------------------------------------------
s = new_slide("ZEIT 1:00. KERNAUSSAGE: Alles, was wir gezeigt haben, kommt aus einer einfachen, offenen Kette von Programmen; jede Zahl lässt sich nachrechnen. "
              "PIPELINE (oben, Schlangenlinie 1 → 6): (1) TED-API: Abfrage der Bekanntmachungen per Programm (src/ted_download.py; vorher die aktuelle API-Dokumentation geprüft). "
              "(2) Rohdaten unverändert in data/raw (nicht im Git, Abruf reproduzierbar, docs/reproduzierbarkeit.md). (3) Aufbereitung: Laufzeit und Optionen lesen, Leseregeln 1a/1b und 6 bis 10 (src/prepare/vertragsliste.py). "
              "(4) Vertragsliste: 9.325 Lose, je Los Ende der Grundlaufzeit, Höchstende nur als Hinweis, Herkunft in Stufen A bis F. "
              "(5) Prüfung: Zufallsstichproben mit Seed, KI-Leser und Kommilitone, Vergleich mit Vergabeweiser, Backtest der Terminprognose (src/model/baseline.py, reports/evaluation_iteration*.md). "
              "(6) Webseite und Demo nur zur Darstellung (docs/prototyp/vertragsliste.html, docs/demo/live_demo.html). "
              "CODE UNTEN: Die Prognoseregel R1 aus src/model/baseline.py (vor dem Lauf eingefroren und committet): Prognose = Höchstende (sonst Ende der Grundlaufzeit) minus 6 Monate; Treffer, wenn die Neuausschreibung ±3 Monate um die Prognose veröffentlicht wurde. "
              "Ergebnis auf 52 handgeprüften Paaren: 15 von 52 = 28,8 % (Wilson 18,3–42,3 %), gefordert 60 %; R0 9 von 52 = 17,3 %. "
              "SENSITIVITÄT (Nachtrag, reports/sensitivitaet_iteration5.md; NACHTRÄGLICHE OBERGRENZE, KEIN NEUER TEST): Vorlauf 0 bis 24 Monate auf denselben Paaren variiert: Der beste Vorlauf im Nachhinein ist genau 6 Monate (15 von 52 = 28,8 %). "
              "Selbst ein Fenster von ±12 Monaten bringt nur 26 von 52 = 50,0 %, und ein Jahr Unsicherheit nützt keinem Betrieb. R1 gegen R0 auf denselben Paaren: nur R1 trifft 10, nur R0 trifft 4, exakter McNemar-Test p ≈ 0,18: Der Vorsprung vor der einfachen Regel ist nicht gesichert. "
              "LIVE-NACHWEIS IN DER FRAGENRUNDE (läuft ohne Rohdaten, liest die Paare aus reports/backtest_iteration5.md): `python src/model/sensitivitaet_backtest.py --vorlauf 9 --fenster 2` → R1: 2 von 52 = 3,8 %, R0: 1 von 52 = 1,9 %. "
              "Ohne Argumente schreibt das Skript den Bericht neu. FRAGE – ANTWORT: „Hättet ihr mit einem anderen Vorlauf 60 % geschafft?“ Nein, auch mit dem im Nachhinein besten Vorlauf nicht (28,8 %); das ist eine optimistische Obergrenze. "
              "„Wo stehen die Regeln?“ Im Kopf von src/prepare/vertragsliste.py; die Fassung der Iteration 9 ist der Stand der Liste. "
              "ZEIG-MIR-WO: src/model/baseline.py (Zeilen 30 bis 55), src/model/sensitivitaet_backtest.py, reports/backtest_iteration5.md, reports/sensitivitaet_iteration5.md, docs/reproduzierbarkeit.md.",
              teil="Produkt")

stufen = (("TED-API", "Abfrage per Programm"), ("Rohdaten", "unverändert abgelegt"), ("Aufbereitung", "Laufzeit, Leseregeln"),
          ("Vertragsliste", "9.325 Lose, Stufen A–F"), ("Prüfung", "Stichproben, Backtest"), ("Webseite, Demo", "nur zur Darstellung"))
bw, gap, bh, rgap = 2.8, 0.2, 0.66, 0.2
for i, (h, t) in enumerate(stufen):
    reihe, pos = divmod(i, 3)
    spalte = pos if reihe == 0 else 2 - pos          # Schlangenlinie: zweite Reihe von rechts nach links
    x, y = 0.6 + spalte * (bw + gap), 1.38 + reihe * (bh + rgap)
    rect(s, x, y, bw, bh, LBLUE if i == 3 else WHITE, radius=0.12, name=f"Pipeline {i + 1}")
    kreis(s, x + 0.1, y + (bh - 0.32) / 2, 0.32, BLUE, str(i + 1), size=12)
    box(s, x + 0.52, y + 0.03, bw - 0.58, bh - 0.06, [[(h, {"bold": True})], [(t, {"color": GREY})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Pipeline {i + 1} Text")
    if pos < 2 and reihe == 0:
        pfeil(s, x + bw + 0.01, y + (bh - 0.22) / 2, 0.18, 0.22, "rechts", name=f"Pipeline Pfeil {i + 1}")
    if pos > 0 and reihe == 1:                     # Pfeil rechts neben dem Kasten zeigt von Schritt i auf diesen Kasten
        pfeil(s, x + bw + 0.01, y + (bh - 0.22) / 2, 0.18, 0.22, "links", name=f"Pipeline Pfeil {i}")
pfeil(s, 0.6 + 2 * (bw + gap) + bw / 2 - 0.11, 1.38 + bh + 0.01, 0.22, rgap - 0.02, "unten", name="Pipeline Pfeil 3-4")

rect(s, 0.6, 3.04, 6.3, 1.82, WHITE, name="Code Karte")
box(s, 0.8, 3.09, 5.9, 0.28, "Die Prognoseregel im Programm (Auszug)", size=14, bold=True, color=GREY, name="Code Kopf")
code = [[("VORLAUF_MONATE = 6", {}), ("   # Prognose: 6 Monate vor Ende", {"color": DGREEN})],
        [("FENSTER_MONATE = 3", {}), ("   # Treffer: ±3 Monate", {"color": DGREEN})],
        [("def ", {"color": BLUE}), ("r1(gl, hoechstende):", {}), ("  # Höchstende, sonst Grundlaufzeit", {"color": DGREEN})],
        [("    return ", {"color": BLUE}), ("plus_monate(hoechstende or gl, -VORLAUF_MONATE)", {})],
        [("def ", {"color": BLUE}), ("treffer(prognose, veroeffentlicht, fenster):", {})],
        [("    return ", {"color": BLUE}), ("(plus_monate(prognose, -fenster)", {})],
        [("            <= veroeffentlicht <= plus_monate(prognose, fenster))", {})]]
box(s, 0.8, 3.4, 6.0, 1.42, code, size=12, font=MONO, color=INK, name="Code")
rect(s, 7.05, 3.04, 2.35, 1.82, LBLUE, name="Kurz gesagt Karte")
box(s, 7.22, 3.04, 2.05, 1.82,[[("Kurz gesagt: ", {"bold": True, "color": DBLUE}), ("Die Regel ist einfach und offen nachprüfbar. Sie traf 15 von 52 Fällen = 28,8 %.", {"color": DBLUE})]],
    size=14, anchor=MSO_ANCHOR.MIDDLE, name="Kurz gesagt Satz")
s.notes_slide.notes_text_frame.text += " KURZ GESAGT (für Laien, steht auf der Folie): Die Regel ist einfach und offen nachprüfbar. Sie traf 15 von 52 Fällen = 28,8 %."
fuss(s, "Nur öffentliche TED-Daten; Rohdaten bleiben unverändert, jede Auswertung ist ein eigenes Programm.")

# Folie 9: KI-Irrwege ------------------------------------------------------------
s = new_slide("ZEIT 1:15 (Teil 1 Irrwege etwa 0:40, Teil 2 Trennung von Entwicklung und Test etwa 0:35). KERNAUSSAGE: Claude Code hat Regeln, Stichproben und Auswertungen mitgebaut; jeder dieser Fehler wurde von einem getrennten Evaluator, im Test oder vom Nutzer gefunden, nicht von der Hand, die ihn gemacht hat. "
              "Vier von 31 Einträgen in docs/ki_irrwege.md (drei auf der Folie, der vierte steht als Fußnote auf Folie 5; der Paket-B-Fall steht im Lab-Log, Abschnitt 8): (1) Entwicklung 10–11 von 12 plausibel, im Test 11 von 24 richtig (Iteration 3): Regel verworfen. "
              "(2) „Blind“ war nicht blind: Die KI-Leser (eine zweite KI, die die Bekanntmachung unabhängig lesen sollte) hatten in Iteration 8 die Projektbeschreibung im Kontext (CLAUDE.md), gefunden vom Evaluator, offen genannt. "
              "(3) Konkurrenz übersehen: Die Suche vom 24.10. fand keinen deutschen Dienst, tatsächlich gibt es zwei; gefunden vom Recherche-Agenten nach dem Hinweis des Dozenten. "
              "(4) Schwelle unerreichbar: Claude übernahm die Abweichungsrate von 17 % aus Iteration 10 für 160 Lose, es waren 9,4 %; gefunden vor den Leserantworten, nicht nachträglich geändert. "
              "LERNPUNKT STATT SCHWÄCHE: „Konkurrenz erst in Iteration 10 gesehen“ ist ein Prozessfehler, kein Pech. Plan G1.1 (Wettbewerber sichten) blieb offen; die Entscheidung gegen Kundenkontakt fiel am 2026-10-29. "
              "Kosten: Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos gibt. Lehre: ein Marktgate in Phase 1, vor der Modellierung. "
              "LERNPUNKT „Null = Verdachtsmoment“ (ein Satz, wenn Zeit): Paket B fand zunächst 0 von 84 Verfahren nicht auf TED; die Robustheitsprüfung zeigte ein Filterartefakt; danach 26,7 %. "
              "TEIL 2, TRENNUNG VON ENTWICKLUNG UND TEST (Zeitstrahl rechts): Hypothese, Kriterien und Seed stehen im Git, bevor die Stichprobe gezogen und die Antworten gelesen werden; die Reihenfolge im Versionsverlauf ist der Nachweis. "
              "Iteration 10b: 4f50436 (Hypothese, Kriterien, Skript und Seed 20261112 vorab), 9d63c59 (Stichprobe gezogen, SHA-256 des Schlüssels 2cd00206…3e33), 49bb198 (Abruf- und Auswertungsskript), "
              "6b7e8d8 (Paket und Leseskript vor den Antworten), 69917ff (Antworten der Leser unverändert), f6583cc (Auswertung). Iteration 9 genauso: Regeln a03a4a8, Seed und Skript 4521952, Stichprobe b3b1471, Antworten erst e1726e7. "
              "LIVE IN DER FRAGENRUNDE: `git log --oneline` zeigen; eine Regel in src/prepare/vertragsliste.py öffnen; Fehlwerte (Stufe F) in reports/beispiel_liste_oberpfalz.csv. "
              "EHRLICHE LÜCKEN: das Lauf-Skript der Iteration-9-Leser wurde erst mit den Antworten committet; in Iteration 8 kannten die Leser den Fehlertyp; in 10b liegt das Protokoll der Leserläufe außerhalb des Repos. "
              "FRAGE – ANTWORT: „Warum erst jetzt die Konkurrenz?“ Weil die Sichtung (G1.1) offen blieb und die Suche am 24.10. zu eng war. Prozessfehler im Business Understanding; er hat Zeit gekostet, aber das Ergebnis geändert. "
              "ZEIG-MIR-WO: docs/ki_irrwege.md (31 Einträge), docs/projektplan.md (G1.1), reports/evaluation_iteration10b.md, git log, src/prepare/stichprobe_iteration10b.py, docs/reproduzierbarkeit.md.",
              teil="Prüfung")

items = (("Im Test viel schlechter", "Beim Entwickeln 10–11 von 12 richtig, im Test nur 11 von 24."),
         ("„Blind“ war nicht blind", "Die prüfende KI kannte unsere Projektbeschreibung."),
         ("Konkurrenz zu spät gesehen", "Lehre: früh fragen, ob es das schon gibt."))
for i, (h, t) in enumerate(items):
    y = 1.4 + i * 0.96
    rect(s, 0.6, y, 4.5, 0.88, WHITE, name=f"Irrweg {i + 1}")
    box(s, 0.8, y + 0.07, 4.1, 0.28, h, size=14, bold=True, color=RED if i == 0 else DARK)
    box(s, 0.8, y + 0.37, 4.1, 0.5, t, size=14)
box(s, 5.3, 1.4, 4.1, 0.6, "Trennung von Entwicklung und Test: erst Regeln festlegen, dann testen.", size=14, bold=True)
rect(s, 5.3, 2.08, 4.1, 2.12, WHITE, name="Zeitstrahl Karte")
xs = (5.95, 7.35, 8.75)
rect(s, xs[0], 2.5, xs[2] - xs[0], 0.04, LINE, MSO_SHAPE.RECTANGLE, name="Zeitstrahl Linie")
for i, (x, t) in enumerate(zip(xs, ("Regeln festgelegt", "Stichprobe gezogen", "Ergebnis ausgewertet"))):
    kreis(s, x - 0.21, 2.31, 0.42, BLUE, str(i + 1), size=14, name=f"Zeitstrahl Punkt {i + 1}")
    box(s, x - 0.65, 2.85, 1.3, 0.55, t, size=14, align=PP_ALIGN.CENTER, name=f"Zeitstrahl Text {i + 1}")
box(s, 5.45, 3.6, 3.8, 0.5, "Reihenfolge im Versionsverlauf belegt", size=14, color=GREY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, name="Zeitstrahl Unterschrift")
kurz(s, "KI-Ergebnisse erst glauben, wenn jemand sie getrennt geprüft hat.")
fuss(s, "Drei Beispiele aus unserer Liste von 31 KI-Irrwegen; Lücke: ein Leseprotokoll liegt außerhalb des Projektordners.")

# Folie 10: Empfehlung ------------------------------------------------------------
s = new_slide("ZEIT 1:15. KERNAUSSAGE: Ampel statt Fazit-Text. GRÜN: Die Liste ist als Ausgangspunkt nutzbar, immer mit Blick in die verlinkte Bekanntmachung: 66 von 70 Zufallslosen der Iteration 9 (94,3 %) haben das gleiche Enddatum wie der Vergleichswert zweier KI-Leser "
              "(Leser nicht unabhängig, Vergleichswert teils zirkulär; Mensch 14 von 15). "
              "GELB: Höchstende nur Hinweis (87,1 %); nur TED-Daten: 79,4 % ist der Anteil der Lose mit Enddatum unter den Zuschlägen 10/2025 bis 9/2026 (2.783 von 3.503), rund 73 % aller Lose (6.803 von 9.325); das ist keine Marktabdeckung. "
              "Dazu der Ausblick aus Paket B (rund ein Viertel der Oberpfälzer Reinigungsverfahren im Bekanntmachungsservice nicht auf TED). Gespräche n = 3; Nachfrage ungeprüft, ein Test mit Betrieben ist vorbereitet, nicht durchgeführt (Folie 11). "
              "ROT: Terminprognose (28,8 %); die Liste als eigenes Produkt; Qualitätsvorsprung nicht belegt. "
              "ZEILE „UNSER RAT“ (docs/lab_log.md Abschnitt 7, Deutung unter Annahmen): zuerst die kostenlosen Wege nutzen (TED-Suchprofile mit E-Mail-Alarm, Vergabeweiser-Alerts, diese Liste als CSV); "
              "abonnieren nur für eine Funktion, die man braucht (im Gespräch genannt: Wettbewerbsdaten; Zahlungsbereitschaft in einem von drei Gesprächen); selbst bauen lohnt im Basismodell gegen kostenlose Dienste nie (Modellkonstruktion). "
              "TRANSFERFRAGE „Würdet ihr das Produkt bauen?“: Nein, nicht als Liste allein. Wenn weiter, dann zuerst der vorbereitete Test mit Betrieben (Schwelle vorab), eine menschliche Gegenlesung und ein Maß, das Definition und Losebene trennt. "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1 (Befüllungsquote 90 %, Laufzeitende bestimmbar); eine Geschäftsbegründung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/lab_log.md Abschnitt 7, docs/annahmen.md, reports/evaluation_iteration9.md, reports/evaluation_iteration10b.md, docs/business.md §8.9, docs/business_case_auswahl.md.",
              teil="Fazit")

ampel = (("Ja", GREEN, ["Vertragsenden als Ausgangspunkt", "Immer die Bekanntmachung selbst lesen", "66 von 70: gleiches Enddatum wie zwei KI-Leser"]),
         ("Mit Vorsicht", AMBER, ["Lose mit Enddatum: 79,4 % im letzten Jahr", "Höchstende nur als Hinweis", "Nachfrage ungeprüft, Test vorbereitet"]),
         ("Nein", RED, ["Terminprognose (28,8 %)", "Liste als eigenes Produkt", "Vorsprung nicht belegt"]))
for i, (h, f, pts) in enumerate(ampel):
    x = 0.6 + i * 3.0
    rect(s, x, 1.4, 2.8, 2.25, WHITE, name=h + " Karte")
    kreis(s, x + 0.2, 1.5, 0.36, f, name=h + " Signal")
    box(s, x + 0.7, 1.5, 1.95, 0.36, h, size=16, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 1.98, 2.45, 1.65, pts, size=14, space=6)
rect(s, 0.6, 3.73, 8.8, 0.48, WHITE, name="Rat Karte")
box(s, 0.8, 3.73, 8.5, 0.48, [[("Unser Rat: ", {"bold": True}),("kostenlosen Alarm nutzen · nur für Wettbewerbsdaten abonnieren · nicht selbst bauen", {})]],
    size=14, anchor=MSO_ANCHOR.MIDDLE, name="Rat Text")
kurz(s, "Die Liste hilft beim Planen, ersetzt aber nicht den Blick in die Bekanntmachung.")
fuss(s, "79,4 % = Anteil der Lose mit Enddatum unter den Zuschlägen 10/2025 bis 9/2026, nur TED-Daten.")

# Folie 11: Fazit ------------------------------------------------------------
s = new_slide("ZEIT 0:45. KERNAUSSAGE in einem Satz wiederholen, dann Brücke zur Fragenrunde. Gesamtzeit: 15:00 (Ziel ±30 Sekunden); Zeitbudget je Folie: "
              "0:30 / 3:30 / 1:45 / 1:15 / 1:15 / 1:30 / 1:00 / 1:00 / 1:15 / 1:15 / 0:45 = 15:00 (Business Understanding Folien 3 bis 7: 6:45 = 45 %; Video-Folie 2 inkl. Quiz und Überleitung 3:30, Video ca. 3 Minuten). "
              "Folien 12 bis 14 sind ausgeblendet (Anhang, nicht in der Zeit). "
              "Satz zum Mitnehmen: Den Termin einer Neuausschreibung sagen TED-Daten nicht vorher; eine Liste der Vertragsenden lässt sich lesen, ist aber kein eigenes Produkt, solange Vergabeweiser sie kostenlos bietet. Lehre: Marktgate in Phase 1, vor der Modellierung. "
              "NÄCHSTER SCHRITT (docs/business_case_auswahl.md, Nachtrag K-J, Schwelle vorab festgelegt am 2026-11-09, vor jedem Anruf): eine Stunde TED-Suchprofil mit E-Mail-Alarm anlegen und nach Teams weiterleiten, dann drei Anrufe bei Betrieben. "
              "Schwelle: „Mindestens 2 von 3 Betrieben nutzen Teams oder Planner aktiv, nennen mindestens 1 Stunde pro Woche für Sichten und Übertragen und übertragen heute von Hand; sonst wird K-J verworfen.“ Test nicht durchgeführt; die Schwelle ist eine Setzung. "
              "FRAGENRUNDE vorbereiten: (1) Methodenfrage: warum ±3 Monate, warum diese Vergleichsregel, warum KI-Leser als Maß, warum nur abweichende Lose (Folie 5, Folie 8 Sensitivität, ausgeblendete Folien 12 bis 14). "
              "Ausgeblendete Folien in der Fragerunde über die Foliensortierung öffnen. (2) Live-Nachweis: `python src/model/sensitivitaet_backtest.py --vorlauf 9 --fenster 2` (Folie 8); git log und Reihenfolge der Commits (Folie 9); Live-Demo im Browser (Folie 7). "
              "(3) Transferfragen: „Warum nicht Vergabeweiser nutzen?“ (Folie 4), „Wer zahlt?“ (Folien 3 und 6), „Warum ist W8a verfehlt?“ (Folie 5), „Warum selbst bauen?“, „Welches Verwaltungssystem?“, „Wer pflegt das?“, „Warum nicht bund.de?“ (alle Folie 6), "
              "„Warum eine Demo nach dem Nein?“ (Folie 7), „Was war mit der Null in Paket B?“ und „Warum erst jetzt die Konkurrenz?“ (Folie 9), anderer Standort, andere Nische, doppeltes Volumen (Folien 6 und 10). "
              "Nicht sagen: „genauer als Vergabeweiser“, „Vorsprung belegt“, „kein Unterschied“, „die Liste stimmt zu 94 %“ (richtig: gleiches Enddatum wie zwei KI-Leser).", dark=True, teil="Fazit")

box(s, 0.6, 0.5, 8.8, 1.3, "Den Termin sagt TED nicht voraus. Das Vertragsende lässt sich lesen, ist aber kein eigenes Produkt.", size=26, color=INK, font=HEAD, name="Kernsatz")
for i, (z, t, f) in enumerate((("28,8 %", "Terminprognose, gefordert waren 60 %", RED), ("66 von 70", "gleiches Enddatum wie zwei KI-Leser", GREEN), ("0 €", "Vergabeweiser, kostenlos", BLUE))):
    x = 0.6 + i * 3.0
    rect(s, x, 1.8, 2.8, 1.25, WHITE, name=f"Kachel {i + 1}")
    box(s, x + 0.2, 1.88, 2.4, 0.55, z, size=26, color=f, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 2.45, 2.45, 0.55, t, size=14, color=INK)
box(s, 0.6, 3.3, 8.8, 0.32, [[("Lehre: ", {"bold": True, "color": DBLUE}), ("vor dem Bauen fragen, ob es das schon gibt und wer dafür zahlt.", {"color": INK})]], size=16, name="Lehre")
box(s, 0.6, 3.75, 8.8, 0.62, [[("Nächster Schritt: ", {"bold": True, "color": DBLUE}),
                              ("Test mit drei Betrieben, Schwelle vorab festgelegt: Mindestens 2 von 3 übertragen Treffer heute von Hand (mindestens 1 Stunde pro Woche), sonst verwerfen wir die Idee.", {"color": INK})]],
    size=14, name="Nächster Schritt")
box(s, 0.6, 4.75, 6.0, 0.45, "Vielen Dank. Fragen?", size=22, color=BLUE, font=HEAD, name="Dank")
s.notes_slide.notes_text_frame.text += " KURZ GESAGT (für Laien): Ob ein Vertrag neu ausgeschrieben wird, sagt TED nicht; wann er endet, steht in der Bekanntmachung, und die kostenlose Liste dazu gibt es schon."

# Folie 12 (Anhang): Frage, Kriterium, Daten ------------------------------------------------------------
s = new_slide("AUSGEBLENDET (Anhang für die Fragerunde; im Vortrag ersetzt durch das Video auf Folie 2; Zeit 0:00). Zeigen bei Fragen zu Kriterium, Schwelle, Datenumfang. KERNAUSSAGE: Die Frage hatte eine Entscheidung (auf welche Ausschreibung bereite ich mich vor?) und eine vorab festgelegte Schwelle. "
              "Zielgruppe: Reinigungsfirmen im Mittelstand, Nische Gebäudereinigung (Haupt-CPV 90910/90911/90919). Annahme: Wer früh weiß, wann ein Vertrag endet, kann Personal und Angebot vorbereiten (A1, A15); diese Annahme war zu diesem Zeitpunkt ungeprüft, ein Kundengespräch gab es nicht. "
              "Erfolgskriterium vor dem Backtest festgelegt (docs/business.md 7.1): Treffer = Neuausschreibung im Fenster ±3 Monate um die Prognose, Schwelle 60 %; Vergleichsregel R0 = Ende der Grundlaufzeit minus 6 Monate, 17,3 %. "
              "Daten: TED Search API, eForms-Zuschläge ab Okt. 2023, Rohdaten unverändert in data/raw (nicht im Git, Abruf-Skript in docs/reproduzierbarkeit.md). 9.325 Lose aus 4.011 Zuschlägen (alle eForms-Zuschläge ab Okt. 2023). "
              "Die Angabe „Zuschläge 10/2025 bis 9/2026“ gehört nur zu den 79,4 % (Anteil der Lose mit Enddatum im letzten Jahr), nicht zu den 9.325 Losen. "
              "Laufzeitende bei 90,0 % der Zuschläge bestimmbar; Verlängerungsoptionen nur bei 18,9 % im Feld BT-58, der Rest im Freitext. "
              "Vier Zyklen CRISP-DM, jeder endete mit einer Entscheidung gegen vorab festgelegte Schwellen. Zyklus 4 ist der Rücksprung in Phase 1; er bekommt in diesem Vortrag den größten Teil der Zeit (Folien 3 bis 7, 6:45 von 15:00). "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1: Befüllungsquote etwa 90 %, Laufzeitende bestimmbar, Haupt-CPV klar abgrenzbar. Eine Geschäftsbegründung ist das nicht; sie wurde nicht belegt. "
              "ZEIG-MIR-WO: docs/business.md Abschnitt 7.1, reports/datenqualitaet_DEU_20260722_20261021.md, docs/quellen.md.")

box(s, 0.6, 1.4, 8.8, 0.95, "Reinigungsfirmen erfahren oft spät, wann ein öffentlicher Vertrag endet. Unsere Idee: Das aus Daten von TED vorhersagen, der EU-Plattform für öffentliche Ausschreibungen.", size=16, name="Idee")
tile(s, 0.6, 2.5, 2.8, 1.7, "60 %", "Mindest-Trefferquote, vorab festgelegt (Termin auf ±3 Monate genau)", BLUE, "Schwelle")
tile(s, 3.6, 2.5, 2.8, 1.7, "17,3 %", "so viel schafft eine einfache Faustregel zum Vergleich", GREY, "Faustregel")
tile(s, 6.6, 2.5, 2.8, 1.7, "9.325", "Lose (Teilaufträge) aus 4.011 Zuschlägen seit Okt. 2023", BLUE, "Daten")
kurz(s, "Wer früh Bescheid weiß, kann Personal und Angebot besser planen (Annahme, ungeprüft).")
fuss(s, "Quelle: TED Search API v3. 9.325 Lose = alle eForms-Zuschläge der Gebäudereinigung ab Okt. 2023.")

# Folie 13 (Anhang): Irrwege ------------------------------------------------------------
s = new_slide("AUSGEBLENDET (Anhang für die Fragerunde; im Video Runde 1 und 2; Zeit 0:00). KERNAUSSAGE: Zwei Ideen sind an vorab festgelegten Schwellen gescheitert, und das haben wir so berichtet. "
              "IRRWEG 1 (Iteration 2 bis 4): Jede Neuausschreibung dem Vorgängervertrag zuordnen. Auftraggeber + CPV 16,7 % (Schwelle 80 %), weil große Auftraggeber viele Verträge parallel vergeben; Objekt-Regel (Adresse, Titel) 28,9 % (Schwelle 60 %); "
              "letzter Versuch auf neuen Testdaten 56,7 % (Schwelle 60 %), die Zweitprüfung durch den Nutzer 65 %. Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 richtig. "
              "IRRWEG 2 (Iteration 5, Backtest): R1 = Höchstende (spätestes Vertragsende) minus 6 Monate auf 52 von Hand bestätigten Paaren: 28,8 %; R0 (Ende der Grundlaufzeit minus 6 Monate) 17,3 %; Schwelle 60 %. "
              "20 Neuausschreibungen kamen mehr als 3 Monate früher, 15 im Fenster, 17 später. Entscheidung: Idee anpassen, keine Terminprognose. Grenzen: Paare aus einer Rückwärtssuche (nur auffindbare Vorgänger), Zweitprüfung KI-unterstützt. "
              "Nachtrag Sensitivität (nachträglich, kein neuer Test): bester Vorlauf im Nachhinein 6 Monate (28,8 %), ±12 Monate nur 50 %, McNemar R1 gegen R0 p ≈ 0,18 (Folie 8). "
              "FRAGE – ANTWORT: „Warum ±3 Monate, warum diese Vergleichsregel?“ Das Fenster wurde vor der Rechnung gesetzt, weil ein Betrieb für Personal und Angebot grob ein Vierteljahr Spielraum braucht; die einfache Regel R0 zeigt, was Zufall und Streuung allein schaffen; die Schwelle 60 % war eine Setzung ohne Kundenkontakt. "
              "ZEIG-MIR-WO: reports/zuordnung_iteration3.md, reports/evaluation_iteration4.md, reports/backtest_iteration5.md, reports/evaluation_iteration5.md, reports/sensitivitaet_iteration5.md.")

rect(s, 0.6, 1.4, 5.3, 2.8, WHITE, name="Chart Karte")
box(s, 0.8, 1.5, 5.0, 0.3, "Trefferquote unserer Versuche", size=14, bold=True, color=GREY)
balken(s, 0.7, 1.8, 5.1, 2.35, ["Zuordnung, Versuch 1", "Zuordnung, Versuch 2", "Zuordnung, Versuch 3", "Termin-Vorhersage"],
       [16.7, 28.9, 56.7, 28.8], [RED, RED, RED, RED], "Trefferquote gegen Schwelle", maximum=85)
rect(s, 6.1, 1.4, 3.3, 2.8, WHITE, name="Ergebnis Karte")
box(s, 6.3, 1.5, 2.9, 2.6, [[("Gefordert war", {"color": GREY, "bold": True})], [("80 % / 60 % / 60 % / 60 %", {"size": 16, "bold": True})],
    [("Alle vier Versuche verfehlt.", {"bold": True, "color": RED})], "Neuer Plan: nicht der Termin, sondern eine Liste der Vertragsenden."], size=14, space=8, name="Ergebnis Text")
kurz(s, "Niemand kann aus TED sagen, wann genau ein Vertrag neu ausgeschrieben wird.")
fuss(s, "Termin-Vorhersage: spätestes Vertragsende minus 6 Monate, 52 geprüfte Paare. Schwellen vorab festgelegt.")

# Folie 14 (Anhang): Liste und Genauigkeit ------------------------------------------------------------
s = new_slide("AUSGEBLENDET (Anhang für die Fragerunde; im Video Runde 3; Zeit 0:00). KERNAUSSAGE: Aus dem Rückschlag wird eine andere Frage: nicht „wann wird neu ausgeschrieben?“, sondern „wann endet ein Vertrag laut Bekanntmachung?“. "
              "Vier Messungen messen vier verschiedene Dinge (n = 60, 47, 80, 70), sie sind kein Trend; keine ist eine belastbare Fehlerquote. "
              "Die Liste (Fassung der Iteration 9) hat 9.325 Lose; je Los das Ende der Grundlaufzeit, das Höchstende nur als Hinweis, Auftraggeber, TED-Link und eine Stufe A bis F (woher die Angabe stammt). "
              "Ein Enddatum hat sie für 79,4 % der Lose im letzten Jahr (Zuschläge 10/2025 bis 9/2026: 2.783 von 3.503; Schwelle 80 % knapp verfehlt) und für rund 73 % aller Lose (6.803 von 9.325); die beiden Zahlen gelten für verschiedene Zeiträume und sind keine Marktabdeckung. "
              "Prototyp Oberpfalz: 130 Lose, davon 33 ohne Ende (Stufe F, keine Laufzeitfelder im XML). "
              "Iteration 6: Handprüfung von 60 Zufallslosen, aber die Vorlage zeigte den Listenwert (Verankerung): 88,3 %. Iteration 7: Handprüfung ohne Listenwerte, Nachprüfung im Original: 76,6 %, ein Mischmaß aus Listen- und Prüfungsfehlern. "
              "Iteration 8: zwei KI-Leser (Opus, Sonnet) auf allen 95 Losen: 77 von 80 = 96,2 %, Leser nicht unabhängig. Iteration 9: neue Stichprobe (Seed 20261109), Rohtext ohne Projektkontext, überarbeitete Liste: "
              "66 von 70 = 94,3 % gleich mit dem Vergleichswert zweier KI-Leser (Wilson 86–98 %; Vergleichswert teils zirkulär), Kommilitone 14 von 15; Höchstende 87,1 % (Schwelle 90 % verfehlt). "
              "Die alte Fassung der Liste erreicht auf denselben Losen 65 von 70: Der Nutzen der neuen Regeln ist kaum gesichert. "
              "FRAGE – ANTWORT: „Warum Übereinstimmung mit KI-Lesern als Maß?“ Es gibt keine Wahrheitsquelle außer dem Bekanntmachungstext; Handprüfung ist teuer und hatte Verankerung (It. 6) und Abschreibefehler (It. 7), deshalb zusätzlich KI-Leser mit neutraler Definition „erste feste Laufzeit ohne Optionen“. Alternative: mehr Menschen als Leser; fehlt noch. "
              "ZEIG-MIR-WO: reports/beispiel_liste.md, reports/beispiel_liste_oberpfalz.csv, reports/evaluation_iteration6.md bis 9.")

rect(s, 0.6, 1.4, 8.8, 1.3, WHITE, name="Zeitstrahl Karte")
rect(s, 0.9, 1.55, 4.4, 0.4, BLUE, name="Grundlaufzeit")
box(s, 0.9, 1.55, 4.4, 0.4, "feste Laufzeit (Grundlaufzeit)", size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, 5.35, 1.55, 3.4, 0.4, LBLUE, name="Verlängerung")
box(s, 5.35, 1.55, 3.4, 0.4, "mögliche Verlängerung", size=14, color=DBLUE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, 5.18, 2.03, 0.2, 0.16, BLUE, MSO_SHAPE.ISOSCELES_TRIANGLE, "Marke Grundlaufzeit")
rect(s, 8.65, 2.03, 0.2, 0.16, GREY, MSO_SHAPE.ISOSCELES_TRIANGLE, "Marke Höchstende")
box(s, 0.9, 2.22, 4.4, 0.4, "Ende der Grundlaufzeit: steht in unserer Liste", size=14, bold=True, color=BLUE, align=PP_ALIGN.RIGHT)
box(s, 5.5, 2.22, 3.4, 0.4, "Höchstende: nur Hinweis", size=14, color=GREY, align=PP_ALIGN.RIGHT)
tile(s, 0.6, 2.8, 2.8, 1.4, "66 von 70", "gleiches Enddatum wie zwei KI-Leser", GREEN, "Genauigkeit", zsize=26)
tile(s, 3.6, 2.8, 2.8, 1.4, "9.325", "Lose in der Liste", BLUE, "Lose", zsize=26)
tile(s, 6.6, 2.8, 2.8, 1.4, "79,4 %", "der Lose im letzten Jahr haben ein Enddatum", BLUE, "Enddatum", zsize=26)
kurz(s, "Die Liste nennt je Vertrag das Ende der festen Laufzeit, mit Link zur Bekanntmachung.")
fuss(s, "KI-Leser nicht unabhängig; ein Mensch prüfte 15 Lose, 14 stimmen. 79,4 %: Zuschläge 10/2025 bis 9/2026, nur TED.")

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if args:   # optional: anderer Ausgabepfad (z. B. wenn die Datei in PowerPoint geöffnet ist)
    OUT = Path(args[0])

# Folien 12 bis 14: ausgeblendeter Anhang für die Fragerunde (ob ausgeblendete Folien bei „höchstens 12“ zählen, mit dem Dozenten klären)
if "--ohne-anhang" in sys.argv:
    ids = prs.slides._sldIdLst
    for sld in list(ids)[-3:]:
        prs.part.drop_rel(sld.rId)
        ids.remove(sld)
else:
    for sl in list(prs.slides)[-3:]:
        sl._element.set("show", "0")
OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(len(prs.slides), "Folien (ausgeblendet:", 0 if "--ohne-anhang" in sys.argv else 3, "); Video:", VIDEO_STATUS, "; Demo:", DEMO_STATUS, ";", OUT)
