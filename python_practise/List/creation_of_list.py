#list
#insertoin order is preserved


#creation of list

# 1) we can create empty list object as follows
list=[]
print(list)
print(type(list))

#2) if we know elements already then we can create list as follows
list = [23,45,66]

#3) with dynamic input
list = eval(input("Enter a list"))
print(list)

# 4) with list function
l = list(range(0,10,2))
print(l)
print(type(list))

# 4) with split() function

s=" I am Rohini"
l=s.split()
print(l)