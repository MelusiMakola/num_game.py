# Random number guessing game
# M N Makola 2023
# Python

#Import randrange to generate a random number
from random import randrange 


# Variables
secret_num = randrange(20) + 1
chances = 5
guess = 0



# Try Catch to catch the ValueError (Incase user enters a string) 
try:
    while chances > 0:
        print (f"Chances Left {chances}")
        guess = int(input("Enter Your Guess:\n"))
        if guess == secret_num:
            print(f"The guess {guess} is correct!YOU WIN")
            break
        elif guess > secret_num:
            print(f"The guess {guess} is too high. Try Again")
        else:
            print(f"The guess {guess} is too low. Try Again")
        chances -= 1


# Here we reset the game if the user wants to play again
        if chances == 0:
            print(f"Chance: {chances}. You lose")
            reset = input(f"Would you like to platy again? [y/n]:\n>>")
            if reset == "y":
                secret_num = randrange(20) + 1
                chances = 5
            elif reset == "n":
                break
            else:
                print("Value added not in options. Ending Game...")
    print("Game Over")
except ValueError as error:
    print(error)