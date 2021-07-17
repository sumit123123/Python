b = 'Harry"s'
greeting = "Good boy"

# print(type(b))

# concating two strings
c = b+greeting

# Get length of the string
# print(len(b))

# print(c)

# String slicing

# print(greeting[0:2+1])

# Negative indensix

# print(greeting[:4])
# If you place this space none it will take it as 0

# print(greeting[0:])

'''if you place end index clear then it will take the len to the string'''

# print(greeting[-4:-1])

# slicing with skip value
harr = "my name is jack potter"

d = harr[0::3]
# print(d)

# # Skiping value index start from 1

# # Endswith

# End = harr.endswith("mE")

# print(End)

# # Count
# End = harr.count("m")
# print(End)

# Capitalize 
End = "my name is jack potter"
# print(End.capitalize())
# Capitalize the index 1 charecter

# Find

# print(End.find("jack potter"))

# Gives the index of that string

# Replace
replace = End.replace("jack potter", "George griffendor")

# print(replace)
# Replace the old value from new value


# Escape sequance charecter

story = "Harry is good \n\tgeorge is good\nsnape is bad"

print(story)