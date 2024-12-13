from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()

"""
how to switch between browser window - 
ccurrent_window_handle ----> return windowID of single browser window
window_handles ------------> return window ID's of multiple browser windows


driver.switch_to.window(windowID)
"""
#
# driver.get("https://www.opencart.com/")
#
# windowid = driver.current_window_handle
# print(windowid) #D8E6D7B8198DEF663548D715CABA49C4
# driver.get("https://www.opencart.com/")
# #everytime we will get different window id
# windowid = driver.current_window_handle
# print(windowid) #3EC52621877317FA02B2E10A51962EB3

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element("xpath","//a[normalize-space()='OrangeHRM, Inc']").click()
windowIDs=driver.window_handles # we will get list
parentwindowid = windowIDs[0]
childwindowid = windowIDs[1]
print(parentwindowid,childwindowid)
driver.switch_to.window(childwindowid)
print("title of the child window" ,driver.title)
driver.switch_to.window(parentwindowid)
print("title of the parent window" , driver.title)

#2nd approach
for i in windowIDs:
    driver.switch_to.window(i)
    print(driver.title)

#close our choice window
for i in windowIDs:
    driver.switch_to.window(i)
    if driver.title == "OrangeHRM":
        driver.close()
