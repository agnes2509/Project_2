""""""""""
# projekt_2.py: druhy projekt do Engeto Online Python Akademie
# author: Agnieszka Sobień-Lewandowska
# email: agnieszka.sobien@gmail.com
# discord: Agnieszka_SL
"""""""""
#Import random 
import random

# Initializing program 
print("Welcome! I've generated a random 4 digit number for you. Let's play a bulls and cows game.")

#Generate random number
def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    
    if digits[0] == 0:
    #first number should not be 0
        for i in range (1,10):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break

#Turn 4 digits into a string
    number = ''.join(str(d) 
    for d in digits[:4])
    return number

#Ensuring validity of the input
def is_valid_guess(guess):

#Check if the user's guess is a valid 4-digit number with unique digits, not starting with 0
    if not guess.isdigit():
        print("Invalid input: Please enter numbers only.")
        return False
    if len(guess) != 4:
        print("Invalid input: The number must be exactly 4 digits.")
        return False
    if guess[0] == '0':
        print("Invalid input: The number cannot start with 0.")
        return False
    if len(set(guess)) != 4:
        print("Invalid input: Digits must be unique.")
        return False
    return True

#Compare user's guess with generated number
def evaluate_guess(secret, guess):
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    cows = sum(1 for i in range(4) if guess[i] in secret and guess[i] != secret[i])
    return bulls, cows

#Main game part
def main():
    secret_number = generate_number()
    
    while True:
        #User's guess
        user_guess = input("Enter a 4-digit number: ")
        
        if not is_valid_guess(user_guess):
            continue
        
        bulls, cows = evaluate_guess(secret_number, user_guess)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        
        if bulls == 4:
            print("Congratulations! You've guessed the number correctly.")
            break

main()

