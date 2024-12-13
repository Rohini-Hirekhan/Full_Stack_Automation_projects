import pytest
from Ticket_module.Pages.LoginPage.login_through_yopmail import Login_Page
from config.config import TestData
# from Ticket_module.Pages.add_ticket_step1 import Add_Ticket_step1
from Ticket_module.Pages.add_user_page import add_user


@pytest.mark.usefixtures("init_driver")
class Test_AddUser():
    @pytest.mark.login
    def test_adduser(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        self.lp = Login_Page(self.driver)
        self.lp.setemail()
        self.lp.click_on_login()
        self.driver.maximize_window()
        self.driver.get(TestData.YOPMAIL_URL)
        # self.lp.login_to_yopmail()
        self.lp.login_to_yopmail()

        self.adduser = add_user(self.driver)
        self.adduser.click_on_teammanagement()
        self.adduser.click_on_users()


        # title = self.adduser.get_title_adduser(TestData.ADD_USER_TITLE)
        # assert title == TestData.ADD_USER_TITLE

        # self.adduser.click_on_addnewuser()



