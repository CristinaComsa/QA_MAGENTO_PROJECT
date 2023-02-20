"""
all the methods for login page
"""
from features.pages.base_page import BasePage
from features.resources.login_locators import LoginPageLocators



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_sign_in_button(self):
        self.click(LoginPageLocators.sign_in_button)

    def get_customer_message(self):
        return self.get_text(LoginPageLocators.customer_message)

    def enter_email(self,email):
        self.enter_text(LoginPageLocators.email_field,email)

    def enter_password(self,password):
        self.enter_text(LoginPageLocators.password_field,password)

    def login(self, email, password):
        self.click_on_sign_in_button()
        self.enter_email(email)
        self.enter_password(password)
        self.sign_in()

    def sign_in(self):
        self.click(LoginPageLocators.sign_in)

    def get_welcome_message(self):
        return self.get_text(LoginPageLocators.welcome_message)

    def get_customer_login_message(self):
        return self.get_text(LoginPageLocators.customer_login_message)

    def logout_button(self):
        self.click(LoginPageLocators.button)

    def logout(self):
        self.click(LoginPageLocators.sign_out_button)

