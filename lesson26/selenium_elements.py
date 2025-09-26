from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_form():
    # Ініціалізація драйвера
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/html/elements.html")

    # Знаходження текстових полів за ID і введення тексту
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("example_username")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("example_password")

# Знаходження радіо кнопок за ID і вибір варіанта
    male_radio = driver.find_element(By.ID, "male")
    female_radio = driver.find_element(By.ID, "female")
    try:
        chupacabra_radio = driver.find_element(By.ID, "chupacabra")
        assert chupacabra_radio.is_displayed() is True
    except NoSuchElementException:
        print("No Chupakabra on the page")
    male_radio.click()
    assert male_radio.is_selected()
    assert female_radio.is_selected() is False


# Знаходження чекбоксу за ID і встановлення прапорця
    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    newsletter_checkbox.click()

# Вибір значення з випадаючого списку за ID
    country_dropdown = Select(driver.find_element(By.ID, "country"))
    country_dropdown.select_by_visible_text("США")

    country_dropdown.select_by_index(2)

    country_dropdown.select_by_value("ukraine")

    assert country_dropdown.first_selected_option.text == "Україна"

    # Натискання на кнопку за ID
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Зачекати 5 секунд перед завершенням


# Закрити браузер
    driver.quit()