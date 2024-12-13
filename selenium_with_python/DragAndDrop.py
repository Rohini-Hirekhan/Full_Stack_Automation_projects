

#create webelement of source element
source = driver.find_element(By.ID,"")
#create webelement of target element
target = driver.find_element(By.ID,"")
#create ActionChains class object
act_chains = ActionChains(driver)
#perform drag drop operation on source and target element
act_chains.drag_and_drop(source,target).perform()

#how to perform multiple ways
# 1)click and hold
# 2)move to particular method
# 3)release
act_chains.click_and_hold(source).move_to_element(target).release().perform()

#Right Click
