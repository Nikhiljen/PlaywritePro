import re

import pytest
from playwright.sync_api import expect

from pages.register_page import RegisterPage
from tests.base_test import BaseTest


class TestNavigation(BaseTest):
    @pytest.mark.smoke
    def test_navigation_to_register_page(self):
        register_page = self.home_page.open_register()
        expect(self.page).to_have_url(re.compile("register"))
        expect(register_page.heading).to_be_visible()

    @pytest.mark.smoke
    def test_navigation_to_login_page(self):
        register_page = self.home_page.open_register()
        expect(self.page).to_have_url(re.compile("register"))
        expect(register_page.heading).to_be_visible()