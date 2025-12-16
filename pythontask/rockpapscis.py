import random

def play_game():
    comp_score = 0
    user_score = 0
    game = ["rock", "paper", "scissors"]

    rounds = int(input("Enter number of rounds you want to play: "))

    for i in range(rounds):
        print(f"\nRound {i+1}")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        comp_choice = random.choice(game)

        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1

    # Final Result
    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {comp_score}")

    if user_score > comp_score:
        print("Congratulations! You won the game!")
    elif comp_score > user_score:
        print("Computer wins the game! Better luck next time.")
    else:
        print("The game is a tie!")

# Function call
play_game()
