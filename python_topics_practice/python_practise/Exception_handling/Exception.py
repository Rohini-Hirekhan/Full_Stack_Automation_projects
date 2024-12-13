"""
An unwanted and unexpected event that disturbs normal flow of program is called
exception.
Eg:
 ZeroDivisionError
 TypeError
 ValueError
 FileNotFoundError
 EOFError
 SleepingError
 TyrePuncturedError
It is highly recommended to handle exceptions. The main objective of exception handling
is Graceful Termination of the program (i.e we should not block our resources and we
should not miss anything)

Exception handling does not mean repairing exception. We have to define alternative way
to continue rest of the program normally.
Eg: For example our programming requirement is reading data from remote file locating
at London. At runtime if London file is not available then the program should not be
terminated abnormally. We have to provide local file to continue rest of the program
normally. This way of defining alternative is nothing but exception handling.
try:
Read Data from Remote File locating at London.
except FileNotFoundError:
use local file and continue rest of the program normally

Default Exception Handing in Python:
 Every exception in Python is an object. For every exception type the corresponding
classes are available.
 Whevever an exception occurs PVM will create the corresponding exception object
and will check for handling code. If handling code is not available then Python
interpreter terminates the program abnormally and prints corresponding exception
information to the console.
 The rest of the program won't be executed.

Every Exception in Python is a class.
 All exception classes are child classes of BaseException.i.e every exception class
extends BaseException either directly or indirectly. Hence BaseException acts as root
for Python Exception Hierarchy.
 Most of the times being a programmer we have to concentrate Exception and its child
classes.


Customized Exception Handling by using try-except:
 It is highly recommended to handle exceptions.
 The code which may raise exception is called risky code and we have to take risky code
inside try block. The corresponding handling code we have to take inside except block.
try:
 Risky Code
except XXX:
 Handling code/Alternative Code

 Control Flow in try-except:
try:
 stmt-1
 stmt-2
 stmt-3
except XXX:
 stmt-4
stmt-5

Case-1: If there is no exception
 1,2,3,5 and Normal Termination
Case-2: If an exception raised at stmt-2 and corresponding except block matched
 1,4,5 Normal Termination
Case-3: If an exception rose at stmt-2 and corresponding except block not matched
 1, Abnormal Termination
Case-4: If an exception rose at stmt-4 or at stmt-5 then it is always abnormal
termination.
Conclusions:
1) Within the try block if anywhere exception raised then rest of the try block won’t be
executed eventhough we handled that exception. Hence we have to take only risky
code inside try block and length of the try block should be as less as possible.
2) In addition to try block, there may be a chance of raising exceptions inside except and
finally blocks also.
3) If any statement which is not part of try block raises an exception then it is always
abnormal termination.


"""
print("stm1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("stm3")









