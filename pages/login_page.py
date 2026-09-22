from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)
        self.username = page.get_by_label('Username')
        self.password = page.get_by_label('Password')
        self.login_button = page.get_by_label('Log In')


    def login(self,username : str, password : str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()