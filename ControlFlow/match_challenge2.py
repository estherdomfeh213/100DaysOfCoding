# A program game using Match Case statements! In this game, the user tries to guess a secret number chosen by the program

import random

# Generate a secret number between 1 and 10
secret_number = random.randint(1, 10)

while True:
    # Get user's guess and convert it to an integer
    guess = int(input("Guess the secret number (between 1 and 10): "))

    # Match the guess with the secret number
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
            break
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

# Ask the user if they want to play again
play_again = input("Do you want to play again? (yes/no): ").lower()

if play_again == 'yes':
    secret_number = random.randint(1, 10)  # Generate a new secret number
    # You can repeat the code above to continue the game if needed
    # Copy the code to restart the game as needed
else:
    print("Thanks for playing!")

