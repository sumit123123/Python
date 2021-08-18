"""
Q-1 Write a Python program to convert all units of time into seconds

Q-2 Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Q-3 Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
"""

# Q-1

def Seconds():
    hr_value = int(input("Enter the hr\n"))
    min_value = int(input("Enter the min\n"))

    print(hr_value*3600+min_value*60,"Seconds",end=" ")

# Seconds()

# Q-2

def year_100():
    from datetime import date

    today = date.today()

    year = today.year
    
    name = input("Enter your name \n")
    age = int(input("Enter your age \n"))

    remaining_year = 100-age

    print(f"{name} you will become 100 years on the year {year+remaining_year}")

    
# year_100()

# Q-3

def oe():
    number = int(input("Enter the number:\n"))

    i = 0

    while i<0:
        i = i + 1

        if (i/2==0):
            print("Even")

        else:
            print("Odd")
oe()