import random
def main():
    print("Welcome to Rock Paper Scissors!")
    print("These are the Rules:Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    choices = ["rock", "paper", "scissors"]

    player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    print(f"You chose: {player_choice}")
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
    play_again = input("Do you want to play again? yes/no: ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    main()