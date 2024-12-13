"""
2)Method Overloading:
 If 2 methods having same name but different type of arguments then those methods
are said to be overloaded methods.
 Eg: m1(int a)
 m1(double d)
 But in Python Method overloading is not possible.
 If we are trying to declare multiple methods with same name and different number of
arguments then Python will always consider only last method.

"""
class test:
    def m1(self):
        print("m1")

    def m1(self):
        print("m2")

t1=test()
t1.m1()
# o/p-> m2
# In the above program python will consider only last method.

"""
How we can handle Overloaded Method Requirements in Python:
Most of the times, if method with variable number of arguments required then we can
handle with default arguments or with variable number of argument methods.
"""