from selenium import webdriver
from selenium.webdriver.support.select import Select

ops = webdriver.ChromeOptions
ops.add_argument("--disable-notification")

driver = webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/")
