from playwright.sync_api import sync_playwright

def test_login_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)

        context = browser.new_context()

        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        page.get_by_label("username").fill("tomsmith")
        page.get_by_label("password").fill("SuperSecretPassword!")
        page.get_by_role("button").click()
        print(page.locator(".flash"))
        page.screenshot(path="./login_success.png")

        browser.close()