import pytest

#all the test should start with "test" keyword or end with "test" keyword
driver= None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("------------setup----------------")
    driver = webdriver.Chrome()
    driver.implicitely_wait(10)
    driver.delete_all_cookies()
    driver.get("")

    yield
    print("-----------tear down--------------")
    driver.quit()

 # method 1 to use fixture
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"

# method 2 to use fixtures
def test_fb_title(init_driver):
    assert driver.title == "Google"


