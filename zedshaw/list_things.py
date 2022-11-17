#Doing things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

#The split function seperate each word and stores it in a list called "stuff"
stuff = ten_things.split(' ')
#Here are some words which are going to be added on the "stuff" list.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
                "Banana", "Girl", "Boy"]

#Adding element from "more_stuff" to "stuff" to complete the sentence in 10 words.
#pop() function takes out one element (from the last) to which it called.
#len() function will calculate total element in the list.
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa ! fancy
print(stuff.pop())

#join() function combines two words using what's given within quotes
print(' '.join(stuff)) #what? cool!
print('#'.join(stuff[3:5])) #super stellar
