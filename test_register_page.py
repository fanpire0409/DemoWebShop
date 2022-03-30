from pages.register_page import RegisterPage
import pytest


@pytest.mark.critical_check
def test_registration(browser):
    register_link = "http://demowebshop.tricentis.com/register"
    register_page = RegisterPage(browser, register_link)
    register_page.open()
    register_page.should_be_register_form()
    user_data = register_page.create_user_data()
    register_page.register_new_user(user_data)
    register_page.should_be_success_message()


