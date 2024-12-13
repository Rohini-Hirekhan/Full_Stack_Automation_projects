
""" variables -
    instance(object)
    static(class level)
    local(method level)

    methods -
    instance
    static
    class

Write a Python program to create a Student class and Creates an object to it.
Call the method talk() to display student details

"""
class Student:
    def __init__(self):
        self.name ="rohini"
    def talk(self):
        print("name of student : ",self.name)

s=Student()
s.talk()
