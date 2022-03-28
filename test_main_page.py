from pages.main_page import MainPage

def test_func(browser):
    link = "http://demowebshop.tricentis.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_register_link()
    main_page.follow_the_register_link()
