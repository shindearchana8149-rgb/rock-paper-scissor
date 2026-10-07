import random

choices = ["rock", "paper", "scissors"]
while True:
    user = input("rock/paper/scissors (q to quit): ").lower()
    if user == "q": break
    if user not in choices:
        print("Invalid choice."); continue
    computer = random.choice(choices)
    print("Computer:", computer)
    if user == computer: print("Draw!")
    elif (user, computer) in [("rock","scissors"),("paper","rock"),("scissors","paper")]:
        print("You win!")
    else: print("Computer wins!")
