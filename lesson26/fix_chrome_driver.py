# chrome_options = webdriver.ChromeOptions()
# chrome_options.browser_version = "114"
# driver = webdriver.Chrome(options=chrome_options)
#
# ------------------------------------------
# pip install chromedriver-autoinstaller
#
# from selenium import webdriver
# import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()
# driver = webdriver.Chrome()
# ------------------------------------------
#
# pip install webdriver_manager
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import ChromiumOptions
# from webdriver_manager.chrome import ChromeDriverManager
#
# chrome_options = ChromiumOptions()
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(options=chrome_options, service=service)