"""
Conditional Expression

if, else, elif is the multiway dicision making using the python program

syntex show below

This is known as the if else ladder

You can set unlimited elif inside the if else ladder 

their is indentation or 4 space after give the condition and colen in which the code was written to show whats happen when these condition is true

Multiple if statement
when you put multiple if statement they are individual in if else ladder but when you type else after the if they both become the ladder. If the single if statement get false than the output gets none or no output come

Relational Operator 
Relational operator are used to find relation between the variable to find is variable equal to greater than smaller than
Sign shown below:
== - Equal to 

=> - Equal to greater than

<= - Equal to less than

!= - Not equal to 

elif clause
when a if and else meet up the else if ladder stop at that way
"""

a = int(72)

if (a == int(100)):
    print("A is smaller than 100")
elif (a <= int(45)):
    print("A is smaller than 45")
elif (a <= int(72)):
    print("A is smaller than 40")
elif (a < int(30)):
    print("A is smaller than 30")
else:
    print("A is greater than 100")


"""
Quick quiz

inp = int(input("Enter the age\n"))

if (inp > 18):
    print("Ok your age is greater than 18")

elif (inp == 18):
    print("Ok your age is equal to 18")

else:
    print("Your age is smaller than 18")
"""