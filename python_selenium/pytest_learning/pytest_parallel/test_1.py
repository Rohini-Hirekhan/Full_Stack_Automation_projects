from selenium import webdriver
import pytest

@pytest.mark.login
def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

@pytest.mark.login
def test_insta():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")