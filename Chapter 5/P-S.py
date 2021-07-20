"""
Q-1 Write a python program to create a dictionary of hindi words as their translation in the hindi. Provide a user to look all the options

Q-2 Write a program to take 8 numbers as input and display them in unique number

Q-3 Can we have 18(int) and 18(str) in a set
Answer: - Yes we can set the 18 as str and int also because it can give the output type as set without any error output like these

Output:
{18, '18'}
<class 'set'>

Q-4 What will be the length of the set S

s = set()

s.add(20)
s.add(20.0)
s.add("20")

Answer: -The len will be 2 because the float value is 20.0 which generally make the int(20) and as we know that no repeatitation happen inside the Set but the float value is from 1 to infinity then the len will be 3

Q-5 S = {} - What is the type of the s
Answer: -S will be a dict because this is a syntax to initialize a dict but if thier are items in sets forms then it's type go to set

If you want to initialize a empty set you have to use this syntax

s = set(items inside the set)

Q-6 Write a python program to take your four friends input as language and set it as the value and set their name as the key

Q-7 If name of 2 friend same what will happen to program in problem six

Answer: -The value gets overwride and the value before change to new value but no any error came

Q-8 What if the value of two friend are same in the Probelm 6

Answer: - Nothing get's the value set as it no any error came because as we know dict is mutable which mean it can be change so no any error came.

Q-9 Can you change the value inside a list which is inside a set

Answer: - As we know list is mutable and no any mutable data type came inside the set so Therefore the question itself is gives a answer that no list can be change inside the set because list cannot add inside the set
"""

# Q-1 

# Dict = {
#     "Uttar":"Answer",
#     "Prashn":"Question",
#     "Internet":"Internet"
# }

# print(Dict.items())

# inp = input("Enter the Word")

# print((Dict.get(inp.capitalize())))

# Q-2

# inp_1 = input("Enter the number\n")
# inp_2 = input("Enter the number\n")
# inp_3 = input("Enter the number\n")
# inp_4 = input("Enter the number\n")
# inp_5 = input("Enter the number\n")
# inp_6 = input("Enter the number\n")
# inp_7 = input("Enter the number\n")
# inp_8 = input("Enter the number\n")

# s = set()

# s.add(inp_1)
# s.add(inp_2)
# s.add(inp_3)
# s.add(inp_4)
# s.add(inp_5)
# s.add(inp_6)
# s.add(inp_7)
# s.add(inp_8)


# print(s)

# Q-3

# set_both = {"18",18}

# print(set_both)
# print(type(set_both))

# Q-4

# s = set()

# s.add(20)
# s.add(20.8)
# s.add("20")

# print(len(s))

# Q-5

# Friend_list = {}

# for i in range(5):
#     inp_1 = input("Enter your name\n")
#     inp_2 = input("Enter your Programming language\n")

#     Friend_list.update({inp_1:inp_2})


# print(Friend_list)

# Q-6

Friend_list = {}

for i in range(2):
    inp_1 = input("Enter your name\n")
    inp_2 = input("Enter your Programming language\n")

    Friend_list.update({inp_1:inp_2})

print(Friend_list)