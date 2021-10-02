
import random


def get_mastermind():

    # function generates number
    # random within the range.
    num = random.randrange(1000, 10000)
    print("???????????????????????????????????")
    print("Please you need to input integer values")
    print("Guess the 4 digit number")
    print("???????????????????????????????????")

    # names of the player
    playerOne = str(input("Enter a name for player 1: "))
    playerTwo = str(input("Enter a name for player 2: "))

    # print out the player names
    print("-------------------------------\n")
    print(f"Player {playerOne} : ----, ****")
    print(f"Player {playerTwo} : ----, ****")
    print("-------------------------------\n")

    # player one
    print(f"{playerOne}'s turn:")
    player_a = int(input("What is your guess? "))

    print("-------------------------------\n")
    # player two
    print(f"{playerTwo}'s turn:")
    player_b = int(input("What is your guess? "))

    print("-------------------------------\n")
