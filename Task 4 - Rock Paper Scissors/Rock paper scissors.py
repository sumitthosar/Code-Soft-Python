import random

def get_user_choice():
    print("\nChoose one: rock, paper, or scissors")
    choice = input("Your choice: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please type rock, paper, or scissors.")
        choice = input("Your choice: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if result == "tie":
        print("Result: It's a tie!")
    elif result == "user":
        print("Result: You win! 🎉")
    else:
        print("Result: You lose. 😢")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to Rock-Paper-Scissors Game!")
    while True:
        print(f"\n--- Round {round_number} ---")
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)
        
        display_result(user, computer, result)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\nScores: You {user_score} - {computer_score} Computer")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break
        round_number += 1

# Run the game
play_game()
