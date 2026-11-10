"""Foliengerüst für den Vortrag (LN B: 15 min Vortrag + 5 min Fragen, höchstens 12 Inhaltsfolien) mit Sprechernotizen.

Stand nach Iteration 10/10b, Business-Case-Prüfung und Nachtrag Sensitivität (2026-11-09). Gestaltung im Apple-/Keynote-Stil: Titel als Aussagesatz
(höchstens 2 Zeilen), viel Weißraum, weiße Karten auf hellgrauem Grund (F2F2F7), Systemfarben mit fester Bedeutung (Grün = erfüllt/gut,
Rot = verfehlt, Orange = Vorsicht, Blau = neutral/Hervorhebung; dunkle Karte nur für die Publikumsfrage auf Folie 3), Schrift Segoe UI.
Text mindestens 14 pt; Fußnoten und Abschnittszeile 11 pt, Fußnoten einzeilig, ohne Dateipfade (Pfade stehen in den Notizen).
Oben auf jeder Inhaltsfolie eine graue Abschnittszeile (Idee · Betriebe · Markt · Produkt · Prüfung · Fazit), der aktuelle Abschnitt fett und blau.
Unten der Kasten „Kurz gesagt:“ mit der Folgerung für Laien. Notizen je Folie: SPRICHT (erste Zeile), ZEIT, KERNAUSSAGE, FRAGE – ANTWORT, ZEIG-MIR-WO,
KURZ GESAGT, bei Sprecherwechsel ÜBERGANG (letzter Satz). Summe der Zeiten der sichtbaren Folien: 15:00.
Sprecher: Ludwig Richthammer Folien 1, 2, 5, 6, 7, 9 (9:15 Folienzeit, davon 3:32 Video, also etwa 5:45 gesprochen); Manuel Strobel Folien 3, 4, 8, 10, 11 (5:45).
QR-Code zum Repo auf Folie 11: docs/vortrag/qr_repo.png, erzeugt mit segno (requirements.txt).

Folien (11 sichtbar, 6 ausgeblendet):
   1 Titel (0:30)
   2 Video „Franz und die Glaskugel“ (4:15: Einleitung und Quizfrage vor dem Start 0:30, Video 3:32 ohne Pause, Überleitung 0:13)
   3 Betriebe heute und unsere Idee (1:30, mit Publikumsfrage)
   4 Konkurrenz: Vertragsenden kostenlos bei Vergabeweiser (1:15)
   5 Vergleich mit Vergabeweiser, mit Zeitleiste Grundlaufzeit / spätestes Vertragsende (1:15)
   6 Make or Buy aus Sicht des Betriebs (1:00)
   7 Demo als Zielbild (1:00, Bildschirmaufnahme)
   8 So funktioniert es technisch: Pipeline und Prognoseregel (1:00)
   9 KI-Irrwege und Trennung von Entwicklung und Test (1:15)
  10 Empfehlung und Grenzen (1:15)
  11 Fazit (0:45)
  12–17 ausgeblendeter Anhang für die Fragerunde (Vier Versuche, vier verfehlte Schwellen; Frage/Kriterium/Daten; Trefferquote je Vorlauf;
        Liste und Genauigkeit; zwei Sicherungsfolien „Falls die Technik streikt“ mit Terminal-Ausgaben vom 2026-11-09)
Begriff auf den sichtbaren Folien: „spätestes Vertragsende (mit allen Verlängerungen)“ beim ersten Auftreten (Folie 2), danach „spätestes Vertragsende“
(im Code und in den Notizen auch „Höchstende“).
Option --ohne-anhang lässt den Anhang weg (ANHANG Folien). Video: bevorzugt docs/video/franz_video_ton_kurz.mp4 (Kürzung von Manuels Fassung durch Claude für den Vortrag, 3:32,
Stimmen ElevenLabs), Rückfall auf franz_und_die_glaskugel_szenen_0-5_v4.mp4, dann v3, v2, v1. Das Posterbild wird aus dem Video geschnitten
(ffmpeg aus .venv-video, Standbild Glaskugel bei 1:50), sonst gezeichnet. Zahlen aus docs/iterationen.md, docs/business.md §7 bis §9, docs/business_case_auswahl.md, docs/demo_push.md,
reports/evaluation_iteration5.md bis 10b, reports/sensitivitaet_iteration5.md, docs/lab_log.md, docs/fragenrunde.md (Teil A, Sicherungsfolien),
docs/lab_log_bilder/diagramm_vorlauf.png (Bild der Anhangsfolie 14).
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
    ("1C1C1E", "34618F", "FF9F0A", "FF3B30", "34C759", "6E6E73", "F2F2F7", "1C1C1E", "FFFFFF", "AEAEB2", "E4EBF3", "264A70", "D1D1D6"))
# Akzent: gedecktes Stahlblau statt grellem Systemblau #007AFF (Wunsch 2026-11-10)
DAMBER = RGBColor.from_string("B25E00")   # Orange als Schrift (lesbar auf Weiß)
DGREEN = RGBColor.from_string("248A3D")   # Grün als Schrift (lesbar auf Weiß)
HEAD, BODY, MONO = "Segoe UI Semibold", "Segoe UI", "Consolas"   # Ersatz für San Francisco unter Windows

ABSCHNITTE = ("Idee", "Betriebe", "Markt", "Produkt", "Prüfung", "Fazit")

# Kernaussage je Folie (Titel als Aussagesatz, höchstens 2 Zeilen)
TITEL = [None,
    "",
    "Video: Was TED vorhersagt und was nicht",
    "Ein Betrieb hatte nur 28 Tage für sein Angebot; wir wollten Monate daraus machen",
    "Vertragsenden gibt es schon kostenlos bei Vergabeweiser",
    "Bei 27 von 230 Losen weichen wir von Vergabeweiser ab, meist wegen der Zählweise",
    "Im Modell lohnt Selbstbauen nicht; ob Betriebe die Daten im eigenen System brauchen, ist ungeprüft",
    "So hätte das Produkt aussehen sollen: passende Hinweise direkt an die Firma",
    "So funktioniert es technisch: von der TED-Abfrage zur geprüften Liste",
    "Die KI machte Fehler; gefunden wurden sie durch getrennte Prüfung",
    "Nutzbar als Ausgangspunkt, aber nicht als eigenes Produkt",
    "",
    # ausgeblendeter Anhang (Folien 12 bis 17)
    "Vier Versuche, vier verfehlte Schwellen – und was jeder geändert hat",
    "Wer früh weiß, wann ein Auftrag endet, kann sich besser vorbereiten",
    "Auch im Nachhinein erreicht kein Vorlauf die Schwelle von 60 %",
    "Das Vertragsende lässt sich meist lesen: 66 von 70 wie zwei KI-Leser",
    "Falls die Technik streikt: Live-Nachweise als Bild (1/2)",
    "Falls die Technik streikt: Live-Nachweise als Bild (2/2)",
]
ANHANG = 6   # Zahl der ausgeblendeten Folien am Ende

# Wer spricht (erste Zeile jeder Notiz); Anhang: wer die zugehörige sichtbare Folie hält
SPRECHER = {1: "Ludwig", 2: "Ludwig", 3: "Manuel", 4: "Manuel", 5: "Ludwig", 6: "Ludwig", 7: "Ludwig", 8: "Manuel", 9: "Ludwig", 10: "Manuel", 11: "Manuel",
            12: "Ludwig (Anhang, gehört zu Folie 2)", 13: "Ludwig (Anhang, gehört zu Folie 2)", 14: "Manuel (Anhang, gehört zu Folie 8)",
            15: "Ludwig (Anhang, gehört zu Folie 2)", 16: "Manuel (Anhang, gehört zu Folie 8)", 17: "Ludwig (Anhang, gehört zu Folie 9)"}
REPO_URL = "https://github.com/ludwigrichthammer9-web/vergabe_radar"
QR_BILD = ROOT / "docs" / "vortrag" / "qr_repo.png"

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
    s.notes_slide.notes_text_frame.text = "SPRICHT: " + SPRECHER[_nr[0]] + "\n" + notes
    return s


def uebergang(s, text):
    """Übergangssatz zum nächsten Sprecher, als letzter Satz der Notiz (nach KURZ GESAGT)."""
    tf = s.notes_slide.notes_text_frame
    tf.text = tf.text + " ÜBERGANG (letzter Satz, dann übergeben): „" + text + "“"


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
s = new_slide("ZEIT 0:30. EINSTIEG (wörtlich, langsam): „28 Tage. So viel Zeit hatte ein Reinigungsbetrieb mit rund 120 Beschäftigten für Begehung und Kalkulation, kalkuliert wurde nachts. "
              "Lässt sich aus EU-Daten vorhersagen, wann so ein Vertrag neu ausgeschrieben wird? Vorweg: den Termin nicht, das Vertragsende ja, und das gibt es schon kostenlos.“ "
              "(Beleg: Gespräch 1 am 2026-11-05, Betrieb mittlerer Größe, rund 120 Beschäftigte, Meldung 28 Tage vor Abgabe, Kalkulation nachts; docs/business.md §8.9.) "
              "KERNAUSSAGE: Eine Reinigungsfirma will früh wissen, wann ein öffentlicher Vertrag endet und neu ausgeschrieben wird. Wir zeigen, was TED-Daten dazu hergeben "
              "(eine Liste der Vertragsenden), was nicht (eine Terminprognose), und was an der Idee gegenüber der kostenlosen Konkurrenz übrig bleibt. "
              "Ablauf in einem Satz: eine Quizfrage an euch, dann ein Video von ca. 3,5 Minuten (Franz und die Glaskugel: Frage, zwei Irrwege mit verfehlten Schwellen, Liste samt Genauigkeit), dann der längere Teil aus Sicht eines Betriebs: "
              "Wie arbeiten Betriebe, was war unsere Idee, wer bietet es schon, was hätte das Produkt sein sollen, wie funktioniert es technisch, was bleibt. "
              "Kernbotschaft schon jetzt nennen: Die Liste lässt sich aus TED lesen, ein eigenes Produkt ist sie nicht, und ein Qualitätsvorsprung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/iterationen.md (Übersicht und Ergebnis Iteration 10 und 10b), docs/lab_log.md Abschnitt 0.", dark=True, teil="titel")

# Radar-Grafik: Kreise um einen Mittelpunkt
rect(s, 6.1, 0.9, 3.4, 3.4, RGBColor.from_string("E4EBF3"), MSO_SHAPE.OVAL, "Radar außen")
rect(s, 6.6, 1.4, 2.4, 2.4, RGBColor.from_string("C5D4E4"), MSO_SHAPE.OVAL, "Radar mitte")
rect(s, 7.1, 1.9, 1.4, 1.4, BLUE, MSO_SHAPE.OVAL, "Radar innen")
rect(s, 8.15, 1.55, 0.3, 0.3, AMBER, MSO_SHAPE.OVAL, "Radar Punkt")
box(s, 0.6, 1.35, 5.2, 1.0, "Vergabe-Radar", size=48, color=INK, font=HEAD, name="Titel")
box(s, 0.6, 2.4, 5.1, 1.2, "Wann endet ein öffentlicher Auftrag, und wer weiß es schon?", size=24, color=GREY, name="Untertitel")
box(s, 0.6, 3.75, 5.1, 0.6, "Was die EU-Plattform TED verrät und was nicht", size=16, color=BLUE, name="Zusatz")
box(s, 0.6, 4.65, 8.4, 0.3, "Manuel Strobel · Ludwig Richthammer", size=16, color=INK, font=HEAD, name="Namen")
box(s, 0.6, 5.0, 8.0, 0.3, "Big Data Analytics · Leistungsnachweis B", size=14, color=GREY, name="Autoren")
s.notes_slide.notes_text_frame.text += " KURZ GESAGT (für Laien): Wir haben geprüft, ob man aus öffentlichen Daten vorhersagen kann, wann ein Reinigungsauftrag neu ausgeschrieben wird."

# Folie 2: Video ---------------------------------------------------------
VIDEO_KANDIDATEN = ("franz_video_ton_kurz.mp4",                      # Kürzung von Manuels Fassung (Claude; 3:32, Stimmen ElevenLabs, ohne Runde 4)
                    "franz_und_die_glaskugel_szenen_0-5_v4.mp4",     # v4: Edge-Stimmen (Microsoft Neural), sonst wie v3
                    "franz_und_die_glaskugel_szenen_0-5_v3.mp4",
                    "franz_und_die_glaskugel_szenen_0-5_v2.mp4",     # Piper-Stimme
                    "franz_und_die_glaskugel_szenen_0-5.mp4")        # SAPI-Stimme
VIDEO = next((ROOT / "docs" / "video" / n for n in VIDEO_KANDIDATEN if (ROOT / "docs" / "video" / n).exists()),
             ROOT / "docs" / "video" / VIDEO_KANDIDATEN[0])
POSTER = ROOT / "docs" / "vortrag" / "poster_franz_und_die_glaskugel.png"
POSTER_SEKUNDE = 110   # Standbild im Kurzfilm: Franz mit der Glaskugel „Vertragsende − 6 Monate“ (vor der Quizfrage, keine Auflösung)


def poster_aus_video(video, pfad, sekunde=POSTER_SEKUNDE):
    """Standbild aus dem Video schneiden (ffmpeg aus .venv-video) und unten eine Leiste „Kurzfilm · ca. 3,5 Minuten · Abspielen“ darüberlegen.
    Gibt True zurück, wenn es geklappt hat."""
    import subprocess
    import tempfile
    from PIL import Image, ImageDraw, ImageFont
    ffmpeg = sorted((ROOT / ".venv-video" / "Lib" / "site-packages" / "imageio_ffmpeg" / "binaries").glob("ffmpeg*.exe"))
    if not ffmpeg:
        return False
    with tempfile.TemporaryDirectory() as tmp:
        bild = Path(tmp) / "standbild.png"
        r = subprocess.run([str(ffmpeg[-1]), "-v", "error", "-y", "-ss", str(sekunde), "-i", str(video), "-frames:v", "1", str(bild)], capture_output=True)
        if r.returncode != 0 or not bild.exists():
            return False
        with Image.open(bild) as roh:
            im = roh.convert("RGB").resize((1600, 900))
    d = ImageDraw.Draw(im)
    try:
        f1 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 46)
        f2 = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 40)
    except OSError:
        f1 = f2 = ImageFont.load_default()
    d.rectangle((0, 745, 1600, 900), fill=(28, 28, 30))               # verdeckt die Untertitelzeile des Standbilds
    d.polygon([(70, 790), (70, 870), (140, 830)], fill=(255, 255, 255))
    d.text((180, 798), "Franz und die Glaskugel", font=f1, fill=(255, 255, 255))
    d.text((760, 804), "Kurzfilm · ca. 3,5 Minuten · Abspielen", font=f2, fill=(174, 174, 178))
    pfad.parent.mkdir(parents=True, exist_ok=True)
    im.save(pfad)
    return True


def poster_erzeugen(pfad):
    """Rückfall ohne ffmpeg: Posterbild 1600x900 aus der Foliengestaltung (dunkle Fläche, Glaskugel, Abspielzeichen)."""
    from PIL import Image, ImageDraw, ImageFont
    w, h = 1600, 900
    im = Image.new("RGB", (w, h), (28, 28, 30))
    d = ImageDraw.Draw(im)
    d.ellipse((1000, 160, 1480, 640), fill=(44, 44, 46))
    d.ellipse((1080, 240, 1400, 560), fill=(58, 58, 60))
    d.ellipse((1160, 320, 1320, 480), fill=(52, 97, 143))
    d.ellipse((1290, 270, 1340, 320), fill=(255, 159, 10))
    try:
        f1 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 92)
        f2 = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 44)
    except OSError:
        f1 = f2 = ImageFont.load_default()
    d.text((100, 300), "Franz und", font=f1, fill=(255, 255, 255))
    d.text((100, 410), "die Glaskugel", font=f1, fill=(255, 255, 255))
    d.text((100, 560), "Kurzfilm · ca. 3,5 Minuten", font=f2, fill=(174, 174, 178))
    d.polygon([(100, 700), (100, 790), (180, 745)], fill=(255, 255, 255))
    d.text((210, 715), "Abspielen", font=f2, fill=(255, 255, 255))
    pfad.parent.mkdir(parents=True, exist_ok=True)
    im.save(pfad)


s = new_slide("ZEIT 4:15 = Einleitung und Quizfrage vor dem Start 0:30 + Video 3:32 (läuft ohne Pause durch) + Überleitung 0:13. "
              "KERNAUSSAGE: Der Kurzfilm „Franz und die Glaskugel“ erzählt die ersten Zyklen des Projekts: "
              "Franz (Gebäudereiniger, erfährt alles zu spät), Rathaus und Ausschreibung, die Idee einer Glaskugel, TED als Datenquelle, CRISP-DM als Vorgehen; "
              "Runde 1: Vorgänger zuordnen, 11 von 24 Vorschlägen richtig (Schwelle verfehlt). "
              "KLARSTELLUNG zu 11 von 24 (Iteration 3, docs/iterationen.md, reports/evaluation_iteration3.md): Das ist die Präzision der Vorschläge (V2 = 11/24 = 45,8 %, Schwelle 80 %), NICHT der Anteil gefundener Vorgänger; "
              "gefunden wurden 11 von 38 Vorgängern (Trefferquote V3 = 28,9 %, Schwelle 60 %). Die ausgeblendete Folie 12 zeigt für denselben Versuch die Trefferquote 28,9 %; beides ist verfehlt, die Zahlen messen Verschiedenes. "
              "Runde 2: die Glaskugel „spätestes Vertragsende minus 6 Monate“ (Regel R1: Höchstende, also Ende mit allen Verlängerungen, minus 6 Monate), 28,8 % gegen 17,3 % der einfachen Vergleichsregel, Ziel 60 %; dazu die Vergabestelle: „Option wird meist verlängert“; "
              "Runde 3: die Vertragsliste, 66 von 70 Stichproben mit gleichem Enddatum wie zwei KI-Leser, ein Mensch prüft 15, 9.325 Lose. "
              "Abspann: „Franz gibt es nicht. Die Daten schon.“ und der Satz „Vorhersagen? Mit unserer einfachen Regel nicht. Selbst bauen? Lohnt sich nach unserem Modell nicht. Wie sicher wir uns sind und wo nicht, zeigen wir euch jetzt.“ "
              "Das Video ersetzt die Folien Vier Versuche, Frage/Kriterium/Daten und Liste und Genauigkeit (ausgeblendet im Anhang, Folien 12, 13 und 15). "
              "RUNDE 4 BEWUSST NICHT IM VIDEO: Die Kurzfassung lässt Runde 4 (kostenlose Liste bei Vergabeweiser, Vergleich auf 230 Losen, Waage Make or Buy, Oberpfalz, Bauplan) weg, weil die Folien 4 bis 6 genau das danach live zeigen (dazu Folie 7 Demo, Folie 8 Technik). "
              "BEGRIFF: Auf Karte 2 steht beim ersten Auftreten „spätestes Vertragsende (mit allen Verlängerungen)“, danach auf allen Folien nur „spätestes Vertragsende“ (in Dateien: Höchstende). "
              "ABLAUF: (1) Einleitung 0:15: Daten und Kriterium in einem Satz sagen: TED, Gebäudereinigung, Deutschland, Daten ab Okt. 2016 (Liste: eForms ab Okt. 2023), "
              "Treffer = Neuausschreibung im Fenster ±3 Monate, Schwelle 60 % vorab festgelegt. "
              "(2) QUIZFRAGE VOR DEM START, ca. 0:15 (wörtlich): „Bevor der Film läuft: Wie oft trifft ‚spätestes Vertragsende minus 6 Monate‘ den Termin auf ±3 Monate? Hand hoch: über 60 %, 30 bis 60, unter 30?“ "
              "Hände kurz zählen, nicht auflösen. (3) Video starten (Folie anklicken, Wiedergabe), Länge 3:32, OHNE PAUSE durchlaufen lassen; die Auflösung kommt im Video bei ca. 2:10 (28,8 % gegen 17,3 %, also „unter 30“). "
              "Die Frage im Video (etwa 2:02 bis 2:06) ist dann nur noch Erinnerung, nicht anhalten. "
              "(4) Überleitung nach dem Abspann, 0:13 (knapp): wörtlich „Das Video vereinfacht: Der Mensch, der 15 Fälle prüfte, ist Manuel aus unserem Team; die Vergabestelle ist ein einziges Gespräch, ein Hinweis; "
              "‚lohnt nicht‘ heißt: im Kostenmodell mit Annahmen nie günstiger als ein kostenloser Dienst.“ (Quelle: Prüfung in docs/video/README.md, Szene 31 V6 Teammitglied, Szene 23 Vergabestelle n = 1; Kostenmodell reports/make_or_buy.md), "
              "dann den Übergangssatz am Ende dieser Notiz. Nur bei Zeitreserve vorher kurz auf die Handzeichen zurückkommen („Wer hatte unter 30?“). "
              "SICHERUNG, falls das Video nicht läuft: die drei Karten rechts nennen die Kernzahlen (11 von 24 Vorschlägen richtig · 28,8 % statt 60 % · 66 von 70); die Geschichte in 60 Sekunden frei erzählen, Quizfrage trotzdem vorher stellen; "
              "bei Bedarf die ausgeblendete Folie 12 (Vier Versuche) über die Foliensortierung zeigen. Details in den ausgeblendeten Folien 12 bis 15. "
              "HINWEISE: Die Animation hat Manuel Strobel KI-gestützt erstellt; Ludwig Richthammer und Manuel Strobel haben sie gemeinsam überarbeitet (Zahlen gegen Belege geprüft, zu starke Sätze eingeschränkt). Stimmen KI-generiert (ElevenLabs, laut Abspann), Figuren erfunden. Das im Vortrag offen sagen. "
              "EHRLICHE EINSCHRÄNKUNGEN (bei Nachfrage oder in einem Satz am Ende): Die Figuren (Franz) sind erfunden, die Gespräche sind im Video nachgestellt (die drei echten Telefongespräche, n = 3, sind nur Hinweise, keine Belege). "
              "Die 66 von 70 heißen nur: gleiches Enddatum wie der Vergleichswert zweier KI-Leser; die Leser sind nicht unabhängig (gleiche Modellfamilie), und ihr Vergleichswert ist teils zirkulär (er nutzt wie die Liste das Feld als Ende der Grundlaufzeit); "
              "dazu prüfte ein Kommilitone 15 Lose, 14 stimmen. Der Vergleichswert 17,3 % der Terminprognose ist die einfache Regel R0 (Ende der Grundlaufzeit minus 6 Monate) auf denselben 52 Paaren; die Paare stammen aus einer Rückwärtssuche. "
              "Ein Qualitätsvorsprung gegenüber der Konkurrenz ist nicht belegt (Folien 4 und 5). "
              "FRAGE – ANTWORT: „Warum ±3 Monate, warum 60 %?“ Das Fenster und die Schwelle wurden vor der Rechnung gesetzt, ohne Kundenkontakt, begründete Setzung (Anhang Folien 12 und 13). "
              "Nachträglich, kein neuer Test: Auch mit dem im Nachhinein besten Vorlauf bleibt R1 bei 28,8 % (Folie 8, Anhang Folie 14). "
              "„Waren die 66 von 70 nicht vom Entwickler selbst bewertet?“ Nein, neue Stichprobe, Rohtext ohne Projektkontext, aber KI-Leser nicht unabhängig (Folie 9, Anhang Folie 15). "
              "ZEIG-MIR-WO: docs/video/franz_video_ton_kurz.mp4 (Langfassung mit Runde 4: docs/video/franz_video_ton.mp4, 4:28), docs/video/README.md (Korrekturen), docs/iterationen.md, reports/backtest_iteration5.md, reports/evaluation_iteration3.md bis 9, Anhang Folien 12 bis 15.",
              teil="Idee")
if VIDEO.exists():
    if not poster_aus_video(VIDEO, POSTER):
        poster_erzeugen(POSTER)
    s.shapes.add_movie(str(VIDEO), Inches(0.6), Inches(1.4), Inches(4.97), Inches(2.8), poster_frame_image=str(POSTER), mime_type="video/mp4").name = "Video Franz und die Glaskugel"
    VIDEO_STATUS = "eingebettet"
else:
    rect(s, 0.6, 1.4, 4.97, 2.8, DARK, name="Video Platzhalter")
    box(s, 0.85, 1.6, 4.5, 2.4, [[("Video hier einbetten", {"bold": True, "color": AMBER, "size": 20, "font": HEAD})],
        [("Datei noch nicht vorhanden. Skript erneut ausführen, dann wird das Video automatisch eingebettet.", {"color": SOFT, "size": 14})]],
        space=10, anchor=MSO_ANCHOR.MIDDLE, name="Video Platzhalter Text")
    VIDEO_STATUS = "Platzhalter"
for i, (zahl, text, f) in enumerate((("11 von 24", "Vorschlägen richtig: Runde 1 verfehlt", RED),
                                      ("28,8 % statt 60 %", "„Spätestes Vertragsende (mit allen Verlängerungen) − 6 Monate“", RED),
                                      ("66 von 70", "gleiches Enddatum wie zwei KI-Leser", GREEN))):
    y = 1.4 + i * 0.955
    rect(s, 5.77, y, 3.63, 0.89, WHITE, name=f"Kernzahl {i + 1} Karte")
    box(s, 5.97, y + 0.02, 3.3, 0.36, zahl, size=22, color=f, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name=f"Kernzahl {i + 1} Zahl")
    box(s, 5.97, y + 0.37, 3.3, 0.48, text, size=14, name=f"Kernzahl {i + 1} Text")
kurz(s, "Wann neu ausgeschrieben wird, sagt niemand voraus; wann ein Vertrag endet, lässt sich meist lesen.")
fuss(s, "Animation: Manuel Strobel (KI-gestützt), gemeinsam überarbeitet; Stimmen KI-generiert (ElevenLabs), Figuren erfunden.")
uebergang(s, "Franz ist erfunden, die drei Gespräche nicht. Manuel.")


# Folie 3: Betriebe heute und unsere Idee ----------------------------------------
s = new_slide("ZEIT 1:30 (Prozesskarten zeigen, je einen Satz zu Meldung und Begehung; die Idee-Kette in einem Atemzug; Publikumsfrage etwa 0:20). "
              "KERNAUSSAGE: Ab hier der Teil, den wir zu knapp behandelt hatten und den das Video bewusst auslässt (Runde 4): das Business Understanding aus Sicht eines Gebäudereinigers (Folien 3 bis 7, zusammen 6:00 = 40 % der Zeit). "
              "Zuerst, wie Betriebe heute vorgehen und was unsere Idee für sie war, dann die Konkurrenz. "
              "OBERE REIHE, PROZESS (Fakten, drei Gespräche des Nutzers am 2026-11-05; 9 Anrufe, 3 erreicht, 105 Minuten; Notizen ohne Namen; n = 3, Hinweise, keine Belege): Betrieb mittlerer Größe (rund 120 Beschäftigte): "
              "Meldung der Ausschreibung 28 Tage vor Abgabe; eng bei der Objektbegehung (ein Termin, der beste Vorarbeiter krank); Kalkulation nachts; Entscheidung mitzubieten „hauptsächlich Entfernung und Personal“; "
              "Vertragsenden bei anderen „eine Blackbox“. Kleinbetrieb (rund 15 Beschäftigte): Entscheidung nach Kapazität des Teams; die Bürokratie (viele Eigenerklärungen) ist der Engpass. "
              "Vergabestelle: plant etwa 9 Monate vor Vertragsende, verlängert „fast immer, wenn eine Option im Vertrag steht“, vergibt „sehr oft“ unterhalb der EU-Schwelle (also nicht auf TED). "
              "MITTLERE KARTE, UNSERE IDEE (so steht es in den Quellen): (1) Zuschläge enthalten meist ein Vertragsende oder eine Laufzeit (Annahme A4, bestätigt: Laufzeitende bei Gebäudereinigung in 80,9 % der Zuschläge bestimmbar, 90,0 %, wenn eine Dauer ohne Beginn mitzählt; Iteration 1, 440 Zuschläge, docs/iterationen.md). "
              "(2) Also ist das Vertragsende bekannt. (3) Annahme A8: „Eine Neuausschreibung erscheint ungefähr zum Vertragsende minus einer typischen Vorlaufzeit.“ "
              "(4) Nutzen laut fachlichem Kriterium (docs/business.md §7.1): „Der Betrieb kann Angebot, Referenzen und Personal gezielt vorbereiten, statt Bekanntmachungen dauernd zu beobachten.“ "
              "Also statt rund 28 Tagen ab Meldung Monate für Begehung, Kalkulation, Personal und Referenzen. Gespräch 1 bestätigt den Wunsch („Absolut“: Personal in der Zielregion früher suchen), der Kleinbetrieb nicht („Eigentlich nicht“). "
              "Ehrlich: A8 wurde in Iteration 5 widerlegt (28,8 %, Video); A1 und A15 (Betriebe wollen früh wissen und zahlen dafür) sind ungeprüft. "
              "PUBLIKUMSFRAGE (dunkle Karte, am Ende der Folie; 20 Sekunden, Handzeichen): „Gibt es kostenlos eine Liste auslaufender öffentlicher Verträge?“ Ja / nein / weiß nicht. Auflösung auf Folie 4: Ja, Vergabeweiser. "
              "Zwischenstand: 0:30 nach Folie 1, 4:45 nach Folie 2, 6:15 nach Folie 3, 7:30 nach Folie 4; liegt ihr nach Folie 2 hinten, die Frage als Satz überspringen und direkt auf Folie 4 auflösen. "
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
s.notes_slide.notes_text_frame.text += (" ZEITNOT (Streichliste, siehe Folie 11): die Publikumsfrage nur als Satz stellen und sofort auf Folie 4 auflösen.")

# Folie 4: Konkurrenz ------------------------------------------------------------
s = new_slide("ZEIT 1:15. KERNAUSSAGE: Auflösung der Publikumsfrage: Ja, es gibt sie kostenlos. Vergabeweiser listet 1.005 Gebäudereinigungs-Verträge, die in 12 Monaten enden, mit Zuschlagsempfänger, Zahl der Angebote und Verlängerungsoptionen, "
              "nach eigener Angabe auch unterhalb der EU-Schwelle (von uns nicht gemessen). "
              "TABELLE (Prüfstand): Vergabeweiser sowie die Vertragsende-Seite und die Preisseite von AusschreibungsRadar hat Claude am 2026-11-05 selbst nachgelesen (docs/business.md §8.2; Lab-Log Abschnitt 1: „Seiten und Preisseite von uns gelesen“); "
              "AusschreibungsRadar laut Preisseite (netto, monatlich kündbar): Free 0 €, Starter 29 € mit voller KI-Eignungsanalyse, Business 79 € mit Match-Score und Bid/No-Bid-Check, Professional 149 € (docs/quellen.md nennt dazu eine Watchlist für 9 €); "
              "Stand 2026-11-05, seitdem nicht erneut geprüft; die Funktionen sind nur gelesen, nicht getestet. "
              "aufträge.io (43.373 Verträge mit Ende in 12 Monaten, auf Anfrage) und subreport (84–198 € im Monat) stammen aus der Recherche eines Agenten und sind nicht einzeln nachgeprüft; "
              "DTAD nach Aussage des Betriebs mittlerer Größe: knapp 1.500 € im Jahr, eine Liste auslaufender Verträge kenne er dort nicht. Beide geprüften deutschen Anbieter schreiben selbst, dass der Auftraggeber über die Neuausschreibung entscheidet. "
              "HINWEIS (Fakt, Paket A, 130 Oberpfalz-Lose): Auftragnehmer genannt bei 99,2 %, Zuschlagswert über 1 € nur bei 47,7 %, Zahl der Angebote bei 60,8 %. TED-Daten allein reichen für Preisbenchmarks also nur zur Hälfte. "
              "Beobachtung (Hypothese, n = 3): Zwei Betriebe nutzen keinen der Dienste, einer kannte sie vom Hörensagen, die andere gar nicht: eher ein Bekanntheits- als ein Angebotsproblem der Konkurrenz. "
              "FRAGE – ANTWORT: „Warum nicht einfach Vergabeweiser nutzen?“ Doch, für die Suche nach Vertragsenden spricht vieles dafür: kostenlos, nach eigener Angabe auch unterschwellige Verfahren, Zuschlagsempfänger und Bieterzahl. "
              "Unsere Liste ist als eigenes Produkt nicht tragfähig; die Sicht des Betriebs (selbst bauen) steht auf Folie 6. "
              "SPALTE „STAND DER PRÜFUNG“: Vergabeweiser „nachgelesen“ = Seite und API selbst geprüft und genutzt; AusschreibungsRadar „Preise nachgelesen“ = Vertragsende-Seite und Preisseite selbst gelesen (Preise also nicht aus der Recherche); "
              "subreport „Recherche“ = Preis aus der Recherche eines Agenten, nicht einzeln geprüft; DTAD „Gespräch“ = Angabe des Betriebs. "
              "SPALTE „VERTRAGSENDEN?“ (docs/lab_log.md Abschnitt 1, Tabelle Konkurrenz; docs/business.md §8.2 und §8.9): ja = Funktion auf der Anbieterseite selbst nachgelesen (Vergabeweiser, AusschreibungsRadar, Stand 2026-11-05); "
              "aufträge.io „ja, ungeprüft“ = 43.373 Verträge mit Ende in 12 Monaten laut Recherche, nicht selbst nachgelesen, Preis auf Anfrage; subreport und DTAD „nicht belegt“ = eine Funktion für auslaufende Verträge steht in unseren Quellen nicht "
              "(DTAD: der Betrieb kennt dort keine Listen auslaufender Verträge). „Nicht belegt“ heißt nicht „gibt es nicht“. "
              "ZEIG-MIR-WO: docs/business.md §8.2 (Wettbewerber), §8.7 (Marktzahlen), reports/nebentest_ausschreibungsradar.md, reports/wettbewerbsbild_oberpfalz.md.",
              teil="Markt")

box(s, 0.6, 1.38, 8.8, 0.5, [[("Vergabeweiser: ", {"bold": True}), ("1.005 Reinigungsverträge enden in den nächsten 12 Monaten, mit Auftragnehmer und Zahl der Angebote.", {})]], size=14, name="Vergabeweiser Satz")
spalten = ((0.8, 2.3, "Anbieter"), (3.15, 1.6, "Vertragsenden?"), (4.85, 2.2, "Preis"), (7.15, 2.15, "Stand der Prüfung"))
for x, w, k in spalten:
    box(s, x, 1.9, w, 0.26, k, size=14, color=GREY, name="Kopf " + k)
zeilen = (("Vergabeweiser", "ja", "kostenlos", "nachgelesen"), ("AusschreibungsRadar", "ja", "0–149 € im Monat", "Preise nachgelesen"),
          ("subreport", "nicht belegt", "84–198 € im Monat", "Recherche"), ("DTAD", "nicht belegt", "rund 1.500 € im Jahr", "Gespräch"),
          ("aufträge.io", "ja, ungeprüft", "auf Anfrage", "Recherche"))
for i, (n, v, p, t) in enumerate(zeilen):
    y = 2.2 + i * 0.41
    rect(s, 0.6, y, 8.8, 0.36, WHITE, radius=0.12, name=n + " Zeile")
    box(s, 0.8, y, 2.3, 0.36, n, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 3.15, y, 1.6, 0.36, v, size=14, bold=(v == "ja"), color=DGREEN if v == "ja" else GREY, anchor=MSO_ANCHOR.MIDDLE, name=n + " Vertragsenden")
    box(s, 4.85, y, 2.2, 0.36, p, size=14, bold=(i == 0), color=BLUE if i == 0 else INK, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 7.15, y, 2.15, 0.36, t, size=14, color=GREY, anchor=MSO_ANCHOR.MIDDLE)
kurz(s, "Wer nur Vertragsenden sucht, braucht kein Abo.")
fuss(s, "nachgelesen = selbst gelesen · Recherche = nicht einzeln geprüft · nicht belegt = in unseren Quellen nicht genannt")
uebergang(s, "Wenn es die Liste kostenlos gibt, ist unsere wenigstens anders? Ludwig.")

# Folie 5: Vergleich mit Vergabeweiser ------------------------------------------------------------
s = new_slide("ZEIT 1:15. ZEITLEISTE OBEN zuerst erklären (10 Sekunden): Ein Vertrag hat eine feste Laufzeit (Grundlaufzeit); danach kann die Verwaltung Verlängerungen ziehen. "
              "Das späteste Vertragsende (in unseren Dateien „Höchstende“) ist das Ende mit allen Verlängerungen. Unsere Liste nennt das Ende der Grundlaufzeit; Vergabeweiser nennt in einem Teil der Fälle das späteste Ende (Balken „spätestes Ende gemeint“). "
              "KERNAUSSAGE: Wir haben vorab festgelegt und dann geprüft, ob unsere Liste das Ende der Grundlaufzeit häufiger trifft als Vergabeweiser. "
              "Die Abweichung 27 von 230 Losen (11,7 %) steht im Titel. "
              "Ergebnis: Auf zwei Stichproben weichen beide bei 27 von 230 Losen voneinander ab (11,7 %); nur unsere Liste richtig ist bei 23 von 230 Losen (10,0 %, Wilson etwa 6,8–14,6 %, roh gepoolt laut reports/evaluation_iteration10b.md). Darin steckt M54: Unsere Pipeline hatte Vergabeweiser einen fremden Eintrag zugeordnet (Vreden statt Lengerich), also unser Fehler, kein Lesefehler von Vergabeweiser; ohne M54 wären es 22 von 230 (eigene Rechnung, Fußnote ¹; Balken „Zuordnung falsch“). "
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

# Zeitleiste (aus der Anhangsfolie „Liste und Genauigkeit“): Beginn → Ende der Grundlaufzeit → Verlängerungen → spätestes Vertragsende
rect(s, 0.6, 1.36, 8.8, 0.84, WHITE, name="Zeitleiste Karte")
x0, x1, x2 = 0.85, 5.0, 8.95
rect(s, x0, 1.44, x1 - x0, 0.32, BLUE, radius=0.08, name="Zeitleiste Grundlaufzeit")
box(s, x0, 1.44, x1 - x0, 0.32, "feste Laufzeit (Grundlaufzeit)", size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, x1 + 0.04, 1.44, x2 - x1 - 0.04, 0.32, LBLUE, radius=0.08, name="Zeitleiste Verlängerungen")
box(s, x1 + 0.04, 1.44, x2 - x1 - 0.04, 0.32, "Verlängerungen (Optionen)", size=14, color=DBLUE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, x1 - 0.08, 1.79, 0.16, 0.12, BLUE, MSO_SHAPE.ISOSCELES_TRIANGLE, "Marke Ende Grundlaufzeit")
rect(s, x2 - 0.08, 1.79, 0.16, 0.12, GREY, MSO_SHAPE.ISOSCELES_TRIANGLE, "Marke spätestes Vertragsende")
box(s, x0, 1.9, 1.2, 0.26, "Beginn", size=14, color=GREY, name="Zeitleiste Beginn")
box(s, x1 - 2.2, 1.9, 2.3, 0.26, "Ende der Grundlaufzeit", size=14, bold=True, color=BLUE, align=PP_ALIGN.RIGHT, name="Zeitleiste Ende GL")
box(s, x2 - 2.6, 1.9, 2.7, 0.26, "spätestes Vertragsende", size=14, bold=True, color=GREY, align=PP_ALIGN.RIGHT, name="Zeitleiste spätestes Ende")

rect(s, 0.6, 2.3, 4.0, 1.92, WHITE, name="Vergleich Karte")
box(s, 0.8, 2.36, 3.6, 0.28, "Gleiches Enddatum wie zwei KI-Leser", size=14, bold=True, color=GREY, name="Vergleich Kopf")
box(s, 0.8, 2.64, 1.9, 0.42, "66 von 70", size=26, color=BLUE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name="Vergleich Liste Zahl")
box(s, 0.8, 3.06, 1.9, 0.28, "bei uns", size=14, name="Vergleich Liste Text")
box(s, 2.6, 2.64, 1.9, 0.42, "58 von 70", size=26, color=GREY, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name="Vergleich VW Zahl")
box(s, 2.6, 3.06, 1.9, 0.28, "bei Vergabeweiser", size=14, name="Vergleich VW Text")
box(s, 0.8, 3.42, 3.65, 0.76, [[("Nur bei uns richtig: ", {"bold": True}), ("23 von 230 (10 %)¹", {})],
                              [("Meist zählen wir anders, nicht besser.", {"bold": True, "color": BLUE})]], size=14, space=4, name="Vergleich Text")
rect(s, 4.75, 2.3, 4.65, 1.92, WHITE, name="Ursachen Karte")
box(s, 4.95, 2.36, 4.3, 0.28, "Warum 15 von 160 Losen abweichen", size=14, bold=True, color=GREY)
balken(s, 4.8, 2.6, 4.55, 1.6, ["spätestes Ende gemeint", "Teilauftrag (Los)", "Ursache offen", "Zuordnung falsch¹", "mehrdeutig"],
       [7, 4, 2, 1, 1], [BLUE, BLUE, GREY, GREY, GREY], "Ursachen der 15 abweichenden Lose", maximum=9, fmt='0')
kurz(s, "Beide Listen sind brauchbar; das Datum in der Bekanntmachung selbst nachlesen.")
fuss(s, "¹ Darin 1 Zuordnungsfehler unserer Pipeline (ohne ihn 22). Vorab-Schwelle (≥ 16 Lose) war unerreichbar, offen berichtet.")

# Folie 6: Make or Buy ------------------------------------------------------------
s = new_slide("ZEIT 1:00 (gekürzt: Balken in einem Satz, dann die drei Karten; symmetrische Variante und Ausblick nur bei Nachfrage). KERNAUSSAGE: Aus Sicht eines Betriebs, der seine Aufträge selbst filtern könnte (Make or Buy): Im Modell rechnet sich Selbstbauen gegen kostenlose Dienste nicht; "
              "ob Betriebe die Daten in ihrem eigenen System brauchen, ist ungeprüft; ebenso Nachfrage und Zahlungsbereitschaft (Lab-Log §1 und §7). Als eigenes Produkt ergibt die Liste keinen Sinn. "
              "BALKEN LINKS (Paket D, Quelle reports/make_or_buy.md, docs/business.md §9.4; ALLE Kosten sind Annahmen): Rechnung bei 100 € pro Stunde: Niedrig (20 h einmalig, 5 h im Jahr) 3.500 € in drei Jahren, Mittel (60 h, 20 h) 12.000 €, Hoch (120 h, 50 h) 27.000 €. "
              "Break-even im Basismodell: gegen DTAD (knapp 1.500 € im Jahr, Gespräch) nur im Szenario Niedrig, nach 2,0 Jahren; gegen AusschreibungsRadar Starter und gegen Vergabeweiser nie. "
              "KARTE 1: Dieses „nie“ ist eine Folge der Modellkonstruktion (Abos und kostenlose Dienste ohne Eigenaufwand gerechnet, Eigenbau mit Stunden), keine Messung. "
              "SYMMETRISCHE VARIANTE (Annahmen): Rechnet man auch für Abo und kostenlose Dienste Nutzungsstunden (10 / 30 / 60 Stunden im Jahr), liegt der Break-even gegen DTAD bei 1,0 / 2,4 / 4,8 Jahren und gegen einen kostenlosen Dienst mit Übernahme von Hand bei 4,0 / 6,0 / 12,0 Jahren. "
              "KARTE 2 (docs/business.md §9.4): Die Kosten der ersten drei Jahre entsprechen 0,14 bis 1,08 zusätzlichen Aufträgen (Marge 5 %, Median-Jahresumsatz 167.404 €, Deckungsbeitrag 25.110 € je Auftrag ohne Angebotsaufwand und Zuschlagswahrscheinlichkeit); "
              "eine Rechengröße, kein Nutzenbeleg. Nicht die Kostenfrage entscheidet, sondern ob ein früher Hinweis überhaupt einen Auftrag bringt (nicht belegt). "
              "KARTE 3 (docs/business.md §8.9, docs/business_case_auswahl.md; Aussage aus EINEM Gespräch, Zahlungsbereitschaft nicht geprüft): Gezahlt hätte im Gespräch nur der größere Betrieb, und zwar für alte Preise und den aktuellen Auftragnehmer („wenn der aktuelle Dienstleister bei 18 Euro pro Stunde lag, brauche ich gar nicht erst mitbieten“). "
              "Preise je Einheit, Mengen und Vertragsklauseln stehen nicht in öffentlichen Daten; den Zuschlagswert als Gesamtsumme nennt TED nur bei knapp der Hälfte der Lose (47,7 %). "
              "WICHTIG: Karte 3 heißt NICHT, dass ein Abo alte Stundenpreise liefert; ob ein Dienst das kann, haben wir nicht geprüft. Die Karte sagt nur, wofür im Gespräch gezahlt würde und dass es in offenen Daten fehlt. "
              "KURZ GESAGT = unser Rat, gleicher Wortlaut wie auf Folie 10, im Lab-Log und in der Entscheidungsvorlage: kostenlosen Alarm nutzen; Abo nur, wenn eine Funktion fehlt, vorher testen; nicht selbst bauen, solange niemand Treffer von Hand ins eigene System überträgt. "
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
          [("Ein Betrieb sagte: ", {"bold": True}), ("Zahlen würde er für alte Preise. Stundenpreise stehen in keinen offenen Daten.", {})])
for i, k in enumerate(karten):
    y = 1.4 + i * 0.97
    rect(s, 5.2, y, 4.2, 0.86, WHITE, name=f"Make or Buy Karte {i + 1}")
    box(s, 5.4, y, 3.85, 0.86, [k], size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Make or Buy Text {i + 1}")
kurz(s, "Kostenlosen Alarm nutzen · Abo nur, wenn eine Funktion fehlt – vorher testen · nicht selbst bauen, solange niemand Treffer von Hand ins eigene System überträgt.", y=4.25, h=0.66)
fuss(s, "Annahmen: 100 € je Stunde; Niedrig 20 h einmalig + 5 h im Jahr, Mittel 60 + 20, Hoch 120 + 50; Marge 5 %.")
s.notes_slide.notes_text_frame.text += (" ZEITNOT (Streichliste, siehe Folie 11): nur den Balken erklären (3.500 bis 27.000 € in drei Jahren, alles Annahmen) und den Rat vorlesen; die drei Karten weglassen.")

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
s.notes_slide.notes_text_frame.text += (" ZEITNOT (Streichliste, siehe Folie 11): die Aufnahme nur 30 Sekunden laufen lassen (Trichter bis 2 Treffer, dann die Teams-Karte), dann stoppen.")
uebergang(s, "Wie die Daten in diese Demo kommen, zeigt Manuel.")

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
              "BEGRIFF: Im Code heißt das späteste Vertragsende (mit allen Verlängerungen) „hoechstende“. LIVE-NACHWEIS IN DER FRAGENRUNDE (läuft ohne Rohdaten, liest die Paare aus reports/backtest_iteration5.md; Sicherung als Bild: Anhang Folie 16): `python src/model/sensitivitaet_backtest.py --vorlauf 9 --fenster 2` → R1: 2 von 52 = 3,8 %, R0: 1 von 52 = 1,9 %. "
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
        [("def ", {"color": BLUE}), ("r1(gl, hoechstende):", {}), ("  # spätestes Ende, sonst Grundlaufzeit", {"color": DGREEN})],
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
uebergang(s, "Viel davon hat eine KI programmiert. Warum wir ihr nicht ungeprüft geglaubt haben: Ludwig.")

# Folie 9: KI-Irrwege ------------------------------------------------------------
s = new_slide("ZEIT 1:15 (Teil 1 Irrwege etwa 0:40, Teil 2 Trennung von Entwicklung und Test etwa 0:35). KERNAUSSAGE: Claude Code hat Regeln, Stichproben und Auswertungen mitgebaut; jeder dieser Fehler wurde von einem getrennten Evaluator, im Test oder vom Nutzer gefunden, nicht von der Hand, die ihn gemacht hat. "
              "Vier von 32 Einträgen in docs/ki_irrwege.md (drei auf der Folie, der vierte steht als Fußnote auf Folie 5; der Paket-B-Fall steht im Lab-Log, Abschnitt 8): (1) Entwicklung 10–11 von 12 plausibel, im Test 11 von 24 richtig (Iteration 3): Regel verworfen. "
              "(2) „Blind“ war nicht blind: Die KI-Leser (eine zweite KI, die die Bekanntmachung unabhängig lesen sollte) hatten in Iteration 8 die Projektbeschreibung im Kontext (CLAUDE.md), gefunden vom Evaluator, offen genannt. "
              "(3) Konkurrenz übersehen: Die Suche vom 24.10. fand keinen deutschen Dienst, tatsächlich gibt es zwei; gefunden vom Recherche-Agenten nach dem Hinweis des Dozenten. Auf der Folie steht das als UNSER gemeinsamer Prozessfehler (wir und KI), nicht als reiner KI-Fehler: Die Sichtung G1.1 blieb bei uns offen (Lab-Log §1, Lernpunkt). "
              "(4) Schwelle unerreichbar: Claude übernahm die Abweichungsrate von 17 % aus Iteration 10 für 160 Lose, es waren 9,4 %; gefunden vor den Leserantworten, nicht nachträglich geändert. "
              "LERNPUNKT STATT SCHWÄCHE: „Konkurrenz erst in Iteration 10 gesehen“ ist ein Prozessfehler, kein Pech. Plan G1.1 (Wettbewerber sichten) blieb offen; die Entscheidung gegen Kundenkontakt fiel am 2026-10-29. "
              "Kosten: Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos gibt. Lehre: ein Marktgate in Phase 1, vor der Modellierung. "
              "LERNPUNKT „Null = Verdachtsmoment“ (ein Satz, wenn Zeit): Paket B fand zunächst 0 von 84 Verfahren nicht auf TED; die Robustheitsprüfung zeigte ein Filterartefakt; danach 26,7 %. "
              "TEIL 2, TRENNUNG VON ENTWICKLUNG UND TEST (Zeitstrahl rechts): Hypothese, Kriterien und Seed stehen im Git, bevor die Stichprobe gezogen und die Antworten gelesen werden; die Reihenfolge im Versionsverlauf ist der Nachweis. "
              "Iteration 10b: 4f50436 (Hypothese, Kriterien, Skript und Seed 20261112 vorab), 9d63c59 (Stichprobe gezogen, SHA-256 des Schlüssels 2cd00206…3e33), 49bb198 (Abruf- und Auswertungsskript), "
              "6b7e8d8 (Paket und Leseskript vor den Antworten), 69917ff (Antworten der Leser unverändert), f6583cc (Auswertung). Iteration 9 genauso: Regeln a03a4a8, Seed und Skript 4521952, Stichprobe b3b1471, Antworten erst e1726e7. "
              "LIVE IN DER FRAGENRUNDE (Sicherung als Bild: Anhang Folien 16 und 17): `git log --oneline` zeigen; eine Regel in src/prepare/vertragsliste.py öffnen; Fehlwerte (Stufe F) in reports/beispiel_liste_oberpfalz.csv. "
              "EHRLICHE LÜCKEN: das Lauf-Skript der Iteration-9-Leser wurde erst mit den Antworten committet; in Iteration 8 kannten die Leser den Fehlertyp; in 10b liegt das Protokoll der Leserläufe außerhalb des Repos. "
              "FRAGE – ANTWORT: „Warum erst jetzt die Konkurrenz?“ Weil die Sichtung (G1.1) offen blieb und die Suche am 24.10. zu eng war. Prozessfehler im Business Understanding; er hat Zeit gekostet, aber das Ergebnis geändert. "
              "ZEIG-MIR-WO: docs/ki_irrwege.md (32 Einträge), docs/projektplan.md (G1.1), reports/evaluation_iteration10b.md, git log, src/prepare/stichprobe_iteration10b.py, docs/reproduzierbarkeit.md.",
              teil="Prüfung")

items = (("Im Test viel schlechter", "Beim Entwickeln hielt die KI 10–11 von 12 für plausibel, im Test waren nur 11 von 24 richtig."),
         ("„Blind“ war nicht blind", "Die prüfende KI kannte unsere Projektbeschreibung."),
         ("Konkurrenz zu spät gesehen", "Unser Prozessfehler, nicht nur der KI. Lehre: früh fragen, ob es das schon gibt."))
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
fuss(s, "Drei Beispiele aus unserer Liste von 32 KI-Irrwegen; Lücke: ein Leseprotokoll liegt außerhalb des Projektordners.")
uebergang(s, "Was heißt das für den Betrieb? Manuel.")

# Folie 10: Empfehlung ------------------------------------------------------------
s = new_slide("ZEIT 1:15. KERNAUSSAGE: Ampel statt Fazit-Text. GRÜN: Die Liste ist als Ausgangspunkt nutzbar, immer mit Blick in die verlinkte Bekanntmachung: 66 von 70 Zufallslosen der Iteration 9 (94,3 %) haben das gleiche Enddatum wie der Vergleichswert zweier KI-Leser "
              "(Leser nicht unabhängig, Vergleichswert teils zirkulär; Mensch 14 von 15). "
              "GELB: spätestes Vertragsende (Höchstende) nur Hinweis (87,1 %); nur TED-Daten: 79,4 % ist der Anteil der Lose mit Enddatum unter den Zuschlägen 10/2025 bis 9/2026 (2.783 von 3.503), rund 73 % aller Lose (6.803 von 9.325); das ist keine Marktabdeckung. "
              "Dazu der Ausblick aus Paket B (rund ein Viertel der Oberpfälzer Reinigungsverfahren im Bekanntmachungsservice nicht auf TED). Gespräche n = 3; Nachfrage ungeprüft, ein Test mit Betrieben ist vorbereitet, nicht durchgeführt (Folie 11). "
              "ROT: Terminprognose (28,8 %); die Liste als eigenes Produkt; Qualitätsvorsprung nicht belegt. "
              "ZEILE „UNSER RAT“ (gleicher Wortlaut wie im Lab-Log und in der Entscheidungsvorlage, Deutung unter Annahmen): „Kostenlosen Alarm nutzen · Abo nur, wenn eine Funktion fehlt – vorher testen · nicht selbst bauen, solange niemand Treffer von Hand ins eigene System überträgt.“ Erläuterung: kostenlos = TED-Suchprofile mit E-Mail-Alarm, Vergabeweiser-Alerts, diese Liste als CSV; Abo nur für eine Funktion, die fehlt (im Gespräch genannt: Wettbewerbsdaten; Zahlungsbereitschaft in einem von drei Gesprächen), vorher in der kostenlosen Stufe oder im Probezeitraum testen; selbst bauen lohnt im Basismodell gegen kostenlose Dienste nie (Modellkonstruktion) und wäre nur dann zu prüfen, wenn jemand heute Treffer von Hand ins eigene System überträgt (Test K-J, Folie 11). "
              "TRANSFERFRAGE „Würdet ihr das Produkt bauen?“: Nein, nicht als Liste allein. Wenn weiter, dann zuerst der vorbereitete Test mit Betrieben (Schwelle vorab), eine menschliche Gegenlesung und ein Maß, das Definition und Losebene trennt. "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1 (Laufzeitende bei 80,9 % der Zuschläge bestimmbar, 90,0 %, wenn eine Dauer ohne Beginn mitzählt); eine Geschäftsbegründung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/lab_log.md Abschnitt 7, docs/annahmen.md, reports/evaluation_iteration9.md, reports/evaluation_iteration10b.md, docs/business.md §8.9, docs/business_case_auswahl.md.",
              teil="Fazit")

ampel = (("Ja", GREEN, ["Vertragsenden als Ausgangspunkt", "Immer die Bekanntmachung selbst lesen", "66 von 70: gleiches Enddatum wie zwei KI-Leser"]),
         ("Mit Vorsicht", AMBER, ["Lose mit Enddatum: 79,4 % im letzten Jahr", "Spätestes Ende nur als Hinweis", "Nachfrage ungeprüft, Test vorbereitet"]),
         ("Nein", RED, ["Terminprognose (28,8 %)", "Liste als eigenes Produkt", "Vorsprung nicht belegt"]))
for i, (h, f, pts) in enumerate(ampel):
    x = 0.6 + i * 3.0
    rect(s, x, 1.38, 2.8, 2.12, WHITE, name=h + " Karte")
    kreis(s, x + 0.2, 1.46, 0.36, f, name=h + " Signal")
    box(s, x + 0.7, 1.46, 1.95, 0.36, h, size=16, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 1.9, 2.45, 1.58, pts, size=14, space=4)
rect(s, 0.6, 3.58, 8.8, 0.64, WHITE, name="Rat Karte")
box(s, 0.8, 3.58, 8.45, 0.64, [[("Unser Rat: ", {"bold": True}),
                               ("Kostenlosen Alarm nutzen · Abo nur, wenn eine Funktion fehlt – vorher testen · nicht selbst bauen, solange niemand Treffer von Hand ins eigene System überträgt.", {})]],
    size=14, anchor=MSO_ANCHOR.MIDDLE, name="Rat Text")
kurz(s, "Die Liste hilft beim Planen, ersetzt aber nicht den Blick in die Bekanntmachung.")
fuss(s, "79,4 % = Anteil der Lose mit Enddatum unter den Zuschlägen 10/2025 bis 9/2026, nur TED-Daten.")

# Folie 11: Fazit ------------------------------------------------------------
s = new_slide("ZEIT 0:45. KERNAUSSAGE in einem Satz wiederholen, dann Brücke zur Fragenrunde. Gesamtzeit: 15:00 (Ziel ±30 Sekunden); Zeitbudget je Folie: "
              "0:30 / 4:15 / 1:30 / 1:15 / 1:15 / 1:00 / 1:00 / 1:00 / 1:15 / 1:15 / 0:45 = 15:00 (11 sichtbare Folien; Video-Folie 2: 4:15 = Einleitung und Quizfrage vor dem Start 0:30 + Video 3:32 ohne Pause + Überleitung 0:13; "
              "Business Understanding Folien 3 bis 7: 6:00 = 40 %; der Iterationsweg steckt im Video, die Folie Vier Versuche ist ausgeblendet, Folie 12). "
              "Sprecher: Ludwig 1, 2, 5, 6, 7, 9 · Manuel 3, 4, 8, 10, 11 (je etwa 5:45 gesprochen; Ludwig 9:15 Folienzeit, davon 3:32 Video); Probeziel 14:30; Zwischenzeiten 4:45 (nach Folie 2) / 7:30 (nach Folie 4) / 10:45 (nach Folie 7) / 13:00 (nach Folie 9). "
              "STREICHLISTE bei Zeitnot (in dieser Reihenfolge): Frage auf Folie 3 nur als Satz, sofort auf Folie 4 auflösen; Folie 6 nur Balken und Rat; Demo-Aufnahme auf Folie 7 nur 30 Sekunden. "
              "Folien 12 bis 17 sind ausgeblendet (Anhang, nicht in der Zeit). "
              "SCHLUSS (wörtlich, dann „Vielen Dank“): „Für den Betrieb mit den 28 Tagen heißt das: heute einen kostenlosen Alarm einrichten, statt 3.500 bis 27.000 € in einen Eigenbau zu stecken (Modell mit Annahmen). "
              "Und für uns: vor dem Bauen fragen, ob es das schon gibt und wer dafür zahlt.“ (3.500 bis 27.000 € = Kosten in drei Jahren, Szenarien Niedrig bis Hoch, Folie 6, reports/make_or_buy.md.) "
              "QR-CODE unten rechts: führt zum Repo " + REPO_URL + " (docs/vortrag/qr_repo.png, erzeugt mit segno). "
              "Satz zum Mitnehmen: Den Termin einer Neuausschreibung sagen TED-Daten nicht vorher; eine Liste der Vertragsenden lässt sich lesen, ist aber kein eigenes Produkt, solange Vergabeweiser sie kostenlos bietet. Lehre: Marktgate in Phase 1, vor der Modellierung. "
              "NÄCHSTER SCHRITT (docs/business_case_auswahl.md, Nachtrag K-J, Schwelle vorab festgelegt am 2026-11-09, vor jedem Anruf): eine Stunde TED-Suchprofil mit E-Mail-Alarm anlegen und nach Teams weiterleiten, dann drei Anrufe bei Betrieben. "
              "Schwelle: „Mindestens 2 von 3 Betrieben nutzen Teams oder Planner aktiv, nennen mindestens 1 Stunde pro Woche für Sichten und Übertragen und übertragen heute von Hand; sonst wird K-J verworfen.“ Test nicht durchgeführt; die Schwelle ist eine Setzung. "
              "Auf der Folie steht sie gekürzt in einer Zeile („weiter nur, wenn 2 von 3 heute Treffer von Hand übertragen“), die beiden übrigen Bedingungen (Teams oder Planner aktiv, mindestens 1 Stunde pro Woche) stehen in der Fußnote. "
              "FRAGENRUNDE vorbereiten: (1) Methodenfrage: warum ±3 Monate, warum diese Vergleichsregel, warum KI-Leser als Maß, warum nur abweichende Lose (Folie 5, Folie 8 Sensitivität, ausgeblendete Folien 12 bis 15). "
              "Ausgeblendete Folien in der Fragerunde über die Foliensortierung öffnen. (2) Live-Nachweis: `python src/model/sensitivitaet_backtest.py --vorlauf 9 --fenster 2` (Folie 8); git log und Reihenfolge der Commits (Folie 9); Live-Demo im Browser (Folie 7). "
              "Streikt die Technik: ausgeblendete Folien 16 und 17 (Terminal-Ausgaben vom 2026-11-09 als Bild). "
              "(3) Transferfragen: „Warum nicht Vergabeweiser nutzen?“ (Folie 4), „Wer zahlt?“ (Folien 3 und 6), „Warum ist W8a verfehlt?“ (Folie 5), „Warum selbst bauen?“, „Welches Verwaltungssystem?“, „Wer pflegt das?“, „Warum nicht bund.de?“ (alle Folie 6), "
              "„Warum eine Demo nach dem Nein?“ (Folie 7), „Was war mit der Null in Paket B?“ und „Warum erst jetzt die Konkurrenz?“ (Folie 9), anderer Standort, andere Nische, doppeltes Volumen (Folien 6 und 10). "
              "Nicht sagen: „genauer als Vergabeweiser“, „Vorsprung belegt“, „kein Unterschied“, „die Liste stimmt zu 94 %“ (richtig: gleiches Enddatum wie zwei KI-Leser).", dark=True, teil="Fazit")

box(s, 0.6, 0.5, 8.8, 1.3, "Den Termin sagt TED nicht voraus. Das Vertragsende lässt sich lesen, ist aber kein eigenes Produkt.", size=26, color=INK, font=HEAD, name="Kernsatz")
for i, (z, t, f) in enumerate((("28,8 %", "Terminprognose, gefordert waren 60 %", RED), ("66 von 70", "gleiches Enddatum wie zwei KI-Leser", GREEN), ("0 €", "Vergabeweiser, kostenlos", BLUE))):
    x = 0.6 + i * 3.0
    rect(s, x, 1.8, 2.8, 1.25, WHITE, name=f"Kachel {i + 1}")
    box(s, x + 0.2, 1.88, 2.4, 0.55, z, size=26, color=f, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 2.45, 2.45, 0.55, t, size=14, color=INK)
box(s, 0.6, 3.22, 8.8, 0.32, [[("Lehre: ", {"bold": True, "color": DBLUE}), ("vor dem Bauen fragen, ob es das schon gibt und wer dafür zahlt.", {"color": INK})]], size=16, name="Lehre")
box(s, 0.6, 3.62, 8.8, 0.3, [[("Nächster Schritt: ", {"bold": True, "color": DBLUE}),
                             ("drei Betriebe anrufen; weiter nur, wenn 2 von 3 heute Treffer von Hand übertragen.", {"color": INK})]],
    size=14, name="Nächster Schritt")
box(s, 0.6, 4.12, 6.0, 0.45, "Vielen Dank. Fragen?", size=22, color=BLUE, font=HEAD, name="Dank")
box(s, 0.6, 4.6, 7.3, 0.3, [[("Code und Daten: ", {"color": GREY}), (REPO_URL.removeprefix("https://"), {"color": INK})]], size=14, name="Repo Adresse")
box(s, 0.6, 4.97, 7.4, 0.25, "Schwelle vorab festgelegt; dazu Teams oder Planner aktiv, ≥ 1 Stunde pro Woche. Test nicht durchgeführt.",
    size=11, color=GREY, name="Fußnote")


def qr_erzeugen(pfad, url=REPO_URL):
    """QR-Code zum Repo als PNG (dunkles Grau auf Weiß, Fehlerkorrektur M, Ruhezone 2 Module; der helle Foliengrund verlängert sie); gibt die Modulmatrix-Größe zurück."""
    import segno
    qr = segno.make(url, error="m", micro=False)
    pfad.parent.mkdir(parents=True, exist_ok=True)
    qr.save(str(pfad), kind="png", scale=20, border=2, dark="#2C2C2E", light="#FFFFFF")
    return qr.symbol_size(border=0)[0]


QR_MODULE = qr_erzeugen(QR_BILD)
QR_SEITE = 1.3                               # Zoll, mit Ruhezone; reine Codefläche etwa 1,15 Zoll
s.shapes.add_picture(str(QR_BILD), Inches(9.4 - QR_SEITE), Inches(3.95), Inches(QR_SEITE), Inches(QR_SEITE)).name = "QR-Code Repo"
s.notes_slide.notes_text_frame.text += " KURZ GESAGT (für Laien): Ob ein Vertrag neu ausgeschrieben wird, sagt TED nicht; wann er endet, steht in der Bekanntmachung, und die kostenlose Liste dazu gibt es schon."

# Folie 12 (Anhang): Vier Versuche, vier verfehlte Schwellen (bis zum Kurzfilm sichtbare Folie 3) ------------------------------------------------------------
s = new_slide("AUSGEBLENDET (Anhang für die Fragerunde; Zeit 0:00). Wieder ausgeblendet, weil das Video dieselben Zahlen zeigt (11 von 24, 28,8 % gegen 17,3 %, Ziel 60 %); die Folie bleibt für Fragen zum Iterationsweg "
              "und als Sicherung, falls das Video nicht läuft (Folie 2). KERNAUSSAGE: Der Iterationsweg auf einen Blick: Vier Versuche, jeder an einer vorab festgelegten Schwelle gescheitert, und jeder hat den nächsten Schritt geändert. Das haben wir so berichtet. "
              "ZEILE 1 (Iteration 2): Zuordnung neuer Auftrag → Vorgänger über Auftraggeber + CPV: K2 = 5 von 30 = 16,7 % (Wilson 7,3–33,6 %), Schwelle 80 %; große Auftraggeber vergeben viele Verträge parallel. Danach: Zuordnung über das Objekt (Adresse, Titel). "
              "ZEILE 2 (Iteration 3): Objekt-Regel: V3 Trefferquote 11 von 38 = 28,9 %, Schwelle 60 % (dazu V1 63,3 % und V2 45,8 %, Schwelle je 80 %). Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 richtig. KLARSTELLUNG: Die 11 von 24 im Video und auf Folie 2 sind die Präzision der Vorschläge (V2 = 45,8 %, Ziel 80 %); diese Folie zeigt für denselben Versuch die Trefferquote V3 = 11 der 38 vorhandenen Vorgänger gefunden = 28,9 % (Ziel 60 %). Kein Widerspruch, zwei Maße. Danach: ein letzter Versuch auf neuen Testdaten. "
              "ZEILE 3 (Iteration 4): erweiterte Regel auf neuen Testdaten (Q1 2026): W3 17 von 30 = 56,7 %, Schwelle 60 % (W4 Zweitprüfung des Nutzers 65 %, Schwelle 85 %). Danach: keine weitere Zuordnungsregel; das Vertragsende aus dem Zuschlag selbst lesen und daraus den Termin berechnen. "
              "ZEILE 4 (Iteration 5, Backtest): R1 = spätestes Vertragsende (Höchstende, mit allen Verlängerungen) minus 6 Monate auf 52 von Hand bestätigten Paaren: 15 von 52 = 28,8 % (Wilson 18,3–42,3 %), Schwelle 60 %; "
              "die einfache Faustregel R0 (Ende der Grundlaufzeit minus 6 Monate) schafft 9 von 52 = 17,3 %. 20 Neuausschreibungen kamen mehr als 3 Monate früher, 15 im Fenster, 17 später. Danach: keine Terminprognose, nur eine Liste der Vertragsenden. "
              "Grenzen: Paare aus einer Rückwärtssuche (nur auffindbare Vorgänger), Zweitprüfung KI-unterstützt. "
              "NACHTRAG SENSITIVITÄT (nachträglich, kein neuer Test; Diagramm Trefferquote je Vorlauf im Anhang Folie 14): bester Vorlauf im Nachhinein 6 Monate (28,8 %), ±12 Monate nur 50 %, McNemar R1 gegen R0 p ≈ 0,18 (Folie 8). "
              "FRAGE – ANTWORT: „Warum ±3 Monate, warum diese Vergleichsregel?“ Das Fenster wurde vor der Rechnung gesetzt, weil ein Betrieb für Personal und Angebot grob ein Vierteljahr Spielraum braucht; die einfache Regel R0 zeigt, was Zufall und Streuung allein schaffen; die Schwelle 60 % war eine Setzung ohne Kundenkontakt. "
              "ZEIG-MIR-WO: docs/iterationen.md (Übersichtstabelle, K2, V3, W3, X3), docs/lab_log.md Abschnitt 0, reports/zuordnung_iteration3.md, reports/evaluation_iteration4.md, reports/backtest_iteration5.md, reports/evaluation_iteration5.md, reports/sensitivitaet_iteration5.md.")

versuche =(("Iteration 2 · Zuordnung", "Vorgänger über Auftraggeber finden", "16,7 %", "Ziel 80 %", "Danach: über das Objekt suchen (Adresse, Titel)"),
            ("Iteration 3 · Zuordnung", "Vorgänger über das Objekt finden", "28,9 %", "Ziel 60 %", "Danach: letzter Versuch auf neuen Testdaten"),
            ("Iteration 4 · Zuordnung", "Objekt-Regel auf neuen Testdaten", "56,7 %", "Ziel 60 %", "Danach: Termin aus dem Vertragsende berechnen"),
            ("Iteration 5 · Terminprognose", "Spätestes Vertragsende − 6 Monate", "28,8 %", "Ziel 60 %", "Danach: keine Prognose, nur Liste der Vertragsenden"))
for i, (it, was, quote, ziel, danach) in enumerate(versuche):
    y = 1.38 + i * 0.71
    rect(s, 0.6, y, 8.8, 0.64, WHITE, radius=0.12, name=f"Versuch {i + 1} Karte")
    kreis(s, 0.75, y + 0.14, 0.36, RED, str(i + 1), size=13, name=f"Versuch {i + 1} Nummer")
    box(s, 1.25, y + 0.04, 3.75, 0.56, [[(was, {"bold": True})], [(it, {"color": GREY})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Versuch {i + 1} Text")
    box(s, 5.05, y + 0.04, 1.2, 0.56, [[(quote, {"bold": True, "color": RED, "size": 18, "font": HEAD})], [(ziel, {"color": GREY})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Versuch {i + 1} Quote")
    pfeil(s, 6.25, y + 0.21, 0.18, 0.22, name=f"Versuch {i + 1} Pfeil")
    box(s, 6.55, y + 0.04, 2.75, 0.56, danach, size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Versuch {i + 1} Danach")
kurz(s, "Keiner der vier Versuche erreichte seine Schwelle; die Terminregel traf 28,8 % (einfache Faustregel: 17,3 %), also eine Liste statt einer Prognose.")
fuss(s, "Schwellen vor jedem Ergebnis festgelegt. Zuordnung: neuer Auftrag → Vorgängervertrag; Termin: 52 geprüfte Paare.")

# Folie 13 (Anhang): Frage, Kriterium, Daten ------------------------------------------------------------
s = new_slide("AUSGEBLENDET (Anhang für die Fragerunde; im Vortrag ersetzt durch das Video auf Folie 2; Zeit 0:00). Zeigen bei Fragen zu Kriterium, Schwelle, Datenumfang. KERNAUSSAGE: Die Frage hatte eine Entscheidung (auf welche Ausschreibung bereite ich mich vor?) und eine vorab festgelegte Schwelle. "
              "Zielgruppe: Reinigungsfirmen im Mittelstand, Nische Gebäudereinigung (Haupt-CPV 90910/90911/90919). Annahme: Wer früh weiß, wann ein Vertrag endet, kann Personal und Angebot vorbereiten (A1, A15); diese Annahme war zu diesem Zeitpunkt ungeprüft, ein Kundengespräch gab es nicht. "
              "Erfolgskriterium vor dem Backtest festgelegt (docs/business.md 7.1): Treffer = Neuausschreibung im Fenster ±3 Monate um die Prognose, Schwelle 60 %; Vergleichsregel R0 = Ende der Grundlaufzeit minus 6 Monate, 17,3 %. "
              "Daten: TED Search API, eForms-Zuschläge ab Okt. 2023, Rohdaten unverändert in data/raw (nicht im Git, Abruf-Skript in docs/reproduzierbarkeit.md). 9.325 Lose aus 4.011 Zuschlägen. Herleitung (Nachrechnung 2026-11-09 mit src/population_iteration4.py und src/prepare/vertragsliste.py): 4.307 eForms-Zuschläge Haupt-CPV 90910/90911/90919, nur Originale, 25.10.2023 bis 30.09.2026 (reports/verlaengerung_praxis_iteration5.md); minus 98 nach den Ausschlussregeln der Population (Baureinigung, Endreinigung, Schimmel, Fahrzeug, Industriereinigung, Schädlinge; Bauprojekte ohne wiederkehrende Reinigung) = 4.209; minus 198 Zuschläge, deren Lose alle ohne Zuschlag sind (Regel 7) = 4.011 mit 9.325 Losen (vor Regel 7: 9.915 Lose). "
              "Die Angabe „Zuschläge 10/2025 bis 9/2026“ gehört nur zu den 79,4 % (Anteil der Lose mit Enddatum im letzten Jahr), nicht zu den 9.325 Losen. "
              "Iteration 1 (Zuschläge veröffentlicht 22.07. bis 21.10.2026, reports/datenqualitaet_DEU_20260722_20261021.md): Laufzeitende bei Gebäudereinigung in 80,9 % der Zuschläge bestimmbar (90,0 %, wenn eine Dauer ohne Beginn mitzählt; n = 440); "
              "Verlängerungsfeld BT-58 befüllt bei 18,9 % aller deutschen Zuschläge (15.706); bei Gebäudereinigung > 0 in 42,0 %; die Länge der Verlängerung steht nur im Freitext (A5 widerlegt; Lab-Log Tabelle Datenqualität). "
              "Vier Zyklen CRISP-DM, jeder endete mit einer Entscheidung gegen vorab festgelegte Schwellen. Zyklus 4 ist der Rücksprung in Phase 1; er bekommt in diesem Vortrag den größten Teil der Zeit (Folien 3 bis 7, 6:00 von 15:00; der Iterationsweg steht im Video und auf der ausgeblendeten Folie 12). "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1: Laufzeitende bei 80,9 % der Zuschläge bestimmbar (90,0 %, wenn eine Dauer ohne Beginn mitzählt), Haupt-CPV klar abgrenzbar. Eine Geschäftsbegründung ist das nicht; sie wurde nicht belegt. "
              "ZEIG-MIR-WO: docs/business.md Abschnitt 7.1, reports/datenqualitaet_DEU_20260722_20261021.md, docs/quellen.md.")

box(s, 0.6, 1.4, 8.8, 0.95, "Reinigungsfirmen erfahren oft spät, wann ein öffentlicher Vertrag endet. Unsere Idee: Das aus Daten von TED vorhersagen, der EU-Plattform für öffentliche Ausschreibungen.", size=16, name="Idee")
tile(s, 0.6, 2.5, 2.8, 1.7, "60 %", "Mindest-Trefferquote, vorab festgelegt (Termin auf ±3 Monate genau)", BLUE, "Schwelle")
tile(s, 3.6, 2.5, 2.8, 1.7, "17,3 %", "so viel schafft eine einfache Faustregel zum Vergleich", GREY, "Faustregel")
tile(s, 6.6, 2.5, 2.8, 1.7, "9.325", "Lose (Teilaufträge) aus 4.011 Zuschlägen seit Okt. 2023", BLUE, "Daten")
kurz(s, "Wer früh Bescheid weiß, kann Personal und Angebot besser planen (Annahme, ungeprüft).")
fuss(s, "Quelle: TED API v3. 4.011 von 4.307 eForms-Zuschlägen: ohne Baureinigung u. Ä. und ohne Lose ohne Zuschlag.")

# Folie 14 (Anhang): Trefferquote je Vorlauf ------------------------------------------------------------
VORLAUF_BILD = ROOT / "docs" / "lab_log_bilder" / "diagramm_vorlauf.png"   # erzeugt von src/report/diagramme.py
s = new_slide("AUSGEBLENDET (Anhang für die Fragerunde; Zeit 0:00). Zeigen bei der Frage „Hättet ihr mit einem anderen Vorlauf 60 % geschafft?“. "
              "KERNAUSSAGE: Nein. Nachträglich (kein neuer Test) wurde der Vorlauf von 0 bis 24 Monaten auf denselben 52 Paaren variiert, Fenster ±3 Monate: Der beste Vorlauf ist genau der vorab gewählte (6 Monate, 15 von 52 = 28,8 %). "
              "Blaue Linie R1 = spätestes Vertragsende (Höchstende) minus Vorlauf; graue Linie R0 = Ende der Grundlaufzeit minus Vorlauf (einfache Faustregel, bei 6 Monaten 9 von 52 = 17,3 %); rote Linie = Schwelle 60 % (32 Treffer). "
              "Erst ein Fenster von ±12 Monaten bringt 26 von 52 = 50,0 %; ein Jahr Unsicherheit nützt keinem Betrieb. McNemar R1 gegen R0: p ≈ 0,18, der Vorsprung vor der Faustregel ist nicht gesichert. "
              "Das ist eine optimistische Obergrenze, weil der Vorlauf im Nachhinein gewählt wird. "
              "LIVE: `python src/model/sensitivitaet_backtest.py --vorlauf 9 --fenster 2`; Bild der Ausgabe auf Folie 16. "
              "ZEIG-MIR-WO: reports/sensitivitaet_iteration5.md (Tabellen Vorlauf und Fenster), src/model/sensitivitaet_backtest.py, docs/lab_log_bilder/diagramm_vorlauf.png (Skript src/report/lab_log_bilder.py), docs/lab_log.md Abschnitt 3.")
rect(s, 0.6, 1.38, 6.3, 2.84, WHITE, name="Vorlauf Karte")
if VORLAUF_BILD.exists():
    bh = 2.74                                   # Bild 1600 x 720 Pixel, Seitenverhältnis bleibt
    bw = bh * 1600 / 720
    s.shapes.add_picture(str(VORLAUF_BILD), Inches(0.6 + (6.3 - bw) / 2), Inches(1.43), Inches(bw), Inches(bh)).name = "Diagramm Trefferquote je Vorlauf"
else:
    box(s, 0.8, 1.38, 5.9, 2.84, "Diagramm fehlt (src/report/lab_log_bilder.py ausführen).", size=14, color=GREY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
for i, (z, t, f) in enumerate((("28,8 %", "bester: 6 Monate", RED), ("50,0 %", "erst bei ±12 Monaten", RED), ("17,3 %", "einfache Faustregel", GREY))):
    y = 1.38 + i * 0.97
    rect(s, 7.05, y, 2.35, 0.9, WHITE, name=f"Vorlauf Zahl {i + 1} Karte")
    box(s, 7.25, y + 0.06, 2.0, 0.4, z, size=22, color=f, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name=f"Vorlauf Zahl {i + 1}")
    box(s, 7.25, y + 0.5, 2.0, 0.32, t, size=14, name=f"Vorlauf Zahl {i + 1} Text")
kurz(s, "Auch der im Nachhinein beste Vorlauf trifft nur 28,8 %; gefordert waren 60 %.")
fuss(s, "Nachträglich, kein neuer Test: Vorlauf 0 bis 24 Monate auf denselben 52 Paaren, Fenster ±3 Monate.")

# Folie 15 (Anhang): Liste und Genauigkeit ------------------------------------------------------------
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
rect(s, 8.65, 2.03, 0.2, 0.16, GREY, MSO_SHAPE.ISOSCELES_TRIANGLE, "Marke spätestes Vertragsende")
box(s, 0.9, 2.22, 4.4, 0.4, "Ende der Grundlaufzeit: steht in unserer Liste", size=14, bold=True, color=BLUE, align=PP_ALIGN.RIGHT)
box(s, 5.1, 2.22, 3.8, 0.4, "spätestes Vertragsende: nur Hinweis", size=14, color=GREY, align=PP_ALIGN.RIGHT)
tile(s, 0.6, 2.8, 2.8, 1.4, "66 von 70", "gleiches Enddatum wie zwei KI-Leser", GREEN, "Genauigkeit", zsize=26)
tile(s, 3.6, 2.8, 2.8, 1.4, "9.325", "Lose in der Liste", BLUE, "Lose", zsize=26)
tile(s, 6.6, 2.8, 2.8, 1.4, "79,4 %", "der Lose im letzten Jahr haben ein Enddatum", BLUE, "Enddatum", zsize=26)
kurz(s, "Die Liste nennt je Vertrag das Ende der festen Laufzeit, mit Link zur Bekanntmachung.")
fuss(s, "KI-Leser nicht unabhängig; ein Mensch prüfte 15 Lose, 14 stimmen. 79,4 %: Zuschläge 10/2025 bis 9/2026, nur TED.")


# Folien 16 und 17 (Anhang): Sicherung „Falls die Technik streikt“ ------------------------------------------------------------
# Terminal-Ausgaben am 2026-11-09 erzeugt (Befehle aus docs/fragenrunde.md Teil A, im Repo-Wurzelordner) und hier unverändert abgeschrieben;
# nur lange Einzeiler und Commit-Texte sind gekürzt (mit „…“ markiert).


def terminal(s, x, y, w, h, kopf, zeilen, name):
    """Helle Karte mit Terminal-Text in Consolas 12 pt (wie der Code auf Folie 8); zeilen: (art, text), art = cmd / out / note."""
    rect(s, x, y, w, h, WHITE, name=name + " Karte")
    box(s, x + 0.2, y + 0.05, w - 0.4, 0.27, kopf, size=14, bold=True, color=GREY, name=name + " Kopf")
    tb = s.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.34), Inches(w - 0.4), Inches(h - 0.38))
    tb.name = name + " Ausgabe"
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, (art, text) in enumerate(zeilen):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.line_spacing = Pt(13)
        runs = [("> ", BLUE), (text, INK)] if art == "cmd" else [(text, DGREEN if art == "note" else INK)]
        for txt, farbe in runs:
            r = para.add_run()
            r.text = txt
            r.font.name, r.font.size, r.font.color.rgb = MONO, Pt(12), farbe


def kuerzen(text, n=76):
    return text if len(text) <= n else text[:text.rfind(" ", 0, n)] + " …"


s = new_slide("AUSGEBLENDET (Anhang, Sicherung für die Fragerunde; Zeit 0:00). Nur zeigen, wenn das Terminal nicht läuft. "
              "INHALT: echte Ausgaben vom 2026-11-09, erzeugt im Repo-Wurzelordner mit .venv\\Scripts\\python.exe -I, unverändert abgeschrieben (Dezimalpunkt wie im Skript). "
              "(a) Parameter ändern: src/model/sensitivitaet_backtest.py liest die 52 Paare aus reports/backtest_iteration5.md; mit Argumenten schreibt es nichts. Kontrolle 6/3 = vorab festgelegte Regel (R0 17,3 %, R1 28,8 %); "
              "Variante 9/2: Die Prognose rückt 3 Monate früher, das Fenster wird schmaler, fast alle Treffer fallen weg (R1 2 von 52). Nachträglich, kein neuer Test. "
              "(c) Fehlwerte: reports/beispiel_liste_oberpfalz.csv, 130 Lose; 38 leere gl_ende = 33 Stufe F (kein Ende in der Bekanntmachung, Laufzeitfelder fehlen im XML) + 5 Stufe E (Ende nur geschätzt, eigene Spalte gl_geschaetzt). "
              "Wir füllen die Lücke nicht mit einer Schätzung auf, sondern zeigen sie als Stufe F. Der vollständige Einzeiler steht in docs/fragenrunde.md Teil A (c). "
              "ZEICHENSATZ: Im echten Terminal vorher `chcp 65001`, sonst erscheinen ± und – als Ersatzzeichen. "
              "ZEIG-MIR-WO: docs/fragenrunde.md Teil A, reports/sensitivitaet_iteration5.md, reports/stufe_f_ursachen.md, reports/beispiel_liste.md.")
PY = r".venv\Scripts\python.exe -I"
terminal(s, 0.6, 1.1, 8.8, 1.84, "Parameter ändern (nachträglich, kein neuer Test)", [
    ("cmd", PY + r" src\model\sensitivitaet_backtest.py --vorlauf 6 --fenster 3"),
    ("out", "R0: Vorlauf 6 Monate, Fenster ±3: 9 von 52 = 17.3 % (Wilson 9.4–29.7 %)"),
    ("out", "R1: Vorlauf 6 Monate, Fenster ±3: 15 von 52 = 28.8 % (Wilson 18.3–42.3 %)"),
    ("out", "Vorab festgelegt: Vorlauf 6, Fenster ±3, Schwelle 60 %."),
    ("cmd", PY + r" src\model\sensitivitaet_backtest.py --vorlauf 9 --fenster 2"),
    ("out", "R0: Vorlauf 9 Monate, Fenster ±2: 1 von 52 = 1.9 % (Wilson 0.3–10.1 %)"),
    ("out", "R1: Vorlauf 9 Monate, Fenster ±2: 2 von 52 = 3.8 % (Wilson 1.1–13.0 %)"),
    ("out", "Vorab festgelegt: Vorlauf 6, Fenster ±3, Schwelle 60 %.")], "Sensitivität")
terminal(s, 0.6, 3.06, 8.8, 0.94, "Fehlwerte zeigen (130 Lose der Oberpfalz, Spalte stufe)", [
    ("cmd", PY + ' -c "import csv,collections as c; …"   # Einzeiler gekürzt'),
    ("out", "130 Lose; Stufen: [('A', 54), ('B', 2), ('C', 27), ('D', 9), ('E', 5), ('F', 33)]"),
    ("out", "gl_ende leer: 38 nach Stufe: [('E', 5), ('F', 33)]")], "Fehlwerte")
kurz(s, "Echte Ausgaben vom 9. November; live laufen die Befehle ohne Rohdaten.")
fuss(s, "Unverändert abgeschrieben, Dezimalpunkt wie im Skript; lange Einzeiler gekürzt (vollständig im Spickzettel).")

GIT_LOG = (
    ("4f50436", "Iteration 10b und Pakete A, C, F: Hypothese und Kriterien vorab, Skript und Seed vor dem Ziehen; Nachtrag Listenfehler 527230-2026"),
    ("9d63c59", "Iteration 10b: Stichprobe gezogen (Seed 20261112, 160 Lose aus 154 Bekanntmachungen; Population 5.754 Lose), SHA-256 des Schlüssels 2cd00206…3e33 (data/processed/stichprobe_iteration10b_schluessel.csv, lokal)"),
    ("d6e2335", "Paket F: Optionsanalyse an den 52 Backtest-Paaren (Hinweis, kein Beleg zur Aussage der Vergabestelle)"),
    ("49bb198", "Iteration 10b: Skript für Abruf und Auswertung (vor dem Abruf); Festlegungen im Skriptkopf: Lose ohne Vergabeweiser-Eintrag nur in W10, Ursachenklassen c-a-b-d-e"),
    ("ea5ebfb", "Paket A: Wettbewerbsbild der 130 Oberpfalz-Lose aus TED (Auftragnehmer, Wert, Angebote), Handabgleich 5 von 5"),
    ("79fd0df", "Paket C: Ursachen der 33 Lose ohne Ende, Fehlertyp Dauerfeld = Gesamtdauer (12 Lose in 5 Bekanntmachungen); Berichtigung des Nachtrags 527230-2026"),
    ("64a23e3", "Iteration 10b: Abruf abgeschlossen (160 Lose, Vergabeweiser hat 160, diskordant 15: a 5, b 6, e 4); W8a rechnerisch nicht erreichbar bei 15 diskordanten Losen (Fehler der Vorab-Schwelle)"),
    ("6b7e8d8", "Iteration 10b: Paket und Skript für die blinde Lesung der 15 diskordanten Lose (vor den Antworten der Leser)"),
    ("69917ff", "Iteration 10b: Antworten der Leser A (Opus) und B (Sonnet) zu den 15 diskordanten Losen, unverändert"),
    ("f6583cc", "Iteration 10b: Auswertung nach den Lesern (Liste 15/15 bei den diskordanten Losen, W8a formal verfehlt, W8b erfüllt) und Bericht des Evaluators; KI-Irrwege"))
s = new_slide("AUSGEBLENDET (Anhang, Sicherung für die Fragerunde; Zeit 0:00). Nur zeigen, wenn das Terminal nicht läuft. "
              "INHALT (b) Trennung von Entwicklung und Test: (1) Überschneidung der Entwicklungsfälle (reports/entwicklung_iteration9_notices.txt) mit der Stichprobe der Iteration 9 (reports/stichprobe_iteration9_lose.csv): 0. "
              "Mit beiden Entwicklungslisten (Iteration 7 und 9) laut Spickzettel 27 Entwicklungsfälle, Überschneidung ebenfalls 0; die Stichprobe hat 110 Lose aus 104 Bekanntmachungen. "
              "(2) Reihenfolge der Commits der Iteration 10b, älteste zuerst (am 2026-11-09 ausgeführt, Commit-Texte für die Folie gekürzt): Kriterien und Seed (4f50436) vor der Stichprobe (9d63c59), "
              "Auswertungsskript vor dem Abruf (49bb198), Paket für die Leser vor den Antworten (6b7e8d8), Antworten unverändert (69917ff), dann Auswertung (f6583cc). "
              "Iteration 9 genauso: `git log --oneline --reverse a03a4a8^..e1726e7` (Regeln a03a4a8, Seed 4521952, Stichprobe b3b1471, Antworten e1726e7). "
              "GRENZEN (ehrlich sagen): Commit-Zeiten setzen wir selbst, belegt ist die Reihenfolge in der Git-Kette; 4f50436 und 9d63c59 liegen in derselben Minute; das Lauf-Skript der Leser in Iteration 9 kam erst mit den Antworten ins Git; "
              "das Leseprotokoll der Iteration 10b liegt außerhalb des Repos. "
              "ZEIG-MIR-WO: docs/fragenrunde.md Teil A (b), docs/reproduzierbarkeit.md, docs/ki_irrwege.md, src/prepare/stichprobe_iteration9.py.")
terminal(s, 0.6, 1.1, 8.8, 2.98, "Trennung von Entwicklung und Test (Iterationen 9 und 10b)", [
    ("cmd", PY + ' -c "import csv; …"   # Einzeiler gekürzt'),
    ("out", "7 Entwicklung, 104 Stichprobe, Ueberschneidung: 0"),
    ("cmd", "git log --oneline --reverse 4f50436^..f6583cc"),
    *[("out", h + " " + kuerzen(m)) for h, m in GIT_LOG]], "Git")
kurz(s, "Erst Regeln und Seed, dann Stichprobe, dann Antworten: Die Reihenfolge steht im Git.")
fuss(s, "Grenze: Commit-Zeiten setzen wir selbst; belegt ist die Reihenfolge der Git-Kette. Commit-Texte gekürzt.")

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if args:   # optional: anderer Ausgabepfad (z. B. wenn die Datei in PowerPoint geöffnet ist)
    OUT = Path(args[0])

# Folien 12 bis 17: ausgeblendeter Anhang für die Fragerunde (ob ausgeblendete Folien bei „höchstens 12“ zählen, mit dem Dozenten klären)
if "--ohne-anhang" in sys.argv:
    ids = prs.slides._sldIdLst
    for sld in list(ids)[-ANHANG:]:
        prs.part.drop_rel(sld.rId)
        ids.remove(sld)
else:
    for sl in list(prs.slides)[-ANHANG:]:
        sl._element.set("show", "0")
OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(len(prs.slides), "Folien (ausgeblendet:", 0 if "--ohne-anhang" in sys.argv else ANHANG, "); Video:", VIDEO_STATUS, "; Demo:", DEMO_STATUS, ";", OUT)
