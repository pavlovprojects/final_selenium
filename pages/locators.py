from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR,".btn-group")
    BASKET_ITEMS = (By.CSS_SELECTOR,".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR,"#content_inner")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFORM_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBBMIT = (By.CSS_SELECTOR, "#register_form .btn")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR,".col-sm-6 h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,"p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alertinner strong")

