from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager


'''
2)conditional commands
------------------------
following method can be access through only web element
is_displayed() - check perticular web element is present on web page or not
- if element id displayed return true or displayed false
is_enabled() - check if radio button is enabled or not (return true or false)
is_selected() - check if checkbox is selected or not (return true or false)

'''

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
searchbox = driver.find_element("xpath","/html/body/div[6]/div[1]/div[2]/div[2]/form/input")
print("displayed status : ",searchbox.is_displayed()) #displayed status :  True
print("displayed status : ",searchbox.is_enabled()) #displayed status :  True
rd_male = driver.find_element("id","gender-male")
rd_female = driver.find_element("id","gender-female")
print("default selecting radio button")
print(rd_male.is_selected())#False
print(rd_female.is_selected()) #False
rd_male.click()
print("after selecting radio button")
print(rd_male.is_selected())#True
print(rd_female.is_selected()) #False
