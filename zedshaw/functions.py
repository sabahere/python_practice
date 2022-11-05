#defining 4 function

#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#we can also do print_two as this
def printTwo_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this one just takes one argument
def print_one(arg1):
    print(f"arg1 : {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'")


print_two("Saba", "Hussain")
printTwo_again("My", "Name")
print_one("one")
print_none()