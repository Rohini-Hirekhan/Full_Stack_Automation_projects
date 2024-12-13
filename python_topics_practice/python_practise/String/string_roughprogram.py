# Write a program to display unique vowels present in the given word?
v=['a','e','i','o','u']
s=input("enter word : ")
f=[]
for i in s:
    if i in v:
        if i  not in f:
            f.append(i)
print(f)


v = ['a','e','i','o','u']
s = input("Enter a word : ")
f =[]
for i in s:
    if i in v:
        if i not in f:
            f.append(i)
print(f)

















