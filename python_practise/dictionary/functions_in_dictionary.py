#1) dict(): - to create dictionary
d=dict()#it creates empty dictionary
d=dict({100:"rohini",200:"rushi"})#it create dictionary with specified elements
d=dict([(100,"rohini"),(200,"rushi")])#it creates dictionary with the given list of tuple elements

#2)len()-returns the number of items in the dictionary

#3)clear() : to remove all the elements from dict

#4)get(): to get value associated with the key
# d.get(key) if the key available then return corresponding value otherwise return none
#it wont raise any error

# d.get(key,defaultvalue) - if the key is available then returns corresponding value otherwise return default value

#5) pop(): it removes the entry associated with the specified key and returns the corresponding value.
# if the specified key is not available then we will get keyError

d={100:"rohini",200:"rushi"}

print(d)#{100: 'rohini', 200: 'rushi'}
print(d.pop(100))#rohini
print(d)#{200: 'rushi'}

#6) popitem(): it removes an arbitrary item(key-value) from the dictionary and return it.
d={100:"rohini",200:"rushi",300:"malakwade"}

print(d)#{100: 'rohini', 200: 'rushi'}
print(d.popitem())#(300, 'malakwade')
print(d)#{100: 'rohini', 200: 'rushi'}

#if the dict is empty will get keyError
a={}
print(a.popitem())#KeyError: 'popitem(): dictionary is empty'


#7) keys() : - it returns all keys associted with dict
d={100:"rohini",200:"rushi",300:"malakwade"}

print(d.keys())#dict_keys([100, 200, 300])
for k in d.keys():
    print(k)
#100
# 200
# 300

# 8) Values(): - it returns all the values associated with dict
d={100:"rohini",200:"rushi",300:"malakwade"}

print(d.values())#dict_values(['rohini', 'rushi', 'malakwade'])
for k in d.values():
    print(k)
# rohini
# rushi
# malakwade


# 9) items(): -it returns list of tuples representing key-value pairs.- [(k,v),(a,b)]
d={100:"rohini",200:"rushi",300:"malakwade"}

print(d.items())#dict_items([(100, 'rohini'), (200, 'rushi'), (300, 'malakwade')])
for k,v in d.items():
    print(k,v)
# 100 rohini
# 200 rushi
# 300 malakwade

#10) copy() : to create exactly duplicate dictionary
d1 = d.copy()

#11) setdefault(): -d.setdefault(k,v)
#if the key is already available then this function return the corresponding value
#if the key is not available then the specified key-value will be added as new item to dictionary

#12) update(): d.update(x) - all items present in dict x will be added to dict d
d={100:"rohini",200:"rushi",300:"malakwade"}
k={}
k.update(d)
print(k)#{100: 'rohini', 200: 'rushi', 300: 'malakwade'}