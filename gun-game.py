###Russian Roulette
from random import randint
import os

def game():
    number = input("Enter a number between 1 and 6. ")
    number = int(number)
    if number < 1 or number > 6:
        print("Invalid number!")
        game()
    correctNumber = randint()
    if correctNumber == number:
        print("Congratulations! You win!")
    
    else:
        print("Bang")
    
game()
