"""
3)Constructor Overloading:
⚽ Constructor overloading is not possible in Python.
⚽ If we define multiple constructors then the last constructor will be considered.

Constructor with Variable Number of Arguments:

"""

class test:
    def __init__(self,*a):
        print("constructor")

t1=test()
t2=test(10)