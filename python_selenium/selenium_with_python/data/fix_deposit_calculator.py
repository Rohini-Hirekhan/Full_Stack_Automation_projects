import time

from selenium import webdriver
import openpyxl
from selenium.webdriver.support.ui import Select
from selenium_with_python.data import excel_utility

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

file ="C:\data\excel4.xlsx"
rows=excel_utility.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    price = excel_utility.readData(file,"Sheet1",r,1)
    rate_of_interest = excel_utility.readData(file, "Sheet1", r, 2)
    per1 = excel_utility.readData(file, "Sheet1", r, 3)
    per2 = excel_utility.readData(file, "Sheet1", r, 4)
    frequency = excel_utility.readData(file, "Sheet1", r, 5)
    exp_value = price = excel_utility.readData(file,"Sheet1",r,6)
#     passing data to the application
    driver.find_element("xpath","//input[@id='principal']").send_keys(price)
    driver.find_element("xpath","//input[@id='interest']").send_keys(rate_of_interest)
    driver.find_element("xpath", "//input[@id='tenure']").send_keys(per1)

    perioddrop=Select(driver.find_element("xpath","//select[@id='tenurePeriod']"))
    perioddrop.select_by_visible_text(per2)

    fre=Select(driver.find_element("xpath","//select[@id='frequency']"))
    fre.select_by_visible_text(frequency)

    driver.find_element("xpath","//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    act_val=driver.find_element("xpath","//span[id='resp_matval']/strong").text

    # validation
    if float(exp_value)==float(act_val):
        print("test pass")
        excel_utility.weiteData(file,"Sheet1",r,8,"Passed")

    else:
        print("test pass")
        excel_utility.weiteData(file, "Sheet1", r, 8, "failed")
    driver.find_element("xpath","//img[@class='PL5']").click()
    time.sleep(3)
