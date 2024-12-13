import pytest
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from config.config import TestData


@pytest.fixture( scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
