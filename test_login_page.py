from pages.login_page import LoginPage
from pages.locators import LinksLocators
import pytest


@pytest.mark.critical_check
def test_log_in(browser):
    log_in_page = LoginPage(browser, LinksLocators.REGISTER_LINK)
    log_in_page.open()
    user_data = log_in_page.create_user_data()
    log_in_page.register_new_user(user_data)
    log_in_page.follow_the_log_out_link()
    log_in_page.follow_the_log_in_link()
    log_in_page.returning_customer(user_data)
    log_in_page.check_user_log_in()
