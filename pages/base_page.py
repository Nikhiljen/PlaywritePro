from playwright.sync_api import Page


class BasePage:
    def __init__(self, page : Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title

    def refresh_page(self):
        self.page.reload()

    def go_back(self):
        self.page.go_back()

    def wait_for_load(self):
        self.page.wait_for_load_state()

    def take_screenshot(self, path: str):
        self.page.screenshot(path=path)