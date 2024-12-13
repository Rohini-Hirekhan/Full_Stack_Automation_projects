from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains

"""
can do scroll using 3 option
1) scroll down page by pixel - executing js

"""

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(20)
#  scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)","")
value = driver.execute_script("return window.pageYOffset;")
print(value)

# scroll down page till the element is visible
flag = driver.find_element("xpath","//img[@alt='Flag of India']")
driver.execute_script("argument[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print(value)

# scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)

# scroll up to starting position

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)

