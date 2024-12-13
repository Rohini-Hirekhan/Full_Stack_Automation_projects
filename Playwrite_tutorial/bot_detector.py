from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://test.authsafe.ai/")
    page.locator("xpath=/html/body/div/nav/div/div/ul/li[12]/a").click()
    page.get_by_placeholder("Full Name").fill("daizy")
    page.get_by_placeholder("Mobile Number").fill("9098898909")
    page.get_by_placeholder("Email").fill("daizy@gmail.com")
    page.get_by_placeholder("Password").fill("123")
    page.get_by_role("button",name="Register").click()

# driver.find_element("link text", "Register").click()
# driver.find_element("id","inputName").send_keys("rohini123")
# driver.find_element("id","phone").send_keys("9098898784")
# driver.find_element("id","inputEmail").send_keys("rohini123@yopmail.com")
# driver.find_element("name","password").send_keys("rohini")
# driver.find_element("id","register-button").click()