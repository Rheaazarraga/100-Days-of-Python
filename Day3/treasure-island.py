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
print("Your mission is to find the treasure and escape with your life.")

crossroad = input('You are at a crossroad. Which path will you take? Type "left" or "right": ').lower()
if crossroad == "left":
    print("You have stumbled upon a murky swamp surrounded by a forest.")
    nextChoice = input('Will you trench through the swamp or go through the forest? Type "swamp" or "forest": ').lower()
    if nextChoice == "forest":
        print("You race through the trees in the dark forest, and see a mysterious hut ahead with the windows lit up.\nAs you approach the hut, you notice 3 different colored doors.")
        doors = input('It\'s clear you are meant to go through only one of the doors. Which will you choose? Type "red", "green" or "blue": ').lower()
        if doors == "red":
            print("You walk into a dark room and are set on fire. You burn to death.")
        elif doors == "green":
            print(
                "As you enter, you step in a bear trap.\nYou hear a large growl come from the opposite corner of the room with beaming red eyes coming closer towards you.\nParalyzed by your fear and inability to move, you let out a bloodcurdling scream.\nGame over.")
        else:
            print(
                "You find a mound of disturbed ground in the center of the room, and a rusty shovel on the floor next to it.\nYou begin to dig and suddenly, you hit something with a loud 'KLANG!'\nCongrats!! You found the treasure!")
    else:
        print("You feel something swimming beside you but can't see through the water...\nYou try to swim faster in a panick, but the thing pulls you into the water with it. You drown to death.")
else:
    print("The end of the path leads to a cliff. You take a step forward to see what lies below. The ground quickly collapses beneath you and you fall to your death.")