"""
2) float - We can use float() function to convert other type values to float type.
print(float(234))
# 234.0
# print(float("rohini"))
# ValueError: could not convert string to float: 'rohini'
print(float("45"))
# 45.0
print(float("45.898"))
# 45.898
print(float(False))
# 0.0
print(float(True))
# 1.0
print(float(23+67j))
# TypeError: float() argument must be a string or a real number, not 'complex'

Note:
1. We can convert any type value to float type except complex type.
2. Whenever we are trying to convert str type to float type compulsary str should be
either integral or floating point literal and should be specified only in base-10.
"""
print(float(234))
# 234.0
# print(float("rohini"))
# ValueError: could not convert string to float: 'rohini'
print(float("45"))
# 45.0
print(float("45.898"))
# 45.898
print(float(False))
# 0.0
print(float(True))
# 1.0
print(float(23+67j))
# TypeError: float() argument must be a string or a real number, not 'complex'
