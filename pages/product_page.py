from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def prod_name_equals_cart_prod_name(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        cart_prod_name = self.browser.find_element(*ProductPageLocators.CART_PROD_NAME).text
        assert prod_name == cart_prod_name, "Название товара на странице не соответсвует " \
                                            "названию товара добавленного в крозину"

    def prod_price_equals_cart_prod_price(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.encode()
        cart_prod_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text.encode()
        assert prod_price == cart_prod_price, "Цена корзины не соответствует цене товара"


