from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
wait = WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located("id","name"))



driver.find_element("id","name").send_keys("rohini")
driver.find_element("id","email").send_keys("rohini3.h@yopmail.com")
driver.find_element("id","phone").send_keys("998898980")
driver.find_element("id","textarea").send_keys("pune")

