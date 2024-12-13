"""


"""

# class p1():
#     def __init__(self):
#         print("parent constructor")
#
# class c1(p1):
#     def __init__(self):
#         print("child constructor")
#
# c=c1()

# o/p->child constructor


# In the above example,if child class does not contain constructor then parent class
# constructor will be executed
# From child class constuctor we can call parent class constructor by using super() method.

# Demo Program to call Parent Class Constructor by using super():

class p1():
    def __init__(self):
        print("parent constructor")

class c1(p1):
    def __init__(self):
        super().__init__()
        print("child constructor")
c=c1()