import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
fr = driver.find_element("id","frame-one796456169")
driver.switch_to.frame(fr)
drp = Select(driver.find_element("id","RESULT_RadioButton-3"))

driver.find_element("id","RESULT_TextField-0").send_keys("rohini")
driver.find_element("xpath","//label[@for='RESULT_RadioButton-1_1']").click()

drp.select_by_value("Radio-0")
driver.find_element("id","FSsubmit").click()

driver.switch_to.default_content()
driver.find_element("id","name").send_keys("rohini")
time.sleep(10)

