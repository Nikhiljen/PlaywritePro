from playwright.sync_api import sync_playwright,expect

def test_auto_wait():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
        page.get_by_role("button").click()
        text = page.locator("#finish h4")
        expect(text).to_be_visible(timeout=10000)
        print(text.inner_text())
        browser.close()