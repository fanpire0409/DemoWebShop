import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FfOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store_true', help="Run in headless mode")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nYou use Chrome browser for test..")
        options = ChOptions()
        if request.config.getoption("--headless"):
            options.headless = True
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nYou use  Firefox browser for test..")
        options = FfOptions()
        if request.config.getoption("--headless"):
            options.headless = True
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
