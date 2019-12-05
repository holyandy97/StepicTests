import time

import pytest

from Pages.login_page import LoginPage
from Pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_add_product_to_basket(browser):

    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_of_addition_message()
    page.should_be_the_right_price_of_the_cart()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_cart()
    time.sleep(1)
    page.should_be_dissapeared()

@pytest.mark.user_add_to_cart
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "sword123pas"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        self.browser = browser

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_the_cart()
        page.should_be_success_of_addition_message()
        page.should_be_the_right_price_of_the_cart()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()