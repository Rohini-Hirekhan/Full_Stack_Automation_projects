import unittest

"""
- in automation testig.organizing your code is very important and client
execute us to write automation scripts according to the manual test cases.
- we can get good reporting structure if we can exactly map our automation code with manual test cases
- in python we can use "UnitTest Testing framework" to organize our automation code and to extract reports
- to use the methods present in the unit test framework, we have to extend the testcases class present in the unittest module



Test class should extend from testecase class which is coming from unittest module
"""

class Test(unittest.TestCase):
    def test_firstTest(selfself):
        print("hi")

if __name__ == "__main__":
    unittest.main()