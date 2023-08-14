from selenium.webdriver.common.by import By


class BasePageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    CART_PRICE = (By.CSS_SELECTOR, ".fade.in > div > p:nth-child(1) > strong")
    PROD_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    CART_PROD_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasketPageLocators:

    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset > div")
