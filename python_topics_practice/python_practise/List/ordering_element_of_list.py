# 1) reverse() - we can use to reverse() order of elements of list
l=[12,34]
l.reverse()
print(l)

# 2) sort() - In list bydefault insertion order is preserved.if we want to sort the elements of list according to
# default natural sorting order then we should go for sort() method
# for numbers - default natural sorting order is ascending order
# for sorting - default natural sorting order is alphabetical order

n=[2222,33,1,23,45]
n.sort()
print(n) #[1, 23, 33, 45, 2222]

s=['rohini','rushikesh','abc','xyz']
s.sort()
print(s)#['abc', 'rohini', 'rushikesh', 'xyz']

# Note - to use sort() function compulsory list should contain only homogeneous elements otherwise we will get error
n=[2,3,'sorting']
n.sort()
print(n) #TypeError: '<' not supported between instances of 'str' and 'int'

# To sort in reverse of default natural sorting order
n=[4,2,1,7,5,8,3]
n.sort()
print(n)
n.reverse()
print(n)
#or
n.sort(reverse=True)
print(n)#o/p - [8, 7, 5, 4, 3, 2, 1]
n.sort(reverse=False)
print(n)#o/p - [1, 2, 3, 4, 5, 7, 8]

#Aliasing and cloning of list objects ->
# the process of giving another refernce variable to the existing list is called ALIASING
x=[2,56,75,23,22]
y=x

print(y)# o/p ->[2, 34, 75, 23, 22]
# the problem in this approach is by using one reference variable if we are changing content,ten those changes will be reflected
# to the other reference variable
x=[2,56,75,23,22]
print(y)#o/p ->[2, 56, 75, 23, 22]
y[1] = 34

# To overcome this problem we should go for cloning
# we can implement by using slice operator or by using copy() function
x=[1,5,6,3]
y=x[:]
y[1] = 100
print(x) # [1, 5, 6, 3]
print(y)# [1, 100, 6, 3]
#by using  copy()

x=[1,5,6,3]
y=x.copy()
y[1] = 100
print(x) # [1, 5, 6, 3]
print(y)# [1, 100, 6, 3]

#using mathematical operators for list objects-we can use + and * operators for list objects
# 1) concatenation operator (+): we can use to concatenate 2 lists into a single list
a=[2,1]
b=[3,5]
c = a+b
print(c)# [2, 1, 3, 5]
# to use list object compulsory both should be list object otherwise we will get type error
c=c+40 #TypeError: can only concatenate list (not "int") to list
c=a+[45]
# print(c)
[2, 1, 45]

# 2)Repetition operator (*): we can use repetion operator * to repeat elements of list specified number of items

x=[12,34,3]
a=x*3
print(a)#[12, 34, 3, 12, 34, 3, 12, 34, 3]

# Comparing List Objects - we can use comparison operators for list objects
x=['rohit','abc']
z=['rohit']
m=['abc','rohit']
y=[23,56]
print(x==y)#False
print(x==z)#False
print(x==m)#false
# whenever we are using comparison operator(==,!=)for list objects then the following should be considered
# 1) Number of element
# 2) the order of element
# 3)the content of element(case sensitive)
# whenver we are using relational operators(<,>.<=,>=)between list objects, only first element comparison will be performed


#Membership operator - we can check whether element is a member of element or not by using membership operator
# 1) in operator
# 2) not in operator
s=[12,32,34,32,21]
print(10 in s)#False
print(100 not in s)#True

#clear() function ->we can use clear() function to remove all elements of list
s=[12,32,34,32,21]
print(s)#[12, 32, 34, 32, 21]
s.clear()
print(s)#[]

#Nested Lists- sometimes we can take one list inside another list such type of lists are called nested list
n=[12,23,[3,54]]
print(n[0])
print(n[1])
print(n[2])#[3,54]
print(n[2][0])#3

#Nested List vs Matrix

#list comprenhensive-it is very easy and compact way to creating list objects from any iterable objects
#(like list,tuple,dictionary,range etc)based on some conditions
#list = [expression for item in the list if condition]
s=[x*x for x in range(1,11)]
print(s)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
s=[2**x for x in range(1,6)]
print(s)#[2, 4, 8, 16, 32]

# WAP to display unique vowels present in given word
vowels = ['a', 'e', 'i', 'o', 'u']
w = input("enter a word, we will give you vowels : ")
r = []

for i in w:

    if i in vowels:
        r.append(i)

print(r)


