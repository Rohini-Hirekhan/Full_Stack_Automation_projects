#tuple is exactly same as list except it is immutable. i.e once we creates tuple object, we cannot perform any changes in that object
# hence tuple is read only version of list
# if our data is fixed and never changes then we should go for tuple
# insertion order is preserved
# duplicates are allowed
# heterogenous objects are allowed
# we can preserve insertion order and we can differentiate duplicate objects by using index.
# tuple both support +ve and -ve index
# wecan represent yuple elements within parenthesis and with comma seperator

t=10,23,44
print(t)#(10, 23, 44)
print(type(t))#<class 'tuple'>

#we have to take special care about single value tuple. compulsory it should end with comma,otherwise it is not treated as tuple
t=(10)
print(type(t))#<class 'int'>

t=(10,)
print(type(t))#<class 'tuple'>

#Tuple Creation
#1) t = () - creation of empty tuple
#2) t=(10,)- creation of single valued tuple, parenthesis are optional, should ends with comma
#3) t=10,20,30 - creation of multi values tuples and parenthesis are optional
#4) By using tuple() function :
list = [12,45,78]
t = tuple(list)
print(t)#(12, 45, 78)

#Accessing elements of tuple : we can access either by index or by slice operator
#1)By using index

# 1) by using index:
t=(12,67,677,78,987)
print(t[0])#12
print(t[-1])#987
print(t[1])#IndexError: tuple index out of range

#2) by using slice operator:
t=(10,37,67,89)
print(t[2:5])
print(t[2:100])
print(t[::2])
# o/p -
# (67, 89)
# (67, 89)
# (10, 67)

#Tuple vs Immutability
#once we creates tuple, we cannot change its content
#hence tuple objects are immutable

t=(12,34,21)
t[1]=45#TypeError: 'tuple' object does not support item assignment

