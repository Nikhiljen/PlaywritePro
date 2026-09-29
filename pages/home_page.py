from playwright.sync_api import Page

from pages.base_page import BasePage


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

