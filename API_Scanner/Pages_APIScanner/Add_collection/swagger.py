import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from config.config import TestData

class Swagger():
    xpath_username = ("xpath","//input[@placeholder='Username']")
    xpath_password =("xpath","(//input[@placeholder='Password'])[1]")
    xpath_login = ("xpath","//button[normalize-space()='Login']")
    name_license =("name","license")

    xpath_collectiondrp = ("xpath","//span[normalize-space()='Collections']")
    xpath_newCollection = ("xpath","//a[normalize-space()='New collection']")


    xpath_uploadCollection = ("xpath","//i[@class='fas fa-upload']")
    xpath_collectionName = ("xpath","//input[@name='application_name']")
    xpath_description = ("xpath","//textarea[@name='description']")
    xpath_selectscanType =("xpath","//select[@name='testcase_type']")
    xpath_selectAuthType = ("xpath","//select[@name='auth_type']")
    xpath_baseURL = ("xpath","//input[@name='base_url']")
    xpath_naxtbtn = ("xpath","//button[normalize-space()='Next']")

    xpath_nextpage = ("css selector","button[class='btn primary-btn mt-3']")
    xpath_initiatescan = ("xpath","//button[normalize-space()='Save']")
    xpath_continue = ("xpath","//button[normalize-space()='Continue']")

    xpath_runScan = ("xpath", "//button[normalize-space()='Run a Scan']")

    def __init__(self,driver):
        self.driver = driver

    def initiate_scan(self):
        # self.driver.implicit_wait(20)
        #LoginPage
        self.wait = WebDriverWait(self.driver,30)
        # self.wait.until(ec.visibility_of_element_located(self.xpath_username)).send_keys("admin")
        # self.wait.until(ec.visibility_of_element_located(self.xpath_password)).send_keys("admin@123")
        # self.wait.until(ec.visibility_of_element_located(self.name_license)).send_keys("0OhYsg5IEgFfJL01oFInQ3MrLljeG2rRR70Q+Ss7OyFlmEqGqIBTkSjQHD+Qihqm11TaXdyDed3qhcNAI0ncJBuutuDVLwxWA/p4FgnnSmw=")
        # self.wait.until(ec.visibility_of_element_located(self.xpath_login)).click()

        #Collections-NewCollection
        self.wait.until(ec.visibility_of_element_located(self.xpath_collectiondrp)).click()
        self.wait.until(ec.visibility_of_element_located(self.xpath_newCollection)).click()

        #step1-collection details
        WebDriverWait(self.driver,20).until(ec.presence_of_element_located(self.xpath_uploadCollection)).click()

        time.sleep(1)
        pyautogui.write(r"C:\Users\HP\Downloads\scan_data\API.swagger_collection2.json")
        time.sleep(1)
        pyautogui.press('enter')

        self.wait.until(ec.visibility_of_element_located(self.xpath_collectionName)).send_keys("swagger_collection")
        self.wait.until(ec.visibility_of_element_located(self.xpath_description)).send_keys("description")
        self.drp=Select(self.wait.until(ec.visibility_of_element_located(self.xpath_selectscanType)))
        self.drp.select_by_value("authenticated")

        self.drp=Select(self.wait.until(ec.visibility_of_element_located(self.xpath_selectAuthType)))
        self.drp.select_by_value("1")
        time.sleep(3)
        WebDriverWait(self.driver,30).until(ec.visibility_of_element_located(self.xpath_baseURL)).send_keys("www.baserl.com")

        WebDriverWait(self.driver,30).until(ec.visibility_of_element_located(self.xpath_naxtbtn)).click()

        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(self.xpath_nextpage)).click()
        WebDriverWait(self.driver,30).until(ec.visibility_of_element_located(self.xpath_initiatescan)).click()
        WebDriverWait(self.driver,30).until(ec.visibility_of_element_located(self.xpath_continue)).click()

        WebDriverWait(self.driver,30).until(ec.visibility_of_element_located(self.xpath_runScan)).click()
        time.sleep(3)




