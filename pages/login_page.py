from .register_page import RegisterPage
from .locators import LoginPageLocators


class LoginPage(RegisterPage):
    def checkout_as_guest(self):
        checkout_as_guest_button = self.browser.find_element(*LoginPageLocators.BUTTON_CHECKOUT_AS_GUEST)
        checkout_as_guest_button.click()

    def returning_customer(self, user_data):
        login_email = self.browser.find_element(*LoginPageLocators.FIELD_EMAIL)
        login_email.send_keys(user_data['email'])
        login_password = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD)
        login_password.send_keys(user_data['password'])
        login_button = self.browser.find_element(*LoginPageLocators.BUTTON_LOG_IN)
        login_button.click()

    def should_be_log_in_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_FORM), "Log_in form is not presented!"

    def should_be_log_in_url(self):
        assert "login" in self.browser.current_url, "Error! It's not a log in page"

    def go_to_registration_by_button(self):
        registration_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        registration_button.click()
