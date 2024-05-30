from art import logo, clear
import random

def guess():
    for i in range(upper,0,-1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))
        if guess<number:
            print("Too low")
        elif guess>number:
            print("Too high")
        else:
            print(f"You got it! The answer was {number}.")
            return
        if i==1:
            print(f"You loose! The answer was {number}.")
            return
        print("Guess again.")

again='y'

while again=='y':
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number=random.randint(1,101)
    
    diff=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    
    if diff=="easy":
        upper=10
    else:
        upper=5

    guess()
    again=input("You want to play again,[y/n]:")
    clear()

print("Thanks for playing.")