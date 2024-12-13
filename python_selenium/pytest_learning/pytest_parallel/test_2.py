from selenium import webdriver
import pytest

@pytest.mark.login
def test_youtube():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")