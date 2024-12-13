#manipulating_element_of_list
# 1) append() function : we can use append() function to add items at the end of the list
list = []
list.append("A")
list.append("B")
list.append("C")
print(list)

#to add all elements to list upto 100 which are divisible by 10
l=[]
for i in range(101):
    if i%10==0:
        l.append(i)
print(l)

# 2)insert() - to insert item at specified index position

n=[12,23]
print(n)
n.insert(1,234)
print(n)
n.insert(-10,77)
print(n)

# iw- difference between append() and insert()
# append() -> In list when we add any element it will come in last i.e it will be last element
# insert() -> In list we can insert any elements in particular index numbers

# 3) remove() - we can use this function to remove specified item from the list.if the element present multiple times then only
# first occurence will be removed
# if specified item not present in list then we will get value error hence before using remove() method first we have to check
#specified element present in the list or not by using in perator
list = [12,2,3,2,2,22,2]
list.remove(12)
print(list)
#o/p -> [2, 3, 2, 2, 22, 2]

# 5) pop() - it removes and returns last element of the list
list=[12,23,45]
print(list.pop())
print(list)
# o/p -> 45
# [12, 23]

#pop(index) -> we can use to remove and return element present at specified index

#iw que - diff between remove() and pop()












