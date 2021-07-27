"""
Q-1 Write a Python program to solve (x + y) * (x + y)

Q-2 Write a Python program to check whether a file exists

Q-3 Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS

Q-4 Write a Python program to find out the number of CPUs using.

Q-5 Write a Python program to parse a string to Float or Integer
"""

# Q-1
"""
x = int(input("Enter the number\n"))
y = int(input("Enter the number\n"))

new_value = x+y

print(new_value*new_value)
"""

# Q-2
"""
import os

file_name = str(input("Enter the file name\n"))

path = os.listdir("c:\\Users\\Dell\\Desktop\\Programming\\Python\\Practise Problem")

if (file_name in list(path)):
    print("Yes, these file is their in the Directory")

else:
    print("No this file is not in the directory")
"""

# Q-3
 
"""
import platform as pp

path = pp.architecture()[0]=="32bit"

if (path == False):
    print("64 Bit")

else:
    print("32 Bit")
"""

# Q-4

"""

import psutil

print(psutil.cpu_percent(4))

"""

# Q-5
"""
string = "123456789S"

for item in string:
    new_iem = int(item)
    print(new_iem)

print(type(new_iem))
"""