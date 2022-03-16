# Coding Rooms, Interactive Coding Exercises

# Exercise 1: Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# 1. Check the data type of two_digit_number
print(type(two_digit_number)) # string type

# 2. Get the first and second digits by grabbing the index of each, then convert str to int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
# 3. Add the 2 digits together
print(first_digit + second_digit)

# Exercise 2: Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1. check the data types
# print(type(height)) = str
# print(type(weight)) = str

# 2. Convert the strings so height(m) becomes a float, and weight(kg) becomes an int
height_as_float = float(height)
weight_as_int = int(weight)

# 3. Use the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# an alternative way using multiplication and PEDMAS:
# bmi = weight_as_int / (height_as_float * height_as_float)

# Change the bmi result to display as a whole number
bmi_as_int = int(bmi)
print(bmi_as_int)
