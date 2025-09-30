from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from ..locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = "https://www.saucedemo.com"
        self.locators = LoginPageLocators()

    def _user_input(self):
        return self._input_field(self.locators.user_name_input)

    def _user_pass_input(self):
        return self._input_field(self.locators.password_input)

    def _login_button(self):
        return self._button(self.locators.login_button)

    def set_user_name(self, user_name):
        self._user_input().send_keys(user_name)
        return self

    def set_password(self, password):
        self._user_pass_input().send_keys(password)
        return self

    def click_login(self):
        self._login_button().click()
        return self

    def login_user(self, user_name, password):
        self.set_user_name(user_name).set_password(password).click_login()
        return self
