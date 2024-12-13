import pytest

# execute methods multiple times
@pytest.fixture()
def setup():
    print("once before every method")
def testmathod(setup):
    print("test1")

def testmethod2(setup):
    print("method2")

