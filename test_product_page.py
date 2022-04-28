import pytest
import time
import math
import random
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        time.sleep(2)
        self.my_email = str(time.time()) + "@fakemail.org"
        self.my_password = "password" + str(time.time())
        self.page = LoginPage(browser, self.link)
        self.page.open()
        self.page.register_new_user(self.my_email, self.my_password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_msg()

    def test_user_can_add_product_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_cart()
        page.get_product_name()
        page.get_product_price()

def test_guest_cant_see_success_message(self,browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_msg()

@pytest.mark.parametrize("promo_offer", [pytest.param(i, marks=pytest.mark.xfail(i=="{i}", reason="")) for i in range (10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.get_product_name()
    page.get_product_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_msg()



@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser,link)
    basket_page.items_are_not_in_basket()
    basket_page.basket_is_empty_notification()