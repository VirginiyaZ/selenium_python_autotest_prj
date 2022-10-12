from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    


class BasketPageLocators():
    BASKET_MSG_TXT = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.XPATH, "//header/div/div/div[2]/span/a")
    

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_NAME_AFT_ADDED = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")


