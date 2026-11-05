from playwright.sync_api import Page

from pages.base_page import BasePage


class RegisterResultPage(BasePage):
    def __init__(self,page : Page):
        super().__init__(page)

        # Locator
        registration_success_message = page.get_by_text("Your registration completed")
        continue_button = page.locator("//input[@value='Continue']")

    def clickOnContinue(self):
        pass