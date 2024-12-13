from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()

"""
frames(windows)/iframes(web aap)-
if any element is in frame then we have to switch to frame

selenium4 - 
switch_to.frame("name of the frame")
switch_to.frame(id of the frame)
switch_to.frame(webelement)
switch_to.frame(0)

html name -
frame
iframe
form

if we switch to one frame then if we want to switch to 2nd frame then we have to 
use - driver.switch_to.default_content() - go back to main page

inner frames -
outerframe ka webelement nikala ek variable me save kya
driver.switch_to.frame(outerframe)
innerframe =driver.findelement()
driver.switch_to.frame(innerframe)
driver.findelement().sendkeys()
driver.switch_to.parent_frame() #directly switch to parent frame(outer frame)

how to switch between browser window - 
ccurrent_window_handle ----> return windowID of single browser window
window_handles ------------> return window ID's of multiple browser windows


driver.switch_to.window(windowID)

 
"""

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.find_element("link text","org.openqa.selenium").click()

# -------------------------------------------------
# frame is webelement
# driver.switch_to.frame(2)
driver.switch_to.frame('main')
# main is name of frame
#or also you can create web element for it because frame is webelement then use function as
driver.switch_To_frame(frame_element)

# for come back
driver.switch_to.default_content()

#or
driver.switch_to.parenet_frame()

#if you have pop up where you have to login
#Authentication pop up
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")


 #then create web element

