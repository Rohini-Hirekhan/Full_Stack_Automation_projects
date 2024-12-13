from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Chrome()


driver.implicitly_wait(10)
driver.get("https://google.com")
driver.maximize_window()
driver.implicitly_wait(20)