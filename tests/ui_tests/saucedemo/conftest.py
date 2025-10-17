import pytest
from selenium.webdriver import Chrome

from core.ui.saucedemo.pages.login_page import LoginPage
from core.ui.saucedemo.pages.products_page import ProductsPage

@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()

@pytest.fixture
def login_page(driver):
    login_page=LoginPage(driver)
    login_page.open_page()
    return login_page

@pytest.fixture
def products_page(driver):
    return ProductsPage(driver)