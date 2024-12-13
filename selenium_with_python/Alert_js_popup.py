
#Java Script Pop up Alert

alert = driver.switch_to_alert
print(alert.text)
alert.accept() #accept it , click on OK
alert.dismiss()#cancel the pop up
alert.send_keys("hi")

driver.switch_to_default_content()#come back to driver
