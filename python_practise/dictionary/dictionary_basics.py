#we can use list,tuple and set to represent a group of individual objects as a single entity
# if we want to represent a group of objects as key-value pairs then we should go for Dictionary

# 1) duplicates keys are not allowed but values can be duplicated
# 2) heterogeneous objects are allowed for both key and values
# 3) insertion order is not preserved
# 4) Dictionaries are mutable
# 5) dictionaries are dynamic
# 6) indexing and slicing concepts are not applicable

#how to create dictionary

d={}
d = dict()
#we are creating empty dictionaries we can add entries as follows

d[100]="rohini"
d[200] = "sakshi"
d[300] = "shiva"
print(d)#{100: 'rohini', 200: 'sakshi', 300: 'shiva'}

#if we know data in advance then we can create dictionary as follows

d = {100:"vilas",200:"ravi",300:"kashmir"}

#How to access data from dictionary - we can access data by using keys
d={100:"durga",200:"rohini"}
print(d[100])#durga
#if the specified key is not available then we will get keyError
print(d[400])#KeyError: 400

#we can prevent this by checking whether key is already available or not by using has_key() function or by using in operator
d.has_key(400)#return 1 if key is available otherwise return 0(used in python 2)

#WAP

#How to update Dictionaries -
d[key]= value
# if the key is not available then new entry will be added to the dictionary with the specified key-value pair
# if the key is already available then old value will be replaced with new value
d={100:"rohini",200:"durga"}
d[200] = "rushi"
d[300] = "malakwade"
print(d)#{100: 'rohini', 200: 'rushi', 300: 'malakwade'}

#How to delete elements from dictionary
#1) del d[key] - It delete entry associated with the specified key.
#2) if the key is not available then we will get keyError

d={100:"rohini",200:"durga"}
d[200] = "rushi"
d[300] = "malakwade"
print(d)#{100: 'rohini', 200: 'rushi', 300: 'malakwade'}
del d[100]
print(d)#{200: 'rushi', 300: 'malakwade'}
del d[500]
print(d)#KeyError: 500
del d
print(d)#NameError: name 'd' is not defined. Did you mean: 'id'?

#2) d.clear() - to remove all entries from the dictionary
d={100:"rohini",200:"durga"}
d[200] = "rushi"
d[300] = "malakwade"
print(d)#{100: 'rohini', 200: 'rushi', 300: 'malakwade'}
d.clear()
print(d)#{}

#3)del d - to delete total dictionary.now we cannot access d
d={100:"rohini",200:"durga"}
d[200] = "rushi"
d[300] = "malakwade"
print(d)#{100: 'rohini', 200: 'rushi', 300: 'malakwade'}
del d
print(d)#NameError: name 'd' is not defined. Did you mean: 'id'?




