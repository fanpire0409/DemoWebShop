from selenium.webdriver.common.by import By


class BasePageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, ".ico-register")
    LOG_IN_LINK = (By.CSS_SELECTOR, ".ico-login")
    LOG_OUT_LINK = (By.CSS_SELECTOR, ".ico-logout")
    LINK_ACCOUNT = (By.CSS_SELECTOR, ".header-links .account")
    CART_LINK = (By.CSS_SELECTOR, "#topcartlink .ico-cart")
    CART_LINK_AFTER_ADDED_PRODUCT = (By.CSS_SELECTOR, "#topcartlink .cart-qty")


class CartPageLocators():
    PRODUCT_UNIT_PRICE = (By.CSS_SELECTOR, ".product-unit-price")
    FIELD_QTY = (By.CSS_SELECTOR, ".qty-input")
    PRODUCT_SUBTOTAL = (By.CSS_SELECTOR, ".product-subtotal")
    CHECKBOX_TERMS_OF_SERVICE = (By.CSS_SELECTOR, "input#termsofservice")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "button#checkout")


class CustomerPageLocators():
    LINK_PASSWORD_CHANGE = (By.XPATH, "//a[text() = 'Change password']")
    FIELD_OLD_PASSWORD = (By.CSS_SELECTOR, "#OldPassword")
    FIELD_NEW_PASSWORD = (By.CSS_SELECTOR, "#NewPassword")
    FIELD_CONFIRM_NEW_PASSWORD = (By.CSS_SELECTOR, "#ConfirmNewPassword")
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, ".change-password-button")
    MESSAGE_CHANGE_PASSWORD = (By.CSS_SELECTOR, "div.result")


class LinksLocators():
    MAIN_LINK = "http://demowebshop.tricentis.com/"
    PRODUCT_LINK = "http://demowebshop.tricentis.com/health"
    PRODUCT_LIST_LINK = "http://demowebshop.tricentis.com/books"
    REGISTER_LINK = "http://demowebshop.tricentis.com/register"
    CART_LINK = "http://demowebshop.tricentis.com/cart"
    ORDER_LINK = "http://demowebshop.tricentis.com/onepagecheckout"


class LoginPageLocators():
    LOG_IN_FORM = (By.CSS_SELECTOR, ".form-fields>form")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#Email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#Password")
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ".login-button")
    BUTTON_REGISTER = (By.CSS_SELECTOR, ".register-button")
    BUTTON_CHECKOUT_AS_GUEST = (By.CSS_SELECTOR, ".checkout-as-guest-button")


class OnePageCheckout():
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "#BillingNewAddress_FirstName")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "#BillingNewAddress_LastName")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#BillingNewAddress_Email")
    LIST_SELECT_COUNTRY = (By.CSS_SELECTOR, "select#BillingNewAddress_CountryId")
    FIELD_CITY = (By.CSS_SELECTOR, "#BillingNewAddress_City")
    FIELD_ADDRESS1 = (By.CSS_SELECTOR, "#BillingNewAddress_Address1")
    FIELD_ZIP = (By.CSS_SELECTOR, "#BillingNewAddress_ZipPostalCode")
    FIELD_PHONE_NUMBER = (By.CSS_SELECTOR, "#BillingNewAddress_PhoneNumber")
    BUTTON_ADDRESS_CONTINUE = (By.CSS_SELECTOR, "div#billing-buttons-container input")
    CHECKBOX_PICK_UP_IN_STORE = (By.CSS_SELECTOR, "#PickUpInStore")
    BUTTON_PICK_UP_CONTINUE = (By.CSS_SELECTOR, "#shipping-buttons-container input")
    BUTTON_PAYMENT_METHOD_CONTINUE = (By.CSS_SELECTOR, "#payment-method-buttons-container input")
    BUTTON_PAYMENT_INFO_CONTINUE = (By.CSS_SELECTOR, "#payment-info-buttons-container input")
    BUTTON_CONFIRM = (By.CSS_SELECTOR, ".confirm-order-next-step-button")
    SUCCESS_MESSAGE = "Your order has been successfully processed!"
    SUCCESS_MESSAGE_CSS_SELECTOR = (By.CSS_SELECTOR, ".master-wrapper-main strong")


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "input#add-to-cart-button-22")
    ADD_TO_CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".bar-notification.success p")


class ProductListPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".product-box-add-to-cart-button")
    ADD_TO_CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".bar-notification.success p")


class RegisterPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, ".registration-page>.page-body")
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.result")
    RADIO_GENDER_M = (By.CSS_SELECTOR, "#gender-male")
    RADIO_GENDER_F = (By.CSS_SELECTOR, "#gender-female")
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "#FirstName")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "#LastName")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#Email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#Password")
    FIELD_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#ConfirmPassword")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "#register-button")
    BUTTON_REGISTER_CONTINUE = (By.CSS_SELECTOR, ".register-continue-button")
