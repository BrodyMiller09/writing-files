#-----------------------------
# Brody Miller
# Writing files
# 10/15/2026
#-----------------------------

file = open("my_file.txt", "w")
file.write("hello welcome to my text\n")
file.write("I am writing this in a code and its writing in a file thats cool.")
file.close

file = open("my_file.txt", "r")
content = file.read()
print("here is my information in the file:")
print(content)
file.close()