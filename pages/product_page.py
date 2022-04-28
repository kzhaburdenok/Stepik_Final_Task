from .locators import ProductPageLocators
from .base_page import BasePage



class ProductPage(BasePage):
    def add_product_to_cart(self):

        add_to_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_BTN)
        add_to_cart.click()
    
    def product_should_be_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PPODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        text_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_CART_ALLERT).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert text_in_alert == product_name, "Another Product was added to cart"
        assert price_in_alert == product_price, "Different price"
