"""
Q-1 Write a python program to create dict and set key is a English word and its value is in translation in hindi and user can get the value by input

Q-2 Write a python program to take 8 number input from the user and then display them uniquely
"""

# Q.1

Word_list = {
    "Answer":"उत्तर",
    "Question":"सवाल",
    "language":"भाषा",
    "Place":"जगह"
}
# inp = input("Enter the word\n")

# print(Word_list[inp])

# 2 

sets = set()

input_1 = input("Enter the number")
input_2 = input("Enter the number")
input_3 = input("Enter the number")
input_4 = input("Enter the number")
# input_5 = input("Enter the number")
# input_6 = input("Enter the number")
# input_7 = input("Enter the number")
# input_8 = input("Enter the number")

set1 = set(input_1,input_2,input_3,input_4)

print(set1)