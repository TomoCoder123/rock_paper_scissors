def main():
    print("Welcome to Rock Paper Scissors!")
    print("These are the Rules:Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    print(f"You chose: {player_choice}")

if __name__ == "__main__":
    main()