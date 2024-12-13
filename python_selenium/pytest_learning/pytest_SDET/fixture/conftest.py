import pytest
from selenium import webdriver

@pytest.fixture
def init_driver(request):
    driver = webdriver.Chrome()

