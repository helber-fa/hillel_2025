import time

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

webdriver = WebDriver()
webdriver.get("https://regex101.com/")
webdriver.maximize_window()
time.sleep(5)
command_line = webdriver.find_element(By.XPATH, "//*[contains(@class, 'cm-line')]")
command_line.click()
command_line.send_keys("Hi")

time.sleep(5)
