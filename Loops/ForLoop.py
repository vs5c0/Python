# for loop --> is a loop used to repeat a block of code until the condition is true
# if condition is false loop stop execution.

# Example 1

for animal in "Elephant":
    print(animal)

# Example 2 by using the List

friends = ["Ram","Kiran","Varma"]
for name in friends:
    print(name)

# Example 3 by using index
for index in range(10):
    print(index)


# Example 4 using list with index

Hero = ["Vikas","Ajay","Varma"]
for index in range(len(Hero)):
    print(Hero[index])

# Example 5 by using a if cond stmt

frie = ["ram","vidya","Var"]

for index in range(3):
    if index == 0:
        print("First iteration")
else:
    print("Not a First iteration")
