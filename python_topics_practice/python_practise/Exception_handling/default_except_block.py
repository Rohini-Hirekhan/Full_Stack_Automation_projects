"""
Default except Block:
We can use default except block to handle any type of exceptions.
In default except block generally we can print normal error messages.

Syntax:
 except:
 statements

*Note: If try with multiple except blocks available then default except block should be
 last, otherwise we will get SyntaxError

 Note: The following are various possible combinations of except blocks
1) except ZeroDivisionError:
2) except ZeroDivisionError as msg:
3) except (ZeroDivisionError,ValueError) :
4) except (ZeroDivisionError,ValueError) as msg:
5) except :

"""

except name_of_exception:
except name_of_exception as msg:




