from pages.main_page import MainPage
from pages.register_page import RegisterPage

def test_register_link(browser):
    link = "http://demowebshop.tricentis.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_register_link()
    main_page.follow_the_register_link()
    register_page = RegisterPage(browser, browser.current_url)
    register_page.should_be_register_url()
