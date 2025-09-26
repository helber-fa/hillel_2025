from selenium import webdriver

# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Chrome()

# Відкриття веб-сторінки
driver.get("https://www.example.com")
driver.find_element()

# Робота з веб-елементами і виконання дій на сторінці

# Закриття браузера
driver.quit()
driver.close()