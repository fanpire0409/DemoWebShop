from pages.customer_page import CustomerPage
import time
import pytest


@pytest.mark.critical_check
def test_change_password(browser):
    register_link = "http://demowebshop.tricentis.com/register"
    customer_page = CustomerPage(browser, register_link)
    customer_page.open()
    user_data = customer_page.create_user_data()
    customer_page.register_new_user(user_data)
    customer_page.follow_the_customer_link()
    customer_page.go_to_the_password_change_section()
    customer_page.check_change_password_url()
    customer_page.change_password(user_data['password'], str(time.time()))
    customer_page.check_success_message_change_password()
