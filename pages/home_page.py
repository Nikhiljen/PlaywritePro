import re

from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.whishlist_page import WishlistPage


class HomePage(BasePage):
    def __init__(self,page : Page):
        super().__init__(page)

        # Locator
        self.register_link = page.get_by_role("link",name="Register")
        self.login_link = page.get_by_role("link",name="Log in")
        self.shopping_cart = page.locator("#topcartlink")
        self.wishlist = page.get_by_role("link",name="Wishlist")

        self.search_box = page.locator("#small-searchterms")
        self.search_button = page.locator("input[type='submit']")


    def open_register(self) -> RegisterPage:
        self.register_link.click()
        return RegisterPage(self.page)

    def open_login(self) -> LoginPage:
        self.login_link.click()
        return LoginPage(self.page)

    def open_shopping_cart(self) -> ShoppingCartPage:
        self.shopping_cart.click()
        return ShoppingCartPage(self.page)

    def open_wishlist(self) -> WishlistPage:
        self.wishlist.click()
        return WishlistPage(self.page)

    def get_shopcart_value(self) -> int:
        cart_value = self.shopping_cart.filter(has=self.page.locator(".cart-qty")).inner_text()
        return int(re.search(r"\d+",cart_value).group())
