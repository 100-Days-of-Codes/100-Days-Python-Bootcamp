import random

art =[ """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
, """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
, """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choose = random.randint(0, 2)

print("You choose:")
print(art[user_choose])

print("Computer choose:")
print(art[computer_choose])

if user_choose == computer_choose:
    print("It's a draw!")
else:
    if user_choose == 0:
        if computer_choose == 1:
            print("You lose!")
        else:
            print("You win!")
    if user_choose == 1:
        if computer_choose == 2:
            print("You lose!")
        else:
            print("You win!")
    if user_choose == 2:
        if computer_choose == 0:
            print("You lose!")
        else:
            print("You win!")