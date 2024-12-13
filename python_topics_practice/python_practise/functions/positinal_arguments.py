"""
Returning multiple values from a function:
In other languages like C,C++ and Java, function can return atmost one value. But in
Python, a function can return any number of values.
Types of arguments
def f1(a,b):
 ------
 ------
 ------
f1(10,20)
a,b are formal arguments where as 10,20 are actual arguments
There are 4 types are actual arguments are allowed in Python.
1. positional arguments
2. keyword arguments
3. default arguments
4. Variable length arguments

1. positional arguments:
These are the arguments passed to function in correct positional order.
def sub(a,b):
 print(a-b)
sub(100,200)
sub(200,100)
The number of arguments and position of arguments must be matched. If we change the
order then result may be changed.
If we change the number of arguments then we will get error.

"""

def f1(a,b):
    return a+b
r=f1(10,20)
print(r)