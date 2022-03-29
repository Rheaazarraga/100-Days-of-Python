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
game_choices = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if users_choice >=3 or users_choice <0:
  print("You entered an invalid number, you lose")
else:
  print(game_choices[users_choice])

computers_choice = random.randint(0, 2)
print("The computer chose:")
print(game_choices[computers_choice])

if users_choice == 0 and computers_choice == 2:
  print(f" You win!")
elif computers_choice == 0 and users_choice == 2:
  print(f"You lose")
elif computers_choice > users_choice:
  print("You lose")
elif users_choice > computers_choice:
  print("You win!")
elif computers_choice == users_choice:
  print("It's a draw!")