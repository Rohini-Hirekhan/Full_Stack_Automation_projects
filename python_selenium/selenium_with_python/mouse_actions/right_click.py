from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element("xpath","/html/body/div/section/div/div/div/p/span")

act = ActionChains(driver)
# crete action and then perform right click
act.context_click(button).perform()

# --------------------------------------------------------



"""right/context click"""
#create webelement
right_click_ele =

act_chain = ActionChains(driver)
act_chain.context_click(right_click_ele).perform()



#create collection of list to extract values
right_click_option = driver.find_Elements(By.CSS_SELECTOR,"")
for ele in right_click_option:
    print(ele.text)
    if ele.text == "copy":
        ele.click()
        break

