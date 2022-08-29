import random
def play():
    user = input("pick rock (R) , paper (P) or scissors (S)").upper()
    computer = random.choice(["R","P","S"])
    if user == computer:
        print(f"computer choose {computer}")
        return "Its a tie"
    elif (user == "R" and computer == "S") or (user == "S" and computer == "P") or (user == "P" and computer == "R"):
        print(f"computer choose {computer}")
        return "You Won"
    else:
        print(f"computer choose {computer}")
        return "You Lost"


print (play())






