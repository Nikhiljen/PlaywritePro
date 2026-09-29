import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from config.config_reader import URL


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self,page):
        self.page = page
        self.home_page = HomePage(self.page)
        print("Navigate to the home page of application")
        self.home_page.navigate(URL)
