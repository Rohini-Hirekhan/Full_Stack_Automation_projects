from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

'''
implicit wait-
adv-
1) single statement
2) performance will not be reduced(if the element is available within the time it proceed to execute further statements)
disadv-if the element is not available within the time metioned,still there is chance of getting exception
1)
it will applicable for all element which is present from bottom of implicit wait
so specify it beginning of the script after driver is created.
it will not wait for maximum time out if element is got in 5 sec then it will not wait for 5sec
so performance issue will not be there
one implicit wait handling synchronization problem for throughout the script
default time is 0 secrets
application must be loaded in 10sec if not then report performance bug
'''
driver= webdriver.Chrome()
driver.implicitly_wait(10)