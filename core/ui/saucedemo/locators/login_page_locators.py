from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_text_element = (By.XPATH, "//h3[@data-test='error']")
    red_cross = (By.XPATH, "//*[@data-prefix='fas']")