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
a.add(45)
a.add(75)
a.add(1)
# print(a)

# We cannot add a list inside the set but we can add the tuple inside the set and dict also.

# Mutable objects can only add into a set a list and a dict can be changed so 

# Get the length of the set

# print(len(a))

# print(a)

# a.remove(2)
# Removes the items from the set

# Throw error like this when item in not their in the set
# KeyError: 2
# print(a)

# print(a)

# print(a.pop())
# Removes a random element

# print(a)

# a.clear()
# clear the items

# print(a)


"""
Medium level Sets in mathematics

1. Union
The union() method returns a set that contains all items from the original set, and all items from the specified set(s)

in set the item is in order but when we use union fucntion it get unordered

syntex shown below
"""

set_2 = {-111,-112,113}

z = set.union(a,set_2)

# print(z)

x = {"Apple","Microsoft","Amazon"}

y = {"NASA","Amazon","Space-x","More-Earth","Deep Mining"}

A = x.intersection(y)

print(A)

"""
Intersetion is a method in which you can interset two element and inside that elements if any items is similar then you get it in a return

syntex show above
"""