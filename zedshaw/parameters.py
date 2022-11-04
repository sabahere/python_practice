from sys import argv
#running using argv(command line argument)
#argv is argument variable

#it assign the value from command line to all these variable from left to right
script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)