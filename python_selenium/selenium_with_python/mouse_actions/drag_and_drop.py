from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains



driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# source element
source_ele = driver.find_element("xpath","//div[@id='box6']")
# destination element
target_ele = driver.find_element("xpath","//div[@id='box106']")

act = ActionChains(driver)
# drag and drop
act.drag_and_drop(source_ele,target_ele).perform()
