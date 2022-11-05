from sys import argv

#prompting user from cla
script, input_file = argv

#this function print all the text in the file 
def print_all(f):
    print(f.read())

#this function goes back to the beginning of the file
def rewind(f):
    f.seek(0)

#this function prints one line at a time
def print_a_line(line_count, f):
    print(line_count, f.readline(), end= '')

#opening the file
current_file = open(input_file)

print("First let's print the whole file:\n")

#printing the whole file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#using rewind function to get to the beginning of the file
rewind(current_file)

print("Let's print three lines:")

#printing line no. 1, 2, 3
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)