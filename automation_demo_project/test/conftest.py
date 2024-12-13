import pytest
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from automation_demo_project.configuration.config import TestData


@pytest.fixture()
def init_driver(request):
    # if request.param == "chrome":
        # web_driver = webdriver.Chrome(executable_path = TestData.CHROME_EXECUTABLE_PATH)
        driver = webdriver.Chrome()
    # if request.param == "firefox":
        # web_driver = webdriver.Chrome(executable_path = TestData.FIREFOX_EXECUTABLE_PATH)
        # driver = webdriver.Firefox()
        request.cls.driver = driver
    # web_driver.implicitly_wait(10)
        yield
        driver.close()