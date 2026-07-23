# Project 2: Guess the Number
# program picks a random number 1-100, player guesses with higher/lower hints

import random


def get_guess(low, high):
    # validation - number must be in range
    while True:
        try:
            guess = int(input(f"Enter your guess ({low}-{high}): "))
            if low <= guess <= high:
                return guess
            print(f"Your guess must be between {low} and {high}!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def play_game():
    # one round of the game
    low = 1
    high = 100

    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nI picked a number between {low} and {high}. Try to guess it!")

    while True:
        guess = get_guess(low, high)
        attempts += 1

        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return attempts


def main():
    # keeps playing rounds until the player quits
    print("=== Guess the Number ===")

    while True:
        play_game()

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            break


if __name__ == "__main__":
    main()
