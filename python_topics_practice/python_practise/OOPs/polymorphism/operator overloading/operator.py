"""
Overloading
 We can use same operator or methods for different purposes.
Eg 1: + operator can be used for Arithmetic addition and String concatenation
 print(10+20)#30
 print('durga'+'soft')#durgasoft
Eg 2: * operator can be used for multiplication and string repetition purposes.
 print(10*20)#200
 print('durga'*3)#durgadurgadurga
Eg 3: We can use deposit() method to deposit cash or cheque or dd
 deposit(cash)
 deposit(cheque)
 There are 3 types of Overloading
1) Operator Overloading
2) Method Overloading
3) Constructor Overloading
1)Operator Overloading:
 We can use the same operator for multiple purposes, which is nothing but operator
overloading.
 Python supports operator overloading.
Eg 1: + operator can be used for Arithmetic addition and String concatenation
 print(10+20)#30
 print('durga'+'soft')#durgasoft
Eg 2: * operator can be used for multiplication and string repetition purposes.
 print(10*20)#200
 print('durga'*3)#durgadurgadurga

⚽ We can overload + operator to work with Book objects also. i.e Python supports
Operator Overloading.
⚽ For every operator Magic Methods are available. To overload any operator we have to
override that Method in our class.
⚽ Internally + operator is implemented by using __add__() method.This method is called
magic method for + operator. We have to override this method in our class.

The following is the list of operators and corresponding magic methods.
1) +
2) -
3) *
4) /
5) //
6) %
7) **
8) +=
9) -=
10) *=
11) /=
12) //=


object.__add__(self,other)
object.__sub__(self,other)
object.__mul__(self,other)
object.__div__(self,other)
object.__floordiv__(self,other)
object.__mod__(self,other)
object.__pow__(self,other)
object.__iadd__(self,other)
object.__isub__(self,other)
object.__imul__(self,other)
object.__idiv__(self,other)
object.__ifloordiv__(self,other)

13) %=
14) **=
15) <
16) <=
17) >
18) >=
19) ==
20) !=
object.__imod__(self,other)
object.__ipow__(self,other)
object.__lt__(self,other)
object.__le__(self,other)
object.__gt__(self,other)
object.__ge__(self,other)
object.__eq__(self,other)
object.__ne__(self,other

"""


