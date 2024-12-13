"""
Method Overriding
⚽ What ever members available in the parent class are bydefault available to the child
class through inheritance. If the child class not satisfied with parent class
implementation then child class is allowed to redefine that method in the child class
based on its requirement. This concept is called overriding.
⚽ Overriding concept applicable for both methods and constructors.
"""

class parent:
    def p1(self):
        print("parent method")

class child(parent):
    def p1(self):
        print("child method")

t1=parent()
t1.p1() #parent method
t1 = child()
t1.p1() #child method