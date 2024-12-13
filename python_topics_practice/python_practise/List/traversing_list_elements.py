# traversal - sequential access of each element is called "Traversal"

# 1_ by using while loop


n=[1,3,44,55,3,21,1]
i=0
while i<len(n):
    print(n[i])
    i+=1

#By using for loop


n = [1, 3, 44, 55, 3, 21, 1]

for i in n:
    print(i)

#To disply only even numbers
n=[2,3,4,5,6,7]
for i in n:
    if i%2==0:
        print(i)

# to display elements by index wise(not executed)
n = ["A","B","C"]
n1 = len(n)
for i in range(n1):
    print(n[i],"is avalilable at positive index : ", i, "and at negative index :",i-n)
