#if we want to represent a group of unique values as a single entity then we should go for set
#duplicates are not allowed
#insertion order is not preserved but we can sort the elements
# indexing and slicing not allowed for the set
#heterogenous elements are allowed
#set objects are mutable i.e once we creates set objects we can perform any changes in that object based on our requirement
#we can represent set elements within curly braces and with comma seperation
#We can apply mathematical operations like union,intersection,difference etc on set objects.

#Creation of set object

s={10,20,30}
print(s)#{10, 20, 30}
print(type(s))#<class 'set'>

#we can create set objects by using set() function s=set(any sequence)

i=[12.32,2332.43,22,3,2]
s=set(i)
print(s)#{2, 3, 12.32, 22, 2332.43}

#Note - while creating empty set we have to take special care
#compulsory we should use set() function
# s={} it is treated as dictionary but not empty set

s={}
print(s)
print(type(s))#<class 'dict'>

s=set()
print(s)#set()
print(type(s))#<class 'set'>


