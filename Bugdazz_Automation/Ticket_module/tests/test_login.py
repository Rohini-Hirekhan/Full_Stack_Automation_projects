import pytest
from Pages.login_through_yopmail import LoginPage
from config.config import TestData
from tests.test_base import BaseTest

class Test_001_Login:
    def test_login(self,BaseTest):

        self.driver.get(TestData.BASE_URL)
        slf.lp = pages(self.driver)
        lp.setemail(TestData.EMAIL)
        lp.click_on_login()
        driver.get(TestData.YOPMAIL_URL)
        lp.login_to_yopmail()




