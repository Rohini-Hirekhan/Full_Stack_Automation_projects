"""
we can covert one type value into another type is called type casting
following inbuilt functions for type casting -
int()
float()
complex()
str()
bool()
1) int()
print(int(456.678)) 456
print(int("rooho")) - invalid literal for int() with base 10: 'rooho'
print(int("23")) - 23
print(True) - True
print(int(2+34j)) - TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
1. We can convert from any type to int except complex type.
2. If we want to convert str type to int type, compulsary str should contain only integral
value and should be specified in base-10



"""
print(int(456.678))
# 456
print(int("rooho"))
# invalid literal for int() with base 10: 'rooho'
print(int("23"))
# 23
print(True)
# True
print(int(2+34j))
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
