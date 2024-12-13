"""
Types of Variables:
Inside Python class 3 types of variables are allowed.
1) Instance Variables (Object Level Variables)
2) Static Variables (Class Level Variables)
3) Local variables (Method Level Variables)
1)Instance Variables:
 If the value of a variable is varied from object to object, then such type of variables are
called instance variables.
 For every object a separate copy of instance variables will be created.
Where we can declare Instance Variables:
1) Inside Constructor by using self variable
2) Inside Instance Method by using self variable
3) Outside of the class by using object reference variable

"""
# Inside Constructor by using Self Variable:We can declare instance variables inside a constructor by using self keyword. Once we
# creates object, automatically these variables will be added to the object.

# class Employee:
#     def __init__(self):
#         self.a="rohini"
#         print(self.a)
# emp=Employee()
# rohini

# Inside Instance Method by using Self Variable:
# We can also declare instance variables inside instance method by using self variable. If
# any instance variable declared inside instance method, that instance variable will be

class student:
    def book(self):
        self.str = "amit"
# print(self.str)

st=student()
#
# print(self.str)
#           ^^^^
# NameError: name 'self' is not defined

class student:
    def book(self):
        self.str = "amit"
        print(self.str)
# print(st.str)

st=student()
st.book()
print(st.str)
# print(st.str)
#           ^^^^^^
# AttributeError: 'student' object has no attribute 'str'

#3) Outside of the Class by using Object Reference Variable:
# We can also add instance variables outside of a class to a particular object.
class Employee:
    def __init__(self):
        self.a="rohini"
        print(self.a)
emp=Employee()
print(emp.a)

# How to Access Instance Variables:
# We can access instance variables with in the class by using self variable and outside of the
# class by using object reference.


# How to delete Instance Variable from the Object:
# 1) Within a class we can delete instance variable as follows
# del self.variableName
# 2) From outside of class we can delete instance variables as follows
# del objectreference.variableName

class Employee:
    def __init__(self):
        self.a="rohini"
        print(self.a)
emp=Employee()
print(emp.a)
del emp.a
print(emp.a)
# print(emp.a)
#           ^^^^^
# AttributeError: 'Employee' object has no attribute 'a'


# Note: The instance variables which are deleted from one object,will not be deleted from
# other objects.
