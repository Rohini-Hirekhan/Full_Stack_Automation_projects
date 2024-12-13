#in brute force, attacker has one valid email and tries multiple passwords for the same user
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Chrome("C:\myData\Python_Automation\chromedriver\chromedriver-win32\chromedriver.exe")
driver.implicitly_wait(10)

df = pd.read_csv('bf_registerdata.csv').dropna()

for _,curr_row in df.iterrows():
    username = curr_row['username']
    mobile = curr_row['mobile']
    email = curr_row['emailid']
    password = curr_row['password']
    driver.implicitly_wait(10)
    driver.get("https://test.authsafe.ai/register.php")
    driver.find_element("id", "inputName").send_keys(username)
    driver.find_element("id","phone").send_keys(mobile)
    driver.find_element("id","inputEmail").send_keys(email)
    driver.find_element("name","password").send_keys(password)
    driver.find_element("id","register-button").click()
