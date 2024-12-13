


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

