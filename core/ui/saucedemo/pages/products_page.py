from settings import settings
from .base_page import BasePage
from selenium.webdriver.support.ui import Select
from ..locators.products_page_locators import ProductsPageLocators


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = f"{settings.saucedemo_base_url}/inventory.html"
        self.locators = ProductsPageLocators

    default_sort_option = "Name (A to Z)"

    def products_images(self):
        return self._images(self.locators.images)

    def _sorting_select(self):
        return Select(self._present_element(self.locators.sorting_select))

    def get_current_select_option(self):
        return self._sorting_select().first_selected_option.text

    def _product_names(self):
        return self._present_elements(self.locators.product_name)

    def get_product_name_as_text(self):
        return [k.text for k in self._product_names()]



