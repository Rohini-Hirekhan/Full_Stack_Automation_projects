import pytest
from Pages.LoginPage.login_through_yopmail import Login_Page
from config.config import TestData
from Ticket_module.Pages.trialanderror import Add_Ticket_step1
# from Ticket_module.Pages.add_ticket_step1 import Add_Ticket_step1


@pytest.mark.usefixtures("init_driver")
class Test_002_step1:

    def test_home_page_title(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        self.lp = Login_Page(self.driver)
        self.lp.setemail()
        self.lp.click_on_login()
        self.driver.maximize_window()
        self.driver.get(TestData.YOPMAIL_URL)
        # self.lp.login_to_yopmail()
        self.lp.login_to_yopmail()

        self.stepone = Add_Ticket_step1(self.driver)

        title = self.stepone.get_title(TestData.HOME_PAGE_TITILE)
        assert title == TestData.HOME_PAGE_TITILE
        self.driver.maximize_window()
        self.stepone.click_on_ticketModule()
        # self.loginpage=LoginPage(self.driver)
        # homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # title = homepage.get_home_page_title(TestData.HOME_PAGE_TITILE)
        # assert title == TestData.HOME_PAGE_TITILE

    #
    # def test_login(self):
    #     self.driver.get(TestData.BASE_URL)
    #     self.lp=Login_Page(self.driver)
    #     self.lp.setemail()
    #     self.lp.click_on_login()
    #     self.driver.get(TestData.YOPMAIL_URL)
    #     self.stepone = self.lp.login_to_yopmail()
    #     self.stepone.click_on_ticketModule()
        # self.lp.login_to_yopmail()
        # self.stepone = Add_Ticket_step1(self.driver)
        # self.stepone.click_on_ticketModule()

