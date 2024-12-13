from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()

"""
Authentication pop up- where asked for username and password
we can handle this situation by bypass(inject username and password in the url)
http://the-internet.herokuapp.com/basic_auth
syntax : http://username:password@test.com
example - http://admin:admin@the-internet.herokuapp.com/basic_auth

"""

# driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
#by using sendkeys only enter value in one field what about password field so do bypass
# inject username and pass and bypass
