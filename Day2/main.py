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