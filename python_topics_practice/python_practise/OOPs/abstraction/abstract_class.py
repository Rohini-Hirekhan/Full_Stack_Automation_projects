"""
parent class me abstract methos hai or child class ne use inherit kiya to use uski method override krni pdegi otherwise child cls ke object creation me error aayegi
agar apne oi cls extend nhi kiya or object create kiya to koi error nhi aayegi


Abstract class:
Some times implementation of a class is not complete,such type of partially
implementation classes are called abstract classes. Every abstract class in Python should
be derived from ABC class which is present in abc module.

Conclusion: If a class contains atleast one abstract method and if we are extending ABC
class then instantiation is not possible.
"abstract class with abstract method instantiation is not possible"
Parent class abstract methods should be implemented in the child classes. Otherwise we
cannot instantiate child class.If we are not creating child class object then we won't get
any error.


"""
# case1
# class test:
#     pass
#
# t=test()

# In the above code we can create object for Test class b'z it is concrete class and it does not
# conatin any abstract method.

# Case-2:
# from abc import *
# class test(ABC):
#     pass
#
# t=test()

# In the above code we can create object, even it is derived from ABC class,b'z it does not
# contain any abstract method.

# Case-3:
# from abc import *
# class test():
#     @abstractmethod
#     def m1(self):
#         pass
# t=test()

# We can create object even class contains abstract method b'z we are not extending ABC
# class.

# Case-4:
# from abc import *
# class test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
# t=test()
# o/p->TypeError: Can't instantiate abstract class test with abstract method m1

# Conclusion: If a class contains atleast one abstract method and if we are extending ABC
# class then instantiation is not possible.
# "abstract class with abstract method instantiation is not possible"
# Parent class abstract methods should be implemented in the child classes. Otherwise we
# cannot instantiate child class.If we are not creating child class object then we won't get
# any error.

