from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains


driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.switch_to.frame("iframeResult")

field1 = driver.find_element("","")
field1.clear()
field1.send_keys("welcome")

button = driver.find_element("","")

act = ActionChains(driver)
# perform double click action
act.double_click(button).perform()