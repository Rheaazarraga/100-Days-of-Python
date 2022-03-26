# Coding Rooms, Interactive Coding Exercises

# Exercise 1: Heads or Tails
# Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# ** Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

# Write the rest of your code below this line 👇
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# ------------------------------------------------------------

# Exercise 2: Banker Roulette
# write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# ** Important: You are not allowed to use the choice() function.
# Hint: You might need the help of the len() function.

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# get the total number of items in the list
print(len(names))

num_items = len(names)
random_name = random.randint(0, num_items - 1) # because like in JS, the length of a list minus 1 = the index position
# print(random_name)
person_paying = names[random_name]
print(person_paying + " is going to buy the meal today!")

# ------------------------------------------------------------

# Exercise 3: Treasure Map
# Write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.
# Write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number.

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# print(type(position)) = str

horizontal = int(position[0]) # column
vertical = int(position[1]) # row
map[vertical - 1][horizontal - 1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")