from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains
import os

"""
In driver there is method is available to capture screenshot
how to capture screenshot of any webpage - 
we can capture full page screenshot
always maximize window otherwise it will not take screenshot
driver.save_screenshot - we need to specify path where screenshot will save
 - if you dont want to give full path then current file path can give using os.getcwd() method
 os.getcwd() - driver.save_screenshot(os.getcwd()+"\\screenshpt.png")

"""
driver.get("https://google.com")
#need to maximize window for capture screenshot
driver.maximize_window()

# driver.save_screenshot(os.getcwd()+"rohini.png")
# if you will not specify the path from where script is running from there file will be created
# driver.get_screenshot_as_file("sc.png")
driver.get_screenshot_as_base64("base.png")
driver.get_screenshot_as_png("kl.png")

