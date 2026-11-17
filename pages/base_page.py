from playwright.sync_api import Page, Locator
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from pages.home_page import HomePage

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.get_by_alt_text("Tricentis Demo Web Shop")

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def screenshot(self, path: str) -> None:
        self.page.screenshot(path=path)

    def clicked_logo(self) -> HomePage:
        from pages.home_page import HomePage
        self.logo.click()
        return HomePage(self.page)