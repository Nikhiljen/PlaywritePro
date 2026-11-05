import logging
from operator import truediv

import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from config.config_reader import BROWSER, HEADLESS

log = logging.getLogger(__name__)
ARTIFACTS = Path("reports/artifacts")

def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default=BROWSER,choices=["chromium", "firefox", "webkit"])
    parser.addoption("--headless", default = str(HEADLESS).lower(), choices=["true", "false"])

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}",report)

# Open Play write
@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser_instance(pw,request):
    name = request.config.getoption("--browser-name")
    headless = request.config.getoption("--headless") == "true"
    browser = getattr(pw, name).launch(headless=headless)
    log.info("Launched %s (headless=%s)", name, headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context_instance(browser_instance):
    ctx = browser_instance.new_context(viewport={"width": 1440, "height": 900})
    yield ctx
    ctx.close()

@pytest.fixture(scope="function")
def page(context_instance,request):
    context_instance.tracing.start(
        screenshots = True,
        snapshots = True,
        sources = True

    )
    page = context_instance.new_page()
    yield page
    page.close()

    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    name = request.node.name
    if failed:
        page.screenshot(path=ARTIFACTS / f"{name}.png")
        context_instance.tracing.stop(path=ARTIFACTS / f"{name}.zip")
        log.error("FAILED: %s -> screenshot + trace saved", name)
    else:
        context_instance.tracing.stop()
    page.close()
