from .base_page import BasePage
from .locators import RegisterPageLocators

class RegisterPage(BasePage):
    def completion_of_registration(self):
        continue_button = self.browser.find_element(*RegisterPageLocators.BUTTON_REGISTER_CONTINUE)
        continue_button.click()

    def register_new_user(self, user_data):
        if user_data['gender'] == "M":
            register_gender = self.browser.find_element(*RegisterPageLocators.RADIO_GENDER_M)
        else:
            register_gender = self.browser.find_element(*RegisterPageLocators.RADIO_GENDER_F)
        register_gender.click()
        register_first_name = self.browser.find_element(*RegisterPageLocators.FIELD_FIRST_NAME)
        register_first_name.send_keys(user_data['name'])
        register_last_name = self.browser.find_element(*RegisterPageLocators.FIELD_LAST_NAME)
        register_last_name.send_keys(user_data['surname'])
        register_email = self.browser.find_element(*RegisterPageLocators.FIELD_EMAIL)
        register_email.send_keys(user_data['email'])
        register_password1 = self.browser.find_element(*RegisterPageLocators.FIELD_PASSWORD)
        register_password1.send_keys(user_data['password'])
        register_password2 = self.browser.find_element(*RegisterPageLocators.FIELD_CONFIRM_PASSWORD)
        register_password2.send_keys(user_data['password'])
        register_button = self.browser.find_element(*RegisterPageLocators.BUTTON_REGISTER)
        register_button.click()

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented!"

    def should_be_register_url(self):
        assert "register" in self.browser.current_url, "Error! It's not a register page"

    def should_be_success_message(self):
        assert "Your registration completed" == \
               self.browser.find_element(*RegisterPageLocators.REGISTER_SUCCESS_MESSAGE).text, \
            "Registration isn't completed!"
