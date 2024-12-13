# To get information about list

# 1) len(): - return the number of elements present in list

n= [10,20,30]
print(len(n))

# 2) count(): - it returns number of occurrences of specified items in the list

n=[2,2,2,3,2,2,2,2,3,3,3,3,34,4,4,]
print(n.count(3))

#0/p -> 5

# 3) index(): - Returns the index of first occurrence of the specified item

n=[2,2,2,3,2,2,2,2,3,3,3,3,34,4,4,]
print(n.index(2))#0
print(n.index(34))#12
#if the element is not present in the list then we will get ValuError hence before index() method we have to check
# whether item is present in list or not by using "in" operator