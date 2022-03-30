from .register_page import RegisterPage
from .locators import CustomerPageLocators


class CustomerPage(RegisterPage):
    def check_change_password_url(self):
        assert "changepassword" in self.browser.current_url, "Error! It's not a change password page"

    def check_success_message_change_password(self):
        success_message = self.browser.find_element(*CustomerPageLocators.MESSAGE_CHANGE_PASSWORD)
        assert "Password was changed" == success_message.text, "Password has not been changed"

    def change_password(self, old_password, new_password):
        change_old_password = self.browser.find_element(*CustomerPageLocators.FIELD_OLD_PASSWORD)
        change_old_password.send_keys(old_password)
        change_new_password = self.browser.find_element(*CustomerPageLocators.FIELD_NEW_PASSWORD)
        change_new_password.send_keys(new_password)
        change_confirm_new_password = self.browser.find_element(*CustomerPageLocators.FIELD_CONFIRM_NEW_PASSWORD)
        change_confirm_new_password.send_keys(new_password)
        change_password_button = self.browser.find_element(*CustomerPageLocators.BUTTON_CHANGE_PASSWORD)
        change_password_button.click()

    def go_to_the_password_change_section(self):
        link_change_password = self.browser.find_element(*CustomerPageLocators.LINK_PASSWORD_CHANGE)
        link_change_password.click()
