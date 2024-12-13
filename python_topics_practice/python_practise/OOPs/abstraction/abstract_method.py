"""
Abstract Method:
 Sometimes we don't know about implementation, still we can declare a method. Such
types of methods are called abstract methods.i.e abstract method has only declaration
but not implementation.
 In python we can declare abstract method by using @abstractmethod decorator as
follows.
 @abstractmethod
 def m1(self): pass
 @abstractmethod decorator present in abc module. Hence compulsory we should
import abc module,otherwise we will get error.
 abc  abstract base class module

Child classes are responsible to provide implemention for parent class abstract methods.


"""

# class test:
#     @abstractmethod
#     def m1(self):
#         pass
# NameError: name 'abstractmethod' is not defined

from abc import *
class test:
    @abstractmethod
    def m1(self):
        pass
# Child classes are responsible to provide implemention for parent class abstract methods.
