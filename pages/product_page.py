from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()


    def should_be_message_about_product_into_basket(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_added_to_basket_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFT_ADDED).text
        assert product_title == product_added_to_basket_alert, f"Product {product_title} do not added to basket"
        # print(product_title)

    def should_be_message_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text  
        assert product_price == basket_total, "Total amount does not match with added product price"
        # print(product_price)


    def should_be_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_AFT_ADDED),"Success message! But should not to be"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFT_ADDED),  "Success message! But should not to be"
           