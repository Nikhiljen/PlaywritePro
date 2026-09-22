# Assignment
#
# Automate the login page again, but this time:
#
# Open https://the-internet.herokuapp.com/login.
# Enter valid credentials.
# Click Login.
# Verify:
# The URL contains /secure.
# The success message is visible.
# The Logout button is visible.
# Click Logout.
# Verify that you're back on the login page.
import re

from playwright.sync_api import sync_playwright, expect


def test_assignment_1():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        page.get_by_label("username").fill("tomsmith")
        page.get_by_label("password").fill("SuperSecretPassword!")
        page.get_by_role("button").click()

        expect(page).to_have_url(re.compile(r".*/secure.*"))
        expect(page.locator(".flash")).to_be_visible()
        expect(page.locator("//a[@href='/logout']")).to_be_visible()

        page.locator("//a[@href='/logout']").click()
        expect(page.get_by_text("Login Page")).to_be_visible()

        # closed Browser

        browser.close()