"""

Q-1 Write a python program to print multiplecation number of the table using the for loop

Q-2 Solve problem 1 using while loop

Q-3 Write a python program to greet person inside the list which name start from S

Q-4 Write a python program to find n natural number of the given number

Q-5 Write a python program to mulitply the table any print it into reversed form.
"""

# Q-1
"""
number = int(input("Enter the number\n"))

for i in range(1,11):
    print(number*i)
"""

# Q-2

"""
i = 0

number = int(input("Enter the number\n"))

while i<10:
    i = i + 1
    print(i*number)
"""

# Q-3
"""
l1 = ["Harry","Soham","Sachin","Rahul","sumit"]

for item in l1:
    first_letter = item[0]

    if (first_letter == "S" or first_letter == "s"):
        print(item.capitalize())
    else:
        pass
"""

# Q-4
"""
number = int(input("Enter the number\n"))

print(number*int(number+1)/2)
"""
# Q-5

number = int(input("Enter the number\n"))

table_list = []

for i in range(1,11):
    table_list.append(i*number)

table_list.reverse()

for item in table_list:
    print(item)