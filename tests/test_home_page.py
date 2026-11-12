import pytest
from playwright.sync_api import expect

from config.config_reader import URL
from tests.base_test import BaseTest


class TestHomePage(BaseTest):
    @pytest.mark.smoke
    def test_home_page_title(self):
        expect(self.page).to_have_title("Demo Web Shop")

    @pytest.mark.smoke
    def test_home_page_load(self):
        expect(self.page).to_have_url(URL)

    @pytest.mark.smoke
    def test_home_page_logo(self):
        expect(self.home_page.logo).to_be_visible()

    @pytest.mark.smoke
    def test_register_link_visible_and_enabled(self):
        expect(self.home_page.register_link).to_be_visible()

    @pytest.mark.smoke
    def test_login_link_visible_and_enabled(self):
        expect(self.home_page.login_link).to_be_visible()



