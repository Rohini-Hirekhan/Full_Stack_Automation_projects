#webdriver manager - no need to download .exe file for driver
# to install run cmd get from "webdriver manager link" - pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdiver_manager.Chrome import ChromeDriverManager
from webdiver_manager.firefox import GeckoDriverManager

browserName = "chrome"

if browserName == "chrome" :
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox" :
    driver = webdriver.Firefox(GeckoDriverManager().install())
elif browserName == "safari" :
    driver = webdriver.Safari()
else:
    print('pls pass the correct browser name : ' + browserName)





