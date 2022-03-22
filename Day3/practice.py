# Coding Rooms, Interactive Coding Exercises

# Exercise 1: Odd or Even
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore, the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# ------------------------------------------------------------

# Exercise 2:
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# Try to use the exponent operator in your code.
# Remember to round your result to the nearest whole number.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# ------------------------------------------------------------

# Exercise 3: Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how you work out whether if a particular year is a leap year:
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# must be cleanly divisible by 4
# must also NOT be cleanly divisible by 100
# must also be cleanly divisible by 400

if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print("Leap year.")
else:
    print("Not leap year.")

# ------------------------------------------------------------

# Exercise 4: Python Pizza
# Build a pizza order program
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# S = 15
# M = 20
# L = 25
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# ------------------------------------------------------------

# Exercise 5: Love Calculator
# write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2-digit number.
# Hint 1: Use the lower() function to change all the letters in a string to lower case
# Hint 2: Use the count() function to count the number of times a letter occurs in a string

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

Lovers = name1.lower() + name2.lower()
t = Lovers.count("t")
r = Lovers.count("r")
u = Lovers.count("u")
e = Lovers.count("e")

true = t + r + u + e # this is the first digit of the love score

l = Lovers.count("l")
o = Lovers.count("o")
v = Lovers.count("v")
e = Lovers.count("e")

love = l + o + v + e # this is the second digit of the love score

Love_score = int(str(true) + str(love)) # must convert strings to ints otherwise comparison operators in conditional statements below will give a type error

if (Love_score < 10) or (Love_score > 85):
    print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif (Love_score >= 40) and (Love_score <= 50):
    print(f"Your score is {Love_score}, you are alright together.")
else:
    print(f"Your score is {Love_score}.")