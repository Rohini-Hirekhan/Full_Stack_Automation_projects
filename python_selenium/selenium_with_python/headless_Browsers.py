

#headless mode for chrome
Options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.reddit.com/")

#or
options = webdriver.ChromeOptions()
options.headless = false
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.reddit.com/")


#headless mode for firefox
Options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path = GeckoDriverManager().install(), options=options)
driver.get("https://www.reddit.com/")