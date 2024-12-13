from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# whatever your browser version download that chromedriver exe and provide path of exe here

class login_page:

    username = ("xpath","//input[@placeholder='Username']")
    password = ("xpath","(//input[@placeholder='Password'])[1]")
    login = ("xpath","//button[normalize-space()='Login']")

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.findelement(self.username).send_keys(username)

    def setPassword(self,password):
        self.driver.findelement(self.password).send_keys(password)

    def do_click(self):
        self.driver.findelement(self.login).click()