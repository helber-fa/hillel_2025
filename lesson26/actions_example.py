from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time

# iніціалізуємо веб-драйвер
driver = Chrome()

# відкриваємо сторінку з прикладом
driver.get("http://localhost:8000/html/action_chains.html")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys("w").key_up(Keys.Com).key_up(Keys.ALT).perform()

# знаходимо eлемент circle
circle = driver.find_element(By.ID, "circle")

# cтворюємо екземпляр класу ActionChains


# отримаємо розміри зони, де ми можемо переміщувати коло
zone = driver.find_element(By.ID, "container")

# дозволена довжина/ширина зони для руху
azw = zone.size['width'] - circle.size['width'] - 10
azh = zone.size['height'] - circle.size['height'] - 10
pass
try:
    # центр зони
    actions.click_and_hold(circle).move_to_element(zone).perform()
    time.sleep(2)
    # правий нижнiй кут
    actions.move_to_element(circle).move_by_offset(azw / 2, azh / 2).perform()
    time.sleep(2)
    # правий верхнiй кут
    actions.move_to_element(circle).move_by_offset(0, -azh).perform()
    time.sleep(2)
    # лiвий верхнiй кут
    actions.move_to_element(circle).move_by_offset(-azw, 0).perform()
    time.sleep(2)
    # лiвий  нижнiй кут
    actions.move_to_element(circle).move_by_offset(0, azh).perform()
    time.sleep(2)
    # центр зони
    actions.click_and_hold(circle).move_to_element(zone).perform()
    time.sleep(2)
    # подвiйний клiк
    actions.double_click(circle).perform()
    time.sleep(2)
    # одинарний клiк
    actions.click(circle).perform()
    time.sleep(2)

    # перевіряємо чи змінився фоновий колір на зелений
    background_color = circle.value_of_css_property("background-color")
    # RGBA значення кольору зеленого (0, 128, 0)
    # з повним непрозорістю (alpha = 1)
    if background_color == "rgba(0, 128, 0, 1)":
        print("Фон змінився на зелений!")

    # курсор поза межi circle
    actions.move_by_offset(-100, -100).perform()
    time.sleep(1)

    # перевіряємо чи змінився фоновий колір на червоний
    background_color_out = circle.value_of_css_property("background-color")
    # RGBA значення кольору зеленого (255, 0, 0)
    # з повним непрозорістю (alpha = 1)
    if background_color_out == "rgba(255, 0, 0, 1)":
        print("Фон змінився на червоний!")

    # натискання клавіші Enter
    actions.send_keys(Keys.ENTER).perform()
    actions.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down("W").perform()
    time.sleep(2)
    alert = Alert(driver)
    # закриваємо Confirm вiкно
    alert.accept()
    time.sleep(0.5)
    pass
finally:
    # закриваємо веб-драйвер
    driver.quit()