from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# new tab - selenium4 - opens a new tab and switches to new tab
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com/")
# opens a new browser window and switches to window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")