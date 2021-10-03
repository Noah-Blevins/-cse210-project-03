import random

class player():
    def __init__(self):
        self.name = ""
    def get_name(self):
        self.name = input("Please enter your name.")

class Code():
    def __init__(self):
        self.name = ""
        self.code = ""
        self.guess = ""
        self.hint = ""
        self._items = []

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        self.name = player.get_name()
        self.code = str(random.randint(1000, 10000))
        self.guess = "----"
        self.hint = "****"
        self._items[self.name] = [self.code, self.guess, self.hint]

    def _create_guess(self,  guess):
        """Receives a guess from the player.

        Args:
            self (Board): An instance of Board.
            guess (string): The guess that is being made.

        Returns:
            None, variable is stored locally.
        """ 

        self.guess = guess

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def value(self):
      """Returns the value of the code."""
      
      return self.code
