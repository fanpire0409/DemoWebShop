from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.locators import LinksLocators
import pytest


@pytest.mark.critical_check
class TestLink():
    def test_register_link(self, browser):
        main_page = MainPage(browser, LinksLocators.MAIN_LINK)
        main_page.open()
        main_page.should_be_register_link()
        main_page.follow_the_register_link()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_url()

    def test_log_in_link(self, browser):
        main_page = MainPage(browser, LinksLocators.MAIN_LINK)
        main_page.open()
        main_page.should_be_log_in_link()
        main_page.follow_the_log_in_link()
        log_in_page = LoginPage(browser, browser.current_url)
        log_in_page.should_be_log_in_url()
