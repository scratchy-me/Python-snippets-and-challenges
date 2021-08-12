import random

def playerGo():
    user_selection = input("Pick rock (r), paper (p) or scissors (s)")
    if user_selection not in ["r","p","s"]:
        print("I'm not sure what you mean")
        user_selection = input("Pick rock (r), paper (p) or scissors (s)")
    return user_selection

def computerGo():
    computer_selection = random.randint(1,3)
    if computer_selection == 1:
        computer_selection = "r"
    if computer_selection == 2:
        computer_selection = "p"
    if computer_selection == 3:
        computer_selection = "s"
    return computer_selection

playerLives = 3
computerLives = 3

while playerLives >0 and computerLives >0:
    player = playerGo()
    computer = computerGo()
    print("------Player chose:", player, "---------")
    print("------Computer chose:", computer, "-------")
    if player == "r" and computer == "s" or player == "s" and computer=="p" or player =="p" and computer =="r" :
        computerLives = computerLives - 1
        print("You won this round.")
        print("You have ", playerLives, "lives remaining")
        print("The computer has ", computerLives, "lives remaining")
    elif computer == "r" and player == "s" or computer == "s" and player=="p" or computer =="p" and player == "r" :
        playerLives = playerLives -1
        print("Haha, you lost this round")
        print("You have ", playerLives, "lives remaining")
        print("The computer has", computerLives, "lives remaining")
    else:
        print("Draw!")
        print("You have", playerLives, "lives remaining")
        print("The computer has", computerLives, "lives remaining")

if playerLives == 0:
    print("Haha! Loserrr")
elif computerLives == 0:
    print("Yay - you won")