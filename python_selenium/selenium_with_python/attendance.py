from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

xpath_email =("xpath","/html/body/app-root/app-login/div/div/div/div[2]/div/div/app-login-page/div/div/div[1]/div[1]/mat-form-field/div[1]/div[2]/div/input")
xpath_nextbuttonclick =("xpath","/html/body/app-root/app-login/div/div/div/div[2]/div/div/app-login-page/div/div/div[1]/div[2]/button")
xpath_password =("xpath","/html/body/app-root/app-login/div/div/div/div[2]/div/div/app-login-page/div/div/div[3]/div[1]/mat-form-field/div[1]/div[2]/div[1]/input")
xpath_nxtbtn =("xpath","/html/body/app-root/app-login/div/div/div/div[2]/div/div/app-login-page/div/div/div[3]/div[3]/button[2]")
xpath_markattendance = ("xpath","/html/body/app-root/app-main/div/app-sidebar/mat-sidenav-container/mat-sidenav-content/div/app-social-enterpise-wall/div/app-social-wall-header/section/div/div[2]/div[1]/div[2]/div/button")
xpth_crossbtn =("xpath","/html/body/div[2]/div/div[3]/div/a/em")
# /html/body/div[2]/div/div[3]/div/a/em


driver = webdriver.Chrome()
driver.get("https://app.hrone.cloud/login")
driver.implicitly_wait(20)
WebDriverWait(driver, 100).until(EC.visibility_of_element_located(xpath_email)).send_keys("rohini.hirekhan@securelayer7.net")
WebDriverWait(driver, 100).until(EC.visibility_of_element_located(xpath_nextbuttonclick)).click()
WebDriverWait(driver, 100).until(EC.visibility_of_element_located(xpath_password)).send_keys("Daizy@777")


WebDriverWait(driver, 100).until(EC.visibility_of_element_located(xpath_nxtbtn)).click()

ops = webdriver.ChromeOptions
ops.add_argument("--disable-notification")
WebDriverWait(driver, 100).until(EC.visibility_of_element_located(xpth_crossbtn)).click()
WebDriverWait(driver, 100).until(EC.visibility_of_element_located(xpath_markattendance)).click()


#Java Script Pop up Alert

# alert = driver.switch_to_alert
# print(alert.text)
# alert.accept() #accept it , click on OK
# alert.dismiss()#cancel the pop up
# alert.send_keys("hi")
#
# driver.switch_to_default_content()#come back to driver