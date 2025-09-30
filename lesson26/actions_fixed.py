import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import settings
# iніціалізуємо веб-драйвер
driver = Chrome()

# відкриваємо сторінку з прикладом
driver.get(settings.BASE_URL)
input_line = driver.find_element(By.CSS_SELECTOR, ".sMRwm .cm-line")
input_line.send_keys("Hello there")
actions = ActionChains(driver)
actions.click(input_line).key_down(Keys.CONTROL).send_keys('a').send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".tPLNx .cm-line").click()
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)

driver.execute_script("window.open('https://www.google.com','_blank');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
