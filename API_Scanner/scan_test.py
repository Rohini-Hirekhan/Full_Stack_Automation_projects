import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

xpath_username = ("xpath","//input[@placeholder='Username']")
xpath_password =("xpath","(//input[@placeholder='Password'])[1]")
xpath_login = ("xpath","//button[normalize-space()='Login']")
name_license =("name","license")

xpath_collectiondrp = ("xpath","//span[normalize-space()='Collections']")
xpath_newCollection = ("xpath","//a[normalize-space()='New collection']")


xpath_uploadCollection = ("xpath","//i[@class='fas fa-upload']")
xpath_collectionName = ("xpath","//input[@name='application_name']")
xpath_description = ("xpath","//textarea[@name='description']")
xpath_selectscanType =("xpath","//select[@name='testcase_type']")
xpath_selectAuthType = ("xpath","//select[@name='auth_type']")
xpath_baseURL = ("xpath","//input[@name='base_url']")
xpath_naxtbtn = ("xpath","//button[normalize-space()='Next']")

xpath_nextpage = ("css selector","button[class='btn primary-btn mt-3']")
xpath_initiatescan = ("xpath","//button[normalize-space()='Save']")
xpath_continue = ("xpath","//button[normalize-space()='Continue']")

xpath_runScan =("xpath","//button[normalize-space()='Run a Scan']")



driver = webdriver.Chrome()
driver.get("http://localhost:9090/#/login")
driver.maximize_window()

#LoginPage
wait = WebDriverWait(driver,20)
wait.until(ec.visibility_of_element_located(xpath_username)).send_keys("admin")
wait.until(ec.visibility_of_element_located(xpath_password)).send_keys("admin@123")
wait.until(ec.visibility_of_element_located(name_license)).send_keys("t7pqPWQldg8tO1IHPMcasvVzeRkB5+SNTzbNl/sh+xWYVAnjN9d3WeaQuECkfhIxrR4wfMHLJm5soxQprk6f6xH8cnef4KS+mWU9ySWjxBE=")
wait.until(ec.visibility_of_element_located(xpath_login)).click()

# 1 sensfrx-------------------------------------------------------------------------------------
#Collections-NewCollection
wait.until(ec.visibility_of_element_located(xpath_collectiondrp)).click()
wait.until(ec.visibility_of_element_located(xpath_newCollection)).click()

#step1-collection details
WebDriverWait(driver,20).until(ec.presence_of_element_located(xpath_uploadCollection)).click()
# send_keys("C:/Users/HP/PycharmProjects/API_Scanner/files/sensfrx.json")
time.sleep(1)
pyautogui.write(r"C:\Users\HP\Downloads\scan_data\sensfrx.json")
time.sleep(1)
pyautogui.press('enter')

# file_input = WebDriverWait(driver,20).until(ec.element_to_be_clickable(xpath_uploadCollection))
# driver.execute_script("arguments[0].style.display = 'block';", file_input)  # Ensure element is visible
# file_input.send_keys("files/sensfrx.json")

wait.until(ec.visibility_of_element_located(xpath_collectionName)).send_keys("sensfrx_collection")
wait.until(ec.visibility_of_element_located(xpath_description)).send_keys("description - sensfrx collection")
drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectscanType)))
drp.select_by_value("authenticated")

drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectAuthType)))
drp.select_by_value("1")

wait.until(ec.visibility_of_element_located(xpath_baseURL)).send_keys("www.baserl.com")
wait.until(ec.visibility_of_element_located(xpath_naxtbtn)).click()

wait.until(ec.visibility_of_element_located(xpath_nextpage)).click()
wait.until(ec.visibility_of_element_located(xpath_initiatescan)).click()
wait.until(ec.visibility_of_element_located(xpath_continue)).click()

# wait.until(ec.visibility_of_element_located(xpath_runScan)).click()
time.sleep(10)
#2 swagger------------------------------------------------------------------------------
wait.until(ec.visibility_of_element_located(xpath_collectiondrp)).click()
wait.until(ec.visibility_of_element_located(xpath_newCollection)).click()

#step1-collection details
WebDriverWait(driver,30).until(ec.presence_of_element_located(xpath_uploadCollection)).click()
# send_keys("C:/Users/HP/PycharmProjects/API_Scanner/files/sensfrx.json")
time.sleep(1)
pyautogui.write(r"C:\Users\HP\Downloads\scan_data\API.swagger_collection2.json")
time.sleep(1)
pyautogui.press('enter')

# file_input = WebDriverWait(driver,20).until(ec.element_to_be_clickable(xpath_uploadCollection))
# driver.execute_script("arguments[0].style.display = 'block';", file_input)  # Ensure element is visible
# file_input.send_keys("files/sensfrx.json")

wait.until(ec.visibility_of_element_located(xpath_collectionName)).send_keys("swagger_collection")
wait.until(ec.visibility_of_element_located(xpath_description)).send_keys("description")
drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectscanType)))
drp.select_by_value("authenticated")

drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectAuthType)))
drp.select_by_value("1")

wait.until(ec.visibility_of_element_located(xpath_baseURL)).send_keys("www.baserl.com")
wait.until(ec.visibility_of_element_located(xpath_naxtbtn)).click()

wait.until(ec.visibility_of_element_located(xpath_nextpage)).click()
wait.until(ec.visibility_of_element_located(xpath_initiatescan)).click()
wait.until(ec.visibility_of_element_located(xpath_continue)).click()
# wait.until(ec.visibility_of_element_located(xpath_runScan)).click()
#3 haircut-----------------------------------------------------------------------------------------


wait.until(ec.visibility_of_element_located(xpath_collectiondrp)).click()
wait.until(ec.visibility_of_element_located(xpath_newCollection)).click()

#step1-collection details
WebDriverWait(driver,30).until(ec.presence_of_element_located(xpath_uploadCollection)).click()
# send_keys("C:/Users/HP/PycharmProjects/API_Scanner/files/sensfrx.json")
time.sleep(1)
pyautogui.write(r"C:\Users\HP\Downloads\scan_data\Haircut Store API-withdocs.json")
time.sleep(1)
pyautogui.press('enter')

# file_input = WebDriverWait(driver,20).until(ec.element_to_be_clickable(xpath_uploadCollection))
# driver.execute_script("arguments[0].style.display = 'block';", file_input)  # Ensure element is visible
# file_input.send_keys("files/sensfrx.json")

wait.until(ec.visibility_of_element_located(xpath_collectionName)).send_keys("hair_cut_store_collection")
wait.until(ec.visibility_of_element_located(xpath_description)).send_keys("description")
drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectscanType)))
drp.select_by_value("authenticated")

drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectAuthType)))
drp.select_by_value("1")

wait.until(ec.visibility_of_element_located(xpath_baseURL)).send_keys("www.baserl.com")
wait.until(ec.visibility_of_element_located(xpath_naxtbtn)).click()

wait.until(ec.visibility_of_element_located(xpath_nextpage)).click()
wait.until(ec.visibility_of_element_located(xpath_initiatescan)).click()
wait.until(ec.visibility_of_element_located(xpath_continue)).click()
# wait.until(ec.visibility_of_element_located(xpath_runScan)).click()


#4 zoho crm----------------------------------------------------------------------------------------------------
wait.until(ec.visibility_of_element_located(xpath_collectiondrp)).click()
wait.until(ec.visibility_of_element_located(xpath_newCollection)).click()

#step1-collection details
WebDriverWait(driver,20).until(ec.presence_of_element_located(xpath_uploadCollection)).click()
# send_keys("C:/Users/HP/PycharmProjects/API_Scanner/files/sensfrx.json")
time.sleep(1)
pyautogui.write(r"C:\Users\HP\Downloads\scan_data\Zoho CRM REST APIs.postman_collection (3).json")
time.sleep(1)
pyautogui.press('enter')

# file_input = WebDriverWait(driver,20).until(ec.element_to_be_clickable(xpath_uploadCollection))
# driver.execute_script("arguments[0].style.display = 'block';", file_input)  # Ensure element is visible
# file_input.send_keys("files/sensfrx.json")

wait.until(ec.visibility_of_element_located(xpath_collectionName)).send_keys("zoho crm rest api")
wait.until(ec.visibility_of_element_located(xpath_description)).send_keys("description")
drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectscanType)))
drp.select_by_value("authenticated")

drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectAuthType)))
drp.select_by_value("1")

wait.until(ec.visibility_of_element_located(xpath_baseURL)).send_keys("www.baserl.com")
wait.until(ec.visibility_of_element_located(xpath_naxtbtn)).click()

wait.until(ec.visibility_of_element_located(xpath_nextpage)).click()
wait.until(ec.visibility_of_element_located(xpath_initiatescan)).click()
wait.until(ec.visibility_of_element_located(xpath_continue)).click()

wait.until(ec.visibility_of_element_located(xpath_runScan)).click()
#5 zoho desk api --------------------------------------------------------------------------------------------
wait.until(ec.visibility_of_element_located(xpath_collectiondrp)).click()
wait.until(ec.visibility_of_element_located(xpath_newCollection)).click()

#step1-collection details
WebDriverWait(driver,20).until(ec.presence_of_element_located(xpath_uploadCollection)).click()
# send_keys("C:/Users/HP/PycharmProjects/API_Scanner/files/sensfrx.json")
time.sleep(1)
pyautogui.write(r"C:\Users\HP\Downloads\scan\Zoho Desk API.postman_collection.json")
time.sleep(1)
pyautogui.press('enter')

# file_input = WebDriverWait(driver,20).until(ec.element_to_be_clickable(xpath_uploadCollection))
# driver.execute_script("arguments[0].style.display = 'block';", file_input)  # Ensure element is visible
# file_input.send_keys("files/sensfrx.json")

wait.until(ec.visibility_of_element_located(xpath_collectionName)).send_keys("sensfrx_collection")
wait.until(ec.visibility_of_element_located(xpath_description)).send_keys("description")
drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectscanType)))
drp.select_by_value("authenticated")

drp=Select(wait.until(ec.visibility_of_element_located(xpath_selectAuthType)))
drp.select_by_value("1")

wait.until(ec.visibility_of_element_located(xpath_baseURL)).send_keys("www.baserl.com")
wait.until(ec.visibility_of_element_located(xpath_naxtbtn)).click()

wait.until(ec.visibility_of_element_located(xpath_nextpage)).click()
wait.until(ec.visibility_of_element_located(xpath_initiatescan)).click()
wait.until(ec.visibility_of_element_located(xpath_continue)).click()

wait.until(ec.visibility_of_element_located(xpath_runScan)).click()