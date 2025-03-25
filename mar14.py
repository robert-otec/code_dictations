import random

secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempts -= 1

if attempts == 0:
    print(f"Sorry, the secret number was {secret_number}.")