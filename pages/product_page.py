from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_total_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

    def should_be_correct_product_name_in_success_message(self, product_name):
        success_product_name = self.get_success_message_product_name()
        assert product_name == success_product_name, f"Product name '{product_name}' does not match success message '{success_product_name}'"

    def should_be_correct_basket_total_price(self, product_price):
        basket_total = self.get_basket_total_price()
        assert product_price == basket_total, f"Product price '{product_price}' does not match basket total '{basket_total}'"