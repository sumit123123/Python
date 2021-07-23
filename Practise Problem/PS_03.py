"""
Q-1 Write a Python program that will accept the base and height of a triangle and compute the area

Q-2 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

Q-3 Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

Q-4 Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

Q-5 Write a Python program to display your details like name, age, address in three different lines
"""

# Q-1

"""
base = int(input("Enter the base\n"))

height = int(input("Enter the height\n"))

print("Area of Triangle: ",1/2*base*height)
"""

# Q-2
"""
num_1 = int(input("Enter the number 1\n"))
num_2 = int(input("Enter the number 2\n"))
num_3 = int(input("Enter the number 3\n"))

if (num_1 == num_2 or num_2==num_3 or num_3==num_1):
    print("The value will be 0")

else:
    print(num_1+num_2+num_3)

"""

# Q-3

"""
num_1 = int(input("Enter the number 1\n"))
num_2 = int(input("Enter the number 2\n"))

if (num_1>=15 and num_1<=20):
    print("20")

elif (num_2>=15 and num_2<=20):
    print("20")

else:
    print(num_2+num_1)
"""

# Q-4

"""
num_1 = int(input("Enter the number 1\n"))
num_2 = int(input("Enter the number 2\n"))

if (num_2-num_1==5 or num_1+num_2==5):
    print(True)
elif (num_1==num_2):
    print(True)
else:
    print(num_1+num_2,"Sum")
    print(num_2-num_1,"Difference")

"""

# Q-5

"""
detail_1 = str(input("Name:\n"))
detail_2 = int(input("Age:\n"))
detail_3 = str(input("Address:\n"))

print('''
Name:{}\nAge:{}\nAddress:{}
'''.format(detail_1,detail_2,detail_3))

"""