from selenium.webdriver.common.by import By


class BasePageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, ".ico-register")

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
