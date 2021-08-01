"""
File IO

In every programming language their is ability to read and write. Example in JS you can read it by the Fetch on XMLHTTPREQUEST but in python it is very simple just 5 to 6 lines of the code

Types of files:
There are two types of files:

1. Text Files (.txt etc)
2. Binary Files(.jpg etc)

How to open the file and read?

-> Python file can be open by the function "open" and "with"

syntax:

file = open("Index.txt","r")
print(file.read())

.read() is used to read all the text

.readlines() is append in a list and acces it by a loop

.readline() is the function is used access the value by the index in the first line index can be given by the parameter

.readable() is the function is return True if the file is readable or not.
"""

# Opening File
file = open("Index.txt","r")

if (file.readable() == True):
    print(file.read())

else:
    print("Not a readable file")