#functions can return something

#add function
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a+b

#substract function
def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a-b

#divide function
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a/b

#multiply function
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

print("Let's do some math with just functions!")

age = add(20, 1)
height = substract(70, 8)
weight = multiply(40, 1)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

#what is the value of this line
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what)