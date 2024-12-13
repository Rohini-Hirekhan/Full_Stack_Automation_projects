import pytest
@pytest.mark.login
def test_m1():
    a=2
    b=3
    assert a+1 == b , "test failed"
    assert a==b , "test failed if a is not eq to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

def test_m3():
    assert True

@pytest.mark.login
def test_m4():
    assert False

def test_m5():
    assert 100==100

def test_m6():
    assert "naveen" == "NAVEEN"