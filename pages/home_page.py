from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class HomePage(BasePage):
    def __init__(self,page : Page):
        super().__init__(page)

        # Locator

        self.logo = page.locator("//img[@alt='Tricentis Demo Web Shop']")
        self.register_link = page.get_by_role("'link",name="Register")
        self.login_link = page.get_by_role("'link",name="Log in")
        self.shopping_cart = page.get_by_role("'link",name="Shopping cart")
        self.wishlist = page.get_by_role("'link",name="Wishlist")

        self.search_box = page.locator("#small-searchterms")
        self.search_button = page.locator("input[type='submit']")

    def get_home_page_url(self):
        return self.get_url()

    def is_logo_present(self) -> bool:
        return self.is_visible(self.logo)

    def get_home_page_title(self) -> str:
        return self.get_title()

    def is_register_link_ready(self) -> bool:
        return self.is_visible(self.register_link) and self.is_enabled(self.register_link)

    def is_login_link_ready(self) -> bool:
        return self.is_visible(self.login_link) and self.is_enabled(self.login_link)

    def click_on_register_link(self) -> RegisterPage:
        self.register_link.click()
        return RegisterPage(self.page)

    def click_on_login_link(self) -> LoginPage:
        self.login_link.click()
        return LoginPage(self.page)