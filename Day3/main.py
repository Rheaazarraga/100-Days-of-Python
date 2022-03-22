# conditional statements: if/ else:
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

##############################

# replit example:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: # testing condition uses colon's instead of {}'s
    print("You can ride the rollercoaster!") # within the scope of the if
else:
    print("Sorry, you're not tall enough to ride.") # within the scope of the else

##############################

# remember comparison operators : >x, <x, >=x, <=x, ==, !=
# single = is assigning a value to a variable, double == check's the equality of values

# modulo operator % (same as JS) gives you the remainder after a division:
# 7 % 2  - 7 split into portions of 2 is 2 + 2 + 2 + 1 (can be divided 3 times with a remainder of 1)
# 7 % 2 = 1
# 7 % 3 = 3 + 3 + 1 (leaves remainder of 1)

##############################

# nested if/ else & elif statements:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18: # catches everybody between the ages of 12-18
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
    # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}") #note the indentation
else:
    print("Sorry, you're not tall enough to ride.")

##############################

# Logical Operators - combining conditions
# and, or, not

# a = 12
# a > 15 = false
# a > 10 = true
# a > 10 and a < 13 =  true
# a > 15 and a < 13 = false (if one condition is false, automatically becomes false)

# if only 1 condition needs to be true, use or operator

# not operator reverses a condition - if a condition is true, it becomes false and if false, becomes true
# not a > 15 = true because 12 is not greater than 15


