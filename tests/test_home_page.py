from config.config_reader import URL
from tests.BaseTest import BaseTest


class TestHomePage(BaseTest):
    def test_home_page_title(self):
        title = self.home_page.get_home_page_title()
        assert title == "Demo Web Shop","Page is not Loaded properly"

    def test_home_page_load(self):
        url = self.home_page.get_home_page_url()
        assert url == URL,"Home Page is not loaded Successfully"

    def test_home_page_logo(self):
        assert self.home_page.is_logo_present() is True, "logo not present on home page"

    def test_register_link_visible(self):
        title = self.home_page.get_home_page_title()
