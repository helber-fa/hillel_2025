from selenium.webdriver.common.by import By


class ProductsPageLocators:
    images = (By.XPATH, "//img[@class='inventory_item_img']")
    sorting_select = (By.XPATH, "//select[@class='product_sort_container']")
    product_name = (By.CSS_SELECTOR, ".inventory_item_name")