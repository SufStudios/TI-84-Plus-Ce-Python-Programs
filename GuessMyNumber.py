import random
from ti_system import *


def get_key(parameter1 = ""):

    user_input = input()

    return user_input == parameter1        




def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    exitgame = False
    print("Welcome to Guess My Number")
    print("Press x or Enter to quit")
    print("------------------------")
    print("--- Guess My Number ---")
    print("I'm thinking of 1-100")
    
    while True:
        # Use input() for numbers
        try:
            #guess = int(input("Your guess: "))
            attempts += 1
            
            guess = input("Your guess: ")
            
            if guess == "" or guess == "x":
                exitgame = True
                break
            else:
                guess = int(guess)

                if guess < secret_number:
                    print("Too low! Higher...")
                elif guess > secret_number:
                    print("Too high! Lower...")            
                else:
                    print("CORRECT! You win!")
                    print("Attempts: " + str(attempts))
                    break
        except:
            print("Enter a number!")
    
    if not exitgame:
        print("\nPress [Enter] to quit.")
    # Wait for a key press to exit
    while not (exitgame or get_key()):
        pass
        

    print("Exiting based on KeyPress\nHave a nice day!")

# -----------------------------------
disp_clr()
play_game()
