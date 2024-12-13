"""
not executed for prompt - given input is not entered
"""

import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


alert = ("xpath","//button[normalize-space()='Alert']")
confirm = ("xpath","//button[@onclick='myFunctionConfirm()']")
prompt = ("xpath","//button[@onclick='myFunctionPrompt()']")

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
wait = WebDriverWait(driver,10)

#simple Alert
# wait.until(ec.presence_of_element_located(alert)).click()
# alert = driver.switch_to.alert
# time.sleep(10)
# alert.accept()

#confirm box alert
# wait.until(ec.presence_of_element_located(confirm)).click()
# alert = driver.switch_to.alert
# time.sleep(10)
# alert.accept()
# wait.until(ec.presence_of_element_located(confirm)).click()
# alert = driver.switch_to.alert
# time.sleep(10)
# alert.dismiss()

#prompt alert
wait.until(ec.presence_of_element_located(prompt)).click()
alert = driver.switch_to.alert


alert.send_keys("rohini")
time.sleep(10)


