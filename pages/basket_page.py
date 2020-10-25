from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_message_basket_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text, "Message basket empty is not presented"