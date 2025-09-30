from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.url = None

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _input_field(self, locator): #locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout=5).until(
            EC.presence_of_element_located(locator))

    def _button(self, locator): #locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout=5).until(
            EC.element_to_be_clickable(locator))

    def _images(self, locator): #locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout=5).until(
            EC.presence_of_all_elements_located(locator))

    def _text(self, locator, text): #locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout=5).until(
            EC.text_to_be_present_in_element(locator, text))