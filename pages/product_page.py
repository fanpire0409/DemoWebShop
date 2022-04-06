from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_cart.click()

    def check_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE), \
            "Error! Product wasn't added to cart"
