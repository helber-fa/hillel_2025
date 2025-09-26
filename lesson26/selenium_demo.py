import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://localhost:8000/html/demo.html")

# Знаходження елемента за ID
user_field = driver.find_element(By.ID, "username")
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")

# Знаходження елемента за XPath
user_field = driver.find_element(By.XPATH, "//input[@id='username']")
pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
l_button = driver.find_element(By.XPATH, "//button[@id='login_button']")

# Знаходження елемента за CSS класом
user_field = driver.find_element(By.CSS_SELECTOR, ".input-field#username")
pass_field = driver.find_element(By.CSS_SELECTOR, ".input-field#password")
login_button = driver.find_element(By.CSS_SELECTOR, "#login_button")

# Знаходження елемента за назвою тегу
form_element = driver.find_element(By.TAG_NAME, "li")

li_elements = driver.find_elements(By.TAG_NAME, "li")

# Пошук конкретного елемента серед отриманих
for li in li_elements:
    # пошук може бути повiльним якщо елементiв багато
    if li.text == "Елемент списку 2":
        # Знайдено потрібний елемент
        print("Знайдено елемент:", li.text)
        break

pass