"""Bilder für das Lab-Log: Screenshots (Hell-Modus) der Webseite, der Demos und eines Video-Standbilds.

Aufruf (eigene venv mit Playwright, installiertes Edge):
    .venv-video\\Scripts\\python.exe -I src\\report\\lab_log_bilder.py      Ausgabe: docs/lab_log_bilder/*.png
Es wird nichts geladen oder gesendet; alle Seiten liegen lokal im Repo.
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "docs" / "lab_log_bilder"
OUT.mkdir(exist_ok=True)
B, H = 780, 540  # Bildausschnitt in Pixeln (später im PDF klein gesetzt)


def main() -> None:
    with sync_playwright() as pw:
        br = pw.chromium.launch(channel="msedge", headless=True)
        ctx = br.new_context(viewport={"width": B, "height": H}, color_scheme="light")
        pg = ctx.new_page()

        def shot(url: str, name: str, scroll: int = 0, warte: int = 800, sel: str | None = None) -> None:
            pg.goto("about:blank")
            pg.goto(url)
            pg.wait_for_timeout(warte)
            if sel:
                pg.locator(sel).first.scroll_into_view_if_needed()
            elif scroll:
                pg.evaluate("y=>window.scrollTo(0,y)", scroll)
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / name))
            print(name)

        web = (ROOT / "docs/prototyp/vertragsliste.html").as_uri()
        shot(web + "#theme=light", "webseite_1.png")
        shot(web + "#theme=light", "webseite_2.png", scroll=520)

        push = (ROOT / "docs/demo/push_demo.html").as_uri()
        shot(push, "push_demo_1.png")
        shot(push, "push_demo_2.png", scroll=650)

        live = (ROOT / "docs/demo/live_demo.html").as_uri()
        par = "#set=bayern&sitz=DE235&radius=50&lz=12&fenster=12m&theme=light&run=1"
        shot(live + par + "&anim=3300", "live_demo_1.png", sel="#schritt2")
        pg.goto("about:blank")
        pg.goto(live + par)  # Seite neu laden, damit der Filterlauf wirklich neu startet
        pg.wait_for_timeout(11000)  # Filterlauf dauert rund 8 s
        pg.locator("#treffer").scroll_into_view_if_needed()
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT / "live_demo_2.png"))
        print("live_demo_2.png")

        v = br.new_context(viewport={"width": 1280, "height": 720}).new_page()
        v.goto((ROOT / "docs/video/franz_und_die_glaskugel.html").as_uri() + "?render")
        v.wait_for_function("typeof window.render === 'function'")
        v.evaluate("t=>window.render(t)", 171.0)
        v.wait_for_timeout(500)
        v.screenshot(path=str(OUT / "video_standbild.png"))
        print("video_standbild.png")
        br.close()


if __name__ == "__main__":
    main()
