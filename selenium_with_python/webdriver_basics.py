from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# whatever your browser version download that chromedriver exe and provide path of exe here

driver=webdriver.Chrome("C:\myData\Python_Automation\chromedriver\chromedriver-win32\chromedriver.exe")
driver.get("https://www.google.com")
driver.quit()
