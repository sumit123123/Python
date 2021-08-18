# *Args and **kwargs 

def function(*para1):
    print("Name is ",para1[0], "Class is ",para1[1] , "Roll no is ", para1[2])

detail_list = ["Sumit Ghotane",9,44589]


    # function(*detail_list)

"""
*args are used to set multiple value by taking n no or value 

*args create a tuple in which your value get add and display by the index 

you can also provide a list of argument and type the *listname 
syntax shown above

You can also set the any name of the args but the important thing is used the *before
"""


"""
**kwargs
"""

def Show_marks(**marks):
    for name , marks in marks.items():
        print("Student "+name+" Marks "+marks)

marklist = {
    "Sumit":"78",
    "Omkar":"85",
    "Atharv":"71"
}

if (__name__ == '__main__'):
    Show_marks(**marklist)