# Coding Rooms, Interactive Coding Exercises

# Exercise 1: Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# 1. check the data type of two_digit_number
print(type(two_digit_number)) # string type

# 2. Get the first and second digits by grabbing the index of each, then convert str to int
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
# print(first_digit)
# print(second_digit)
result = int(first_digit) + int(second_digit) # converts the type from string to numbers
# print(type(first_digit))
print(result)

