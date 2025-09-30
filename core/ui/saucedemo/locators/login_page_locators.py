from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")