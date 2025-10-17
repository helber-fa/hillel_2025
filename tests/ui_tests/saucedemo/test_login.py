import pytest

from settings import settings
import pytest_check
import allure

@allure.epic("UI tests - Saucedemo")
@allure.feature("Authentication user")
@allure.story("Authentication positive")
@pytest.mark.ui
@pytest.mark.negative
def test_product_page_is_open(driver, login_page, products_page):
    login_page.login_user(settings.saucedemo_user, settings.saucedemo_pass)
    products_page.products_images()

@allure.epic("UI tests - Saucedemo")
@allure.feature("Authentication user")
@allure.story("Authentication negative")
@allure.description("Test that check incorrect authentication of user")
@allure.title("Incorrect data - {user_name}, {password}")
@allure.link("jira/0888479")
@pytest.mark.ui
@pytest.mark.parametrize("user_name, password", [
    ("placeholder", settings.saucedemo_pass),
    (settings.saucedemo_user, "placeholder")])
def test_invalid_credentials(user_name, password, driver, login_page):
    login_page.login_user(user_name, password)
    pytest_check.equal(login_page.get_error_message(), "Epic sadface: Username and password do not match any user in this service")
    pytest_check.equal(login_page.get_error_crosses_number(), 3)


