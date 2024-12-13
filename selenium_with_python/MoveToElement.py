from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
"""Move to element"""
# create webelement
login_ele = driver.find_element(By.ID,"")
#use "ActionChains" and pass driver, create reference
act_chains = ActionChains(driver)
#user "ActionChains" methods to move element by using created webelement
#whenever you use ActionChain methods you have to always use perform() -> to perform actions
#MoveToElement - it moves the mouse cursor to a specific element on a web page.
act_chains.move_to_element(login_ele).perform()
#mouse ke hover par per dropdown open hota hai tab ye method use hoti hai