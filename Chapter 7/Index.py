"""
Loops

What is loop?
When you want to repeat a set of item we can repeat it by loops

Types of loops
1. For loop
2. While loop

Syntax

"""

# Syntax of while Loop
"""
i = 0
while i < 10:
    print("Yes")
    i = i + 1

print("Done")
"""

# Quiz-1 Write a python program to print 1 to 50 using while loop
"""
i = 0

while i<50+1:
    print(str(i))
    i = i + 1

"""

# Another example

"""
i = 0

while i<5:
    print("Harry")
    i = i + 1
"""

# Quiz-2 Write a python program to type a content of the list using while loops

blank_list = ["Sumit","Harry","Rohan","Sandesh","Ojas"]

# i = 0

# while i<len(blank_list):
#     print(blank_list[i])
#     i = i + 1

# Range

# for i in range(0,8,2):
#     print(i)

# Step size use the gap between the start stop


# For loop in using else break continue pass

"""
Using else is optoinal when the loop condition become false these else execute
"""

# Else
"""
for i in range(10):
    print(i)

else:
    print("This is inside else of for")
"""

# Break

"""
for i in range(10):
    if (i == 5):
        print("I is 5")
        break
    else:
        print(i)
"""

# continue
"""
for i in range(100):
    if (i >= 5):
        continue
    print(i)
"""