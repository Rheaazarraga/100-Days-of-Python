# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input:
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15?"))
num_of_people = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill + bill
# print(bill_with_tip)

# calculating the tip
tip_as_percent = tip / 100
# multiply the bill by percent to get the total tip amount
total_tip_amount = bill * tip_as_percent
# calculating the entire bill with tip included
total_bill = bill + total_tip_amount
# divide the bill total by number of people
bill_per_person = total_bill / num_of_people

final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

# for the original test case amount of $150.00, the result final_amount still prints as #33.6, which is a formatting problem