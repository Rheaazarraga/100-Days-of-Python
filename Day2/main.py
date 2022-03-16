# Data Types: Strings, Integers, Floats, Booleans

# String - print the index of "o"
print("Hello"[4])

# Integers/ Numbers - whole numbers, no decimal places
print(123 + 456)
# Large numbers like 1,000,000 can be written as
print(1_000_000)

# Float / Floating Point Number - numbers with decimals
print(3.14159)

# Boolean - True or False

##############################

# Type Error, Type Checking and Type Conversion/ Type Casting

num_char = len(input("What is your name?\n"))
# print("Your name has " + num_char + " characters.") - this results in a type error because you can NOT concatenate strings and integers

# type() function checks what is passed in as params and tells you the data type
print(type(num_char)) # tells us num_char is an integer

# to convert num_char into a string to be concatenated (ref line21) use str() function
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.") # now all the same data type

# another example:

a = 123
print(type(a)) # integer

a = str(123)
print(type(a)) # converted to string

print(70 + float("100.5")) # converting string "100.5" into a floating point #, then adding 70 to it, and printing the result = 170.5

print(type(str(70)+ str(100))) # results in 70100 because it has been converted to string data type

##############################

# Mathematical Operations in Python - +, -, *, /, ** (exponent/ to the power of)
# *note* dividing will always give you a float
print(2**3) # = 8

# PEMDAS: order of operation is a rule that tells the correct sequence of steps for evaluating a math expression - and works from Left to Right (PEMDASLR)
# *note* in Canada, we use BEDMAS, but it's essentially the same and order of multiplcation and division doesn't matter, just work from left to right as mentioned previously
# () parentheses
# ** exponents
# * multiplication
# / division
# + addition
# - subtraction

#  --- PRACTICE EXAMPLE ---
print(3 * 3 + 3 / 3 - 3)
# 3*3 = 9
# 3/3 = 1
# 9+1 = 10
# 10-3 = 7

# --- change line 57 to now equal 3 ---
print(3 * (3 + 3) / 3 - 3)
# (3 + 3) = 6 becomes highest priority
# 3 * 6 = 18
# 18 / 3 = 6
# 6 - 3 = 3

##############################

# Rounding numbers up or down using the round() function
print(8/3) # = 2.66666 floating point number
print(round(8/3)) # = 3
print(round(8/3, 2)) # = 2.67 this second parameter rounds the number to a given precision in decimal points
print(round(8/3, 3)) # = 2.667 and so on
print(8//3) # this floors the number = 2

# important to remember that even with a clean division, ie. 4/2, the result would still return as a floating point number (2.0)

# incrementing and decrementing are the same as JS: +=, -=, *=, /=