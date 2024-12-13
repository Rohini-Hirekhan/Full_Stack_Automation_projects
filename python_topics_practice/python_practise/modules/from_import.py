"""
from ... import:
We can import particular members of module by using from ... import .
The main advantage of this is we can access members directly without using module
name.


We can import all members of a module as follows
from durgamath import *
"""
from demo2 import a,rohini

print(a)
rohini()
rushi() #NameError: name 'rushi' is not defined