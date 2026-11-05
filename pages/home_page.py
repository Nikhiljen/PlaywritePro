from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class HomePage(BasePage):
    def __init__(self,page : Page):
        super().__init__(page)

        # Locator

        self.logo = page.get_by_alt_text("Tricentis Demo Web Shop")
        self.register_link = page.get_by_role("link",name="Register")
        self.login_link = page.get_by_role("link",name="Log in")
        self.shopping_cart = page.get_by_role("link",name="Shopping cart")
        self.wishlist = page.get_by_role("link",name="Wishlist")

        self.search_box = page.locator("#small-searchterms")
        self.search_button = page.locator("input[type='submit']")


    def open_register(self) -> RegisterPage:
        self.register_link.click()
        return RegisterPage(self.page)

    def open_login(self) -> LoginPage:
        self.login_link.click()
        return LoginPage(self.page)