# Coding Rooms, Interactive Coding Exercises

# Exercise 1: Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# 1. check the data type of two_digit_number
print(type(two_digit_number)) # string type

# 2. Get the first and second digits by grabbing the index of each, then convert str to int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
# 3. Add the 2 digits together
print(first_digit + second_digit)

