import random
def main():
    print("Welcome to Rock Paper Scissors!")
    print("These are the Rules:Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    choices = ["rock", "paper", "scissors"]

    player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    print(f"You chose: {player_choice}")
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")


if __name__ == "__main__":
    main()