from .base_page import BasePage
from .locators import OnePageCheckout
from selenium.webdriver.support.ui import Select


class OnePageCheckoutPage(BasePage):
    def choice_of_delivery_address(self):
        checkbox_choice = self.browser.find_element(*OnePageCheckout.CHECKBOX_PICK_UP_IN_STORE)
        checkbox_choice.click()
        continue_button = self.browser.find_element(*OnePageCheckout.BUTTON_PICK_UP_CONTINUE)
        continue_button.click()

    def choice_of_pay_method(self):
        button_continue = self.browser.find_element(*OnePageCheckout.BUTTON_PAYMENT_METHOD_CONTINUE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button_continue)
        button_continue.click()

    def confirm_the_order(self):
        button_confirm = self.browser.find_element(*OnePageCheckout.BUTTON_CONFIRM)
        button_confirm.click()

    def read_payment_information(self):
        button_continue = self.browser.find_element(*OnePageCheckout.BUTTON_PAYMENT_INFO_CONTINUE)
        button_continue.click()

    def specify_the_address(self, user_data=None, address=None):
        if user_data is not None:
            first_name = self.browser.find_element(*OnePageCheckout.FIELD_FIRST_NAME)
            first_name.send_keys(user_data['name'])
            last_name = self.browser.find_element(*OnePageCheckout.FIELD_LAST_NAME)
            last_name.send_keys(user_data['surname'])
            email = self.browser.find_element(*OnePageCheckout.FIELD_EMAIL)
            email.send_keys(user_data['email'])
        country = Select(self.browser.find_element(*OnePageCheckout.LIST_SELECT_COUNTRY))
        country.select_by_value("1")
        city = self.browser.find_element(*OnePageCheckout.FIELD_CITY)
        city.send_keys(address['city'])
        address1 = self.browser.find_element(*OnePageCheckout.FIELD_ADDRESS1)
        address1.send_keys(address['address1'])
        postcode = self.browser.find_element(*OnePageCheckout.FIELD_ZIP)
        postcode.send_keys(address['zipcode'])
        phone_number = self.browser.find_element(*OnePageCheckout.FIELD_PHONE_NUMBER)
        phone_number.send_keys(address['phone_number'])
        button_continue = self.browser.find_element(*OnePageCheckout.BUTTON_ADDRESS_CONTINUE)
        button_continue.click()

    def successful_order_check(self):
        success_message = self.browser.find_element(*OnePageCheckout.SUCCESS_MESSAGE_CSS_SELECTOR)
        assert OnePageCheckout.SUCCESS_MESSAGE == success_message.text,\
            "The order was not placed successfully"
