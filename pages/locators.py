from selenium.webdriver.common.by import By


class BasePageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, ".ico-register")
    LOG_IN_LINK = (By.CSS_SELECTOR, ".ico-login")
    LOG_OUT_LINK = (By.CSS_SELECTOR, ".ico-logout")
    LINK_ACCOUNT = (By.CSS_SELECTOR, ".header-links .account")

class CustomerPageLocators():
    LINK_PASSWORD_CHANGE = (By.XPATH, "//a[text() = 'Change password']")
    FIELD_OLD_PASSWORD = (By.CSS_SELECTOR, "#OldPassword")
    FIELD_NEW_PASSWORD = (By.CSS_SELECTOR, "#NewPassword")
    FIELD_CONFIRM_NEW_PASSWORD = (By.CSS_SELECTOR, "#ConfirmNewPassword")
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, ".change-password-button")
    MESSAGE_CHANGE_PASSWORD = (By.CSS_SELECTOR, "div.result")

class LoginPageLocators():
    LOG_IN_FORM = (By.CSS_SELECTOR, ".form-fields>form")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#Email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#Password")
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ".login-button")


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "input#add-to-cart-button-22")
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
