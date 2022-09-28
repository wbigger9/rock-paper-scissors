#rock-paper-scissors
 


    
def determine_winner():
    choice1 = input("choose your fighter: ")
    choice2 = input("choose your fighter: ")
    
    if choice1 == "rock" and choice2 == "scissors":
        print("player 1 wins")
    elif choice1 == "scissors" and choice2 == "rock":
        print("player 2 wins")
    elif choice1 == "scissors" and choice2 == "paper":
        print("player 1 wins")
    elif choice1 == "paper" and choice2 == "scissors":
        print("player 2 wins")
    elif choice1 == "paper" and choice2 == "rock":
        print("player 1 wins")
    elif choice1 == "rock" and choice2 == "paper":
        print("player 2 wins")
    elif choice1 == choice2:
        print("it's a tie: go again")

determine_winner()