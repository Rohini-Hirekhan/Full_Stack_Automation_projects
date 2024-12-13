import reload2
import reload2
import reload2
"""
In the above program test module will be loaded only once eventhough we are importing
multiple times.
The problem in this approach is after loading a module if it is updated outside then
updated version of module1 is not available to our program.
We can solve this problem by reloading module explicitly based on our requirement.
We can reload by using reload() function of imp module.
import imp
imp.reload(module1)
"""
from imp import reload

reload(reload2)