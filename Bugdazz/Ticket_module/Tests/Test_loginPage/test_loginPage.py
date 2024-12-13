import pytest
from Ticket_module.Pages.LoginPage.login_through_yopmail import Login_Page
from config.config import TestData


@pytest.mark.usefixtures("init_driver")
class Test_001_Login:
    def test_login(self):
        self.driver.get(TestData.BASE_URL)
        self.lp = Login_Page(self.driver)
        self.lp.setemail()
        self.lp.click_on_login()
        self.driver.get(TestData.YOPMAIL_URL)
        self.lp.login_to_yopmail()






