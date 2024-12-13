import requests
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
'''
broken links - which doesnt have any target page
>400 -> represent broken link

capture all link from webpage
read aall link
display in console
capture using href
-install request package
'''
alllinks=driver.find_elements("tag name","a")
count=0
for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, " is broken link")
        count+=1
    else:
        print(url,"valid link")

print("total number of broken links : ",count)



