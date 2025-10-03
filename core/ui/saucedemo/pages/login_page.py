from settings import settings
from .base_page import BasePage
from ..locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.saucedemo_base_url
        self.locators = LoginPageLocators()

    def _user_input(self):
        return self._input_field(self.locators.user_name_input)

    def _user_pass_input(self):
        return self._input_field(self.locators.password_input)

    def _login_button(self):
        return self._button(self.locators.login_button)

    def _error_h3_text(self):
        return self._text(self.locators.error_text_element, "Epic sadface: Username and password do not match any user in this service")

    # def error_crosses(self):
    #     return self._wait_for_n_elements_are_present(self.locators.red_cross, 3)

    def error_crosses(self):
        return self._present_elements(self.locators.red_cross)

    def get_error_crosses_number(self):
        return len(self.error_crosses())

    def set_user_name(self, user_name):
        self._user_input().send_keys(user_name)
        return self

    def get_error_message(self):
        return self._present_element(self.locators.error_text_element).text


    def set_password(self, password):
        self._user_pass_input().send_keys(password)
        return self

    def click_login(self):
        self._login_button().click()
        return self

    def login_user(self, user_name, password):
        self.set_user_name(user_name).set_password(password).click_login()
        return self
