import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(20)
drp = Select(driver.find_element("id","country"))
time.sleep(10)
drp.select_by_visible_text("India")
time.sleep(10)
drp.select_by_value('japan')
time.sleep(10)
#
# opt=drp.options
# # for i in opt:
# #     print(i.text)
#
# #select option from dropdown without using buit-in method
# for i in opt:
#     if i.text == "china":
#         i.click()

# -------------------------------------------------------------------
#
# drp = Select(driver.find_element("id","colors"))
#
# drp.select_by_value('white')
# time.sleep(10)
# drp.select_by_visible_text('Green')
# time.sleep(10)
# drp.select_by_index(0)