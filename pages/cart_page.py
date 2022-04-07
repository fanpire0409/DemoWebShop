from .base_page import BasePage
from .locators import CartPageLocators
from selenium.webdriver.common.keys import Keys
import random


class CartPage(BasePage):

    def change_the_quantity_of_goods(self):
        random.seed(2)
        change_to = random.randint(1, 10)
        field_product_quantity = self.browser.find_element(*CartPageLocators.FIELD_QTY)
        global value_product_quantity
        value_product_quantity = int(field_product_quantity.get_attribute("value")) + change_to
        field_product_quantity.clear()
        field_product_quantity.send_keys(str(value_product_quantity))
        field_product_quantity.send_keys(Keys.ENTER)

    def check_change_the_quality(self):
        product_quantity = int(self.browser.find_element(*CartPageLocators.FIELD_QTY).get_attribute("value"))
        assert product_quantity == value_product_quantity, "Item Quantity Error"

    def check_coast(self):
        product_quantity = int(self.browser.find_element(*CartPageLocators.FIELD_QTY).get_attribute("value"))
        product_price = float(self.browser.find_element(*CartPageLocators.PRODUCT_UNIT_PRICE).text)
        products_coast = float(self.browser.find_element(*CartPageLocators.PRODUCT_SUBTOTAL).text)
        assert (product_quantity * product_price) == products_coast, "The cost is wrong!"

    def should_be_cart_url(self):
        assert "cart" in self.browser.current_url, "Error! It's not a cart page"
