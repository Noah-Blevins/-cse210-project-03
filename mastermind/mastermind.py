import random


def _create_hint(code, guess):
    """Generates a hint based on the given code and guess.
    Args:
        code (string): The code to compare with.
        guess (string): The guess that was made.
    Returns:
        string: A hint in the form [xxxx]
    """
    code = str(code)
    guess = str(guess)
    hint = ""
    for index, letter in enumerate(guess):
        if code[index] == letter:
            hint += "x"
        elif letter in code:
            hint += "o"
        else:
            hint += "*"
    return hint


def get_mastermind():
    num1 = random.randrange(1000, 10000)

    # names of the player
    playerOne = str(input("Enter a name for player 1: "))
    playerTwo = str(input("Enter a name for player 2: "))

    # print out the player names
    print("-------------------------------\n")
    print(f"Player {playerOne} : ----, ****")
    print(f"Player {playerTwo} : ----, ****")
    print("-------------------------------\n")

    # player one guesses
    print(f"{playerOne}'s turn:")
    player_a = int(input("What is your guess? "))

    print("-------------------------------\n")
    # player two guesses
    print(f"{playerTwo}'s turn:")
    player_b = int(input("What is your guess? "))

    print("-------------------------------\n")
    while True:
        # player one guesses
        print(f"{playerOne}'s turn:")
        player_a = int(input("What is your guess? "))
        print(_create_hint(num1, player_a))

        print("-------------------------------\n")
        # player two guesses
        print(f"{playerTwo}'s turn:")
        player_b = int(input("What is your guess? "))

        print(_create_hint(num1, player_b))

        print("-------------------------------\n")

        # guess condition terminates if true.
        if (player_a == num1):
            print(f"{playerOne} Won!")
            break
        elif (player_b == num1):
            print(f"{playerTwo} Won!")
            break

