from .base_page import BasePage
from .locators import ProductListPageLocators
import numpy as np


class ProductListPage(BasePage):
    def add_to_basket(self):
        np.random.seed(2)
        button_cart = self.browser.find_elements(*ProductListPageLocators.BUTTON_ADD_TO_CART)
        button_cart = np.random.choice(button_cart)
        button_cart.click()

    def check_add_to_cart(self):
        assert self.is_element_present(*ProductListPageLocators.ADD_TO_CART_SUCCESS_MESSAGE), \
            "Error! Product wasn't added to cart"
