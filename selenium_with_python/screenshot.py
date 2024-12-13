#there is two ways to take screenshot
#one is direct take page ss and another way is to take full top to botton page ss

Options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.reddit.com/")
driver.get_screenshot_as_file('redit.png');

#second way for full screenshot
#make sure that you are running in headless mode

s= lambda X:driver.execute_Script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('width'),S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit.png');