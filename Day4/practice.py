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

#Write your code below this line 👇
