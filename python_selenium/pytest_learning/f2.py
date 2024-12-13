import pytest

@pytest.fixture()
def setup():
    print("execute once before every method")

def testmethod1(setup):
    print("this is test method1")

def testmethod2(setup):
    print("this is test method 2")

