from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import Select

dropdown_Ticket_xpath = "/html/body/app-root/div/app-app-layout/div/app-sidebar/header/nav/div[2]/ul/div[2]/li[5]/a"
text_addticket_xpath = "/html/body/app-root/div/app-app-layout/div/app-sidebar/header/nav/div[2]/ul/div[2]/li[5]/ul/li[1]/a"
selectprogram_id = "ID-5b1659c0-f7ac-46e7-a521-8a00c3f86875"
addFinding_xpath = "ticketSubmenu"
selectProgram_dropdown_xpath = "ID-9580d529-ce98-4adc-9971-07817c465b00"


select =Select(dropdown_Ticket_xpath)


def __init__(self, driver):
    self.driver = driver

def click_on_ticket(self):
    self.driver.findelement("xpath","dropdown_Ticket_xpath")
