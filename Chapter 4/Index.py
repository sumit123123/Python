# List and tuple These are the container in python to stores the data in the string , int , float or boolen

# List

# Initialize list 
My_List_1 = [1,5,3,4,2]

# print(My_List_1)

# This code genrally pring the items inside the list container

# List indexing

'''
A list can be index by how the string get index

1. [0:] - Here the items get print from 0th index to the len of the list

2. [0::2] - Here the items get print from the 0th index to the len of the list keeping  
a 2 index of gap

! both Methods shown below
'''

# 1. 

# print(My_List_1[0:])

# another 

# print(My_List_1[:2])

# 2.

# print(My_List_1[0::3]) 


# Function in the List

# My_List_1.sort() #Sort the list or arrange the list items form assending to desending order

# My_List_1.reverse() #Reverse function reverse all the items in the string

appending_object = 72

# My_List_1.append(appending_object) # Append or add an object inside the list

My_List_1.insert(3, appending_object)

# Deleting function pop and remove

'''
.pop remove the element from the index of the list

.remove remove the element value given in the parameter
'''

print(My_List_1)
