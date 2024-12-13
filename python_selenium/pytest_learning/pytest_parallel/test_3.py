from selenium import webdriver
import pytest


def test_fb():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")