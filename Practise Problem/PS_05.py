"""
Q-1 Write a Python program to list all files in a directory in Python.

Q-2  Write a Python program to get execution time for a Python method

Q-3 Write a Python program to convert height (in feet and inches) to centimeters

1 inch = 2.54s
1 Foot = 30.48s

Q-4 Write a Python program to calculate the hypotenuse of a right angled triangle.
"""

# Q-1

"""
import os 

input_path = str(input("Enter the path\n"))

for item in os.listdir(input_path):
    print(item)
    

print("Total Files and Folders are: ",len(os.listdir(input_path)))

"""

# Q-2
"""
import time

def Joker():
    print("Joker")
    return f"{time.time()} Nano Seconds"

print(Joker())
"""


# Q-3

"""
input_num = int(input("Enter the number\n"))
input_task = int(input("Convert into 1. Inch 2. Foot\n"))

if (input_task == 1):
    print(input_num*2.54,"cm")

else:
    print(input_num*30.48,"cm")
"""

# Q-4

base = int(input("Enter the base Length\n"))
height = int(input("Enter the height Length\n"))

for i in range(1):
    square_base = base*base
    height_base = height*height

print("Hypotnuse of the the Given triangle: ",square_base+height_base)