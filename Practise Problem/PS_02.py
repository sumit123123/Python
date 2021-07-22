"""
Q-1 Write a Python program to print the following 'here document'

Q-2 Write a Python program to calculate number of days between two dates

Q-3 Write a Python program to get the volume of a sphere with radius 6.

V = 4/3 πr³

Q-4 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

Q-5 Write a Python program to test whether a number is within 100 of 1000 or 2000

"""

# Q-1
"""
print('''
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
''')
"""
# Q-2
"""
Date_1 = input("Enter the date 1:\n")
Month_1 = input("Enter the Month 1:\n")

Date_2 = input("Enter the date 2:\n")
Month_2 = input("Enter the Month 2:\n")

if (Month_1 == Month_2):
    print(f"The days between the {Month_1}/{Date_1} - {Month_2}/{Date_2} is {int(Date_2)-int(Date_1)}")
else:
    print("Sorry, Our program cannot find\nthe dates between the two month because some\nmonths have 31 days")
"""

# Q-3

# print(4/3*22/7*6*6*6,"cm³")

# Q-4

"""
inp = int(input("Enter the number\n"))

if (inp<17):
    print(17-inp)

else:
    new_value = inp-17

    print(new_value*2)
"""

# Q-5

num = int(input("Enter the number:\n"))

if (num>100 and num<1000):
    print("The number is between 100 to 1000")

elif (num>1000 and num<2000):
    print("The number is smaller than 2000 and greater than 1000")

else:
    print("The number is greater than 2000")