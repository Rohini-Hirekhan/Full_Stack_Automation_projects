from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


xpath_Ticket_Module = ("xpath","/html/body/app-root/div/app-app-layout/div/app-sidebar/header/nav/div[2]/ul/div[2]/li[5]/a")

xpath_addticket_xpath = ("xpath","/html/body/app-root/div/app-app-layout/div/app-sidebar/header/nav/div[2]/ul/div[2]/li[5]/ul/li[1]/a")
# //*[@id="ID-81b8d50d-0a6e-4b4f-90f6-65bd72f4687b"]
# class="input-search ng-touched remove-rdius ng-invalid is-invalid ng-dirty"
# id = "ID-cf06909a-ca8d-4841-903f-b4c715509b64"
inputsearch_selectprogram_id = ("xpath","/html/body/app-root/div/app-app-layout/div/div/app-vulnerability-overview/section[2]/div/div/div/div/section/div/div/div[1]/form/div[1]/input-search-select-option/div/input")
selectProgram_dropdown_xpath = ("ID-9580d529-ce98-4adc-9971-07817c465b00")
text_Findingtitle_xpath = ("xpath","/html/body/app-root/div/app-app-layout/div/div/app-vulnerability-overview/section[2]/div/div/div/div/section/div/div/div[1]/form/div[2]/input")
# vulnerableasset
# affectmodule
btn_nextpage_xpath = ("xpath","/html/body/app-root/div/app-app-layout/div/div/app-vulnerability-overview/footer/div/div/div/button")


class Add_Ticket_step1:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self,title):
        WebDriverWait(self.driver , 100).until(EC.title_is(title))
        return self.get_title()
    def click_on_ticketModule(self):
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(xpath_Ticket_Module)).click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(xpath_addticket_xpath)).click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(inputsearch_selectprogram_id)).click()


    # def select_program(self):
    #     select = Select(dropdown_Ticket_xpath)
    #     select.
    # def set_findingtitle(self):
    #
    # def select_vulnerableasset(self):

    # def select_affectmodule(self):
    #
    # def click_nextpagebtn(Self):
    #
    #
    #
