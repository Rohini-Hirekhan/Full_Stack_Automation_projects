import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixtures(params =["chrome" ,"firefox"] ,scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver= webdriver.Firefox(executable_path = GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()
