#Ask a user questions and add 1 if correct to their score -> print e.g. 7 out of 10 and % correct

play = input("Welcome to the Quiz Game! Would you like to play (yes / no): ?")

score = 0
if play.lower() == "yes":
    print("Ok let's play!")
    q1 = input("What does CPU stand for? ")
    if q1.lower() == "central processing unit":
        print("That's correct!")
        score +=1
    else:
        print("That's incorrect!")
    q2 = input("What does GPU stand for? ")
    if q2.lower() == "graphical processing unit":
        print("That's correct!")
        score +=1
    else:
        print("That's incorrect!")
    q3 = input("What does GM stand for? ")
    if q3.lower() == "gross margin":
        print("That's correct!")
        score +=1
    else:
        print("That's incorrect!")
    q4 = input("What does AR stand for? ")
    if q4.lower() == "accounts receivable":
        print("That's correct!")
        score +=1
    else:
        print("That's incorrect!")
else:
    quit()

print("Game is over. Your score is ", score, " points." )
print("That's ", ((score / 4) *100), " percentage points." )
