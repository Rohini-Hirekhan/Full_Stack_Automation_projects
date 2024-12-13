from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Firefox()
driver.get("https://securelayer7.bugdazz.com/a/login")
# driver.get("https://securelayer7.bugdazz.com")
driver.implicitly_wait(10)

driver.find_element("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[1]/div/div"
                            "/input").send_keys("daizyh777@gmail.com")
driver.implicitly_wait(10)
driver.find_element("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[2]/a/button").click()
driver.implicitly_wait(50)
driver.get("https://mail.google.com/mail/u/0/#spam/FMfcgzGtxTBXlcsMDGsHxmkVRtTWKrhL")
driver.find_element("id","identifierId").send_keys("daizyh777@gmail.com")


driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]"
                            "/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("Malakwade@777")
driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/"
                            "button/span").click()