from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

xpath_click_on_teammanagement = ("xpath","/html/body/app-root/div/app-app-layout/div/app-sidebar/header/nav/div[2]/ul/div[2]/li[3]/a")
xpah_click_on_users = ("xpath","/html/body/app-root/div/app-app-layout/div/app-sidebar/header/nav/div[2]/ul/div[2]/li[3]/ul/li[1]/a")
xpath_click_on_addnewuser = ("xpath","/html/body/app-root/div/app-app-layout/div/div/app-invite-users/section[2]/div/div[2]/div/div[2]/button")
xpath_email=("xpath","/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-new-user-invite/mat-dialog-content/div/div/div/div/form/div/div[1]/div/input")
xpath_designation =("xpath","/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-new-user-invite/mat-dialog-content/div/div/div/div/form/div/div[2]/div/input")
xpath_usergroup = ("xpath","/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-new-user-invite/mat-dialog-content/div/div/div/div/form/div/div[3]/div/input-search-select-option/div/input")
xpath_timezone = ("xpath","/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-new-user-invite/mat-dialog-content/div/div/div/div/form/div/div[4]/div/input-search-select-option/div/input")
xpath_invite =("xpath","/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-new-user-invite/mat-dialog-actions/div/div")

class add_user():
    def __init__(self, driver):
        self.driver = driver

    def click_on_teammanagement(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpath_click_on_teammanagement)).click()

    def click_on_users(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpah_click_on_users)).click()
    #
    # def get_title_adduser(self,title):
    #     WebDriverWait(self.driver , 100).until(EC.title_is(title))
    #     return self.title(title)

    def click_on_addnewuser(self):
        click_button=WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(xpath_click_on_addnewuser))
        click_button.click()
    def enter_email(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpath_click_on_addnewuser)).sendkeys("r1@yopmail.com")

    def enter_designation(self):
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(xpath_click_on_addnewuser)).sendkeys("QA")

    def enter_usergroup(self):
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(xpath_click_on_addnewuser)).sendkeys("Admin")

    def enter_timezone(self):
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(xpath_click_on_addnewuser)).sendkeys("r1@yopmail.com")

    def click_on_invitebutton(self):
        click_button = WebDriverWait(self.driver, 500).until(EC.element_to_be_clickable(xpath_click_on_addnewuser))
        click_button.click()