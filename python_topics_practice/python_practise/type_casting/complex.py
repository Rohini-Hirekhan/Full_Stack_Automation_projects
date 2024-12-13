"""
complex -We can use complex() function to convert other types to complex type

print(complex(34))
# (34+0j)

print(complex(True))
# (1+0j)

print(complex(False))
# 0j

print(complex(45.677))
# (45.677+0j)

print(complex("rohini"))
# ValueError: complex() arg is a malformed string

print(complex("456.5"))
# (456.5+0j)

print(complex("45"))
# (45+0j)

Form-2: complex(x,y)
We can use this method to convert x and y into complex number such that x will be real
part and y will be imaginary part.


"""
print(complex(34))
# (34+0j)

print(complex(True))
# (1+0j)

print(complex(False))
# 0j

print(complex(45.677))
# (45.677+0j)

# print(complex("rohini"))
# ValueError: complex() arg is a malformed string

print(complex("456.5"))
# (456.5+0j)

print(complex("45"))
# (45+0j)

print(complex(12,-90))
# (12-90j)

