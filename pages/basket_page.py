from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_element_present_into_basket(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def is_not_element_present_into_basket(self, how, what, timeout= 4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def should_be_empty_basket(self):
        assert self.is_not_element_present_into_basket( *BasketPageLocators.PRODUCTS_IN_BASKET), "There are items into basket"

    
    def should_be_empty_basket_text(self):
        assert self.is_element_present_into_basket(*BasketPageLocators.BASKET_MSG_TXT), "Text: 'Your basket is empty' is not presented"


    


    