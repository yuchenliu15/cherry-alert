from playwright.sync_api import sync_playwright

CHERRY_URL = "https://www.bbg.org/collections/cherries"
OUTPUT_IMAGE = "cherries.png"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(CHERRY_URL)
    page.wait_for_load_state("networkidle")
    page.locator("#cherrymap").screenshot(path=OUTPUT_IMAGE )
    browser.close()
