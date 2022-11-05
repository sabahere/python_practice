#here we can open and read file and print it out 
from sys import argv

#opening and reading file using argv as an input from user
script, filename = argv

#open file
txt = open(filename)

#printing the text 
print(f"Here's your file {filename}:")
print(txt.read())

#prompting user again for filename
print("Type the filename again:")
file_again = input("> ")

#open that file using open()
txt_again = open(file_again)

#printing text contained by that file
print(txt_again.read())

#closing both files
txt.close()
txt_again.close()


