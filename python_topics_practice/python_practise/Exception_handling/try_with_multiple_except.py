"""
try with Multiple except Blocks:
The way of handling exception is varied from exception to exception.Hence for every
exception type a seperate except block we have to provide. i.e try with multiple except
blocks is possible and recommended to use.

Eg:
try:
 -------
 -------
 -------
except ZeroDivisionError:
 perform alternative arithmetic operations

 except FileNotFoundError:
 use local file instead of remote file
If try with multiple except blocks available then based on raised exception the
corresponding except block will be executed.

If try with multiple except blocks available then the order of these except blocks is
important .Python interpreter will always consider from top to bottom until matched
except block identified.

Single except Block that can handle Multiple Exceptions:
We can write a single except block that can handle multiple different types of exceptions.
except (Exception1,Exception2,exception3,..): OR
except (Exception1,Exception2,exception3,..) as msg : 
"""