import random

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

choise = input("type paper, scissors, or rock: ")
if choise == "scissors":
    x = 0
elif choise == "paper":
    x = 1
elif choise == "rock":
    x = 2

opponent = random.randint(0,2)
if opponent == 0:
    y = "scissors"
elif opponent == 1:
    y = "paper"
elif opponent == 2:
    y = "rock"

if x == 0 and y == "paper":
    print(f'You choose scissors: \n{scissors}')
    print(f'Your oponent choose paper: \n{paper}')
    print("you won")
elif x == 0 and y == "rock":
    print(f'You choose scissors: \n{scissors}')
    print(f'Your oponent choose rock: \n{rock}')
    print("you loose")
elif x == 0 and y == "scissors":
    print(f'You choose scissors: \n{scissors}')
    print(f'Your opponent choose scissors: \n{scissors}')
    print("Draw")

if x == 1 and y == "rock":
    print(f'You choose paper: \n{paper}')
    print(f'Your oponent choose rock: \n{rock}')
    print("you won")
elif x == 1 and y == "scissors":
    print(f'You choose paper: \n{paper}')
    print(f'Your oponent choose scissors: \n{scissors}')
    print("you loose")
elif x == 1 and y == "paper":
    print(f'You choose papers: \n{paper}')
    print(f'Your opponent choose paper: \n{paper}')
    print("Draw")

if x == 2 and y == "scissors":
    print(f'You choose rock: \n{rock}')
    print(f'Your oponent choose scissors: \n{scissors}')
    print("you won")
elif x == 2 and y == "paper":
    print(f'You choose rock: \n{rock}')
    print(f'Your oponent choose paper: \n{paper}')
    print("you loose")
elif x == 2 and y == "rock":
    print(f'You choose rock: \n{rock}')
    print(f'Your opponent choose rock: \n{rock}')
    print("Draw")