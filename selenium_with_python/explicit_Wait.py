from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
#sometimes it takes time to display login page so we need to apply wait for particular webelement only
#use to solve synchronization issues

# time.sleep(5) it will wait for 5s even if element get early - performance of the script is very poor


wait = WebDriverWait(driver,10)
email_id = wait.until(ec.visibility_of_element_located(By.ID,"username"))
email_id.send_keys('test@gmail.com')




#
#
#  wait = WebDriverWait(driver,10)
#  #once it will visible on page then it will give you webelement
#  email_id = wait.until(ec.presence_of_element_located((By.ID,'username')))
#  email_id.send_keys("test@gmail.com")
#
# wait = WebDriverWait(driver, 10)
# footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'ul.footer-nav li')))
# #or can use this method as well
# footer_links = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR,'ul.footer-nav li')))
# print(len(footer_links))
#
# for ele in footer_links:
#     print(ele.text)
#
#
# wait.until(ec.frame_to_be_available_And_switch_to_it(By.ID,'test'))
# #check element from check box is selected or not
# wait.until(ec.element_to_be_selected('checkbox'))
#
#
# #webdriver explicit wait can be applied for non webelement,frames,url,alerts,single or multiple webelements





















