"""
3. Default Arguments:
Sometimes we can provide default values for our positional arguments.

onal arguments.
Eg:
1) def wish(name="Guest"):
2) print("Hello",name,"Good Morning")
3)
4) wish("Durga")
5) wish()
6)
7) Output
8) Hello Durga Good Morning
9) Hello Guest Good Morning

7
DURGASOFT, # 202, 2
nd Floor, HUDA Maitrivanam, Ameerpet, Hyderabad - 500038,
 040 – 64 51 27 86, 80 96 96 96 96, 92 46 21 21 43 | www.durgasoft.com
If we are not passing any name then only default value will be considered.
***Note:
After default arguments we should not take non default arguments
def wish(name="Guest",msg="Good Morning"): ===>Valid
def wish(name,msg="Good Morning"): ===>Valid
def wish(name="Guest",msg): ==>Invalid
SyntaxError: non-default argument follows default argument
"""