import pytest

@pytest.yield_fixture()
def setup():
    print("execute once before every method")
    yield
    print("excute after every fixture")

def testmethod1(setup):
    print("this is test method1")

def testmethod2(setup):
    print("this is test method 2")

