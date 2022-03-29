# For Loop
# for item in list_of_items:
   #Do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    #print(fruit)
    print(fruit + " Pie")
    print(fruits) # prints the list and iterates 3 times because there's 3 items in the list
print(fruits) # prints the list once because it's outside the loop

##############################

# For loops with the range function
# if you want to generate a range of numbers to loop through
for number in range(1, 10): # *does not include 10*
    print(number)
# by default, the range function will step through all numbers from the start to the end and increment by 1
# otherwise, you can add a third parameter indicating how much you want to increment (step) by
for number in range(1, 11, 3):
    print(number) # outputs 1, 4, 7, 10

##############################

total = 0 # accumulator
for number in range(1, 101): # for 1 - 100
    total += number # add every number in the range to the total
print(total) # = 5050