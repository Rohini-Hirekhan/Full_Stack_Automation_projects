from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains

"""
bootstrap dropdown - 

"""

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element("xpath","//span[@id='select2-billing_country-container']").click()

country_list = driver.find_elements("xpath","//ul[@id='select2-billing_country-results']/li")
print(len(country_list))

#i is a webelement - so to capture text from webelement by using text
for i in country_list:
    # print(i.text)
    if i.text == "India":
        i.click()

