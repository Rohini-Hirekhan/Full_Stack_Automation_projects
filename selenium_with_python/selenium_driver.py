from selenium import webdriver
from selenium.webdriver.common.by import By
from webdiver_manager.Chrome import ChromeDriverManager
from webdiver_manager.firefox import GeckoDriverManage
from selenium.webdriver.common.selenium_manager import SeleniumManager


def web():
    # WebDriver driver = new ChromeDriver()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https:www.google.com")
web()