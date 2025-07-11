# Rock, Paper, Scissors - tracking how many times user vs PC wins

import random

play = input("welcome to the Rock / Paper / Scissors Game! Are you ready to play? ")

if play.lower() == "yes":
    print("Cool, let's go then!")
else: 
    quit()

user_wins = 0
pc_wins = 0

while True:
    pick = input("Rock / Paper / Scissors? ")
    if pick.lower() in ["rock","paper","scissors"]:
        rnd = random.randint(0,2)
        options = ["rock","paper","scissors"]
        pc = options[rnd] 
        if pick.lower() == "rock" and pc == "scissors":
            user_wins +=1
            print("Computer picked scissors - you won!")
            continue
        if pick.lower() == "paper" and pc == "rock":
            user_wins +=1
            print("Computer picked rock - you won!")
            continue
        if pick.lower() == "scissors" and pc == "paper":
            user_wins +=1
            print("Computer picked rock - you won!")
            continue
        if pick.lower() == pc :
            print("Draw!")
            continue
        else:
            pc_wins += 1
            print("Computer picked ", pc , ". Computer won!")
    elif pick.lower() == "q": 
        print("Finish! You won", user_wins,"times and PC won", pc_wins,"times.")
        quit()
    else:
        print("Invalid entry.")
        continue
