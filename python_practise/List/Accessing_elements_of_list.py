# we can access elements of the list by using index or slice operator(:)

# 1) By using Index

# list follows zero based index
# it supports both +ve _ve indexes

# 2) by using slice operator

list = list1[start:stop:step]

# 3) list vs mutability - once we create list object, we can modify its content.hence list object are mutable

n= [10,20,30]
print(n)
n[1] = 101
print(n)