from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.wait import WebDriverWait


'''
3) browser commands
- close - 1) close single browser window (where driver should focused)but internally process is running(can close single browser at a time)
- quit() - 1) close all browser along with browser(it will close all browser and will kill the process)
'''

driver = webdriver(Chrome)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(300)
driver.find_element("link text","OrangeHRM, Inc").click()
# driver.find_element("xpath","/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
# driver.find_element("partial link text","OrangeHRM, I").click()
driver.implicitly_wait(100)
# driver.find_element("xpath","/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[1]").click()
driver.implicitly_wait(300)
driver.close()
# # //*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a