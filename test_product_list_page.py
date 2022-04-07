from pages.product_list_page import ProductListPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.locators import LinksLocators
import pytest


@pytest.mark.critical_check
class TestLinks():
    def test_register_link(self, browser):
        product_page = ProductListPage(browser, LinksLocators.PRODUCT_LIST_LINK)
        product_page.open()
        product_page.should_be_register_link()
        product_page.follow_the_register_link()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_url()

    def test_log_in_link(self, browser):
        product_page = ProductListPage(browser, LinksLocators.PRODUCT_LIST_LINK)
        product_page.open()
        product_page.should_be_log_in_link()
        product_page.follow_the_log_in_link()
        product_page = LoginPage(browser, browser.current_url)
        product_page.should_be_log_in_url()


@pytest.mark.critical_check2
class TestGuest():
    def test_guest_add_to_cart(self, browser):
        product_list_page = ProductListPage(browser, LinksLocators.PRODUCT_LIST_LINK)
        product_list_page.open()
        product_list_page.add_to_cart()
        product_list_page.check_add_to_cart()


@pytest.mark.critical_check2
class TestUser():
    def test_user_add_to_cart(self, browser):
        register_page = RegisterPage(browser, LinksLocators.REGISTER_LINK)
        register_page.open()
        user_data = register_page.create_user_data()
        register_page.register_new_user(user_data)
        product_page = ProductListPage(browser, LinksLocators.PRODUCT_LIST_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.check_add_to_cart()
