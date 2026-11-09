import random


def number_guessing_game():
    print("=======================================")
    print("  Welcome to the Number Guessing Game! ")
    print("=======================================")

    # Generate a random number between 1 and 100 inclusive
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?\n")

    # Core game loop
    while True:
        user_input = input("Enter your guess: ").strip()

        # Input validation: Ensure the user typed a valid integer
        try:
            guess = int(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")
            continue

        # Range check validation
        if guess < 1 or guess > 100:
            print("⚠️ Out of bounds! Your guess must be between 1 and 100.")
            continue

        # Increment the attempt counter only after valid input
        attempts += 1

        # Evaluate the guess
        if guess < secret_number:
            print("📉 Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("📈 Too high! Try a lower number.\n")
        else:
            print(f"\n🎉 Congratulations! You guessed the correct number!")
            print(f" It took you {attempts} attempt(s).")
            break  # Exit the loop and end the game


# Run the game
if __name__ == "__main__":
    number_guessing_game()
