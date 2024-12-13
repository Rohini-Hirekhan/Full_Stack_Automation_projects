from selenium import webdriver


"""
date picker/calendar
----------
1) standard - button,checkbox,img,links,radio button
2) non standard (customized)- those element which is not same for all page
date picker contains multiple standard elements
according to design need to write script

"""
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
# driver.find_element("xpath","//input[@id='datepicker']").send_keys("01/30/2022")
year = "2024"
month ="june"
date = "30"

driver.find_element("xpath","//input[@id='datepicker']").click()

while True:

    mon = driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
    yr = driver.find_element("xpath","//span[@class='ui-datepicker-year']").text
    if mon==month and year==yr:
        break;
    else:
        driver.find_element("xpath","//span[@class='ui-icon ui-icon-circle-triangle-e']")
