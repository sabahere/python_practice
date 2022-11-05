from sys import argv

#prompting user a filename form command line argument 
script, filename = argv

#asking user if they want to erase the file
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

#opening the file
print("Opening the file...")
target = open(filename, 'w')

#emptying file
print("Truncating the file. Goodbye!")
target.truncate()

#prompting user for 3 new lines
print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#writing those 3 lines into that same file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#close that file
print("And finally, we close it.")
target.close()