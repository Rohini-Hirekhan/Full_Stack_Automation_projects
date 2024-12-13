"""
Parameters
Parameters are inputs to the function. If a function contains parameters,then at the time
of calling,compulsory we should provide values otherwise,otherwise we will get error.

Return Statement:
Function can take input values as parameters and executes business logic, and returns
output to the caller with return statement.
"""
# Eg: Write a function to take number as input and print its square value
def square(number):
    print("square of a ",number," is : ", number*number)

square(340)
square(2)

# Write a function to find factorial of given number?
def fact(num):
    total=1
    while num>=1:
        total=total*num
        num=num-1
    return total
for i in range(1,5):
    print("factorial of", i, "is :",fact(i))