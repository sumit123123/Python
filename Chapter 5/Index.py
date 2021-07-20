"""
In these Chapter we get learn about the Dictionary and the set

1. Dictionary and set is a data type to collect data

2. Initializeing the dict and set is like these

dict :- {"Key":"Value"}

set :- s = set{ items , items }

3. Data inside the dict is keep in the key = value pair and no repeatation allowed in the set
"""

# Dict
"""
Properties of python dict
1. It is unordered - Not in a order
2. It is mutable - can be change
3. It is indexed - We can access key by the index also
4. cannot contain duplicate key = Multiple value can be their but not any multiple key
"""
My_dict = {"Name":"Sumit"}


# Print the list in the output form {'Name': 'Sumit'}

# .items gives the all key and value inside the dict

# .keys gives the all keys inside the dict

# .update updates all the dict by taking input key and value syntax be like

# .get() gets the value of the key given inside the bracket

"""
Syntax

.update({key:value})
"""
# print(My_dict.get("Name"))


# Set

a = {1,2,3,3,2,1,5}

# print(a)

# Important empty {} did not give the type set it give type as Dictionary

a = set()
# print(type(a))

# Adding items in the set

a.add(72)
# print(a)

# We cannot add a list inside the set but we can add the tuple inside the set and dict also.

# Mutable objects can only add into a set a list and a dict can be changed so 

import pyttsx3

engine = pyttsx3.init()

engine.say("ahahahahahahahahahahahahahahahahahahahahahahahahahahahaha")

engine.runAndWait()