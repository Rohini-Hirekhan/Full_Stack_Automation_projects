import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

dp =("id","datepicker")

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
wait = WebDriverWait(driver,10)
date_picker=wait.until(ec.visibility_of_element_located(dp))
# date_picker.click()
date_picker.send_keys("02/02/1996")
time.sleep(10)
# //input[@id='datepicker']
# email_id = wait.until(ec.visibility_of_element_located(By.ID,"username"))
# email_id.send_keys('test@gmail.com')