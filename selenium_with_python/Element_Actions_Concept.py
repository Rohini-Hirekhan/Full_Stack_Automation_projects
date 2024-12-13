

#launch browser
#get url -https://classic.crmpro.com/
username = driver.find_element(By.NAME, "username")
login = driver.find_element(By.NAME, "login")
login_button_ele = driver.find_element(By.XPATH,"")

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username , "rohini").perform()
act_chains.send_keys_to_element(password , "rohini123").perform()
act_chains.click(login_button_ele).perform()

