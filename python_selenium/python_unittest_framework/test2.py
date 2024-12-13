import unittest
from selenium import webdriver

class searchENgineTest(unittest.TestCase):
    # function name always start with test name
    def test_google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        print("title is : " , self.driver.title)

    def test_Bing(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bing.com")
        print("title is : ",self.driver.title)

if __name__ == "__main__":
    # run as module
    unittest.main()



