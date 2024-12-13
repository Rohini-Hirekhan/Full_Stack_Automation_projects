import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class login_page():

    xpath_username = ("xpath", "//input[@placeholder='Username']")
    xpath_password = ("xpath", "(//input[@placeholder='Password'])[1]")
    xpath_login = ("xpath", "//button[normalize-space()='Login']")
    name_license = ("name", "license")

    # LoginPage
    def login(self):
        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located(xpath_username)).send_keys("admin")
        wait.until(ec.visibility_of_element_located(xpath_password)).send_keys("admin@123")
        wait.until(ec.visibility_of_element_located(name_license)).send_keys()
        wait.until(ec.visibility_of_element_located(xpath_login)).click()

