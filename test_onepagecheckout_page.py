from pages.onepagecheckout_page import OnePageCheckoutPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.locators import LinksLocators
import pytest


@pytest.mark.critical_check
class TestLinks():
    def test_register_link(self, browser):
        order_page = OnePageCheckoutPage(browser, LinksLocators.ORDER_LINK)
        order_page.open()
        order_page.should_be_register_link()
        order_page.follow_the_register_link()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_url()

    def test_log_in_link(self, browser):
        order_page = OnePageCheckoutPage(browser, LinksLocators.ORDER_LINK)
        order_page.open()
        order_page.should_be_log_in_link()
        order_page.follow_the_log_in_link()
        product_page = LoginPage(browser, browser.current_url)
        product_page.should_be_log_in_url()


@pytest.mark.smoke_test
class TestUser():
    # specify_the_address(user_data=None, address=None)
    def test_order_with_pre_authorization(self, browser):
        register_page = RegisterPage(browser, LinksLocators.MAIN_LINK)
        register_page.open()
        register_page.follow_the_register_link()
        user_data = register_page.create_user_data()
        register_page.register_new_user(user_data)
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.follow_the_cart_link_after_added_product()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.go_to_one_page_checkout()
        order_page = OnePageCheckoutPage(browser, browser.current_url)
        address = order_page.create_user_address()
        order_page.specify_the_address(address=address)
        order_page.choice_of_delivery_address()
        order_page.choice_of_pay_method()
        order_page.read_payment_information()
        order_page.confirm_the_order()

    def test_order_with_authorization_in_progress(self, browser):
        register_page = RegisterPage(browser, LinksLocators.REGISTER_LINK)
        register_page.open()
        user_data = register_page.create_user_data()
        register_page.register_new_user(user_data)
        register_page.follow_the_log_out_link()
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.follow_the_cart_link_after_added_product()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.go_to_one_page_checkout()
        main_page = LoginPage(browser, browser.current_url)
        main_page.returning_customer(user_data)
        cart_page.go_to_one_page_checkout()
        order_page = OnePageCheckoutPage(browser, browser.current_url)
        address = order_page.create_user_address()
        order_page.specify_the_address(address=address)
        order_page.choice_of_delivery_address()
        order_page.choice_of_pay_method()
        order_page.read_payment_information()
        order_page.confirm_the_order()


@pytest.mark.smoke_test
class TestGuest():
    # specify_the_address(user_data=None, address=None)
    def test_order_with_registration_in_progress(self, browser):
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.follow_the_cart_link_after_added_product()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.go_to_one_page_checkout()
        main_page = LoginPage(browser, browser.current_url)
        main_page.go_to_registration_by_button()
        register_page = RegisterPage(browser, browser.current_url)
        user_data = register_page.create_user_data()
        register_page.register_new_user(user_data)
        register_page.completion_of_registration()
        cart_page.go_to_one_page_checkout()
        order_page = OnePageCheckoutPage(browser, browser.current_url)
        address = order_page.create_user_address()
        order_page.specify_the_address(address=address)
        order_page.choice_of_delivery_address()
        order_page.choice_of_pay_method()
        order_page.read_payment_information()
        order_page.confirm_the_order()

    def test_order_without_registration(self, browser):
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.follow_the_cart_link_after_added_product()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.go_to_one_page_checkout()
        main_page = LoginPage(browser, browser.current_url)
        main_page.checkout_as_guest()
        register_page = RegisterPage(browser, browser.current_url)
        user_data = register_page.create_user_data()
        order_page = OnePageCheckoutPage(browser, browser.current_url)
        address = order_page.create_user_address()
        order_page.specify_the_address(user_data=user_data, address=address)
        order_page.choice_of_delivery_address()
        order_page.choice_of_pay_method()
        order_page.read_payment_information()
        order_page.confirm_the_order()
