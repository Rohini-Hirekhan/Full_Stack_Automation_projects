from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Ticket_module.Pages.trialanderror import Add_Ticket_step1
from config.config import TestData

txt_enteremail = ("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[1]/div/div/input")
btn_login =("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/form/div[2]/a/button")
txt_enteremailonyopmail = ("id","login")
btn_clickonlogintoyopmail =("xpath", "/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div/div[4]/button/i")
# driver = webdriver.Chrome()

class Login_Page:
    def __init__(self, driver):
        self.driver = driver


    #enter email in email id field
    def setemail(self):
        # self.driver.find_element(txt_enteremail_xpath).send_keys(TestData.EMAIL)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(txt_enteremail)).send_keys(TestData.EMAIL)
        # self.driver.implicitly_wait(10)
    #click on login button
    def click_on_login(self):
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(btn_login)).click()
        # self.driver.find_element("xpath",btn_login).click()
        # self.driver.implicitly_wait(50)

    def login_to_yopmail(self):
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(txt_enteremailonyopmail)).send_keys(TestData.YEMAIL)
        # self.driver.find_element("id",txt_enteremailonyopmail_id).send_keys(TestData.YEMAIL)
        #click on login button on yopmail
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(btn_clickonlogintoyopmail)).click()
        # self.driver.find_element("xpath",btn_clickonlogintoyopmail_xpath).click()
        # self.driver.implicitly_wait(10)
        self.driver.switch_to.frame('ifmail')
        loginlink= self.driver.find_element("link text","Login").get_attribute("href")
        self.driver.get(loginlink)

        self.driver.implicitly_wait(100)
        self.driver.switch_to.default_content()



