#studying about different types of formatting

#formatting a variable in other sentence
types_of_people = 10
x = f"There are {types_of_people} types of people."

#formatting two variable in a sentence
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

#printing those variables
print(x)
print(y)

#priting those agian with formatting
print(f"I said: {x}")
print(f"I also said: '{y}")

#assigning string to a variable
hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

#using format()
print(joke_evaluation.format(hilarious))

#this prooves that adding string in python add sentence 
w = "This is the left side of..."
e = "a string with a right side."
print(w+e)

#even if integer written within the quotes is counted as string
a = "2"
b = "3"
print(a + b)
