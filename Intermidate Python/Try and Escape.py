# try:
#     file = open("this.txt","r")
#     print(file.read())

# except Exception as e:
#     print("No any This.txt file")

try:
    file = open("Changu.txt","r")

except Exception as e:
    print(EOFError.__name__)

finally:
    print("All done")