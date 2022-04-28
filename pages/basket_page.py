from .locators import BasketPageLocators
from .base_page import BasePage
import time

class BasketPage(BasePage):
    def items_are_not_in_basket(self):
        items_in_basket = len(self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS))
        assert items_in_basket == 0, "Basket is not empty"

    def basket_is_empty_notification(self):
        notification_basket_empty = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_NOTIF)
        assert notification_basket_empty, "Notification that basket is not empty is missed"
