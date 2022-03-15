# basic printing:
print("Hello World! This is my first time using Python!")

# print on a new line:
print("Hello World!\nThis is my first time using Python!\nPython is cool!")

##############################

# string concatenation:
str1 = "Hello "
str2 = "Bita"
print(str1 + str2)
# OR add a separate empty string between "Hello" and "Bita"
print("Hello" + " " + "Bita")
# OR with a space after "Hello"/ before "Bita"
print("Hello " + "Bita")

##############################

# Python input() function: allows the user to input in the console
# Then print() will print the word "Hello" and the user input
# input("What is your name?") will prompt the user to respond in the console
print("Hello " + input("What is your name?") + "!")

# variables
name = input("What is your name?")
# variable is attached to the input value - data is saved from input action to a name
print(name)
# refactor print(len(input("What is your name?"))) by using variables
length = len(name)
print(length)