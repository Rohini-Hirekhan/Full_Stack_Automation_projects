from selenium import webdriver
from selenium.webdriver.support.select import Select


"""
headless mode - execute script without any UI
test case execute in backend
disadvantage -
1)while executing sceipt in headless - can not perform other activities
2) if u newly joined you dont know the flow then how u will know whether it is properly doing or not
advantage - 
1) can do multiple task parallely - you can minimize window and can do other task parallely
2) script execution very fast
It is useful when u already perform multiple round of execution of automation script
before relese /sign up



"""
def headless_chrome():
    driver= webdriver.Chrome()
    ops=webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=None,options=ops)
    return driver

driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
