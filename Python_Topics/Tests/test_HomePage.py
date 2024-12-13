from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):
    def test_home_page_title(self):
        self.loginpage=LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITILE)
        assert title == TestData.HOME_PAGE_TITILE


    def test_home_page_header(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homepage.get_header_value()
        assert header== TestData.HOME_PAGE_HEADER

    def test_account_name_value(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homepage.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_settings_icon(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homepage.is_settings_icon_exist()
