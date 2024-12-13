import pytest
import selenium import webdriver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://google.com")
        assert  self.driver.title == "Google"


# cmd to run -> pytest test_fixture.py -v -n 2