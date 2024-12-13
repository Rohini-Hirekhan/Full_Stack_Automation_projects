# Mathematical operators for tuple
# 1) Concatenation operator -
t=912,23,43
t2 = 2,3,4
print(t+t2)#(912, 23, 43, 2, 3, 4)


#2) multiplication operator
t=912,23,43
t2 = t*3
print(t2)#(912, 23, 43, 912, 23, 43, 912, 23, 43)

#Functions of Tuple
#1) to return number of elements present in the tuple


#2)count() - to return number of occurrence of given element in the tuple


#3) index() : return index of first occurrence of given element if ele not there will get " ValueError

#4) sorted() :to sort elements based on default natural sorting order
t=(12,23,10,15)
t1 = sorted(t)
print(t1)#[10, 12, 15, 23]

#we can sort according to reverse of default sorting order as follows
t=(12,23,10,15)
t1 = sorted(t,reverse=True)
print(t1)#[23, 15, 12, 10]

#5) min() and max()-these functions return min and max values according to default natural sorting order
t=(12,23,10,15)
print(max(t))#23
print(min(t))#10

#6) cmp()- it compares the elements of both tuples
#if both tuples are equal then return 0
#if the first tuple is less than second tuple then it returns -1
#if the first tuple is greater than second tuple then it returns +1

t1=(10,20,30,40)
t2=(40,50,90)
t3=(10,20,30)
print(cmp(t1,t2))
print(cmp(t2,23))
print(cmp(t1,t3))


#Tuple Packing and Unpacking - we can create tuple by packing a group of variables.

#Tuple Packing
a=10
b=20
c=30
t=a,b,c
print(t)#(10, 20, 30)

#tuple unpacking
t=(10,20,30,40)
a,b,c,d = t
print(a)#10
print(d)#40

#Tuple comprehension -
t = (x ** 2 for x in range(1, 6))
print(type(t))
for x in t:
    print(x)

1
4
9
16
25



