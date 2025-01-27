from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.wait import WebDriverWait
# # there are two types of wait
# static wait -
# dynamic wait - we have given 10 sec time but element found in 5sec then rest of the time will be ignored.
# 2 types of dynamic wait -> 1) implicit wait 2) explicit wait

driver = webdriver.Chrome()
#1) explicit wait
#declaration of explicit wait
obj = WebDriverWait(driver,10)
obj = WebDriverWait(driver,10,poll_frequency=2,ignored_exception = [NoSuchElemetException,ElementNotVisibleException,Excetion])
#usage of explicit wait
element = obj.until(EC.presence_of_element_located(("xpath","")))


# # 5) wait commands - to solve synchronization problem we use wait statements
# # sometimes scripts run faster than application so application is not sync with scripts
# # 1) implicit wait
# # 2) explicit wait
# # time.sleep()-
# # adv -
# # 1)simple to use
# # disadvantage -
# # it took maximum time out for all elements
# # 1) performance of the script is very poor
# # 2) if the element is not available within the time metioned,still there is chance of getting exception
# # implicit wait-
# # adv-
# # 1) single statement
# # 2) performance will not be reduced(if the element is available within the time it proceed to execute further statements)
# # disadv-if the element is not available within the time metioned,still there is chance of getting exception
# # 1)
# # it will applicable for all element which is present from bottom of implicit wait
# # so specify it beginning of the script after driver is created.
# # it will not wait for maximum time out if element is got in 5 sec then it will not wait for 5sec
# # so performance issue will not be there
# # one implicit wait handling synchronization problem for throughout the script
# # default time is 0 secrets
# # application must be loaded in 10sec if not then report performance bug
#
# 3) explicit wait
# it worked based on the condition not based on the time
# for condition we need element
# to use this we need to define predefine class named as "WebDriverWait"
# WebDriverWait - it will take 2 arguments
# 1) driver instance
# 2) maximum time out but this is not time
# - explicit wait declaration -> obj = WebDriverWait(driver,10)
# - all condition can be used through this "obj" only
# - when we use explicit wait then no need to use find element method
# usage of explicit wait - element = obj.until(EC.presence_of_element_located(("xpath","")
# until method is wait until that condition becomes true means if condition is present
# if condition is satisfied it will return element
# all the condition will be displayed through EC object
# que - if element is not present? - if condition will not satisfy(if element is not on the webpage) so it will wait until given time
# then quit or come out from that and execute next statement
# que - it worked o codition then why we specify time? -
# if element not found it will throw exception so we can add new parameter to webdriverwait
# obj = WebDriverWait(driver,10,poll_frequency=2,ignored_exception = [NoSuchElemetException,ElementNotVisibleException,Excetion])
# disadv -
# 1) multiple places - written for every element
# 2) feel some difficulty
# poll_frequency - it will find element in given time period
# poll_frequency should be less than total time.
#



