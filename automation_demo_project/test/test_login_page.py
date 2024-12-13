import pytest
from selenium import webdriver

from automation_demo_project.pages.login_page import login_page
from automation_demo_project.configuration.config import TestData

# @pytest.mark.usefixtures("init_driver")
class Test_Login:
    def test_login(self,init_driver):

        self.driver.get(TestData.url)
        # driver=webdriver.Chrome()
        self.lp = login_page(self.driver)
        self.lp.setUsername(TestData.username)
        self.lp.setPassword(TestData.password)
        self.lp.do_click()

