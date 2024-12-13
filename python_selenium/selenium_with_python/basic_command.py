import time

from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Chrome()
# 1) application commands -
# ---------------------------------
# - get - openeing the application URL
# - title - to capture the title of the current page
# - current url - to capture the current url of the web page
# - page_Source - to capture source code of the page
#
# driver.get("https://opensource-demo.orangehrmlive.com/")
# print(driver.title) #OrangeHRM
# print(driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# print(driver.page_source)

# 2)conditional commands
# ------------------------
# following method can be access through only web element
# is_displayed() - check perticular web element is present on web page or not
# - if element id displayed return true or displayed false
# is_enabled() - check if radio button is enabled or not (return true or false)
# is_selected() - check if checkbox is selected or not (return true or false)

# driver.get("https://demo.nopcommerce.com/register")
# searchbox = driver.find_element("xpath","/html/body/div[6]/div[1]/div[2]/div[2]/form/input")
# print("displayed status : ",searchbox.is_displayed()) #displayed status :  True
# print("displayed status : ",searchbox.is_enabled()) #displayed status :  True
# rd_male = driver.find_element("id","gender-male")
# rd_female = driver.find_element("id","gender-female")
# print("default selecting radio button")
# print(rd_male.is_selected())#False
# print(rd_female.is_selected()) #False
# rd_male.click()
# print("after selecting radio button")
# print(rd_male.is_selected())#True
# print(rd_female.is_selected()) #False

# 3) browser commands
# - close - 1) close single browser window (where driver should focused)but internally process is running(can close single browser at a time)
# - quit() - 1) close all browser along with browser(it will close all browser and will kill the process)
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# driver.implicitly_wait(300)
# driver.find_element("link text","OrangeHRM, Inc").click()
# # driver.find_element("xpath","/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
# # driver.find_element("partial link text","OrangeHRM, I").click()
# driver.implicitly_wait(100)
# # driver.find_element("xpath","/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[1]").click()
# driver.implicitly_wait(300)
# driver.close()
# # //*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a

# 4) navigational command - directly access through driver instance
# - back()
# - forward()
# - refresh()
# driver.get("https://www.snapdeal.com")
# driver.get("http://www.amazon.com")
# driver.back()
# driver.forward()
# driver.refresh()

# find_element
# find_elements
# text vs get_attribute()
# text - returns inner text of the element
# get_attribute() - returns values of any attribute of web element


# 5) wait commands - to solve synchronization problem we use wait statements
# sometimes scripts run faster than application so application is not sync with scripts
# 1) implicit wait
# 2) explicit wait
# time.sleep()-
# adv -
# 1)simple to use
# disadvantage -
# it took maximum ime out for all elements
# 1) performance of the script is very poor
# 2) if the element is not available within the time metioned,still there is chance of getting exception
# implicit wait-
# adv-
# 1) single statement
# 2) performance will not be reduced(if the element is available within the time it proceed to execute further statements)
# disadv-if the element is not available within the time metioned,still there is chance of getting exception
# 1)
# it will applicable for all element which is present from bottom of implicit wait
# so specify it beginning of the script after driver is created.
# it will not wait for maximum time out if element is got in 5 sec then it will not wait for 5sec
# so performance issue will not be there
# one implicit wait handling synchronization problem for throughout the script
# default time is 0 secrets
# application must be loaded in 10sec if not then report performance bug

