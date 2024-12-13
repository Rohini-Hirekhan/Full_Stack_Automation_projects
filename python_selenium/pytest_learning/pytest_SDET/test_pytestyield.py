import pytest
"""
fixture -> execute before test method
yieldd - execute after test method
"""

@pytest.fixture()
def setup():
    print("before test")
    yield
    print("after test")

def test1(setup):
    print("test")

def test2(setup):
    print("test2")