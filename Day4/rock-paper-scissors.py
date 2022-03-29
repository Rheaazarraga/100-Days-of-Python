rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computers_choice = random.randint(0, 2)
print(computers_choice)

# if users_choice == 0:
#   print(rock)
#   if computers_choice == 1:
#     print(paper + "The computer wins")
#   elif computers_choice == 2:
#     print(scissors + "The player wins!")
#   else:
#     print(rock + "It's a draw!")
# elif users_choice == 1:
#   print(paper)
#   if computers_choice == 2:
#     print(scissors + "The computer wins")
#   elif computers_choice == 0:
#     print(rock + "The computer wins")
#   else:
#     print(paper + "It's a draw!")
# else:
#   print(scissors)
#   if computers_choice == 0:
#     print(rock + "The computer wins")
#   elif computers_choice == 1:
#     print(paper + "The player wins!")
#   else:
#     print(scissors + "It's a draw!")

if users_choice >=3 or users_choice <0:
  print("You entered an invalid number, you lose")
elif users_choice == 0 and computers_choice == 2:
  print(f"{rock}\n{scissors} The computer chose scissors. You win! :)")
elif computers_choice == 0 and users_choice == 2:
  print(f"{scissors}\n{rock} The computer chose rock, you lose")
elif computers_choice > users_choice:
  print("You lose")
elif computers_choice == users_choice:
  print("It's a draw!")