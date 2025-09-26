from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ініціалізуємо драйвер Chrome
driver = webdriver.Chrome()
#
# # Відкриваємо головну сторінку
driver.get("http://localhost:8000/html/scroll_frame.html")
driver.maximize_window()
# time.sleep(2)
# # Прокрутка вниз
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)  # Зачекайте трохи після прокрутки вниз
#
# # Прокрутка вгору
# driver.execute_script("window.scrollTo(0, 0);")
# time.sleep(2)  # Зачекайте трохи після прокрутки вгору
#
# # Перемикаємося до фрейму
# driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))


# # Натискання на кнопку три рази
# for _ in range(3):
#     button = driver.find_element(By.ID, "myButton")
#     button.click()
#     time.sleep(1)  # Зачекайте трохи після кожного натискання
# # iframe_button = driver.find_element(By.CSS_SELECTOR, "#myButton")
# # iframe_button.click()
# time.sleep(5)


# Закриваємо браузер
driver.quit()