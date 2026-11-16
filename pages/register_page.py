from typing import Optional

from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.register_result_page import RegisterResultPage


class RegisterPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        # Locator for register Page
        self.heading = page.get_by_role('heading',name = 'Register',exact=True)
        self.male_gender = page.locator("#gender-male")
        self.first_name = page.locator("#FirstName")
        self.last_name = page.locator("#LastName")
        self.email = page.locator("#Email")
        self.password = page.locator("#Password")
        self.confirm_password = page.locator("#ConfirmPassword")
        self.register_button = page.locator("#register-button")

    def register(self, first_name: str = "", last_name: str = "", email: str = "",
                 password: str = "", confirm_password: Optional[str] = None) -> None:
        """Fill the whole form and submit. Any argument can be wrong or empty."""
        if confirm_password is None:
            confirm_password = password          # same as password unless a test overrides it
        self.male_gender.check()
        self.fill_input(self.first_name, first_name)
        self.fill_input(self.last_name, last_name)
        self.fill_input(self.email, email)
        self.fill_input(self.password, password)
        self.fill_input(self.confirm_password, confirm_password)
        self.click_on_button(self.register_button)

    def to_result_page(self) -> RegisterResultPage:
        """Call this only when registration is expected to succeed."""
        return RegisterResultPage(self.page)