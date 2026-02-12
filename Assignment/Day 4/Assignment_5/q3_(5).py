import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"Guess the secret number between 1 and 100. You have {max_attempts} attempts!!.")
    
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess > secret_number:
            print("Too high! Try a smaller number.")
        elif guess < secret_number:
            print("Too low! Try a larger number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")

number_guessing_game()
