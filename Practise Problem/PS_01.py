"""
Q.1 Write a python program to print the version of the python.

Q.2 Write a Python program to display the current date and time.

Q-3 Write a Python program which accepts the radius of a circle from the user and compute the area.

Q-4 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

Q-5 Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

Q-6 Write a Python program to accept a filename from the user and print the extension of that

Q-7 Write a Python program to display the first and last colors from the following list

Q-8 Write a Python program to display the examination schedule. (extract the date from exam_st_date)

Q-9 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

Q-10 Write a Python program to print the calendar of a given month and year.
"""

"""
What to search
1. What is %S while printing 
"""

# q.1
"""
1. Open the terminal
2. Type python --version

You will get the output
"""

# q.2

# import time as tt

# print(tt.asctime(tt.localtime(tt.time())))

# q.3

# radius = float(input("Enter the radius:\n"))

# print(22/7*radius*radius)

# q.4

# inp = str(input("Enter your first name:\n"))

# inp_1 = str(input("Enter your last name:\n"))

# print(inp_1,inp)

# q.5

# input_1 = int(input("Enter the number\n"))
# input_2 = int(input("Enter the number\n"))
# input_3 = int(input("Enter the number\n"))
# input_4 = int(input("Enter the number\n"))

# blank_number_list = []

# blank_number_list.append(str(input_1))
# blank_number_list.append(str(input_2))
# blank_number_list.append(str(input_3))
# blank_number_list.append(str(input_4))

# print(blank_number_list)

# tup = (str(input_1),str(input_2),str(input_3),str(input_4))

# print(tup)

# Q-6

# file_name = str(input("Enter the file name\n"))

# if ("." in file_name):
#     jk = file_name.find(".")
#     sliceing = file_name[jk:]
#     print(sliceing)

# else:

#     print("Try again!!!")

# Q-7

# 1 way
# color_list = ["Red","Green","White" ,"Black"]

# print(color_list[::3])

# Note while space scling the indexing number start from the 1 to infinite

# 2 Way

# print(color_list[0],color_list[-1])

# Note slicing list in reverse from end to start can be start by negative property like -1 -2 -3 The will give the index from the end

# Q-8

# exam_st_date = [26, 1, 2022]

# print(f"Examination date is: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}",)

# Q-9

# 1 way

# n = int(input("Enter the number:\n"))

# n1 = int(n)
# n2 = int(n,n)
# n3 = int(n,n,n)

# print(n1*n2*n3)

# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# Q-10

import calendar

y = int(input("Enter the year"))

print(calendar.calendar(y))