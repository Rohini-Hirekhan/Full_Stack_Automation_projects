# String -any sequence of characters within either single or double quotes is considered as String
s='see'
s="string"
#define multiline string(we can also use triple quotes to use single or double quotes as symbol inside sstring literal
s="""
'deep,'kamini'
"""
#how to access characters of string - 1)by index 2) by slice operator
# 1) By Index - python supports both +ve and -ve index
s='durga'
print(s[0])#d
print(s[-1])#a
print(s[-100])#IndexError: string index out of range
print(s[100])#IndexError: string index out of range

# 2) By slice operator
# syntax = s[begin_index : end_index : step]
# begin_index = from where we have to consider slice (substring)
# end index = we have to terminate the slice (substring) at endindex-1
# step = incremented value
#
# NOTE - if we are not specifying begin index it will consider from beginning of the string
# - if we are not specifying end index it will consider up to end of the string
# - the default value for step is 1


#Behaviour of slice operator
# 1) s[begin:end:slice]
# 2) step can be +ve and -ve
# 3) if +ve then it should be forward direction(left to right) and we have to consider from begin to end-1
# 4) if -ve then it should be backward direction( right to left ) and we have to consider from begin to end+1

# Note -
# - In the backward direction if end value is -1 then result is always empty.
# - In the forward direction if end value is 0 then result is always empty.

# In Forward Direction
# - default value for begin : 0
# - default value for end : length of string
# default value for step : +1
#
# In Backward Direction
# - default value for begin -> -1
# - default value for end -> -[length of string+1]

# NOTE - Either forward or backward direction, we can take both +ve and -ve values for begin and end index

#mathematical operator for strings

# we can apply the following mathrmatical operators for string
# 1) + -> concatenation
# 2) * -> repetition

print("love"+"you"+"mom")#loveyoumom
print(3*"mom")#mommommom

# Note -
# 1) To use + operator for strings, compulsory both arguments should be string type
# 2) To use * operator for Strings , compulsory one argument should be str and other argument should be int

#len() in-built function - we can use this to find no of characters present in the string

s = "rohini"
print(len(s))#6

#WAP to access each character of string in forward and backward direction by using while loop

#checking membership - we can check whether the character or string is the member of another string or not by using
# in and not in operators

s='durga'
print('d' in s)#True
print('z' in s)#False

#Comparison of Strings - we can use comparison operators (<,>,<=,>=) and equality operators(==,!=) for string
#it is based on alphabetical order
#Removing spaces from string
# 1) rstrip()-> to remove spaces at right hand side
# 2) lstrip()-> to remove spaces at left hand side
# 3) strip()-> to remove spaces both side

# find substring
# for forward direction -
# 1) find()
# 2) index()

# for backward direction -
# 1) rfind()
# 2) rindex()

# 1) find(): - s.find(substring) - return index occurrence of the given substring. if it is not available then we will get -1

s="rohini"
print(s.find("h"))#2
print(s.find("q"))#-1

#Note - By default find() method can search total string, we can also specify the boundaries to search
# s.find(substring,begin,end)
# it will always search from begin index to end-1 index
print(s.find("i",3,6))#3

# 2) index(): - exactly same as find() method except that if the specified substring is not available then will get ValueError

#program to display all positions of substring in a given main string

#Counting substring in the given string
# we can find number of occurrences of substring present in the given string by using count() method
# 1) s.count(substring) -> it will search through out the string
# 2) s.count(substring,begin,end) -> it will search from begin index to end-1

s="aabbvgdghjhdjhbsaaa"
print(s.count('a'))#5
print(s.count("v"))#1

#Replacing string with another string
# s.replace(oldstring,newstring)
# inside s,every occurrence of old string, will be replaced with new string

#String Objects are immutable then how we can change the content by using replace() method
# once we create string object, we cannot change the content.this non changable behaviour is nothing but immediately. if we are
# trying to change the content by using any method,then with those changes a new object will be created and changes wont be happened
# in existing object
#
# hence with replace()method also a new object got created but existing object wont be changed.

#Splitting of strings - we can spilt the given string according to specified seperator by using spilt() method
l=s.split(seperator)
# the default seperator is space. the return type of split() method is list.
s = "I am learning python"
l = s.split()
for i in l:
    print(i)

# o/p -
I
am
learning
python

#Joining of Strings - we can join group of strings(list or tuple)wrt the given seperator
# s = seperator.join(group of strings)

s = ("m good","hi dear","go ")
l='$'.join(s)
print(l)#m good$hi dear$go

#Changing case of string
# upper()->
# lower()->
# swapcase()->convert lower to upper and upper to lower
# title()-> convert first first character in every word should be upper case and all remaining lower
# capitalize ()-> only first character will be converted to upper case


#checking starting and ending part of the string
s.startswith(substring)
s.endswith(substring)
# it returns true or false

#To check type of characters present in a string
# isalnum(): - returns true if all characters are alphanumeric(a-z,A-Z,0-9)
# isalpha(): - returns
# isdigit():
# islower():
# isupper():
# istitle():
# isspace():returns true if string contains only spaces

#formatting the strings : we can format strings with variable values by using replacement operator {} and format() method
#basic formatting for default,positional and keyword arguments
print("{}'s salary is {} and his age is {}".format(name,salary,age))
print("{1}'s salary is {0} and his age is {2}".format(name,salary,age))
print("{0}'s salary is {1} and his age is {2}".format(name,salary,age))
print("{x}'s salary is {y} and his age is {z}".format(x=name,y=salary,z=age))
#o/p
# rohini's salary is 123000 and his age is 27
# 123000's salary is rohini and his age is 27
# rohini's salary is 123000 and his age is 27
# rohini's salary is 123000 and his age is 27