"""
Fuctions and Recurssion Erros

What is function?

Function is a group of statement performing a specific task

syntax:
def Function_name():
    All the statement here
    pass
    print("Hello world")

Output:
No any error came and not any appropriate output. Because function is not call

Function calling

Function calling is way to perform the task written inside the function at the given point.

Syntax:

Function_name()

Output:

Hello world


Quiz-1 Write a pyhton program to greet user good day

Types of function 
There are two types of function 1. Builtin-Function 2. User-Defined

1. Builtin-Function are function which are already installed with python some are len() type() print()
2. User-Defined function are function which are define and written by the user and call

Fucntion with argument

Argument are the input given for the fucntion which are take as value need for the statement to runs

Syntax:

def Hello(Name):
    print("Hello ",Name)

Hello("Sumit")

Output:

Hello Sumit

Default parameter value

We also have a default value in the function

syntax:

def greet(name="Anonymous"):
    print(name)

greet()

Here i did not give parameters but not error came because as it is defaulty set a Anonymous

if i give arrgument Sumit
it will print sumit
"""


def Hello():
    print("By world")

# Hello()

# Quiz 1

def Great():
    print("Good Day")

# Great()

def Hello(Name):
    print("Hello",Name)

Hello("Sumit")