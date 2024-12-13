"""

If a group of statements is repeatedly required then it is not recommended to write these
statements everytime seperately.We have to define these statements as a single unit and
we can call that unit any number of times based on our requirement without rewriting.
This unit is nothing but function.
The main advantage of functions is code Reusability.
Note: In other languages functions are known as methods,procedures,subroutines etc
Python supports 2 types of functions
1. Built in Functions
2. User Defined Functions
1. Built in Functions:
The functions which are coming along with Python software automatically,are called built
in functions or pre defined functions

Eg:
id()
type()
input()
eval()
etc..
2. User Defined Functions:
The functions which are developed by programmer explicitly according to business
requirements ,are called user defined functions.

Syntax to create user defined functions:
def function_name(parameters) :
 doc string

 return value

Parameters
Parameters are inputs to the function. If a function contains parameters,then at the time
of calling,compulsory we should provide values otherwise,otherwise we will get error.

Return Statement:
Function can take input values as parameters and executes business logic, and returns
output to the caller with return statement.

"""
# Eg: Write a function to take name of the student as input and print wish message by
# name.
# Write a function to check whether the given number is even or odd?

# def f1(number):
#     if number%2==0:
#
#         print("no is even")
#     else:
#         print("no is odd")
#
# f1(45)


# Q. Write a function to find factorial of given number?

def fact(number):
    total=1
    for i in range(1,number+1):
        total= i*total
    return total

ans=fact(3)
print(ans)