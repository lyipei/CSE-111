#This is one of the simple python projects yet an exciting one. 
#You can even call it a mini-game. This project is particularly useful for beginners. 
#Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. 
#Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced. 
#The clue can be multiples, divisible, greater or smaller, or a combination of all.

import random


def generate_random_unmber(start, end):
    return random.randint(start, end)

def main():
    print("Welcome! Which game would you like to play?")
    print("1.Number Guessing Game")
    print("2.1A2B game")

    while True:
        choice= input("Enter your choice (1 or 2):")

        if choice == '1':
            print("Choose difficulty level:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            difficulty_choice = input("Enter your difficulty choice (1, 2, or 3): ")

            if difficulty_choice == "1":
                play_guess_game(1, 50, 'easy')
                break
            elif difficulty_choice == "2":
                play_guess_game(1, 100, 'medium')
                break
            elif difficulty_choice == "3":
                play_guess_game(1, 1000, 'hard')
                break
            else:
                print("Invalid difficulty choice.")
        elif choice == '2':
            play_1a2b_game()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, int(number**0.5) + 1 ):
        if number % divisor == 0:
            return False
    return True

def get_hint(secret_number, guessed_number, used_hints):

    hints = []

    if secret_number % 2 == 0:
        hints.append("Your guess is divisible by 2.")
    if secret_number % 3 == 0:
        hints.append("Your guess is divisible by 3.")
    if secret_number % 4 == 0:
        hints.append("Your guess is divisible by 4.")
    if secret_number % 5 == 0:
        hints.append("Your guess is divisible by 5.")
    if secret_number % 6 == 0:
        hints.append("Your guess is divisible by 6.")
    if secret_number % 7 == 0:
        hints.append("Your guess is divisible by 7.")
    if secret_number % 8 == 0:
        hints.append("Your guess is divisible by 8.")
    if secret_number % 9 == 0:
        hints.append("Your guess is divisible by 9.")
    if secret_number % 10 == 0:
        hints.append("Your guess is divisible by 10.")
    if is_prime(guessed_number):
        hints.append("Your guess is a prime number.")
    if guessed_number > secret_number:
        hints.append("Try a lower number.")
    if guessed_number < secret_number:
        hints.append("Try a higher number.")
    if secret_number - guessed_number == 1:
        hints.append("The difference is 1")
    
    available_hints = [hint for hint in hints if hint not in used_hints]

    if available_hints:
        new_hint = random.choice(available_hints)
        used_hints.append(new_hint)
        return new_hint
    else:
        return "No more unique hints available."



def play_guess_game(start, end):
    secret_number = generate_random_unmber(start, end)
    attempt = 0
    used_hints = []
    score = 100

    print(f"Welcome to the Number Guessing game! Guess a number between {start} to {end}")
    print("A hint will be given to you for each wrong guess.")

    while True:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("Invalid input. Please enter a number again.")
            continue

        guessed_number = int(user_input)
        attempt += 1
        score -= 10
        hint = get_hint(secret_number, guessed_number, used_hints)
        print(hint)

        if guessed_number == secret_number:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            print(f"Your score: {score}/100")
            break

def generate_secret_number():
    return str(random.randint(0000,9999))

def get_clues(guess, secret):
    A = 0 
    B = 0

    for i in range(len(guess)):
        if guess[i] == secret [i]:
            A += 1
        elif guess[i] in secret:
            B += 1
    return A, B

def play_1a2b_game():
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to the 1A2B game! Please enter a 4-digit number.")

    while True: 
        user_guess = input("Enter your guess:")
        
        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Invalid input. Please enter a 4-digit number")
            continue
    
        attempts += 1
        A, B = get_clues(user_guess, secret_number)
        print(f"clues:{A}A {B}B")

        if A == 4:
            print(f"Congratulations! You guessed the nember {secret_number} in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()