import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
        "username , password",
        [
            ("admin@gmail.com", "admin@123"),
            ("naveen@gmail.com", "naveen123"),
        ]
    )
    def test_login(self,username,password):
        """This method is use to login to hubsopt application"""
        self.driver.get("https://app.hubspot.com")
        self.driver.find_element(By.ID, "username").sendkeys(username)
        self.driver.find_element(By.ID,"password").sendkeys(password)