import pytest
from selenium.webdriver import Chrome

from core.ui.saucedemo.pages.login_page import LoginPage
from core.ui.saucedemo.pages.products_page import ProductsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = ChromiumOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)
    # driver = Chrome()
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