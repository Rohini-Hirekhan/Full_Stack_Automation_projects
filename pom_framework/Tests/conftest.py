"""Global fixture for all test cases"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from Config.config import TestData


@pytest.fixture(params=["chrome","firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # web_driver = webdriver.Chrome(executable_path = TestData.CHROME_EXECUTABLE_PATH)
        driver = webdriver.Chrome()
    if request.param == "firefox":
        # web_driver = webdriver.Chrome(executable_path = TestData.FIREFOX_EXECUTABLE_PATH)
        driver = webdriver.Firefox()
    request.cls.driver = web_driver
    # web_driver.implicitly_wait(10)
    yield
    web_driver.close()
