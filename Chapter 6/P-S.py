"""
Q-1 Find the greatest number given from the four user as input?

Solution - code:

Number_1 = int(input("Enter the number:\n"))
Number_2 = int(input("Enter the number:\n"))
Number_3 = int(input("Enter the number:\n"))
Number_4 = int(input("Enter the number:\n"))


Final_Number_1 = 0

Final_Number_2 = 0

if (Number_1>Number_2):
    Final_Number_1 = Number_1

else:
    Final_Number_1 = Number_2

if (Number_3>Number_4):
    Final_Number_2 = Number_3

else:
    Final_Number_2 = Number_4

if (Final_Number_1>Final_Number_2):
    print(Final_Number_1," is the greatest of all")

else:
    print(Final_Number_2," is the greatest of all")

Q-2 Give the output is student fail or pass assuming that their total percentage is above 40 and each subject above 33 percentage. Take marks as input

Solution - code

Percentage formula - value/100*total marks

Subject_1 = int(input("Enter the marks:\n"))
Subject_2 = int(input("Enter the marks:\n"))
Subject_3 = int(input("Enter the marks:\n"))

total_subject_1_marks = Subject_1/100*80
total_subject_2_marks = Subject_2/100*80
total_subject_3_marks = Subject_3/100*80

total_mark = Subject_1+Subject_2+Subject_3/100*240

if (total_mark > 80):
    print("You are pass your total score is {}".format(total_mark))
    if (total_subject_1_marks and total_subject_2_marks and total_subject_3_marks >=40):
        print("You are pass in all subject")
    else:
        print("You failed in a subject")

else:
    print("You got failed your total score is {}".format(total_mark))

Q-3 Write a spam detection program.

Solution - Code

span_comment = """
"make a lot of money, click this , subscribe this , buy now"
"""

if (len(span_comment) == 0):
    print("Nothing in spam comment")

else :
    print("Some text is inside the span comment"),
    ask = str((input("Enter Y or N:\n")))

    if (ask == "Y"):
        print(span_comment)
    else:
        print("Ok ,not opening the Comment")

Q-4 Write a python program to find the username has give the character less than 10 character.

Solution - code

print("The password must be more than 10 character")
Name = str(input("Enter the password\n"))

if (len(Name) >10):
    print("Ok this will set is your password")
else:
    print("Please re-enter the password")

Q-5 Write a python program to find a given user input name is their in the list 

Solution - code

Name_list = ["Sumit","Shubham","Omkar","Pranav","Ojas","Samarath","Viraj"]

Ask = input("Enter the name:\n")

if (Ask.capitalize() in Name_list):
    print("Yes this name {} is the list".format(Ask.capitalize()))
else:
    print("No this name is not in the name list")


Q-6 Write a python progarm to get grade from the marks

Solution - code

inp = int(input("Enter the Subject number\n"))

if (inp >=90):
    print("Congratulation you got excellent grade")

elif (inp >=80):
    print("Congratulation you got A grade")

elif (inp >=70):
    print("Congratulation you got B grade")

elif (inp >=60):
    print("you got C grade")

elif (inp >=50):
    print("you got D grade")

else:
    print("Do better you got failed")

Q-7 Write a program to find a post is taking about harry or not 

Solutin - code
"""

Post = """
Articles are words that define a noun as specific or unspecific. Consider the following examples:

After the long day, the cup of tea tasted particularly good.
By using the article the, we’ve shown that it was one specific day that was long and one specific cup of tea that tasted good.
After a long day, a cup of tea tastes particularly good.
By using the article a, we’ve created a general statement, implying that any cup of tea would taste good after any long day.

Harry

Solution - code

if ("Harry" in Post):
    print("Yes their is harry in the post")
    print(len(Post))
    print(Post.index("Harry"),"This is the index")
else:
    print("No their is no harry in the post")
"""

Subject_1 = int(input("Enter the marks:\n"))
Subject_2 = int(input("Enter the marks:\n"))
Subject_3 = int(input("Enter the marks:\n"))

total_subject_1_marks = Subject_1/100*80
total_subject_2_marks = Subject_2/100*80
total_subject_3_marks = Subject_3/100*80

total_mark = Subject_1+Subject_2+Subject_3/100*240

if (total_mark > 80):
    print("You are pass your total score is {}".format(total_mark))
    if (total_subject_1_marks and total_subject_2_marks and total_subject_3_marks >=40):
        print("You are pass in all subject")
    else:
        print("You failed in a subject")

else:
    print("You got failed your total score is {}".format(total_mark))