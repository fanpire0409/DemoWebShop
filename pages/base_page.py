from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
import faker
import time
import numpy as np

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def check_user_log_in(self):
        assert self.is_element_present(*BasePageLocators.LINK_ACCOUNT), "User isn't log in!"

    def create_user_data(self):
        np.random.seed(2)
        gender = np.random.choice(["M", "F"])

        fake = faker.Faker()
        if gender == "M":
            name = fake.first_name_male()
            surname = fake.last_name_male()
        else:
            name = fake.first_name_female()
            surname = fake.last_name_female()
        email = fake.email()
        password = str(time.time())

        return {'gender': gender, 'name': name, 'surname': surname, 'email': email, 'password': password}

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def follow_the_customer_link(self):
        customer_link = self.browser.find_element(*BasePageLocators.LINK_ACCOUNT)
        customer_link.click()

    def follow_the_log_in_link(self):
        register_link = self.browser.find_element(*BasePageLocators.LOG_IN_LINK)
        register_link.click()

    def follow_the_log_out_link(self):
        register_link = self.browser.find_element(*BasePageLocators.LOG_OUT_LINK)
        register_link.click()

    def follow_the_register_link(self):
        register_link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        register_link.click()

    def open(self):
        self.browser.get(self.url)

    def should_be_log_in_link(self):
        assert self.is_element_present(*BasePageLocators.LOG_IN_LINK), "Log_in link is not presented"

    def should_be_register_link(self):
        assert self.is_element_present(*BasePageLocators.REGISTER_LINK), "Register link is not presented"
