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

if height > 120: # uses colon's instead of {}'s
    print("You can ride the rollercoaster!") # within the scope of the if
else:
    print("Sorry, you're not tall enough to ride.") # within the scope of the else