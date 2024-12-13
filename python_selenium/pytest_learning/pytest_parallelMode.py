from selenium import webdriver
import pytest

""""
all test execute alphabetical order
parallel test - 
py.test -n 5 -> 5 browser will execute on same time from all test classes
every test will run simultaneously in perticular window
Run test in group :
1) can create no of markers then execute based on marker also can do parallel execution
2) @pytest.mark.login - if we define this in above function then all fun with "login" marker it will execute by running command
cmd - py.test -m login
-m -> marker for login

jitne test hoge vo ek sath run hoge
"""
@pytest.mark.login
def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

def test_youtube():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
#
def test_fb():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")

