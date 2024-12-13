from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
"""

alert is not an webelement is a special type of object
how to handle alert -
alertwindow = driver.switch_to.alert - handle alert by using - switch to alert window
alertwindow.text - return text of the alert window
alertwindow.send_keys("welcome") - enter value to field on alert pop up
alertwindow.accept() - close aalert window by using OK button
alertwindow.dismiss() - close alert window by using cancel button

Authentication pop up- where asked for username and password
we can handle this situation by bypass(inject username and password in the url)
http://the-internet.herokuapp.com/basic_auth
syntax : http://username:password@test.com
example - http://admin:admin@the-internet.herokuapp.com/basic_auth

"""
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#open alert window
driver.find_element("xpath","//button[normalize-space()='Click for JS Prompt']").click()
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
# alertwindow.accept() #close aalert window by using OK button
alertwindow.dismiss() # close alert window by using cance button
# -----------------------------------------------------------

#Java Script Pop up Alert
driver.get("https://www.google.com")
alert = driver.switch_to_alert
print(alert.text)
alert.accept() #accept it , click on OK
alert.dismiss()#cancel the pop up
alert.send_keys("hi")

driver.switch_to_default_content()#come back to driver
