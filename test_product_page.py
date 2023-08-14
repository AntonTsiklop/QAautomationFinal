import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators


class TestProductPage:

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                                   "?promo=offer7", marks=pytest.mark.xfail)])
    def test_guest_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.prod_name_equals_cart_prod_name()
        product_page.prod_price_equals_cart_prod_price()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.add_to_cart()
        assert product_page.is_not_element_present(*ProductPageLocators.CART_PROD_NAME), "может видеть сообщение об " \
                                                                                         "успехе после добавления в корзину"

    def test_guest_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        assert product_page.is_not_element_present(*ProductPageLocators.CART_PROD_NAME), "может видеть сообщение об успехе" \
                                                                                         "без добавления в корзину"

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.add_to_cart()
        assert product_page.is_disappeared(*ProductPageLocators.CART_PROD_NAME), "сообщение не исчезает"

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.basket_should_be_empty()
        basket_page.should_be_basket_is_empty_text()


class TestUserAddToBasketFromProductPage:

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", 'olyuhnitup')

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                                   "?promo=offer7", marks=pytest.mark.xfail)])
    def test_user_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.prod_name_equals_cart_prod_name()
        product_page.prod_price_equals_cart_prod_price()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.add_to_cart()
        assert product_page.is_not_element_present(*ProductPageLocators.CART_PROD_NAME), "может видеть сообщение об " \
                                                                                         "успехе после добавления в корзину"

