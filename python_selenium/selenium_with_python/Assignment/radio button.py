from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element("id","male").click()
driver.find_element("id","female").click()