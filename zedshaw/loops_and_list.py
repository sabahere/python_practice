#Loops and List

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#for-loop
for number in the_count:
    print(f"This is count {number}.")

for fruit in fruits:
    print(f"A fruit of type: {fruit}.")

for i in change:
    print(f"I got {i}")

elements = []

#range(x, y) starts from x and goes to y-1
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a function to add something to the list
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")