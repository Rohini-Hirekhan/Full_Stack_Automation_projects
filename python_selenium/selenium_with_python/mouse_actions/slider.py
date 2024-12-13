from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains

"""
slider element - drag_and_drop_by_offset(element,x,y)
"""

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider = driver.find_element("xpath","//body//div//span[1]")
max_slider = driver.find_element("xpath","//body//div//span[2]")
# {'x': 59, 'y': 250}
# {'x': 412, 'y': 250}
print(min_slider.location)
print(max_slider.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-42,0).perform()

print(min_slider.location)
print(max_slider.location)
# {'x': 158, 'y': 250}
# {'x': 370, 'y': 250}