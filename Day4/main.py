# Randomisation

# deterministic - like computers, performs repeatable actions in a predictable way - pseudorandom number generator -  produced by an algorithm that generates a series of bits that appear unpredictable, but in fact are computed from an algorithm
# nondeterministic - a nondeterministic function may return different results every time it is called, even when the same input values are provided - a truly random number is a number selected from a range with each number in the range having equal and completely unpredictable chance of selection
# python uses the Mersenne Twister pseudorandom number generator (PRNG)

# using the random module - refer to askpython.com for documentation, tutorials, and examples
import random
random_integer = random.randint(1, 10) # specifying a range of numbers, including 1 and 10
print(random_integer)

# creating a random floating point number again refer to askpython.com
randomFloat = random.random() # returns the next random floating point number between 0.0 to 1.0, but does NOT include 1.0
print(randomFloat)

# how to create a random decimal number between 0 and 5?
randomFloat = random.random() * 5
print (randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

##############################

# Lists: are a data structure - just like arrays in JS
# store many pieces of related data with the same order of indices starting at 0
# fruits = ["apple", "banana"]
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
print(states_of_america[0]) # prints Delaware
print(states_of_america[-1]) # negative index will count backwards from the end of the list - prints Connecticut
states_of_america[1] = "Pencilvania" # reassigns the value of the item at index 1

states_of_america.append("Bitaland") # append function adds a single item to the end of the list
states_of_america.extend(["Bitaland, Besquitteropolis"]) # adds to the states of america list and extends it by 2 more items
# along with many other list functions found in python docs

# IndexError: index out of range error are common with large lists, usually occur when the index doesn't exist. Remember to use [index] - 1
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# how can we use lists to keep them within the same dirty_dozen container, but separate the fruits and vegetables?
# you can make 2 lists:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]
# then use nested lists!
dirty_dozen = [fruits, vegetables]
print(dirty_dozen) # [[], []]