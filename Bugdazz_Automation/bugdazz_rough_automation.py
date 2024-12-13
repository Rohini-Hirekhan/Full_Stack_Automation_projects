from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Firefox()

# driver.get("https://outlook.office.com/mail/inbox")
driver.get("https://securelayer7.bugdazz.com/a/login")
driver.implicitly_wait(10)
driver.find_element("xpath","/html/body/app-root/div/app-session-layout/section/app-login/div/div/div[4]/div/a/div/span").click()


# driver.get("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=191dfa42-6e83-4310-af24-dc71e2c9f3d7&scope=user.read openid profile offline_access&redirect_uri=https%3A%2F%2Fsecurelayer7.bugdazz.com%2Fdashboard&client-request-id=f1d424ff-d179-45b2-9879-bea4e263a985&response_mode=fragment&response_type=code&x-client-SKU=msal.js.browser&x-client-VER=2.32.1&client_info=1&code_challenge=rLob7GNHmTmE2jlH-v457RZSAT7qq2jAiDPZeKbkT-Y&code_challenge_method=S256&nonce=9bd94e9a-abdd-4d6b-abe6-e655b98c4258&state=eyJpZCI6ImQ1MTkxODNmLTE4NWQtNDBiMy04YTdhLTg2MzQ0MWNiMzY3ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicG9wdXAifX0%3D")
driver.find_element("id","i0116").send_keys("rohini.hirekhan@securelayer7.net")
driver.find_element("id","idSIButton9").click()
driver.find_element("id","i0118").send_keys("daizy@777")
driver.find_element("id","idSIButton9").click()

# //*[@id="i0116"]