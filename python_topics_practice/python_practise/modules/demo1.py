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

"""

import demo2


print(demo2.a)
print(demo2.b)
demo2.rohini()

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'demo2']
print(dir(demo2))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'rohini', 'rushi']

"""
Note: For every module at the time of execution Python interpreter will add some special
properties automatically for internal use.
"""
