from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#select single checkbox
# driver.find_element("id","monday").click()


#select all the checkboxes
ch=driver.find_elements("xpath","//input[@type='checkbox' and @class='form-check-input']")
# print(len(ch)) #7
# print(ch)

#approach 1
# for i in range(len(ch)):
#     ch[i].click()

#approach2
# for i in ch:
#     i.click()

# select checkboxes based on my choise
# for checkbox in ch:
#     weekname=checkbox.get_attribute("id")
#     if weekname == "monday":
#          checkbox.click()

# select last 2 checkbox
# select first 2 checkbox

# for checkbox in range(0,len(ch)-4):
#     ch[checkbox].click()

# clearing all the checkboxes
for checkbox in ch:
    if checkbox.is_selected():
        checkbox.click()