from pages.register_page import RegisterPage
from pages.locators import LinksLocators
import pytest


@pytest.mark.critical_check
def test_registration(browser):
    register_page = RegisterPage(browser, LinksLocators.REGISTER_LINK)
    register_page.open()
    register_page.should_be_register_form()
    user_data = register_page.create_user_data()
    register_page.register_new_user(user_data)
    register_page.should_be_success_message()


