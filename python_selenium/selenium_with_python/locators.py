
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Chrome()


driver.implicitly_wait(10)
driver.get("https://demo.authsafe.ai/login.php")
link=driver.find_element("link text", "Login")
print(link)
driver.implicitly_wait(70)

# driver.find_element("id", "inputEmail").send_keys("admin1")
# driver.find_element("name", "password").send_keys("admin1")
#
# driver.find_element("id", "login-button").click()

driver.get("https://yopmail.com/wm")
#click on first mail
# driver.find_element("xpath","/html/body/div[2]/div[2]/button").click()
#enter email on yopmail
driver.find_element("id","login").send_keys("rohini7.h@yopmail.com")
#click on login button on yopmail
driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div/div[4]/button/i").click()
driver.implicitly_wait(10)
# driver.find_element("id","refresh").click()
driver.switch_to.frame('ifmail')
# driver.find_element("xpath","/html/body/header/div[3]/div[4]/button/span").click()
#login button of yopmail mail
print("hi")
loginlink=driver.find_element("link text","Login")
links = loginlink.get_attribute("href")
print(links)
driver.get(loginlink)

"""
id
name
link text
css selector
class name
tag name
partial link text

"""