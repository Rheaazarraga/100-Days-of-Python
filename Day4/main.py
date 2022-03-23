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