from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_products_in_basket()
        self.should_be_empty_basket_message()

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket contains products, but should be empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "empty" in empty_message.lower(), "Basket empty message is incorrect"

    def go_to_checkout(self):
        checkout_button = self.browser.find_element(*BasketPageLocators.CHECKOUT_BUTTON)
        checkout_button.click()