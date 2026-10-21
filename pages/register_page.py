from playwright.sync_api import Page

from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        # Locator for register Page
        self.male_gender = page.locator("#gender-male")
        self.first_name = page.locator("#FirstName")
        self.last_name = page.locator("#LastName")
        self.email = page.locator("#Email")
        self.password = page.get_by_role("input",name="Password")
        self.confirm_password = page.get_by_role("input",name="ConfirmPassword")
        self.register_button = page.get_by_role("input",name="register-button")

    def select_gender_field(self):
        self.click_on_button(self.male_gender)

    def fill_first_name_field(self,first_name):
        self.fill_input(self.first_name,first_name)

    def fill_last_name_field(self,last_name):
        self.fill_input(self.last_name,last_name)

    def fill_email_field(self,email):
        self.fill_input(self.email,email)

    def fill_password_field(self,password):
        self.fill_input(self.password,password)

    def fill_confirm_password_fill(self,confirm_password):
        self.fill_input(self.confirm_password,confirm_password)

    def click_on_register_button(self):
        self.click_on_button(self.register_button)