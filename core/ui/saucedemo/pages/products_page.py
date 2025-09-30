from .base_page import BasePage
from ..locators.products_page_locators import ProductsPageLocators


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = "https://www.saucedemo.com/inventory.html"
        self.locators = ProductsPageLocators

    def products_images(self):
        return self._images(self.locators.images)
