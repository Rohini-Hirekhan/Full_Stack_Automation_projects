from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
driver.implicitly_wait(20)
drp_con=Select(driver.find_element("xpath","//select[@id='input-country']"))
#select is predefined class it will return select class object
drp_con.select_by_visible_text("India")

'''
select option from the dropdown
obj.select_by_visible_text('India")
obj.select_by_value("10) - here given value of value attribute
obj.select_by_index(13) - index will not shown on web page we will have to count this


capture all the options and print them
alloptions = obj.options
for i in alloptions:
    print(i.text())
    
'''
#capture all the options and print
alloption - drp_con.options #return all the option
print(len(alloption))

for i in alloption:
    print(i.text())

#select option from dropdown without using buit-in method
for i in alloptions:
    if i.text=="India":
        opt.click()
        break


