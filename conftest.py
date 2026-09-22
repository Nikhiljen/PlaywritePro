import pytest
from playwright.sync_api import sync_playwright
from config.config_reader import BROWSER,HEADLESS

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        print("Playwright engine initialized")
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    print("Creating new browser session for test")

    if BROWSER.lower() == "chromium":
        browser = playwright.chromium.launch(headless=HEADLESS)

    elif BROWSER.lower() == "firefox":
        browser = playwright.firefox.launch(headless=HEADLESS)

    elif BROWSER.lower() == "webkit":
        browser = playwright.webkit.launch(headless=HEADLESS)

    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    yield browser

    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    print("Creating new context for browser")
    context = browser.new_context()

    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    print("Creating new page for test")
    page = context.new_page()

    yield page

    page.close()