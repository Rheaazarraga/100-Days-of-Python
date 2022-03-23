print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input("You are at a crossroad. Which path will you take? Type left or right: ")
if crossroad == "left":
    print("You have stumbled upon a murky swamp surrounded by a forest.")
    nextChoice = input("Will you trench through the swamp or go through the forest? Type swamp or forest: ")
    if nextChoice == "swamp":
        print("You feel something swimming beside you but can't see through the water...\nYou try to swim faster in a panick, but the thing pulls you into the water with it. You drowned to death.")
    else:
        print("You race through the trees in the dark forest, and see a mysterious hut ahead with the windows lit up.\n As you approach the hut, you notice 3 different colored doors.")

else:
    print("The end of the path leads to a cliff. You take a step forward to see what lies below. The ground quickly collapses beneath you and you fall to your death.")