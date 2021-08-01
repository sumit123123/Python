# Q-1

"""
number_1 = int(input("Enter the number\n"))
number_2 = int(input("Enter the number\n"))
number_3 = int(input("Enter the number\n"))

number_list = [number_1,number_2,number_3]

def Find_great():
    number_list.sort()
    print(number_list[-1])

Find_great()
"""

# Q-2
"""
def Convert(celcius):
    return int(celcius) * 9/5 +32

celci = int(input("Enter the celsius\n"))

Fahrenheit = Convert(celci)

print(Fahrenheit, "°F")
"""

# Q-4

number = int(input("Enter the number\n"))

for i in range(number):
    if i == 0 or i == 1:
        number = 0
    else:
        print(number*number-1)

    