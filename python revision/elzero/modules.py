"""
-----PIP----
> pip --version /check version of anything
> pip list / list of modules you have
> pip install anything=2.12.4 / install module with the version
> pip install --user module --upgrade / update
"""

# import random # to import the hole module
# from random import * # to import the hole module as functions
from random import choice, random, randint
import sys
import termcolor
import pyfiglet


import my_module as alis_module
sys.path.append(r"Z:\programing")
print(sys.path)

x = [1,2,3,4,5,6,7,8,9]

print(f"random number from x: {choice(x)}")
print(f"random number: {randint(1, 100)}")

# to see all the things inside a dir or a module
print(dir(random))

print(alis_module.sayHello('ali'))

My_nice_name = pyfiglet.figlet_format("Ali")
print(termcolor.colored(My_nice_name, color="blue"))