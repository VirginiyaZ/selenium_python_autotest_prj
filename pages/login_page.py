from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def register_new_user(self,email, password):
        email_registration = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_registration.send_keys(email)
        password_number1 = self.browser.find_element(*LoginPageLocators.PASSWORD_NUMBER1)
        password_number1.send_keys(password)
        re_password_number1 = self.browser.find_element(*LoginPageLocators.RE_PASSWORD_NUMBER1)
        re_password_number1.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()



    def should_be_login_url(self):
        assert "login" in self.url, "URL not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"