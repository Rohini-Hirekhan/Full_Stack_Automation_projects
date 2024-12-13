from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
titlex = driver.title
print(titlex)
#click on first mail
# driver.find_element("xpath","/html/body/div[2]/div[2]/button").click()
#enter email on yopmail
# driver.find_element("id","login").send_keys("rohini7.h@yopmail.com")
#click on login button on yopmail
# driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div/div[4]/button/i").click()
# driver.implicitly_wait(10)
# driver.find_element("id","refresh").click()
# driver.switch_to.frame('ifmail')
# driver.find_element("xpath","/html/body/header/div[3]/div[4]/button/span").click()
#login button of yopmail mail
# print("hi")
# driver.find_element("link text","Login").click()
# driver.implicitly_wait(10)
# print("hello")
#
# loginlink= driver.find_element("link text","Login").get_attribute("href")
# url = loginlink
# links.click()
# print(url)
# driver.get(loginlink)
# print("run")