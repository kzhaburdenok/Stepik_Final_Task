import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize("promo_offer", [pytest.param(i, marks=pytest.mark.xfail(i=="{i}", reason="")) for i in range (10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.get_product_name()
    page.get_product_price()