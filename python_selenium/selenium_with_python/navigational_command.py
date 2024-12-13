from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

'''
4) navigational command - directly access through driver instance
- back()
- forward()
- refresh()
driver.get("https://www.snapdeal.com")
driver.get("http://www.amazon.com")
driver.back()
driver.forward()
driver.refresh()

find_element - return single webelement
find_elements - return multiple webelement

text vs get_attribute()
text - returns inner text of the element
get_attribute() - returns values of any attribute of web element

'''
driver = webdriver(Chrome)
driver.get("https://www.snapdeal.com")
driver.get("http://www.amazon.com")
driver.back()
driver.forward()
driver.refresh()


























