from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "отсутствует сообщение о том, что " \
                                                                                  "корзина пуста"

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "корзина не пуста"
