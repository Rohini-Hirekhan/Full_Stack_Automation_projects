from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.wait import WebDriverWait

'''
3) explicit wait
it worked based on the condition not based on the time for condition we need element to use this we need to define predefine
 class named as "WebDriverWait"
WebDriverWait - it will take 2 arguments
1) driver instance
2) maximum time out but this is not time
- explicit wait declaration -> obj = WebDriverWait(driver,10)
- all condition can be used through this "obj" only
- when we use explicit wait then no need to use find element method
usage of explicit wait - element = obj.until(EC.presence_of_element_located(("xpath","")
until method is wait until that condition becomes true means if condition is present if condition is satisfied it will return
 element
all the condition will be displayed through EC object
que - if element is not present? - if condition will not satisfy(if element is not on the webpage) so it will wait until given time
then quit or come out from that and execute next statement
que - it worked o codition then why we specify time? -
if element not found it will throw exception so we can add new parameter to webdriverwait
obj = WebDriverWait(driver,10,poll_frequency=2,ignored_exception = [NoSuchElemetException,ElementNotVisibleException,Excetion])
disadv -
1) multiple places - written for every element
2) feel some difficulty
poll_frequency - it will find element in given time period
poll_frequency should be less than total time.

'''
#sometimes it takes time to display login page so we need to apply wait for particular webelement only
#use to solve synchronization issues

# time.sleep(5) it will wait for 5s even if element get early - performance of the script is very poor

driver = webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
#explicit wait declaration
wait = WebDriverWait(driver,10)
#usage of explicit wait
email_id = wait.until(ec.visibility_of_element_located(By.ID,"username"))
email_id.send_keys('test@gmail.com')

obj = WebDriverWait(driver,10,poll_frequency=2,ignored_exception = [NoSuchElemetException,ElementNotVisibleException,Excetion])

'''
wait = WebDriverWait(driver,10)
 #once it will visible on page then it will give you webelement
 email_id = wait.until(ec.presence_of_element_located((By.ID,'username')))
 email_id.send_keys("test@gmail.com")

wait = WebDriverWait(driver, 10)
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'ul.footer-nav li')))
#or can use this method as well
footer_links = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR,'ul.footer-nav li')))
print(len(footer_links))

for ele in footer_links:
    print(ele.text)


wait.until(ec.frame_to_be_available_And_switch_to_it(By.ID,'test'))
#check element from check box is selected or not
wait.until(ec.element_to_be_selected('checkbox'))


#webdriver explicit wait can be applied for non webelement,frames,url,alerts,single or multiple webelements


'''




















