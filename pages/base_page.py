from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def screenshot(self, path: str) -> None:
        self.page.screenshot(path=path)