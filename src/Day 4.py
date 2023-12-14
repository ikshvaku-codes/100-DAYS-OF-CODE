#Day 4:- Randomization and Python Lists
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

userChoice = int(input("Make your choice: Rock(0), Paper(1), Scissors(2), ..."))

if userChoice == 0:
    print(rock)
elif userChoice == 1:
    print(paper)
elif userChoice == 2:
    print(scissors)
else:
    print("Invalid Choice")

if userChoice <=3 or userChoice>0:  
    computerChoice = random.randint(0,3)

    print("Computer Choice: ")
    if computerChoice == 0:
        print(rock)
    elif computerChoice == 1:
        print(paper)
    elif computerChoice == 2:
        print(scissors)
    
    if userChoice == computerChoice:
        print("GAME DRAWN!!!!!!!!!!!")
    elif userChoice > computerChoice and computerChoice - userChoice == 1:
        print("YOU WON")
    elif userChoice == 0 and computerChoice == 2:
        print("YOU WON")
    else:
        print("YOU LOSE")
        
    

