from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

txt_enteremail_xpath = "/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[1]/div/div/input"
btn_login_xpath ="/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[2]/a/button"
txt_enteremailonyopmail_id = "login"
btn_clickonlogintoyopmail_xpath = "/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div/div[4]/button/i"
# driver = webdriver.Chrome()

class Login_Page:


    #enter email in email id field
    def setemail(self):
        driver.find_element("xpath",txt_enteremail_xpath).send_keys(TestData.EMAIL)
        driver.implicitly_wait(10)
    #click on login button
    def click_on_login(self):
        driver.find_element("xpath",btn_login_xpath).click()
        driver.implicitly_wait(50)

    def login_to_yopmail(self):
        driver.find_element("id",txt_enteremailonyopmail_id).send_keys(TestData.YEMAIL)
        #click on login button on yopmail
        driver.find_element("xpath",btn_clickonlogintoyopmail_xpath).click()
        driver.implicitly_wait(10)
        driver.switch_to.frame('ifmail')
        loginlink= driver.find_element("link text","Login").get_attribute("href")
        driver.get(loginlink)
        driver.implicitly_wait(30)
        driver.switch_to.default_content()
