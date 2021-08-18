def Add_Details(*det):
    for item in det:
        student = 'Name is {item[0]} Class is {item[1]} Roll no is {item[2]}'

    return student
    print("Student detail has been added")

def Show_Student():
    a = Add_Details()
    print(a)

details = ["Sumit","9","36"]

Add_Details(details)

Show_Student()