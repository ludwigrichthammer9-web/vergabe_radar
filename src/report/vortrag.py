"""Foliengerüst für den Vortrag (LN B: 15 min, höchstens 12 Folien) mit Sprechernotizen.

Stand nach Iteration 10 und 10b. Gestaltung im Apple-/Keynote-Stil: eine Kernaussage als Satz je Folie, viel Weißraum, weiße Karten auf hellgrauem Grund,
Systemfarben, Schrift Segoe UI. Text mindestens 14 pt, Fußnoten 11 pt. Jede Folie beantwortet in einem Satz, was sie für einen Gebäudereiniger heißt.
Fachbegriffe (Wilson, Seed, Hash, CPV, NUTS, Diskordanz) stehen nur in den Notizen. Die Notizen enthalten je Folie ZEIT, KERNAUSSAGE, FRAGE – ANTWORT,
ZEIG-MIR-WO und neu FÜR LAIEN IN EINEM SATZ (Summe der Zeiten der sichtbaren Folien 15:00).
Folie 2 ist das Video „Franz und die Glaskugel“ (ersetzt Frage/Kriterium/Daten, Irrwege, Liste und Genauigkeit), Business Understanding auf Folien 3 bis 6, Demo auf Folie 7,
KI-Irrwege und Live-Nachweis auf Folie 8, Empfehlung 9, Fazit 10; Folien 11 bis 13 sind ausgeblendeter Anhang (Fragerunde).
Option --ohne-anhang lässt den Anhang weg. Das Video wird eingebettet, sobald docs/video/franz_und_die_glaskugel_szenen_0-5.mp4 existiert (Skript erneut ausführen).
Zahlen aus docs/iterationen.md, docs/business.md §8, reports/evaluation_iteration5.md bis 10b, reports/wettbewerbsbild_oberpfalz.md.
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
HEAD, BODY = "Segoe UI Semibold", "Segoe UI"   # Ersatz für San Francisco unter Windows

# Kernaussage je Folie (Titel als Satz)
TITEL = [None,
    "",
    "Video: Was TED vorhersagt und was nicht",
    "In unseren Gesprächen blieben für ein Angebot rund 28 Tage",
    "Eine solche Liste gibt es schon, kostenlos bei Vergabeweiser",
    "Unsere Liste weicht in rund 10 % der Lose von Vergabeweiser ab",
    "Selbst bauen lohnt sich nur, wenn man die Daten im eigenen System braucht",
    "Demo: Aus einer Bekanntmachung wird eine Nachricht",
    "Die KI machte Fehler; gefunden wurden sie durch getrennte Prüfung",
    "Nutzbar als Ausgangspunkt, aber nicht als eigenes Produkt",
    "",
    # ausgeblendeter Anhang (Folien 11 bis 13)
    "Wer früh weiß, wann ein Auftrag endet, kann sich besser vorbereiten",
    "Den Termin der Neuausschreibung kann TED nicht vorhersagen",
    "Das Vertragsende lässt sich auslesen: 66 von 70 Stichproben stimmen",
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


def new_slide(titel, notes, dark=False):
    s = prs.slides.add_slide(LAYOUT_BLANK if dark else LAYOUT_TITLE_ONLY)
    _nr[0] += 1
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = DARK if dark else PALE
    if not dark:
        t = s.shapes.title
        t.left, t.top, t.width, t.height = Inches(0.6), Inches(0.35), Inches(8.8), Inches(0.9)
        tf = t.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.TOP
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run()
        r.text = TITEL[_nr[0]]
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = HEAD, Pt(26), False, DARK
    box(s, 9.0, 5.25, 0.5, 0.25, str(_nr[0]), size=11, color=SOFT if dark else GREY, align=PP_ALIGN.RIGHT, name="Foliennummer")
    s.notes_slide.notes_text_frame.text = notes
    return s


def laien(s, text):
    """Satz „Für Gebäudereiniger“ unten auf der Folie; derselbe Satz kommt in die Notizen."""
    rect(s, 0.6, 4.3, 8.8, 0.55, LBLUE, radius=0.275, name="Laien Pille")
    box(s, 0.85, 4.3, 8.3, 0.55, [[("Für Gebäudereiniger: ", {"bold": True, "color": DBLUE}), (text, {"color": DBLUE})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Laien Satz")
    tf = s.notes_slide.notes_text_frame
    tf.text = tf.text + " FÜR LAIEN IN EINEM SATZ: " + text


def fuss(s, text, h=0.4):
    box(s, 0.6, 4.97, 8.2, h, text, size=11, color=GREY, name="Fußnote")


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



# Folie 1 ------------------------------------------------------------
s = new_slide("", "ZEIT 0:30. KERNAUSSAGE: Eine Reinigungsfirma will früh wissen, wann ein öffentlicher Vertrag endet und neu ausgeschrieben wird. Wir zeigen, was TED-Daten dazu hergeben "
              "(eine Liste der Vertragsenden), was nicht (eine Terminprognose), und was an der Idee gegenüber der kostenlosen Konkurrenz übrig bleibt. "
              "Ablauf in einem Satz: ein kurzes Video (Franz und die Glaskugel: Frage, zwei Irrwege, Liste samt Genauigkeit), dann der längere Teil: Wie arbeiten Betriebe, wer bietet es schon, was bleibt. "
              "Kernbotschaft schon jetzt nennen: Die Liste lässt sich aus TED lesen, ein eigenes Produkt ist sie nicht, und ein Qualitätsvorsprung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/iterationen.md (Übersicht und Ergebnis Iteration 10 und 10b).", dark=True)

# Radar-Grafik: Kreise um einen Mittelpunkt
rect(s, 6.1, 0.9, 3.4, 3.4, RGBColor.from_string("2C2C2E"), MSO_SHAPE.OVAL, "Radar außen")
rect(s, 6.6, 1.4, 2.4, 2.4, RGBColor.from_string("3A3A3C"), MSO_SHAPE.OVAL, "Radar mitte")
rect(s, 7.1, 1.9, 1.4, 1.4, BLUE, MSO_SHAPE.OVAL, "Radar innen")
rect(s, 8.15, 1.55, 0.3, 0.3, AMBER, MSO_SHAPE.OVAL, "Radar Punkt")
box(s, 0.6, 1.35, 5.2, 1.0, "Vergabe-Radar", size=48, color=WHITE, font=HEAD, name="Titel")
box(s, 0.6, 2.4, 5.1, 1.2, "Wann endet ein öffentlicher Auftrag, und wer weiß es schon?", size=24, color=SOFT, name="Untertitel")
box(s, 0.6, 3.75, 5.1, 0.6, "Was die EU-Plattform TED verrät und was nicht", size=16, color=BLUE, name="Zusatz")
box(s, 0.6, 4.65, 8.4, 0.3, "Manuel Strobel · Ludwig Richthammer", size=16, color=WHITE, font=HEAD, name="Namen")
box(s, 0.6, 5.0, 8.0, 0.3, "Big Data Analytics · Leistungsnachweis B", size=14, color=SOFT, name="Autoren")
s.notes_slide.notes_text_frame.text += " FÜR LAIEN IN EINEM SATZ: Wir haben geprüft, ob man aus öffentlichen Daten vorhersagen kann, wann ein Reinigungsauftrag neu ausgeschrieben wird."

# Folie 2: Video ---------------------------------------------------------
VIDEO = ROOT / "docs" / "video" / "franz_und_die_glaskugel_szenen_0-5_v3.mp4"   # v3: Synchronität geprüft, Schluss-Einordnung
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


s = new_slide("",
              "ZEIT 3:30 (Video etwa 3:00 inklusive Pause für die Quizfrage; dazu Einleitung und Überleitung etwa 0:30). KERNAUSSAGE: Das Video „Franz und die Glaskugel“ erzählt die ersten Zyklen des Projekts in drei Runden: "
              "Problem (Franz, Gebäudereiniger, erfährt zu spät, wann Verträge enden), Idee (TED-Daten), Runde 1: Vorgänger finden, 11 von 24 (Schwelle verfehlt), Runde 2: die Glaskugel „Vertragsende − 6 Monate“, 28,8 % statt der geforderten 60 %, Runde 3: die Vertragsliste, 66 von 70 Stichproben. Es ersetzt die Folien Frage/Kriterium/Daten, Irrwege, Liste und Genauigkeit (ausgeblendet am Ende, Folien 11 bis 13). "
              "ABLAUF: (1) Einleitung 15 Sekunden: „Drei Minuten Video, in der Mitte eine Frage an euch.“ Daten und Kriterium in einem Satz sagen (steht als Fußzeile auf der Folie): TED, Gebäudereinigung, Deutschland, Daten ab Okt. 2016, Treffer = Neuausschreibung im Fenster ±3 Monate, Schwelle 60 % vorab festgelegt, einfache Vergleichsregel 17,3 %. "
              "(2) Video starten (Folie anklicken, Wiedergabe; bei einer HTML-Fassung: Leertaste = Pause/weiter). (3) QUIZFRAGE LIVE in der Mitte, Video anhalten: „Wie oft lag die Regel ‚Vertragsende − 6 Monate‘ richtig? Ziel waren 60 %.“ Handzeichen oder Zuruf, 20 Sekunden; dann Video weiter: Auflösung 28,8 %. "
              "(4) Überleitung nach dem Video, 15 Sekunden: „Franz hat also eine Liste statt einer Glaskugel. Die gibt es allerdings vielleicht schon, dazu gleich.“ "
              "SICHERUNG, falls das Video nicht läuft: die drei Karten rechts auf der Folie nennen die Kernzahlen (11 von 24 · 28,8 % statt 60 % · 66 von 70); die Geschichte in 60 Sekunden frei erzählen, Quizfrage trotzdem stellen. Details in den ausgeblendeten Folien 11 bis 13. "
              "HINWEISE: Die Stimme im Video ist synthetisch. Das Video wurde KI-gestützt erstellt (Skript, Bilder, Stimme) und von uns korrigiert; das im Vortrag offen sagen. "
              "EHRLICHE EINSCHRÄNKUNGEN (bei Nachfrage oder in einem Satz am Ende): Die Figuren (Franz) sind erfunden, die Gespräche sind im Video nachgestellt (die drei echten Telefongespräche, n = 3, sind nur Hinweise, keine Belege). Die 66 von 70 beruhen auf KI-Lesern, die nicht unabhängig sind (gleiche Modellfamilie), dazu Kommilitone 14 von 15; der Vergleichswert 17,3 % ist teils zirkulär (naive Regel auf denselben 52 Paaren). Die Paare der Terminprognose stammen aus einer Rückwärtssuche. Ein Qualitätsvorsprung gegenüber der Konkurrenz ist nicht belegt (Folien 4 und 5). "
              "FRAGE – ANTWORT: „Warum ±3 Monate, warum 60 %?“ Das Fenster und die Schwelle wurden vor der Rechnung gesetzt, ohne Kundenkontakt, begründete Setzung (Anhang Folie 11). „Waren die 66 von 70 nicht vom Entwickler selbst bewertet?“ Nein, neue Stichprobe, Rohtext ohne Projektkontext, aber KI-Leser nicht unabhängig (Folie 8, Anhang Folie 13). "
              "ZEIG-MIR-WO: docs/video/franz_und_die_glaskugel_szenen_0-5.mp4, docs/iterationen.md, reports/evaluation_iteration3.md bis 9, Anhang Folien 11 bis 13.")
if VIDEO.exists():
    poster_erzeugen(POSTER)
    s.shapes.add_movie(str(VIDEO), Inches(0.6), Inches(1.4), Inches(4.97), Inches(2.8), poster_frame_image=str(POSTER), mime_type="video/mp4").name = "Video Franz und die Glaskugel"
    VIDEO_STATUS = "eingebettet"
else:
    rect(s, 0.6, 1.4, 4.97, 2.8, DARK, name="Video Platzhalter")
    box(s, 0.85, 1.6, 4.5, 2.4, [[("Video hier einbetten", {"bold": True, "color": AMBER, "size": 20, "font": HEAD})],
        [("docs/video/franz_und_die_glaskugel_szenen_0-5.mp4", {"color": WHITE, "size": 14})],
        [("Datei noch nicht vorhanden. Skript erneut ausführen, dann wird das Video automatisch eingebettet.", {"color": SOFT, "size": 14})]],
        space=10, anchor=MSO_ANCHOR.MIDDLE, name="Video Platzhalter Text")
    VIDEO_STATUS = "Platzhalter"
for i, (zahl, text, f) in enumerate((("11 von 24", "Vorgänger gefunden: Runde 1 verfehlt", RED),
                                      ("28,8 % statt 60 %", "Glaskugel „Vertragsende − 6 Monate“", RED),
                                      ("66 von 70", "Vertragsenden stimmen: die Liste", GREEN))):
    y = 1.4 + i * 0.955
    rect(s, 5.77, y, 3.63, 0.89, WHITE, name=f"Kernzahl {i + 1} Karte")
    box(s, 5.97, y + 0.06, 3.3, 0.45, zahl, size=22, color=f, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name=f"Kernzahl {i + 1} Zahl")
    box(s, 5.97, y + 0.52, 3.3, 0.33, text, size=14, name=f"Kernzahl {i + 1} Text")
laien(s, "Ein kurzer Film: Den Termin kennt niemand, das Vertragsende steht in der Bekanntmachung.")
fuss(s, "Daten: TED, Gebäudereinigung, Deutschland (API ab Okt. 2016, Liste: eForms ab Okt. 2023). Kriterium vorab: Treffer ±3 Monate, Schwelle 60 %; einfache Regel 17,3 %. Stimme synthetisch, Figuren erfunden, KI-gestützt erstellt.")


# Folie 5 ------------------------------------------------------------
s = new_slide("Wie gehen Betriebe heute vor?",
              "ZEIT 1:30. KERNAUSSAGE: Ab hier der Teil, den wir zu knapp behandelt hatten: das Business Understanding (Folien 3 bis 6, zusammen 6:30 = 43 % der Zeit). Zuerst der Prozess aus Sicht der Betriebe, dann die Konkurrenz. "
              "PUBLIKUMSFRAGE (gleich zu Beginn der Folie, bevor Folie 6 aufgelöst wird; 20 Sekunden, Handzeichen): „Gibt es kostenlos eine Liste auslaufender öffentlicher Verträge?“ Ja / nein / weiß nicht. Auflösung auf Folie 4: Ja, Vergabeweiser. FALLS die Quizfrage im Video (Folie 2) schon Publikum eingebunden hat: diese zweite Frage nur stellen, wenn die Zeit stimmt (Zwischenstand 4:00 nach Folie 2, 5:30 nach Folie 3); sonst als Satz überspringen und direkt auf Folie 4 auflösen. "
              "PROZESS (Fakten, drei Gespräche des Nutzers am 2026-11-05; 9 Anrufe, 3 erreicht, 105 Minuten; Notizen ohne Namen; n = 3, Hinweise, keine Belege): Betrieb mittlerer Größe: Meldung der Ausschreibung 28 Tage vor Abgabe; eng bei der Objektbegehung (ein Termin, der beste Vorarbeiter krank); Kalkulation nachts; Entscheidung mitzubieten „hauptsächlich Entfernung und Personal“; Vertragsenden bei anderen „eine Blackbox“. Kleinbetrieb: Entscheidung nach Kapazität des Teams; die Bürokratie (viele Eigenerklärungen) ist der Engpass; sucht auf Webseiten und in der Zeitung. Vergabestelle: plant etwa 9 Monate vor Vertragsende, verlängert „fast immer, wenn eine Option im Vertrag steht“, vergibt „sehr oft“ unterhalb der EU-Schwelle (also nicht auf TED). "
              "KOSTEN der Suche: Portal-Abo des mittleren Betriebs knapp 1.500 € im Jahr (Suchprofile); Dienste wie subreport 84–198 € im Monat (Produktübersicht, Recherche, nicht einzeln nachgeprüft). Der Kleinbetrieb zahlt für nichts in dem Bereich. "
              "FRAGE – ANTWORT: „Wer zahlt?“ Gespräche n = 3: Der größere Betrieb würde für den aktuellen Auftragnehmer und alte Preise zahlen, die Enddaten nannte er „nett für die Planung“; der Kleinbetrieb für nichts. Ein Betrag wurde nicht genannt. Aus TED ist das nur teilweise lieferbar (Folie 4). Preisanker der Konkurrenz: 0 bis 200 € im Monat. Ehrlich: Zahlungsbereitschaft ist nicht belegt. "
              "FRAGE – ANTWORT: „Sind die Gespräche anonym?“ Ja. Es gibt keine Namen von Personen oder Firmen, die Betriebe sind nur beschrieben (Betrieb mittlerer Größe, Kleinbetrieb, Vergabestelle). "
              "GRENZE: Welches Verwaltungssystem die Betriebe nutzen und wie ein Treffer dort landet, wurde in den drei Gesprächen nicht erfragt; die Perspektive des Betriebs (selbst filtern, Datenübergabe) steht auf Folie 6, der Kurztest ist vorbereitet, nicht durchgeführt. ZEIG-MIR-WO: docs/business.md §8.1 (wie Betriebe an Aufträge kommen) und §8.9 (Gespräche), §9 (Perspektive des Betriebs), docs/annahmen.md (A1, A15).")

schritte = (("Meldung", "Hinweis kommt 28 Tage vor Abgabe"), ("Begehung", "Nur ein Termin vor Ort"),
            ("Kalkulation", "Nachts, unter Zeitdruck"), ("Entscheidung", "Entfernung, Personal, Bürokratie"))
for i, (h, t) in enumerate(schritte):
    x = 0.6 + i * 2.25
    rect(s, x, 1.4, 2.1, 1.55, WHITE, name=h + " Karte")
    kreis(s, x + 0.15, 1.52, 0.4, BLUE, str(i + 1), size=14)
    box(s, x + 0.65, 1.52, 1.4, 0.4, h, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.15, 2.05, 1.85, 0.85, t, size=14)
rect(s, 0.6, 3.1, 4.3, 1.1, WHITE, name="Kosten Karte")
box(s, 0.8, 3.15, 3.95, 1.0, [[("Suchen kostet: ", {"bold": True}), ("ein Portal-Abo rund 1.500 € im Jahr (mittlerer Betrieb)", {})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Kosten Text")
rect(s, 5.1, 3.1, 4.3, 1.1, DARK, name="Publikumsfrage Karte")
box(s, 5.3, 3.15, 3.95, 1.0, [[("Frage an euch: ", {"bold": True, "color": AMBER}), ("Gibt es kostenlos eine Liste auslaufender öffentlicher Verträge?", {"color": WHITE})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Publikumsfrage")
laien(s, "Je früher der Hinweis, desto mehr Zeit für Begehung und Kalkulation (Annahme).")
fuss(s, "Quelle: drei Gespräche (n = 3: mittlerer Betrieb, Kleinbetrieb, Vergabestelle), Hinweise, keine Belege; docs/business.md §8.1, §8.9.")

# Folie 6 ------------------------------------------------------------
s = new_slide("Auflösung: Wer bietet es schon?",
              "ZEIT 1:30. KERNAUSSAGE: Auflösung der Publikumsfrage: Ja, es gibt sie kostenlos. Vergabeweiser listet 1.005 Gebäudereinigungs-Verträge, die in 12 Monaten enden, mit Zuschlagsempfänger, Zahl der Angebote und Verlängerungsoptionen, nach eigener Angabe auch unterhalb der EU-Schwelle (von uns nicht gemessen). "
              "TABELLE (Prüfstand): Vergabeweiser und die Vertragsende-Seite von AusschreibungsRadar hat Claude am 2026-11-05 selbst nachgelesen; AusschreibungsRadar: 0 bis 149 € im Monat, KI-Eignungsanalyse ab 29 €, Bid/No-Bid-Check mit Match-Score ab 79 € (Preise aus der Recherche); aufträge.io (43.373 Verträge mit Ende in 12 Monaten, auf Anfrage) und subreport (84–198 € im Monat) stammen aus der Recherche eines Agenten und sind nicht einzeln nachgeprüft; DTAD nach Aussage des Betriebs mittlerer Größe: knapp 1.500 € im Jahr, eine Liste auslaufender Verträge kenne er dort nicht. Beide geprüften deutschen Anbieter schreiben selbst, dass der Auftraggeber über die Neuausschreibung entscheidet. "
              "HINWEIS (Fakt, Paket A, 130 Oberpfalz-Lose): Auftragnehmer genannt bei 99,2 %, Zuschlagswert über 1 € nur bei 47,7 %, Zahl der Angebote bei 60,8 %. TED-Daten allein reichen für Preisbenchmarks also nur zur Hälfte. "
              "Beobachtung (Hypothese, n = 3): Zwei Betriebe nutzen keinen der Dienste, einer kannte sie vom Hörensagen, die andere gar nicht: eher ein Bekanntheits- als ein Angebotsproblem der Konkurrenz. "
              "FRAGE – ANTWORT: „Warum nicht einfach Vergabeweiser nutzen?“ Doch, für die Suche nach Vertragsenden spricht vieles dafür: kostenlos, nach eigener Angabe auch unterschwellige Verfahren (wir nutzen dieselbe Quelle, den Bekanntmachungsservice, nur teilweise), Zuschlagsempfänger und Bieterzahl. Unsere Liste ist als eigenes Produkt nicht tragfähig; was bleibt und die Sicht des Betriebs (selbst bauen), steht auf Folie 6. "
              "ZEIG-MIR-WO: docs/business.md §8.2 (Wettbewerber), §8.7 (Marktzahlen), reports/nebentest_ausschreibungsradar.md, reports/wettbewerbsbild_oberpfalz.md.")

box(s, 0.6, 1.38, 8.8, 0.5, [[("Vergabeweiser: ", {"bold": True}), ("1.005 Reinigungsverträge enden in den nächsten 12 Monaten, mit Auftragnehmer und Zahl der Angebote.", {})]], size=14, name="Vergabeweiser Satz")
zeilen = (("Vergabeweiser", "kostenlos", "nachgelesen", GREEN), ("AusschreibungsRadar", "0–149 € im Monat", "Funktion nachgelesen", BLUE),
          ("subreport", "84–198 € im Monat", "Recherche", BLUE), ("DTAD", "rund 1.500 € im Jahr", "Gespräch", BLUE),
          ("aufträge.io", "auf Anfrage", "Recherche", BLUE))
for i, (n, p, t, f) in enumerate(zeilen):
    y = 1.95 + i * 0.45
    rect(s, 0.6, y, 8.8, 0.4, WHITE, radius=0.12, name=n + " Zeile")
    box(s, 0.8, y, 2.6, 0.4, n, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 3.5, y, 3.0, 0.4, p, size=14, bold=(i == 0), color=f, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 6.6, y, 2.7, 0.4, t, size=14, color=GREY, anchor=MSO_ANCHOR.MIDDLE)
laien(s, "Vertragsenden nachsehen kostet bei Vergabeweiser nichts.")
fuss(s, "nachgelesen = von uns auf der Anbieterseite gelesen; Recherche = nicht einzeln geprüft; Gespräch = Aussage eines Betriebs. Preise ohne Gewähr.")

# Folie 7 ------------------------------------------------------------
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

rect(s, 0.6, 1.4, 4.0, 2.8, WHITE, name="Vergleich Karte")
box(s, 0.8, 1.5, 3.6, 0.8, "66 : 58", size=44, color=BLUE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name="Vergleich Zahl")
box(s, 0.8, 2.35, 3.6, 1.8, [ "richtige Enddaten bei 70 Losen: unsere Liste gegen Vergabeweiser, auf Los- und Definitionsebene.",
    [("Ein Qualitätsvorsprung ist nicht belegt.", {"bold": True})]], size=14, space=8, name="Vergleich Text")
rect(s, 4.8, 1.4, 4.6, 2.8, WHITE, name="Ursachen Karte")
box(s, 5.0, 1.5, 4.2, 0.55, "Warum 15 von 160 Losen abweichen", size=14, bold=True, color=GREY)
balken(s, 4.9, 1.85, 4.4, 2.3, ["Höchstende gemeint", "Teilauftrag (Los)", "Ursache offen", "Fehler bei uns", "mehrdeutig"],
       [7, 4, 2, 1, 1], [AMBER, AMBER, GREY, GREY, GREY], "Ursachen der 15 abweichenden Lose", maximum=10, fmt='0')
laien(s, "Beide Listen sind brauchbar; das Datum in der Bekanntmachung selbst gegenprüfen.")
fuss(s, "Vorab-Schwelle (mindestens 16 Lose) war bei 15 abweichenden Losen unerreichbar: unser Fehler, offen berichtet. Gleiche TED-Quelle, Leser aus einer Modellfamilie, kein Mensch.")

# Folie 8 ------------------------------------------------------------
s = new_slide("Competitive Edge und Make or Buy",
              "ZEIT 2:00. KERNAUSSAGE: Aus Unternehmersicht ergibt die Liste als eigenes Produkt keinen Sinn. Von der Idee bleibt ein Merkmalsunterschied, kein belegter Vorsprung und kein belegter Markt. Neu: Wir haben die Frage auch aus Sicht des Betriebs gestellt, der seine Aufträge selbst filtert (Make or Buy). "
              "GRÜNDE GEGEN EIN EIGENES PRODUKT (Interpretation, docs/business.md §8.4, Streifen oben): (1) Das Kernprodukt gibt es schon, kostenlos und nach eigener Angabe auch unterhalb der EU-Schwelle (von uns nicht gemessen). (2) Das Kundenproblem ist eine Setzung: Der Engpass liegt nach den Quellen eher bei Preis (63 % der Vergaben nur nach Preis), Personal und Bürokratie; ob „früher wissen“ hilft, ist offen (A1, A15). (3) Die nahe Zukunft fehlt: Die Vorgänger heutiger Neuausschreibungen stammen meist aus der Zeit vor eForms (55 von 68 Backtest-Vorgängern). (4) Vertragsende ist kein Termin: Verlängerung ist der Normalfall, Backtest 28,8 %. (5) Markt klein: grobe Schätzung des Gutachtens 3,6–7,2 Mio. € bei offenen Annahmen. "
              "MAKE OR BUY (Paket D, Nachtrag 2026-11-06; Quelle reports/make_or_buy.md, Skript src/report/make_or_buy.py; ALLE Kosten sind Annahmen): Idee des Nutzers: Der Betrieb holt kostenlose TED-Daten, filtert selbst und übergibt die Treffer maschinenlesbar in sein Verwaltungssystem; die Webseite stellt nur dar. Rechnung bei 100 € pro Stunde (Annahme): Niedrig (20 h einmalig, 5 h im Jahr) 3.500 € in drei Jahren, Mittel (60 h, 20 h) 12.000 €, Hoch (120 h, 50 h) 27.000 €. Break-even im Basismodell: gegen DTAD (knapp 1.500 € im Jahr, Gespräch) nur im Szenario Niedrig, nach 2,0 Jahren; gegen AusschreibungsRadar Starter und gegen Vergabeweiser nie. Dieses „nie“ ist eine Folge der Modellkonstruktion (Abos und kostenlose Dienste ohne Eigenaufwand gerechnet, Eigenbau mit Stunden), keine Messung. SYMMETRISCHE VARIANTE (Annahmen): Rechnet man auch für Abo und kostenlose Dienste Nutzungsstunden (10 / 30 / 60 Stunden im Jahr; Import eines kostenlosen Dienstes 20 Stunden einmalig plus 10 im Jahr), liegt der Break-even gegen DTAD bei 1,0 / 2,4 / 4,8 Jahren und gegen einen kostenlosen Dienst mit Übernahme von Hand bei 4,0 / 6,0 / 12,0 Jahren. Die Zahl der zusätzlichen Aufträge, die ein früher Hinweis bringen müsste, damit sich die Kosten der ersten drei Jahre lohnen: 0,14 bis 1,08 (Marge 5 %, Median-Jahresumsatz 167.404 €, Deckungsbeitrag 25.110 € je Auftrag ohne Angebotsaufwand und Zuschlagswahrscheinlichkeit); das ist eine Rechengröße, kein Nutzenbeleg. Die Kosten sind klein gegen einen Auftrag: Nicht die Kostenfrage entscheidet, sondern ob ein früher Hinweis überhaupt einen Auftrag bringt (nicht belegt). "
              "EHRLICHES FAZIT: „Keine Abo-Kosten“ trägt nicht, denn kostenlose Wege existieren und der Eigenbau hat Einrichtungs-, Betriebs- und Pflegekosten. Ein Mehrwert müsste aus Funktion kommen. OFFENE HYPOTHESEN (ungeprüft): Daten ins eigene System mit dokumentiertem Schema (Referenz-Export, Schema 1.1, 26 Felder, drei Dateien plus Variante ohne Auftragnehmer, vom Skript gegen das Schema validiert, in Excel nicht getestet), Anreicherung (Ende je Los, Herkunft je Feld), Wettbewerbsfelder nur zur Hälfte aus TED; die Nische, wobei der Kanal der Vorteil wäre, nicht die Technik, denn die Daten sind offen. Zielgruppe nur Betriebe mit Branchensoftware und IT-Kapazität: rund ein Drittel arbeitet laut einem sekundär zitierten Branchenartikel durchgängig mit Branchensoftware (Original nicht geprüft). Die Perspektive des Betriebs wurde in den drei Gesprächen NICHT erfragt; der Kurztest ist vorbereitet (Fragen im Wizard-of-Oz-Blatt), nicht durchgeführt. Kriterium D4 vorab: „Datenübergabe ist relevant“ nur zulässig, wenn H1 und H2 bei mindestens 2 von 3 Betrieben bestätigt sind; bisher keine Aussage. "
              "WAS BLEIBT (Fakten): (1) Ende je Los und Ende der Grundlaufzeit statt Höchstende; in rund 10 % der Lose weicht Vergabeweisers Datum davon ab, auf Los- und Definitionsebene (Folie 5). (2) Ein dokumentiertes Prüfverfahren mit Seeds, Hashes und Evaluator. Optionsanalyse an 52 Paaren: Bei belegter Option kam die Neuausschreibung in 70,8 % zwischen Ende der Grundlaufzeit und Höchstende (n = 24, Hinweis). Beide Punkte sind Fakten aus dem Projekt; ein Vorteil gegenüber Vergabeweiser folgt daraus nicht. "
              "AUSBLICK (Paket B, Oberpfalz): Im Bekanntmachungsservice (OCDS-Jahresdateien 2024 bis 2026, CC0) stehen 32 von 120 Reinigungsverfahren (26,7 %, Intervall 19,6–35,2 %) nicht auf TED, also rund ein Viertel. Das ist ein Hinweis auf eine Lücke der TED-Basis, kein belegter Vorsprung und keine Schwelle, die gemessen wurde; „national“ heißt „nicht auf TED gefunden“; B1 (≥ 33 %) ist nicht entscheidbar. Nicht sagen: „TED-Daten reichen“, „0 %“, „genau 27 %“, „Vergabeweiser deckt mehr ab“ als Tatsache, etwas über Nachfrage. "
              "NICHT BELEGT: Qualitätsvorteil beim Lesen; Nachfrage und Zahlungsbereitschaft; Relevanz der Datenübergabe (H1, H2); Abdeckung unterhalb von TED (A3); der Vertriebskanal. "
              "FRAGE – ANTWORT: „Ist ‚nie günstiger‘ nicht trivial?“ Ja, es ist eine Modellkonstruktion: Im Basismodell haben Abo und kostenlose Dienste keinen Eigenaufwand, der Eigenbau hat Stunden, also kann der Eigenbau dort nicht günstiger sein. Deshalb haben wir die symmetrische Variante gerechnet (auch Nutzungsstunden bei den Alternativen); dort hängt das Ergebnis an den angenommenen Stunden. Die Aussage ist, dass der Preis kein Vorteil ist, nicht dass Eigenbau teuer wäre. FRAGE – ANTWORT: „Warum selbst bauen statt Vergabeweiser nutzen?“ Gar nicht, wenn es nur um das Finden geht: Im Modell (Annahmen) ist Eigenbau gegen Vergabeweiser nie günstiger, als Folge der Konstruktion. Selbst bauen wäre nur sinnvoll, wenn der Betrieb Daten mit festem Schema und Herkunft je Feld in sein eigenes System braucht; ob er das braucht, ist nicht geprüft. "
              "FRAGE – ANTWORT: „Welches Verwaltungssystem haben Betriebe?“ Nicht erfragt. Sekundär: rund ein Drittel der Gebäudedienstleister arbeitet durchgängig mit Branchensoftware (hagel-it.de, zitiert den BIV-Branchenreport, Original nicht geprüft); der Kleinbetrieb aus den Gesprächen hat keines genannt. Ob Branchen-ERP Importschnittstellen für Ausschreibungsdaten hat, ist nicht geprüft. "
              "FRAGE – ANTWORT: „Wer pflegt das?“ Der Betrieb selbst oder ein Integrator; im Modell 5 bis 50 Stunden im Jahr (Annahme, nicht gemessen). TED-Felder, Schema und Dienste ändern sich; die Pflege ist der Kostenpunkt, der ein Abo erklärt. Das Projekt liefert keine Plattform und keinen Pflegevertrag. "
              "FRAGE – ANTWORT: „Warum ist die Webseite nur eine Demo?“ Sie ist Darstellung; die Datenübergabe leistet der Export mit dokumentiertem Schema 1.1 (CSV, CSV für deutsches Excel, JSON; dazu eine Variante ohne Auftragnehmernamen). Die Schaltfläche „Auswahl als CSV“ auf der Webseite liefert dieselben Spalten. "
              "FRAGE – ANTWORT: „Warum nicht gleich die Daten von bund.de einbauen?“ Die Quelle, die wir geprüft haben, ist der Bekanntmachungsservice (oeffentlichevergabe.de, CC0); ob bund.de dieselben Daten hält, haben wir nicht geprüft. Die Lücke ist nur ein Hinweis, die Feldqualität der Verfahren, die nicht auf TED stehen, ist nicht gemessen, und ohne belegte Nachfrage wäre es Aufwand ohne Ziel. Deshalb Ausblick. "
              "TRANSFERFRAGE „Anderer Standort, andere Nische, doppeltes Volumen?“: Pipeline und Prüfverfahren übertragbar, Lese-Regeln neu testen; doppeltes Volumen: Abruf skaliert, die menschliche Prüfung nicht. "
              "FRAGE – ANTWORT: „Warum habt ihr noch eine Demo gebaut, obwohl der Auswahlbogen K-I ausgeschlossen hat?“ Sie wurde auf Wunsch gebaut, nach dem Auswahlbogen, als Veranschaulichung der Datenübergabe (Teams-Karte, E-Mail, offline aus einem TED-Schnappschuss). K-I hat dort K7 = 0 und bleibt nur Ausblick; die Demo ändert das nicht und sagt nichts über Nachfrage. Profile und Stichtag sind erfunden und datengetrieben gewählt, die Zahlen 4 und 2 Treffer sind kein Befund. „13 von 14“ KI gegen Regel hat keine Referenz durch einen Menschen und ist nur teils informativ (5 Fälle trivial, gleiche Entfernung, kein inhaltlicher Ablehnungsfall). Der Vorgänger-Hinweis ist gebaut, an echten Bekanntmachungen aber nie ausgelöst (0 von 6), also nicht belegt. Belegt ist nur die Machbarkeit der Datenübergabe. "
              "FRAGE – ANTWORT: „Wo ist der Unterschied zu AusschreibungsRadar?“ Es gibt keinen belegten Unterschied: Einen Eignungsabgleich mit dem Firmenprofil und Alerts bietet AusschreibungsRadar laut Anbieterseite (Eigenangabe, von uns nicht geprüft) schon, KI-Eignungsanalyse und Match-Score ab 79 €. Die Demo beansprucht kein Alleinstellungsmerkmal. Ein Teams-Kanal ist bei keinem deutschen Dienst belegt, ob Betriebe Teams als Zielort nutzen, wurde nicht erfragt. Zeig-mir-wo: docs/demo_push.md, docs/demo/push_demo.html. "
              "ZEIG-MIR-WO: docs/prototyp/export/vertragsliste_v1_de.csv (Beispiel-Export, in Excel öffnen: ein Los pro Zeile, 26 Spalten; Datei in Excel nicht getestet), docs/export_schema.md, reports/make_or_buy.md, docs/business.md §8.4, §8.5, §9, reports/wettbewerbsbild_oberpfalz.md, reports/optionsanalyse.md, docs/annahmen.md.")

rect(s, 0.6, 1.4, 4.4, 2.8, WHITE, name="Kosten Karte")
box(s, 0.8, 1.5, 4.0, 0.55, "Eigenbau: Kosten in 3 Jahren, in € (Annahmen)", size=14, bold=True, color=GREY)
balken(s, 0.7, 1.95, 4.2, 2.2, ["Niedrig", "Mittel", "Hoch"], [3500, 12000, 27000], [GREEN, AMBER, RED], "Eigenbau Kosten", maximum=40000, fmt='#,##0')
rect(s, 5.2, 1.4, 4.2, 1.05, WHITE, name="Nie Karte")
box(s, 5.4, 1.4, 3.85, 1.05, [[("„Nie günstiger“ ", {"bold": True}), ("als kostenlose Dienste folgt aus der Rechnung, nicht aus einer Messung.", {})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Nie Text")
rect(s, 5.2, 2.55, 4.2, 0.85, WHITE, name="Daten Karte")
box(s, 5.4, 2.55, 3.85, 0.85, [[("Lohnt nur, ", {"bold": True, "color": GREEN}), ("wenn die Daten ins eigene System sollen. Ungeprüft.", {})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Daten Text")
rect(s, 5.2, 3.5, 4.2, 0.7, DARK, name="Nicht belegt Karte")
box(s, 5.4, 3.5, 3.85, 0.7, [[("Nicht belegt: ", {"bold": True, "color": AMBER}), ("Nachfrage, Zahlungsbereitschaft", {"color": WHITE})]], size=14, anchor=MSO_ANCHOR.MIDDLE, name="Nicht belegt Text")
laien(s, "Kostenlose Dienste genügen, solange die Daten nicht ins eigene System sollen.")
fuss(s, "Annahmen: 100 € je Stunde; Niedrig 20 h einmalig + 5 h im Jahr, Mittel 60 + 20, Hoch 120 + 50. „Nie“ = Modellkonstruktion. Gespräche n = 3.")

# Folie 7 (Demo) ------------------------------------------------------------
DEMO_VIDEO = ROOT / "docs" / "video" / "live_demo_aufnahme.mp4"      # erzeugt von src/report/demo_aufnahme.py
DEMO_POSTER = ROOT / "docs" / "vortrag" / "poster_live_demo.png"
DEMO_LINK_REL = "../demo/live_demo.html"                             # relativ zur PPTX (docs/vortrag/); gilt, wenn der Ordner docs/ mitgenommen wird
DEMO_NOTIZEN = (
    "ZEIT 0:45 (bleibt 0:45; dauert die Live-Vorführung länger, die Aufnahme zeigen oder die Demo überspringen und nur die Einordnung sagen). "
    "KERNAUSSAGE: Eine kleine Demo zeigt, wie die Datenübergabe aussehen könnte: Aus echten, öffentlichen TED-Bekanntmachungen (großer Datensatz: 590 Ausschreibungen mit Leistungsort Bayern, 16.10.2025 bis 06.11.2026) filtert das Profil einer erfundenen Firma, und das Ergebnis erscheint als Teams-Karte und als E-Mail-Vorschau. Nichts wird gesendet, alles läuft offline im Browser. "
    "KLICKFOLGE LIVE (8 Schritte, Datei docs/demo/live_demo.html, Link auf der Folie oder vorher in einem Browser-Tab öffnen): "
    "(1) Seite zeigen und den gelben Hinweis vorlesen: fiktive Firma, kein Business Case, nichts gesendet. "
    "(2) Datensatz „Großer Datensatz (Bayern, 12 Monate)“ wählen. "
    "(3) Schnellknopf „Cham, 50 km“; der Frist-Filter bleibt AN („nur Ausschreibungen, bei denen man sich noch bewerben kann“). "
    "(4) „Filterung starten“: der Trichter läuft etwa 8 Sekunden; dabei mitlesen, 590 → 562 → 428 → 405 → 37 → 19 → 2 (Zeitraum, Mehrfachveröffentlichung, Reinigungs-CPV, Oberpfalz, Radius, Frist). "
    "(5) Ergebnis: 2 Treffer; sagen: „Treffer sind kein Befund über den Markt, die Firma ist erfunden.“ "
    "(6) Einen Treffer anklicken: Teams-Karte mit den Fakten aus der Bekanntmachung, getrennt von der Deutung („Datenfeld“ gegen „im Text, nicht im Datenfeld“). "
    "(7) Kanal „E-Mail“ umschalten: derselbe Inhalt als Mail-Vorschau. "
    "(8) Frist-Filter AUS schalten (Schritt 1, Haken entfernen), erneut starten oder „Sofort anzeigen“: jetzt 16 statt 2 Treffer, 14 davon mit abgelaufener Frist. Dazu sagen: „Das ist nur zur Veranschaulichung; auf diese Ausschreibungen kann man sich nicht mehr bewerben.“ Der Warnhinweis „nur zur Veranschaulichung“ steht auch in der Seite. "
    "RÜCKFALL: Öffnet der Browser nicht oder hakt die Seite, die Aufnahme auf der Folie abspielen (docs/video/live_demo_aufnahme.mp4, etwa 1 Minute, ohne Ton, dieselbe Klickfolge) und live dazu sprechen. "
    "EINORDNUNG (wichtig, immer sagen): Die Demo ist eine Veranschaulichung der Datenübergabe, kein Business Case und kein Beleg für Nachfrage; der Auswahlbogen (docs/business_case_auswahl.md) hat diese Idee (K-I) wegen K7 = 0 ausgeschlossen. Sie wurde danach auf Wunsch gebaut. Firma und Stichtag sind erfunden; nichts wird gesendet; Treffer sind kein Befund; ein KI-Urteil gibt es nur für die gespeicherten Beispiele P1 und P2, bei jeder anderen Firma gilt eine Stichwortregel (im Bild „Stichwortregel, keine KI“). "
    "ZAHLEN (Fakt aus dem Lauf, docs/demo/ergebnis_lauf.json, Beispiel-Schnappschuss): 621 Bekanntmachungen, 145 im Fenster, 131 ohne Doppelveröffentlichung, 125 mit Reinigungs-CPV, davon in der Oberpfalz 4. Profil P1 (Schwandorf, 60 km): 4 Nachrichten, KI passt/unklar/nicht 3/1/0; Profil P2 (Amberg, 25 km): 2 Treffer, 1/1/0. KI gegen Regel stimmt in 13 von 14 Fällen überein, davon 5 trivial, ohne Referenz durch einen Menschen. Der Vorvertrags-Hinweis ist gebaut, an echten Bekanntmachungen nie ausgelöst (0 von 6), also nicht belegt. Teams-Anzeige, Versand und Live-Modus wurden nie getestet. "
    "FRAGE – ANTWORT: „Warum eine Demo, wenn es keinen Business Case gibt?“ Sie zeigt nur die technische Machbarkeit der Datenübergabe (offene Daten, Schema, Filter, Nachricht); sie sagt nichts über Nachfrage. „Wo ist der Unterschied zu AusschreibungsRadar?“ Ein Alleinstellungsmerkmal beanspruchen wir nicht: AusschreibungsRadar bietet Eignungsabgleich laut Anbieterseite schon; unser Merkmalsunterschied (Ende je Los, Grundlaufzeit) steckt nicht in dieser Demo, und ein Qualitätsvorsprung ist nicht belegt (Folien 4 und 5). "
    "ZEIG-MIR-WO: docs/demo_push.md (Abschnitte 10 und 11), docs/demo/live_demo.html, docs/demo/push_demo.html, docs/demo/nachrichten/, Aufnahme docs/video/live_demo_aufnahme.mp4 (Skript src/report/demo_aufnahme.py). ")

s = new_slide("Demo: von der Bekanntmachung zur Push-Nachricht", DEMO_NOTIZEN)

if DEMO_VIDEO.exists() and DEMO_POSTER.exists():
    # Bildschirmaufnahme der Live-Demo (ohne Ton) links, Link und Einordnung rechts
    s.shapes.add_movie(str(DEMO_VIDEO), Inches(0.6), Inches(1.4), Inches(4.97), Inches(2.8), poster_frame_image=str(DEMO_POSTER), mime_type="video/mp4").name = "Aufnahme Live-Demo"
    rect(s, 5.8, 1.4, 3.6, 1.35, LBLUE, name="Link Karte")
    tb = box(s, 5.95, 1.45, 3.3, 1.25, [[("Live-Demo im Browser", {"bold": True, "color": DBLUE, "size": 14, "font": HEAD})], "", ""],
             size=14, color=DBLUE, anchor=MSO_ANCHOR.MIDDLE, name="Link Text", space=2)
    # Absatz 2: anklickbarer Link (relativ zur PPTX); Absatz 3: Textpfad für den Fall, dass der Link auf dem Vortragsrechner nicht greift
    p2, p3 = tb.text_frame.paragraphs[1], tb.text_frame.paragraphs[2]
    r = p2.add_run()
    r.text = "docs/demo/live_demo.html"
    r.font.size, r.font.bold, r.font.name = Pt(14), True, BODY
    r.hyperlink.address = DEMO_LINK_REL
    r2 = p3.add_run()
    r2.text = "Pfad: ...\\vergabe_radar\\docs\\demo\\live_demo.html"
    r2.font.size, r2.font.color.rgb, r2.font.name = Pt(11), DBLUE, BODY
    rect(s, 5.8, 2.85, 3.6, 1.35, WHITE, name="Einordnung Karte")
    box(s, 5.95, 2.9, 3.3, 1.25, [[("Fiktive Firma, kein Business Case", {"bold": True, "color": RED, "size": 14, "font": HEAD})],
                                  "Nichts gesendet. Treffer sind kein Befund. KI-Urteil nur für P1/P2, sonst Stichwortregel."],
        size=12, anchor=MSO_ANCHOR.MIDDLE, name="Einordnung Text", space=3)
    DEMO_STATUS = "Aufnahme eingebettet"
else:
    # Fallback ohne Aufnahme: Trichter und Karten-Mock wie bisher
    stufen = (("621", "Bekanntmachungen"), ("145", "vom 2. bis 16.10.2026"), ("125", "zur Gebäudereinigung"), ("4", "in der Oberpfalz"))
    for i, (zahl, text) in enumerate(stufen):
        y = 1.4 + i * 0.7
        rect(s, 0.6, y, 4.0, 0.6, WHITE, name=f"Trichter {i + 1} Karte")
        box(s, 0.8, y, 1.0, 0.6, zahl, size=24, color=BLUE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, name=f"Trichter {i + 1} Zahl")
        box(s, 1.8, y, 2.7, 0.6, text, size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Trichter {i + 1} Text")
    # Mock einer Teams-Karte (Aufbau der echten Karte docs/demo/nachrichten/P1_691173-2026.json)
    rect(s, 4.8, 1.4, 4.6, 2.05, WHITE, name="Karte Rahmen").line.color.rgb = LINE
    rect(s, 4.8, 1.4, 0.1, 2.05, BLUE, MSO_SHAPE.RECTANGLE, name="Karte Akzent")
    box(s, 5.1, 1.48, 4.15, 0.5, "Neue Ausschreibung: Unterhalts- sowie Glas- und Rahmenreinigung", size=14, bold=True, name="Karte Titel")
    box(s, 5.1, 2.1, 4.15, 0.7, [[("Ort  ", {"color": GREY}), ("Schwandorf", {})], [("Frist  ", {"color": GREY}), ("11.11.2026", {})]], size=14, name="Karte Fakten")
    rect(s, 5.1, 2.82, 4.15, 0.5, PALE, radius=0.1, name="Karte KI Block")
    box(s, 5.2, 2.82, 4.0, 0.5, "KI-Deutung, nicht Fakt", size=14, color=GREY, anchor=MSO_ANCHOR.MIDDLE, name="Karte KI Text")
    rect(s, 4.8, 3.55, 4.6, 0.65, BLUE, name="Hinweis Live-Demo")
    box(s, 4.95, 3.55, 4.3, 0.65, "Live-Demo im Browser: docs/demo/live_demo.html", size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, name="Hinweis Live-Demo Text")
    DEMO_STATUS = "Fallback ohne Aufnahme"
laien(s, "So könnte ein passender Hinweis im Alltag aussehen. Gesendet wurde nichts.")
fuss(s, "Veranschaulichung, kein Business Case. Firma und Stichtag erfunden, Anzeige in Teams nie getestet. Aufnahme ohne Ton: docs/video/live_demo_aufnahme.mp4.")

# Folie 10 ------------------------------------------------------------
s = new_slide("KI-Irrwege und Trennung von Entwicklung und Test",
              (              "ZEIT 1:30 (Teil 1 Irrwege etwa 0:45, Teil 2 Trennung von Entwicklung und Test etwa 0:45). KERNAUSSAGE: Claude Code hat Regeln, Stichproben und Auswertungen mitgebaut; jeder dieser Fehler wurde von einem getrennten Evaluator, im Test oder vom Nutzer gefunden, nicht von der Hand, die ihn gemacht hat. "
              "Vier von 27 Einträgen in docs/ki_irrwege.md (der Paket-B-Fall steht im Lab-Log, Abschnitt 7): (1) Entwicklung 10–11 von 12 plausibel, im Test 11 von 24 richtig (Iteration 3): Regel verworfen. (2) „Blind“ war nicht blind: Leser der Iteration 8 hatten die Projektbeschreibung im Kontext (CLAUDE.md), gefunden vom Evaluator, offen genannt. "
              "(3) Konkurrenz übersehen: Die Suche vom 24.10. fand keinen deutschen Dienst, tatsächlich gibt es zwei; gefunden vom Recherche-Agenten nach dem Hinweis des Dozenten. (4) Schwelle unerreichbar: Claude übernahm die Diskordanzrate von 17 % aus Iteration 10 für 160 Lose, es waren 9,4 %; gefunden vor den Leserantworten, nicht nachträglich geändert. "
              "LERNPUNKT STATT SCHWÄCHE: „Konkurrenz erst in Iteration 10 gesehen“ ist ein Prozessfehler, kein Pech. Plan G1.1 (Wettbewerber sichten) blieb offen; die Entscheidung gegen Kundenkontakt fiel am 2026-10-29. Kosten: Iterationen 5 bis 9 arbeiteten an einer Liste, die es kostenlos gibt. Lehre: ein Marktgate in Phase 1, vor der Modellierung (Gibt es das schon? Wer zahlt dafür? Nach Gesprächen, nicht nach Annahmen). "
              "FRAGE – ANTWORT: „Warum erst jetzt die Konkurrenz?“ Weil die Sichtung (G1.1) offen blieb und die Suche am 24.10. die Dienste nicht fand; die Suche war zu eng. Das ist ein Prozessfehler im Business Understanding. Er hat Zeit gekostet (Iterationen 5 bis 9), aber das Ergebnis geändert: Wir sagen heute, dass die Liste kein eigenes Produkt ist. "
              "LERNPUNKT „Null = Verdachtsmoment“ (ein Satz, wenn Zeit): Paket B fand zunächst 0 von 84 Verfahren nicht auf TED; wir haben die Null nicht berichtet, sondern geprüft, und die Robustheitsprüfung zeigte ein Filterartefakt (nationale Verfahren tragen am Lieferort meist nur „DE2“). Danach 26,7 %. Eine Null ist ein Verdachtsmoment, kein Ergebnis. Die erste Auswertung („B1 deutlich verfehlt“) gilt nicht; B1 ist nicht entscheidbar. "
              "Weitere (nicht auf der Folie): Prüfer und Regel von derselben Hand (Iteration 2), versteckte Felder (65 von 95 „unbekannt“, Iteration 7), Dauerfeld enthält die Option schon (12 Lose, 0,13 % der Liste). Ein eigener Subagent (Evaluator) prüft jede Iteration kritisch. "
              "ZEIG-MIR-WO: docs/ki_irrwege.md, docs/projektplan.md (G1.1), reports/evaluation_iteration10b.md. ") + (              "TEIL 2, TRENNUNG VON ENTWICKLUNG UND TEST. KERNAUSSAGE: Hypothese, Kriterien und Seed stehen im Git, bevor die Stichprobe gezogen und die Antworten gelesen werden; die Commit-Reihenfolge ist der Nachweis, dass Test und Entwicklung getrennt sind. Die Folie zeigt die Reihenfolge der Iteration 10b (Kurzfassung der Commit-Nachrichten, im Terminal von unten nach oben lesen). "
              "WAS IN DER FRAGERUNDE LIVE GEZEIGT WIRD: (1) Im Terminal `git log --oneline`: 4f50436 (Hypothese, Kriterien, Skript und Seed 20261112 vorab), 9d63c59 (Stichprobe gezogen, SHA-256 des Schlüssels 2cd00206…3e33; Schlüsseldatei lokal, nicht im Git: data/processed/stichprobe_iteration10b_schluessel.csv), 49bb198 (Skript für Abruf und Auswertung vor dem Abruf), 6b7e8d8 (Paket und Leseskript vor den Antworten), 69917ff (Antworten der Leser unverändert), f6583cc (Auswertung). "
              "(2) Eine Regel in src/prepare/vertragsliste.py öffnen und einen Parameter ändern (z. B. Seed in src/prepare/stichprobe_iteration10b.py): Erwartung: Zahlen ändern sich leicht, die Aussagen bleiben, da die Stichprobe nur 70 bzw. 160 Lose hat. (3) Fehlwerte zeigen: 33 der 130 Oberpfalz-Lose ohne Ende (Stufe F), keine Laufzeitfelder im XML (reports/beispiel_liste_oberpfalz.csv). "
              "Iteration 9 genauso: Regeln a03a4a8, Seed und Skript 4521952, Stichprobe und Auswertungsskript b3b1471, Antworten erst e1726e7. Entwicklungsfälle sind aus der Stichprobe ausgeschlossen (reports/entwicklung_iteration9_notices.txt). "
              "EHRLICHE LÜCKEN: das Lauf-Skript der Iteration-9-Leser wurde erst mit den Antworten committet; in Iteration 8 kannten die Leser den Fehlertyp; in 10b liegt das Protokoll der Leserläufe außerhalb des Repos. Der 10b-Fehler (Schwelle unerreichbar) wurde vor den Leserantworten bemerkt und offengelegt, aber nicht mehr geändert. "
              "ZEIG-MIR-WO: git log, src/prepare/stichprobe_iteration10b.py, docs/reproduzierbarkeit.md."))

items = (("Im Test viel schlechter", "Beim Entwickeln 10–11 von 12 richtig, im Test nur 11 von 24."),
         ("„Blind“ war nicht blind", "Die KI-Leser kannten die Projektbeschreibung."),
         ("Konkurrenz zu spät gesehen", "Erst spät entdeckt. Lehre: früh fragen, ob es das schon gibt."))
for i, (h, t) in enumerate(items):
    y = 1.4 + i * 0.95
    rect(s, 0.6, y, 4.5, 0.88, WHITE, name=f"Irrweg {i + 1}")
    box(s, 0.8, y + 0.05, 4.1, 0.28, h, size=14, bold=True, color=RED if i == 0 else DARK)
    box(s, 0.8, y + 0.33, 4.1, 0.55, t, size=14)
box(s, 5.3, 1.4, 4.1, 0.7, "Trennung von Entwicklung und Test: erst Regeln festlegen, dann testen.", size=14, bold=True)
rect(s, 5.3, 2.15, 4.1, 1.5, INK, name="Terminal")
box(s, 5.45, 2.22, 3.85, 1.4, [[("$ git log --oneline", {"color": AMBER})],
    "f6583cc Auswertung", "69917ff Antworten unverändert", "6b7e8d8 Paket vor den Antworten",
    "9d63c59 Stichprobe gezogen", "4f50436 Kriterien, Seed vorab"],
    size=11, color=WHITE, font="Consolas", space=2, name="Terminal Text")
box(s, 5.3, 3.72, 4.1, 0.5, "Von unten nach oben lesen: Kriterien stehen vor der Stichprobe im Verlauf.", size=11, color=GREY, name="Terminal Unterschrift")
laien(s, "KI-Ergebnisse erst glauben, wenn jemand sie getrennt geprüft hat.")
fuss(s, "Vier von 27 Einträgen aus docs/ki_irrwege.md (Iterationen 3, 8, 10). Lücke: Leseprotokoll 10b liegt außerhalb des Repos.")

# Folie 11 ------------------------------------------------------------
s = new_slide("Empfehlung und Grenzen",
              "ZEIT 1:30. KERNAUSSAGE: Ampel statt Fazit-Text. GRÜN: Die Liste ist als Ausgangspunkt nutzbar, immer mit Blick in die verlinkte Bekanntmachung: 94,3 % der Zufallslose der Iteration 9 (n = 70) stimmen mit zwei KI-Lesungen überein (Mensch 14 von 15); Merkmal Ende je Los und Grundlaufzeit. Für Betriebe heißt das praktisch: Vertragsenden bei Vergabeweiser nachsehen (kostenlos; Genauigkeit dort nicht von uns belegt; Höchstende/Ende je Verfahren beachten, die Bekanntmachung selbst lesen) und das Enddatum in der Bekanntmachung prüfen, ob Grundlaufzeit oder Höchstende gemeint ist. "
              "GELB: Höchstende nur Hinweis (87,1 %); Abdeckung nur TED, 79,4 % im letzten Jahr (Zuschläge 10/2025 bis 9/2026) und rund 73 % aller Lose (6.803 von 9.325), dazu der Ausblick aus Paket B (rund ein Viertel der Oberpfälzer Reinigungsverfahren im Bekanntmachungsservice nicht auf TED, Hinweis, kein Vorsprung; Erweiterung nur mit belegter Nachfrage); Listenfehler offen (Dauerfeld enthält die Option: 12 von 9.325 Losen; Textmuster „läuft vom … bis … und verlängert sich“); Gespräche n = 3; Leser nicht unabhängig, keine Menschenprüfung der 15 Lose aus 10b. "
              "ROT: Terminprognose (28,8 %); die Liste als eigenes Produkt; „keine Abo-Kosten“ als Vorteil (Eigenbau gegen kostenlose Dienste im Modell nie günstiger, Folge der Modellkonstruktion); Nachfrage, Zahlungsbereitschaft, Relevanz der Datenübergabe und Qualitätsvorsprung nicht belegt. "
              "TRANSFERFRAGE „Würdet ihr das Produkt bauen?“: Nein, nicht als Liste allein. Wenn weiter, dann ein Gespräch mit mehr größeren Betrieben und Vergabestellen, eine menschliche Gegenlesung und ein Maß, das Definition und Losebene trennt. Neuer Standort oder andere Nische: Pipeline übertragbar, Lese-Regeln neu testen. Doppeltes Volumen: Abruf skaliert, die menschliche Prüfung nicht. "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1 (Befüllungsquote 90 %, Laufzeitende bestimmbar); eine Geschäftsbegründung ist nicht belegt. "
              "ZEIG-MIR-WO: docs/annahmen.md, reports/evaluation_iteration9.md, reports/evaluation_iteration10b.md, docs/business.md §8.9.")

ampel = (("Ja", GREEN, ["Vertragsenden als Ausgangspunkt", "Immer den Link zur Bekanntmachung prüfen", "66 von 70 Stichproben stimmen"]),
         ("Mit Vorsicht", AMBER, ["Nur TED-Daten: 79,4 % im letzten Jahr", "Höchstende nur als Hinweis", "Nur 3 Gespräche"]),
         ("Nein", RED, ["Terminprognose (28,8 %)", "Liste als eigenes Produkt", "Nachfrage und Vorsprung nicht belegt"]))
for i, (h, f, pts) in enumerate(ampel):
    x = 0.6 + i * 3.0
    rect(s, x, 1.4, 2.8, 2.8, WHITE, name=h + " Karte")
    kreis(s, x + 0.2, 1.52, 0.4, f, name=h + " Signal")
    box(s, x + 0.75, 1.52, 1.9, 0.4, h, size=16, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 2.1, 2.45, 2.05, pts, size=14, space=8)
laien(s, "Vertragsenden bei Vergabeweiser nachsehen und die Bekanntmachung selbst lesen.")
fuss(s, "Quellen: reports/evaluation_iteration9.md und 10b, docs/business.md §8. Abdeckung: Zuschläge 10/2025 bis 9/2026.")

# Folie 12 ------------------------------------------------------------
s = new_slide("", "ZEIT 0:45. KERNAUSSAGE in einem Satz wiederholen, dann Brücke zur Fragenrunde. Gesamtzeit: 15:00 (Ziel ±30 Sekunden); Zeitbudget je Folie: 0:30 / 3:30 / 1:30 / 1:30 / 1:30 / 2:00 / 0:45 / 1:30 / 1:30 / 0:45 (Business Understanding Folien 3 bis 6: 6:30 = 43 %; Video-Folie 2 inkl. Quiz und Überleitung 3:30). Folien 11 bis 13 sind ausgeblendet (Anhang, nicht in der Zeit). "
              "Satz zum Mitnehmen: Den Termin einer Neuausschreibung sagen TED-Daten nicht vorher; eine Liste der Vertragsenden lässt sich lesen, ist aber kein eigenes Produkt, solange Vergabeweiser sie kostenlos bietet. Lehre: Marktgate in Phase 1, vor der Modellierung. "
              "FRAGENRUNDE vorbereiten: (1) Methodenfrage: warum ±3 Monate, warum diese Baseline, warum KI-Leser als Maß, warum nur diskordante Lose (Folie 5 und ausgeblendete Folien 11 bis 13; im Video Folie 2). Ausgeblendete Folien in der Fragerunde über die Foliensortierung öffnen oder die Ausblendung aufheben. (2) Live-Nachweis: git log und die Reihenfolge der Commits zeigen, Seed und Schlüssel-Hash (Folie 8), Regel in src/prepare/vertragsliste.py öffnen, Fehlwerte (Stufe F) in reports/beispiel_liste_oberpfalz.csv zeigen. "
              "(3) Transferfrage: „Warum nicht Vergabeweiser nutzen?“ (Folie 4), „Warum nicht gleich die Daten von bund.de einbauen?“ (Folie 6), „Was war mit der Null in Paket B?“ (Folie 8), „Warum erst jetzt die Konkurrenz?“ (Folie 8), „Wer zahlt?“ (Folie 3), „Warum ist W8a verfehlt?“ (Folie 5), „Warum selbst bauen statt Vergabeweiser nutzen?“, „Welches Verwaltungssystem haben Betriebe?“, „Wer pflegt das?“, „Warum eine Demo ohne Business Case?“ (Folie 7), „Warum ist die Webseite nur Demo?“ (alle Folie 6; Zeig-mir-wo: docs/prototyp/export/vertragsliste_v1_de.csv), anderer Standort, andere Nische, doppeltes Volumen (Folie 6 und 9), „Wie war das Kriterium, warum ±3 Monate?“ (Video, Anhang Folie 11). Nicht sagen: „genauer als Vergabeweiser“, „Vorsprung belegt“ ohne den Zusatz „auf Los- und Definitionsebene“, „kein Unterschied“.", dark=True)

box(s, 0.6, 0.55, 8.8, 1.8, "Den Termin sagt TED nicht voraus. Das Vertragsende lässt sich lesen, ein eigenes Produkt ist das nicht.", size=30, color=WHITE, font=HEAD, name="Kernsatz")
for i, (z, t, f) in enumerate((("28,8 %", "Terminprognose, gefordert waren 60 %", RED), ("66 von 70", "Vertragsenden stimmen", GREEN), ("0 €", "Vergabeweiser, kostenlos", AMBER))):
    x = 0.6 + i * 3.0
    rect(s, x, 2.5, 2.8, 1.25, RGBColor.from_string("2C2C2E"), name=f"Kachel {i + 1}")
    box(s, x + 0.2, 2.58, 2.4, 0.55, z, size=26, color=f, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.2, 3.15, 2.45, 0.55, t, size=14, color=WHITE)
box(s, 0.6, 4.0, 8.8, 0.35, [[("Lehre: ", {"bold": True, "color": AMBER}), ("vor dem Bauen fragen, ob es das schon gibt.", {"color": WHITE})]], size=16, name="Lehre")
box(s, 0.6, 4.45, 8.8, 0.45, [[("Nächster Schritt: ", {"bold": True, "color": AMBER}), ("menschliche Gegenlesung und mehr Gespräche mit größeren Betrieben.", {"color": SOFT})]], size=14, name="Nächster Schritt")
box(s, 0.6, 4.9, 6.0, 0.45, "Vielen Dank. Fragen?", size=22, color=BLUE, font=HEAD, name="Dank")
s.notes_slide.notes_text_frame.text += " FÜR LAIEN IN EINEM SATZ: Ob ein Vertrag neu ausgeschrieben wird, sagt TED nicht; wann er endet, steht in der Bekanntmachung, und die kostenlose Liste dazu gibt es schon."

# Folie 2 ------------------------------------------------------------
s = new_slide("Frage, Kriterium, Daten",
              "AUSGEBLENDET (Anhang für die Fragerunde; früher Folie 2, im Vortrag ersetzt durch das Video auf Folie 2; Zeit 0:00; das Video deckt Frage, Kriterium und Daten in Kurzform ab). Zeigen bei Fragen zu Kriterium, Schwelle, Datenumfang. KERNAUSSAGE: Die Frage hatte eine Entscheidung (auf welche Ausschreibung bereite ich mich vor?) und eine vorab festgelegte Schwelle. "
              "Zielgruppe: Reinigungsfirmen im Mittelstand, Nische Gebäudereinigung (Haupt-CPV 90910/90911/90919). Annahme: Wer früh weiß, wann ein Vertrag endet, kann Personal und Angebot vorbereiten (A1, A15); diese Annahme war zu diesem Zeitpunkt ungeprüft, ein Kundengespräch gab es nicht. "
              "Erfolgskriterium vor dem Backtest festgelegt (docs/business.md 7.1): Treffer = Neuausschreibung im Fenster ±3 Monate um die Prognose, Schwelle 60 %; Baseline R0 = naive Regel 17,3 %. "
              "Daten: TED Search API, eForms-Zuschläge ab Okt. 2023, Rohdaten unverändert in data/raw (nicht im Git, Abruf-Skript in docs/reproduzierbarkeit.md). 9.325 Lose aus 4.011 Zuschlägen (alle eForms-Zuschläge ab Okt. 2023), im Richtwert von 200 bis 10.000 Zeilen. Die Quellenzeile „Q4 2025 bis Q3 2026“ gehört nur zu den 79,4 % Abdeckung im letzten Jahr, nicht zu den 9.325 Losen. "
              "Laufzeitende bei 90,0 % der Zuschläge bestimmbar; Verlängerungsoptionen nur bei 18,9 % im Feld BT-58, der Rest im Freitext. "
              "Streifen unten: vier Zyklen CRISP-DM, jeder endete mit einer Entscheidung gegen vorab festgelegte Schwellen. Zyklus 4 ist der Rücksprung in Phase 1; er bekommt in diesem Vortrag den größten Teil der Zeit (Folien 3 bis 6, 6:30 von 15:00). "
              "FRAGE – ANTWORT: „Warum Gebäudereinigung?“ Nische aus Iteration 1: Befüllungsquote etwa 90 %, Laufzeitende bestimmbar, Haupt-CPV klar abgrenzbar. Eine Geschäftsbegründung ist das nicht; sie wurde nicht belegt. "
              "ZEIG-MIR-WO: docs/business.md Abschnitt 7.1, reports/datenqualitaet_DEU_20260722_20261021.md, docs/quellen.md.")

box(s, 0.6, 1.4, 8.8, 0.95, "Reinigungsfirmen erfahren oft spät, wann ein öffentlicher Vertrag endet. Unsere Idee: Das aus Daten von TED vorhersagen, der EU-Plattform für öffentliche Ausschreibungen.", size=16, name="Idee")
tile(s, 0.6, 2.5, 2.8, 1.7, "60 %", "Mindest-Trefferquote, vorab festgelegt (Termin auf ±3 Monate genau)", BLUE, "Schwelle")
tile(s, 3.6, 2.5, 2.8, 1.7, "17,3 %", "so viel schafft eine einfache Faustregel zum Vergleich", GREY, "Faustregel")
tile(s, 6.6, 2.5, 2.8, 1.7, "9.325", "Lose (Teilaufträge) aus 4.011 Zuschlägen seit Okt. 2023", BLUE, "Daten")
laien(s, "Wer früh Bescheid weiß, kann Personal und Angebot besser planen (Annahme, ungeprüft).")
fuss(s, "Quelle: TED Search API v3 (docs/quellen.md). 9.325 Lose = alle eForms-Zuschläge der Gebäudereinigung ab Okt. 2023.")

# Folie 3 ------------------------------------------------------------
s = new_slide("Irrwege: Zuordnung, Terminprognose",
              "AUSGEBLENDET (Anhang für die Fragerunde; früher Folie 3, im Video Runde 1 und 2; Zeit 0:00). KERNAUSSAGE: Zwei Ideen sind an vorab festgelegten Schwellen gescheitert, und das haben wir so berichtet. "
              "IRRWEG 1 (Iteration 2 bis 4): Jede Neuausschreibung dem Vorgängervertrag zuordnen. Auftraggeber + CPV 16,7 % (Schwelle 80 %), weil große Auftraggeber viele Verträge parallel vergeben; Objekt-Regel (Adresse, Titel) 28,9 % (Schwelle 60 %); letzter Versuch auf neuen Testdaten 56,7 % (Schwelle 60 %), die Zweitprüfung durch den Nutzer 65 %. Auf Entwicklungsdaten hielt Claude 10–11 von 12 Vorschlägen für plausibel, im Test waren 11 von 24 richtig. "
              "IRRWEG 2 (Iteration 5, Backtest): R1 = Höchstende − 6 Monate auf 52 von Hand bestätigten Paaren: 28,8 %; R0 17,3 %; Schwelle 60 %. 20 Neuausschreibungen kamen mehr als 3 Monate früher, 15 im Fenster, 17 später. Entscheidung: Idee anpassen, keine Terminprognose. Grenzen: Paare aus einer Rückwärtssuche (nur auffindbare Vorgänger), Zweitprüfung KI-unterstützt. "
              "OPTIONALE BACKTEST-FRAGE (nur wenn Zeit, sonst weglassen; die Publikumsfrage des Vortrags steht auf Folie 3): „Wie oft trifft ‚Höchstende − 6 Monate‘ den Termin im Fenster ±3 Monate?“ Antwort: 28,8 %. "
              "FRAGE – ANTWORT: „Warum ±3 Monate, warum diese Baseline?“ Das Fenster wurde vor der Rechnung gesetzt, weil ein Betrieb für Personal und Angebot grob ein Vierteljahr Spielraum braucht; die naive Regel R0 zeigt, was Zufall und Streuung allein schaffen; die Schwelle 60 % war eine Setzung ohne Kundenkontakt. Ein Fenster ±6 Monate wäre für die Entscheidung zu unscharf. "
              "ZEIG-MIR-WO: reports/zuordnung_iteration3.md, reports/evaluation_iteration4.md, reports/backtest_iteration5.md, reports/evaluation_iteration5.md.")

rect(s, 0.6, 1.4, 5.3, 2.8, WHITE, name="Chart Karte")
box(s, 0.8, 1.5, 5.0, 0.3, "Trefferquote unserer Versuche", size=14, bold=True, color=GREY)
balken(s, 0.7, 1.8, 5.1, 2.35, ["Zuordnung, Versuch 1", "Zuordnung, Versuch 2", "Zuordnung, Versuch 3", "Termin-Vorhersage"],
       [16.7, 28.9, 56.7, 28.8], [RED, RED, AMBER, RED], "Trefferquote gegen Schwelle", maximum=85)
rect(s, 6.1, 1.4, 3.3, 2.8, WHITE, name="Ergebnis Karte")
box(s, 6.3, 1.5, 2.9, 2.6, [[("Gefordert war", {"color": GREY, "bold": True})], [("80 % / 60 % / 60 % / 60 %", {"size": 16, "bold": True})],
    [("Alle vier Versuche verfehlt.", {"bold": True, "color": RED})], "Neuer Plan: nicht der Termin, sondern eine Liste der Vertragsenden."], size=14, space=8, name="Ergebnis Text")
laien(s, "Niemand kann Ihnen aus TED sagen, wann genau Ihr Vertrag neu ausgeschrieben wird.")
fuss(s, "Zuordnung = eine Neuausschreibung dem alten Vertrag zuordnen. Termin-Vorhersage: Höchstende minus 6 Monate, 52 geprüfte Paare. Schwellen vorab festgelegt.")

# Folie 4 ------------------------------------------------------------
s = new_slide("Die Liste und ihre Genauigkeit",
              "AUSGEBLENDET (Anhang für die Fragerunde; früher Folie 4, im Video Runde 3; Zeit 0:00). KERNAUSSAGE: Aus dem Rückschlag wird eine andere Frage: nicht „wann wird neu ausgeschrieben?“, sondern „wann endet ein Vertrag laut Bekanntmachung?“. Vier Messungen messen vier verschiedene Dinge (n = 60, 47, 80, 70), sie sind kein Trend; keine ist eine belastbare Fehlerquote. "
              "Die Liste (Fassung der Iteration 9) hat 9.325 Lose; je Los das Ende der Grundlaufzeit, das Höchstende nur als Hinweis, Auftraggeber, TED-Link und eine Stufe A bis F (woher die Angabe stammt). Ein Datum liefert sie für 79,4 % der Lose im letzten Jahr (Zuschläge 10/2025 bis 9/2026: 2.783 von 3.503; Schwelle 80 % knapp verfehlt) und für rund 73 % aller Lose (6.803 von 9.325); die beiden Zahlen gelten für verschiedene Zeiträume. Prototyp Oberpfalz: 130 Lose, davon 33 ohne Ende (Stufe F, keine Laufzeitfelder im XML). "
              "Iteration 6: Handprüfung von 60 Zufallslosen, aber die Vorlage zeigte den Listenwert (Verankerung): 88,3 %. Iteration 7: Handprüfung ohne Listenwerte, Nachprüfung im Original: 76,6 %, ein Mischmaß aus Listen- und Prüfungsfehlern. "
              "Iteration 8: zwei KI-Leser (Opus, Sonnet) auf allen 95 Losen: 77 von 80 = 96,2 %, Leser nicht unabhängig. Iteration 9: neue Stichprobe (Seed 20261109), Rohtext ohne Projektkontext, überarbeitete Liste: 66 von 70 = 94,3 % (n = 70, Wilson 86–98 %), Kommilitone 14 von 15; Höchstende 87,1 % (Schwelle 90 % verfehlt). "
              "Die alte Fassung der Liste erreicht auf denselben Losen 65 von 70: Der Nutzen der neuen Regeln ist kaum gesichert. "
              "FRAGE – ANTWORT: „Warum Übereinstimmung mit KI-Lesern als Maß, was wäre die Alternative?“ Es gibt keine Wahrheitsquelle außer dem Bekanntmachungstext; Handprüfung ist teuer und hatte Verankerung (It. 6) und Abschreibefehler (It. 7), deshalb zusätzlich KI-Leser mit neutraler Definition „erste feste Laufzeit ohne Optionen“. Alternative: mehr Menschen als Leser; fehlt noch. "
              "FRAGE – ANTWORT: „Was brachten Iteration 6 bis 9?“ Eine Basisregel (Feld EndDate) trifft 63 von 70; die Fassung mit den Regeln 6 bis 10 trifft 66 von 70 (alte Fassung 65): ein kleiner, kaum gesicherter Zugewinn, dafür bekannte Fehlerarten behoben und Lose ohne Zuschlag entfernt (590). "
              "ZEIG-MIR-WO: reports/beispiel_liste.md, reports/beispiel_liste_oberpfalz.csv, reports/evaluation_iteration6.md bis 9.")

rect(s, 0.6, 1.4, 8.8, 1.3, WHITE, name="Zeitstrahl Karte")
rect(s, 0.9, 1.55, 4.4, 0.4, BLUE, name="Grundlaufzeit")
box(s, 0.9, 1.55, 4.4, 0.4, "feste Laufzeit (Grundlaufzeit)", size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, 5.35, 1.55, 3.4, 0.4, LBLUE, name="Verlängerung")
box(s, 5.35, 1.55, 3.4, 0.4, "mögliche Verlängerung", size=14, color=DBLUE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, 5.18, 2.03, 0.2, 0.16, BLUE, MSO_SHAPE.ISOSCELES_TRIANGLE, "Marke Grundlaufzeit")
rect(s, 8.65, 2.03, 0.2, 0.16, GREY, MSO_SHAPE.ISOSCELES_TRIANGLE, "Marke Höchstende")
box(s, 0.9, 2.22, 4.4, 0.5, "Ende der Grundlaufzeit: steht in unserer Liste", size=14, bold=True, color=BLUE, align=PP_ALIGN.RIGHT)
box(s, 5.5, 2.22, 3.4, 0.5, "Höchstende: nur Hinweis", size=14, color=GREY, align=PP_ALIGN.RIGHT)
tile(s, 0.6, 2.8, 2.8, 1.4, "66 von 70", "Stichproben stimmen mit zwei KI-Lesern überein", GREEN, "Genauigkeit", zsize=26)
tile(s, 3.6, 2.8, 2.8, 1.4, "9.325", "Lose in der Liste", BLUE, "Lose", zsize=26)
tile(s, 6.6, 2.8, 2.8, 1.4, "79,4 %", "der Lose im letzten Jahr haben ein Enddatum", BLUE, "Abdeckung", zsize=26)
laien(s, "Die Liste nennt je Vertrag das Ende der festen Laufzeit, mit Link zur Bekanntmachung.")
fuss(s, "94,3 % von n = 70 Zufallslosen (Schwelle 90 %); Kommilitone 14 von 15; Leser nicht unabhängig, nicht alle Fehler bekannt. 79,4 %: Zuschläge 10/2025 bis 9/2026, nur TED.")

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if args:   # optional: anderer Ausgabepfad (z. B. wenn die Datei in PowerPoint geöffnet ist)
    OUT = Path(args[0])

# Folien 11 bis 13: ausgeblendeter Anhang für die Fragerunde (ob ausgeblendete Folien bei „höchstens 12“ zählen, mit dem Dozenten klären)
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
