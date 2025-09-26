from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.get("http://localhost:8000/html/alert.html")

# Показати Alert і отримати текст з нього
driver.find_element(By.XPATH, "//button[text()='Показати Alert']").click()
alert = Alert(driver)
print("Текст Alert:", alert.text)
time.sleep(2)
alert.accept()


# Показати Confirm і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
alert = Alert(driver)
print("Текст Confirm:", alert.text)
time.sleep(2)
alert.accept()

# Показати Prompt, ввести текст і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
alert = Alert(driver)
print("Текст Prompt:", alert.text)
alert.send_keys("John")
time.sleep(2)
# alert.accept()
alert.dismiss()

# Зачекати 2 секунди перед завершенням
time.sleep(2)

# Закрити браузер
driver.quit()