from pages.login_page import LoginPage

def test_log_in(browser):
    register_link = "http://demowebshop.tricentis.com/register"
    log_in_page = LoginPage(browser, register_link)
    log_in_page.open()
    user_data = log_in_page.create_user_data()
    log_in_page.register_new_user(user_data)
    log_in_page.follow_the_log_out_link()
    log_in_page.follow_the_log_in_link()
    log_in_page.returning_customer(user_data)
    log_in_page.check_user_log_in()
