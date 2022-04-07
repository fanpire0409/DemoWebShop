from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.locators import LinksLocators
import pytest


@pytest.mark.critical_check
class TestLinks():
    def test_register_link(self, browser):
        cart_page = CartPage(browser, LinksLocators.CART_LINK)
        cart_page.open()
        cart_page.should_be_register_link()
        cart_page.follow_the_register_link()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_url()

    def test_log_in_link(self, browser):
        cart_page = CartPage(browser, LinksLocators.CART_LINK)
        cart_page.open()
        cart_page.should_be_log_in_link()
        cart_page.follow_the_log_in_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_log_in_url()


@pytest.mark.critical_check2
class TestGuest():
    def test_guest_changing_product_quantity_in_cart(self, browser):
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.follow_the_cart_link()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_cart_url()
        cart_page.change_the_quantity_of_goods()
        cart_page.check_change_the_quality()
        cart_page.check_coast()


@pytest.mark.critical_check2
class TestUser():
    def test_user_changing_product_quantity_in_cart(self, browser):
        register_page = RegisterPage(browser, LinksLocators.REGISTER_LINK)
        register_page.open()
        user_data = register_page.create_user_data()
        register_page.register_new_user(user_data)
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.follow_the_cart_link()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_cart_url()
        cart_page.change_the_quantity_of_goods()
        cart_page.check_change_the_quality()
        cart_page.check_coast()
