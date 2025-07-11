#Number guesser -> generate a random number and track how many times it takes user to guess this number

import random


# Requesting an upper limit input
while True: 
    limit = input("Please provide an upper limit for me to generate a random number: ")
    if limit.isdigit() and int(limit) > 1:
        limit = int(limit)
        rnd = random.randint(0, limit)
        break
    else:
        print("Invalid entry.")

attempts = 0

# Guess Game
while True:
    while True:
        guess = input("Take a guess: ")
        if guess.isdigit():
            guess = int(guess)
            break
        else: print("Invalid entry.") 
    if  guess > rnd:
            print("That is above.")
            attempts += 1
            continue
    elif guess < rnd:
            print("That is below.")
            attempts += 1
            continue
    else: 
            print("That's correct!")
            attempts += 1
            print("You got at in ", attempts, " attempt.")
            break

