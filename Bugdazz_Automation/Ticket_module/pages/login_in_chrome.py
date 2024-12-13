from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://securelayer7.bugdazz.com/a/login")
# driver.get("https://securelayer7.bugdazz.com")
driver.implicitly_wait(50)
# microsoft login btn
# wait = WebDriverWait(driver, 10)
# microsoft_login = wait.until(ec.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/app-session-layout/section/app-login/div/div/div[4]/div/a/div/span")))
# microsoft_login.click()
# print("hi")
# click_ticket = wait.until(ec.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/app-app-layout/div/app-sidebar/header/nav/div[2]/ul/div[2]/li[5]/a")))
# click_ticket.click()
# driver.implicitly_wait(50)
# /html/body/app-root/div/app-session-layout/section/app-login/div/div/div[4]/div/a/div/span
# driver.find_element("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/div[4]/div/a/div").click()
# driver.implicitly_wait(30)
#through logic mail
#enter email in email id field
driver.find_element("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[1]/div/div/input").send_keys("rohini7.h@yopmail.com")
driver.implicitly_wait(10)
#click on login button
driver.find_element("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[2]/a/button").click()
driver.implicitly_wait(50)
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
loginlink= driver.find_element("link text","Login").get_attribute("href")
driver.get(loginlink)

driver.implicitly_wait(30)
print("hello")
# login=driver.find_element("xpath","/html/body/main/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/a")
# login.click()
# print("hello")
# driver.implicitly_wait(50)

#click login button using explicit wait
# wait = WebDriverWait(driver, 10)
# login = wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/main/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/a')))
# login.click()
# print("hello")
# driver.implicitly_wait(50)

#click on login button using ActionChain
# login = driver.find_element("xpath","/html/body/main/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/a")
# act_chains = ActionChains(driver)
# driver.implicitly_wait(50)
# act_chains.move_to_element(login).perform()
# print("hello")
driver.switch_to.default_content()
print("rohini")
# /html/body/main/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/a
# driver.find_element("Link_Text","https://securelayer7.bugdazz.com/a/verify?token=$2y$10$zZH7/8vj6FiBZapI3aqYNex1TsFUe7XcbnVOyGpPBpwc42zttda8a")
# driver.quit()

# //*[@id="ID-9856f125-2d60-4944-8bda-b5662f960523"]
