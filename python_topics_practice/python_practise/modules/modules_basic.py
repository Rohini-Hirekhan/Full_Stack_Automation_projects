"""

 A group of functions, variables and classes saved to a file, which is nothing but module.
 Every Python file (.py) acts as a module.

If we want to use members of module in our program then we should import that module.
import modulename
We can access members by using module name.
modulename.variable
modulename.function()

Note:
whenever we are using a module in our program, for that module compiled file will be
generated and stored in the hard disk permanently.

Renaming a module at the time of import (module aliasing):
Eg:
import durgamath as m
here durgamath is original module name and m is alias name.
We can access members by using alias name m

from ... import:
We can import particular members of module by using from ... import .
The main advantage of this is we can access members directly without using module
name.


We can import all members of a module as follows
from durgamath import *

Various possibilties of import:
import modulename
import module1,module2,module3
import module1 as m
import module1 as m1,module2 as m2,module3
from module import member
from module import member1,member2,memebr3
from module import memeber1 as x
from module import *

member aliasing:
from durgamath import x as y,add as sum
print(y)
sum(10,20)
Once we defined as alias name,we should use alias name only and we should not use
original name



"""
