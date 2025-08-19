from abc import abstractmethod

class BasePage:
    def close_popup(self):
        print("Closing pop up")

    @abstractmethod
    def is_displayed(self):
        pass

class LoginPage(BasePage):
    def __init__(self):
        self.root_element = "Login form"
    def is_displayed(self):
        print(f"Page visible by {self.root_element}")

    def do_login(self):
        pass

login_page = LoginPage()
login_page.is_displayed()