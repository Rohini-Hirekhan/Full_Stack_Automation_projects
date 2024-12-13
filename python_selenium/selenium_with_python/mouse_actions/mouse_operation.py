from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
"""
we have class to perform mouse operation to handle mouse actiona -
ActionChains

from selenium.webdriver.common.action_chains import ActionChains

1) Mouse hover - move_to_element(element)
2) Right click - context_click(webelement)
3) Double click - double_click(webelement)
4) Drag and drop - drag_and_drop(source_ele,target_ele)

slider element - drag_and_drop_by_offset(element,x,y)

scrolling - it is coming from browser not from application

"""
#MouseHover

admin = driver.find_element("","")
user = driver.find_element("","")

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(user).click().perform()
#without writing perform it will not perform any action
