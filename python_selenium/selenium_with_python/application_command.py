import time

from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager


'''
1) application commands -
- title
- current url
- page_Source
# 1) application commands -
# ---------------------------------
# - get - openeing the application URL
# - title - to capture the title of the current page
# - current url - to capture the current url of the web page
# - page_Source - to capture source code of the page
'''
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# print(driver.title) #OrangeHRM
# print(driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# print(driver.page_source)



driver = webdriver.Chrome()
driver.get("https://test.authsafe.ai/")
driver.find_element("link_text","register.php")